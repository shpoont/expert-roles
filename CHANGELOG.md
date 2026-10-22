# Changelog

Record meaningful changes by version under the
[release convention](docs/delivery.md#versions-and-releases).

## Unreleased

## v1.3.0 — 2026-10-22

Current source catalogues, clearer setup and contribution guidance, stronger
preview checks and cleaner native provenance headers. The collection retains
68 experts, 96 specialties in 14 groups and 136 native role files; expert
profiles, visuals, selection descriptions and execution instructions are unchanged.

### Added

- Check local links, readable raster/SVG images and heading or explicit anchors
  against the generated review preview in CI, with portable diagnostics and
  regression coverage for valid and broken references.

### Changed

- Keep source catalogues current on main independently of native releases.
  Add docs-only generation and freshness checks while preserving VERSION and
  dist as release-owned outputs; publish the accepted catalogue presentation.
- Simplify native role headers, align source/version/ID comment values and
  separate them from host settings, preserving all parsed role content.
- Feature Jordan Peterson in place of Marie Curie on the homepage, with a task
  cue about personality and motivation.
- Remove the per-image type captions from the full catalogue, retaining
  accessible image descriptions and complete profile provenance.
- Complete manual host setup and invocation-verification guidance, clarify the
  external contribution and Markdown-preview handoffs, and use the project
  Python environment consistently in portrait commands.
- Show existing perspective cues beside overlapping specialty matches in
  the catalogues, while preserving role descriptions and instructions.
- Correct the source-directory description and simplify current project records,
  preserving historical decisions and evidence.
- Regenerate all native files with `1.3.0` provenance and refresh both host
  indexes with comparison cues, preserving parsed metadata and instructions.

### Validation and limits

All 72 tests and strict release checks pass. All 141 generated outputs match
their sources; both native formats agree for every expert, and all 136 parsed
payloads remain identical to v1.2.0. Expert source files, images, vocabulary,
shared templates and credited terms are unchanged. This release adds no new
host-runtime or comparative-effectiveness result. Exact-commit hosted Checks
and the [release record](https://github.com/shpoont/expert-roles/releases/tag/v1.3.0)
establish delivery separately from the declared version.

## v1.2.0 — 2026-10-22

Eleven new expert perspectives and a clearer catalogue introduction. The
collection has 68 experts, 96 specialties in 14 groups and 136 native role files.

### Added

- Leslie Lamport, Donella Meadows, Nancy Leveson, Daniel Jackson, David Parnas
  and Atul Gawande, with source-backed profiles and credited visuals.
- Warren Buffett, Jeff Bezos, Bill Gates, Richard Feynman and Marie Curie, with
  documented perspectives, public references and reference-based studio portraits.
- Fourteen specialty concepts, including formal methods, systems thinking,
  system safety, patient safety, value investing, physics and radiochemistry.
- Twenty-two native files for the new experts, using the existing flat Codex
  and Claude Code paths and whole-library source/version/ID provenance.

### Changed

- Lead the main README with a recognizable six-expert sample and task cues,
  then concise setup guidance. Keep one homepage image note, accessible image
  types and detailed profile credits. Retain correction/removal commitments in
  a linked policy and simplify project information.
- Separate source contributions from maintainer release preparation. Ordinary
  PRs retain VERSION, committed distribution files and generated catalogue
  sections; release PRs choose the final stable version and regenerate them.
- Make source validation the generator default, provide isolated unreleased
  previews and require explicit `--release` for committed generation. Keep
  `--check` as strict, read-only release freshness validation.
- Add CI ownership checks, maintainer `release` label routing and temporary
  review artifacts; update contributor, portrait and delivery guidance.
- Refresh the complete catalogue, generated summary, specialty indexes and all
  native version comments for v1.2.0 while preserving existing settings,
  descriptions, shared instructions, source profiles, visuals and image terms.

See the [release record](https://github.com/shpoont/expert-roles/releases/tag/v1.2.0)
and [validation evidence](evidence/README.md#v120-publication--2026-10-22).

## v1.1.0 — 2026-10-22

Compatible portrait contribution tooling, broader studio-portrait coverage and
source/version provenance in both native export formats. The catalogue retains
57 experts, 82 specialties in ten groups and stable export paths.

### Added

- A reproducible studio-v1 portrait workflow, versioned shared prompt and local
  helper for distinct per-expert palettes, exact photographic input records,
  reference hashes and deterministic 512 × 512 RGB JPEG preparation.
- A copyable generated-image credit block and repository/CI checks for image
  disclosures, explicit generation fields, stable recipes and each reference's
  linked source and reuse terms. A separate temporary contribution walkthrough
  exercises the documented process with actual built-in generation.
- Canonical source repository, whole-library version and expert ID comments in
  all 114 Codex and Claude Code exports. One validated root `VERSION` file owns
  the version, finalized as `1.1.0`; check mode detects stale headers. Comments
  stay outside host settings and instruction bodies.
- A private correction/removal contact and voluntary request process for
  featured experts and their representatives.

### Changed

- Use 40 owner-accepted reference-based studio portraits, with direct eye
  contact, a new studio sitting and distinct moderately muted backgrounds.
  Preserve five historical depictions and twelve full-name placeholders where
  a suitable photographic reference was not established.
- Expand source research with name variants, accented names and original event
  photographs, including a new Goldratt portrait and six former placeholders.
  Keep all source creators, individual licenses, permission notices and edit
  histories; explicitly label generated images in profiles and catalogues.
- Clarify source attribution versus output rights, minimum local generation
  records and preview-tool choice. Keep photographic references and private
  run artifacts outside the public repository.
- Explicitly identify roles as AI perspectives inspired by public work and
  prohibit claiming to be or represent the expert or their estate. Use singular
  first-person wording for the maintainer in the README request policy.
- Preserve expert identifiers, biographies, source metadata, vocabulary and flat
  Codex/Claude paths. Provenance headers do not change parsed role settings or
  the already accepted AI-identity instructions. Consumer integrations remain
  separate.

### Validation and limits

45 local tests pass and all 119 generated files match their sources. All 57
native pairs parse and agree; the stable version changes only the version
comment in each accepted development export. Accepted visuals, profile files,
expert metadata, vocabulary and shared templates retain their bytes.
One independent temporary contribution walkthrough passed; this is bounded
process evidence, not general repeatability or identity verification. No new
host-runtime or comparative role testing was performed. Images retain their
individually credited terms, including noncommercial conditions where applicable.
GitHub Checks records exact-commit hosted validation.

## v1.0.0 — 2026-10-21

First stable baseline of the complete Expert Roles library.

### Added

- 57 expert profiles, 82 specialties in ten groups, 38 credited portraits and
  19 full-name placeholders, with Codex and Claude Code files for every expert.
- A compact six-expert README sample, a full alphabetical and specialty
  catalogue, shared instructions and a copyable contributor starter.
- Original material under MIT, with photographs and referenced vocabulary
  retaining their individually documented terms.
- Whole-library `MAJOR.MINOR.PATCH` versioning, a dated changelog, fixed annotated
  Git tags and matching GitHub releases, independent of consuming integrations.

### Changed

- Consolidate native exports under `dist/codex/` and `dist/claude/`, preserving
  their contents. Generate a host chooser and alphabetical/specialty indexes
  from existing metadata; update profile, starter and download links.
- Check missing or changed indexes, obsolete or duplicate exports and legacy
  locations. Add a read-only CI workflow for the suite and generated consistency.
- Explain independent AI interpretation near the introduction. Show existing
  perspective cues for comparison, add a browser Find hint and link specialty
  labels to stable, precise catalogue rows.
- Clarify copying the whole starter once, preparing Python and choosing the
  image before generation. Separate release notes from historical development.

### Validation and limits

25 local tests pass and all 119 generated files match their sources. All 114
relocated exports retain their bytes; all 57 native pairs parse and agree.
Three sampled Codex calls previously passed through explicit registration.
Claude runtime, automatic Codex discovery and comparative role benefit remain
unverified. A stable library version does not extend those observed results.

## Initial development history

The notes below preserve intermediate states and superseded choices in the
initial implementation. Earlier counts and pending work describe those stages;
the current collection and validation summary above describe today's state.

### Documentation and selection changes

- Recorded owner acceptance of the fifty-seven-expert catalogue and closed
  its implementation and visual-review work. Aligned current instructions,
  agreement, delivery and handover guidance with completed status, preserving
  all expert content and historical records. Final verification and later
  runtime/effectiveness work remain separately documented; work is uncommitted.

- Clarified the project's scope as a broad expert catalogue. Superseded deferral
  recommendations based on a narrower interpretation while retaining the
  criteria and research. All forty-one experts and their files are preserved.

- Refined expert selection criteria to distinguish evidence of expertise,
  accessible approaches, task fit and scope, collection contribution and
  faithful use. Adopted main company functions as a curation coverage
  checklist, alongside the existing specialty vocabulary. Candidate additions
  and possible initial deferrals remain proposals; the forty-one-expert roster,
  native files and short expert definition are preserved.

- Simplified the README's expert-request example and removed the exporter
  aside. Clarified documented Codex name-based requests and Claude Code's
  `@` selection in the setup guide. Retained License before Disclaimer to
  match the existing public projects.

### Removed during development

- Zdeněk Rybka's current profile and both native exports, as selected by the
  owner after reviewing overlap with Tomáš Baťa. Historical inclusion records
  and source references remain available.

### Additions during development

- Socrates, Aristotle, Epictetus, Immanuel Kant, John Stuart Mill, Confucius
  and Karl Popper, with concise sourced profiles, credited reusable portraits
  and both generated native formats. Eight mapped specialties and a Philosophy
  group bring the catalogue to fifty-seven experts and eighty-two specialties.
  Profiles distinguish historical sources and later artistic representations;
  Socrates' photograph retains CC BY-SA 2.5 and Popper's photograph records
  LSE Library's explicit reuse terms. Earlier profiles, shared instructions
  and the fixed README sample are preserved. Work remains uncommitted.
- Dave Ulrich, Amy Edmondson, Marty Cagan, Mark Roberge, Benjamin Gomes-Casseres,
  Bill Price, Patricia Dechow, Jeanne Ross, Hau Lee and Kenneth A. Adams, with
  sourced profiles, both native formats, two credited portraits and eight
  full-name placeholders. Thirteen mapped specialties bring the catalogue to
  fifty experts and seventy-four specialties. Earlier retained profiles,
  shared instructions and the fixed README sample are preserved.

- Jeff Hawkins, David Premack, Pieter Levels and Ed Frawley, checked against
  the expert criteria and their documented public work. Added concise profiles,
  both native formats, a credited CC BY-SA 2.0 Hawkins portrait and three
  full-name placeholders. Added Computational neuroscience, Comparative
  psychology, Operant conditioning and Dog training, with Animal behavior as
  a new navigation group. The catalogue now has forty-one experts and
  sixty-one specialties. Earlier profiles, shared instructions and the fixed
  README sample are preserved; work remains uncommitted.

- Jordan Peterson's sourced personality-psychology profile, credited CC BY-SA
  3.0 portrait and generated Codex and Claude Code files. Added Personality
  psychology under the existing Psychology group. The catalogue now has
  thirty-seven experts and fifty-seven specialties; the fixed README sample,
  earlier experts and shared instruction are preserved. Work remains uncommitted.

- A README disclaimer following the public project pattern: no warranty,
  liability limits and independence from the featured experts, their estates
  or organizations and the host vendors. AI-generated role output is not a
  statement by the actual expert.

- Zdeněk Rybka's profile on the Bata management system, with the existing
  Operations management specialty, a distinguishing perspective, full-name
  placeholder and both generated native formats. The catalogue now has
  thirty-six experts; its fifty-six specialty definitions and earlier profiles
  are preserved. Work remains uncommitted.
- Tomáš Baťa, Milan Zelený, Steve Jobs and Nicole Forsgren, assessed against the
  existing expert criteria and documented public work. Added concise profiles,
  distinctive perspective cues and both generated native formats. Zelený and
  Jobs have credited reusable portraits; Baťa and Forsgren use full-name
  placeholders. Added DevOps, Product design and Multiple-criteria decision
  analysis, bringing the catalogue to thirty-five experts and fifty-six
  specialties. Earlier profiles and shared instructions are preserved; work
  remains local and uncommitted.
- A bounded three-case Codex host-validation contract, covering discovery and
  selection, independent judgment and professional scope with temporary project
  placement. The CLI attempt stopped at catalogue-role discovery, leaving
  behavior initially unverified. An owner-requested `codex exec` retry explicitly
  registered the unchanged exports for each invocation; native calls and child
  answers confirm the three sampled checks. Automatic directory discovery and
  broader reliability remain unverified. Temporary placement is removed;
  exports and personal role files are preserved. Deployment and management
  remain a separate plugin's responsibility.
- Completed the four remaining accepted profiles: Michael Hammer, Karen
  Holtzblatt, Neil Rackham and Richard Susskind, with full-name placeholders and
  both native formats. Added five sourced specialties and Sales navigation.
  The catalogue now contains thirty-one experts and fifty-three specialties;
  existing profiles and instructions are preserved and work remains uncommitted.
- Shared SVG initials template, exact contributor commands and support for
  either a photo or standardized initials image in each profile and catalogue
  row. D023 makes photos optional while retaining photo permissions and credits.
  Added Taiichi Ohno (TO) and Roger Fisher (RF), both native formats and four
  sourced specialties. The catalogue now has twenty-seven experts and
  forty-eight specialties. Earlier profiles and photographs are preserved;
  all work remains uncommitted.
- Léonie Watson's accessibility profile with a credited CC BY-NC 2.0 portrait,
  a new Web accessibility specialty and both generated native formats. D022
  reassesses Watson, Ohno and Fisher under the general photo policy: Watson's
  crop is permitted for this noncommercial prototype; Ohno's known photo does
  not permit the required crop, and Fisher's sources still lack a free reuse
  grant. The catalogue has twenty-five experts and forty-four specialties,
  with six portrait dependencies remaining. All work remains uncommitted.
- Chip Huyen's previously accepted profile, using a credited frame from her
  Creative Commons-licensed Linux Foundation keynote. Reused the existing
  Machine learning and Large language models specialties and generated both
  native formats. The catalogue now has twenty-four experts and forty-three
  specialties; seven portrait dependencies remain. New source checks retain
  the existing permission rules, with all work uncommitted.
- Five profiles to broaden field coverage: Judea Pearl, Ellen Lupton, Ross
  Anderson, Andy Grove and David Aaker, with credited reusable portraits and
  generated native files. Added eight sourced specialty concepts using the
  existing groups, bringing the catalogue to twenty-three experts and forty-three
  specialties. Léonie Watson, Taiichi Ohno and Roger Fisher qualify but join
  the five earlier candidates pending cleared portraits. Other recommendations
  remain proposals outside this first batch.
- Twelve profiles spanning entrepreneurship, software, quality improvement,
  marketing, finance and law: Steve Blank, Saras Sarasvathy, Martin Fowler,
  Kent Beck, Eric Evans, Martin Kleppmann, W. Edwards Deming, Geoffrey Moore,
  Aswath Damodaran, Robert S. Kaplan, Lawrence Lessig and Philip Kotler. Each
  includes sourced task fit, a credited reusable portrait and generated native
  files. Added twenty-one mapped specialty concepts and Finance, Law and
  Marketing navigation. Huyen, Hammer, Holtzblatt, Rackham and Susskind qualify
  but remain pending portraits with verified reuse permission.
- AI profiles for Andrej Karpathy and Andrew Ng, with sourced specialties,
  credited reusable portraits and generated native files. Added four precise
  Computing concepts to the shared vocabulary. Chip Huyen meets the expert
  criteria; her addition remains pending a cleared portrait.
- Expert definition in the main README and concise selection criteria in the
  contribution guide, linked from project guidance and the profile starter.
  Existing profile fields provide the supporting evidence; no extra fields
  or detailed expert briefs are required.
- Coherent specialty rules for human and AI task matching, shared vocabulary,
  reference concepts and consistent grouping, with an assessment of central
  registry storage. Existing entries and the YAML format remain under review.
- MIT license for original profiles, role instructions, metadata, documentation
  and tooling, with matching contribution terms and standalone-copy guidance.
  Portraits retain their individually credited licenses and are excluded from MIT.
- Uncommitted profile prototype for Don Norman, Alan Cooper, Jakob Nielsen and
  Eliyahu Goldratt, including short introductions, credited photos and sources.
- Provisional specialty vocabulary, one shared instruction and deterministic
  catalogue / Codex / Claude Code exports with source-validation checks.
- Central native-role usage steps linked from the catalogue and profiles, and
  an independent multiple-specialty export check.
- Expert-addition checklist in `CONTRIBUTING.md` and a copyable profile README /
  metadata starter under `src/templates/profile/`.

- Public role-library scaffold with a visible catalogue, contribution guidance
  and retained owner decisions.
- Project Structure v1.0.0 organization for the current agreement, design, active
  work, delivery, working materials, explorations, checks and evidence.

### Catalogue and instruction changes

- Applied the owner's section-by-section README review under D034. Shortened
  the introduction, usage, selection, contribution, project links and license
  sections; explicit expert requests are optional. Moved the full alphabetical
  and specialty catalogue into `src/roles/README.md`, with a fixed six-expert
  showcase and generated total in the main README. Updated the generator,
  boundary/growth checks, profile/starter navigation and connected guidance;
  release procedure now lives in delivery documentation. Role metadata,
  specialties, images, credits, shared instructions and native exports are
  preserved. Work remains unstaged and uncommitted.

- Closed the initial catalogue implementation records and recorded the owner's
  acceptance of its rendered presentation. Updated current guidance and
  handover to make the planned README improvement review the next step;
  the README and role sources are preserved and work remains uncommitted.
- Prepared the initial catalogue documentation for commit review: clarified the
  current thirty-one-expert scope and export status, shortened current-work
  guidance, removed temporary contributor restrictions and documented explicit
  Codex registration with the known discovery and Claude runtime limits.
  Historical records and role content are preserved; work remains uncommitted.
- Extended Holtzblatt's perspective to include design alongside contextual
  research and product requirements; regenerated both native descriptions.
- Added optional `perspective` metadata for twenty-four experts with overlapping
  specialties and regenerated all thirty-one Codex/Claude description pairs.
  Seven profiles retain name/specialty descriptions. Updated the starter,
  contribution and selection guidance, and both metadata validation paths.
  Shared execution instructions, specialty assignments and images are preserved;
  selection reliability remains unverified and work stays uncommitted.
- Applied both accepted Pro review refinements: continue clear, independent
  in-scope work during clarification and explicitly prohibit fabricated
  biographical facts. Regenerated both native formats; work stays uncommitted.
- Made professional-role adoption explicit in the shared instruction and
  replaced the blanket impersonation prohibition with precise authorship and
  attribution limits. Regenerated both native formats; work stays uncommitted.
- Clarified mixed-request handling in the shared instruction: mark excluded
  parts as out of scope without recommending other experts or next steps.
  Regenerated both native formats; all work remains uncommitted.
- Refined the shared instruction to require professional scope checks,
  out-of-expertise decline, clarification and independent challenge of forced
  conclusions or suppressed expertise. Clarified documented ideas versus AI
  adaptations, aligned discovery descriptions and scope guidance, and
  regenerated both native formats for all thirty-one experts. Runtime behavior
  remains unverified; all work stays uncommitted.
- Refined the shared full-name placeholders with regular Georgia serif type,
  a warm paper background, an inset frame and subtle accent rules. Updated all
  six existing SVGs and the image guide; full names and image sizes are retained.
  The design is ready for review and remains uncommitted.
- Replaced abbreviated initials with full-name SVG placeholders. The command
  now reads the full name from expert metadata and wraps/sizes it automatically.
  Renamed the template and both profile images to `placeholder.svg`, simplified
  contributor commands and updated Ohno, Fisher and the starter. Photos and
  native role instructions are preserved; work remains uncommitted.
- Portrait eligibility accepts any verified free reuse permission, with or
  without attribution, including custom grants. The collection always keeps
  attribution. Replaced the fixed license list and automatic category exclusions
  with review of conditions against actual use and image preparation. Updated
  the contribution guide, starter, checks and project records; pending sources
  are marked for reassessment. Existing profiles and portraits are unchanged.
- Adopted the central YAML specialty registry with source concept references.
  Updated all four experts with shared broad fields and distinctive approaches,
  replaced provisional Usability evaluation with Usability engineering, and
  regenerated the main catalogue and both native formats. Added reference and
  duplicate-concept validation; catalogue groups show only assigned terms in
  name order. Recorded vocabulary attribution and reuse terms.
- Clarified the task-matching purpose of specialties in project guidance and
  linked contribution steps and the starter to the shared rules. Current
  assignments, generated roles and instructions are unchanged.
- Applied the simplified layout to all four profiles and the starter: linked
  specialties appear once, introductions are shorter, role-file/setup links
  appear earlier and source-file links move to a collapsed footer. Full photo
  credits, reference lists and suggested uses are preserved.
- Portraits now explicitly require verified reuse permission; missing, unclear
  and fair-use-only permissions are excluded. Updated the contribution guide,
  starter and project records, including the Goldratt source findings. Existing
  photos and role files are unchanged.
- Expert profiles now show labeled image Source and License links. The starter
  explicitly requires the image's own source page, with matching contribution
  guidance. Current photos are unchanged.
- Added recommended portrait sources and explicit credit, notice, edit-history
  and ShareAlike requirements to the contributor guide and starter. Completed
  Nielsen's credit with the supplied photo title. A further image search
  retained the four current portraits and prepared alternatives for review.
- Broader photo-source review replaced Cooper's and Norman's portraits with
  clearer freely reusable photographs and updated their credits. Nielsen's and
  Goldratt's existing portraits were retained in that first source review.
- Every expert now requires a credited 512 × 512 RGB JPEG, with uniform display
  sizes. Portraits are cropped consistently; Norman uses a clearer source photo.
  The exporter validates images with Pillow before writing generated files.
- Contribution guidance is shortened to essential steps, and the starter now
  requires a portrait and photo credit.
- Shared instructions and descriptions clarify that specialties guide the
  perspective while the task determines the focus.
- The full expert catalogue is generated directly in the main README, preserving
  authored sections outside its markers. It uses three columns and one expert
  per row; the source-folder README points back to it.
- Goldratt's portrait crop and caption identify him, with source credits and
  image modifications recorded.
- Profiles, specialty vocabulary and shared templates moved under `src/`, with
  matching generator paths, fixtures, navigation and project guidance.
- Canonical decision record moved from `docs/decision-log.md` to
  `docs/decisions.md`; existing decision contents are preserved.

### Fixes during development

- The no-partial-output test now places the invalid profile after a valid one.
- Markdown display text is escaped so punctuation preserves table cells and
  expert links.
