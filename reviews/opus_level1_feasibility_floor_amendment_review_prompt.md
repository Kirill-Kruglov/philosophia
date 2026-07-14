# Opus 4.8 prompt: Level 1 feasibility-floor amendment X-line review

Perform a hostile but bounded X-line review of Fable's proposed Level 1
feasibility-floor amendment. Review the candidate as written; do not edit it,
write implementation code, execute a trajectory, inspect or reconstruct a
series, compare arms, select N3, create a lock, or generate a panel/escrow.

## Read

1. `experiments/level_1_contact/FEASIBILITY_GATE_DECISION_DRAFT.md`
2. `reviews/fable_level1_feasibility_gate_closure.md`
3. `experiments/level_1_contact/SCIENTIFIC_SPEC_V3_1_ADDENDUM.md` A8-A9
4. `experiments/level_1_contact/SCIENTIFIC_SPEC_V3_1_1_CORRECTION.md` C6-C7
5. `experiments/level_1_contact/SCIENTIFIC_SPEC_V3_DRAFT.md` learner and endpoint
6. `experiments/level_1_contact/feasibility/LEVEL1_NONCOMPARATIVE_FEASIBILITY.json`
7. `reviews/sol_level1_feasibility_scope_review.md`
8. `experiments/level_0_grokking/OUTCOME_RESULT.md`
9. `experiments/level_0_grokking/SCIENTIFIC_SPEC.json`
10. `experiments/level_0_grokking/COMPANION_CONFIG_TRACE.md`
11. `src/philosophia/level1/{acquisition,config,feasibility,model,train,interlock}.py`

The v1 evidence is immutable and non-outcome. `censored_at_b:true` means only
that one RANDOM-STATIC development fixture did not complete the frozen solve
window within B. It is not evidence that other worlds or arms would censor.

## Candidate under review

The sole proposed change is minibatch-32 replay -> exactly one AdamW step per
oracle answer on the entire accumulated own history as one unchunked full batch,
identically for every arm. B, U=1, model, optimizer settings, panel, endpoint,
cadence, persistence, margins, population, selector, and inference remain fixed.
The proposed v2 gate uses the same fixture and binary criterion, a new one-shot
path/schema/token linked to v1, and a 36-hour wall. Pass opens comparative-scout
review; censoring or invalidity blocks Level 1 with no third attempt.

## Required attacks

### X1. Is the repair scientifically licensed and genuinely single-valued?

- Decide whether "all accumulated history" is parameter-free in the relevant
  sense, or a substantive learner-capacity/training-policy change that needs a
  more explicit signed cell than Fable provides.
- Trace the implicit temporal weighting: an early contact participates in many
  more optimizer steps than a late contact. Decide whether that is a legitimate
  consequence of online full-history training and whether it changes the C1
  treatment interpretation despite being applied to all arms.
- Verify that retirement of replay PRF streams cannot perturb any other stream
  or allocation counter and that the exact history order and tensor
  serialization are already single-valued or must be pinned.

### X2. Audit the Level 0 anchor rather than accepting "example-gradients"

The arithmetic is correct:

- `sum(min(32,t), t=1..2000) = 63,504`;
- `sum(t, t=1..2000) = 2,001,000`;
- ratio about `31.51`.

But under CE `reduction='mean'`, processing 31.5x more examples does not create
31.5x optimizer updates or scale the gradient by 31.5. Level 1 remains at 2,000
updates, while Level 0 generalized at about 5,200-7,700 full-batch updates.
Level 0 also differs in task, sequence length, architecture, decay policy, and
data distribution. Determine exactly what the Level 0 result can anchor:
optimizer family/betas and full-batch viability, sample exposure, update count,
or none of these. Require weaker wording if the candidate overclaims.

### X3. Resource and numerical contract

- Decide whether multiplying the measured minibatch-32 component by 31.51 is a
  planning projection or a defensible upper bound. Batch-dependent kernels,
  memory pressure, allocation, and checkpoint evaluation may invalidate an
  upper-bound claim.
- Audit whether one unchunked batch at t=2000, sequence length 277, four-member
  committee, backward state, and CPU float32 fits the 128 GB platform without
  outcome-bearing scouting. If a bounded shape/memory/timing check is needed,
  specify a non-outcome cap that cannot become a configuration search.
- Decide whether 36h is outcome-independent and whether a resource timeout must
  be distinguished from scientific censoring.

### X4. Bit-exact v2 protocol and failure routes

The draft names claim and authorization schemas but appears not to name the
report schema or authorization file path. Audit all required paths, schemas,
hashes, source-byte pins, HEAD binding, environment enforcement, canonical JSON,
claim-before-run behavior, atomic report creation, and refusal if either v1 or
v2 evidence is missing/mutated.

Separate at least these states:

1. valid v2 + `censored_at_b:false`;
2. valid v2 + `censored_at_b:true`;
3. non-finite learner state under the signed routing;
4. process/resource/environment failure before or after durable claim;
5. evidence/seal/hash violation.

Decide whether Fable's single "censored again, or invalid execution -> BLOCKED"
route improperly converts platform/process invalidity into evidence about the
learner floor. Preserve no quiet retry and no third feasibility intervention.

### X5. Negative space

Reject or require withdrawal of any claim that the one n=66 RANDOM fixture makes
all development contrasts "predictably all-censored" or proves the outcome
battery would be `INSUFFICIENT`. It may motivate a gate block; it cannot predict
unobserved arms/worlds.

## Deliverable

Write `reviews/opus_level1_feasibility_floor_amendment_review.md` with exactly one
verdict:

- `LEVEL1_FEASIBILITY_FLOOR_AMENDMENT_XLINE_CONFIRMED`
- `REVISE_LEVEL1_FEASIBILITY_FLOOR_AMENDMENT`
- `REJECT_LEVEL1_FEASIBILITY_FLOOR_AMENDMENT`

Lead with Critical/Major/Minor findings and exact mandatory edits. Answer:

1. Is branch 1 (amendment before comparative scout) the correct gate route?
2. Is full-history training an honest single repair, and what claim can Level 0
   support?
3. Is a bounded implementation/resource audit eligible before author signature,
   after it, or unnecessary?
4. What exact valid/censored/process-invalid routes must v2 implement?
5. After corrections, may Kirill sign
   `I_ACCEPT_LEVEL1_FEASIBILITY_FLOOR_AMENDMENT`, or is another bounded review
   required?

State the implementation authorization boundary. Confirm that you ran no
feasibility trajectory and created no entropy, comparative datum, N3, lock,
panel, escrow, or outcome.
