# Opus 4.8 X-line review — Philosophia Level 0 design

Reviewer: Opus 4.8 (adversarial X-line). Stage: design, before implementation
and before preregistration. No Level 0 outcome has been run. This review does
not predict whether grokking will occur.

## Verdict

**READY_FOR_REVISION**

Rationale (and explicit rejection of the other two verdicts):

- Not **BLOCKED_SOURCE.** The paper (Nanda et al., 2301.05217) is a published,
  citeable anchor. Every architecture cell is triangulated — paper text and the
  inspected artifact tensor shapes agree independently. The optimizer family,
  learning rate, training fraction, modulus, seed count, weight-decay scalar, and
  epoch budget are all stated in the paper. That is sufficient to preregister a
  *paper-mainline* positive arm as an independent reimplementation. The remaining
  gaps (split RNG, initialization, seed values, attention scale, equals-logit
  treatment) are reconstruction-free choices to be *documented as deviations*,
  not source blockers. Over-blocking here would be its own error.
- Not **REJECT_DESIGN.** The scaffolding is correct on the load-bearing points:
  full-run replication unit, no early success stop, fail-closed train/eval
  separation, deterministic CPU canonical path, artifact-vs-paper resolution
  rule, and an explicit refusal to synthesize a hybrid config. These are the
  hard things and they are already right.
- **READY_FOR_REVISION** is the honest call: the design is structurally sound and
  the source is adequate for the paper arm, but named Critical revisions must
  land before implementation, and further named revisions before lock. Cursor
  may not implement yet (see §10).

---

## 1. Findings (Critical → Major → Minor)

### Critical

**C1 — "weight_decay=1" is uninterpretable without the update equation.**
AdamW decouples weight decay and, in PyTorch, applies `p ← p − lr·λ·p` each step,
so the *effective* per-step decay scales with the learning rate. The scalar "λ=1"
therefore means nothing until the exact optimizer update — decay coupling, whether
λ is lr-scaled, betas 0.9/0.98, ε 1e-8 — is pinned. The paper's "λ=1" and the
artifact's executable λ=0.1 may reflect different runs *or* the same run under
different coupling conventions. Until the update equation is fixed, a null result
on the paper arm is uninterpretable. This must be closed before implementation.

**C2 — Output class count (equals-logit in cross-entropy) is unresolved and
changes the metric semantics.** Embedding/unembedding are width 114, but targets
occupy the 113 residues. Whether the equals logit participates in the softmax /
cross-entropy changes both loss and accuracy definitions. FIT and GENERALIZE are
defined on accuracy; if the class count is ambiguous, so are the outcome
predicates. Must be pinned to one convention (recommend: score over the 113
residue logits only, with the 114th excluded from the argmax and the loss)
before implementation, and recorded as a reconstruction choice.

**C3 — Attention scaling is unspecified and dynamics-relevant.** 1/√d_head vs
1/√d_model vs unscaled changes attention temperature and therefore the training
trajectory and the *timing* of any transition. Nanda's own transformer
conventionally uses 1/√d_head, but this must be pinned from the traced spec, not
assumed. Unresolved at implementation time → uninterpretable timing, which
directly corrupts the DELAYED predicate.

**C4 — DELAYED is circular unless Δ_min is fixed from published variance before
the run.** "GENERALIZE follows FIT by a locked minimum delay" is self-fulfilling
if Δ_min is chosen after seeing curves. Δ_min must be derived from the anchor's
reported separation (paper reports early fit and grokking ≈10k epochs with seed
variation) with a stated margin, and locked before any outcome run. Absent this,
DELAYED is not falsifiable.

### Major

**M1 — The artifact arm cannot be reproduced literally: it used early stopping.**
Artifact config: num_epochs=1,000,000, stopping_thresh=5e-7, stored epoch 107,790.
That is an early-stopped run, which directly contradicts the design's "no early
success stop, run to fixed budget." If the artifact arm is run at all, its budget
must be converted to a fixed, preregistered number of epochs, and that conversion
recorded as a loud choice — not inherited. Additionally, if that stopping
threshold monitored *test* loss, it is stopping-by-leakage and a second reason
never to inherit it.

**M2 — Primary/secondary arm hierarchy is not committed.** The design lists the
paper and artifact configs but does not lock which is the grokking-decision arm.
Because the two anchors disagree precisely on the hyperparameter grokking is most
sensitive to (weight decay), a single arm creates an interpretability hazard: a
paper-arm failure cannot be distinguished from "λ=1 was never the released
value." Fix: lock the paper mainline (λ=1, 40k, 5 seeds) as the single
grokking-decision arm; run the artifact reconstruction (λ=0.1, fixed budget,
seed=1+) as a *labeled fidelity control only* (§4, §6). Neither's parameters may
change after failure without a new lock.

