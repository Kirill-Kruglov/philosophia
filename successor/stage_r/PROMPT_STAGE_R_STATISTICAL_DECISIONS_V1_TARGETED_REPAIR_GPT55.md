# Prompt — targeted repair of Stage-R statistical decision proposal V1

ROLE: Original scientific design statistician, bounded repair pass. Paper-only
and read-only. Repair only the enumerated R1–R9 defects in
`successor/stage_r/STAGE_R_AUTHOR_DECISION_PROPOSAL_V1.md`. This is not a new
scientific or architecture review. Do not edit files, write code, execute a
learner, generate data/items, invoke the frozen selector, mint keys/roots,
commit or push.

## Read

- `successor/stage_r/STAGE_R_AUTHOR_DECISION_PROPOSAL_V1.md`
- `successor/stage_r/PROMPT_STAGE_R_STATISTICAL_DECISIONS_GPT55.md`
- `successor/recovery/phase2_stage_b_20260815/science_inputs/TASK_SCIENTIFIC-CONTRACT_REVIEW_OPUS5.md`
- `successor/dev/PHASE2_POST_REVIEW_DRIVER_DECISION_19.md`

All route and scope decisions in the original prompt remain fixed. Stage H
remains demoted. Do not add arms, worlds, reviewers or Stage-B universality.

## Repair findings

### R1 — the injected positive-control gate is impossible at `B_disp=4`

V1 D8 requires a two-sided exact sign-flip test at `alpha=0.10` on four
complete blocks. Even with all four centered effects in the favourable
direction, the smallest attainable two-sided p-value is
`2 / 2**4 = 0.125`. Therefore the lower interval bound cannot exceed `delta`;
the control is guaranteed to fail. Choose a positive-control block count and
criterion that can pass under the frozen interval law, and prove attainability
from its exact p-value resolution. Do not use a mid-p convention unless it is
explicitly justified and frozen.

### R2 — the sign-flip interval overclaims its estimand and degenerate behavior

An inverted sign-flip test is exact for a symmetry/location model, not
distribution-free inference for an arbitrary population mean. State the exact
estimand and symmetry/exchangeability assumption, or replace the method.
Correct the claim that identical `D_j` values automatically make the interval
collapse to one point; derive the actual inversion behavior, including all-zero
and nonzero-constant samples. Specify how continuous candidate `m` endpoints
are computed without an unstated grid. If no low-`N` distribution-free mean
interval is feasible under bounded `D_j in [-C,C]`, say so explicitly rather
than calling an assumption exact.

### R3 — four disposable contrasts do not support the claimed robust sizing

With four values, MAD is frequently zero or unstable; replacing zero by
`delta` can force `N=8` without conservative evidence. Repair the disposable
sample count and dispersion upper-bound/inflation rule, or supply a bounded
worst-case rule and show its resource consequence. Preserve the separation
between disposable sizing data and scientific blocks. The repair must state
what happens when variance cannot be estimated adequately.

### R4 — cap/margin/variance/N/envelope selection is circular

V1 chooses `C` from timing, defines `delta=0.05*C`, estimates variance of
cap-dependent `D_j`, sizes `N`, and then asks whether `N` fits the envelope used
to choose `C`. Give one total, single-pass chronology. If candidate caps are
evaluated, specify which permanently excluded observations exist for every
candidate and a deterministic candidate-selection rule. No value may depend on
a scientific outcome.

### R5 — censoring direction and notation are wrong

V1 defines `h_{r<-q,j}` as an already aggregated cap-hit fraction and then
places it under `mean_g`. Define the cap indicator at theorem level first and
then its reciprocal block contrast. More importantly, more cap hits in the
mismatched arms generally compress their high latent work and can attenuate a
positive uncapped interaction; cap-hit direction alone does not prove that it
“favours positive D.” Because overshoot beyond `C` is unobserved, use a
scientifically defensible symmetric guard or prove any asymmetric rule. Keep
clear that the registered primary estimand itself is capped work; uncapped work
is only a companion/sensitivity target.

### R6 — Latin-square balance and arbitrary `N`

V1 permits every integer `N=8..24`, but exact four-position Latin-square balance
requires `N` divisible by four. Add a deterministic rounding rule and recheck
power/resource logic. Define behavior after missing/invalid blocks without
silently breaking order balance.

### R7 — several author choices are mislabeled as derivable

The following are scientifically material preferences, not consequences of the
driver or algebra: margin fraction `0.05`, 90% confidence, 80% power at
`2*delta`, `N_max=24`, the cap candidate set, four strata, 32 held-out items,
16 selected tasks, AUC/Jaccard thresholds, censoring thresholds, attrition
thresholds and available compute. Reclassify each honestly as one of:

- `DERIVED_FIXED`;
- `CLOSED_DISPOSABLE_RULE`;
- `AUTHOR_RATIFICATION_REQUIRED`.

You may recommend values, but do not disguise them as derived. Consolidate the
ratification list so the author can accept or replace it once.

### R8 — selector qualification is not statistically closed

For the AUC and incremental-AUC gates, name the independent sampling unit,
minimum disposable sample size, resampling/interval algorithm and precedence
when the CI cannot be computed. Explain whether rank/quantile normalization
makes the proposed median/IQR gate tautological; if so, replace it with a gate
on the raw selector signal or an implementation equality check. Keep
`CELL_CANNOT_HOST_ESTIMAND_FOR_THIS_LEARNER_CLASS` distinct from implementation
invalidity.

### R9 — frame terminology and accepted bands

Clarify whether the scientific blocks share one sealed reservoir and held-out
panel or receive block-specific frames. The governing claim is conditional on
one sealed frame. Do not invent new “stratum cutpoints” if the intended strata
are the already accepted S1–S4 bands; either bind to those exact bands or name a
separate outcome-blind mapping and why it is necessary. State how repeated use
of the fixed held-out panel affects the scope of inference.

## Required output

Return a standalone `STAGE_R_AUTHOR_DECISION_PROPOSAL_V2`, not a diff. Preserve
D1–D14 but repair every downstream dependency. Include:

1. a total chronology from excluded qualification through author ratification,
   disposable sizing, freeze and scientific analysis;
2. an exact feasibility proof for the positive-control test;
3. the mathematical assumptions and attainable resolution of the interval;
4. a table mapping R1–R9 to repaired D-sections;
5. one compact `AUTHOR_RATIFICATION_REQUIRED` table with recommended values and
   consequences;
6. a statement that no third statistical design pass is authorized. Any
   remaining disagreement is resolved by author choice or route closure.

If the proposed `N_max` cannot make both `R_POSITIVE` and
`R_BOUNDED_NEGATIVE` realistically attainable under the corrected interval and
variance rule, set `STAGE_R_AUTHOR_DECISIONS_READY=NO`; do not preserve a small
number for aesthetic reasons.

End with exactly:

```text
ROUTE_REOPENED=NO
STAGE_H_DEMOTED=YES
INDEPENDENT_UNIT=COMPLETE_TWIN_BLOCK
GENERAL_REVIEWS_REMAINING=0
STATISTICAL_REPAIR_PASSES_REMAINING=0
SCIENTIFIC_EXECUTION_AUTHORIZED=NO
STAGE_R_AUTHOR_DECISIONS_READY=YES|NO
```
