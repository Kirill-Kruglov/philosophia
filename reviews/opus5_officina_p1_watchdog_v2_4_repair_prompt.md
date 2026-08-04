# Officina P1 watchdog v2.4: bounded completeness and install repair

You are Claude Code Opus 5, specification author. Produce a narrowly scoped v2.4 correction. You are **not** the independent X reviewer.

## Governing inputs

Read:

- watchdog packet chain through `successor/OFFICINA_P1_WATCHDOG_FREEZE_AUTHOR_CHOICE_PACKET_V2_3_CORRECTION.md`;
- the two v2.3 governing files;
- `reviews/opus_officina_p1_watchdog_v2_3_final_x_confirmation.md`;
- `reviews/sol_officina_p1_watchdog_v2_3_final_y_confirmation.md`;
- the accepted generic-harness and batch-settlement chains.

Both v2.3 lines returned `REVISE`. Preserve every item they confirmed. Modify no historical file. The new v2.4 pair must wholly replace the v2.3 governing pair when accepted.

## A. Restore omitted behavior in the peer amendment

Adopt the X report's exact bounded repairs:

1. Add governing constants: quiescence max passes `8`, interval `100_000_000 ns`, watchdog update-ack timeout `1_000_000_000 ns`; distinguish the already governed ack-absence timeout. State these are restatements, not choices.
2. Add the complete forbidden-disposition rule for a deadline freeze: forbid `T_PROCESS_CLOSED`, `T_PROCESS_VOLUNTARY_STOP`, `T_PROCESS_E1_EXHAUSTED`, `T_PROCESS_E3_DUE`, and `T_PROCESS_RESOURCE_STOP`; forbid valid close/exhaustion/pause/review terminals from a freeze overrun; preserve ordinary harness P3→P4 resource stop. Cause is single-valued `PROCESS`; restate PROVED/UNKNOWN routing.
3. Restate publication/ack/liveness completely: atomic lease table, strictly increasing `table_seq`, publication before `SIGCONT`/capability/admission, exact ack schema and keys, `healthy`, `dead`, `updated_monotonic_ns`, `ack_monotonic_ns`, old deadline authoritative until ack, and the exact meaning of `ACKED`.
4. Make the swap-only carve-out constructible by restating the replacement-freeze id preimage, record key sets, resume/invalidation companions, `I1..I7`, `ACK_PENDING`, ordering and terminal routes. No historical lookup may be required.
5. Restate the total production/duplicate/conflict/consumption order across fallback, freeze and replacement-freeze object classes, including fallback priority and conflicting rejected-object hashes.
6. State the lease-table publication rule explicitly even where redundant with item 3.

## B. Repair guards and installation atomically

Adopt both X and Y findings:

1. Reserve `G-10` uniquely for unresolved W-A/W-B variant blocks. Move its literal patterns into GUARDDATA so it cannot match itself. Rename the earlier authoring-discipline label to a distinct non-conflicting id.
2. Move the **complete handoff list into both governing files**. No normative dependency on an author closure is allowed.
3. Narrow the one-file rule to body/wording guards. Define a closed multi-file input set for the joint-install guard.
4. Treat the pre-install verifier digest only as a non-enforced baseline. Explicitly permit and pin the post-handoff verifier implementing the joint-install guard.
5. Define one externally anchored, content-addressed install record that binds: the v2.4 peer amendment and composite, exact immutable provenance set, accepted peer/batch chain, manifest schema/version/bytes, post-handoff verifier bytes, tests 92..103 and passing attestation. No component may attest its own presence or digest. State the trust root, creation order, no-replace rule, pre-production check and fail-closed recovery without circularity.
6. Add omission, extra-member, stale, mixed-generation and substituted verifier/manifest/test fixtures for every component class. No partial subset may run.

## C. Recompute authority accounting

State a reproducible counting rule with pairwise-disjoint categories. Correct the v2.3 `112` count; independently derive the v2.4 count after all additions. Keep exactly two governing specification files for behavior, zero historical loci with force, zero historical bytes edited. Distinguish governing-locus counts, provenance occurrence counts and the generated install record.

## D. Preserve confirmed behavior

Preserve route D/W exhaustiveness, one supervisor writer, `SIGNAL_GROUP`, killer-watchdog rejection, four retained reads, PCS journal non-scientific status, W-A/W-B definitions, endpoint counts, recommendation, filename/namespace conclusions, no implicit option selection and all negative destinations.

No new option, token, scientific cell, implementation authority or activation authority may be introduced.

## Deliverables

Write new files only:

- `successor/OFFICINA_P1_WATCHDOG_FREEZE_AUTHOR_CHOICE_PACKET_V2_4_CORRECTION.md`
- `successor/OFFICINA_GENERIC_HARNESS_WATCHDOG_FREEZE_AUTHORITY_AMENDMENT_V1_1_DRAFT.md`
- `successor/OFFICINA_GENERIC_HARNESS_SUPERVISOR_CONTROL_CHANNEL_P1_OPERATIVE_COMPOSITE_V1_4.md`
- `reviews/opus5_officina_p1_watchdog_freeze_choice_v2_4_closure.md`

The closure must:

- emit `READY_FOR_OFFICINA_P1_WATCHDOG_V2_4_INDEPENDENT_XY_CONFIRMATION` or a precise blocker;
- disposition X23-B1..B4, M1..M4 and every Y install finding one-to-one;
- give exact hashes, restatement checklist, counting proof and partial-install state table;
- explicitly require the next X review to be performed by an agent that did not author v2.3/v2.4, preferably Claude Opus 4.8 or Fable 5;
- authorize nothing; keep T `NOT_ACTIVATED`, claim `OPEN`, both author cells unsigned.

Do not modify existing files and do not commit.
