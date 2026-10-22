# Decision log

## Purpose

Preserve lasting decisions about the role library, their ownership and rationale,
and the choices that remain open.

D005 updates the catalogue location chosen in D001 and retained in D003; those
entries preserve the earlier reasoning.
D030 records the initial export formats; D041 records the accepted current
catalogue and its documentation closeout. D042 records the subsequent visitor
journey improvements and review; D043 records acceptance and commit approval.
Earlier scaffold and prototype
entries retain their original scopes and pending choices; later decisions
record which choices were adopted, completed or superseded.

## D001 — 2026-10-18: Independent public role library

- **Status:** Adopted repository boundary; role implementation pending.
- **Owner:** Leon.id Komarovsky.
- **Context:** The owner wants a visible role catalogue that people can
  potentially contribute to, independently of an integration's package layout.
- **Decision:** Use public repository `shpoont/expert-roles` for canonical role
  definitions, references, examples and contribution guidance. Place the role
  catalogue at top-level `roles/`.
- **Rationale:** Make the collection directly discoverable and reusable by
  independent consumers.
- **Consequences:** This initial revision contains documentation only. No roles,
  schema, installer, integration or orchestration are implemented. Consumers can
  identify a selected revision by its full commit SHA and own their packaging.
- **Alternatives:** Keeping the collection inside an integration package would
  give contributors a less direct entry point.
- **Source:** Owner's request to separate the public roles from the consuming
  plugin and selection of the name `expert-roles`.

## D002 — 2026-10-18: Product and contribution decisions remain open

- **Status:** Pending owner decisions.
- **Owner:** Leon.id Komarovsky.
- **Context:** The owner wants to discuss role contents and other details before
  implementation.
- **Decision:** Do not settle the role roster, file format, expert attribution,
  evaluation method, license or contribution terms in this scaffold.
- **Rationale:** Repository separation should enable discussion without turning
  exploratory recommendations into an implementation specification.
- **Consequences:** Design proposals and documentation corrections can be
  discussed now. Role definitions and distribution require the relevant choices
  to be agreed first.
- **Source:** Owner's setup-only scope and requirement to discuss role contents
  before implementation.

## D003 — 2026-10-18: Adopt Project Structure v1.0.0

- **Status:** Adopted structure; product choices remain pending.
- **Owner:** Leon.id Komarovsky.
- **Context:** The owner asked this library to follow Project Structure.
- **Decision:** Use its connected agreement, design, current-work, decisions,
  delivery, working-materials, exploration, checks and evidence records. Follow
  its independent changelog and release convention without making a release in
  this task. Rename this canonical record to `docs/decisions.md`, preserving the
  preceding entries.
- **Rationale:** Make the current agreement, active work, reasons and check
  results discoverable for contributors and continuation.
- **Consequences:** Keep `roles/` at the top level and link it from the
  working-materials guide. Add no duplicate role catalogue, role format,
  implementation, license or outcome claim. The current agreement is
  [PROJECT.md](../PROJECT.md), with the approach in [design](design.md),
  prepared [checks](../tests/README.md) and results in
  [evidence](../evidence/README.md).
- **Alternatives:** Leaving only a repository overview and decision log would
  omit the requested project's agreement, continuation and delivery records.
  Moving the role catalogue into `src/` would reduce its intended visibility.
