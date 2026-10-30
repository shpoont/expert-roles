"""Build frozen Harbor cases and explicitly configured paired Codex jobs."""

from __future__ import annotations

import argparse
import hashlib
import json
import os
from pathlib import Path, PurePosixPath
import random
import re

import yaml

from evaluation import read_json, write_json

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
CONDITIONS = ("previous", "updated")
EFFORTS = ("none", "minimal", "low", "medium", "high", "xhigh", "max")
MODEL_HOSTS = ("api.openai.com", "chatgpt.com", "*.chatgpt.com", "auth.openai.com")


def digest(content: bytes):
    return hashlib.sha256(content).hexdigest()


def load_cases(root: Path = ROOT):
    cases = []
    for path in sorted((root / "tests/harbor/cases").glob("*.yaml")):
        group = yaml.safe_load(path.read_text(encoding="utf-8"))
        if set(group) != {"expert", "cases"} or not isinstance(group["cases"], list):
            raise ValueError(f"Invalid case group: {path.name}")
        expert = group["expert"]
        if not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", expert):
            raise ValueError("Invalid expert identifier")
        if not (root / "src/roles" / expert / "expert.yaml").is_file():
            raise ValueError(f"Unknown catalogue expert: {expert}")
        for case in group["cases"]:
            if not {"id", "title", "turns"} <= set(case) <= {"id", "title", "turns", "equivalent_to"}:
                raise ValueError("Unexpected case fields")
            if not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", case["id"]):
                raise ValueError("Invalid case identifier")
            if not isinstance(case["title"], str) or not case["title"].strip() or not case["turns"]:
                raise ValueError("Case title and turns are required")
            for turn in case["turns"]:
                required = {"prompt", "requirements", "critical_failures", "reference"}
                if not required <= set(turn) <= required | {"files"}:
                    raise ValueError("Unexpected turn fields")
                for key in ("prompt", "reference"):
                    if not isinstance(turn[key], str) or not turn[key].strip():
                        raise ValueError(f"Nonempty {key} is required")
                for key in ("requirements", "critical_failures"):
                    if not isinstance(turn[key], list) or not turn[key] or any(
                            not isinstance(v, str) or not v.strip() for v in turn[key]):
                        raise ValueError(f"Nonempty {key} are required")
                if not isinstance(turn.get("files", {}), dict):
                    raise ValueError("Case files must be a mapping")
                for name, content in turn.get("files", {}).items():
                    p = PurePosixPath(name)
                    if (p.is_absolute() or ".." in p.parts or not p.parts
                            or p.parts[0] != "data" or len(p.parts) < 2 or not isinstance(content, str)):
                        raise ValueError("Case files must be text under data/")
            cases.append({**case, "expert": expert})
    ids = [case["id"] for case in cases]
    if not ids or len(set(ids)) != len(ids):
        raise ValueError("Case identifiers must be nonempty and unique")
    by_id = {case["id"]: case for case in cases}
    for case in cases:
        equivalent = case.get("equivalent_to")
        if equivalent and (equivalent not in by_id or by_id[equivalent]["expert"] != case["expert"]):
            raise ValueError("Equivalent briefs must name a case for the same expert")
    return cases


def render_instruction(root: Path, template: str, expert: str):
    if set(re.findall(r"\{\{(.*?)\}\}", template)) != {"name", "specialties"}:
        raise ValueError("Only the native name and specialties placeholders are supported")
    metadata = yaml.safe_load((root / "src/roles" / expert / "expert.yaml").read_text())
    registry = yaml.safe_load((root / "src/specialties.yaml").read_text())
    labels = [registry[key]["name"] for key in metadata["specialties"]]
    labels = labels[0] if len(labels) == 1 else ", ".join(labels[:-1]) + " and " + labels[-1]
    return template.strip().replace("{{name}}", metadata["name"]).replace("{{specialties}}", labels) + "\n"


def fresh_directory(path: Path, root: Path = ROOT):
    path = path.resolve()
    if path.exists() or path == root or root in path.parents or path in root.parents:
        raise ValueError("Use a new output directory outside the repository")
    path.mkdir(parents=True)
    return path


def emit(path: Path, text: str, executable=False):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")
    if executable:
        path.chmod(0o755)


def task_config(name: str, runtime: dict, steps=None, grading=False):
    artifact = "/app/grade.json" if grading else "/app/data"
    text = ('artifacts = [{ source = ' + json.dumps(artifact) + ', destination = "record.json" }]\n')
    if steps:
        text += 'multi_step_reward_strategy = "final"\n'
    text += f'''\n[task]
name = "expert-roles/{name}"
version = "0.1.0"

[environment]
cpus = 1
memory_mb = 2048
storage_mb = 4096
network_mode = "public"

[agent]
user = "agent"
timeout_sec = 300
network_mode = "allowlist"
allowed_hosts = {json.dumps(MODEL_HOSTS)}

[verifier]
user = "root"
timeout_sec = 30
environment_mode = "separate"
network_mode = "no-network"

[verifier.environment]
cpus = 1
memory_mb = 512
network_mode = "no-network"
'''
    for step in steps or []:
        text += '\n[[steps]]\nname = ' + json.dumps(step) + '\n'
    return text


