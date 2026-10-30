"""Prepare blinded Harbor judging and report paired results without hiding errors."""

from __future__ import annotations

import argparse
from collections import Counter, defaultdict
from copy import deepcopy
import json
from pathlib import Path
import random

from evaluation import extract_response, read_json, validate_grade, write_json
from suite import (CONDITIONS, EFFORTS, agent_settings, digest, emit, environment_files,
                   fresh_directory, job_config, oracle_script, task_config, verify_build,
                   verifier_files)

METRICS = ("wrong_acceptance", "wrong_refusal", "quality", "continuity", "critical_error")


def checked_trial(path, expected_agent, expected_task):
    result = read_json(path)
    if not result.get("trial_name") or "config" not in result:
        raise ValueError("Not a Harbor trial result")
    config = result["config"]
    if any(config.get("agent", {}).get(k) != v for k, v in expected_agent.items()):
        raise ValueError("Recorded agent settings differ from the planned condition")
    if Path(config.get("task", {}).get("path", "")).resolve() != expected_task.resolve():
        raise ValueError("Recorded task differs from the frozen task")
    if config.get("environment", {}).get("type") != "docker":
        raise ValueError("Recorded environment differs from the planned Docker environment")
    if not result.get("finished_at"):
        raise ValueError("Trial has not finished")
    exceptions = [result.get("exception_info")] + [
        step.get("exception_info") for step in result.get("step_results") or []]
    if any(exceptions):
        raise ValueError("Harbor recorded an execution exception")
    return result


def trial_paths(job):
    directory = Path(job["config"]["jobs_dir"]) / job["job_name"]
    return sorted(directory.glob("*/result.json"))


def participant_records(experiment):
    manifest = verify_build(experiment)
    plan = read_json(experiment / "plan.json")
    cases = {c["id"]: c for c in read_json(experiment / "cases.json")}
    records, seen = [], set()
    for job in plan["jobs"]:
        expert, condition, repeat = job["expert"], job["condition"], job["repeat"]
        if condition not in CONDITIONS or type(repeat) is not int or not 1 <= repeat <= plan["repeats"]:
            raise ValueError("Invalid condition or repetition in plan")
        instruction = (experiment / "instructions" / expert / f"{condition}.txt").read_text()
        agent = agent_settings(plan["model"], plan["effort"], instruction, manifest["runtime"], resume=True)
        if job["config"]["agents"] != [agent]:
            raise ValueError("Plan changed the frozen instruction or model settings")
        expected_cases = {c["id"] for c in manifest["cases"] if c["expert"] == expert}
        if set(job["cases"]) != expected_cases or len(job["cases"]) != len(expected_cases):
            raise ValueError("Plan changed the matched case set")
        discovered = defaultdict(list)
        for path in trial_paths(job):
            result = read_json(path)
            case_id = Path(result.get("config", {}).get("task", {}).get("path", "")).name
            if case_id not in expected_cases:
                raise ValueError("Unexpected trial in a planned job")
            discovered[case_id].append(path)
        for case_id in job["cases"]:
            key = (case_id, condition, repeat)
            if key in seen:
                raise ValueError("Duplicated planned condition")
            seen.add(key)
            record = {"case_id": case_id, "expert": expert, "condition": condition,
                      "repeat": repeat, "status": "incomplete", "turns": []}
            paths = discovered[case_id]
            try:
                if len(paths) != 1:
                    raise ValueError("Missing or duplicated trial result")
                task = experiment / "tasks" / case_id
                result = checked_trial(paths[0], agent, task)
                steps = result.get("step_results") or []
                if len(steps) != len(cases[case_id]["turns"]):
                    raise ValueError("Incomplete multi-turn trial")
                native_context = []
                for index, (step, turn) in enumerate(zip(steps, cases[case_id]["turns"]), 1):
                    name = f"turn-{index:02d}"
                    if step.get("step_name") != name:
                        raise ValueError("Wrong or reordered conversation step")
                    reward = (step.get("verifier_result") or {}).get("rewards") or {}
                    directory = paths[0].parent / "steps" / name
                    wrapped = read_json(directory / "verifier/inputs.json")
                    expected = {"case_id": case_id, "turn": index,
                                "prompts": [t["prompt"].strip() for t in cases[case_id]["turns"][:index]]}
                    actual = extract_response(read_json(directory / "agent/trajectory.json"), expected)
                    if reward.get("inputs_valid") != 1 or wrapped.get("status") != "valid":
                        raise ValueError("Synthetic input verification failed")
                    if actual["history_answers"] != [t["answer"] for t in record["turns"]]:
                        raise ValueError("Recorded resumed answers differ from earlier turns")
                    if actual["native_context"][:len(native_context)] != native_context:
                        raise ValueError("Recorded runtime context differs from earlier turns")
                    native_context = actual["native_context"]
                    record["turns"].append({"turn": index, "prompt": turn["prompt"].strip(),
                        "requirements": turn["requirements"], "critical_failures": turn["critical_failures"],
                        "new_files": turn.get("files", {}), "answer": actual["answer"],
                        "observed_tools": actual["observed_tools"]})
                if not result.get("task_checksum"):
                    raise ValueError("Harbor did not record a task checksum")
                execution = {k: deepcopy(result["config"].get(k)) for k in ("agent", "environment", "verifier")}
                execution["native_context"] = native_context
                execution["agent"]["kwargs"]["config"].pop("developer_instructions")
                record.update(status="valid", agent_info=result.get("agent_info"), task_checksum=result["task_checksum"],
                              execution_sha256=digest(json.dumps(execution, sort_keys=True).encode()))
            except (OSError, ValueError, KeyError, TypeError) as error:
                record["status"] = "incomplete" if not paths else "collection_error"
                record["error"] = str(error)[:400]
                record["turns"] = []
            records.append(record)
    expected_count = len(cases) * 2 * plan["repeats"]
    if len(records) != expected_count:
        raise ValueError("Plan omits required paired conditions")
    for case_id in cases:
        checksums = {r["task_checksum"] for r in records if r["case_id"] == case_id and r["status"] == "valid"}
        if len(checksums) > 1:
            raise ValueError("Paired trials used different Harbor task contents")
        settings = {r["execution_sha256"] for r in records if r["case_id"] == case_id and r["status"] == "valid"}
        if len(settings) > 1:
            raise ValueError("Paired trials used different recorded execution settings")
    return manifest, plan, records


