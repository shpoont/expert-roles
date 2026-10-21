"""Prepare reproducible portrait inputs and JPEGs; never call a model or install anything."""

from __future__ import annotations

import argparse
import colorsys
from datetime import date
import hashlib
import html
from html.parser import HTMLParser
import json
from pathlib import Path
import re
from string import Template
import sys
from urllib.parse import urlsplit

import yaml
from PIL import Image, ImageOps, __version__ as PILLOW_VERSION


STYLE_ID = "studio-v1"
APPROVED_BACKGROUNDS = {
    "martin-fowler": (["#AFC8BD", "#ABBAD0", "#D5C7B9"],
                      "Sage dominates a broad diagonal sweep, with a mineral-blue pool and a quiet sand transition."),
    "don-norman": (["#CFB4A6", "#DAD0BA", "#B5BED0"],
                   "Warm clay and sandstone dominate asymmetrical sideways curves, with a dusty slate edge."),
    "chip-huyen": (["#BCB0CF", "#AEBFD2", "#D6C7C1"],
                   "Violet and steel blue merge in a broad off-center arc, with a quiet pinkish-taupe accent."),
}
FLOWS = (
    "A broad diagonal sweep, with the secondary hue pooling in the opposite corner.",
    "Asymmetrical sideways curves, with a quiet accent along one edge.",
    "A broad off-center arc, with a slightly deeper outer corner and a soft center.",
    "A gently rising diagonal fold, with a soft secondary-color transition near the lower edge.",
    "Oversized softly curving vertical fields, with an off-center lighter region.",
    "A wide gentle S-shaped flow, with the smallest color field confined to a corner.",
)


class _Images(HTMLParser):
    def __init__(self):
        super().__init__()
        self.images = []

    def handle_starttag(self, tag, attrs):
        if tag == "img":
            self.images.append(dict(attrs))


def _web_link(text: str) -> bool:
    for value in re.findall(r"\]\(([^\s)]+)\)", text):
        try:
            url = urlsplit(html.unescape(value))
            if (url.scheme in {"http", "https"} and url.hostname
                    and url.username is None and url.password is None):
                return True
        except ValueError:
            pass
    return False


