# Fable 5 prompt: close the Level 1 v2 scientific specification

Revise the Level 1 scientific specification after the independent Opus X-line
and Sol Y-line reviews. This is a bounded pre-S-gate design task. Do not write
implementation code, run a comparative scout, generate escrow, create a lock or
outcome artifact, choose a winner, or describe any development contrast as
evidence.

## Read first

1. `reviews/LEVELS1_3_CLAIM_GRAPH_SIGNATURES.md`
2. `reviews/fable_levels1_3_claim_graph_v2.md`
3. `reviews/fable_levels1_3_claim_graph_v2_1.md`
4. `experiments/level_1_contact/SCIENTIFIC_SPEC_DRAFT.md`
5. `reviews/opus_level1_spec_review.md`
6. `reviews/sol_level1_spec_review.md`
7. `experiments/level_1_contact/README.md`
8. `canonical/CLAIM_LEDGER.md`
9. `canonical/KILL_MATRIX.md`
10. `ROADMAP.md`
11. `essay/climbing-the-wall-of-experience.md`, especially sections VI-VII

The two chat-response captures are provenance only; the formal review files
govern. Verify governing text against the current HEAD. Opus minor finding mn-5
is stale: the README, KILL_MATRIX, and ROADMAP already replace equal-answer-
entropy matching with ACTIVE/YOKED/RANDOM and treat answer entropy as a
mediator. Record that finding as already closed; do not reintroduce the old
language.

## Objective

Write a complete, standalone v2 specification that can be reviewed for an
S-gate signature. It must close every world, estimand, arm, endpoint, and
analysis choice that must precede comparative data. `N3` is the one intended
post-scout scientific number: define its frozen precision rule and capacity
ceiling now, but do not invent its realized value.

Create both:

1. `experiments/level_1_contact/SCIENTIFIC_SPEC_V2_DRAFT.md`
2. `reviews/fable_level1_spec_v2_closure.md`

Preserve the committed v1 draft unchanged. The closure memo must map every Opus
Critical/Major/Minor and every Sol Major/Minor finding to an exact v2 section,
or give a reasoned rejection. Nothing may disappear silently.

Use exactly one verdict in the closure memo:

- `READY_FOR_LEVEL1_S_GATE_REVIEW`
- `REVISE_LEVEL1_WORLD`
- `BLOCKED_LEVEL1_SPEC`

Emit `READY_FOR_LEVEL1_S_GATE_REVIEW` only if the v2 document is executable as
a scientific contract and its remaining blanks cannot change the world,
estimand, unit, endpoint, arm behavior, or decision rule.

## Mandatory repairs

### 1. Honest scope and finite world supply

Keep pure `Z/n` unless the arithmetic proves it unusable. State that Level 1 C1
tests target-adaptive **probe-scale choice for a hidden modulus** under this
specific learner and acquisition rule, not active learning in general.

Close jointly, with exact candidate values and proofs:

- the finite registered `n` population and its strata;
- disjoint development, target, and donor allocations;
- the capacity inequality needed for `2*N3 + N_dev` distinct values per
  relevant stratum, or a better exact construction;
- `2*N2 >= n_max` for a one-period witness, strengthened as required by the
  selected multi-period evaluator probes;
- the maximum admissible post-scout `N3` and what happens if the precision rule
  asks for more blocks than the registry can supply;
- the donor-target distance distribution, its scientific justification, and
  its mandatory mediator report.

Prefer a construction that controls donor distance by design rather than a
broad size band followed by narrative adjustment. If adjacent or otherwise
fixed-distance target/donor pairs are used, define role randomization,
stratification, allocation, and the resulting assignment-conditioned scope.

### 2. One pool, two levels, no privileged semantic leak

Replace raw-word candidate cells with an exact two-level contract:

- a semantic design geometry that removes raw-word multiplicity as an arm
  advantage and caps trivial difference-zero cells;
- a seeded, fixed-multiplicity syntactic realization map that supplies raw
  `{R,L}` word pairs to the learner;
- one stable query index and one admissible pool shared by target ACTIVE, donor
  ACTIVE, YOKED, and RANDOM-STATIC;
- a world-independent pool within the declared registry/stratum so the mere
  candidate set, query ids, shortlist, or syntax distribution cannot reveal
  target `n`;
- an arm-independent shortlist rule, if any, with a proof that the full
  admissible support and estimand are unchanged;
- a complete enumeration verifier and a proof that pool size cannot be
  exhausted within B.

Do not silently give ACTIVE the displacement, difference class, semantic group,
label balance, or any other privileged metadata. Resolve explicitly how ACTIVE
scores opaque raw realizations while the offline verifier can still audit
semantic balance. Pool grouping or aggregation visible to the acquisition
policy counts as a possible `net`/abelianization leak and must be either removed
or defended mechanically.

Also resolve the interaction between a world-independent pool and Opus's phrase
"balanced over the periodicity structure": candidate geometry must not depend
on hidden `n`, and realized answer balance remains a mediator rather than a
matched treatment variable.

### 3. Learner and acquisition rule

Freeze the trajectory-bearing contract exactly enough to implement after the
S-gate:

- learner architecture and raw-word encoding;
- shared within-block initialization and domain-separated stochastic streams;
- optimizer, update count, replay/history view, calibration, and checkpoint
  state;
- ACTIVE uncertainty rule with an early-signal justification;
- deterministic tie-breaking and the answered-query/repeat policy;
- RANDOM-STATIC distribution over the same opaque pool;
- selection-compute accounting and a mechanical side-effect-free scorer
  contract covering parameters, optimizer, normalization state, caches, and RNG.

