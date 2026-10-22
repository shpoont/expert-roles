# Delivery and handover

## Review the catalogue

Start at the [full catalogue](../src/roles/README.md), then open individual
profiles and their Codex or Claude Code files. The v1.2.0 baseline contains
68 profiles, 96 shared specialties in 14 groups and 136 native role files.
It has 50 generated portraits, five original historical depictions and thirteen
full-name placeholders. The eleven expert additions reviewed after v1.1.0
are included; all previously accepted experts remain in the collection.

Review images and their provenance using the
[portrait workflow](elements/portraits.md). Historical depictions remain unchanged;
generation applies only to supported photographic subjects. The adopted style
uses direct eye contact, a new studio sitting and an individual moderately muted
background. The published v1.1.0 baseline passed 45 tests and matched all 119
generated files. D056's contribution/release process has its own
[checks and evidence](../evidence/README.md#contribution-and-release-separation--2026-10-22).
The owner accepted the final
image selections; file checks do not verify likeness. D049 adds the copyable
credit block and repository validation. The independent
[fresh-session walkthrough](../tests/portrait-walkthrough.md) completed one
temporary Grace Hopper contribution in a disposable copy, with actual built-in
generation and screenshot-backed profile/catalogue review. See the
[bounded results](../evidence/README.md#independent-portrait-contribution-walkthrough--2026-10-21).
This does not establish repeatability; owner acceptance is recorded separately.
D052's signed local squash is retained. D055 delivered D053's accepted portraits
and D054's provenance standard in v1.1.0, with a signed commit, completed
exact-commit hosted checks, annotated tag and latest stable GitHub release.
That authority applies only to the delivered release; deployment remains separate.

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
sources during release preparation. Source contributions use a
[separate preview](../src/README.md#generate-the-catalogue-and-native-files)
and leave these files unchanged. CI checks contribution ownership or release
consistency without rewriting the checkout. The exporter reports obsolete
or duplicate files for review rather than deleting them. Temporary release
archives and build/cache files are excluded from Git.

## Use a native role

Role files contain the expert's name, selection cues and shared instruction.
Profiles and references support browsing; include any source material the task
needs in the assignment.

Choose a setup route before downloading: Codex supports a one-off CLI trial
and manual persistent registration below; Claude Code uses project or personal
agent files. The recorded Codex result covers only explicit one-off registration.
Persistent Codex setup follows official configuration guidance, automatic
directory discovery remains unresolved, and Claude runtime is untested.

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

For an initial invocation check, explicitly request the export's `expert-` name
and inspect the named delegation as described below. A plausible answer or a
pre-existing alias does not establish that this export ran. Once setup is
verified, naming an expert in every task is optional. In current local Codex,
delegation follows a direct request or applicable project or skill instructions;
see the [subagent guide](https://learn.chatgpt.com/docs/agent-configuration/subagents#orchestration-and-thread-controls).

### Codex: explicit registration

Each Codex TOML contains `name`, `description` and `developer_instructions`.
Both formats also carry [source, version and expert ID comments](../src/README.md#export-provenance)
for people and consuming tools; these do not enter the execution instructions.
The [configuration reference](https://learn.chatgpt.com/docs/config-file/config-reference)
defines `agents.<name>.description` and `agents.<name>.config_file`.

#### Keep a role available in future chats

This manual route follows the official configuration reference; it has not
received a separate catalogue runtime test. Use your configured Codex client.

1. Keep the downloaded TOML and LICENSE at a stable location of your choice.
2. Add a role table to your personal `~/.codex/config.toml`, or to a trusted
   project's `.codex/config.toml` for that project. Merge it with an existing
   table of the same name instead of creating a duplicate. Replace the example
   path with the file's absolute path. For another expert, use its exact `name`
   and `description` from the downloaded file.

   ```toml
   [agents.expert-eliyahu-goldratt]
   description = """\
   Consider Eliyahu Goldratt's perspective, especially on system constraints \
   and overall throughput, including dependencies and shared-resource contention \
   in project delivery. Relevant specialties include Operations management, \
   Project management, Theory of Constraints and Critical Chain project management.\
   """
   config_file = "/absolute/path/to/expert-eliyahu-goldratt.toml"
   ```

   The backslashes join the wrapped description without adding line breaks.
   Relative `config_file` paths resolve from the configuration file that declares
   the role. Personal and trusted project configuration are described in
   [Config basics](https://learn.chatgpt.com/docs/config-file/config-basic).
3. Start a new Codex chat in that project, explicitly request
   `expert-eliyahu-goldratt` as a subagent, and verify the invocation below.

#### Try a role for one CLI invocation

The successful [Codex CLI 0.163.0 check](../evidence/README.md#codex-exec-retry--2026-10-20)
used `codex exec -c` overrides without a persistent registry. This example uses
that registration mechanism. Run it from a Git project with your configured
CLI; replace the absolute path. It applies only to this invocation. Shell line
continuations wrap the description inside its quoted argument.

```sh
codex exec --sandbox read-only \
  -c "agents.expert-eliyahu-goldratt.description='''\
Consider Eliyahu Goldratt's perspective, especially on system constraints \
and overall throughput, including dependencies and shared-resource contention \
in project delivery. Relevant specialties include Operations management, \
Project management, Theory of Constraints and Critical Chain project management.\
'''" \
  -c 'agents.expert-eliyahu-goldratt.config_file="/absolute/path/to/expert-eliyahu-goldratt.toml"' \
  'Use the expert-eliyahu-goldratt subagent to review this plan:
preparation 12 units/hour, assembly 4, packing 10, demand 8.
Explain the constraint and the effect of doubling packing.'
```

For another expert, copy its exact name and description, taking care with shell
quoting, and use its file path. Consumers own model and permission configuration,
registration and lifecycle; this library provides no installer.

#### Confirm that the Codex export ran

Request a subagent explicitly, for example:

```text
Use the expert-eliyahu-goldratt subagent to review this delivery plan.
Identify the main constraint and explain what limits overall throughput.
```

An `@` prefix is not required for this documented natural-language request.

- In the app, open the subagent activity in the main chat and inspect the
  delegated thread. In the interactive CLI, use `/subagents` to inspect it.
  Check that the requested role is `expert-eliyahu-goldratt` and that the child
  received the assignment. See [Managing subagents](https://learn.chatgpt.com/docs/agent-configuration/subagents#managing-subagents).
- For `codex exec`, inspect its delegation output for the requested agent type
  and a completed child response. A successful sample names the
  `expert-eliyahu-goldratt` delegation and contains that child's result; the
  parent merely saying it used Goldratt is insufficient. The recorded check
  above illustrates the evidence boundary.
- If the role is unavailable or no child runs, check the exact registered name,
  description, file path and active configuration scope. Project configuration
  requires a trusted project. Check whether subagents are disabled, then start
  a new chat and repeat the explicit request. If it still fails, report setup
  as unresolved rather than treating the parent answer as a role result.

[Codex also documents](https://learn.chatgpt.com/docs/agent-configuration/subagents#custom-agents)
`.codex/agents/` and `~/.codex/agents/` for project and personal files. Automatic
discovery from a temporary project did not work in the recorded attempt.
Copying a file into those directories alone is therefore not a verified setup
path for this catalogue. The explicit-registration result does not resolve that
separate discovery issue.

### Claude Code: runtime untested

The Markdown exports contain YAML `name` and `description` frontmatter followed
by the shared instruction. Syntax and generated consistency are checked; no
Claude runtime test has run. The following sequence follows the
[official subagent guide](https://code.claude.com/docs/en/sub-agents).

1. Choose scope: `.claude/agents/` in your project makes the role available in
   that project; `~/.claude/agents/` makes it available across your projects.
   Use one location to avoid competing definitions of the same name.
2. Create that directory if needed and copy the downloaded file into it,
   keeping the filename and frontmatter unchanged. For example, from the
   project root, replace the download path:

   ```sh
   mkdir -p .claude/agents
   cp /absolute/path/to/expert-eliyahu-goldratt.md .claude/agents/
   ```

   Keep LICENSE with your copies. For personal scope, use `~/.claude/agents/`
   in both commands instead.
3. Start Claude Code in the project. If you created the `agents` directory
   during an existing session, restart Claude Code; its watcher only covers
   directories that existed when that session started. Existing watched
   directories normally pick up new or edited files without a restart.
4. For this first check, ask Claude to use the `expert-eliyahu-goldratt`
   subagent. You can also type `@` and choose it from suggestions; the manual
   mention is `@agent-expert-eliyahu-goldratt`. See
   [explicit invocation](https://code.claude.com/docs/en/sub-agents#invoke-subagents-explicitly).
5. Inspect the delegation tool row in the transcript. It should show the
   subagent's name and task, for example
   `expert-eliyahu-goldratt(Review the delivery plan)`, followed by its result.
   If the name is unavailable or no delegation appears, check scope, filename,
   YAML name and duplicate definitions, restart if needed and retry explicitly.
   A parent-only answer does not validate the export.

These are documented host features, not additional catalogue runtime results.
After verification, you can let Claude select a suitable available expert from
the task or name one when useful.

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

Library version: **[v1.3.0](https://github.com/shpoont/expert-roles/releases/tag/v1.3.0)**.
The linked GitHub release records publication separately from the version declaration.
One `MAJOR.MINOR.PATCH` version covers profiles, metadata, vocabulary, shared
instructions, templates, tooling and both native formats. The consuming plugin
and other integrations keep independent histories. Individual experts and export
formats do not have separate versions.

The root [VERSION](../VERSION) file is the machine-readable source for export
provenance, set to `1.3.0` for this baseline. Contributions leave it unchanged;
temporary previews use `0.0.0-preview` independently. A version header identifies
a declared library version, not proof of publication or an
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
authorization. D064 authorizes v1.3.0 publication after the required gates;
future releases need their
own owner instruction. Complete the applicable steps below:

### Source contribution

Submit canonical profile/metadata/image changes, necessary vocabulary or tooling
changes, relevant authored documentation and an **Unreleased** changelog entry.
Refresh and include the source catalogues with `src/generate.py --docs`.
Leave `VERSION` and `dist/` unchanged. Routine
expert additions do not require project-wide status, decision or release records.
Validate sources, run the suite and inspect an isolated preview using the
[source commands](../src/README.md#generate-the-catalogue-and-native-files).

Ordinary PRs have no `release` label. CI requires fresh source catalogues,
rejects release-owned edits, builds an
isolated preview and checks its local links, readable images and anchors before
attaching the unreleased **expert-roles-preview** artifact for review. External
URLs are not fetched. The source catalogues track current main; distribution
files reflect the last prepared release. Complete native outputs for unreleased
additions are reviewed in the preview. Merge approved sources under the owner's
authorization; their native exports become distributed additions at release.

### Maintainer release PR

1. Review accepted changes since the last release, compatibility impact and
   evidence; choose the intended version. Create a separate release PR and apply
   the maintainer-controlled `release` label (create that label when first used).
   The label explicitly selects strict release validation; it does not publish.
2. Set `VERSION` to the final stable version, without `v` or a development suffix, for a
   stable release. Finalize the dated changelog entry and update the main README
   and this guide's baseline references. Leave **Unreleased** for subsequent work.
   Run `src/generate.py --release`, then the [checks](../tests/README.md), including export headers,
   local links, native consistency and applicable source/content preservation.
   `VERSION`, both formats' comments and the intended tag must agree.
   Review and remove obsolete exports explicitly if experts were removed or
   renamed; the generator never deletes them. Check the full release locally:

   ```sh
   .venv/bin/python src/generate.py --check
   .venv/bin/python src/check_changes.py --base origin/main --release
   .venv/bin/python -m unittest discover -s tests -v
   ```

3. Commit with the configured signing identity, verify the signature and submit
   the release PR under the owner's authorization. CI requires a greater final
   stable version, exactly one matching dated changelog heading, an Unreleased
   heading and complete output freshness. Require successful review and checks,
   then merge under the owner's authorization. The resulting main push receives
   the same release validation because `VERSION` changed. Both the exact-commit
   **Checks** workflow and its **validate** check must conclude successfully
   before tagging; passing logs or an in-progress check are insufficient.

### Tag and publish

With the release PR merged, owner publication authorization and the exact main
commit's successful hosted checks established:

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

The workflow never tags or publishes automatically. For a manual **Checks** run,
select an ancestor comparison `base` and enable `release` only for a prepared
release. PR runs select that mode from the `release` label; main pushes select
it when their diff changes `VERSION`. Adding or removing the label reruns checks.
Source-only main pushes continue to pass while released artifacts lag behind.

### v1.3.0 release baseline

D064's [release contract](design.md#release-expert-roles-v130) covers the
accepted documentation and tooling changes since v1.2.0. Source catalogues stay
current independently of native releases; new commands update and check them
without changing VERSION or dist. CI checks fresh-preview links, images and
anchors. Setup and contribution guidance is complete, and both source and host
catalogues include the accepted comparison cues.

Version 1.3.0 is a compatible minor increment for these capabilities. All 136
native exports gain the cleaner aligned provenance header and `1.3.0` version;
their parsed fields and instructions, and all expert profiles and visuals,
remain unchanged. The [release page](https://github.com/shpoont/expert-roles/releases/tag/v1.3.0)
and exact-commit Checks establish publication, separately from these declarations.
Prior release records below remain historical baselines.

### Prepared v1.2.0 candidate

Historical preparation checkpoint, completed by D059's
[published v1.2.0 baseline](#v120-release-baseline). The original candidate
included 68 experts, 96 specialties in 14 groups
and 136 native files. Eleven new experts and the README presentation update are
compatible additions; stable paths, existing role settings and shared
instructions are preserved. Existing native exports change only version comments.

The candidate originally depended on [the README source PR](https://github.com/shpoont/expert-roles/pull/12).
That PR and the updated release PR are now merged; the annotated tag and
GitHub release were published after the required checks. The `release` label
selects validation and does not itself authorize publication. See the historical
[candidate evidence](../evidence/README.md#v120-preparation--2026-10-22).

### v1.2.0 release baseline

D059's [publication contract](design.md#publish-expert-roles-v120) is complete.
Source PR #12 and the separate release PR #13 are squash merged. The annotated
`v1.2.0` tag targets
[`c493c44`](https://github.com/shpoont/expert-roles/commit/c493c44bd14c7a54adce74f10bb6ea3c5bfd7359),
after its [Checks run](https://github.com/shpoont/expert-roles/actions/runs/39789914230)
and validation check completed successfully. The stable GitHub release was
published on 2026-10-22. See the [publication evidence](../evidence/README.md#v120-publication--2026-10-22).
Version 1.2.0 is a compatible minor increment for eleven new expert perspectives,
broader specialty coverage, clearer presentation and the contribution/release
separation process.

The [release page](https://github.com/shpoont/expert-roles/releases/tag/v1.2.0)
and [Checks workflow](https://github.com/shpoont/expert-roles/actions/workflows/checks.yml)
record hosted delivery. Require completed exact-commit checks on the release
PR and resulting main before tagging, then verify the annotated tag's target,
latest stable release, VERSION and both native formats. Prior released tags
stay fixed; deployment and installation remain separate.

### Release notes for v1.2.0

**Expert Roles v1.2.0** expands the collection to 68 experts, 96 specialties in
14 groups and 136 Codex and Claude Code files.

- Add Leslie Lamport, Donella Meadows, Nancy Leveson, Daniel Jackson, David
  Parnas, Atul Gawande, Warren Buffett, Jeff Bezos, Bill Gates, Richard Feynman
  and Marie Curie, with public-work references and credited visuals.
- Introduce fourteen specialty concepts while keeping expert identifiers and
  the flat distribution paths stable.
- Lead the README with recognizable experts and task cues, explain independent
  AI interpretation at direct entry points and simplify setup and project
  information. Preserve native descriptions and shared instructions.
- Separate source contributions from maintainer release preparation, with
  isolated previews, explicit generation and CI ownership checks.

Validation requires 55 passing tests, all 141 generated outputs, 68 matching
native pairs, preserved source content and role payloads, and resolving local
references. The 114 previously released exports change only their version
comment. Hosted notes link the successful exact-main check and fixed snapshot
after those results are observed. No new runtime or comparative-effectiveness
assessment is included. Preserve each image's individually credited terms.

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
