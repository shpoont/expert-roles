"""Exercise source contributions and release gates in disposable Git repositories."""

from contextlib import redirect_stderr, redirect_stdout
from io import StringIO
from pathlib import Path
import shutil
import subprocess
import tempfile
import tomllib
import unittest

from PIL import Image
import yaml

from src.check_changes import check_changes, main as check_main
from src.generate import FEATURED_EXPERTS, main as generate


class ContributionReleaseTests(unittest.TestCase):
    def setUp(self):
        directory = tempfile.TemporaryDirectory()
        self.addCleanup(directory.cleanup)
        self.outer = Path(directory.name)
        self.root = self.outer / "repo"
        self.root.mkdir()
        self.source = Path(__file__).resolve().parents[1]
        (self.root / "VERSION").write_text("1.1.0\n")
        (self.root / "CHANGELOG.md").write_text("# Changelog\n\n## Unreleased\n\n## v1.1.0 — 2026-10-22\n\nPrevious release.\n")
        (self.root / "README.md").write_text(
            "# Collection\n\nAuthored introduction.\n\n"
            "<!-- BEGIN GENERATED SUMMARY -->\n<!-- END GENERATED SUMMARY -->\n\n"
            "<!-- BEGIN GENERATED FEATURED -->\n<!-- END GENERATED FEATURED -->\n"
        )
        (self.root / "src/roles").mkdir(parents=True)
        (self.root / "src/roles/README.md").write_text(
            "# Catalogue\n\n<!-- BEGIN GENERATED CATALOGUE -->\n<!-- END GENERATED CATALOGUE -->\n"
        )
        shutil.copytree(self.source / "src/templates", self.root / "src/templates")
        shutil.copyfile(self.source / "src/specialties.yaml", self.root / "src/specialties.yaml")
        for slug, _, _ in FEATURED_EXPERTS:
            self.add_expert(slug, yaml.safe_load((self.source / "src/roles" / slug / "expert.yaml").read_text()))
        self.add_expert("other-expert")
        self.assertEqual(self.run_generator("--release"), 0)
        self.git("init", "-q")
        (self.root / ".gitignore").write_text(".venv/\n__pycache__/\n")
        self.git("add", ".")
        # Unsigned synthetic fixture only; never commit in the user's checkout.
        self.git("-c", "user.name=Fixture", "-c", "user.email=fixture@example.invalid",
                 "-c", "commit.gpgsign=false", "commit", "-qm",
                 "Create test baseline\n\nIsolate contribution and release checks from the real repository.")

    def git(self, *args):
        return subprocess.check_output(["git", "-C", str(self.root), *args], stderr=subprocess.PIPE)

    def add_expert(self, slug, metadata=None):
        profile = self.root / "src/roles" / slug
        profile.mkdir()
        metadata = metadata or {"name": slug.replace("-", " ").title(), "specialties": ["human-centered-design"]}
        (profile / "expert.yaml").write_text(yaml.safe_dump(metadata))
        (profile / "README.md").write_text(
            f"# {metadata['name']}\n\n## Photo credit\n\n"
            "**Source:** [Synthetic fixture](https://example.org/fixtures/portrait).\n\n"
            "**License:** [CC0](https://creativecommons.org/publicdomain/zero/1.0/).\n"
        )
        Image.new("RGB", (512, 512)).save(profile / "portrait.jpg")

    def run_generator(self, *args):
        with redirect_stdout(StringIO()), redirect_stderr(StringIO()):
            return generate(["--root", str(self.root), *args])

    def snapshot(self):
        return {p.relative_to(self.root): p.read_bytes() for p in self.root.rglob("*")
                if p.is_file() and ".git" not in p.relative_to(self.root).parts}

    def test_source_addition_correction_and_removal_pass_with_retained_artifacts(self):
        self.add_expert("new-expert")
        metadata = self.root / "src/roles/don-norman/expert.yaml"
        entry = yaml.safe_load(metadata.read_text())
        entry["perspective"] = "a corrected emphasis"
        metadata.write_text(yaml.safe_dump(entry))
        shutil.rmtree(self.root / "src/roles/other-expert")
        before = self.snapshot()
        self.assertEqual(self.run_generator(), 0)
        self.assertEqual(self.run_generator("--validate"), 0)
        with redirect_stderr(StringIO()), redirect_stdout(StringIO()):
            self.assertTrue(check_changes(self.root, "HEAD"))
        self.assertEqual(self.run_generator("--check"), 1)
        self.assertEqual(before, self.snapshot())
        self.assertEqual(self.run_generator("--docs"), 0)
        after_docs = self.snapshot()
        catalogues = {Path("README.md"), Path("src/roles/README.md")}
        self.assertEqual({p: text for p, text in before.items() if p not in catalogues},
                         {p: text for p, text in after_docs.items() if p not in catalogues})
        self.assertEqual(check_changes(self.root, "HEAD"), [])
        self.assertEqual(after_docs, self.snapshot())
        self.assertTrue((self.root / "dist/codex/expert-other-expert.toml").exists())
        self.assertFalse((self.root / "dist/codex/expert-new-expert.toml").exists())

    def test_docs_refresh_is_isolated_idempotent_and_freshness_checks_are_read_only(self):
        self.add_expert("new-expert")
        before = self.snapshot()
        self.assertEqual(self.run_generator("--check-docs"), 1)
        self.assertEqual(before, self.snapshot())
        self.assertEqual(self.run_generator("--docs"), 0)
        after = self.snapshot()
        self.assertEqual({path for path in before if before[path] != after[path]},
                         {Path("README.md"), Path("src/roles/README.md")})
        self.assertIn("Authored introduction.", (self.root / "README.md").read_text())
        self.assertIn("New Expert", (self.root / "src/roles/README.md").read_text())
        self.assertNotIn("Unreleased review preview", (self.root / "README.md").read_text())
        self.assertEqual(self.run_generator("--check-docs"), 0)
        self.assertEqual(self.run_generator("--docs"), 0)
        self.assertEqual(after, self.snapshot())
        self.assertEqual(check_changes(self.root, "HEAD"), [])
        self.assertEqual(self.run_generator("--check"), 1)  # Exports still belong to the earlier release.

    def test_docs_commands_cannot_be_combined_with_writing_or_preview_modes(self):
        for arguments in (("--docs", "--release"), ("--docs", "--check-docs"),
                          ("--check-docs", "--preview", str(self.outer / "preview"))):
            with self.subTest(arguments=arguments):
                before = self.snapshot()
                self.assertEqual(self.run_generator(*arguments), 1)
                self.assertEqual(before, self.snapshot())
                self.assertFalse((self.outer / "preview").exists())

    def test_preview_is_complete_unreleased_and_leaves_checkout_unchanged(self):
        self.add_expert("new-expert")
        (self.root / ".venv").mkdir()
        (self.root / ".venv/do-not-copy").write_text("fixture")
        before = self.snapshot()
        preview = self.outer / "preview"
        self.assertEqual(self.run_generator("--preview", str(preview)), 0)
        self.assertEqual(before, self.snapshot())
        self.assertEqual((preview / "VERSION").read_text(), "0.0.0-preview\n")
        self.assertIn("Unreleased review preview", (preview / "README.md").read_text())
        self.assertIn("New Expert", (preview / "src/roles/README.md").read_text())
        self.assertTrue((preview / "src/roles/new-expert/portrait.jpg").exists())
        self.assertTrue((preview / "dist/claude/expert-new-expert.md").exists())
        current = (self.root / "dist/codex/expert-don-norman.toml").read_text()
        rendered = (preview / "dist/codex/expert-don-norman.toml").read_text()
        self.assertIn("# expert_roles.version: 0.0.0-preview", rendered)
        self.assertEqual(tomllib.loads(current), tomllib.loads(rendered))
        self.assertFalse((preview / ".git").exists())
        self.assertFalse((preview / ".venv").exists())

    def test_preview_rejects_existing_or_internal_destination_without_writes(self):
        for destination in (self.root / "build/preview", self.root, self.outer):
            with self.subTest(destination=destination):
                before = self.snapshot()
                self.assertEqual(self.run_generator("--preview", str(destination)), 1)
                self.assertEqual(before, self.snapshot())

    def test_invalid_sources_prevent_validation_and_preview_creation(self):
        self.add_expert("invalid-expert", {"name": "Invalid Expert", "specialties": ["unknown"]})
        before = self.snapshot()
        preview = self.outer / "invalid-preview"
        for mode in ("--validate", "--docs", "--check-docs"):
            with self.subTest(mode=mode):
                self.assertEqual(self.run_generator(mode), 1)
                self.assertEqual(before, self.snapshot())
        self.assertEqual(self.run_generator("--preview", str(preview)), 1)
        self.assertFalse(preview.exists())
        self.assertEqual(before, self.snapshot())

    def test_contributions_reject_release_edits_and_stale_catalogues(self):
        edits = {
            "VERSION": "1.2.0-dev\n",
            "dist/codex/expert-don-norman.toml": "# changed\n",
            "dist/claude/new-untracked-file.md": "# untracked\n",
            "README.md": (self.root / "README.md").read_text().replace("7 experts", "8 experts"),
            "src/roles/README.md": (self.root / "src/roles/README.md").read_text().replace("Other Expert", "Changed Expert"),
            "CHANGELOG.md": "# Changelog\n\n## Unreleased\n\n## v1.2.0 — 2026-10-23\n",
        }
        for name, content in edits.items():
            with self.subTest(name=name):
                path = self.root / name
                previous = path.read_bytes() if path.exists() else None
                path.write_text(content)
                before = self.snapshot()
                with redirect_stdout(StringIO()), redirect_stderr(StringIO()):
                    errors = check_changes(self.root, "HEAD")
                self.assertTrue(errors)
                if name in {"README.md", "src/roles/README.md"}:
                    self.assertIn("Source catalogues must match", " ".join(errors))
                self.assertEqual(before, self.snapshot())
                if previous is None:
                    path.unlink()
                else:
                    path.write_bytes(previous)

        # Text-mode newline normalization must not hide generated-block edits.
        path = self.root / "README.md"
        previous = path.read_bytes()
        path.write_bytes(previous.replace(b"\n", b"\r\n"))
        self.assertTrue(check_changes(self.root, "HEAD"))
        path.write_bytes(previous)

    def test_authored_readme_edits_and_unreleased_notes_remain_possible(self):
        for name in ("README.md", "src/roles/README.md"):
            path = self.root / name
            path.write_text("Author's new introduction.\n\n" + path.read_text())
        path = self.root / "CHANGELOG.md"
        path.write_text(path.read_text().replace("## Unreleased", "## Unreleased\n\n- A source correction."))
        self.assertEqual(check_changes(self.root, "HEAD"), [])

    def test_release_requires_new_final_version_dated_changelog_and_fresh_outputs(self):
        self.assertTrue(check_changes(self.root, "HEAD", release=True))
        (self.root / "VERSION").write_text("1.2.0-dev\n")
        self.assertTrue(check_changes(self.root, "HEAD", release=True))
        (self.root / "VERSION").write_text("1.2.0\n")
        self.assertTrue(check_changes(self.root, "HEAD", release=True))
        changelog = self.root / "CHANGELOG.md"
        changelog.write_text(changelog.read_text().replace("## Unreleased", "## Unreleased\n\n## v1.2.0 — 2026-10-23\n\nNext release."))
        with redirect_stderr(StringIO()), redirect_stdout(StringIO()):
            self.assertTrue(check_changes(self.root, "HEAD", release=True))
        self.assertEqual(self.run_generator("--release"), 0)
        before = self.snapshot()
        with redirect_stdout(StringIO()):
            self.assertEqual(check_changes(self.root, "HEAD", release=True), [])
        self.assertEqual(before, self.snapshot())
        self.assertTrue(check_changes(self.root, "HEAD"))

    def test_release_rejects_downgrade_and_obsolete_exports(self):
        (self.root / "VERSION").write_text("1.0.0\n")
        self.assertIn("greater than", " ".join(check_changes(self.root, "HEAD", release=True)))
        (self.root / "VERSION").write_text("1.2.0\n")
        changelog = self.root / "CHANGELOG.md"
        changelog.write_text(changelog.read_text().replace("## Unreleased", "## Unreleased\n\n## v1.2.0 — 2026-10-23\n"))
        self.assertEqual(self.run_generator("--release"), 0)
        (self.root / "dist/codex/obsolete.toml").write_text("# obsolete\n")
        with redirect_stdout(StringIO()), redirect_stderr(StringIO()):
            self.assertTrue(check_changes(self.root, "HEAD", release=True))

    def test_missing_base_and_damaged_markers_fail_cleanly(self):
        with redirect_stdout(StringIO()), redirect_stderr(StringIO()):
            self.assertEqual(check_main(["--root", str(self.root), "--base", "missing-ref"]), 1)
            path = self.root / "README.md"
            path.write_text(path.read_text().replace("<!-- END GENERATED SUMMARY -->", ""))
            self.assertEqual(check_main(["--root", str(self.root), "--base", "HEAD"]), 1)


if __name__ == "__main__":
    unittest.main()
