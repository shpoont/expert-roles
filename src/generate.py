"""Create name placeholders or render catalogues and dist role files; never install them."""

from __future__ import annotations

import argparse
import html
import json
from pathlib import Path
import re
import sys
import tomllib
from urllib.parse import urlsplit
import xml.etree.ElementTree as ET

import yaml
from PIL import Image, ImageFont


# Curated for breadth; each display label resolves through an assigned specialty.
FEATURED_EXPERTS = (
    ("chip-huyen", "machine-learning"),
    ("martin-fowler", "software-architecture"),
    ("don-norman", "human-centered-design"),
    ("eliyahu-goldratt", "theory-of-constraints"),
    ("philip-kotler", "marketing-management"),
    ("aswath-damodaran", "corporate-finance"),
)
PORTRAIT_SIZE = (512, 512)


class UniqueLoader(yaml.SafeLoader):
    """Reject duplicate YAML keys instead of silently discarding a value."""


def unique_mapping(loader, node):
    result = {}
    for key_node, value_node in node.value:
        key = loader.construct_object(key_node, deep=True)
        if not isinstance(key, str) or key in result:
            raise ValueError(f"YAML keys must be unique strings: {key!r}")
        result[key] = loader.construct_object(value_node, deep=True)
    return result


UniqueLoader.add_constructor(yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG, unique_mapping)


def read_yaml(path: Path):
    return yaml.load(path.read_text(encoding="utf-8"), Loader=UniqueLoader)


def read_expert(directory: Path) -> dict:
    entry = read_yaml(directory / "expert.yaml")
    if (not isinstance(entry, dict) or not {"name", "specialties"} <= set(entry)
            or set(entry) - {"name", "specialties", "perspective"}):
        raise ValueError(f"src/roles/{directory.name}/expert.yaml requires name and specialties, with optional perspective")
    if "perspective" in entry:
        value = entry["perspective"]
        if (not isinstance(value, str) or not value.strip()
                or "{{" in value or "}}" in value):
            raise ValueError(f"Perspective must be nonempty authored text: {directory.name}")
        entry["perspective"] = " ".join(value.split()).removesuffix(".")
        if not entry["perspective"]:
            raise ValueError(f"Perspective must be nonempty authored text: {directory.name}")
    return entry


def text_value(value) -> bool:
    return isinstance(value, str) and bool(value.strip()) and "\n" not in value


def identifier(value) -> bool:
    return isinstance(value, str) and re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", value) is not None


def reference_url(value) -> bool:
    if not text_value(value) or any(character.isspace() for character in value):
        return False
    try:
        parsed = urlsplit(value)
        return bool(parsed.scheme in {"http", "https"} and parsed.hostname
                    and parsed.username is None and parsed.password is None
                    and parsed.path.strip("/"))
    except ValueError:
        return False


def markdown_text(value: str) -> str:
    """Keep display text literal inside Markdown table cells and link labels."""
    return re.sub(r"([\\`*_\[\]<>|&~#])", r"\\\1", value)


def heading_anchor(value: str) -> str:
    return re.sub(r"[^\w\- ]", "", value.lower()).replace(" ", "-")


def update_readme(readme: str, content: str, section: str, source: str) -> str:
    """Replace only the generated section, refusing ambiguous boundaries."""
    start_marker = f"<!-- BEGIN GENERATED {section} -->"
    end_marker = f"<!-- END GENERATED {section} -->"
    error = f"{source} requires one ordered BEGIN GENERATED {section} / END GENERATED {section} marker pair"
    if readme.count(start_marker) != 1 or readme.count(end_marker) != 1:
        raise ValueError(error)
    start = readme.index(start_marker) + len(start_marker)
    end = readme.index(end_marker)
    if end < start:
        raise ValueError(error)
    if re.search(r"<!-- (?:BEGIN|END) GENERATED [A-Z]+ -->", readme[start:end]):
        raise ValueError(f"Generated sections must not overlap or nest: {source}")
    return readme[:start] + "\n\n" + content.rstrip() + "\n\n" + readme[end:]


def catalogue_image(expert: dict, profile_path: str) -> str:
    name = html.escape(expert["name"], quote=True).replace("|", "&#124;")
    caption = "name placeholder" if expert["image"] == "placeholder.svg" else "photo credits on profile"
    return (f'<a href="{profile_path}/README.md"><img src="{profile_path}/{expert["image"]}" '
            f'alt="{name}; {caption}" width="160" height="160"></a>')


