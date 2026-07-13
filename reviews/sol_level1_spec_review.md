# Sol Y-line review - Level 1 endpoint and inference specification

Reviewer: Sol, independent causal/statistical Y-line. Scope:
`experiments/level_1_contact/SCIENTIFIC_SPEC_DRAFT.md` against the signed
Levels 1-3 claim graph and canonical ledger. This is pre-S-gate and
pre-comparative-data. I did not write code, create scout/lock/escrow/outcome
artifacts, choose numeric margins, invent effect sizes, tune thresholds, or
predict any arm.

## Verdict

INFERENCE_SPEC_ELIGIBLE_FOR_CLOSURE

The consolidated Level 1 draft is scientifically eligible to proceed to S-gate
closure. The remaining choices are real and load-bearing, but they are
identified as pre-comparative S-gate choices rather than silently defaulted.
No structural defect requires rejecting the estimand, and the finite cyclic
world unit is correctly recognized as the distinct `n`, not a seed, query,
checkpoint, or duplicate instance id.

## Critical Findings

None.

## Major Findings

**M1 - The endpoint event time must be observation-cadence explicit.** The draft
correctly uses fixed-budget, no-early-stop, right-censored
budget-to-certified-solve, but the S-gate must decide whether event time is the
first observation in a subsequently persistent window or the later observation
that confirms persistence. Either is defensible; switching later would move the
endpoint. Mandatory S-gate closure: cadence, persistence window, event-time
timestamp convention, and treatment of interval uncertainty between
observations.

**M2 - The finite-population model must be chosen before N3.** The draft
correctly says the truth table is determined by `n`, duplicate `n` is not a new
world, and target+unique-donor blocks are disjoint. Because blocks are sampled
without replacement from a finite N1 set, ordinary i.i.d. block inference is
valid only as a superpopulation approximation if explicitly chosen. Mandatory
S-gate closure: finite-population versus superpopulation model, finite
population correction if used, and how seed-level repeated measures are
aggregated inside each block before block-level inference.

**M3 - Balanced panel cells must force cyclic structure, not syntactic
shortcuts.** A balanced YES/NO panel is necessary but not sufficient. For fixed
R/L cyclic semantics, the panel must include wrap-around positives where integer
displacements differ but are congruent modulo `n`, hard negatives with similar
length and displacement magnitude, repeated/symmetric orientation controls, and
relation-type strata that make trivial "unequal unless syntactically identical"
fail. Mandatory S-gate closure: exact panel strata, arm-independent generation,
and a proof that the panel construction and serialized artifacts cannot leak
`n` to learners or policies.

**M4 - N6 margins must be scientific relevance margins, not scout products.**
The draft and signatures correctly move N6 before any comparative scout. The
S-gate must make this operational: equivalence, non-inferiority, and
non-superiority margins may use mathematical baselines, external task
requirements, or declared conservative relevance bounds, but not observed arm
differences or scout-estimated variance.

## Minor Findings

**m1 - Donor-target unequal `n` supports a narrow estimand.** YOKED with
`n_donor != n_target` is necessary to break oracle identity. It estimates the
value of target-specific coupling relative to independent active geometry from
the same size stratum, not relative to an oracle-identical but nonadaptive
counterfactual.

**m2 - RANDOM-superior is an anomaly, not a design failure.** The signed total
selector handles this correctly if the anomaly is reported without changing the
selector or rewriting C1.

**m3 - Repeated queries are handled correctly.** They cost one unit, return the
same bit, and are not silently deduplicated; keep this in the lock.

## S1. Experimental and Variance Unit

Under the fixed R/L cyclic world, `n` determines the full oracle truth table.
Therefore distinct `n` values are the world units. Repeated runs on the same
`n`, multiple learner seeds, repeated queries, checkpoints, and evaluation-panel
items are repeated measurements or diagnostics, not new replications.

The correct inferential block for the signed design is one target `n`, its three
target arms, and one unique disjoint donor transcript/world. This block
definition is appropriate because YOKED is only meaningful through its donor
transcript, and donor reuse would couple nominal blocks. Seeds should be nested
or crossed inside the block and reduced to block-level summaries or modeled with
block as the variance unit.

