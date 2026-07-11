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
| `timing-storage-scout` | 100 | 120 seconds | forbidden | forbidden |
| `locked-outcome` | fixed locked budget | locked separately | allowed | allowed |

A raw `InterlockedAdamW.step()` without a capability fails closed. Reissuing a
single-step capability cannot advance the same optimizer twice. The scout cap is
checked in code before every step. A step that itself crosses the wall limit
cannot be interrupted, so the future scout driver must also check elapsed time
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
persistence verdict. A future scout driver must additionally persist no
per-step loss series and no held-out metric, create no `PREREG.lock` or
`decision.json`, and tag its single report
`timing-storage-scout / non-outcome`.
