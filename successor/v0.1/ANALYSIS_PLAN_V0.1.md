# Confirmatory analysis plan v0.1

**Status:** DRAFT FOR EXTERNAL REVIEW — must be code-implemented and hash-locked before confirmation.

---

## 1. Independent unit and pairing

The independent unit is one replicate seed with two matched arms.

Probes at k=1,2,4,6 are repeated measurements inside the same seed and are **not** independent observations.

The primary analysis uses only k=1 and k=6.

---

## 2. Raw event time

For arm `a`, seed `i`, probe position `k`, let `T_i,a,k` be the optimizer update count at the first evaluation of the earliest run of three consecutive held-out accuracies >=0.95.

If no qualifying run is fully observed by the locked cap `tau`, raw `T` is missing/right-censored beyond the cap and `censored=true`.

Step-0 competence is allowed, so `T` may equal 0.

---

## 3. Restricted adaptation cost

Define

`C_i,a,k = 1 + min(T_i,a,k, tau)`

where censored values use the known restricted boundary `tau` **only inside this explicitly capped cost functional**, not as an imputed uncensored event time.

Then

`R_i,a,k = ln(C_i,a,k)`.

This makes the primary quantity always defined and permits T=0.

Interpretation fence: because `R` saturates at `ln(1+tau)`, it **understates the magnitude of extreme loss of plasticity**. If one arm repeatedly reaches the cap, the direction may remain informative but absolute effect magnitude beyond the cap is not identified.

---

## 4. Within-arm transfer gain

For each seed and arm:

`G_i,a = R_i,a,1 - R_i,a,6`.

Positive `G` means the six-world history made the fresh C cheaper relative to that arm’s own k=1 state.

Exponentiating:

`exp(G_i,a) = C_i,a,1 / C_i,a,6`.

This is the multiplicative reduction in `1 + restricted optimizer updates` from k=1 to k=6.

---

## 5. Primary paired differential

For each seed:

`d_i = G_i,ALIASED - G_i,SEPARABLE`.

Primary estimator:

`delta_hat = mean_i(d_i)`.

Equivalent ratio interpretation:

`exp(delta_hat)` estimates the geometric-scale ratio of the two arms’ multiplicative history gains.

Because k=1 arms are identical by construction, valid deterministic runs should have

`R_i,ALIASED,1 = R_i,SEPARABLE,1` exactly,

so algebraically the per-seed differential reduces to

`d_i = R_i,SEPARABLE,6 - R_i,ALIASED,6`.

The full difference-in-differences formula remains canonical because the exact k=1 equality is also an integrity check.

---

## 6. Signed SESOI

Signed before calibration:

`delta_SESOI = ln(1.20) = 0.1823215567939546`.

Meaning:

`exp(delta) = 1.20`

means the multiplicative transfer gain from k=1 to k=6 is 20% larger in ALIASED than in SEPARABLE.

Example: if SEPARABLE reduces restricted cost by a factor of 2.0 and ALIASED by 2.4, the effect equals the SESOI.

The symmetric negative SESOI is `-ln(1.20)`.

---

## 7. Primary confidence interval

Let valid paired confirmatory sample size be the locked N; otherwise the run is incomplete-invalid.

Compute sample SD `s_d` over `d_i`.

95% two-sided Student-t CI:

`delta_hat +/- t_ppf(0.975, N-1) * s_d/sqrt(N)`.

Report also the two-sided paired t-test p-value versus zero, but p-value alone never determines the scientific category.

No mixed model is used for the primary decision.

---

## 8. Practical-equivalence interval

For the TOST-style practical-null check, compute the 90% two-sided Student-t CI for `delta`.

The practical equivalence region is:

`[-delta_SESOI, +delta_SESOI]`.

If the entire 90% CI is inside this region, the result qualifies as `PRACTICALLY_NULL` unless a higher-priority terminal invalidation applies.

---

## 9. Preregistered decision ordering

Apply in this order after validity gates:

### 9.1 PRODUCTIVE_ALIASING_CANDIDATE

Require both:

