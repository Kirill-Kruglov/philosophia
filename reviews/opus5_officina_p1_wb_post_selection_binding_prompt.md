# Officina P1 W-B post-selection binding and implementation handoff

You are Claude Code Opus 5, post-selection binding author. Work in:

`/home/master/llm_projects/philosophia`

Base commit: `6306e28` (`Select sensor-only P1 watchdog freeze architecture`).
Do not modify historical/governing files, code, tests, untracked work,
signatures, runtime artifacts or prior reviews. Do not commit.

## Author state

Kirill selected:

```text
I_SELECT_P1_WATCHDOG_FREEZE_B_PCS_FREEZES_ON_PEER_ENDPOINT_LOSS
```

Formal signature:

```text
ffcb4116a9171d873be773138cc2c97547f8ff919a1d71f4cbd46e328eb3a7dc  successor/OFFICINA_P1_WATCHDOG_FREEZE_SELECTION_V1_SIGNATURE.md
```

Governing bytes and confirmations:

```text
06aa44fbe3221c9d41484e14fa2a31df42ce58ae17c8b899278b0bf6c5608e9d  successor/OFFICINA_P1_WATCHDOG_FREEZE_AUTHOR_CHOICE_PACKET_V2_10_CORRECTION.md
4b7442bd1dafa1ff141212ac8cd59e94983f32633561b6396837ff0767aa48ff  successor/OFFICINA_GENERIC_HARNESS_WATCHDOG_FREEZE_AUTHORITY_AMENDMENT_V1_7_DRAFT.md
86755531f5a7a5f11085802c3e6b5770f4ef5aa90d98ae1a62599348e11f0e8f  successor/OFFICINA_GENERIC_HARNESS_SUPERVISOR_CONTROL_CHANNEL_P1_OPERATIVE_COMPOSITE_V1_10.md
0998fce3b881e0d0d1947c450b442821047f040a4bdd4a987a1a091ece3a56f7  reviews/fable_officina_p1_watchdog_v2_10_targeted_x_confirmation.md
90fb9f9155926df89e9993de1146c05e279639469d7bf2a60c63c6419bc37e52  reviews/sol_officina_p1_watchdog_v2_10_targeted_y_confirmation.md
```

The selection signature completes only OR-2. OR-3 through OR-11 remain
unauthorized. `T=NOT_ACTIVATED`; programme claim `OPEN`.

## Objective

Produce the smallest reviewable bridge from the signed W-B choice to a
Cursor-ready, inactive implementation. Do not execute the atomic handoff. Do
not generate keys, Stage A/B, resolved governing artifacts, manifests,
attestations or install records.

## Deliverables

Create exactly:

1. `successor/OFFICINA_P1_WB_POST_SELECTION_BINDING_V1_DRAFT.md`
2. `successor/OFFICINA_P1_WB_IMPLEMENTATION_HANDOFF_V1_DRAFT.md`
3. `reviews/opus5_officina_p1_wb_post_selection_binding_closure.md`

## B1 - bind the selected semantics

The binding draft must state one and only one operative branch:

- W-B / `P1_WATCHDOG_SENSOR_ONLY_PCS_FREEZE_V1`;
- watchdog has two sealed pipes, slot 6 closed, no socket and no transport
  request capability;
- watchdog on EOF sends/writes/freezes/signals nothing and exits;
- PCS detects peer-endpoint loss, record-first classifies, and is the sole group
  stop executor for this route;
- W-A and `P1_WATCHDOG_SINGLE_OPCODE_CAPABILITY_V1` are rejected/non-selected.

Bind the four common amendments without changing their meaning:

```text
P1_FREEZE_ABSENT_FALLBACK_NULLABLE_IDENTITY_V1
P1_PCS_FREEZE_CLASSIFIER_V1
P1_WATCHDOG_FREEZER_ROLE_REASSIGNMENT_V1
P1_FREEZE_PUBLICATION_L6_L9_V1
```

Give a complete option-resolution table over every variant-bearing locus and a
mechanical invariant: after actual OR-4, no W-A/W-B marker or rejected-branch
capability may remain. This document is a plan/contract for that transformation,
not the transformation itself.

## B2 - separate dry-run verification from OR-3/OR-4

Define a test-only, in-memory transformation oracle that may be implemented and
unit-tested before acceptance. It:

- consumes copies of the v1.7/v1.10 source bytes;
- selects W-B in memory;
- checks marker elimination, W-A absence and W-B invariants;
- may report hashes tagged `test-only/non-installed/non-authoritative`;
- writes no resolved amendment/composite to a governing or runtime path;
- creates no key, Stage A/B, manifest, attestation, signature or record;
- cannot be used as production input or as OR-4 evidence.

