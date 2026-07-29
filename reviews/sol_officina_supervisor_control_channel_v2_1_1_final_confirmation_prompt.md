# Prompt for GPT-5.6 Sol: independent Officina supervisor v2.1.1 Y-line confirmation

Act as the **independent clean-context Y-line reviewer**. Claude Code Opus 5
authored v2.1.1 as a specification author; its closure is not review evidence.
Re-derive every conclusion from the contract bytes and the signed selections.

Work in the local `philosophia` repository at or after commit `9a60ca5`. Read
these artifacts in full:

- `successor/OFFICINA_GENERIC_HARNESS_SUPERVISOR_CONTROL_CHANNEL_V2_DRAFT.md`
- `successor/OFFICINA_GENERIC_HARNESS_SUPERVISOR_CONTROL_CHANNEL_V2_1_CORRECTION.md`
- `successor/OFFICINA_GENERIC_HARNESS_SUPERVISOR_CONTROL_CHANNEL_V2_1_1_CORRECTION.md`
- `successor/OFFICINA_SUPERVISOR_AUTHOR_SELECTIONS_V1_SIGNATURE.md`
- `successor/OFFICINA_SUPERVISOR_OUTPUT_CAPACITY_SELECTION_V1_SIGNATURE.md`
- `successor/OFFICINA_GENERIC_HARNESS_CONTRACT_V2_3_1_CORRECTION.md`
- `successor/OFFICINA_BATCH_SETTLEMENT_CORE_AMENDMENT_V1_1_1_CORRECTION.md`
- `reviews/sol_officina_supervisor_control_channel_v2_1_final_confirmation.md`
- `reviews/opus_officina_supervisor_control_channel_v2_1_final_confirmation.md`
- `reviews/officina_supervisor_v2_1_authorship_note.md`

Treat
`reviews/opus5_officina_supervisor_control_channel_v2_1_1_closure.md` as an
untrusted author claim. Recompute the v2.1.1 SHA-256; expected committed value:

```text
ee3171724c89bd7e8f890141f42bf478838608c6f1908f9284218f1e940be635
```

This is a static contract review. Run no code, tests, probes, supervisor,
controller, worker, watchdog, endpoint, or smoke. Alter no existing file,
runtime state, code, test, specification, signature, or review.

## Required question

Does v2.1.1 implement signed A3, B1, C1, D1, and K1 literally, with:

- exactly-once, retry-stable, generation-total semantics for all eight commands,
  including observation-form `OPERATION_STATUS`;
- validity-first dominance at takeover;
- a constructible and total spawn/bootstrap identity with a reviewed adapter as
  the executable root;
- no K1 capacity replenishment at settlement, rename, promotion, failure, or
  unused reservation;
- one closed, executable author custody-absence authority;
- an honest A3 leakage boundary;
- no scientific, resource, or invalidity field left to implementer discretion;
- no author cell reopened?

## Mandatory independent traces

Re-run, from the rules rather than the author's examples:

1. Your complete eight-row B1 trace table: lost request; lost reply; client
   crash after observing reply; generation change; effect before committed;
   ack+GC+old retry; concurrent same-scope clients; repeated STATUS. Apply it to
   all eight commands and distinguish `NEW` from explicit `RETRY(handle)`.
2. Tombstone/allocator arithmetic under arbitrary client-file deletion,
   concurrent allocation, missing `.done`, successor ack with the wrong prior
   hash, non-contiguous acknowledgements, GC, and post-GC replay. No predicate
   may rely on an unavailable old reply hash.
3. Reducer chain logic under legitimate descendant heads, accepted-only legal
   prefixes, conflicting suffixes, and supervisor loss. Verify that ordinary
   history cannot become G5 and behavior cannot continue across takeover.
4. Spawn/bootstrap construction: independently recompute both hashes and check
   every fork/exec role, fixed descriptor, adapter phase, timeout, lock, PID
   reuse/start identity, stale grandchild, and watchdog identity cut.
5. C1 evidence-authority checklist: publication/ack triggers, old-deadline
   authority, drain-before-freeze, stale-generation collision, strict-positive
   overrun, supervisor witness validation, UNKNOWN fallback, and proof that the
   watchdog cannot settle or select a valid terminal.
6. OPERATION_ADMIT ordering across all crash cuts and supervisor loss.
7. K1 trace: reservation → live/pending → settlement/failure → quarantine or
   promotion → delivery ack → disposition. Attack stale, substituted, replayed,
   partial, forged, wrong-parent, and custody-still-present disposition cases.
   Confirm `actual_bytes` never reduces accounted capacity.
8. Worker-status/EOF and output-integrity matrix, including zero frames,
   equal-size substitution and the named directory-swap/timing/metadata A3
   residuals.

Check that every new control constant/schema/path is deterministic and only
mechanical. Look for new defects introduced by v2.1.1. A fail-closed route is
not automatically correct if it manufactures invalidity from ordinary valid
history or silently destroys forward progress.

## Deliverable

Create exactly one new file and modify nothing else:

`reviews/sol_officina_supervisor_control_channel_v2_1_1_final_confirmation.md`

Line 1 must be exactly one of:

- `CONFIRM_OFFICINA_SUPERVISOR_V2_1_1_Y`
- `REVISE_OFFICINA_SUPERVISOR_V2_1_1`

Then include:

- recomputed hashes and review base;
- one-to-one disposition for Sol C1..C5 and M1..M3;
- the complete B1, C1, K1, reducer/takeover, spawn, admission, and output traces;
- any new findings ordered Critical/Major/Minor, with exact loci and smallest
  bounded repair;
- a no-regression table for A3/B1/C1/D1/K1 and inherited signed surfaces;
- whether any genuinely new author cell is required;
- the exact authorization boundary.

If confirmed, authorize only Kirill's informed author signature token
`I_ACCEPT_OFFICINA_SUPERVISOR_CONTROL_CHANNEL_AMENDMENT`. Do not authorize
implementation, T activation, entropy, runtime construction, or scientific
work. If revised, keep the token unavailable and require another independent
X/Y check of the repaired bytes.

Confirm no code/test/probe/process ran, no existing file changed, no T/Q/C or
scientific artifact was created, T remains `NOT_ACTIVATED`, and the programme
claim remains `OPEN`.
