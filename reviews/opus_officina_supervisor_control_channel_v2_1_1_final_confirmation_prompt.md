# Prompt for Claude Code Opus 4.8: independent Officina supervisor v2.1.1 X-line confirmation

Act as the **independent clean-context X-line reviewer**. You did not author
v2.1.1. Claude Code Opus 5 authored it in the specification-author role while
Fable 5 was unavailable. Do not treat shared model-family identity as review
continuity: re-derive the result from the bytes.

Work in the local `philosophia` repository at or after commit `9a60ca5`. Read
these files in full:

- `successor/OFFICINA_GENERIC_HARNESS_SUPERVISOR_CONTROL_CHANNEL_V2_DRAFT.md`
- `successor/OFFICINA_GENERIC_HARNESS_SUPERVISOR_CONTROL_CHANNEL_V2_1_CORRECTION.md`
- `successor/OFFICINA_GENERIC_HARNESS_SUPERVISOR_CONTROL_CHANNEL_V2_1_1_CORRECTION.md`
- `successor/OFFICINA_SUPERVISOR_AUTHOR_SELECTIONS_V1_SIGNATURE.md`
- `successor/OFFICINA_SUPERVISOR_OUTPUT_CAPACITY_SELECTION_V1_SIGNATURE.md`
- `successor/OFFICINA_GENERIC_HARNESS_CONTRACT_V2_3_1_CORRECTION.md`
- `successor/OFFICINA_BATCH_SETTLEMENT_CORE_AMENDMENT_V1_1_1_CORRECTION.md`
- `reviews/officina_supervisor_v2_1_authorship_note.md`
- `reviews/opus_officina_supervisor_control_channel_v2_1_final_confirmation.md`
- `reviews/sol_officina_supervisor_control_channel_v2_1_final_confirmation.md`

Read
`reviews/opus5_officina_supervisor_control_channel_v2_1_1_closure.md` only as
an **untrusted authored self-assessment**. It is not review evidence. Recompute
the v2.1.1 SHA-256; the expected committed value is:

```text
ee3171724c89bd7e8f890141f42bf478838608c6f1908f9284218f1e940be635
```

You may inspect the frozen/inactive implementation read-only solely to test
implementability claims. Do not execute tests, probes, supervisors,
controllers, workers, watchdogs, pipes, FIFOs, or smoke commands. Do not edit
code, tests, runtime state, existing specifications, signatures, or reviews.

## Required question

Are all five v2.1 Criticals X21-C1..C5, all eight Majors X21-M1..M8,
and all seven Minors closed by exact, executable, non-circular v2.1.1 text,
with no repair introducing a new defect, no fail-closed behavior weakened to
obtain liveness, no watchdog fact promoted into a second runtime authority,
and no signed author cell A3/B1/C1/D1/K1 reopened?

Attack rather than summarize. At minimum independently trace:

1. **B1 occurrence semantics:** concurrent `NEW`, explicit `RETRY`, lost request,
   lost reply, client-state deletion, reply-observed-before-done crash,
   generation change, successor ack with/without the prior reply hash,
   own-terminal `CLOSE`, contiguous GC, old retry after GC, and both STATUS
   forms. Confirm that allocation is supervisor-authoritative, total,
   reuse-free, and wedge-free.
2. **Reducer/takeover:** committed/replied plans followed by ordinary later
   ledger history; every accepted-only prefix; conflicting suffixes; supervisor
   death at each point. Confirm phase 2A makes all affected live invalidity and
   batch settlement durable before any non-behavioral phase 2B, and that no
   cross-generation reducer can spawn, renew, admit, or `SIGCONT`.
3. **Spawn/bootstrap:** recompute the template and complete-argv identities;
   prove `spawn_intent_id` is non-circular and stable where the contract needs
   stability; verify fixed fds and per-role ordering; inspect every pre-identity
   crash/wedge cut, bounded lock/ack waits, PID/start/PGID death proof, adapter
   self-stop, target preflight, and the separate no-argv watchdog record.
4. **Watchdog:** claim-start/renew/remove publication and acknowledgement,
   drain-before-freeze schedules, stale tables/generations, witness naming,
   the full supervisor acceptance predicate, equality at deadline, missing or
   contradictory evidence, and the C1 sole-authority boundary.
5. **Admission:** every cut before/after `RUNNING.json`, `SIGCONT`, committed,
   and cached `ADMITTED`; confirm same-generation idempotence and
   post-supervisor-loss invalidation cannot strand or resume behind success.
6. **K1:** trace reserve, output, settlement, failure, quarantine, promotion,
   delivery ack, author disposition, and release. Confirm `bytes_reserved`
   remains accounted throughout and only a valid same-lock custody-absence
   disposition releases it. Attack stale, substituted, replayed, forged, and
   partially installed disposition objects.
7. **Output/A3:** worker status/EOF totality, zero output, bounded rehash,
   inode/content substitution, directory-swap residual, timing/metadata
   leakage, and whether every residual is honestly procedural and non-citable.
8. **Exactness:** frame/argv arithmetic, all schemas/enums/paths, no-replace
   ownership, EEXIST continuations, retention/GC, target/interpreter preflight,
   and compatibility with the signed generic-harness and batch-settlement
   surfaces.

Do not accept a worked example unless the governing rule is total. Search for
new contradictions introduced by the repair, not only closure of old ones.

## Deliverable

Create exactly one new file and alter nothing else:

`reviews/opus_officina_supervisor_control_channel_v2_1_1_final_confirmation.md`

Line 1 must be exactly one of:

- `CONFIRM_OFFICINA_SUPERVISOR_V2_1_1_X`
- `REVISE_OFFICINA_SUPERVISOR_V2_1_1`

Then provide:

- recomputed hashes and precise review base;
- one-to-one disposition for X21-C1..C5, X21-M1..M8, and all seven Minors;
- any new findings ordered Critical/Major/Minor with exact loci and smallest
  bounded repair;
- the eight attack traces above;
- a no-regression table for A3/B1/C1/D1/K1 and signed inherited surfaces;
- a direct statement whether a new author cell is genuinely required;
- an authorization boundary.

If confirmed, authorize **only Kirill's informed author signature token**
`I_ACCEPT_OFFICINA_SUPERVISOR_CONTROL_CHANNEL_AMENDMENT`; do not authorize
implementation, T activation, entropy, runtime construction, or scientific
work. If revised, the token remains unavailable and the smallest correction
must receive another independent X/Y check.

Confirm that no process/test/probe ran, no existing file changed, no runtime or
scientific artifact was created, T remains `NOT_ACTIVATED`, and the programme
claim remains `OPEN`.