State exactly what later authorized OR-4 does that this oracle does not. Do not
create the resolved-byte files in this task.

## B3 - close the gate ledger, including identity

Give one total ledger from current state through inactive implementation,
acceptance, atomic handoff and T activation. At minimum distinguish:

1. W-B author selection: COMPLETE.
2. Watchdog authority amendment v1.7 acceptance: NOT ACCEPTED.
3. Process identity Option A selection: COMPLETE.
4. `P1_IDENTITY_OBSERVATION_BOUNDED_WEAKENING_V1`: NOT ACCEPTED.
5. Inactive code/test implementation: candidate eligibility only.
6. OR-3..OR-11: NOT AUTHORIZED.
7. T activation: NOT AUTHORIZED.

Resolve, without inventing a choice, whether inactive implementation may include
the observation-only identity code while the weakening token is unaccepted.
The fail-closed minimum is:

- code and dummy tests may exist;
- no production/install/activation path may make identity observation operative;
- the active verifier must refuse until the separately reviewed weakening token
  is accepted and bound, or the observation feature remains disabled in a way
  consistent with the selected Option A contract.

If the governing identity documents require a stricter boundary, state
`BLOCKED_PENDING_IDENTITY_WEAKENING_REVIEW` and identify the exact clauses. Do
not silently treat the token as accepted.

## B4 - Cursor-ready inactive implementation scope

The handoff must be sufficiently exact for Cursor to implement without design
discretion. Include:

- exact allowed code/test/script paths;
- exact frozen paths it must not edit;
- public APIs, types, enums, schemas and error codes;
- process/descriptor topology for W-B;
- PCS endpoint-loss trigger and record-first ordering;
- watchdog EOF/exit behavior;
- classifier inputs, scope recomputation and group-stop authority;
- filesystem/runtime-control negative surfaces;
- canonical serialization and hashing rules;
- restart/crash-cut behavior;
- deterministic dummy fixtures and test-only keys/seeds, mechanically unable to
  create a production artifact;
- full unit, adversarial, multi-fault and disposable integration-test matrix;
- verifier behavior while inactive: fail closed before any production action;
- exact evidence that T remains `NOT_ACTIVATED`.

Account for the existing dirty/untracked Cursor implementation work in
`accounting.py`, `generic_harness.py` and their tests without adopting it as
governing evidence or overwriting unrelated changes. The handoff must require a
fresh code audit against signed contracts before reuse.

No real process-control smoke may run in the shared runtime tree. Disposable
integration tests may use isolated temporary roots only, with test-only
capabilities and no production artifact names.

## B5 - provenance residual

Carry the confirmed v2.10 ruling: four deferred MS-2 rows are bounded accounting,
not a fail-open. Decide where they enter the first actual post-selection
generation ledger, without editing historical MS-2. The implementation handoff
must not pretend they are already members.

## B6 - acceptance and authorization boundary

The only watchdog amendment acceptance token available after bounded X/Y review
is:

```text
I_ACCEPT_OFFICINA_GENERIC_HARNESS_WATCHDOG_FREEZE_AUTHORITY_AMENDMENT_V1_7
```

State exactly what that future token accepts and what it still does not
authorize. It must not itself start OR-3, generate a key, execute OR-4, install
code or activate T. A separate implementation authorization and later one-shot
atomic-handoff authorization are required.

## Closure

Emit exactly one:

- `READY_FOR_OFFICINA_P1_WB_BINDING_XY_REVIEW`
- `REVISE_OFFICINA_P1_WB_BINDING`
- `BLOCKED_PENDING_IDENTITY_WEAKENING_REVIEW`
- `BLOCKED_OFFICINA_P1_WB_BINDING`

The closure must provide:

1. complete W-B/rejected-W-A resolution matrix;
2. dry-run-versus-OR-4 boundary;
3. total gate ledger and identity-token disposition;
4. exact Cursor implementation surface and test matrix;
5. provenance-row disposition;
6. negative authorization confirmation;
7. bounded X/Y questions focused on binding correctness and implementation
   eligibility, not another architecture review.

Nothing in this task authorizes code edits, tests, keys, artifacts, OR-3/OR-4,
install, activation, candidate, datum, outcome or Proof.

In chat report the verdict, paths/hashes, W-B binding, identity gate, Cursor
scope, provenance disposition, negative space and exact next boundary.