1. lower bound of the 95% CI > 0; and
2. `delta_hat >= +delta_SESOI`.

This means there is confirmatory evidence for a positive direction and the estimated effect reaches the signed practical threshold.

It licenses Experiment B / separately locked structural diagnostics. It does **not** establish the full programme thesis or mechanism.

### 9.2 SEPARABILITY_ADVANTAGE

Require both:

1. upper bound of the 95% CI < 0; and
2. `delta_hat <= -delta_SESOI`.

Interpretation: explicit world separation transferred better by an estimated practically meaningful amount.

### 9.3 PRACTICALLY_NULL

If the entire 90% CI lies inside `[-delta_SESOI, +delta_SESOI]`.

Interpretation: the experiment resolves effects of the predeclared meaningful magnitude as unsupported at this scale, even if a tiny directional difference exists.

### 9.4 UNRESOLVED

Any valid result not matching 9.1–9.3.

Examples include a noisy estimate whose CI spans zero and a SESOI boundary, or a statistically directional effect whose magnitude/uncertainty does not resolve practical meaning.

No post-hoc sample increase is allowed.

---

## 10. k=1 integrity analysis

Before the primary estimator:

- compare H1 checkpoint hashes across arms per seed;
- compare complete k=1 C-probe trajectory hashes/log sequence;
- require exact equality of T/censor state.

Any paired seed mismatch is not sampling noise. It triggers the preregistered implementation/platform invalidation path.

If any confirmatory seed violates the exact k=1 identity, aggregate primary analysis is not authorized until the validity status is resolved under project governance; v0.1 must not simply drop the seed.

---

## 11. Secondary curve shape

For k=1,2,4,6 report by arm:

- mean/median R;
- paired arm difference in R;
- censor fraction;
- raw T distribution where observed.

Plots are descriptive. No polynomial/slope fit, changepoint, monotonicity story, or selected k subset may replace the primary k1-to-k6 differential.

---

## 12. Secondary H1 reacquisition

Compute restricted reacquisition cost after k=6 using the same R functional.

Report paired ALIASED-SEPARABLE difference and raw/censor summaries descriptively with a 95% paired CI.

Do not interpret cheap H1 reacquisition alone as “absorption” or meta-structure; retention is an alternative explanation.

---

## 13. Ceiling/saturation reporting

For every arm/k report the fraction of probes capped at tau.

If `SEPARABILITY_ADVANTAGE` is driven by ALIASED cap saturation, the sign is still a valid bounded statement about the locked budget; the magnitude is explicitly conservative/underidentified beyond tau.

Do not extrapolate censored event times in the primary analysis.

An optional AFT/survival model may be reported only as a labeled sensitivity analysis if it was coded and hash-locked before confirmation. It cannot change the primary category.

---

## 14. Confirmatory tables/plots fixed before run

At minimum produce:

1. validity/integrity table;
2. primary `delta_hat`, 95% CI, 90% CI, SESOI lines, decision;
3. per-arm R summaries at k=1,2,4,6;
4. paired spaghetti plot of R across k (one line per seed, arm facets or explicit paired coding);
5. censor fractions;
6. H1 reacquisition summary;
7. exact config/hashes.

No plot-based scientific decision is permitted.

---

## 15. Conditional SHUFFLED-TAG diagnostic

If this diagnostic is authorized under the locked decision surface, it is not part of the primary estimate.

History code for each training example is drawn independently and uniformly from the six fixed history context vectors, independent of current world and operands/target, using a deterministic diagnostic RNG.

A fixed world-to-code permutation is invalid because it leaves world identity fully recoverable.

Run/analysis details must be fixed before the diagnostic is executed. Report it as mechanism-adjacent evidence only.

---

## 16. Structural null fence

`PRODUCTIVE_ALIASING_CANDIDATE` remains a regime-level result. It cannot be rewritten as proof that the common modular law was learned.

A structural claim requires an independently preregistered null/follow-up that removes the reusable modular structure while preserving the relevant nuisance properties. Until that follow-up passes, wording must stay at the forced-sharing/transfer level.
