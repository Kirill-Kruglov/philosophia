# Level 0 anchor claim archive

Status: pre-outcome source evidence for the scientific lock.

## Archived paper

- Nanda et al., *Progress Measures for Grokking via Mechanistic
  Interpretability*, arXiv:2301.05217v3 / ICLR 2023.
- PDF SHA-256:
  `93dcdafc2ecf75d31ab2e32e74cdc11e2e488fec42edfef58ad3d4b6515bcd5f`.
- Main configuration location: PDF page 3, Section 3, "Setup and
  Background."
- Seed timing location: PDF page 22 (printed page 22), Appendix C.2.1,
  Figure 18 and its following paragraph.
- Weight-decay timing location: PDF page 28, Appendix D.1, text preceding
  Figure 27.

## Exact source-supported cells

Section 3 identifies the mainline experiment as P=113, one ReLU transformer
layer, d_model=128, four 32-dimensional heads, MLP width 512, learned positional
embeddings, no LayerNorm, untied embedding/unembedding, 30% of all ordered
pairs, full-batch AdamW, learning rate 0.001, weight decay lambda=1, and 40,000
training epochs. The same section says train accuracy quickly reaches 100% and
test accuracy rises to near 100% after around 10,000 epochs.

Appendix C.2.1 says all five same-architecture runs complete memorization by
around 1,400 epochs, while circuit formation, cleanup, and the exact grokking
time vary by seed. Figure 18 shows the four additional seed trajectories on
fixed epoch axes.

Appendix D.1 summarizes lambda=1 grokking timing as approximately 5,000 to
10,000 epochs across the runs discussed there. This is used only to bound a
conservative minimum delay, not to predict our trajectories.

## Delta derivation

The published lower timing anchor is 5,000 epochs and the published common
memorization completion anchor is 1,400 epochs, leaving a 3,600-epoch gap.
Level 0 locks:

- `delta_min = 2,000 epochs`;
- `persistence_window = 1,000 epochs`;
- metric cadence = 100 epochs.

The 0.99/0.95 accuracy values are pre-outcome operational thresholds rather
than recovered paper thresholds. The 2,000-epoch delay leaves 1,600 epochs of
margin for the independently
seeded companion-distribution initialization, threshold mismatch (paper prose
uses near-perfect behavior, while our predicates use 0.99/0.95 accuracy), and
timing variance across seeds. It is fixed before any outcome trajectory.

This derivation does not assert that our runs will grok or that their timing
will match the paper. It defines what Level 0 will call delayed if they do.

## Companion executable evidence

- Repository: `mechanistic-interpretability-grokking/progress-measures-paper`.
- Commit: `23d2c64dd1f8a5ca65efaf27e15c2b2cd47dedf1`.
- `transformers.py` SHA-256:
  `de946fddb1ec509d662829c6bb1e5b456120a1c5bfb31548cdc66b7650cef6ad`.
- `Grokking_Analysis.ipynb` SHA-256:
  `76e5888a9afc44ca44cb380266993ba1b174b6dab4def20afeba99355b3872e4`.

The companion source governs initialization distribution/order, Python shuffle,
ten-update learning-rate warmup, and 114-class training CE. Paper prose governs
the Arm A 40,000-update decision budget and prohibition on outcome-dependent
early stopping.
