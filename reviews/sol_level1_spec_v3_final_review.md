# Sol review — Level 1 v3 final inference and decision review

Verdict: `BLOCKED_LEVEL1_RANDOMIZATION`

This is a pre-signature, pre-data Y-line review of
`experiments/level_1_contact/SCIENTIFIC_SPEC_V3_DRAFT.md`, read against
the signed claim graph, the v2 S-gate reviews, the v3 closure memo, the
claim ledger, and the kill matrix. No feasibility run, comparative scout,
escrow, lock, or outcome step was run or authorized.

## Critical findings

1. **The allocation mechanism is deterministic, not randomized.**
   V3 uses SHA-256 counter streams keyed only by public fixed strings
   such as `"philosophia-L1v3-alloc/dev"`, `"role"`, and `"sample"`.
   That is reproducible selection, not a realized random draw. Conditional
   on the protocol, each pair's inclusion probability is 0 or 1, so the
   stated design-based inclusion probabilities, finite-population
   correction, and "stratified simple random sampling without replacement"
   are not justified.

   Mandatory edit: replace the public-string-only streams with an actual
   one-generation randomization protocol before any development scout:
   an externally auditable entropy source or witnessed CSPRNG transcript;
   one generated entropy value; no redraw; committed allocation log; and
   domain-separated streams for dev selection, role assignment, outcome
   sampling, seeds, pool reservation, replay, and shortlists. Specify the
   exact timing: `D` is drawn before any development use; roles over `O`
   are assigned once and conditioned on; `N3` is selected only by the
   frozen precision rule; `R_h` is drawn once after `N3`; no allocation is
   re-generated after seeing feasibility, censoring, loss, or contrast
   information. If deterministic public-string selection is retained, the
   design must drop SRS/FPC language and restrict inference to the selected
   blocks only.

2. **The integer sampler is not fully specified and "rejection-free
   Fisher-Yates" risks modulo bias.** Fisher-Yates is unbiased only if each
   integer draw is uniform over the current range.

   Mandatory edit: define the sampler mechanically. For each draw over
   `{0,...,r-1}`, consume fixed-width SHA/CSPRNG chunks, reject values
   outside the largest multiple of `r`, then take `u mod r`; or give an
   equivalent exact combinatorial sampler. Domain-separate every stream by
   level, stage, stratum, contrast/arm if applicable, block id, seed id,
   member id, and counter. Remove "rejection-free" unless a proof of exact
   unbiasedness is supplied.

## Major findings

1. **The estimator is close but not yet executable.** V3 states
   "Satterthwaite exact formula frozen" without writing the formula,
   defining `s_h^2`, the critical quantile, or zero-variance behavior.

   Mandatory edit: add the corrected notation below, including the
   denominator of `s_h^2`, the variance components, the Satterthwaite df,
   the Bonferroni quantile, the non-census zero-variance rule, and the
   census rule at `N3 = 24`.

2. **The determinacy guard still discards valid one-sided evidence.**
   V3 makes `SUP` floor-free but requires at least one observed solve in
   each compared arm for `NI` and `NONSUP`. That blocks directional
   conclusions when one arm solves and the other is censored, including
   the negative C1 boundary when YOKED solves and ACTIVE does not.

   Mandatory edit: replace the guard with the exact determinacy table in
   this review. All-censored remains unresolved; equivalence requires
   events in both arms; one-sided predicates require at least one event
   across the compared pair, not one event in each arm.

3. **The N3 precision rule is underspecified and too optimistic for six
   development blocks.** Two development pairs per stratum cannot stably
   estimate three stratum variances and simultaneous half-widths without
   a predeclared projection and conservative fallback. V3 also sizes only
   the primary contrast even though the total selector consumes the
   three-arm comparison family.

   Mandatory edit: define the projection formula for each of `{A-Y, Y-R,
   A-R}`, use the maximum projected Bonferroni simultaneous half-width,
   define zero/undefined scout variance behavior conservatively, and state
   that failure at `N3 = 24` means no lock rather than clamping or choosing
   the least bad value.

4. **Calibration and invalidity gates are not yet finite-sample complete.**
   The global Brier score over non-abstained items can be dominated by
   the 124 all-NO S1 items and can be improved by abstaining on difficult
   items. The encoding probe and shuffled-answer gates lack complete
   protocols and null finite-sample rules.

   Mandatory edit: replace the global non-abstained Brier with either
   per-stratum Brier requirements or an equal-stratum weighted Brier over
   all panel items with ABSTAIN assigned a fixed penalty, and freeze the
   exact encoding-probe and shuffled-answer protocols: number of runs,
   seeds, probe class, train/test split or exact permutation/binomial
   rule, and the invalidity threshold.

