# Delivery and handover

## Review the catalogue

Start at the [full catalogue](../src/roles/README.md), then open individual
profiles and their Codex or Claude Code files. The fifty-seven completed profiles
use one simplified layout, eighty-two shared specialties, thirty-eight credited
portraits and nineteen full-name placeholders. All accepted additions are included.

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

Codex TOML and Claude Code Markdown are the initial export formats. The current
work is uncommitted at the owner's request; no role-library release is made.

## Use a native role

Role files contain the expert's name, selection cues and shared instruction.
Profiles and references support browsing; include any source material the task
needs in the assignment.

1. Open an expert in the [catalogue](../src/roles/README.md) and choose the
   **Codex** or **Claude Code** file. From a checkout, use the generated file.
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

The owner accepted the compact main README and the updated fifty-seven-expert
catalogue. The initial implementation and rendered review are complete; no
accepted profile, required portrait, layout or specialty decision remains open.
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
commit on 2026-10-21 under D043.
The [latest additions](../evidence/README.md#seven-philosophy-additions--2026-10-21)
record the fifty-seven-expert sources, images, native files and local rendering;
earlier decisions and evidence retain their historical scopes. Acceptance of
the rendering is separate from structural checks and observed runtime behavior.

Automatic Codex directory discovery, Claude runtime validation, deployment and
comparative role benefit remain later consumer or assessment work. They do not
block committing this accepted catalogue. No new invocation or deployment is
included. D043 supersedes the earlier no-commit restriction for this accepted
tree. Push, publication, tags and releases require separate owner instructions.

Original sources, role instructions, tooling and name artwork use [MIT](../LICENSE).
Photographs retain the terms and credits on their profiles; they are excluded
from MIT. Always preserve attribution, source, permission notices and edit
history, and follow each image's conditions. Watson's CC BY-NC 2.0 portrait and
Ross's CC BY-NC 4.0 video-derived portrait retain their noncommercial conditions.
The collection does not promise uniform photo reuse rights. Vocabulary labels retain their
[source credits and terms](elements/specialties.md#source-attribution).
Follow the [photo policy](../CONTRIBUTING.md#photo-sources-and-licenses) and
[image instructions](../src/README.md#choose-the-profile-image) for changes.

## Versions and releases

The role library has no released baseline yet. Its release history is independent
of the starter and consuming integrations. Record meaningful changes under
**Unreleased** in [CHANGELOG.md](../CHANGELOG.md).

For an approved release, use `MAJOR.MINOR.PATCH`: major for incompatible changes,
minor for compatible additions and patch for corrections that preserve the
intended behavior and agreements. Review the intended scope and evidence,
finalize the dated changelog entry and version references, and commit the exact
contents before creating an annotated `vMAJOR.MINOR.PATCH` tag. Released tags
remain fixed; a hosted release, when used, refers to the same tag. Committing
catalogue changes does not create a release or tag.

## Outcomes and learning

No comparative role-benefit or contributor outcome assessment has run. Agree
representative tasks, comparison conditions, criteria and responsibility before
such assessment. Keep future observations in [evidence](../evidence/README.md)
and current follow-ups in [current work](current-work.md).
