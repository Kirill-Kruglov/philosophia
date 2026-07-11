# Relay prompt: Opus 4.8 review of gated Level 0 implementation

Review commit `3a06ac0` in `/home/master/llm_projects/philosophia` against its
parent. This is a code review after your Round 2 `REVISE_CHOICES` response.

No outcome run, full training loop, resource scout, `PREREG.lock`, or
`decision.json` exists. Do not run a scientific training trajectory. Unit tests
and bounded single-step/round-trip checks are allowed.

Read at minimum:

- `reviews/opus_level0_choices_v1_review.md`
- `experiments/level_0_grokking/RECONSTRUCTION_CHOICES_V1.md`
- `experiments/level_0_grokking/CONFIG_TRACE.md`
- `experiments/level_0_grokking/IMPLEMENTATION_SPEC_DRAFT.md`
- `src/philosophia/level0/{config,data,model,train,metrics,fourier,checkpoint}.py`
- `tests/test_level0_modules.py`

The local suite reports 42 passed. Treat tests as evidence, not proof.

## Audit questions

1. Is the transformer mathematically and dimensionally faithful to the traced
   architecture, including causal attention, `1/sqrt(32)`, residual paths,
   final-token readout, and artifact-oriented `W_in=(512,128)`,
   `W_out=(128,512)` storage?
2. Is Xavier initialization independently applied at `gain=1.0`, with correct
   per-matrix/per-head bound and realized-scale observables?
3. Does AdamW implement the pinned scalar path and uniformly decay every
   trainable tensor without an accidental parameter omission or scheduler?
4. Does data construction exactly cover 113 squared lexicographic pairs, use
   domain-separated per-master split/init seeds, and prevent learner code from
   receiving an `EvaluationView`?
5. Does canonical configuration reject every meaningful A/B hybrid, including
   seed schedules, while leaving the final B expansion a pre-outcome lock choice?
6. Are 114 model logits and 113 scored logits handled consistently in training,
   evaluation, accuracy, and parameter norm?
7. Is checkpoint save/load fail-closed on config/split/schema mismatch and strong
   enough to support an identical next optimization step? Identify missing
   metadata or integrity checks required before a scout.
8. Are the real Fourier basis/projection primitives correct and claim-neutral?
9. Can any repository entry point currently launch a full trajectory or derive a
   scientific verdict despite the intended gate? Check imports and APIs, not only
   filenames.
10. What important tests are missing, especially tests capable of catching a
    mathematically wrong but shape-correct implementation?

## Required response

Write the full review to
`reviews/opus_level0_implementation_review.md` and do not commit it. Start with
exactly one verdict:

- `IMPLEMENTATION_ACCEPTED`
- `REVISE_IMPLEMENTATION`
- `BLOCKED`

Then provide:

1. Findings ordered Critical, Major, Minor, with file/line references.
2. Mandatory code and test edits.
3. Explicitly accepted contracts.
4. Whether work may proceed to lock-stage design.
5. Whether a bounded, non-outcome timing/storage scout is eligible; if yes,
   specify the maximum safe scope and required contamination guards.
6. Remaining risks that only the signed preregistration can resolve.

Do not predict grokking, select thresholds, invent cadence/quorum defaults, or
execute enough steps to inspect a learning curve. Distinguish an implementation
defect from a preregistration-stage open cell.
