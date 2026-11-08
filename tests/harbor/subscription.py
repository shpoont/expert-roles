"""Prepare existing expert cases for the shared Docker/subscription recipe.

This adapter preserves canonical prompts, expert developer instructions and the
existing input verifier. A successful native reward establishes input fidelity;
response quality still requires review against the unchanged case criteria.
"""
import argparse
import hashlib
import json
from pathlib import Path
import re
import shutil
import subprocess

import suite
from evaluation import extract_response, validate_grade


def task_files(task):
    """Snapshot regular task files before execution; reject redirected inputs."""
    files = {}
    for path in sorted(task.rglob('*')):
        if path.is_symlink():
            raise ValueError('Frozen tasks must not contain symlinks')
        if path.is_file():
            files[str(path.relative_to(task))] = suite.digest(path.read_bytes())
    return files


def prepare(case_id, output, recipes, *, cases_directory=None, instruction_file=None):
    cases = {case['id']: case for case in suite.load_cases(directory=cases_directory)}
    if case_id not in cases:
        raise ValueError('Select a canonical case ID')
    case = cases[case_id]
    output = output.resolve()
    if output.is_relative_to(suite.ROOT):
        raise ValueError('Keep generated tasks and private runtime evidence outside source Git')
    output.mkdir(parents=True, exist_ok=False)
    task = output / 'task'
    env = task / 'environment'; env.mkdir(parents=True)
    base = recipes / 'examples/docker-codex-i01/environment/Dockerfile'
    dockerfile = base.read_text().replace('COPY --chown=node:node project/ /app/project/',
                                        'RUN mkdir -p /app/data && chown node:node /app/data')
    if dockerfile == base.read_text(): raise ValueError('Qualified agent recipe changed')
    (env / 'Dockerfile').write_text(dockerfile)
    instruction = suite.render_instruction(suite.ROOT,
        (suite.ROOT / 'src/templates/invocation.md').read_text(), case['expert'])
    if instruction_file is not None:
        instruction = instruction_file.read_bytes().decode("utf-8")
        if not instruction.strip() or "\x00" in instruction or len(instruction.encode()) > 131072:
            raise ValueError("Supply a complete nonempty rendered developer instruction up to 128 KiB")
    (output / 'developer-instructions.md').write_bytes(instruction.encode())
    config = '''schema_version = "1.4"
multi_step_reward_strategy = "final"
artifacts = [{source="/app/data", destination="data"}]
[task]
name = "expert-roles/subscription"
version = "0.1.0"
[agent]
user = "node"
timeout_sec = 600
network_mode = "allowlist"
allowed_hosts = HOSTS
[environment]
cpus = 1
memory_mb = 2048
network_mode = "public"
[verifier]
timeout_sec = 60
environment_mode = "separate"
'''.replace('HOSTS', json.dumps(suite.MODEL_HOSTS))
    contexts = {'agent': env}
    supplied = {}
    history = []
    for index, turn in enumerate(case['turns'], 1):
        name = f'turn-{index:02d}'; step = task / 'steps' / name
        tests = step / 'tests'; tests.mkdir(parents=True)
        (step / 'instruction.md').write_text(turn['prompt'].strip() + '\n')
        history += [{'step_id': len(history)+1, 'source': 'user', 'message': turn['prompt'].strip()},
                    {'step_id': len(history)+2, 'source': 'agent', 'message': turn['reference']}]
        suite.oracle_script(step / 'solution/solve.sh', '/logs/agent/trajectory.json',
            {'schema_version': 'ATIF-v1.7', 'agent': {'name': 'oracle-fixture', 'version': '1'}, 'steps': list(history)})
        for name_in, content in turn.get('files', {}).items():
            path = step / 'workdir' / name_in; path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(content); supplied[name_in.removeprefix('data/')] = content
        shutil.copy2(suite.HERE / 'evaluation.py', tests / 'evaluation.py')
        suite.write_json(tests / 'expected.json', {'files': dict(supplied)})
        (tests / 'check.py').write_text('''import json
from pathlib import Path
from evaluation import structural_check
logs = Path('/logs/verifier'); logs.mkdir(parents=True, exist_ok=True)
result, native = structural_check('inputs', json.loads(Path('/tests/expected.json').read_text()), Path('/app/data'))
clean = not any(Path(p).exists() for p in ('/tmp/codex-secrets', '/installed-agent/codex-home/auth.json'))
(logs/'inputs.json').write_text(json.dumps(result))
(logs/'checks.json').write_text(json.dumps({'no_agent_credentials_in_verifier': clean}))
(logs/'reward.json').write_text(json.dumps({**native, 'reward': float(result['status']=='valid' and clean)}))
''')
        (tests / 'test.sh').write_text('#!/bin/sh\nset -eu\npython3 /tests/check.py\n')
        (tests / 'Dockerfile').write_text('FROM python:3.12-slim-bookworm@sha256:6dd8b6dab6b3adc7812bab69eca5dbdc1a5cc690ad28306d234ffb4ef8ac9753\nCOPY . /tests/\nRUN chmod 755 /tests/test.sh\nWORKDIR /app\n')
        contexts[name] = tests
        config += f'\n[[steps]]\nname = "{name}"\nmin_reward = 1.0\n[steps.verifier.environment]\ncpus = 1\nmemory_mb = 512\nnetwork_mode = "no-network"\n'
    images = {}
    for role, context in contexts.items():
        with (output / f'build-{role}.log').open('w') as log:
            image = subprocess.run(['docker', 'build', '--quiet', str(context)], stdout=subprocess.PIPE,
                stderr=log, text=True, check=True, timeout=600).stdout.strip().splitlines()[-1]
        if not re.fullmatch(r'sha256:[0-9a-f]{64}', image): raise ValueError('Missing image pin')
        images[role] = image
    config = config.replace('[environment]\n', f'[environment]\ndocker_image = "{images["agent"]}"\n', 1)
    pins = iter(images[name] for name in contexts if name != 'agent')
    config = re.sub(r'\[steps.verifier.environment\]\n', lambda _: '[steps.verifier.environment]\ndocker_image = '+json.dumps(next(pins))+'\n', config)
    (task / 'task.toml').write_text(config)
    suite.write_json(output / 'case.json', case)
    suite.write_json(output / 'manifest.json', {'case_id': case_id, 'images': images,
        'task_files': task_files(task),
        'case_sha256': suite.digest((output/"case.json").read_bytes()),
        'developer_instruction_sha256': hashlib.sha256(instruction.encode()).hexdigest(),
        'grading_scope': 'input fidelity only; review response quality separately',
        'recipe_runner_sha256': hashlib.sha256((recipes / 'tooling/run_docker_case.py').read_bytes()).hexdigest(),
        'canonical_files': {str(p.relative_to(suite.ROOT)): hashlib.sha256(p.read_bytes()).hexdigest()
                            for p in [suite.HERE/'suite.py', suite.HERE/'evaluation.py',
                                      suite.ROOT/'src/templates/invocation.md', *sorted((suite.HERE/'cases').glob('*.yaml'))]}})
    print(json.dumps({'task': str(task), 'case': case_id, 'images': images}))


