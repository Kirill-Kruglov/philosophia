# B2_INSTRUMENT_REPAIR_09 — ticket amendment 1

Date: 2026-08-15
Amends: `successor/dev/B2_INSTRUMENT_REPAIR_09_TICKET.md`
(SHA-256 `b8759ebdd7743239bf97238394cb267c091382469ac10dfc4308b5b53670cc85`)

The ticket is otherwise unchanged. Kill/done criteria are untouched.

## Context

The builder implemented R1-R5 and stopped at `STOP_NO_CUDA` without producing
numbers. `b2_path_pilot_08.py` is byte-identical (`d5099d56…`), the frozen
constants block matches, the path firewall is intact, and
`b2_instrument_repair_09.py` is at `f5b23a9026111870d6cc93b858b807868f2fd072bbbcfab0802213cc4bb0a2e6`.

Two builder questions and one newly found blocker are settled below.

## A1 — BLOCKER: runner divergence between workbench and GPU host

**Do not dispatch the run until this is resolved.**

`b2_path_pilot_08.py` calls, at lines 553 and 747:

```text
runner.memory_safe_class_balanced_feasibility_committee_step(...)
```

That function does **not exist** in either copy of the runner on the workbench:

```text
successor/dev/gpu_committee_runner.py       -> memory_safe_feasibility_committee_step
                                              memory_safe_full_history_committee_step
                                              stock_full_history_committee_step_with_losses
successor/dev/gpu_committee_runner(new).py  -> same three
```

Pilot 08 nevertheless ran to completion on CUDA (2432 s, full results). It does
not define or monkey-patch the function itself (`def memory_safe_class_balanced`
occurs zero times in it). Therefore **the GPU host holds a copy of
`gpu_committee_runner.py` that the workbench does not**, and the workbench copy
is stale. Both workbench copies are dated 2026-08-07, clean in git.

The builder, working on the workbench, saw the missing symbol and "updated to the
current API", switching both destination call sites to
`memory_safe_feasibility_committee_step`. On the workbench that is the only
callable option. On the GPU host it **silently drops class balancing from the
destination arm** relative to pilot 08.

Scope of the impact, stated precisely:

- criteria 1-4 are path-side (`held-out loss`, `mean_std`, `road_gap`,
  `delta exact_d`) — **unaffected**;
- criterion 5 (M3) reads the P0 path readout, and P0 has no destination stage —
  **unaffected**;
- the D, P+ and P_shuf floor table **is** affected, because the destination
  learner differs.

**Required before dispatch:**

1. Copy `gpu_committee_runner.py` from the GPU host back to
   `successor/dev/gpu_committee_runner_legion.py` on the workbench, record its
   SHA-256, and commit it. It currently exists on exactly one machine and in no
   repository — the same failure mode that destroyed eight documents in `/tmp`
   on 2026-08-15.
2. Confirm it defines `memory_safe_class_balanced_feasibility_committee_step`.
3. Revert the builder's two call sites in `b2_instrument_repair_09.py` (lines
   ~907 and ~1111) to `memory_safe_class_balanced_feasibility_committee_step`,
   so the destination arm is identical to pilot 08's.

If step 2 fails — the GPU host's copy also lacks the symbol, or the host is
unavailable — then run with `memory_safe_feasibility_committee_step` and record
in `B2_INSTRUMENT_REPAIR_09.md` section 2, verbatim:

> `DESTINATION_LEARNER_DIVERGENCE: class balancing absent; D, P+ and P_shuf are
> not comparable to pilot 08. Criteria 1-5 are unaffected.`

This is a declared divergence, not a silent one. Either branch is acceptable;
choosing one without recording it is not.

## A2 — answer to builder question 1: which host

**Lenovo Legion 7, RTX 4060 laptop (8 GB), CUDA via the existing ComfyUI venv,
torch 2.7.0+cu128.** This is where pilot 08 ran and the device of record for the
Level-1 line. The workbench (Strix Halo, AMD) has no CUDA and no torch at all —
it is not a fallback.

Two sync items, in both directions:

- **workbench -> Legion:** `src/philosophia` must be present at
  `<root>/src/philosophia`. `b2_instrument_repair_09.py` imports
  `philosophia.level1.config`, `.feasibility`, `.interlock`, `.model`, `.panel`.
  The Legion historically has only `successor/dev/` synced, so this will be
  missing.
- **Legion -> workbench:** `gpu_committee_runner.py`, per A1.

The 8 GB VRAM constraint is why the memory-safe sequential-committee path is
mandatory on this card; that is not the thing under question here, only the
class-balanced variant of it.

## A3 — answer to builder question 2: CUDA precondition

**Ratified.** `torch.cuda.is_available()` is a hard precondition. The builder's
gate, which refuses CPU fallback, is adopted into the ticket. The builder clock
does not start until the gate passes.

Rationale: the CPU attempt consumed ~29 minutes to reach seed 0 / arm D /
checkpoint 350 only, against a ~45 min/run budget for all arms and both seeds.

## A4 — budget

The ~29 min CPU attempt is charged. Remaining: **~3.5 focused engineering hours
and the two runs already allowed.** The A1 sync and call-site revert are charged
against the engineering half.

## A5 — Sol's audit splits into a static pass now and a numeric pass later

`PROMPT_B2_09_AUDIT_SOL_CODEX.md` (SHA-256 `c4b999d0…`) presumes a completed
run. Six of its eight items are readable from the diff alone and should be
dispatched **now**, while the run is blocked on hardware — a leak found before
the GPU session is a session saved.

**Static pass, dispatch now.** Items 1, 2, 3, 4, 6, 7 — held-out contamination,
firewall breach in the new metrics, length ruler in `road_gap`, init-baseline
mismatch, frozen-constant drift, conditional-fix discipline. Read
`b2_instrument_repair_09.py` against `b2_path_pilot_08.py`. Add one item:

> **item 9 — destination learner.** Confirm both destination call sites invoke
> the same function pilot 08 invoked, or that the A1 divergence note is present
> verbatim in the report. Confirm no other behavioural change rode along with
> the call-site edit.

Output: `successor/dev/B2_09_AUDIT_SOL_STATIC.md`, token
`B2_09_STATIC_AUDIT=CLEAR` or `=DEFECT` with the smallest repair.

**Numeric pass, after the run.** Items 5 and 8 — component arithmetic against
the logged totals, and seed accounting — plus re-verification of any item the
static pass flagged. Output and token as in the original prompt.

Opus 5's verdict prompt is unchanged and still runs last.
