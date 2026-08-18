# Preregistration v0.2 — candidate for lock
## Forced sharing versus explicit world separation in sequential modular worlds

**Status:** CANDIDATE FOR LOCK — NOT YET LOCKED  
**Programme:** `philosophia`, separately chartered successor cell  
**Independent unit:** paired replicate seed  
**Primary arms:** `ALIASED`, `SEPARABLE`  
**Primary endpoints:** fresh-world probe after history length `k=1` and `k=6`  
**Secondary endpoints:** fresh-world probes `k=2,4`; H1 reacquisition after `k=6`  
**Conditional diagnostic:** `SHUFFLED_TAG`, mandatory after any valid primary outcome other than `ALIASED_TRANSFER_ADVANTAGE`  
**Signed SESOI:** `ln(1.20)=0.1823215567939546`

---

## 1. Scientific scope

This cell tests one deliberately narrow proxy:

> **Does forced non-separability of the latent modulus across six sequential modular worlds reduce the in-weights adaptation cost of that latent on a seventh unseen world more than the same history when world identity is available at learner input?**

The experiment does **not** claim to isolate “contradiction alone.” In this construction:

- if the same observable input can map to incompatible targets across worlds, world identity is not recoverable from the learner input;
- making those worlds simultaneously non-conflicting requires some input information that separates them.

The causal manipulation is therefore the complete information regime:

- `ALIASED`: world identity is unavailable from learner input during history; the same learner input may receive incompatible targets in different sequential blocks;
- `SEPARABLE`: world identity is available via fixed non-trainable context codes, so the worlds are represented as distinct input-conditioned functions.

The first cell deliberately leaves unresolved whether any benefit comes from a reusable modular mechanism. A positive primary result licenses a separately locked structural null / Experiment B. It does not pre-earn that result.

---

## 2. Relation to the stopped-open programme

The earlier programme required candidate experience to reduce future work outside the exact description in which it was learned. This successor cell operationalizes only that work-reduction obligation.

The prior stopped-open route remains unchanged. Earlier ACTIVE/YOKED comparisons were never run and successor development branches stopped at their own gates. No result from this cell may be retroactively promoted into those canonical claims.

This cell also rejects the impossible requirement that one feed-forward parameter state, with no world signal, answer contradictory modular worlds simultaneously. What may become reusable in weights is an **adaptation structure**; the current active world is a state reached by later in-weights adaptation.

---

## 3. Primary scientific question

For each replicate seed, a learner traverses six modular worlds. Two paired histories are identical in:

- model initialization;
- ordered modulus sequence;
- operands and targets;
- train/held-out split;
- batch order;
- optimizer family and numerical hyperparameters;
- number of history updates per world;
- optimizer resets at boundaries;
- reserved fresh world `C`;
- C probe data/order/budget;
- all deterministic seeds except the arm-specific context assignment required by the manipulation.

They differ only in whether context input carries world identity after H1.

The primary question is whether the reduction in fresh-C restricted adaptation cost from `k=1` to `k=6` is larger in `ALIASED` than in `SEPARABLE`.

---

## 4. Hypotheses and outcome vocabulary

The exact restricted cost `R`, within-arm gain `G`, paired differential `d_i`, and population estimand `delta` are defined in `ANALYSIS_PLAN_V0.2_CANDIDATE_FOR_LOCK.md`.

### Positive direction

`delta > 0`: ALIASED history produces greater later transfer than SEPARABLE history.

The confirmatory scientific status is named **`ALIASED_TRANSFER_ADVANTAGE`** when the preregistered inferential and SESOI rules are met.

### Negative direction

`delta < 0`: SEPARABLE history produces greater later transfer.

The primary status is **`SEPARABLE_TRANSFER_ADVANTAGE`** when the preregistered rules are met. This is initially a **regime-level** result. It must not be described causally as “world identity/informative separation helps” until the mandatory `SHUFFLED_TAG` diagnostic separates context variability from context informativeness.

### Practical equivalence

The primary status **`PRACTICALLY_EQUIVALENT`** is available only when the 90% CI is entirely inside the signed SESOI region and the heavy-cap gate is not active.

