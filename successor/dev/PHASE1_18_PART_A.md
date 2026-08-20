# PHASE1_18 Part A - checkpoint identity

Status: `INSTRUMENT_INTEGRITY__NO_SEED_SPEND_AUTHORIZED`

Outcome: **weights_differ_sets_identical**

Part B authorized: `True`

## Load path (code-traced)

- `main task==eval -> evaluate_agent(cfg)`
- `evaluate_agent -> make_agent(config)`
- `make_agent -> torch.load(config['agent_path'])`
- `results JSON records config agent_path`

source_checks: `{"task_eval_calls_evaluate_agent": true, "evaluate_agent_calls_make_agent": true, "make_agent_torch_loads_agent_path": true, "results_record_agent_path": true}`

## Per-checkpoint digests

| ck | nbytes | file SHA-256 | param digest (loaded LM) | n_solved (PHASE1_17) |
|---|---:|---|---|---:|
| ck0 | 1946691 | `c0776153f60408b57465af89b599273c38f085441be092a8848a05bde8beac73` | `8dbeb0f175ccf4c8ca673d0fdadfaeb6bb892773bf8999feedb66b434e700d5c` | 11 |
| ck1 | 5794267 | `1a6b2fbe77da802b5144fbbb7e688f1011501785aa1b99919a646a3fba382f49` | `de92df13b97c3f9f9d210c44a5731a69ae1bfccaaebbdeaeb9364b2fea270e16` | 19 |
| ck2 | 5794267 | `eedfe1b9b6d8312a93bd02fb65d9e3ef46e8b74284e3a6723dfd345f76d0fab4` | `1fb94e440a54a6201be3be3ea34fc4bd631616c669753eb2560d144205d9d067` | 11 |
| ck3 | 5794267 | `7044ef7f893e52e87eefa5f1b21796c28e83d53d109eb217f453f5fdfe92bbc6` | `00cac37feabfd8c07ba6b3aaea20268a60f9914cfa9d86fd8be3ec27e5b6637f` | 11 |
| ck4 | 5794267 | `10014b04735cbc4a25a00715a816e781ad4044e490a7f44e797af06cb2353fff` | `d25293108d6f373aa0b0992f34e6acf4a5036630e1fdd624ab08e58574f0f294` | 13 |

## Pairwise

| a | b | file_equal | param_digest_equal | solved_set_equal |
|---|---|---|---|---|
| ck0 | ck1 | False | False | False |
| ck0 | ck2 | False | False | True |
| ck0 | ck3 | False | False | True |
| ck0 | ck4 | False | False | False |
| ck1 | ck2 | False | False | False |
| ck1 | ck3 | False | False | False |
| ck1 | ck4 | False | False | False |
| ck2 | ck3 | False | False | True |
| ck2 | ck4 | False | False | False |
| ck3 | ck4 | False | False | False |

## Reading

All five file hashes differ; all five loaded-parameter digests differ (unique_param_digests=5). Eval task=eval loads config.agent_path via make_agent/torch.load and records that path in the results JSON. Hydra overrides for 16B/16C/17 name the matching N.pt. So ck2/ck3 did not silently run cold: they are distinct trained states whose external solved sets (PHASE1_17) coincide with ck0.

## Hashes

- script raw `57acd4a60c47978859a50e288afa636e02729a6e36484066c7daefd8520413df` lf `57acd4a60c47978859a50e288afa636e02729a6e36484066c7daefd8520413df`
- proofsearch raw `128e13d14d74db40e857f785cb066444a69e718943d3626b42c580dc9a2fd62e` lf `128e13d14d74db40e857f785cb066444a69e718943d3626b42c580dc9a2fd62e`

- `/home/master/llm_projects/minimo/learning/outputs/2026-08-10/00-14-33/0.pt` raw `c0776153f60408b57465af89b599273c38f085441be092a8848a05bde8beac73` lf `07dbbe8838e78982542be8399ff9448e675bfc0fed1c89bead4769cd72079c6b`
- `/home/master/llm_projects/minimo/learning/outputs/2026-08-10/00-14-33/1.pt` raw `1a6b2fbe77da802b5144fbbb7e688f1011501785aa1b99919a646a3fba382f49` lf `4b9b5418fba0183bdbde44d07760c5a1562664e001657ef3416acec8ea62233e`
- `/home/master/llm_projects/minimo/learning/outputs/2026-08-10/00-14-33/2.pt` raw `eedfe1b9b6d8312a93bd02fb65d9e3ef46e8b74284e3a6723dfd345f76d0fab4` lf `64191f0599424dcc9cb64e6805ad47c71ec9fa2338daa983de7af07f710a6e28`
- `/home/master/llm_projects/minimo/learning/outputs/2026-08-10/00-14-33/3.pt` raw `7044ef7f893e52e87eefa5f1b21796c28e83d53d109eb217f453f5fdfe92bbc6` lf `b8d53c2342c6a33c312186d6667f0a3e87f805d9e849cb143faaf7b45391301e`
- `/home/master/llm_projects/minimo/learning/outputs/2026-08-10/00-14-33/4.pt` raw `10014b04735cbc4a25a00715a816e781ad4044e490a7f44e797af06cb2353fff` lf `33785c30f5e644af1b1e67586b53bcb8a7a1d1fdb06f53ac03012181dae98d26`

STOP after Part A. No Part B in this run.