Prefer committee/disagreement acquisition unless a weaker scalar is explicitly
scoped and justified. All three arms must carry the same learner capacity and
training work; acquisition inference compute is reported separately and cannot
mutate the learner.

Choose exact pre-scout candidate values for model size, ensemble size, B,
updates, replay, and seeds from mathematical/resource bounds or declared
conservative design requirements, never imagined arm effects. Distinguish
learner seeds as repeated measures from world blocks.

### 4. Certified solve that cannot be a lookup table

Replace the generic balanced panel with a precise family-independent cyclic
certificate. It must include:

- held-out raw realizations and held-out semantic displacement classes;
- all required residue classes under the locked construction;
- wrap positives and matched near-miss negatives;
- explicit periodicity probes `k*n` versus `k*n +/- 1`, with selected `k`
  values and the resulting N2/grammar coverage proof;
- symmetry/orientation, word-length, length-imbalance, and relation strata;
- separate constraints within the periodicity stratum so global accuracy or an
  ABSTAIN budget cannot hide failure exactly where the modulus is tested;
- calibration, ABSTAIN, confident-lie, and class-balance rules;
- a proof that syntax memorization, displacement lookup over contacted support,
  and "unequal unless identical" cannot pass.

Clarify what "never contacted" means at raw-query and semantic-class levels.
If evaluator probes extend beyond the acquisition pool, justify that
extrapolation as part of the claimed certificate and ensure the learner input
contract supports it without exposing `n`.

The evaluator runs post-B over frozen checkpoints. Its panel, labels, thresholds,
and solve results stay sealed from learner, acquisition, and researcher until
explicit outcome authorization.

### 5. Event time, censoring, and inference

Freeze:

- evaluation cadence and persistence window;
- whether event time is the first qualifying observation or its later
  confirmation observation;
- the interval/cadence convention and the last-window boundary at B;
- administrative right-censoring and the all/few-solve rule;
- seed aggregation inside a target+unique-donor block;
- the exact stratified finite-population estimator with finite-population
  correction, assignment-conditioned scope, and simultaneous uncertainty for
  all three pairwise arm contrasts;
- `SUP`, `EQ`, `NI`, and `NONSUP` directions on one benefit scale;
- familywise/multiplicity handling and the total contact-mode selector;
- rules routing unresolved, non-transitive, all-censored, or incoherent patterns
  to `INSUFFICIENT`, never equivalence or success.

Because censoring is only administrative at common B, consider whether the
primary RMST can be represented exactly as the finite-population mean of
`min(T, B)` and state the consequences. Do not let "all arms reached B" become
evidence of equivalence by arithmetic convention.

All N6 margins and solve thresholds must have non-comparative scientific or
mathematical provenance. The scout may estimate variance, covariance,
censoring, feasibility, and precision only.

### 6. Invalidity, scout boundary, and escrow

Make the invalidity cascade executable:

- distinguish block invalidity, design invalidity, incomplete evidence, and a
  resolved negative result;
- state whether any invalid block aborts or whether a blinded replacement rule
  exists; no silent exclusion;
- treat shuffled-answer and pre-contact encoding success as design-invalidating
  development gates, while post-contact transcript structure remains a
  legitimate mediator;
- freeze donor balance, missing-run, non-finite-state, resume-integrity, and
  deterministic-replay consequences;
- list exactly what the development scout may record and the outcome-independent
  resource wall.

Repair procedural escrow for a low-entropy finite world:

- confidentiality rests on public-key encryption, not a plaintext hash;
- the integrity commitment uses a high-entropy secret salt stored inside the
  ciphertext and released only at authorized outcome;
- the plaintext validator stays inside the isolated generator environment and
  emits only the locked proof/attestation surface;
- evaluator output is sealed;
- isolated filesystem, log/stdout/shell-history controls, wipe, one-generation
  rule, and malformed-generation termination are explicit;
- LOCAL_LLAMA remains generator/witness only; Kirill retains procedural custody,
  and no cryptographic independence is claimed.

### 7. Gate and implementation boundary

Give a final gate ledger separating:

1. neutral dummy-fixture substrate;
2. candidate-pool/evaluator/learner implementation;
3. S-gate signature;
4. comparative scout driver and execution;
5. N3 closure and Level 1 lock;
6. real escrow;
7. outcome driver and execution.

Reconcile the reviewers conservatively: Sol's broad statement that candidate-
pool machinery may be implemented now does not override Opus CR-2. Until this
v2 contract is reviewed and signed, only the pure oracle, fail-closed dataflow,
salt-capable commitments, and donor bookkeeping on dummy fixtures are neutral.

## Required closure memo

In `reviews/fable_level1_spec_v2_closure.md`, include:

1. the single verdict token;
2. a finding-by-finding disposition table for both reviewers;
3. an exact list of choices still requiring Kirill's authorial signature;
4. explicit negative space: what Level 1 can never establish;
5. a reviewer handoff with precise questions for Opus and Sol;
6. an implementation authorization for Codex/Cursor that names modules allowed
   before and after S-gate;
7. confirmation that no comparative datum, scout, escrow, lock, or outcome was
   created.

Preserve all signed negative destinations and the two-layer Proof definition.
Do not treat a C1 failure as programme falsification, an UNKNOWN as a boundary,
or a Level 1 success as evidence for `PROOF_CORE`.
