# Current work

## Current focus and status

The **v1.0.0** whole-library baseline is complete. D044's
[distribution layout](design.md#distribution-layout-and-generated-indexes)
provides one native file per expert and host, plus generated alphabetical and
specialty indexes. D045 adopts the
[versioning and release procedure](delivery.md#versions-and-releases) and
explicitly authorizes committing all pending work, pushing it and releasing
this first version after checks. This supersedes the earlier uncommitted boundary.

Local verification passes: 25 tests, all 119 generated outputs, native syntax and
equality, local links/anchors and an isolated completed-starter trial. All 114
relocated exports retain their original bytes; expert metadata, visuals,
vocabulary, shared instructions and generated catalogue sections are preserved.
See the [distribution evidence](../evidence/README.md#distribution-layout--2026-10-21)
and [release preparation](../evidence/README.md#first-release-preparation--2026-10-21).

The [release record](https://github.com/shpoont/expert-roles/releases/tag/v1.0.0),
[fixed snapshot](https://github.com/shpoont/expert-roles/tree/v1.0.0) and
[hosted checks](https://github.com/shpoont/expert-roles/actions/workflows/checks.yml)
record publication and CI state. Delivery verifies the signed commit, successful
hosted checks for that exact commit, annotated tag, matching public release and
clean local tree; source preparation alone does not establish publication.

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

The catalogue contains fifty-seven experts and eighty-two specialties in ten
groups, with thirty-eight credited portraits and nineteen full-name SVG
placeholders. Each expert has canonical metadata, a concise profile, one
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

No catalogue implementation remains for the v1.0.0 baseline. Use the
[release procedure](delivery.md#versions-and-releases) for delivery; published
tags remain fixed and subsequent changes go under **Unreleased**. The owner has
authorized this first release, not future releases or consuming-integration work.

Further experts and optional portrait improvements follow the existing
[contribution process](../CONTRIBUTING.md). Later runtime or effectiveness work
needs its own agreed scope. Deployment and role management remain external.

## Findings and handover

Use [delivery](delivery.md#delivery-acceptance-and-remaining-work) for acceptance
and remaining obligations, [usage](delivery.md#use-a-native-role) for host limits,
[checks](../tests/README.md) for validation and
[evidence](../evidence/README.md#distribution-layout--2026-10-21)
for observed results. The Project Structure organization and independent
release convention remain in place. Original content uses MIT; portraits retain
their individually credited permission terms and are excluded from MIT.
