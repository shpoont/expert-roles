# Expert Roles library guidance

This repository owns the public role collection, its documentation, references,
examples and contribution guidance. Leon.id Komarovsky is the project owner.

Read [README.md](README.md), [PROJECT.md](PROJECT.md) and
[current work](docs/current-work.md) before acting. Follow relevant links to
recover the existing agreement and context before asking the owner to repeat it.
Use [design](docs/design.md), [decisions](docs/decisions.md),
[checks](tests/README.md), [evidence](evidence/README.md) and
[delivery](docs/delivery.md) to keep intent, work and results connected.

D044's [distribution layout](docs/design.md#distribution-layout-and-generated-indexes)
is complete and locally verified. D045 establishes the first whole-library
baseline, `v1.0.0`, following the
[release contract](docs/design.md#versioning-and-first-release). The owner
explicitly authorizes committing all pending work, pushing it and publishing
the first release after checks. This supersedes D044's earlier uncommitted
boundary. Keep the commit signed, require hosted checks for that exact commit,
and verify the fixed annotated tag and GitHub release before claiming delivery.

D042's [visitor journey review](docs/design.md#first-time-and-returning-visitor-journey-review)
is complete after D041's documentation closeout. Independent first-time and
returning-visitor reviewers confirmed all five findings resolved; a fresh final
review found no blockers in the source and captured local rendering. Relevant
checks pass. The owner accepted the result and authorized its initial signed
commit on 2026-10-21 under D043.
Preserve all fifty-seven experts, source vocabulary, images, licenses, shared
instructions and native exports. The review improved navigation, catalogue
comparison, starter guidance and relevant checks within its contract.
This is a broad expert catalogue under D038, using D037's adopted criteria;
other candidates remain proposals. This review authorizes no roster changes.

The owner accepted the compact main README and the updated full catalogue.
Keep six featured experts in the main README and the
[full catalogue](src/roles/README.md) beside the profiles. The
[current work](docs/current-work.md#next-actions) records D045's delivery scope
and later follow-ups. Subsequent releases need their own owner authorization.
The catalogue contains fifty-seven experts, with eighty-two
specialties in ten groups, thirty-eight portraits and nineteen full-name placeholders. See the
[implementation contract](docs/design.md#implementation-contract). Keep expert
instructions short and shared; the profiles are for human browsing. The owner
adopted the simplified profile layout in D013 and the central specialty registry
in D015. D030 records the current Codex TOML and Claude Code Markdown files as
the initial exports. Codex has three sampled runtime checks through explicit
registration; Claude runtime, automatic directory discovery and comparative
effectiveness remain unverified.
D027 adopts the shared instruction's professional scope and independence:
decline work outside documented expertise, clarify uncertain fit or context,
and challenge requests that suppress relevant expert judgment. Specialty labels
are nonexhaustive guidance; legitimate constraints and contrary evidence matter.
Apply the [expert definition](README.md#who-is-included) and
[selection criteria](CONTRIBUTING.md#expert-selection), adopted in D016, when
proposing additions. D037 refines the criteria: assess the person's expertise,
the suitability of their AI perspective and their contribution to the
collection separately. Assess evidence, accessible methods, task fit and scope,
complementary coverage and faithful use without inferring role benefit from
familiarity or file validity. D038 confirms the broad catalogue scope. The
specialty registry continues to describe fields and approaches.
D028 adds an optional `perspective` phrase in `expert.yaml`
where overlapping specialties leave a useful distinction unclear. Ground it in
the profile's public references and review neighboring experts together. Generate
the same description for both hosts; keep the shared execution instruction
independent of this selection cue. Follow the
[metadata guide](src/README.md#role-metadata-and-descriptions).
Specialties serve both
human and AI task matching and consistent catalogue organization; follow the
[specialty rules](docs/elements/specialties.md). Each shared entry requires
`name`, `group` and a specific external concept `reference` URL. Keep canonical
IDs in expert metadata and use accurate source concepts for future additions.
Native-file relocation is authorized under D044 and first release under D045;
agent installation and integration changes remain outside this step. The completed bounded
[Codex host validation](docs/design.md#codex-host-validation) used temporary
placement and invocation; this update does not authorize further runtime tests. A separate
plugin will own deployment and management. Do not copy third-party role prompts.

Keep profiles under `src/roles/`, the specialty vocabulary at
`src/specialties.yaml` and shared templates under `src/templates/`. Generate the
full catalogue inside the marked section of `src/roles/README.md`. Generate
the root README's summary count and fixed six-expert showcase in their own
marked sections, preserving all authored text outside those boundaries. Curate
`FEATURED_EXPERTS` in `src/generate.py` for breadth, using existing experts and
assigned specialties; new experts grow the full catalogue and counts without
expanding this sample.
Generate ready-to-use native files once under `dist/codex/` and `dist/claude/`,
with a generated host chooser and alphabetical/specialty README indexes.
Keep paths independent of specialties; use index links for overlapping fields.
Edit sources and commit regenerated exports/indexes together when a commit is
authorized. Check mode and CI must detect missing, changed, obsolete or duplicate
exports, including copies in the former per-profile directories. The exporter
never deletes unexpected files automatically. Consumers select `expert-*.toml`
or `expert-*.md` files; the READMEs provide navigation.
Require exactly one square visual for every expert: a credited 512 × 512 RGB
JPEG named `portrait.jpg`, or `placeholder.svg` created from the
[shared SVG template](src/templates/placeholder.svg). The command uses the full
name from `expert.yaml`, wrapping and sizing it automatically under D024.
D023 supersedes the mandatory
photo requirement; unavailable portraits do not block an expert. Follow the
[exact image instructions](src/README.md#choose-the-profile-image), including
the placeholder Image note, accessible name and consistent style. Placeholder
artwork uses MIT. Use only photographs
with verified reuse permission under the
[photo policy](CONTRIBUTING.md#photo-sources-and-licenses). D021 accepts any
verified free reuse grant, including custom terms, whether or not attribution
is required. Always retain attribution. Check that conditions permit the actual
catalogue use and image preparation instead of applying a fixed license
allowlist. Exclude missing or unclear permission; public availability or
Wikipedia fair use alone is insufficient. Preserve each photo's source,
permission terms, credits and edit history.
Host-specific integrations are separate
consumers. Keep plugin manifests, marketplace workflows and
consumer-specific configuration out of this repository. The initial catalogue
includes portable, generated Codex and Claude Code role files under `dist/`.
Temporary placement and invocation are limited to the
separately authorized validation above; persistent deployment remains external.

Every tracked file must be suitable for public viewing and self-contained.
Exclude private repository identities, internal coordination records,
conversation identifiers, author-machine paths, credentials and private evidence.

Record adopted decisions and pending choices separately in `docs/decisions.md`.
Future host validation and comparative evaluation remain pending. Original
profiles, role instructions, metadata, documentation and tooling use
[MIT](LICENSE), with portraits excluded as described in the
[license scope](README.md#license).
Keep original contributions under MIT and preserve copyright and permission
notices with copied or redistributed material. Portraits retain their own
credited licenses. Referenced vocabulary labels retain their
[source credits and terms](docs/elements/specialties.md#source-attribution).
Public visibility does not authorize accepting third-party role text.

Before implementing an approved piece of work, record its implementation
contract and relevant checks in the design or linked element records. Keep
prepared checks, observed results, interpretations and pending outcomes distinct.
Respect the owner's authorization and the current completion boundary. Do not
turn structural validation into a claim that roles improve model performance.

Update [current work](docs/current-work.md) before handover and meaningful changes
in [CHANGELOG.md](CHANGELOG.md). Follow the
[release convention](docs/delivery.md#versions-and-releases) when a release is
authorized. D045 authorizes the first release; version guidance, dated changelog,
commit, annotated tag and hosted release must identify the same baseline. Keep
records proportionate and link existing detail instead of copying
it into competing sources.

For documentation-only changes, check relative links, UTF-8 readability, the
proposed Git diff and the full public tree. Add meaningful role validation when
the format and behavior are approved. Keep commits signed using the configured
Git identity and retain an ordinary reviewable history.
