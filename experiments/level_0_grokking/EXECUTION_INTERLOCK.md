# Level 0 execution interlock

Status: implemented; the scout executed exactly once; no preregistration lock
or outcome authorization exists.

Every optimizer step requires an `ExecutionInterlock`. Evaluation and persistence
verdicts require capabilities that the unit-check and scout modes do not possess.
The interlock is a contamination boundary, not a substitute for preregistration.

## Modes

| Mode | Step cap | Wall cap | Evaluation | Verdict |
|---|---:|---:|---|---|
| `single-step-check` | 1 per optimizer | none | forbidden | forbidden |
| `bounded-check` | 1..16 | none | forbidden | forbidden |
| `timing-storage-scout` | 100 | 120 seconds | forbidden | forbidden |
| `locked-outcome` | fixed locked budget | locked separately | allowed | allowed |

The bounded-check ceiling of 16 leaves four steps above the 12-step
warmup-sequence test. This fixed headroom supports short numerical checks without
admitting evaluation, verdicts, or a learning curve.

A raw `InterlockedAdamW.step()` without a capability fails closed. Reissuing a
single-step capability cannot advance the same optimizer twice. The scout cap is
checked in code before every step. A step, checkpoint operation, or subprocess
that itself crosses the wall limit
cannot be interrupted. The scout driver checks elapsed time around each step;
inter-phase I/O is checked before the next step.

## Lock envelope

`locked-outcome` can be constructed only from a file named `PREREG.lock`.
The loader requires canonical JSON with this authorization envelope:

- `schema_version=1`;
- `kind=philosophia-level0-preregistration`;
- `status=locked`;
- `authorized_by=Kirill`;
- `before_lock_complete=true`;
- the exact canonical `config_hash`;
- the arm's exact `fixed_steps`.

These fields authorize execution only. The eventual lock must also contain or
hash the complete scientific specification; its verifier is a separate
before-lock deliverable. Merely creating the envelope is forbidden until Kirill
accepts every open scientific cell.

## Scout contamination boundary

The timing/storage scout capability cannot call held-out evaluation or derive a
persistence verdict. The driver was reviewed and executed exactly once. It
persisted no per-step loss series or held-out metric, created no lock or decision
artifact, and tagged its report timing-storage-scout / non-outcome.

## Threat model

This mechanism prevents accidental scientific execution through committed
Philosophia APIs. It is not a security seal against a determined operator, who
could construct a raw PyTorch optimizer or deliberately call an unbound base
method. Repository review, provenance, and Kirill's authorization remain part of
the control boundary.
