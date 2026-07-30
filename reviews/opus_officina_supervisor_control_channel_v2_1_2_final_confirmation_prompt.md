# Prompt for Claude Code Opus 4.8: independent Officina supervisor v2.1.2 X-line confirmation

Act as the **independent clean-context X-line reviewer**. Claude Code Opus 5
authored v2.1.2 as the specification author; you did not author it. Re-derive
the verdict from the bytes and do not trust its closure.

Work in the local `philosophia` repository at or after commit `9743d1f`. Read
in full:

- `successor/OFFICINA_GENERIC_HARNESS_SUPERVISOR_CONTROL_CHANNEL_V2_DRAFT.md`
- `successor/OFFICINA_GENERIC_HARNESS_SUPERVISOR_CONTROL_CHANNEL_V2_1_CORRECTION.md`
- `successor/OFFICINA_GENERIC_HARNESS_SUPERVISOR_CONTROL_CHANNEL_V2_1_1_CORRECTION.md`
- `successor/OFFICINA_GENERIC_HARNESS_SUPERVISOR_CONTROL_CHANNEL_V2_1_2_CORRECTION.md`
- `successor/OFFICINA_SUPERVISOR_AUTHOR_SELECTIONS_V1_SIGNATURE.md`
- `successor/OFFICINA_SUPERVISOR_OUTPUT_CAPACITY_SELECTION_V1_SIGNATURE.md`
- `successor/OFFICINA_GENERIC_HARNESS_CONTRACT_V2_3_1_CORRECTION.md`
- `successor/OFFICINA_BATCH_SETTLEMENT_CORE_AMENDMENT_V1_1_1_CORRECTION.md`
- `reviews/opus_officina_supervisor_control_channel_v2_1_1_final_confirmation.md`
- `reviews/sol_officina_supervisor_control_channel_v2_1_1_final_confirmation.md`

Treat `reviews/opus5_officina_supervisor_control_channel_v2_1_2_closure.md`
only as an untrusted authored self-assessment. Recompute the correction hash;
expected value:

```text
2cd8b7b53c8efc292535ef79f38aa5e33ce57c5834138cc3deb1700f7edae373
```

Static review only. Read-only source inspection and hashing literal documented
bytes are allowed. Do not run repository code, tests, probes, supervisors,
controllers, workers, watchdogs, adapters, endpoints, or smoke commands. Do
not edit existing files or runtime state.

## Required question

Is X211-C1 closed by an acyclic, forward-computable, content-closed disposition
authority; are X211-m1 and X211-m2 disposed of without a new defect; does
v2.1.2 close every converged Sol C1–C4/M1–M5/m1 repair that intersects X-line
process/crash/hash semantics; and does it introduce no new Critical or Major,
weaken no fail-closed behavior, create no second watchdog authority, and reopen
no A3/B1/C1/D1/K1 author cell?

Independently attack at least:

1. **Hash DAG:** reproduce the §N1 dependency order and illustrative digests.
   Search every id/path/file-hash binding for direct or transitive
   self-reference. Attack path substitution, extra author bytes, stale parent,
   replay, wrong operation, and partial installation.
2. **Custody set:** prove the derived set includes every source, quarantine,
   promoted, staging, temporary, operation-bound, and unknown location the
   protocol can create. Trace both sides of `os.replace`, every crash, and the
   one-lock absence proof. No existing byte may coexist with release.
3. **Earliest fork cut:** inspect the literal first instruction, both sealed
   channels, first-fork group record, middle-child report, CLI record, release
   gate, PID/start/PGID proof, CLI/middle/grandchild death, and every bounded
   `SPAWN.lock` route. There must be no unkillable lock holder or deadlock.
4. **Write/hash once:** account for every content-byte read/write/hash across
   output ingestion, verification, result-metadata hashing, settlement,
   promotion, retries, and crash recovery. Check that substitution defence
   survives while each content byte is written once and hashed once.
5. **Watchdog:** rejected-witness fallback naming and no-replace behavior,
   `UNKNOWN` with zero current unresolved members, consumption order, and the
   non-overdue replacement-resume proof. Confirm no freeze instant is invented
   and no supervisor-loss resume is possible.
6. **FD remap:** exhaustively simulate `(3,4)`, `(4,3)`, one source in the
   target set, both outside, repeated temporary collisions, failures, closure,
   inheritability, direction checks, and self-stop order. Prove termination.
7. **B1/GC:** wrong/null/exact/stale hash priority before allocation; published
   frontier; all eight commands; ack-prefix advance; later GC; ack-before-
   archival; observation STATUS; concurrent retry/GC; crash mid-GC; prefix-first
   classification; owed-reply preservation and retention bound.
8. **Reconciliations:** absent tombstone defaults, canonical empty-result hash,
   schemas/enums/path grammars/object ownership, import allowlist, signed
   inherited surfaces, and any new contradiction introduced by §N1–§N9.

Do not infer totality from worked examples. Verify the governing rules over all
admitted cases.

## Deliverable

Create exactly one new file and modify nothing else:

`reviews/opus_officina_supervisor_control_channel_v2_1_2_final_confirmation.md`

Line 1 must be exactly one of:

- `CONFIRM_OFFICINA_SUPERVISOR_V2_1_2_X`
- `REVISE_OFFICINA_SUPERVISOR_V2_1_2`

Then include recomputed hashes/review base, a one-to-one disposition for
X211-C1/m1/m2 and all new Sol findings, the eight attack traces, any new
findings by severity with exact loci and smallest bounded repair, a
no-regression table, whether any new author cell is required, and an exact
authorization boundary.

If confirmed, authorize only Kirill's informed signature token
`I_ACCEPT_OFFICINA_SUPERVISOR_CONTROL_CHANNEL_AMENDMENT`; do not authorize
implementation, T activation, entropy, runtime construction, or scientific
work. If revised, keep the token unavailable and require another X/Y check.

Confirm no process/test/probe ran, no existing file changed, no runtime or
scientific artifact was created, T remains `NOT_ACTIVATED`, and the programme
claim remains `OPEN`.
