# Sol Y-line review - Level 1 v2 endpoint and inference S-gate

Reviewer: Sol, independent causal/statistical Y-line. Scope:
`experiments/level_1_contact/SCIENTIFIC_SPEC_V2_DRAFT.md` against the signed
claim graph, prior Sol/Opus reviews, Fable's v2 closure memo, and canonical
claim/kill files. This is pre-S-gate and pre-comparative-data. I did not write
code, create a scout/escrow/lock/outcome, invent an effect size, select a
winner, or repair the source document.

## Verdict

REVISE_LEVEL1_V2_INFERENCE

The v2 draft is much closer than v1, but it is not S-gate signable. Several
items that can move the endpoint, estimand, interval predicates, or invalidity
routing remain unresolved or internally inconsistent. The design is repairable;
the finite cyclic world unit is not blocked and the C1 estimand is not rejected.

## Critical Findings

**C1 - The evaluator panel definition is internally inconsistent.** The draft
says panel items are built from evaluator-reserved cells, but the reserved-cell
partition is drawn from the acquisition cell universe with `|d| <= 125`. The
periodicity stratum then requires `d = 2n` and `d = 2n +/- 1`, which for every
`n >= 66` lies outside `|d| <= 125`. Thus the periodicity probes cannot be both
reserved cells from the stated partition and outside the contacted support.
Mandatory edit: define a separate evaluator-only cell universe with its own
support, reservation, serialization, and leak-proofing, or change the acquisition
and reserved-cell universe consistently.

**C2 - The `2n + 1` support claim fails at the upper edge.** With word
displacements `a,b in [-125,125]`, possible differences are `[-250,250]`.
For `n = 125`, `2n + 1 = 251` is impossible. The strengthened requirement
`2*N2 >= 2*n_max` supports `2n`, not `2n + 1`. Mandatory edit: either increase
the evaluator displacement support so `2*N2_eval >= 2*n_max + 1`, or replace
the near-miss construction with a realizable top-edge rule that is symmetric
and fixed before data.

**C3 - YES/NO balance within each residue class is mathematically impossible.**
For fixed `n`, label is determined by `d mod n`: residue `0` is YES and every
nonzero residue is NO. A requirement for YES/NO balance within each residue
class cannot be satisfied. Mandatory edit: define label balance across residue
classes or across matched residue/near-miss strata, while acknowledging that
individual nonzero residues are single-label cells.

**C4 - The persistence window arithmetic is ambiguous.** The draft states
cadence `C = 50`, persistence `W_p = 200`, and "4 consecutive checkpoints."
Four checkpoints at 50-step cadence span 150 steps, not 200. A 200-step
inclusive span requires five checkpoints: `t, t+50, t+100, t+150, t+200`.
Mandatory edit: choose one convention, state the checkpoint count, step span,
last eligible start time, and step-0 behavior explicitly.

## Major Findings

**M1 - The finite population and sample are not fully specified.** After six
development pairs are removed, the outcome population appears to be 24 adjacent
pairs, eight per stratum, with a locked target/donor role assignment. But only
`N3` of those 24 may be run, and the draft does not define which `N3` pairs are
sampled, their inclusion probabilities, or whether the estimand is over all 24
outcome pairs or only over realized pairs. Mandatory edit: before S-gate,
define the outcome population, the `N3` sampling design, stratum weights, and
whether inference is finite-population over 24 pairs or descriptive over the
realized `N3`.

**M2 - The solve-count floor can discard informative bounded-cost contrasts.**
The candidate floor, ">= 25% of blocks with observed solve in each compared
arm," correctly prevents all-censored arithmetic from becoming equivalence.
But it also blocks cases where one arm solves and another does not, which can be
informative for superiority on bounded cost. Mandatory edit: replace the
per-arm floor with a predicate-specific determinacy rule, or explicitly justify
why even one-sided superiority is unresolved when one arm has enough solves and
the other is censored. All-censored comparisons must remain `INSUFFICIENT`.

**M3 - The exact interval estimator is still not frozen.** Bonferroni-adjusted
paired t intervals and a studentized block bootstrap are not interchangeable
signature choices. They can produce different `SUP`, `EQ`, `NI`, `NONSUP`, and
selector outcomes. Mandatory edit: choose the primary simultaneous interval
method, degrees of freedom, variance estimator, and fallback behavior before
S-gate. The other method may be sensitivity only.

**M4 - N6 margins are anchored but not numerically frozen.** The draft names a
60-query scan as provenance but does not state the actual superiority,
equivalence, non-inferiority, and non-superiority margins. Mandatory edit:
freeze exact margin values on the benefit scale and the direction for each
predicate. One 60-query value may govern all predicates only if the S-gate
states the scientific reason; otherwise use separate margins.

