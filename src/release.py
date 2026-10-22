"""Check a prepared release branch; explicitly --push only that branch to origin."""

from __future__ import annotations

import argparse
from dataclasses import dataclass
import json
from pathlib import Path
import re
import shlex
import subprocess
import sys

if __package__:
    from .check_changes import check_changes
    from .generate import read_version
else:
    from check_changes import check_changes
    from generate import read_version


REPOSITORY = "shpoont/expert-roles"
ORIGIN_URLS = {f"git@github.com:{REPOSITORY}.git", f"https://github.com/{REPOSITORY}.git",
               f"https://github.com/{REPOSITORY}"}
STABLE_VERSION = r"(?:0|[1-9][0-9]*)\.(?:0|[1-9][0-9]*)\.(?:0|[1-9][0-9]*)"


def run(root: Path, *arguments: str) -> str:
    result = subprocess.run(arguments, cwd=root, capture_output=True, text=True)
    if result.returncode:
        raise ValueError(result.stderr.strip() or result.stdout.strip() or f"{arguments[0]} failed.")
    return result.stdout.strip()


def git(root: Path, *arguments: str) -> str:
    return run(root, "git", *arguments)


def github(root: Path, endpoint: str, *options: str):
    return json.loads(run(root, "gh", "api", "--hostname", "github.com", *options,
                          f"repos/{REPOSITORY}/{endpoint}"))


def contains(actual, expected) -> bool:
    """Allow server-added object defaults, but preserve declared values and lists."""
    if isinstance(expected, dict):
        return isinstance(actual, dict) and all(
            key in actual and contains(actual[key], value) for key, value in expected.items())
    return actual == expected


def check_protection(root: Path) -> None:
    expected = json.loads((root / ".github/rulesets/main.json").read_text(encoding="utf-8"))
    pages = github(root, "rulesets", "--paginate", "--slurp")
    matches = [item for page in pages for item in page if item["name"] == expected["name"]]
    if len(matches) != 1:
        raise ValueError("Expected exactly one Protect main ruleset; review the hosted rules before pushing.")
    actual = github(root, f"rulesets/{matches[0]['id']}")
    for key in ("name", "target", "enforcement", "bypass_actors", "conditions"):
        if key not in actual or not contains(actual[key], expected[key]):
            raise ValueError(f"Protect main ruleset drift: {key}; review the hosted rules before pushing.")
    actual_rules = {item["type"]: item for item in actual["rules"]}
    expected_rules = {item["type"]: item for item in expected["rules"]}
    if actual_rules.keys() != expected_rules.keys() or any(
            not contains(actual_rules[key], value) for key, value in expected_rules.items()):
        raise ValueError("Protect main ruleset drift: rules; review the hosted rules before pushing.")
    effective = {item["type"]: item for item in github(root, "rules/branches/main")}
    if any(key not in effective or not contains(effective[key], value)
           for key, value in expected_rules.items()):
        raise ValueError("Protect main ruleset is not effective on main; stop before pushing.")


def remote_refs(root: Path, version: str) -> dict[str, str]:
    result = git(root, "ls-remote", "--refs", "origin", "refs/heads/main",
                 f"refs/heads/release/v{version}", f"refs/tags/v{version}")
    return {name: sha for sha, name in (line.split() for line in result.splitlines())}


@dataclass(frozen=True)
class ReleasePlan:
    version: str
    branch: str
    head: str
    base: str


def push_command(branch: str) -> list[str]:
    if not re.fullmatch(rf"release/v{STABLE_VERSION}", branch):
        raise ValueError("Only release/vMAJOR.MINOR.PATCH branches can be pushed by this helper.")
    ref = f"refs/heads/{branch}"
    return ["git", "push", "--no-follow-tags", "--set-upstream", "origin", f"{ref}:{ref}"]


def preflight(root: Path) -> ReleasePlan:
    root = root.resolve()
    if Path(git(root, "rev-parse", "--show-toplevel")).resolve() != root:
        raise ValueError("--root must be the repository root.")
    if git(root, "status", "--porcelain=v1", "--untracked-files=all"):
        raise ValueError("Commit the reviewed release first; the checkout must be clean, including untracked files.")
    version = read_version(root)
    if not re.fullmatch(STABLE_VERSION, version):
        raise ValueError("A release push requires a final MAJOR.MINOR.PATCH VERSION.")
    branch = git(root, "symbolic-ref", "--quiet", "--short", "HEAD")
    if branch != f"release/v{version}":
        raise ValueError(f"Use release/v{version}; this helper never pushes main or another branch.")
    fetch_urls = git(root, "remote", "get-url", "--all", "origin").splitlines()
    push_urls = git(root, "remote", "get-url", "--push", "--all", "origin").splitlines()
    if len(fetch_urls) != 1 or len(push_urls) != 1 or any(
            url not in ORIGIN_URLS for url in fetch_urls + push_urls):
        raise ValueError("origin must have one canonical Expert Roles fetch and push URL.")
    head = git(root, "rev-parse", "HEAD")
    refs = remote_refs(root, version)
    if f"refs/tags/v{version}" in refs:
        raise ValueError(f"v{version} already exists on origin; released tags stay fixed.")
    base = refs.get("refs/heads/main")
    if not base:
        raise ValueError("origin/main was not found.")
    try:
        git(root, "merge-base", "--is-ancestor", base, head)
    except ValueError as error:
        raise ValueError("Fetch origin and update the release branch against current main before retrying.") from error
    git(root, "verify-commit", head)
    errors = check_changes(root, base, release=True)
    if errors:
        raise ValueError("Release validation failed:\n" + "\n".join(errors))
    check_protection(root)
    return ReleasePlan(version, branch, head, base)


def push(root: Path, plan: ReleasePlan) -> None:
    if (git(root, "rev-parse", "HEAD") != plan.head or
            git(root, "symbolic-ref", "--quiet", "--short", "HEAD") != plan.branch or
            git(root, "status", "--porcelain=v1", "--untracked-files=all")):
        raise ValueError("The checkout changed during preflight; rerun the helper.")
    before = remote_refs(root, plan.version)
    if before.get("refs/heads/main") != plan.base or f"refs/tags/v{plan.version}" in before:
        raise ValueError("Remote main or the release tag changed during preflight; rerun the helper.")
    run(root, *push_command(plan.branch))
    after = remote_refs(root, plan.version)
    if after.get(f"refs/heads/{plan.branch}") != plan.head:
        raise ValueError("Release branch readback differs from the checked head; do not continue.")
    if after.get("refs/heads/main") != plan.base or f"refs/tags/v{plan.version}" in after:
        raise ValueError("Remote main or the tag changed during the push; inspect before continuing.")


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    modes = parser.add_mutually_exclusive_group()
    modes.add_argument("--check", action="store_true", help="Read-only preflight (the default)")
    modes.add_argument("--push", action="store_true", help="Preflight and push only the matching release branch")
    args = parser.parse_args(argv)
    root = args.root.resolve()
    try:
        plan = preflight(root)
        print(f"Checked release v{plan.version}: {plan.head}; current main: {plan.base}")
        print(shlex.join(push_command(plan.branch)))
        if args.push:
            push(root, plan)
            print("Release branch pushed and read back. PR checks, merge, main checks and publication remain separate.")
        else:
            print("Preflight passed; nothing was pushed. Use --push only when the release branch push is authorized.")
        return 0
    except (ValueError, OSError) as error:
        print(f"Release preflight failed: {error}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
