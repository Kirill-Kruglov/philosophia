# Fable 5 prompt: produce the signable Level 1 v3 specification

Revise Level 1 v2 after the independent Opus X-line and Sol Y-line S-gate
reviews. This is a bounded pre-S-gate correction. Do not write implementation
code, run any feasibility or comparative check, generate escrow, create a lock
or outcome, or predict an arm.

## Read first

1. `reviews/LEVELS1_3_CLAIM_GRAPH_SIGNATURES.md`
2. `reviews/fable_levels1_3_claim_graph_v2.md`
3. `reviews/fable_levels1_3_claim_graph_v2_1.md`
4. `experiments/level_1_contact/SCIENTIFIC_SPEC_V2_DRAFT.md`
5. `reviews/fable_level1_spec_v2_closure.md`
6. `reviews/opus_level1_spec_v2_sgate_review.md`
7. `reviews/sol_level1_spec_v2_sgate_review.md`
8. `canonical/CLAIM_LEDGER.md`
9. `canonical/KILL_MATRIX.md`
10. `experiments/level_1_contact/README.md`

The formal reviews govern; chat captures are provenance only. Both reviewers
require revision. Preserve v1 and v2 unchanged.

## Deliverables

Write:

1. `experiments/level_1_contact/SCIENTIFIC_SPEC_V3_DRAFT.md` — standalone and
   complete.
2. `reviews/fable_level1_spec_v3_closure.md` — finding disposition, explicit
   choices, signature packet, and reviewer handoff.

Use exactly one closure-memo verdict:

- `READY_FOR_FINAL_LEVEL1_S_GATE_REVIEW`
- `REVISE_LEVEL1_V3_SPEC`
- `BLOCKED_LEVEL1_CERTIFICATE`

`READY` is allowed only if every value that can move a trajectory, solve event,
interval predicate, invalidity route, or estimand is exact in v3. Do not call an
unset scientific value a “signature confirmation.” `N3` alone remains a
post-comparative-scout realized number under a fully frozen rule.

## Governing design choices for v3

### A. Keep adjacent-only, with honest asymmetric scope

Use the existing adjacent target/donor construction as the primary candidate;
do **not** add a second distance arm in v3. State why: C1 is a modifier, not a
`PROOF_CORE` conjunct; distance 1 gives the strongest positive detector while a
second donor axis would multiply blocks, comparisons, and the one-week cost.

Correct the estimand name to **online responsiveness under near-matched probe
scale**. A positive C1 is strong within that scope. A resolved null supports
only `BOUNDARY_CONTACT_CHOICE_AT_DISTANCE_1` as the scope annotation carried by
the canonical `BOUNDARY_CONTACT_CHOICE`; it says nothing about larger donor
distances or active learning generally. Include an authorial signature line:

`I_ACCEPT_ADJACENT_ONLY_C1_DETECTOR_SCOPE`

and name the alternative `I_REQUIRE_LEVEL1_DISTANCE_AXIS` as a redesign that
reopens world supply, arms, multiplicity, budget, and review.

### B. Use one coherent finite population

Resolve the Opus/Sol tension in favor of a design-based 24-pair outcome frame:

- `P`: 30 adjacent pairs;
- `D`: six development pairs selected by an exact locked pre-data procedure;
- `O = P \ D`: 24 outcome pair-blocks, eight per stratum;
- target/donor role assigned once per pair by an exact locked procedure and
  conditioned on;
- `R_h`: `n_h = N3/3` pairs sampled by stratified simple random sampling without
  replacement from each `O_h`, with known inclusion probability `n_h/8`;
- estimand: the finite mean over all 24 role-assigned outcome pair-blocks,
  conditional on `D`, role assignment, and the locked finite learner-seed
  schedule.

Explain explicitly why this rejects Opus's suggestion to redefine the
population as already-realized `N3`: that would make FPC/generalization to the
registered outcome frame meaningless. At `N3=24`, the outcome frame is a census,
world-sampling variance is exactly zero, and the claim becomes descriptive of
those 24 blocks under the conditioned seed schedule. Do not imply scope over all
60 integers or an algorithmic-seed superpopulation.

## Mandatory scientific repairs

### 1. Three-zone support with correct arithmetic

Separate and name:

- maximum individual word displacement `A_word`;
- maximum raw word length and padding/parity rule;
- acquisition difference cap `d_acq`;
- raw-novel reserved cells inside acquisition support;
- evaluator-only extrapolation support outside acquisition differences.

