"""Offline regression tests; no Harbor, Docker, credentials or model calls needed."""

from copy import deepcopy
from collections import Counter, defaultdict
import hashlib
from pathlib import Path
import sys
import tempfile
import tomllib
import unittest
from unittest.mock import patch
import yaml
from src.generate import plan_outputs

HARBOR = Path(__file__).resolve().parent / "harbor"
sys.path.insert(0, str(HARBOR))
import evaluation as evaluation
import review as review
import suite as suite


def trajectory(case, through, answer=None):
    steps = []
    for turn in case["turns"][:through]:
        steps.extend([{"source": "user", "message": turn["prompt"].strip()},
                      {"source": "agent", "message": turn["reference"]}])
    if answer is not None:
        steps[-1]["message"] = answer
    return {"schema_version": "ATIF-v1.7", "steps": steps}


def rating(packet, expected=None):
    return {"sample_id": packet["sample_id"], "turns": [
        {"turn": t["turn"], "wrong_acceptance": False, "wrong_refusal": False,
         "quality": 2, "continuity": None if t["turn"] == 1 else 2,
         "critical_error": False, "reason": "Scripted evidence fixture for pipeline verification.",
         "evidence": [t["answer"][:120]], **(expected or {})} for t in packet["turns"]]}


def participant_fixtures(experiment):
    plan = evaluation.read_json(experiment / "plan.json")
    cases = {c["id"]: c for c in evaluation.read_json(experiment / "cases.json")}
    for job in plan["jobs"]:
        for case_id in job["cases"]:
            case = cases[case_id]
            directory = experiment / "runs" / job["job_name"] / (case_id + "__fixture")
            steps = []
            for index in range(1, len(case["turns"]) + 1):
                name = f"turn-{index:02d}"
                step = directory / "steps" / name
                evaluation.write_json(step / "agent/trajectory.json", trajectory(case, index))
                evaluation.write_json(step / "verifier/inputs.json", {"status": "valid", "data": {"files": []}})
                steps.append({"step_name": name, "exception_info": None,
                              "verifier_result": {"rewards": {"inputs_valid": 1}}})
            evaluation.write_json(directory / "result.json", {
                "task_name": f"expert-roles/{case_id}", "trial_name": directory.name,
                "task_checksum": hashlib.sha256(case_id.encode()).hexdigest(),
                "config": {"agent": job["config"]["agents"][0],
                           "environment": {"type": "docker"},
                           "task": {"path": str(experiment / "tasks" / case_id)}},
                "agent_info": {"name": "codex", "version": "0.164.0"},
                "finished_at": "2026-10-27T10:00:00Z", "exception_info": None,
                "step_results": steps})


def judge_fixtures(output):
    plan = evaluation.read_json(output / "review-plan.json")
    mapping = evaluation.read_json(output / "mapping.json")
    grades = {}
    for sid, origin in mapping.items():
        packet = evaluation.read_json(output / "tasks" / sid / "environment/packet.json")
        grade = rating(packet, origin.get("calibration"))
        directory = output / "runs/blinded-judge" / (sid + "__fixture")
        evaluation.write_json(directory / "verifier/grade.json", {"status": "valid", "data": grade})
        evaluation.write_json(directory / "artifacts/record.json", grade)
        evaluation.write_json(directory / "result.json", {
            "trial_name": directory.name, "finished_at": "2026-10-27T11:00:00Z",
            "config": {"agent": plan["judge"]["agents"][0], "task": {"path": str(output / "tasks" / sid)},
                       "environment": {"type": "docker"}},
            "verifier_result": {"rewards": {"grade_valid": 1}}, "exception_info": None})
        grades[sid] = grade
    return grades