def environment_files(path: Path, runtime: dict):
    uid = runtime["agent_uid"]
    if type(uid) is not int or uid <= 0:
        raise ValueError("The container agent UID must be a positive non-root integer")
    emit(path / "environment/Dockerfile", f'''FROM {runtime['base_image']}
RUN useradd --create-home --uid {uid} agent && mkdir -p /app/data && chown -R agent:agent /app
WORKDIR /app
USER agent
''')


def verifier_files(path: Path, expected: dict, *, grading=False):
    mode = "grade" if grading else "inputs"
    artifact = "/app/grade.json" if grading else "/app/data"
    emit(path / "test.sh", f'''#!/bin/bash
set -euo pipefail
python3 /tests/evaluation.py {mode} --expected /tests/expected.json \\
  --artifact {artifact} --output /logs/verifier/{mode}.json
''', executable=True)
    emit(path / "evaluation.py", (HERE / "evaluation.py").read_text())
    write_json(path / "expected.json", expected)


def oracle_script(path: Path, destination: str, value: dict):
    payload = json.dumps(value, ensure_ascii=False)
    emit(path, '#!/bin/bash\nset -euo pipefail\npython3 - <<\'PY\'\n'
         'from pathlib import Path\n'
         f'p = Path({destination!r})\np.parent.mkdir(parents=True, exist_ok=True)\n'
         f'p.write_text({payload!r}, encoding="utf-8")\nPY\n', executable=True)


def build(output: Path, *, root: Path = ROOT, agent_uid: int | None = None):
    cases = load_cases(root)
    source = root / "tests/harbor"
    runtime = yaml.safe_load((source / "runtime.yaml").read_text())
    if agent_uid is None:
        if not hasattr(os, "getuid"):
            raise ValueError("Specify --agent-uid for a host without a POSIX UID")
        agent_uid = os.getuid()
    if type(agent_uid) is not int or agent_uid <= 0:
        raise ValueError("Use a positive non-root agent UID; host UID 0 cannot run this default setup")
    runtime["agent_uid"] = agent_uid
    baseline = (source / "baselines/previous.md").read_bytes()
    provenance = yaml.safe_load((source / "baselines/previous.yaml").read_text())
    if digest(baseline) != provenance["sha256"]:
        raise ValueError("The frozen previous instruction has changed")
    updated = (root / "src/templates/invocation.md").read_bytes()
    templates = {"previous": baseline.decode(), "updated": updated.decode()}
    rendered = {expert: {condition: render_instruction(root, template, expert)
                        for condition, template in templates.items()}
                for expert in sorted({case["expert"] for case in cases})}
    output = fresh_directory(output, root)
    emit(output / "LICENSE", (root / "LICENSE").read_text())
    emit(output / "grader/instruction.txt", (source / "grader-instruction.md").read_text())
    emit(output / "grader/evaluation.py", (source / "evaluation.py").read_text())
    write_json(output / "calibration.json", yaml.safe_load((source / "calibration.yaml").read_text()))
    for expert, conditions in rendered.items():
        for condition, instruction in conditions.items():
            emit(output / "instructions" / expert / f"{condition}.txt", instruction)
    for case in cases:
        task = output / "tasks" / case["id"]
        steps = [f"turn-{i:02d}" for i in range(1, len(case["turns"]) + 1)]
        emit(task / "task.toml", task_config(case["id"], runtime, steps))
        environment_files(task, runtime)
        history, supplied_files = [], {}
        for index, (name, turn) in enumerate(zip(steps, case["turns"]), 1):
            step = task / "steps" / name
            emit(step / "instruction.md", turn["prompt"].strip() + "\n")
            for name, text in turn.get("files", {}).items():
                emit(step / "workdir" / name, text)
                supplied_files[name.removeprefix("data/")] = text
            expected = {"case_id": case["id"], "turn": index,
                        "files": dict(supplied_files)}
            verifier_files(step / "tests", expected)
            history += [{"step_id": len(history) + 1, "source": "user", "message": turn["prompt"].strip()},
                        {"step_id": len(history) + 2, "source": "agent", "message": turn["reference"]}]
            oracle_script(step / "solution/solve.sh", "/logs/agent/trajectory.json",
                          {"schema_version": "ATIF-v1.7", "agent": {"name": "oracle-fixture", "version": "1"},
                           "steps": history})
    write_json(output / "cases.json", cases)
    hashes = {str(p.relative_to(output)): digest(p.read_bytes())
              for p in sorted(output.rglob("*")) if p.is_file()}
    manifest = {"schema_version": 1, "runtime": runtime, "baseline": provenance,
                "instruction_sha256": {"previous": digest(baseline), "updated": digest(updated)},
                "cases": [{"id": c["id"], "expert": c["expert"], "turns": len(c["turns"])} for c in cases],
                "files": hashes}
    write_json(output / "manifest.json", manifest)
    return manifest


