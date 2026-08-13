# PHASE1_MINIMO_REPRO_15

NON-CITABLE Phase-1 reproduction. Not an experiment. No scientific claim.

Instrument construction only: does the Minimo phenomenon run on this hardware, and what does it cost?

Paper reference (figures only, for eye-check of curve shape): [arXiv:2407.00695](https://arxiv.org/abs/2407.00695) — Fig. 2 (proof length), Fig. 4 (extrinsic). Target numbers are those given in the task prompt.

---

## Setup

| item | value |
| --- | --- |
| minimo clone | `C:\Users\LEGION\Kirill\ShareTops\minimo` |
| commit | `6066f482c6752915ad21119f93dc162f4cb9db72` (`6066f48 Fix proof checking scope including later definitions`) |
| Python | 3.12.9 venv at `minimo/.venv` |
| peano module | `maturin develop --release` OK (`import peano` OK) |
| peano binary | `environment/target/release/peano.exe theories/natural_number_game.p t_example1` → `Verifying t_example1... ok` |
| torch | `2.11.0+cu128`; `cuda=True`; GPU = NVIDIA GeForce RTX 4060 Laptop GPU (8188 MiB) |
| command | `python bootstrap.py theory=propositional-logic job.wandb_project=null` |
| Hydra run dir | `minimo/learning/outputs/2026-08-09/23-57-05` |

Config matched paper defaults (from `.hydra/config.yaml`): `iterations=5`, `n_conjectures=200`, `agent=mcts-lm` with `expansions=1000`, `train_policy_on_hindsight_examples=true`, `wandb_project=null`. One seed (default; no seed override). Sequential single process (no Celery/Redis).

### Local modifications (logged; none are algorithm/config/theory edits)

1. **Host toolchain (required to build on Windows):** rustup (Rust 1.97.1) + Visual Studio 2022 Build Tools with VCTools workload (MSVC `link.exe` was missing).
2. **CUDA torch:** `pip install -r requirements.txt` pulled CPU `torch 2.13.0+cpu`; replaced with `torch 2.11.0+cu128` from the PyTorch cu128 index so the 4060 is visible.
3. **Helper only:** `minimo/build_peano_bin.bat` sets `PYO3_PYTHON` / `VIRTUAL_ENV` for `cargo build --bin peano --release` (Windows path quirk). Not used by bootstrap.
4. **No** edits to minimo algorithm, Hydra defaults, or theory files.

---

## Stop condition hit

**Iteration 0 proving exceeded the ~6 h / iteration stop.**

- Outer tqdm at kill: **146 / 200** conjectures, elapsed **7:15:14**, ETA remaining **~4:47**.
- `outcomes_*.json` is written only after all 200 finish → **no full iteration artifact**.
- Process killed per task stop rule. Partial curve recovered from stdout/stderr logs.

---

## 1. COST (the number we actually need)

| metric | value |
| --- | --- |
| Wall (iter 0 partial, to 146/200) | **~7.25 h** (tqdm 7:15:14) |
| Est. full iter 0 at this pace | **~12–15 h** (tqdm projected) |
| Est. 5 iters × prop-logic only | **days** on one 4060 laptop |
| Peak VRAM | **7911 MiB** / 8188 (~97%) |
| Mean VRAM (sampled) | ~7726 MiB |
| Peak system RAM | ~14600 MiB used (~88%) |
| Mean / median GPU util | ~79% / **95%** |
| Process RSS | ~1.0–1.1 GiB |
| Bound | **GPU-bound** (MCTS policy LM on CUDA; VRAM pegged). CPU also active, not idle. |

Raw samples: `successor/dev/phase1_resource_samples.jsonl`.
Run logs: `PHASE1_MINIMO_REPRO_15_run.log` (stdout), `.log.err` (tqdm/stderr, ~3.8 MB), `PHASE1_MINIMO_REPRO_15_progress.log`.

**One-line scale estimate:** prop-logic alone is ~15 h/iteration × 5 ≈ multi-day on this 4060; the other three theories ≫ week on a single laptop — Phase 2 needs distributed workers or a reduced conjecture budget for cost control.

---

## 2. PROVEN FRACTION (iteration 0, partial)

Among **146 completed** proof searches (of 200):

| | |
| --- | --- |
| Found solution | **54** |
| Did not find | **92** |
| Incomplete (killed mid-search) | 1 |
| **Proven fraction** | **54/146 ≈ 37.0%** |

Paper (prompt): initial batches ~**10–20%**. Our iter-0 batch is **higher** than that band (easy `false`-heavy conjectures from a cold LM are a plausible cause). Not comparable to a finished 5-iter curve.

---

## 3. PROOF LENGTH (iteration 0 successes only)

Paper Fig. 2 / prompt (propositional logic across 5 iters): mean **2.75 → 4.21**; longest **5 → 11**.

From reconstructed proofs after `Found solution!` (count of `apply` + `intro` tactics — closest log-native length proxy; **not** the paper’s exact metric, no `outcomes_*.json`):

| | |
| --- | --- |
| n successes | 54 |
| mean tactics | **3.19** |
| max | **8** |
| min | 0 |
| mean `apply` only | 1.31 (max 4) |

Single partial iteration → **no growth-across-iterations measurement**.

---

## 4. EXTRINSIC EVALUATION — SKIPPED

`learning/extrinsic/propositional-logic.p` is present, but `problems.load_problemset()` only registers `lean-library-logic` / `natural-number-game`. `proofsearch.py` `task=eval` → `evaluate_agent` needs a registered problemset. Wiring Kleene’s 35 statements requires **new code** → skipped per task rules (no evaluation harness in Phase 1).

---

## 5. Binary verdict

**PARTIAL**

- Not **REPRODUCED**: zero complete iterations → cannot show proof-length growth across iters, and extrinsic did not run.
- Not **FLAT**: insufficient iterations to claim flatness; iter-0 search is live and solving ~37% of completed conjectures.
- Held: setup works on Windows+4060; GPU training/search path is real; cost is measured.
- Failed / incomplete: full 5-iter curve; extrinsic; paper Fig. 2/4 shape confirmation.

Raw numbers: `successor/dev/PHASE1_MINIMO_REPRO_15_results.json`.

---

## Artifacts

| path | role |
| --- | --- |
| `successor/dev/PHASE1_MINIMO_REPRO_15.md` | this report |
| `successor/dev/PHASE1_MINIMO_REPRO_15_results.json` | per-iteration / partial metrics |
| `successor/dev/PHASE1_MINIMO_REPRO_15_run.log` | bootstrap stdout |
| `successor/dev/PHASE1_MINIMO_REPRO_15_run.log.err` | tqdm / stderr |
| `successor/dev/PHASE1_MINIMO_REPRO_15_progress.log` | wall/VRAM poller |
| `successor/dev/phase1_resource_samples.jsonl` | 20 s VRAM/RAM samples |
| `minimo/learning/outputs/2026-08-09/23-57-05/` | Hydra cwd (`0.pt`, `log.jsonl`) |