**M5 - Invalid block exclusion does not preserve a design-based estimand unless
failure classes are fixed by cause.** Excluding up to four invalid blocks and
recomputing finite-population correction on survivors changes the finite
population if invalidity is related to trajectory difficulty, non-finite
learning, deterministic replay, resource limits, or missing arms. Mandatory
edit: separate exogenous infrastructure loss from potentially outcome-related
failure before outcome, and route each class deterministically. Potentially
outcome-related failures may not simply shrink the population.

**M6 - Census FPC must not erase algorithmic-seed uncertainty by accident.** If
`N3 = 24`, the block-sampling FPC is zero for the 24-pair finite population. That
is coherent only if the target estimand conditions on the locked seed/committee
schedule and all within-block stochasticity is part of the observed finite
descriptive quantity. Mandatory edit: state whether seeds are conditioned on or
sampled from an algorithmic-seed population; do not switch readings after
outcome.

## Minor Findings

**m1 - Adjacent-pair yoking narrows C1 but does not remove donor mismatch.**
Distance is fixed at one, so mismatch is controlled and conservative, not
eliminated. The claim remains "target-adaptive probe-scale choice versus
adjacent-modulus active geometry."

**m2 - Step 0 needs an explicit endpoint rule.** If an untrained model qualifies
for a persistent window beginning at step 0, the endpoint should either allow
`T = 0` or explicitly forbid step-0 event starts. Either choice is endpoint
defining.

**m3 - Missing checkpoints must be terminally classified.** A missing checkpoint
inside a candidate persistence window should be either block invalidity,
incomplete evidence, or a nonqualifying observation by a locked rule.

## Y1. Population, Allocation, and Estimand

Let `Omega_int = {66,...,125}` be the integer registry. The scientific block
unit is not an integer alone but an adjacent pair after role assignment:

- `P = {(66,67), (68,69), ..., (124,125)}`, `|P| = 30`;
- development set `D` contains six pairs, two per stratum, permanently removed;
- outcome registry `O = P \ D`, `|O| = 24`, eight pairs per stratum;
- within each pair, target/donor role is randomized once at S-gate and then
  conditioned on;
- `N3` pairs are sampled or selected from `O` for the actual outcome battery;
- learner seeds and committee members repeat within each sampled block.

The v2 text sometimes speaks as if the population is all 60 integers, sometimes
the 24 outcome pairs, and sometimes the realized `N3` blocks. These are distinct
objects. A signable estimand must condition on the development exclusion and
role assignment, then state whether it targets the 24-pair outcome registry or
only the realized `N3` sample.

If `N3 < 24`, the sampling probabilities must be known. A balanced sample such
as `n_h = N3/3` pairs per stratum from `N_h = 8` has inclusion probability
`pi_h = n_h / 8` within stratum. If the S-gate instead preselects named pairs,
there is no sampling inference to the unsampled outcome pairs without a model.

Adjacent matching fixes donor-target distance at one and therefore fixes, rather
than removes, donor-target mismatch. It supports the narrow C1 estimand:
ACTIVE target-specific coupling versus an adjacent-modulus donor ACTIVE query
geometry, with all target answers generated by the target oracle.

## Y2. Event Time and Bounded RMST

The intended latent-time convention is: each arm has a certified-solve time `T`
equal to the first checkpoint at which a full future persistence window qualifies
and completes by `B`; otherwise the arm is administratively censored at `B`.
Under common administrative censoring and the bounded-cost convention,
`RMST(B) = E[min(T,B)]` is correct.

But the current checkpoint arithmetic is not unambiguous. With `C = 50` and
`W_p = 200`, "4 consecutive checkpoints" is incompatible with a 200-step span.
The S-gate must define:

- whether the window uses 4 checkpoints spanning 150 steps or 5 checkpoints
  spanning 200 steps;
- whether step 0 can be a solve start;
- whether the last eligible start is `B - W_p`;
- how missing checkpoints inside a window are routed;
- whether an event whose confirming window extends past `B` is censored.

The contrast orientation is correct:

`Delta_choice = RMST_YOKED(B) - RMST_ACTIVE(B)`.

Positive values favor ACTIVE. On the benefit scale `beta = -RMST`, the same
fact is `beta_ACTIVE - beta_YOKED > 0`.

A solve-count floor is a valid guard against all-censored equivalence only if it
is predicate-specific and preregistered. The current per-arm floor is too blunt:
it can suppress an otherwise informative bounded-cost superiority contrast.
`UNKNOWN` means unresolved evidence; it is not equivalence, boundary, or
success.

