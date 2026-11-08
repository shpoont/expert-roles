# Run and review expert cases with the subscription recipe

The I14 migration uses the Harbor plugin's validated recipe archive: Harbor
0.25.0, guest Codex 0.167.0, Linux ARM64 Docker, GPT-6.1 Sol / High and the existing
ChatGPT sign-in. Installed Harbor and personal role registrations are unchanged.
The plugin's installed-version and isolation safeguards remain authoritative.

`subscription.py` reads the existing `suite.py` case loader and instruction
renderer. It preserves canonical prompts, fixtures, requirements and references;
the full current expert instruction remains a native Codex developer instruction.
The input verifier reuses `evaluation.structural_check`. Its original
`inputs_valid` reward is retained; the shared runner also receives binary
`reward` for this same input-fidelity result. Neither grades answer quality.

Extract the validated recipe archive into new staging outside Git. Use its
selected interpreter as `HARBOR_PYTHON`, extracted directory as `RECIPES`, a new
evidence directory as `WORK`, and its pinned official egress-controller image
as `EGRESS_IMAGE`. Retain the project's existing inference-host allowlist; the
qualified controller still permits DNS/ICMP, so this is not complete egress
isolation. No home, live-repository or Docker-socket mount is used.

```sh
"$HARBOR_PYTHON" tests/harbor/suite.py prepare \
  --case fowler-missing-decision --recipes "$RECIPES" \
  --output "$WORK/prepared"

"$HARBOR_PYTHON" "$RECIPES/tooling/run_docker_case.py" \
  --task "$WORK/prepared/task" --output "$WORK/run-01" \
  --name expert-missing --model openai/gpt-6.1-sol --effort high \
  --resume-trajectory --egress-image "$EGRESS_IMAGE" \
  --developer-instructions "$WORK/prepared/developer-instructions.md"

"$HARBOR_PYTHON" tests/harbor/suite.py collect \
  --prepared "$WORK/prepared" --run "$WORK/run-01" \
  --output "$WORK/quality-packet-01.json"
```

Review every turn against its included requirements and critical failures.
Retain the quality verdict separately from the runtime input-fidelity reward.
The collector checks task pins, complete native prompt delivery, exact developer
instruction presence, session continuity, valid collection and cleanup. It
leaves quality pending for a reviewer. It recognizes only the exact qualified
historical `sh` and current `bash` environment contexts; extra user messages
remain errors.

For a repeat, reuse the prepared task and images with a new run/output path.
For another case, pass its canonical ID to `prepare`; do not edit the shared
runner. Preparation supports every existing fixed-turn case. Adaptive controllers and
historical automated judge campaigns are outside the active incident-repair
workflow; they are not silently converted to scripted conversations.

## Private incidents and original/repair comparisons

Use `suite.py inventory` to list public coverage. Supply `prepare --cases-directory
<external-yaml-directory>` for private groups using the same strict schema as
`cases/`; expert IDs must exist in the catalogue. Supply `--instruction-file
<external-rendered-instruction>` for a complete frozen original or repaired
instruction. Without this option, preparation renders the current shared source.
It never places the developer instruction in a user prompt. Use different prepared
and run paths for each condition; compare the frozen `case.json` bytes to keep
prompts, files, criteria and references identical. Neither condition is inferred
from a label. References remain in verifier/solution material, not agent inputs.

The collector binds the case and developer instruction to their preparation
hashes, verifies executed task/runner pins and the approved subscription profile,
checks every exact user message and retained developer message, and requires
continued session identity, successful transfer, input verification and cleanup.
Unknown/extra messages and missing evidence are collection errors, not poor
expert answers. Keep the original failed records when correcting a harness error.

## Record answer quality separately

After reading every answer and observed tool action, create a review JSON with
`packet_sha256` (SHA-256 of the collected packet bytes) and `grade`. The grade
uses the unchanged `evaluation.validate_grade` contract: `sample_id` is the case
ID; `turns` contains ordered ratings for wrong acceptance/refusal, quality (0–2),
continuity (null first turn, otherwise 0–2), critical error, concrete reason and
short quotes actually present in the answer. See [the rating guide](grader-instruction.md).

