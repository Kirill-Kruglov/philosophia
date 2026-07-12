# Opus 4.8 X-line review — companion-source reconciliation before Level 0 lock

Reviewer: Opus 4.8 (adversarial X-line). Stage: pre-lock, pre-outcome source
reconciliation after discovery of the official companion training repository. No
training trajectory was run and I inspected no new outcome. I read the companion audit,
the prior source/config/choices docs, the current v1 modules, and my earlier reviews.
This review does not predict grokking, choose W/Δ_min/quorum, or treat the completed
resource scout as an outcome.

## Verdict

**REVISE_TO_COMPANION**

The companion repository `mechanistic-interpretability-grokking/progress-measures-paper`
is executable training code that self-identifies as "the code used to train the model"
and was committed 2022-10-07, before arXiv v1. For the unreported, trajectory-sensitive
details the paper prose leaves open (initialization distribution, split algorithm,
learning-rate warmup, and training cross-entropy class set), it is the strongest
available evidence short of the unrecoverable original RNG state. The R1–R6 choices were
accepted only under the now-falsified premise that no training source existed
(`SOURCE_AUDIT.md`), so that premise must be reopened where the companion speaks.

Decisively for Level 0's kill logic: the kill condition is "no grok after a *faithful*
implementation → fix platform, not theory." If we knowingly retained a weaker
paper-text reconstruction while the actual training code was in hand, a failure to
reproduce could not cleanly be charged to the platform — the faithfulness premise would
already be broken. Reconciliation is therefore required, not optional. Because no
outcome has run, this is pre-outcome revision, not tuning. Not `KEEP_INDEPENDENT` (it
would ship a knowingly weaker reconstruction); not `BLOCKED` (facts are usable as
evidence without copying, and the task is bounded).

---

## 1. Findings

### Critical

**C1 — The companion's executable details are not yet pinned cell-by-cell; a cited
companion trace must precede v2 implementation.** "Normal scaled 1/√width," "Python
`random.seed`+`shuffle`," and "LambdaLR `min(step/10,1)`" are directions, not
specifications. Before any code changes, produce a companion executable trace (analogous
to `CONFIG_TRACE.md`), keyed to `transformers.py` SHA
`de946f…cef6ad`, pinning: the exact per-tensor init divisor (which width per matrix and
per bias), the split RNG call order (build list → `random.seed(seed)` → `random.shuffle`
→ first ⌊30%⌋ train), the exact warmup indexing and optimizer/scheduler step order, the
114-class training CE and 113-class reporting slice, and the storage orientations. Values
extracted from source, labeled evidence, no code copied. Implementation is blocked on
this trace.

**C2 — Training cross-entropy class set must flip from 113 to 114; my Round 2 acceptance
of 113-class CE is hereby superseded.** The companion's `full_loss` uses all 114 logits;
the equals column therefore participates in the softmax as an always-incorrect class and
receives real (suppressive) gradients plus weight decay — it is **not** the inert
decaying dead column I described in Round 2. Training must use 114-class CE while
FIT/GENERALIZE accuracy and Fourier diagnostics slice to the 113 residue logits. This is
trajectory-affecting and mandatory for fidelity.

**C3 — Initialization must change from Xavier-uniform to the companion normal-scaled
distribution, and the exact original weights are unrecoverable.** No `torch.manual_seed`
exists in the source, so we can reproduce the init *distribution* (the scientifically
relevant object) but not the original realized sample. Pin the per-tensor normal scale
from C1, seed torch with a documented domain-separated seed labeled a reconstruction
choice, and accept that Δ_min must absorb the resulting timing variance (see §4). Xavier
must be removed, not retained.

### Major

**M1 — Split algorithm must change from `torch.randperm` to Python `random.shuffle`,
preserving per-seed variation.** `data.py:62-63` uses a torch CPU generator; the
companion seeds Python's RNG and shuffles a lexicographic list. Exact train/test
membership changes. The Round 2 anti-pseudoreplication conclusion — vary the split per
master seed — is *preserved*; only the algorithm changes (Python `seed=master`). The
`torch_version`-pinned split-hash caveat now attaches to Python's RNG stability, which is
CPython-version-stable for `random.shuffle` given a seed; pin the CPython version
alongside torch.

**M2 — A 10-step learning-rate warmup must be added; R1's "constant LR from step 0" is
superseded.** LambdaLR factor `min(step/10,1)` ramps the first ten updates. This is
pure arithmetic (version-stable), so a modern reconstruction is legitimate — but the
exact realized lr per step depends on indexing and the optimizer/scheduler step order,
which C1 must pin. Consequence for the hardening tests: the J1 zero-gradient decay factor
is now lr-dependent during warmup (decay factor `1 − lr(step)·λ`), so
`test_adamw_uniform_decay` must be re-pinned to a post-warmup step or parameterized by
`lr(step)`.

**M3 — The v1 deterministic prefix hash is void for v2; a new bounded v2 determinism
check is mandatory before full runs.** The scout's resource numbers stand (§5), but the
init and split RNG paths changed entirely, so v2 determinism is uncertified. This is a
re-certification, not a new resource scout.