5. **Predicate boundary behavior is not fully explicit.** V3 uses strict
   `>` and `<` for one-sided predicates but `⊂ [−60,+60]` for equivalence,
   which is ambiguous at exactly `−60` and `+60`.

   Mandatory edit: write the boundary rules in inequalities. Recommended:
   `SUP(X,Y)` iff `L_XY > +60`; `NI(X,Y)` iff `L_XY > -60`;
   `NONSUP(X,Y)` iff `U_XY < +60`; `EQ(X,Y)` iff `L_XY >= -60` and
   `U_XY <= +60`, subject to the determinacy guard. Exact equality at a
   one-sided margin is unresolved/false for that one-sided predicate, not
   a success or boundary by narration.

## Minor findings

1. **The endpoint panel repair is substantively improved.** The three-zone
   construction closes the v2 `2n`, `2n±1`, and `n=125` support defects,
   and it now states honestly that S4 tests period plus novel
   opposite-displacement composition rather than pure hidden-`n` recovery.

2. **Step-0 solve and later divergence are coherent if kept literal.**
   `T=0` may qualify only through a full five-checkpoint window
   `0..200`; divergence after an already complete qualifying window does
   not undo the first solve time, while non-finite trajectories before any
   qualifying window are censored at `B`.

3. **Failure routing is directionally correct.** Outcome-related learner
   failure is retained as censored cost; process failures allow only one
   outcome-independent re-execution or fail closed. The remaining risk is
   evidentiary: "outcome-independent" must be established from pre-unseal
   mechanical logs, not from observed performance.

4. **Adjacent-only scope is now honestly named.** It supports only a
   distance-1 detector of online responsiveness relative to near-matched
   donated geometry; it does not test active learning generally.

## Y1 — actual randomization and finite population

Under fixed cyclic semantics, each `n` defines the oracle truth table. The
proper experimental world unit is the target adjacent-pair block: one
target `n`, its unique adjacent donor transcript/world, all three arms for
that block, and the locked finite seed replicates. Learner seeds, queries,
checkpoints, panel items, and committee members are repeated measurements
inside the block, not replication units.

Target+unique-donor is the correct inferential block for the signed C1
scope. It estimates the benefit of online target-coupled acquisition over
one adjacent donated active geometry under the locked role assignment. It
does not identify a pure target-specific coupling effect separated from
donor-target difficulty; unequal adjacent `n` values and donor transcript
idiosyncrasy remain part of the block-level contrast. Stratification and
one-to-one pairing can balance that difficulty, not decompose it.

Finite sampling without replacement from `O_h` would justify an FPC only
if `R_h` is actually randomized. With V3's public-string deterministic
selection, the design-based variance model is blocked. After the mandatory
randomization repair, the finite frame is coherent: `O_h` has eight
role-assigned blocks per stratum; `R_h` samples `n_h = N3/3` without
replacement; inference targets the 24-block frame conditional on `D`,
roles, and seeds; at `N3 = 24` the frame is a census.

## Y2 — estimator, df, and census rule

Corrected notation to freeze before the scout:

- Let `P_h` be the ten adjacent pairs in stratum `h`, `D_h` the two
  development pairs drawn once, and `O_h = P_h \ D_h`, with `N_h = 8`.
- Let `S_h` be the outcome sample, `n_h = N3/3`, drawn without
  replacement from `O_h` after `N3` is fixed.
- For arm `X` and block `p`, define
  `Y_X(p) = (1/2) Σ_{k=1}^2 min(T_Xpk, B)` under the conditioned two-seed
  schedule.
- For ordered contrast `X-Y`, define
  `d_XY(p) = Y_Y(p) - Y_X(p) = β_X(p) - β_Y(p)`, so positive favors `X`.
- Estimate
  `Δhat_XY = Σ_h W_h mean_{p∈S_h} d_XY(p)`, with `W_h = 1/3`.
- Define
  `s_h,XY^2 = (n_h - 1)^(-1) Σ_{p∈S_h} (d_XY(p) - mean_h)^2`.
- Define the estimated variance
  `Vhat_XY = Σ_h W_h^2 (1 - n_h/N_h) s_h,XY^2 / n_h`.
- For `N3 < 24`, use
  `ν_XY = Vhat_XY^2 / Σ_h [v_h,XY^2 / (n_h - 1)]`, where
  `v_h,XY = W_h^2 (1 - n_h/N_h) s_h,XY^2 / n_h`; zero `v_h` terms
  contribute zero to the denominator. If all `v_h = 0`, the interval is a
  point by the frozen estimator, but it must be reported as estimated
  zero sample variance, not known zero world uncertainty.
- Use the two-sided Bonferroni critical value
  `t_{1 - 0.05/(2·3), ν_XY}` for each simultaneous contrast interval.
