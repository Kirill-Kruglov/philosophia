# Opus 4.8 X-line review — Level 0 hardening (commit 80241c0 vs 36c97d5)

Reviewer: Opus 4.8 (adversarial X-line). Stage: verification of the mandatory
J1/J2/J3 edits from `reviews/opus_level0_implementation_review.md`. No `PREREG.lock`,
`decision.json`, scout report, or full-run driver exists. I did not run a scientific
trajectory. I ran the full suite (52 pass), both repository verifiers (pass), and
bounded isolated checks: the scout cap (exactly 100 steps, raises on the 101st), the
forward oracle, and the interlock threat-model surface. This review does not predict
grokking, selects no scientific threshold, and treats no unit-test loss as an
observation.

## Verdict

**HARDENING_ACCEPTED**

J1, J2, and J3 are closed. The forward pass is now protected by an independent
loop oracle plus explicit causality/normalization tests; AdamW's exact decay factors
are pinned on all 11 tensors including nonzero biases; checkpoints carry verified
model/optimizer state-integrity hashes and enforce PyTorch 2.9.1 / CPU / float32 under
safe `weights_only=True` loading; and every optimizer step now requires an
`ExecutionInterlock` whose scout mode is capped and cannot evaluate or derive a
verdict. The residual items below are Minor hygiene notes and do not block scout
implementation. Acceptance is contingent only on the two Minor edits being logged, not
on re-review.

---

## 1. Findings

### Critical
None.

### Major
None. All three mandatory closures are present and independently verified (§3).

### Minor

**m1 — The determinism round-trip test spends the scout capability, blurring the
audit trail (Q7).** `tests/test_level0_modules.py:167,207` uses
`ExecutionInterlock.timing_storage_scout()` to take two steps (pre-save and post-load)
because `single_step_check` caps at one step per optimizer. This is *behaviorally*
safe — the capability cannot evaluate or derive a verdict, and only a `tmp_path`
checkpoint is written — but it exercises **scout mode outside the scout**, so "scout
mode was used exactly once, by the real scout" is no longer a clean audit invariant.
Recommend a distinct, clearly-labeled test-only capability
(e.g. `ExecutionInterlock.bounded_check(max_steps=k)` with `allow_evaluation=False,
allow_verdict=False`) reserved for multi-step unit tests, leaving
`timing_storage_scout()` unused until the actual scout. Non-blocking.

**m2 — The interlock is a procedural boundary, not a seal; state the threat model in
code, not only in the doc.** `EXECUTION_INTERLOCK.md` correctly calls the interlock "a
contamination boundary, not a substitute for preregistration," but the code invites
two trivial deliberate bypasses: constructing a plain `torch.optim.AdamW` instead of
`make_optimizer`, or calling the unbound `torch.optim.AdamW.step(instance)` to skip the
override (both confirmed present). This is acceptable under the stated threat model
(preventing *accidental* outcome derivation before a human-signed lock, not defeating a
determined operator), but the module docstring in `interlock.py` should say so
explicitly so no future reader mistakes it for a sandbox. Non-blocking.

**m3 — Provenance metadata fields are recorded but not integrity-checked.**
`checkpoint.py` verifies `config_hash`, `split_hash`, `model_state_hash`,
`optimizer_state_hash`, `torch_version`, `device`, `dtype`, but `repository_head`,
`source_hashes`, `python_version`, and `init_scales` can be edited in a saved payload
without detection. The scout-critical integrity surface is fully covered; this is a
provenance-only nit. Consider hashing the full metadata blob before lock. Non-blocking.

---

## 2. Exact mandatory edits

None are blocking. Recommended (log before the scout; no re-review required):
- Add a distinct test-only bounded capability and switch the round-trip test to it
  (m1), so `timing_storage_scout()` remains unused until the real scout.
- Add a one-paragraph threat-model docstring to `interlock.py` (m2).

## 3. Explicitly accepted J1/J2/J3 closures

**J1 — forward-pass regression protection: ACCEPTED.**
- `tests/test_level0_numerics.py:88` `_oracle_forward` is an *independent* triple-loop
  reimplementation using explicit `@` and `.T` (not the production einsums), compared at
  `rtol=2e-5`. It pins Q/K roles (`W_Q@residual[q]` vs `W_K@residual[k]`), the attention
  contraction (`attended@W_O[head]`), MLP orientation (`W_in.T`/`W_out.T`), and the final
  `@W_U` logits — a shape-preserving transpose in any of these breaks it.
- `test_attention_is_causal_and_normalized:75` asserts query pos 0 has zero weight on
  keys 1–2, query pos 1 zero on key 2, rows sum to 1, and query pos 2 attends all three —
  protecting the causal mask and the softmax axis. (I re-derived these externally; they
  hold.)
- `test_final_readout_depends_on_both_operands:97` guards against a readout that ignores
  an operand. The `attention_weights()` accessor (`model.py:_attention` refactor) exposes
  weights for the test while leaving `forward` numerically unchanged.

**J2 — checkpoint integrity + canonical environment: ACCEPTED.**
- `state_tree_hash` (`checkpoint.py:57`) recurses tensors + param_groups + state;
  `model_state_hash`/`optimizer_state_hash` are stored in metadata and **verified against
  the payload on load** (`checkpoint.py:157-162`). `test_checkpoint_detects_state_and_
  environment_tampering:202` confirms a one-element `W_E` edit and an
  `optimizer.param_groups[0].lr` edit are both caught.
