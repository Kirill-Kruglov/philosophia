# Level 0 companion executable configuration trace

Status: binding source trace for reconstruction v2; committed before v2 code.
This document authorizes no outcome run and creates no preregistration lock.

## Provenance

- Paper: Nanda et al., arXiv 2301.05217 v3.
- Paper PDF SHA-256:
  93dcdafc2ecf75d31ab2e32e74cdc11e2e488fec42edfef58ad3d4b6515bcd5f.
- Companion repository:
  mechanistic-interpretability-grokking/progress-measures-paper.
- Companion commit:
  23d2c64dd1f8a5ca65efaf27e15c2b2cd47dedf1.
- transformers.py SHA-256:
  de946fddb1ec509d662829c6bb1e5b456120a1c5bfb31548cdc66b7650cef6ad.
- Grokking_Analysis.ipynb SHA-256:
  76e5888a9afc44ca44cb380266993ba1b174b6dab4def20afeba99355b3872e4.
- Companion source first commit: 2022-10-07, before arXiv v1.
- No repository license file was found. Facts are traced; code is not copied.

## Initialization distribution

The companion constructs parameters in this RNG draw order:

1. W_E;
2. W_pos;
3. W_K;
4. W_Q;
5. W_V;
6. W_O;
7. W_in;
8. b_in=zeros, consuming no RNG;
9. W_out;
10. b_out=zeros, consuming no RNG;
11. W_U.

| Tensor | Companion storage | Companion draw | V2 storage | V2 draw |
|---|---:|---|---:|---|
| W_E | 128 x 114 | normal / sqrt(128) | 114 x 128 | transpose-equivalent normal / sqrt(128) |
| W_pos | 3 x 128 | normal / sqrt(128) | 3 x 128 | same |
| W_K | 4 x 32 x 128 | normal / sqrt(128) | same | same |
| W_Q | 4 x 32 x 128 | normal / sqrt(128) | same | same |
| W_V | 4 x 32 x 128 | normal / sqrt(128) | same | same |
| W_O | 128 x 128 | normal / sqrt(128) | 4 x 32 x 128 | reshape/transpose-equivalent normal / sqrt(128) |
| W_in | 512 x 128 | normal / sqrt(128) | same | same |
| b_in | 512 | zeros | same | same |
| W_out | 128 x 512 | normal / sqrt(128) | same | same |
| b_out | 128 | zeros | same | same |
| W_U | 128 x 114 | normal / sqrt(114) | same | same |

Storage orientation is an independent math-equivalent reconstruction choice.
There is no checkpoint sharing with the unlicensed companion. Per-element
distributions, RNG draw order, and operation semantics are binding.

The companion does not call torch.manual_seed. Exact original weights are
unrecoverable. V2 therefore resets the CPU torch generator to
init_seed=10000+master_seed inside a forked RNG context before applying the draw
order above. This matches the source distribution, not its unknown sample.

For each random tensor, the frozen init observable records shape, configured
divisor, expected population standard deviation, realized population standard
deviation, minimum, maximum, and SHA-256.

## Dataset split

Binding source algorithm under CPython 3.12.3:

1. enumerate tuples (a, b, 113) with a outermost and b innermost;
2. create a dedicated random.Random(master_seed);
3. call shuffle exactly once on the complete 12,769-element list;
4. take the first int(0.3 * 12,769)=3,830 tuples as learner data;
5. take the remaining 8,939 tuples as evaluation data;
6. perform no other call on that Random instance.

A dedicated Random instance is state-equivalent to source-level
random.seed(seed) followed immediately by random.shuffle(pairs), while avoiding
global RNG coupling. Split hashes are valid only for the pinned CPython minor
version; a version change forces explicit regeneration and review.

Splits continue to vary across master seeds 0..4. Arm A and Arm B share the same
split and initialization for a matched master seed.

## Optimizer and warmup

The companion creates AdamW, then LambdaLR with:

lambda scheduler_step: min(scheduler_step / 10, 1)

It executes each training epoch in this order:

1. forward and 114-class learner CE;
2. backward;
3. optimizer.step;
4. scheduler.step;
5. optimizer.zero_grad.

Pinned reconstruction: CPython 3.12.3, PyTorch 2.9.1+cpu, scalar AdamW path,
lr base 0.001, betas (0.9, 0.98), epsilon 1e-8, one uniformly decayed parameter
group, no AMSGrad, foreach/fused/capturable/differentiable false.

PyTorch 2.9.1 calls the LR lambda at scheduler construction with index 0.
Therefore the LR used by optimizer updates is:

| Epoch update | LR used | LR after scheduler.step |
|---:|---:|---:|
| 0 | 0 | 0.0001 |
| 1 | 0.0001 | 0.0002 |
| 2 | 0.0002 | 0.0003 |
| 3 | 0.0003 | 0.0004 |
| 4 | 0.0004 | 0.0005 |
| 5 | 0.0005 | 0.0006 |
| 6 | 0.0006 | 0.0007 |
| 7 | 0.0007 | 0.0008 |
| 8 | 0.0008 | 0.0009 |
| 9 | 0.0009 | 0.001 |
| 10+ | 0.001 | 0.001 |

The AdamW decay multiplier at an update is 1 - lr_used * weight_decay.
The exact 0.999 Arm A and 0.9999 Arm B factors apply only from epoch update 10
onward.

## Training and reporting class boundary

The companion training function sends all 114 final-token logits to
cross-entropy. Labels remain residues 0..112. The equals logit at index 113 is a
real softmax competitor and receives suppressive CE gradients plus weight decay.

V2 binding:

- training loss: logits indices 0..113, 114 classes;
- reported train/evaluation loss: residue logits indices 0..112, 113 classes;
- FIT/GENERALIZE accuracy: residue logits indices 0..112;
- Fourier diagnostics: residue logits indices 0..112;
- parameter diagnostics: record both full 114-column norm and residue-only
  113-column norm; neither is an outcome predicate.

The v1 dead-column interpretation is superseded.

## Budget, stopping, and cadence evidence

Paper prose governs Arm A: 40,000 fixed epochs and five seeds. No early success
stop is allowed.

The companion saved mainline config reports 50,000 epochs, threshold 1e-10,
save_every=100, seed=0, and weight_decay=1. The notebook truncates analysis to
the first 40,000 epochs and 400 checkpoints. Therefore:

- 40,000 remains the decision budget;
- the threshold is not inherited;
- save_every=100 is source evidence for the later lock-stage cadence choice.

Arm B remains fixed at 120,000 epochs with no early stop. Its final seed count
remains a lock-stage choice.

## Supersession map

Preserved: architecture, causal sqrt(d_head) attention, AdamW family and
decoupled semantics, full-batch training, master seed schedule, Arm A/B hierarchy,
paper budgets, no early stop, interlocks, checkpoint integrity, and outcome gates.

Superseded for v2: R2 training-class boundary, R4 Xavier initialization, R5 split
algorithm, and R1 constant learning rate. The exact torch init seed remains an
independent deterministic reconstruction choice.

No PREREG.lock or decision.json is eligible until v2 implementation, tests,
bounded prefix re-certification, and final companion-fidelity review complete.
