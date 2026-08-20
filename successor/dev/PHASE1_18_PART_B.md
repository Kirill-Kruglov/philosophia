# PHASE1_18 Part B (amendment 5)

Status: `PART_B_AUTHORIZED_AS_AMENDED__NO_SEED_SPEND`

Full five-checkpoint OMP=16 arm: **CUT**.

OMP=1 role: `intended_instrument_pending_no_contradiction`

Standing rules: `/home/master/llm_projects/philosophia/successor/dev/STANDING_RULES.md`

Structural gate: passed. Pin equality vs PHASE1_17 is reported, not gated.

## 0. OMP=1 vs PHASE1_17 pins (configuration sensitivity; not a gate)

- ck0 identical=True symdiff=(empty)
- ck1 identical=True symdiff=(empty)
- ck2 identical=True symdiff=(empty)
- ck3 identical=True symdiff=(empty)
- ck4 identical=True symdiff=(empty)

## 1. ck0 across binary change (pre-patch vs canonical post-patch)

- pre_patch_sha: `66ffb139374696cc51b55fe1e5b88c6bf2243b0911b32b83cc084b178de2bf4e` [INFERRED]
- post_patch_sha: `4826c2946817b9e9e8094bc143ec2a54f1c2dc7916d82b0160938a2473a27a72` [MEASURED_IN_PROCESS]
- identical_sets: `True`
- symmetric_difference: (empty)
- on_disagree: record and continue; ck1 same-binary repeat resolves causes

## 2. Homogeneous identity (ck2/ck3 vs canonical ck0)

- ck2_equals_ck0: `True`
- ck3_equals_ck0: `True`
- pre_patch_identity_not_established_if_ck0_binary_sensitive: `False`

## 3. Determinism control (OMP=1 ck1 repeat)

- expected: identical
- identical_sets: `True`
- symmetric_difference: (empty)
- on_mismatch: record and continue to noise floor

## 4. Noise floor (size against the union)

Never size the multi-seed run against the fresh floor alone.

### Fresh floor (lower bound)

- bound on: lower_bound_most_favourable_back_to_back_same_host_state_same_seed_same_binary
- union flip: kleene_12
- host_otherwise_idle_all_repeats: `False` [DERIVED]
- note: At least one fresh repeat saw other Phase-1/2 jobs in the series; do not average that away. Fresh floor remains a lower bound.
- omp16_rep1 vs omp16_rep2: (empty)
- omp16_rep1 vs omp16_rep3: kleene_12
- omp16_rep2 vs omp16_rep3: kleene_12
- omp16_rep1 wall_s=3737 idle=False n_periodic=63 max_load1=12.28125
- omp16_rep2 wall_s=3719 idle=False n_periodic=62 max_load1=11.75634765625
- omp16_rep3 wall_s=3725 idle=False n_periodic=63 max_load1=12.51123046875

### Historical pair 16C vs 17 (realistic)

- bound on: realistic_days_apart_host_state_and_binary_differ_inferred_thread_config
- omp classes: `INFERRED` / `INFERRED`
- symmetric_difference: kleene_12
- kleene_12 in scope / in difference: `True` / `True`

### Total union (use for multi-seed sizing)

- bound on: union_of_fresh_lower_bound_and_historical_realistic_pair
- union: kleene_12

## 5. Configuration sensitivity

### ck0 [omp_class=MEASURED_IN_PROCESS sha=4826c2946817b9e9]
- vs 17 [omp MEASURED_IN_PROCESS/INFERRED]: (empty)
### ck1 [omp_class=MEASURED_IN_PROCESS sha=4826c2946817b9e9]
- vs 16c [omp MEASURED_IN_PROCESS/INFERRED]: (empty)
- vs 17 [omp MEASURED_IN_PROCESS/INFERRED]: kleene_12
- vs omp16_rep1 [omp MEASURED_IN_PROCESS/MEASURED_IN_PROCESS]: kleene_12
- vs omp16_rep2 [omp MEASURED_IN_PROCESS/MEASURED_IN_PROCESS]: kleene_12
- vs omp16_rep3 [omp MEASURED_IN_PROCESS/MEASURED_IN_PROCESS]: (empty)
### ck2 [omp_class=MEASURED_IN_PROCESS sha=4826c2946817b9e9]
- vs 16c [omp MEASURED_IN_PROCESS/INFERRED]: (empty)
- vs 17 [omp MEASURED_IN_PROCESS/INFERRED]: (empty)
### ck3 [omp_class=MEASURED_IN_PROCESS sha=4826c2946817b9e9]
- vs 16c [omp MEASURED_IN_PROCESS/INFERRED]: (empty)
- vs 17 [omp MEASURED_IN_PROCESS/INFERRED]: (empty)
### ck4 [omp_class=MEASURED_IN_PROCESS sha=4826c2946817b9e9]
- vs 17 [omp MEASURED_IN_PROCESS/INFERRED]: (empty)