**M3 — "Five observations" reintroduces pseudoreplication.** FIT/GENERALIZE are
"at least 0.99/0.95 for five observations." Five *what*? If five consecutive
checkpoints of one run, those are not independent replicates and must never count
toward the seed quorum. Define FIT/GENERALIZE per seed as a persistence window
(first step where the threshold is met and held for W locked steps), and make the
unit of variance the seed/run only. State explicitly that L0 is a replication
demonstration over 5 seeds, not a powered hypothesis test, and lock the quorum
(k of 5) before the run.

**M4 — Initialization scheme is unspecified and grokking-timing-sensitive.** The
exact init distribution and scale were not established from the source. It cannot
be bit-matched; pick a named convention, document it as a deviation, and ensure
Δ_min's margin (C4) tolerates init-driven timing variance. Must be fixed before
implementation so the config module is honest.

**M5 — Missing memorization / negative controls that separate platform-kill from
replication-kill.** The design's kill logic says "no grok after faithful setup →
fix platform, not theory," but provides no control that isolates *which* broke.
Add (a) a memorization control — every arm must reach FIT even if it never
generalizes; failure to memorize 30% of pairs at full-batch AdamW is a platform
kill, not a grokking result; (b) the random-label control repurposed as a
leakage/generalization negative control — it must FIT but never GENERALIZE; if it
generalizes, the harness leaks (platform kill); if it cannot memorize, capacity/
optimizer bug (platform kill). These pass/fail semantics must be preregistered.

### Minor

**m1 — Split RNG library and order unpinned.** Choose (recommend NumPy
`default_rng(seed)` permutation over the 113² pair index), log the split hash
before step 0 (design already requires the write; it does not yet name the
algorithm).

**m2 — Checkpoint cadence is a proposal, not locked, and must be uniform.**
Dense logging chosen post-hoc around an observed transition is analysis leakage.
Lock a fixed uniform cadence before the run; let the storage/timing scout size
it. 100-step cadence over 40k epochs × 5 seeds × full optimizer state must be
storage-budgeted.

**m3 — ROCm equivalence is under-defined and should not enter the L0 decision.**
Cross-backend float results are generally not bit-identical, so "identical prefix
hashes" is likely unachievable and "within tolerance" is undefined for a discrete
grokking event. Recommend: the locked L0 replication decision runs on CPU
float32 only; ROCm stays an engineering note, never an outcome path.

**m4 — Resource stop must be outcome-independent.** The battery/time/storage wall
must be a hard preregistered bound that cannot be triggered by "it looks like it
won't grok." State it in wall-clock/step/byte terms, decorrelated from metrics.

**m5 — Paper source not yet pinned by hash to the specific claim location.** The
trace marks λ=1 and 40k as "paper-confirmed" but does not archive the exact
section/table asserting them as the *mainline*. Given the artifact's contradiction,
archive that location by hash before lock; if the paper does not unambiguously
assert λ=1/40k as mainline, resolve before lock.

---

## 2. Mandatory changes before implementation

1. **Pin the AdamW update equation** (C1): decay coupling, λ semantics, betas
   0.9/0.98, ε 1e-8. State whether λ is lr-scaled. Use one explicit update.
2. **Pin the output class count** (C2): 113 vs 114 logits in loss/argmax. Record
   as reconstruction choice.
3. **Pin attention scaling** (C3): the exact 1/√· convention.
4. **Pin the initialization scheme** (M4): named distribution + scale, documented
   as a deviation.
5. **Pin the split algorithm and RNG** (m1).
6. **Commit the primary arm** (M2): paper mainline λ=1/40k/5-seeds as the single
   grokking-decision arm; artifact arm demoted to labeled fidelity control.

Amend `CONFIG_TRACE.md` to move these six cells from "unresolved" to "independent
reconstruction, chosen value + justification," honestly labeled. None of these is
a source blocker; all are bounded reconstruction closures.

## 3. Mandatory changes before preregistration lock

1. **FIT/GENERALIZE persistence window W** in steps (M3), unit of variance = seed.
2. **Δ_min for DELAYED** derived from published anchor variance, with margin (C4).
3. **Quorum (k of 5)** locked, with the explicit statement that L0 is a
   replication demonstration, not a powered test (M3).
4. **Positive/negative control semantics** locked: memorization control, random-
   label leakage control, artifact fidelity arm — each with pass/fail that
   separates platform-kill from replication-kill (M5, §6).
5. **Null/control set finalized** per §5: random-label control *in*; shuffled-
   checkpoint predictive null and weight-decay-necessity *deferred to L3*.
