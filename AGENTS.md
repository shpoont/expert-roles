# Expert Roles library guidance

This repository owns the public role collection, its documentation, references,
examples and contribution guidance. Leon.id Komarovsky is the project owner.

The current authorized scope is repository and contribution scaffolding only.
Do not implement expert roles, role schemas, templates, installers, native agent
deployment or orchestration until the owner agrees the design. Do not copy role
content from other projects as part of setup.

Keep the catalogue visible under top-level `roles/`. Host-specific integrations
are separate consumers. Keep plugin manifests, marketplace workflows and
consumer-specific configuration out of this repository unless explicitly agreed.

Every tracked file must be suitable for public viewing and self-contained.
Exclude private repository identities, internal coordination records,
conversation identifiers, author-machine paths, credentials and private evidence.

Record adopted decisions and pending choices separately in `docs/decision-log.md`.
Role format, evaluation protocol and licensing remain pending. Public visibility
does not authorize selecting license terms or accepting third-party role text.

For documentation-only changes, check relative links, UTF-8 readability, the
proposed Git diff and the full public tree. Add meaningful role validation when
the format and behavior are approved. Keep commits signed using the configured
Git identity and retain an ordinary reviewable history.