### Minor

**m1 — Storage orientation is free, but the init scale is not.** W_E (114×128 vs 128×114)
and W_O (4×32×128 vs flat 128×128) are mathematically equivalent transposes/reshapes, and
since we do not load companion checkpoints, key-compatibility is irrelevant — keeping our
current orientations is acceptable. The binding constraint is that the **per-element init
distribution** match the companion's convention (its 1/√width computed on the companion's
storage width), regardless of our orientation. A test must assert per-tensor realized std
against the companion scale.

**m2 — Reconsider the parameter-norm diagnostic's equals-column exclusion.** Under
114-class CE the equals column is a trained, live parameter, not a decaying dead column.
Excluding it from *reported* diagnostics remains consistent with the companion's 113-class
analysis, but the code comment/justification must be updated: the exclusion is now a
reporting convention, not an "inert column" fact.

## 2. Exact mandatory changes

**Precondition (C1):** commit `COMPANION_CONFIG_TRACE.md` (cited, `transformers.py` hash,
no copied code) pinning every cell below. Implementation is blocked until it lands.

- **config.py:** add a versioned `reconstruction_id` = v2/companion; record the
  domain-separated torch init seed and the Python split seed policy; keep frozen
  architecture; add the warmup descriptor (steps, factor rule) and the training-CE class
  count (114) and reporting class count (113) as explicit fields.
- **data.py:** replace the `torch.Generator`/`torch.randperm` split (`:62-63`) with a
  lexicographic list shuffled by `random.seed(master)` + `random.shuffle`; keep
  ⌊0.30·12769⌋ = 3830 / 8939; recompute `split_hash` under a Python-RNG + CPython-version
  tag.
- **model.py:** replace `xavier_uniform_` (`:76-80`) with the companion per-tensor normal
  scale from C1; keep orientations (m1) but assert scales; keep zero biases per the source
  if confirmed (verify against C1).
- **optimizer/train.py:** add a `LambdaLR` (or explicit multiplier) warmup consistent with
  C1; training CE over 114 logits (remove the `[:, -1, :113]` slice from the *training*
  loss while keeping the final-token readout); keep AdamW family, betas, eps, one group,
  uniform decay incl. biases, base lr 0.001; Arm A budget 40k, no early stop.
- **metrics.py:** keep FIT/GENERALIZE accuracy and Fourier on the 113 residue logits
  (final token); update the parameter-norm comment (m2).
- **tests:** update the numerics oracle to the v2 init and 114-class training CE; re-pin
  `test_adamw_uniform_decay` for warmup (M2); add a per-tensor init-scale test (m1); add a
  warmup lr-sequence test pinning `lr(step)` for steps 0..11 and constant 0.001 after; add
  a split test asserting Python-shuffle membership and per-seed variation; assert training
  CE uses 114 classes while accuracy uses 113.
- **docs:** supersede R2/R4/R5 and the R1 constant-LR clause in
  `RECONSTRUCTION_CHOICES_V1.md` via a v2 addendum; record the companion audit hashes.

## 3. Source hierarchy

Governing layer per cell (highest applicable wins):

| Cell | Paper prose | Companion executable | Saved artifact | Independent reconstruction | Governs |
|---|---|---|---|---|---|
| Decision budget 40k, no early stop | **40k, no post-hoc stop** | 50k + thresh 1e-10 (harness ceiling; notebook truncates to 40k) | old 1M/1e-7 | — | **Paper prose** |
| Architecture (dims, heads, MLP, no LN, untied, √d_head) | states | **confirms** | confirms | — | Paper = companion (confirmed) |
| AdamW family (betas 0.9/0.98, eps 1e-8, one group, wd A=1/B=0.1, base lr 0.001) | lr, wd | **confirms** | betas/eps | — | Paper + companion |
| LR schedule (10-step warmup) | silent (lr 0.001) | **`min(step/10,1)`** | constant | — | **Companion executable** |
| Initialization distribution/scale | silent | **normal, per-tensor 1/√width** | — | — | **Companion executable** |
| Split algorithm | "30% of pairs" | **Python `seed`+`shuffle`** | — | — | **Companion executable** |
| Training CE class set | silent | **114 logits** | vocab 114 | — | **Companion executable** |
| Reporting (accuracy/Fourier) class set | 113 residues | **113 (slices off equals)** | — | — | Paper + companion (113) |
| Storage orientation (W_E, W_O) | — | 128×114, flat 128×128 | 128×114 | **our equivalent orientation OK** | Independent (math-equivalent; init scale ← companion) |
| Exact torch init seed / realized weights | — | **absent (unrecoverable)** | — | **domain-separated seed, documented** | Independent reconstruction |
| Checkpoint cadence | — | save_every=100 / 400 ckpts at 40k (informs) | save_every default | lock-stage cell | Informs a lock-stage cell |

## 4. Explicitly preserved earlier decisions

- The entire gate architecture: `ExecutionInterlock`, fail-closed schema-3 checkpoints with
  state-integrity + environment enforcement, `weights_only=True` loading, `bounded_check`
  vs scout separation, no outcome before a signed `PREREG.lock`. Unaffected.