- `_enforce_canonical_environment:122` rejects non-2.9.1 torch, non-CPU device, and
  non-float32 dtype (recorded *and* live), each covered by the parametrized test.
- Loading is now `weights_only=True` (`checkpoint.py:146`); the schema round-trips under
  it (the corruption test loads with `weights_only=True`), so J2's safe-load requirement
  is met without an unusable schema. Key-ordering in `state_tree_hash` is deterministic
  (sorted by `repr`), sufficient for hashing.

**J3 — outcome-gate interlock: ACCEPTED.**
- `InterlockedAdamW.step` (`train.py:20`) fails closed without an interlock, and a
  `single-step-check` optimizer cannot advance twice (`test_...:164,171`). `optimization_
  step`, `evaluate`, and `first_persistent_step` all require capabilities; the public
  verdict function `first_persistent_step` now calls `require_verdict()` and the private
  `_first_persistent_step` is used only in a pure-predicate unit test.
- Scout mode: `max_steps=100`, `max_seconds=120`, `allow_evaluation=False`,
  `allow_verdict=False` (`interlock.py:54`). I verified the cap admits exactly 100 steps
  and raises on the 101st. Evaluation and verdict APIs raise under a non-outcome
  capability.
- Critically, **no committed code can run a trajectory even with a lock**:
  `run_outcome_training` still raises ("no full-run driver exists"), and nothing consumes
  the `locked-outcome` capability. Execution requires *both* a signed `PREREG.lock` *and*
  a not-yet-written, separately reviewable driver.

## 4. Scout implementation eligibility

**Eligible.** The J1/J2/J3 prerequisites are closed, so the bounded timing/storage scout
*driver* may be implemented against `ExecutionInterlock.timing_storage_scout()`. The
driver must: consume only the scout capability; run a single seed (master 0), Arm A;
persist no per-step loss series and no held-out metric; never call `evaluate` or
`first_persistent_step`; create no `PREREG.lock`/`decision.json`; check elapsed wall-time
around each step (the in-step wall crossing is uninterruptible, per the documented
limitation); and emit one report tagged `timing-storage-scout / non-outcome`. Applying
m1 first is advisable so the scout is the sole user of scout mode.

## 5. Scout execution eligibility and remaining guards

**Not yet — implement the driver, then obtain one more bounded sign-off before the single
execution.** The interlock caps the mode, but no committed driver exists to review, and
execution should not be authorized against unreviewed orchestration. Sequence:
1. Implement the scout driver (§4) and its unit tests (dry-run with a stubbed/≤3-step cap
   asserting the contamination guards) — no real multi-step run.
2. A bounded review confirms the driver honors every §4 guard.
3. Then a single scout execution: master 0, Arm A, ≤100 steps or ≤120 s, canonical CPU
   float32, recording only per-step latency, peak memory, one checkpoint byte size, and
   the deterministic prefix-replay hash.

Guards that remain mandatory at execution: single seed; no held-out evaluation; no
persisted loss curve; no lock/decision file; explicit non-outcome tagging; and the run
must not be read as evidence about grokking.

## 6. Lock-stage design in parallel

**Yes.** Lock-stage design continues unblocked and independent of the scout: persistence
window W, Δ_min (with margin absorbing Xavier init-timing shift), quorum k-of-5 and
demonstration-only claim strength, control pass/fail semantics (memorization,
random-label leakage, Arm B's asymmetric interpretation), uniform cadence + storage
projection (informed by the scout), the outcome-independent resource wall, the paper-claim
archive hash, the final null set, and the Arm B seed-count decision. None is resolved by
this hardening; the `PREREG.lock` envelope authorizes *execution only* and, per
`EXECUTION_INTERLOCK.md`, must be accompanied by a separate before-lock scientific-spec
verifier — creating the envelope remains forbidden until Kirill accepts every open cell.

---

### Question index

1. Oracle + attention tests protect masking, softmax axis, Q/K roles, contraction, MLP
   orientation, and final logits — yes (§3 J1).
2. Zero-gradient tests pin 0.999/0.9999 on all 11 tensors incl. nonzero biases, one
   group, no scheduler — yes (§3 J1/J2 boundary; `test_...:112`).
3. Model/optimizer state hashes are deterministic and catch tensor and param-group
   corruption — yes (§3 J2).
4. `weights_only=True` + 2.9.1/CPU/float32 enforcement closes J2 without an unusable
   schema — yes (§3 J2).
5. `InterlockedAdamW` blocks raw and repeated non-scout steps; scout ≤100 steps/120 s and
   cannot evaluate or derive a verdict — yes, with the m2 threat-model caveat (§3 J3).
6. The `PREREG.lock` envelope is an execution-only interlock that resolves no scientific
   cell — yes (§3 J3, §6).
7. The round-trip test's use of scout mode is behaviorally valid but audit-blurring;
   prefer a distinct test-only capability — m1.
8. No J1/J2/J3 requirement remains open before the scout; only Minor hygiene edits (§2).
9. Codex may implement the scout **driver** now; a single scout **execution** waits on a
   bounded review of that driver (§4–§5).

*Distinguishing defect from open cell: nothing here is a defect; the two recommended
edits are auditability hygiene. Every item in §6 is a preregistration-stage cell for the
signed lock, untouched by this hardening. Negative space preserved: the interlock raises
the bar against accidental outcome derivation but is not a seal against deliberate
bypass, and the scout driver is authorized to be written, not yet to run.*
