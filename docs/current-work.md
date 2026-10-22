# Current work

## Current focus and status

D065 covers the owner's two selected improvements: release safeguards and
concise active agent guidance. Follow the
[contract](design.md#release-safeguards-and-concise-agent-guidance).

- Require PRs and the current GitHub Actions `validate` check on main, with no
  bypass actors, no force pushes and no deletion. Zero required approvals keep
  a sole-maintainer PR workflow usable.
- Track the ruleset in `.github/rulesets/main.json`; verify both its hosted
  settings and effective main-branch rules.
- Add a release preflight/push helper that uses an explicit identical source and
  destination ref. It must ignore dangerous upstream/push.default configuration
  and leave main, tags and publication untouched.
- Keep AGENTS.md focused on durable policy and links, with completed release
  evidence here and in the existing historical records.

Implementation and local verification are complete. The hosted
[Protect main ruleset](https://github.com/shpoont/expert-roles/rules/25674519)
is active; its settings and effective rules match the tracked policy.
All 83 tests pass, including disposable Git regressions, and source/release
ownership and retained-output freshness pass. Source changes are prepared for
PR review; their hosted CI and merge are separate delivery evidence.
Preserve all experts, metadata,
visuals, specialties, templates, source catalogue blocks, VERSION, dist and
published tags. This is a source/process improvement, not a new release.
No installation, integration change or role-runtime evaluation is included.

## Published baseline

**v1.3.0 is published as the latest stable release.**
[PR #14](https://github.com/shpoont/expert-roles/pull/14) was squash merged into
[`29e7636`](https://github.com/shpoont/expert-roles/commit/29e763631d953be8fc36d9b48b042e7f88da3179)
after completed successful [PR checks](https://github.com/shpoont/expert-roles/actions/runs/39846429359).
The resulting main's [workflow](https://github.com/shpoont/expert-roles/actions/runs/39846714660)
and separate validation check also completed successfully, including all
72 tests and strict freshness of 141 generated files.

The locally verified signed annotated `v1.3.0` tag targets that main commit.
Remote tag, latest stable [release](https://github.com/shpoont/expert-roles/releases/tag/v1.3.0),
notes, VERSION and both native headers were read back. Earlier release tags
were unchanged; release branches were removed and main was clean and synced.
See the [publication evidence](../evidence/README.md#v130-publication--2026-10-22).

The baseline contains **68 experts, 96 specialties in 14 groups**, 50 generated
portraits, five historical depictions, 13 placeholders and 136 native role files.
Source catalogues track current main independently of versioned native releases.

## Verification and handover

Use [tests](../tests/README.md#release-safeguards-d065) and
[delivery](delivery.md#release-safeguards) for the current checks. Reproduce the
push hazard only in disposable bare repositories. Hosted ruleset readback proves
configuration; do not risk changing live main to demonstrate a rejected push.
Record implemented changes, actual checks and remaining limits separately.

## Next actions

Review the source PR and its exact-head hosted checks before an authorized merge.
Future release PRs still require their own owner instruction; VERSION, dist and
published tags remain unchanged in this source contribution.

A separate plugin owns role deployment and lifecycle. Recorded library runtime
coverage remains three explicitly registered Codex samples; automatic directory
discovery and Claude runtime remain unverified. Broader selection reliability
and comparative benefit require separate evaluation. Quality-evaluation work
was not selected for this step.
