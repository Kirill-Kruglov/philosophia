# Relay prompt: Opus 4.8 review of Level 0 reconstruction choices v1

This is Round 2 of your READY_FOR_REVISION review. No training loop, scout, or
Level 0 outcome has been run. No PREREG.lock or decision.json exists.

Your Round 1 required six choices before implementation. We propose:

1. AdamW: PyTorch 2.9.1 CPU scalar path, foreach/fused/capturable/differentiable
   false; lr 0.001, betas 0.9/0.98, eps 1e-8, all trainable tensors in one group.
   Decay is theta <- theta - lr*lambda*theta before the adaptive step. A uses
   lambda=1; B uses 0.1.
2. Classes: model preserves 114-column unembedding, but CE and accuracy slice
   logits to residue indices 0..112. Equals index 113 is never scored.
3. Attention: causal softmax(QK^T/sqrt(32)).
4. Initialization: Xavier uniform independently for every matrix, zero MLP
   biases, explicitly labeled a reconstruction deviation.
5. Seeds/split: masters [0,1,2,3,4]; split seed=master; init seed=10000+master;
   lexicographic 12,769 pairs; CPU randperm; first floor(30%)=3,830 train;
   remaining 8,939 test. A and B match split/init by master.
6. Arms: A is sole decision arm, lambda=1, 40k fixed epochs, five seeds. B is
   fidelity control, lambda=0.1, 120k fixed epochs, seed 1, no early stop.
   Serializer must reject A/B hybrids.

Full rationale is in RECONSTRUCTION_CHOICES_V1.md. Evaluate the choices
themselves rather than repeating the first review.

## Questions

1. Does the pinned AdamW equation close C1, including decay of MLP biases?
2. Does 114-column unembedding with 113 scored logits close C2, or create an
   uncontrolled dead-column effect? Give a precise replacement if rejected.
3. Does sqrt(d_head)=sqrt(32) close C3 as a legitimate reconstruction choice?
4. Is Xavier-uniform sufficiently named and timing-robust for implementation
   eligibility, while leaving DELAYED margin to the lock stage?
5. Does the split/seed construction avoid code-order coupling and
   pseudoreplication? Should split be fixed across seeds instead?
6. Is B at 120k/seed1 an interpretable fidelity control, or is another fixed
   budget/seed set mandatory?
7. Are any of the six cells still unclosed before implementation?
8. May Codex implement and unit-test modules after your response, while keeping
   all training/outcome entry points disabled?

## Required response

Start with exactly one:

- CHOICES_ACCEPTED
- REVISE_CHOICES
- BLOCKED

Then list:

1. Critical/Major/Minor findings.
2. Exact mandatory edits to the six choices.
3. Cells explicitly accepted as written.
4. Whether implementation is eligible.
5. The remaining before-lock checklist, without deciding outcome-dependent
   values.

Do not predict outcomes. Do not ask to recover unavailable original code unless
a choice is scientifically uninterpretable without it. Distinguish faithful
paper-mainline reconstruction from artifact fidelity control.
