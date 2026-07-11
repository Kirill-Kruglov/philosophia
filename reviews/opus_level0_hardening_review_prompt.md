# Relay prompt: Opus 4.8 verification of Level 0 hardening

Review commit `80241c0` in `/home/master/llm_projects/philosophia` against
`36c97d5`. This is a bounded verification of the mandatory J1/J2/J3 edits from
your implementation review.

Do not run a scientific trajectory. Running the unit suite and isolated
forward/zero-gradient/checkpoint checks is allowed. Ignore the unrelated,
untracked `essay/OUTLINE.md`.

Read:

- `reviews/opus_level0_implementation_review.md`
- `experiments/level_0_grokking/EXECUTION_INTERLOCK.md`
- `src/philosophia/level0/{model,train,metrics,checkpoint,interlock,data}.py`
- `tests/test_level0_{modules,numerics,implementation_review_gate}.py`

The local result is 52 passed; both repository verifiers pass. No
`PREREG.lock`, `decision.json`, scout report, or full-run driver exists.

## Verify

1. Does the independent loop oracle plus explicit attention tests protect causal
   masking, softmax axis, Q/K roles, attention contraction, MLP orientation, and
   final logits from shape-correct regressions?
2. Do the zero-gradient tests establish exact AdamW factors 0.999/0.9999 on all
   11 tensors, including nonzero MLP biases, with one group and no scheduler?
3. Are model and optimizer state hashes deterministic and complete enough to
   detect tensor/param-group corruption before load?
4. Does safe `weights_only=True` loading plus PyTorch 2.9.1, CPU, and float32
   enforcement close J2 without creating an unusable checkpoint schema?
5. Does `InterlockedAdamW` prevent raw or repeated non-scout steps? Can the
   scout capability execute at most 100 steps/120 seconds while being unable to
   call evaluation or persistence verdict APIs?
6. Is the minimal `PREREG.lock` authorization envelope a legitimate interlock
   without silently resolving any scientific lock cell?
7. The round-trip test uses a scout capability for two tiny steps and persists
   only a temporary checkpoint. Is that a valid non-outcome test, or should it
   use a distinct test-only capability?
8. Are any J1/J2/J3 requirements still open before a timing/storage scout?
9. If hardening is accepted, specify whether Codex may implement and execute the
   previously bounded scout exactly once, or whether only its driver may be
   implemented pending another review.

## Required response

Write the full review to `reviews/opus_level0_hardening_review.md` and do not
commit it. Start with exactly one:

- `HARDENING_ACCEPTED`
- `REVISE_HARDENING`
- `BLOCKED`

Then provide:

1. Critical/Major/Minor findings with file/line references.
2. Exact mandatory edits, if any.
3. Explicitly accepted J1/J2/J3 closures.
4. Scout implementation eligibility.
5. Scout execution eligibility and exact remaining guards.
6. Whether lock-stage design may proceed in parallel.

Do not predict grokking, select scientific thresholds, or treat unit-test losses
as observations.
