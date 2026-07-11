# Opus 4.8 X-line review — gated Level 0 implementation (commit 3a06ac0)

Reviewer: Opus 4.8 (adversarial X-line). Stage: code review of the gated
reconstruction modules, after Round 2 `REVISE_CHOICES`. No outcome run, full
training loop, resource scout, `PREREG.lock`, or `decision.json` exists. I did not
execute a scientific trajectory; I ran the unit suite (42 pass locally; 9 in
`test_level0_modules.py`) and two bounded single-forward checks. This review does
not predict grokking and does not select any locked value.

## Verdict

**REVISE_IMPLEMENTATION**

The reconstruction is mathematically faithful and dimensionally correct — I
hand-traced the forward pass and confirmed numerically that attention is causal
(query position 0 places exactly 0 weight on future keys), softmax normalizes over
keys, the final-token readout attends to all three positions, and the scored output
is (·,113). AdamW, data construction, config hybrid-rejection, and the Fourier
primitives are correct. **No Critical defect is present.** The verdict is
REVISE_IMPLEMENTATION, not IMPLEMENTATION_ACCEPTED, because the test suite cannot
distinguish this correct implementation from a shape-correct but mathematically
wrong one (Q10), the checkpoint lacks a verified state-integrity hash (Q7), and the
outcome gate is procedural rather than interlocked (Q9). It is not BLOCKED: nothing
is uninterpretable and no source cell reopened.

---

## 1. Findings

### Critical
None. No present correctness defect; the gate holds procedurally; no source cell is
reopened.

### Major

**J1 — The test suite cannot catch a shape-correct-but-mathematically-wrong model
(Q10).** `test_level0_modules.py:96` checks only shapes, determinism, and the
114→113 slice. Nothing pins the *numerics*: a transposed score einsum, a softmax
over the wrong axis, an inverted causal mask, or Q/K swapped would pass all 42
tests. The forward pass at `src/philosophia/level0/model.py:108-134` is correct
today (I verified externally), but the entire scientific edifice rests on it and a
future refactor could break it with a green suite. Mandatory before any scout: add
numerical/analytic tests — see §2.

**J2 — Checkpoint integrity is under-guarded for a scout (Q7).**
`load_checkpoint` (`checkpoint.py:79-112`) verifies schema, internal config-hash
consistency, and the expected config/split hashes, and loads with `strict=True` —
good. But it stores **no hash of `model_state`/`optimizer_state`**, so silent tensor
corruption that leaves the config intact passes load undetected; and the recorded
`torch_version`/`device`/`dtype` (`checkpoint.py:44-54`) are **never enforced on
load**, so version/backend drift is invisible even though `data.build_dataset`
enforces the torch pin at `data.py:56`. The existing round-trip test
(`test_level0_modules.py:194`) compares stored-to-stored `init_scales`, not
stored-to-reconstructed model state. Mandatory before scout: store and verify a
`model_state_hash`/optimizer-state hash on load, and enforce `torch_version` and
CPU/float32 on the canonical path.

**J3 — The outcome gate is procedural, not interlocked (Q9).** No committed entry
point runs a trajectory: `run_outcome_training` fail-closes (`train.py:66-69`),
`optimization_step` rejects an `EvaluationView` (`train.py:48`), and
`test_training_boundary_is_fail_closed` enforces the train-module import boundary.
**But** `optimization_step` (single step), `metrics.evaluate`, and
`metrics.first_persistent_step` are all public and freely composable by any caller
into a full learning curve *and* a FIT/GENERALIZE verdict, with no technical
interlock; the only thing preventing it is that no driver / `run.py` is committed
and no `PREREG.lock` exists. This is not a current violation, but the exact artifact
that must be gated (a derived verdict) is assemblable from public primitives.
Mandatory before any multi-step driver / `run.py` is added: a lock-file interlock
gating multi-step execution, plus a test asserting no committed module runs more
than one optimization step outside the scout scope.

### Minor

- **m1 — `torch.load(..., weights_only=False)` (`checkpoint.py:87`)** loads an
  arbitrary pickle. Acceptable for self-produced local files; note it and consider
  `weights_only=True` with an allowlist once the payload schema is stable.
- **m2 — `random_label_control` reuses `bundle.split_hash` unchanged
  (`data.py:110`)** while changing only `universe_hash`. Provenance is technically
  captured, but a distinct control-split tag would make the negative-control lineage
  unambiguous.