def validate_credit(directory: Path, filename: str, name: str) -> dict:
    """Check declared provenance and recipe consistency, never likeness or legal clearance."""
    text = (directory / "README.md").read_text(encoding="utf-8")
    sections = list(re.finditer(r"^## (Image|Photo credit)\s*\n(.*?)(?=^## |^<details>|\Z)",
                                text, re.M | re.S))
    if filename == "placeholder.svg":
        if any("AI-generated portrait" in section[2] for section in sections):
            raise ValueError(f"Placeholder has stale generated-image credits: {directory.name}")
        return {"caption": "name placeholder", "palette": None}
    if len(sections) != 1:
        raise ValueError(f"Portrait requires exactly one Image or Photo credit section: {directory.name}")
    section = sections[0]
    heading, body = section[1], section[2]
    generated = "**AI-generated portrait**" in body
    images = _Images()
    images.feed(text)
    if not generated:
        generated_metadata = (re.search(r"^\*\*Style:\*\*\s*\[studio-v\d+\]", body, re.M)
                              or re.search(r"^\*\*Tool:\*\*[^\n]*ImageGen", body, re.M | re.I))
        generated_alt = any(i.get("alt", "").endswith(" — AI-generated portrait") for i in images.images)
        if heading != "Photo credit" or generated_metadata or generated_alt:
            raise ValueError(f"Missing AI-generated portrait disclosure or invalid image type: {directory.name}")
        if not re.search(r"\*\*Source:\*\*\s*\[[^\]]+\]\(https?://", body):
            raise ValueError(f"Photo credit requires a linked Source: {directory.name}")
        caption = ("Historical depiction; sources and terms on profile"
                   if "**Historical depiction**" in body else "photo credits on profile")
        return {"caption": caption, "palette": None}
    if heading != "Image" or "{{" in body or "}}" in body:
        raise ValueError(f"Generated portrait needs a completed Image section: {directory.name}")
    expected = {"src": "portrait.jpg", "alt": name + " — AI-generated portrait",
                "width": "240", "height": "240"}
    if len(images.images) != 1 or any(images.images[0].get(k) != v for k, v in expected.items()):
        raise ValueError(f"Generated portrait requires one correctly labeled 240px hero image: {directory.name}")

    def field(label):
        found = list(re.finditer(r"^\*\*" + re.escape(label) + r":\*\*\s*(.*?)(?=^\*\*[^*\n]+:\*\*|^#{1,6} |\Z)",
                                 body, re.M | re.S))
        if len(found) != 1 or not found[0][1].strip():
            raise ValueError(f"Generated portrait requires one nonempty {label} field: {directory.name}")
        return found[0][1].strip()

    style = re.match(r"\[" + re.escape(STYLE_ID) + r"\]\([^)]+\),\s*background variant \*\*(\d+)\*\*;", field("Style"))
    if not style:
        raise ValueError(f"Generated portrait requires {STYLE_ID} and a background variant: {directory.name}")
    recipe = background_recipe(directory.name, int(style[1]))
    palette = tuple(re.findall(r"#[0-9a-fA-F]{6}\b", field("Palette")))
    if palette != tuple(recipe["palette"]) or field("Flow") != recipe["flow"]:
        raise ValueError(f"Generated portrait background differs from its stable recipe: {directory.name}")
    for label in ("Tool", "Model", "Method", "Changes"):
        field(label)
    created = field("Created")
    try:
        if not re.fullmatch(r"\d{4}-\d{2}-\d{2}", created):
            raise ValueError
        date.fromisoformat(created)
    except ValueError:
        raise ValueError(f"Generated portrait Created must be an ISO calendar date: {directory.name}") from None
    terms = [label for label in ("Generated adaptation license", "Generated contribution license")
             if f"**{label}:**" in body]
    if len(terms) != 1:
        raise ValueError(f"Generated portrait requires one output-terms field: {directory.name}")
    output = field(terms[0])
    local_mit = ("[MIT](../../../LICENSE)" in output and (directory.parents[2] / "LICENSE").is_file())
    if not _web_link(output) and not local_mit:
        raise ValueError(f"Generated portrait output terms need a license/permission link: {directory.name}")
    references = re.search(r"^### Reference attribution\s*\n(.*)", body, re.M | re.S)
    sources = (list(re.finditer(r"\*\*Source:\*\*[ \t]*(\[[^\]]+\]\([^\s]+\))", references[1]))
               if references else [])
    if not sources or not all(_web_link(source[1]) for source in sources):
        raise ValueError(f"Generated portrait requires linked reference attribution: {directory.name}")
    for index, source in enumerate(sources):
        end = sources[index + 1].start() if index + 1 < len(sources) else len(references[1])
        reference = references[1][source.start():end]
        reference_terms = re.findall(
            r"^(?:- )?\*\*(License(?: / permission)?|Permission|Copyright status):\*\*[ \t]*(.*?)"
            r"(?=^(?:- )?\*\*[^*\n]+:\*\*|^#{1,6} |\Z)", reference, re.M | re.S)
        valid_terms = (all(_web_link(value) or (label == "Copyright status"
                           and re.search(r"public[ -]domain", value, re.I))
                           for label, value in reference_terms) if reference_terms
                       else re.search(r"public[ -]domain", reference, re.I))
        if not valid_terms:
            raise ValueError(f"Generated portrait requires recorded reference terms for each Source: {directory.name}")
    return {"caption": "AI-generated portrait; sources and terms on profile", "palette": palette}


def background_recipe(slug: str, variant: int = 0) -> dict:
    if not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", slug) or variant < 0:
        raise ValueError("Use a canonical expert slug and a nonnegative background variant")
    if variant == 0 and slug in APPROVED_BACKGROUNDS:
        palette, flow = APPROVED_BACKGROUNDS[slug]
        return {"variant": variant, "palette": list(palette), "flow": flow}
    digest = hashlib.sha256(f"{STYLE_ID}:{slug}:{variant}".encode()).digest()
    hue = int.from_bytes(digest[:2], "big") / 65536
    turn = (35 + digest[2] % 36) / 360 * (-1 if digest[3] % 2 else 1)
    settings = ((hue, .72 + digest[4] / 255 * .06, .24 + digest[5] / 255 * .06),
                ((hue + turn) % 1, .74 + digest[6] / 255 * .06, .21 + digest[7] / 255 * .05),
                ((hue + .45) % 1, .77 + digest[8] / 255 * .05, .12 + digest[9] / 255 * .06))
    palette = ["#" + "".join(f"{round(c * 255):02X}" for c in colorsys.hls_to_rgb(*values))
               for values in settings]
    return {"variant": variant, "palette": palette, "flow": FLOWS[digest[10] % len(FLOWS)]}