### Unresolved

Any otherwise valid result that resolves neither a directional threshold nor practical equivalence is **`UNRESOLVED`** (or `UNRESOLVED_HEAVY_CAP` when heavy-cap restrictions apply).

---

## 5. Signed SESOI

The author signs before calibration:

> A scientifically interesting positive result requires the **observed ALIASED multiplicative history-to-transfer gain** to be at least 20% larger than the corresponding SEPARABLE gain.

Therefore:

`delta_SESOI = ln(1.20) = 0.1823215567939546`.

The reference quantity is the ratio of the two arms' multiplicative reductions in `1 + restricted optimizer updates` from k=1 to k=6.

### SESOI interpretation fixed in v0.2

The SESOI is a **point-estimate licensing threshold**, not a confidence-bound threshold. A directional status additionally requires the preregistered 95% CI to exclude zero in the corresponding direction.

Thus v0.2 distinguishes:

- evidence for direction: CI-based;
- practical magnitude licensing: point-estimate-based.

It does **not** claim to prove that the true population effect exceeds `delta_SESOI`.

No pilot mean may alter the SESOI.

---

## 6. Learner and provenance

One small transformer is used throughout.

### 6.1 Preflight provenance gate

Before any calibration trajectory:

`MODEL_CONFIG_REF = <exact Level 0 paper-mainline config path>@<SHA256>`

must resolve mechanically from the project repository.

If an exact recoverable source does not exist, terminal=`BLOCKED_CONFIG_PROVENANCE`. Hyperparameters must not be reconstructed from memory, prose, or approximate companion settings under v0.2.

### 6.2 Inherited parameters

Architecture, initialization family, optimizer family, batch size, base LR, weight decay, dtype, gradient accumulation/drop-last behavior, and trajectory-relevant transformer settings inherit the exact locked Level 0 config except the explicit deviations below.

### 6.3 Allowed deviations only

1. numeric vocabulary/output range enlarged to the selected world scale;
2. one fixed non-trainable context vector is prepended as input position 0;
3. positional/max-position handling changes only as specified in the implementation contract;
4. LR is constant at the inherited base value: no warmup and no schedule;
5. optimizer state resets at each history boundary and every probe;
6. data generation, fixed history budget, and probe stopping semantics follow v0.2.
7. execution is pinned to a single intra-op and single inter-op thread, overriding the inherited Level 0 runtime thread pinning (16 intra-op / 32 inter-op); the inherited `configure_canonical_torch_runtime()` is not invoked. This is a runtime/determinism setting, not an architecture or optimizer change; single-thread execution is required for the bit-reproducibility that the k=1 identity gate and the D0/D1 replays depend on (implementation contract §17).

No architecture search, head/layer/width change, optimizer-family change, LR/WD sweep, curriculum search, per-arm tuning, or post-calibration hyperparameter change is authorized.

---

## 7. World family

For scale `M`:

`a,b in {0,...,M-1}`

and world modulus `n` returns

`c=(a+b) mod n`.

All worlds share one ambient numeric vocabulary; `n` is never exposed as a token/scalar.

Authorized scale selector only:

- first candidate `M=96`, module pool `131..138`;
- one permitted escalation `M=128`, module pool `176..183`.

No other scale is authorized.

For M=96, pairwise disagreement probabilities over uniform operand pairs lie in the locked narrow band approximately `[0.1553,0.1986]`; for M=128 approximately `[0.1604,0.1929]`. Exact counts are acceptance-tested in the implementation contract.

Dose and latent identifiability are coupled in this family. v0.2 does not interpret a dose-response curve.

The single-change-point character of this substrate is intentional. The P0/P2 headroom gates exist to prevent a trivial transfer floor from being misreported as a scientific null.

---

## 8. World allocation per replicate

Each seed deterministically permutes the eight locked module values:

- item 0 -> reserved fresh world `C`;
- items 1..6 -> `H1..H6` in order;
- item 7 -> unused spare.

