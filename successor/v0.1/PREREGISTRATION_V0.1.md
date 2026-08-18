# Preregistration v0.1 — Productive forced sharing in sequential modular worlds

**Status:** DRAFT FOR EXTERNAL REVIEW — NOT LOCKED  
**Programme:** `philosophia`, separately chartered successor cell  
**Primary unit:** paired replicate seed  
**Primary arms:** `ALIASED`, `SEPARABLE`  
**Primary endpoints:** fresh-world probe after history length `k = 1` and `k = 6`  
**Secondary endpoints:** fresh-world probes at `k = 2, 4`; reacquisition of history world 1 after `k = 6`  
**Signed SESOI:** `ln(1.20) = 0.1823215567939546`

---

## 1. Scientific scope

This experiment tests one narrow proxy:

> **Does forced non-separability of one latent parameter (the modulus) across six sequential worlds reduce the in-weights adaptation cost of that latent on a seventh unseen world more than the same sequence when world identity is available at input?**

It does **not** claim to isolate an abstract causal factor called “contradiction” while holding world identifiability fixed. That isolation is logically unavailable in this construction: when the same observable input maps to different targets across worlds, the input is insufficient to identify the world; making the mapping simultaneously non-contradictory requires some input information that separates the worlds.

The manipulation is therefore stated causally as:

- `ALIASED`: world identity is unavailable from the learner input during history; the same learner input may receive incompatible targets in different sequential blocks.
- `SEPARABLE`: world identity is available through a fixed non-trainable context code; the same worlds can be represented as distinct input-conditioned functions.

A positive result is evidence only that this **forced-sharing regime** produced greater later transfer in this bounded substrate. It is not by itself evidence of the full `philosophia` programme claim, a general `balcony`, semantics, language learning, or manufactured experience.

---

## 2. Rationale and relation to the prior programme

The earlier programme requires candidate experience to do work beyond the description in which it was found: in particular, to reduce future work. This cell operationalizes only that one obligation.

The prior stopped-open route remains untouched. This is a new successor cell because the earlier ACTIVE/YOKED comparison never ran and later development branches stopped at their own gates. No result here may be retroactively promoted into an earlier canonical claim.

The present cell also deliberately abandons the impossible requirement that a single feed-forward parameter state, with no world signal, answer two contradictory modular worlds simultaneously. What may be shared in weights is a reusable adaptation structure; the currently active world remains a state reached by adaptation.

---

## 3. Primary scientific question

Let a learner traverse six worlds from a family of modular-addition tasks. Compare two histories that are identical in:

- model initialization;
- ordered modulus sequence;
- operand/target examples;
- train/held-out split;
- batch order;
- optimizer family and hyperparameters;
- number of updates per history world;
- optimizer resets at world boundaries;
- fresh held-out world `C`;
- probe procedure and probe budget.

They differ only in whether the context input carries world identity after world 1.

The primary question is whether the reduction in fresh-`C` acquisition cost from `k=1` to `k=6` is larger in `ALIASED` than in `SEPARABLE`.

---

## 4. Hypotheses

Define the restricted log adaptation cost `R`, history gain `G`, and paired differential `delta` exactly as in `ANALYSIS_PLAN_V0.1.md`.

### H0 / unresolved reference

`delta = 0`: the two history regimes produce the same average reduction in fresh-world restricted adaptation cost.

### Positive scientific direction

`delta > 0`: forced non-separability produces greater later transfer than explicit world separation.

A result is large enough to license the next scientific stage only if its point estimate reaches the signed SESOI and its 95% confidence interval excludes zero in the positive direction.

### Negative scientific direction

`delta < 0`: explicit world separation produces greater later transfer; aliasing/conflict is a cost rather than productive pressure in this cell.

The negative direction is a substantive outcome, not a failed experiment.

### Practical-null region

Effects smaller than the signed SESOI in either direction are treated as scientifically small for this cell when the preregistered equivalence criterion is met.

---

## 5. Signed SESOI

The author signs the following operational definition before calibration:

> A scientifically interesting productive effect requires ALIASED to have at least a **20% larger multiplicative history-to-transfer gain** than SEPARABLE.

Therefore:

`delta_SESOI = ln(1.20) = 0.1823215567939546`.

The reference quantity is the ratio of the two arms’ multiplicative reductions in `1 + restricted optimizer updates` from the `k=1` fresh-`C` probe to the `k=6` fresh-`C` probe. This removes the ambiguity “20% of what?”.

No pilot mean may alter this SESOI.

---

## 6. Learner

One small transformer is used throughout.

### Frozen provenance rule

`MODEL_CONFIG_REF` must be resolved **before calibration** to the exact Level 0 paper-mainline repository configuration and its content hash. The uploaded public materials do not expose the numerical values, so this preregistration does not invent them.

