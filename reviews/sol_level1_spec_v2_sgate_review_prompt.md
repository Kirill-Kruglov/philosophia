# GPT-5.6 Sol prompt: Level 1 v2 endpoint and inference S-gate review

Review the Level 1 v2 draft as the independent Y-line causal/statistical
reviewer. This is pre-S-gate and pre-comparative-data. Do not write code, create
a scout/escrow/lock/outcome, invent an effect, select a winner, or repair the
document yourself.

## Read first

1. `reviews/LEVELS1_3_CLAIM_GRAPH_SIGNATURES.md`
2. `reviews/fable_levels1_3_claim_graph_v2_1.md`
3. `reviews/sol_level1_spec_review.md`
4. `reviews/opus_level1_spec_review.md`
5. `reviews/fable_level1_spec_v2_closure.md`
6. `experiments/level_1_contact/SCIENTIFIC_SPEC_V2_DRAFT.md`
7. `canonical/CLAIM_LEDGER.md`
8. `canonical/KILL_MATRIX.md`

No Level 1 result exists. Independently verify formulas and populations; do not
treat the closure memo's `READY` verdict as evidence.

## Decision standard

The S-gate may be signed only if no later choice can change the estimand,
endpoint, censoring event, variance unit, interval predicates, or invalidity
routing. A threshold, panel count, seed schedule, or interval method is
load-bearing when changing it could move a block's solve time or a verdict.

## Required review

### Y1. Population, allocation, and estimand

Define exactly the finite population after:

- `Omega = {66,...,125}` is partitioned into 30 adjacent pairs;
- six pairs are permanently assigned to development;
- target/donor roles are randomized within the remaining pairs;
- only `N3` of up to 24 outcome pairs may be run;
- learner seeds/committee members repeat within blocks.

State the sampling probabilities and the estimand's conditioning. Check whether
the draft inconsistently calls all 60 integers, 24 outcome pairs, and realized
targets the same population. Determine whether adjacent matching removes or
merely fixes donor-target mismatch and how that narrows C1.

### Y2. Event time and bounded RMST

Verify that first-checkpoint timestamping with future persistence, cadence 50,
window 200, and completion by B defines one unambiguous event. Address step 0,
inclusive checkpoint count, missing checkpoints, events in the last window, and
whether "4 consecutive checkpoints" spans 150 or 200 steps.

The identity `RMST(B) = E[min(T,B)]` under common administrative censoring is
correct only under a precise latent-time convention. Verify its use here and
the orientation of all contrasts. Check whether a solve-count floor is a valid
identifiability guard or an outcome-dependent analysis gate that discards
otherwise informative bounded-cost contrasts. All-censored must never become
equivalence, but the repair must itself be preregistered and coherent.

### Y3. Panel and threshold completeness

Determine whether the solve event is defined while exact panel strata/counts,
accuracy, calibration statistic/bound, ABSTAIN/confident-lie caps, and leakage
tolerances remain open. Audit the proposed residue coverage: since label is
determined by `d mod n`, verify whether YES/NO balance within each residue class
is possible. Also verify evaluator support for `2n +/- 1`, especially `n=125`,
and whether evaluator-reserved cells as defined can contain those probes.

Classify each open item as endpoint-defining, analysis-defining, resource-only,
or harmless clerical confirmation. State what must be numerically frozen before
any S-gate signature and what provenance is legitimate without comparative
data.

### Y4. Finite-population estimator and uncertainty

Require the exact estimator, not only "stratified paired differences with FPC."
Specify/check:

- stratum weights and population sizes after development exclusion;
- block-arm seed aggregation;
- variance estimator and degrees of freedom for as few as four sampled blocks
  per stratum;
- FPC under partial sampling and the census case `N3=24`;
- what randomness remains when every outcome pair is run;
- simultaneous intervals for A-Y, Y-R, A-R and familywise handling;
- whether Bonferroni t intervals and a studentized block bootstrap are
  interchangeable (they are not a harmless signature choice);
- exact `SUP`, `EQ`, `NI`, and `NONSUP` predicates and N6 values.

Check whether a census FPC of zero makes the precision rule automatically pass
while seed/algorithm stochasticity remains outside the target population. The
spec must either condition honestly on a finite seed schedule or model the
algorithmic-seed population; it cannot switch readings after outcome.

### Y5. N3 rule and invalid/missing blocks

Audit the half-width `<= N6/2` rule, `[12,24]` range, balanced increments,
solve-count floor, and overflow fork. Clarify whether "clamped" means use 24
even when precision fails (unacceptable) or declare infeasibility as the later
text says.

Missing arms, non-finite trajectories, and deterministic-replay failures can be
informative missingness. Assess whether excluding up to four blocks and
recomputing FPC on survivors preserves any design-based estimand. Require
explicit routing for exogenous infrastructure failure versus potentially
outcome-related failure, with no post-outcome classification discretion.

### Y6. Margins, selector, and scout boundary

The draft names a 60-query scan as an N6 anchor but does not clearly freeze the
actual superiority/equivalence/non-inferiority/non-superiority margins. Decide
whether one 60-query value can govern all predicates and justify the direction
of each. Review multiplicity, non-transitive routing, RANDOM-superior anomaly,
and separation of the C1 verdict from mode selection.

State exactly what a non-comparative resource check may determine before the
S-gate and what the comparative development scout may estimate afterward.
Thresholds, margins, policies, and endpoint composition may not be learned from
comparative data.

## Required output

Write `reviews/sol_level1_spec_v2_sgate_review.md`. Use exactly one verdict:

- `LEVEL1_INFERENCE_S_GATE_ACCEPTED`
- `REVISE_LEVEL1_V2_INFERENCE`
- `BLOCKED_FINITE_POPULATION_DESIGN`
- `REJECT_LEVEL1_ENDPOINT`

Lead with Critical/Major/Minor findings. Then answer Y1-Y6, provide a corrected
estimand and population notation, list every mandatory pre-signature freeze,
and state the exact gate/implementation boundary. UNKNOWN and all-censored data
must never be narrated as equivalence, boundary, or success.