- At `N3 = 24`, `n_h = N_h` for all strata, the FPC is zero by census of
  the 24-block outcome frame, intervals collapse to points, and the result
  is descriptive only of those 24 role-assigned blocks under the
  conditioned seed schedule. It does not generalize over learner seeds,
  role reassignments, unsampled integers, or alternate donors.

For `N3 = 24`, point intervals are coherent. For `N3 < 24`, every variance
pattern must have a defined interval before the scout; no variance pattern
may trigger ad hoc widening, shrinkage, or block exclusion.

## Y3 — directional determinacy table

The guard should separate no-information administrative censoring from
one-sided bounded-cost evidence. For an ordered comparison `X-Y` with
interval `[L_XY, U_XY]`:

| Observed solve pattern | Eligible predicates | Forbidden predicates | Route if no eligible predicate resolves |
|---|---|---|---|
| `X` none, `Y` none | none | `SUP`, `EQ`, `NI`, `NONSUP` | `INSUFFICIENT`; never equivalence, boundary, or success |
| `X` at least one, `Y` none | one-sided predicates (`SUP`, `NI`, `NONSUP`) decided only by `[L_XY,U_XY]` | `EQ` | `INSUFFICIENT` |
| `X` none, `Y` at least one | one-sided predicates (`SUP`, `NI`, `NONSUP`) decided only by `[L_XY,U_XY]` | `EQ` | `INSUFFICIENT` |
| `X` at least one, `Y` at least one | all predicates decided by `[L_XY,U_XY]` | none | `INSUFFICIENT` |

Thus an all-censored pair cannot earn `EQ`, `NONSUP`, a boundary, or a
selector success merely because bounded costs tie at `B`. Conversely, if
one arm solves and the other is censored, the interval may legitimately
resolve superiority, non-inferiority, or non-superiority in either
direction. The interval, not the event-count pattern alone, determines the
direction.

## Y4 — N3 precision from six development blocks

The scout may estimate only feasibility, censoring, covariance, and
block-difference variability under the already frozen endpoint. It may not
change the endpoint, margins, arms, policies, panel, cadence, censoring
rules, or predicates.

The N3 rule must be written as a projection, not prose:

- Compute development block differences for all three ordered contrasts
  `{A-Y, Y-R, A-R}` under the same seed aggregation and bounded-cost
  endpoint.
- Within each stratum and contrast, estimate `s_dev,h,XY^2` from the two
  development blocks, with the same denominator convention as the outcome
  estimator.
- For each candidate `N3 ∈ {12,15,18,21,24}`, set `n_h=N3/3` and project
  `Vproj_XY(N3)=Σ_h W_h^2 (1-n_h/8) s_dev,h,XY^2/n_h`, with the matching
  Satterthwaite df and Bonferroni critical value.
- Choose the smallest `N3` for which the maximum projected half-width over
  the three contrasts is `≤ 30`.
- If any scout variance is undefined, non-finite, or mechanically
  unavailable, use a predeclared conservative fallback. If any zero
  variance is allowed to remain zero, the spec must state why two
  development blocks are sufficient to license that; otherwise use a
  bounded-cost fallback. The fallback itself must be frozen before the
  scout.
- If the rule fails at `N3 = 24`, no lock may be created. It is not
  permissible to clamp to 24 and proceed with a warning.

Using the same six development blocks for censoring, covariance, and
precision is acceptable only as a declared engineering precision model,
not as evidence about the final contrast.

## Y5 — endpoint and control statistics

The solve certificate is now mostly aligned with the intended hidden
structure: S4 supplies the anti-difference-lookup tooth; S1/S2/S3/S5
prevent trivial syntactic and base-rate solutions; all scoring is
per-stratum except Brier. The panel surface must remain byte-identical
across worlds, and all target-specific labels and `d` values must stay
inside the sealed evaluator.

Required repairs:

- Replace or supplement the global non-abstained Brier rule. Because S1
  has 124 all-NO items, a global score can be dominated by easy negatives;
  excluding ABSTAINs can also improve calibration by withholding hard
  items. Use per-stratum Brier or equal-stratum weighted Brier, and assign
  ABSTAIN a fixed probability/penalty in the calibration calculation.
- Specify the encoding probe as an exact finite-sample test: artifacts
  visible to the probe, model class, training protocol, split or
  cross-validation, number of random seeds if any, and the null rule for
  `top-1 <= 1/6` over 12 development worlds.
- Specify shuffled-answer controls exactly: which worlds, arms, seeds,
  transcripts, checkpoint cadence, number of runs, and why zero solves is
  the finite-sample invalidity threshold.
- Keep parameter-shift reporting diagnostic only unless a finite-sample
  null and threshold are frozen pre-scout.
