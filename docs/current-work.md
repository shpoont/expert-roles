# Current work

## Current focus and status

D083 defines the v1.5.0 minor release from source PR #25. The owner authorized
both requested expert additions and publication through the protected process.
The baseline has 74 experts, 101 specialties and 148 native files. Preserve all
accepted profile and image sources, shared instructions and earlier native
payloads; only their version comments advance. Follow the
[release contract](design.md#release-expert-roles-v150) and
[procedure](delivery.md#versions-and-releases). Verify publication from the
matching signed annotated tag and remote release. Consumer deployment and the
two selected installations are separately owned; this library phase runs no
new live expert test or personal-file change.

## Released v1.4.2 context

D082 defines the v1.4.2 patch baseline from source PR #23. The owner authorized
the separate release PR, merge and publication through the protected process.
VERSION and all native version comments declare 1.4.2; exactly six Codex
candidates are normalized. Verify actual publication from the matching signed
annotated tag and remote release. Follow the
[release contract](design.md#release-expert-roles-v142) and
[procedure](delivery.md#versions-and-releases). No personal-role update, client
write, additional upstream native render or model run is part of this phase.

## Completed host-character correction

D081 corrects a newly observed v1.4.1 loader regression: six Codex nickname
values violate CLI 0.166.0's ASCII character restriction. The owner authorized
the narrowly scoped library fix and normal protected source/release pipeline;
the intended patch is v1.4.2. Canonical names, profiles, IDs, descriptions,
instructions, Claude semantics and personal installations remain fixed.

All 108 offline tests pass. The two planned offline renders selected 66 of 72
unchanged fixture definitions, then all 72 corrected definitions. Neither emitted
diagnostics, so the original diagnostic assertion failed and is retained. The
actual hash-verified Deming runtime error establishes the restriction; source
markers establish corrected loader acceptance. The evidence composition was
clarified within the original bounded scope. No model runs or retries occurred.
All other Codex fields, all Claude bytes and canonical inputs are preserved at
the same version. Source [PR #23](https://github.com/shpoont/expert-roles/pull/23)
was squash merged as `8416579` after its required PR checks. It left VERSION
and dist unchanged; the separate D082 release updates those artifacts.
See the [contract](design.md#host-valid-codex-nicknames) and
[bounded record](../evidence/README.md#codex-nickname-character-correction--2026-11-02).

## Released v1.4.1 context

D080 defines the v1.4.1 baseline from the merged D079 source correction and the already
accepted D078 provenance maintenance. The owner authorized a separate release
PR, its merge and publication after completed exact-commit workflow and
validation checks on the PR and resulting main. VERSION and generated exports
declare 1.4.1; verify publication from the matching remote release and tag. Follow
the [release contract](design.md#release-expert-roles-v141) and
[release procedure](delivery.md#versions-and-releases). No installation,
integration update or additional live expert test is part of this release.

## Completed Codex naming correction

The [issue #20](https://github.com/shpoont/expert-roles/issues/20) source candidate
implements [D079's contract](design.md#expert-names-for-codex-instances): derive
`nickname_candidates` from the existing expert name without changing other
Codex payload fields or Claude exports. All 105 offline tests pass. The owner
also authorized the planned host validation, using Codex CLI 0.166.0 and the
existing ChatGPT login with GPT-6.1 Sol/xhigh.

The first host attempt stopped after an unrelated configured nickname. The
subsequently authorized investigation established that the temporary project
was untrusted: Codex excluded its definition and exposed the existing personal
role instead. The CLI trust override had not activated the project layer.

A fresh `codex exec` cohort used normal configuration loading in a disposable
directory within an already trusted checkout. An offline marker check proved
the project definition was selected before each run; the exact export bytes
were restored before inference. The baseline received Archimedes, the configured
instance Martin Fowler, and the concurrent pair Martin Fowler and Martin
Fowler the 2nd. Distinct native IDs and overlapping execution were confirmed.
See [corrected host results and limits](../evidence/README.md#codex-configuration-trace-and-corrected-host-validation--2026-11-02).

Source implementation and the bounded CLI check are complete. Computer Use
blocks access to the Codex app, so desktop labels remain visually unconfirmed;
older-version compatibility and broader discovery reliability are untested.
Source [PR #21](https://github.com/shpoont/expert-roles/pull/21) was squash merged
as `569714d`; its exact-head PR and resulting-main workflow and validation
checks passed. The source PR preserved VERSION and dist. The separate D080
release updates those artifacts; profiles and personal installations stay fixed.

## Completed Project Structure update

D078 adopted Project Structure v1.0.1 provenance via
[.project-structure.yaml](../.project-structure.yaml). Project and contributor
guidance use that file as the baseline source; review previews retain it.
Project-specific adaptations, Expert Roles v1.4.0 and its native exports remain
unchanged. [D078](decisions.md#d078--2026-10-31-adopt-project-structure-v101-provenance)
records the adoption; focused results are retained in
[evidence](../evidence/README.md#project-structure-v101-provenance--2026-10-31).
[PR #19](https://github.com/shpoont/expert-roles/pull/19) was squash merged as
`48de2ce`; the exact-head PR and resulting main checks passed. No product
release, installation or runtime test was part of that update.

## Retained release and repair context

D077 prepared the v1.4.0 release from the accepted main source. It distributed
the four research and discovery additions and the shared consultation repairs.
D075 applied the tested goal-coverage paragraph to the existing shared
consultation draft. That increment preserves every previous instruction
paragraph and adds the tested 57 words verbatim. The combined source differs
from the isolated instruction and has passed its own four fresh checks.

The approved reconstructed source case concerns an expert endorsing a narrow
proposal without identifying an intended personal difference it leaves
unresolved. The original role missed that gap. A first repair passed once and
failed once; the refined paragraph passed both fresh repetitions. An explicitly
limited pilot and a new survey-review analogy also passed with both original
and refined roles. These are bounded observations, not general reliability.

The current application passed two fresh source-case conversations, the
limited-pilot control and the survey analogy using the combined instruction.
All 99 offline tests, source/catalogue validation, contribution ownership and
the complete preview's local references pass. Both native formats reproduce the
shared instruction for all 72 experts. The editorial cycle is complete, with
source-guide navigation and environment clarifications. The required comparative
Pro review is complete on the final instruction and guide, with no blocking
finding. Fresh preservation and blind-comprehension checks also pass. The pilot
answer respects the narrowed assignment but could attach its endorsement
condition more clearly. These results do not establish incremental benefit over
the 382-word draft.
See the [contract](design.md#goal-coverage-in-proposal-reviews),
[checks](../tests/README.md#goal-coverage-application-d075) and
[evidence](../evidence/README.md#goal-coverage-repair-and-application--2026-10-29).

D071's unsuccessful reproduction and D072–D074's separate expertise-boundary
experiments remain historical evidence. Their software/dinner case does not
reproduce the source consultation issue and does not establish its repair.
The earlier broad screening and grading remain archived; none replaces the
current literal before/after comparison.

Keep profiles, selection metadata, images, vocabulary, the accepted shared
instruction, installations and existing published tags unchanged. D077 updates
VERSION and committed dist through a separate release PR.

## Source PR closeout (D076)

The owner authorized the complete branch review and source PR preparation.
Retain the historical Harbor fixtures and their offline regressions because the
documentation and tests depend on them; keep private experiments outside Git.
Review found that collection could accept changed indentation or extra user
messages. Focused checks reproduced both weaknesses. The revised collector
preserves internal whitespace, rejects undeclared task messages and validates
the pinned adapter's environment metadata separately. The four saved D075
conversations pass the stricter check with unchanged answers; no inference was
rerun. All 103 offline tests, source/catalogue and ownership checks pass. The
complete preview's local references pass, and all 72 native pairs match the
reviewed instruction. [PR #17](https://github.com/shpoont/expert-roles/pull/17)
was squash merged as `58963f5`; its exact-head workflow and validate check passed,
as did the [resulting main checks](https://github.com/shpoont/expert-roles/actions/runs/41053842183).

## Release baseline

**v1.5.0 contains 74 experts, 101 specialties in 15 groups and 148 native role files.**
There are 54 generated portraits, five historical depictions and 15 placeholders.
Existing expert identifiers, selection descriptions, formats and paths remain
stable. The two new selection cues distinguish precise vector construction
from realistic vector rendering; both hosts' version comments advance. The
shared instruction and all prior native payloads are unchanged from v1.4.2.

The [release contract](design.md#release-expert-roles-v150) requires the full suite,
strict generated freshness, native equality, preservation and preview checks.
The release PR and resulting main workflow and validate check must all finish
successfully before tagging. The matching
[GitHub release](https://github.com/shpoont/expert-roles/releases/tag/v1.5.0)
and annotated tag establish publication separately from this declared baseline.
The earlier v1.3.0 publication remains in
[evidence](../evidence/README.md#v130-publication--2026-10-22).

## Verification and handover

Review the actual before/after answers and their limits separately from the
normal source/export checks. Verify exact instruction equality in both native
formats, fresh source catalogues, contribution ownership, the complete external
preview's local references, UTF-8, public suitability and protected-content
hashes. Review the entire proposed diff and inventory, including untracked files.

<a id="next-actions"></a>

## Delivery and follow-ups

D083 authorizes the release PR, merge and publication through the
[release procedure](delivery.md#versions-and-releases). Hosted checks and the
matching release record identify the actual remote state.
Nonblocking follow-ups are a case that preserves the requested distinction under a different
representation, and more explicit native-payload inspection guidance. The
current source guide supplies the file locations and formats; automated parity
was checked separately. Neither follow-up is a demonstrated prompt failure or
part of the completed case set.
Installation remains separate from library publication.
A separate plugin owns deployment and lifecycle. The behavioral checks use
explicitly supplied Codex instructions; they do not validate Claude runtime,
parent selection, installation or automatic directory discovery.
