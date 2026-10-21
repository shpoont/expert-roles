"""Contract checks for invalid inputs and read-only drift detection."""

from contextlib import redirect_stderr, redirect_stdout
from copy import deepcopy
from io import StringIO
from pathlib import Path
import re
import shutil
import tempfile
import tomllib
import unittest
import xml.etree.ElementTree as ET

import yaml
from PIL import Image

from src.generate import FEATURED_EXPERTS, main, plan_outputs, render_placeholder


class GenerationContractTests(unittest.TestCase):
    def setUp(self):
        self.directory = tempfile.TemporaryDirectory()
        self.addCleanup(self.directory.cleanup)
        self.root = Path(self.directory.name)
        self.readme = self.root / "README.md"
        self.readme.write_text(
            "# Test collection\n\nAuthored introduction.\n\n"
            "<!-- BEGIN GENERATED SUMMARY -->\nOld summary.\n<!-- END GENERATED SUMMARY -->\n\n"
            "## Role catalogue\n\n<!-- BEGIN GENERATED FEATURED -->\nOld showcase.\n"
            "<!-- END GENERATED FEATURED -->\n\n## Project notes\n\nKeep these notes.\n",
            encoding="utf-8",
        )
        source = Path(__file__).resolve().parents[1]
        (self.root / "src/templates").mkdir(parents=True)
        shutil.copyfile(source / "src/specialties.yaml", self.root / "src/specialties.yaml")
        shutil.copyfile(source / "src/templates/invocation.md", self.root / "src/templates/invocation.md")
        shutil.copyfile(source / "src/templates/placeholder.svg", self.root / "src/templates/placeholder.svg")
        self.catalogue = self.root / "src/roles/README.md"
        self.catalogue.parent.mkdir(parents=True)
        self.catalogue.write_text(
            "# Expert catalogue\n\nAuthored catalogue introduction.\n\n"
            "<!-- BEGIN GENERATED CATALOGUE -->\nOld catalogue.\n"
            "<!-- END GENERATED CATALOGUE -->\n\nKeep this catalogue footer.\n"
        )
        for slug, _ in FEATURED_EXPERTS:
            profile = self.root / "src/roles" / slug
            profile.mkdir()
            shutil.copyfile(source / "src/roles" / slug / "expert.yaml", profile / "expert.yaml")
            (profile / "README.md").write_text("# Test expert\n", encoding="utf-8")
            self.write_portrait(profile)
        self.profile = self.root / "src/roles/don-norman"

    @staticmethod
    def write_portrait(directory, *, size=(512, 512), image_format="JPEG", mode="RGB"):
        Image.new(mode, size).save(directory / "portrait.jpg", format=image_format)

    def run_exporter(self, *args):
        with redirect_stdout(StringIO()), redirect_stderr(StringIO()):
            return main(["--root", str(self.root), *args])

    def test_unknown_specialty_does_not_write_partial_outputs(self):
        second = self.root / "src/roles/zz-invalid-expert"
        second.mkdir()
        self.write_portrait(second)
        (second / "README.md").write_text("# Another expert\n", encoding="utf-8")
        (second / "expert.yaml").write_text(
            "name: Another expert\nspecialties: [unknown-specialty]\n", encoding="utf-8"
        )
        before = {path: path.read_bytes() for path in self.root.rglob("*") if path.is_file()}
        self.assertEqual(self.run_exporter(), 1)
        after = {path: path.read_bytes() for path in self.root.rglob("*") if path.is_file()}
        self.assertEqual(before, after)

    def test_duplicate_yaml_key_is_rejected(self):
        (self.profile / "expert.yaml").write_text(
            "name: Don Norman\nname: Someone else\nspecialties: [human-centered-design]\n",
            encoding="utf-8",
        )
        with self.assertRaisesRegex(ValueError, "unique strings"):
            plan_outputs(self.root)

    def test_invalid_or_duplicate_specialty_references_do_not_write_outputs(self):
        registry = self.root / "src/specialties.yaml"
        original = yaml.safe_load(registry.read_text())
        for failure in ("missing reference", "invalid scheme", "site homepage", "credentials",
                        "malformed URL", "duplicate concept", "duplicate name"):
            with self.subTest(failure=failure):
                data = deepcopy(original)
                entry = data["human-centered-design"]
                if failure == "missing reference":
                    del entry["reference"]
                elif failure == "invalid scheme":
                    entry["reference"] = "javascript:invalid"
                elif failure == "site homepage":
                    entry["reference"] = "https://www.wikidata.org/"
                elif failure == "credentials":
                    entry["reference"] = "https://user@example.org/concept"
                elif failure == "malformed URL":
                    entry["reference"] = "https://[invalid/concept"
                elif failure == "duplicate concept":
                    data["another-name"] = {**entry, "name": "A different label"}
                else:
                    data["another-name"] = {**entry, "name": "HUMAN-CENTERED DESIGN",
                                            "reference": "https://example.org/another-concept"}
                registry.write_text(yaml.safe_dump(data))
                before = {p: p.read_bytes() for p in self.root.rglob("*") if p.is_file()}
                self.assertEqual(self.run_exporter(), 1)
                after = {p: p.read_bytes() for p in self.root.rglob("*") if p.is_file()}
                self.assertEqual(before, after)

    def test_shared_specialties_reuse_labels_and_unused_groups_are_hidden(self):
        second = self.root / "src/roles/another-designer"
        second.mkdir()
        self.write_portrait(second)
        (second / "README.md").write_text("# Another designer\n")
        (second / "expert.yaml").write_text(
            "name: Another designer\nspecialties: [human-centered-design]\n"
        )
        registry = self.root / "src/specialties.yaml"
        data = yaml.safe_load(registry.read_text())
        data["unused-specialty"] = {"name": "Unused specialty", "group": "Unused group",
                                    "reference": "https://example.org/concepts/unused"}
        registry.write_text(yaml.safe_dump(data))
        self.assertEqual(self.run_exporter(), 0)
        catalogue = self.catalogue.read_text()
        shared = next(line for line in catalogue.splitlines()
                      if 'id="specialty-human-centered-design"' in line)
        self.assertIn("[Don Norman]", shared)
        self.assertIn("[Another designer]", shared)
        self.assertNotIn("Unused specialty", catalogue)
        self.assertNotIn("Unused group", catalogue)
        design = catalogue.split("### Design", 1)[1].split("###", 1)[0]
        self.assertLess(design.index("Human-centered design"), design.index("Human-computer interaction"))
        for slug in ("don-norman", "another-designer"):
            role = self.root / f"src/roles/{slug}/codex/expert-{slug}.toml"
            metadata = tomllib.loads(role.read_text())
            self.assertIn("Human-centered design", metadata["description"])
            self.assertNotIn("wikidata.org", metadata["developer_instructions"])

    def test_invalid_portraits_do_not_write_partial_outputs(self):
        second = self.root / "src/roles/zz-photo-expert"
        second.mkdir()
        (second / "README.md").write_text("# Photo expert\n", encoding="utf-8")
        (second / "expert.yaml").write_text(
            "name: Photo expert\nspecialties: [human-centered-design]\n", encoding="utf-8"
        )
        portrait = second / "portrait.jpg"
        for failure in ("missing", "wrong size", "disguised PNG", "CMYK", "truncated JPEG"):
            with self.subTest(failure=failure):
                if portrait.exists():
                    portrait.unlink()
                if failure == "wrong size":
                    self.write_portrait(second, size=(512, 511))
                elif failure == "disguised PNG":
                    self.write_portrait(second, image_format="PNG")
                elif failure == "CMYK":
                    self.write_portrait(second, mode="CMYK")
                elif failure == "truncated JPEG":
                    self.write_portrait(second)
                    data = portrait.read_bytes()
                    portrait.write_bytes(data[:len(data) // 2])
                before = {path: path.read_bytes() for path in self.root.rglob("*") if path.is_file()}
                self.assertEqual(self.run_exporter(), 1)
                after = {path: path.read_bytes() for path in self.root.rglob("*") if path.is_file()}
                self.assertEqual(before, after)

    def test_readme_generation_preserves_authored_content(self):
        def authored(text):
            return re.sub(r"(<!-- BEGIN GENERATED ([A-Z]+) -->).*?(<!-- END GENERATED \2 -->)",
                          r"\1\3", text, flags=re.S)

        before = {path: authored(path.read_text()) for path in (self.readme, self.catalogue)}
        self.assertEqual(self.run_exporter(), 0)
        for path, text in before.items():
            self.assertEqual(authored(path.read_text()), text)
            self.assertNotIn("Old ", path.read_text())
            path.write_text(path.read_text() + "\nAnother authored note.\n")
        self.assertIn("[Don Norman](don-norman/README.md)", self.catalogue.read_text())
        self.assertEqual(self.run_exporter("--check"), 0)
        for path, label in ((self.readme, "<strong>Don Norman</strong>"),
                            (self.catalogue, "[Don Norman]")):
            with self.subTest(path=path.name):
                edited = path.read_text()
                drift = edited.replace(label, "Wrong catalogue label")
                self.assertNotEqual(drift, edited)
                path.write_text(drift)
                self.assertEqual(self.run_exporter("--check"), 1)
                self.assertEqual(path.read_text(), drift)
                path.write_text(edited)

    def test_catalogue_growth_keeps_six_featured_cards_and_updates_both_counts(self):
        self.assertEqual(self.run_exporter(), 0)
        initial = self.readme.read_text()
        second = self.root / "src/roles/another-designer"
        second.mkdir()
        self.write_portrait(second)
        (second / "README.md").write_text("# Another designer\n")
        (second / "expert.yaml").write_text("name: Another designer\nspecialties: [human-centered-design]\n")
        self.assertEqual(self.run_exporter(), 0)
        showcase = self.readme.read_text()
        self.assertEqual(showcase.count('<td align="center"'), 6)
        self.assertEqual(showcase.count("<tr>"), 2)
        self.assertIn("**7 experts ·", showcase)
        self.assertIn("Browse all 7 experts", showcase)
        self.assertNotIn("Another designer", showcase)
        self.assertIn("[Another designer](another-designer/README.md)", self.catalogue.read_text())
        self.assertEqual(initial.replace("6 experts", "7 experts"), showcase)

    def test_invalid_featured_selection_does_not_write_partial_outputs(self):
        path = self.profile / "expert.yaml"
        entry = yaml.safe_load(path.read_text())
        entry["specialties"].remove("human-centered-design")
        path.write_text(yaml.safe_dump(entry))
        before = {p: p.read_bytes() for p in self.root.rglob("*") if p.is_file()}
        self.assertEqual(self.run_exporter(), 1)
        self.assertEqual(before, {p: p.read_bytes() for p in self.root.rglob("*") if p.is_file()})

    def test_placeholder_command_and_mixed_image_catalogue_preserve_native_instructions(self):
        expected = plan_outputs(self.root)
        (self.profile / "portrait.jpg").unlink()
        before = {p: p.read_bytes() for p in self.root.rglob("*") if p.is_file()}
        self.assertEqual(self.run_exporter("--create-placeholder", "don-norman"), 0)
        after = {p: p.read_bytes() for p in self.root.rglob("*") if p.is_file()}
        self.assertEqual(set(after) - set(before), {self.profile / "placeholder.svg"})
        self.assertTrue(all(after[p] == data for p, data in before.items()))
        actual = plan_outputs(self.root)
        readmes = {Path("README.md"), Path("src/roles/README.md")}
        self.assertEqual({p: v for p, v in expected.items() if p not in readmes},
                         {p: v for p, v in actual.items() if p not in readmes})
        second = self.root / "src/roles/photo-expert"
        second.mkdir()
        self.write_portrait(second)
        (second / "README.md").write_text("# Photo expert\n")
        (second / "expert.yaml").write_text("name: Photo expert\nspecialties: [human-centered-design]\n")
        self.assertEqual(self.run_exporter(), 0)
        self.assertEqual(self.run_exporter("--check"), 0)
        catalogue = self.catalogue.read_text()
        self.assertIn('don-norman/placeholder.svg" alt="Don Norman; name placeholder"', catalogue)
        self.assertIn('photo-expert/portrait.jpg" alt="Photo expert; photo credits on profile"', catalogue)

    def test_placeholder_creation_escapes_the_accessible_name(self):
        (self.profile / "portrait.jpg").unlink()
        name = 'A&B <Expert> "Jr."'
        (self.profile / "expert.yaml").write_text(yaml.safe_dump(
            {"name": name, "specialties": ["human-centered-design"]}))
        self.assertEqual(self.run_exporter("--create-placeholder", "don-norman"), 0)
        svg = ET.fromstring((self.profile / "placeholder.svg").read_text())
        self.assertEqual(svg.find("{http://www.w3.org/2000/svg}title").text,
                         name + " — name placeholder")
        self.assertEqual(self.run_exporter(), 0)

    def test_invalid_or_ambiguous_placeholder_do_not_write_outputs(self):
        (self.profile / "portrait.jpg").unlink()
        self.assertEqual(self.run_exporter("--create-placeholder", "don-norman"), 0)
        path = self.profile / "placeholder.svg"
        original = path.read_text()
        for failure in ("both images", "wrong name", "wrong dimensions", "active content", "malformed XML"):
            with self.subTest(failure=failure):
                path.write_text(original)
                if (self.profile / "portrait.jpg").exists():
                    (self.profile / "portrait.jpg").unlink()
                if failure == "both images":
                    self.write_portrait(self.profile)
                elif failure == "wrong name":
                    path.write_text(original.replace("Don Norman", "Another person"))
                elif failure == "wrong dimensions":
                    path.write_text(original.replace('width="512"', 'width="256"', 1))
                elif failure == "active content":
                    path.write_text(original.replace("</svg>", "<script>unexpected()</script></svg>"))
                else:
                    path.write_text(original.replace("</text>", ""))
                before = {p: p.read_bytes() for p in self.root.rglob("*") if p.is_file()}
                self.assertEqual(self.run_exporter(), 1)
                self.assertEqual(before, {p: p.read_bytes() for p in self.root.rglob("*") if p.is_file()})

    def test_placeholder_command_rejects_invalid_inputs_and_never_overwrites_an_image(self):
        for args in (
            ("--create-placeholder", "don-norman"),
            ("--create-placeholder", "../outside"),
            ("--create-placeholder", "don-norman", "--check"),
        ):
            with self.subTest(args=args):
                before = {p: p.read_bytes() for p in self.root.rglob("*") if p.is_file()}
                self.assertEqual(self.run_exporter(*args), 1)
                self.assertEqual(before, {p: p.read_bytes() for p in self.root.rglob("*") if p.is_file()})
        (self.profile / "portrait.jpg").unlink()
        source = self.profile / "expert.yaml"
        original = source.read_text()
        for name in ("", "{{name}}"):
            with self.subTest(name=name):
                source.write_text(yaml.safe_dump({"name": name, "specialties": ["human-centered-design"]}))
                before = {p: p.read_bytes() for p in self.root.rglob("*") if p.is_file()}
                self.assertEqual(self.run_exporter("--create-placeholder", "don-norman"), 1)
                self.assertEqual(before, {p: p.read_bytes() for p in self.root.rglob("*") if p.is_file()})
        source.write_text(original)
        self.assertEqual(self.run_exporter("--create-placeholder", "don-norman"), 0)
        before = {p: p.read_bytes() for p in self.root.rglob("*") if p.is_file()}
        self.assertEqual(self.run_exporter("--create-placeholder", "don-norman"), 1)
        self.assertEqual(before, {p: p.read_bytes() for p in self.root.rglob("*") if p.is_file()})

    def test_long_full_names_wrap_without_abbreviation(self):
        template = (self.root / "src/templates/placeholder.svg").read_text()
        for name in ("Jean-Baptiste Joseph Fourier", "W. Edwards Deming", "Léonie Watson"):
            with self.subTest(name=name):
                svg = ET.fromstring(render_placeholder(template, name))
                lines = [node.text for node in svg.findall(".//{http://www.w3.org/2000/svg}tspan")]
                self.assertGreater(len(lines), 1)
                self.assertEqual(" ".join(lines), name)
                text = svg.find("{http://www.w3.org/2000/svg}text")
                self.assertGreaterEqual(int(text.attrib["font-size"]), 36)

    def test_malformed_readme_markers_do_not_write_outputs(self):
        for target, section in ((self.readme, "SUMMARY"), (self.readme, "FEATURED"),
                                (self.catalogue, "CATALOGUE")):
            original = target.read_text()
            start = f"<!-- BEGIN GENERATED {section} -->"
            end = f"<!-- END GENERATED {section} -->"
            for content in (original.replace(start, ""), original.replace(end, ""),
                            original.replace(start, "REVERSED_START").replace(end, start).replace("REVERSED_START", end),
                            original.replace(start, start + start), original.replace(end, end + end)):
                with self.subTest(section=section, content=content):
                    target.write_text(content)
                    before = {p: p.read_bytes() for p in self.root.rglob("*") if p.is_file()}
                    self.assertEqual(self.run_exporter(), 1)
                    self.assertEqual(before, {p: p.read_bytes() for p in self.root.rglob("*") if p.is_file()})
            target.write_text(original)
        self.readme.write_text("<!-- BEGIN GENERATED FEATURED --><!-- BEGIN GENERATED SUMMARY -->"
                               "<!-- END GENERATED SUMMARY --><!-- END GENERATED FEATURED -->")
        before = {p: p.read_bytes() for p in self.root.rglob("*") if p.is_file()}
        self.assertEqual(self.run_exporter(), 1)
        self.assertEqual(before, {p: p.read_bytes() for p in self.root.rglob("*") if p.is_file()})

    def test_misspelled_metadata_field_is_rejected(self):
        (self.profile / "expert.yaml").write_text(
            "name: Don Norman\nspeciality: [human-centered-design]\n", encoding="utf-8"
        )
        with self.assertRaisesRegex(ValueError, "requires name and specialties, with optional perspective"):
            plan_outputs(self.root)

    def test_specialty_targets_survive_label_and_group_changes(self):
        before = plan_outputs(self.root)[Path("src/roles/README.md")]
        registry = self.root / "src/specialties.yaml"
        data = yaml.safe_load(registry.read_text())
        data["human-centered-design"]["name"] = "People-centered design"
        data["human-centered-design"]["group"] = "Another design group"
        registry.write_text(yaml.safe_dump(data))
        after = plan_outputs(self.root)[Path("src/roles/README.md")]
        for catalogue in (before, after):
            self.assertEqual(catalogue.count('id="specialty-human-centered-design"'), 1)
            self.assertIn("](#specialty-human-centered-design)", catalogue)
            anchors = re.findall(r'<a id="([^"]+)"', catalogue)
            self.assertEqual(len(anchors), len(set(anchors)))
            targets = re.findall(r'\]\(#(specialty-[^)]+)\)', catalogue)
            self.assertTrue(set(targets) <= set(anchors))
        self.assertIn('[People-centered design](#specialty-human-centered-design)', after)

    def test_optional_perspective_changes_catalogue_and_matching_host_descriptions(self):
        source = self.profile / "expert.yaml"
        entry = yaml.safe_load(source.read_text())
        entry.pop("perspective", None)
        source.write_text(yaml.safe_dump(entry))
        baseline = plan_outputs(self.root)
        phrase = 'people\'s expectations, "feedback" and café interfaces'
        source.write_text(yaml.safe_dump({**entry, "perspective": phrase}))
        outputs = plan_outputs(self.root)
        self.assertEqual(outputs[Path("README.md")], baseline[Path("README.md")])
        self.assertNotEqual(outputs[Path("src/roles/README.md")], baseline[Path("src/roles/README.md")])
        row = next(line for line in outputs[Path("src/roles/README.md")].splitlines()
                   if line.startswith("| [Don Norman]"))
        self.assertIn("Perspective: " + phrase, row)
        native = Path("src/roles/don-norman")
        codex_path = native / "codex/expert-don-norman.toml"
        claude_path = native / "claude/expert-don-norman.md"
        for content, expected in ((baseline, False), (outputs, True)):
            codex = tomllib.loads(content[codex_path])
            _, frontmatter, instruction = content[claude_path].split("---\n", 2)
            claude = yaml.safe_load(frontmatter)
            self.assertEqual(codex["description"], claude["description"])
            self.assertEqual(phrase in codex["description"], expected)
            self.assertIn("Relevant specialties include", codex["description"])
            self.assertEqual(codex["developer_instructions"], instruction.lstrip("\n"))
            self.assertEqual(codex["developer_instructions"],
                             tomllib.loads(baseline[codex_path])["developer_instructions"])
            self.assertNotIn(phrase, codex["developer_instructions"])
            self.assertEqual(set(codex), {"name", "description", "developer_instructions"})
            self.assertEqual(set(claude), {"name", "description"})

    def test_folded_perspective_is_one_description_paragraph(self):
        source = self.profile / "expert.yaml"
        entry = yaml.safe_load(source.read_text())
        entry.pop("perspective", None)
        source.write_text(yaml.safe_dump(entry) +
                          "perspective: >\n  conceptual models,\n  feedback and error.\n")
        outputs = plan_outputs(self.root)
        codex = tomllib.loads(outputs[Path("src/roles/don-norman/codex/expert-don-norman.toml")])
        self.assertIn("especially on conceptual models, feedback and error.", codex["description"])
        self.assertNotIn("\n", codex["description"])
        self.assertNotIn("error..", codex["description"])

    def test_invalid_late_perspective_does_not_write_partial_outputs(self):
        second = self.root / "src/roles/zz-invalid-expert"
        second.mkdir()
        self.write_portrait(second)
        (second / "README.md").write_text("# Another expert\n")
        source = second / "expert.yaml"
        for value in (None, True, 7, [], {}, "", " \n ", ".", "{{perspective}}"):
            with self.subTest(value=value):
                source.write_text(yaml.safe_dump({"name": "Another expert",
                    "specialties": ["human-centered-design"], "perspective": value}))
                before = {p: p.read_bytes() for p in self.root.rglob("*") if p.is_file()}
                self.assertEqual(self.run_exporter(), 1)
                self.assertEqual(before, {p: p.read_bytes() for p in self.root.rglob("*") if p.is_file()})

    def test_check_detects_drift_without_rewriting_it(self):
        self.assertEqual(self.run_exporter(), 0)
        self.assertEqual(self.run_exporter("--check"), 0)
        role = self.profile / "codex/expert-don-norman.toml"
        changed = role.read_text(encoding="utf-8") + "# Local change\n"
        role.write_text(changed, encoding="utf-8")
        self.assertEqual(self.run_exporter("--check"), 1)
        self.assertEqual(role.read_text(encoding="utf-8"), changed)

    def test_multiple_specialties_preserve_expert_identity_in_both_hosts(self):
        profile = self.root / "src/roles/eliyahu-goldratt"
        profile.mkdir(exist_ok=True)
        self.write_portrait(profile)
        (profile / "README.md").write_text("# Eliyahu Goldratt\n", encoding="utf-8")
        (profile / "expert.yaml").write_text(
            "name: Eliyahu Goldratt\nspecialties:\n"
            "  - operations-management\n  - project-management\n"
            "  - theory-of-constraints\n  - critical-chain-project-management\n",
            encoding="utf-8",
        )
        self.assertEqual(self.run_exporter(), 0)
        self.assertIn("[Eliyahu Goldratt](eliyahu-goldratt/README.md)", self.catalogue.read_text())
        codex = tomllib.loads((profile / "codex/expert-eliyahu-goldratt.toml").read_text())
        _, frontmatter, body = (profile / "claude/expert-eliyahu-goldratt.md").read_text().split("---\n", 2)
        claude = yaml.safe_load(frontmatter)
        for metadata, instruction in ((codex, codex["developer_instructions"]), (claude, body)):
            with self.subTest(host="Codex" if metadata is codex else "Claude Code"):
                self.assertEqual(metadata["name"], "expert-eliyahu-goldratt")
                for value in ("Eliyahu Goldratt", "Operations management", "Project management",
                              "Theory of Constraints", "Critical Chain project management"):
                    self.assertIn(value, metadata["description"])
                    self.assertIn(value, instruction)
                self.assertNotIn("Don Norman", instruction)
                self.assertIn("Let the task determine the focus", instruction)


if __name__ == "__main__":
    unittest.main()