def specialty_group_links(groups: list[str]) -> str:
    return " · ".join(f"[{markdown_text(group)}](#{heading_anchor(group)})" for group in groups)


def specialty_tables(experts, specialties, groups, destination, column="Experts") -> list[str]:
    """Render the same assignments for profile or native-file destinations."""
    lines = []
    for group in groups:
        lines += [f"### {markdown_text(group)}", "", f"| Specialty | {column} |", "| --- | --- |"]
        for tag, entry in sorted(specialties.items(), key=lambda item: item[1]["name"].casefold()):
            if entry["group"] != group:
                continue
            links = [f'[{markdown_text(expert["name"])}]({destination(expert)})'
                     for expert in experts if tag in expert["tags"]]
            if links:
                lines.append(f'| <a id="specialty-{tag}"></a>{markdown_text(entry["name"])} | {", ".join(links)} |')
        lines.append("")
    return lines


def distribution_index(experts, specialties, groups, title: str, extension: str) -> str:
    experts = sorted(experts, key=lambda expert: expert["name"].casefold())
    lines = [
        f"# {title} roles", "",
        "<!-- Generated by src/generate.py; edit source metadata, specialties or the generator. -->", "",
        "[Other formats](../README.md) · [Setup guide](../../docs/delivery.md#use-a-native-role) ·",
        "[Full catalogue](../../src/roles/README.md)", "",
        f"**{len(experts)} role files.** Each expert has one file in this directory.",
        "An expert may appear under several specialties below.", "",
        f"For programmatic imports, select `expert-*.{extension}` files.", "",
        "[By name](#by-name) · [By specialty](#by-specialty)", "",
        f"Jump to a specialty group: {specialty_group_links(groups)}", "",
        "## By name", "",
        "Use your browser's Find (Cmd+F or Ctrl+F) to find a known expert.", "",
        "| Expert | Role file |", "| --- | --- |",
    ]
    for expert in experts:
        slug = expert["slug"]
        filename = f"expert-{slug}.{extension}"
        lines.append(f'| [{markdown_text(expert["name"])}](../../src/roles/{slug}/README.md) | [{filename}]({filename}) |')
    lines += [
        "", "## By specialty", "",
        f"Names in these tables link directly to the {title} role files.",
        "For introductions, perspective cues and suggested uses, follow the profiles",
        "in [By name](#by-name) or compare experts in the [full catalogue](../../src/roles/README.md).", "",
    ]
    lines += specialty_tables(experts, specialties, groups,
                              lambda expert: f'expert-{expert["slug"]}.{extension}', "Role files")
    lines += [
        "## Use and licensing", "",
        "Follow the [setup guide](../../docs/delivery.md#use-a-native-role) for host requirements",
        "and validation limits. Role files use [MIT](../../LICENSE); retain its copyright",
        "and permission notice with copies. Specialty labels retain their",
        "[source credits and terms](../../docs/elements/specialties.md#source-attribution).", "",
        "These files are generated. Edit the [sources](../../src/README.md#generate-the-catalogue-and-native-files)",
        "and regenerate; include source changes and updated outputs together.", "",
    ]
    return "\n".join(lines)


def validate_portrait(directory: Path) -> None:
    path = directory / "portrait.jpg"
    if not path.is_file():
        raise ValueError(f"Required portrait.jpg is missing: {directory.name}")
    try:
        with Image.open(path) as portrait:
            if (portrait.format != "JPEG" or portrait.mode != "RGB"
                    or portrait.size != PORTRAIT_SIZE):
                raise ValueError(f"portrait.jpg must be a 512 x 512 RGB JPEG: {directory.name}")
            portrait.load()
    except OSError as error:
        raise ValueError(f"Unreadable portrait.jpg for {directory.name}: {error}") from error


