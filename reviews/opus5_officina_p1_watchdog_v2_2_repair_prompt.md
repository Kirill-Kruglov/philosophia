# Task: bounded v2.2 correction of P1 watchdog-freeze choice

You are Claude Code Opus 5 acting as specification author, not reviewer. This correction closes the peer-chain and remaining composite residuals in the final v2.1 X/Y reviews. No implementation, process control, activation, spend, data, outcome or claim movement.

## Inputs

Read committed bytes of:

- `successor/OFFICINA_P1_WATCHDOG_FREEZE_AUTHOR_CHOICE_PACKET_V2_DRAFT.md`
- `successor/OFFICINA_P1_WATCHDOG_FREEZE_AUTHOR_CHOICE_PACKET_V2_1_CORRECTION.md`
- `reviews/opus_officina_p1_watchdog_freeze_choice_v2_1_final_confirmation.md`
- `reviews/sol_officina_p1_watchdog_freeze_choice_v2_1_final_confirmation.md`
- the full accepted generic-harness, §W3/§Z4/§N5, settlement, binding and operative-composite chain

Treat both `REVISE` verdicts as binding. Preserve existing files.

## Deliverables

Create exactly:

1. `successor/OFFICINA_P1_WATCHDOG_FREEZE_AUTHOR_CHOICE_PACKET_V2_2_CORRECTION.md`
2. `reviews/opus5_officina_p1_watchdog_freeze_choice_v2_2_closure.md`

## A. Amend the complete governing peer writer/executor surface

Perform and record an exhaustive peer-chain audit. At minimum replace:

- accepted generic-harness v2 §5a watchdog execution sequence (`revoke -> freeze/terminate -> backend synchronize -> prove quiescence -> settle`);
- §W3.3's watchdog-written freeze procedure and its logical/physical writer statements;
- §W3.5 supervisor-death row;
- every governing file/durable-object table that assigns `t-freeze-observation.v1` to watchdog or “watchdog, or supervisor when dead”;
- §Z4.6 conjunct 8 allowing `killer == WATCHDOG` and conjunct 9's “watchdog-written witness” binding;
- §N5.3 “watchdog remains a witness only” and both §N5.4 “watchdog-written” descriptions;
- every settlement, archive, recovery, reader, predicate, writer and single-writer statement reached by these objects.

Under either W-A/W-B, new-contract paths must reject `killer == WATCHDOG`; row-4 `t-freeze-observation.v1` is supervisor-written only on the signed dead-watchdog route. The common PCS classifier writes only its P1 journal, never peer evidence. `t-freeze-fallback-observation.v1` remains a separate supervisor-written fallback.

Enumerate exact governing files/sections and revise blast radius/common-token surface. A disclosure of an unaudited peer surface is not closure.

## B. Resolve the composite supervisor-identity read cluster

Use the minimal single-valued route: **retain the watchdog's read-only supervisor-identity check**, while removing freeze/write authority.

- Amend `R8` so “role-entry only” explicitly permits the existing read-only identity operation but no signal, freeze, quiescence proof, evidence write or settlement.
- Enumerate and preserve consistently §P1-9.2 property 8, §P1-13.2 row-3 reader (b), §P1-13.7 watchdog read row and invariant 87.
- Recompute the final composite site count and separate “replaced role sites” from “checked-and-retained read sites.”

## C. Correct W-A descriptor wording

- Give `R16` an explicit W-A variant with three sealed endpoints, including slot-6 request socket, and a W-B variant with two sealed pipes.
- Keep the PCS from retaining the update-pipe write end in both variants.
- Reconcile endpoint types, descriptor accounting and leak proof.

## D. Correct filename/object identity history

- Withdraw v2 §0.3/§1.1 and v2.1 `O-8` claims that `<witness_id>.json` versus `<process_id>.json` is unresolved.
- State the governing sequence: §W3.3 predecessor used `<process_id>.json`; §Z4.5 expressly superseded it with `WATCHDOG/FREEZE/<witness_id>.json`; operative composite agrees.
- Preserve `witness_id = SHA-256(canonical {supervisor_generation_sha256, process_id, table_seq})`, no-replace identity and replay naming. Do not reopen filename selection.

## E. Preserve and verify

- Keep all v2/v2.1 repairs accepted by both lines: constants, classifier, endpoint-loss semantics, W-A gate, W-B pre-action journal, nullable fallback, count-key rename, schema separation and publication boundary.
- Recompute exact site counts, peer files, predicates, tests, handoff and token blast radius.
- W-B may remain recommended but unselected; identity cell unselected; T `NOT_ACTIVATED`; claim `OPEN`.

## Closure

Verdict `READY_FOR_OFFICINA_P1_WATCHDOG_V2_2_FINAL_XY_CONFIRMATION` only if the entire governing peer chain is closed. Include hashes, exhaustive replacement index, corrected counts, no-regression table, one bounded question per reviewer, residual choices and negative authorization. Do not modify existing files.
