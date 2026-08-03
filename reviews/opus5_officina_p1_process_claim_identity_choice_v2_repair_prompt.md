# Task: bounded repair of the P1 process-claim identity author-choice packet

You are Claude Code Opus 5 acting as the **specification author**, not as an independent reviewer. Work in the local `philosophia` repository. Do not implement code, execute process-control behavior, activate T, create entropy, or alter any scientific/programme state.

## Governing inputs

Read the committed bytes of:

- `successor/OFFICINA_P1_PROCESS_CLAIM_IDENTITY_AUTHOR_CHOICE_PACKET_V1_DRAFT.md`
- `reviews/opus5_officina_p1_process_claim_identity_author_choice_packet.md`
- `reviews/opus_officina_p1_process_claim_identity_choice_review.md`
- `reviews/sol_officina_p1_process_claim_identity_choice_review.md`
- the governing supervisor/P1/activation contracts cited by those reviews

Treat both reviews as binding defect reports for this bounded repair. Preserve v1 and both reviews untouched.

## Required deliverables

Create exactly:

1. `successor/OFFICINA_P1_PROCESS_CLAIM_IDENTITY_AUTHOR_CHOICE_PACKET_V2_DRAFT.md`
2. `reviews/opus5_officina_p1_process_claim_identity_choice_v2_closure.md`

The v2 packet must be a self-contained replacement, not a loose patch. The closure must disposition every X/Y finding one-to-one and state whether the packet is ready for one bounded X/Y confirmation round. Do not select A or B and do not mint or accept an author token.

## Mandatory repairs

### 1. Durable J4 operand vector and replay

Repair X M-1 / Y-C2 explicitly:

- Amend the durable J4 `COMPLETED` journal record schema for `AWAIT_STOP` so it records the complete response operand vector needed after a crash, including at least `outcome`, `handle_id`, `start_identity`, `pgid_is_leader`, `attested_pid`, and `attested_pgid`, plus every existing replay-relevant field.
- Pin canonical field order/encoding and require `COMPLETED` and `ACKED` replay to redeliver the recorded vector byte-identically, without any re-observation of `/proc`, pid, pgid, handle state, or child state.
- Update Option A's blast-radius table and the v1.3 implementation handoff to include this journal-schema/replay change.
- Withdraw the unsupported phrase that this is inherited “exactly as `start_identity` already is.” State that v2 makes `start_identity` durability explicit together with the new tuple.
- Cover the crash cut between J4 durability and peer claim installation.

### 2. Closed immediate-use whitelist

Repair X M-2 without relying on incomplete general taint analysis:

- For the two parsed response names, define a closed syntactic whitelist: bind once at the one parse site and pass each unmodified only into its named process-claim constructor field.
- Forbid every other direct syntactic use, including arithmetic, formatting, calls/lambdas, casts, comparisons other than mandatory validation, container insertion, comprehensions, unpacking, aliasing, logging, request construction, addressing, capacity/custody/selection, Q/C, and science.
- Specify a decidable verifier over the parsed AST and the exact exceptions needed for mandatory structural/cross-field validation. Do not leave an open “and similar” category.

### 3. Persistent-use boundary: claim, lease, freeze predicate

Repair Y-C1:

- Withdraw the false claim that the two process-claim fields are the only durable sinks.
- Enumerate the already-signed legitimate persistent flow exactly: immediate claim write; claim-to-active-lease copy because the lease contains all claim keys; and the signed freeze-predicate read of `process_group_id` (and any other governing read proved from the contracts).
- Define how **every** direct or reloaded read/alias of `controller_pid` and `process_group_id` remains in the restricted identity class. A claim/lease reload must never declassify the values.
- Use a closed persistent-consumer whitelist or centralized verified accessor surface. Every other consumer must route deterministically to process invalidity, never to capacity, custody, spend, selection, Q/C, or scientific evidence.
- Recompute all relevant schema readers rather than claiming generic taint completeness.

### 4. Crash, collision, and invalidity dominance

Repair Y-M1:

- If PCS dies after the process claim is durably installed, retain the claim and route through the signed invalid-process settlement; never narrate the claim as absent.
- `EEXIST` converges only after canonical byte, schema, cross-field, and expected-hash identity verification. Malformed, partial, conflicting, or inconsistent occupants route record-first to dominant invalidity.
- Bind malformed/incomplete identity replies and tuple mismatch to the same dominant invalidity surface.
- Make every crash row consistent with the exact durable boundary it follows.

### 5. Correct Option B comparison

Repair Y-M2:

- Recompute Option B's exact schema and reader blast radius from the governing schemas.
- Do not claim `t-process-record.v1` inherits PID/PGID keys: it has its own key set and references `process_claim_sha256`.
- If any process-record/archive change is still claimed, justify it through an explicit dependency; otherwise remove it from the count.
- Re-evaluate but do not outcome-tune the recommendation after the corrected comparison. Option B may remain non-selectable if the signed authority gap remains, but the reason must be exact.

### 6. Bounded clarifications

- Pin whether A-P4 uses the handle-table `pgid_or_null` or a fresh `getpgid`, which is authoritative, and why; make implementations single-valued.
- Pin Linux `PID_MAX_LIMIT = 4194304` as the provenance for the seven-digit bound and fail closed on an eight-digit value.
- Correct the stale `/proc/cmdline` rationale: the deleted argv-evidence rule was scoped to clean-image/fresh-exec/executor-set claims; the route remains unauthorized because its indices are stale and it bypasses P1 handle-only, PCS-mediated authority.
- Distinguish supervisor inability to freeze after PCS death from the separate watchdog inability to freeze after supervisor death.

## Invariants that must remain unchanged

- The identity conflict remains real and loud.
- Option A remains an explicit weakening of the lexical “cannot express a PID” sentence, not a hidden reinterpretation.
- Observing PID/PGID does not grant authorized process-control authority; only handles, the closed request grammar, and PCS execution do.
- Both-or-neither tuple semantics, stopped/unreaped direct-child proof, PID-reuse binding, fail-closed absence, and no replay re-observation remain.
- The watchdog-freeze cell remains orthogonal and unresolved by this packet.
- `T = NOT_ACTIVATED`; programme claim `OPEN`.

## Closure requirements

The closure must include:

- a verdict, preferably `READY_FOR_OFFICINA_P1_PROCESS_CLAIM_IDENTITY_CHOICE_V2_XY_CONFIRMATION` if and only if all findings are closed;
- exact hashes of both new files and the reviewed inputs;
- a finding-disposition table for X M-1/M-2/m-1..m-3 and Y-C1/Y-C2/Y-M1/Y-M2/Y-m1;
- a corrected blast-radius table for A and B;
- one bounded yes/no confirmation question for each reviewer;
- explicit negative authorization: no selection, implementation, activation, process execution, spend, datum, outcome, Proof, or claim movement.

Do not modify any existing file. Report the created paths, verdict, and the exact residual author choices.
