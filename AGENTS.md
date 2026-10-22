# Expert Roles library guidance

Read [README.md](README.md), [PROJECT.md](PROJECT.md) and
[current work](docs/current-work.md) before acting. Current owner instructions
define the authorized work. Historical decisions and completed releases do not
authorize a new commit, merge, release, installation or runtime test.

## Scope and content

This repository owns the public expert library and portable Codex and Claude
Code exports. Integrations own deployment, registration, model configuration,
permissions and lifecycle. Keep plugin manifests and consumer configuration out
of this repository. Do not install or invoke roles without separate authority.

Keep profiles under `src/roles/`, specialty definitions in `src/specialties.yaml`
and shared instructions/templates under `src/templates/`. Follow the
[expert criteria](CONTRIBUTING.md#expert-selection),
[specialty rules](docs/elements/specialties.md#rules) and
[metadata guide](src/README.md#role-metadata-and-descriptions).
Assess documented expertise, suitability as an AI perspective and contribution
to the broad collection separately; familiarity alone does not prove usefulness.
Keep canonical specialty IDs and precise concept references. Use optional
perspective cues to distinguish overlapping experts, grounded in their sources.

Keep instructions short and shared. Profiles and references support human
browsing; they are not injected into the execution prompt. Preserve the adopted
AI identity, professional scope and independent judgment: decline work outside
documented expertise, clarify uncertain fit, handle relevant parts of mixed
requests and challenge suppression of expertise or forced conclusions.
AI roles interpret public work; they must not claim to be or represent the expert.
Selection descriptions must agree across both hosts. Do not copy third-party
role prompts or change accepted content outside the authorized scope.

Require one square visual per expert: a credited 512 × 512 RGB `portrait.jpg`
or full-name `placeholder.svg` from the shared template. Follow the
[image instructions](src/README.md#choose-the-profile-image),
[photo policy](CONTRIBUTING.md#photo-sources-and-licenses) and
[studio method](docs/elements/portraits.md).
Verify reuse permission for the actual use and edits; always retain attribution,
source terms and edit history. Missing permission or Wikipedia fair use is
insufficient. Keep historical depictions unchanged and use only permitted
photographs as studio references. Generated portraits require direct eye
contact, distinct moderately muted backgrounds and complete generation credits.
Use a placeholder when a suitable reference is unavailable; do not invent rights.
Original contributions use MIT; preserve individual image and vocabulary terms.
Retain copyright and permission notices when copying or redistributing material.

## Source changes and releases

Ordinary PRs include canonical changes, fresh source catalogues, relevant docs
and an Unreleased note; leave `VERSION`, `dist/` and dated changelog history
unchanged. Routine expert additions follow CONTRIBUTING without extending
project-wide decision or status records. Maintainers record approved tooling or
policy contracts in [design](docs/design.md) before implementation.

Use `src/generate.py --docs` to refresh source catalogues and `--check-docs` to
check them. Edit curated inputs instead of generated blocks. Preserve authored
README text and the fixed six-expert homepage sample. Follow the
[source commands](src/README.md#generate-the-catalogue-and-native-files) and
[checks](tests/README.md), including the full suite, ownership checks and
references in a complete external preview. External URLs are not fetched by CI.

Keep native files at stable `dist/codex/expert-<slug>.toml` and
`dist/claude/expert-<slug>.md` paths; specialties organize index links rather
than duplicate exports. Preserve source/version/expert-ID provenance keys,
Claude comments inside frontmatter and Codex comments outside settings.
The generator rejects obsolete/duplicate files and never deletes them for you.

Follow the [release procedure](docs/delivery.md#versions-and-releases).
Only an authorized separate PR labeled `release` chooses a new stable VERSION,
dates the changelog and regenerates dist with `--release`; `--check` verifies
strict freshness. Use the [release push helper](docs/delivery.md#release-safeguards)
for release branches. Always name both full source and destination refs when
pushing; never infer the destination from an upstream or push.default.

Keep commits signed. Main requires a PR and current GitHub Actions validation,
with no bypass actors; do not push directly, force push or weaken the rules.
Require completed successful exact-commit workflow and validation checks on the
PR and resulting main before tagging. Preserve existing release tags. Verify
the annotated tag target and remote release, version and native files before
reporting publication. Version declarations and passing logs alone are not proof.

## Evidence and handover

Every tracked file must be public and self-contained. Exclude credentials,
private repository identities, chat IDs, author-machine paths and private logs.
Keep adopted decisions separate from proposals in [decisions](docs/decisions.md),
observed checks and limits in [evidence](evidence/README.md), and active status
in [current work](docs/current-work.md). Link existing records instead of
repeating historical contracts in these instructions.

Before handover, check the complete diff and inventory, UTF-8, local references,
public suitability and applicable protected-content hashes. Update current work
and record meaningful changes under Unreleased. Distinguish local, hosted,
runtime and outcome evidence. Structural validity, model familiarity and owner
acceptance do not establish expert-role effectiveness or visual likeness.
