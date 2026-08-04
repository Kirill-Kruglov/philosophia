I have the amendment written. Now let me check the `§P1-14` subsection numbering so the handoff section lands in sequence.

`§P1-14.8` is free. Generating composite v1.4 now.

Two defects in my own generation: test 102 reintroduces the self-match, and the GUARDDATA opening is ragged. Fixing both.

Let me fix a tag collision I created (`S-1..S-5` vs `S1/S2`), then count mechanically.

Now let me establish the counting rule mechanically and derive the v2.4 figures.

Now the v2.4 packet.

Now the closure.

One placeholder hash to correct in the closure.

**`READY_FOR_OFFICINA_P1_WATCHDOG_V2_4_INDEPENDENT_XY_CONFIRMATION`** — four new files, zero existing files modified, nothing committed.

| File | SHA-256 |
|---|---|
| [PACKET_V2_4_CORRECTION.md](successor/OFFICINA_P1_WATCHDOG_FREEZE_AUTHOR_CHOICE_PACKET_V2_4_CORRECTION.md) | `ce68b810…` |
| [AMENDMENT_V1_1_DRAFT.md](successor/OFFICINA_GENERIC_HARNESS_WATCHDOG_FREEZE_AUTHORITY_AMENDMENT_V1_1_DRAFT.md) | `ec5ddff8…` |
| [COMPOSITE_V1_4.md](successor/OFFICINA_GENERIC_HARNESS_SUPERVISOR_CONTROL_CHANNEL_P1_OPERATIVE_COMPOSITE_V1_4.md) | `c904ec43…` |
| [v2_4_closure.md](reviews/opus5_officina_p1_watchdog_freeze_choice_v2_4_closure.md) | `1e230432…` |

## A — behaviour restored

All six X omissions closed in the amendment: `QC-1..QC-5` (8, 100 ms, 1 s; ack-absence distinguished as already-governed, all marked restatements); `FD-1..FD-4` (the five forbidden terminals, ordinary P3→P4 resource stop expressly preserved, single-valued `PROCESS`, PROVED/UNKNOWN routing); `AK-1..AK-7` (ack schema, `healthy`, `dead`, whose clock each sample is, the exact meaning of `ACKED`); `RF`/§A7.1–3 (preimage, three key sets, `I1..I7`, `S1/S2`, `ACK_PENDING` with its bound); `TO-1..TO-5` (production/duplicate/conflict/total order, fallback priority); `PUB-1..PUB-4` standalone.

The closure carries a **34-row restatement checklist** — 20 rows were restored or made constructible in v2.4, which is the honest measure of how incomplete v2.3 was.

## B — guards and install

The Y line's `G-10` diagnosis was **more complete than my own X self-review**: the identifier was already taken by the §P1-14.3 authoring discipline with test 76 exercising it. So: discipline renamed `AD-1`, `G-10` reserved uniquely, patterns moved to GUARDDATA as `VARIANT_MARKER` outside `AD-1`'s range.

Generating v1.4 I caught two of my own defects and fixed them: **test 102 quoted the markers**, which would have reproduced the identical self-match in the test matrix; and a ragged `§P1-17` opening. Body markers fell 26 → 24, balanced 12/12, all in real variant blocks.

`§P1-14.1` narrowed to body/wording guards with `G-11` as the one exception over a closed seven-class set. The `verification.py` digest is now a named **non-enforced pre-install baseline** excluded from `M2` — resolving the circularity where the gate forbade its own installation. Install record is content-addressed, trust root is the external signature file, no member attests itself, record installed last. Twelve new fixtures (104–115), with omission/extra/stale each being seven fixtures — one per class.

## C — counting

`112` is withdrawn. The failure was that v2.3 stated a *membership* rule but no *counting* rule, so masthead edits were counted inconsistently and C1 was double-counted. v2.4 defines one locus, excludes document metadata explicitly, and derives **180 = 126 + 54** mechanically. The disjointness check caught a tag collision I'd introduced (`S-1..S-5` vs `S1/S2`), repaired by renaming to `FB-1..FB-5`.

## Two things you should weigh

**Only one independent line has reviewed this work.** The v2.3 X pass was mine on my own bytes, and this round proves that under-detects — the independent Y line found a defect I missed while examining the very same guard. The closure states as a precondition that the next X review must come from a non-author agent (Opus 4.8 or Fable 5). Until then v2.4 has one independent line, not two.

**The partial-install table has 20 rows, and row 20 — the only runnable one — is not reachable today.** Both author cells are unsigned. `T = NOT_ACTIVATED`, claim `OPEN`, no install record created, nothing authorized.
