"""Exercise release pushes in disposable bare repos; never push to live GitHub."""

from contextlib import redirect_stderr, redirect_stdout
from copy import deepcopy
from io import StringIO
import json
from pathlib import Path
import subprocess
import tempfile
import unittest
from unittest.mock import patch

import yaml

from src import release


SOURCE = Path(__file__).resolve().parents[1]
POLICY = json.loads((SOURCE / ".github/rulesets/main.json").read_text())


class ReleaseGitTests(unittest.TestCase):
    def setUp(self):
        directory = tempfile.TemporaryDirectory()
        self.addCleanup(directory.cleanup)
        outer = Path(directory.name).resolve()
        self.root, self.origin = outer / "repo", outer / "origin.git"
        self.command("git", "init", "--bare", "--initial-branch=main", str(self.origin))
        self.command("git", "init", "--initial-branch=main", str(self.root))
        self.git("config", "user.name", "Release Fixture")
        self.git("config", "user.email", "fixture@example.invalid")
        self.git("config", "push.default", "upstream")
        self.git("config", "push.followTags", "true")
        (self.root / "VERSION").write_text("1.3.0\n")
        self.commit("Create fixture baseline")
        self.git("remote", "add", "origin", str(self.origin))
        self.git("push", "--no-follow-tags", "--set-upstream", "origin", "refs/heads/main:refs/heads/main")
        self.base = self.git("rev-parse", "HEAD")
        self.git("switch", "--track", "-c", "release/v1.4.0", "origin/main")
        (self.root / "VERSION").write_text("1.4.0\n")
        self.commit("Prepare fixture release")
        self.head = self.git("rev-parse", "HEAD")
        self.git("-c", "tag.gpgsign=false", "tag", "-a", "v1.4.0-test", "-m", "Unpublished fixture tag")

    def command(self, *arguments):
        result = subprocess.run(arguments, capture_output=True, text=True, check=True)
        return result.stdout.strip()

    def git(self, *arguments):
        return self.command("git", "-C", str(self.root), *arguments)

    def commit(self, subject):
        self.git("add", ".")
        # Unsigned synthetic fixture only; the real checkout retains signing.
        self.git("-c", "commit.gpgsign=false", "commit", "-m",
                 subject + "\n\nIsolate release safety checks from the real repository.")

    def refs(self):
        return self.git("ls-remote", "--refs", "origin")

    def preflight(self):
        real_git = release.git

        def git(root, *arguments):
            # Verify that production requests a signature, without requiring
            # the user's signer or creating real signed commits in test fixtures.
            if arguments[:1] == ("verify-commit",):
                self.assertEqual(arguments[1], self.head)
                return ""
            return real_git(root, *arguments)

        with patch.object(release, "ORIGIN_URLS", {str(self.origin)}), \
                patch.object(release, "git", side_effect=git), \
                patch.object(release, "check_changes", return_value=[]) as changes, \
                patch.object(release, "check_protection") as protection:
            plan = release.preflight(self.root)
            changes.assert_called_once_with(self.root, self.base, release=True)
            protection.assert_called_once_with(self.root)
            return plan

    def test_explicit_push_ignores_main_upstream_and_does_not_follow_tags(self):
        self.assertEqual(self.git("rev-parse", "--abbrev-ref", "@{upstream}"), "origin/main")
        # Reproduce the original failure mode safely, against a local bare repo.
        dry_run = subprocess.run(["git", "-C", str(self.root), "push", "--dry-run", "origin",
                                  "release/v1.4.0"], capture_output=True, text=True, check=True)
        self.assertIn("release/v1.4.0 -> main", dry_run.stderr)
        before = self.refs()
        plan = self.preflight()
        self.assertEqual(self.refs(), before)  # Default preflight performs no push.
        release.push(self.root, plan)
        refs = dict(line.split()[::-1] for line in self.refs().splitlines())
        self.assertEqual(refs, {"refs/heads/main": self.base, "refs/heads/release/v1.4.0": self.head})
        self.assertEqual(self.git("rev-parse", "--abbrev-ref", "@{upstream}"), "origin/release/v1.4.0")

    def test_other_branch_and_development_version_fail_before_remote_access(self):
        for branch in ("main", "feature/change", "release/v1.4.0-dev"):
            with self.subTest(branch=branch):
                self.git("switch", "-C", branch)
                with patch.object(release, "remote_refs") as remote:
                    with self.assertRaisesRegex(ValueError, "never pushes main"):
                        release.preflight(self.root)
                    remote.assert_not_called()
        (self.root / "VERSION").write_text("1.4.0-dev\n")
        self.commit("Prepare invalid development fixture")
        with self.assertRaisesRegex(ValueError, "final MAJOR.MINOR.PATCH"):
            release.preflight(self.root)

    def test_dirty_checkout_and_changed_push_url_fail_without_push(self):
        before = self.refs()
        (self.root / "untracked").write_text("not reviewed")
        with self.assertRaisesRegex(ValueError, "must be clean"):
            release.preflight(self.root)
        (self.root / "untracked").unlink()
        self.git("remote", "set-url", "--push", "origin", "https://example.invalid/other.git")
        with self.assertRaisesRegex(ValueError, "canonical Expert Roles"):
            release.preflight(self.root)
        self.assertEqual(self.refs(), before)

    def test_existing_tag_and_stale_base_are_rejected(self):
        self.git("-c", "tag.gpgsign=false", "tag", "v1.4.0")
        self.git("push", "--no-follow-tags", "origin", "refs/tags/v1.4.0:refs/tags/v1.4.0")
        before = self.refs()
        with patch.object(release, "ORIGIN_URLS", {str(self.origin)}):
            with self.assertRaisesRegex(ValueError, "already exists"):
                release.preflight(self.root)
        self.assertEqual(self.refs(), before)
        with patch.object(release, "ORIGIN_URLS", {str(self.origin)}), \
                patch.object(release, "remote_refs", return_value={"refs/heads/main": "f" * 40}):
            with self.assertRaisesRegex(ValueError, "update the release branch"):
                release.preflight(self.root)
        with patch.object(release, "ORIGIN_URLS", {str(self.origin)}), \
                patch.object(release, "remote_refs", return_value={}):
            with self.assertRaisesRegex(ValueError, "origin/main was not found"):
                release.preflight(self.root)

    def test_unsigned_head_and_release_validation_failure_cannot_push(self):
        before = self.refs()
        with patch.object(release, "ORIGIN_URLS", {str(self.origin)}):
            with self.assertRaises(ValueError):
                release.preflight(self.root)  # The fixture is deliberately unsigned.
        real_git = release.git

        def git(root, *args):
            return "" if args[:1] == ("verify-commit",) else real_git(root, *args)

        with patch.object(release, "ORIGIN_URLS", {str(self.origin)}), \
                patch.object(release, "git", side_effect=git), \
                patch.object(release, "check_changes", return_value=["VERSION must increase"]):
            with self.assertRaisesRegex(ValueError, "VERSION must increase"):
                release.preflight(self.root)
        self.assertEqual(self.refs(), before)

    def test_local_or_remote_change_between_preflight_and_push_stops(self):
        plan = self.preflight()
        before = self.refs()
        (self.root / "untracked").write_text("concurrent edit")
        with self.assertRaisesRegex(ValueError, "checkout changed"):
            release.push(self.root, plan)
        (self.root / "untracked").unlink()
        with patch.object(release, "remote_refs", return_value={"refs/heads/main": "f" * 40}):
            with self.assertRaisesRegex(ValueError, "changed during preflight"):
                release.push(self.root, plan)
        self.assertEqual(self.refs(), before)

    def test_helper_never_force_updates_a_diverged_release_branch(self):
        plan = self.preflight()
        self.git("switch", "--detach", self.base)
        (self.root / "remote-only").write_text("someone else's release work")
        self.commit("Create competing fixture release")
        self.git("push", "--no-follow-tags", "origin", "HEAD:refs/heads/release/v1.4.0")
        self.git("switch", plan.branch)
        before = self.refs()
        with self.assertRaises(ValueError):
            release.push(self.root, plan)
        self.assertEqual(self.refs(), before)


