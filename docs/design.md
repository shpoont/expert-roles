# Design and approach

## Approach and important parts

Follow the [project agreement](../PROJECT.md). The public library owns canonical
role content, references, examples and contribution guidance. Independent
integrations select a revision and own their host-specific behavior.

Keep the catalogue at top-level [roles/](../roles/README.md) for contributor
navigation. The [working-materials guide](../src/README.md) links to that
canonical location rather than duplicating it under `src/`. Use
[element records](elements/README.md) only when a real part needs more detail.

## Connections and open questions

No role representation, expert roster, evaluation method or runtime architecture
has been chosen. Proposed examples belong in [explorations](../mocks/README.md)
when authorized; evaluation criteria belong in [checks](../tests/README.md).
Retain relevant reasons in [decisions](decisions.md) and findings in
[evidence](../evidence/README.md).

## Implementation contract

The owner's current instruction authorizes structure alignment. For this piece
of work, implementation means: provide the starter's connected records, preserve
the visible catalogue and prior decisions, keep one current agreement and one
decision log, validate local navigation and public suitability, and make no role
or runtime implementation. The prepared checks are in
[tests/README.md](../tests/README.md).

Before later role implementation, agree its expected behavior, checks, observable
pass criteria and required evidence. Identify assessments that require actual
use and their responsible owner and timing. No such role contract is adopted
by this documentation alignment.

## Findings and changes

Record current status in [current work](current-work.md). When findings change
the design, update affected agreements and checks and retain lasting reasons in
the decision record.