- R3 (attention `1/√d_head`) — confirmed by the companion. Preserved.
- R6 arm hierarchy — Arm A sole decision arm at **40k, no early stop**; Arm B differs only
  by weight decay (0.1) and fixed budget (120k) and locked seeds; asymmetric B
  interpretation. Preserved and reinforced (paper 40k corroborated by the notebook
  truncation to 40k/400 checkpoints; companion 50k/1e-10 is a harness ceiling, mirroring
  the earlier 1M/threshold resolution).
- The resolution rule "paper prose outranks executable for the claimed decision budget;
  executable outranks prose for unreported trajectory details." Preserved and now the
  organizing principle of §3.
- The principle that Δ_min must absorb reconstruction init-timing variance — preserved and
  strengthened: we now match the companion init *distribution* but not its sample, so a
  timing margin is still required; the "Xavier" phrasing is superseded by "companion
  normal."
- J1/J2/J3 hardening *architecture* (independent forward oracle, integrity hashes,
  interlock). Preserved; only specific test values change with the v2 init/CE.

## 5. New non-outcome prefix check

**Required (M3):** one bounded, non-outcome v2 determinism prefix check before full runs —
a repeated short v2 prefix (single seed, Arm A, well under the 100-step reviewed cap, no
held-out evaluation, no verdict, no persisted loss, purpose-tagged) confirming identical
init, split, loss-sequence, and final-state hashes across the repeat. It re-uses the scout
contamination guards and the `bounded_check`/scout capability; it is a determinism
certificate, not a resource scout.

**Not required to repeat:** the resource scout itself. Parameter count and full-batch
dimensions are unchanged, and 114-vs-113 CE and warmup do not change per-step FLOPs or
tensor shapes, so the completed scout's latency, peak RSS, and checkpoint-byte numbers
remain valid rough measurements. Only its deterministic *prefix hash* is void for v2.

## 6. Conditions for resuming lock-stage design

Reconstruction-independent lock-stage drafting (persistence window W, quorum k-of-5 and
demonstration-only strength, control pass/fail semantics incl. the random-label leakage
control and Arm B's asymmetric rule, the final null set, cadence/storage projection
informed by the standing scout) **may resume now, in parallel** with reconciliation
implementation. Δ_min's *numeric* value must wait until v2 is implemented (its structure
may be drafted). The `PREREG.lock` may be created only after: (a) the C1 companion trace is
committed; (b) v2 is implemented per §2; (c) the numerics/decay/warmup/split/CE tests are
re-green and the full suite + verifiers pass; (d) the M3 v2 determinism check passes; and
(e) a final review confirms companion-fidelity. Until then, no `PREREG.lock` or Philosophia
`decision.json`.

---

### Question index

1. Yes — the companion is stronger evidence for unreported executable details; our prior
   choices were accepted under a now-false unavailability premise (Verdict, C1–C3).
2. Yes — reopen R2 (→114-CE), R4 (→normal scaled), R5 (→Python shuffle), and add the LR
   warmup (R1's constant-LR clause superseded) (C2, C3, M1, M2).
3. Yes — 114-class training CE with 113-class accuracy/FIT/GENERALIZE and Fourier, exactly
   as the companion does (C2).
4. The init *distribution* is sufficiently pinned once C1 fixes the per-tensor scale; the
   *sample* is unrecoverable, so a documented domain-separated torch seed is the honest
   reconstruction label, and Δ_min absorbs the timing variance (C3, §4).
5. Storage orientations may stay (math-equivalent, no checkpoint sharing); the binding
   constraint is the per-element init scale from the companion convention (m1).
6. Yes — paper 40k outranks companion 50k/threshold for the decision arm; 50k/1e-10 is a
   harness ceiling and the early-stop threshold is forbidden by policy (§3, §4).
7. Legitimate — the warmup is version-stable arithmetic; tests must pin `lr(step)` for
   steps 0..11 (base 0.001 × the companion-indexed `min(step/10,1)`) and constant 0.001
   thereafter, with the optimizer/scheduler order fixed by C1 (M2).
8. The prior scout remains the sole *resource* scout; a new bounded v2 *determinism* prefix
   check is mandatory before full runs (M3, §5).
9. Preserved: gate architecture, R3, R6/40k, the source-hierarchy rule, the Δ_min-margin
   principle, J1–J3 architecture. Superseded: R2 (113-CE), R4 (Xavier), R5 (randperm),
   R1's constant-LR clause, and the v1 prefix hash (§4, §1).
10. Lock-stage drafting resumes now for reconstruction-independent cells; the lock itself
    waits on §6 conditions.

*Distinguishing evidence from defect: nothing in the v1 code is a bug — it faithfully
implemented the best evidence then available. The companion is simply better evidence, and
Level 0's faithfulness premise obliges us to adopt it before outcome. Negative space
preserved: we can match the companion's init distribution but not its exact weights, and
the paper's 40k budget — not the companion's 50k harness ceiling — governs the decision
arm.*
