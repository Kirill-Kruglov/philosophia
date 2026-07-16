# Opus 4.8 X-line — Level 1 feasibility v2 A6 closure confirmation

**`LEVEL1_FEASIBILITY_V2_A6_XLINE_CONFIRMED`**

Reviewer: Opus 4.8 (X-line, bounded to Sol's A6 parameter-finiteness blocker).
Repository: `/home/master/llm_projects/philosophia`. **The v2 driver was not
invoked; no v2 authorization, claim, report, invalidity record, probe, entropy,
panel, N3, lock, trajectory, or outcome was created. Nothing was committed.**
Closure commit: `f025cf7fe981c8ae41f502d2e7608e6e9273fc25`; original anchor:
`d8c46637adf6f0caab039559c9031b1af65985b4`.

**Diff scope verified.** `git diff d8c46637 f025cf7` touches only review-only
files plus the three load-bearing paths named in the task —
`src/philosophia/level1/train.py`, `src/philosophia/level1/feasibility.py`, and
`tests/test_level1_feasibility_v2.py`. The closure commit is byte-identical to
current HEAD (`cc1b745…`) over the full driver source-pin set and the v2 tests.
No driver, interlock, public_root, schema, path, cap, or v1 file changed.

**Results reproduced.** Focused v2+v1 tests → 25 passed; full suite → 158 passed;
`verify_all.py` VALID; both immutable v1-evidence hashes still match their pinned
values; no `feasibility_v2/` and no `FEASIBILITY_EXECUTION_AUTHORIZATION_V2.json`
exist.

I read Sol's `sol_level1_feasibility_v2_scope_review.md` — its sole **Critical**
finding (A6 parameter non-finiteness not detected at the first non-finite learner
state, letting an optimizer-created Inf/NaN reach panel scoring as *process*
invalidity or miss the mandatory diagnostic at B) and its three mandatory edits.
All three are landed.

---

## Confirmation of the five checks

1. **Loss-finiteness vs parameter-finiteness, scanned after AdamW, before any
   panel eval or next step — CONFIRMED.** `full_history_committee_step`
   (`train.py:74`) now returns `FullHistoryStepResult(losses_finite,
   parameters_finite)`: `losses_finite` is the pre-update CE result from
   `feasibility_committee_step`; `parameters_finite` is a fresh scan
   `all(torch.isfinite(parameter).all() for model in models for parameter in
   model.parameters())` performed **after** that call returns — i.e. after all four
   `optimizer.step()`/`zero_grad()` have run. `finite = losses_finite and
   parameters_finite`. In `run_noncomparative_feasibility_v2`, `if not
   result.finite: break` precedes the `step % CHECKPOINT_CADENCE == 0`
   `_panel_qualifies` block, so an optimizer-created Inf/NaN parameter halts the
   trajectory **before** any dummy-panel evaluation or next oracle step, returning
   the signed scientific non-finite state rather than raising later from panel
   scoring. `test_full_history_step_detects_optimizer_created_nonfinite_parameter`
   poisons `optimizer.step` to fill a parameter with `inf` and asserts
   `losses_finite=True, parameters_finite=False, finite=False, trajectory_steps==1`.

2. **Separate `all_losses_finite` and `all_parameters_finite`; v1 unchanged —
   CONFIRMED.** A new `TrajectoryFeasibilityV2` dataclass (`feasibility.py:76`)
   carries **both** flags; `FeasibilityV2Run.trajectory` points at it; the v2
   runner accumulates each as a scalar running-AND and `report_payload_v2` surfaces
   both via `asdict`. `test_v2_report_surface_is_trajectory_only` asserts both
   fields appear. The original `TrajectoryFeasibility` (one flag), the v1
   `run_noncomparative_feasibility` runner, and the v1 report schema are untouched,
   and both immutable v1-evidence hashes still verify — so v1 evidence semantics
   are unchanged. Reporting two finiteness flags is squarely within A8's permitted
   "finiteness flags" surface (no schema string or interpretation changed).

3. **First bad state stops the trajectory; prior window stands; else censored; no
   series — CONFIRMED.** `if not result.finite: break` stops at the first
   loss-*or*-parameter non-finite state; `censored_at_b = not first_complete_window`
   is unchanged, so a five-checkpoint window completed before the break keeps
   `censored_at_b:false` (the non-finiteness surviving only as the scalar
   diagnostic flags), while no prior window yields the valid A6 censored terminal.
   Only two scalar booleans persist — no per-step non-finiteness series and no
   checkpoint/panel curve (`recent_qualifying` stays in memory, never in the
   payload). `test_post_step_nonfinite_skips_checkpoint_panel_and_censors`
   (bad at step 2, no prior window → `censored_at_b:true`) and
   `test_post_step_nonfinite_at_b_preserves_completed_window` (window over steps
   0–4, bad terminal step 5 → `censored_at_b:false`, window stands) pin both
   directions.

4. **Tests: direct post-AdamW Inf; bad-before-window and bad-after-complete-window;
   no panel call after the bad state; process/resource/hash/seal install no
   report/binary — CONFIRMED.** The direct post-AdamW Inf is created by monkeypatching
   `optimizer.step`. The two wiring tests cover a bad checkpoint before a window and
   the final bounded step after a complete window, and each asserts the **exact**
   panel-call count excluding the bad step (`panel_calls == 2` and `== 5`
   respectively), proving `_panel_qualifies` is never called after the first
   non-finite state. `test_driver_failure_after_claim_leaves_binary_unset_and_no_report`
   (parametrized over a `RuntimeError` process fault and an `ExecutionNotAuthorized`
   resource-wall fault) asserts the durable claim carries
   `censored_at_b_status: unset-until-valid-terminal-report`, has **no**
   `censored_at_b` key, and that **no report** is written; and
   `test_driver_preflight_failure_creates_no_claim_or_report` (a `PermissionError`
   standing in for hash/seal invalidity, raised inside `_preflight` before the
   claim) asserts **neither** claim nor report is created. This matches §7 exactly:
   route 4 leaves the durable claim with the binary unset; route 5 (pre-claim
   hash/seal) produces nothing.

5. **Closes A6 without reopening endpoint/cadence/persistence/learner-policy/
   resource-cap/paths/schemas/interpretation — CONFIRMED.** The delta is exactly a
   post-step parameter scan, a second finiteness flag, and its tests. The schedule,
   world, committee, `CHECKPOINT_CADENCE`, the five-checkpoint persistence rule, the
   full-history learner policy, the `2000/0/129600` caps, the driver paths/schemas,
   and every interpretation string are untouched; `censored_at_b` semantics and the
   pass criterion are unchanged. The report gains one honest, A6-mandated flag and
   nothing else.

**Adversarial re-check.** The exact hole Sol named — a non-finite *parameter*
surviving into a checkpoint `_panel_qualifies`/`PanelObservation` call and
surfacing as *process* invalidity, or being missed at B because no next loss
exposes it — is closed: the parameter scan runs every step immediately after the
AdamW steps, and the finiteness break precedes every panel evaluation, so a
divergent parameter is always classified as the signed A6 scientific
non-finiteness terminal, never a process fault and never silently dropped at B.

---

## Authorization-candidate boundary

With the A6 blocker closed at `f025cf7`, tests green, and the source scope
contained, **Codex may now prepare the v2 authorization candidate for separate
review, but not execute it.** The candidate must bind the **newly reviewed code
HEAD** (`f025cf7…`, the closure commit — not the superseded `d8c46637`) together
with the already-frozen fields the preflight validates: `schema =
philosophia.level1.feasibility-authorization.v2`, `token =
I_AUTHORIZE_LEVEL1_NONCOMPARATIVE_FEASIBILITY_V2` (as the field **Kirill** must
sign, not asserted on his behalf), `scientific_outcome:false`,
`execution_once:true`, `arm:"RANDOM-STATIC"`, `caps={development_worlds:1,
trajectory_steps:2000, scorer_steps:0, wall_seconds:129600}`,
`development_world={pair_slot:0, modulus:66}`, `output_directory =
experiments/level_1_contact/feasibility_v2`, and the frozen
`governing_signature_sha256` / `governing_amendment_sha256` / `v1_evidence_sha256`
maps. Codex must **not** create the authorization with Kirill's token, commit it,
invoke `scripts/level1_run_feasibility_v2.py`, create the claim/report/invalidity
record, draw entropy, build a real panel, or touch any later gate. Execution is a
separate, Kirill-authorized one-shot.

## G-1 / G-2

Not reopened. This A6 closure touches only `train.py`/`feasibility.py` finiteness
logic and their tests; it does not make `allocation.py` reachable on the v2 path
(still never called) nor change the transcript-hash handling, so neither optional
guard becomes load-bearing.

## Negative space (preserved, unweakened)

A resource/process/hash/seal fault sets no `censored_at_b` bit and authorizes no
automatic rerun; a non-finite loss *or* parameter is A6 scientific censoring
(never a process fault), with a pre-divergence completed window still standing; a
valid second censoring → `BLOCKED_LEVEL1_FEASIBILITY` (C1 untested), no third
learner-policy intervention; no v1/v2 contrast may ever be formed; feasibility is
`scientific_outcome:false`, single-arm, one replicate, dummy-panel-only — never a
contrast, N3, lock, escrow, or decision; censored/`UNKNOWN` never success,
equivalence, or a narrated boundary; development artifacts non-citable forever;
Level 1 is a detector, never evidence for `PROOF_CORE`. The immutable v1 evidence
is untouched.

**No v2 execution, authorization, entropy, probe, real panel, N3, lock, escrow,
trajectory, or outcome is authorized by this confirmation.**

— Opus 4.8, X-line. No outcome is asserted or predicted in this document.