`C` is reserved before history training and is never used by the main history trajectory.

The same C is probed after k=`1,2,4,6` within a replicate. Every probe is a disposable fork.

ALIASED and SEPARABLE receive the same allocation/order for the seed.

---

## 9. Context-code and arm semantics

### 9.1 Fixed non-trainable codes

Each world receives a deterministic seed-specific fixed vector `z_world` of dimension `d_model`. The vector is not looked up from a trainable per-world table and creates no world-specific parameters.

Context-vector scale is frozen from the **initial** numeric-token embedding norm and is never dynamically rescaled. Token-embedding norm drift is logged at history boundaries as a diagnostic only.

### 9.2 SEPARABLE

Hj uses `z_Hj`.

### 9.3 ALIASED

H1 uses `z_H1`; H2..H6 also use `z_H1`.

No other learner-visible field identifies world index, modulus, arm, or boundary.

### 9.4 k=1 identity

Through H1, ALIASED and SEPARABLE are exactly identical. Under the locked deterministic execution contract, H1 checkpoints and the full k=1 C probe must match bit-for-bit. Any mismatch is an invalidation, not sampling noise.

### 9.5 Fresh C

Both primary arms probe C using the same novel fixed code `z_C`.

SEPARABLE has experienced context-code variation during history; ALIASED has not. This difference is part of the primary regime. It is not erased by interpretation.

Because this leaves a possible pure input-perturbation contribution to non-positive primary outcomes, v0.2 pre-locks the `SHUFFLED_TAG` diagnostic and makes it mandatory after any valid primary result other than `ALIASED_TRANSFER_ADVANTAGE`.

---

## 10. Sequential history semantics

History worlds are **contiguous blocks**, never interleaved.

For each H1..H6:

1. create a fresh optimizer around current weights;
2. train exactly `B_history` optimizer updates on that world;
3. never early-stop history;
4. discard optimizer state at the boundary;
5. carry model weights only into the next block.

Both arms receive identical world/example/update counts. `B_history` is mechanically derived by the locked calibration protocol.

No replay, ledger, EWC penalty, prior-world minibatch, task head, or explicit world classifier is permitted.

---

## 11. Fresh-C fork probes

After history positions `k=1,2,4,6`:

1. hash main checkpoint;
2. clone/reload to a separate probe model;
3. create a fresh optimizer;
4. train only on reserved C training pairs with `z_C`;
5. evaluate held-out C at step 0 and every 100 updates;
6. stop at locked `tau`;
7. finalize immutable probe artifacts;
8. discard probe branch;
9. re-hash main checkpoint and require equality;
10. continue history only from untouched main checkpoint.

Probe results cannot feed the main learner.

---

## 12. Competence and raw event time

Competence requires held-out accuracy `>=0.95` at three consecutive scheduled evaluations.

Evaluations: step `0,100,200,...`.

`T` is the first evaluation step of the earliest fully observed qualifying run.

If no qualifying run begins by `tau-200`, raw T is right-censored beyond the cap. The primary restricted-cost functional remains defined.

The same criterion is used at every stage.

---

## 13. Primary and secondary endpoints

### Primary

Fresh-C restricted adaptation cost after k=1 and k=6; paired differential `delta` across ALIASED and SEPARABLE.

### Secondary non-decisive

- C cost k=2,4;
- H1 reacquisition after k=6;
- history held-out accuracy at block ends;
- step-0 C accuracy;
- cap fraction per arm×k;
- context-norm drift ratio.

H1 reacquisition is not evidence of absorption/meta-structure by itself; retention is an alternative.

---

## 14. Development -> confirmation workflow

1. P-1 exact `MODEL_CONFIG_REF` provenance gate;
2. pre-calibration scientific/code hash root;
3. P0 single-world headroom calibration;
4. P1 mechanical derivation of M/B_history/tau;
5. P1.5 duplicated full H1 + k1 C deterministic replay;
6. P2 six-seed paired endpoint/headroom pilot;
7. P3 variance-only dual-target power calculation;
8. final confirmatory config/seed/allocation/analysis root lock;
9. ALIASED + SEPARABLE confirmatory run;
10. locked primary analysis and heavy-cap gate;
11. if primary valid and not `ALIASED_TRANSFER_ADVANTAGE`, mandatory pre-locked `SHUFFLED_TAG` run on the same N seeds;
12. only separately locked structural/mechanistic follow-ups thereafter.

