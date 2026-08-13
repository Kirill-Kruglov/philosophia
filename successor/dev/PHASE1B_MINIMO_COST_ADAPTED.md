# PHASE1B_MINIMO_COST_ADAPTED

NON-CITABLE Phase-1b. Not an experiment. No scientific claim.

Continuation after PHASE1_MINIMO_REPRO_15 (`PARTIAL`, stopped at ~6 h/iter on paper-scale `n_conjectures=200`).

## Why not resume the Hydra dir

`bootstrap.py continue=` only reloads the latest `i.pt` and restarts that **whole** iteration. With only `0.pt` and no `outcomes_0.json`, mid-batch progress (146/200) cannot be resumed. Paper-scale restart ≈ 12–15 h/iter × 5 on this 4060.

## Cost budget table (4060 laptop, measured from Phase 1)

Empirical rate from Phase 1 iter 0: **146 conjectures in 7.25 h** ≈ **3.0 min mean**; late tqdm **~5–7 min**/conjecture. Use **5 min** as planning rate (conservative). Training between iters is extra (minutes–tens of minutes), not dominant vs MCTS.

| profile | n_conjectures | iters | searches | wall @ 5 min/search | fits 24 h wall? | notes |
| --- | ---: | ---: | ---: | --- | --- | --- |
| Paper-faithful (Phase 1) | 200 | 5 | 1000 | ~83 h | **No** | hit 6 h/iter stop at 146/200 |
| Cost-adapted A (this run) | **40** | 5 | 200 | ~17 h | **Likely** | same agent/expansions/hindsight |
| Cost-adapted B (tight) | 20 | 5 | 100 | ~8 h | Yes | thinner proven-fraction estimate |
| One full paper iter only | 200 | 1 | 200 | ~12–15 h | borderline | no cross-iter growth test |
| All 4 theories @ paper | 200 | 5×4 | 4000 | ≫ week | No | needs distributed Celery/Redis |

**Scale line:** one 4060 cannot finish paper-scale Minimo in Phase 1 wall limits; Phase 2 must budget workers or reduce `n_conjectures`.

## Phase 1b run (authorized continuation)

- Same: `theory=propositional-logic`, `iterations=5`, `agent=mcts-lm` (`expansions=1000`), hindsight ON, `job.wandb_project=null`, one seed.
- **Only cost dial changed:** `n_conjectures=40` (not a hyperparameter search — single pre-chosen budget from the table).
- Stop: total wall **~24 h**, or FLAT after 5 iters.
- Success criterion (same binary): proof length grows across iters; extrinsic skipped unless already wired (still not).

### Live run

| | |
| --- | --- |
| Hydra dir | `minimo/learning/outputs/2026-08-10/07-27-05` |
| Started | 2026-08-10 07:27 local |
| Worker PID | 2916 (stub 34148) |
| Logs | `successor/dev/PHASE1B_MINIMO_run.log` (+ `.err`), `PHASE1B_MINIMO_progress.log`, `phase1b_resource_samples.jsonl` |

Status: **running** (iter 0 conjecturing at launch). Metrics will be written to `PHASE1_MINIMO_REPRO_15_results.json` under key `phase1b` when finished.