Sampling without replacement from the finite N1 set makes the target population
finite unless the lock explicitly declares a superpopulation model over possible
`n`. Either route is acceptable if frozen. Without replacement generally reduces
sampling variance relative to with-replacement sampling; treating finite
exhaustive strata as i.i.d. without justification would overstate the sampling
model.

Donor/target pairing within size strata but unequal `n` does not identify a
pure same-world nonadaptive counterfactual. It identifies the narrow estimand:
target-adaptive ACTIVE versus independent donor-active query geometry sampled
from the locked same-stratum donor distribution, with all answers supplied by
the target oracle. If strata are broad, donor-target difficulty mismatch enters
the estimand; the S-gate should define strata tight enough that this is an
accepted feature rather than an accidental confound.

## S2. Censoring and RMST

For each block and seed aggregate, define potential solve time `T_X` for arm X
and observed data `(min(T_X, B), delta_X)`, where `delta_X = 1` only if the
certified-solve event is observed by the common horizon B. Censoring is
administrative if B is fixed before data, common to all arms, and not chosen
because a curve looks promising or hopeless. This draft satisfies that
conceptually.

Persistent solve times are formed from evaluator observations at locked cadence.
The S-gate must define whether the timestamp is the start of the persistent
window or the confirmation observation. A non-solve at B is right-censored and
UNKNOWN for solve, never success and never equivalence.

The orientation is correct:

`Delta_choice = RMST_YOKED(B) - RMST_ACTIVE(B)`.

Positive Delta means ACTIVE has lower restricted mean budget-to-certified-solve
than YOKED, hence ACTIVE is better on the C1 benefit scale.

A valid estimator family for paired finite blocks may be one of: paired
block-level restricted-mean differences with censoring handled by a prespecified
survival estimator, a bounded-cost score with non-solves assigned by a locked
rule, or a randomization/paired-sign style procedure on block summaries if its
assumptions are declared. Because the YOKED counterfactuals for alternate donor
assignments are not run, assignment permutation cannot be the primary estimator.
Uncertainty should be over independent blocks, with seeds treated as repeated
measures.

If few or no arms solve, the result is not equivalence. It is unresolved unless
the prespecified restricted-mean/bounded-cost interval yields a determinate
superiority or non-superiority predicate. `UNKNOWN` means the evidence does not
resolve the required comparison; a boundary requires a resolved predicate such
as ACTIVE not superior to YOKED under the locked rule.

Evidence required before comparative data: resource timing for feasible B,
mathematical grammar coverage for possible solve, non-comparative endpoint
sanity on development fixtures, and a declared scientific reason for the
persistence/cadence convention. Comparative arm differences may not choose B,
cadence, persistence, or thresholds.

## S3. Solve Certificate and Balanced Panel

A balanced held-out EQ panel can measure recovery of hidden cyclic structure if
it is not merely a syntactic classifier. Required strata:

- label balance: YES/NO within each major stratum;
- displacement class: exact syntactic equality, modulo-`n` wrap positives,
  near-miss negatives, and same-length hard negatives;
- word length and length imbalance;
- orientation: `(u, v)` canonicalization plus held-out symmetric checks;
- repeat status: novel panel queries separated from training repeats;
- `n` stratum: every sampled size stratum represented without revealing `n`.

The panel must be generated after lock, be arm-independent, and be visible only
to the evaluator. Serialized panel sizes, query ids, stratum names, hashes, or
ordering must not leak `n` or target identity to learner/acquisition code.

Calibration, ABSTAIN, confident-lie, repeated-query, and class-balance rules
must be fixed before comparative data. ABSTAIN is not a correct solve; it may
be useful only within a locked abstention rule. Confident lies should be a
separate failure or constraint, not hidden inside average accuracy. Repeated
queries cost budget and may appear in training histories; panel credit should
distinguish genuinely held-out queries from repeats.

Threshold provenance:

- mathematical baselines can set chance performance on balanced binary panels,
  trivial inequality baselines, and grammar coverage requirements;
- external or scientific anchors are needed for calibration tolerances,
  persistence windows, and confident-lie relevance;
