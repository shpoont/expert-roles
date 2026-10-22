# Current work

## Current focus and status

D064 authorizes the v1.3.0 release PR, local and hosted checks, squash merge,
annotated tag and publication if every gate passes. This supersedes the earlier
no-release hold for v1.3.0 only. See the
[release contract](design.md#release-expert-roles-v130).

- `--docs` refreshes only the main README and source catalogue's generated regions.
- `--check-docs` checks their freshness without writes. Contribution CI requires
  this result and rejects edits to VERSION, dist and dated release history.
- Source catalogues follow current main. This release sets VERSION and all
  native headers to `1.3.0` and regenerates dist; future source contributions
  leave those versioned outputs alone until their release preparation.
- The accepted presentation removes visible per-image catalogue captions,
  retains accessible descriptions and profile credits, shows existing comparison
  cues, and features Jordan Peterson in place of Marie Curie on the homepage.

All 68 individual profiles, images, expert metadata, specialty vocabulary and
shared templates remain unchanged. Native files change only their comments;
all 136 parsed role payloads remain unchanged.
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

## Delivered catalogue correction

D063's verified signed commit
[`4a162b6`](https://github.com/shpoont/expert-roles/commit/4a162b6a3ab970ba9d0c3ade26a32e1250273811)
delivered the catalogue/release boundary correction. Its
[hosted Checks](https://github.com/shpoont/expert-roles/actions/runs/39842759977)
and validation check completed successfully with all 72 tests. GitHub-rendered
HTML confirmed 68 catalogue images without visible captions and the accepted
Jordan Peterson homepage card; accessible image descriptions remain present.

## Versioned release baseline

VERSION and native provenance use `1.3.0`. The
[v1.3.0 release record](https://github.com/shpoont/expert-roles/releases/tag/v1.3.0)
and fixed annotated tag establish publication only after D064's required checks.
The previous v1.2.0 tag remains at
`c493c44bd14c7a54adce74f10bb6ea3c5bfd7359`, with its
[successful checks](https://github.com/shpoont/expert-roles/actions/runs/39789914230).

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

D064's publication gates apply only to v1.3.0. Any subsequent release requires a
new owner instruction and release PR. Only that process updates dist, native
version comments and published tags. Source catalogues continue to track main.

A separate plugin owns role deployment and lifecycle. Existing Codex runtime
coverage is limited to three explicitly registered one-off samples; automatic
directory discovery and Claude runtime remain unverified. Broader comparative
benefit and contributor outcomes require separate evaluation. Accepted name
placeholders remain valid where a usable photographic reference is unavailable.