def make_packet(sample_id, record):
    return {"sample_id": sample_id, "expert": record["expert"], "turns": record["turns"]}


def controls(experiment, seed):
    cases = {c["id"]: c for c in read_json(experiment / "cases.json")}
    packets = []
    for control in read_json(experiment / "calibration.json")["controls"]:
        case = cases[control["case"]]
        first = case["turns"][0]
        for kind, answer, expected in (
            ("good", first["reference"], {"wrong_acceptance": False, "wrong_refusal": False,
                                      "quality": 2, "critical_error": False}),
            ("bad", control["bad_answer"], control["bad_rating"])):
            sample_id = digest(f"{seed}:control:{case['id']}:{kind}".encode())[:16]
            record = {"expert": case["expert"], "turns": [
                {"turn": 1, "prompt": first["prompt"].strip(), "requirements": first["requirements"],
                 "critical_failures": first["critical_failures"], "new_files": first.get("files", {}),
                 "answer": answer, "observed_tools": deepcopy(
                     control.get("good_observed_tools", []) if kind == "good" else [])}]}
            packets.append((make_packet(sample_id, record), {**expected, "continuity": None}))
    return packets


def prepare(experiment, output, *, model, effort, audit_size=8):
    manifest, plan, records = participant_records(experiment)
    judge = agent_settings(model, effort, (experiment / "grader/instruction.txt").read_text(), manifest["runtime"])
    valid = [r for r in records if r["status"] == "valid"]
    if not valid:
        raise ValueError("No complete participant conversations are available for judging")
    if audit_size < 1:
        raise ValueError("At least one blinded audit sample is required")
    if audit_size < len({(r["expert"], r["condition"]) for r in valid}):
        raise ValueError("Audit size must cover every available expert/condition stratum")
    output = fresh_directory(output)
    packets, mapping = [], {}
    for record in valid:
        key = f"{plan['seed']}:{record['case_id']}:{record['condition']}:{record['repeat']}"
        sample_id = digest(key.encode())[:16]
        packets.append(make_packet(sample_id, record))
        mapping[sample_id] = {k: record[k] for k in ("case_id", "expert", "condition", "repeat")}
    for packet, expected in controls(experiment, plan["seed"]):
        packets.append(packet)
        mapping[packet["sample_id"]] = {"calibration": expected}
    random.Random(plan["seed"]).shuffle(packets)
    tasks = []
    for packet in packets:
        sample_id = packet["sample_id"]
        task = output / "tasks" / sample_id
        emit(task / "task.toml", task_config(sample_id, manifest["runtime"], grading=True))
        environment_files(task, manifest["runtime"])
        dockerfile = task / "environment/Dockerfile"
        dockerfile.write_text(dockerfile.read_text() + "COPY --chown=agent:agent packet.json /app/packet.json\n")
        write_json(task / "environment/packet.json", packet)
        emit(task / "instruction.md", "Evaluate /app/packet.json using your grading instructions. Write /app/grade.json.\n")
        verifier_files(task / "tests", packet, grading=True)
        emit(task / "tests/evaluation.py", (experiment / "grader/evaluation.py").read_text())
        # The oracle validates transfer and shape only; it does not calibrate a model.
        rating = {"sample_id": sample_id, "turns": [
            {"turn": t["turn"], "wrong_acceptance": False, "wrong_refusal": False,
             "quality": 2, "continuity": None if t["turn"] == 1 else 2, "critical_error": False,
             "reason": "Scripted schema fixture; this is not a semantic judgment.",
             "evidence": [t["answer"][:160]]} for t in packet["turns"]]}
        oracle_script(task / "solution/solve.sh", "/app/grade.json", rating)
        tasks.append(task)
    config = job_config("blinded-judge", output / "runs", tasks, judge)
    write_json(output / "judge.json", config)
    write_json(output / "mapping.json", mapping)
    write_json(output / "collection.json", records)
    # Round-robin strata before extra samples: every expert/condition is represented.
    strata = defaultdict(list)
    for sample_id, origin in mapping.items():
        if "calibration" not in origin:
            strata[(origin["expert"], origin["condition"])].append(sample_id)
    if audit_size < len(strata):
        raise ValueError("Audit size must cover every available expert/condition stratum")
    rng = random.Random(plan["seed"])
    for ids in strata.values():
        rng.shuffle(ids)
    selected = []
    while len(selected) < min(audit_size, len(valid)):
        for ids in strata.values():
            if ids and len(selected) < audit_size:
                selected.append(ids.pop())
    rng.shuffle(selected)
    packet_map = {p["sample_id"]: p for p in packets}
    for sample_id in selected:
        write_json(output / "audit/packets" / f"{sample_id}.json", packet_map[sample_id])
    write_json(output / "audit-template.json", {"reviews": [
        {"sample_id": sid, "turns": [{"turn": t["turn"],
            **{k: None for k in METRICS}, "reason": "", "evidence": []}
            for t in packet_map[sid]["turns"]]} for sid in selected]})
    write_json(output / "review-plan.json", {"participant": {k: plan[k] for k in ("model", "effort", "repeats", "seed")},
        "experiment_manifest_sha256": digest((experiment / "manifest.json").read_bytes()),
        "judge": config, "audit_samples": selected})
    hashes = {str(p.relative_to(output)): digest(p.read_bytes()) for p in sorted(output.rglob("*")) if p.is_file()}
    write_json(output / "manifest.json", {"runtime": manifest["runtime"], "files": hashes})
    return {"participants": len(valid), "controls": len(packets) - len(valid), "audit_samples": len(selected),
            "collection": dict(Counter(r["status"] for r in records))}