- Keep missing checkpoints on the process-failure route. They must never
  become non-qualifying observations that silently change solve times.

No invalid block may be excluded from the estimator. Either the run is a
retained censored scientific failure, a permitted outcome-independent
single re-execution, whole-level invalidity, or insufficient evidence.

## Y6 — predicates, selector, and signature readiness

The benefit orientation is correct: larger benefit means lower
budget-to-certified-solve, and for ordered contrast `X-Y`,
`d_XY = cost_Y - cost_X` is positive when `X` is better.

Corrected comparison table:

| Comparison | Contrast | Positive means | Primary use | Predicate interpretation |
|---|---|---|---|---|
| `A-Y` | `Δ_AY = β_A - β_Y = cost_Y - cost_A` | ACTIVE solves sooner | C1 | `SUP(A,Y)` earns C1; `NONSUP(A,Y)` supports the distance-1 boundary; unresolved blocks Level 2 |
| `Y-R` | `Δ_YR = β_Y - β_R = cost_R - cost_Y` | YOKED geometry beats RANDOM | geometry diagnostic and selector | Directional geometry evidence; cannot rescue or rewrite C1 |
| `A-R` | `Δ_AR = β_A - β_R = cost_R - cost_A` | ACTIVE beats RANDOM | total selector | Operational mode selection only |

Minimum simultaneous family: `{A-Y, Y-R, A-R}` with familywise coverage
over the three paired finite-population intervals. `SUP`, `EQ`, `NI`, and
`NONSUP` all consume these same intervals on the common benefit scale.
Non-transitive, cyclic, or otherwise unclassifiable interval patterns must
route to `INSUFFICIENT`; they cannot be repaired by narrative priority.
The least-adaptive tie priority is scientifically acceptable only after
all required comparisons are resolved and the equivalent-best set is
well-defined. A RANDOM-superior result remains a registered anomaly and
never changes the meaning of C1.

V3 is not ready for signature until the randomization repair and the
mandatory inference-contract edits above are made. The 24-pair target
frame and adjacent-only detector scope can be preserved; no mathematical
contradiction requires reopening the distance axis.

## Pre-scout freeze list

Before any comparative development scout, the following must be frozen:

- Actual randomization source, one-generation log, domain separation,
  unbiased integer sampler, `D`, role assignment timing, seed schedule,
  and post-`N3` outcome sampling rule.
- Population frame, target+donor block definition, seed nesting,
  estimator, FPC, `s_h^2`, Satterthwaite df, critical quantile,
  zero-variance behavior, and census interpretation.
- Panel construction, exposed byte-identical surface, all solve counts,
  ABSTAIN, confident-lie, calibration/Brier rule, persistence window,
  `B`, cadence, step-0, missing-checkpoint, and divergence routing.
- Leakage gates: shuffled-answer protocol, encoding-probe protocol,
  parameter-shift status, finite-sample invalidity rules.
- Predicate inequalities, determinacy table, familywise comparison
  family, total selector, C1 reading, RANDOM anomaly handling, and all
  boundary behavior at exactly `±60`.
- N3 projection formula, conservative fallback for zero/undefined scout
  variance, and the rule that failure at 24 blocks prevents lock creation.

After that freeze, the scout may estimate only variance, covariance,
censoring, feasibility, and the resulting `N3` under the frozen rule.

## Implementation and gate boundary

Implementation may proceed only for neutral, non-data-bearing components:
parameterized world enumeration, pure panel/pool verifiers, fail-closed
process interlocks, commitment plumbing, and dummy-fixture tests. The
allocation sampler itself should not be committed as scientific machinery
until the randomization protocol is repaired.

Kirill should not sign the Level 1 S-gate, create a lock, run the
comparative scout, generate real escrow, or issue outcome commands until
the mandatory edits are incorporated and independently checked. The
optional non-comparative feasibility driver remains permissible only after
the endpoint and implementation boundary are repaired, and only under the
single-arm development-world contract.

## Residual forbidden claims

Level 1 remains forbidden to claim:

- `PROOF_CORE` or `PROOF_STRONG` in either direction.
- Active learning advantage beyond the locked adjacent-distance detector.
- A conclusion about larger donor distances, all possible role
  assignments, all `n ∈ 66..125`, or any learner-seed superpopulation.
- That certificate failure proves the learner did not recover `n`.
- That all-censored, censored, or `UNKNOWN` outcomes establish
  equivalence, boundary support, or success.
- That development-scout contrasts are citable evidence.
- That RANDOM superiority rewrites C1.
- That YOKED donor transcripts encode target-specific hidden structure
  rather than adjacent donor structure.
- That calibration, leakage absence, or encoding safety has been shown
  until the finite-sample gate protocols are frozen and passed.
