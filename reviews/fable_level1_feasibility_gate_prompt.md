# Fable 5 prompt: Level 1 feasibility-gate decision

Review the completed, committed **non-comparative feasibility gate** and decide
the next scientifically permitted branch. This is a bounded gate decision, not
an invitation to tune Level 1. Do not run code, inspect or reconstruct a loss,
query, score, or solve series, compare arms, select N3, generate escrow, create a
lock, or predict an outcome.

## Read first

1. `experiments/level_1_contact/SCIENTIFIC_SPEC_V3_DRAFT.md`
2. `experiments/level_1_contact/SCIENTIFIC_SPEC_V3_1_ADDENDUM.md`, especially A8-A9
3. `experiments/level_1_contact/SCIENTIFIC_SPEC_V3_1_1_CORRECTION.md`, especially C6-C7
4. `experiments/level_1_contact/SCIENTIFIC_SPEC_V3_1_2_CORRECTION.md`
5. `experiments/level_1_contact/SCIENTIFIC_SPEC_V3_1_4_PANEL_ADDENDUM.md`
6. `experiments/level_1_contact/SCIENTIFIC_SPEC_V3_1_4_1_CORRECTION.md`
7. `experiments/level_1_contact/SCIENTIFIC_SPEC_SIGNATURES.md`
8. `experiments/level_1_contact/FEASIBILITY_EXECUTION_AUTHORIZATION.json`
9. `experiments/level_1_contact/feasibility/LEVEL1_NONCOMPARATIVE_FEASIBILITY_CLAIM.json`
10. `experiments/level_1_contact/feasibility/LEVEL1_NONCOMPARATIVE_FEASIBILITY.json`
11. `reviews/sol_level1_feasibility_scope_review.md`
12. `reviews/opus_level1_feasibility_hardening_confirmation.md`
13. `ROADMAP.md`

The canonical JSON artifacts and formal reviews govern. Chat captures are
provenance only. The raw claim/report are immutable and must remain non-citable
`scientific_outcome:false` evidence.

## Facts already verified by Codex

- execution HEAD: `c89a6b6c92af7b4aae0cae9626693d042c922147`;
- evidence commit: `052a341`;
- canonical claim SHA-256:
  `357baef22226bfb92b909192d2264420923facd55115b9c272bb2cb848c106ab`;
- canonical report SHA-256:
  `1c3843ec66f57e8a7e05b88d5f942093113f11f5ac36746f202f1a6556820b7f`;
- authorization and public-root hash links verify;
- all 200 scorer steps and 2,000 trajectory steps completed;
- all scorer values and losses were finite; the dummy panel was computable;
- learner state was unchanged by scorer measurement;
- every contamination guard is false;
- `censored_at_b:true`;
- RANDOM-STATIC component projection: about 3,437 s for B;
- ACTIVE scorer-only component projection: about 14,467 s for B;
- combined component projection: about 17,904 s, explicitly not a full Level 1
  runtime forecast;
- peak RSS: 1,474,896 KiB; checkpoint estimate: 25,768,935 bytes;
- 143 tests pass; inheritance and both existing decision verifiers are valid;
- no comparative scout, N3 selection, preregistration lock, real panel, escrow,
  or Level 1 outcome exists.

The signed interpretation is narrow: `censored_at_b:true` says only that the
single predeclared RANDOM-STATIC development fixture did not complete a
five-checkpoint dummy-panel solve window within B. It does not say that the
learner lacks the modulus, that RANDOM-STATIC is inferior, or that Level 1 is
false.

## Governing tension to resolve

A8 says the censoring indicator may justify only a **binary feasibility-floor
amendment**: the locked architecture/B produced at least one complete
development solve, or did not. Any change requires a signed addendum and repeat
review before S-gate completion. C6 says a lock may be blocked by
`feasibility-gate failure`. C7 places reviewed optional feasibility before the
comparative scout.

Determine whether the observed `true` censoring:

1. blocks the comparative scout pending an amendment;
2. permits the scout under the current signed contract; or
3. blocks Level 1 without an honest bounded repair.

Do not resolve ambiguity in favor of progress. `UNKNOWN` and censored are never
success.

## Required scientific discipline

- The completed execution is one-shot. It may not be deleted, repeated, renamed,
  or treated as a failed attempt.
- No value may be chosen from an unpersisted trajectory or by trying multiple
  architectures, budgets, update counts, thresholds, panels, or optimizers.
- Do not change the endpoint, panel criteria, persistence window, inference
  margins, C1 scope, operational certificate, arm definitions, donor yoke,
  population, or estimator.
- Do not use the timing fields as arm comparisons or as a full-run guarantee.
- Preserve the distinction between a **new amended feasibility experiment** and
  a rerun. If a new check is needed, it requires a new schema/path, new reviewed
  code HEAD, new explicit Kirill token, fail-closed refusal on existing
  artifacts, and an immutable link to this censored report.
- A repair must be single-valued and justified from the binary floor failure
  plus architecture/task mechanics or an external non-comparative anchor. It
  must not optimize toward a desired solve rate.
- State explicitly whether a second binary check can authorize the comparative
  scout, what pass/fail means, and what happens if it is censored again.
- Preserve every signed negative destination and the rule that Level 1 remains a
  detector, not a programme falsifier.

## Deliverables

Write exactly two files, leaving all earlier specs and evidence untouched:

1. `experiments/level_1_contact/FEASIBILITY_GATE_DECISION_DRAFT.md`
2. `reviews/fable_level1_feasibility_gate_closure.md`

Use exactly one primary verdict:

- `READY_FOR_LEVEL1_COMPARATIVE_SCOUT_REVIEW`
- `READY_FOR_LEVEL1_FEASIBILITY_FLOOR_AMENDMENT_REVIEW`
- `BLOCKED_LEVEL1_FEASIBILITY`

If the verdict is `READY_FOR_LEVEL1_FEASIBILITY_FLOOR_AMENDMENT_REVIEW`, the
decision draft must contain one exact normative amendment, not alternatives:

1. the one frozen change and why the binary observation licenses that class of
   change;
2. every unchanged scientific and implementation cell;
3. an exact amended feasibility protocol and allowed report surface;
4. a new one-shot artifact schema/path/token and no-delete/no-retry behavior;
5. a deterministic pass/fail route: pass -> comparative-scout review; censored
   or invalid -> a named blocked/boundary destination with no third attempt;
6. resource implications using the existing aggregates only as component
   projections;
7. the author signature token required after bounded Opus and Sol reviews.

If the current contract already permits proceeding, quote the exact governing
text and explain why C6's `feasibility-gate failure` does not apply. If Level 1
must stop, name precisely which claim remains untested and why no bounded repair
is scientifically honest.

The closure memo must disposition A8, C6, C7, the allowed/forbidden table, every
resource field, and the no-rerun rule. Include three sharp bounded questions for
Opus and three for Sol. Confirm that you created no code, entropy, data, scout,
N3 selection, lock, panel, escrow, trajectory, or outcome.