The architecture, initialization family, optimizer family, batch size, base learning rate, and weight decay are inherited verbatim unless an exception appears below.

### Allowed, declared deviations from Level 0

Only these changes are permitted:

1. numeric vocabulary/output range enlarged to the selected ambient modular world;
2. one fixed non-trainable context vector is prepended as an input position;
3. no LR warmup or LR schedule in this cell; learning rate is constant at the inherited locked base value;
4. optimizer state is reset at every history-world boundary and at every forked probe;
5. training data and stopping semantics are those in this preregistration.

No architecture search, hidden-width change, layer/head change, optimizer-family change, LR sweep, weight-decay sweep, curriculum search, or per-arm tuning is allowed under v0.1.

---

## 7. World family

For scale `M`, operands are

`a,b in {0,...,M-1}`

and a world with modulus `n` returns

`c = (a + b) mod n`.

All worlds in a locked run use one common ambient numeric vocabulary. The modulus itself is never presented as a scalar or token to the learner.

The scale and module pool are selected only by the preregistered calibration procedure:

- first candidate: `M = 96`, pool `n = 131..138`;
- one permitted escalation for transfer-floor only: `M = 128`, pool `n = 176..183`.

No other scale is authorized by v0.1.

For `M=96`, the exact uniform-input disagreement probabilities `P[(a+b mod n) != (a+b mod n')]` for a pair `n<n'` equal `P(a+b >= n)` and range from `0.1985677083` at threshold 131 to `0.1552734375` at threshold 138. The corresponding `M=128` pool ranges from `0.19287109375` at 176 to `0.160400390625` at 183.

Dose and latent identifiability are coupled in this family; v0.1 therefore does **not** interpret a dose-response curve. It uses one narrow dose band.

---

## 8. World allocation inside one replicate

Each replicate seed deterministically generates a permutation of the eight locked module values.

- permutation item 0: reserved fresh world `C`;
- items 1..6: ordered history worlds `H1..H6`;
- item 7: unused spare.

`C` is reserved before any history training. It is never used by the main history trajectory.

The same `C` is probed after `k = 1, 2, 4, 6` history worlds. Every probe is a disposable fork; the main history trajectory never continues from a `C`-trained branch.

Both arms use exactly the same allocation and order for a given replicate seed.

---

## 9. Arm semantics

### 9.1 Fixed context codes

Each world receives a deterministic, seed-specific **non-trainable** context vector generated as specified in `IMPLEMENTATION_CONTRACT_V0.1.md`. A context code adds no per-world trainable parameter row.

### 9.2 `SEPARABLE`

History world `Hj` is presented with its own fixed context vector `z_Hj`.

### 9.3 `ALIASED`

History world `H1` uses `z_H1`; every later history world `H2..H6` also uses that same `z_H1`.

Thus world identity after the first block is unavailable from the context input, while the numerical operands are drawn from the same common domain.

### 9.4 Built-in k=1 integrity property

At history length `k=1`, the two arms are byte-identical by construction: same model initialization, same context vector `z_H1`, same examples, same order, same optimizer, same updates.

Under the deterministic execution contract, the world-1 checkpoint hashes and the entire `C` probe trajectory at `k=1` must match exactly. Failure is an implementation/platform invalidation, not a scientific outcome.

### 9.5 Fresh C

Both arms probe `C` with the same new fixed code `z_C`, which was unseen in history.

This is intentionally a regime comparison, not a pure “contradiction-only” manipulation: `SEPARABLE` has experienced informative code variation during history; `ALIASED` has not. That fact is part of the scientific scope and may not be erased from interpretation.

---

## 10. Sequential history semantics

History worlds are trained in **contiguous sequential blocks**, never interleaved.

For each of `H1..H6`:

1. create a fresh optimizer around the current model weights;
2. train exactly `B_history` optimizer updates on that world’s training split;
3. do not early-stop even if competence is reached;
4. discard optimizer state at the boundary;
5. carry model weights only into the next history world.

The same fixed number of history updates is used in both arms. Thus neither arm can gain extra pre-`C` compute because one history world was harder.

`B_history` is not hand-tuned; it is mechanically derived by `CALIBRATION_AND_POWER_PROTOCOL_V0.1.md`.

No replay, ledger, prior-world minibatch, EWC penalty, task head, or explicit world classifier is allowed.

---

## 11. Fresh-C fork probes

After history worlds `k = 1, 2, 4, 6`:

1. hash and clone the current model checkpoint;
2. create a new optimizer with the locked constant hyperparameters and empty state;
3. train only on `C`’s training split using `z_C`;
4. evaluate on `C` held-out pairs at step 0 and every 100 optimizer updates;
5. stop the fork at the locked probe cap `tau`;
6. write probe artifacts;
7. destroy/discard the fork;
8. verify the main checkpoint hash is unchanged;
9. continue the main history trajectory from the untouched checkpoint.