Use exact candidate values satisfying at least:

- `A_word >= 126`;
- `2*A_word >= 2*n_max + 1 = 251`;
- `n_max <= d_acq < 2*n_min - 1` so every `d=n` is contactable and every
  `2n-1, 2n, 2n+1` is outside acquisition support;
- all chosen words and `u SEP v` sequences fit the model's positional contract.

`A_word=126` and `d_acq=125` are the minimal repair unless a stronger exact
reason is given. Make acquisition cells world-independent. Define evaluator
zones explicitly:

1. acquisition cells presented to arms;
2. reserved raw-novel cells with `|d| <= d_acq`, useful for syntax/robustness but
   **not** difference-novel;
3. extrapolation cells containing `2n` and realizable `2n +/- 1`, raw- and
   difference-novel and never available to acquisition.

Ensure acquisition includes the full marginal range of individual
displacements/lengths used by extrapolation wherever mathematically possible,
so the load-bearing test is novel **composition/difference**, not merely an
unseen token length. State the irreducible remaining corner-composition scope.

Replace every false claim that all panel items are semantically never-contacted.
Only the extrapolation stratum has that property. The opaque flat index, fixed
syntactic multiplicity, world-independent pool, offline-only semantic map, and
side-effect-free policy boundary remain accepted.

### 2. Algebraically valid fixed panel

Replace the residue paragraph with an exact table. For each stratum specify:

- fixed item count;
- positive/negative count and label rule;
- allowed `d` support and exact construction;
- raw novelty and difference novelty separately;
- word-length/marginal matching;
- scientific role and whether it carries anti-lookup force.

EQ is YES only at residue zero; never demand YES/NO balance inside one residue
class. Balance across matched classes/strata. Cover every nonzero residue at
least once or give an exact fixed-size coverage rule valid for every
`n in [66,125]` without leaking variable panel metadata. Panel size, ordering,
ids, strata, and counts exposed outside the sealed evaluator must be
world-independent; any target-specific structure remains encrypted/sealed.

State exactly:

- within-support reserved items test raw/syntactic generalization but a
  difference lookup can pass them;
- the `2n` versus `2n +/- 1` stratum is the sole anti-difference-lookup tooth;
- the certificate jointly tests learned period and extrapolation to a novel
  opposite-displacement composition. This is an intentionally conservative
  endpoint: a pass is strong, a failure is ambiguous and yields censoring, not a
  claim that the learner never recovered `n`.

Give enumeration obligations proving every panel item is realizable at both
edges of the registry.

### 3. Fully executable learner contract

Freeze, with no “Level 0 hyperparameters” placeholder:

- tokenization, segment/separator handling, padding mask;
- positional/length scheme and exact maximum input length;
- layer count, dimensions, heads, activation, normalization, dropout, output
  head, parameter initialization;
- committee size and shared-across-arm initialization;
- exact ensemble probability aggregation used by evaluator;
- training loss;
- AdamW `lr`, weight decay, betas, epsilon, decay groups, scheduler/warmup;
- replay minibatch definition at steps 1..B, sampling RNG, update/zero ordering;
- acquisition disagreement formula, shortlist RNG relationship between target
  ACTIVE and donor ACTIVE, tie-break, and state-hash invariance;
- checkpointed state and deterministic resume.

Do not claim random-init disagreement is meaningful knowledge. It is a locked
randomized heuristic that may become epistemic after contact; early behavior is
near-random, and a null is scoped to that policy. Justify architecture capacity
for sequences up to the chosen maximum without citing Level 0's 3-token success
as sufficient evidence.

If architecture/B feasibility genuinely requires observation, define a
separate **non-comparative feasibility check contract**: development worlds,
single policy/arm only, no arm contrast, no escrow, exact permitted outputs,
hard resource cap, no effect/margin tuning, and a rule for signed pre-S-gate
amendment. Do not run or implement it.

### 4. Exact solve event

Choose exact, non-comparatively justified values for:

- panel counts from the table;
- ensemble aggregation;
- predicted label and ABSTAIN mapping;
- per-stratum accuracy;
- calibration statistic and bound;
- ABSTAIN cap;
- confident-lie definition and cap;
- shuffled-answer and pre-contact encoding tolerances;
- any parameter-shift hard threshold, or state explicitly that it is diagnostic
  only.

