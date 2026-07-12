# Claude Opus 4.8 review prompt: Level 0 scientific lock and outcome driver

Perform the final pre-lock adversarial review of Philosophia Level 0. No outcome
run has occurred. Reconstruction v2 and its deterministic prefix were previously
accepted; this review must not reopen faithful cells without new evidence and
must not tune scientific choices toward an expected result.

## Files to inspect

Read the same complete candidate surface:

- `experiments/level_0_grokking/PREREGISTRATION_DRAFT.md`
- `experiments/level_0_grokking/SCIENTIFIC_SPEC.json`
- `experiments/level_0_grokking/ANCHOR_CLAIMS.md`
- `experiments/level_0_grokking/COMPANION_CONFIG_TRACE.md`
- `experiments/level_0_grokking/RECONSTRUCTION_CHOICES_V2.md`
- `experiments/level_0_grokking/RESOURCE_SCOUT.md`
- `experiments/level_0_grokking/EXECUTION_INTERLOCK.md`
- `experiments/level_0_grokking/OUTCOME_RUNBOOK_DRAFT.md`
- `scripts/level0_create_lock.py`
- `scripts/level0_run_outcome.py`
- `scripts/level0_evaluate_battery.py`
- `scripts/level0_verify_decision.py`
- `scripts/verify_all.py`
- `src/philosophia/level0/scientific_spec.py`
- `src/philosophia/level0/interlock.py`
- `src/philosophia/level0/outcome.py`
- `src/philosophia/level0/outcome_evaluator.py`
- `src/philosophia/level0/decision_verifier.py`
- `tests/test_level0_scientific_lock.py`

Prior governing reviews:

- `reviews/opus_level0_hardening_review.md`
- `reviews/opus_level0_scout_driver_review.md`
- `reviews/opus_level0_companion_source_reconciliation_review.md`
- `reviews/opus_level0_companion_v2_fidelity_review.md`

Run the full tests and both repository verifiers if you have local access. Do not
run the outcome driver.

## Required audit

1. Trace every scientific cell from prose to JSON, validation, schema-2 lock,
   runtime interlock, driver, evaluator, independent verifier, and tests. Name
   any asymmetric or hard-coded value that can drift silently.
2. Verify the two-commit provenance model: reviewed/accepted sources are
   committed first; lock records that source commit and hashes; the lock is then
   committed; execution HEAD may only descend from the source commit, locked
   paths remain byte-identical, and `PREREG.lock` is tracked and unchanged.
3. Verify no outcome can run under draft status or without the canonical lock;
   no training module derives a predicate; the evaluator cannot optimize; no
   decision appears before all nine fixed-budget completion reports.
4. Verify exact resume behavior at a normal checkpoint and at interruption
   between metric append, snapshot, resume replacement, and archival copy.
   Audit the hash-only recovery log and ensure recovery cannot discard multiple
   or outcome-selected observations.
5. Verify model/optimizer/scheduler and metrics/manifest/final-report integrity,
   fixed budgets, cadence, wall clocks, per-run and battery artifact ceilings,
   non-finite behavior, no early success/failure stop, and no warm start.
6. Verify decision logic: A 4/5 only, B 1/3 annotation only, all real-label FIT,
   R-0 FIT and not GENERALIZE, and exact persistence/delay boundary behavior.
7. Review the two-terminal runbook. State whether A and B may run concurrently
   on the locked CPU without altering semantics; flag only concrete integrity or
   deterministic-platform issues, not mere performance uncertainty.
8. Look for a shape-correct, test-green but trajectory/outcome-wrong mutation
   still admitted by the new test surface.

## Output contract

Write the review to
`reviews/opus_level0_scientific_lock_outcome_review.md` and do not commit it.
Use exactly one verdict:

- `LOCK_CANDIDATE_ACCEPTED`
- `REVISE_LOCK`
- `REJECT_DESIGN`
- `BLOCKED_SOURCE`

Findings first, ordered Critical/Major/Minor with file/line references and exact
mandatory edits. Then answer separately:

- May the candidate implementation/spec be committed before signature?
- After Sol/Opus findings are closed, may Kirill set status to
  `accepted-by-kirill-before-outcome`?
- May the canonical lock script then run exactly once and its result be committed?
- Only after that lock commit, may Codex give Kirill the runbook commands?
- Are two distinct run-id processes authorized concurrently?

Do not create a lock, outcome directory, checkpoint, metric, or decision. Do not
predict grokking or infer Philosophia's thesis from a future Level 0 result.
