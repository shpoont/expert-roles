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

Canonical sources contain 68 experts, 96 specialties in 14 groups, 50 generated
portraits, five original historical depictions and 13 full-name placeholders.
The eleven reviewed expert contributions are merged. Every source profile has
canonical metadata, a short human-readable README and one square visual.
The adopted [studio-v1 method](docs/elements/portraits.md) is retained.
Previews generate a Codex and Claude Code file for every source profile, with
alphabetical and specialty indexes that link to stable, unduplicated paths.
The published v1.2.0 `dist/` files and generated catalogue sections cover all
68 experts. D059's release is complete; v1.1.0 is the previous release with
57 experts. The
[release record](https://github.com/shpoont/expert-roles/releases/tag/v1.2.0)
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

- **Current status and boundary:** v1.2.0 is published after D057's source
  PR #12 and D058's release PR #13 were squash merged and exact-commit hosted
  checks completed. D060 implements the seven accepted documentation findings;
  independent journey re-reviews and checks pass. D061 adds local link, image
  and anchor checks against the CI preview and simplifies native provenance
  headers. D062 delivered these source changes in verified signed commit
  `43023e2` with successful hosted Checks. D063 corrects the catalogue freeze,
  refreshes the public READMEs and cleans current records. The owner authorizes
  signed commits and a normal push without a release. Keep VERSION and dist at
  the released baseline; review complete native outputs in an external preview.
  Preserve expert content, native descriptions and instruction bodies.
  Installation, integration and role invocation remain separate. Earlier
  portrait, provenance and release decisions and their observed results remain
  in [decisions](docs/decisions.md) and [evidence](evidence/README.md).
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
exports and their indexes live under `dist/`. The released library version is
`1.2.0`, independently versioned from the starter and consuming integrations.
The canonical `VERSION` file and both hosts' provenance comments use `1.2.0`.
The latest stable [release record](https://github.com/shpoont/expert-roles/releases/tag/v1.2.0)
and annotated tag identify `c493c44bd14c7a54adce74f10bb6ea3c5bfd7359`, published
on 2026-10-22. Earlier released tags remain fixed. See the
[release procedure](docs/delivery.md#versions-and-releases).

Continue through [design](docs/design.md), [current work](docs/current-work.md),
[decisions](docs/decisions.md) and [delivery](docs/delivery.md). Historical
contracts, decisions and evidence retain earlier scopes and superseded choices.
