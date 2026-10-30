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
exports. Native files and all three distribution indexes are committed during
release preparation. Between releases they may lag behind canonical sources;
review complete contribution outputs in a separate preview. The main README
and source catalogue are regenerated and committed with source changes, so
their presentation and expert lists stay current without a release.
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
Original name placeholders, their template and original generated contributions
use MIT to the extent rights can be granted. Photographs and adaptations of
licensed references retain their separately credited terms; see the
[license scope](../README.md#license).

```text
VERSION
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
  check_docs.py
  check_changes.py
  release.py
dist/
  README.md
  codex/
    README.md
    expert-<slug>.toml
  claude/
    README.md
    expert-<slug>.md
```

Maintainers use the [release safeguard commands](../docs/delivery.md#release-safeguards)
to check and push an authorized release branch. The helper does not generate
files, merge PRs, tag or publish.

## Role metadata and descriptions

`expert.yaml` requires `name` and `specialties`; `perspective` is optional.
Use it when overlapping specialties leave a useful distinction unclear, and
review neighboring experts together. Keep it a short phrase about a distinctive
emphasis supported by the profile's public references. It should read naturally
after “especially on”. Generic activities such as analysis or feedback belong
in the assignment; execution rules belong in the [shared instruction](templates/invocation.md).

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
full catalogue to help readers compare overlapping experts. Specialty tables
also show existing perspective cues when several experts share a specialty;
single-expert rows stay compact. It is not added to
execution instructions or automatically copied into profile prose. The catalogue
keeps its name, specialty and image columns; all roles retain the shared instruction.

## Export provenance

Every native export carries the same three provenance keys. Exports use a short
title, aligned values and a blank line before the
host settings:

```text
# Expert Roles
# expert_roles.source:  https://github.com/shpoont/expert-roles
# expert_roles.version: 1.3.0
# expert_roles.id:      eliyahu-goldratt

```

`source` identifies the canonical public repository, `version` comes from the
root [VERSION](../VERSION) file, and `id` is the expert directory's stable slug.
Both formats share the whole-library version; individual experts have no
separate version. The example uses v1.3.0; isolated previews use
`0.0.0-preview`. Historical release tags retain their original formatting.

Codex comments appear before the TOML settings. Claude comments appear inside
the YAML frontmatter, after its opening `---`; the closing `---` and instruction
body are unchanged. These are file provenance for people and consuming tools,
not host configuration fields or additions to the description or instructions.
The hosts do not automatically display or act on these comments.
Consumers reading the comments should accept whitespace after each colon;
the key names and their meanings remain unchanged.

Keep `VERSION` as one Semantic Version without a `v` prefix. Contributions leave
it unchanged; temporary previews use `0.0.0-preview` without changing the checkout.
A version comment does not identify an exact snapshot or prove publication.
Consumers still pin a released tag or commit. Maintainers set the intended final
stable version during [release preparation](../docs/delivery.md#versions-and-releases).
Missing or malformed release versions fail before export writes; strict check
mode detects stale or edited provenance. Do not add generation timestamps,
machine paths or Git-dependent values: the same source files must generate the
same exports in an ordinary checkout or a source archive.

## Prepare the Python environment

Use Python 3.11 or newer from the repository root. Prepare an environment if
a suitable one is not already available:

```sh
python -m venv .venv
.venv/bin/python -m pip install -r requirements.txt
```

All examples below use `.venv/bin/python`. If you reuse an environment elsewhere,
substitute its Python executable throughout and ensure it has Python 3.11 or
newer and the dependencies from `requirements.txt`.

For a new expert, finish the starter and [choose the profile image](#choose-the-profile-image)
before validation. For changes to existing profiles or shared behavior, retain
the valid existing images and continue to the contribution checks below. Image
authoring is needed only when adding or changing an image; validation still
checks every completed profile.

## Generate the catalogue and native files

### Contribution checks

With the [Python environment](#prepare-the-python-environment) prepared and
every profile's required image present, refresh the main README's generated
sections and the full source catalogue, then check the contribution from the
repository root:

```sh
.venv/bin/python src/generate.py --docs
.venv/bin/python -m unittest discover -s tests -v
.venv/bin/python src/check_changes.py --base origin/main
```

The boundary check compares your working tree with an ancestor Git ref. Use
`origin/main` when it is an ancestor of your feature branch, or the specific
common base commit. It includes untracked files. In a downloaded source archive,
source validation and previews work without Git; run the boundary check in the
Git checkout used for the PR. It also runs the read-only `--check-docs` gate:
Both generated source views—the marked sections of the main `README.md` and
`src/roles/README.md`—must match the generator. Hand edits inside generated
regions or stale output fail. `--docs` preserves authored prose outside those
regions and never changes VERSION or dist. Running the generator without an
action, or with `--validate`, validates only. Source validation renders
everything in memory, checking all
profiles, images, credits, vocabulary, shared templates and generated syntax.
It does not require retained release artifacts to match current sources.

### Create the review copy

Create a browsable review copy in a **new directory outside the checkout**:

```sh
.venv/bin/python src/generate.py --preview /tmp/expert-roles-review
.venv/bin/python src/check_docs.py --root /tmp/expert-roles-review
```

The preview includes profiles, images, documentation, both native formats and
their indexes. Start with its `README.md` or `src/roles/README.md`; relative links
target the preview's outputs. Its native comments use `0.0.0-preview`, and its
entry points identify it as unreleased. Git metadata, environments and caches
are excluded. An existing destination is rejected; choose a new review directory
for each run. The source checkout and its `VERSION` stay unchanged.

The read-only documentation checker parses Markdown links and images,
reference-style links and embedded HTML. It checks local files, readable raster
and SVG images, heading fragments and explicit anchors inside the preview.
External URLs are not fetched; code examples and HTML comments are ignored.
Only unfilled `{{...}}` targets under `src/templates/` and the profile starter's
not-yet-created `placeholder.svg` are exempt. Completed profiles get no such
exception. Fragments in unsupported file types fail with an explicit diagnostic.
CI runs this check against fresh outputs before attaching the same tree as the
**expert-roles-preview** artifact for seven days. This avoids checking new
contributions against retained files from the previous release.

### View the review copy

The preview is a linked Markdown tree, not a generated HTML website. Open its
folder in a Markdown previewer that supports raw HTML and tables, then preview
`README.md` and follow its links to the catalogue and changed profiles. For
example, in VS Code use **Markdown: Open Preview to the Side**. Check that the
portraits and tables render, and that links stay inside this review copy.

If your previewer cannot render the HTML tables or images, use a compatible
local Markdown renderer; keep any generated HTML outside the checkout. The
[rendered-review guidance](../docs/elements/portraits.md#review-a-rendered-preview)
describes what to inspect and how to record viewing limits. Opening Markdown as
plain text does not establish visual verification.

### Submit a source contribution

Submit canonical sources, the refreshed generated source views, relevant authored
documentation and an **Unreleased** changelog note. Leave `VERSION` and `dist/`
untouched. These views describe current sources; native files for unreleased
additions are available in the preview until the next release. Use a released
tag when you need its complete prepared distribution. Routine expert additions
do not need project-wide decision, status or release records.

### Release preparation

Maintainers prepare committed artifacts in a separate
[release PR](../docs/delivery.md#versions-and-releases). After choosing `VERSION`:

```sh
.venv/bin/python src/generate.py --release
.venv/bin/python src/generate.py --check
```

Release generation reads [VERSION](../VERSION), [specialties.yaml](specialties.yaml), each expert's metadata
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

### Shared instruction behavior

To change behavior shared by every expert, edit
[templates/invocation.md](templates/invocation.md), then use the contribution
checks and review preview above. Retained native files update in a separate
release.

The [shared instruction](templates/invocation.md) accepts clear prose or structured
briefs. It requires professional scope and independent judgment: decline unrelated
work, withhold conclusions that need missing essential information, complete
independent requested parts and challenge forced conclusions. Consequential
assessments must state their scope, evidence and material limits. Keep the user's
objective separate from a proposed solution or the caller's interpretation. For
proposal reviews, briefly state the intended outcome and material distinctions,
including supplied examples; check what the proposal represents, omits or defers.
Explain claimed equivalence and put consequential gaps in the conclusion. An
explicit user-authorized pilot may narrow the assessment; earlier reviews or
a draft cannot authorize that change themselves.
Simplifications must preserve requested distinctions or name concrete losses;
references to earlier positions must follow the available record. Specialty labels
are nonexhaustive guidance. All experts use this one template; profile prose is
not added to their operational instructions. An early scope check applies to
each requested contribution, including mixed requests and follow-ups; unrelated
work stays outside the role while independent in-scope work continues. The
[consultation candidate](../docs/design.md#concise-expert-consultation-instruction)
has structural checks and a limited [Harbor comparison](../tests/harbor/README.md).
Current integration checks exercise the combined instruction; they do not
compare it with the 382-word working draft.
See the [current repair record](../evidence/README.md#goal-coverage-repair-and-application--2026-10-29)
and [earlier findings and limits](../evidence/README.md#shared-instruction-comparison--2026-10-28)
before drawing conclusions about behavioral benefit. Retained release files
update only during a separate release.

### Image requirements

Each profile requires exactly one image: a decodable 512 × 512 RGB JPEG named
`portrait.jpg`, or a 512 × 512 `placeholder.svg` matching the shared template and
expert's name. The exporter validates either image before writing outputs and
rejects a missing image or both files together. Display either at 160 × 160 in
the catalogue and 240 × 240 on profiles. See the exact steps below.
JPEGs may be photographs, original historical depictions or explicitly labeled
AI-generated studio portraits. Keep drawings, paintings and statues unchanged.
Follow the [portrait workflow](../docs/elements/portraits.md) for source selection,
generation, appearance review, provenance and uncertainty. File validation does
not establish likeness or authentic historical appearance.
Photograph and supplied-reference reuse permission requires manual verification under the
[photo policy](../CONTRIBUTING.md#photo-sources-and-licenses); image-format
validation does not establish it. Do not add photos with unclear permission.

### Catalogue generation rules

Keep one ordered `BEGIN GENERATED CATALOGUE` / `END GENERATED CATALOGUE`
HTML-comment pair in `src/roles/README.md`. The main README has separate ordered
`SUMMARY` and `FEATURED` pairs using the same `BEGIN GENERATED` / `END GENERATED`
convention. Regeneration replaces only the content inside those boundaries;
missing, duplicate, reversed, overlapping or nested markers fail before writes.
Specialties are grouped and sorted by name; only assigned entries appear.

The six `(expert slug, specialty ID, task cue)` entries in `FEATURED_EXPERTS`
within `src/generate.py` curate the main README sample for recognition and
breadth. Every selected expert must exist and have the supporting specialty
assigned in canonical metadata. Task cues are short, single-line suggestions
grounded in the profile's public work; they do not enter role instructions.
Names and visuals are read from their sources. The homepage retains image types
in accessible descriptions and one nearby note; the full catalogue retains
accessible image descriptions and links to profile credits without per-image
captions. In previews and release outputs, adding an expert updates the full
catalogue and total without enlarging the sample; changing the showcase is a
separate editorial choice.

### Validation coverage

`--check-docs` is the read-only source-catalogue freshness check used for
contributions. `--check` is the strict release freshness check. It may fail between releases
because retained artifacts intentionally lag behind source changes. This does
not replace source validation or the contribution boundary check above.

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
expert, leave released exports in place in the contribution; maintainers review
and remove obsolete exports in the release change before regenerating. Check
mode also reports missing or edited distribution indexes and native files
without writing them. The [CI workflow](../.github/workflows/checks.yml) always
runs the suite, source validation, a change-boundary check and an isolated preview.
A maintainer's `release` PR label selects strict release validation; ordinary
PRs reject release-owned edits. No CI step commits, publishes or installs roles.
Keep preview directories and temporary archives out of Git.
Catalogue display text is escaped
for Markdown; names and specialty labels retain their original values in native
files. Perspective whitespace is normalized as described above.

## Choose the profile image

Use a suitable photograph with verified reuse permission, an existing historical
depiction or a clearly labeled generated studio portrait following the
[portrait workflow](../docs/elements/portraits.md). Do not generate replacements
for drawings, paintings, statues or similar depictions.
The versioned [portrait prompt](templates/portrait.txt) and [helper](portraits.py)
provide stable individual backgrounds, reference hashes and deterministic JPEG
preparation. Generated portraits require direct eye contact; save run recipes
outside this public repository.
Otherwise use a full-name placeholder; uncertain likeness does not block an accepted expert.
Each profile has exactly one of `portrait.jpg` or `placeholder.svg`. Identify an
existing artwork or statue with **Historical depiction** in its credit section
so both catalogue entries retain that distinction.

### Create a full-name placeholder

After [copying the starter](../CONTRIBUTING.md#adding-an-expert), filling its
metadata and profile, and [preparing Python](#prepare-the-python-environment):

1. Remove the README's authoring comments and replace every `{{...}}` field. Keep
   `src="placeholder.svg"`, the full-name placeholder alt text and the **Image**
   section. The SVG will use the complete name from `expert.yaml`.
2. Replace `your-expert` below with your chosen directory slug, then run:

   ```sh
   .venv/bin/python src/generate.py --create-placeholder your-expert
   .venv/bin/python src/generate.py --validate
   .venv/bin/python src/generate.py --preview /tmp/expert-roles-profile-preview
   .venv/bin/python -m unittest discover -s tests -v
   ```

The first command reads the name from `expert.yaml`, escapes it for XML and
creates only that expert's `placeholder.svg` from the
[shared template](templates/placeholder.svg). It does not overwrite an existing
photo or SVG, generate role files or change other profiles. The following
commands validate sources and generate a separate catalogue/native-file preview.

The command wraps the full name across centered lines and adjusts the type size
to fit. Keep the template's size, colors, typography and accessible title.
The shared style uses a warm paper background, a subtle frame and regular
Georgia type with standard serif fallbacks; it includes no font downloads.
To correct the name, update `expert.yaml` and the README, remove that profile's
`placeholder.svg` and rerun the first command. Review at both display sizes.
The template and generated placeholder artwork use
[MIT](../LICENSE); no third-party photo credit is needed.

### Use a generated studio portrait

Follow the [studio-v1 method](../docs/elements/portraits.md), including permitted
references, the shared prompt, an individual background and visual review.
Prepare the selected master with the portrait helper, then remove the profile's
`placeholder.svg`. Keep exactly one active visual.

Change the existing hero image to `portrait.jpg`, with accessible text
`Full Name — AI-generated portrait` and width/height **240**. Replace only the
profile's **Image** section using the [copyable credit block](templates/portrait-credit/README.md).
Fill every field from the actual recipe and run, including all supplied-reference
credits and terms. Keep this section titled **Image**. Run the generator and
checks above; the same validation runs in CI. Image generation does not remove
applicable source rights or establish copyright in the generated portion.

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