def verify_build(output: Path):
    output = output.resolve()
    manifest = read_json(output / "manifest.json")
    for name, expected in manifest["files"].items():
        path = output / name
        if (Path(name).is_absolute() or ".." in Path(name).parts
                or output not in path.resolve().parents or path.is_symlink()
                or any(p.is_symlink() for p in path.parents if p != output and output in p.parents)
                or not path.is_file() or digest(path.read_bytes()) != expected):
            raise ValueError(f"Frozen input changed: {name}")
    return manifest


def agent_settings(model: str, effort: str, instruction: str, runtime: dict, *, resume=False):
    if not model.startswith("openai/") or len(model) <= len("openai/") or any(c.isspace() for c in model):
        raise ValueError("Select an explicit openai/ model for this Codex-only comparison")
    if effort not in EFFORTS:
        raise ValueError("Choose an explicit effort supported by the pinned Harbor adapter")
    return {"name": "codex", "model_name": model, "resume_trajectory": resume,
            "kwargs": {"version": runtime["codex_version"], "reasoning_effort": effort,
                       "disable_web_search": True,
                       "config": {"developer_instructions": instruction, "web_search": "disabled"}}}


def job_config(name: str, jobs_dir: Path, tasks: list[Path], agent: dict, concurrency=1):
    return {"job_name": name, "jobs_dir": str(jobs_dir.resolve()), "n_attempts": 1,
            "n_concurrent_trials": concurrency, "retry": {"max_retries": 0},
            "environment": {"type": "docker"}, "agents": [agent],
            "tasks": [{"path": str(p.resolve())} for p in tasks]}


def configure(output: Path, *, model: str, effort: str, repeats=2, seed=43):
    manifest = verify_build(output)
    if repeats < 1 or repeats > 20:
        raise ValueError("Repeats must be between one and twenty")
    config_dir = output / "configs"
    if config_dir.exists():
        raise ValueError("Configuration already exists; build a new frozen experiment")
    jobs = []
    for repeat in range(1, repeats + 1):
        for expert in sorted({c["expert"] for c in manifest["cases"]}):
            tasks = [output / "tasks" / c["id"] for c in manifest["cases"] if c["expert"] == expert]
            random.Random(seed + repeat).shuffle(tasks)
            for condition in CONDITIONS:
                name = f"{expert}-{condition}-r{repeat:02d}"
                instruction = (output / "instructions" / expert / f"{condition}.txt").read_text()
                agent = agent_settings(model, effort, instruction, manifest["runtime"], resume=True)
                config = job_config(name, output / "runs", tasks, agent)
                jobs.append({"job_name": name, "expert": expert, "condition": condition,
                             "repeat": repeat, "cases": [p.name for p in tasks], "config": config})
    random.Random(seed).shuffle(jobs)
    for job in jobs:
        write_json(config_dir / f"{job['job_name']}.json", job["config"])
    plan = {"model": model, "effort": effort, "repeats": repeats, "seed": seed,
            "trials": len(manifest["cases"]) * 2 * repeats, "jobs": jobs}
    write_json(output / "plan.json", plan)
    return plan


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest="command", required=True)
    build_parser = sub.add_parser("build", help="Freeze cases and both instructions; no model calls")
    build_parser.add_argument("--output", type=Path, required=True)
    build_parser.add_argument("--agent-uid", type=int,
                              help="Non-root container UID; defaults to the host UID for Harbor log ownership")
    config = sub.add_parser("configure", help="Write jobs with explicit settings; does not launch them")
    config.add_argument("--output", type=Path, required=True)
    config.add_argument("--model", required=True)
    config.add_argument("--effort", choices=EFFORTS, required=True)
    config.add_argument("--repeats", type=int, default=2)
    config.add_argument("--seed", type=int, default=43)
    args = parser.parse_args()
    if args.command == "build":
        result = build(args.output, agent_uid=args.agent_uid)
        print(f"Frozen {len(result['cases'])} cases; no jobs or model runs started.")
    else:
        result = configure(args.output, model=args.model, effort=args.effort,
                           repeats=args.repeats, seed=args.seed)
        print(f"Prepared {result['trials']} paired-condition trials; no jobs started.")


if __name__ == "__main__":
    main()
