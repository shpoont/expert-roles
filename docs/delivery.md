# Delivery and handover

## Review the catalogue

Start at the [full catalogue](../src/roles/README.md), then open individual
profiles and their Codex or Claude Code files. The fifty-seven completed profiles
use one simplified layout and eighty-two shared specialties. The working tree
contains forty generated portraits, five original historical depictions and
twelve full-name placeholders. The owner accepted D053's eleven additions;
the 29 generated images accepted under D050 are unchanged. All
accepted experts remain included.

Review images and their provenance using the
[portrait workflow](elements/portraits.md). Historical depictions remain unchanged;
generation applies only to supported photographic subjects. The adopted style
uses direct eye contact, a new studio sitting and an individual moderately muted
background. The documented method, shared prompt and helper are locally checked:
43 tests pass and all 119 generated files match. The owner accepted the final
image selections; file checks do not verify likeness. D049 adds the copyable
credit block and repository validation. The independent
[fresh-session walkthrough](../tests/portrait-walkthrough.md) completed one
temporary Grace Hopper contribution in a disposable copy, with actual built-in
generation and screenshot-backed profile/catalogue review. See the
[bounded results](../evidence/README.md#independent-portrait-contribution-walkthrough--2026-10-21).
This does not establish repeatability; owner acceptance is recorded separately.
D052's signed local squash is retained. D055 authorizes finalizing D053's
accepted portraits and D054's provenance standard into the v1.1.0 release,
with a signed commit, ordinary main push, completed exact-commit hosted checks,
annotated tag and latest stable GitHub release. Deployment remains separate.

The catalogue remains broad under D038 and uses D037's adopted criteria.
D039 implements the owner's ten selected additions and Rybka removal; D040
adds seven philosophical perspectives with documented historical limits.
Other candidates remain proposals; earlier deferral recommendations based on
a narrow scope are superseded. Any further roster proposal must assess useful
coverage and actual overlap across the collection.

Each `expert.yaml` supplies the name, specialties and optional perspective cue.
The [specialty registry](../src/specialties.yaml) resolves labels; one
[shared instruction](../src/templates/invocation.md) defines execution behavior.
Profiles, public references and visuals support browsing. Follow the
[source guide](../src/README.md) to edit sources and regenerate outputs.

Codex TOML and Claude Code Markdown are the initial export formats. The
`v1.0.0` baseline includes the accepted catalogue and D044's distribution layout.
The [release record](https://github.com/shpoont/expert-roles/releases/tag/v1.0.0)
identifies the published snapshot.

## Distribution files

Start at the [host chooser](../dist/README.md), or browse the
[Codex](../dist/codex/README.md) and [Claude Code](../dist/claude/README.md)
indexes directly. Each host index lists experts alphabetically and by specialty,
using the existing vocabulary and assignments. One expert may appear under
several specialties while retaining exactly one file per host:

- `dist/codex/expert-<slug>.toml`
- `dist/claude/expert-<slug>.md`

These paths depend on the expert's stable slug, not specialty labels or groups.
Consumers importing a collection select `expert-*.toml` or `expert-*.md`;
the README files provide navigation. Retain [LICENSE](../LICENSE) and the
[vocabulary credits](elements/specialties.md#source-attribution) with redistributed
material as applicable. The profiles hold the separate portrait credits.

Native files and distribution indexes are generated and committed with their
sources. Edit source metadata or shared templates, then
[regenerate and check](../src/README.md#generate-the-catalogue-and-native-files).
CI checks consistency without rewriting files. The exporter reports obsolete
or duplicate files for review rather than deleting them. Temporary release
archives and build/cache files are excluded from Git.

## Use a native role

Role files contain the expert's name, selection cues and shared instruction.
Profiles and references support browsing; include any source material the task
needs in the assignment.

1. Open an expert in the [catalogue](../src/roles/README.md) and choose the
   **Codex** or **Claude Code** file, or use the [distribution indexes](../dist/README.md).
   From a checkout, use the generated file under `dist/codex/` or `dist/claude/`.
   On GitHub, use **Download raw file**, preserving its filename and contents.
   Retain [LICENSE](../LICENSE) with copies of the role files.
2. Register the export with the intended host using the guidance below.
   Managed Codex deployment and lifecycle belong to a separate plugin.
3. Describe the task, relevant evidence and constraints. Once roles are
   registered, the assistant can select a suitable expert when useful. You can
   also request a specific expert by name. For example:

   ```text
   Use Eliyahu Goldratt's expert role to review this delivery plan.
   Identify the main constraint and explain what limits overall throughput.
   ```

When checking that a particular export is invoked, verify the actual delegated call's
`expert-` name. This is an invocation check, not a requirement to name an expert
in every task. An answer from a pre-existing alias does not validate that export.

### Codex: explicit registration

[Codex's examples](https://learn.chatgpt.com/docs/agent-configuration/subagents#example-custom-agents)
request agents by their registered names in natural language. After registration,
you can write `Use the expert-eliyahu-goldratt agent to review this delivery plan.`
An `@` prefix is not required for this documented request pattern.

Each Codex TOML contains `name`, `description` and `developer_instructions`.
Both formats also carry [source, version and expert ID comments](../src/README.md#export-provenance)
for people and consuming tools; these do not enter the execution instructions.
Consumers register the file using its generated name and description plus the
file path. The [configuration reference](https://learn.chatgpt.com/docs/config-file/config-reference)
defines `agents.<name>.description` and `agents.<name>.config_file`.

The successful [Codex CLI 0.163.0 check](../evidence/README.md#codex-exec-retry--2026-10-20)
passed these registrations as `codex exec -c` overrides for each invocation,
without a persistent registry. Run this manual example from a Git project using
your configured Codex CLI, replacing the absolute path with the downloaded
export's location:

```sh
codex exec --sandbox read-only \
  -c "agents.expert-eliyahu-goldratt.description=\"Consider Eliyahu Goldratt's perspective, especially on system constraints and overall throughput, including dependencies and shared-resource contention in project delivery. Relevant specialties include Operations management, Project management, Theory of Constraints and Critical Chain project management.\"" \
  -c 'agents.expert-eliyahu-goldratt.config_file="/absolute/path/to/expert-eliyahu-goldratt.toml"' \
  'Use the expert-eliyahu-goldratt agent to review this plan: preparation 12 units/hour, assembly 4, packing 10, demand 8. Explain the constraint and the effect of doubling packing.'
```

The description argument copies the generated file's description. When using
another expert, take its exact `name` and `description` and point `config_file`
to that expert's file. Consumers own model and permission configuration as well
as registration and lifecycle; this library provides no installer.

[Codex also documents](https://learn.chatgpt.com/docs/agent-configuration/subagents#custom-agents)
`.codex/agents/` and `~/.codex/agents/` for project and personal files. Automatic
discovery from a temporary project did not work in the recorded attempt.
Copying a file into those directories alone is therefore not a verified setup
path for this catalogue. The explicit-registration result does not resolve that
separate discovery issue.

### Claude Code: runtime untested

The Markdown exports contain YAML `name` and `description` frontmatter followed
by the shared instruction. Syntax and generated consistency are checked; no
Claude runtime test has run. The [official subagent guide](https://code.claude.com/docs/en/sub-agents)
documents project `.claude/agents/` and personal `~/.claude/agents/` locations.
For a natural-language request, name the registered agent; Claude decides whether
to delegate. To explicitly select a subagent, type `@` and choose it from the
suggestions. For this local role, the manual mention is
`@agent-expert-eliyahu-goldratt`. See
[explicit invocation](https://code.claude.com/docs/en/sub-agents#invoke-subagents-explicitly).
These are documented host features, not additional catalogue runtime results;
verify an actual invocation before treating an export as runtime-validated.

### Scope and selection

Descriptions combine name and specialties with an optional perspective phrase
where it distinguishes overlapping expertise. These cues are nonexhaustive; the
expert's documented work defines professional scope. The shared instruction
requires declining out-of-expertise work, bounded handling of mixed requests,
clarification where needed, independent challenge and transparent attribution.
See the [metadata guide](../src/README.md#role-metadata-and-descriptions).

Consuming integrations own parent-level selection guidance: consider expert
judgment when useful, handle routine work directly and choose a small set with
distinct questions. Clarify missing context when it affects the assignment.
The parent retains task coverage and synthesis. The three Codex samples do not
establish broad reliability or comparative benefit.

## Delivery acceptance and remaining work

The owner accepted the compact main README and the fifty-seven-expert catalogue
that became the published `v1.0.0` baseline. Its implementation and rendered
review were complete; no baseline profile, portrait, layout or specialty
decision remained open. The owner separately accepted D048's studio-v1 selections
under D050, authorizing a signed local commit without a push or release.
D041 records the acceptance and the
[documentation closeout](design.md#final-documentation-closeout-for-the-accepted-catalogue).

The current [agreement](../PROJECT.md), [checks](../tests/README.md) and
[closeout evidence](../evidence/README.md#accepted-catalogue-documentation-closeout--2026-10-21)
cover D041's completed proposed tree. The owner subsequently requested D042's
[visitor journey review](design.md#first-time-and-returning-visitor-journey-review)
before commit. All five findings are resolved in re-review; a fresh independent
final review found no blockers in source or captured local rendering. Relevant
checks and an isolated completed-starter trial pass. See the
[visitor review evidence](../evidence/README.md#visitor-journey-review--2026-10-21).
Actual-user, hosted GitHub and assistive-technology outcomes remain unverified.
The owner accepted the result and authorized the initial signed catalogue
commit on 2026-10-21 under D043; that signed commit was subsequently pushed.
D044 adds the [distribution layout](design.md#distribution-layout-and-generated-indexes)
without changing native file contents or accepted expert content. Its checks
and current status are recorded in [current work](current-work.md).
The [latest additions](../evidence/README.md#seven-philosophy-additions--2026-10-21)
record the fifty-seven-expert sources, images, native files and local rendering;
earlier decisions and evidence retain their historical scopes. Acceptance of
the rendering is separate from structural checks and observed runtime behavior.

Automatic Codex directory discovery, Claude runtime validation, deployment and
comparative role benefit remain later consumer or assessment work. They do not
block the accepted baseline's publication. No new invocation or deployment is
included. D045 authorized committing D044's completed changes with the versioning
setup and publishing `v1.0.0` after final checks. The
[release contract](design.md#versioning-and-first-release) requires verifying the
remote commit, successful hosted checks, annotated tag and GitHub release.

Original sources, role instructions, tooling and name artwork use [MIT](../LICENSE).
Photographs and generated adaptations of licensed references retain the terms
and credits on their profiles; they are excluded from MIT. Original generated
contributions use MIT to the extent rights can be granted. Always preserve attribution, source, permission notices and edit
history, and follow each image's conditions. Watson's new selection uses CC
BY-SA 2.0 references; copies of her previous CC BY-NC 2.0 image retain those terms.
Ross's CC BY-NC 4.0 adaptation and the other credited noncommercial sources
retain their individual conditions.
The collection does not promise uniform photo reuse rights. Vocabulary labels retain their
[source credits and terms](elements/specialties.md#source-attribution).
Follow the [photo policy](../CONTRIBUTING.md#photo-sources-and-licenses) and
[image instructions](../src/README.md#choose-the-profile-image) for changes.

## Versions and releases

Library version: **[v1.1.0](https://github.com/shpoont/expert-roles/releases/tag/v1.1.0)**.
One `MAJOR.MINOR.PATCH` version covers profiles, metadata, vocabulary, shared
instructions, templates, tooling and both native formats. The consuming plugin
and other integrations keep independent histories. Individual experts and export
formats do not have separate versions.

The root [VERSION](../VERSION) file is the machine-readable source for export
provenance, finalized as `1.1.0` for this release. Use a development suffix for
unfinalized future exports. A version header identifies a declared library version, not proof of publication or an
exact content digest. Keep released tags fixed and use Git refs for snapshots.

Choose the increment by its effect on users and consumers:

| Increment | Use for |
| --- | --- |
| Major | Removed or renamed expert identifiers; incompatible metadata, native formats, documented commands or export paths; material changes to an existing role's intended scope or execution behavior. |
| Minor | New experts, specialties or compatible capabilities that preserve existing consumption and intended role behavior. |
| Patch | Documentation, attribution or implementation corrections that preserve intended behavior and agreements. |

Maintenance alone need not produce a release. Record meaningful changes under
**Unreleased** in [CHANGELOG.md](../CHANGELOG.md) until preparing the next version.
The first stable baseline includes `dist/codex/expert-<slug>.toml` and
`dist/claude/expert-<slug>.md`; classification changes do not move those files.
A versioned export is not a broader host-compatibility or effectiveness claim.

Preparation, local commits and publication follow the owner's current
authorization. D055 authorizes v1.1.0 publication; future releases need their
own owner instruction. Complete the applicable steps below:

1. Review scope, compatibility impact and evidence; choose the intended version.
2. Set `VERSION` to the final version, without `v` or a development suffix for a
   stable release. Finalize the dated changelog entry and update the main README
   and this guide's baseline references. Leave **Unreleased** for subsequent work.
   Regenerate and run the [checks](../tests/README.md), including export headers,
   local links, native consistency and applicable source/content preservation.
   `VERSION`, both formats' comments and the intended tag must agree.
3. Commit the exact intended contents using the configured signing identity,
   verify the signature, and push. Require the hosted **Checks** workflow to
   succeed for that exact commit before publishing.
4. Create an annotated `vMAJOR.MINOR.PATCH` tag on that commit, verify its target
   and push the tag explicitly. Released tags stay fixed; corrections require
   a new version. Consumers pin a released tag or full commit.
5. Create the matching GitHub release from the existing tag, with a title naming
   Expert Roles and its version, notes summarizing the baseline, validation and
   limits, and a link to the fixed snapshot. Mark stable library releases Latest.
   GitHub's tagged source archives include `src/`, `dist/` and the license
   records. Additional host-specific archives are not part of the initial
   release convention.
6. Read back the remote commit, tag target, release metadata/notes and relevant
   source files. Confirm the local tree is clean. Keep preparation evidence
   distinct from successful publication; a commit alone does not make a release.

### v1.1.0 release baseline

D055's [publication contract](design.md#publish-expert-roles-v110) includes
D052's signed local squash, D053's accepted expansion to forty generated
portraits and D054's native export provenance. Version v1.1.0 is a minor
increment for compatible portrait tooling and provenance capabilities. Existing
expert identifiers, source metadata, native settings, export paths and intended
role scope remain compatible. The AI-identity and request-policy changes since
v1.0.0 are included in this whole-library release.

The [release page](https://github.com/shpoont/expert-roles/releases/tag/v1.1.0)
and [Checks workflow](https://github.com/shpoont/expert-roles/actions/workflows/checks.yml)
record hosted delivery. Require both the release commit's workflow and its
validation check to conclude successfully before creating the annotated tag.
Read back remote main, tag object/target, release metadata, `VERSION` and both
native formats before reporting publication. Version declarations alone do not
prove delivery; never move an existing released tag.

<a id="draft-release-notes-for-v110"></a>

### Release notes for v1.1.0

**Expert Roles v1.1.0** adds a reproducible portrait contribution workflow,
expanded studio-portrait coverage and portable export provenance across the
57-expert catalogue.

- 40 owner-accepted generated portraits, including Goldratt, with five unchanged
  historical depictions and twelve full-name placeholders. Profiles retain
  source creators, individual terms, generation disclosures and edit history;
  both catalogues identify image types visibly and accessibly.
- A versioned studio-v1 prompt, stable per-expert background recipes, reference
  hashes, deterministic 512 × 512 RGB JPEG preparation, a copyable credit block
  and per-reference validation in the generator and CI.
- Source repository, version `1.1.0` and expert ID comments in all 114 Codex and
  Claude Code exports, generated from one validated `VERSION` file. Existing
  parsed settings and execution instructions are preserved by these comments.
- Explicit AI-inspired identity and a private voluntary correction/removal
  process for featured experts and representatives.
- Stable expert identifiers, 82 specialties in ten groups and flat `dist/`
  paths. Consuming integrations and installation remain separate.

Local validation: 45 tests pass and all 119 generated files match. All 57 native
pairs parse and agree. The stable version changes only the version comment in
each accepted development export; accepted images, individual profiles, expert
metadata, vocabulary and shared templates retain their bytes. One independent
temporary contribution walkthrough passed. No new host-runtime testing ran;
Claude runtime, automatic Codex discovery, general contributor reliability,
identity verification and comparative role benefit remain unestablished.
Images retain their individually credited terms, including noncommercial
conditions where applicable. Hosted release notes include the successful
exact-commit check and fixed snapshot links after those results are observed.

## Outcomes and learning

No comparative role-benefit or contributor outcome assessment has run. Agree
representative tasks, comparison conditions, criteria and responsibility before
such assessment. Keep future observations in [evidence](../evidence/README.md)
and current follow-ups in [current work](current-work.md).
