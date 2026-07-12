# Opus 4.8 X-line review — companion-faithful Level 0 v2 (commit 919538e)

Reviewer: Opus 4.8 (adversarial X-line). Stage: final implementation-fidelity and
bounded-prefix-driver review against the binding `COMPANION_CONFIG_TRACE.md` and the
companion-source reconciliation decision. I did not execute the prefix driver, run a
learning curve, evaluate held-out data, create any lock/decision, or predict grokking. I
read the trace and every changed module, ran the suite (75 pass) and both verifiers
(pass; 71 inherited files match), and ran bounded, non-persisting unit-level checks.

## Verdict

**COMPANION_V2_ACCEPTED**

The implementation matches the binding companion trace at every trajectory-sensitive cell
I audited: the init draw order (W_E, W_pos, **W_K, W_Q**, W_V, W_O, W_in, zeros b_in,
W_out, zeros b_out, W_U) with normal/√128 for the first eight banks and normal/√114 for
W_U; the Python `random.Random(master_seed).shuffle` split with CPython pinning; the
10-step LambdaLR warmup whose update-0 LR is 0; the forward/backward/optimizer.step/
scheduler.step/zero_grad order with checkpointed scheduler state; and 114-class training
CE with 113-class reporting. The test suite is strong enough to catch a shape-correct but
trajectory-wrong refactor (§ findings). The prefix driver is contamination-safe and is
authorized for exactly one run (§ execution). Findings are Minor only; none blocks the
run. Not `REVISE` (no fidelity gap) and not `BLOCKED` (facts are cited, not copied; the
task is complete).

---

## 1. Findings

### Critical / Major
None. Every companion-governed cell is implemented to the trace, and each is pinned by a
test that fails under a wrong reconstruction (init order/scale, split membership, warmup
sequence, decay factor, 114-vs-113 CE, forward oracle, checkpoint integrity/resume).

### Minor

**m1 — The split hash embeds the CPython *micro* version while enforcement is *minor*
(`data.py:87-88`, `config.py:10`).** `require_pinned_environment` gates on
`PINNED_PYTHON_MINOR = (3,12)`, but `version_tag` interpolates the full micro string, and
`test_companion_v2.py:38,53` pins `python_version == "3.12.3"` and a golden `split_hash`.
`random.shuffle` is stable across 3.12.x, so on a 3.12.4 point release the *membership*
assertion (`permutation[:3830]`) still passes while the micro-string and hash assertions
fail — a spurious "split changed" signal on an identity anchor. Resolve before lock: embed
the pinned minor in `version_tag` and assert minor (recommended, matches enforcement
granularity), or tighten enforcement to the exact micro and document why. Does not affect
trajectory fidelity or the single-environment prefix run.

**m2 — `bounded_check` ceiling raised to 16 without a recorded rationale
(`interlock.py:66-78`).** The maximum step count any committed caller needs is 12 (the
warmup test); the prefix uses 10, the decay test 11. A ceiling of 16 is harmless for a
capability that still forbids evaluation and verdicts and is orders of magnitude below any
learning curve, but the headroom should be documented in `EXECUTION_INTERLOCK.md` so the
non-outcome ceiling does not creep. Non-blocking.

**m3 — Budget accounting: update 0 is an LR-0 no-op (`train.py`, trace table).** Faithful
to the companion (the first optimizer update uses LR 0, changing no weights and applying
no decay — only Adam moments populate), so this is correct, not a defect. Flag it only so
the lock-stage budget/Δ_min accounting treats Arm A's 40,000 epochs as 39,999 effective
weight updates plus one moment-priming step. A preregistration note, not a code change.

## 2. Mandatory edits

None blocking. m1 should be resolved before the `PREREG.lock` (identity-anchor stability);
m2 is a one-line doc note. Neither gates the authorized prefix run or reconstruction
fidelity.

## 3. Accepted contracts

- **Initialization (Q2) — accepted, exactly pinned.** `model.py:73-92` draws each bank
  once via `randn_like(...)/divisor` in the trace order (K before Q), √128 for the eight
  d_model banks and √114 for W_U, zero biases consuming no RNG.
  `test_companion_v2.py:61` independently reconstructs the draw and asserts `torch.equal`
  per tensor plus realized-vs-expected std — a reorder, wrong divisor, or wrong
  distribution fails it. Storage orientations remain math-equivalent (no checkpoint
  sharing); the domain-separated `init_seed=10000+master` is the honest reconstruction
  label for the unrecoverable original sample.
- **Split (Q3) — accepted.** `data.py:78-85` shuffles `list(range(12769))` once with a
  dedicated `random.Random(seed)`, takes the first 3,830, varies by master seed, and pins
  torch+CPython (subject to m1). Golden fixture + independent `random.Random(0)` recompute
  in `test_companion_v2.py:31`.
- **Warmup + ordering + decay (Q4) — accepted.** `train.py:20-63` builds `LambdaLR
  min(step/10,1)`, and `optimization_step` reads LR before stepping, then AdamW.step →
  scheduler.step; the exact sequence (used 0,0.0001..0.0009,0.001…; after shifted by one)
  is pinned by `test_companion_v2.py:93`, and post-warmup uniform decay (0.999/0.9999 on
  all 11 tensors incl. biases) by `:116`. Scheduler + `warmup_updates` are in the
  optimizer state dict, hashed, and restored with a warmup-mismatch guard.
- **114/113 boundary (Q5) — accepted.** Training CE over `training_classes=114`
  (`train.py:104`); reporting, accuracy, Fourier, and the residue parameter norm over
  `reporting_classes=113` (`metrics.py`), with a new `full_parameter_l2` recording the
  114-column norm per the trace. `test_companion_v2.py:138` proves the equals column
  receives gradient and that the training loss equals the 114-class CE, not the 113-class
  CE. The v1 "dead column" reasoning is correctly retired in code and comment.