def render_placeholder(template: str, name: str) -> str:
    if not text_value(name) or "{{" in name or "}}" in name:
        raise ValueError("Fill expert.yaml with the expert's full name before creating a placeholder")
    if set(re.findall(r"\{\{(.*?)\}\}", template)) != {"name", "font_size", "lines"}:
        raise ValueError("SVG template requires only {{name}}, {{font_size}} and {{lines}}")
    for font_size in range(72, 0, -1):
        font = ImageFont.load_default(size=font_size)
        lines = []
        for word in name.split():
            candidate = f"{lines[-1]} {word}" if lines else word
            if lines and font.getlength(candidate) <= 352:
                lines[-1] = candidate
            else:
                lines.append(word)
        if (max(font.getlength(line) for line in lines) <= 352
                and len(lines) * font_size * 1.25 <= 352):
            break
    else:
        raise ValueError("The full name needs a reviewed layout to fit the placeholder")
    first_baseline = 256 - (len(lines) - 1) * font_size * 1.25 / 2 + font_size * .35
    spans = "".join(
        f'\n    <tspan x="256" y="{first_baseline + index * font_size * 1.25:.1f}">{html.escape(line)}</tspan>'
        for index, line in enumerate(lines)
    )
    svg = template.replace("{{name}}", html.escape(name)).replace(
        "{{font_size}}", str(font_size)).replace("{{lines}}", spans)
    try:
        ET.fromstring(svg)
    except ET.ParseError as error:
        raise ValueError("The name or template contains invalid XML") from error
    return svg


def create_placeholder(root: Path, slug: str) -> Path:
    if not identifier(slug):
        raise ValueError("Choose an existing expert's lowercase, hyphenated directory slug")
    directory = root / "src/roles" / slug
    entry = read_expert(directory)
    template = (root / "src/templates/placeholder.svg").read_text(encoding="utf-8")
    svg = render_placeholder(template, entry["name"])
    if any((directory / name).exists() for name in ("portrait.jpg", "placeholder.svg")):
        raise ValueError(f"An image already exists for {slug}; this command never overwrites it")
    destination = directory / "placeholder.svg"
    with destination.open("x", encoding="utf-8") as output:
        output.write(svg)
    return destination.relative_to(root)


def validate_image(directory: Path, name: str, template: str) -> str:
    images = [directory / filename for filename in ("portrait.jpg", "placeholder.svg")
              if (directory / filename).exists()]
    if len(images) != 1 or not images[0].is_file():
        raise ValueError(f"Provide exactly one of portrait.jpg or placeholder.svg: {directory.name}")
    image = images[0]
    if image.name == "portrait.jpg":
        validate_portrait(directory)
    else:
        svg = image.read_text(encoding="utf-8")
        if svg != render_placeholder(template, name):
            raise ValueError(f"Recreate placeholder.svg using --create-placeholder for {directory.name}")
    return image.name


