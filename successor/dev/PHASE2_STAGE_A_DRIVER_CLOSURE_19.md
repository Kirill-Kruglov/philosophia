# Phase 2 Stage A driver closure 19

Status: `STAGE_A_ACCEPTED`

Date: 2026-08-14

## Frozen inputs

- Philosophia base: `b0b9adf4eaeee45b86291ce4f4510b3f0242862d`
- MINIMO base: `6066f482c6752915ad21119f93dc162f4cb9db72`
- accepted cumulative patch:
  `successor/dev/minimo_phase2_stage_a_19.patch`
- patch SHA-256:
  `e08a8d29d67d82297216722b3e13e6c1a3f4bd354962a2865b1cfc57a9980bbd`
- scientific spec: 26 exact keys, CPU-debug reference parameter count 478720,
  canonical `init_seed` domain `[0, 2**32-1]`

## Acceptance evidence

- driver fresh-tree apply/check, `git diff --check`, and targeted boundary
  probes: pass;
- driver Stage-A test gate: 126/126;
- driver Philosophia test gate after V4.3.1: 416/416; V4.3.2 changes only the
  seed bound and its tests;
- final X: `CONFIRM_STAGE_A_V4_3_2_X`, 126/126;
- final Y: `CONFIRM_STAGE_A_V4_3_2_Y`, 126/126;
- both reviewers independently reproduced the pinned Torch CPU `0`/`2**32`
  alias and confirmed typed pre-spawn rejection at the canonical boundary.

V4.3.1 X correctly found that `[0, 2**63-1]` still contained lower-domain
aliases. V4.3.2 repaired only that boundary. The earlier Y seed disposition was
explicitly superseded; every other V4.3.1 confirmation remained closed.

## Closed Stage-A surface

The accepted patch provides the strict scientific constructor and manifest,
exact no-truncation codec, canonical complete action handling, exact search
accounting, hindsight/config repairs, process isolation and typed terminals,
zero-budget evidence, Peano-proxy containment, ambient-independent deterministic
construction, and real fresh-process nat-add replay required by the Stage-A
contract.

## Still unauthorized and deferred

This closure authorizes no learner training, carrier generation, selector
qualification, SELF/YOKED branch, Phase-2 outcome, MINIMO commit, or push.

Deferred harness gates remain:

- byte-identical optimizer/full training-branch replay;
- deterministic item-addressed batch sampling;
- trained-checkpoint transport and manifest verification before Peano;
- the capability token is trusted in-tree discipline, not a malicious-Python
  sandbox.

The next permitted work is Stage-B contract review and pre-audit freeze. No
audit root, carrier candidate, cost block or scientific outcome may be generated
until the Stage-B preregistration's section-0 placeholders are closed and the
contract is independently accepted.
