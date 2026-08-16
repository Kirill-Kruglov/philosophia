**Part A outcome: `weights_differ_sets_identical`.** Part B is authorized under the ticket; not started.

### What Part A measured
All five checkpoints under `outputs/2026-08-10/00-14-33/{0..4}.pt` have **distinct file SHA-256** and **distinct loaded LM parameter digests** (`unique_param_digests=5`). ck2/ck3 are not frozen copies of ck0 or of each other.

### Load path (code, not filenames)
`task=eval` → `evaluate_agent(cfg)` → `make_agent` → `torch.load(config['agent_path'])`, with that path written into the results JSON. Hydra overrides for 16B/16C/17 name the matching `N.pt`. So ck2/ck3 did not silently run cold.

### Reading
Training moved the parameters; on this 30-theorem set, ck2 and ck3 still solve exactly ck0’s identities (PHASE1_17 §3). That is a transfer fact, not an instrument defect. The `[11, 19, 11, 11, 13]` curve is not voided by Part A.

### Artifacts
- `successor/dev/phase1_18_part_a.py` (132 lines)
- `successor/dev/PHASE1_18_PART_A.md`
- `successor/dev/phase1_18_part_a_results.json`

**STOP.** No Part B run, no seed spend.

---

1. Confirm Part B now? Note: `mcts_expansions` is already in `proofsearch.py` from PHASE1_17 — Part B may be schema-guard + 16C-identical re-run + paired table, without a further minimo diff.
2. For quality: should Part B pin `OMP_NUM_THREADS=1` to reduce the fp/reduction noise that flipped `kleene_12` in 17, or stay at 16 to match 16C exactly?
