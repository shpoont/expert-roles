# Tests and assessments

Checks follow the [project expectations](../PROJECT.md#scope-and-expectations)
and [implementation contract](../docs/design.md#implementation-contract).

## Studio portrait refresh (D047, D048 and D049)

D048's [studio-v1 rollout](../docs/design.md#reproducible-studio-portrait-method-and-catalogue-rollout)
adds stable per-expert background recipes, reference hashes, an exact shared
prompt and deterministic preparation. The portrait helper tests cover individual
palettes, pinned samples, changed input hashes, public-record boundaries, EXIF
orientation, repeatable encoding and explicit replacement. Review direct eye
contact and background distinctness visually; file tests cannot establish them.

D049 adds a copyable credit block and provenance validation to both normal
generation and read-only check mode, so the existing CI command enforces it.
Tests reject missing/blank fields, inconsistent disclosures, malformed dates,
unlinked terms and stable-recipe drift without partial exporter writes. Each
Source entry needs its own terms; mixed-reference tests prevent a public-domain
notice from masking another reference's missing declaration. A
synthetic new-profile fixture copies the contributor starter, creates a
placeholder, prepares a master, applies the shared credit block and checks the
new native pair while preserving existing role bytes. It does not call an image
model or establish independent agent reliability. The separate
[fresh-session walkthrough](portrait-walkthrough.md) completed one temporary
Grace Hopper case with actual built-in generation, both exports and rendered
review. Its [evidence](../evidence/README.md#independent-portrait-contribution-walkthrough--2026-10-21)
does not establish repeatability or owner acceptance.

Follow the [portrait contract](../docs/design.md#studio-portrait-refresh-for-owner-review)
and [workflow](../docs/elements/portraits.md). Check one valid active visual per
expert, visible and accessible image-type labels, complete supplied-reference
credits and applicable adaptation terms. Compare candidates with the source at
profile and catalogue sizes, retaining photographs or placeholders when uncertain.
Historical depictions retain their original image bytes and credits; do not
generate replacements. Name-only candidates remain outside accepted portrait replacements. All experts
need an explicit generated-or-retained outcome.

Run the complete suite and generator check; verify all 114 native file bytes,
57 metadata files, vocabulary, shared instruction and non-image profile content
against the baseline. Review links, the complete diff and public suitability.
Commit the reviewed refresh only when authorized; do not push without separate
authorization. Rendered checks and visual inspection
are evidence of presentation, not identity verification or owner acceptance.

## Profile prototype checks

| Check | Observable pass condition |
| --- | --- |
| Source layout | Profiles, specialties and templates live under `src/`; ready-to-use exports and generated indexes live under `dist/`. Generator paths, fixtures and links resolve in the adopted layout. |
| Profile coverage | Each completed expert in the catalogue has a linked profile, valid photo or name visual and two portable native files. Accepted drafts outside the current addition step are accurately recorded. Missing photographs do not block a profile that uses standard name. |
| Expert selection guidance | The main README defines an expert, and the linked contribution criteria cover established expertise, accessible work, useful task fit and a preference for public familiarity within the field. Fame alone is insufficient; formal credentials are optional, and living and historical people may qualify. Existing profile fields support editorial selection, without claims of model familiarity or effectiveness. |
| Profile layout | Every completed profile and the starter show linked specialties once, a short introduction, early role-file/setup links and one independent-AI notice. Suggested uses and references precede visible image provenance: a Photo credit for photographs or an Image section for generated images and placeholders. A collapsed Source files footer retains metadata and shared-instruction links. |
| Metadata | Names and specialty lists are nonempty, identifiers are unique and all specialty references exist. An optional perspective is nonempty authored text; malformed values and unknown fields are rejected before generation or placeholder writes. Registry entries require name, group and an absolute HTTP(S) concept reference; duplicate names/concepts and invalid references are rejected before writes. |
| Selection descriptions | An optional perspective distinguishes an expert's emphasis within overlapping specialties, grounded in the profile's public work. Both host descriptions match, retain all labels and remain nonexhaustive. Omission is supported; quotes, Unicode and folded text survive correctly. The phrase also appears beneath catalogue specialty labels but does not enter execution instructions. |
| Specialty guidance | One linked rules document covers task matching, shared terms, source selection, overlap and grouping. Source meanings and public work support the assigned specialties; concept matching is editorial review, not an inference from URL validity. |
| Shared vocabulary | Experts reuse canonical specialty IDs and labels. Only assigned specialties appear in the catalogue, grouped consistently and sorted by name. Reference URLs stay out of native instructions. |
| Shared instruction | Each native instruction is exactly the shared template with the expert name and labels substituted. |
| Breadth | Specialty labels are nonexhaustive guidance; the task and evidence determine the focus within documented expertise. |
| Professional scope and independence | The shared instruction requires a fit/context check, out-of-expertise decline, bounded handling of mixed requests, clarification, independent challenge and transparent attribution. Generated text can be checked structurally; actual behavior needs separate assessment. |
| Catalogue growth and display text | The expert table has three columns and one row per expert; accepted punctuation renders as text without changing cells or links. |
| README entry points | The main README has exactly six featured experts in two rows, a generated total and a full-catalogue link. The full alphabetical and specialty catalogue lives in src/roles/README.md. Adding an expert grows that catalogue and both counts without enlarging the sample. Authored text outside each marker pair survives; missing, duplicate, reversed, overlapping or nested boundaries fail before writes. Invalid curated sources also fail before writes. |
| Native syntax | Codex files parse as TOML with the three required fields; Claude files have valid YAML frontmatter and a nonempty instruction body. |
| Generated consistency | Exporter check mode reports no missing, changed or obsolete generated role files, distribution indexes or catalogue content. It rejects legacy and nested duplicate exports before writes and never deletes them automatically. |
| Invalid input | An invalid profile sorted after a valid profile is rejected before outputs are written; malformed metadata is also rejected. |
| Multiple specialties | Both host files retain Goldratt's identity and all four assigned specialty labels. |
| Navigation | Relative Markdown file links, local HTML image references, heading anchors and explicit canonical specialty anchors resolve. Named specialty links land on the exact row; IDs remain stable across label/group changes. |
| Images | Every expert has exactly one of portrait.jpg (a decodable 512 × 512 RGB JPEG) or placeholder.svg (matching the shared 512 × 512 SVG template and complete expert name). Missing, ambiguous, malformed or altered visuals fail before generated outputs are written. The catalogue selects the correct filename and labels placeholders accurately. |
| Placeholder creation | The documented command reads the full name from expert.yaml, wraps and sizes it to fit, escapes XML text and creates only that profile's SVG. It rejects invalid names/arguments and never overwrites a photo or SVG. An isolated copy/fill/create/generate/check trial completes the starter. Full-name and photographic variants render at both display sizes without changing native instructions. |
| Photo reuse | Accept any verified free reuse grant, with or without an attribution requirement, including custom terms. Manual review confirms compatibility with the actual catalogue use and required image preparation; license categories alone do not decide eligibility. Missing or unclear permission is excluded. Profiles and the starter always retain available creator, title and source attribution, license/version or other permission terms, required notices and edit history. Applicable conditions are followed; modified CC BY-SA portraits retain their license. |
| Library license | Root LICENSE matches the standard MIT text and Copyright (c) 2026 Shpoont. MIT covers original material, the SVG template, name artwork and original generated contributions to the extent rights can be granted. Photographs and adaptations of licensed references retain separately recorded terms. Portrait replacements preserve source attribution, conditions and change notices; standalone role copies retain MIT notices. |
| Public suitability | Proposed files contain no credentials, private repository identities, coordination identifiers or author-machine paths. |
| Handover | Current work, scope, decisions, contribution guidance and delivery accurately describe the initial catalogue and documented host limits. |
| Direct use | A linked central section explains obtaining an export, tested Codex registration, untested host paths and the separate deployment responsibility. Explicit expert requests are optional; exact names are useful for targeted requests and invocation validation. |
| Starter profile | The documented starter can be copied, completed with name and generated into a linked catalogue entry and valid native files without changing the real expert collection. Exact instructions also explain replacing name with a permitted photo and restoring name. |
| Git boundary | Diff has no whitespace errors. Follow the owner's current authorization. D052 authorizes one signed squash commit into local main and v1.1.0 preparation, with no push, tag or publication. Deployment remains separate. Temporary host validation follows its own contract below. |

Run the exporter in check mode as described in [src](../src/README.md).
Record actual results, baseline and limitations in
[evidence](../evidence/README.md). Review the rendered catalogue and profiles
before handover; source validity alone does not establish a good presentation.

## Release checks

Follow the [release procedure](../docs/delivery.md#versions-and-releases) and
the current implementation contract. Version references in the README,
delivery guide, dated changelog, intended tag and release title must agree.
Distinguish a prepared candidate from the latest published version; retain
Unreleased for future changes. Check compatibility and all changes since the
previous released tag, including work already delivered on main.

For D052, follow the [v1.1.0 preparation contract](../docs/design.md#local-squash-merge-and-v110-preparation).
The actual squash must apply cleanly. Compare all 173 protected files, 57
selected visuals and 57 individual profile READMEs against the accepted rebased
portrait tree. Release preparation changes documentation only; all feature
implementation and generated bytes remain unchanged. Existing native files and
the shared instruction also match pre-merge main.

Run the full suite, read-only generation check, native equality, local links,
UTF-8/public suitability, preservation and complete staged Git diff checks
before the signed commit. Verify its signature, single main parent and clean
local tree. D052 includes no push, tag or publication, so hosted checks and
release readback remain pending.

When publication is authorized, require hosted Checks to pass on the exact
release commit. Verify the annotated tag target, remote branch/tag, GitHub
release version/title/body/Latest state, and clean local tree. No host
installation, invocation or consumer update follows from library publication.
The historical [D045 contract](../docs/design.md#versioning-and-first-release)
records the already delivered v1.0.0 release.

## Distribution layout (D044)

Follow the [distribution contract](../docs/design.md#distribution-layout-and-generated-indexes).
Each expert has exactly one native file per host, with no legacy per-profile
copy or specialty subdirectories. Compare all 114 relocated files byte-for-byte
against the committed baseline and confirm source metadata, visuals, templates,
profile prose/credits and the generated catalogue sections are preserved.

Regression checks cover all three generated distribution indexes, alphabetical
sorting by display name, multiple specialties and groups pointing to one file,
hidden unused specialties/groups and stable paths/anchors after classification
changes. Check mode must detect missing or edited indexes and both native
formats without writing; generation must reject unexpected legacy or nested
exports before changing any file. Authored profile and starter download links
must target `dist/`.

Run the full suite and `src/generate.py --check`, native syntax/equality, complete
local-link/anchor checks, UTF-8/public-suitability and Git diff checks. The
[CI workflow](../.github/workflows/checks.yml) runs the suite and read-only
consistency check on pull requests and main-branch pushes; it makes no commits
and publishes no artifacts. Local verification does not establish a hosted CI
result. Record observed results and limits in [evidence](../evidence/README.md).
Commit sources and generated outputs together only when authorized; runtime
tests and releases are separate.

## Four requested expert additions

For [D031's addition contract](../docs/design.md#four-requested-expert-additions),
review all four experts against the existing definition, linked primary work
and neighboring perspectives. Confirm the three new specialty meanings and
assignments, verify both new portraits' grants and credits, and check the two
name placeholders against the shared template. Review the rendered catalogue
and four profiles. Run the existing suite, generated consistency, native-file
syntax/equality, local-link, public-content and Git checks. Compare every
pre-existing expert directory, shared template, generator and test file with
the pre-addition hashes. Preserve earlier decision and evidence text; confirm
an empty index and unchanged HEAD. No new runtime test is required or authorized.

Apply the same source, generated-file, image, navigation, preservation and Git
checks to [D032's Rybka addition](../docs/design.md#zdeněk-rybka-addition), reusing
the established specialty and full-name placeholder without changing templates.

Apply those checks to [D035's Peterson addition](../docs/design.md#jordan-peterson-addition),
including the new Personality psychology concept and the photograph's source,
CC BY-SA 3.0 attribution and recorded crop. Preserve earlier expert directories,
shared templates, generator, tests and the fixed six-expert README sample.

Apply those checks to
[D036's four additions](../docs/design.md#hawkins-premack-levels-and-frawley-additions).
Verify their fit against linked public work, the four new concept meanings and
the Animal behavior group, Hawkins's CC BY-SA 2.0 source and edits, and the
three full-name placeholders. Preserve all thirty-seven earlier expert
directories, the shared instruction, templates, code, tests and README sample.
Review the four rendered profiles and full catalogue; no runtime invocation
is included.

Apply those checks to
[D039's ten additions and Rybka removal](../docs/design.md#ten-expert-additions-and-rybka-removal).
Verify all ten profiles against their public work and all thirteen new concept
mappings. Check Edmondson's CC BY-SA 2.0 source and earlier crop credit, Ross's
MIT CC BY-NC 4.0 video source and frame/crop credit, and the eight full-name
placeholders. Confirm exactly Rybka's five files are removed, all other forty
expert directories retain their bytes, both native formats agree, and the fixed
README sample is unchanged. Preserve historical inclusion records, replacing
the removed profile link with its public references. Review the rendered new
profiles and fifty-expert catalogue; no runtime invocation is included.

## Selection criteria and company coverage review (D037)

For [D037's selection update](../docs/design.md#selection-criteria-and-company-coverage-review),
check consistency with the short expert definition, separate source-backed
eligibility from initial selection priorities and observed role benefit, and
confirm additions and deferrals remain proposals. Run generated consistency,
local-link, UTF-8, public-content, full-diff and Git checks. Compare every
expert directory, registry, shared template, code and test file with the
pre-update hashes; reuse the existing code-test results while these stay unchanged.

For [D038's scope clarification](../docs/design.md#broad-catalogue-scope-clarification),
check that current guidance describes a broad expert catalogue and supersedes
deferral recommendations based on the earlier narrow interpretation. Apply the same
documentation and preservation checks without changing the roster or exports.

## Completed documentation review (D030)

The completed [documentation cleanup](../docs/design.md#documentation-cleanup-and-final-checks)
checked guidance for the thirty-one-expert baseline and initial export
formats, distinguishing the sampled Codex registration result from unresolved
discovery and untested Claude runtime, and keeps deployment external. Remove
temporary contributor restrictions while retaining the owner's no-commit
constraint in project guidance. Preserve historical decision and evidence text.

Run the existing suite and exporter check; validate both hosts' actual files,
all local references and public content. Compare protected content with the
pre-cleanup hashes, review the complete proposed Git inventory and diff,
including untracked files and portrait credits, and confirm an empty index and
unchanged HEAD. Retain observations in [evidence](../evidence/README.md).

## Codex host validation

The owner authorized the three-case
[Codex check](../docs/design.md#codex-host-validation), using unchanged exports
in a temporary project and fresh sessions. Observe actual custom-agent calls,
description-guided selection, an in-scope challenge and an out-of-scope decline.
Retain private raw evidence and a public summary of results and limitations.
This exception does not authorize persistent deployment or plugin work.
The initial attempt was blocked at catalogue-role discovery. The subsequent
`codex exec` retry used invocation-only name/description/file registrations;
all three sampled cases met their expected results, with native calls confirming
the exact catalogue agents. See the
[retry results and limits](../evidence/README.md#codex-exec-retry--2026-10-20).
Automatic directory discovery remains unresolved; this is not a broad benchmark.

## Role benefit assessments

The bounded Codex check above is complete. Claude launches and comparative
benefit assessments remain outside the current task. Broader discovery,
runtime reliability and useful expert judgment remain unverified.
Future behavioral checks should cover an in-scope assignment, clear
out-of-expertise work, mixed requests, uncertain fit or missing essential
context, forced conclusions, suppression of expert judgment and legitimate
constraints or contrary evidence. Also check work supported by the expert's
public record but absent from the specialty tags. Expected responses follow
the [shared instruction](../src/templates/invocation.md). The three samples above
cover only a clear heuristic-review match, one forced conclusion and one
out-of-expertise decline; the remaining scenarios and repeatability are untested.
Future selection checks should also cover clear matches, overlapping expertise,
irrelevant name or topic mentions, mixed requests, and legitimate expertise
absent from the description's examples. Assess the parent choice and distinct
assignments, including when no role or clarification is appropriate. Description
review and structural checks alone do not establish selection reliability.
Before assessing benefit, agree representative tasks, comparison conditions,
criteria and responsibility. Structural checks do not establish model uplift.

## Previous structure alignment

The completed documentation-only adoption checks are retained in
[evidence](../evidence/README.md#project-structure-adoption--2026-10-18).

## Seven philosophy additions (D040)

Apply the existing checks to the [seven additions](../docs/design.md#seven-philosophy-additions).
Review each expert's fit, references, historical attribution limits and
distinguishing perspective. Confirm the eight concept mappings and Philosophy
group. Verify the image terms separately from the underlying artwork: Socrates'
photograph retains CC BY-SA 2.5, Aristotle's photographer supplies a public-domain
dedication, four historical two-dimensional portraits are public domain, and
Popper's archive photograph uses LSE Library's explicit Flickr reuse statement.
Retain credits, source links and crops; label later artistic depictions.

Run the existing suite, generated/native consistency, image, navigation, UTF-8,
public-content and Git checks. Preserve the other fifty expert directories,
all earlier registry definitions, templates, generator, tests, license and
authored main README; only its generated counts change. Review the rendered
catalogue and seven profiles. No runtime invocation or deployment is included.

## Accepted catalogue documentation closeout (D041)

For the [closeout contract](../docs/design.md#final-documentation-closeout-for-the-accepted-catalogue),
confirm that current guidance records owner acceptance, completed implementation
and commit readiness without stale pending-review requests. Keep historical
records and runtime limitations distinct from current work. Verify current
counts and evidence links, including both noncommercial portrait conditions.

Run the existing suite, generated/native consistency, image, local-reference,
UTF-8, bounded public-content and complete Git-inventory/whitespace checks.
Compare the entire tree with the accepted baseline: only current guidance and
linked design, decision, test-guidance, changelog and evidence records may
change. Every expert file, source registry, shared template, generator, code
test, requirement, license and both catalogue entry points must retain its
bytes. Confirm an empty Git index and unchanged HEAD. Existing render acceptance
remains applicable while all catalogue and visual content is preserved.

## Visitor journey review (D042)

Walk through first-time discovery, expert comparison, profile/file access and
setup, then known-name retrieval, precise specialty alternatives, changes and
contribution. Use independent reviewer feedback and saved fresh screenshots;
re-review supported fixes and run an independent final review. Separate local
Markdown rendering from hosted GitHub, actual users and assistive-technology
outcomes. Long-code overflow in a preview alone is not a repository defect.

Run the existing suite, generated/native equality, image, complete local-link,
explicit-anchor, UTF-8, public-tree and Git checks. The navigation regression
check must preserve specialty targets when labels or groups change. Confirm
all fifty-seven metadata records, visuals and native pairs remain unchanged;
profile README changes are limited to specialty destinations. Keep the fixed
six-expert sample and previous decision/evidence bodies. Record results in
[evidence](../evidence/README.md); do not invoke or install roles.
