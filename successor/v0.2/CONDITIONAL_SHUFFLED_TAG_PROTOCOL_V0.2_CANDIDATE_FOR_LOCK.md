# Conditional SHUFFLED_TAG protocol v0.2 — candidate for lock

**Status:** PRE-LOCKED CONDITIONAL DIAGNOSTIC — implementation and analysis must be hash-committed before primary confirmation. Execution is outcome-conditional.

---

## 1. Why this arm exists

At k6 the primary comparison can contain two separable components:

1. context-input **variability exposure**: ALIASED history uses one context direction; SEPARABLE history sees varying context directions;
2. context **informativeness**: in SEPARABLE, code identifies world; in ALIASED it does not.

A novel z_C can therefore impose an input-perturbation shock on ALIASED independent of world modelling. This nuisance is conservative to a positive ALIASED advantage but can explain a negative/equivalent/unresolved primary result.

SHUFFLED_TAG supplies context variability without world information.

---

## 2. Trigger

Run SHUFFLED_TAG iff:

- primary confirmation is valid; and
- primary status is anything except `ALIASED_TRANSFER_ADVANTAGE` or `ALIASED_TRANSFER_ADVANTAGE_BOUNDED`.

This includes:

- SEPARABLE_TRANSFER_ADVANTAGE;
- SEPARABLE_TRANSFER_ADVANTAGE_BOUNDED;
- PRACTICALLY_EQUIVALENT;
- UNRESOLVED;
- UNRESOLVED_HEAVY_CAP.

Invalid/incomplete primary confirmation does not trigger the diagnostic.

The trigger is automatic; author discretion after seeing the result is forbidden.

---

## 3. Replicates and pairing

Use exactly the same locked N confirmatory replicate seeds.

For each seed reuse/reconstruct exactly:

- initial model parameters from same model-init seed;
- C/H1..H6 allocation;
- train/held-out split;
- batch-order sequence;
- B_history;
- tau;
- context vector set `{z_H1,...,z_H6,z_C}`;
- optimizer/hyperparameters/runtime.

Only history context assignment differs.

No new N, power calculation, seed replacement, or tuning.

---

## 4. History context assignment

For every training-example presentation in each history block, choose a code index from `{1,...,6}` using the locked `shuffled-tag` RNG, **independently of current world, operands, and target**.

A fixed or blockwise world->code permutation is invalid.

### 4.1 Balanced per-block schedule

To match code-frequency marginals and guarantee empirical world/code independence as closely as possible:

For each history block, before training:

1. let `P` be the number of individual example presentations implied by B_history, batch size, and inherited final-batch behavior;
2. construct a multiset of code indices 1..6 with counts differing by at most one and total P;
3. choose the `P mod 6` code indices receiving one extra presentation from a seed-specific subset that is fixed for the **entire replicate**, not separately by world;
4. therefore construct the **same code-count vector in every history block**;
5. independently pseudorandomize the within-block ordering of that multiset using `(replicate, history_position)` in the locked `shuffled-tag` namespace;
6. consume one code index per training-example presentation in exact batch order.

Thus empirical code-count marginals are identical in every history world (so code frequency does not identify world), while individual example assignments remain unrelated to world/operand/target.

Record schedule root/hash before training each diagnostic seed.

---

## 5. Training/probe scope

Run all six history worlds sequentially for exactly B_history updates each, with normal optimizer resets.

Only one fresh-C fork after k=6 is required.

C uses the same novel `z_C` as primary arms.

No k1/k2/k4 probe and no H1 reacquisition are required for this diagnostic unless emitted for engineering audit; they cannot affect interpretation.

---

## 6. Primary diagnostic contrasts

Using restricted k6 C cost R:

`V_i = R_ALIAS,6 - R_SHUFFLED,6`.

Positive V = history exposure to varying but uninformative context directions reduces later novel-code shock relative to constant-code ALIASED history.

`I_i = R_SHUFFLED,6 - R_SEPARABLE,6`.

Positive I = the **stable world-informative coding regime** contributes beyond the per-example uninformative variability regime. Because SHUFFLED and SEPARABLE cannot simultaneously match temporal code stability while making code uninformative, I is not described as a pure one-factor effect of identity.

The primary regime differential decomposes as:

`V_i + I_i = R_ALIAS,6 - R_SEP,6 = -d_i`.

---

## 7. Diagnostic inference

Report mean V and I with preplanned two-sided 97.5% paired t CIs (Bonferroni familywise alpha <=.05 across two contrasts).

If cap fraction >0.10 in any arm used by a contrast, apply the conservative sign gate from the main analysis plan to that contrast; a resolved component claim requires both interval direction and sign gate.

No SESOI threshold and no primary-category revision.

---

## 8. Allowed wording

If V resolved positive and I not resolved positive:

> The non-positive primary regime difference is consistent with a substantial context-variability / novel-code perturbation component; informative world separation itself was not isolated as the advantage.

If I resolved positive and V not resolved positive:

> The stable world-informative context regime contributed to lower fresh-world restricted adaptation cost beyond the per-example uninformative context-variation regime; the contrast does not isolate identity from temporal code stability.

If both resolved positive:

> Both context-variability exposure and world-code informativeness contributed to the primary regime difference.

Otherwise:

> The SHUFFLED_TAG decomposition did not resolve the nuisance components; only the original primary regime-level result is licensed.

This diagnostic cannot turn a non-positive primary result into a positive ALIASED result or vice versa.