def collect(prepared, run, output):
    """Admit native evidence; leave substantive answer ratings to the reviewer."""
    output = output.resolve()
    if output.exists() or output.is_relative_to(suite.ROOT):
        raise ValueError('Use a new evidence file outside source Git')
    case = suite.read_json(prepared / 'case.json')
    manifest = suite.read_json(prepared / 'manifest.json')
    if manifest.get("case_sha256") != suite.digest((prepared/"case.json").read_bytes()):
        raise ValueError("Frozen case or grading criteria changed")
    summary = suite.read_json(run / 'summary.json')
    inputs = suite.read_json(run / 'inputs.json')
    actual = task_files(prepared/'task')
    if actual != manifest.get('task_files') or actual != inputs['task_files']:
        raise ValueError('Prepared or executed task differs from the preparation snapshot')
    if inputs["runner_sha256"] != manifest["recipe_runner_sha256"]:
        raise ValueError("Executed runner differs from the prepared recipe")
    if inputs.get("harbor") != "0.25.0" or not inputs.get("resume_trajectory") or inputs.get("agent") != "codex":
        raise ValueError("Run differs from the qualified native continuation profile")
    if inputs.get("auth_route") != "existing native Codex ChatGPT file":
        raise ValueError("Unexpected authentication route")
    if (summary.get('agent_info', {}).get('version') != '0.167.0'
            or summary.get('separate_verifier') is not True
            or any(summary.get('checks', {}).get(f'turn-{i:02d}', {}).get(
                'no_agent_credentials_in_verifier') is not True
                   for i in range(1, len(case['turns'])+1))):
        raise ValueError('Guest version or separate-verifier credential checks differ')
    if (summary['disposition'] != 'passed' or not summary['workflow_complete']
            or not summary['collection_ok'] or not summary['cleanup_passed']):
        raise ValueError('Native input fidelity, collection or lifecycle did not pass')
    if inputs['model'] != 'openai/gpt-6.1-sol' or inputs['effort'] != 'high':
        raise ValueError('Run differs from the qualified Sol / High profile')
    trials = list((run/'jobs').glob('*/*/result.json'))
    if len(trials) != 1: raise ValueError('Expected one complete native trial')
    trial = trials[0].parent
    instruction = (prepared/'developer-instructions.md').read_bytes().decode("utf-8")
    if manifest["developer_instruction_sha256"] != suite.digest(instruction.encode()):
        raise ValueError("Frozen developer instruction changed")
    if inputs.get('developer_instructions', {}).get('sha256') != suite.digest(instruction.encode()):
        raise ValueError('Developer instruction provenance differs')
    answers, sessions = [], []
    for index, turn in enumerate(case['turns'], 1):
        agent = trial/'steps'/f'turn-{index:02d}'/'agent'
        answer = extract_response(suite.read_json(agent/'trajectory.json'), {
            'case_id': case['id'], 'turn': index,
            'prompts': [t['prompt'].strip() for t in case['turns'][:index]]})
        if answer['history_answers'] != [prior['answer'] for prior in answers]:
            raise ValueError('Recorded resumed answers differ from earlier turns')
        answers.append(answer)
        events = [json.loads(line) for line in (agent/'codex.txt').read_text().splitlines()
                  if line.startswith('{')]
        ids = [e.get('thread_id') for e in events if e.get('type') == 'thread.started']
        if len(ids) != 1 or not ids[0]: raise ValueError('Expected one native session per step')
        sessions.append(ids[0])
        native = list((agent/'sessions').rglob('*.jsonl'))
        if len(native) != 1: raise ValueError('Expected one retained native history')
        rows = [json.loads(line) for line in native[0].read_text().splitlines()]
        developer = [''.join(c.get('text','') for c in row['payload'].get('content',[]) if isinstance(c,dict))
            for row in rows if row.get('type')=='response_item' and row.get('payload',{}).get('role')=='developer']
        if not any(instruction in text for text in developer):
            raise ValueError('Complete expert instruction missing from native developer messages')
    if len(set(sessions)) != 1: raise ValueError('Conversation did not continue the same native session')
    suite.write_json(output, {'case': case, 'answers': answers, 'sessions': sessions,
        'quality_review': 'pending against the canonical turn requirements and critical failures',
        'input_fidelity': 'passed', 'cleanup_passed': True, 'usage': summary['usage'],
        'usage_basis': summary['usage_basis'],
        'collector_sha256': suite.digest(Path(__file__).read_bytes()),
        'evaluation_sha256': suite.digest((suite.HERE/'evaluation.py').read_bytes())})
    print(json.dumps({'case': case['id'], 'turns': len(answers), 'input_fidelity': 'passed',
                      'quality_review': 'pending', 'output': str(output)}))


