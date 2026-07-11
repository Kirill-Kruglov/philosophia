# Opus 4.8 X-line review — Level 0 reconstruction choices v1 (Round 2)

Reviewer: Opus 4.8 (adversarial X-line). Stage: reconstruction-choice closure of
Round 1 §2. No training loop, scout, or outcome has been run. No `PREREG.lock` or
`decision.json` exists. This review does not predict outcomes and evaluates the
choices themselves.

## Verdict

**REVISE_CHOICES**

Four of six cells (R1 AdamW, R2 classes, R3 attention, R5 split/seeds) are closed
as written or with cosmetic labeling. R4 (init) is implementation-eligible but
carries a timing note that must ride to the lock stage. **R6 (arm hierarchy) has a
genuine gap: a single-seed fidelity control has no preregistered interpretation
rule, so a B failure is currently uninterpretable — which defeats B's stated
purpose.** The required edits are bounded and mostly documentation/interpretation;
none is a source blocker and none blocks implementation. Hence REVISE_CHOICES, not
CHOICES_ACCEPTED (the R6 gap is substantive) and not BLOCKED (nothing is
scientifically uninterpretable without unavailable code).

---

## 1. Findings

### Critical
None. No choice is scientifically uninterpretable, and no cell requires recovering
the unavailable original training code.

### Major

**J1 — R6: B at n=1 is an asymmetric control with no interpretation rule.**
B exists to interpret an A failure. But our "seed 1" is not the artifact's seed 1
(our split via `torch.randperm` and our Xavier init differ from the artifact's
unknown split/init), so B-seed-1 is just one sample of our own reconstruction. The
paper reports grokking *timing varies by seed*. Therefore:
- B **groks** → informative: the platform can produce delayed generalization under
  artifact parameters → an A failure is anchor-fidelity, not platform.
- B **fails** → *uninformative* at n=1: indistinguishable from seed variance.
As written, the A-failure branch can land on "B also failed," which resolves
nothing. Fix: preregister the **asymmetric interpretation** (only B-success carries
weight; B-failure indicts neither platform nor anchor by itself), and — resources
permitting per the scout — expand B to ≥3 seeds so the A-failure branch is not left
ambiguous. The 120k budget and no-early-stop are fine; the seed *interpretation* is
the gap.

**J2 — R4: init scale is the most grokking-timing-sensitive cell and is not logged
as an observable.** Xavier-uniform is a legitimate, deterministic, named choice and
is eligible. But applying it uniformly gives embedding-table scales
(bound ≈ 0.157 for W_E/W_U, 0.214 for W_pos, 0.097 for the 512-wide MLP) that are a
reconstruction artifact, not the paper's init, and grokking *timing* is init-scale
sensitive. Two required follow-throughs: (a) log per-matrix init scale (bound/std)
as a frozen observable so init is inspectable rather than implicit; (b) carry an
explicit note to the lock stage that DELAYED's Δ_min margin must absorb Xavier-
driven timing shift relative to the paper's ~10k-epoch report. This does not block
implementation and does not make results uninterpretable (FIT remains reachable at
these scales), but it must not be silently forgotten at lock.

### Minor

**n1 — R1: decaying MLP biases is stated incidentally, not labeled as a choice.**
Putting all params (incl. the ~640 MLP-bias params) in one decayed group is
defensible and bounded, and lr-scaled decoupled decay is the interpretation under
which λ=1 is even sane — which *supports* faithfulness. But "including MLP biases"
is currently a side effect of single-group AdamW, not an explicit labeled decision.
Label it: uniform decay, bounded effect, reconstruction choice (the original's
bias-decay treatment is not established).

**n2 — R2: the dead unembedding column contaminates the parameter-norm diagnostic.**
Scoring 0..112 is clean and creates no dead-column effect on the scored logits or
their softmax (column 113 is sliced out before softmax; it receives no CE gradient
and only decays toward zero — inert). One residue: if ‖θ‖ is a logged progress
observable, the monotonically decaying column 113 adds a spurious shrinking term.
Either exclude column 113 from the logged norm or note its inclusion. Diagnostic
only, non-blocking.

**n3 — R4: pin `xavier_uniform_(gain=1.0)` explicitly.** The default is 1.0; state
it so the scale is fully determined by the document, not the library default.

**n4 — R5: name the `torch.randperm` version-stability dependency.** The split is
reproducible only under the pinned PyTorch 2.9.1 (already pinned in R1); state that
the split hash is valid only under that pin, so a future version bump forces a
re-hash rather than a silent split change.

---

## 2. Exact mandatory edits to the six choices

- **R1:** Add one sentence labeling uniform weight decay including the MLP biases as
  an explicit, bounded reconstruction choice (original bias-decay treatment not
  established). *(n1)*
- **R2:** Add a sentence on the logged parameter norm excluding (or explicitly
  including, with note) unembedding column 113. *(n2)* No replacement to the scoring
  rule — 113-scored/114-column is accepted (see §3).
- **R3:** No edit. Accepted as written.
- **R4:** Pin `gain=1.0`; add per-matrix init-scale logging as a frozen observable;
  add a lock-stage note that Δ_min must absorb Xavier-driven timing shift. *(J2, n3)*
- **R5:** Add the `torch.randperm`/PyTorch-2.9.1 version-stability caveat on the
  split hash. *(n4)* Otherwise accepted; keep split varying per seed (see §3).
