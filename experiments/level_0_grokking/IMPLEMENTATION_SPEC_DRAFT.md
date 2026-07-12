# Level 0 implementation specification draft

Status: companion-fidelity v2 modules are implemented and unit-tested; its bounded
determinism-prefix driver is implemented but unexecuted. Full training and every outcome run remain disabled.

## Boundary

Implement independently in src/philosophia. Do not copy unlicensed code or
weights. The implementation exposes model construction, deterministic dataset
construction, a single optimization step, evaluation, checkpoint round-trip,
and Fourier probes as separately testable units.

## Proposed modules

- level0/config.py: typed configuration and canonical serialization.
- level0/data.py: all ordered residue pairs, split, tokens, targets, hashes.
- level0/model.py: minimal transformer matching COMPANION_CONFIG_TRACE.md.
- level0/train.py: full-batch AdamW construction and one optimization step.
- level0/metrics.py: loss, accuracy, parameter norm, and persistence primitive.
- level0/fourier.py: real basis, projections, and frequency-energy diagnostics.
- level0/checkpoint.py: state integrity, config, split, environment, and source
  hashes.
- level0/interlock.py: capability gates for steps, evaluation, and verdicts.
- level0/scout.py: historical one-shot timing/storage orchestration, already executed.
- level0/prefix_check.py: unexecuted bounded v2 determinism re-certification.
- No scientific outcome harness exists before lock-stage closure.

The scientific outcome harness is not implementation-eligible until the remaining
lock-stage threshold, cadence, control, resource, and quorum cells are closed. Library
modules must expose no alternate full-run entry point.

## Fail-closed API rules

- Dataset constructors return separate learner and evaluation views.
- Training code never receives test targets or progress-measure verdicts.
- Split, initialization, and data-order hashes are written before step zero.
- Every checkpoint includes source commit, repository HEAD, Python/PyTorch
  versions, device, dtype, seed, and complete optimizer state.
- Resume refuses schema, config, split, model-state, optimizer-state, or canonical
  environment mismatch.
- Raw optimizer steps, evaluation, and verdict derivation require capabilities;
  scout capabilities cannot evaluate or derive verdicts.
- The outcome evaluator reads frozen artifacts after training; it cannot change
  stopping behavior.

## Determinism contract

Canonical confirmation uses CPU float32 and deterministic PyTorch algorithms.
The split and initialization use separately seeded Python and PyTorch RNGs. A repeated prefix
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
10. Random-label control generation and Fourier basis construction are deterministic.

## Resolved reconstruction choices

- Arm A alone decides replication: lambda=1, 40k epochs, masters 0..4.
- Arm B is a separately named fidelity control: lambda=0.1, 120k, initially seed 1.
- Split uses pinned CPython Random(seed).shuffle; initialization uses a domain-separated PyTorch seed.
- The model trains with 114 output columns; reporting accuracy and loss score residues 0..112.
- Attention scales by sqrt(32); matrices use the companion normal distribution and pinned divisors.

## Deliberately unresolved before lock

- Checkpoint cadence and retained optimizer checkpoints.
- Numeric decision thresholds and seed quorum.
- Exact definitions and timing claims for Fourier progress measures.
- Control pass/fail rules, resource wall, and final B seed count.

No code or test may manufacture defaults for these unresolved cells.
