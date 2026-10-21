# Expert sources and generation

The canonical profiles live in [roles/](roles/README.md). Each
expert's `expert.yaml` is the single source for their name, assigned
specialty IDs and optional perspective; the directory name supplies their
identifier. The profile README
and photo or name placeholder support browsing and are not injected into the operational prompt.
The full [catalogue](roles/README.md) is generated beside the profiles, with
alphabetical and specialty views. The [main README](../README.md#role-catalogue)
shows a fixed six-expert sample and the current total.

Ready-to-use files live under [dist/](../dist/README.md), with one stable file
per expert and host. The [Codex](../dist/codex/README.md) and
[Claude Code](../dist/claude/README.md) indexes provide alphabetical and specialty
navigation from this same metadata. Specialty assignments affect index links,
not file paths; an expert may appear under several specialties without duplicate
exports. Native files and all three distribution indexes are generated and
committed alongside their sources.
Both formats share the [whole-library version](../README.md#versions-and-releases).
Consumers pin a released tag or full commit for reproducible imports.

Specialties help people and AI choose experts for tasks. Their shared labels
and groups currently live in [specialties.yaml](specialties.yaml); expert
metadata references those entries instead of repeating their definitions.
Follow the [specialty rules](../docs/elements/specialties.md#rules) when choosing
terms. The central YAML registry is adopted; each entry requires `name`,
`group` and `reference`. The reference URL identifies the specific external
concept and includes its source ID when available; documented rule-7 exceptions
can use a precise primary-source concept page. New specialties are added to this shared
registry before their canonical IDs are used in expert metadata. Use preferred
terms or recognized aliases; duplicate names and concept references are rejected.

For a new expert, follow [Adding an expert](../CONTRIBUTING.md#adding-an-expert)
to copy the entire [profile starter folder](templates/profile/) and fill both
`README.md` and `expert.yaml` before choosing an image.
Link each profile specialty to `../README.md#specialty-<canonical-id>`.
These catalogue anchors use registry IDs, so label and group changes preserve
the destination. The catalogue also links its labels to those specialty rows.

Original sources and generated role files use [MIT](../LICENSE). Keep its
copyright and permission notice with copies, including standalone exports.
Vocabulary labels retain their [source credits and terms](../docs/elements/specialties.md#source-attribution).
Original name placeholders and their template use MIT. Photographs retain their separately credited licenses; see the
[license scope](../README.md#license).

```text
src/
  README.md
  specialties.yaml
  roles/
    README.md
    <expert>/
      README.md
      expert.yaml
      portrait.jpg OR placeholder.svg
  templates/
    invocation.md
    placeholder.svg
    profile/
      README.md
      expert.yaml
  generate.py
dist/
  README.md
  codex/
    README.md
    expert-<slug>.toml
  claude/
    README.md
    expert-<slug>.md
```

## Role metadata and descriptions

`expert.yaml` requires `name` and `specialties`; `perspective` is optional.
Use it when overlapping specialties leave a useful distinction unclear, and
review neighboring experts together. Keep it a short phrase about a distinctive
emphasis supported by the profile's public references. It should read naturally
after “especially on”. Generic activities such as analysis or feedback belong
in the assignment; execution rules belong in the shared instruction.

For example:

```yaml
name: Don Norman
specialties:
  - human-centered-design
  - cognitive-psychology
  - human-computer-interaction
perspective: >-
  the relationship between people's expectations and a product's conceptual
  models, discoverability, feedback and errors
```

The generated description uses “Consider [name]'s perspective, especially on
[perspective]” when the phrase is present, or “Consider [name]'s perspective
within their documented expertise” otherwise, followed by “Relevant specialties
include [labels].” Both native formats receive exactly the same description.
These cues remain nonexhaustive; the expert's documented work defines scope.
Omit the field when it adds no useful distinction. A supplied value must be
nonempty authored text; folded YAML is accepted, whitespace is normalized and
an optional final period is handled when generating the description. Empty,
non-text and unfilled template values are rejected before outputs are written,
including when creating a placeholder.

The phrase appears in selection metadata and beneath specialty labels in the
full catalogue to help readers compare overlapping experts. It is not added to
execution instructions or automatically copied into profile prose. The catalogue
keeps its name, specialty and image columns; all roles retain the shared instruction.

## Prepare the Python environment

After copying and filling the starter, prepare Python 3.11 or newer from the
repository root:

```sh
python -m venv .venv
.venv/bin/python -m pip install -r requirements.txt
```

Then [choose the profile image](#choose-the-profile-image). Generate the catalogue
and role files after that required image is ready.

## Generate the catalogue and native files

With the [Python environment](#prepare-the-python-environment) prepared and
every profile's required image present, run from the repository root:

```sh
.venv/bin/python src/generate.py
```

The exporter reads [specialties.yaml](specialties.yaml), each expert's metadata
and [the shared instruction](templates/invocation.md). It updates the full
catalogue in `src/roles/README.md`, the summary and featured sections in the
main README, the native files under `dist/codex/` and `dist/claude/`, and all
three `dist` README indexes. Authored text outside the source catalogue and
main README's marked sections is maintained separately; distribution indexes
are generated in full.
It does not install, launch or configure agents, and it does not access the
network.
The profile starter stays under `templates/`; only completed directories under
`roles/` are included in the catalogue and native exports.

The shared instruction requires professional scope and independent judgment:
decline work outside documented expertise, clarify uncertain fit or essential
context, and challenge forced conclusions or suppression of relevant expertise.
Specialty labels are nonexhaustive guidance. All experts use this one template;
profile prose is not added to their operational instructions.

Each profile requires exactly one image: a decodable 512 × 512 RGB JPEG named
`portrait.jpg`, or a 512 × 512 `placeholder.svg` matching the shared template and
expert's name. The exporter validates either image before writing outputs and
rejects a missing image or both files together. Display either at 160 × 160 in
the catalogue and 240 × 240 on profiles. See the exact steps below.
Photograph reuse permission requires manual verification under the
[photo policy](../CONTRIBUTING.md#photo-sources-and-licenses); image-format
validation does not establish it. Do not add photos with unclear permission.

Keep one ordered `BEGIN GENERATED CATALOGUE` / `END GENERATED CATALOGUE`
HTML-comment pair in `src/roles/README.md`. The main README has separate ordered
`SUMMARY` and `FEATURED` pairs using the same `BEGIN GENERATED` / `END GENERATED`
convention. Regeneration replaces only the content inside those boundaries;
missing, duplicate, reversed, overlapping or nested markers fail before writes.
Specialties are grouped and sorted by name; only assigned entries appear.

The six `(expert slug, specialty ID)` pairs in `FEATURED_EXPERTS` within
`src/generate.py` curate the main README sample for breadth of subjects and
perspectives. Every selected expert must exist and have the displayed specialty
assigned in canonical metadata. Names, visuals and labels are read from their
sources. Adding an expert updates the full catalogue and total without enlarging
the sample; changing the showcase is a separate editorial choice.

Check generated content without changing it:

```sh
.venv/bin/python src/generate.py --check
.venv/bin/python -m unittest discover -s tests -v
```

The tests cover invalid source rejection, read-only drift detection, authored
content preservation in both READMEs, marker validation, fixed-size
showcase behavior as the catalogue grows, shared specialties, unused-group hiding,
reference validation, optional perspectives and multiple specialties across both host formats. Source
URLs are kept in the registry and are not injected into role instructions.
They also cover full-name creation and wrapping, mixed image types, invalid/ambiguous SVGs,
XML escaping and preserving native instructions when the visual changes.
All inputs are validated before
output files are written. Unexpected native files are reported for review; the
exporter does not delete them automatically. This includes obsolete exports,
nested duplicate files and copies left in the former
`src/roles/<slug>/codex/` or `claude/` locations. When removing or renaming an
expert, review and remove their obsolete exports in the same change before
regenerating. Check mode also reports missing or edited distribution indexes
and native files without writing them. The
[CI workflow](../.github/workflows/checks.yml) runs the suite and this read-only
consistency check; it does not regenerate or commit changes. Include updated
outputs with source changes, and keep temporary archives/build files out of Git.
Catalogue display text is escaped
for Markdown; names and specialty labels retain their original values in native
files. Perspective whitespace is normalized as described above.

## Choose the profile image

Use a suitable photograph with verified reuse permission when available.
Otherwise use a full-name placeholder; a missing photo does not block an accepted expert.
Each profile has exactly one of `portrait.jpg` or `placeholder.svg`.

### Create a full-name placeholder

After [copying the starter](../CONTRIBUTING.md#adding-an-expert), filling its
metadata and profile, and [preparing Python](#prepare-the-python-environment):

1. Remove the README's authoring comments and replace every `{{...}}` field. Keep
   `src="placeholder.svg"`, the full-name placeholder alt text and the **Image**
   section. The SVG will use the complete name from `expert.yaml`.
2. Replace `your-expert` below with your chosen directory slug, then run:

   ```sh
   .venv/bin/python src/generate.py --create-placeholder your-expert
   .venv/bin/python src/generate.py
   .venv/bin/python src/generate.py --check
   .venv/bin/python -m unittest discover -s tests -v
   ```

The first command reads the name from `expert.yaml`, escapes it for XML and
creates only that expert's `placeholder.svg` from the
[shared template](templates/placeholder.svg). It does not overwrite an existing
photo or SVG, generate role files or change other profiles. The following
commands generate and check the catalogue and native files.

The command wraps the full name across centered lines and adjusts the type size
to fit. Keep the template's size, colors, typography and accessible title.
The shared style uses a warm paper background, a subtle frame and regular
Georgia type with standard serif fallbacks; it includes no font downloads.
To correct the name, update `expert.yaml` and the README, remove that profile's
`placeholder.svg` and rerun the first command. Review at both display sizes.
The template and generated placeholder artwork use
[MIT](../LICENSE); no third-party photo credit is needed.

### Use a photograph instead

Verify permission under the
[photo policy](../CONTRIBUTING.md#photo-sources-and-licenses), then prepare
`portrait.jpg` to the [photo standard](../CONTRIBUTING.md#photo-standard).
Remove the profile's `placeholder.svg` if present. In its README, use:

```html
<img src="portrait.jpg" alt="Portrait of Full Name" width="240" height="240">
```

Replace `Full Name`, and replace the **Image** placeholder section with
**Photo credit**. Include the available title/creator, a **Source** link to the
specific photo's information page, a **License** link to its exact terms,
required notices and earlier edits, and our crop, resize or other changes.
Regenerate and run the checks above. The catalogue selects the supplied file;
photo terms remain separate from MIT. To switch back to a name placeholder, remove
`portrait.jpg`, restore the starter's image markup and **Image** section, then
create `placeholder.svg` and regenerate. Keep historical source findings in the
project records rather than presenting a placeholder as a photograph.

## Native formats

- [Codex custom agents](https://learn.chatgpt.com/docs/agent-configuration/subagents#custom-agents):
  TOML with `name`, `description` and `developer_instructions`.
- [Claude Code subagents](https://code.claude.com/docs/en/sub-agents#write-subagent-files):
  Markdown with YAML `name` / `description` frontmatter and the instruction body.

Both contain the exact same rendered instruction. No host model or capability
overrides are added. These are the initial export formats. Three Codex samples
passed using explicit invocation-only registration; automatic directory
discovery remains unresolved. Claude exports are structurally checked and
runtime-untested. Follow the [usage guidance](../docs/delivery.md#use-a-native-role)
and [checks](../tests/README.md) for the observed method and its limits.
