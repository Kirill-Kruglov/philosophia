# GPT-5.6 Sol review prompt: Level 0 scientific lock and outcome system

You are the independent scientific/statistical reviewer for Philosophia Level 0.
No outcome run has occurred. The candidate preregistration and driver are a
pre-outcome draft. Review adversarially; do not predict whether grokking occurs
and do not optimize thresholds for expected success.

## Governing question

Does this preregistration support only the narrow claim that a faithful,
canonical CPU reconstruction reproduced delayed generalization in at least 4/5
paper-mainline seeds, while separating platform invalidity and an alternate
artifact-fidelity arm? Are every predicate, control, unit of replication,
resource stop, and interpretation fixed before observations?

## Files to inspect

Read all of these, not only this prompt:

- `experiments/level_0_grokking/PREREGISTRATION_DRAFT.md`
- `experiments/level_0_grokking/SCIENTIFIC_SPEC.json`
- `experiments/level_0_grokking/ANCHOR_CLAIMS.md`
- `experiments/level_0_grokking/COMPANION_CONFIG_TRACE.md`
- `experiments/level_0_grokking/RECONSTRUCTION_CHOICES_V2.md`
- `experiments/level_0_grokking/RESOURCE_SCOUT.md`
- `experiments/level_0_grokking/EXECUTION_INTERLOCK.md`
- `experiments/level_0_grokking/OUTCOME_RUNBOOK_DRAFT.md`
- `src/philosophia/level0/scientific_spec.py`
- `src/philosophia/level0/interlock.py`
- `src/philosophia/level0/outcome.py`
- `src/philosophia/level0/outcome_evaluator.py`
- `src/philosophia/level0/decision_verifier.py`
- `tests/test_level0_scientific_lock.py`

The prior accepted companion-fidelity review is
`reviews/opus_level0_companion_v2_fidelity_review.md`.

## Required audit

1. Audit FIT >=0.99, GENERALIZE >=0.95, persistence W=1000, and
   DELAYED gap >=2000 against the archived evidence. Identify circularity,
   threshold leakage, cadence aliasing, or a definition that can reward a
   transient excursion.
2. Audit 4/5 Arm A quorum and the exact claim strength. Decide whether this is a
   defensible replication demonstration rather than an underpowered statistical
   claim. Require revised language if needed.
3. Audit platform controls: every real-label run must FIT; R-0 must FIT and must
   not GENERALIZE. Check whether Arm B's three-seed asymmetric interpretation is
   coherent and cannot rescue the primary verdict.
4. Audit pseudoreplication and seed/split dependence. Check whether checkpoints,
   cadence observations, and Fourier vectors remain diagnostics rather than
   replication units or post-hoc predictors.
5. Audit resource walls and incomplete runs. Integrity/resource failure must
   abort without an outcome; completed control failures may yield
   PLATFORM_INVALID. Check that this distinction is coherent.
6. Audit the evaluator and verifier for discrepancies from the prose/machine
   spec, including edge cases exactly at thresholds/windows and all nine runs.
7. Audit the forbidden-claims list. Name any inference the proposed decision
   artifact could still invite but the evidence would not license.
8. Decide whether two distinct run ids may be executed concurrently without
   changing the scientific estimand. Distinguish scientific validity from timing
   efficiency and resource-wall risk.

## Output contract

Write a review suitable for `reviews/sol_level0_scientific_lock_outcome_review.md`
with exactly one verdict:

- `LOCK_CANDIDATE_ACCEPTED`
- `REVISE_LOCK`
- `REJECT_DESIGN`
- `BLOCKED_SOURCE`

Lead with Critical/Major/Minor findings. For every blocking finding, give the
exact mandatory edit. Then state: (a) whether implementation can be committed as
a reviewed candidate, (b) whether Kirill may change spec status and create the
lock after those edits, and (c) whether the long-run commands may be issued.
Explicitly list residual claims Level 0 remains forbidden to make. Do not run any
outcome step, create `PREREG.lock`, or select values using anticipated curves.
