# Fable 5 prompt: reconcile the Level 1 feasibility-floor amendment

Write a bounded v2 amendment candidate that reconciles the Opus X-line and Sol
Y-line reviews. Preserve the original Fable candidate as the reviewed historical
artifact; do not edit it. Do not implement code, execute a trajectory or resource
probe, inspect/reconstruct a series, compare arms, select N3, create an
authorization, assert Kirill's token, create a lock, or generate panel/escrow.

## Read

1. `experiments/level_1_contact/FEASIBILITY_GATE_DECISION_DRAFT.md`
2. `reviews/fable_level1_feasibility_gate_closure.md`
3. `reviews/opus_level1_feasibility_floor_amendment_review.md`
4. `reviews/sol_level1_feasibility_floor_amendment_review.md`
5. `experiments/level_1_contact/SCIENTIFIC_SPEC_V3_DRAFT.md` sections 5-8
6. `experiments/level_1_contact/SCIENTIFIC_SPEC_V3_1_ADDENDUM.md` A2, A5-A10
7. `experiments/level_1_contact/SCIENTIFIC_SPEC_V3_1_1_CORRECTION.md` C2, C4, C6-C7
8. `experiments/level_1_contact/SCIENTIFIC_SPEC_SIGNATURES.md`
9. `experiments/level_1_contact/feasibility/LEVEL1_NONCOMPARATIVE_FEASIBILITY.json`
10. `experiments/level_0_grokking/OUTCOME_RESULT.md`

Formal reviews govern; chat captures are provenance only. Adopt every compatible
Opus/Sol mandatory edit. If they differ, choose the more conservative route and
name the disposition rather than hiding it.

## Closed decisions: do not reopen

- Branch 1 is correct: the original learner is blocked at the feasibility gate;
  a signed floor amendment may be reviewed before any comparative scout.
- The only candidate remains one full-history, CE-mean AdamW update per oracle
  answer, applied identically to every target and donor learner. Do not introduce
  alternatives or a numeric tuning range.
- B=2000 queries, U=1, model, optimizer settings, committee size, endpoint,
  cadence, persistence, panel, margins, population, yoke, selector, and N3 rule
  remain frozen.
- The v1 evidence and authorization are immutable and non-outcome.
- A valid v2 pass opens only comparative-scout **review**. A valid v2 censoring
  blocks this Level 1 learner route with C1 untested and no third learner-policy
  intervention.
- No v2 process/resource/hash/seal invalidity may be narrated as censoring or a
  learner-floor result.

## Mandatory reconciliation

### R1. Narrow the v1 inference

Use the Sol replacement meaning: v1 establishes only a floor failure on the one
frozen original-policy RANDOM-STATIC n=66 fixture. It blocks spending the scout
under the original learner and permits, but does not empirically select, a signed
floor amendment. Delete every statement that other worlds/arms would be
all-censored or that a battery would be designed to return `INSUFFICIENT`.

### R2. State the learner-class amendment honestly

Full-history training has **no new numeric hyperparameter**, but it is a
substantive capacity/optimization-policy and temporal-weighting change, not an
inferentially inert edit. Add literal scope text:

> All Level 1 potential outcomes and contrasts are conditional on the
> full-history, mean-CE, one-update-per-answer learner policy. This replaces the
> stochastic replay learner class; it preserves the high-level ACTIVE-vs-YOKED
> question and estimator form but defines a new learner-class conditional
> estimand.

Name the temporal weighting: contact 1 participates in all 2000 later/current
updates while contact 2000 participates once. State that applying the same rule
to every learner prevents an arm-label implementation asymmetry but does not
make the learner intervention neutral.

### R3. Correct the Level 0 provenance and work arithmetic

- Both v1 and v2 take exactly 2000 optimizer updates.
- `63,504` and `2,001,000` count example **evaluations**, not gradients,
  conserved gradient mass, or learning-capacity units.
- `31.5098...` is a compute-work ratio only.
- Level 0 is only an engineering precedent that full-batch AdamW with the same
  optimizer family/betas ran on this platform for a different locked task. It
  supplies no choice among Level 1 repairs, update-count floor, solve
  probability, or prediction.
- The defensible non-empirical reasons for retaining this sole candidate are its
  simplicity, determinism, full use of declared contact history, and removal of
  replay sampling. Do not call the v1 failure mechanically unsurprising.

### R4. Provide literal signed replacement text

Write exact replacement text for every changed governing cell in v3 section 5,
v3.1 A2/A5, and v3.1.1 C2/C4 as needed:

- at oracle step t, assemble all t answered pairs in canonical contact-schedule
  order;
- one shared full-history tensor is used by all four committee members, with
  each member taking exactly one forward/backward/AdamW step and zeroing grads;
- CE reduction mean; U=1 unchanged; no chunking;
- the replay PRF domain is retired and consumes no digest/counter;
- prove domain separation means its retirement perturbs no allocation, init,
  shortlist, control, feasibility, or other stream;
