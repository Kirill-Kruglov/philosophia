# Level 0 execution interlock

Status: schema-2 scientific interlock and outcome driver reviewed; the
scientific spec is accepted by Kirill before outcome; canonical `PREREG.lock` is
committed unchanged; outcome execution is now authorized but has not run.

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

`locked-outcome` can be constructed only from a committed, unchanged file named
`PREREG.lock`. Schema 2 binds Kirill's exact authorization statement to the
accepted scientific-spec hash, the reviewed source commit and per-file hashes,
all nine named runs, their config/split/control/budget fields, the canonical
16/32 PyTorch thread contract, their wall and artifact ceilings, and the
battery-wide artifact ceiling.

Outcome checkpoints use schema 5 and bind model, optimizer/scheduler, source
prefixes, and both PyTorch thread counts. The source commit may be an ancestor of the execution commit because creation
and commitment of `PREREG.lock` necessarily follow the reviewed source commit.
Every locked source file must retain its recorded hash. The training driver
records metrics but contains no persistence/verdict call; the separate evaluator
cannot optimize or instantiate a model and runs only after all nine completion
reports exist.

`SCIENTIFIC_SPEC.json` records Kirill's pre-outcome acceptance after the
external review findings were closed. Lock commit `e4a0fee` now binds the
accepted spec and reviewed source hashes. Runtime still fails closed on any
source, spec, lock, run identity, environment, or artifact drift.

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
