# Level 0 official companion-source audit

Status: LOCK BLOCKER, NOT AN OUTCOME. No training trajectory was run.

## Why this audit exists

The initial audit inspected the repository linked through the earlier analysis
materials, neelnanda-io/Grokking. Before lock, a second official companion
repository was found:

- repository: mechanistic-interpretability-grokking/progress-measures-paper;
- README claim: transformers.py contains the code used to train the model;
- HEAD: 23d2c64dd1f8a5ca65efaf27e15c2b2cd47dedf1;
- training source first committed 2022-10-07, before arXiv v1;
- transformers.py SHA-256:
  de946fddb1ec509d662829c6bb1e5b456120a1c5bfb31548cdc66b7650cef6ad;
- Grokking_Analysis.ipynb SHA-256:
  76e5888a9afc44ca44cb380266993ba1b174b6dab4def20afeba99355b3872e4;
- no LICENSE, COPYING, or NOTICE file was present.

The source will be cited as evidence, not copied or vendored.

Paper archive:

- arXiv 2301.05217 v3 PDF SHA-256:
  93dcdafc2ecf75d31ab2e32e74cdc11e2e488fec42edfef58ad3d4b6515bcd5f.

## Confirmations

The companion source independently confirms:

- p=113, vocabulary 114, sequence length 3;
- one layer, residual width 128, four 32-dimensional heads;
- ReLU MLP width 512, no active LayerNorm, untied embed/unembed;
- causal attention scaled by sqrt(d_head);
- W_in storage 512 x 128 and W_out storage 128 x 512;
- AdamW lr=0.001, betas=(0.9, 0.98), one parameter group;
- Python seed controls a shuffled lexicographic list of all ordered pairs;
- source defaults include save_every=100 and five-paper-run analysis uses
  100-epoch checkpoint spacing.

## Material discrepancies

| Cell | Current Philosophia reconstruction | Companion executable source | Consequence |
|---|---|---|---|
| Initialization | Xavier uniform gain 1 per matrix/head | independent normal draws with component-specific 1/sqrt(width) scales | trajectory and grok timing may change |
| Split | CPU torch.randperm per master seed | Python random.seed(seed) plus random.shuffle | exact train/test membership changes |
| Learning rate | constant 0.001 | LambdaLR warmup min(step/10, 1) | first ten optimizer updates differ |
| Training CE | equals column sliced; 113 classes | full_loss uses all 114 logits | gradients and dead-column behavior differ |
| Reported analysis | 113 logits | accuracy/Fourier metrics slice off equals | training and reporting use different class sets |
| W_E storage | 114 x 128 | 128 x 114 | mathematically transposed but not checkpoint-compatible |
| W_O storage | 4 x 32 x 128 | flat 128 x 128 | mathematically reshape/transposed but not checkpoint-compatible |
| Mainline config | fixed 40,000, no success stop | saved config says 50,000 and threshold 1e-10; paper analysis truncates to 40,000 | paper 40k remains the clean decision budget |
| Torch init seed | explicitly domain-separated | no torch.manual_seed found | exact original initialization is unrecoverable |

The notebook prints its mainline saved config as lr=0.001, p=113,
d_model=128, frac_train=0.3, num_epochs=50000, save_every=100,
stopping_thresh=1e-10, seed=0, weight_decay=1. It then analyzes only the first
40,000 epochs / 400 checkpoints, matching the paper budget.

## Source hierarchy problem

Earlier reviews accepted named independent reconstruction choices because the
training source appeared unavailable. That premise is now incomplete. The new
source predates the paper and explicitly identifies itself as training code, so
it must be reconciled before lock.

Paper prose should still control the claimed 40,000-epoch decision budget and
the no-post-hoc-stop policy. Executable companion code is stronger evidence for
unreported trajectory details: initialization distribution, split algorithm,
warmup, and 114-class training CE.

## Proposed resolution for review

Recommended direction: revise the source-fidelity implementation before outcome
execution while retaining modern deterministic reconstruction labels:

1. use companion normal initialization distributions and storage orientations;
2. use Python shuffle for the split, seeded by each master seed;
3. reproduce the ten-step warmup under pinned PyTorch semantics;
4. train with 114-class CE but score accuracy and Fourier diagnostics on 113
   residue logits;
5. keep the paper-fixed 40,000 Arm A budget and forbid early stopping;
6. explicitly seed torch with a domain-separated seed because the original torch
   seed is unavailable;
7. keep Arm B distinct by weight decay and budget only.

Alternative: retain the current implementation as an independent paper-text
reconstruction. This is now scientifically weaker and must not be called the
closest available source-fidelity reconstruction.

## Effect on completed work

- No outcome run exists, so revision is pre-outcome and not tuning.
- The one-shot scout remains valid as a rough CPU timing/storage measurement
  because parameter count and full-batch dimensions are unchanged.
- Its deterministic prefix hash applies only to the superseded v1 reconstruction.
- No PREREG.lock or Philosophia decision.json may be created until reconciliation
  is reviewed, implemented, and re-tested.
