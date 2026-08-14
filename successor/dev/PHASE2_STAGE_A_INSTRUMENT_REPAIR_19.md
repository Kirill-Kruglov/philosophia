# Phase-2 Stage A instrument repair 19 (V4.3.2)

Bounded seed-domain correction after driver
`STAGE_A_SEED_DOMAIN_CORRECTION_REQUIRED_V4_3_1`.
Not a scientific outcome. Not a carrier. Not training. Not SELF/YOKED.
Not a reopened design round.

Verdict: `STAGE_A_V4_3_2_READY_FOR_TARGETED_XY_CONFIRMATION`

Supersedes the V4.3.1 submission (patch SHA-256
`38afd4233e94fb479954ae2f4902188b72732e9f293c640094d8de69a1c2e571`,
verdict `STAGE_A_V4_3_1_READY_FOR_BOUNDED_XY_CONFIRMATION`, driver
`STAGE_A_SEED_DOMAIN_CORRECTION_REQUIRED_V4_3_1`). X returned
`REVISE_STAGE_A_V4_3_1_X`; Y returned `CONFIRM_STAGE_A_V4_3_1_Y`. The
driver reproduced the remaining seed-alias blocker and closed every other
reviewed cell. V4.3.2 changes only the canonical `init_seed` domain.

## Bases

- Philosophia: `b0b9adf4eaeee45b86291ce4f4510b3f0242862d`
- MINIMO pinned commit: `6066f482c6752915ad21119f93dc162f4cb9db72`
- Development: fresh disposable clone; submitted V4.3.1 patch applied first; V4.3.2 on that tree
- Cumulative patch: `successor/dev/minimo_phase2_stage_a_19.patch`
- Patch SHA-256: `e08a8d29d67d82297216722b3e13e6c1a3f4bd354962a2865b1cfc57a9980bbd`

## One-to-one V4.3.1 X/Y disposition

| ID | Source | Finding | V4.3.2 disposition |
|---|---|---|---|
| X-3 / driver | X revise; driver reproduced | Accepted seeds `0`, `2**32`, and `2**62` have distinct spec hashes but identical CPU streams and learner state hashes | **Repaired.** `init_seed` is an exact non-bool int in `[0, 2**32-1]`. Validator, constants, report, acceptance JSON, and fixtures updated. Upper-bound regression accepts `2**32-1`, typed-rejects `2**32`, and read-only demonstrates the `0`/`2**32` Torch CPU generator alias. Public `init_seed=2**32` raises `IsolatedInvalidSpec` before `multiprocessing.get_context` |
| X-1, X-2, X-4, X-5 | X confirm | Spec/dtype boundary, ambient construction, preserved search/codec/replay cells | **Preserved.** Not reopened |
| Y-1, Y-2, Y-3, Y-5 | Y confirm | PEANO_PANIC identity, containment/timeout/codec terminals, ambient construction, remaining closed cells | **Preserved.** Not reopened |
| Y-4 | Y question superseded by driver | Seed-domain question superseded by the reproduced `2**32` alias | **Repaired** as X-3 / driver above |

## Preserved V4.3 / V4.3.1 repairs (not reopened)

Ambient-closed construction; exact-str dtype; semantic `PEANO_PANIC`; zero-budget public evidence; closed optimizer domains; Peano-proxy containment; public `action_timeout_s`; dedicated `ARTIFACT_ID_LIMIT`; `bos=False` codec causality; faithful terminal-hit fixture; real isolated `budget>=4` two-process replay.

## Later obligations (explicitly not implemented)

- Byte-identical optimizer / full training-branch replay
- Deterministic keyed batch sampling
- Trained checkpoint transport with manifest verification **before** Peano reconstruction (carrier Stage B does not need an LM)
- Treating the underscore capability token as a sandbox against malicious Python

## Repair summary

Canonical `init_seed` domain is `[0, 2**32-1]` because the pinned Torch CPU
generator aliases `s` and `s + 2**32`.

CPU-debug spec hash (26-key, dropout 0, `init_seed=0`):
`b2fd8e4887909dfdf269123dc484a876d6a826c650a7098f6abdc852215c6b09`

CPU-debug parameter count remains `478720`.

`init_seed` range: `[0, 4294967295]` (`2**32-1`).

## Changed paths (cumulative vs pinned MINIMO)

Phase-1: `learning/problems.py`, `learning/proofsearch.py`, `learning/test_mcts_expansion_counter.py`

Stage A: `learning/policy.py`, `learning/bootstrap.py`, `learning/phase2_*.py`,
`learning/test_phase2_*.py`

Not changed: `learning/util.py`, yaml, theory/Rust/Peano sources, Phase-1 JSON/checkpoints.

## Surface widening

None beyond the allowed Stage-A surface. Envelope codes remain the V4.3 closed
set. No yaml, util, theory, or Rust/Peano edits.

## Negative authorization (confirmed)

No scientific training job, no carrier, no Phase-2 outcome, no SELF/YOKED, no
Phase-1 checkpoint rerun, no commit, no push.
