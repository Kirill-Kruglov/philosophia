# Level 0 anchor configuration trace

Status: reopened before lock by official companion training source. Existing
modules remain testable, but full training and preregistration are unauthorized
until source reconciliation.

Sources:

- Paper: Nanda et al., https://arxiv.org/abs/2301.05217
- Linked repository: https://github.com/neelnanda-io/Grokking
- Repository commit: dfbd38f7d23e09aaa5e5c9bd0483b69ca533e580
- Official companion training repository: mechanistic-interpretability-grokking/progress-measures-paper
- Companion commit: 23d2c64dd1f8a5ca65efaf27e15c2b2cd47dedf1
- Saved artifact inspected:
  saved_runs/wd_10-1_mod_addition_loss_curve.pth

## Round 1 resolution status

Opus Round 1 found the anchor sufficient for an independent paper-mainline
reimplementation, subject to six named reconstruction choices. Their proposed
values and rationale are versioned in `RECONSTRUCTION_CHOICES_V1.md`.

| Required cell | Proposal | Review status |
|---|---|---|
| AdamW equation and lambda semantics | R1 | accepted; bias decay labeled |
| Output class count and scored logits | R2 | accepted; diagnostic norm clarified |
| Attention scaling | R3 | accepted |
| Initialization | R4 | implementation-eligible; lock note retained |
| Split algorithm and RNG | R5 | accepted; hash versioned |
| Primary and fidelity-control arms | R6 | implementation-eligible; lock rule retained |

Round 2 accepted implementation with the bounded revisions recorded in
RECONSTRUCTION_CHOICES_V1.md. Remaining observation predicates, B-control
interpretation, and resource rules are mandatory before Kirill can create a
preregistration lock.

## Confirmed cells

| Item | Paper | Saved artifact | Status |
|---|---|---|---|
| Task | addition modulo P | config fn_name=add | confirmed |
| Modulus | P=113 | config p=113 | confirmed |
| Input | tokens a, b, equals; predict above final token | positional tensor has length 3 | confirmed |
| Training fraction | 30% of all 113 squared pairs | frac_train=0.3 | confirmed |
| Test set | every pair not in training | loss arrays include train/test | paper-confirmed; split algorithm unresolved |
| Layers | one transformer layer | blocks.0 only | confirmed |
| Residual width | 128 | embedding and residual tensors width 128 | confirmed |
| Attention | 4 heads, head dimension 32 | W_Q/K/V shapes 4 x 32 x 128 | confirmed |
| MLP | 512 hidden units, ReLU | W_in 512 x 128 and W_out 128 x 512 | confirmed |
| Position | learned positional embeddings | W_pos shape 3 x 128 | confirmed |
| LayerNorm | absent | no normalization parameters | confirmed |
| Embed/unembed tying | absent | distinct W_E and W_U | confirmed |
| Optimizer family | full-batch AdamW | optimizer state is Adam-compatible | paper-confirmed |
| Learning rate | 0.001 | config and optimizer group 0.001 | confirmed |
| Adam betas | not found in paper text | optimizer state 0.9, 0.98 | artifact-confirmed |
| Adam epsilon | not found in paper text | optimizer state 1e-8 | artifact-confirmed |
| Scheduler | not specified | constant LambdaLR state at 0.001 | artifact-confirmed |
| Main seed count | five | inspected artifact seed=1 | paper-confirmed count; schedule unresolved |

## Blocking discrepancies

### Weight decay

The paper names AdamW weight decay lambda=1. The artifact config also stores
weight_decay=1, but its optimizer param group stores weight_decay=0.1 and its
filename says wd_10-1. The executable value for that artifact was therefore 0.1.
It is not established that this artifact is the paper's mainline run.

### Budget and stopping

The paper states 40,000 epochs. The artifact config states num_epochs=1,000,000,
stopping_thresh=5e-7, and the stored epoch is 107,790. This artifact cannot be
used to silently replace the paper's fixed budget.

### Vocabulary

The paper denotes d_vocab=113 while treating the equals token separately. The
artifact embedding and unembedding tensors both have width 114. Targets appear
to occupy the 113 residues, but whether the equals logit participates in
cross-entropy must be traced from training code or reconstructed explicitly.

### Split and initialization

The exact permutation procedure, RNG library/order, five seed values, parameter
initialization, attention scaling, and initialization of biases were not
established by the paper text or analysis repository.

### Logging and checkpoints

The artifact config stores save_every=10,000. Its train loss list is per epoch
while test loss is approximately every ten epochs. The paper does not make this
cadence normative. The original full-run checkpoint set was linked separately
from Google Drive and is not licensed in the inspected repository.

## Derived architecture constraints

The independent implementation must have:

- input vocabulary 114 including equals;
- sequence length 3;
- learned token and position embeddings;
- causal one-layer attention with 4 heads and head dimension 32;
- residual width 128;
- one 512-unit ReLU MLP;
- residual paths around attention and MLP;
- no LayerNorm;
- untied embedding/unembedding;
- no embedding, attention, or unembedding bias;
- MLP input/output biases, matching checkpoint keys;
- loss read only at the final token.

## Source resolution rule

Paper text outranks artifact names for the claimed mainline configuration.
Executable optimizer state outranks a stale config field for describing a saved
artifact. Neither may be combined into a synthetic configuration without
labeling the combination as an independent reconstruction.

The proposed arm hierarchy is paper mainline at lambda=1 and 40k epochs as the
sole decision arm, plus a separately named fixed-budget artifact-fidelity
control at executable lambda=0.1. This hierarchy is implementation-eligible and must never be serialized as a
hybrid configuration. Its final B seed count remains a lock-stage resource
choice.

No preregistration lock is allowed until the separate before-lock checklist is
closed.

## Companion-source reconciliation gate

COMPANION_SOURCE_AUDIT.md records pre-paper executable evidence that reopens
four trajectory-sensitive v1 choices: initialization distribution, split
algorithm, ten-step learning-rate warmup, and 114-class training CE. Storage
orientations for W_E and W_O are also source-resolved.

The prior Round 2 acceptance was correct under the evidence then presented, but
cannot serve as final lock approval after this source correction. No outcome
driver or PREREG.lock is eligible until a new review resolves the hierarchy
between paper prose, companion executable source, and the saved artifact.