The main learner never receives information from a `C` probe.

---

## 12. Competence criterion

A probe reaches competence when held-out accuracy is at least `0.95` at **three consecutive scheduled evaluations**.

`T` is the update count at the first evaluation of the earliest qualifying three-evaluation run.

- evaluations occur at step 0, 100, 200, ...;
- a qualifying run must be fully observable within the probe cap;
- if no qualifying run begins by `tau - 200`, the raw event time is right-censored beyond the cap;
- the primary estimand uses the preregistered restricted cost and therefore remains defined.

The same criterion is used in calibration, power pilot, confirmatory probes, and the secondary reacquisition probe.

---

## 13. Primary and secondary endpoints

### Primary

Fresh-`C` restricted adaptation cost after `k=1` and `k=6`; paired differential `delta` across arms.

### Secondary, non-decisive

- fresh-`C` cost at `k=2` and `k=4` to show curve shape;
- reacquisition cost of `H1` from the `k=6` checkpoint, using `z_H1` in both arms;
- end-of-block held-out history accuracy;
- frequency of probes reaching the cap;
- step-0 `C` held-out accuracy.

Reacquisition is not accepted as proof of a meta-representation because simple retention can also make `H1` cheap.

---

## 14. Development and confirmatory separation

The workflow is fixed as:

1. **pre-calibration scientific/implementation lock**;
2. P0 single-world calibration;
3. mechanical derivation of selected `M`, `B_history`, and `tau`;
4. paired endpoint power/headroom pilot using development-only seeds;
5. mechanical derivation of confirmatory `N` from the signed SESOI and pilot variance only;
6. confirmatory config, seed list, runner, analysis, and input manifests hash-locked;
7. confirmatory run;
8. preregistered analysis;
9. only if licensed, separately governed diagnostics/follow-up.

Development seeds and confirmatory seeds are disjoint namespaces.

Pilot outcome means may not be used to alter the SESOI, arms, scale rule, analysis rule, learner, or scientific claim.

---

## 15. Confirmatory N

The number of independent units is the number of paired replicate seeds, not the number of probes.

`N` is calculated mechanically after the 6-seed paired power pilot using only the upper preregistered variance bound and `delta_SESOI`; see the calibration protocol.

- minimum confirmatory `N = 20` paired seeds;
- maximum authorized `N = 128` paired seeds;
- if the calculated requirement exceeds 128, terminal = `BLOCKED_POWER` and no underpowered confirmatory run is authorized.

---

## 16. Statistical decision

The exact estimator, confidence intervals, equivalence rule, and signed decision categories are in `ANALYSIS_PLAN_V0.1.md` and are part of this preregistration.

The primary result cannot be rescued or vetoed by LLC, MDL, mechanistic interpretation, curve aesthetics, reacquisition, or post-hoc probes.

---

## 17. Conditional diagnostics

### 17.1 SHUFFLED-TAG diagnostic

Not part of the primary factorial. If run, context code is randomized **per training example**, independently of the current world, from the same fixed history-code set. A mere permutation of the mapping `world -> code` is forbidden because it preserves full world information.

This diagnostic asks whether context-vector variability itself, rather than world information, explains an effect.

### 17.2 Scrambled-family structural null

A positive primary result does **not** automatically establish structural transfer. A stronger structural interpretation requires a separately locked scrambled-family null that destroys the common modular rule while matching relevant marginals/conflict exposure.

The exact scrambled generator is intentionally **not invented post hoc inside v0.1**. `PRODUCTIVE_ALIASING_CANDIDATE` licenses the separate preregistration; it does not pre-earn its result.

---

## 18. Interpretation fence

Permitted positive wording is bounded to this form:

> In this sequential modular cell, forced non-separability across six history worlds produced a larger reduction in restricted in-weights adaptation cost to a seventh unseen world than explicit world separation.

Forbidden without later experiments:

- “the learner acquired general intelligence”;
- “experience was manufactured”;
- “the learner discovered the true group theory”;
- “contradiction alone caused abstraction”;
- “a balcony was demonstrated”;
- “the result transfers to language/Sanskrit”;
- “the mechanism is known”.

A negative result may state that explicit separation transferred better under the locked cell. An unresolved or inadmissible run may state only the registered boundary.

---

## 19. Pre-run unresolved repository reference

The only non-numerical item that must be filled before pre-calibration lock is:

`MODEL_CONFIG_REF = <exact Level 0 paper-mainline config path>@<content SHA256>`

This is a repository lookup, not a tuning decision. If no exact recoverable source exists, v0.1 cannot claim Level 0 inheritance and must be revised before any run.