- batch order is pinned for deterministic bytes even though mean CE is
  permutation-invariant in exact arithmetic;
- scorer state-hash/noninterference contracts remain unchanged.

### R5. Resource matching and projection

Add a table for target ACTIVE, donor ACTIVE, YOKED target, and RANDOM-STATIC at
each t: oracle answers accessible to that learner, committee size, update count,
batch size, scorer work, and donor-generation work. Say precisely:

- target scientific query exposure and per-trajectory training work are matched;
- total arm-package compute is not matched because ACTIVE scoring and YOKED donor
  generation are treatment machinery and belong in the later operational ledger;
- donor answers/state never enter the YOKED learner, only frozen query geometry.

Replace "upper bound" with **30 h linear-scaling planning projection**. The 36 h
wall is frozen outcome-independently but is not known sufficient. It is checked
without consulting panel performance. A partial wall-stopped run has no
`censored_at_b` value.

### R6. Make the v2 artifact contract bit-exact

Freeze these names:

- authorization path:
  `experiments/level_1_contact/FEASIBILITY_EXECUTION_AUTHORIZATION_V2.json`;
- output directory: `experiments/level_1_contact/feasibility_v2/`;
- claim:
  `LEVEL1_NONCOMPARATIVE_FEASIBILITY_V2_CLAIM.json`;
- report: `LEVEL1_NONCOMPARATIVE_FEASIBILITY_V2.json`;
- authorization schema:
  `philosophia.level1.feasibility-authorization.v2`;
- claim schema: `philosophia.level1.feasibility-run-claim.v2`;
- report schema: `philosophia.level1.noncomparative-feasibility.v2`;
- execution token: `I_AUTHORIZE_LEVEL1_NONCOMPARATIVE_FEASIBILITY_V2`;
- caps: `{development_worlds:1, trajectory_steps:2000, scorer_steps:0,
  wall_seconds:129600}`;
- arm/world: `RANDOM-STATIC`, `{pair_slot:0, modulus:66}`.

Require canonical JSON, exact environment, clean tracked tree/empty index,
EXPECTED_HEAD==HEAD, source-byte pins over every amended/reachable module, and
the committed amendment hash. Preflight must recompute and verify the exact v1
claim/report SHA-256 values, refuse if either is missing or mutated, refuse on
any v2 claim/report path already existing, and refuse on any later-gate artifact.
The durable claim precedes any learner step; the report is atomic after valid
completion. Do not create the authorization candidate in this task.

### R7. Validity-first terminal table

Provide mutually exclusive routes:

1. valid completed v2, qualifying window: `censored_at_b:false` -> PASS ->
   comparative-scout review only, no arm/C1/programme inference;
2. valid completed v2, no qualifying window: `censored_at_b:true` ->
   `BLOCKED_LEVEL1_FEASIBILITY`, C1 untested, no third learner intervention;
3. validly recorded scientific non-finiteness: preserve the already signed A6
   rule (a completed earlier window stands; otherwise scientific censoring with
   the non-finite flag), never relabel it a hardware crash;
4. environment/resource-cap/process fault: `LEVEL1_FEASIBILITY_V2_INVALID:<cause>`,
   `censored_at_b` unset, no learner inference and no automatic retry;
5. hash/seal/evidence/source violation: fail closed / whole-check invalidity,
   no learner evidence.

Reconcile the only reviewer nuance conservatively: an invalid run authorizes
nothing automatically. Any future mechanically justified resource recovery
would require a new explicit Kirill-signed process/resource decision and bounded
review with the learner rule unchanged; it is not a third floor amendment, but
this amendment does not pre-authorize it.

Add the exact future canonical ledger and ROADMAP status lines required by Sol
for valid v2 censoring and each invalidity class. Do not edit the ledger or
ROADMAP now.

## Deliverables

Write exactly:

1. `experiments/level_1_contact/FEASIBILITY_FLOOR_AMENDMENT_V2_DRAFT.md`
2. `reviews/fable_level1_feasibility_floor_amendment_v2_closure.md`

Use exactly one verdict:

- `READY_FOR_LEVEL1_FEASIBILITY_FLOOR_AMENDMENT_FINAL_CHECK`
- `REVISE_LEVEL1_FEASIBILITY_FLOOR_AMENDMENT_V2`
- `BLOCKED_LEVEL1_FEASIBILITY_AMENDMENT`

The closure must disposition every Opus AM-1 through AM-7 and every Sol C/M/m
finding, explicitly identifying the strictest resolution where the reviews
differ. Include two bounded final-confirmation questions for Opus and two for
Sol. The author token remains
`I_ACCEPT_LEVEL1_FEASIBILITY_FLOOR_AMENDMENT`, but state that it is not signable
until both final confirmations accept this v2 text.

Confirm that no code, authorization, entropy, resource probe, trajectory,
comparative datum, N3, lock, panel, escrow, or outcome was created.
