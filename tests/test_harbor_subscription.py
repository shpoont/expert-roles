"""The subscription migration must retain strict native-message admission."""
from pathlib import Path
import sys
import unittest
import tempfile
import json
from unittest.mock import patch
sys.path.insert(0, str(Path(__file__).parent / 'harbor'))
import subscription
import suite


class RecipeAdapterTests(unittest.TestCase):
    def test_private_case_and_original_instruction_use_same_generator(self):
        import yaml
        with tempfile.TemporaryDirectory() as tmp:
            root=Path(tmp); cases=root/'private';cases.mkdir()
            case=suite.load_cases()[0].copy(); expert=case.pop('expert')
            case['id']='private-reproduction'
            (cases/'incident.yaml').write_text(yaml.safe_dump({'expert':expert,'cases':[case]}))
            recipes=root/'recipes'
            base=recipes/'examples/docker-codex-i01/environment/Dockerfile'
            base.parent.mkdir(parents=True);base.write_text('COPY --chown=node:node project/ /app/project/')
            runner=recipes/'tooling/run_docker_case.py';runner.parent.mkdir();runner.write_text('runner')
            original=root/'original.md';original.write_bytes(b'Original complete instruction\r\n')
            with patch.object(subscription.subprocess,'run') as run:
                run.return_value.stdout='sha256:'+'a'*64
                subscription.prepare(case['id'],root/'prepared',recipes,cases_directory=cases,instruction_file=original)
            self.assertEqual((root/'prepared/developer-instructions.md').read_bytes(),original.read_bytes())
            self.assertEqual(suite.read_json(root/'prepared/case.json'),{**case,'expert':expert})

    def test_collector_rejects_invalid_execution_and_instruction_evidence(self):
        with tempfile.TemporaryDirectory() as tmp:
            root=Path(tmp); prepared=root/'prepared'; run=root/'run'
            (prepared/'task').mkdir(parents=True)
            (prepared/'developer-instructions.md').write_text('complete expert instruction')
            case={'id':'case','expert':'martin-fowler','turns':[
                {'prompt':'First','requirements':['first'],'critical_failures':['bad'],'reference':'Answer'},
                {'prompt':'Next','requirements':['next'],'critical_failures':['bad'],'reference':'Answer'}]}
            suite.write_json(prepared/'case.json',case)
            manifest={'case_sha256':suite.digest((prepared/'case.json').read_bytes()),
                'recipe_runner_sha256':'runner','developer_instruction_sha256':suite.digest(b'complete expert instruction'),
                'task_files':{}}
            suite.write_json(prepared/'manifest.json',manifest)
            summary={'disposition':'passed','workflow_complete':True,'collection_ok':True,'cleanup_passed':True,
                'usage':{},'usage_basis':'unknown','agent_info':{'version':'0.167.0'},'separate_verifier':True,
                'checks':{f'turn-{i:02d}':{'no_agent_credentials_in_verifier':True} for i in (1,2)}}
            inputs={'task_files':{},'runner_sha256':'runner','harbor':'0.25.0','resume_trajectory':True,
                'agent':'codex','auth_route':'existing native Codex ChatGPT file','model':'openai/gpt-6.1-sol',
                'effort':'high','developer_instructions':{'sha256':manifest['developer_instruction_sha256']}}
            suite.write_json(run/'summary.json',summary);suite.write_json(run/'inputs.json',inputs)
            trial=run/'jobs/job/trial';suite.write_json(trial/'result.json',{})
            for index in (1,2):
                agent=trial/'steps'/f'turn-{index:02d}'/'agent'
                steps=[]
                for turn in case['turns'][:index]:
                    steps.extend([{'source':'user','message':turn['prompt']},{'source':'agent','message':'Answer'}])
                suite.write_json(agent/'trajectory.json',{'steps':steps})
                (agent/'codex.txt').write_text(json.dumps({'type':'thread.started','thread_id':'same'})+'\n')
                (agent/'sessions').mkdir()
                (agent/'sessions/session.jsonl').write_text(json.dumps({'type':'response_item','payload':{
                    'role':'developer','content':[{'text':'complete expert instruction'}]}})+'\n')
            subscription.collect(prepared,run,root/'valid.json')
            with self.subTest('task changed before execution'):
                changed=prepared/'task/task.toml';changed.write_text('changed verifier configuration')
                altered={**inputs,'task_files':{'task.toml':suite.digest(changed.read_bytes())}}
                suite.write_json(run/'inputs.json',altered)
                with self.assertRaises(ValueError):subscription.collect(prepared,run,root/'changed-task.json')
            changed.unlink();suite.write_json(run/'inputs.json',inputs)
            trajectory=trial/'steps/turn-02/agent/trajectory.json'
            original=suite.read_json(trajectory)
            altered=suite.read_json(trajectory);altered['steps'][1]['message']='rewritten earlier answer'
            suite.write_json(trajectory,altered)
            with self.subTest('earlier answer changed on resume'):
                with self.assertRaises(ValueError):subscription.collect(prepared,run,root/'changed-history.json')
            suite.write_json(trajectory,original)
            for field,value in [('cleanup_passed',False),('collection_ok',False),('workflow_complete',False),('disposition','error')]:
                altered={**summary,field:value};suite.write_json(run/'summary.json',altered)
                with self.assertRaises(ValueError):subscription.collect(prepared,run,root/'invalid.json')
            suite.write_json(run/'summary.json',summary)
            second=trial/'steps/turn-02/agent'
            (second/'codex.txt').write_text(json.dumps({'type':'thread.started','thread_id':'different'})+'\n')
            with self.assertRaises(ValueError):subscription.collect(prepared,run,root/'invalid.json')
            (second/'codex.txt').write_text(json.dumps({'type':'thread.started','thread_id':'same'})+'\n')
            (second/'sessions/session.jsonl').write_text('{}\n')
            with self.assertRaises(ValueError):subscription.collect(prepared,run,root/'invalid.json')

    def test_all_cases_preserve_turns_files_and_hidden_criteria(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            recipes = root/'recipes'
            base = recipes/'examples/docker-codex-i01/environment/Dockerfile'
            base.parent.mkdir(parents=True)
            base.write_text('FROM qualified\nCOPY --chown=node:node project/ /app/project/\n')
            runner = recipes/'tooling/run_docker_case.py'
            runner.parent.mkdir(); runner.write_text('qualified runner')
            with patch.object(subscription.subprocess, 'run') as run:
                run.return_value.stdout = 'sha256:'+'a'*64
                for case in suite.load_cases():
                    output = root/case['id']
                    subscription.prepare(case['id'], output, recipes)
                    self.assertEqual(suite.read_json(output/'case.json'), case)
                    supplied = {}
                    for i, turn in enumerate(case['turns'], 1):
                        step = output/'task/steps'/f'turn-{i:02d}'
                        self.assertEqual((step/'instruction.md').read_text(), turn['prompt'].strip()+'\n')
                        supplied.update({p.removeprefix('data/'): v for p,v in turn.get('files',{}).items()})
                        self.assertEqual(suite.read_json(step/'tests/expected.json'), {'files': supplied})
                        for p,v in turn.get('files',{}).items():
                            self.assertEqual((step/'workdir'/p).read_text(), v)

    def test_quality_review_is_bound_to_packet_and_actual_answer(self):
        with tempfile.TemporaryDirectory() as tmp:
            root=Path(tmp); packet=root/'packet.json'; grade=root/'grade.json'
            suite.write_json(packet, {'case':{'id':'case','turns':[{'prompt':'Explain'}]},
                'answers':[{'case_id':'case','turn':1,'answer':'A preserves observable behavior.'}],
                'input_fidelity':'passed','cleanup_passed':True, 'usage':{}, 'usage_basis':'unknown'})
            rating={'turn':1,'wrong_acceptance':False,'wrong_refusal':False,'critical_error':False,
                'quality':2,'continuity':None,'reason':'Names preservation of observable behavior.',
                'evidence':['preserves observable behavior']}
            payload={'packet_sha256':suite.digest(packet.read_bytes()), 'grade':{'sample_id':'case','turns':[rating]}}
            suite.write_json(grade,payload)
            subscription.review(packet,grade,root/'report.json')
            self.assertEqual(suite.read_json(root/'report.json')['quality_disposition'],'pass')
            rating['critical_error']=True; suite.write_json(grade,payload)
            subscription.review(packet,grade,root/'failed.json')
            self.assertEqual(suite.read_json(root/'failed.json')['quality_disposition'],'fail')
            rating['evidence']=['invented evidence']; suite.write_json(grade,payload)
            with self.assertRaises(ValueError): subscription.review(packet,grade,root/'invalid.json')
            payload['packet_sha256']='tampered'; suite.write_json(grade,payload)
            with self.assertRaises(ValueError): subscription.review(packet,grade,root/'mismatch.json')

    def test_quality_review_rejects_empty_or_incomplete_packets(self):
        with tempfile.TemporaryDirectory() as tmp:
            root=Path(tmp);packet=root/'packet.json';grade=root/'grade.json'
            for turns in ([],[{'prompt':'Expected answer'}]):
                with self.subTest(turns=turns):
                    suite.write_json(packet,{'case':{'id':'case','turns':turns},'answers':[],
                        'input_fidelity':'passed','cleanup_passed':True,'usage':{},'usage_basis':'unknown'})
                    suite.write_json(grade,{'packet_sha256':suite.digest(packet.read_bytes()),
                        'grade':{'sample_id':'case','turns':[]}})
                    with self.assertRaises(ValueError):subscription.review(packet,grade,root/f'report-{len(turns)}.json')

sys.path.insert(0, str(Path(__file__).parent / 'harbor'))
import evaluation


class SubscriptionHistoryTests(unittest.TestCase):
    def setUp(self):
        self.old = (Path(__file__).parent / 'harbor/baselines/codex-environment.txt').read_text().strip()
        self.current = self.old.replace('<shell>sh</shell>', '<shell>bash</shell>')

    def test_exact_new_context_and_historical_context(self):
        self.assertTrue(evaluation.native_environment(self.old))
        self.assertTrue(evaluation.native_environment(self.current))
        for value in (self.current.replace('bash', 'fish'), self.current.replace('/app', '/home'),
                      self.current+'\nextra', self.current.replace('2026-10-29', '2026-02-31')):
            self.assertFalse(evaluation.native_environment(value))

    def test_actual_task_prompts_remain_exact_and_extra_users_rejected(self):
        expected = {'case_id':'x','turn':1,'prompts':['  preserve\n  indentation']}
        trajectory = {'steps':[{'source':'user','message':self.current},
            {'source':'user','message':expected['prompts'][0]}, {'source':'agent','message':'Answer'}]}
        self.assertEqual(evaluation.extract_response(trajectory, expected)['answer'], 'Answer')
        trajectory['steps'].insert(2, {'source':'user','message':'undeclared'})
        with self.assertRaises(ValueError): evaluation.extract_response(trajectory, expected)


if __name__ == '__main__': unittest.main()
