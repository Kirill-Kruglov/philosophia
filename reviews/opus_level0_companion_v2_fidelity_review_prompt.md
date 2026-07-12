# Relay prompt: Opus 4.8 review of companion-faithful Level 0 v2

Review commit `919538e` against your companion-source reconciliation review and
the binding trace committed immediately before it. This is a final
implementation-fidelity and bounded-prefix-driver review, not an outcome review.

Do **not** execute the prefix driver, create `PREREG.lock` or `decision.json`, run
a learning curve, evaluate held-out data, select scientific thresholds, or
predict whether grokking will occur. You may inspect source, run the unit suite
and repository verifiers, and run pure or bounded unit-level checks that do not
persist a prefix report.

## Governing evidence

- `experiments/level_0_grokking/COMPANION_CONFIG_TRACE.md`
- `experiments/level_0_grokking/RECONSTRUCTION_CHOICES_V2.md`
- `experiments/level_0_grokking/COMPANION_SOURCE_AUDIT.md`
- `reviews/opus_level0_companion_source_reconciliation_review.md`
- companion source commit and file hashes recorded in the trace

## Implementation under review

- `src/philosophia/level0/{config,data,model,train,metrics,checkpoint,interlock}.py`
- `src/philosophia/level0/prefix_check.py`
- `scripts/level0_companion_v2_prefix_check.py`
- `tests/test_level0_{companion_v2,modules,numerics,prefix_check}.py`
- Level 0 status/spec documents changed by `919538e`

Local verification at the reviewed commit: 75 tests pass; `verify_all.py` reports
the inherited decision valid and no Philosophia decision; `verify_inheritance.py`
reports all 71 inherited files match. No v2 prefix report, preregistration lock,
or Philosophia decision exists. The previous resource scout is not rerun and its
v1 prefix is treated as superseded.

## Exact v2 claims to audit

1. Configuration identity is `level0-companion-v2`; CPU PyTorch 2.9.1 and
   CPython 3.12 are fail-closed where trajectory identity depends on them.
2. The split enumerates all 12,769 ordered pairs lexicographically, applies one
   dedicated `random.Random(master_seed).shuffle`, takes the first 3,830 for
   training, and varies by master seed.
3. Initialization uses a domain-separated torch seed and the exact traced draw
   order: W_E, W_pos, W_K, W_Q, W_V, W_O, W_in, zero b_in, W_out, zero b_out,
   W_U. The first eight matrices/tensor banks use normal / sqrt(128); W_U uses
   normal / sqrt(114). Storage orientations remain math-equivalent and no source
   code or checkpoint is copied.
4. AdamW retains one parameter group and uniform decay. LambdaLR construction
   makes update 0 use LR 0; updates 1..9 use 0.0001..0.0009; update 10 onward
   uses 0.001. Each training step orders forward/backward, optimizer step,
   scheduler step, zero_grad. Scheduler state participates in checkpoint hashing
   and exact resume.
5. Training CE receives 114 final-token logits. Reported evaluation and the
   residue parameter-norm convention use the first 113; the equals column is
   trained and its exclusion from the reporting norm is explicitly conventional.
6. Checkpoint schema 4 hashes model plus optimizer/scheduler state and enforces
   canonical CPU float32, PyTorch, and CPython on load.
7. The independent loop oracle, exact init replay, pinned split fixture, warmup
   sequence 0..11, post-warmup decay on all 11 tensors, 114-vs-113 CE, equals
   gradient, checkpoint tampering, and resume contracts are test-covered.

## Prefix driver to audit without running

The proposed one-time check uses Arm A/master 0, canonical CPU float32, and two
fresh ten-step full-training prefixes. Each repeat has its own `bounded_check(10)`
cap under the test-only maximum of 16. It compares init, split, loss-sequence,
and final model+optimizer hashes. The report contains hashes only, not raw loss
values; it imports no metrics, never accesses `evaluation`, creates no checkpoint,
cannot derive a verdict, and fail-closes if its report already exists.

If and only if the orchestration is acceptable, authorize exactly one invocation:

```bash
.venv/bin/python scripts/level0_companion_v2_prefix_check.py \
  --output-dir experiments/level_0_grokking/prefix
```

State whether the resulting JSON alone may be committed after verifying
`scientific_outcome:false`, two ten-step repeats, all four hashes match, and all
contamination guards are false. A failed invocation must be reported and not
deleted/retried without new review.

## Questions

1. Does commit `919538e` implement every companion-governed cell exactly enough
   to preserve Level 0's faithful-replication kill condition?
2. Are init RNG order, divisors, biases, and retained storage orientations sound?
3. Are Python-shuffle construction and version/hash pinning sufficient?
4. Is the warmup indexing and optimizer/scheduler/zero ordering exact, including
   checkpoint resume and AdamW decay semantics?
5. Is the 114-class training / 113-class reporting boundary consistently enforced?
6. Can a shape-correct or trajectory-wrong refactor still pass the present tests?
7. Does schema 4 protect all trajectory-relevant optimizer/scheduler state and
   environment identity?
8. Is raising `bounded_check` from 10 to 16 scientifically harmless and still
   fail-closed for this non-outcome purpose?
9. Is the proposed prefix driver contamination-safe, and may it be executed once
   with the exact command above?
10. After a matching prefix report, is a further companion-fidelity review needed,
    or may reconstruction-independent lock-stage drafting resume while numeric
    Delta_min remains separately unresolved?

## Deliverable

Write the review to
`reviews/opus_level0_companion_v2_fidelity_review.md` and do not commit it. Begin
with exactly one verdict:

- `COMPANION_V2_ACCEPTED`
- `REVISE_COMPANION_V2`
- `BLOCKED_COMPANION_V2`

Then provide findings ordered Critical, Major, Minor; mandatory edits; accepted
contracts; exact prefix execution authorization or denial; allowed report fields
and forbidden interpretations; and remaining before-lock cells. Distinguish code
defects from preregistration choices. Do not predict outcomes or silently choose
W, Delta_min, quorum, control thresholds, B seed count, or the final null set.