- **R6:** Add the asymmetric interpretation rule for B (only B-success is
  informative; B-failure indicts neither platform nor anchor); flag ≥3 B-seeds as a
  scout-conditioned recommendation. *(J1)*

## 3. Cells explicitly accepted as written

- **R1 (AdamW) — closes C1.** PyTorch 2.9.1 scalar path, single group, betas
  0.9/0.98, ε 1e-8, constant lr 0.001, decoupled `θ ← θ − γλθ` before the adaptive
  step. Per-step decay factors verified: **A 0.999, B 0.9999** (full-batch ⇒ per-
  epoch = per-step). lr-scaled decoupled decay is the only interpretation under
  which λ=1 is non-degenerate, so this is the *faithful* reading of the paper
  scalar, not merely a defensible one. C1 closed (subject to the n1 label).
- **R2 (classes) — closes C2, no uncontrolled dead-column effect.** 114-column
  unembedding with logits sliced to 0..112 before CE/argmax. Column 113 gets no CE
  gradient and is sliced out of the softmax, so it cannot interfere with the scored
  logits; it merely decays to zero (inert). Accuracy is essentially invariant to
  113-vs-114 scoring (the equals logit could never win once trained), so the outcome
  predicates are robust. **No replacement required.**
- **R3 (attention) — closes C3.** `QK^T/√32` = 1/√d_head is the standard scaled-
  dot-product convention for 4×32 heads and the conventional Nanda-style default;
  legitimate reconstruction choice for an unpinned source cell.
- **R5 (split/seeds) — accepted, and the varying-split direction is correct.**
  Domain separation (split_seed=master, init_seed=10000+master) removes code-order
  coupling. Sizes verified: floor(0.30·12769)=**3830 train / 8939 test**, over all
  113²=12769 ordered pairs. Crucially, **do not fix the split across seeds**: a
  shared held-out set would *reintroduce* pseudoreplication (5 correlated test
  estimates over one partition). Varying both split and init per seed is the
  stronger, anti-pseudoreplication replication claim. A and B sharing split+init at
  master 1 correctly isolates B to the λ/budget difference — keep it.

## 4. Implementation eligibility

**Eligible now.** All six cells are closed enough to write and unit-test modules;
the mandatory edits are documentation (n1–n4), an observable-logging addition (J2),
and a preregistration-stage interpretation rule (J1) — none changes module code or
blocks correct implementation. Codex/Cursor may implement and unit-test
`config/data/model/train/metrics/fourier/checkpoint` with **all training and
outcome entry points disabled**: no outcome run, no `PREREG.lock`, no
`decision.json`; the training loop may be written and exercised only by
determinism/round-trip/shape unit tests. The J1 interpretation rule and the J2
lock-stage note must be resolved before lock, not before code.

Answer to the posed Q8: **yes** — implement and unit-test with training/outcome
paths gated off, adding the §2 edits in parallel.

## 5. Remaining before-lock checklist (no outcome-dependent values decided here)

Carried from Round 1, unchanged, plus this round's additions:

- Persistence window W (steps).
- DELAYED minimum gap Δ_min, derived from published seed variation — **now with the
  explicit requirement that its margin absorb Xavier-driven init-timing shift (J2).**
- Quorum k-of-5 and the demonstration-only claim strength.
- Control pass/fail semantics — **now including R6's asymmetric B-interpretation
  rule (J1)** and the memorization / random-label leakage-control semantics.
- Uniform metric/checkpoint cadence and storage projection.
- Outcome-independent resource wall (incl. whether B expands to ≥3 seeds — a scout
  decision, made before any curve is seen).
- Archive hash for the paper's mainline λ=1/40k claim.
- Final null set (random-label control in L0; shuffled-checkpoint and wd-necessity
  deferred to L3).

None of the above is decided in this review; they remain outcome-independent and
belong to the lock stage under Kirill's signature.

---

### Question index

1. C1 closed; decaying MLP biases is bounded and defensible — label it (n1); lr-
   scaled decay is the faithful reading of λ=1. → §3, n1.
2. C2 closed; **no uncontrolled dead-column effect** — column 113 is inert; accuracy
   robust; no replacement. → §3, n2.
3. C3 closed; √32 = √d_head is a legitimate reconstruction choice. → §3.
4. Xavier is sufficiently named and eligible; **log init scale and carry a Δ_min
   margin note to lock** (J2). → §1 J2, n3.
5. Split/seed construction avoids code-order coupling and pseudoreplication;
   **do not fix the split across seeds** (that would add pseudoreplication). → §3.
6. B at 120k is an interpretable budget; **seed-1-only requires the asymmetric
   interpretation rule, and ≥3 seeds is recommended if the scout allows** (J1).
   → §1 J1.
7. All six closed for implementation; the only substantive open item is R6's
   interpretation rule (a lock-stage, not code-stage, edit). → §2, §4.
8. Yes — Codex may implement and unit-test with outcome entry points disabled. → §4.

*Faithful paper-mainline reconstruction (Arm A: λ=1, 40k, 5 seeds, √32, Xavier,
113-scored) is distinguished from the artifact-parameter fidelity control (Arm B:
λ=0.1, 120k, differing from A-master-1 only in λ and budget). Negative space
preserved: the choices are sufficient to implement and to anchor a paper-mainline
replication, and insufficient to (a) treat B-failure as evidence at n=1, or (b)
fix DELAYED's Δ_min before it absorbs Xavier-driven timing variance — both deferred
to the lock stage, not silently defaulted.*