- **Sources:** Owner's structure-alignment request;
  [Project Structure v1.0.0](https://github.com/shpoont/project-structure/releases/tag/v1.0.0),
  commit `96fdd6bd7950778f5b6c6f8269ab2b82167cb99a`.

## D004 — 2026-10-19: Try browsable expert profiles and shared instructions

- **Status:** Authorized local prototype; product choices remain provisional.
- **Owner:** Leon.id Komarovsky.
- **Context:** The owner prefers a simple collection that relies on the model's
  relevant knowledge of recognizable experts, while giving each expert a
  browsable profile and optionally a photo.
- **Decision:** Try one directory per expert, short source metadata, a shared
  instruction template and generated Codex/Claude Code files. Include Don Norman,
  Alan Cooper, Jakob Nielsen and Eliyahu Goldratt. Use overlapping specialty
  labels with broad navigation groups for the trial.
- **Rationale:** Make profiles tangible and easy to review without requiring
  detailed expert briefs or permanently adopting a taxonomy.
- **Constraints:** Do not commit, push, install, release or alter integrations.
  Library licensing and contribution terms remain open. Credit included images
  under their existing individual terms.
- **Consequences:** The current source is a review prototype, not an accepted
  release or evidence of role effectiveness. The current agreement and checks
  replace the previous setup-only completion boundary for this piece of work.
- **Source:** Owner's request to try the proposed directory layout, add Eliyahu
  Goldratt and leave the result uncommitted.

## D005 — 2026-10-19: Keep the role collection under working materials

- **Status:** Adopted location; prototype content and format remain provisional.
- **Owner:** Leon.id Komarovsky.
- **Context:** The owner questioned the top-level roles and specialty locations
  and asked to move the files and templates into the proposed `src/` layout.
- **Decision:** Use `src/roles/` for profiles and generated native files,
  `src/specialties.yaml` for the vocabulary and `src/templates/` for shared
  instructions. Retain one catalogue and link it from the root README.
- **Rationale:** These are the materials used to produce the collection, matching
  Project Structure's purpose for `src/`. A root README link keeps them visible.
- **Consequences:** Replace the location exception in D001/D003. Update the
  exporter, test fixtures, relative links and current guidance together, without
  changing profiles, classifications or operational instructions. Keep all work
  uncommitted and preserve the existing integration boundary.
- **Source:** Owner's request to move the files and folders, including templates.

## D006 — 2026-10-19: Apply the prototype review recommendations

- **Status:** Authorized local refinement; format and classification remain provisional.
- **Owner:** Leon.id Komarovsky.
- **Context:** Review identified ambiguity in specialty scope, duplicated public
  navigation, a weak test fixture and catalogue growth and formatting issues.
- **Decision:** Clarify the shared instruction and descriptions, lead with the
  catalogue, use fixed-column expert rows, escape Markdown display text, improve
  the invalid-input test and cover multiple specialties. Add central usage
  instructions and an identifying caption to Goldratt's existing photograph.
- **Rationale:** Improve the current contribution and use experience while
  retaining the simple metadata and shared instruction model.
- **Consequences:** Regenerate the portable files and catalogue, check the
  rendered result and retain the `src/` layout and existing classification.
  No installation, runtime efficacy claim, commit or release is authorized.
  Keep the current uncommitted status until an eventual commit is authorized.
- **Source:** Owner's request to implement the previous review recommendations.

## D007 — 2026-10-19: Generate the catalogue in the main README

- **Status:** Adopted display location; expert sources remain under `src/`.
- **Owner:** Leon.id Komarovsky.
- **Context:** The owner wants every expert visible when opening the repository.
- **Decision:** Generate the expert table and specialty groups inside a marked
  section of the main README. Preserve authored text outside that section and
  make the source-folder README a short pointer to the public catalogue.
- **Rationale:** Show the collection immediately while maintaining one generated
  catalogue from canonical metadata.
- **Consequences:** Update generator paths, profile navigation and checks. This
  replaces the catalogue-link placement in D005/D006 without moving sources or
  changing role instructions. Keep the work local and uncommitted.
- **Source:** Owner's request to generate the catalogue directly in the main
  README without committing.

## D008 — 2026-10-19: Document expert additions and provide a starter

- **Status:** Adopted contributor entry point; profile format remains provisional.
- **Owner:** Leon.id Komarovsky.
- **Decision:** Keep the addition checklist in `CONTRIBUTING.md` and a copyable
  README / metadata starter under `src/templates/profile/`. Link existing
  generator instructions and keep shared agent instructions unchanged.
- **Rationale:** Make the core contribution easy to start without a separate
  process document or independently authored per-expert prompts.
- **Constraints:** Verify the starter in a temporary checkout. Keep the actual
  collection and generated files unchanged and leave all work uncommitted.
- **Source:** Owner's request to add the process and starter profile template.

## D009 — 2026-10-19: Require standard portraits and shorten contribution steps

- **Status:** Mandatory-photo requirement superseded by D023; photo format and
  display dimensions remain adopted.
- **Owner:** Leon.id Komarovsky.
- **Decision:** Require a credited `portrait.jpg` for each expert: 512 × 512
  pixels, RGB JPEG. Display it at 160 × 160 in the catalogue and 240 × 240 on
  profiles. Keep the contribution guide to the essential steps and make the
  starter's image and credit mandatory.
- **Rationale:** Make profiles consistent while keeping additions easy.
- **Consequences:** Validate actual image format, dimensions, color mode and
  decoding before generating outputs. Deterministically crop and resize current
  photos, consider more suitable reusable sources, and record all edits in
  credits. This replaces optional-photo behavior and the earlier requirement
  to preserve image bytes. Keep instructions and metadata unchanged, and leave
  all work uncommitted.
- **Source:** Owner's photo-standard request, explicit approval of deterministic
  cropping and resizing, and authorization to find more suitable photos.

## D010 — 2026-10-19: Document portrait-license obligations

- **Status:** Adopted contribution guidance for the current prototype.
- **Owner:** Leon.id Komarovsky.
- **Decision:** Include recommended portrait sources and the credits, notices,
  edit history and ShareAlike obligations in the contribution guide and starter.
  Verify each photo's own terms, preserve its license, and keep the license for
  the library's original work open.
- **Source:** Owner's request to include what the photo licenses require and
  search for more images. Keep the work uncommitted.

## D011 — 2026-10-19: Use portraits only with verified reuse permission

- **Status:** Adopted; D021 broadens eligibility and makes attribution universal.
- **Owner:** Leon.id Komarovsky.
- **Decision:** Do not use a portrait when reuse permission is missing or
  unclear. Follow the [photo policy](../CONTRIBUTING.md#photo-sources-and-licenses):
  verified public-domain / CC0, CC BY or CC BY-SA status permits inclusion under
  the applicable terms. An existing suitable license supplies permission;
  separate individual permission is not required. Record the image's specific
  source, license, required credits, notices and edits in its profile.
- **Rationale:** A recognizable person, publicly visible image, source credit
  or Wikipedia fair-use rationale does not establish the reuse rights needed
  for cropped portraits in a redistributable collection.
- **Consequences:** Retain Goldratt's current Commons photo. Exclude the
  non-free Wikipedia portrait and clearer publisher or organization photos
  without verified permission. The [source findings](../evidence/README.md#verified-portrait-permission--2026-10-19)
  record the bounded search; no rights-holder outreach is authorized. The
  library's original-content license remains open, and work stays uncommitted.
- **Source:** Owner's confirmation to exclude images without permission and
  update the relevant project files with the recent conclusions.

## D012 — 2026-10-19: Adopt MIT for the library's original material

- **Status:** Adopted; supersedes the earlier library-license deferrals.
- **Owner:** Leon.id Komarovsky.
- **Decision:** Use the standard [MIT license](../LICENSE) with
  `Copyright (c) 2026 Shpoont` for original profiles, role instructions, metadata,
  documentation and tooling. Original contributions use MIT. Portraits are
  excluded and retain their individually credited licenses and obligations.
- **Rationale:** Follow the existing public method repositories and permit
  straightforward modification and reuse, including in private and commercial
  integrations, while retaining copyright and permission notices.
- **Consequences:** Explain the license scope and contribution terms in the
  main README and contributor guide, and retain the MIT notice with standalone
  role copies. Preserve existing photo bytes and credits. This decision does
  not adopt the provisional profile format or authorize a commit or release.
- **Source:** Owner's instruction to use the same license after comparing
  `project-execution-model` and
  `simple-method-for-processing-unorganized-items`, both MIT-licensed.

## D013 — 2026-10-19: Adopt the simplified profile layout

- **Status:** Adopted for all four profiles and the starter.
- **Owner:** Leon.id Komarovsky.
- **Decision:** Present each expert with a name, portrait, one line of linked
  specialties, a short introduction and early role-file/setup links. Follow
  with one independent-AI notice, suggested uses, public references and full
  visible photo credit. Put metadata and shared-instruction links in a
  collapsed Source files footer, followed by catalogue navigation.
- **Rationale:** Make profiles easier to scan and use by removing duplicate
  specialty sections and repeated generation explanations.
- **Constraints:** Preserve photo bytes, complete credits, suggested uses and
  reference lists. Keep metadata, classifications and operational instructions
  unchanged. The specialty vocabulary and native role format remain provisional.
  Keep all work uncommitted.
- **Source:** Owner's request to apply the reviewed simplified layout to all
  four profiles and the starter template without committing.

## D014 — 2026-10-19: Define specialties for task matching and consistency

- **Status:** Purpose agreed; working rules documented. Vocabulary mappings
  and the storage recommendation remain under review.
- **Owner:** Leon.id Komarovsky.
- **Decision:** Specialties help people and AI choose experts suited to a task
  and provide a common vocabulary for a predictable catalogue. Keep coherent
  [rules](elements/specialties.md#rules) in one record, linked from contribution
  guidance and the starter. Reuse canonical terms, allow useful overlap, and
  choose accurate reference concepts without narrowing experts to generic
  task roles or forcing unsuitable matches.
- **Rationale:** A name alone may not give people or AI enough guidance to
  select an expert. Shared terminology makes the catalogue easier to navigate
  and keeps equivalent specialties consistent across profiles.
- **Consequences:** The specialty record recommends ESCO knowledge concepts
  with accurate Wikidata concepts for gaps, and assesses keeping a small central
  YAML registry. Retain the current registry during that review. Final term
  assignments, external-reference representation and storage remain open;
  this documentation step changes no current expert assignments, generated
  roles or shared instructions. Keep all work uncommitted.
- **Source:** Owner's clarification of task matching and common vocabulary,
  followed by the request for coherent rules, a specialties.yaml assessment
  and relevant repository updates.

## D015 — 2026-10-19: Keep the central registry and apply specialty rules

- **Status:** Adopted central YAML registry; initial assignments implemented
  locally and kept uncommitted.
- **Owner:** Leon.id Komarovsky.
- **Decision:** Keep `src/specialties.yaml` as the shared vocabulary and apply
  the [specialty rules](elements/specialties.md#rules) to all four experts.
  Each used concept has a stable local ID, readable name, shared group and
  specific external `reference` URL. Six entries reference verified ESCO
  knowledge concepts and four reference Wikidata concepts.
- **Rationale:** Broad fields help task matching, while specific approaches
  retain useful differences among experts. Shared entries make terminology
  consistent across profiles and generated native descriptions. Recording
  concept URLs keeps reference meanings inspectable without network access
  during generation or copying full taxonomies.
- **Consequences:** Use ten concepts across Design, Management and Psychology.
  Reuse Human-computer interaction across the three design experts. Add useful
  broader fields and specific methods, replace the provisional
  `usability-evaluation` assignment with `usability-engineering`, and regenerate
  the catalogue and both host formats. Preserve the shared instruction and
  photo material. Reject invalid references and duplicate names/concepts before
  writes; show only assigned terms in name order. Retain source credits and
  vocabulary terms separately from the library's MIT original material.
- **Boundary:** This resolves the storage recommendation in D014. The registry
  can grow through the same rules; deeper hierarchy, separate alias fields,
  native-role acceptance and effectiveness evaluation are not implemented by
  this step. No commit, installation or release is authorized.
- **Source:** Owner's instruction to keep specialties.yaml and update the four
  experts according to the new rules.

## D016 — 2026-10-19: Define experts and selection criteria

- **Status:** Adopted for the catalogue and future additions.
- **Owner:** Leon.id Komarovsky.
- **Decision:** Keep the [expert definition](../README.md#who-is-included)
  in the main README and [selection criteria](../CONTRIBUTING.md#expert-selection)
  in the contribution guide. Consider established expertise, accessible public
  work and useful task fit; prefer people well known within their field.
  Fame alone is insufficient, formal credentials are not required, and both
  living and historical people may qualify.
- **Rationale:** A named perspective needs a credible, documented basis and a
  useful relationship to tasks. Public familiarity supports the lightweight
  approach that relies largely on the model's existing knowledge.
- **Consequences:** Use existing introductions, references, specialties and
  suggested uses to support selection, without extra fields or detailed briefs.
  This is editorial guidance, not proof that a model knows a person or applies
  their work effectively. The final roster and benefit assessment remain open.
  Keep all work uncommitted; no native instructions or current profiles change.
- **Source:** Owner's acceptance of the proposed definition and criteria,
  followed by the request to update relevant documents.

## D017 — 2026-10-19: Accept three AI candidates and add cleared profiles

- **Status:** All three candidates meet the expert criteria; Karpathy and Ng
  are added locally, while Huyen remains pending a cleared portrait.
- **Owner:** Leon.id Komarovsky.
- **Decision:** Add Andrej Karpathy, Chip Huyen and Andrew Ng using the adopted
  [selection criteria](../CONTRIBUTING.md#expert-selection) and profile process.
  Their research, teaching, books and public work establish useful perspectives
  on model implementation, production AI systems and AI project adoption.
- **Rationale:** Each has documented contributions, substantial accessible
  work and recognition within the field. The existing profile fields and
  shared instruction can represent their task fit without detailed briefs.
- **Consequences:** Karpathy and Ng have completed profiles and licensed
  portraits. Add four precise Wikidata fields under Computing, preserving the
  existing vocabulary and role instructions. Keep Huyen's prepared draft
  outside the live collection until a portrait meets the
  [photo policy](../CONTRIBUTING.md#photo-sources-and-licenses). Public headshots
  without clear permission and noncommercial-only event photos do not qualify.
- **Boundary:** Expert selection does not establish model familiarity or role
  effectiveness. Preserve the original four profiles; keep this work unstaged
  and uncommitted, without installation, integration changes or publication.
- **Source:** Owner's instruction to add the three proposed AI experts if they
  match the adopted expert definition.

## D018 — 2026-10-19: Expand the catalogue using the same selection and photo rules

- **Status:** Twelve further profiles added locally; five accepted additions
  remain pending cleared portraits. Work remains uncommitted.
- **Owner:** Leon.id Komarovsky.
- **Decision:** Add the previously recommended candidates who meet the
  [selection criteria](../CONTRIBUTING.md#expert-selection), and broaden the
  search for a freely reusable Huyen portrait. Public work supports each
  candidate's task fit through the existing introduction, specialties,
  suggested uses and references; no extra fields or detailed briefs are added.
- **Consequences:** The catalogue grows to eighteen completed profiles with
  thirty-five sourced specialty concepts. Reuse existing broad groups and add
  Finance, Law and Marketing. Keep all earlier entries, six complete profiles,
  shared instructions and generation behavior unchanged. All live additions
  require licensed, credited 512 × 512 RGB JPEG portraits and both native files.
- **Remaining dependencies:** Huyen, Michael Hammer, Karen Holtzblatt, Neil
  Rackham and Richard Susskind qualify but remain outside the live collection
  until suitable portraits have verified reuse permission. Additional public
  headshots, noncommercial/no-derivatives licenses, unrelated namesakes and
  deleted files do not satisfy the adopted photo policy. No rights-holder
  messages were sent.
- **Boundary:** This is editorial expansion of the local prototype, not proof
  of model familiarity or expert-role effectiveness. No staging, commit,
  publication, installation or consumer integration change is authorized.
- **Source:** Owner's request to try other Huyen photo sources and add the
  previously recommended promising catalogue candidates.

## D019 — 2026-10-20: Add the first batch to broaden field coverage

- **Status:** Five further profiles added locally; three new and five earlier
  accepted additions remain pending cleared portraits. Work remains uncommitted.
- **Owner:** Leon.id Komarovsky.
- **Decision:** Add the recommended first batch of Judea Pearl, Ellen Lupton,
  Léonie Watson, Ross Anderson, Taiichi Ohno, Andy Grove, David Aaker and Roger
  Fisher under the existing selection, specialty and portrait rules. Their
  documented research, books, methods and practice provide useful perspectives
  on gaps in the current catalogue. Fisher means the Harvard negotiation scholar.
- **Consequences:** Pearl, Lupton, Anderson, Grove and Aaker have complete
  profiles, credited reusable portraits and both generated native formats.
  Eight used concepts extend the vocabulary to forty-three entries, reusing
  the seven existing groups. Preserve all eighteen earlier profiles and native
  files, previous vocabulary entries, shared instructions and tooling.
- **Remaining dependencies:** Watson's checked photos have restrictive terms;
  Ohno's historical portrait has unresolved territorial rights, and another
  upload has unclear provenance; no eligible Fisher portrait was verified.
  Keep their drafts outside the live collection alongside the five earlier
  pending candidates. Existing evidence for those five remains applicable;
  no new cleared portrait or rights-holder permission is established here.
- **Boundary:** This first batch does not authorize the other gap-filling
  recommendations. Editorial selection does not prove representative field
  coverage, model familiarity or role effectiveness. No staging, commit,
  publication, installation, live-agent launch or integration change is authorized.
- **Source:** Owner's instruction to carry out the recommended next additions.

## D020 — 2026-10-20: Complete Huyen from a newly cleared portrait source

- **Status:** Huyen added locally; seven earlier accepted additions remain
  pending suitable cleared portraits. Work remains uncommitted.
- **Owner:** Leon.id Komarovsky.
- **Decision:** Continue the accepted additions under the existing expert,
  specialty and photo rules. Complete Huyen's prepared profile using a frame
  from her Linux Foundation keynote, explicitly marked Creative Commons
  Attribution for reuse. Its per-video license link resolves to YouTube's
  terms identifying CC BY 4.0 when checked on 2026-10-20.
- **Consequences:** Add her short profile, source metadata, credited 512 × 512
  RGB JPEG and both generated native files. Reuse the existing Machine learning
  and Large language models specialties. Preserve all twenty-three earlier
  complete profiles, the registry, shared instruction, templates and tooling.
  Credit the recording, publisher, exact frame timestamp, license and edits.
- **Remaining dependencies:** New photo and recording leads do not establish
  qualifying permission for Watson, Ohno, Fisher, Hammer, Holtzblatt, Rackham
  or Susskind. Keep their drafts outside the live collection. Public access,
  absent metadata or restrictive licenses do not replace verified permission.
- **Boundary:** This completes an already accepted addition and changes no
  selection or license policy. No further roster expansion, staging, commit,
  publication, installation, integration change or live-agent assessment is
  authorized. No rights-holder messages were sent.
- **Source:** Owner's instruction to keep working on the outstanding additions.

## D021 — 2026-10-20: Accept any free reuse permission and always keep attribution

- **Status:** Adopted; broadens the eligibility rule in D011.
- **Owner:** Leon.id Komarovsky.
- **Decision:** Accept any verified free reuse permission, whether or not the
  source requires attribution. Public-domain status, standard licenses and
  clear custom grants can qualify. Always include available creator, title
  and source attribution, applicable terms, required notices and edits.
- **Rationale:** Eligibility depends on permission for the intended use rather
  than membership in a short list of license names. Attribution also preserves
  provenance when the source makes credit optional.
- **Consequences:** Assess conditions against actual catalogue use and required
  image preparation. Commercial-use or edit restrictions are evaluated for
  compatibility instead of causing automatic rejection by category. Follow
  each source's terms; do not infer permission from public visibility or
  attribution alone. An existing clear grant needs no additional approval.
  Attribution is this collection's practice and adds no conditions to a source
  grant that permits reuse without credit.
- **Boundary:** Reassess earlier category-based exclusions under the new rule.
  This documentation step does not itself clear a portrait or change any
  profile, image, specialty or native instruction. Preserve the required photo
  format and permission evidence. Keep all work unstaged and uncommitted.
- **Source:** Owner's instruction that the policy accept any free reuse with
  or without attribution while retaining attribution regardless of the license.

## D022 — 2026-10-20: Reassess Watson, Ohno and Fisher and complete Watson

- **Status:** Implemented locally under D021; owner review remains pending.
- **Owner:** Leon.id Komarovsky.
- **Decision:** Complete Watson's accepted profile with Mike Gifford's
  *Leonie and her Smart Phone*, licensed CC BY-NC 2.0. Record attribution,
  source, exact terms and crop. Add Web accessibility using its precise
  Wikidata concept and reuse Human-computer interaction. Regenerate the
  catalogue and both native formats.
- **Rationale:** The grant permits adaptation for this noncommercial catalogue
  prototype. Its noncommercial condition is retained; the portrait is excluded
  from the library's MIT license and has no commercial-reuse promise.
- **Unresolved:** Toyota's landscape Ohno photograph is CC BY-NC-ND 2.0; the
  grant does not cover the required square crop. Harvard Law School's Fisher
  sources require prior written permission; public availability and an
  editorial/educational-use description do not supply that permission.
- **Boundary:** Preserve all twenty-four earlier profiles and their files,
  existing specialty definitions, shared instructions, generator, tests,
  contribution policy and MIT license. Six portrait dependencies remain;
  no format exception or rights-holder request is made. Keep work uncommitted,
  without publication, installation, integration changes or role assessment.
- **Source:** Owner's request to reassess these three portraits under the
  updated policy and add the experts where possible. Source observations and
  verification are in the [reassessment results](../evidence/README.md#watson-ohno-and-fisher-portrait-reassessment--2026-10-20).

## D023 — 2026-10-20: Use initials when portraits are unavailable

- **Status:** Adopted image policy; initials details superseded by D024.
- **Owner:** Leon.id Komarovsky.
- **Decision:** Require one standardized square visual per profile. Prefer a
  suitable permitted `portrait.jpg`; otherwise use `initials.svg` from the
  shared template, with one to three uppercase initials and an accessible
  full-name title. Keep 160 × 160 catalogue and 240 × 240 profile display sizes.
  Add Ohno and Fisher with TO and RF and both generated native formats.
- **Rationale:** Expert selection follows the person's public work and useful
  task fit. An unavailable photograph should not block a qualified addition.
  Initials provide a consistent visual without borrowing an uncleared image.
- **Consequences:** Supersedes D009's mandatory-photo requirement; D021's
  photo permission and attribution policy is unchanged. The original SVG
  template and initials artwork use MIT; photographs retain separate terms.
  The starter defaults to initials. A command creates the file from the
  profile name and chosen initials, without overwriting existing images.
  Generation validates the supplied image and rejects both files together.
  Follow the [exact contributor steps](../src/README.md#choose-the-profile-image).
- **Boundary:** Preserve all twenty-five earlier profiles, photographs, native
  instructions, metadata schema and specialty definitions. Four other accepted
  drafts remain outside this two-profile addition; they can use initials later.
  Keep work unstaged and uncommitted; no installation, publication, integration
  changes, permission requests or live role assessment.
- **Source:** Owner's instruction to adopt initials placeholders, update the
  relevant documents, add Ohno and Fisher, and provide the SVG template and
  exact usage instructions. Results are in the
  [initials/additions evidence](../evidence/README.md#initials-placeholders-and-ohno-and-fisher-additions--2026-10-20).

## D024 — 2026-10-20: Display full names in placeholders

- **Status:** Adopted refinement; implemented locally for owner review.
- **Decision:** Replace initials with the expert's complete display name.
  Use `placeholder.svg` and the shared template of the same name. The
  `--create-placeholder EXPERT_SLUG` command reads `expert.yaml`, wraps the
  name and adjusts type size; no abbreviation or extra metadata is required.
- **Rationale:** Full names identify the person directly and retain the simple,
  consistent square visual when a photograph is unavailable.
- **Consequences:** Update Ohno and Fisher, the starter, command instructions
  and current guidance. D023's photo-or-placeholder policy and D021's actual
  photo permissions remain unchanged. Earlier initials results are historical.
  Preserve all photographs, specialty definitions, metadata and native roles.
- **Boundary:** No additional experts, installation, publication, integration
  changes or commit. Keep work unstaged and uncommitted. Verification is in the
  [full-name results](../evidence/README.md#full-name-placeholders--2026-10-20).

## D025 — 2026-10-20: Complete the four remaining accepted profiles

- **Status:** Implemented locally; owner review remains pending.
- **Decision:** Add Michael Hammer, Karen Holtzblatt, Neil Rackham and Richard
  Susskind with D024 full-name placeholders, prepared profile content, sourced
  specialties and both native formats. The catalogue contains thirty-one
  experts and fifty-three specialties; all accepted additions are complete.
- **Vocabulary:** Add Business process reengineering, Contextual design, SPIN
  Selling, Legal informatics and Access to justice, plus Sales navigation.
  Four entries use precise Wikidata concepts. SPIN Selling uses Huthwaite's
  specific method guide under specialty rule 7: Wikidata identifies the book
  and ESCO's ICT sales-methodologies concept changes the intended scope.
- **Boundary:** Preserve the twenty-seven earlier profiles, existing vocabulary,
  schema, shared instruction, SVG template, generator, tests and MIT license.
  Prepare a rendered preview for owner review and keep work unstaged and
  uncommitted, without installation, publication or new roster proposals.
- **Source:** Owner's instruction to add the remaining four experts using
  full-name placeholders and show the result. Verification is recorded in the
  [completion results](../evidence/README.md#remaining-four-expert-additions--2026-10-20).

## D026 — 2026-10-20: Refine the full-name placeholder design

- **Status:** Implemented locally for owner review.
- **Decision:** Use a warm paper background, a subtle inset frame and regular
  Georgia serif type with standard serif fallbacks in the shared SVG template
  and all six existing placeholders. Retain complete names, accessible titles,
  automatic wrapping, the creation command and existing image sizes.
- **Boundary:** No font downloads, new experts or changes to photographs,
  profile text, metadata, specialties, native roles or generator behavior.
  Keep everything unstaged and uncommitted. Verification is recorded in the
  [visual refinement results](../evidence/README.md#placeholder-visual-refinement--2026-10-20).

## D027 — 2026-10-20: Require professional scope and independent judgment

- **Status:** Adopted instruction requirements; implemented locally.
- **Decision:** Apply the accepted wording refinement and require roles to
  assess assignment fit and context before proceeding. Decline tasks outside
  documented expertise, handle relevant parts of mixed requests and clarify
  uncertain fit or essential missing context. Specialty labels are useful,
  nonexhaustive guidance rather than a complete expertise boundary.
- **Judgment:** Challenge unsupported premises, forced conclusions and
  instructions that suppress or override relevant expertise. Respect legitimate
  constraints and contrary evidence; explain conflicts with the expert's public
  approach. Decline requests that require misrepresenting expertise or judgment.
  Distinguish documented ideas from AI adaptations and retain the identity and
  attribution constraints.
- **Owner clarification, 2026-10-20:** For mixed requests, mark excluded parts
  as out of scope. Do not recommend other experts or next steps for those parts.
- **Persona clarification, 2026-10-20:** Adopt the expert's professional role,
  guided by public work. Replace the blanket impersonation prohibition with
  limits on presenting generated responses as the real person's statements
  and on fabricating personal experiences, quotations or endorsements.
- **Review refinements, 2026-10-20:** Continue clear, independent in-scope
  parts while clarifying unclear fit or essential context. Explicitly prohibit
  fabricated biographical facts alongside experiences, quotations and
  endorsements. The owner accepted both static-review recommendations.
- **Consequences:** Align discovery descriptions and scope guidance and
  regenerate both native formats. This refines D006's broad task-focus wording;
  assignments must fit documented expertise. Native schemas remain provisional.
- **Boundary:** Preserve all profiles, metadata, specialty definitions and
  visuals. No live role launch, installation, integration, publication or commit
  is authorized. Behavioral scenarios are prepared, not executed; structural
  checks do not establish actual refusal or challenge behavior. See the
  [instruction results](../evidence/README.md#shared-instruction-and-professional-scope--2026-10-20).

## D028 — 2026-10-20: Distinguish overlapping expert perspectives

- **Status:** Adopted; implemented locally and uncommitted.
- **Decision:** Add an optional `perspective` phrase to `expert.yaml` when name
  and specialties leave a useful distinction unclear. The phrase describes a
  distinctive professional emphasis supported by the profile's public work.
  Review neighboring experts together; generic activities such as analysis,
  feedback or advice remain shared, rather than defining different role jobs.
- **Scope:** Add cues for twenty-four overlapping experts across UX, AI,
  software, operations, marketing, strategy and entrepreneurship. Seven experts
  with already distinct specialty labels retain the simpler description. This
  is an editorial pass, not a rule that every shared label requires more prose.
- **Source and generation:** Keep one canonical phrase in metadata. Generate
  the same description for Codex and Claude, combining it with name and resolved
  specialty labels. The optional field does not add execution instructions,
  create an exhaustive expertise boundary or require a separate human-profile
  section. D016's lightweight contribution process remains; no long brief is
  required. See the [metadata guide](../src/README.md#role-metadata-and-descriptions).
- **Checks and limits:** Cover omission, folded text, native escaping and
  matching descriptions, invalid-input atomicity and both metadata consumers.
  Preserve all shared execution instructions, expert identities, specialty
  assignments, profile READMEs and visuals. Consumers own parent-level selection
  guidance; static checks do not establish live selection reliability. No role
  launch, installation, integration change, publication or commit is authorized.
  See the [results](../evidence/README.md#expert-perspectives-and-selection-descriptions--2026-10-20).

## D029 — 2026-10-20: Bound Codex validation and keep deployment external

- **Status:** Adopted scope; three sampled checks passed through explicit registration.
- **Decision:** Run a small live Codex check using temporary project copies of
  the unchanged native files. A separate plugin will deploy and manage roles;
  this repository retains portable source content and exports.
- **Boundary:** This explicitly permits temporary placement and invocation for
  the [three-case contract](design.md#codex-host-validation), superseding earlier
  no-launch constraints only for that check. Keep personal role files,
  integrations and exported instructions unchanged. Do not commit or publish.
- **Observation:** The tested CLI did not expose the requested catalogue role;
  a substituted pre-existing role is not a valid test of these instructions.
  Record this limitation rather than changing exports or adding deployment
  tooling to make the check pass. See the
  [host results](../evidence/README.md#codex-host-validation--2026-10-20).
- **Owner-requested retry:** Run `codex exec` with documented invocation-only
  name/description/file registrations for the unchanged temporary exports.
  Native calls and direct child answers confirm Nielsen's selection,
  Goldratt's challenge and Norman's decline. The three-case result does not
  establish automatic directory discovery, repeatability or comparative benefit.
  Temporary placement is removed and deployment remains external; see the
  [retry results](../evidence/README.md#codex-exec-retry--2026-10-20).

## D030 — 2026-10-20: Prepare the initial catalogue for commit review

- **Status:** Adopted documentation scope and initial-export baseline; uncommitted.
- **Decision:** Present the completed thirty-one-expert catalogue and the
  existing Codex TOML and Claude Code Markdown files as the initial collection
  and exports. Preserve their content and schemas; this records the current
  baseline rather than creating a release or a compatibility guarantee.
- **Usage:** Document the successful Codex invocation-only name, description
  and file registration mechanism. Keep automatic directory discovery separate
  and unresolved. Mark Claude exports as structurally checked and runtime-untested.
  Deployment and management remain a separate plugin's responsibility.
- **Documentation:** Make current agreement, contribution and handover guidance
  consistent with the completed catalogue. Remove stale four-profile references
  and temporary public contributor restrictions. Retain historical decisions,
  contracts and evidence, and keep the owner's no-commit constraint in current
  project guidance.
- **Checks and boundary:** Run the existing checks and review the complete
  proposed file set under the
  [cleanup contract](design.md#documentation-cleanup-and-final-checks). No new
  experts, role instructions, runtime launches, deployment tooling, commit,
  publication or release are part of this step. Broader effectiveness remains
  unproven. See the
  [final observations](../evidence/README.md#documentation-cleanup-and-final-checks--2026-10-20).

## D031 — 2026-10-20: Add four requested experts using the established criteria

- **Status:** Adopted scope and selection; uncommitted.
- **Decision:** Include Tomáš Baťa, Milan Zelený, Steve Jobs and Nicole Forsgren.
  Their documented enterprise practice, management research, product leadership
  and software-delivery research meet D016's criteria. Their profile references
  support distinctive perspectives alongside existing experts; fame alone is
  not the basis for selection. Baťa is the founder born in 1876, not his son.
- **Specialties:** Reuse Entrepreneurship, Operations management, Strategic
  management and Software engineering where relevant. Add ESCO's DevOps
  knowledge concept and precise Wikidata concepts for Product design and
  Multiple-criteria decision analysis. Keep labels nonexhaustive and use short
  perspective cues to distinguish overlapping experts.
- **Images:** Use Zelený's confirmed CC BY 3.0 portrait and Jobs's original
  CC BY-SA 3.0 photograph with credited square crops. Use the adopted full-name
  placeholders for Baťa and Forsgren: the examined Baťa postcard has conflicting
  ownership and licensing information, and no suitable Forsgren photo with a
  verified reuse grant was established. Missing photos do not block inclusion.
- **Boundary:** Follow the
  [addition contract](design.md#four-requested-expert-additions), preserve the
  existing collection and shared instruction, and regenerate both hosts' files.
  No commit, deployment, runtime launch or publication is authorized. Catalogue
  fit is an editorial judgment; these additions have no live model validation.
- **Verification:** Source, presentation and preservation checks passed; see
  the [addition results](../evidence/README.md#four-requested-expert-additions--2026-10-20).

## D032 — 2026-10-20: Add Zdeněk Rybka as a Bata-system specialist

- **Status:** Adopted selection and addition scope; uncommitted.
- **Decision:** Add Zdeněk Rybka (1927–2022), the management author and lecturer.
  The foundation's publication record and the management school's teaching
  record support the existing expert criteria. Reuse Operations management;
  distinguish his systematic interpretation of the Bata management principles
  from Baťa's enterprise-building perspective. Keep the source references in
  the profile and avoid implying measured model familiarity or effectiveness.
- **Image:** Use the standard full-name placeholder. The bounded photo review
  did not establish a suitable reuse grant; licensed exhibition results refer
  to the painter of the same name, born in 1938, and are not this expert.
- **Boundary:** Follow the [addition contract](design.md#zdeněk-rybka-addition).
  Preserve the earlier collection, vocabulary and shared instruction. No
  commit, installation, runtime launch, publication or release is authorized.
- **Verification:** Source, rendered-profile, navigation and preservation checks
  passed; see the [addition results](../evidence/README.md#zdeněk-rybka-addition--2026-10-20).

## D033 — 2026-10-20: Close the initial catalogue documentation and queue README review

- **Status:** Adopted documentation closeout; uncommitted.
- **Acceptance:** The owner reviewed the rendered main README and accepted its
  current presentation. The initial thirty-six-expert catalogue implementation
  and required source checks are complete. This does not establish broader
  runtime reliability or comparative effectiveness.
- **Next work:** The owner intends to review README improvements after this
  closeout. Record that review as the next step; its changes remain to be
  discussed. Preserve the current README during closeout.
- **Boundary:** Follow the
  [closeout contract](design.md#initial-catalogue-documentation-closeout).
  Update current guidance and handover records, preserving sources, historical
  records and the no-commit constraint. No staging, commit, publication,
  runtime invocation or integration change is included.
- **Verification:** Documentation closeout checks passed; see the
  [closeout results](../evidence/README.md#initial-catalogue-documentation-closeout--2026-10-20).

## D034 — 2026-10-20: Keep the README compact and the complete catalogue beside profiles

- **Status:** Adopted section-by-section review and implementation scope;
  implementation and local checks complete, rendering shown for owner review,
  uncommitted.
- **Presentation:** Use the agreed short introduction, usage, expert definition,
  contribution, project links, license and disclaimer. Explicit expert requests
  are optional. Retain the warranty/liability and independence pattern used in
  other public projects, including clear authorship limits for expert personas.
- **Follow-up review:** Use a natural-language example and remove the exporter
  aside. Keep host-specific invocation syntax in delivery guidance. Retain
  License before Disclaimer, matching the reviewed public projects.
- **Catalogue:** Supersede the earlier full-catalogue-in-main-README location.
  Put both complete alphabetical and specialty views in `src/roles/README.md`.
  The main README shows Chip Huyen, Martin Fowler, Don Norman, Eliyahu Goldratt,
  Philip Kotler and Aswath Damodaran in two rows, with existing visuals and one
  assigned specialty each. Curate this fixed sample for breadth as the library
  grows; it is not a ranking or a claim of complete field representation.
- **Generation:** Keep source metadata unchanged. Generate the summary total,
  six-card sample and full catalogue from the existing sources; validate the
  curated slug/specialty pairs in `FEATURED_EXPERTS`. Preserve authored text
  outside the separate generated boundaries and reject invalid inputs before
  writing outputs. Update profile/starter navigation and connected guidance;
  move release procedure to delivery documentation.
- **Checks and boundary:** Follow the
  [implementation contract](design.md#compact-readme-and-separate-full-catalogue).
  Preserve native instructions, metadata, specialties, images and credits;
  check growth, boundary preservation, source consistency, navigation and the
  actual rendering. No staging, commit, runtime invocation, deployment,
  integration change, push, publication, tag or release is authorized.
- **Verification:** All twenty tests and seventy-four generated-output checks
  pass; links resolve and all thirty-six native pairs remain unchanged and
  agree. Safari confirms six loaded portraits, two rows of three and no
  horizontal page overflow. See the
  [results](../evidence/README.md#compact-readme-and-separate-full-catalogue--2026-10-20).

## D035 — 2026-10-20: Add Jordan Peterson

- **Status:** Owner-requested addition; implementation and local checks complete,
  uncommitted. See the [results](../evidence/README.md#jordan-peterson-addition--2026-10-20).
- **Expert fit:** His coauthored Big Five personality research and accessible
  books and teaching meet the existing established-expertise, accessible-work,
  task-fit and public-familiarity criteria. The profile emphasizes personality
  differences, motivation, goals, personal responsibility and meaning.
- **Specialty:** Add Personality psychology under Psychology using Wikidata
  Q271716. ESCO's Theories of personality is narrower and its Psychology concept
  broader. One specific field identifies this expert without an additional
  perspective phrase. Preserve all earlier assignments and definitions.
- **Image:** Use Gage Skidmore's 15 June 2018 photograph from Wikimedia Commons
  under CC BY-SA 3.0 Unported. Record the source, creator, license and square
  crop/resize in the profile; retain that license for the modified portrait.
- **Boundary:** Follow the [addition contract](design.md#jordan-peterson-addition).
  Generate both native formats and catalogue totals, preserving earlier experts,
  shared instructions and the fixed README sample. No staging, commit,
  installation, runtime invocation, integration change or publication is included.

## D036 — 2026-10-20: Add Hawkins, Premack, Levels and Frawley

- **Status:** Owner-requested additions after reassessment against the existing
  expert criteria. Implementation, local checks and rendered review are
  complete. Work remains uncommitted. See the
  [results](../evidence/README.md#hawkins-premack-levels-and-frawley-additions--2026-10-20).
- **Expert fit:** Hawkins's documented neuroscience research and books support
  a brain-inspired AI perspective. Premack's reinforcement and comparative
  cognition research support a distinct experimental-psychology perspective.
  Levels's operating products, book and public account of building them support
  practical bootstrapping expertise. Frawley's professional training history
  and substantial authored instruction support dog-training practice. The
  latter two qualify through demonstrated practice and creations; academic
  credentials are not required. Frawley's own courses establish his work
  separately from the other instructors published by Leerburg. These are
  editorial fit judgments, not measurements of AI-role benefit or endorsements
  of every claim or method associated with each person.
- **Specialties:** Reuse Artificial intelligence, Cognitive psychology and
  Entrepreneurship as relevant. Add Computational neuroscience (Q8037925),
  Comparative psychology (Q1483503), Operant conditioning (Q847079) and Dog
  training (Q38490) using precise Wikidata concepts after checking ESCO.
  The returned ESCO concepts are adjacent, narrower or activities. Add Animal
  behavior as the shared navigation group for Dog training; keep the
  psychological research concepts under Psychology and computational
  neuroscience under Computing. Preserve all fifty-seven earlier definitions.
- **Selection cues:** Add short, sourced perspective phrases for Hawkins,
  Premack and Levels to distinguish overlapping AI, psychology and
  entrepreneurship roles. Dog training identifies Frawley sufficiently at
  present. Keep the shared execution instruction unchanged.
- **Images:** Use Jeff Kubina's eTech 2007 Hawkins photograph from Wikimedia
  Commons under CC BY-SA 2.0 Generic. Retain the creator, source, terms and
  square crop/resize in the profile, and the source license for the portrait.
  Bounded searches did not establish suitable reusable portraits for the
  other three; use the approved full-name placeholders. A Commons photograph
  associated with Frawley depicts the Leerburg facility, not a portrait.
- **Boundary:** Follow the
  [addition contract](design.md#hawkins-premack-levels-and-frawley-additions).
  Add four profiles and both formats, regenerate catalogue totals, and update
  connected records. Preserve all earlier experts, templates, code, tests,
  history and authored README text. No staging, commit, runtime invocation,
  installation, integration change, publication, tag or release is included.

## D037 — 2026-10-21: Refine selection criteria and review company coverage

- **Status:** The owner approved the proposed criteria refinement and requested
  research into main company departments and possible people to defer from an
  initial selection. The criteria are adopted; specific additions and deferrals
  remain proposals. Implementation and the first-pass research and documentation
  checks are complete; see the
  [review evidence](../evidence/README.md#selection-criteria-and-company-coverage-review--2026-10-21).
- **Criteria:** Keep the short expert definition as the eligibility threshold.
  Assess the person's expertise, suitability of their AI perspective and
  contribution to the collection separately. The contribution guide now asks
  for evidence of expertise, an accessible approach, task fit and scope,
  collection contribution and faithful use. Check what sources establish,
  seek independent corroboration where available and preserve uncertainty.
  Academic credentials remain optional; prominence and model familiarity do
  not establish expertise or role benefit. Keep profiles and the contribution
  process concise, without a detailed expert brief or schema change.
- **Coverage:** Use main company functions as the current curation priority.
  A general cross-industry company is the working assumption; specialized
  functions depend on its products, industry, jurisdiction and stage. APQC's
  public process-framework overview informs the coverage check without importing
  its process hierarchy into the specialty registry. Departments guide coverage;
  canonical specialty concepts retain their meanings and groups. Review
  relevant work, subfields and complementary methods rather than matching counts.
- **Selection:** Propose initial deferrals based on task focus or marginal
  coverage, with an explicit trade-off. Deferral does not reject an expert's
  eligibility. The new research also distinguishes an absent expert from an
  existing person's relevant documented work that is not yet surfaced in
  their profile. Marketing is already represented by Kotler, Aaker and Moore;
  HR is a genuine gap. Additions and profile refinements require selection
  before implementation.
- **Boundary:** Follow the
  [selection and coverage contract](design.md#selection-criteria-and-company-coverage-review).
  Preserve the roster, expert directories, images, registry, templates, native
  exports, code, tests, both README entry points and historical records.
  No staging, commit, installation, runtime invocation, integration change,
  publication, tag or release is included.

## D038 — 2026-10-21: Clarify the collection's broad scope

- **Status:** The project is a broad expert catalogue.
- **Correction:** This supersedes D037's narrower interpretation and resulting
  deferral recommendations. Retain the revised expert criteria and research.
- **Curation:** Assess expertise, the suitability of the AI perspective and
  contribution to the whole collection. Review useful coverage, complementary
  approaches and actual redundancy across relevant fields, without equal-count
  quotas or assumptions that particular fields have lower priority.
  Possible overlap remains a review question, not an automatic removal.
- **Boundary:** Follow the
  [clarification contract](design.md#broad-catalogue-scope-clarification).
  Correct current guidance and preserve historical records with this explicit
  supersession. No expert is added or removed; all profile sources, images,
  native files, code and tests are preserved. Work remains local, unstaged and
  uncommitted, without invocation, integration change or publication.

## D039 — 2026-10-21: Add ten selected experts and remove Rybka

- **Status:** The owner selected Dave Ulrich, Amy Edmondson, Marty Cagan,
  Mark Roberge, Benjamin Gomes-Casseres, Bill Price, Patricia Dechow,
  Jeanne Ross, Hau Lee and Kenneth A. Adams, and authorized removing
  Zdeněk Rybka. The fifty-expert collection is implemented and locally checked;
  the rendered catalogue has been shown for review. Work remains uncommitted.
- **Fit and contribution:** Their documented research, professional practice
  and accessible methods support inclusion under the adopted criteria.
  Profiles distinguish HR capabilities, team learning, product discovery,
  sales management, alliances, customer service, earnings quality, enterprise
  architecture, supply-chain coordination and contract language from existing
  neighboring perspectives. These editorial judgments do not measure AI-role
  benefit. The catalogue's broad scope and shared instruction are unchanged.
- **Removal:** Rybka's current profile and both exports are removed as selected
  after reviewing overlap with Baťa. This prioritization does not reverse his
  earlier qualification. Preserve inclusion history and its public references;
  the other forty expert directories retain their bytes.
- **Specialties:** Add thirteen accurate concepts using five ESCO knowledge
  entries and eight Wikidata entries. Reuse the existing nine groups and all
  sixty-one earlier definitions; the registry now contains seventy-four entries.
  The [specialty record](elements/specialties.md#current-implementation) explains
  the mappings and the Strategic alliances display label.
- **Images:** Edmondson uses Eliseeva's CC BY-SA 2.0 portrait, shared by her
  office on Flickr, retaining Rosiestep's earlier crop credit. Ross uses a frame
  from MIT CISR's own CC BY-NC 4.0 video, with the time, crop and noncommercial
  condition recorded on the profile. The other eight use the approved full-name
  placeholders after bounded searches did not establish suitable permitted
  portraits. A Commons Ross image had an unreviewed YouTube grant; the MIT
  source supplies directly documented permission for the selected frame.
- **Checks and boundary:** Follow the
  [addition and removal contract](design.md#ten-expert-additions-and-rybka-removal)
  and [observed checks](../evidence/README.md#ten-expert-additions-and-rybka-removal--2026-10-21).
  Twenty tests pass, 102 generated outputs match and all fifty native pairs
  agree. The authored README and fixed six-expert sample remain unchanged.
  No staging, commit, installation, runtime invocation, integration change,
  publication, tag or release is included.

## D040 — Add seven philosophical perspectives

The owner selected Socrates, Aristotle, Epictetus, Immanuel Kant, John Stuart
Mill, Confucius and Karl Popper after reviewing their complementary approaches.
Add their concise profiles, source-mapped specialties, permitted visuals and
both native exports under the [addition contract](design.md#seven-philosophy-additions).
Use the existing criteria and broad catalogue scope; retain material
historical attribution limits. Preserve the other fifty experts and the
compact README sample. Implement and show a rendered preview, keeping all
work local, unstaged and uncommitted. Comparative role benefit and runtime
validation remain separate from this addition.

## D041 — 2026-10-21: Close the accepted catalogue documentation

- **Status:** Complete. Owner acceptance is recorded, documentation is aligned
  and final checks pass. The owner accepted the rendered fifty-seven-expert
  catalogue and requested documentation closeout and final checks.
- **Decision:** Close the initial implementation and visual-review work.
  Update current instructions, agreement and delivery/handover summaries to
  the completed fifty-seven-expert, eighty-two-specialty catalogue. Supersede
  stale pending-review wording in current guidance while preserving historical
  decision and evidence entries. No further accepted profile, required image,
  layout or specialty decision is open.
- **Checks:** Follow the
  [closeout contract](design.md#final-documentation-closeout-for-the-accepted-catalogue)
  and [observed results](../evidence/README.md#accepted-catalogue-documentation-closeout--2026-10-21).
  Preserve all catalogue content, code, tests, shared instructions, vocabulary,
  licenses and native files; run the existing suite and final source, native,
  image, local-link, public-content, preservation and Git checks.
- **Boundary:** Runtime discovery, Claude execution, deployment and comparative
  benefit remain separately scoped follow-ups. Keep work local, unstaged and
  uncommitted; this closeout authorizes no commit, push, publication, tag or release.

## D042 — 2026-10-21: Review first-time and returning visitor journeys

- **Status:** Complete and uncommitted. All five findings resolved in journey
  re-review; a fresh final review found no blockers. Relevant checks pass.
- **Decision:** Review discovering, choosing, comparing, obtaining and setting
  up roles, then returning to find an expert, inspect changes or contribute.
  Use independent subagent walkthroughs and fresh local rendering. Expert
  walkthroughs do not establish actual user outcomes or hosted GitHub behavior.
- **Changes:** Explain AI independence near the introduction; reuse existing
  perspective cues for human catalogue comparison; provide a browser Find hint
  and stable `specialty-<canonical-id>` destinations from catalogue and profile
  labels. Clarify whole-folder copying and environment/image/generation order.
  Put a current changelog summary above preserved, clearly labeled history.
- **Boundary:** Preserve the six featured experts, all fifty-seven experts,
  vocabulary, images, photo terms, source metadata, shared instruction and
  native files. The perspective cue gains a human display under D028 without
  changing descriptions or execution. No invocation, deployment or publication.
- **Checks:** Follow the [journey contract](design.md#first-time-and-returning-visitor-journey-review)
  and [assessment guidance](../tests/README.md#visitor-journey-review-d042).
  Results and limits are in the
  [visitor review evidence](../evidence/README.md#visitor-journey-review--2026-10-21).

## D043 — 2026-10-21: Commit the accepted initial catalogue

- **Status:** The owner accepted the completed visitor-review result and
  explicitly authorized the initial catalogue commit.
- **Decision:** Commit the reviewed fifty-seven-expert collection, portable
  exports, generator, tests, licensing and project records using the configured
  signing identity. This supersedes the earlier no-commit restriction for the
  accepted tree; historical contracts and evidence retain their original scope.
- **Verification and boundary:** Preserve the reviewed catalogue bytes and
  record only this approval in current guidance. Confirm the staged tree,
  generated consistency, local references and whitespace before committing,
  then verify the signed commit and clean working tree. Push, publication,
  installation, integration changes, tags and releases remain unauthorized.

## D044 — 2026-10-21: Consolidate native exports and generate specialty indexes

- **Status:** Implemented and locally verified; unstaged and uncommitted.
- **Decision:** Generate and commit one native file per expert and host under
  `dist/codex/` and `dist/claude/`. Generate a host chooser and alphabetical and
  specialty indexes from the existing canonical metadata. Keep profiles and
  the full human catalogue under `src/roles/`; update download links and remove
  the old export copies.
- **Rationale:** Ready-to-use text exports are directly consumable from a Git
  revision. Forty-nine of the fifty-seven experts have multiple specialties,
  including seven spanning groups. Index links support those relationships
  without duplicated files, arbitrary primary specialties or unstable paths.
- **Checks and boundary:** Follow the
  [distribution contract](design.md#distribution-layout-and-generated-indexes).
  Preserve native bytes and source content, check all indexes and links, and
  add CI consistency checks. Leave this work uncommitted; deployment, consuming
  integrations, tags and releases are separate. Versioning and the first release
  remain pending.
- **Verification:** 25 tests pass and all 119 generated files match. All 114
  exports are byte-identical after relocation; source content, generated
  catalogue sections and profile prose/credits are preserved. Local links and
  an isolated starter trial pass. The CI workflow is configured but has not run
  on GitHub. See the
  [distribution evidence](../evidence/README.md#distribution-layout--2026-10-21).

## D045 — 2026-10-21: Establish whole-library versioning and release v1.0.0

- **Status:** Adopted first stable baseline and authorized delivery.
- **Decision:** Version the complete library as `MAJOR.MINOR.PATCH`, independently
  of consuming integrations. Start at `v1.0.0`, finalize its dated changelog and
  version references, and publish a fixed annotated tag and matching GitHub
  release. Keep version guidance in the main README and delivery guide rather
  than adding a competing version document or per-expert version fields.
- **Rationale:** Follow the release conventions already used by Project
  Structure and the public method repositories. One version identifies a
  reviewed snapshot of the profiles, metadata, templates, tooling and both
  native distributions. Compatibility concerns documented interfaces, stable
  identifiers/paths and intended role behavior; it does not imply broader host
  validation or measured role benefit.
- **Authority and checks:** The owner explicitly requests committing all pending
  work and releasing the first version. This supersedes the earlier uncommitted
  boundary for D044. Follow the
  [release contract](design.md#versioning-and-first-release), including signed
  commit, exact-commit hosted checks, verified annotated tag, public release
  readback and clean local state. Source archives follow the peer convention;
  host-specific packages and consumer changes remain outside this release.


## D046 — 2026-10-21: Clarify AI identity and offer featured-expert removal

- **Status:** Adopted; signed commit and push authorized.
- **Decision:** Add a dedicated main README section for featured experts and
  representatives to request corrections or voluntary removal privately at
  `leonid@komarovsky.info`. State target response times, minimal identity
  confirmation and the limits concerning historical and third-party copies.
  Replace the shared role opening with an explicitly AI-inspired perspective
  and a prohibition on claiming to be or represent the expert or their estate;
  substitute each expert's own name and regenerate both native formats.
- **Rationale:** Make independence explicit in execution instructions and offer
  an accessible request process without requiring a legal complaint. This is
  a presentation and maintenance policy, not legal clearance or a claim of
  improved role behavior.
- **Checks and boundary:** Follow the
  [focused contract](design.md#expert-identity-wording-and-removal-requests).
  Keep the roster, profiles, descriptions, images, vocabulary, remaining shared
  instruction and generated indexes unchanged. Record the work under Unreleased;
  preserve published tags and leave deployment to consuming integrations.

## D047 — 2026-10-21: Review a generated studio portrait refresh

- **Status:** Adopted implementation scope; portrait acceptance remains pending owner review.
- **Decision:** Refresh suitable catalogue visuals using ImageGen, calibrate generation approaches, preserve reference provenance and applicable terms, and update contribution guidance to distinguish synthetic portraits from photographs and existing historical depictions.
- **Boundary:** Isolated worktree; no commit, push or release. Preserve role content and retain existing visuals where likeness is uncertain. See the [implementation contract](design.md#studio-portrait-refresh-for-owner-review).
- **Owner review:** Exclude drawings, paintings, statues and similar depictions
  from generation and restore the five original historical visuals. The first
  photographic results resembled background removal; compare a new studio pose,
  lighting and clothing on two trials before further replacements.

## D048 — 2026-10-21: Adopt the studio portrait method and apply it across the catalogue

- **Status:** Adopted style, implemented and locally checked; final portrait review pending.
- **Decision:** Use direct eye contact, reference-grounded likeness and a new
  studio sitting with a different moderately muted background for each expert.
  Document a reproducible method and apply it to every supported photographic
  subject. Preserve historical depictions, unsupported placeholders and uncertain
  likenesses. Keep source conditions and attribution.
- **Boundary:** Existing isolated worktree, no commit or push, no role-content
  or integration changes. See the [implementation contract](design.md#reproducible-studio-portrait-method-and-catalogue-rollout).

- **D048 result:** All 57 experts are assessed: 29 generated portraits, five
  retained photographs, five historical depictions and eighteen placeholders.
  The documented prompt/helper and 32 tests pass; 119 generated outputs match
  and 173 protected files remain unchanged. See the
  [rollout evidence](../evidence/README.md#studio-v1-method-and-catalogue-rollout--2026-10-21).

## D049 — 2026-10-21: Make portrait contributions consistently checkable

- **Status:** Credit template and repository validation implemented and locally
  checked; one independent fresh-session walkthrough completed in a disposable
  copy. The owner subsequently accepted the portrait selections under D050.
- **Decision:** Provide a copyable Image block, use explicit tool/date/model/
  method fields, and validate declarations and stable background recipes through
  normal generation, read-only check mode and the existing CI path. Invalid
  provenance must fail before exporter writes.
- **Source rights:** Keep supplied-reference attribution as project provenance.
  Preserve applicable source conditions when material is reused or adapted;
  generation does not automatically remove rights, transfer every input license
  to every output or create copyright in generated portions. Record source and
  contribution terms separately, using the existing conservative image policy.
- **Evidence boundary:** The synthetic new-profile test validates the documented
  tooling path, not image generation, independent agent behavior or likeness.
  The separate [walkthrough](../tests/portrait-walkthrough.md) subsequently
  completed one temporary Grace Hopper case with actual built-in generation,
  both exports, passing checks and rendered review. Its findings clarify the
  minimum generation record and permitted preview-tool choice; see the
  [observed results](../evidence/README.md#independent-portrait-contribution-walkthrough--2026-10-21).
  This is a bounded contributor observation, not repeatability or owner approval.
  Images, biographies, metadata, vocabulary, shared instructions and native role
  bytes are preserved. Keep the work uncommitted and unpushed.

## D050 — 2026-10-21: Accept the portrait refresh for a local commit

- **Status:** Portrait selections accepted by the owner after the bounded
  independent contributor check.
- **Decision:** Close current review notes and create one signed commit in the
  existing isolated worktree after final local checks. This supersedes the
  earlier no-commit boundary for the portrait refresh.
- **Boundary:** No push, merge, tag, release, roster change, role deployment or
  global configuration change. The published v1.0.0 baseline remains fixed.
- **Evidence:** See the [local closeout](../evidence/README.md#portrait-owner-acceptance-and-local-commit--2026-10-21).

## D051 — 2026-10-22: Assess local integration of the portrait work

- **Status:** Local rebase and squash-readiness assessment authorized; no push
  or merge into maintained main is included.
- **Decision:** Preserve both main's identity/request follow-up and the accepted
  portrait work. Keep the already delivered D046 record and renumber the local
  portrait decisions to D047–D050 to avoid conflicting identifiers. Preserve
  their original dates, policy and acceptance meaning.
- **Checks:** Follow the [integration contract](design.md#local-portrait-integration-assessment).
  Keep the original signed commit recoverable; verify the new signature,
  generated consistency, protected content and a disposable squash result.

## D052 — 2026-10-22: Squash locally and prepare v1.1.0

- **Status:** Owner-authorized local integration and minor-release preparation.
- **Decision:** Squash the accepted, rebased portrait work into local main and
  create one signed commit including release preparation. This supersedes
  D051's no-merge boundary. Keep the published v1.0.0 tag fixed; do not push,
  create a version tag or publish a release.
- **Version rationale:** The reproducible portrait workflow and provenance
  checks are compatible capabilities. Use v1.1.0 for the whole library,
  including main's AI-identity and featured-expert request follow-up since
  v1.0.0. Existing identifiers, metadata, formats, export paths and intended
  role scope remain compatible.
- **Checks and handover:** Follow the
  [preparation contract](design.md#local-squash-merge-and-v110-preparation).
  Preserve the accepted portrait tree outside release documentation. Provide
  a dated changelog, draft notes, signed commit and local evidence. Hosted CI,
  annotated tagging, publication and remote readback await separate authority.

## D053 — 2026-10-22: Increase generated portrait coverage

- **Status:** Owner-authorized reference research and local image work.
- **Decision:** Try harder to cover remaining photographic subjects with
  generated portraits, especially Eliyahu Goldratt. Reassess the retained photos
  and name placeholders using the adopted method and verified source terms.
- **Boundary:** Preserve historical artwork, accepted generated images and all
  role content. Keep new candidates and results local and uncommitted; no push,
  version tag, release publication or consumer change is included. Follow the
  [coverage contract](design.md#increase-photographic-portrait-coverage).

## D054 — 2026-10-22: Standardize native export provenance

- **Status:** Adopted; local implementation authorized.
- **Decision:** Every Codex and Claude Code export carries generated source,
  whole-library version and expert ID comments. One root `VERSION` file owns
  the version; use `1.1.0-dev` for the current development exports. Keep comments
  outside execution instructions and ordinary host settings.
- **Boundary:** The owner accepted D053's expanded portrait result before this
  decision. Preserve all visuals and role behavior. D054 permits provenance-only
  native byte changes and relevant generator, checks and documentation updates.
  It authorizes no commit, deployment or publication. Follow the
  [provenance contract](design.md#standard-export-provenance).

## D055 — 2026-10-22: Publish Expert Roles v1.1.0

- **Status:** Owner-authorized release.
- **Decision:** Release the accepted portrait expansion and export provenance
  standard together with the previously prepared v1.1.0 work. Set `VERSION` and
  both export formats to `1.1.0`; finalize the changelog and release notes.
- **Boundary:** A signed release commit, ordinary main push, annotated v1.1.0
  tag and latest stable GitHub release are authorized. Require completed
  exact-commit workflow and validation-check success before tagging, preserve
  v1.0.0 and verify remote delivery. This supersedes the earlier no-commit/push
  boundaries for this release; installation remains separate. Follow the
  [publication contract](design.md#publish-expert-roles-v110).

## D056 — 2026-10-22: Separate source contributions and release artifacts

- **Status:** Adopted by the owner; locally implemented and checked. The owner
  authorizes a signed process commit and ordinary main push, with hosted
  workflow and artifact verification separate from the local evidence.
- **Decision:** Ordinary contributions contain canonical sources, relevant
  authored documentation and an Unreleased changelog entry. Maintainers choose
  versions and regenerate committed `dist/` files, indexes and catalogue blocks
  in a separate release change. Keep `dist/` committed for released consumers.
- **Checks:** Validate sources and isolated previews for contributions; reject
  release-owned edits. Require an explicit maintainer `release` PR label,
  changed final version, dated changelog and strict output freshness for release
  changes. See the [contract](design.md#separate-contributions-from-release-preparation).
- **Boundary:** Supersedes D044's requirement to commit sources and generated
  outputs together for ordinary contributions. Preserve published versions,
  roster, visuals and role behavior. No new release or installation is included.

## D057 — 2026-10-22: Make the README a concise catalogue introduction

- **Status:** Implemented and checked; the owner accepted the rendered result
  and authorized its squash merge, completed in source PR #12.
- **Decision:** Put a recognizable six-expert sample before setup, use concrete
  task cues, and keep image disclosure concise on the homepage while retaining
  accessible labels and complete profile credits. Simplify usage and project
  information, preserve optional expert requests and the correction/removal
  policy, and link to detailed guides. See the
  [contract](design.md#readme-presentation-refresh).
- **Checks:** Source and ownership validation, the contract suite, unchanged
  native payloads and protected profiles, resolving preview links and actual
  rendered review. Preserve the contribution/release separation.
- **Boundary:** All eleven reviewed expert PRs are merged, giving 68 source
  profiles. v1.1.0 remains the published baseline with 57 distributed experts.
  The owner requests the README improvement and separate release preparation;
  publication and installation remain outside this work.

## D058 — 2026-10-22: Prepare a separate v1.2.0 candidate

- **Status:** Preparation authorized; locally implemented and checked. The
  separate release candidate remains subject to PR review and hosted checks.
- **Decision:** Use a compatible minor increment for eleven new experts and the
  source/process/presentation improvements. Set the candidate to `1.2.0` and
  refresh committed catalogues, distribution indexes and native provenance in
  a separate maintainer release PR. See the
  [contract](design.md#prepare-v120-without-publication).
- **Checks:** Full suite, source validation, strict freshness, release ownership,
  native parity and payload preservation, complete local links, public content,
  whitespace and exact-head hosted checks. Preserve all source profiles and
  fixed published tags.
- **Boundary:** The candidate depends on D057's separate source PR. Update it
  against main and repeat release ownership after that source change merges.
  v1.1.0 remains the latest published version. No tag, publication, installation,
  role invocation or consuming-plugin update is authorized here.

## D059 — 2026-10-22: Publish Expert Roles v1.2.0

- **Status:** The owner accepted the rendered result and explicitly authorizes
  the README squash merge, updating the release PR against main, its merge and
  publication of the new version. D057's source PR is squash merged as
  `6a301fec01e9ebb96c5a813cb20bcc74cf00fdfe`.
- **Decision:** Finalize the separate v1.2.0 release PR against updated main,
  retain its `release` label and publish the compatible minor baseline after
  the required local and hosted gates. See the
  [publication contract](design.md#publish-expert-roles-v120).
- **Checks:** Recheck release ownership against main, all 55 tests, 141 generated
  outputs, 68 native pairs, preserved source and role payloads, links and public
  content. Require completed exact-head hosted checks on the PR and resulting
  main, then verify the annotated tag and latest stable release readback.
- **Boundary:** Supersedes D058's no-publication hold for v1.2.0 only. Keep prior
  release tags fixed, preserve native descriptions and instructions, and leave
  installation, role invocation and consuming-plugin updates separate.
