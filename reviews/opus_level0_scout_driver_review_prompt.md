# Relay prompt: Opus 4.8 review of Level 0 scout driver

Review commit `5ea236b` in `/home/master/llm_projects/philosophia` against
`7f4ca5f`. This is the bounded orchestration review required by your
`HARDENING_ACCEPTED` decision before the single scout execution.

Do not execute the scout. Unit tests, source inspection, and pure helper checks
are allowed. Ignore the unrelated untracked `essay/OUTLINE.md`.

Read:

- `reviews/opus_level0_hardening_review.md`
- `experiments/level_0_grokking/EXECUTION_INTERLOCK.md`
- `src/philosophia/level0/{scout,interlock,train,checkpoint,data}.py`
- `scripts/level0_timing_storage_scout.py`
- `tests/test_level0_scout_driver.py`

Local verification: 58 tests pass; both repository verifiers pass. No scout
report/checkpoint, `PREREG.lock`, or `decision.json` exists.

## Driver summary to verify

- Arm A, master seed 0, canonical CPU float32 only.
- One scout capability is consumed by the driver and nowhere else.
- 25 primary full-batch steps + 25 independent replay steps = 50 total, below
  the reviewed 100-step hard cap.
- A 120-second deadline is checked around every step.
- No metrics import, held-out view access, evaluation, persistence verdict, or
  persisted loss value/series.
- One purpose-tagged checkpoint is saved and loaded; its byte size and hash are
  recorded.
- Only aggregate primary-step latency, process peak RSS, checkpoint size, and
  combined model/optimizer deterministic prefix hashes enter the JSON report.
- Existing report/checkpoint paths cause a fail-closed refusal.
- The driver has not been run.

## Questions

1. Is 25+25 a valid interpretation of one ≤100-step scout, including the
   independent determinism replay?
2. Does the wall-clock enforcement cover setup/checkpoint/replay sufficiently,
   including the fact that an individual PyTorch step cannot be interrupted?
3. Are RSS and latency aggregates scientifically adequate for resource
   projection without becoming a learning curve?
4. Does the checkpoint purpose tag plus filenames satisfy the artifact
   contamination label?
5. Can any code path touch held-out targets, persist train loss, derive a
   verdict, exceed caps, overwrite a previous scout, or create lock/decision
   artifacts accidentally?
6. Is checkpoint schema 3's required `purpose` field correct and compatible
   with the accepted integrity contract?
7. Specify the exact approved output directory. Prefer a path whose JSON report
   can later be admitted while the ignored checkpoint remains local.
8. If accepted, may Codex execute the command exactly once and commit only the
   non-outcome JSON report plus documentation derived from its resource numbers?

## Required response

Write the review to `reviews/opus_level0_scout_driver_review.md` and do not
commit it. Start with exactly one:

- `SCOUT_DRIVER_ACCEPTED`
- `REVISE_SCOUT_DRIVER`
- `BLOCKED`

Then provide:

1. Critical/Major/Minor findings with file/line references.
2. Mandatory code/test edits, if any.
3. Exact execution authorization: command, output directory, and one-run guards.
4. Allowed report fields and forbidden interpretations.
5. Whether the JSON report may be committed after inspection.
6. Which lock-stage resource cells the scout may inform, and which scientific
   cells it cannot resolve.

Do not run the driver, predict grokking, inspect a learning curve, or choose
scientific outcome thresholds.
