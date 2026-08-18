# Confirmatory analysis plan v0.2 — candidate for lock

**Status:** CANDIDATE FOR LOCK — implementation must be hash-locked before confirmation.

---

## 1. Independent unit

Independent unit = one replicate seed with matched ALIASED and SEPARABLE arms.

k=1,2,4,6 probes are repeated measurements inside a seed, not independent observations.

Primary uses k=1 and k=6 only.

---

## 2. Raw event time

`T_i,a,k` = optimizer update count at first evaluation beginning earliest fully observed run of 3 consecutive held-out accuracies >=0.95.

If no qualifying run is fully observed by tau: raw T is right-censored beyond cap; `capped=true`.

T may equal 0.

---

## 3. Restricted adaptation cost

Define

`C_i,a,k = 1 + min(T_i,a,k, tau)`

where capped raw events use tau **only inside this explicitly defined restricted functional**, not as an uncensored event-time imputation.

`R_i,a,k = ln(C_i,a,k)`.

R is always defined and bounded.

Interpretation fence: R saturates at ln(1+tau), so it does not identify uncapped severity beyond tau. Extreme loss of plasticity can therefore have understated magnitude. This is disclosed for every result.

---

## 4. Within-arm history-to-transfer gain

`G_i,a = R_i,a,1 - R_i,a,6`.

Positive G = C became cheaper after six worlds than after one.

`exp(G_i,a)=C_i,a,1/C_i,a,6`.

---

## 5. Primary paired differential

`d_i = G_i,ALIASED - G_i,SEPARABLE`.

Estimator:

`delta_hat = mean(d_i)`.

Because k1 arms are exactly identical in valid runs:

`d_i = R_i,SEPARABLE,6 - R_i,ALIASED,6`.

The full difference-in-differences form remains canonical because k1 equality is an integrity gate.

Positive delta -> ALIASED cheaper at k6 relative to matched baseline.

---

## 6. SESOI

`Delta = ln(1.20)=0.1823215567939546`.

`exp(delta)=1.20` means ALIASED's multiplicative k1->k6 transfer gain is 20% larger than SEPARABLE's.

v0.2 fixes Delta as a **point-estimate licensing threshold**. It is not interpreted as a lower confidence bound on the unknown effect.

---

## 7. Ordinary primary intervals

For N valid paired seeds:

- sample SD s_d;
- 95% two-sided Student-t CI for delta;
- 90% two-sided Student-t CI for equivalence;
- paired t-test p-value versus zero as supplemental output only.

No mixed model controls the primary decision.

---

## 8. Practical-equivalence rule

Equivalence region `[-Delta,+Delta]`.

If no heavy-cap gate is active and the entire 90% CI lies inside this region, status may be `PRACTICALLY_EQUIVALENT` subject to decision ordering.

The power protocol explicitly prices 90% equivalence power at true delta=0.

---

## 9. Confirmatory heavy-cap gate

For primary arms at k=6 compute:

`f_cap(a)=# capped probes / N`.

`HEAVY_CAP=true` iff `f_cap(ALIASED)>0.10` OR `f_cap(SEPARABLE)>0.10`.

### 9.1 Consequences

If HEAVY_CAP=false: ordinary decision rules in section 10 apply.

If HEAVY_CAP=true:

- ordinary t CIs and delta_hat remain reported for the restricted-cost estimand;
- they cannot alone license a directional status;
- `PRACTICALLY_EQUIVALENT` is forbidden;
- a conservative paired sign gate must agree with the proposed direction;
- otherwise status=`UNRESOLVED_HEAVY_CAP`;
- no uncapped magnitude extrapolation is allowed.

### 9.2 Conservative sign gate

Let `q_i = R_i,SEPARABLE,6 - R_i,ALIASED,6 = d_i` in valid runs.

For positive direction:

- successes `s_plus = # {q_i > 0}`;
- denominator is **N**, not number of non-ties; q_i<=0, including ties, count as failures;
- compute one-sided 95% Clopper-Pearson lower confidence bound `L_plus` for Bernoulli success probability;
- `SIGN_POS_PASS` iff `L_plus > 0.5`.

For negative direction:

- successes `s_minus = # {q_i < 0}`;
- q_i>=0 including ties are failures;
- one-sided 95% CP lower bound `L_minus`;
- `SIGN_NEG_PASS` iff `L_minus > 0.5`.

Canonical implementation:

- if s=0 -> lower bound 0;
- else `L = beta_ppf(0.05, s, N-s+1)` using locked SciPy version.

This supplement is intentionally conservative under ceiling ties.

---

## 10. Primary decision ordering

Apply validity gates first, then heavy-cap gate, then:

### 10.1 ALIASED_TRANSFER_ADVANTAGE

If HEAVY_CAP=false, require:

1. lower 95% CI >0;
2. delta_hat >= +Delta.

