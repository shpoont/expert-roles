"""Check local links, images and anchors in an isolated documentation preview."""

from __future__ import annotations

import argparse
from dataclasses import dataclass, field
from html.parser import HTMLParser
import os
from pathlib import Path
import sys
import unicodedata
from urllib.parse import unquote, urlsplit
import xml.etree.ElementTree as ET

from markdown_it import MarkdownIt
from PIL import Image
import yaml


DOCUMENT_SUFFIXES = {".md", ".markdown", ".html", ".htm"}
SKIP_DIRECTORIES = {".git", ".venv", "node_modules", "__pycache__"}
MARKDOWN = MarkdownIt("commonmark").enable("table")


@dataclass
class Reference:
    target: str
    line: int
    image: bool = False


@dataclass
class Document:
    anchors: set[str] = field(default_factory=set)
    references: list[Reference] = field(default_factory=list)
    errors: list[tuple[int, str]] = field(default_factory=list)


@dataclass
class Report:
    documents: int = 0
    local_references: int = 0
    images: int = 0
    external_references: int = 0
    template_references: int = 0
    errors: list[str] = field(default_factory=list)


class HTMLReferences(HTMLParser):
    """Read attributes without executing HTML; comments do not contain links."""

    def __init__(self, document: Document, explicit: set[str], line: int = 1):
        super().__init__(convert_charrefs=True)
        self.document, self.explicit, self.line = document, explicit, line

    def handle_starttag(self, tag, attributes):
        line = self.line + self.getpos()[0] - 1
        attrs = dict(attributes)
        anchors = {value for key, value in attributes
                   if value and (key == "id" or (tag == "a" and key == "name"))}
        for anchor in sorted(anchors):
            if anchor in self.explicit:
                self.document.errors.append((line, f"duplicate explicit anchor {anchor!r}"))
            self.explicit.add(anchor)
            self.document.anchors.add(anchor)
        for attribute in ("href", "src"):
            if attribute in attrs and attrs[attribute] is not None:
                self.document.references.append(Reference(
                    attrs[attribute], line, image=tag == "img" and attribute == "src"))

    handle_startendtag = handle_starttag


def without_frontmatter(text: str) -> str:
    """Keep line numbers while excluding valid YAML frontmatter from Markdown."""
    lines = text.splitlines(keepends=True)
    if not lines or lines[0].strip() != "---":
        return text
    for end in range(1, len(lines)):
        if lines[end].strip() == "---":
            try:
                metadata = yaml.safe_load("".join(lines[1:end]))
            except yaml.YAMLError:
                return text
            if isinstance(metadata, dict):
                return "\n" * (end + 1) + "".join(lines[end + 1:])
            return text
    return text


def heading_text(tokens) -> str:
    parts = []
    for token in tokens:
        if token.type in {"text", "code_inline"}:
            parts.append(token.content)
        elif token.type == "image":
            parts.append(heading_text(token.children or []))
        elif token.type in {"softbreak", "hardbreak"}:
            parts.append(" ")
    return "".join(parts)


def heading_slug(text: str) -> str:
    # GitHub's section-link rules: discard markup/punctuation, lowercase and
    # replace spaces with hyphens. Keep Unicode letters, marks and numbers.
    # https://docs.github.com/en/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax#section-links
    return "".join(character for character in text.strip().lower()
                   if character in " _-" or unicodedata.category(character)[0] in "LMN").replace(" ", "-")


def parse_document(path: Path) -> Document:
    text = path.read_text(encoding="utf-8")
    document, explicit = Document(), set()
    if path.suffix.lower() in {".html", ".htm"}:
        HTMLReferences(document, explicit).feed(text)
        return document

    tokens = MARKDOWN.parse(without_frontmatter(text))
    headings = set()
    for index, token in enumerate(tokens):
        line = token.map[0] + 1 if token.map else 1
        if token.type == "heading_open":
            slug = heading_slug(heading_text(tokens[index + 1].children or []))
            anchor, suffix = slug, 0
            while anchor in headings:
                suffix += 1
                anchor = f"{slug}-{suffix}"
            headings.add(anchor)
            document.anchors.add(anchor)
        elif token.type == "html_block":
            HTMLReferences(document, explicit, line).feed(token.content)
        elif token.type == "inline":
            child_line = line
            for child in token.children or []:
                if child.type == "link_open":
                    document.references.append(Reference(child.attrGet("href") or "", child_line))
                elif child.type == "image":
                    document.references.append(Reference(child.attrGet("src") or "", child_line, image=True))
                elif child.type == "html_inline":
                    HTMLReferences(document, explicit, child_line).feed(child.content)
                child_line += 1 if child.type in {"softbreak", "hardbreak"} else child.content.count("\n")
    return document


def svg_anchors(path: Path) -> set[str]:
    root = ET.parse(path).getroot()
    if root.tag not in {"svg", "{http://www.w3.org/2000/svg}svg"}:
        raise ValueError("document is not an SVG image")
    return {node.attrib["id"] for node in root.iter() if "id" in node.attrib}