Development and confirmatory seed namespaces are disjoint.

Pilot means cannot alter SESOI, arms, learner, analysis, module pools, or interpretation.

---

## 15. Confirmatory N

Independent N = paired replicate seeds.

N is mechanically derived from the six-seed pilot variance only. v0.2 prices both:

- 90% power for directional superiority against zero at absolute effect `delta_SESOI`;
- 90% power for TOST practical equivalence when true `delta=0` with margin `±delta_SESOI`.

`N=max(20,N_superiority,N_equivalence)`; if N>128, terminal=`BLOCKED_POWER`.

No observed pilot mean enters the N calculation.

---

## 16. Heavy-cap rule

After valid confirmation, report cap fraction at k=6 for each primary arm.

Define `HEAVY_CAP=true` if **more than 10%** of paired-seed probes in either ALIASED,k6 or SEPARABLE,k6 are capped at `tau`.

The primary estimand remains the restricted-cost `delta`. Under HEAVY_CAP:

- Student-t intervals are reported but cannot alone license a directional status;
- a preregistered conservative paired sign gate must also support the direction;
- `PRACTICALLY_EQUIVALENT` is unavailable;
- if no directional status passes both ordinary and sign gates, status=`UNRESOLVED_HEAVY_CAP`;
- no uncapped magnitude extrapolation is allowed.

Exact sign-gate rules are fixed in the analysis plan.

---

## 17. Mandatory conditional SHUFFLED_TAG diagnostic

If primary confirmation is valid and the primary status is anything except `ALIASED_TRANSFER_ADVANTAGE` (including heavy-cap bounded variants), run `SHUFFLED_TAG` using:

- the same locked N confirmatory seeds;
- identical initialization/world allocation/data/batch order/B_history/tau;
- the same fixed six history context vectors;
- context code assigned at training-example level independently of world/operand/target, with per-block balancing specified in the diagnostic protocol;
- only the k=6 C probe required.

This diagnostic is pre-locked before confirmatory data exist. It cannot change the primary category; it only constrains the causal wording of non-positive outcomes. In particular, SHUFFLED_TAG does not perfectly isolate identity from temporal code stability: it is an uninformative per-example variability control, whereas SEPARABLE uses stable per-world informative codes.

---

## 18. Structural null fence

`ALIASED_TRANSFER_ADVANTAGE` is a regime-level transfer result. It cannot be rewritten as evidence that the modular law was learned.

Any structural claim requires a separately preregistered null/follow-up that removes the common reusable modular structure while preserving the relevant nuisance properties. The exact scrambled-family generator is not invented inside v0.2 after seeing a primary result.

---

## 19. Interpretation fence

Permitted positive wording:

> In this locked sequential modular cell, history with world identity unavailable at learner input produced a larger reduction in restricted in-weights adaptation cost to a seventh unseen world than matched history with explicit non-trainable world separation.

Before SHUFFLED_TAG resolves a non-positive result, negative wording is restricted to:

> The SEPARABLE regime transferred better / the primary regimes were practically equivalent / unresolved under the locked restricted-cost analysis.

It is forbidden to infer from the primary alone that:

- contradiction alone caused abstraction;
- explicit world information itself caused a negative advantage;
- context variability alone caused a negative advantage;
- the learner discovered group theory;
- a balcony was demonstrated;
- manufactured experience was established;
- results transfer to language/Sanskrit;
- the mechanism is known.

---

## 20. Candidate-for-lock condition

v0.2 may become locked only after external review finds no unresolved BLOCKER/MAJOR and the pre-calibration lock manifest can be populated, including exact `MODEL_CONFIG_REF`, implementation hashes, deterministic tests, and pre-locked SHUFFLED_TAG implementation/analysis.
