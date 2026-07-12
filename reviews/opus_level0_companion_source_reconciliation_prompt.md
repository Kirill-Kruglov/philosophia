# Relay prompt: Opus 4.8 companion-source reconciliation before Level 0 lock

A new primary source was discovered before any outcome run: the official
companion repository mechanistic-interpretability-grokking/progress-measures-paper.
Its README states that transformers.py contains training code, and the source
was committed in October 2022, before arXiv v1.

Review the evidence in /home/master/llm_projects/philosophia. Do not run a
training trajectory or inspect any new outcome.

Read:

- experiments/level_0_grokking/COMPANION_SOURCE_AUDIT.md
- experiments/level_0_grokking/SOURCE_AUDIT.md
- experiments/level_0_grokking/CONFIG_TRACE.md
- experiments/level_0_grokking/RECONSTRUCTION_CHOICES_V1.md
- src/philosophia/level0/{config,data,model,train,metrics}.py
- reviews/opus_level0_choices_v1_review.md

Primary hashes:

- companion HEAD:
  23d2c64dd1f8a5ca65efaf27e15c2b2cd47dedf1
- transformers.py:
  de946fddb1ec509d662829c6bb1e5b456120a1c5bfb31548cdc66b7650cef6ad
- Grokking_Analysis.ipynb:
  76e5888a9afc44ca44cb380266993ba1b174b6dab4def20afeba99355b3872e4
- arXiv v3 PDF:
  93dcdafc2ecf75d31ab2e32e74cdc11e2e488fec42edfef58ad3d4b6515bcd5f

No license was found; use source facts as evidence, do not request code copying.

## New executable evidence

The source confirms the existing architecture and AdamW family but differs from
v1 in trajectory-sensitive details:

1. normal scaled initialization rather than Xavier uniform;
2. Python random.seed(seed) plus random.shuffle rather than torch.randperm;
3. LambdaLR warmup min(step/10, 1) rather than constant lr from step zero;
4. training full_loss uses all 114 logits, while reported accuracy and Fourier
   analysis slice to 113;
5. W_E is stored 128 x 114 and W_O is stored flat 128 x 128;
6. the saved mainline config is 50k with threshold 1e-10, while paper analysis
   truncates to 40k and paper prose claims 40k;
7. no torch.manual_seed was found, so exact original initialization is still
   unrecoverable.

## Proposed resolution

Revise to companion-fidelity v2 before outcome execution:

- adopt companion initialization distributions and storage orientations;
- use Python shuffle per master seed;
- pin modern PyTorch semantics for the ten-step warmup;
- train with 114-class CE, report accuracy/Fourier metrics on 113 classes;
- explicitly seed torch with a domain-separated seed as a documented
  reconstruction choice;
- retain paper-fixed Arm A budget 40k and no early stopping;
- keep Arm B distinct only by weight decay, fixed 120k budget, and locked seeds.

Treat the completed scout as resource-only: parameter count and full-batch size
are unchanged, but its deterministic prefix belongs to v1.

## Questions

1. Does the companion repository qualify as stronger evidence for unreported
   executable details than our previously accepted independent choices?
2. Must R2, R4, and R5 plus the learning-rate schedule be reopened?
3. Should 114-class CE be used for training while FIT/GENERALIZE use 113-class
   accuracy?
4. Is normal scaled initialization sufficiently pinned if torch gets an explicit
   domain-separated seed absent from the original source?
5. Must W_E/W_O storage orientations match the companion source, or are
   mathematically equivalent orientations acceptable?
6. Does paper 40k outrank companion 50k/threshold for the decision arm?
7. Is a ten-step modern LambdaLR reconstruction legitimate, and what exact
   lr sequence must tests pin?
8. May the prior scout remain the sole resource scout, or is a new bounded
   v2 prefix check mandatory before full runs?
9. Which earlier review conclusions remain valid, and which must be superseded?
10. After reconciliation implementation, may lock-stage choice drafting resume?

## Required response

Write the full review to
reviews/opus_level0_companion_source_reconciliation_review.md and do not commit
it. Start with exactly one verdict:

- REVISE_TO_COMPANION
- KEEP_INDEPENDENT_RECONSTRUCTION
- BLOCKED

Then provide:

1. Critical/Major/Minor findings with source/code references.
2. Exact mandatory changes to config, data, model, optimizer, tests, and docs.
3. A source hierarchy table: paper prose vs companion executable vs saved
   artifact vs independent reconstruction.
4. Explicitly preserved earlier decisions.
5. Whether any new non-outcome prefix check is required.
6. Conditions for resuming lock-stage design.

Do not predict grokking, choose W/delta_min/quorum yet, or treat the existing
resource scout as an outcome.
