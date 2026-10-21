# Current work

## Current focus and status

D052 authorizes squashing the accepted portrait work into local main and
preparing **v1.1.0**, a compatible minor release. The signed local commit includes
the portrait implementation and release documentation. No push, tag or
publication is authorized. The latest published version remains v1.0.0. See the
[preparation contract](design.md#local-squash-merge-and-v110-preparation) and
[draft release notes](delivery.md#draft-release-notes-for-v110).

D051's rebase and disposable squash preview passed, including signature
verification and an exact tree match. The actual squash applies cleanly to
local main. Preserve main's delivered AI-identity wording and request policy
alongside the portrait work. Final checks and signed-commit readback are
recorded in the [preparation evidence](../evidence/README.md#local-squash-and-v110-preparation--2026-10-22).

The resolved candidate passes all 43 tests and all 119 generated outputs match.
All 114 native files and the shared instruction match current main; all 57
accepted visuals and profile bodies are unchanged from the portrait commit.
Local links, UTF-8, public suitability and whitespace checks pass. D046 remains
the delivered identity/request decision; the local portrait records are
renumbered to D047–D050 without changing their dates or meaning.

D050 records the [accepted portrait closeout](design.md#portrait-owner-acceptance-and-local-commit)
in the isolated worktree. The owner accepted the 29 selected portraits and
authorized one signed local commit, with no push or release. D049's copyable Image
credit block and explicit tool/date/model/method fields support future additions.
Normal generation and read-only check mode now validate portrait disclosures,
the stable background recipe and linked provenance before export writes;
the existing CI path runs these checks. The published v1.0.0 baseline stays fixed.

The independent [fresh-session walkthrough](../tests/portrait-walkthrough.md)
completed one temporary Grace Hopper contribution in a disposable copy of the
complete working tree. A fresh agent used the exact shared prompt and credit
template, one permitted photographic input, a separate held-out photograph and
one actual built-in image-generation call. The resulting 512 × 512 RGB JPEG,
both exports and rendered profile/catalogue passed the bounded check. All 43
tests passed in the copy and all 121 generated files matched. Existing expert
content, images and native bytes were preserved. Grace Hopper is only a fixture;
the real catalogue remains at 57 experts.

The walkthrough found nonblocking gaps in preview-tool choice and the
post-generation record format. The [workflow](elements/portraits.md) now makes
both explicit. A trailing blank line in the new synthetic test fixture was also
removed. The automated fixture remains separate evidence: it does not invoke an
image model. Broader independent reliability remains unverified. Owner acceptance
of the real portrait selections is recorded separately under D050. See the
[observations](../evidence/README.md#independent-portrait-contribution-walkthrough--2026-10-21).

D048's adopted studio-v1 rollout is preserved. All fifty-seven experts have explicit outcomes: **29 generated portraits,
five retained photographs, five original historical depictions and eighteen
full-name placeholders**. The three adopted samples are reused. Goldratt,
Watson and Kaplan retain photographs because their references lack detail;
Lupton's side view does not support a confident frontal likeness; Zelený's
output was blocked by the image tool. These are retained outcomes, not generated
portraits. Artwork and statues remain outside generation.

The [documented method](elements/portraits.md), shared prompt and local helper
record stable individual backgrounds, exact prompts, reference hashes and
deterministic 512 × 512 RGB JPEG preparation. The workflow and inputs are
reproducible; identical image-model output pixels are not guaranteed. Targeted
corrections and accepted-sample reuse are recorded separately.

**43 tests pass**, and all **119 generated files match** their sources.
All **173 protected files** retain their hashes, including all 114 native role
files, 57 metadata files, vocabulary and shared instruction. Non-image profile
content is unchanged for every expert. Active-image, source-credit, local-link
and public-content checks pass. See the
[rollout evidence](../evidence/README.md#studio-v1-method-and-catalogue-rollout--2026-10-21).

Final source review found and corrected a mixed-reference validation gap:
one reference's public-domain notice could mask another reference's missing
terms. Each labeled Source now needs its own linked terms or explicit
public-domain notice. Regression checks cover missing declarations and mixed
reuse grants; existing source permissions and all image bytes are preserved.

The earlier Safari review confirmed all 57 comparison cards and 143 loaded images,
with no broken images or horizontal overflow. The generated portraits were
also inspected together at catalogue size. The owner subsequently accepted the
portrait selections.
Final closeout readback confirms all 29 overview portraits load at catalogue
size without overflow. Fresh native screenshots returned a blank page, so no
new screenshot-backed visual acceptance is claimed.

Original images, licensed references, recipes, exact prompts, generated masters
and per-expert decisions remain in local task artifacts outside the public tree.
The published `v1.0.0` baseline stays fixed. D052 authorizes the signed squash
commit into local main and minor-release preparation; no push, tag, publication,
roster, role-instruction, deployment or integration change is included.

## Delivered AI-identity and request follow-up

D046 adds a [private correction/removal request process](../README.md#requests-from-featured-experts)
and explicit AI-inspired identity wording in the shared instruction and both
native formats. The request policy uses the maintainer's singular first-person
voice. The owner authorizes a signed commit and push for this focused
follow-up. It is included in the prepared v1.1.0 entry; the published v1.0.0
snapshot remains fixed. See the [contract](design.md#expert-identity-wording-and-removal-requests)
and [decision](decisions.md#d046--2026-10-21-clarify-ai-identity-and-offer-featured-expert-removal).
Local checks pass: 25 tests, all 119 generated outputs, 57 matching native
pairs and 1,932 resolved local references. Only the approved opening changes in
the 114 exports; profiles, visuals, metadata, descriptions and generated indexes
are preserved. See the [follow-up evidence](../evidence/README.md#ai-identity-and-featured-expert-requests--2026-10-21).

D046's implementation and local verification are complete. The Git history and
hosted checks record delivery of the authorized signed commit and push, including
the exact-commit CI outcome. This follow-up does not authorize a new release or
consuming-integration changes.

## Accepted baseline

The initial catalogue implementation and owner review are complete. On
2026-10-21, the owner accepted the rendered fifty-seven-expert catalogue,
including the seven philosophical additions, after the compact main README
review. D041 and the
[closeout contract](design.md#final-documentation-closeout-for-the-accepted-catalogue)
cover recording that acceptance, updating current guidance and final checks.
That closeout passed. The owner subsequently requested D042's
[visitor journey review](design.md#first-time-and-returning-visitor-journey-review)
before commit. Independent first-time and returning-visitor walkthroughs used
source files and fresh local-render screenshots. All five findings are resolved
in re-review, and a fresh independent final review found no blockers. Relevant
checks pass. The owner accepted the result and authorized the reviewed
catalogue's initial signed commit on 2026-10-21 under D043. That signed commit
was completed and subsequently pushed before D044 began.

The published v1.0.0 catalogue contained fifty-seven experts and eighty-two
specialties in ten groups, with thirty-eight credited portraits and nineteen
full-name SVG placeholders. Each expert has canonical metadata, a concise profile, one
square visual and generated Codex and Claude Code files. All accepted additions
are included; no profile, required image, layout or specialty decision remains
open. Other candidates remain proposals.

The compact main README retains its fixed six-expert showcase, with the complete
alphabetical and specialty catalogue beside the profiles. The broad scope,
expert criteria, shared instruction, optional perspective cues and licensing
policy remain adopted. Historical implementation and source findings are kept
in [decisions](decisions.md), [design](design.md) and
[evidence](../evidence/README.md); this status supersedes their earlier review
and completion dependencies.

The [latest addition checks](../evidence/README.md#seven-philosophy-additions--2026-10-21)
record twenty passing tests, 116 matching generated outputs, fifty-seven
agreeing native pairs and resolved local references. Sixty local HTML pages
were refreshed; Safari readback confirmed all fifty-seven catalogue rows and
seven new portrait images loaded. The
[closeout evidence](../evidence/README.md#accepted-catalogue-documentation-closeout--2026-10-21)
records acceptance and verification for D041's documentation tree. The
[visitor review evidence](../evidence/README.md#visitor-journey-review--2026-10-21)
records the current improvements, re-review and checks. These are expert
walkthroughs of local Markdown rendering, with actual-user, hosted GitHub and
assistive-technology outcomes unverified.

### Host validation and limits

The [Codex exec check](../evidence/README.md#codex-exec-retry--2026-10-20)
used CLI 0.163.0, fresh sessions and explicit invocation-only registrations.
Native calls and direct child responses confirmed three successful samples:
Nielsen was selected for a heuristic review, Goldratt challenged a forced
bottleneck conclusion and Norman declined astrophysics. The temporary exports
and project were removed afterward; personal roles were preserved.

Automatic Codex directory discovery remains unresolved. Claude exports have
syntax and consistency checks without runtime validation. Broader selection,
mixed requests, repeatability, comparative role benefit and contributor outcomes
remain untested. A separate plugin owns deployment, registration and lifecycle.
These follow-ups are separate from the accepted catalogue and commit readiness.

## Next actions

Review the prepared v1.1.0 changelog and draft release notes. Publication needs
its own owner instruction: push the signed main commit, require successful
hosted Checks for that exact commit, then verify and push an annotated v1.1.0
tag and publish the matching release. Read back the remote state before calling
the version released. No publication step is part of this local preparation.

The accepted portraits and bounded contribution walkthrough are retained; the
temporary Grace Hopper fixture is not a roster addition.

Further experts follow the existing [contribution process](../CONTRIBUTING.md).
Runtime or effectiveness work needs its own scope; deployment and role management
remain external.

## Findings and handover

Use [delivery](delivery.md#delivery-acceptance-and-remaining-work) for acceptance
and remaining obligations, [usage](delivery.md#use-a-native-role) for host limits,
[checks](../tests/README.md) for validation and
[evidence](../evidence/README.md#distribution-layout--2026-10-21)
for observed results. The Project Structure organization and independent
release convention remain in place. Original content uses MIT. Photographs and adaptations of licensed references
retain their individually credited terms; original generated contributions use
MIT to the extent rights can be granted.
