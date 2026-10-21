# Design and approach

## Approach and important parts

Follow the [project agreement](../PROJECT.md). Each expert has one directory
under [src/roles/](../src/roles/README.md). The README presents the person to
readers; `expert.yaml` holds the name, specialty identifiers and optional
perspective phrase for generated selection descriptions. Profile prose,
source links and photos do not become hidden additions to the agent prompt.

The full catalogue is generated inside a marked section of
[src/roles/README.md](../src/roles/README.md), with alphabetical and specialty
views. The [main README](../README.md#role-catalogue) contains a fixed six-expert
showcase and a generated total. D034's curated sample uses existing names,
visuals and assigned labels; it illustrates breadth as the collection grows.
The exporter preserves authored text outside the three separate marker pairs.

[src/specialties.yaml](../src/specialties.yaml) holds the adopted shared
vocabulary with broad navigation groups and external concept references. Specialties help people and AI
match tasks to experts and provide consistent catalogue terminology. The
[specialty record](elements/specialties.md) defines the rules and assesses
storage options; D015 adopts YAML with `name`, `group` and `reference` fields.
Experts may have multiple specialties. Generic activities such as reviewing,
planning and implementation are supplied with each assignment.

[src/templates/invocation.md](../src/templates/invocation.md) is the only authored
operational instruction. A small exporter combines it with each expert's name
and specialty labels to create native Codex TOML and Claude Code Markdown.
The optional perspective contributes to their shared generated description and
appears beneath specialty labels in the full catalogue for human comparison,
as described in the [metadata guide](../src/README.md#role-metadata-and-descriptions).
The portable files are versioned outputs. D043 records owner acceptance and
authorization to commit the reviewed initial catalogue. D044 moves the unchanged
native files to `dist/codex/` and `dist/claude/` and generates alphabetical and
specialty indexes there. File paths depend only on host and expert slug;
classification changes affect index links. Integrations own their
installation, model configuration and lifecycle.

## Implementation contract

### Versioning and first release

Under D045, finish whole-library versioning using the existing peer convention:
`MAJOR.MINOR.PATCH`, a dated changelog, an annotated immutable Git tag and a
matching GitHub release. Adopt `v1.0.0` as the first stable baseline for profiles,
metadata, shared instructions, templates, tooling and both native formats.
The consuming plugin keeps its own version history. Keep policy in the main
README and delivery guide, changes in the changelog and decisions in the
[decision log](decisions.md); no separate version file or per-expert versions are needed.

Define compatibility around stable expert identifiers, documented source/native
formats and export paths, and the intended scope and execution behavior of
existing roles. Compatible expert or specialty additions are minor changes;
corrections preserving intended behavior are patches. A stable release does
not expand the recorded host validation or prove role effectiveness.

Finalize the dated first-release changelog and current version/status references.
Preserve all accepted expert content and the completed D044 distribution work.
Run the full suite, generated/native consistency, local links, public suitability,
preservation and Git checks. The owner explicitly authorizes staging and signing
the complete pending tree, pushing it, then publishing the first release.
This supersedes D044's no-commit/no-release boundary for this delivery.

After pushing the signed commit, require successful hosted checks for that exact
commit before tagging. Create and verify an annotated `v1.0.0` tag on it, push
the tag, and create the matching public GitHub release as Latest. Use GitHub's
tagged source archives, matching the peer releases; additional host-specific
packages are not part of this step. Verify the remote branch, tag target,
release state and notes, and clean local tree before reporting completion.
Keep local preparation evidence separate from actual publication results.
No host installation, invocation or consuming-integration change is included.

### Distribution layout and generated indexes

Under D044, keep canonical profiles, metadata, visuals, specialty vocabulary
and templates under `src/`. Move each unchanged native export to exactly one
stable path: `dist/codex/expert-<slug>.toml` or
`dist/claude/expert-<slug>.md`. Remove the former per-profile export copies and
update profile, starter and usage links. Specialty or group changes must not
change export paths or require a primary specialty.

Generate `dist/README.md` as the host chooser and one complete `README.md` per
host, with alphabetical role links and specialty tables grouped from the same
registry and assignments as the source catalogue. An expert may appear in
several index rows while retaining one file per host. Include links to the
source profiles, setup guidance and license notices. Keep the existing compact
main README, full source catalogue and native file bytes intact apart from
authored navigation links.

Treat exports and distribution indexes as committed, deterministic outputs:
edit sources, regenerate and include both in changes. Extend read-only check
mode and regression tests to cover missing or stale indexes/exports, obsolete
or duplicate native files in either layout, multi-specialty navigation, stable
paths and invalid-input rejection before writes. Add a read-only CI workflow
that runs the suite and generation consistency check. Temporary release
archives and build/cache files stay untracked.

Verify all 114 moved exports byte-for-byte against the committed baseline;
preserve metadata, images, shared instructions, specialty assignments and
profile prose/credits. Run the full suite, consistency, native syntax/equality,
local-link and public-content checks, then inspect the complete diff. Record
results and current status. Leave work unstaged and uncommitted; no runtime
invocation, deployment, consumer changes, push, tag or release is included.
Versioning and the first release remain a separate pending step.

### First-time and returning-visitor journey review

Under D042, use independent subagent feedback to review first-time and returning
visitor journeys through the existing repository: understanding the catalogue,
choosing and comparing experts, finding a known expert again, obtaining a native
file, understanding setup and discovering how to contribute or see changes.
Capture fresh local Markdown renderings and distinguish expert walkthroughs
from real user research and hosted GitHub behavior.

Apply concrete improvements supported by the journeys, using the existing
Markdown structure and visual style. Keep the main README short with its six
featured examples, the complete catalogue under src/roles, the broad scope,
accepted expert roster, profile format, source vocabulary, images and licenses.
Preserve the shared role instruction and native export semantics. Catalogue
navigation or generation may change where required, with relevant regression
checks; avoid building a separate application or adding deployment tooling.

Re-review the changed journeys with subagents, run an independent final review
and appropriate source, generated/native, image, navigation, public-content,
preservation and Git checks. Update current status and record findings, applied
changes, observed results and material limits. Keep all work local, unstaged
and uncommitted; no runtime invocation, installation, publication, push, tag or
release is authorized. This review reopens only the user-facing experience
covered here; unrelated historical decisions and content remain unchanged.

### Final documentation closeout for the accepted catalogue

Under D041, record the owner's acceptance of the rendered fifty-seven-expert
catalogue and complete the requested documentation closeout and final checks.
Replace stale current-phase instructions and pending-review wording with
completed status. Refresh delivery and handover summaries to reference the
current catalogue, acceptance and evidence. Keep historical decision and
evidence entries intact, with the latest record establishing current status.

Preserve all fifty-seven expert directories, the eighty-two-entry specialty
registry, shared instructions, templates, code, tests, requirements, license,
compact main README and complete generated catalogue. Change only current
project guidance and the linked design, decision, check, changelog and evidence
records. No new profiles, image work, vocabulary, runtime invocation or
integration change is included.

Run the existing test suite and generated/native consistency, image, local-link,
UTF-8, bounded public-content, preservation and complete Git-inventory checks.
Record observed results and separate later host/runtime/effectiveness work
from commit readiness. Keep all work local, unstaged and uncommitted; no push,
publication, tag or release is authorized.

### Seven philosophy additions

Under D040, add the owner's selected Socrates, Aristotle, Epictetus, Immanuel
Kant, John Stuart Mill, Confucius and Karl Popper. Apply the adopted criteria
and concise profile format. Ground their suggested uses and distinguishing
perspectives in documented work; distinguish historical sources and later
interpretations where material, especially for Socrates and Confucius.

Reuse canonical specialties and add accurate source-mapped concepts under a
Philosophy navigation group. Keep all existing specialty meanings and the
other fifty expert directories. Preserve the shared instruction, templates,
generator, tests, license, authored main README and fixed six-expert sample.

Use suitable credited portraits with verified reuse permission after bounded
source searches, or the approved full-name placeholders. Identify ancient
busts and later artistic depictions accurately without claiming an
authenticated lifetime likeness. Retain source, creator, permission and edits.
Regenerate both native formats and catalogue entry points; update current
totals and connected records. Run the existing suite plus generated/native
consistency, image, link, UTF-8, public-content, preservation and Git checks.
Render and inspect the seven profiles and full catalogue. Keep all work local,
unstaged and uncommitted; no runtime invocation, installation, integration
change, publication, tag or release is included.

### Ten expert additions and Rybka removal

Under D039, add Dave Ulrich, Amy Edmondson, Marty Cagan, Mark Roberge,
Benjamin Gomes-Casseres, Bill Price, Patricia Dechow, Jeanne Ross, Hau Lee
and Kenneth A. Adams. Apply the adopted criteria, concise profiles and shared
instruction. Ground specialties, suggested uses and distinguishing perspective
cues in their documented work. Reuse canonical concepts and add accurate,
source-mapped specialties only where needed. Keep the broad catalogue scope.

Remove Zdeněk Rybka's profile directory and both exports from the current
collection, as selected by the owner. Retain historical decisions and evidence
of his earlier inclusion. Preserve the other forty expert directories, existing
vocabulary definitions, shared templates, code, tests, license, authored main
README and fixed six-expert sample.

Use suitable portraits with verified reuse permission where available after
bounded source searches; otherwise use the approved full-name placeholders.
Credit each photo's source, creator, terms and edits. Regenerate both native
formats and catalogue entry points; update current totals and connected records.
Run the existing suite, generated and native consistency, image, local-link,
UTF-8, public-content, preservation and Git checks. Render and inspect the new
profiles and catalogue. Keep work local, unstaged and uncommitted; no runtime
invocation, deployment, integration change, publication, tag or release is included.

### Broad catalogue scope clarification

Under D038, describe the project as a broad expert catalogue. Simplify current
scope wording and the D038 records without enumerating fields. Retain the
adopted criteria and existing research. Supersede deferral recommendations based
on the earlier narrow interpretation and assess useful coverage and actual
overlap across the whole catalogue. No roster change is included.

Update current scope, contribution and handover guidance, and append the
clarification to decision and evidence records without rewriting history.
Preserve all experts, source metadata, visuals, generated files, code, tests
and both README entry points. Check generated consistency, local links, UTF-8,
public suitability, preservation and the full proposed diff. Reuse passing
code tests while their inputs remain unchanged. Keep work local, unstaged
and uncommitted; no addition, removal, invocation, integration change or
publication is included.

### Selection criteria and company coverage review

Under D037, implement the owner's accepted distinction between the person's
expertise, the suitability of their AI perspective and their contribution to
the collection. Keep the short expert definition and concise contribution
process. Clarify evidence quality, accessible methods, task fit and scope,
complementary perspectives and the separate evidence needed for role benefit.
Formal credentials remain optional and public familiarity remains a selection
cue. Do not require detailed per-expert briefs or change the source schema.

Use the main functions of a general company as a coverage checklist for
candidate research. Treat the checklist as a coverage lens, preserving the
specialty registry's meaning and organization. Map current strengths and gaps,
research candidates through public primary sources, and propose people who
could be deferred from a smaller initial company-focused selection with the
reason and resulting trade-off. New candidates and possible deferrals remain
proposals; this step changes no expert roster, profile, image or native export.

Update connected criteria, current-work, decision and evidence records. Check
generated consistency, local links, UTF-8, public suitability, Git whitespace,
source preservation and the complete proposed diff, including untracked files.
Reuse existing code tests while code, tests and generated sources are unchanged.
Keep all work local, unstaged and uncommitted. No role invocation, deployment,
integration change, publication, tag or release is included.

### Hawkins, Premack, Levels and Frawley additions

Under D036, assess and add the owner's requested Jeff Hawkins, David Premack,
Pieter Levels and Ed Frawley using the established expert definition. Ground
their profiles in documented research, creations or professional practice and
accessible public work. Describe Hawkins's brain-inspired AI, Premack's
comparative cognition and reinforcement research, Levels's bootstrapped internet
businesses and Frawley's dog-training practice without extending those scopes
to adjacent expertise or treating their prescriptions as settled evidence.

Reuse accurate specialties and add only missing, source-mapped concepts. Add
Animal behavior as a navigation group for Dog training; keep Comparative
psychology under Psychology and Computational neuroscience under Computing,
alongside related task perspectives. Preserve every earlier registry entry.
Use the simplified profiles and optional perspective cues where useful for
overlapping experts. Each expert receives a permitted, credited 512 × 512 RGB
JPEG or the standard full-name placeholder. Preserve permission terms and edits.

Regenerate both native formats and both catalogue entry points, preserving the
fixed six-expert showcase, authored main README, all earlier expert directories,
shared templates, generator, tests and historical records. Update current totals
and connected records. Run the existing suite and generated consistency, native
syntax/equality, image, local-link, public-content, preservation and Git checks.
Render and inspect the new profiles and catalogue. Keep all work local,
unstaged and uncommitted; no runtime invocation, installation, integration
change, publication, tag or release is included.

### Jordan Peterson addition

Under D035, add the owner's requested Jordan Peterson profile using the existing
expert criteria and simplified layout. Ground his fit and suggested uses in
published personality research and accessible books and teaching. Add the
precise Personality psychology concept under Psychology, preserving all earlier
specialty entries and groups. Use a permitted, credited 512 × 512 RGB JPEG or
the standard full-name placeholder; retain source, terms and image edits.
Generate both native files and refresh both catalogue entry points without
changing the fixed six-expert sample or shared instruction. Update current
totals and records. Run the existing suite, generated consistency, native
syntax/equality, local links, image, public-content, preservation and Git checks;
refresh the local preview. Keep earlier expert directories and authored README
text unchanged. Keep all work local, unstaged and uncommitted; this addition
does not include role invocation, installation, integration work or publication.

### Compact README and separate full catalogue

Under D034, apply the owner's section-by-section README review. Keep a short
introduction, usage guidance with optional explicit expert requests, a fixed
six-expert showcase, the expert definition under “Who is included?”, concise
contribution and project-documentation links, license scope and a disclaimer.
Feature Chip Huyen, Martin Fowler, Don Norman, Eliyahu Goldratt, Philip Kotler
and Aswath Damodaran in two rows, using their existing visuals and one assigned
specialty each. The sample illustrates breadth and remains fixed as the library
grows. Move the complete alphabetical and specialty tables into
`src/roles/README.md`; link there from the main README and profiles.

Keep generation deterministic. Validate the curated showcase against canonical
metadata and generate both README counts and visuals alongside the full
catalogue and existing native files. Preserve authored content outside each
ordered generated-marker pair; reject invalid sources or boundaries before
writing any output. Update affected navigation, the starter and contributor
guidance, and move the release procedure into delivery documentation. Retain
historical decisions, contracts and evidence, while updating current records.

Preserve every expert identity, metadata record, specialty assignment, image,
credit, shared execution instruction and native export. Check meaningful
catalogue growth, generated-section preservation and read-only drift/error
cases, run the existing suite and consistency check, and verify native equality,
local links, UTF-8, public suitability, preservation hashes and Git whitespace.
Render the updated Markdown, verify the six-card layout and catalogue links,
and show the main README in Safari. Keep changes unstaged and uncommitted;
this work includes no role invocation, deployment, integration change, push,
publication, tag or release. Report rendered verification separately from
subsequent owner acceptance.

The owner's follow-up review requests a natural-language example without
assuming shared mention syntax, removal of the exporter aside and the same
License/Disclaimer order as other public projects. Check both hosts' official
invocation guidance; keep host-specific syntax in delivery documentation.
Preserve the existing License-then-Disclaimer order if confirmed by those
projects. Check links, UTF-8, public suitability, generated consistency and the
documentation diff, refresh the preview and confirm unchanged role sources,
exports, HEAD and empty index. Reuse the passing code tests while code is unchanged.

### Initial catalogue documentation closeout

The owner accepted the current rendered thirty-six-expert catalogue and
requested documentation closeout before a separate README improvement review.
Under D033, record the completed implementation, accepted current presentation
and existing validation in current guidance, status and handover records. Make
README review the next action, with its proposed changes still to be discussed.

Preserve the entire README, expert directories, vocabulary, templates, native
exports, generator, tests, license and historical records. Reuse the completed
source and runtime observations while their protected files remain unchanged.
Check generated consistency, local links, UTF-8, public suitability, preservation
hashes and Git whitespace; confirm an empty index and unchanged HEAD. Keep all
work local and uncommitted. This step includes no README edits, new role work,
runtime tests, integration changes, publication, tag or release.

### Zdeněk Rybka addition

The owner accepted the preceding assessment and requested adding Zdeněk Rybka
(1927–2022), the management author, without committing. Under D032, add a short
sourced profile, reuse Operations management and distinguish his interpretation
of the Bata management system through the existing optional perspective field.
Use the standard full-name placeholder unless a suitable permitted photo is
verified. Regenerate both native formats and the main catalogue; update current
totals and connected records. Preserve the thirty-five earlier expert
directories, specialty registry, templates, code, tests and historical records.
Run the existing suite, generated consistency, native syntax/equality, local
links, image, public-content, preservation and Git checks; review the rendered
profile and catalogue. Keep all changes local, unstaged and uncommitted. No
runtime invocation, integration change, publication, tag or release is included.

### Four requested expert additions

The owner requested Tomáš Baťa, Milan Zelený, Steve Jobs and Nicole Forsgren,
conditional on the existing expert definition and catalogue fit. Assess their
documented contributions, accessible public work and useful task perspectives
under D031. Add qualifying experts using the existing simplified profile,
canonical metadata, optional perspective and both generated native formats.
Keep everything local, unstaged and uncommitted.

Reuse accurate specialty entries. Add only the missing sourced concepts:
DevOps under Computing, Product design under Design and Multiple-criteria
decision analysis under Management. Keep the registry schema and eight groups.
Use credited, permitted 512 × 512 RGB JPEGs for Zelený and Jobs, prepared by
deterministic cropping and resizing. Use full-name placeholders for Baťa and
Forsgren where the bounded source review does not establish suitable permission.
Record actual image sources, terms and preparation in the profiles.

Regenerate the catalogue and native exports, update current totals and record
selection and image findings. Preserve all thirty-one existing expert
directories, shared templates, generator code, tests and historical records.
Run the existing suite, generated consistency, native syntax/equality, image
and source review, local-link, UTF-8, public-content, preservation and Git checks.
Review the four visuals and rendered catalogue. No runtime invocation,
deployment work, publication, commit, tag or release is authorized by this step.

### Documentation cleanup and final checks

The owner authorized cleaning the current documentation, aligning usage with
observed host behavior and checking the complete proposed initial catalogue
commit, without committing. Present the thirty-one completed profiles and
current native files as the initial catalogue and exports. Mark Claude runtime
use as untested and keep the limited Codex result distinct from automatic
directory discovery and comparative effectiveness.

Update current entry points, project guidance, contribution wording and handover
records. Keep historical decisions and evidence intact; earlier contracts below
record their original scope and superseded constraints. Explain obtaining and
registering an export, the exact named-agent request and the separate plugin's
deployment responsibility. Use the tested Codex registration fields and link
upstream host documentation. Do not present copying a Codex file into an agent
directory as a verified setup path.

Preserve the generated catalogue section, every profile, metadata record,
specialty assignment, visual, shared template and native export, plus generator
code and tests. Run the full existing test suite, generated consistency, native
syntax/equality, local-link, UTF-8, public-content and Git checks. Review the full
proposed file inventory and diff, including untracked content, and retain the
existing portrait provenance and license conditions. Record results and limits
in evidence and current work. Do not add experts, runtime tests, deployment
tooling, CI, commits, publication or a release in this step.

### Initial four-profile prototype

The owner authorized trying this layout and explicitly requested no commit.

- Create profiles for Don Norman, Alan Cooper, Jakob Nielsen and Eliyahu Goldratt.
- Keep profiles and generated native files under `src/roles/`, the specialty
  vocabulary at `src/specialties.yaml` and the shared template under
  `src/templates/`. Update generator paths, test fixtures and relative links;
  verify generated consistency and keep one canonical copy of each source.
- Keep one canonical name/specialty record per person. The directory slug is the
  stable expert identifier; native names use an `expert-` prefix.
- Provide a short, sourced introduction, required credited photo, provisional
  specialty links, example tasks and links to both native role files.
- Use exactly one shared instruction template. No per-person method checklists,
  biographies or profile examples are injected into the operational instruction.
- Render native files and the browsable catalogue deterministically from their
  sources. Reject invalid metadata and unknown specialty identifiers.
- Check native syntax, generated-file consistency, catalogue coverage, local
  navigation, image identity/provenance, public suitability and Git whitespace.
- Leave all work uncommitted. Do not install or invoke the exported roles, alter
  integrations, tag or release. Follow the MIT license adoption below.

### Shared instruction and professional scope

Apply the owner's accepted wording refinement and requirement for realistic
professional scope and independent judgment. The one shared instruction must
check assignment fit, decline work outside documented expertise, separate
relevant parts of mixed requests and mark the rest as out of scope, without
referral or next-step advice for those parts. Seek clarification when essential
context or fit is unclear while addressing clear, independent in-scope parts.
Treat specialty labels as useful, nonexhaustive
guidance. Challenge unsupported premises, forced conclusions and suppression
of relevant expert judgment while respecting legitimate constraints and
contrary evidence. Adopt the expert's professional role, replacing the blanket
impersonation prohibition with precise authorship and attribution limits:
generated responses must not be presented as the real person's statements;
biographical facts, personal experiences, quotations and endorsements must not
be fabricated.

Align discovery descriptions and current scope guidance, then regenerate both
native formats for all thirty-one experts. Preserve profile text, metadata,
specialty definitions, all images, native schemas and shared-template ownership.
Run existing generation tests, check all outputs and local links, and review
the complete proposed diff and public files. Record behavioral scenarios as
future checks; structural checks do not establish actual refusal or challenge
behavior. No live role launch, installation, integration, publication or commit
is authorized. Keep all work unstaged and uncommitted.

### Expert perspectives and selection descriptions

Add an optional `perspective` phrase to `expert.yaml` where shared specialties
leave a useful distinction implicit. Review neighboring experts together and
ground each phrase in the public work already linked from its profile. Describe
the distinctive emphasis, rather than generic activities or a separate workflow.
Keep specialties and perspective cues nonexhaustive; they do not replace the
expert's documented expertise or the assignment.

Generate one description from name, specialty labels and the optional phrase,
then reuse it verbatim in Codex and Claude. Profiles without the field retain
a description based on name and specialties. Accept wrapped YAML text, normalize
whitespace for the description and reject empty, malformed or unfilled optional
values before writing outputs. Show the optional field in the starter and keep
the short contribution guide, source schema and selection guidance consistent.

Check optional-field omission and inclusion, both hosts' matching descriptions,
escaping, invalid-input atomicity and generated drift. Preserve the shared
instruction and all rendered execution instructions, profile READMEs, names,
specialty assignments, registry and images. Review the descriptions together,
check local links, public suitability and the diff, and record observed results.
No live role selection test, installation, integration change or commit is
authorized; actual selection reliability remains unverified.

The accepted Holtzblatt review follow-up adds design to her existing contextual
research and product-requirements emphasis. Change only her perspective source
and regenerate the two native descriptions. Verify the exact wording, matching
hosts, preserved execution instructions and unchanged unrelated outputs; use
the exporter consistency check and retain the uncommitted boundary.

### Codex host validation

The owner authorized a small live Codex check after reviewing the shared
instruction and selection descriptions. This supersedes earlier no-launch
constraints only for this bounded check. A separate plugin will own deployment
and management; this library will not gain installation or lifecycle tooling.

Use the existing signed-in Codex CLI and a fresh, temporary project containing
byte-identical copies of all thirty-one generated Codex files and the MIT
notice. Leave personal agent files and consumer integrations untouched. Capture
the host version, source hashes, prompts, actual agent types and returned
answers in private working evidence. Test three cases, each in a fresh session:

1. Select a suitable expert from the available descriptions for an interface
   heuristic review, without naming an expert in the request. Check the actual
   delegated role and whether its response addresses the supplied interface.
2. Explicitly request Goldratt for an operations-capacity problem containing a
   forced conclusion. Check the named role runs, identifies the limiting step
   from the evidence and challenges the unsupported premise.
3. Explicitly request Norman for an astrophysics calculation. Check the named
   role declines the out-of-expertise task without supplying the calculation,
   recommending another expert or giving next-step advice for it.

Do not alter exported instructions to help them pass. Record failures and
limits as well as successes; a loaded role and one sampled response do not
establish reliable selection or improved judgment. Remove the temporary agent
placement afterward, verify preservation of source files and personal agent
files, check generation consistency and documentation links, and leave the
repository unstaged and uncommitted. Claude, persistent deployment, broader
behavioral coverage and comparative effectiveness remain outside this check.

The initial attempt stopped at discovery: the requested catalogue role was not exposed
in the tested CLI sessions, and a substituted pre-existing role cannot validate
these exports. See the [observations and limits](../evidence/README.md#codex-host-validation--2026-10-20).

The owner requested a further `codex exec` attempt. For the retry, use the
documented `agents.<name>.description` and `agents.<name>.config_file` command
overrides to register the unchanged temporary copies for that invocation only.
Keep the same three assignments and prohibit substituting existing role aliases.
Inspect native calls and returned answers. This tests explicit registration and
execution separately from the unresolved automatic directory discovery; it does
not authorize a persistent registry, installer or plugin change. Retain failures,
remove the disposable project and verify the same preservation boundaries.
The retry completed all three cases with the expected native agent types and
sampled behavior; see the [retry observations](../evidence/README.md#codex-exec-retry--2026-10-20).

### Placeholder visual refinement

Refine the shared full-name tile with a warm paper background, a subtle inset
frame and regular Georgia serif type with standard serif fallbacks. Apply the
same design to all six existing placeholders and retain complete names,
automatic wrapping, the accessible title and 512 × 512 SVG format. Do not add
font downloads, per-expert styles or new metadata. Keep the existing 160- and
240-pixel display sizes and image-creation command.

Render and inspect all six names at both display sizes, including longer-name
examples. Run the existing tests and generated consistency check; verify local
links, public suitability and preservation of photographs, profile text,
metadata, specialties and native roles. Prepare a preview for owner review.
Leave everything unstaged and uncommitted.

### Review follow-up

Apply the accepted review recommendations within the existing prototype:

- Clarify the shared instruction and discovery description so specialties guide
  the perspective while the task determines its focus. Regenerate both hosts.
- Lead the root README with the catalogue and usage; maintain the expert roster
  only in the generated catalogue.
- Use a fixed three-column catalogue with one expert per row. Escape display
  text in Markdown tables and links, retaining original values in native files.
- Put the invalid profile after a valid profile in the no-partial-write test;
  add one independent test for Goldratt's identity and both specialty labels.
- Document obtaining, placing and explicitly requesting a native role in one
  central usage section, linked from profiles. Check host instructions against
  official documentation without installing or invoking roles.
- Clarify Goldratt's identity in the photograph with a caption. The later
  required portrait standard below supersedes the original image-preservation
  constraint.

Check generated consistency, the automated tests, rendered catalogue shape and
special-character examples, native syntax, navigation and the Git boundary.
Refresh the local previews and record observed results before handover. Keep the
current source layout, classification, short shared instructions and no-commit
constraint. Change the uncommitted status only when a commit is authorized.

### Main README catalogue

Historical catalogue-location contract; D034's compact README contract above
supersedes its requirement to put the complete catalogue in the main README.

Generate the complete expert table and specialty groups directly beneath the
root README's catalogue heading. Use one ordered pair of
`<!-- BEGIN GENERATED CATALOGUE -->` / `<!-- END GENERATED CATALOGUE -->`
markers; reject missing, duplicate or reversed markers before writing outputs.
Preserve all authored text outside the markers, including later manual edits.
Use root-relative profile and image paths. Replace the source-folder catalogue
with a short pointer and update profile back-links, specialty anchors and
project guidance. Check preservation, marker rejection, generated consistency,
native-file byte preservation, navigation and the rendered main README. Keep
the source layout and no-commit constraint.

### Adding an expert

Keep the short addition process in `CONTRIBUTING.md`, linking the existing
generator instructions rather than duplicating them. Provide a copyable profile
README and two-field metadata starter under `src/templates/profile/`, outside
the live role directories. Explain placeholders, unique directory slugs,
specialties, primary references, required credited photos, generated outputs
and the final review. Keep role instructions shared; contribution licensing
follows the MIT adoption below.

Verify the starter by copying and completing it in a temporary checkout, then
generating its catalogue entry and both native files and checking their syntax,
identity and links. Check the real repository's generated outputs and navigation;
preserve existing profiles, catalogue and native files. Keep all work uncommitted.

### Required portrait standard

Historical D009 contract; D023 below replaces the mandatory-photo requirement
with a photo-or-initials visual. The photographic format remains unchanged.

Each live expert must supply `portrait.jpg`: a decodable RGB JPEG exactly
512 by 512 pixels. Reject missing photos, other actual formats, incorrect
dimensions, other color modes and corrupt data before writing generated files.
Use 160 by 160 pixels in the catalogue and 240 by 240 in profile image tags.
Keep the contributor guide to the essential copy, fill, photo and generate steps.
The starter includes required image markup and a photo-credit section.

The owner authorized deterministic cropping and resizing, and looking for more
suitable source photos. Compare reusable photographs and retain clear source
and license records for any replacement. Preserve recoverable originals, keep
identities unchanged, and update credits and captions to describe crops,
resizing and JPEG encoding. Check the images visually, cover
validation failures and no-partial-write behavior, and verify the finished
starter with a supplied portrait. Keep native instructions and metadata unchanged
and leave all work uncommitted.

### Broader portrait search

Search Openverse, Flickr's openly licensed photography and official portrait
or press pages for all four current experts. Replace a photo only when it is a
clear visual improvement and the source provides verified terms allowing
cropping and redistribution, including commercial reuse. Retain a suitable
existing portrait when no qualifying improvement is found.

Keep recoverable source files and a brief record of candidates and license
checks. Inspect selected originals and final crops, retain the 512 × 512 RGB
JPEG standard, and update profile credits and identifying text. Refresh the
local catalogue preview and check image decoding, generated consistency,
navigation and preservation of instructions and metadata. Leave
`CONTRIBUTING.md` unchanged until the owner reviews the result. Keep all work
uncommitted.

### Portrait licenses and further source review

The owner now requested including the photo-license requirements and searching
for more images. This authorizes updating the contribution guide and starter,
replacing the earlier deferral of contribution-guide changes for the first
source-search trial. Keep the guide concise and link the original license terms.
Explain creator and supplied title credits, source and license links, retained
notices, edit history and ShareAlike for modified portraits. Keep photo terms
separate from the library's license and avoid implying an expert's endorsement.

Search additional portrait candidates for all four experts, prioritizing
Nielsen and Goldratt, and compare them with the previous search rather than
counting the same results as new discoveries. Check Wikipedia file pages,
Commons, openly licensed photography and relevant institutional collections.
Keep only clearly identified photographs with verifiable reuse terms; replace
a current portrait only for a visual improvement under the existing standard.
Retain source records and recoverable originals, and show useful alternatives
for review when no replacement is warranted. Check attribution completeness,
image decoding, generated consistency, local links, public suitability and the
Git boundary. Keep all work uncommitted.

### Explicit image sources

The owner requested recording each image's source in the expert profile. Show a
labeled Source link to the specific image's information page in all four photo
credits and the starter. Keep creator, license and edit details alongside it;
link the image record rather than only a biography or website homepage. Check
the owner-linked Wikipedia portrait's file terms before considering a change.
Preserve current photo bytes unless a qualifying replacement is verified.
Check generated consistency, profile source links and the uncommitted boundary.

### Verified portrait permission

The owner confirmed that portraits without verified reuse permission must not
be used. Make this rule explicit in the contribution guide and profile starter,
and link it from project and source guidance. A suitable existing open license
or verified public-domain status qualifies; separate individual permission is
not needed for those photos. Public visibility, a credit or a Wikipedia
fair-use label does not satisfy this collection's reuse requirements.

Record the Goldratt search conclusion and retain the current licensed Commons
photo. Exclude the clearer candidates whose rights were not cleared; this task
does not authorize contacting rights holders. Preserve all four photo files,
profile credits, metadata, generated role files and shared instructions. Check
generated consistency, local navigation, public suitability, byte preservation
and the Git boundary. Refresh the existing local preview and leave the work
uncommitted. Portrait terms remain separate from the MIT adoption below.

### MIT license adoption

The owner selected the same MIT license used by the public method repositories.
Add the standard root `LICENSE` with `Copyright (c) 2026 Shpoont`, matching
`project-execution-model`. Apply MIT to original profiles, role instructions,
metadata, documentation and tooling. Exclude portraits and preserve their
individually credited licenses, source links, notices and edits.

Replace current statements that library licensing is undecided, and explain
original contributions under MIT in the short contributor guide. Record the
adopted decision without rewriting historical decisions or evidence. Document
keeping the MIT copyright and permission notice with standalone role copies;
preserve photo bytes, profile credits, metadata and generated role contents.
Check the exact license text, generated consistency, local navigation, public
suitability, byte preservation and the Git boundary. Refresh the existing local
preview. Keep everything uncommitted; no installation, publication or release
is authorized.

### Simplified profile layout

The owner selected the simplified layout for all four profiles and the starter.
Use this order: name, existing portrait, one line of linked specialties, a short
introduction, native role-file and setup links, one independent-AI notice,
suggested uses, public references, full visible photo credit, collapsed source
file links and catalogue navigation. Remove duplicate specialty sections and
repeated generation explanations. Keep introductions to one or two sentences.

Preserve each expert's suggested uses, reference links, portrait bytes and full
credit, including source, license, notices and edits. Keep metadata, specialty
classification, shared instructions, generated files and the MIT license
unchanged. Update the starter to the same pattern and record layout adoption
separately from the still-provisional role format and specialties. Check rendered
Markdown structure, local navigation, generated consistency, preservation,
public suitability and the Git boundary. Refresh the local previews; leave
everything uncommitted.

### Specialty rules and vocabulary storage review

The owner clarified that specialties help both people and AI select experts
for tasks, and provide a common vocabulary for a predictable catalogue.
Document coherent rules in [the specialty record](elements/specialties.md),
link the short contribution steps and starter to them, and align current
project guidance with that purpose. Distinguish vocabulary rules from the
remaining choice of storage format and the final specialty assignments.

Assess the existing central YAML registry against those rules. Retain the
current registry and its data format during this review; recommend whether it
is needed without treating the storage recommendation as an adopted change.
Keep current specialty assignments, profiles, photos, generated native files,
shared instructions, generator behavior and license bytes unchanged. Do not
import an external taxonomy or implement a new schema in this documentation step.

Check local links and anchors, UTF-8 and public suitability across the full
project tree, generated consistency, protected-file preservation and Git
whitespace. Record observed results and open decisions; leave all work
unstaged and uncommitted.

### Adopt the specialty registry and update assignments

The owner accepted keeping `src/specialties.yaml` and requested updating all
four experts according to the specialty rules. Keep a small shared registry
of used terms, with stable IDs, readable names, groups and a required
`reference` URL that identifies each external concept. Use verified ESCO
knowledge concepts and precise Wikidata concepts for gaps. Recognized source
aliases may supply a natural display name; do not duplicate a concept under
multiple local IDs. Retain flat navigation groups for this step.

Review the four profiles against public work, assign useful broad fields and
specific methods, and update metadata and the profile specialty line together.
Use a new `usability-engineering` ID in place of the provisional
`usability-evaluation` ID; these are not treated as equivalent aliases.
Regenerate the main catalogue and both native formats. Keep the shared
instruction, expert introductions, suggested uses, photo bytes and full photo
credits unchanged; add only relevant public-work references where needed.

Extend validation for required concept references and duplicate concepts or
names. Validate all inputs before writes, retain canonical IDs in expert
metadata, and show only assigned specialties in the generated catalogue.
Record vocabulary attribution and the adopted storage decision in current
guidance. Separate reference meanings from editorial expert assignments.

Check invalid registry rejection before writes, shared-term reuse across
experts, unused-term visibility, both native formats, generated consistency,
profile links, preservation, UTF-8/public suitability and Git whitespace.
Leave all changes unstaged and uncommitted; no integration changes, installation,
publication or role-effectiveness assessment is part of this step.

### Expert definition and selection

The owner accepted a definition of an expert and four practical selection
criteria. Put the short definition in the main README and the criteria in
`CONTRIBUTING.md`, linked from current project guidance and the profile starter.
Cover established expertise, accessible public work, useful task fit and a
preference for people well known within their field. Fame alone is insufficient;
formal credentials are not required, and living and historical people may qualify.

Use the existing introduction, references, specialties and suggested uses to
support selection. Add no profile fields or individual expert briefs. Keep
current profiles, metadata, portraits, shared instructions, generator and native
outputs unchanged. Check the agreed meaning, links and anchors, UTF-8/public
suitability, generated consistency, preservation and Git whitespace. Record the
decision and observed results; leave everything unstaged and uncommitted.
These criteria guide editorial selection; model familiarity and useful expert
judgment still require separate assessment.

### AI expert additions

The owner authorized adding Andrej Karpathy, Chip Huyen and Andrew Ng if they
meet the adopted expert definition and selection criteria. Review their
recognized contributions and accessible public work, and record the task fit
through the existing profile fields. Add qualifying people using the adopted
starter, short shared instruction and source layout.

Map useful specialties to accurate ESCO knowledge concepts, using precise
Wikidata concepts for gaps. Reuse canonical entries and add a consistent
Computing navigation group for these fields. Keep the registry schema unchanged.
Each added expert requires a verified reusable portrait with complete source,
license and edit credits, cropped deterministically to a 512 × 512 RGB JPEG.
If a required portrait cannot be cleared, leave that addition pending and
report the dependency rather than weakening the photo policy.

Regenerate the main catalogue and both native formats, and update current scope
and project records for the completed additions. Preserve the four existing
profiles, portraits, metadata, native files, shared instructions and license.
Check sources and image permissions, specialty concepts, generated consistency,
existing automated checks, profile layout and image standards, navigation,
UTF-8/public suitability, protected-file preservation and Git whitespace.
Refresh the local preview. Keep all work unstaged and uncommitted; no installation,
integration change, publication or live-role evaluation is part of this step.

### Catalogue expansion and further Huyen portrait search

The owner requested another search for a freely reusable Huyen portrait and
adding the previously recommended catalogue candidates. The scope includes
Steve Blank, Saras Sarasvathy, Martin Fowler, Kent Beck, Eric Evans, Martin
Kleppmann, Michael Hammer, W. Edwards Deming, Karen Holtzblatt, Neil Rackham,
Geoffrey Moore, Aswath Damodaran, Robert Kaplan, Lawrence Lessig and Richard
Susskind, plus Philip Kotler from the proposed first batch. These are additions
to the six completed profiles; Huyen is the seventeenth pending addition.

Apply the adopted selection criteria and source each person's public work.
Choose accurate, task-relevant specialties using the existing vocabulary rules,
extending the registry without changing its schema. Require an individually
verified reusable portrait, complete credits and deterministic 512 × 512 RGB
JPEG preparation for every live addition. Explore additional author-name
variants, conference archives, institutional collections and openly licensed
media for Huyen. Leave additions with unresolved portrait rights pending;
do not waive the photo policy or send rights-holder messages without authorization.

Use the existing profile layout and shared instruction, and regenerate the
catalogue and both native formats. Preserve all six existing profiles, portraits,
metadata, native files, the existing vocabulary entries, shared instructions,
generator, tests and license. Update the current project records, distinguishing
completed additions from remaining dependencies. Verify source support, specific
image licenses, concepts, existing automated checks, generated consistency,
profile/image standards, local links, public suitability, preservation and Git
whitespace. Refresh the local preview; keep everything unstaged and uncommitted.
Installation, integration changes, publication and live-role evaluation remain
outside this task.

### First batch to broaden field coverage

The owner accepted the recommended first batch: Judea Pearl, Ellen Lupton,
Léonie Watson, Ross Anderson, Taiichi Ohno, Andy Grove, David Aaker and Roger
Fisher. Add their distinct perspectives using the existing expert definition,
short profile layout, shared instruction and contribution process. Continue
bounded searches for the five existing pending portraits when new source leads
are available. This step does not automatically add the remaining recommendations.

Verify public work, task fit and precise specialty concepts. Reuse existing
registry entries and groups where accurate; add only used, sourced concepts
without changing the schema. Require a verified permitted portrait with full
credits and edit history, prepared deterministically as a 512 × 512 RGB JPEG.
Keep any unresolved addition pending outside the live collection and record
the specific dependency. Do not waive photo rules or send permission requests.

Preserve the eighteen existing profiles, portraits and native files, all
existing specialty entries, shared templates, generator, tests, contribution
guide and MIT license. Generate the updated catalogue and native formats only
from complete profiles. Check source support, image permissions and quality,
specialty meanings, generated consistency, existing tests, profile/image
standards, local links, public suitability, preservation and Git whitespace.
Refresh the local preview and update connected scope, decisions, current work,
delivery and evidence records. Keep all changes unstaged and uncommitted;
installation, integration changes, publication and live-agent assessment remain
outside this task.

### Complete pending profiles from newly cleared portrait sources

The owner requested continued work on the accepted additions. Search new
portrait sources for the eight pending candidates, including original
conference recordings with explicit qualifying reuse permission. Reuse prior
findings rather than repeating unchanged searches. A recording's visibility or
an absent license label does not establish permission. Verify each selected
source's attribution terms and linked license version before public use.

Complete any cleared addition using its prepared short profile, existing
specialty rules and the unchanged shared instruction. Preserve the twenty-three
existing complete profiles, their native files and portraits, all existing
vocabulary entries, shared templates, generator, tests, contribution guide and
MIT license. Prepare a deterministic 512 × 512 RGB JPEG crop, credit the source
recording and exact frame timestamp, and record the license and edits. Keep
uncleared additions pending; do not send permission requests or weaken the policy.

Regenerate the catalogue and native formats, refresh the local preview, and
update connected scope and progress records. Check source support and rights,
portrait quality, metadata/native consistency, existing automated tests, local
links, public suitability, preservation and whitespace. Keep work unstaged and
uncommitted, without installation, integration changes, release or live-agent
assessment. End this search pass when the new leads are assessed and cleared
additions are checked; retain unresolved dependencies for future new sources.

### General free-reuse portrait policy

The owner requested acceptance of any free reuse, with or without an attribution
requirement, while the collection always keeps attribution. Replace the fixed
license allowlist with a general rule: accept a clear no-cost reuse grant or
public-domain status whose terms cover the actual catalogue use and required
image preparation. Standard licenses and explicit custom permission can qualify.
Record and follow applicable conditions; assess compatibility with the intended
use instead of rejecting solely by license category. Attribution is always a
collection requirement, including when the source makes it optional.

Update the contribution guide, starter notes, current project guidance and
manual checks consistently. Record D021 as broadening D011's eligibility rule.
Retain historical source findings and mark pending portraits for reassessment
under the updated policy. Preserve all profiles, portraits, metadata, native
files, vocabulary, shared operational templates, generator, automated tests
and MIT license. Verify local links, UTF-8/public suitability, generated-output
consistency, preservation and whitespace. This documentation step does not
itself clear or replace an image; keep all work unstaged and uncommitted.

### Reassess Watson, Ohno and Fisher under the general photo policy

Review the three previously accepted candidates against D021, starting with
their known source photographs and exact reuse terms. Add a profile only when
the grant covers this noncommercial catalogue prototype and preparation of the
required 512 × 512 RGB JPEG. Keep attribution, source, license and edit history
in the profile; preserve any noncommercial or no-derivatives conditions.
Do not infer permission to crop from permission to reproduce an entire image.

Preserve the twenty-four completed profiles, existing vocabulary definitions,
shared templates, generator, tests, contribution policy and MIT license. Add
only concepts used by a cleared profile and regenerate its native files and
the catalogue. Update the connected records, inspect originals and final crops,
run existing tests and generated-output checks, check links, public suitability,
preservation and whitespace, and refresh the structural HTML preview. Record
uncleared dependencies precisely. No permission requests, integration changes,
installation, publication or commit are part of this step. End this pass once
the three sources are assessed and any cleared additions are verified.

### Initials placeholders and the Ohno and Fisher additions

Historical D023 contract; D024 below changes the initials to full names.

The owner adopts initials placeholders when a suitable permitted photograph is
unavailable. D023 supersedes D009's mandatory-photo requirement: every profile
needs exactly one square visual, either the existing 512 × 512 RGB JPEG
`portrait.jpg` or a standardized 512 × 512 `initials.svg`. Preserve existing
portraits and their credits, including Watson's current photo. Actual photos
continue to follow D021's permission and attribution rules.

Provide a shared SVG template and a documented command that reads the profile's
name, accepts explicitly chosen initials and creates the SVG without overwriting
an existing visual. Keep the style neutral and accessible. Validate either
visual before generating any outputs; reject missing, ambiguous or altered
placeholder inputs. The catalogue selects the supplied file and identifies
initials as a placeholder. The starter uses an Image section for the placeholder;
photographic profiles retain their full photo credits.

Complete the accepted Ohno and Fisher drafts with TO and RF placeholders,
supported specialty concepts and both native formats. Preserve all twenty-five
existing profiles and native files, shared instructions, metadata schema, earlier
specialty definitions and the MIT license. Update current guidance, the short
contribution steps and connected records; keep historical photo-search findings
as historical evidence. The four other accepted pending candidates are outside
this addition step and no longer depend on photo clearance for eligibility.

Check the two new profiles, sourced concepts, meaningful generation/error cases,
exact contributor commands in an isolated starter trial, SVG rendering at both
display sizes, generated consistency, links, public suitability, preservation and
Git whitespace. Refresh the local preview. Stop when these changes are checked;
leave everything unstaged and uncommitted, without installation, publication,
integration changes, rights-holder messages or live role assessment.

### Full-name placeholders

D024 replaces the initials in D023 with the expert's complete name. Rename the
shared template and the two profile SVGs to `placeholder.svg`; the creation
command reads the name directly from `expert.yaml`, without an abbreviation
argument. Wrap names across centered lines and size the text to fit the same
512 × 512 canvas. Preserve the existing colors and display sizes, all photos,
metadata, specialty definitions and native instructions. Update current usage
guidance and the starter while retaining historical initials decisions/results.

Verify full-name text and XML escaping, long-name wrapping, mixed image types,
invalid/ambiguous inputs and overwrite prevention. Exercise the exact commands
in an isolated starter, inspect both actual names and longer examples at the
160/240 pixel display sizes, and check generation, links, preservation and Git
whitespace. Keep the work unstaged and uncommitted, without installation,
publication, integration changes or additional expert profiles.

### Complete the four remaining accepted profiles

D025 adds Michael Hammer, Karen Holtzblatt, Neil Rackham and Richard Susskind
from the prepared, accepted drafts, using D024's full-name placeholders. Check
their public references and specialty concepts, reuse existing vocabulary and
add only used concepts. Generate both native formats and the catalogue; retain
the current profile layout, metadata schema, shared instruction and SVG template.
Preserve the twenty-seven existing profiles and all earlier vocabulary entries.
Update connected status and delivery records, run the existing checks, inspect
the new SVGs at display sizes, and prepare a rendered catalogue/profile preview
for owner review. Stop after these four additions and their preview are checked.
Keep work unstaged and uncommitted, without installation or publication.

Observable pass criteria are in [checks](../tests/README.md). Record current
results in [evidence](../evidence/README.md). Native runtime behavior, expert
quality and owner acceptance require later assessment; these are not claims
made by this prototype.

## Connections and open questions

The simplified human profile layout is adopted for the current prototype.
The specialty task-matching purpose is agreed, with rules documented in the
[specialty record](elements/specialties.md). D015 adopts the central YAML registry,
its minimal reference schema and updated assignments for the four experts.
Future vocabulary entries follow those rules. The native role format and
effectiveness assessment remain trial choices. D016 adopts the
[expert definition](../README.md#who-is-included) and
[selection criteria](../CONTRIBUTING.md#expert-selection), supported through
existing profile fields. D023 adopts a required square photo or placeholder visual;
D024 replaces initials with the complete name from metadata,
with the shared SVG template and exact contributor instructions. The photo
standard and verified reuse permission still apply to actual photographs. D021 accepts
any compatible free reuse grant and keeps attribution universally, replacing
the earlier fixed list and automatic category exclusions. Rich expert briefs
are optional future additions only if a concrete need justifies them. Original
material and contributions use [MIT](../LICENSE), with portraits retaining their
credited licenses. Outcome assessment remains pending.

D017 accepted the three AI candidates and added two profiles. D018 added twelve
more completed profiles. D019 adds five of the recommended eight-person first
batch, bringing the collection to twenty-three. D020 completes Huyen's earlier
accepted addition, bringing the collection to twenty-four. D022 then completes
Watson under D021, bringing the collection to twenty-five. D023 completes Ohno
and Fisher with initials, bringing the catalogue to twenty-seven. D024 changes
the placeholders to full names. D025 completes the four remaining accepted
profiles, bringing the catalogue to thirty-one; see
[current work](current-work.md#next-actions). No accepted draft remains pending.

D031 adds the four later owner-requested experts, bringing the catalogue to
thirty-five under the contract above. Their addition preserves the earlier
profiles and shared instruction.

D032 adds Rybka using the existing Operations management concept and a
full-name placeholder, bringing the catalogue to thirty-six without changing
the vocabulary or shared instruction.

D035 adds Jordan Peterson with the Personality psychology concept and a credited
photograph, bringing the catalogue to thirty-seven experts and fifty-seven
specialties. Earlier profiles, groups and the shared instruction remain unchanged.

D036 adds Hawkins, Premack, Levels and Frawley, bringing the catalogue to
forty-one experts and sixty-one specialties in nine groups. One credited
portrait and three full-name placeholders bring the image totals to
twenty-nine and twelve. Earlier expert directories, source definitions,
shared instruction and fixed README sample are preserved.

D039 adds the ten selected experts and removes Rybka, producing fifty profiles
and seventy-four specialties within the same nine groups. Two new permitted
portraits and eight full-name placeholders give thirty-one photos and nineteen
placeholders. The other forty profiles, earlier concept definitions, shared
instruction and fixed README sample are preserved.

## Expert identity wording and removal requests

D046 authorizes a focused follow-up to the published v1.0.0 baseline:

- Add **Requests from featured experts** near the bottom of the main README,
  with a private correction/removal route to `leonid@komarovsky.info`, voluntary
  removal without a legal complaint, minimal identity confirmation, target
  response times and an explicit limit concerning historical and third-party copies.
- Replace the shared role opening with an explicitly AI-inspired perspective
  and a prohibition on claiming to be or represent the expert or their estate.
  Substitute each expert's own name and regenerate both native distributions.
- Preserve the rest of the shared instruction, expert roster, profiles, metadata,
  visuals, descriptions, vocabulary and generated catalogue/index content.
- Run the existing suite and generation check; verify both hosts' instructions,
  README rendering/link targets, preserved content and the final diff. Commit
  with the configured signature, push and read back the remote commit and CI.
  Record the changes under Unreleased; published release tags remain fixed.

## Findings and changes

Record the handover in [current work](current-work.md), lasting reasons and
pending choices in [decisions](decisions.md), and meaningful changes in the
[changelog](../CHANGELOG.md).


## Studio portrait refresh for owner review

D047 authorizes an isolated, uncommitted portrait refresh and contribution-guidance update. Assess all fifty-seven experts; prioritize recognizable appearance over photographic polish. Preserve biographies, expert metadata, vocabulary, shared instructions and the bytes of all native exports. No push, commit, tag, release or integration change is authorized in this step.

Retain original visuals and credits outside the public tree. Compare name-only, one-reference and complementary-reference approaches on the four calibration experts, without claiming a universal winner or a model version the tool does not expose. Use permitted, reliably attributed visual references, preserve their applicable terms, and distinguish generated likenesses and historical interpretations from authentic photographs. Retain an existing visual where a replacement lacks adequate support.

Acceptance requires accurate image disclosure and provenance, valid 512 x 512 RGB JPEGs or existing name placeholders, coherent contributor instructions, generated consistency, the existing test suite, unchanged protected role content, public-content and local-link checks, rendered catalogue review and opening the final local preview in Safari for the owner. Automated visual inspection is not biometric identity verification; owner review and uncertain likenesses remain explicit.

The owner's first visual review found the photographic results too close to
background removal and excluded drawings, paintings, statues and similar
depictions from generation. Restore the five existing historical visuals and
credits, retaining their depiction status. Refine the photographic prompt to
permit a new studio pose, lighting and understated clothing while preserving
facial identity and age. Compare two new photographic trials before replacing
more catalogue portraits; trials remain outside the public tree for owner review.

## Reproducible studio portrait method and catalogue rollout

D048 adopts the owner's approved moderately muted sample direction: a distinct
palette and flowing gradient per expert, direct eye contact, a new professional
studio sitting and faithful apparent age and facial characteristics. Document
the method before the catalogue rollout. Use a versioned shared prompt and a
small local helper for stable per-expert background recipes, reference hashes
and deterministic JPEG preparation. Reproducible inputs and procedure do not
guarantee identical model output pixels.

Assess all fifty-seven experts. Generate only photographic subjects supported
by permitted references; preserve drawings, paintings, statues, unsupported
placeholders and uncertain likenesses. Retain original images and credits.
Use approved samples where suitable, then generate and inspect remaining
eligible portraits. Record a per-expert outcome, including every retention.
Preserve biographies, expert metadata, specialties, shared role instructions
and all 114 native exports. No commit, push, release or integration change is
authorized. Continue in the existing isolated worktree.

Check reference provenance, direct eye contact, identity, individual backgrounds,
image labels and dimensions, native-content hashes, source/export consistency,
the full test suite, public suitability and local links. Render the updated
catalogue and make its comparison preview available for owner review. Keep
generation records and local paths outside the public tree. Editorial likeness
inspection remains separate from file validation and owner acceptance.

## Portrait contribution consistency closeout

D049 authorizes a copyable generated-image credit block, reusable repository
validation of portrait content through the normal generator/check and CI path,
and a fresh-session new-profile walkthrough. Keep the accepted studio-v1
appearance, all 57 image bytes, biographies, expert metadata, specialties,
shared instructions and 114 native exports unchanged. Changes stay in the
isolated worktree, uncommitted and unpushed.

Use one authored credit template and explicit tool/date/model/method fields.
Validate generated disclosures, the stable background recipe and reference
sources/terms before the exporter writes any outputs. Cover missing or malformed
credits, accidental loss of disclosure and drift in the stable palette, together
with a new-profile path built from the contributor starter. File checks cannot
establish identity, legal clearance or visual quality. Keep source attribution
as project policy; source-license conditions apply where the underlying rights
and actual use require them. Generation is not a blanket waiver or automatic
transfer of reference licenses to every output.

Final review also checks mixed-reference credits: each separately labeled Source
entry must retain its own linked terms or explicit public-domain notice. A
public-domain reference must not waive another reference's declaration. Repeat
shared terms after each Source entry so the requirement is unambiguous, and
cover missing and unlinked terms with regression checks before closing out.

An independent agent walkthrough is a separate acceptance check. Run its
documented prompt in a disposable copy of the complete reviewed working tree,
including untracked feature files, without the implementation conversation or
author coaching. A temporary expert is a fixture, not a roster addition. Keep
the actual image inputs, masters, commands and rendered evidence outside the
public tree; do not substitute a self-review or deterministic fixture for an
actual independent contribution.

The owner subsequently authorized this fresh-session run and confirmed-issue
cleanup, without committing or pushing. The first bounded Grace Hopper case
completed. Clarify the minimum post-generation record and allowed preview-tool
choice from its findings, then rerun the normal checks and protected-content
comparison. Preserve the shared prompt and all existing expert content and
images. Record the [observations](../evidence/README.md#independent-portrait-contribution-walkthrough--2026-10-21)
separately from broader reliability and portrait-owner acceptance, which remain
unverified.

## Portrait owner acceptance and local commit

D050 records the owner's acceptance of the selected portraits after D049's
independent contribution check. Close out current review notes, verify the
complete proposed commit, run the normal checks and preserve the 57-expert
roster, selected visuals and native role bytes. Create one signed commit in the
existing portrait worktree. This supersedes the earlier no-commit boundary;
do not push, merge, tag, publish a release or change the published v1.0.0 baseline.
Owner acceptance is an editorial decision, separate from identity verification
and the bounded contributor walkthrough.

## Local portrait integration assessment

D051 authorizes rebasing the accepted portrait work onto local main and assessing
a local squash merge. Keep the maintained main checkout unchanged; do not push,
merge into main, tag or release. A disposable copy may stage the squash result
for verification without committing it.

Preserve main's AI-identity instruction, all 114 current native exports and the
featured-expert request policy. Preserve the accepted portrait bytes, roster,
metadata and source permissions. Resolve the competing D046 allocation by keeping
main's identity/request decision as D046 and renumbering the local portrait
records to D047–D050, with their existing dates and meaning unchanged.

Require a backup of the original signed commit, clean conflict resolution, the
full suite, read-only generation, native equality, protected-content comparison,
local links, public suitability and whitespace checks. Verify the rebased
signature and simulate the squash result separately from actually merging main.

## Local squash merge and v1.1.0 preparation

D052 authorizes squashing the accepted, rebased portrait work into local main
and preparing the next minor version. Create one signed local commit containing
the portrait work and release preparation. No push, tag, hosted workflow run or
release publication is included. Preserve the published v1.0.0 tag.

Use v1.1.0 for the compatible portrait-generation and provenance-validation
capability. Include the already delivered AI-identity and featured-expert
request changes since v1.0.0 in the release notes. The version covers the whole
library; existing expert identifiers, metadata, specialty vocabulary, native
formats, export paths and intended role scope remain compatible.

Finalize a dated v1.1.0 changelog entry and retain Unreleased for later work.
Keep the latest published version distinct from the prepared local candidate
in current entry points. Provide draft publication notes and the remaining
exact-commit CI, annotated-tag and release-readback steps in the delivery guide.
Align current instructions, agreement, checks and handover with this boundary.

Before committing, run the full suite, read-only generated consistency, native
syntax/equality, local links, UTF-8, public-suitability and staged-diff checks.
Compare all 173 protected files, 57 selected visuals and 57 individual profile
READMEs with the accepted rebased tree. Release preparation may change only
documentation; the squash must preserve the feature implementation and accepted
content. Reuse the existing portrait-owner acceptance and bounded walkthrough
evidence rather than infer new visual or runtime results. Verify the final
signature, single-parent squash commit and clean local tree; report publication
as pending.