def collect_grades(output, plan):
    mapping = read_json(output / "mapping.json")
    found, errors = {}, {}
    job = {"job_name": plan["judge"]["job_name"], "config": plan["judge"]}
    for path in trial_paths(job):
        raw = read_json(path)
        sample_id = Path(raw.get("config", {}).get("task", {}).get("path", "")).name
        if sample_id not in mapping or sample_id in found or sample_id in errors:
            raise ValueError("Unexpected or duplicate judge trial")
        try:
            result = checked_trial(path, plan["judge"]["agents"][0], output / "tasks" / sample_id)
            wrapped = read_json(path.parent / "verifier/grade.json")
            reward = (result.get("verifier_result") or {}).get("rewards") or {}
            if wrapped.get("status") != "valid" or reward.get("grade_valid") != 1:
                raise ValueError("Judge did not produce a valid grade artifact")
            packet = read_json(output / "tasks" / sample_id / "environment/packet.json")
            raw_grade = read_json(path.parent / "artifacts/record.json")
            if raw_grade != wrapped.get("data"):
                raise ValueError("Transferred grade differs from the verifier record")
            found[sample_id] = validate_grade(raw_grade, packet)
        except (OSError, ValueError, KeyError, TypeError) as error:
            errors[sample_id] = str(error)[:400]
    for sample_id in mapping.keys() - found.keys() - errors.keys():
        errors[sample_id] = "Missing judge trial"
    return found, errors


def summarize(output, *, audit=None):
    verify_build(output)
    plan = read_json(output / "review-plan.json")
    mapping = read_json(output / "mapping.json")
    records = read_json(output / "collection.json")
    grades, errors = collect_grades(output, plan)
    submitted = read_json(audit) if audit is not None else None
    packets = {sid: read_json(output / "audit/packets" / f"{sid}.json")
               for sid in plan["audit_samples"]} if submitted is not None else {}
    return summarize_validated(plan, mapping, records, grades, errors,
                               audit=submitted, audit_packets=packets)


