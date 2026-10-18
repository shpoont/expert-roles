# Expert Roles

## Purpose

Build a public collection of reusable expert perspectives, methods and role
instructions for AI assistants. People should be able to browse, discuss and
contribute roles directly, independently of the tools that consume them.

**Status: initial design scaffold. No role definitions have been published.**
The role roster, format, contents and evaluation approach remain under design.

## Start and continue work

Read the [current project agreement](PROJECT.md), [design](docs/design.md) and
[current work](docs/current-work.md). Follow their links to the relevant
decisions, checks and evidence. Keep one current source for each agreement and
update connected records when the understanding changes.

## Role catalogue

Browse the top-level [roles directory](roles/README.md). It is the intended home
of the canonical role definitions. There are no roles to install or run yet.

## Project boundary

This repository will own role content, references, examples and guidance for
contributors. Host-specific integrations can consume a selected revision of the
collection and manage their own packaging and behavior.

See [PROJECT.md](PROJECT.md) for the current scope, expectations, authority and
open questions, and [delivery](docs/delivery.md) for use and handover. Repository
organization does not establish role effectiveness.

## Contribute

See [CONTRIBUTING.md](CONTRIBUTING.md). During the design stage, use
[issues](https://github.com/shpoont/expert-roles/issues) to propose roles, discuss
their purpose and sources, and suggest how to evaluate them. Role files and
templates will follow an agreed format.

## Decisions and ownership

Leon.id Komarovsky maintains this project. Lasting decisions and open choices
are recorded in [decisions](docs/decisions.md). The repository follows
[Project Structure v1.0.0](https://github.com/shpoont/project-structure/releases/tag/v1.0.0),
adapted to keep the role catalogue directly discoverable.

## Versions and releases

The role library has no released baseline yet. Its release history is independent
of the starter and consuming integrations. Record meaningful changes under
**Unreleased** in [CHANGELOG.md](CHANGELOG.md).

For an approved release, use `MAJOR.MINOR.PATCH`: major for incompatible changes,
minor for compatible additions and patch for corrections that preserve the
intended behavior and agreements. Review the intended scope and evidence,
finalize the dated changelog entry and version references, and commit the exact
contents before creating an annotated `vMAJOR.MINOR.PATCH` tag. Released tags
remain fixed; a hosted release, when used, refers to the same tag. This structure
adoption creates no role-library release or tag.

## Find project information

| Location | What it contains |
| --- | --- |
| [PROJECT.md](PROJECT.md) | Current purpose, scope, expectations and responsibilities. |
| [docs/](docs/README.md) | Design, current work, decisions, delivery and element detail. |
| [roles/](roles/README.md) | Canonical role catalogue; currently empty. |
| [src/](src/README.md) | Guide to working materials and their canonical locations. |
| [mocks/](mocks/README.md) | Future examples and explorations, with their limitations. |
| [tests/](tests/README.md) | Checks and assessments; role-quality evaluation is pending. |
| [evidence/](evidence/README.md) | Selected results and the limits of what was verified. |

## License status

A license has not been selected. Public visibility does not settle distribution
or reuse terms. License and contribution terms remain an owner decision before
role content is accepted for distribution.