def make_recipe(root: Path, slug: str, references: list[Path], *,
                appearance_note: str = "Preserve the documented appearance of the target person.",
                variant: int = 0) -> dict:
    background = background_recipe(slug, variant)
    entry = yaml.safe_load((root / "src/roles" / slug / "expert.yaml").read_text(encoding="utf-8"))
    if not isinstance(entry, dict) or not isinstance(entry.get("name"), str):
        raise ValueError("Expert metadata must contain a name")
    if not references:
        raise ValueError("At least one permitted photographic reference is required")
    reference_records = []
    for path in references:
        path = path.resolve()
        with Image.open(path) as source:
            dimensions = list(source.size)
            source.verify()
        reference_records.append({"file": str(path), "sha256": hashlib.sha256(path.read_bytes()).hexdigest(),
                                  "dimensions": dimensions})
    template = (root / "src/templates/portrait.txt").read_text(encoding="utf-8")
    description = ", ".join(background["palette"]) + ". " + background["flow"]
    prompt = Template(template).substitute(style_id=STYLE_ID, name=entry["name"],
                                           appearance_note=appearance_note, background=description)
    return {"style_id": STYLE_ID, "expert_slug": slug, "name": entry["name"],
            "background": background, "appearance_note": appearance_note,
            "template_sha256": hashlib.sha256(template.encode()).hexdigest(),
            "references": reference_records, "prompt": prompt,
            "tool": "built-in ImageGen", "model": "not disclosed unless exposed by the tool",
            "preparation": {"size": [512, 512], "mode": "RGB", "format": "JPEG",
                            "quality": 95, "subsampling": 0, "pillow": PILLOW_VERSION}}


def save_recipe(record: dict, output: Path, root: Path) -> None:
    if output.resolve().is_relative_to(root.resolve()):
        raise ValueError("Save run records outside the public repository; they contain local reference paths")
    output.parent.mkdir(parents=True, exist_ok=True)
    with output.open("x", encoding="utf-8") as stream:
        json.dump(record, stream, ensure_ascii=False, indent=2)
        stream.write("\n")


def prepare_image(source: Path, output: Path, *, replace: bool = False) -> None:
    if output.suffix.lower() not in {".jpg", ".jpeg"}:
        raise ValueError("The prepared portrait must use a .jpg or .jpeg filename")
    if source.resolve() == output.resolve():
        raise ValueError("Keep the original master; input and output must differ")
    if output.exists() and not replace:
        raise ValueError("Output already exists; use --replace only for an authorized replacement")
    with Image.open(source) as original:
        image = ImageOps.fit(ImageOps.exif_transpose(original).convert("RGB"), (512, 512),
                             method=Image.Resampling.LANCZOS, centering=(.5, .5))
        output.parent.mkdir(parents=True, exist_ok=True)
        image.save(output, format="JPEG", quality=95, subsampling=0)


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    commands = parser.add_subparsers(dest="command", required=True)
    recipe = commands.add_parser("recipe", help="Save a prompt, stable background and reference hashes outside the repo")
    recipe.add_argument("slug")
    recipe.add_argument("--reference", type=Path, action="append", required=True)
    recipe.add_argument("--appearance-note", default="Preserve the documented appearance of the target person.")
    recipe.add_argument("--background-variant", type=int, default=0)
    recipe.add_argument("--output", type=Path, required=True)
    prepare = commands.add_parser("prepare", help="Normalize a selected master to a 512 x 512 RGB JPEG")
    prepare.add_argument("input", type=Path)
    prepare.add_argument("--output", type=Path, required=True)
    prepare.add_argument("--replace", action="store_true")
    args = parser.parse_args(argv)
    try:
        if args.command == "recipe":
            record = make_recipe(args.root, args.slug, args.reference,
                                 appearance_note=args.appearance_note, variant=args.background_variant)
            save_recipe(record, args.output, args.root)
        else:
            prepare_image(args.input, args.output, replace=args.replace)
    except (OSError, ValueError, KeyError, yaml.YAMLError) as error:
        print(str(error), file=sys.stderr)
        return 1
    print("Saved recipe." if args.command == "recipe" else "Prepared 512 x 512 RGB JPEG.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