def plan_outputs(root: Path) -> dict[Path, str]:
    """Validate every input and render in memory before any file is changed."""
    specialties = read_yaml(root / "src/specialties.yaml")
    if not isinstance(specialties, dict) or not specialties:
        raise ValueError("src/specialties.yaml must contain a nonempty mapping")
    specialty_names, references = set(), set()
    for key, entry in specialties.items():
        if (not identifier(key) or not isinstance(entry, dict)
                or set(entry) != {"name", "group", "reference"}
                or not all(text_value(value) for value in entry.values())):
            raise ValueError(f"Invalid specialty entry: {key!r}")
        if not reference_url(entry["reference"]):
            raise ValueError(f"Invalid specialty reference: {key!r}")
        name = " ".join(entry["name"].split()).casefold()
        if name in specialty_names or entry["reference"] in references:
            raise ValueError(f"Duplicate specialty name or reference: {key!r}")
        specialty_names.add(name)
        references.add(entry["reference"])

    template = (root / "src/templates/invocation.md").read_text(encoding="utf-8").strip() + "\n"
    if set(re.findall(r"\{\{(.*?)\}\}", template)) != {"name", "specialties"}:
        raise ValueError("Template must use only {{name}} and {{specialties}}, both required")
    image_template = (root / "src/templates/placeholder.svg").read_text(encoding="utf-8")

    experts = []
    names = set()
    directories = sorted(path for path in (root / "src/roles").iterdir() if path.is_dir())
    for directory in directories:
        slug = directory.name
        source = directory / "expert.yaml"
        if not identifier(slug) or not source.is_file() or not (directory / "README.md").is_file():
            raise ValueError(f"Expert directory needs a valid slug, expert.yaml and README.md: {slug}")
        entry = read_expert(directory)
        name, tags = entry["name"], entry["specialties"]
        if not text_value(name) or name in names:
            raise ValueError(f"Expert names must be nonempty and unique: {slug}")
        if (not isinstance(tags, list) or not tags or not all(identifier(tag) for tag in tags)
                or len(tags) != len(set(tags))):
            raise ValueError(f"Specialties must be a nonempty list of unique identifiers: {slug}")
        unknown = set(tags) - set(specialties)
        if unknown:
            raise ValueError(f"Unknown specialties in {slug}: {', '.join(sorted(unknown))}")
        image = validate_image(directory, name, image_template)
        names.add(name)
        experts.append({"slug": slug, "name": name, "tags": tags, "image": image,
                        "perspective": entry.get("perspective")})
    if not experts:
        raise ValueError("At least one expert profile is required")

    by_slug = {expert["slug"]: expert for expert in experts}
    if len(FEATURED_EXPERTS) != 6 or len({slug for slug, _ in FEATURED_EXPERTS}) != 6:
        raise ValueError("The README showcase requires exactly six distinct experts")
    for slug, tag in FEATURED_EXPERTS:
        if slug not in by_slug or tag not in by_slug[slug]["tags"]:
            raise ValueError(f"Featured expert requires an existing profile and assigned specialty: {slug}, {tag}")

    outputs = {}
    for expert in experts:
        slug, name, tags = expert["slug"], expert["name"], expert["tags"]
        labels = [specialties[tag]["name"] for tag in tags]
        labels = labels[0] if len(labels) == 1 else ", ".join(labels[:-1]) + " and " + labels[-1]
        instruction = template.replace("{{name}}", name).replace("{{specialties}}", labels)
        focus = (f", especially on {expert['perspective']}" if expert["perspective"]
                 else " within their documented expertise")
        metadata = {
            "name": f"expert-{slug}",
            "description": f"Consider {name}'s perspective{focus}. Relevant specialties include {labels}.",
        }
        escaped = instruction.replace("\\", "\\\\").replace('"', '\\"')
        toml = "# Generated by src/generate.py; edit the source metadata or shared template.\n"
        toml += "\n".join(f"{key} = {json.dumps(value, ensure_ascii=False)}" for key, value in metadata.items())
        toml += '\n\ndeveloper_instructions = """\n' + escaped + '"""\n'
        if tomllib.loads(toml)["developer_instructions"] != instruction:
            raise ValueError(f"Generated TOML changed the instruction: {slug}")
        markdown = "---\n# Generated by src/generate.py; edit the source metadata or shared template.\n"
        markdown += yaml.safe_dump(metadata, allow_unicode=True, sort_keys=False, width=1000)
        markdown += "---\n\n" + instruction
        outputs[Path(f"dist/codex/expert-{slug}.toml")] = toml
        outputs[Path(f"dist/claude/expert-{slug}.md")] = markdown

    assigned = {tag for expert in experts for tag in expert["tags"]}
    groups = sorted({specialties[tag]["group"] for tag in assigned})
    group_links = specialty_group_links(groups)
    outputs[Path("dist/README.md")] = "\n".join([
        "# Ready-to-use expert roles", "",
        "<!-- Generated by src/generate.py; edit source metadata, specialties or the generator. -->", "",
        f"**{len(experts)} experts · two native formats**", "",
        "Choose a host to browse role files alphabetically or by specialty:", "",
        "- [Codex — TOML role files](codex/README.md)",
        "- [Claude Code — Markdown role files](claude/README.md)", "",
        "Each expert has one file per host. Specialty indexes link to these same",
        "files wherever an expert's expertise is relevant; file paths do not depend",
        "on specialty labels or groups.", "",
        "For profiles, perspective cues, suggested uses and references, see the",
        "[full catalogue](../src/roles/README.md). Follow the",
        "[setup guide](../docs/delivery.md#use-a-native-role) for registration and host-validation limits.", "",
        "## Sources and licensing", "",
        "These role files and indexes are generated and committed. Follow the",
        "[source guide](../src/README.md#generate-the-catalogue-and-native-files) to edit sources and regenerate them.",
        "Role files use [MIT](../LICENSE); retain its copyright and permission notice",
        "with copies. Specialty labels retain their",
        "[source credits and terms](../docs/elements/specialties.md#source-attribution).", "",
    ])
    for host, title, extension in (("codex", "Codex", "toml"), ("claude", "Claude Code", "md")):
        outputs[Path(f"dist/{host}/README.md")] = distribution_index(
            experts, specialties, groups, title, extension)
    catalogue = [
        "<!-- Generated by src/generate.py; edit expert.yaml or src/specialties.yaml. -->",
        "[Meet the experts](#meet-the-experts) · [Browse by specialty](#browse-by-specialty)", "",
        f"Jump to a specialty group: {group_links}", "",
        "## Meet the experts", "",
        "Know the name? Use your browser's Find (Cmd+F or Ctrl+F).", "",
        "| Expert | Specialties | Image |",
        "| --- | --- | --- |",
    ]
    for expert in experts:
        slug = expert["slug"]
        profile_path = slug
        name = markdown_text(expert["name"])
        labels = " · ".join(
            f'[{markdown_text(specialties[tag]["name"])}](#specialty-{tag})'
            for tag in expert["tags"]
        )
        if expert["perspective"]:
            labels += "<br><br>Perspective: " + markdown_text(expert["perspective"]) + "."
        image = catalogue_image(expert, profile_path)
        catalogue.append(f"| [{name}]({profile_path}/README.md) | {labels} | {image} |")
    catalogue += ["", "## Browse by specialty", "",
                  "Specialties help match tasks to relevant expertise. An expert may appear",
                  "under several specialties; their publicly documented work defines the",
                  "scope of the role.", "",
                  "To compare overlapping experts, see their perspective cues in",
                  "[Meet the experts](#meet-the-experts) and their profiles' **Suggested uses**.", ""]
    catalogue += specialty_tables(experts, specialties, groups,
                                  lambda expert: f'{expert["slug"]}/README.md')
    catalogue_path = Path("src/roles/README.md")
    outputs[catalogue_path] = update_readme(
        (root / catalogue_path).read_text(encoding="utf-8"), "\n".join(catalogue),
        "CATALOGUE", str(catalogue_path),
    )

    showcase = ["<!-- Generated by src/generate.py; curate FEATURED_EXPERTS there. -->", "<table>"]
    for offset in range(0, len(FEATURED_EXPERTS), 3):
        showcase.append("<tr>")
        for slug, tag in FEATURED_EXPERTS[offset:offset + 3]:
            expert = by_slug[slug]
            profile_path = f"src/roles/{slug}"
            showcase.extend([
                '<td align="center" width="33%">',
                catalogue_image(expert, profile_path) + "<br>",
                f'<a href="{profile_path}/README.md"><strong>{html.escape(expert["name"])}</strong></a><br>',
                html.escape(specialties[tag]["name"]),
                "</td>",
            ])
        showcase.append("</tr>")
    showcase.extend(["</table>", "",
        f"**[Browse all {len(experts)} experts by name or specialty →](src/roles/README.md)**"])
    readme = (root / "README.md").read_text(encoding="utf-8")
    readme = update_readme(readme, f"**{len(experts)} experts · Codex and Claude Code role files**",
                           "SUMMARY", "README.md")
    outputs[Path("README.md")] = update_readme(readme, "\n".join(showcase), "FEATURED", "README.md")
    return outputs


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true", help="Report drift without writing files")
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument("--create-placeholder", metavar="EXPERT_SLUG", help="Create placeholder.svg from one expert's full name")
    args = parser.parse_args(argv)
    try:
        if args.create_placeholder:
            if args.check:
                raise ValueError("--create-placeholder cannot be combined with --check")
            destination = create_placeholder(args.root, args.create_placeholder)
            print(f"Created {destination}; update the profile image and regenerate the catalogue.")
            return 0
        outputs = plan_outputs(args.root)
        existing = (set(args.root.glob("dist/**/*.toml")) | set(args.root.glob("dist/**/*.md"))
                    | set(args.root.glob("src/roles/*/codex/**/*.toml"))
                    | set(args.root.glob("src/roles/*/claude/**/*.md")))
        obsolete = existing - {args.root / path for path in outputs}
        if obsolete:
            raise ValueError("Unexpected role or distribution files require review: " + ", ".join(str(p.relative_to(args.root)) for p in sorted(obsolete)))
        changed = [path for path, text in outputs.items()
                   if not (args.root / path).is_file() or (args.root / path).read_text(encoding="utf-8") != text]
        if args.check:
            if changed:
                print("Generated files need updating:\n" + "\n".join(str(path) for path in changed), file=sys.stderr)
                return 1
            print(f"All {len(outputs)} generated files match their sources.")
        else:
            for path in changed:
                destination = args.root / path
                destination.parent.mkdir(parents=True, exist_ok=True)
                destination.write_text(outputs[path], encoding="utf-8")
            print(f"Updated {len(changed)} generated files; nothing was installed.")
        return 0
    except (ValueError, OSError, yaml.YAMLError) as error:
        print(f"Generation failed: {error}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
