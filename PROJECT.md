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

The v1.4.0 release baseline contains 72 experts, 99 specialties in 15 groups,
54 generated portraits, five original historical depictions and 13 full-name
placeholders. It includes four research and customer-discovery experts added
since v1.3.0. See the [source catalogue](src/roles/README.md) for the collection.
Every source profile has
canonical metadata, a short human-readable README and one square visual.
The adopted [studio-v1 method](docs/elements/portraits.md) is retained.
Previews generate a Codex and Claude Code file for every source profile, with
alphabetical and specialty indexes that link to stable, unduplicated paths.
Version v1.4.0's `dist/` files and source catalogues cover all 72 experts; the
previous v1.3.0 release covered 68. The
[release record](https://github.com/shpoont/expert-roles/releases/tag/v1.4.0)
establishes hosted publication separately from the version declaration.
Portrait acceptance is an editorial decision;
structural validity does not establish likeness. Future additions follow the
same contribution process.

D056 separates source contributions and release preparation; D063 corrects its
catalogue boundary. Ordinary PRs submit canonical sources, fresh source
catalogues, relevant authored documentation and Unreleased notes; they leave
`VERSION` and `dist/` at the previous release. Maintainers update versioned
exports and release records in a separate release PR. Source and catalogue
validation and temporary previews support contribution review; strict
generated freshness is a release gate. See the
[process contract](docs/design.md#separate-contributions-from-release-preparation).

Retain drawings, paintings, sculpture and similar depictions unchanged. The
owner found the first photographic results too close to background removal,
then adopted direct eye contact, an individual moderately muted background and
a new studio sitting. D048 documented the method before applying it across the supported photographic
subjects. Preserve uncertain originals and placeholders.

The initial catalogue implementation and owner review are complete. The owner
accepted the compact main README and its fixed six-expert sample, and accepted
the updated fifty-seven-expert catalogue on 2026-10-21. The full catalogue
remains under `src/roles/README.md`. D041 records that acceptance and the documentation
closeout; earlier additions and their checks remain in the
[decision log](docs/decisions.md) and [evidence](evidence/README.md).

Names, specialties and optional perspective cues guide role selection. One
shared instruction defines professional scope, clarification, independent
judgment and attribution. D066 introduced a source candidate to withhold unsupported
conclusions, complete independent requested parts and state assessment limits.
D070 ties further refinement to source-backed incident reproduction rather than
treating the broad screening as evidence that the original failures were fixed.
Roles decline tasks outside documented expertise and challenge forced conclusions
or suppression of expertise. Specialty labels are nonexhaustive. Profiles,
references and visuals support human browsing and are not injected into the
execution instruction. No detailed per-expert brief is required.

Codex TOML and Claude Code Markdown are the initial export formats. The bounded
Codex check passed three cases using explicit invocation-only registrations of
unchanged exports. Automatic directory discovery remains unresolved. Claude
files have structural checks but no runtime validation. These observations do
not establish broad selection reliability or comparative expert benefit.

- **Current status and boundary:** D077 prepares v1.4.0 from the accepted main
  source after PR #17 was squash merged with successful exact-commit hosted checks.
  D075 applies the tested proposal-goal coverage paragraph to the existing
  consultation draft while preserving its safeguards. The isolated repair
  passed two source-case repetitions and two follow-up checks; the combined
  source passed its own four fresh conversations. The complete source branch
  now passes all 103 offline tests.
  Both native formats match the source for all 72 experts, and the complete
  preview's local references pass. The editorial cycle and fresh comparative Pro
  review are complete, with no blocking findings. The pilot answer has a
  verdict-clarity qualification; recognizing a valid alternative representation
  remains a useful follow-up case, rather than demonstrated coverage.
  See the [contract](docs/design.md#goal-coverage-in-proposal-reviews) and
  [bounded evidence](evidence/README.md#goal-coverage-repair-and-application--2026-10-29).
  D071–D074 retain their historical results; the software/dinner scope example
  does not reproduce the source consultation issue. D077 authorizes versioned
  export regeneration, a separate release PR, its merge and publication after
  the required gates. Preserve all accepted canonical sources and existing
  selection metadata. Installation and deployment remain separate.
- **Delivery acceptance:** the catalogue, profiles, contribution process, image
  policy, source schema and usage guidance agree with the initial collection
  and accurately state host-validation limits.
- **Required checks:** the full suite, source validation and isolated previews;
  contribution ownership or strict release consistency as appropriate;
  native syntax and equality, local links, portrait credits and retained reuse
  conditions, public suitability, protected-content hashes and the complete
  proposed Git inventory and diff, including untracked files. Distribution checks
  cover generated indexes, stable paths, duplicate or obsolete files, and
  byte-for-byte preservation of the moved native exports.
- **Outcome success:** useful expert judgment and a good contributor experience.
  These require representative use and review beyond the completed samples.
- **Integration boundary:** a separate plugin will deploy and manage roles in
  Codex. Consumers own registration, model configuration, permissions,
  parent-level selection, packaging and lifecycle. This library provides source
  content and portable exports. The isolated evaluation fixtures add no
  deployment tooling and change no consuming integration.

The completed integration checks followed the attempt limits in the
[repair contract](docs/design.md#goal-coverage-in-proposal-reviews). See
[checks](tests/README.md), [evidence](evidence/README.md) and
[delivery](docs/delivery.md).

## People and responsibilities

Leon.id Komarovsky owns direction, scope, licensing, acceptance and release
decisions. Contributors propose changes through the
[contribution process](CONTRIBUTING.md). Future comparative outcome assessments
need an agreed scope, criteria and responsible owner.

## Assumptions and open questions

Expert directories, the simplified profile layout, the expert definition, the
central specialty registry and its rules, full-name placeholders and optional
perspective cues are adopted. The shared instruction remains one portable
template. D074's 382-word draft preserves the previous consultation safeguards;
D075 adds the tested 57-word proposal-review check without changing those
paragraphs. Isolated repair evidence does not establish the combined prompt's
behavior. Current source integration, structural checks and model evidence
must retain their separate scope. Historical screening results apply only to
their archived conditions and do not establish broad role effectiveness.
The retained native files have the host limits stated above. Broader role
usefulness, repeatability, Claude runtime behavior and automatic Codex directory
discovery remain unverified. These follow-ups do not imply missing experts or
portraits in the accepted initial catalogue.

Original profiles, instructions, metadata, documentation, tooling and placeholder
artwork use [MIT](LICENSE). Original contributions use the same license.
Photographs and generated adaptations of licensed references retain their
individually credited terms and are excluded from MIT. Original generated
contributions follow MIT to the extent rights can be granted;
always preserve attribution, source, permission and edit history. The
[photo policy](CONTRIBUTING.md#photo-sources-and-licenses) accepts any verified
free reuse grant compatible with the actual use and required image preparation.
The new Watson selection uses separate CC BY-SA 2.0 photographs; previous
copies of her former CC BY-NC 2.0 portrait retain their terms. Ross's CC BY-NC
4.0 portrait and the newly credited noncommercial sources retain their
individual conditions. Referenced
vocabulary labels retain their
[source credits and terms](docs/elements/specialties.md#source-attribution).

## Connected work and baseline

This repository follows [Project Structure v1.0.0](https://github.com/shpoont/project-structure/releases/tag/v1.0.0),
commit `96fdd6bd7950778f5b6c6f8269ab2b82167cb99a`. Expert sources live under
`src/`; the full catalogue is generated in `src/roles/README.md`, with a fixed
six-expert showcase and generated count in the main README. Ready-to-use
exports and their indexes live under `dist/`. Library version `1.4.0` is
independent of the starter and consuming integrations. The canonical `VERSION`
file and both hosts' provenance comments use `1.4.0`.
The [versioned release record](https://github.com/shpoont/expert-roles/releases/tag/v1.4.0)
and annotated tag establish publication separately from those declarations.
The previous v1.2.0 tag remains fixed at
`c493c44bd14c7a54adce74f10bb6ea3c5bfd7359`. See the
[release procedure](docs/delivery.md#versions-and-releases).

Continue through [design](docs/design.md), [current work](docs/current-work.md),
[decisions](docs/decisions.md) and [delivery](docs/delivery.md). Historical
contracts, decisions and evidence retain earlier scopes and superseded choices.
