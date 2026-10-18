# Tests and assessments

Checks follow the [project expectations](../PROJECT.md#scope-and-expectations)
and the [implementation contract](../docs/design.md#implementation-contract).
Manual review is appropriate for this documentation-only change; no runtime or
role-performance tests are introduced.

## Structure-alignment checks

Before committing and pushing this change, the implementer checks:

| Check | Pass condition |
| --- | --- |
| Starter coverage | All Project Structure v1.0.0 record locations are represented and adapted to this library. |
| Navigation | Every relative Markdown file link and local heading anchor resolves. |
| Canonical records | `PROJECT.md` holds the current agreement; `docs/decisions.md` is the sole decision log and preserves D001/D002. |
| Catalogue visibility | The root README links directly to top-level `roles/`; no duplicate role catalogue is introduced. |
| Scope and status | No role definitions, schemas, runtime, license choice or release is introduced; pending choices remain explicit. |
| Public suitability | Proposed public files contain no private project identities, conversation IDs, machine paths or credential material. |
| Git hygiene | The reviewed diff has no whitespace errors or unrelated changes. |

Record actual results, date, baseline and limitations in
[evidence](../evidence/README.md). Missing or failed required checks block the
corresponding completion claim; only the owner may authorize a permitted
exception within the agreed scope, recorded in [decisions](../docs/decisions.md)
without relabeling the check as passed.

## Later role assessments

Role behavior and benefit assessments remain pending design agreement. Prepare
their tasks, conditions, expected outcomes, comparison method, evidence and
responsible owner before implementation. A clean repository, valid role file or
well-formed output alone does not establish task usefulness.
