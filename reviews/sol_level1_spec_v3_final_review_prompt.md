# GPT-5.6 Sol prompt: final Level 1 v3 inference and decision review

Perform the final independent Y-line review of Level 1 v3. This is pre-signature
and pre-data. Do not write code, run a feasibility/comparative check, generate
escrow, create a lock/outcome, choose an observed-data-dependent rule, or predict
an arm.

## Read first

1. `reviews/LEVELS1_3_CLAIM_GRAPH_SIGNATURES.md`
2. `reviews/fable_levels1_3_claim_graph_v2_1.md`
3. `reviews/sol_level1_spec_v2_sgate_review.md`
4. `reviews/opus_level1_spec_v2_sgate_review.md`
5. `experiments/level_1_contact/SCIENTIFIC_SPEC_V3_DRAFT.md`
6. `reviews/fable_level1_spec_v3_closure.md`
7. `canonical/CLAIM_LEDGER.md`
8. `canonical/KILL_MATRIX.md`

No Level 1 datum exists. Audit formulas and finite-sample rules from the source,
not from Fable's readiness verdict.

## Required review

### Y1. Actual randomization and finite population

The target frame `O` of 24 role-assigned pairs is accepted in principle. Check
whether SHA-256 keyed only by fixed public strings constitutes an actual
randomized allocation with known inclusion probabilities or merely a
deterministic selection. “Rejection-free Fisher-Yates” may introduce modulo
bias unless an exact unbiased integer sampler is specified. Require:

- source and one-generation commitment of allocation entropy;
- domain separation and counter encoding;
- unbiased integer sampling/Fisher-Yates;
- exact timing of development selection, roles, and `N3` sampling;
- proof no redraw is possible;
- exact conditioning statement.

If deterministic pseudorandom selection is retained, state whether design-based
inclusion probabilities and FPC remain justified. Do not allow a random-sampling
claim without a random mechanism.

### Y2. Estimator, degrees of freedom, and census

Check the stratified estimator and FPC. The draft says the Satterthwaite formula
is “exactly frozen” without displaying it. Require the exact formula, the
definition of `s_h^2`, critical quantile, behavior when a stratum variance is
zero, and the `N3=24` point-interval rule.

Audit the conditioned seed schedule: two replicate counts are stated, but exact
seed generation/allocation must be frozen. Confirm that conditioning on two
seeds makes the census claim descriptive and removes any algorithmic-seed
generalization.

At `N3<24`, verify that Bonferroni t intervals with only 4-7 blocks per stratum
and Satterthwaite df are defined for every variance pattern. At `N3=24`, decide
whether zero world-sampling uncertainty and point comparisons are coherent with
the same predicate family.

### Y3. Directional determinacy guards

Test every censoring pattern. V3 makes `SUP` floor-free but requires at least one
solve in **each** arm for `NI` and `NONSUP`. This may discard strongly
directional evidence: if YOKED solves and ACTIVE never does, a C1-negative
`NONSUP(ACTIVE,YOKED)` may be estimable even though ACTIVE has no event; the
mirror case matters for NI.

Require a mechanical table for each predicate under:

- both arms all-censored;
- X has events, Y none;
- Y has events, X none;
- both have events.

All-censored must remain unresolved; EQ must never arise from ties at B. Decide
whether one-sided predicates should require only at least one event across the
pair plus their interval direction, rather than one per arm.

### Y4. N3 precision from six development blocks

The comparative scout has only two development pairs per stratum. Determine
whether it can estimate three stratum variances and a Satterthwaite simultaneous
half-width stably enough to select among `N3={12,15,18,21,24}`. Specify the exact
projection formula, treatment of zero/undefined scout variance, and conservative
fallback. It may not invent precision or default to a smaller N3.

Check that “fails at 24” means no lock, never clamp. Assess whether using the
same six development blocks for censoring, covariance, and precision creates an
unstated model assumption.

### Y5. Endpoint and control statistics

Verify the panel count thresholds and binomial-tail claims under the actual
imbalanced strata. Audit global Brier over non-abstained items: S1 contributes
124 all-NO items, so the statistic may be dominated by easy negatives, and
excluding abstentions may bias calibration. Decide whether calibration must be
per-stratum or weighted, and whether abstentions must receive a defined Brier
penalty.

The encoding gate “top-1 <= 1/6 over 12 development worlds” lacks a stated
sample/probe protocol. The shuffled-answer gate lacks a number of runs/seeds.
Classify these as design-invalidity statistics only if their null distribution
and finite-sample rule are exact before signature.

Check whether step-0 solve, later divergence, one re-execution, and missing
checkpoint rules create any outcome-dependent exclusion or endpoint switching.

### Y6. Predicates, selector, and signature readiness

Verify exact sign orientation for A-Y, Y-R, A-R, `SUP/EQ/NI/NONSUP`, and the
total selector. Check strict versus non-strict boundary behavior at exactly
`+/-60`, interval familywise coverage, non-transitive routing, and the C1 rule
that uses `NONSUP` for the distance-1 boundary.

List every remaining value/procedure capable of moving a verdict. Decide whether
it is safely implementation-level, requires a bounded v3.1 correction, or
blocks the S-gate. Preserve the declared 24-pair target frame and adjacent-only
detector scope unless a mathematical contradiction forces reopening them.

## Required output

Write `reviews/sol_level1_spec_v3_final_review.md`. Use exactly one verdict:

- `LEVEL1_V3_YLINE_ACCEPTED_FOR_SIGNATURE`
- `REVISE_LEVEL1_V3_INFERENCE_CONTRACT`
- `BLOCKED_LEVEL1_RANDOMIZATION`
- `REJECT_LEVEL1_V3_DECISION_RULE`

Lead with Critical/Major/Minor findings. Answer Y1-Y6, give corrected population
and estimator notation, an exact determinacy table, mandatory edits if any, and
the implementation/gate boundary. UNKNOWN, censoring, and all-censored patterns
must never be converted into equivalence, boundary, or success.
