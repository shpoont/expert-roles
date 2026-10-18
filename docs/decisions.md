# Decision log

## Purpose

Preserve lasting decisions about the role library, their ownership and rationale,
and the choices that remain open.

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