## Y3. Panel and Threshold Completeness

Endpoint-defining items still open:

- exact evaluator panel universe and stratum counts;
- realizable support for `2n`, `2n-1`, and `2n+1`;
- per-stratum accuracy thresholds;
- calibration statistic and bound;
- ABSTAIN and confident-lie caps;
- leakage/null tolerances for shuffled answers and encoding probes;
- missing-checkpoint and step-0 event rules.

Analysis-defining items still open:

- interval method, degrees of freedom, and familywise handling;
- N6 numeric margins;
- seed aggregation and seed-population interpretation;
- N3 block sampling procedure.

Resource-only items:

- wall time, storage ceiling, and non-comparative runtime feasibility, provided
  they cannot change B, endpoint composition, or thresholds after comparative
  data.

Harmless clerical confirmations:

- restating signed negative destinations, anomaly labels, and file paths, if no
  rule value changes.

The residue-balance claim must be revised: since label is determined by
`d mod n`, YES/NO balance within each residue class is impossible. Balance may
be global, by stratum groups, or by matched positive/near-miss constructions,
but not within a single residue.

The evaluator cannot currently support `2n+1` for `n=125` under the stated
support. It also cannot build `2n` probes from evaluator-reserved cells if those
cells are restricted to `|d| <= 125`. This is endpoint-defining and must be
fixed before S-gate.

Legitimate provenance without comparative data: mathematical feasibility
proofs, syntactic enumeration, Level 0 platform precedent for engineering
cadence only, non-comparative resource checks, and external scientific
relevance arguments for margins. Comparative scout data may not choose
thresholds, margins, panel composition, or endpoint support.

## Y4. Finite-Population Estimator and Uncertainty

A signable estimator should look like this if the target is the 24-pair outcome
registry:

- three strata, each with `N_h = 8` outcome pairs after development exclusion;
- if `N3` is balanced, sample `n_h = N3/3` pairs per stratum;
- for each sampled block and arm, aggregate seeds/committee members to one
  block-arm bounded cost `Y_{ihX}`;
- for a contrast `X - Y` on benefit, define a block difference such as
  `D_{ih}^{X,Y} = Y_{ihY} - Y_{ihX}` on the RMST/cost scale, positive favoring
  X;
- estimate `Delta_{X,Y} = sum_h W_h * mean_h(D^{X,Y})`, with
  `W_h = N_h / sum_h N_h = 1/3`;
- estimate variance as
  `sum_h W_h^2 * (1 - n_h/N_h) * s_h^2 / n_h`, unless the S-gate chooses a
  different finite-population estimator.

Degrees of freedom are not automatic with as few as four sampled blocks per
stratum. The S-gate must choose Satterthwaite, conservative minimum-stratum df,
randomization-style intervals, or another exact rule. Bonferroni t intervals and
studentized block bootstrap are not interchangeable and cannot be left as a
signature-time preference after seeing scout behavior.

If `N3 = 24`, the block-sampling FPC is zero for the finite registry. Then the
decision becomes descriptive of the full 24-pair registry under the locked seed
schedule unless seed stochasticity is separately modeled. The precision rule
may pass automatically for block sampling, but that must be the intended
finite-population reading.

Simultaneous intervals are required for A-Y, Y-R, and A-R. Exact `SUP`, `EQ`,
`NI`, and `NONSUP` predicates require exact N6 values and interval directions
before any comparative scout.

## Y5. N3 Rule and Invalid/Missing Blocks

The half-width `<= N6/2` rule is conceptually acceptable as a precision rule
only after N6 and the interval method are fixed. `[12,24]` and balanced
increments imply `N3` should be a multiple of three; state this explicitly.

The word "clamped" must not mean "use 24 even when precision fails." The later
text correctly says if the rule demands more than 24, no lock may be created
without registry extension or an `INSUFFICIENT` design decision. Keep that
reading and remove any ambiguity.

Invalid/missing block handling is not yet design-based. Missing arms,
non-finite trajectories, deterministic replay failures, and resource stops can
be related to the arm outcome. Excluding up to four such blocks and recomputing
FPC on survivors estimates a survivor population, not the registered outcome
population. Mandatory edit: classify failures before outcome into:

- exogenous infrastructure loss, with predeclared routing;
- design/process invalidity, usually design invalid;
- potentially outcome-related trajectory failure, routed to
  `INSUFFICIENT` or design invalid rather than survivor exclusion;
- completed negative scientific result, routed through predicates.

No invalid block may be silently dropped or replaced after outcome.

