"""Portrait reproducibility, archive boundaries and deterministic preparation contracts."""

from pathlib import Path
import re
import shutil
import tempfile
import unittest

from PIL import Image

from src.portraits import background_recipe, make_recipe, prepare_image, save_recipe, validate_credit
from portrait_fixtures import generated_profile


class PortraitMethodTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.directory = Path(self.temp.name)
        self.root = self.directory / "public"
        profile = self.root / "src/roles/test-expert"
        profile.mkdir(parents=True)
        (profile / "expert.yaml").write_text("name: Test Expert\nspecialties: [design]\n")
        templates = self.root / "src/templates"
        templates.mkdir()
        source = Path(__file__).resolve().parents[1]
        shutil.copy2(source / "src/templates/portrait.txt", templates / "portrait.txt")
        self.reference = self.directory / "reference.png"
        Image.new("RGB", (80, 120), "red").save(self.reference)
        self.profile = profile

    def test_backgrounds_are_stable_individual_and_allow_explicit_variants(self):
        baseline = background_recipe("test-expert")
        self.assertEqual(baseline, background_recipe("test-expert"))
        self.assertNotEqual(baseline, background_recipe("another-expert"))
        self.assertNotEqual(baseline["palette"], background_recipe("test-expert", 1)["palette"])
        root = Path(__file__).resolve().parents[1]
        signatures = [tuple(background_recipe(p.name)["palette"]) for p in (root / "src/roles").iterdir()
                      if p.is_dir()]
        self.assertEqual(len(signatures), len(set(signatures)))

    def test_approved_sample_palette_is_pinned_for_style_v1(self):
        self.assertEqual(background_recipe("martin-fowler")["palette"],
                         ["#AFC8BD", "#ABBAD0", "#D5C7B9"])

    def test_recipe_records_changed_reference_bytes_without_changing_style(self):
        first = make_recipe(self.root, "test-expert", [self.reference])
        Image.new("RGB", (80, 120), "blue").save(self.reference)
        second = make_recipe(self.root, "test-expert", [self.reference])
        self.assertNotEqual(first["references"][0]["sha256"], second["references"][0]["sha256"])
        self.assertEqual(first["prompt"], second["prompt"])
        self.assertIn("DIRECT EYE CONTACT", first["prompt"])
        self.assertIn("Test Expert", first["prompt"])
        with self.assertRaises(ValueError):
            make_recipe(self.root, "test-expert", [])

    def test_local_reference_records_cannot_enter_the_public_tree_or_overwrite_history(self):
        record = make_recipe(self.root, "test-expert", [self.reference])
        with self.assertRaises(ValueError):
            save_recipe(record, self.root / "run.json", self.root)
        output = self.directory / "review/run.json"
        save_recipe(record, output, self.root)
        original = output.read_bytes()
        with self.assertRaises(FileExistsError):
            save_recipe(record, output, self.root)
        self.assertEqual(original, output.read_bytes())

    def test_preparation_respects_exif_orientation_and_is_repeatable(self):
        source = self.directory / "oriented.png"
        image = Image.new("RGB", (160, 80), "red")
        image.paste("blue", (80, 0, 160, 80))
        exif = image.getexif()
        exif[274] = 6
        image.save(source, exif=exif)
        first, second = self.directory / "one.jpg", self.directory / "two.jpg"
        prepare_image(source, first)
        prepare_image(source, second)
        self.assertEqual(first.read_bytes(), second.read_bytes())
        with Image.open(first) as prepared:
            self.assertEqual((prepared.size, prepared.mode, prepared.format), ((512, 512), "RGB", "JPEG"))
            self.assertGreater(prepared.getpixel((256, 128))[0], 240)
            self.assertGreater(prepared.getpixel((256, 384))[2], 240)

    def test_preparation_preserves_existing_output_until_replacement_is_explicit(self):
        output = self.directory / "portrait.jpg"
        output.write_bytes(b"keep")
        with self.assertRaises(ValueError):
            prepare_image(self.reference, output)
        self.assertEqual(output.read_bytes(), b"keep")
        with self.assertRaises(ValueError):
            prepare_image(self.reference, self.reference, replace=True)
        prepare_image(self.reference, output, replace=True)
        with Image.open(output) as image:
            self.assertEqual(image.size, (512, 512))

    def test_copyable_credit_template_accepts_a_new_expert(self):
        (self.profile / "README.md").write_text(generated_profile())
        credit = validate_credit(self.profile, "portrait.jpg", "Test Expert")
        self.assertEqual(credit["caption"], "AI-generated portrait; sources and terms on profile")
        self.assertEqual(credit["palette"], tuple(background_recipe("test-expert")["palette"]))

    def test_required_generated_fields_cannot_be_omitted_or_left_blank(self):
        original = generated_profile()
        labels = ("Style", "Palette", "Flow", "Tool", "Created", "Model", "Method", "Changes",
                  "Generated adaptation license")
        for label in labels:
            for value in ("missing", "blank"):
                with self.subTest(label=label, value=value):
                    pattern = r"^\*\*" + re.escape(label) + r":\*\*[^\n]*"
                    replacement = "" if value == "missing" else "**" + label + ":**"
                    text = re.sub(pattern, replacement, original, count=1, flags=re.M)
                    (self.profile / "README.md").write_text(text)
                    with self.assertRaises(ValueError):
                        validate_credit(self.profile, "portrait.jpg", "Test Expert")

    def test_disclosure_and_hero_must_agree(self):
        original = generated_profile()
        invalid = [original.replace("**AI-generated portrait**", "Portrait"),
                   original.replace("## Image", "## Photo credit"),
                   original.replace("Test Expert — AI-generated portrait", "Test Expert"),
                   original.replace('src="portrait.jpg"', 'src="placeholder.svg"'),
                   original.replace('width="240"', 'width="160"'),
                   original + '\n<img src="portrait.jpg" alt="Extra image">',
                   original.replace("not disclosed", "{{model}}")]
        for text in invalid:
            with self.subTest(text=text[:100]):
                (self.profile / "README.md").write_text(text)
                with self.assertRaises(ValueError):
                    validate_credit(self.profile, "portrait.jpg", "Test Expert")
        (self.profile / "README.md").write_text(original)
        with self.assertRaisesRegex(ValueError, "stale"):
            validate_credit(self.profile, "placeholder.svg", "Test Expert")

    def test_background_and_date_drift_is_rejected(self):
        original = generated_profile()
        first = background_recipe("test-expert")["palette"][0]
        for old, new in (("[studio-v1]", "[studio-v2]"),
                         ("variant **0**", "variant **1**"),
                         (first, "#000000"),
                         ("**Flow:** ", "**Flow:** Wrong flow. "),
                         ("2026-10-21", "2026-02-30")):
            with self.subTest(replacement=new):
                (self.profile / "README.md").write_text(original.replace(old, new, 1))
                with self.assertRaises(ValueError):
                    validate_credit(self.profile, "portrait.jpg", "Test Expert")

    def test_reference_and_output_terms_need_actual_links(self):
        original = generated_profile()
        invalid = [original.replace("**Source:**", "Source:"),
                   original.replace("https://example.org/fixtures/reference", "javascript:invalid"),
                   original.replace("**License / permission:** [CC0](https://creativecommons.org/publicdomain/zero/1.0/)",
                                    "**License / permission:** unknown"),
                   original.replace("**Generated adaptation license:** [CC0](https://creativecommons.org/publicdomain/zero/1.0/).",
                                    "**Generated adaptation license:** unknown"),
                   original.replace("### Reference attribution", "### Unspecified inputs")]
        for text in invalid:
            with self.subTest(text=text[-200:]):
                (self.profile / "README.md").write_text(text)
                with self.assertRaises(ValueError):
                    validate_credit(self.profile, "portrait.jpg", "Test Expert")

    def test_custom_permission_and_public_domain_are_not_a_license_allowlist(self):
        original = generated_profile()
        custom = original.replace("**License / permission:** [CC0](https://creativecommons.org/publicdomain/zero/1.0/)",
                                  "**License / permission:** [Custom reuse grant](https://example.org/rights)")
        (self.profile / "README.md").write_text(custom)
        validate_credit(self.profile, "portrait.jpg", "Test Expert")
        public_domain = original.replace("**License / permission:**", "Public-domain reference;")
        public_domain = public_domain.replace("**Generated adaptation license:** [CC0](https://creativecommons.org/publicdomain/zero/1.0/).",
                                             "**Generated contribution license:** [MIT](../../../LICENSE), only to the extent rights can be granted.")
        (self.root / "LICENSE").write_text("MIT fixture\n")
        (self.profile / "README.md").write_text(public_domain)
        validate_credit(self.profile, "portrait.jpg", "Test Expert")

    def test_original_credits_can_describe_a_camera_and_disclaim_ai_generation(self):
        for historical in (False, True):
            with self.subTest(historical=historical):
                label = "**Historical depiction** — not an AI-generated portrait.\n\n" if historical else ""
                text = ("# Test Expert\n\n## Photo credit\n\n" + label
                        + "**Model:** Camera model.\n**Method:** Original photograph or scan.\n\n"
                        + "**Source:** [Original](https://example.org/original).\n\n"
                        + "**License:** [CC0](https://creativecommons.org/publicdomain/zero/1.0/).\n")
                (self.profile / "README.md").write_text(text)
                credit = validate_credit(self.profile, "portrait.jpg", "Test Expert")
                self.assertIsNone(credit["palette"])
                self.assertEqual(credit["caption"].startswith("Historical depiction"), historical)

    def test_reference_terms_are_scoped_to_each_source(self):
        original = generated_profile()
        public_domain = original.replace("**License / permission:**", "Public-domain reference;")
        for first in (original, public_domain):
            for terms in ("", "- **License / permission:** unknown\n"):
                with self.subTest(first_is_public_domain=first == public_domain, terms=terms):
                    second = ("\nAnother photograph.\n\n"
                              "- **Source:** [Second reference](https://example.org/second).\n" + terms)
                    (self.profile / "README.md").write_text(first + second)
                    with self.assertRaisesRegex(ValueError, "reference terms"):
                        validate_credit(self.profile, "portrait.jpg", "Test Expert")

    def test_multiple_references_can_have_distinct_reuse_terms(self):
        text = generated_profile() + (
            "\nSecond photograph.\n\n"
            "- **Source:** [Second reference](https://example.org/second).\n"
            "- **Permission:** [Custom reuse grant](https://example.org/rights).\n\n"
            "Third photograph.\n\n"
            "- **Source:** [Third reference](https://example.org/third).\n"
            "- **Copyright status:** Public-domain reference.\n"
        )
        (self.profile / "README.md").write_text(text)
        validate_credit(self.profile, "portrait.jpg", "Test Expert")


if __name__ == "__main__":
    unittest.main()