def review(packet_path, grade_path, output):
    """Validate a human quality review without turning input fidelity into quality."""
    packet = suite.read_json(packet_path)
    supplied = suite.read_json(grade_path)
    turns = packet.get('case', {}).get('turns')
    answers = packet.get('answers')
    if (packet.get('input_fidelity') != 'passed' or packet.get('cleanup_passed') is not True
            or not isinstance(turns, list) or not turns
            or not isinstance(answers, list) or len(answers) != len(turns)
            or any(not isinstance(a, dict) or a.get('case_id') != packet['case']['id']
                   or type(a.get('turn')) is not int or a['turn'] != i
                   or not isinstance(a.get('answer'), str) or not a['answer'].strip()
                   for i, a in enumerate(answers, 1))):
        raise ValueError('Quality review requires a complete, valid collected conversation')
    if supplied.get("packet_sha256") != suite.digest(packet_path.read_bytes()):
        raise ValueError("Review must identify the exact collected packet")
    grading_packet = {"sample_id": packet["case"]["id"], "turns": packet["answers"]}
    grade = validate_grade(supplied["grade"], grading_packet)
    if output.exists() or output.resolve().is_relative_to(suite.ROOT):
        raise ValueError("Use a new report outside source Git")
    passed = all(not any(t[k] for k in ("wrong_acceptance", "wrong_refusal", "critical_error"))
                 and t["quality"] == 2 and t["continuity"] in (None, 2) for t in grade["turns"])
    suite.write_json(output, {"case_id": packet["case"]["id"], "input_fidelity": packet["input_fidelity"],
        "quality_disposition": "pass" if passed else "fail", "grade": grade,
        "packet_sha256": supplied["packet_sha256"], "usage": packet["usage"],
        "usage_basis": packet["usage_basis"], "reviewer": "direct human/agent review; no model judge invoked"})


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    commands = parser.add_subparsers(dest='command', required=True)
    prep = commands.add_parser('prepare')
    prep.add_argument('--case', required=True)
    prep.add_argument('--output', required=True, type=Path)
    prep.add_argument('--recipes', required=True, type=Path)
    prep.add_argument('--cases-directory', type=Path, help="Private canonical YAML groups, same validated case schema")
    prep.add_argument('--instruction-file', type=Path, help="Complete frozen rendered original or repaired developer instruction")
    report = commands.add_parser('collect')
    report.add_argument('--prepared', required=True, type=Path)
    report.add_argument('--run', required=True, type=Path)
    report.add_argument('--output', required=True, type=Path)
    quality = commands.add_parser("review")
    quality.add_argument("--packet", required=True, type=Path)
    quality.add_argument("--grade", required=True, type=Path)
    quality.add_argument("--output", required=True, type=Path)
    commands.add_parser("inventory")
    args = parser.parse_args()
    if args.command == 'prepare':
        prepare(args.case, args.output, args.recipes, cases_directory=args.cases_directory, instruction_file=args.instruction_file)
    elif args.command == 'collect': collect(args.prepared, args.run, args.output)
    elif args.command == 'review': review(args.packet, args.grade, args.output)
    else:
        print(json.dumps([{"id": c["id"], "expert": c["expert"], "turns": len(c["turns"]),
            "file_arrival": any(t.get("files") for t in c["turns"])} for c in suite.load_cases()], indent=2))


if __name__ == "__main__": main()
