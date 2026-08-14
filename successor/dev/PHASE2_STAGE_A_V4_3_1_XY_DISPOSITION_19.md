# Phase 2 Stage A V4.3.1 bounded X/Y disposition

Status: `STAGE_A_SEED_DOMAIN_CORRECTION_REQUIRED_V4_3_1`

Inputs:

- X: `REVISE_STAGE_A_V4_3_1_X`
- Y: `CONFIRM_STAGE_A_V4_3_1_Y`
- patch SHA-256:
  `38afd4233e94fb479954ae2f4902188b72732e9f293c640094d8de69a1c2e571`

## Accepted convergence

Both reviewers independently confirmed the patch identity, clean application,
125/125 Stage-A tests, typed spec/dtype boundary, ambient dtype/device/RNG
restoration, real zero-budget evidence, exact search accounting, faithful
terminal traversal, codec causality, proxy containment, deadline/result-file
ordering, explicit synthetic enumeration, dedicated artifact-ID terminal, real
PyO3 panic vs forged panic vs child crash, and real budget-4 fresh-process
replay. Opus additionally reproduced 416/416 Philosophia tests. These cells are
closed and must not be reopened by the next repair.

## Reproduced blocker

Sol found, and the driver independently reproduced, accepted lower-domain seed
aliases on the pinned Torch CPU generator:

| `init_seed` | spec hash | learner state hash |
|---:|---|---|
| `0` | `5d4b11c2...` | `0fa58f6727b770...` |
| `2**32` | `8e7ed5d15c55...` | `0fa58f6727b770...` |
| `2**62` | `9e8b158ed1da...` | `0fa58f6727b770...` |

Their generated CPU streams are also byte-identical. The V4.3.1 range
`[0, 2**63-1]` therefore remains non-canonical: distinct declared learner
identities can denote the same initialization. Opus question 4 is superseded on
this one fact by the reproduced counterexample; the rest of the Y confirmation
stands.

## Required bounded correction

Restrict `init_seed` to exact non-bool integers in `[0, 2**32-1]`, reject
`2**32` through the public pre-spawn boundary, and update the artifacts. No
other design or implementation cell is open. Stage B remains unauthorized.
