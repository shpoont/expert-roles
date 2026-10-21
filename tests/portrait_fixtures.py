"""Synthetic credit fixtures; these test the contract, never likeness or model quality."""
from pathlib import Path
import html
import re

from src.portraits import background_recipe


def generated_profile(slug="test-expert", name="Test Expert"):
    source = Path(__file__).resolve().parents[1]
    template = (source / "src/templates/portrait-credit/README.md").read_text()
    template = re.sub(r"<!--.*?-->", "", template, flags=re.S).strip() + "\n"
    background = background_recipe(slug)
    values = {
        "background_variant": str(background["variant"]),
        "palette": ", ".join("`" + color + "`" for color in background["palette"]),
        "flow": background["flow"],
        "tool": "Synthetic fixture generator; no image model was called.",
        "created_date": "2026-10-21",
        "model_or_not_disclosed": "not disclosed",
        "actual_generation_and_correction_method": "Synthetic fixture used only for contract validation.",
        "generation_changes_and_image_preparation": "512 x 512 RGB JPEG preparation.",
        "linked_output_terms_and_scope": "[CC0](https://creativecommons.org/publicdomain/zero/1.0/).",
        "reference_creator_title_and_date": "Test suite, synthetic color fixture, 2026-10-21.",
        "source_title": "Synthetic fixture",
        "source_url": "https://example.org/fixtures/reference",
        "linked_reference_terms": "[CC0](https://creativecommons.org/publicdomain/zero/1.0/)",
        "reference_changes_or_none": "None.",
    }
    for key, value in values.items():
        template = template.replace("{{" + key + "}}", value)
    assert "{{" not in template and "}}" not in template
    hero = '<img src="portrait.jpg" alt="' + html.escape(name, quote=True) + ' — AI-generated portrait" width="240" height="240">\n\n'
    return "# " + name + "\n\n" + hero + template
