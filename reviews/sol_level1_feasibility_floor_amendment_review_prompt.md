# GPT-5.6 Sol prompt: Level 1 feasibility-floor amendment Y-line review

Perform an independent bounded Y-line review of Fable's proposed Level 1
feasibility-floor amendment. Focus on inference discipline, treatment meaning,
and whether the binary development observation licenses the proposed branch.
Do not implement code, execute any trajectory, inspect or reconstruct a series,
compare arms, select N3, create a lock, or generate a panel/escrow.

## Read

1. `experiments/level_1_contact/FEASIBILITY_GATE_DECISION_DRAFT.md`
2. `reviews/fable_level1_feasibility_gate_closure.md`
3. `experiments/level_1_contact/SCIENTIFIC_SPEC_V3_1_ADDENDUM.md` A8-A9
4. `experiments/level_1_contact/SCIENTIFIC_SPEC_V3_1_1_CORRECTION.md` C6-C7
5. `experiments/level_1_contact/SCIENTIFIC_SPEC_V3_DRAFT.md`
6. `experiments/level_1_contact/feasibility/LEVEL1_NONCOMPARATIVE_FEASIBILITY.json`
7. `reviews/sol_level1_feasibility_scope_review.md`
8. `experiments/level_0_grokking/OUTCOME_RESULT.md`
9. `experiments/level_0_grokking/SCIENTIFIC_SPEC.json`

The only performance observation is the frozen binary
`censored_at_b:true` on one RANDOM-STATIC n=66 development fixture. It is valid,
non-outcome evidence and cannot be generalized to other worlds or arms.

## Candidate under review

The candidate changes minibatch-32 replay to one full-history, CE-mean AdamW
update per oracle answer, identically for every arm. B=2000 queries, U=1,
endpoint, cadence, persistence, panel, margins, N3 rule, population, donor yoke,
and arm definitions stay fixed. A new one-shot v2 binary check on the same
fixture would pass to comparative-scout review or, if censored, terminate Level
1 feasibility with no third intervention.

## Required questions

### Y1. What does the binary result license?

- Confirm or reject Fable's branch 1 reading of A8/C6/C7.
- Determine whether one censored fixture licenses a training-policy amendment,
  or only records a floor failure under the original learner.
- Explicitly assess the unsupported-looking statements that the development
  contrasts would "predictably" be all-censored and that the outcome battery
  would be designed to return `INSUFFICIENT`. Require those claims withdrawn if
  they exceed the one-fixture observation.
- Ensure a v2 pass remains a gate condition only, never evidence for an arm or
  for C1.

### Y2. Is full-history training inferentially inert?

- It is applied identically to all arms, but it changes the learner policy and
  gives earlier observations more optimizer-step exposure. Decide whether the
  ACTIVE-vs-YOKED estimand remains the same scientific estimand or becomes a new
  learner-class conditional estimand requiring a loud amendment to scope.
- Decide whether retiring stochastic replay removes a relevant nuisance source
  without favoring an arm, or changes the meaning of retained contact history.
- Verify that query budget and training compute remain matched across arms at
  each t, including donor ACTIVE generation and committee members.

### Y3. Audit the Level 0 provenance claim

Fable uses Level 0's full-batch grokking result as the only external
non-comparative anchor and counts example evaluations. Under mean CE, the
optimizer still takes only 2,000 updates in Level 1, versus roughly 5,200-7,700
updates at Level 0 generalization; architecture, sequence length, task, and
decay differ. Decide whether Level 0 supports:

- choosing full-history as the unique repair;
- only the weaker claim that full-batch AdamW is executable on this platform;
- or no choice among learner repairs.

Assess whether the proposed change is genuinely parameter-free or an
outcome-triggered capacity increase. The signed A8 permission is relevant, but
must not become a license for a preferred result.

### Y4. Decision and invalidity semantics

- Is the same-fixture, same-criterion v2 check an acceptable binary gate after a
  signed amendment, or an impermissible second look?
- Is `pass -> comparative-scout review; censored -> BLOCKED_LEVEL1_FEASIBILITY`
  deterministic and conservative?
- Separate scientific censoring from environment, resource, process, hash, and
  seal invalidity. No invalid run may be narrated as learner-floor evidence;
  no route may silently authorize another feasibility intervention.
- Decide how the canonical ledger and ROADMAP should name a valid second
  censoring versus a process-invalid v2.

### Y5. Resource claims

The exact work ratio is 31.51, but the 30h estimate is derived by linear scaling
of a minibatch-32 component. Determine whether it may be called an upper bound,
or only a planning projection. Assess whether the 36h cap is independent of the
desired pass/fail result and whether timeout semantics preserve validity.

## Deliverable

Write `reviews/sol_level1_feasibility_floor_amendment_review.md` with exactly one
verdict:

- `LEVEL1_FEASIBILITY_FLOOR_AMENDMENT_YLINE_CONFIRMED`
- `REVISE_LEVEL1_FEASIBILITY_FLOOR_AMENDMENT`
- `REJECT_LEVEL1_FEASIBILITY_FLOOR_AMENDMENT`

Lead with Critical/Major/Minor findings and exact mandatory edits. Include an
allowed/forbidden interpretation table for v1 censoring, v2 pass, v2 censoring,
and v2 process invalidity. Answer whether the author token
`I_ACCEPT_LEVEL1_FEASIBILITY_FLOOR_AMENDMENT` is signable after bounded repairs
or requires a new final check.

Preserve every signed negative destination and the rule that Level 1 is a
detector, not programme evidence. Confirm that you created no code, entropy,
comparative datum, N3, lock, panel, escrow, trajectory, or outcome.
