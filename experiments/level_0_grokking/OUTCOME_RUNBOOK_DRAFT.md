# Level 0 outcome runbook draft

Status: **AUTHORIZED BY COMMITTED `PREREG.lock`; NOT YET EXECUTED.** The
scientific spec was accepted by Kirill before outcome, lock commit `e4a0fee`
binds source commit `4dbd3b1`, and repository verifiers pass.

## Preconditions

Run from the repository root on the canonical CPU environment. Do not change
the pinned 16 intra-op / 32 inter-op thread counts, affinity, dtype, backend,
source files, spec, or lock. The driver sets and records both thread counts and
fails closed if the inter-op runtime was already initialized incompatibly. Do
not run
two processes for the same run id. Parallel processes for distinct run ids are
allowed by the preregistration, but their wall clocks include contention.

Before execution:

```bash
.venv/bin/python -m pytest -q
.venv/bin/python scripts/verify_inheritance.py
.venv/bin/python scripts/verify_all.py
```

## Terminal 1: primary Arm A

```bash
for run_id in A-0 A-1 A-2 A-3 A-4; do
  .venv/bin/python scripts/level0_run_outcome.py \
    --run-id "$run_id" \
    --output-root experiments/level_0_grokking/outcomes \
    --spec experiments/level_0_grokking/SCIENTIFIC_SPEC.json \
    --lock experiments/level_0_grokking/PREREG.lock
done
```

## Terminal 2: fidelity Arm B

```bash
for run_id in B-1 B-2 B-3; do
  .venv/bin/python scripts/level0_run_outcome.py \
    --run-id "$run_id" \
    --output-root experiments/level_0_grokking/outcomes \
    --spec experiments/level_0_grokking/SCIENTIFIC_SPEC.json \
    --lock experiments/level_0_grokking/PREREG.lock
done
```

## Terminal 3: random-label control

```bash
.venv/bin/python scripts/level0_run_outcome.py \
  --run-id R-0 \
  --output-root experiments/level_0_grokking/outcomes \
  --spec experiments/level_0_grokking/SCIENTIFIC_SPEC.json \
  --lock experiments/level_0_grokking/PREREG.lock
```

Starting all three groups together is allowed but likely inefficient on 16
physical cores. The default recommendation is two concurrent terminals (A and
B), then R-0 after either group completes. This does not change thresholds or
fixed budgets; it only reduces contention risk against the locked wall clocks.

## Resume after an external interruption

Resume only the interrupted run, without deleting or editing any artifact:

```bash
.venv/bin/python scripts/level0_run_outcome.py \
  --run-id RUN_ID \
  --output-root experiments/level_0_grokking/outcomes \
  --spec experiments/level_0_grokking/SCIENTIFIC_SPEC.json \
  --lock experiments/level_0_grokking/PREREG.lock \
  --resume
```

The driver accepts only a matching immutable manifest and hashed checkpoint
prefix. It can audit and recover one metric line written immediately before an
interrupted checkpoint replacement. On integrity failure, resource stop, or a
second ambiguity, stop and report it; do not delete and rerun.

## Derive and verify the decision

Only after all nine `run_complete.json` files exist:

```bash
.venv/bin/python scripts/level0_evaluate_battery.py \
  --output-root experiments/level_0_grokking/outcomes \
  --spec experiments/level_0_grokking/SCIENTIFIC_SPEC.json \
  --lock experiments/level_0_grokking/PREREG.lock

.venv/bin/python scripts/level0_verify_decision.py \
  --decision experiments/level_0_grokking/outcomes/decision.json \
  --spec experiments/level_0_grokking/SCIENTIFIC_SPEC.json \
  --lock experiments/level_0_grokking/PREREG.lock

.venv/bin/python scripts/verify_all.py
```

Do not inspect partial curves to change execution, thresholds, seed membership,
or the decision rule. Partial metrics are operational artifacts only.
