# Level 0 execution interlock

Status: implemented before any scout; no preregistration lock or outcome
authorization exists.

Every optimizer step requires an `ExecutionInterlock`. Evaluation and persistence
verdicts require capabilities that the unit-check and scout modes do not possess.
The interlock is a contamination boundary, not a substitute for preregistration.

## Modes

| Mode | Step cap | Wall cap | Evaluation | Verdict |
|---|---:|---:|---|---|
| `single-step-check` | 1 per optimizer | none | forbidden | forbidden |
| `bounded-check` | 1..10 | none | forbidden | forbidden |
| `timing-storage-scout` | 100 | 120 seconds | forbidden | forbidden |
| `locked-outcome` | fixed locked budget | locked separately | allowed | allowed |

A raw `InterlockedAdamW.step()` without a capability fails closed. Reissuing a
single-step capability cannot advance the same optimizer twice. The scout cap is
checked in code before every step. A step that itself crosses the wall limit
cannot be interrupted, so the scout driver also checks elapsed time
around each call and record that limitation.

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
persistence verdict. A scout driver is implemented but unexecuted. Before its one permitted
run, review must confirm that it persists no per-step loss series or held-out metric,
creates no `PREREG.lock` or `decision.json`, and tags its single report
`timing-storage-scout / non-outcome`.

## Threat model

This mechanism prevents accidental scientific execution through committed
Philosophia APIs. It is not a security seal against a determined operator, who
could construct a raw PyTorch optimizer or deliberately call an unbound base
method. Repository review, provenance, and Kirill's authorization remain part of
the control boundary.