- comparative scout data may estimate variance/censoring/feasibility but cannot
  set solve thresholds, ABSTAIN thresholds, calibration bounds, or margins.

## S4. Three-Arm Comparisons and Total Selector

Use one benefit scale, larger better:

`beta_X = -RMST_X(B)` or an equivalent locked transformation where lower
budget-to-certified-solve gives larger benefit.

Minimum simultaneous comparison family:

| Purpose | Required comparison | Positive direction |
|---|---|---|
| C1 chosen contact | ACTIVE vs YOKED | ACTIVE superior to YOKED |
| Donated geometry value | YOKED vs RANDOM | YOKED superior to RANDOM |
| Active vs static total | ACTIVE vs RANDOM | ACTIVE superior to RANDOM |
| Level 2 selector | all pairwise intervals | select unique superior or least-adaptive equivalent best set |

Predicate directions:

- `SUP(X,Y)`: benefit X exceeds Y by the locked superiority rule;
- `EQ(X,Y)`: the simultaneous interval for beta_X - beta_Y lies within the
  locked equivalence margin;
- `NI(X,Y)`: X is not meaningfully worse than Y by the locked margin;
- `NONSUP(X,Y)`: X is not meaningfully better than Y by the locked upper-bound
  rule.

Multiplicity/familywise handling must be simultaneous across the three-arm
family because the selector consumes all pairwise relations. Non-transitive or
overlapping intervals route to `INSUFFICIENT`, not narrative resolution. The
least-adaptive tie priority RANDOM-STATIC, then YOKED-GEOMETRY, then ACTIVE is
valid as a conservative operational selector if all margins are frozen before
the scout. RANDOM-superior is a registered anomaly and may select RANDOM under
the signed rule, but it does not rewrite C1 or license a stronger programme
claim.

N6 margins must represent scientific relevance: the smallest budget reduction
or benefit difference worth calling contact-choice value or worth treating arms
as operationally equivalent. They freeze before the scout and cannot be derived
from observed comparative variance or arm means.

## S5. Development Contrast Scout

A non-citable development scout may estimate:

- endpoint computability;
- censoring frequency at the fixed B;
- block-level ACTIVE/YOKED/RANDOM covariance and contrast variance;
- seed-within-block variability for aggregation planning;
- runtime, memory, artifact size, and resource-stop feasibility;
- balance diagnostics for donor assignment and panel construction.

It may not change N1/N2, B, acquisition policy, panel thresholds, calibration,
ABSTAIN semantics, margins, estimator family, or arm meanings after seeing
comparisons. The same development worlds and policies may estimate censoring and
paired variance only if the endpoint and policy are already frozen and those
worlds are permanently excluded from outcome/escrow.

A defensible N3 precision rule without an invented effect size should target
interval width or decision stability under the locked estimator, not power for a
made-up effect. Conceptually require coverage across every N1 size stratum,
enough disjoint target+donor blocks per stratum to estimate block variance, and
enough seeds inside blocks to estimate repeated-measure noise without treating
seeds as blocks. Resource stops in the scout must be outcome-independent:
predeclared wall/storage limits based on feasibility, not arm performance.

## S6. Leakage and Invalidity Statistics

Shuffled answers are a design-level leakage/null test: if a learner can certify
solve under shuffled answers beyond the locked null tolerance, the endpoint or
encoding leaks structure and the design is invalid. Parameter-shift reports are
diagnostic unless the lock defines a hard failure threshold; they should expose
whether the policy is exploiting sampler artifacts. Encoding probes are
design-invalidating if pre-contact serialized artifacts allow recovery of `n`
or panel structure beyond the locked null tolerance.

Donor balance is a pre-treatment validity condition. If target/donor strata,
candidate pools, transcript lengths, or full-B donor commitments fail, the
affected block is invalid; if the assignment procedure systematically fails or
requires post-outcome replacement, the design is invalid.

Block-invalidating failures include donor reuse, target/donor overlap, duplicate
target `n` presented as a new block, partial donor transcript, transcript hash
mismatch, unequal oracle budget, unequal update schedule, missing arm run,
non-finite learner state, evaluator leakage, and arm-dependent panel exposure.
Design-invalidating failures include escrow exposure/regeneration, global
candidate-pool mismatch, post-scout endpoint/margin/policy changes, shuffled-null
success, encoding-probe success, and any systematic invalidity that leaves the
locked block population undefined.

