# Current work

## Current focus and status

D063 keeps source catalogues current between releases. The owner authorized
correcting the boundary, refreshing the public READMEs, cleaning the handover
records, and signed commits with a normal main push. No release is authorized.
See the [focused contract](design.md#keep-source-catalogues-current-between-releases).

- `--docs` refreshes only the main README and source catalogue's generated regions.
- `--check-docs` checks their freshness without writes. Contribution CI requires
  this result and rejects edits to VERSION, dist and dated release history.
- Source catalogues follow current main. Native exports and distribution indexes
  remain at the last prepared release; complete new outputs are reviewed in an
  isolated `0.0.0-preview` tree until release preparation.
- The accepted presentation removes visible per-image catalogue captions,
  retains accessible descriptions and profile credits, shows existing comparison
  cues, and features Jordan Peterson in place of Marie Curie on the homepage.

All 68 individual profiles, images, expert metadata, specialty vocabulary,
shared templates and released native files remain outside this change's scope.
No role installation, host configuration change or runtime invocation is included.

## Delivered source baseline

D062 delivered D060's documentation improvements and D061's preview checker
and cleaner role-header generator in signed commit
[`43023e2`](https://github.com/shpoont/expert-roles/commit/43023e2526bd7890c262ea65e419a94b155036f0).
Its [hosted Checks](https://github.com/shpoont/expert-roles/actions/runs/39819451865)
and validation check completed successfully. Local and remote main matched,
the commit signature was verified locally and by GitHub, and the tree was clean.

The seven documentation findings and independent discovery, host-setup and
contribution re-reviews are complete. They include source-based and local
rendered walkthroughs, not representative human research. D061's 70 tests and
fresh-preview reference checks passed before delivery. Earlier no-commit or
pending-publication statements describe their original historical checkpoints;
D062 superseded the source-delivery hold and D063 corrects the catalogue policy.
See the [evidence](../evidence/README.md) for observed results and limits.

## Published baseline

The latest released version is
[v1.2.0](https://github.com/shpoont/expert-roles/releases/tag/v1.2.0), published
on 2026-10-22. Its annotated tag identifies
`c493c44bd14c7a54adce74f10bb6ea3c5bfd7359` after
[successful exact-commit checks](https://github.com/shpoont/expert-roles/actions/runs/39789914230).
VERSION and released native provenance use `1.2.0`.

The collection contains **68 experts, 96 specialties in 14 groups**, with
50 generated portraits, five historical depictions, 13 placeholders and
136 native files. Prior release tags stay fixed. Current source presentation
can change independently of that native release baseline.

## Verification and handover

Use the [check expectations](../tests/README.md),
[source commands](../src/README.md#generate-the-catalogue-and-native-files) and
[delivery procedure](delivery.md#versions-and-releases). Confirm source and
catalogue validity, contribution ownership, the full suite, preview/public
references, native/source preservation and the complete diff. For authorized
source delivery, verify the signature, remote content and the exact pushed
commit's hosted workflow and validation check. Local success is not hosted CI.

Record observed results in [evidence](../evidence/README.md). Historical
portrait, integration and release details remain in that record and the
[decision log](decisions.md); they are not unfinished current work.

## Next actions

A new release requires a separate owner instruction, version choice and release
PR. Only that process updates dist, native version comments and published tags.
The cleaner role-header formatting is present in the generator and previews;
retained v1.2.0 exports keep their original comments until release preparation.

A separate plugin owns role deployment and lifecycle. Existing Codex runtime
coverage is limited to three explicitly registered one-off samples; automatic
directory discovery and Claude runtime remain unverified. Broader comparative
benefit and contributor outcomes require separate evaluation. Accepted name
placeholders remain valid where a usable photographic reference is unavailable.