Prefer finite-sample count rules whose pass/fail behavior can be unit-tested.
Explain why each value expresses “certified” performance rather than expected
model performance. None may come from a future comparative scout.

Fix persistence arithmetic. If `C=50` and the intended span is 200 steps, use
five checkpoints `t,t+50,t+100,t+150,t+200`. State whether step 0 may start an
event, the last eligible start, inclusive endpoints, and missing-checkpoint
routing. `T` remains the first checkpoint of the earliest complete qualifying
window, found only post-B from sealed evaluation.

### 5. Exact estimator and predicates

Freeze the finite conditioned learner-seed schedule and aggregate it to one
block-arm cost. Committee members are one learner, not extra seeds.

Use the stratified paired finite-population estimator over `O`:

- exact stratum weights;
- exact contrast sign/orientation;
- FPC variance formula for `N3<24`;
- exact degrees-of-freedom rule at four to eight sampled blocks per stratum;
- exact census rule at `N3=24`;
- one primary simultaneous interval method. Use Bonferroni-adjusted paired
  t-intervals with a stated familywise alpha unless a stronger exact primary is
  justified; bootstrap may be sensitivity only.

Freeze numeric N6 margins on the query-budget benefit scale. If 60 queries is
the single scientific relevance margin, define exactly:

- `SUP(X,Y)`: lower simultaneous bound exceeds `+60`;
- `EQ(X,Y)`: full interval lies inside `[-60,+60]`;
- `NI(X,Y)`: lower bound exceeds `-60`;
- `NONSUP(X,Y)`: upper bound is below `+60`.

If any predicate uses a different margin, name and justify it now.

Replace the blunt per-arm 25% solve floor with a predicate-specific determinacy
guard. Requirements:

- all-censored compared arms resolve no predicate;
- one arm solving while the other is censored may support `SUP` if the locked
  bounded-cost interval clears its margin;
- `EQ` cannot be earned from administrative ties at B;
- every guard is pre-data, mechanical, and compatible with the total selector.

Fix the N3 rule: multiples of three, smallest balanced `N3` meeting the locked
simultaneous half-width target, never “clamp to 24 and proceed.” If projected
precision fails at 24, no lock; only the already named signed redesign or
`INSUFFICIENT` route remains.

### 6. Failure routing without survivor bias

Remove discretionary survivor-population inference. Freeze cause classes and
routing before outcome:

- a non-finite learner trajectory is outcome-related scientific failure for
  that arm: record censored/non-solve cost `B`, do not exclude the block;
- missing/corrupt artifacts, hardware failure, deterministic replay mismatch,
  seal breach, or unequal budgets are process/design failures under exact
  predeclared routing; they may not be reclassified from observed performance;
- prefer fail-closed whole-level `PLATFORM_OR_DESIGN_INVALID` or
  `INSUFFICIENT` over excluding blocks and recomputing FPC;
- no post-outcome replacement and no “up to four” discretionary exclusion.

State the exact route for a missing checkpoint inside a persistence window and
for a run that cannot be deterministically resumed.

### 7. Gate sequence

Give exact status for:

1. neutral parameterized substrate;
2. corrected pool/panel/learner implementation;
3. optional non-comparative feasibility driver and one execution;
4. final v3 S-gate review;
5. Kirill's S-gate signatures;
6. comparative development scout;
7. N3 closure and preregistration lock;
8. real escrow;
9. outcome driver and execution.

No comparative scout, lock, real escrow, or outcome is authorized by v3.

## Closure memo requirements

Include:

1. the single verdict;
2. every Opus CR/MJ/mn and Sol C/M/m disposition;
3. a compact table of every exact frozen constant and its non-comparative
   provenance;
4. explicit accepted disagreements: 24-pair population rather than realized-
   `N3` population; adjacent-only detector scope rather than a second donor axis;
5. signature lines, including `I_ACCEPT_ADJACENT_ONLY_C1_DETECTOR_SCOPE` and one
   consolidated `I_ACCEPT_LEVEL1_V3_SCIENTIFIC_SPEC` token;
6. exact questions for final Opus and Sol reviews;
7. Codex/Cursor authorization and negative space;
8. confirmation that no code, datum, scout, escrow, lock, or outcome was made.

Preserve `PROOF_CORE`/`PROOF_STRONG`, C6 as annotation, C1 as non-core modifier,
the total selector, and every signed negative destination. A conservative
certificate failure is censoring/UNKNOWN, not evidence that `n` was absent from
the learner.
