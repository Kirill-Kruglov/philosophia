# Opus 4.8 X-line — Level 1 feasibility hardening confirmation

Reviewer: Opus 4.8 (X-line, bounded to the FS-1..FS-6 closures). Repository:
`/home/master/llm_projects/philosophia` (not committed; **feasibility driver not
invoked**; no feasibility authorization/claim/report created). Anchor:
`308aa6f`; hardening commit under review: `be53fdd`. I ran the unit/full suites
and verifiers and inspected the exact `be53fdd` diff.

**Diff scope verified.** `git diff 308aa6f be53fdd` touches only review docs plus
`scripts/level1_run_feasibility.py` (+3), `src/philosophia/level1/feasibility.py`
(+16/-6), `interlock.py` (+4/-4), `pool.py` (+7), and `tests/test_level1_feasibility.py`
(+218). No signed scientific constant, allocation output, model, or gate changed.
The reviewed source paths are byte-identical at HEAD (`git diff --quiet be53fdd HEAD --`
clean over the changed files).

---

## Verdict

**`LEVEL1_FEASIBILITY_HARDENING_CONFIRMED`**

FS-1 through FS-6 are closed, genuinely and test-pinned. `pytest
tests/test_level1_feasibility.py` → 10 passed; full suite → 143 passed; verifier
VALID; no feasibility authorization, claim, report, real panel, N3, lock, escrow,
trajectory, or outcome exists.

---

## Confirmation of the six closures

1. **FS-1a — `feasibility_committee_step` is exercised (Q1).**
   `test_feasibility_committee_step_spends_once_and_updates_shared_batch` builds
   four actual tiny `_RecordingMember` models, passes one `(tokens, labels)`
   minibatch, and asserts: all four `seen == [tokens]` exactly once (one **shared**
   batch), `capability.trajectory_steps == 1` (one spend, not four), all four
   weights changed (updates to every member), and every `parameter.grad is None`
   post-step (gradients zeroed). The non-finite branch (NaN input) returns
   `finite=False`, still spends exactly one step, and leaves **all** member weights
   unchanged (no update). **Confirmed.**

2. **FS-1b — the bounded wiring test exercises the production loop (Q2).**
   `test_bounded_wiring_pins_cadence_persistence_and_nonfinite_break` runs the real
   `run_noncomparative_feasibility` with injected fixtures (cadence patched to 1)
   and pins the exact event trace `panel,(step,panel)×4` — step-0 evaluation, one
   checkpoint per cadence, and **one oracle-step spend per loop**
   (`trajectory_steps == 4`); a five-checkpoint all-qualifying window yields
   `censored_at_b == False`; the checkpoint-size plumbing surfaces (`== 321`); and
   the non-finite variant breaks at step 2 (`trajectory_steps == 2`,
   `all_losses_finite=False`, `censored_at_b=True`).
   `test_bounded_wiring_scorer_mutation_guard_fires` injects diverging state hashes
   and confirms the `"scorer microbenchmark mutated"` guard raises.
   **The 2→5 unit-cap raise cannot authorize production:** `bounded_feasibility_check`
   caps at 5, wall 120 s, purpose `unit-check-not-feasibility-execution`; the
   production path is reachable only through `feasibility_capability()`
   (`trajectory_cap=2000`, `scorer_cap=200`, wall 43200 s), which the driver alone
   constructs, and a ≤5-step bounded capability would raise at step 6 inside the
   2000-element schedule. `bounded_feasibility_check(trajectory_steps=6)` is tested
   to raise "capped at five". **Confirmed.**