## 6. Paired cost (OMP=1 five-ck, canonical homogeneous arm)

| a | b | n | cheaper/costlier/identical | median ratio | IQR |
|---|---|---:|---|---:|---|
| ck0 | ck1 | 11 | 10/1/0 | 0.6399572649572649 | [0.3867053998632946, 0.7429453262786596] |
| ck0 | ck2 | 11 | 8/3/0 | 0.7142857142857143 | [0.2980839194761096, 0.9750192901234567] |
| ck0 | ck3 | 11 | 8/3/0 | 0.7142857142857143 | [0.28195488721804507, 1.0155893264840183] |
| ck0 | ck4 | 10 | 6/4/0 | 0.7167919799498748 | [0.36088709677419356, 1.7786094622905029] |
| ck1 | ck0 | 11 | 1/10/0 | 1.5626043405676127 | [1.3479999999999999, 2.753669480568864] |
| ck1 | ck2 | 11 | 4/6/1 | 1.0065359477124183 | [0.7506053268765133, 1.3679999999999999] |
| ck1 | ck3 | 11 | 5/5/1 | 1.0 | [0.6912832929782082, 1.2475555555555555] |
| ck1 | ck4 | 13 | 6/6/1 | 1.0 | [0.6860706860706861, 1.7973856209150327] |
| ck2 | ck0 | 11 | 3/8/0 | 1.4 | [1.0377074422583403, 4.042763157894736] |
| ck2 | ck1 | 11 | 6/4/1 | 0.9935064935064936 | [0.7313943541488452, 1.3596491228070176] |
| ck2 | ck3 | 11 | 5/4/2 | 1.0 | [0.8026315789473684, 1.0240990411814408] |
| ck2 | ck4 | 10 | 0/8/2 | 1.6989942528735633 | [1.3995999412757838, 2.049721984602224] |
| ck3 | ck0 | 11 | 3/8/0 | 1.4 | [0.9973375372219302, 4.6875] |
| ck3 | ck1 | 11 | 5/5/1 | 1.0 | [0.8112716763005781, 1.53494623655914] |
| ck3 | ck2 | 11 | 4/5/2 | 1.0 | [0.9765983534769662, 1.2462365591397848] |
| ck3 | ck4 | 10 | 0/9/1 | 1.8649425287356323 | [1.727486559139785, 2.2251982793386205] |
| ck4 | ck0 | 10 | 4/6/0 | 1.395121951219512 | [0.5660886172650879, 3.3096861128725426] |
| ck4 | ck1 | 13 | 6/6/1 | 1.0 | [0.5563636363636364, 1.4575757575757575] |
| ck4 | ck2 | 10 | 8/0/2 | 0.5886012941762071 | [0.49084033613445377, 0.71486856516977] |
| ck4 | ck3 | 10 | 9/0/1 | 0.5363636363636364 | [0.45023009203681474, 0.5790846312077578] |

## Hashes