If HEAVY_CAP=true, require both above **and** `SIGN_POS_PASS`; status is then `ALIASED_TRANSFER_ADVANTAGE_BOUNDED` to mark ceiling-limited interpretation.

### 10.2 SEPARABLE_TRANSFER_ADVANTAGE

If HEAVY_CAP=false, require:

1. upper 95% CI <0;
2. delta_hat <= -Delta.

If HEAVY_CAP=true, require both above **and** `SIGN_NEG_PASS`; status=`SEPARABLE_TRANSFER_ADVANTAGE_BOUNDED`.

Both negative statuses remain **regime-level** until mandatory SHUFFLED_TAG decomposition is complete.

### 10.3 PRACTICALLY_EQUIVALENT

Only if HEAVY_CAP=false and entire 90% CI is inside `[-Delta,+Delta]`.

### 10.4 UNRESOLVED_HEAVY_CAP

HEAVY_CAP=true and neither bounded directional status passes.

### 10.5 UNRESOLVED

Any other valid result.

No post-hoc sample increase or k selection.

---

## 11. k1 integrity analysis

Before aggregate primary analysis:

- compare H1 checkpoint hashes per seed;
- compare full k1 C trajectory hashes/log sequence;
- require exact T/cap equality.

Any mismatch=`INVALID_K1_ARM_DIVERGENCE`; do not drop seed and continue.

---

## 12. Secondary curve shape

At k=1,2,4,6 by arm report:

- mean/median R;
- paired arm difference;
- cap fraction;
- raw T distribution where observed;
- step-0 accuracy.

Plots/descriptive fits cannot replace primary k1->k6 decision.

---

## 13. H1 reacquisition

After k6, compute same restricted cost for H1 reacquisition.

Report paired difference and cap summaries descriptively. Do not interpret as absorption/meta-representation without separate evidence.

---

## 14. Mandatory SHUFFLED_TAG analysis trigger

If primary confirmation is valid and primary status is not `ALIASED_TRANSFER_ADVANTAGE` or `ALIASED_TRANSFER_ADVANTAGE_BOUNDED`, execute the already locked SHUFFLED_TAG protocol on same N seeds.

It does not change the primary category.

Define at k6:

`V_i = R_i,ALIASED,6 - R_i,SHUFFLED,6`

Positive V means exposure to non-informative context variability made novel z_C cheaper than constant-code ALIASED history; this is the preregistered **input-variability / perturbation-shock contrast**.

`I_i = R_i,SHUFFLED,6 - R_i,SEPARABLE,6`

Positive I means the **stable world-informative context regime** improved C adaptation beyond per-example non-informative code variability. This is a residual regime contrast, not a pure causal effect of identity, because temporal code stability cannot be matched while also removing world information in this sequential construction.

Algebraically:

`V_i + I_i = R_ALIAS,6 - R_SEP,6 = -d_i`.

### 14.1 Diagnostic intervals

For mean(V) and mean(I), report two-sided **97.5% paired t CIs** (Bonferroni familywise alpha <=.05 across the two preplanned contrasts).

If >10% of probes are capped in any arm entering a contrast, additionally apply the same conservative sign gate for that contrast; no component claim is licensed unless direction agrees under the sign gate.

### 14.2 Predeclared interpretation patterns

- V positive/resolved, I not positive/resolved -> primary non-positive result may be substantially explained by context-variability/novel-code perturbation; do not claim informative separation advantage.
- I positive/resolved, V not positive/resolved -> evidence that the stable world-informative coding regime contributes beyond per-example code variability; identity and temporal stability are not separately identified.
- both positive/resolved -> mixed contribution.
- neither resolved or opposite signs -> decomposition unresolved; primary regime statement only.

“Resolved positive” means the relevant 97.5% CI lower bound >0 and, under diagnostic heavy cap, sign gate also passes.

No SESOI threshold is imposed on these mechanism-adjacent diagnostics.

---

## 15. Structural null fence

A primary ALIASED advantage does not establish reusable modular structure. Structural claims require separately preregistered scrambled-family/re-encoding/mechanistic work.

---

## 16. Fixed tables/plots

Primary report must include:

1. validity/integrity table;
2. delta_hat, 95% CI, 90% CI, SESOI lines, primary status;
3. k6 cap fractions and HEAVY_CAP flag;
4. sign-gate counts/lower bounds when activated;
5. per-arm R summaries k=1,2,4,6;
6. paired trajectory plot;
7. H1 reacquisition;
8. context-norm drift summary;
9. config/provenance hashes.

If SHUFFLED_TAG triggers, append:

10. R_SHUFFLED,k6 summary/cap fraction;
11. V/I estimates with 97.5% CIs and sign gates if applicable;
12. diagnostic interpretation label from section 14.2.

No plot-based decision.