## Y6. Margins, Selector, and Scout Boundary

The 60-query scan is a plausible non-comparative relevance anchor, but the
actual margins are not frozen. A single 60-query value can govern all predicates
only if the S-gate defines:

- superiority: e.g. benefit difference must exceed the locked relevance margin;
- equivalence: simultaneous interval must lie within `[-m, +m]`;
- non-inferiority: lower bound must exceed `-m`;
- non-superiority: upper bound must be below `+m`.

If these use different scientific meanings, use different margins. The values
must be signed before the scout and cannot be learned from variance or arm
means.

Multiplicity handling must be familywise across the three pairwise contrasts.
Non-transitive or incoherent intervals route to `INSUFFICIENT`. RANDOM-superior
is a registered anomaly and may affect the total selector under the signed rule,
but it does not rewrite the C1 ACTIVE-vs-YOKED verdict.

Before S-gate, a non-comparative resource check may determine runtime,
storage, implementation feasibility, and whether fixed B is computationally
possible, but it may not observe arm comparisons. After S-gate, the comparative
development scout may estimate variance, covariance, censoring, N3 precision,
and resource use under the frozen rules. It may not change thresholds, margins,
policy, endpoint composition, support, panel strata, estimator family, or
invalidity routing.

## Corrected Estimand and Population Notation

Let:

- `P = {(66,67),...,(124,125)}` be the 30 adjacent pairs;
- `D_h` be the two development pairs in stratum `h`;
- `O_h = P_h \ D_h`, with `N_h = 8`;
- `R_h` be the sampled outcome pairs in stratum `h`, with `n_h = N3/3`;
- `A_d` be the locked target/donor role assignment;
- `S` be the locked finite seed/committee schedule, if conditioned on.

If the target is the 24-pair outcome registry, the C1 estimand is:

`Delta_AY = sum_h (N_h/N) * mean_{p in O_h} [Y_YOKED(p,A_d,S) - Y_ACTIVE(p,A_d,S)]`,

where `Y_X = min(T_X,B)` is the block-arm bounded cost after seed aggregation,
and positive `Delta_AY` favors ACTIVE. The estimator samples `R_h` from `O_h`
with known inclusion probabilities. If all 24 pairs are run, the estimand is
observed exactly conditional on the seed schedule and role assignment.

If the design instead targets only realized `N3` blocks, replace `O_h` with
`R_h` and remove finite-population generalization to unsampled pairs. The S-gate
must choose.

## Mandatory Pre-Signature Freeze List

Before S-gate signature, freeze or correct:

- target population: 24-pair registry versus realized `N3` sample;
- `N3` pair sampling design and inclusion probabilities;
- target/donor role assignment procedure and conditioning statement;
- seed schedule interpretation: conditioned finite schedule versus seed
  population;
- evaluator-only support, including `2n`, `2n-1`, `2n+1` realizability;
- correction to impossible per-residue YES/NO balance;
- exact panel stratum counts and thresholds;
- calibration statistic/bound, ABSTAIN caps, confident-lie caps;
- leakage/null tolerances and parameter-shift hard thresholds, if any;
- cadence/window arithmetic, step-0 event rule, missing-checkpoint routing, and
  last eligible event start;
- exact bounded-cost/RMST estimator, variance estimator, degrees of freedom, and
  interval method;
- exact N6 margins and predicate directions for `SUP`, `EQ`, `NI`, `NONSUP`;
- solve-count/determinacy guard, revised so all-censored data cannot become
  equivalence but informative one-sided bounded-cost contrasts are not thrown
  away;
- N3 precision rule wording, including multiples of three and no "clamped"
  success when precision fails;
- invalid/missing block routing by exogenous versus potentially outcome-related
  cause;
- resource wall and non-comparative resource-check boundary.

## Gate and Implementation Boundary

Implementation allowed now only for neutral dummy-fixture substrate that cannot
encode the unresolved choices: pure `Z/n` semantics, word folding, EQ oracle,
truth-table enumeration, donor bookkeeping, salted commitment plumbing, and
dataflow interlocks.

Not signable and not eligible for comparative scout: the current v2 S-gate.
Not yet eligible for implementation as scientific modules: evaluator panel
builder, endpoint evaluator, interval/selector engine, invalidity router, N3
selector, and any learner/acquisition configuration whose behavior depends on
the unresolved support, threshold, margin, or estimator choices.

Forbidden until a revised S-gate is signed: comparative development scout,
real escrow, preregistration lock, Level 1 outcome driver, and any decision or
essay update. UNKNOWN and all-censored data must never be narrated as
equivalence, boundary, or success.
