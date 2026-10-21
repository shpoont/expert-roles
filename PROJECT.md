# Current project agreement

## Purpose and intended result

Maintain a public collection of recognizable expert perspectives for AI
assistants. People can browse profiles and contribute improvements independently
of the integrations that consume the collection. Specialties give people and AI
a common vocabulary for matching tasks to experts and organizing the catalogue.
Use the [expert definition](README.md#who-is-included),
[selection criteria](CONTRIBUTING.md#expert-selection) and
[specialty rules](docs/elements/specialties.md#rules).

This is a broad expert catalogue. Assess expert eligibility, suitability as an
AI perspective and contribution to the collection separately. Compare useful
subfields and approaches; equal counts per group are not the target. Research
candidates and possible deferrals remain proposals until the owner selects
roster changes.

## Scope and expectations

The current catalogue contains fifty-seven completed experts, eighty-two
specialties in ten groups, thirty-eight portraits and nineteen full-name
placeholders. Every profile has canonical metadata, a short human-readable
README, one square visual and generated Codex and Claude Code files. All
accepted additions are included; there are no outstanding profile or image
requirements. Future additions follow the same contribution process.

The initial catalogue implementation and owner review are complete. The owner
accepted the compact main README and its fixed six-expert sample, and accepted
the updated fifty-seven-expert catalogue on 2026-10-21. The full catalogue
remains under `src/roles/README.md`. D041 records that acceptance and the documentation
closeout; earlier additions and their checks remain in the
[decision log](docs/decisions.md) and [evidence](evidence/README.md).

Names, specialties and optional perspective cues guide role selection. One
shared instruction defines professional scope, clarification, independent
judgment and attribution. Roles decline tasks outside documented expertise,
handle only relevant parts of mixed requests and challenge forced conclusions
or suppression of expertise. Specialty labels are nonexhaustive. Profiles,
references and visuals support human browsing and are not injected into the
execution instruction. No detailed per-expert brief is required.

Codex TOML and Claude Code Markdown are the initial export formats. The bounded
Codex check passed three cases using explicit invocation-only registrations of
unchanged exports. Automatic directory discovery remains unresolved. Claude
files have structural checks but no runtime validation. These observations do
not establish broad selection reliability or comparative expert benefit.

- **Current status and boundary:** D041's documentation closeout is complete.
  D042's [visitor journey review](docs/design.md#first-time-and-returning-visitor-journey-review)
  is complete: two independent journey reviewers confirmed all five findings
  resolved, and a fresh final review found no blockers in source or captured
  local rendering. Navigation, comparison and contribution guidance improved;
  expert content and native exports are preserved. Relevant checks pass.
  Other candidates remain proposals. On 2026-10-21 the owner accepted the result
  and authorized its initial signed commit under D043. Push, publication, tags
  and release require separate owner instructions.
- **Delivery acceptance:** the catalogue, profiles, contribution process, image
  policy, source schema and usage guidance agree with the initial collection
  and accurately state host-validation limits.
- **Required checks:** the full existing suite, source and generated consistency,
  native syntax and equality, local links, portrait credits and retained reuse
  conditions, public suitability, protected-content hashes and the complete
  proposed Git inventory and diff, including untracked files.
- **Outcome success:** useful expert judgment and a good contributor experience.
  These require representative use and review beyond the completed samples.
- **Integration boundary:** a separate plugin will deploy and manage roles in
  Codex. Consumers own registration, model configuration, permissions,
  parent-level selection, packaging and lifecycle. This library provides source
  content and portable exports; this step adds no deployment tooling or runtime
  tests and changes no consuming integration.

No additional time or budget limits have been agreed. See
[checks](tests/README.md), [evidence](evidence/README.md) and
[delivery](docs/delivery.md).

## People and responsibilities

Leon.id Komarovsky owns direction, scope, licensing, acceptance and release
decisions. Contributors propose changes through the
[contribution process](CONTRIBUTING.md). Future comparative outcome assessments
need an agreed scope, criteria and responsible owner.

## Assumptions and open questions

Expert directories, the simplified profile layout, the expert definition, the
central specialty registry and its rules, full-name placeholders, the shared
instruction and optional perspective cues are adopted. The current native files
are the initial exports, with the host limits stated above. Broader role
usefulness, repeatability, Claude runtime behavior and automatic Codex directory
discovery remain unverified. These follow-ups do not imply missing experts or
portraits in the accepted initial catalogue.

Original profiles, instructions, metadata, documentation, tooling and placeholder
artwork use [MIT](LICENSE). Original contributions use the same license.
Photographs retain their individually credited terms and are excluded from MIT;
always preserve attribution, source, permission and edit history. The
[photo policy](CONTRIBUTING.md#photo-sources-and-licenses) accepts any verified
free reuse grant compatible with the actual use and required image preparation.
Watson's CC BY-NC 2.0 portrait and Ross's CC BY-NC 4.0 video-derived portrait
retain their noncommercial conditions. Referenced
vocabulary labels retain their
[source credits and terms](docs/elements/specialties.md#source-attribution).

## Connected work and baseline

This repository follows [Project Structure v1.0.0](https://github.com/shpoont/project-structure/releases/tag/v1.0.0),
commit `96fdd6bd7950778f5b6c6f8269ab2b82167cb99a`. Expert sources live under
`src/`; the full catalogue is generated in `src/roles/README.md`, with a fixed
six-expert showcase and generated count in the main README. Its release history
is independent of the starter and consuming integrations. No role-library
release or tag has been created.

Continue through [design](docs/design.md), [current work](docs/current-work.md),
[decisions](docs/decisions.md) and [delivery](docs/delivery.md). Historical
contracts, decisions and evidence retain earlier scopes and superseded choices.