- **m3 — `gradient_l2` sums over all params with non-`None` grad (`train.py:57-61`)**,
  which includes zero-gradient embedding rows for absent tokens. Harmless as a smoke
  value; if it ever becomes a *locked* observable, define it precisely first.
- **m4 — `InitScale.realized_std` uses `unbiased=False` (`model.py:43`)** — fine,
  but document it so the observable is fully specified.
- **m5 — `evaluate`/`scored_parameter_l2` set `model.eval()` (`metrics.py:31`)**
  with no dropout/norm in the model, so train/eval modes are identical here; benign,
  worth a one-line note so no one later assumes eval-mode semantics.

---

## 2. Mandatory code and test edits

**Tests (before scout):**
1. **Attention correctness:** assert softmax rows sum to 1 over keys and that query
   position 0 has ~0 weight on positions 1–2 (catches inverted mask / wrong softmax
   axis). (I ran this externally; it passes — commit it.)
2. **Analytic forward reference:** with small hand-set weights (or a fixed seed and a
   frozen expected output hash), assert the final-token logits equal a hand/oracle
   value — catches transposed einsums that preserve shape.
3. **Weight-decay magnitude:** one AdamW step with a zeroed gradient must shrink each
   trainable tensor (incl. `b_in`,`b_out`) by exactly `1 - lr·λ`; assert the factor
   for Arm A (0.999) and Arm B (0.9999). Confirms uniform decay reaches biases and
   the pinned scalar path (C1).
4. **Optimizer coverage:** assert the optimizer sees all 11 parameter tensors in one
   group at the arm's `weight_decay`, and that no LR scheduler is attached.
5. **Causal-readout independence:** perturbing a token at position 0/1 changes the
   final-token logits (the readout actually depends on both operands).

**Code (before scout):**
6. Store `model_state_hash` and an optimizer-state hash in checkpoint metadata;
   verify both on load (J2).
7. Enforce `torch_version == 2.9.1` and CPU/float32 in `load_checkpoint` on the
   canonical path (J2).
8. Add a lock-file interlock to any future multi-step driver and a test that no
   committed module executes >1 step outside the declared scout scope (J3).

## 3. Explicitly accepted contracts

- **Architecture (Q1) — accepted, verified faithful.** Causal attention with
  `QK^T/√32` (`model.py:108-126`), dual residual paths around attention and MLP
  (`model.py:129,133`), final-token readout, 114-logit output, and artifact-oriented
  `W_in=(512,128)` / `W_out=(128,512)` storage (`model.py:64-66`; test
  `:101-103`). Numerically confirmed causal and correctly normalized.
- **Initialization (Q2) — accepted.** `xavier_uniform_(gain=1.0)` applied
  per-matrix and per-head (`model.py:73-82`), with realized-scale observables
  captured (`model.py:84-101`) and checkpointed (`checkpoint.py:53`). Reported
  `xavier_bound` matches PyTorch fan-in/out.
- **AdamW (Q3) — accepted, closes C1 faithfully.** Pinned scalar path
  (`foreach/fused/capturable/differentiable=False`), single group over all
  parameters incl. MLP biases, no scheduler (`train.py:25-40`).
- **Data (Q4) — accepted.** Exact 113² lexicographic coverage, 3830/8939 split,
  domain-separated split/init seeds (`config.py:122-128`, `data.py:44-67`), and
  `LearnerView`/`EvaluationView` separation with a type-guarded `optimization_step`
  and enforced import boundary (`train.py:48`, test `:211-224`).
- **Config hybrid rejection (Q5) — accepted.** A and B are pinned exactly, seed
  schedules included, hybrids rejected (`config.py:53-79`); the B expansion is left
  as the pre-lock choice between `(1,)` and ≥3 seeds drawn from 0–4.
- **114-vs-113 consistency (Q6) — accepted.** The 113-slice is applied uniformly in
  training (`train.py:52`), evaluation (`metrics.py:32`), accuracy
  (`metrics.py:34`), and the parameter norm excludes the dead unembedding column
  (`metrics.py:43-44`; test `:121-126`).
- **Fourier (Q8) — accepted, claim-neutral.** Orthonormal real basis (113 columns:
  1 DC + 56 cos + 56 sin), correct projection and energy, asserting nothing about
  grokking (`fourier.py:8-41`; test `:129-136`).