- `/home/master/llm_projects/philosophia/successor/dev/phase1_18_part_b_analyze.py` raw `4a9b2880319d9fe6a3dc6936a51fdf99c0c8945a8957632396f82d1741e42fdc` lf `4a9b2880319d9fe6a3dc6936a51fdf99c0c8945a8957632396f82d1741e42fdc`
- `/home/master/llm_projects/philosophia/successor/dev/run_phase1_18_part_b_am2.sh` raw `d65767282ad73f827a797d3937073ac8117a165645e989e54e0b271bfaa3eee0` lf `d65767282ad73f827a797d3937073ac8117a165645e989e54e0b271bfaa3eee0`
- `/home/master/llm_projects/philosophia/successor/dev/phase1_18_stamp_threads.py` raw `142e5a5c89281051bf4a516d8f635aa47b55482af84b9a1576a763105532fe7c` lf `142e5a5c89281051bf4a516d8f635aa47b55482af84b9a1576a763105532fe7c`
- `/home/master/llm_projects/philosophia/successor/dev/phase1_18_host_monitor.py` raw `54d3f404f724430d07eb8bbd3b86afc0961c5a1777fe5be3b45226811e8e6a1e` lf `54d3f404f724430d07eb8bbd3b86afc0961c5a1777fe5be3b45226811e8e6a1e`
- `/home/master/llm_projects/philosophia/successor/dev/STANDING_RULES.md` raw `2a2938c45c6e761c0948ad901ab362bd8b22bf8970d8279b7f0673386b429408` lf `2a2938c45c6e761c0948ad901ab362bd8b22bf8970d8279b7f0673386b429408`
- `/home/master/llm_projects/philosophia/successor/dev/phase1_18_part_b/checkpoint_0_omp1.json` raw `d48a4f0a2c5a3c6c1aeb271fcc887bfd2e7646d9566045d21f59c0271d0fb3a5` lf `d48a4f0a2c5a3c6c1aeb271fcc887bfd2e7646d9566045d21f59c0271d0fb3a5`
- `/home/master/llm_projects/philosophia/successor/dev/phase1_18_part_b/checkpoint_1_omp1.json` raw `fadf9e848cae530084d8b622444a552bfa83202b1dedb37e5baf18d16d9af99c` lf `fadf9e848cae530084d8b622444a552bfa83202b1dedb37e5baf18d16d9af99c`
- `/home/master/llm_projects/philosophia/successor/dev/phase1_18_part_b/checkpoint_2_omp1.json` raw `231479a39002d8008bd8861a599fad449b0661812820c9acc16308184cd9499d` lf `231479a39002d8008bd8861a599fad449b0661812820c9acc16308184cd9499d`
- `/home/master/llm_projects/philosophia/successor/dev/phase1_18_part_b/checkpoint_3_omp1.json` raw `b0c2dc349b220c905dbcbb3ad30766c70d1e77d18739772352174162a3e63970` lf `b0c2dc349b220c905dbcbb3ad30766c70d1e77d18739772352174162a3e63970`
- `/home/master/llm_projects/philosophia/successor/dev/phase1_18_part_b/checkpoint_4_omp1.json` raw `aa3b6aa75d6b6ebc2904d5a4065f2f1a52eae26b84e8792598fb3476f019126f` lf `aa3b6aa75d6b6ebc2904d5a4065f2f1a52eae26b84e8792598fb3476f019126f`
- `/home/master/llm_projects/philosophia/successor/dev/phase1_18_part_b/checkpoint_0_omp1_PRE_PATCH.json` raw `7f75768d196b26ee3fdaa97f3d128a6f41b964d316357d72c7177091ab9ace6f` lf `7f75768d196b26ee3fdaa97f3d128a6f41b964d316357d72c7177091ab9ace6f`
- `/home/master/llm_projects/philosophia/successor/dev/phase1_18_part_b/checkpoint_1_omp1_rep1.json` raw `221a164b3681e86748907ede0ae11267ee6e1d0fc84d54014b57d78dca6a4316` lf `221a164b3681e86748907ede0ae11267ee6e1d0fc84d54014b57d78dca6a4316`
- `/home/master/llm_projects/philosophia/successor/dev/phase1_18_part_b/checkpoint_1_omp16_rep1.json` raw `0ead73350636b2e6ef92594425ff0cd1e5c17f0690319234cc5aef45898429aa` lf `0ead73350636b2e6ef92594425ff0cd1e5c17f0690319234cc5aef45898429aa`
- `/home/master/llm_projects/philosophia/successor/dev/phase1_18_part_b/checkpoint_1_omp16_rep2.json` raw `1226719fe23d9888e32c97d574525668e52a1eb847ab4892d7ebe7cf825e4d23` lf `1226719fe23d9888e32c97d574525668e52a1eb847ab4892d7ebe7cf825e4d23`
- `/home/master/llm_projects/philosophia/successor/dev/phase1_18_part_b/checkpoint_1_omp16_rep3.json` raw `51801e7fb8e42b2e70658c8af7cea70985db0329fa35b58769c4cfd8a906d3a4` lf `51801e7fb8e42b2e70658c8af7cea70985db0329fa35b58769c4cfd8a906d3a4`

No verdict token. Multi-seed unauthorized until noise floor exists.
Last amendment before this report.