3. **FS-2/FS-3 — honest projection boundaries (Q3).** Scorer `started` now precedes
   the shortlist + `realize_pool_index`/`encode_pair`, so scorer latency includes
   realization and encoding; the trajectory `step_latencies.append` now follows the
   checkpoint block, so per-step latency includes scheduled checkpoint evaluation.
   `report_payload` adds a `projection_scope` that states the remaining exclusions
   ("excludes one-time initialization and step-0 evaluation"; "excludes ACTIVE
   training and all other Level 1 arms"), so the report is an explicit per-arm
   resource bound, **not** a full Level 1 runtime forecast; the surface test pins
   both phrases. **Confirmed.**

4. **FS-4 — `public_root.py` pinned (Q4).** It is the thirteenth
   `REVIEWED_SOURCE_PATHS` entry, so the preflight `git diff` byte-identity check now
   covers it, and `test_driver_is_authorization_gated...` asserts the path string is
   present in the driver. **Confirmed.**

5. **FS-5 — `realize_cell` fails closed (Q5).** A `_REALIZATION_ATTEMPT_CAP =
   10_000` counter raises `"raw-pool realization exhaustion is design invalidity"`;
   `test_raw_pool_realization_exhaustion_fails_closed` forces it (patching
   `uniform → 0` so `Cell(0,0,0)` always yields `u==v`). **The cap is acceptable as
   a process/design-invalidity guard:** each attempt is a few cheap PRF draws, four
   distinct pairs are found in a handful of attempts for every real acquisition cell
   (68,848-realization headroom), so 10,000 never triggers in production and only
   fires on a genuinely degenerate cell — a fail-closed ceiling, not a behavioral
   knob. **Confirmed.**

6. **FS-6 — contamination block labelled declarative (Q6).** A source comment now
   marks the `contamination_guards` block as a "Declarative attestation of
   structurally enforced import, capability, report-surface, and later-artifact
   guards checked above," i.e. not runtime-derived evidence; the actual prevention
   remains structural + import/surface/gating tested. **Confirmed.**

---

## Repository-state note (outside this scope, no action taken)

`experiments/level_1_contact/allocation/` now contains a committed, tracked
`PUBLIC_ROOT_TRANSCRIPT.json` (schema `public-root.v1`, `scientific_outcome:false`,
64-char root, `git_head_before_draw = 30091007…`) and its `…DRAW_CLAIM.json`. This
is the **already-completed public-root gate** — a separate one-shot from an earlier
authorization — and is the expected precondition for feasibility. It is orthogonal
to FS-1..FS-6; I did not draw, read the secret of, or modify it. Its presence does
not contradict the "no feasibility authorization/claim/report" evidence, which
concerns the distinct feasibility artifacts (still absent).

---

## May Codex prepare the authorization candidate (not execute)?

**Yes — prepare, do not execute, do not self-authorize.** With the public-root
transcript now committed, Codex may draft the
`FEASIBILITY_EXECUTION_AUTHORIZATION.json` candidate with the frozen structural
fields — `schema = philosophia.level1.feasibility-authorization.v1`,
`scientific_outcome:false`, `execution_once:true`, `arm:"RANDOM-STATIC"`,
`caps = {development_worlds:1, trajectory_steps:2000, scorer_steps:200, wall_seconds:43200}`,
`development_world = {pair_slot:0, modulus:66}`,
`output_directory = experiments/level_1_contact/feasibility`, and
`reviewed_code_head = be53fdd…` — as a reviewable candidate. But the
`token: I_AUTHORIZE_LEVEL1_NONCOMPARATIVE_FEASIBILITY` line and the **commit** of
that file are Kirill's explicit act; Codex must not assert the token on his behalf.
Codex must **not** invoke `scripts/level1_run_feasibility.py`, create the
claim/report, draw entropy, build a real panel, or touch any later gate.

## Negative space (preserved, unweakened)

Adjacent-only detector scope; the operational-modulus certificate and its sole S4
tooth; the public-root / escrow-secret-panel separation and R_h-deferred; the
public-reservation / secret-realization boundary (feasibility uses a dummy panel
only); feasibility is `scientific_outcome:false`, single-arm, one replicate — never
a contrast, N3, lock, escrow, or decision; `UNKNOWN`/censored never success; donor
transcripts encode `n_donor`, never `n_target`; Level 1 never evidence for
`PROOF_CORE`.

**No feasibility execution, authorization, entropy, real panel, N3, lock, escrow,
trajectory, or outcome is authorized by this confirmation.**

— Opus 4.8, X-line. No outcome is asserted or predicted in this document.
