"""Check contribution ownership or a prepared release against a Git baseline."""

from __future__ import annotations

import argparse
from datetime import date
from pathlib import Path
import re
import subprocess
import sys

if __package__:
    from .generate import main as generate, read_version, update_readme
else:
    from generate import main as generate, read_version, update_readme


GENERATED_SECTIONS = {"README.md": ("SUMMARY", "FEATURED"),
                      "src/roles/README.md": ("CATALOGUE",)}


def git(root: Path, *arguments: str) -> bytes:
    result = subprocess.run(["git", "-C", str(root), *arguments], capture_output=True)
    if result.returncode:
        detail = result.stderr.decode("utf-8", errors="replace").strip()
        raise ValueError(detail or "Git comparison failed: --base must identify an ancestor of HEAD.")
    return result.stdout


def baseline_file(root: Path, base: str, path: str) -> str:
    return git(root, "show", f"{base}:{path}").decode("utf-8")


def generated_blocks(text: str, path: str) -> list[str]:
    result = []
    for section in GENERATED_SECTIONS[path]:
        update_readme(text, "", section, path)  # Apply the generator's boundary validation.
        start, end = f"<!-- BEGIN GENERATED {section} -->", f"<!-- END GENERATED {section} -->"
        result.append(text[text.index(start):text.index(end) + len(end)])
    return result


def release_history(changelog: str) -> str:
    match = re.search(r"^## v[0-9]+\.", changelog, re.M)
    return changelog[match.start():] if match else ""


def check_changes(root: Path, base_ref: str, *, release: bool = False) -> list[str]:
    """Inspect committed, staged and unstaged changes, including untracked files."""
    base = git(root, "rev-parse", "--verify", "--end-of-options", f"{base_ref}^{{commit}}").decode().strip()
    git(root, "merge-base", "--is-ancestor", base, "HEAD")
    changed = set(git(root, "diff", "--name-only", "--no-renames", "-z", base, "--").decode().split("\0"))
    changed.update(git(root, "ls-files", "--others", "--exclude-standard", "-z").decode().split("\0"))
    changed.discard("")
    errors = []
    if release:
        version = read_version(root)
        previous = baseline_file(root, base, "VERSION").strip()
        if "VERSION" not in changed or version == previous:
            errors.append("A release change must choose a new VERSION; ordinary contributions leave it unchanged.")
        if not re.fullmatch(r"(?:0|[1-9][0-9]*)\.(?:0|[1-9][0-9]*)\.(?:0|[1-9][0-9]*)", version):
            errors.append("A stable release requires a final MAJOR.MINOR.PATCH VERSION without development suffixes.")
        elif tuple(map(int, version.split("."))) <= tuple(map(int, previous.split("-", 1)[0].split("+", 1)[0].split("."))):
            errors.append("The release VERSION must be greater than the baseline version.")
        changelog = (root / "CHANGELOG.md").read_text(encoding="utf-8")
        headings = re.findall(rf"^## v{re.escape(version)} — (\d{{4}}-\d{{2}}-\d{{2}})$", changelog, re.M)
        if len(headings) != 1:
            errors.append(f"Finalize exactly one dated CHANGELOG.md heading: ## v{version} — YYYY-MM-DD")
        else:
            date.fromisoformat(headings[0])
        if changelog.splitlines().count("## Unreleased") != 1:
            errors.append("Keep one ## Unreleased heading for future contributions.")
        if errors:
            return errors
        if generate(["--root", str(root), "--check"]):
            errors.append("Release artifacts must be fully regenerated with src/generate.py --release.")
        return errors

    for path in sorted(changed):
        if path == "VERSION" or path == "dist" or path.startswith("dist/"):
            errors.append(f"Release-owned file changed: {path}")
        elif path in GENERATED_SECTIONS:
            before = baseline_file(root, base, path)
            after = (root / path).read_bytes().decode("utf-8")
            if generated_blocks(before, path) != generated_blocks(after, path):
                errors.append(f"Release-owned generated section changed: {path}")
        elif path == "CHANGELOG.md":
            before = baseline_file(root, base, path)
            after = (root / path).read_bytes().decode("utf-8")
            if after.splitlines().count("## Unreleased") != 1 or release_history(before) != release_history(after):
                errors.append("Contributions add CHANGELOG.md notes under ## Unreleased; dated release history stays fixed.")
    return errors


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument("--base", required=True, help="Ancestor commit/ref to compare with the working tree")
    parser.add_argument("--release", action="store_true", help="Check a maintainer-prepared stable release instead of a contribution")
    args = parser.parse_args(argv)
    try:
        errors = check_changes(args.root, args.base, release=args.release)
        if errors:
            print("Change checks failed:\n" + "\n".join(errors), file=sys.stderr)
            return 1
        print("Prepared release is consistent." if args.release else
              "Contribution boundary passed; VERSION, dist and generated catalogue sections are unchanged.")
        return 0
    except (ValueError, OSError, UnicodeError) as error:
        print(f"Change checks failed: {error}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
