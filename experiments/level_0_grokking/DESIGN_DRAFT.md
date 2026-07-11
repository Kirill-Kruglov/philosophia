# Level 0 design draft: modular-addition grokking

Status: **DRAFT, NOT LOCKED, NO OUTCOME RUN AUTHORIZED**.

Level 0 is a platform replication, not evidence for Philosophia. Failure first
indicts platform or implementation faithfulness within the bounded repairs below.

## Anchors and question

- [Power et al. 2022](https://arxiv.org/abs/2201.02177).
- [Nanda et al. 2023](https://arxiv.org/abs/2301.05217).
- Complete the linked-code audit and archive allowed evidence by hash before lock; see SOURCE_AUDIT.md.

Question: can the local platform reproduce delayed generalization on modular
addition while saving enough state for published Fourier diagnostics?

## Hardware scout

scripts/hardware_smoke.py checks only forward, backward, optimizer, device, and
deterministic replay on random tensors. It cannot count as a grokking attempt.
CPU is canonical. Acceleration remains exploratory until a fixed prefix matches
identical CPU initial weights and examples.

## Resolve before lock

Copy from one named anchor rather than tune against our outcome:

- modulus, tokenization, and split;
- depth, width, heads, activation, normalization, and position encoding;
- optimizer, learning rate, weight decay, batch policy, and step budget;
- checkpoint and metric schedule;
- exact source revision and every deviation.

Current candidate: Nanda et al.'s transformer, independently reimplemented from a traced specification.

## Proposed observations

At a fixed pre-outcome schedule: train/held-out loss and accuracy, step and wall
time, parameter norm, model and optimizer checkpoint, dataset/config hashes,
Fourier diagnostics, and restricted/excluded loss. Proposed checkpoint interval:
100 steps plus step 0 and final; a timing/storage scout must justify it.

## Proposed decision

Review targets, not locked thresholds:

- FIT: train accuracy at least 0.99 for five observations.
- GENERALIZE: held-out accuracy at least 0.95 for five observations.
- DELAYED: GENERALIZE follows FIT by a preregistered minimum delay.
- Pass: a preregistered quorum of full seeded runs satisfies all three.

Seed count, quorum, and delay require anchor variance. A checkpoint is never the
replication unit.

## Nulls

1. Random labels with identical inputs, split, budget, and schedule.
2. Shuffled checkpoint order for purportedly predictive progress measures.
3. No/low weight decay only if part of the anchor; otherwise exploratory.

## Kills and repairs

Platform kill: non-finite loss, nondeterministic CPU replay beyond tolerance,
corrupt checkpoints, or leakage. Replication kill: anchor-faithful setup fails
within budget across all seeds after bounded repairs. Resource stop: projected
battery exceeds locked time/storage. No early success stop.

Allowed before a replacement lock: dependency/API compatibility, deterministic
kernels, documented batch-size reduction, checkpoint/logging fixes.

Not allowed as platform repair: changing split, quorum, thresholds, optimizer,
weight decay, architecture, budget, seed selection, nulls, or probes after
failure. Scientific changes require a loud amendment and new lock.

## Required reviews

1. Opus: positive arm, failure symmetry, artifact-rewarding criteria.
2. GPT/Codex: source trace, statistics, leakage, determinism, storage.
3. Kirill: signature, sufficiency, and authorization to lock.
