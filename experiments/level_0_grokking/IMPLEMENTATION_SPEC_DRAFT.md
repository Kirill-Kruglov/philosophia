# Level 0 implementation specification draft

Status: design-only; blocked on review; no training loop is authorized.

## Boundary

Implement independently in src/philosophia. Do not copy unlicensed code or
weights. The implementation exposes model construction, deterministic dataset
construction, a single optimization step, evaluation, checkpoint round-trip,
and Fourier probes as separately testable units.

## Proposed modules

- level0/config.py: typed configuration and canonical serialization.
- level0/data.py: all ordered residue pairs, split, tokens, targets, hashes.
- level0/model.py: minimal transformer matching CONFIG_TRACE.md.
- level0/train.py: full-batch AdamW loop and fixed logging/checkpoint schedule.
- level0/metrics.py: loss, accuracy, FIT/GENERALIZE predicates.
- level0/fourier.py: basis, sparsity, restricted/excluded metrics and nulls.
- level0/checkpoint.py: model, optimizer, config, split and source hashes.
- experiments/level_0_grokking/run.py: harness-only orchestration.

## Fail-closed API rules

- Dataset constructors return separate learner and evaluation views.
- Training code never receives test targets or progress-measure verdicts.
- Split, initialization, and data-order hashes are written before step zero.
- Every checkpoint includes source commit, repository HEAD, Python/PyTorch
  versions, device, dtype, seed, and complete optimizer state.
- Resume refuses any config or split hash mismatch.
- The outcome evaluator reads frozen artifacts after training; it cannot change
  stopping behavior.

## Determinism contract

Canonical confirmation uses CPU float32 and deterministic PyTorch algorithms.
The seed schedule controls Python, NumPy, and PyTorch RNGs. A repeated prefix
must produce identical initial-state, split, loss-sequence, and final-state
hashes.

GPU/ROCm is exploratory until a separate equivalence gate defines tolerances.

## Tests required before any scout

1. All 113 squared ordered pairs occur exactly once before splitting.
2. Train/test sets are disjoint and cover the universe.
3. Targets equal a+b modulo 113.
4. Equals is present only in the final input position.
5. Model tensor shapes match the anchor artifact.
6. No LayerNorm or tied embed/unembed parameters exist.
7. A full-batch step changes parameters and remains finite.
8. Checkpoint save/load resumes to an identical next step.
9. Evaluation cannot be imported by the training module through a forbidden
   dependency edge.
10. Random-label and shuffled-checkpoint null generators are deterministic.

## Deliberately unresolved

- Main positive arm: paper lambda=1, artifact lambda=0.1, or both.
- Exact five-seed schedule and split algorithm.
- 40k fixed budget versus separately labeled artifact reproduction.
- Whether output softmax has 113 or 114 logits.
- Checkpoint cadence and retained optimizer checkpoints.
- Numeric decision thresholds and seed quorum.
- Exact definitions and timing claims for Fourier progress measures.

Cursor Compose must not implement this draft. It becomes eligible only after the
unresolved cells are closed, the specification is versioned, and Kirill
authorizes implementation.