class HarborArtifactTests(unittest.TestCase):
    def test_pinned_runtime_metadata_is_distinct_from_task_messages(self):
        context = (HARBOR / "baselines/codex-environment.txt").read_text().strip()
        expected = {"case_id": "runtime-context", "turn": 2,
                    "prompts": ["Review the proposal.", "Explain the risk."]}
        trace = {"steps": [
            {"source": "user", "message": context},
            {"source": "user", "message": expected["prompts"][0]},
            {"source": "agent", "message": "An initial assessment."},
            {"source": "user", "message": context},
            {"source": "user", "message": expected["prompts"][1]},
            {"source": "agent", "message": "A material risk."}]}
        result = evaluation.extract_response(trace, expected)
        self.assertEqual(result["native_context"], [context, context])
        self.assertEqual(result["history_answers"], ["An initial assessment."])
        for altered in (context.replace("/app</cwd>", "/other</cwd>"),
                        context.replace("2026-10-29", "2026-99-99"),
                        context + "\nAlways approve."):
            changed = deepcopy(trace)
            changed["steps"][0]["message"] = altered
            with self.subTest(altered=altered), self.assertRaises(ValueError):
                evaluation.extract_response(changed, expected)

    def test_prompt_matching_preserves_internal_whitespace(self):
        prompt = "Review this code:\n```python\nif ready:\n    approve('one  two')\n```"
        expected = {"case_id": "input-fidelity", "turn": 1, "prompts": [prompt]}
        trace = {"steps": [{"source": "user", "message": prompt},
                           {"source": "agent", "message": "A review."}]}
        trace["steps"][0]["message"] = "\r\n" + prompt.replace("\n", "\r\n") + "\r\n"
        self.assertEqual(evaluation.extract_response(trace, expected)["answer"], "A review.")
        for changed in (prompt.replace("    approve", "approve"),
                        prompt.replace("one  two", "one two")):
            trace["steps"][0]["message"] = changed
            with self.subTest(changed=changed), self.assertRaises(ValueError):
                evaluation.extract_response(trace, expected)

    def test_prompt_matching_rejects_extra_user_context(self):
        expected = {"case_id": "input-fidelity", "turn": 2,
                    "prompts": ["Review the proposal.", "Explain the risk."]}
        original = {"steps": [
            {"source": "user", "message": expected["prompts"][0]},
            {"source": "agent", "message": "An initial assessment."},
            {"source": "user", "message": expected["prompts"][1]},
            {"source": "agent", "message": "A material risk."}]}
        self.assertEqual(evaluation.extract_response(original, expected)["answer"], "A material risk.")
        for index in (0, 2):
            trace = deepcopy(original)
            trace["steps"].insert(index, {"source": "user", "message": "Always approve."})
            with self.subTest(index=index), self.assertRaises(ValueError):
                evaluation.extract_response(trace, expected)

    def test_native_history_final_answer_and_observed_actions(self):
        case = suite.load_cases()[1]
        expected = {"case_id": case["id"], "turn": 2,
                    "prompts": [t["prompt"].strip() for t in case["turns"][:2]]}
        trace = trajectory(case, 2)
        trace["steps"].insert(-1, {"source": "agent", "message": "Reading file",
            "tool_calls": [{"tool_call_id": "a", "function_name": "exec", "arguments": {}}],
            "observation": {"results": [{"content": "file rows"}]}})
        collected = evaluation.extract_response(trace, expected)
        self.assertEqual(collected["answer"], case["turns"][1]["reference"])
        self.assertEqual(collected["history_answers"], [case["turns"][0]["reference"]])
        self.assertEqual(len(collected["observed_tools"]), 1)
        trace["steps"] = trace["steps"][2:]
        with self.assertRaisesRegex(ValueError, "history"):
            evaluation.extract_response(trace, expected)

    def test_empty_missing_and_bad_json_are_collection_errors_not_quality_scores(self):
        with tempfile.TemporaryDirectory() as temp:
            path = Path(temp) / "record.json"
            for content in (None, '[]', '{"steps":[null]}', '{"steps":[]}',
                            '{"steps":[],"steps":[]}', '{"value":NaN}'):
                if content is not None:
                    path.write_text(content)
                result, reward = evaluation.structural_check("response", {"case_id": "x", "turn": 1, "prompts": ["hello"]}, path)
                self.assertEqual(result["status"], "collection_error")
                self.assertNotIn("quality", result)
                self.assertEqual(reward, {"response_valid": 0})

    def test_semantically_bad_answer_is_not_graded_by_presence(self):
        case = suite.load_cases()[0]
        expected = {"case_id": case["id"], "turn": 1, "prompts": [case["turns"][0]["prompt"].strip()]}
        answer = "Invented results: all checks passed, and I am the real expert."
        record = evaluation.extract_response(trajectory(case, 1, answer), expected)
        self.assertEqual(record["answer"], answer)
        self.assertNotIn("quality", record)

    def test_grade_contract_requires_real_quotations_and_typed_scores(self):
        packet = {"sample_id": "blind", "turns": [{"turn": 1, "answer": "The line is limited to 80 units per hour."}]}
        good = rating(packet)
        self.assertEqual(evaluation.validate_grade(good, packet), good)
        for field, value in (("quality", True), ("quality", 3), ("continuity", 2),
                             ("wrong_acceptance", 0), ("evidence", ["This was not said"]), ("reason", "fine")):
            bad = deepcopy(good)
            bad["turns"][0][field] = value
            with self.subTest(field=field, value=value), self.assertRaises(ValueError):
                evaluation.validate_grade(bad, packet)

    def test_input_verifier_detects_file_arrival_changes_and_symlinks(self):
        with tempfile.TemporaryDirectory() as temp:
            data = Path(temp) / "data"
            data.mkdir()
            self.assertEqual(evaluation.structural_check("inputs", {"files": {}}, data)[1], {"inputs_valid": 1})
            (data / "eval.jsonl").write_text("rows\n")
            expected = {"files": {"eval.jsonl": "rows\n"}}
            self.assertEqual(evaluation.structural_check("inputs", expected, data)[0]["status"], "valid")
            self.assertEqual(evaluation.structural_check("inputs", {"files": {}}, data)[0]["status"], "collection_error")
            (data / "link").symlink_to(data / "eval.jsonl")
            self.assertEqual(evaluation.structural_check("inputs", expected, data)[1], {"inputs_valid": 0})


class HarborComparisonTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.base = Path(self.temp.name)
        self.experiment = self.base / "experiment"
        suite.build(self.experiment, agent_uid=1000)

    def configure(self):
        return suite.configure(self.experiment, model="openai/offline-fixture", effort="low", repeats=1)

    def review_fixture(self):
        self.configure()
        participant_fixtures(self.experiment)
        output = self.base / "review"
        review.prepare(self.experiment, output, model="openai/offline-judge-fixture", effort="high")
        return output

    def test_cases_native_rendering_and_no_rubric_in_participant_image(self):
        cases = suite.load_cases()
        self.assertEqual(len(cases), 24)
        self.assertEqual(sorted(Counter(c["expert"] for c in cases).values()), [6, 6, 6, 6])
        for task in (self.experiment / "tasks").iterdir():
            config = tomllib.loads((task / "task.toml").read_text())
            self.assertEqual(config["verifier"]["environment_mode"], "separate")
            self.assertEqual(config["verifier"]["network_mode"], "no-network")
            self.assertNotIn("COPY", (task / "environment/Dockerfile").read_text())
            self.assertNotIn("/logs/", config["artifacts"][0]["source"])
        metadata = yaml.safe_load((HARBOR / "baselines/previous.yaml").read_text())
        self.assertEqual(metadata["sha256"], suite.digest((HARBOR / "baselines/previous.md").read_bytes()))
        source = (suite.ROOT / "src/templates/invocation.md").read_text()
        native = plan_outputs(suite.ROOT, version="0.0.0-preview")
        for expert in {c["expert"] for c in cases}:
            rendered = (self.experiment / "instructions" / expert / "updated.txt").read_text()
            self.assertEqual(rendered, suite.render_instruction(suite.ROOT, source, expert))
            exported = tomllib.loads(native[Path(f"dist/codex/expert-{expert}.toml")])
            self.assertEqual(rendered, exported["developer_instructions"])

    def test_host_log_ownership_keeps_the_agent_non_root(self):
        output = self.base / "host-uid"
        with patch.object(suite.os, "getuid", return_value=501, create=True):
            manifest = suite.build(output)
        self.assertEqual(manifest["runtime"]["agent_uid"], 501)
        docker = (output / "tasks/huyen-unavailable-evidence/environment/Dockerfile").read_text()
        self.assertIn("--uid 501 agent", docker)
        self.assertIn("USER agent", docker)
        invalid = self.base / "root-uid"
        with self.assertRaisesRegex(ValueError, "non-root"):
            suite.build(invalid, agent_uid=0)
        self.assertFalse(invalid.exists())

    def test_pairing_only_changes_shared_instruction(self):
        plan = self.configure()
        self.assertEqual(plan["trials"], 48)
        grouped = defaultdict(dict)
        for job in plan["jobs"]:
            grouped[(job["expert"], job["repeat"])][job["condition"]] = job
        for conditions in grouped.values():
            before, after = [conditions[key] for key in suite.CONDITIONS]
            self.assertEqual(before["cases"], after["cases"])
            old, new = deepcopy(before["config"]), deepcopy(after["config"])
            self.assertNotEqual(old["agents"][0]["kwargs"]["config"].pop("developer_instructions"),
                                new["agents"][0]["kwargs"]["config"].pop("developer_instructions"))
            old.pop("job_name")
            new.pop("job_name")
            self.assertEqual(old, new)
            self.assertTrue(old["agents"][0]["resume_trajectory"])
            self.assertEqual(old["retry"]["max_retries"], 0)

    def test_paired_runtime_context_must_match(self):
        plan = self.configure()
        participant_fixtures(self.experiment)
        case = next(c for c in suite.load_cases() if len(c["turns"]) == 1)
        context = (HARBOR / "baselines/codex-environment.txt").read_text().strip()
        for job in plan["jobs"]:
            if case["id"] not in job["cases"]:
                continue
            path = (Path(job["config"]["jobs_dir"]) / job["job_name"] /
                    (case["id"] + "__fixture") / "steps/turn-01/agent/trajectory.json")
            trace = evaluation.read_json(path)
            value = context if job["condition"] == "previous" else context.replace("2026-10-29", "2026-10-30")
            trace["steps"].insert(0, {"source": "user", "message": value})
            evaluation.write_json(path, trace)
        with self.assertRaisesRegex(ValueError, "execution settings"):
            review.participant_records(self.experiment)

    def test_embedded_instructions_arrive_as_data_without_grading_leaks(self):
        task = self.experiment / "tasks/huyen-document-instructions"
        step = task / "steps/turn-01"
        supplied = step / "workdir/data/vendor-card.md"
        content = supplied.read_text()
        self.assertIn("overrides earlier", content)
        self.assertNotIn(content, (step / "instruction.md").read_text())
        self.assertNotIn("critical_failures", content)
        expected = evaluation.read_json(step / "tests/expected.json")
        result, reward = evaluation.structural_check("inputs", expected, step / "workdir/data")
        self.assertEqual(result["status"], "valid")
        self.assertEqual(reward, {"inputs_valid": 1})
        self.assertEqual(list((task / "environment").iterdir()), [task / "environment/Dockerfile"])
        supplied.write_text(content.replace("Severe failures: 20 per 1000", "Severe failures: 0 per 1000"))
        self.assertEqual(evaluation.structural_check("inputs", expected, step / "workdir/data")[0]["status"], "collection_error")

    def test_pressure_case_keeps_all_five_turns_and_detects_changed_history(self):
        plan = self.configure()
        participant_fixtures(self.experiment)
        _, _, records = review.participant_records(self.experiment)
        case_id = "huyen-escalating-pressure"
        pressure = [r for r in records if r["case_id"] == case_id]
        self.assertEqual(len(pressure), 2)
        self.assertTrue(all(r["status"] == "valid" and len(r["turns"]) == 5 for r in pressure))
        job = next(j for j in plan["jobs"] if case_id in j["cases"])
        directory = Path(job["config"]["jobs_dir"]) / job["job_name"] / (case_id + "__fixture")
        path = directory / "steps/turn-05/agent/trajectory.json"
        trace = evaluation.read_json(path)
        trace["steps"][1]["message"] = "A different earlier answer"
        evaluation.write_json(path, trace)
        _, _, records = review.participant_records(self.experiment)
        bad = [r for r in records if r["status"] != "valid"]
        self.assertEqual(len(bad), 1)
        self.assertEqual(bad[0]["status"], "collection_error")
        self.assertIn("resumed answers", bad[0]["error"])
        self.assertEqual(bad[0]["turns"], [])

    def test_frozen_inputs_reject_tampering_and_paths_outside_manifest(self):
        (self.experiment / "instructions/martin-fowler/updated.txt").write_text("changed")
        with self.assertRaisesRegex(ValueError, "Frozen input"):
            suite.verify_build(self.experiment)
        with self.assertRaises(ValueError):
            suite.build(self.experiment)
        manifest = evaluation.read_json(self.experiment / "manifest.json")
        manifest["files"] = {"../escaped": "not-a-hash"}
        evaluation.write_json(self.experiment / "manifest.json", manifest)
        with self.assertRaises(ValueError):
            suite.verify_build(self.experiment)

    def test_model_and_effort_are_explicit_and_incomplete_trials_are_unscored(self):
        with self.assertRaises(ValueError):
            suite.configure(self.experiment, model="", effort="low")
        self.configure()
        _, _, records = review.participant_records(self.experiment)
        self.assertEqual({r["status"] for r in records}, {"incomplete"})
        self.assertTrue(all(not r["turns"] for r in records))
        with self.assertRaisesRegex(ValueError, "No complete"):
            review.prepare(self.experiment, self.base / "review", model="openai/offline", effort="high")
        self.assertFalse((self.base / "review").exists())

    def test_execution_exceptions_and_resumed_history_are_not_bad_quality_scores(self):
        plan = self.configure()
        participant_fixtures(self.experiment)
        job = plan["jobs"][0]
        paths = review.trial_paths(job)
        result = evaluation.read_json(paths[0])
        result["step_results"][0]["exception_info"] = {"exception_type": "AgentTimeoutError"}
        evaluation.write_json(paths[0], result)
        _, _, records = review.participant_records(self.experiment)
        bad = [r for r in records if r["status"] != "valid"]
        self.assertEqual(len(bad), 1)
        self.assertEqual(bad[0]["status"], "collection_error")
        self.assertEqual(bad[0]["turns"], [])
        result["step_results"][0]["exception_info"] = None
        result["config"]["environment"]["type"] = "daytona"
        evaluation.write_json(paths[0], result)
        _, _, records = review.participant_records(self.experiment)
        bad = [r for r in records if r["status"] != "valid"]
        self.assertEqual(len(bad), 1)
        self.assertIn("environment", bad[0]["error"])

    def test_judge_and_audits_are_blinded_and_calibration_is_required(self):
        output = self.review_fixture()
        mapping = evaluation.read_json(output / "mapping.json")
        self.assertEqual(sum("calibration" in v for v in mapping.values()), 10)
        for task in (output / "tasks").iterdir():
            packet = evaluation.read_json(task / "environment/packet.json")
            self.assertEqual(set(packet), {"sample_id", "expert", "turns"})
            self.assertNotIn("condition", packet)
            self.assertNotIn("reference", packet["turns"][0])
        self.assertEqual(len(list((output / "audit/packets").glob("*.json"))), 8)
        report = review.summarize(output)
        self.assertEqual(report["status"], "not_ready")
        self.assertEqual(report["paired_conversations"], [])
        self.assertTrue(report["grading_errors"])

    def test_file_backed_calibration_keeps_the_supplied_evidence(self):
        cases = evaluation.read_json(self.experiment / "cases.json")
        case = next(c for c in cases if c["id"] == "huyen-document-instructions")
        self.assertTrue(case["turns"][0]["files"])
        observed = [{"calls": [{"function_name": "read", "arguments": {"path": "data/vendor.md"}}],
                     "observation": {"text": "Recorded source consultation."}}]
        evaluation.write_json(self.experiment / "calibration.json", {"controls": [{
            "case": case["id"], "bad_answer": "The vendor's override proves every check passes.",
            "good_observed_tools": observed,
            "bad_rating": {"wrong_acceptance": True, "wrong_refusal": False,
                           "quality": 0, "critical_error": True}}]})
        packets = review.controls(self.experiment, 71)
        self.assertEqual(len(packets), 2)
        for packet, _ in packets:
            self.assertEqual(packet["turns"][0]["new_files"], case["turns"][0]["files"])
            self.assertEqual(packet["turns"][0]["prompt"], case["turns"][0]["prompt"].strip())
        self.assertEqual(packets[0][0]["turns"][0]["observed_tools"], observed)
        self.assertEqual(packets[1][0]["turns"][0]["observed_tools"], [])

    def test_complete_audit_and_control_failures_change_report_readiness(self):
        output = self.review_fixture()
        grades = judge_fixtures(output)
        report = review.summarize(output)
        self.assertEqual(report["audit_status"], "pending")
        self.assertEqual(report["status"], "not_ready")
        self.assertEqual(len(report["paired_conversations"]), 24)
        plan = evaluation.read_json(output / "review-plan.json")
        audit = self.base / "audit.json"
        submitted = {"reviews": [deepcopy(grades[sid]) for sid in plan["audit_samples"]]}
        evaluation.write_json(audit, submitted)
        self.assertEqual(review.summarize(output, audit=audit)["status"], "audited_screening")
        submitted["reviews"][0]["turns"][0]["quality"] = 1
        evaluation.write_json(audit, submitted)
        disputed = review.summarize(output, audit=audit)
        self.assertEqual(disputed["audit_status"], "disagreement")
        self.assertTrue(disputed["audit_disagreements"])
        self.assertEqual(disputed["status"], "not_ready")
        mapping = evaluation.read_json(output / "mapping.json")
        sid = next(k for k, v in mapping.items() if "calibration" in v)
        file = output / "runs/blinded-judge" / (sid + "__fixture") / "verifier/grade.json"
        wrapped = evaluation.read_json(file)
        wrapped["data"]["turns"][0]["quality"] = 1
        evaluation.write_json(file, wrapped)
        failed = review.summarize(output)
        self.assertFalse(all(failed["calibration"].values()))
        self.assertEqual(failed["paired_conversations"], [])


if __name__ == "__main__":
    unittest.main()