## 4. May work proceed to lock-stage design?

**Yes.** The reconstruction is faithful and the six choices are correctly encoded;
lock-stage design (persistence window, Δ_min, quorum, cadence, resource wall, null
set, B-seed decision) may proceed in parallel with the §2 edits. None of the §2
items reopens a reconstruction cell or blocks lock-stage design work; they gate the
*scout*, not the design.

## 5. Bounded timing/storage scout eligibility

**Eligible only after J1 and J2 land**, and strictly bounded so it cannot reveal a
learning curve or a verdict:

- **Scope:** a single seed (master 0), Arm A config, on the canonical CPU float32
  deterministic path; **≤ 100 optimization steps or ≤ 2 minutes wall-clock,
  whichever comes first, enforced by a hard-coded cap.** Grokking is a ≥10⁴-epoch
  phenomenon, so ≤100 steps is orders of magnitude short of any generalization
  signal. Purpose limited to: per-step latency, peak memory, one full checkpoint
  round-trip byte size, and the deterministic prefix-hash replay.
- **Contamination guards:** the scout path must **not** call `metrics.evaluate` on
  the held-out set, must **not** compute or persist any held-out loss/accuracy, must
  **not** invoke `first_persistent_step`, must **not** persist a per-step train-loss
  *series* that could be mined as a curve (a single final smoke value is fine), must
  **not** create `PREREG.lock`/`decision.json`, and must tag every artifact
  `timing-storage-scout / non-outcome`. The hard step cap must be enforced in code,
  not by convention (reuse the J3 interlock).

Until J1/J2 land, only the already-permitted single-step and round-trip unit checks
are eligible.

## 6. Remaining risks only the signed preregistration can resolve

These are open cells, not implementation defects, and must not be silently
defaulted by any module:

- Persistence window W (steps).
- DELAYED minimum gap Δ_min, from published seed variation, with margin absorbing
  Xavier-driven init-timing shift.
- Quorum k-of-5 and demonstration-only claim strength.
- Control pass/fail semantics: memorization control, random-label leakage control,
  and Arm B's asymmetric interpretation (only B-success is informative).
- Uniform metric/checkpoint cadence and storage projection (informed by the scout).
- Outcome-independent resource wall.
- Archive hash for the paper's mainline λ=1/40k claim.
- Final null set (random-label control in L0; shuffled-checkpoint and wd-necessity
  deferred to L3).
- Arm B seed-count expansion (`(1,)` vs ≥3), decided before any curve is seen.

---

### Question index

1. Transformer faithful — causal attention, √32 scaling, dual residual paths,
   final-token readout, `W_in=(512,128)`/`W_out=(128,512)` — **verified** (§3, J1).
2. Xavier `gain=1.0` per-matrix/per-head with correct bounds and realized-scale
   observables — accepted (§3).
3. AdamW pinned scalar path, uniform decay of all 11 tensors incl. biases, no
   scheduler — accepted, closes C1 (§3).
4. Data covers 113² lexicographic pairs, domain-separated seeds, learner never
   receives an `EvaluationView` — accepted (§3).
5. Config rejects A/B hybrids incl. seed schedules; B expansion left pre-lock —
   accepted (§3).
6. 114 model logits / 113 scored handled consistently incl. parameter norm —
   accepted (§3, Q6).
7. Checkpoint fail-closed on config/split/schema; **missing state-integrity hash and
   version/backend enforcement** — J2, §2 items 6–7.
8. Fourier primitives correct and claim-neutral — accepted (§3).
9. No committed entry point launches a trajectory or derives a verdict, but the
   primitives are composable with no interlock — J3, §2 item 8.
10. Missing numerical/analytic, causality, and weight-decay-magnitude tests that
    would catch a shape-correct-but-wrong implementation — J1, §2 items 1–5.

*Distinguishing defect from open cell: no implementation defect blocks progress; the
mandatory edits harden the test suite and checkpoint against future regressions and
interlock the outcome gate. Everything in §6 is a preregistration-stage cell the
signed lock must resolve, not code to change now. Negative space preserved: I verified
the forward pass is correct, but the committed suite does not — so "correct today" is
not yet "protected against a green-but-wrong refactor."*
