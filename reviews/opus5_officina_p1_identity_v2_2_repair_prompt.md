# Task: bounded v2.2 correction of P1 process-claim identity choice

You are Claude Code Opus 5 acting as specification author, not reviewer. This correction closes only the residuals in the final v2.1 X/Y reviews. Do not implement code, execute processes, activate T, spend resources, or move the programme claim.

## Inputs

Read committed bytes of:

- `successor/OFFICINA_P1_PROCESS_CLAIM_IDENTITY_AUTHOR_CHOICE_PACKET_V2_DRAFT.md`
- `successor/OFFICINA_P1_PROCESS_CLAIM_IDENTITY_AUTHOR_CHOICE_PACKET_V2_1_CORRECTION.md`
- `reviews/opus_officina_p1_process_claim_identity_choice_v2_1_final_confirmation.md`
- `reviews/sol_officina_p1_process_claim_identity_choice_v2_1_final_confirmation.md`
- the complete governing signed chain they cite

Treat both `REVISE` verdicts as binding. Preserve existing files.

## Deliverables

Create exactly:

1. `successor/OFFICINA_P1_PROCESS_CLAIM_IDENTITY_AUTHOR_CHOICE_PACKET_V2_2_CORRECTION.md`
2. `reviews/opus5_officina_p1_process_claim_identity_choice_v2_2_closure.md`

## A. Close the fresh claim-reopen path

Adopt the X-line's bounded, taint-free repair:

- Pin the literal/runtime construction of `successor/officina/runtime/T_PROCESS_CLAIMS/` and every derived claim/occupant path to the named approved site `MS-1`.
- Across all five production roots, any `open`, `os` read, `pathlib` read, mmap or equivalent byte-read whose path is or can denote `T_PROCESS_CLAIMS` is legal only inside `_read_claim_bytes` at `MS-2`.
- Every byte string returned by that site must bind immediately to a governed carrier Name. No alternate variable, return wrapper, callback, exception payload or container may receive it.
- Pin `json.loads`/canonical parsing of claim bytes to `MS-3`; no fresh mapping can be produced from a claim-path read outside that site.
- Make recognition syntax-mechanical: enumerate exact path constructors, call forms and operands. Do not require taint, dataflow or semantic “can denote” reasoning without a closed syntactic rule.
- Add the exact counterexample fixture from X (`open` → fresh `raw` → `json.loads` → `list(m.values())[5]`) plus `os`/`pathlib`, alias, helper-return and alternative-path-spelling variants.
- Reconcile these additions with retained peer-root `open()` for unrelated durable records; only claim paths are restricted.

## B. Reconcile two `ACC-5` evaluations

Adopt the Y-line correction exactly:

- State that `ACC-5` has **two authorized evaluations**, not one:
  1. lineage evaluation over newly validated canonical claim bytes; its raw digest reaches only direct destinations D-1 and D-2;
  2. occupant evaluation over independently validated existing canonical occupant bytes; its digest is transient and consumed only by boolean collision conjunct `X-4`.
- Amend `C-5`, `DC-1`, `DC-6`, `S-25e`, `S-25l`, counts, tests and handoff consistently.
- Preserve exactly two direct persistent raw-lineage-digest destinations while enumerating permitted transitive integrity lineage: complete event hashes/lease seed, final-record hash/stop event, archive copies/composites and recovery verification.
- No transient occupant digest may be persisted, logged, returned, compared outside X-4, or become a third destination.

## C. Narrow the cryptographic claim honestly

- Withdraw absolute claims that `process_claim_sha256` is never process identity, never comparison/evidence, non-invertible, or confidentiality-preserving.
- State that it is a searchable full-claim commitment; with the other eighteen fields known, the PID/PGID search space is at most 4,194,304 because `pid == pgid`.
- State that it may provide conditional informational identity/equality evidence and is **not a confidentiality boundary**.
- Preserve the normative authorization boundary: it confers no process-control authority, is not an authorized PID selector, and may not feed handles, opcode requests, signalling, waiting, capacity, custody, spend, settlement, selection, qualification, Q/C, scientific datum/evidence/outcome, or Proof.
- Distinguish informational possibility from authorized conforming use throughout `DC-3..DC-5` and `WL-4`.

## Preserve

- All prior closed findings and Option A/B architecture.
- Historical `OK/CLAIM` matrix remains non-governing, with evidence.
- Option A remains recommended but unselected; B remains non-selectable.
- Watchdog cell unresolved; T `NOT_ACTIVATED`; claim `OPEN`.

## Closure

Verdict `READY_FOR_OFFICINA_P1_IDENTITY_V2_2_FINAL_XY_CONFIRMATION` only if all repairs are exact. Include hashes, exact replacement index, no-regression table, updated counts, one bounded question per reviewer, residual choices and negative authorization. Do not modify existing files.