def check_docs(root: Path) -> Report:
    root = root.resolve()
    if not root.is_dir():
        raise ValueError("--root must be an existing documentation preview directory")
    report = Report()
    documents: dict[Path, Document | None] = {}
    images: dict[Path, str | None] = {}
    svg: dict[Path, set[str]] = {}

    def error(path, line, message):
        report.errors.append(f"{path.relative_to(root).as_posix()}:{line}: {message}")

    def document(path):
        if path not in documents:
            try:
                documents[path] = parse_document(path)
            except (OSError, UnicodeError) as exc:
                documents[path] = None
                error(path, 1, f"cannot read document: {exc}")
            if documents[path] is not None:
                for line, message in documents[path].errors:
                    error(path, line, message)
        return documents[path]

    paths = []
    for directory, children, filenames in os.walk(root, followlinks=False):
        children[:] = sorted(name for name in children if name not in SKIP_DIRECTORIES
                             and not (Path(directory) / name).is_symlink())
        for name in sorted(filenames):
            path = Path(directory) / name
            if path.suffix.lower() in DOCUMENT_SUFFIXES:
                try:
                    resolved = path.resolve()
                except (OSError, RuntimeError) as exc:
                    error(path, 1, f"cannot resolve document: {exc}")
                    continue
                if not resolved.is_relative_to(root):
                    error(path, 1, "document symlink escapes preview root")
                else:
                    paths.append(path)
    report.documents = len(paths)
    if not paths:
        error(root, 1, "no Markdown or HTML documents found")
    for path in sorted(paths):
        parsed = document(path)
        if parsed is None:
            continue
        for reference in parsed.references:
            try:
                url = urlsplit(reference.target)
            except ValueError as exc:
                error(path, reference.line, f"invalid target {reference.target!r}: {exc}")
                continue
            if url.scheme or url.netloc:
                report.external_references += 1
                continue
            relative = path.relative_to(root).as_posix()
            decoded = unquote(reference.target)
            if relative.startswith("src/templates/") and "{{" in decoded and "}}" in decoded:
                report.template_references += 1
                continue
            if (relative == "src/templates/profile/README.md" and reference.image
                    and unquote(url.path) == "placeholder.svg" and not url.fragment
                    and not (path.parent / "placeholder.svg").exists()):
                report.template_references += 1
                continue
            report.local_references += 1
            local = unquote(url.path)
            if local.startswith("/"):
                target = root / local.lstrip("/")
            else:
                target = path.parent / local if local else path
            try:
                target = target.resolve()
            except (OSError, RuntimeError) as exc:
                error(path, reference.line, f"cannot resolve target {reference.target!r}: {exc}")
                continue
            if not target.is_relative_to(root):
                error(path, reference.line, f"target escapes preview root: {reference.target!r}")
                continue
            if not target.exists():
                error(path, reference.line, f"missing target {reference.target!r}")
                continue
            if reference.image:
                report.images += 1
                if target not in images:
                    try:
                        if target.suffix.lower() == ".svg":
                            svg[target] = svg_anchors(target)
                        else:
                            with Image.open(target) as image:
                                image.verify()
                            # JPEG verify() does not decode pixels; reopen to
                            # catch truncated or otherwise unreadable data too.
                            with Image.open(target) as image:
                                image.load()
                        images[target] = None
                    except (OSError, ValueError, ET.ParseError) as exc:
                        images[target] = f"unreadable image: {exc}"
                if images[target] is not None:
                    error(path, reference.line, f"{images[target]} ({reference.target!r})")
                    continue
            if not url.fragment:
                continue
            if target.is_dir():
                target = next((target / name for name in ("README.md", "README.markdown", "index.html")
                               if (target / name).is_file()), target)
                target = target.resolve()
                if not target.is_relative_to(root):
                    error(path, reference.line, f"target escapes preview root: {reference.target!r}")
                    continue
            try:
                if target.suffix.lower() in DOCUMENT_SUFFIXES and target.is_file():
                    destination = document(target)
                    if destination is None:
                        continue
                    anchors = destination.anchors
                elif target.suffix.lower() == ".svg" and target.is_file():
                    if target not in svg:
                        svg[target] = svg_anchors(target)
                    anchors = svg[target]
                else:
                    error(path, reference.line, f"cannot check fragment in target {reference.target!r}")
                    continue
            except (OSError, ValueError, ET.ParseError) as exc:
                error(path, reference.line, f"cannot read anchor target {reference.target!r}: {exc}")
                continue
            if unquote(url.fragment) not in anchors:
                error(path, reference.line, f"missing anchor {url.fragment!r} in {reference.target!r}")
    return report


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, required=True, help="generated preview directory")
    arguments = parser.parse_args(argv)
    try:
        report = check_docs(arguments.root)
    except (OSError, ValueError, RuntimeError) as exc:
        print(f"Documentation check failed: {exc}", file=sys.stderr)
        return 1
    if report.errors:
        print("\n".join(report.errors), file=sys.stderr)
        print(f"Documentation check failed: {len(report.errors)} error(s).", file=sys.stderr)
        return 1
    print(f"Checked {report.documents} documents, {report.local_references} local references "
          f"and {report.images} image references; no errors. "
          f"Skipped {report.external_references} external and "
          f"{report.template_references} unfilled starter references.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