def summarize_validated(plan, mapping, records, grades, errors, *, audit=None, audit_packets=None):
    """Aggregate collected grades; callers must verify execution and input provenance first."""
    calibration = {}
    for sample_id, origin in mapping.items():
        if "calibration" in origin:
            calibration[sample_id] = sample_id in grades and all(
                grades[sample_id]["turns"][0][k] == v for k, v in origin["calibration"].items())
    audit_status, disagreements = "pending", []
    if audit is not None:
        submitted = audit
        if set(submitted) != {"reviews"} or not isinstance(submitted["reviews"], list):
            raise ValueError("Invalid audit submission")
        reviewed = {}
        for grade in submitted["reviews"]:
            sid = grade.get("sample_id")
            if sid not in plan["audit_samples"] or sid in reviewed:
                raise ValueError("Unexpected or duplicated audit sample")
            packet = audit_packets[sid]
            reviewed[sid] = validate_grade(grade, packet)
            if sid in grades:
                for human, model in zip(grade["turns"], grades[sid]["turns"]):
                    for metric in METRICS:
                        if human[metric] != model[metric]:
                            disagreements.append({"sample_id": sid, "turn": human["turn"], "metric": metric,
                                                  "audit": human[metric], "judge": model[metric]})
        audit_status = ("disagreement" if disagreements else "complete") if set(reviewed) == set(plan["audit_samples"]) else "incomplete"
    calibrated = bool(calibration) and all(calibration.values())
    pairs = defaultdict(dict)
    for sid, grade in grades.items():
        origin = mapping[sid]
        if "calibration" not in origin:
            pairs[(origin["case_id"], origin["repeat"])][origin["condition"]] = grade["turns"]
    rows = []
    if calibrated:
        for (case_id, repeat), conditions in sorted(pairs.items()):
            if set(conditions) == set(CONDITIONS):
                rows.append({"case_id": case_id, "repeat": repeat, "conditions": conditions})
    complete = all(r["status"] == "valid" for r in records) and not errors
    ready = complete and calibrated and audit_status == "complete"
    dimensions = {}
    for metric in METRICS:
        counts = {condition: Counter() for condition in CONDITIONS}
        changes = Counter()
        for row in rows:
            for before, after in zip(row["conditions"]["previous"], row["conditions"]["updated"]):
                values = (before[metric], after[metric])
                if None in values:
                    continue
                for condition, value in zip(CONDITIONS, values):
                    counts[condition][str(value).lower()] += 1
                delta = values[1] - values[0]
                if metric in ("wrong_acceptance", "wrong_refusal", "critical_error"):
                    delta = -delta
                changes["better" if delta > 0 else "worse" if delta < 0 else "same"] += 1
        dimensions[metric] = {"turn_distributions": {k: dict(v) for k, v in counts.items()},
                              "paired_turn_changes": dict(changes)}
    return {"status": "audited_screening" if ready else "not_ready", "participant": plan["participant"],
            "judge": {"model": plan["judge"]["agents"][0]["model_name"],
                      "effort": plan["judge"]["agents"][0]["kwargs"]["reasoning_effort"]},
            "collection": dict(Counter(r["status"] for r in records)), "grading_errors": errors,
            "calibration": calibration, "audit_status": audit_status, "audit_disagreements": disagreements,
            "paired_conversations": rows, "dimensions": dimensions,
            "unpaired_or_ungraded": len(records) - 2 * len(rows),
            "limits": ["A small shared-instruction screening, not an expert or model leaderboard.",
                       "No native subagent selection, Claude runtime or real-person fidelity is tested.",
                       "Requested model settings are recorded; provider internals are not independently attested.",
                       "Technical failures are unscored, and audit disagreements require review before conclusions."]}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest="command", required=True)
    prepare_parser = sub.add_parser("prepare", help="Collect trials and create blinded judge jobs; never runs them")
    prepare_parser.add_argument("--experiment", type=Path, required=True)
    prepare_parser.add_argument("--output", type=Path, required=True)
    prepare_parser.add_argument("--judge-model", required=True)
    prepare_parser.add_argument("--judge-effort", choices=EFFORTS, required=True)
    prepare_parser.add_argument("--audit-size", type=int, default=8)
    report = sub.add_parser("report", help="Read recorded results; incomplete or disputed evidence stays not_ready")
    report.add_argument("--output", type=Path, required=True)
    report.add_argument("--audit", type=Path)
    report.add_argument("--save", type=Path, required=True)
    args = parser.parse_args()
    if args.command == "prepare":
        result = prepare(args.experiment.resolve(), args.output, model=args.judge_model,
                         effort=args.judge_effort, audit_size=args.audit_size)
        print(result)
    else:
        result = summarize(args.output.resolve(), audit=args.audit)
        write_json(args.save, result)
        print(result["status"])


if __name__ == "__main__":
    main()