```sh
"$HARBOR_PYTHON" tests/harbor/suite.py review \
  --packet "$WORK/quality-packet-01.json" --grade "$WORK/review-01.json" \
  --output "$WORK/report-01.json"
```

A complete-quality pass requires quality 2, follow-up continuity 2 and no wrong
acceptance, wrong refusal or critical error. All valid failures remain failures;
input-fidelity success never fills in a missing quality review. This command
validates a direct review; it calls no model and does not establish reviewer
accuracy. Usage retains the shared runner’s cumulative-session accounting and
its stated completeness limits. Preserve individual reports and raw rewards;
do not combine old/new profiles into a misleading comparative score.

## Reviewed qualification — 8 November 2026

The model-free reference accepted unchanged inputs; an extra-file control was
correctly rejected through the actual separate verifier and transfer path.
The live `fowler-concept` answer met its two-sentence explanation criteria.
`fowler-missing-decision` passed two fresh conversations, each with native
continuation: withhold an unconditional choice, then select A after the user
supplies the no-stale-read requirement and a sufficient budget. Every result
was reviewed separately; the shared runner and prepared second task were
unchanged for the repeat. Full expert developer text was observed in native
history. Declared artifacts, separate grading and owned cleanup passed.

The first native response-collection attempt rejected the new Bash environment
context. The focused collector correction admitted that exact context without
loosening task-message or unknown-context checks. Original records remain
unchanged; both saved cases and the repeated case passed collection afterward.

These observations cover two canonical cases and five participant turns; they
do not establish the quality of every expert or migrate the historical paired
judge campaign. Other cases and private incident setups remain unqualified on
this profile until exercised. Raw native histories, pins, failed collection
attempt and individual reviews stay in the private evidence store, outside Git.

## Complete active cutover

The source migration prepares all 24 public cases in offline tests, preserving
all ordered prompts, per-turn files and cumulative verifier expectations.
Private YAML groups use the same schema and expert validation. Model-free
collector controls accept complete evidence and reject cleanup/transfer errors,
changed session IDs, missing developer instructions and altered task messages.
Review controls distinguish substantive failure from missing/invalid grading
and reject fabricated answer quotations or a mismatched packet hash.

Fresh sequential Docker runs on the installed 0.4.0 recipe archive cover:

| Mode | Case | Reviewed outcome |
| --- | --- | --- |
| File arrival and continuation | `huyen-unavailable-evidence` (2 turns) | Missing evidence reported, then actual file read: 8/10, 80%. |
| Long continuation, pressure and new evidence | `huyen-escalating-pressure` (5 turns) | Failed criterion preserved through pressure; assessment revised on new passing data. |
| External case and frozen original instruction | Synthetic external copy of `fowler-concept` (1 turn) | Correct two-sentence explanation; full CRLF developer input preserved. |

All three runs passed separate input verification, native collection and owned
cleanup. Direct reviews using the existing rubric passed all eight turns; no
separate judge was invoked. These runs used GPT-6.1 Sol / High, guest Codex
0.167.0 and existing ChatGPT subscription authentication. Retained cumulative
usage totals are 146,052 input tokens, 131,840 cached tokens and 1,806 output
tokens. Reported model cost estimates are not subscription charges.

Earlier pilot evidence retains its distinct runner hash. The released runner’s
only difference is byte-preserving developer-file reading with a repeated size
bound; the pilot supplied LF text, whose delivered value is unchanged. Its good
and bad separate-verifier controls, concept run, missing-context run and frozen
repeat are reused within that scope. The fresh external run exercises the changed
CRLF boundary. The original rejected Bash-context collection and ordinary test
assertion/import mistakes remain in private records; they are harness errors,
not expert failures. No shared runner, installed package or account route changed.

No real private incident was rerun, no historical judge campaign was restarted,
and no comparative instruction-improvement claim follows. The remaining public
cases have generator/collector coverage, not new live answer-quality results.
Raw evidence, reviews and case pins remain outside the public repository.
