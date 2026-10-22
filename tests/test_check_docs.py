"""Portable preview-reference checks with valid and deliberately broken fixtures."""

from contextlib import redirect_stderr, redirect_stdout
from io import StringIO
from pathlib import Path
import tempfile
import unittest

from PIL import Image

from src.check_docs import check_docs, main


class DocumentationReferenceTests(unittest.TestCase):
    def setUp(self):
        self.directory = tempfile.TemporaryDirectory()
        self.addCleanup(self.directory.cleanup)
        self.root = Path(self.directory.name)

    def write(self, name, text):
        path = self.root / name
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(text, encoding="utf-8")
        return path

    def photo(self, name="images/portrait.png"):
        path = self.root / name
        path.parent.mkdir(parents=True, exist_ok=True)
        Image.new("RGB", (8, 8), "blue").save(path)
        return path

    def test_markdown_html_and_reference_links_resolve_rendered_headings_and_images(self):
        self.photo("images/a portrait.png")
        self.write("images/icon.svg", '<svg xmlns="http://www.w3.org/2000/svg"><g id="face"/></svg>')
        self.write("guides/café guide.md", """# *Café* `code` & [choice](../README.md)

Setext title
------------

## 重复标题
## Repeat
## Repeat
## Repeat-1
## v1.2.0 — Notes

<a name="custom"></a><span id="exactCase">Target</span>
""")
        self.write("guides/README.md", "# Directory guide\n")
        self.write("page.html", '<h1 id="html-anchor">HTML</h1><a href="README.md">Home</a>')
        self.write("README.md", """# Home

[Formatted](guides/caf%C3%A9%20guide.md#café-code--choice)
[Setext](guides/café%20guide.md#setext-title)
[Unicode](guides/café%20guide.md#%E9%87%8D%E5%A4%8D%E6%A0%87%E9%A2%98)
[Second](guides/café%20guide.md#repeat-1)
[Collision](guides/café%20guide.md#repeat-1-1)
[Punctuation](guides/café%20guide.md#v120--notes)
[Custom][named]
[HTML case](guides/café%20guide.md#exactCase)
[Directory](guides/#directory-guide)
[Root](/README.md?raw=1#home)
[Top](#)
[HTML](page.html#html-anchor)
![Portrait][portrait]
![SVG](images/icon.svg#face)
<a href="page.html?view=1&amp;raw=1#html-anchor"><img src="images/a%20portrait.png"></a>
<a href="https://example.org/unchecked#remote">External</a>
![Remote](//example.org/remote.png)

[named]: guides/café%20guide.md#custom
[portrait]: images/a%20portrait.png "A title"
""")
        report = check_docs(self.root)
        self.assertEqual(report.errors, [])
        self.assertEqual(report.documents, 4)
        self.assertEqual(report.images, 3)
        self.assertEqual(report.external_references, 2)
        self.assertGreaterEqual(report.local_references, 18)

    def test_missing_targets_and_anchors_report_origin_lines(self):
        self.write("guide.md", "# Renamed heading\n")
        self.write("README.md", "# Home\n\n[Missing](gone.md)\n\n"
                   "![Missing image](gone.png)\n\n[Old](guide.md#old-heading)\n")
        report = check_docs(self.root)
        self.assertEqual(len(report.errors), 3)
        self.assertIn("README.md:3: missing target 'gone.md'", report.errors)
        self.assertIn("README.md:5: missing target 'gone.png'", report.errors)
        self.assertIn("README.md:7: missing anchor 'old-heading' in 'guide.md#old-heading'", report.errors)

    def test_code_and_comments_do_not_create_references_or_heading_anchors(self):
        self.write("README.md", """# Real

`[Inline](missing.md)` and `<img src="missing.png">`.

```markdown
# Fake fenced
[Fenced](missing.md)
```

    # Fake indented
    ![Indented](missing.png)

<!-- <a id="fake-comment" href="missing.md"><img src="missing.png"></a> -->
<a id="real-html"></a>
[Valid](#real-html)
""")
        self.assertEqual(check_docs(self.root).errors, [])
        self.write("references.md", "[Code](README.md#fake-fenced)\n\n"
                   "[Indent](README.md#fake-indented)\n\n[Comment](README.md#fake-comment)\n")
        errors = check_docs(self.root).errors
        self.assertEqual(len(errors), 3)
        self.assertTrue(all("missing anchor" in error for error in errors))

    def test_yaml_frontmatter_comments_are_not_headings_or_links(self):
        self.write("role.md", "---\n# Expert Roles\nname: test\n"
                   "description: '[not a link](missing.md)'\n---\n\n# Actual heading\n")
        self.write("README.md", "[Actual](role.md#actual-heading)\n")
        self.assertEqual(check_docs(self.root).errors, [])
        self.write("README.md", "[Metadata is not a heading](role.md#expert-roles)\n")
        self.assertIn("missing anchor", check_docs(self.root).errors[0])

    def test_corrupt_raster_svg_and_non_image_targets_fail(self):
        self.write("broken.png", "not a PNG")
        self.write("broken.svg", '<svg xmlns="http://www.w3.org/2000/svg"><g>')
        self.write("not-svg.svg", "<html></html>")
        jpeg = self.photo("truncated.jpg")
        jpeg.write_bytes(jpeg.read_bytes()[:-2])
        self.write("README.md", "![Raster](broken.png)\n\n![XML](broken.svg)\n\n"
                   "![Wrong root](not-svg.svg)\n\n<img src=\"README.md\">\n\n![Truncated](truncated.jpg)\n")
        report = check_docs(self.root)
        self.assertEqual(len(report.errors), 5)
        self.assertTrue(all("unreadable image" in error for error in report.errors))

    def test_svg_fragments_and_duplicate_explicit_anchors_are_checked(self):
        self.write("icon.svg", '<svg xmlns="http://www.w3.org/2000/svg"><path id="good"/></svg>')
        self.write("page.html", '<a id="same" name="same"></a>\n<span id="same"></span>')
        self.write("README.md", "[SVG](icon.svg#good)\n\n![Wrong fragment](icon.svg#missing)\n")
        errors = check_docs(self.root).errors
        self.assertEqual(len(errors), 2)
        self.assertTrue(any("page.html:2: duplicate explicit anchor 'same'" in error for error in errors))
        self.assertTrue(any("missing anchor 'missing'" in error for error in errors))

    def test_custom_anchors_do_not_change_duplicate_heading_numbering(self):
        self.write("README.md", '<a name="repeat-1"></a>\n\n# Repeat\n\n# Repeat\n\n'
                   '[First](#repeat) [Second](#repeat-1)\n')
        self.assertEqual(check_docs(self.root).errors, [])

    def test_only_unfilled_starter_targets_are_exempt(self):
        self.write("src/templates/profile/README.md", "# {{name}}\n\n"
                   "![Starter](placeholder.svg)\n\n[Unfilled](../{{slug}}/README.md)\n\n"
                   "[Encoded](../%7B%7Bslug%7D%7D/README.md)\n")
        report = check_docs(self.root)
        self.assertEqual(report.errors, [])
        self.assertEqual(report.template_references, 3)
        self.write("src/templates/ordinary.md", "[Broken](missing.md)\n")
        self.write("src/roles/completed/README.md", "![Missing](placeholder.svg)\n\n[Unfilled]({{url}})\n")
        errors = check_docs(self.root).errors
        self.assertEqual(len(errors), 3)
        self.assertTrue(all("missing target" in error for error in errors))

    def test_present_starter_image_is_still_validated(self):
        self.write("src/templates/profile/README.md", "![Starter](placeholder.svg)\n")
        self.write("src/templates/profile/placeholder.svg", "broken")
        self.assertIn("unreadable image", check_docs(self.root).errors[0])

    def test_escapes_and_symlinks_are_rejected_before_reading_outside_root(self):
        with tempfile.TemporaryDirectory() as other:
            external = Path(other) / "outside.md"
            external.write_text("# Outside\n", encoding="utf-8")
            (self.root / "alias.md").symlink_to(external)
            (self.root / "escape-dir").symlink_to(Path(other), target_is_directory=True)
            self.write("guide/README.md", "# Safe\n")
            (self.root / "guide/README.md").unlink()
            (self.root / "guide/README.md").symlink_to(external)
            self.write("README.md", "[Escape](../outside.md)\n\n[File](alias.md#outside)\n\n"
                       "[Directory](escape-dir/outside.md)\n\n[Readme](guide/#outside)\n")
            errors = check_docs(self.root).errors
            self.assertEqual(len(errors), 6)
            self.assertTrue(all("escapes preview root" in error for error in errors))

    def test_hidden_public_docs_are_checked_but_build_and_git_directories_are_skipped(self):
        self.write(".github/PULL_REQUEST_TEMPLATE.md", "[Broken](missing.md)\n")
        for directory in (".git", ".venv", "node_modules", "__pycache__"):
            self.write(f"{directory}/README.md", "[Ignored](missing.md)\n")
        report = check_docs(self.root)
        self.assertEqual(report.documents, 1)
        self.assertEqual(len(report.errors), 1)
        self.assertIn(".github/PULL_REQUEST_TEMPLATE.md:1:", report.errors[0])

    def test_empty_or_invalid_root_cannot_report_success(self):
        for root in (self.root, self.root / "missing"):
            with self.subTest(root=root), redirect_stdout(StringIO()), redirect_stderr(StringIO()):
                self.assertEqual(main(["--root", str(root)]), 1)

    def test_symlink_loop_fails_with_document_and_reference_diagnostics(self):
        (self.root / "loop.md").symlink_to("loop.md")
        self.write("README.md", "[Loop](loop.md)\n")
        errors = check_docs(self.root).errors
        self.assertEqual(len(errors), 2)
        # Python versions differ on whether resolve() or the later read/stat
        # reports a loop. Both the source document and its incoming link fail.
        self.assertTrue(any(error.startswith("loop.md:1: cannot ") for error in errors))
        self.assertTrue(any(error.startswith("README.md:1:") for error in errors))

    def test_cli_is_read_only_and_returns_failure_with_actionable_output(self):
        self.write("README.md", "# Home\n\n[Top](#home)\n")
        before = {path: path.read_bytes() for path in self.root.rglob("*") if path.is_file()}
        output, errors = StringIO(), StringIO()
        with redirect_stdout(output), redirect_stderr(errors):
            self.assertEqual(main(["--root", str(self.root)]), 0)
        self.assertIn("1 documents, 1 local references", output.getvalue())
        self.assertEqual(errors.getvalue(), "")
        self.assertEqual(before, {path: path.read_bytes() for path in self.root.rglob("*") if path.is_file()})
        self.write("README.md", "[Missing](missing.md)\n")
        output, errors = StringIO(), StringIO()
        with redirect_stdout(output), redirect_stderr(errors):
            self.assertEqual(main(["--root", str(self.root)]), 1)
        self.assertIn("README.md:1: missing target", errors.getvalue())
        self.assertEqual(output.getvalue(), "")


if __name__ == "__main__":
    unittest.main()