No invalid block may be silently excluded. The lock must specify whether any
block invalidity aborts the whole outcome, whether a small predeclared invalid
count yields `PLATFORM_OR_DESIGN_INVALID`, or whether a blinded replacement
scheme exists before outcome. Missing or failed runs are incomplete evidence,
not negative outcomes.

## Corrected Estimand

For finite N1 set Omega, size strata S, locked donor assignment A_d, learner
seed schedule R, and common horizon B:

`Delta_choice = E_{block in Omega, r in R}[RMST_YOKED(B) - RMST_ACTIVE(B)]`.

The expectation is over the locked block-sampling model: finite-population over
the registered target+donor blocks, or a declared superpopulation approximation
over cyclic worlds. Positive values favor ACTIVE. The estimand is conditional
on the realized one-to-one donor assignment unless a design with multiple
executed donor assignments is actually run. Its scope is target-specific
coupling versus independent same-stratum active query geometry in finite cyclic
R/L worlds.

## Corrected Comparison Table

| Decision object | Predicate | Interpretation |
|---|---|---|
| C1 earned | `SUP(ACTIVE, YOKED)` | target-adaptive query choice adds value over donated active geometry |
| C1 boundary | resolved not-`SUP(ACTIVE, YOKED)` | `BOUNDARY_CONTACT_CHOICE`; no programme-core falsification |
| Geometry value | `SUP(YOKED, RANDOM)` | active query geometry transfers without target adaptivity |
| Static anomaly | `SUP(RANDOM, ACTIVE)` or selector chooses RANDOM | report anomaly; do not alter C1 semantics |
| Selector unique winner | one arm `SUP` against both others | choose that Level 2 contact mode |
| Selector tie | mutually `EQ` best set and not worse than outsiders | choose least adaptive member |
| Unclassified | unresolved, cyclic, or non-transitive intervals | `INSUFFICIENT`; Level 2 blocked |

## Pre-Scout Freeze List

Before any comparative development scout, freeze:

- N1 finite `n` set/range, size strata, and without-replacement model;
- N2 word-length cap and wrap-around witness coverage proof;
- B common oracle budget and resource wall;
- candidate-pool enumeration, repeat policy, and query-index serialization;
- learner architecture, initialization, optimizer, online update/replay view,
  and seed aggregation plan;
- ACTIVE uncertainty scalar, calibration method, candidate shortlist rule, and
  deterministic tie-break;
- RANDOM-STATIC distribution;
- target/donor assignment scheme, balance diagnostics, and block invalidity
  rules;
- evaluator panel construction, hidden strata, cadence, persistence,
  event-time timestamp convention, thresholds, calibration, ABSTAIN, and
  confident-lie rules;
- benefit orientation, RMST/bounded-cost estimator family, interval/test family,
  multiplicity handling, and N6 margins;
- development scout outputs allowed to inform N3 and the N3 precision rule;
- leakage/null thresholds for shuffled answers, encoding probes, and any hard
  parameter-shift invalidity;
- outcome-independent resource-stop rules.

## Implementation Boundary

May be implemented now, after this review and before S-gate signature:
pure cyclic R/L world enumeration, EQ oracle, candidate-pool machinery, dummy
non-escrow panel generators, dataflow separation tests, donor transcript
serialization tests, repeated-query accounting, and inert evaluator utilities
that contain no scientific thresholds.

Must wait for S-gate signature: comparative scout driver, any real development
contrast run, finalized endpoint thresholds, margins, estimator/rule constants,
N3, real escrow generation, preregistration lock, and any Level 1 outcome
command. The S-gate must close the freeze list above in one signed artifact
before comparative data exists.

## Source Constraints Used

The only external source constraints materially needed here are standard:
active-learning sources justify treating query choice as the intervention rather
than matching away answer entropy; Kaplan-Meier/Cox-style survival analysis
justifies explicit right-censoring at B; and equivalence-testing practice
requires predeclared relevance margins. These constrain the analysis form only;
they do not provide Level 1 effect sizes, margins, or thresholds.
