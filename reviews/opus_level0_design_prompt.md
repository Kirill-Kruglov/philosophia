# Relay prompt: Opus 4.8 review of Philosophia Level 0

You are the adversarial X-line reviewer for Philosophia. Review a design before
implementation and before preregistration. No Level 0 outcome has been run.

The programme asks whether derivable algebraic/geometric worlds can provide
primary experience to a small model. Level 0 is only a platform replication of
known modular-addition grokking and must not be counted as evidence for that
thesis.

## Anchor facts

Paper: Nanda et al., Progress Measures for Grokking via Mechanistic
Interpretability, https://arxiv.org/abs/2301.05217

Paper mainline:

- addition modulo 113; input tokens a, b, equals; predict at final token;
- 30% of all ordered pairs for training, complement for test;
- one-layer ReLU transformer;
- learned embeddings width 128 and learned positional embeddings;
- 4 attention heads, head dimension 32;
- MLP width 512;
- no LayerNorm; untied embed/unembed;
- full-batch AdamW, learning rate 0.001, weight decay lambda=1;
- 40,000 epochs; five random seeds;
- reported grokking around 10k epochs with seed variation;
- published progress measures include Fourier structure and
  restricted/excluded loss.

Linked repository:

- https://github.com/neelnanda-io/Grokking
- inspected commit dfbd38f7d23e09aaa5e5c9bd0483b69ca533e580;
- README calls it a dump of saved weights/loss curves for a Colab;
- no complete training loop and no LICENSE were found.

Inspected saved artifact wd_10-1_mod_addition_loss_curve.pth:

- config: p=113, d_model=128, frac_train=0.3, lr=0.001, seed=1,
  weight_decay=1, num_epochs=1,000,000, stop threshold 5e-7;
- optimizer state: Adam-compatible, betas 0.9/0.98, epsilon 1e-8,
  executable weight_decay=0.1, constant LR 0.001;
- stored epoch: 107,790;
- tensor shapes confirm one layer, 4x32 attention, MLP 512, sequence length 3;
- embedding and unembedding each have vocabulary width 114;
- MLP has biases; embedding, attention and unembedding do not.

Thus paper and artifact conflict on executable weight decay and budget. Exact
split RNG, initialization, seed schedule, attention scaling, softmax treatment
of the equals class, and original logging cadence remain unresolved.

## Proposed design

- Independent implementation; no copying unlicensed code or weights.
- Canonical CPU float32 deterministic path; ROCm exploratory until equivalence.
- Fixed full-run unit of replication, never checkpoints.
- Proposed outcome concepts, not locked:
  - FIT: train accuracy at least 0.99 for five observations.
  - GENERALIZE: test accuracy at least 0.95 for five observations.
  - DELAYED: GENERALIZE follows FIT by a locked minimum delay.
- Proposed nulls:
  - random labels under matched budget;
  - shuffled checkpoint order for predictive progress measures;
  - no/low weight decay only if part of the chosen anchor.
- No early success stop; every seed runs to fixed budget.
- Platform repairs may address API compatibility, deterministic kernels,
  documented batch size, and serialization only.
- Changing split, architecture, optimizer, weight decay, budget, thresholds,
  quorum, seeds, nulls, or probes after failure requires a new loud lock.

## Your task

Attack the design, not the expected result. In particular:

1. Is Level 0 anchored faithfully enough to preregister, or is source
   incompleteness a blocker?
2. What is the correct positive-arm construction given paper lambda=1/40k and
   artifact executable lambda=0.1/107,790?
3. Is reproducing one arm sufficient, or are both paper and artifact arms needed?
4. Are FIT, GENERALIZE, and DELAYED defined without circularity? Propose exact
   fixes only where the evidence justifies them.
5. Which nulls belong in Level 0, and which should be deferred to Level 3?
6. What positive controls ensure that a failure indicts our platform rather than
   the grokking claim?
7. Identify pseudoreplication, leakage, stopping, checkpoint, and
   backend-equivalence failures.
8. Does the independent implementation preserve enough architecture identity,
   or could a hidden deviation make any result uninterpretable?
9. Which unresolved cells must be closed before implementation, before scout,
   and before lock respectively?
10. State whether Cursor Compose may implement after your revisions, or whether
    another source/configuration audit is required first.

## Required response format

Start with exactly one verdict:

- READY_FOR_REVISION
- BLOCKED_SOURCE
- REJECT_DESIGN

Then provide:

1. Findings ordered Critical, Major, Minor.
2. Mandatory changes before implementation.
3. Mandatory changes before preregistration lock.
4. A proposed positive-arm table with source and rationale.
5. A proposed null/control table.
6. Remaining claims Level 0 is forbidden to make.
7. A concise handoff specification for Codex/Cursor.

Do not predict whether grokking will occur. Do not soften a blocker because the
programme is ambitious. Preserve negative space and say when evidence is
insufficient.
