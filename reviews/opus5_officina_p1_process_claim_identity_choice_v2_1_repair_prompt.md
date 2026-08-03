# Task: bounded v2.1 repair of the P1 process-claim identity choice packet

You are Claude Code Opus 5 acting as the specification author, not an independent reviewer. This is a two-defect bounded correction, not a new architecture round. Do not implement code, execute process-control behavior, activate T, or alter scientific/programme state.

## Inputs

Read the committed bytes of:

- `successor/OFFICINA_P1_PROCESS_CLAIM_IDENTITY_AUTHOR_CHOICE_PACKET_V2_DRAFT.md`
- `reviews/opus5_officina_p1_process_claim_identity_choice_v2_closure.md`
- `reviews/opus_officina_p1_process_claim_identity_choice_v2_confirmation.md`
- `reviews/sol_officina_p1_process_claim_identity_choice_v2_confirmation.md`
- the governing contracts cited by those confirmations

Treat both `REVISE` verdicts as binding. Preserve all existing files untouched.

## Deliverables

Create exactly:

1. `successor/OFFICINA_P1_PROCESS_CLAIM_IDENTITY_AUTHOR_CHOICE_PACKET_V2_1_CORRECTION.md`
2. `reviews/opus5_officina_p1_process_claim_identity_choice_v2_1_closure.md`

The correction must carry v2 forward except for the exact replacements below. Do not select A/B or accept the weakening token.

## Repair 1: close indirect reads in `generic_harness.py`

Close the X-line residual without reintroducing general taint analysis:

- Extend the reflection/name-indirection lockdown to `generic_harness.py`, not only PCS/role roots. Explicitly forbid `locals`, `globals`, `vars`, `eval`, `exec`, `getattr`, `setattr`, `compile`, `__import__`, and equivalent reflective access there.
- Pin the in-memory claim and lease representations as canonical mappings whose restricted fields can be read only through the named centralized accessors.
- Forbid `.values()`, `.items()`, mapping iteration that can expose restricted values, `**` unpacking, attribute-style access, generic serialization/reflection, destructuring, and any alternate route that binds either restricted value without a literal-key accessor.
- Make the rule syntax-mechanical over the five production roots. If helper calls are allowed, enumerate exact approved call sites and operands; do not rely on semantic claims such as “equivalent operations are forbidden.”
- Add direct fixtures for the three demonstrated bypasses: `list(claim.values())[5]`, `locals()["attested_pid"]`, and `claim.controller_pid`, plus unpack/iteration variants.
- Preserve the already-accepted occurrence-count design for direct parsed Names.

## Repair 2: add the fifth legitimate persistent consumer

Close YV2-C1 exactly:

- Add `C-5`: after canonical claim validation, exactly one SHA-256 over the complete canonical claim byte string may produce `process_claim_sha256`.
- The hash is permitted solely for the already-signed `T_PROCESS_STARTED` lineage and `t-process-record.v1` lineage destinations. No partial-field hash, alternate encoding, secondary digest, derived numeric identity, or other destination is allowed.
- Pin a centralized canonical-byte hash accessor. It may accept validated complete canonical bytes but may not bind, expose, iterate, log, or return either identity field individually.
- State the one-way classification boundary: the digest is an integrity/lineage identifier, never process identity or authority, and cannot feed addressing, signalling, waiting, capacity, custody, spend, selection, qualification/comparison, Q/C, datum, evidence, outcome, or Proof.
- Choose one exact model and make it single-valued: either the digest is the sole named declassification from `RESTRICTED_PROCESS_IDENTITY`, or it belongs to a restricted derived class with only the two lineage destinations. Explain why the choice cannot launder the underlying fields.
- Update `P-R1`, `P-R4`, `ACC-R1..ACC-R4`, schema-reader audit, `S-25d/e/g`, tests, consumer counts, blast-radius text, closure dispositions, and v1.3 handoff.
- Reconcile C-5 with Repair 1: the whole-object hasher is the one explicit mapping/byte consumer exempted from field-level accessor rules, but it must operate on canonical validated bytes and expose no field-level value.

## Preserve

- All eight findings both confirmation lines accepted as closed.
- J4/replay, crash, EEXIST, PID bound, fresh PGID rule, corrected Option B count, and `/proc` rationale remain unchanged.
- Option A remains an explicit bounded lexical weakening and grants no process-control authority.
- Option B remains non-selectable behind its authority sub-cells.
- Watchdog-freeze remains orthogonal and unresolved.
- `T = NOT_ACTIVATED`; programme claim `OPEN`.

## Closure

Include:

- verdict `READY_FOR_OFFICINA_P1_PROCESS_CLAIM_IDENTITY_CHOICE_V2_1_FINAL_XY_CONFIRMATION` only if both residual defects are closed;
- hashes and an exact two-row replacement index;
- one-to-one disposition of the X bypass and Y C-5 finding;
- no-regression table for the already-closed findings;
- one literal bounded yes/no question per reviewer;
- exact residual author choices and explicit negative authorization.

Do not modify existing files. Report created paths and verdict.