6. **Artifact-arm fixed budget** (no early stop) chosen and recorded (M1).
7. **Fixed uniform checkpoint cadence** locked; storage scout completed (m2).
8. **Resource-stop wall** stated outcome-independently (m4).
9. **Paper claim location archived by hash** (m5).
10. Confirm no `PREREG.lock` / `decision.json` exists until Kirill signs.

---

## 4. Proposed positive-arm table

| Arm | Role | λ (weight decay) | Budget / stop | Seeds | Source | Rationale |
|---|---|---|---|---|---|---|
| **A — Paper mainline** | **Primary, grokking-decision** | λ=1 under the pinned AdamW update (C1) | 40,000 epochs, fixed, no early stop | 5 (values locked at scout) | Paper text 2301.05217 | Published, citeable, fully specified anchor; the only arm the FIT/GENERALIZE/DELAYED verdict is read on. Independent reimplementation; all reconstruction-free cells documented as deviations. |
| **B — Artifact reconstruction** | **Secondary, fidelity control only** | executable λ=0.1 (optimizer param group) | fixed budget (converted from the 1M+early-stop; e.g. 40k or a separately justified value) — literal early-stop forbidden | ≥1 (start seed=1) | Saved artifact `wd_10-1_mod_addition_loss_curve.pth`, executable optimizer state | Disambiguates a Arm-A failure: if A fails but B groks, the platform breathes and the failure is anchor-fidelity, not platform. Never a second success target; never merged with A into a hybrid config. |

Resolution rule (endorsed as written in the trace): paper text outranks artifact
*names* for the claimed mainline; executable optimizer state outranks a stale
config field for describing the *artifact*; the two may never be fused without
the label "independent reconstruction."

**One arm decides grokking (A); both arms run, B only to interpret an A failure.**

## 5. Proposed null / control table

| Item | Type | Belongs in | Expected role | Kill / interpretation |
|---|---|---|---|---|
| Random labels, identical inputs/split/budget/schedule | Negative control | **L0** | Must FIT (memorize noise), must NOT GENERALIZE | Generalizes → harness leaks (platform kill). Cannot memorize → capacity/optimizer bug (platform kill). |
| Memorization reachability | Positive control | **L0** | Every real arm reaches FIT even absent generalization | Cannot memorize 30% at full-batch AdamW → platform kill, not a grokking result. |
| Artifact fidelity arm (B) | Positive control | **L0** | Cross-checks Arm A | A fails, B groks → anchor-fidelity issue, not platform. |
| Deterministic CPU replay | Platform control | **L0** | Identical prefix hashes on repeat | Divergence beyond tolerance → platform kill. |
| Tensor-shape / no-LayerNorm / untied identity | Platform control | **L0** | Matches artifact keys | Mismatch → implementation kill. |
| Shuffled checkpoint order for predictive progress measures | Null | **L3 (deferred)** | Tests whether a progress measure predicts the transition above chance | L0 makes no progress-measure prediction claim, so this null has nothing to guard here. |
| No/low weight decay as a mechanism test | Null | **L3 (deferred)** | Tests whether wd is necessary for grokking | This is a mechanism claim L0 must not make; λ is the disputed cell and is handled as an *arm*, not a null. |
| Fourier structure, restricted/excluded loss | Diagnostic (recorded, not tested) | **L0 records; L3 tests** | Logged for later analysis | In L0 these are stored, never asserted to predict or explain anything. |

## 6. Remaining claims Level 0 is forbidden to make

- Any claim that a progress measure (Fourier sparsity, restricted/excluded loss)
  *predicts* or *explains* the generalization transition. L0 records these as
  frozen diagnostics only; prediction is an L3 thesis.