class ReleaseProtectionTests(unittest.TestCase):
    def setUp(self):
        self.actual = dict(deepcopy(POLICY), id=123)
        self.effective = deepcopy(POLICY["rules"])

    def github(self, root, endpoint, *options):
        if endpoint == "rulesets":
            self.assertEqual(options, ("--paginate", "--slurp"))
            return [[{"name": "Protect main", "id": 123}]]
        if endpoint == "rulesets/123":
            return self.actual
        if endpoint == "rules/branches/main":
            return self.effective
        self.fail(f"Unexpected API endpoint {endpoint}")

    def test_tracked_policy_requires_prs_actions_validation_and_no_bypass(self):
        self.assertEqual(POLICY["enforcement"], "active")
        self.assertEqual(POLICY["target"], "branch")
        self.assertEqual(POLICY["bypass_actors"], [])
        self.assertEqual(POLICY["conditions"], {"ref_name": {"include": ["refs/heads/main"], "exclude": []}})
        rules = {item["type"]: item for item in POLICY["rules"]}
        self.assertEqual(set(rules), {"deletion", "non_fast_forward", "pull_request", "required_status_checks"})
        self.assertEqual(rules["pull_request"]["parameters"]["required_approving_review_count"], 0)
        self.assertEqual(rules["pull_request"]["parameters"]["allowed_merge_methods"], ["squash"])
        required = rules["required_status_checks"]["parameters"]
        self.assertTrue(required["strict_required_status_checks_policy"])
        self.assertEqual(required["required_status_checks"], [{"context": "validate", "integration_id": 15368}])
        workflow = yaml.safe_load((SOURCE / ".github/workflows/checks.yml").read_text())
        self.assertIn("validate", workflow["jobs"])

    def test_protection_readback_accepts_server_defaults_but_not_drift(self):
        self.actual["rules"][2]["parameters"]["server_default"] = False
        with patch.object(release, "github", side_effect=self.github):
            release.check_protection(SOURCE)
        changes = (("enforcement", "disabled"), ("bypass_actors", [{"actor_type": "RepositoryRole", "actor_id": 5}]),
                   ("conditions", {"ref_name": {"include": ["refs/heads/other"], "exclude": []}}))
        for key, value in changes:
            with self.subTest(key=key):
                self.actual = deepcopy(POLICY)
                self.actual[key] = value
                with patch.object(release, "github", side_effect=self.github):
                    with self.assertRaisesRegex(ValueError, "drift"):
                        release.check_protection(SOURCE)

    def test_missing_wrong_source_or_non_strict_validation_and_inactive_rules_fail(self):
        for edit in ("missing_pr", "wrong_app", "not_strict", "not_effective"):
            with self.subTest(edit=edit):
                self.actual, self.effective = deepcopy(POLICY), deepcopy(POLICY["rules"])
                if edit == "missing_pr":
                    self.actual["rules"] = [r for r in self.actual["rules"] if r["type"] != "pull_request"]
                elif edit == "wrong_app":
                    self.actual["rules"][-1]["parameters"]["required_status_checks"][0]["integration_id"] = 1
                elif edit == "not_strict":
                    self.actual["rules"][-1]["parameters"]["strict_required_status_checks_policy"] = False
                else:
                    self.effective = []
                with patch.object(release, "github", side_effect=self.github):
                    with self.assertRaises(ValueError):
                        release.check_protection(SOURCE)
        for pages in ([], [[{"name": "Other rules", "id": 123}]],
                      [[{"name": "Protect main", "id": 123}, {"name": "Protect main", "id": 456}]]):
            with patch.object(release, "github", return_value=pages):
                with self.assertRaisesRegex(ValueError, "exactly one"):
                    release.check_protection(SOURCE)

    def test_cli_defaults_to_check_and_requires_explicit_push(self):
        plan = release.ReleasePlan("1.4.0", "release/v1.4.0", "a" * 40, "b" * 40)
        for arguments, pushes in (([], False), (["--check"], False), (["--push"], True)):
            with self.subTest(arguments=arguments), patch.object(release, "preflight", return_value=plan), \
                    patch.object(release, "push") as push, redirect_stdout(StringIO()):
                self.assertEqual(release.main(arguments), 0)
                self.assertEqual(push.called, pushes)
        with patch.object(release, "preflight", side_effect=ValueError("Stop")), \
                patch.object(release, "push") as push, redirect_stderr(StringIO()):
            self.assertEqual(release.main(["--push"]), 1)
            push.assert_not_called()
        for branch in ("main", "release/v1.4.0-dev", "--mirror", "release/v01.4.0"):
            with self.assertRaises(ValueError):
                release.push_command(branch)


if __name__ == "__main__":
    unittest.main()
