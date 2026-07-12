# Level 0 scientific preregistration draft

Status: **ACCEPTED BY KIRILL BEFORE OUTCOME. PENDING CANONICAL LOCK COMMIT.
NO OUTCOME RUN AUTHORIZED YET.** The machine-readable governing specification is
`SCIENTIFIC_SPEC.json`. Kirill supplied the exact authorization statement
`I_ACCEPT_LEVEL0_SCIENTIFIC_SPEC` after the Sol and Opus reviews were closed.

## Question and scope

Can the canonical CPU platform reproduce delayed generalization on the
paper-mainline modular-addition task? Level 0 is a five-seed replication
demonstration, not a powered hypothesis test and not evidence for Philosophia.

Arm A alone decides replication: weight decay 1, 40,000 optimizer calls, master
seeds 0..4. Arm B is a fidelity control: weight decay 0.1, 120,000 calls, master
seeds 1..3. R-0 is a random-label platform/leakage control at the Arm A budget.
Every run is fixed-budget with no outcome-dependent stop.

Update 0 faithfully uses learning rate zero under the companion warmup. Thus an
Arm A run contains one moment-priming call and 39,999 effective parameter
updates. Epoch/update numbering is not adjusted to hide that fact.

## Outcome predicates

Metrics are sampled at step 0, every 100 optimizer calls, and the final step.

- FIT starts at the first recorded observation such that every recorded
  reporting-train-accuracy observation through at least start+1,000, inclusive,
  is at least 0.99.
- GENERALIZE starts at the first recorded observation such that every recorded
  held-out-accuracy observation through at least start+1,000, inclusive, is at
  least 0.95.

These are observed-sample persistence predicates at the locked 100-step cadence;
they make no claim about unobserved sub-cadence values. The 0.99 and 0.95 values
are pre-outcome operational thresholds, not thresholds recovered from the paper.
- DELAYED holds when GENERALIZE_start - FIT_start is at least 2,000 steps.

The derivation of W and Delta_min is frozen in `ANCHOR_CLAIMS.md`. Checkpoints
are observations, never replication units.

## Primary decision

All platform controls must pass first. Then:

- `REPRODUCED`: at least 4 of 5 Arm A runs satisfy FIT, GENERALIZE, DELAYED;
- `NOT_REPRODUCED`: at most 3 of 5 satisfy all three;
- no p-value, effect size, or broader architecture/modulus claim is licensed.

Every real-label run must reach FIT. A failure to memorize is
`PLATFORM_INVALID`, not a negative grokking result. R-0 must reach FIT and must
not reach GENERALIZE; either violation is `PLATFORM_INVALID`.

Arm B success means at least one of three runs satisfies all three predicates.
It never enters the primary quorum. Only when the valid primary decision is
`NOT_REPRODUCED` and B succeeds, emit
`ANCHOR_FIDELITY_SENSITIVE_DIAGNOSTIC`; otherwise emit `NO_PRIMARY_INFERENCE`.
B failure is uninformative and does not alter the Arm A verdict. Every completed
real-label run, including each B run, must still FIT because memorization is the
universal platform floor.

## Cadence and resources

- metrics and fixed Fourier energy diagnostics: every 100 steps;
- model-only snapshot: every 100 steps;
- full optimizer/resume checkpoint: every 1,000 steps;
- all include step 0 and final;
- total artifact ceiling: 25 GiB;
- per-run wall: A/R 6 hours, B 18 hours.

The walls are outcome-independent. Crossing one produces `RESOURCE_STOP` and no
scientific verdict. It cannot be used because a curve looks unpromising.

CPU float32, PyTorch 2.9.1+cpu, CPython 3.12.3, 16 intra-op threads,
32 inter-op threads, and deterministic algorithms are the only decision path.
The exact CPython micro version is locked to preserve the
already certified split fingerprint; this resolves the pre-lock micro/minor
identity mismatch without changing the matching v2 prefix.

## Artifact and resume discipline

Each run writes an immutable manifest before step zero and an append-only
metrics stream. Output directories must be new. Resume is allowed only from a
full checkpoint whose schema, model, optimizer/scheduler, thread counts, config,
split, scientific-spec, lock, source, and metric-prefix hashes all match. Resume never
changes the fixed final budget.

The evaluator reads completed run reports only after all nine required runs are
present. It cannot train, change thresholds, densify metrics, or select seeds.

## Null set and deferred claims

Random labels are the only Level 0 scientific null. Shuffled checkpoint order
and weight-decay necessity are Level 3 tests. Fourier energies are recorded as
claim-neutral diagnostics; Level 0 does not say they predict, explain, or cause
the transition.

## Remaining gate

The adversarial Sol and Opus findings are closed and Kirill has accepted every
cell before outcome. The canonical lock script must now bind this committed
specification and the reviewed source hashes; `PREREG.lock` must then be
committed unchanged. Until that lock commit, no outcome directory or scientific
decision is permitted.
