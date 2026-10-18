# Expert Roles library guidance

This repository owns the public role collection, its documentation, references,
examples and contribution guidance. Leon.id Komarovsky is the project owner.

Read [README.md](README.md), [PROJECT.md](PROJECT.md) and
[current work](docs/current-work.md) before acting. Follow relevant links to
recover the existing agreement and context before asking the owner to repeat it.
Use [design](docs/design.md), [decisions](docs/decisions.md),
[checks](tests/README.md), [evidence](evidence/README.md) and
[delivery](docs/delivery.md) to keep intent, work and results connected.

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

Record adopted decisions and pending choices separately in `docs/decisions.md`.
Role format, evaluation protocol and licensing remain pending. Public visibility
does not authorize selecting license terms or accepting third-party role text.

Before implementing an approved piece of work, record its implementation
contract and relevant checks in the design or linked element records. Keep
prepared checks, observed results, interpretations and pending outcomes distinct.
Respect the owner's authorization and the current completion boundary. Do not
turn structural validation into a claim that roles improve model performance.

Update [current work](docs/current-work.md) before handover and meaningful changes
in [CHANGELOG.md](CHANGELOG.md). Follow the README release convention when a
release is authorized; this documentation task does not authorize tags or a
release. Keep records proportionate and link existing detail instead of copying
it into competing sources.

For documentation-only changes, check relative links, UTF-8 readability, the
proposed Git diff and the full public tree. Add meaningful role validation when
the format and behavior are approved. Keep commits signed using the configured
Git identity and retain an ordinary reviewable history.