- Any mechanism claim (e.g., "weight decay causes grokking," "a new basis appears
  at grokking"). Those are L3 rows in the kill matrix.
- Any claim that grokking here is *evidence for the Philosophia thesis* (derivable
  worlds provide primary experience). L0 is platform replication; it is not
  contact, experience, transfer, or path-credit.
- Any cross-world / cross-representation compression claim. Single world, single
  task.
- Any statistical claim beyond "k of 5 seeds reproduced delayed generalization
  under the locked criteria." Five seeds is a demonstration, not a powered test;
  no p-values, no effect sizes, no generalization to other moduli/architectures.
- Any claim built on ROCm results, or on the artifact arm as an independent
  success (it is a control).
- Any post-hoc claim from parameters changed after a failure without a new loud
  lock.

## 7. Handoff specification for Codex / Cursor

**Status: implementation-eligible only after §2 lands and is versioned; NO outcome
run until Kirill's lock. The training loop may be written and unit-tested; it may
not be run for outcome.**

Build in `src/philosophia/level0/` as independently testable units (per the spec
draft): `config.py`, `data.py`, `model.py`, `train.py`, `metrics.py`,
`fourier.py`, `checkpoint.py`; orchestration in
`experiments/level_0_grokking/run.py`.

Frozen constants (confirmed, do not re-derive): p=113; seq len 3 (a, b, equals);
frac_train=0.3; 1 layer; d_model=128; 4 heads × d_head 32; MLP 512 ReLU; learned
token+positional embeddings (W_pos 3×128); no LayerNorm; untied W_E/W_U; no
embed/attn/unembed bias; MLP in/out biases; loss read at final token only;
optimizer betas 0.9/0.98, ε 1e-8, lr 0.001, full-batch AdamW.

Cells the config module must expose as *named reconstruction choices* (values set
by §2, not invented by the implementer): AdamW update/decay coupling and λ per
arm (A: 1, B: 0.1); output class count (recommend 113); attention scale; init
scheme; split RNG (recommend NumPy `default_rng`, log split hash pre-step-0);
fixed epoch budget per arm (A: 40,000; B: converted fixed value); five seed
values.

Fail-closed rules (hard requirements): dataset constructors return separate
learner/eval views; training never receives test targets or progress-measure
verdicts; init/split/data-order hashes written before step 0; every checkpoint
carries source commit, HEAD, Python/PyTorch versions, device, dtype, seed, full
optimizer state; resume refuses any config/split hash mismatch; the evaluator
reads frozen artifacts and cannot alter stopping. No early success stop; no
early failure stop except the outcome-independent resource wall. CPU float32
deterministic is canonical; ROCm never enters the decision.

Tests required before any scout (extend the spec's list): all 113² ordered pairs
occur exactly once pre-split; train/test disjoint and covering; targets = a+b mod
113; equals only in final input position; tensor shapes match artifact keys; no
LayerNorm / no tied embed; a full-batch step changes params and stays finite;
checkpoint round-trip resumes bit-identically; the eval module is unreachable
from train via a forbidden import edge; random-label and (deferred) shuffled-
checkpoint generators are deterministic; **added:** FIT/GENERALIZE persistence-
window predicate is a pure function of a frozen curve; memorization and random-
label controls have locked pass/fail semantics; the config serializer refuses a
hybrid (A+B) configuration.

## 8. Answers to the ten posed questions (index)

1. Faithful enough for the **paper arm**; source incompleteness is *not* a
   blocker — remaining gaps are reconstruction choices (§1 C1–C3, M4; §2).
2. Lock **paper λ=1/40k** as the sole decision arm; artifact λ=0.1 as a labeled
   fidelity control at a *fixed* budget (early-stop forbidden) (§4, M1–M2).
3. **One arm decides** (A); **both run**, B only to interpret an A failure (§3,
   §4, §6).
4. FIT/GENERALIZE are non-circular once class count (C2) and a persistence window
   (M3) are fixed; **DELAYED is circular until Δ_min is locked from published
   variance** (C4).
5. L0 keeps the **random-label negative control**; **shuffled-checkpoint** and
   **wd-necessity** nulls **defer to L3**; Fourier/restricted-excluded are L0
   diagnostics only (§5).
6. Positive controls: **memorization reachability**, **random-label leakage
   control**, **artifact fidelity arm**, deterministic replay, shape identity —
   with preregistered pass/fail that separates platform-kill from replication-
   kill (§5, M5).
7. Pseudoreplication (M3), leakage (C2 class count, M1 stop-by-test-loss),
   stopping (M1, m4), checkpoint (m2), backend equivalence (m3) — all addressed
   above.
8. Architecture identity is adequate on confirmed cells, but **three hidden-
   deviation hazards (C1 AdamW coupling, C2 class count, C3 attention scale) plus
   init (M4)** must be pinned or a null result is uninterpretable (§1, §2).
9. Before **implementation**: C1, C2, C3, M4, m1, arm choice (M2). Before
   **scout**: cadence (m2), seed values, artifact fixed budget (M1), resource
   wall (m4). Before **lock**: persistence window, Δ_min, quorum, control
   semantics, null-set finalization, paper hash (§3).
10. **Cursor may not implement yet.** A bounded configuration audit (§2 closures +
    arm decision, committed and versioned in `CONFIG_TRACE.md`) is required
    first. This is *not* a full source re-audit and *not* BLOCKED_SOURCE. After
    those closures land, implementation of tested-but-not-run modules is eligible;
    the outcome run stays gated on Kirill's lock.

---

*Negative space preserved: the evidence is sufficient to anchor and preregister a
paper-mainline replication, and insufficient to (a) treat the artifact as the
paper's mainline run, (b) fix λ semantics without the update equation, (c) define
DELAYED without an externally-derived Δ_min, or (d) admit any ROCm or progress-
measure-prediction result into the L0 decision. Where insufficient, the fix is a
named reconstruction choice or an L3 deferral, not a silent default.*
