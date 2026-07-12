# Level 0 reconstruction choices v1

Status: historical v1, superseded for lock by RECONSTRUCTION_CHOICES_V2.md.
The current code remains v1 until the separately committed v2 implementation;
no outcome run or preregistration lock is authorized.

## R1: AdamW equation and lambda

Use `torch.optim.AdamW` from pinned PyTorch 2.9.1 CPU with `foreach=False`,
`fused=False`, `capturable=False`, `differentiable=False`, and one parameter
group containing every trainable tensor, including MLP biases.

Pin:

- learning rate gamma = 0.001;
- betas = (0.9, 0.98);
- epsilon = 1e-8;
- amsgrad = false;
- constant learning rate;
- Arm A weight_decay lambda = 1.0;
- Arm B weight_decay lambda = 0.1.

The decoupled decay substep is
`theta_decay = theta_previous - gamma * lambda * theta_previous`, followed by
the bias-corrected Adam adaptive step. Thus the multiplicative decay factors per
epoch are 0.999 for A and 0.9999 for B before the adaptive update. This follows
the PyTorch AdamW algorithm rather than interpreting lambda as an L2 loss term.

Uniform decay of every trainable tensor, including MLP biases, is an explicit,
bounded reconstruction choice. The original run's bias-decay treatment is not
established.

Source: https://docs.pytorch.org/docs/stable/generated/torch.optim.adamw.AdamW_class.html

## R2: output classes

Construct 114 input embeddings and a 114-column unembedding to preserve the
artifact tensor shape. Reserve index 113 for equals. For loss and accuracy, slice
the final-token logits to indices 0 through 112 before cross-entropy/argmax.
The equals logit is never a candidate target and receives only indirect/decay
updates through its unembedding column.

This is an explicit independent-reconstruction choice following Opus's
recommendation to score only 113 residue classes. It is not asserted to reproduce
the unknown original cross-entropy implementation.

The logged parameter-norm diagnostic excludes unembedding column 113. That
column receives no scored-loss gradient and its decay must not masquerade as
progress in the diagnostic.

## R3: attention scaling

Use causal scaled dot-product attention:

`scores = (Q @ K.transpose(-2, -1)) / sqrt(32)`

before the causal mask and softmax. The divisor is sqrt(d_head), not
sqrt(d_model), and not one. This is the standard scaled dot-product convention
for four 32-dimensional heads and is recorded as a reconstruction choice because
the inspected anchor sources do not pin it.

## R4: initialization

Use a named deterministic Glorot-uniform reconstruction:

- apply `torch.nn.init.xavier_uniform_(gain=1.0)` independently to every matrix,
  including token embeddings, positional embeddings, Q/K/V/O, MLP weights, and
  unembedding;
- initialize all MLP biases to zero;
- no other trainable tensors exist.

Before step zero, record a frozen init-scale observable for every independently
initialized matrix: its shape, theoretical Xavier bound, realized population standard
deviation (unbiased=false), minimum, maximum, and content hash. Per-head attention matrices are
recorded separately.

This is a documented deviation, not a claim about the original initialization.
It is chosen because every matrix has an explicit fan-in/fan-out definition and
PyTorch provides a stable named implementation.

Before lock, DELAYED's delta_min margin must explicitly absorb plausible
Xavier-driven timing shift relative to the paper's approximately 10k-epoch
report. This note cannot be removed merely because implementation tests pass.

## R5: split algorithm, RNG, and seeds

Enumerate the 12,769 ordered pairs lexicographically with a outermost and b
innermost. Use full-run master seeds [0, 1, 2, 3, 4].

For each master seed:

- split_seed = master_seed;
- init_seed = 10,000 + master_seed;
- construct a CPU `torch.Generator` seeded by split_seed;
- permute indices with `torch.randperm(12_769, generator=split_generator)`;
- training indices are the first `floor(0.30 * 12_769) = 3,830`;
- test indices are the remaining 8,939;
- initialize the model in a forked CPU RNG context seeded by init_seed;
- full-batch training has no data-order RNG.

Both arms use the same split and initialization for a given master seed. Domain
separation makes split/init independent of incidental code order. This is a
documented reconstruction choice; it does not claim the paper's original split.

The serialized split hash is versioned to PyTorch 2.9.1 because `torch.randperm`
is not promised to preserve its exact permutation across PyTorch versions. Any
version change forces regeneration and explicit re-hashing before lock.

## R6: arm hierarchy

| Arm | Role | Weight decay | Fixed budget | Seeds | Decision use |
|---|---|---:|---:|---|---|
| A | paper-mainline reconstruction | 1.0 | 40,000 epochs | 0,1,2,3,4 | sole replication verdict |
| B | artifact-parameter fidelity control | 0.1 | 120,000 epochs | 1 | interprets A failure only |

Arm B has no early stop. Its 120,000-epoch fixed budget exceeds the inspected
artifact's stored epoch 107,790 without inheriting its test-loss threshold.
The resource scout may reject this proposed battery before any outcome run, but
may not shorten B after observing a curve.

Arm B has an asymmetric interpretation rule. B success is informative: it shows
that the platform can produce delayed generalization under the fidelity-control
parameters and makes an A failure an anchor-fidelity issue. B failure at one
seed is uninformative and indicts neither platform nor anchor because it is
confounded with seed variation.

If the outcome-independent resource scout permits, B should expand to at least
three preregistered master seeds. That decision and the resulting seed list must
be locked before any outcome curve is observed.

The configuration serializer must encode arm identity and reject hybrids:

- A cannot use B lambda, budget, or seed schedule;
- B cannot contribute to A's k-of-5 verdict;
- shared architecture/reconstruction choices are versioned by this document's
  content hash.

## Still unresolved before lock

Round 1 deliberately placed these after implementation eligibility:

- persistence window W;
- DELAYED minimum gap derived from published seed variation;
- quorum k-of-5 and demonstration-only claim strength;
- exact control pass/fail semantics;
- uniform metric/checkpoint cadence and storage projection;
- outcome-independent resource wall;
- archive hash for the paper's mainline claim;
- final null set.

No implementation may expose defaults that silently fill these cells.