- **Schema 4 (Q7) — accepted.** `checkpoint.py` hashes model + wrapped optimizer/scheduler
  state and enforces PyTorch 2.9.1, CPython 3.12, CPU, and float32 on load; the tamper
  test now reaches `optimizer_state.optimizer.param_groups.lr` and a `python_version`
  case. Resume identity (incl. warmup position) is covered by the round-trip test.
- **Regression protection (Q6) — accepted.** The independent forward oracle
  (`test_numerics.py`) is unchanged and still validates attention roles, contraction, MLP
  orientation, and logits; combined with the init-`torch.equal`, split-golden, warmup, and
  114-CE pins, a shape-correct-but-trajectory-wrong refactor fails at least one test. I did
  not find a trajectory-relevant path left unpinned.
- **Q1 — the faithful-replication kill condition is preserved.** Every companion-governed
  cell is now implemented to the traced source, so a future failure to reproduce indicts
  the platform, not an acknowledged deviation.

## 4. Prefix execution authorization

**Authorized: exactly one invocation.** The driver (`prefix_check.py`) runs two fresh
10-step Arm A / master-0 prefixes under its own `bounded_check(10)`, on the canonical CPU
float32 deterministic path; imports no metrics, never touches `evaluation`, creates no
checkpoint, persists only hashes (AST-verified: no `"loss"`/`"losses"` JSON key, exactly
one `bounded_check` call), compares init/split/loss-sequence/final hashes, raises on
divergence, and fail-closes if its report exists.

```bash
.venv/bin/python scripts/level0_companion_v2_prefix_check.py \
  --output-dir experiments/level_0_grokking/prefix
```

**One-run guards:** invoke once; if it raises (including a determinism divergence), report
the failure and stop — do not delete and retry without a new review; create no `.pt`,
`PREREG.lock`, or `decision.json`; the report `.json` is not gitignored and is the only
committable artifact.

## 5. Allowed report fields and forbidden interpretations

**Allowed (the driver's JSON):** `kind`, `scientific_outcome:false`, `reconstruction_id`,
`arm`, `master_seed`, `device`, `dtype`, `torch_version`, `config_hash`,
`steps{per_replay,total,bounded_check_cap}`, `deterministic_prefix{primary,replay,match}`
(hashes only — init/split/loss-sequence/final), and `contamination_guards{…}`. The JSON
**alone** may be committed after verifying `scientific_outcome:false`, two 10-step
repeats, `match:true` with all four hash pairs equal, and every contamination guard false.

**Forbidden:** no raw loss/accuracy value appears or may be added; the matching hashes
certify **determinism only** and say nothing about grokking, learning, or convergence; the
10-step prefix (one LR-0 step + nine warmup updates) is not a learning curve and must not
be read as training dynamics; the hashes are fingerprints, not results.

## 6. Remaining before-lock cells

Reconstruction fidelity is closed by this review **conditional on a matching prefix
report**; no further companion-fidelity review of the reconstruction is then required, and
reconstruction-independent lock-stage drafting may proceed. These remain open and must not
be silently defaulted (they are preregistration choices, not code defects):

- persistence window W;
- Δ_min, from published seed variation, with margin absorbing the v2 companion-normal
  init-timing variance (and noting the LR-0 first update, m3);
- quorum k-of-5 and demonstration-only claim strength;
- control pass/fail semantics (memorization, random-label leakage, Arm B's asymmetric
  interpretation);
- Arm B final seed count (`(1,)` vs ≥3);
- the final null set (random-label control in L0; shuffled-checkpoint and wd-necessity
  deferred to L3);
- checkpoint/metric cadence and storage projection (companion `save_every=100` is evidence
  only);
- the split-hash granularity fix (m1) before the split hash is used as a locked anchor.

The `PREREG.lock` may be created only after the lock-stage scientific cells are drafted,
reviewed, and signed by Kirill; the interlock envelope still authorizes execution only.

---

### Question index

1. Yes — every companion-governed cell is implemented to the trace, preserving the
   faithful-replication kill condition (§3).
2. Init RNG order (K before Q), √128/√114 divisors, zero biases, and math-equivalent
   storage are sound and independently pinned (§3, Q2).
3. Python-shuffle construction is sufficient; version/hash pinning is sound except the
   micro-vs-minor coupling (m1).
4. Warmup indexing and the optimizer/scheduler/zero ordering are exact, including
   checkpoint resume and post-warmup AdamW decay (§3, Q4).
5. The 114-class training / 113-class reporting boundary is consistently enforced and
   tested via the equals-column gradient (§3, Q5).
6. No — the oracle plus init/split/warmup/CE pins make a shape-correct-but-wrong refactor
   fail a test; I found no unpinned trajectory path (§3, Q6).
7. Schema 4 protects model + optimizer + scheduler + warmup state and environment identity
   (torch, CPython, CPU, float32) (§3, Q7).
8. Raising `bounded_check` to 16 is scientifically harmless and still fail-closed and
   non-evaluating; document the headroom (m2).
9. Yes — the prefix driver is contamination-safe; execute once with the command in §4.
10. After a matching prefix report, no further companion-fidelity review is needed;
    reconstruction-independent lock-stage drafting resumes while numeric Δ_min stays
    separately unresolved (§6).

*Distinguishing defect from choice: nothing here is a code defect; m1 is identity-anchor
hygiene, m2 documentation, m3 a budget-accounting note for the lock. The reconstruction
now matches the strongest available evidence, and the only remaining gates are the
scientific lock-stage cells and Kirill's signature — not the code. Negative space
preserved: the prefix run certifies determinism, not behavior, and we match the
companion's init distribution, never its unrecoverable sample.*
