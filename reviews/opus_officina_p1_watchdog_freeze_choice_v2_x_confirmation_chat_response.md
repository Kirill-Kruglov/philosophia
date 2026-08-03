Hashes recorded. Let me read the two v1 reviews to recall the exact findings (X F1–F3, Y-C1..C3/M1..M3/m1) this round must confirm closed.

That's my v1 X-line review (F1, F2, F3). Now the Sol Y-line v1 review for Y-C1..C3/M1..M3/m1:

I have the complete v1 finding set (X F1–F3; Y-C1..C3, M1..M3, m1). Now let me map the v2 packet structure and read the closure (untrusted).

Clean finding-to-section mapping. Let me read the v2 closure (untrusted author self-assessment), then verify against the packet and contracts.

Now let me verify the hashes the closure pins (v1 reviews + contracts), treating all as untrusted claims.

All hashes match. Now the core of this round — the new §3 PCS classifier (determinations 2, 3, 8). Let me read it in full.

§3 is the substantive core. Let me verify the primitive/constant claims (determination 3) and the STAT/quiescence facts (determination 8) directly against the composite and correction bytes.

Let me settle the one live determination-3 risk — the `_clock(CLOCK_MONOTONIC)` call in §3.6 — by checking how the composite actually invokes `_clock` and whether `CLOCK_MONOTONIC` is bound anywhere.

Confirmed a concrete determination-3 finding: `_clock` is `time.clock_gettime_ns` (composite :636), which requires a clock-id argument, but `CLOCK_MONOTONIC` appears nowhere in the composite's pinned constant set and is **not** disclosed (only `_MSG_EOR` is). Let me now read the W-A and W-B repairs (§4, §5) for determinations 4 and 5.

W-A (§4) closes Y-C2 (constant one-shot key, PCS-supplied handle id), Y-M3 (T-1..T-7 window ordered before the non-returning reaper), and prices the action. Let me read §4.1 (descriptor accounting) and the W-B repair §5.2–5.6 (determination 4).

§4.1 closes both W-A non-blocking gaps I flagged in v1 (slot-6 type A5W-1..3; descriptor accounting). Now W-B's endpoint-loss classifier (§5.2–5.6, determination 4):

W-B (§5) fully closes F2/Y-M1 (MSG_EOR discriminator E-1a/b/c, no death claim, endpoint-loss rename) and Y-M2 (R3 ACCEPTED-before-act, R2 no-retry). Now the ABSENT amendment (§6, determination 7) and the twelve-site audit (§7, determination 6):

§6 makes the ABSENT fallback constructible via biconditional nullable keys (determination 7), and §7 lists twelve sites with R7/R6/R11 replacing (not adding to) the contradictory rows. Now the two independent completeness checks: (a) exhaustively audit the composite for any freezer/witness sentence the twelve-site list missed, and (b) verify §6.3's V2_1_2_CORRECTION claims.

My exhaustive grep surfaced freezer/witness sentences that may not be in the twelve-site list — notably line 2283 ("dedicated freezer watchdog as the normal witness") and invariant 89 (line 2758, "wrong freeze writer"). Let me read these precisely to determine whether the twelve-site audit is complete.

Two candidate missed sites found. Let me confirm invariant 89's exact text and check the remaining freeze-reader mention (line 2389) for completeness.

Three composite sites (row-4 rationale ¶ 2278-2287, invariant 89 at 2758, and the reader sentence at 2389) assert the watchdog freezer/witness role or SIGNAL_GROUP-mediation and are **not** in the twelve-site list. Let me verify §6.3's V2_1_2_CORRECTION claims (determination 7) before finalizing.

All §6.3 claims verified: the fallback preimage (:833-840) omits the three amended keys (ids stay stable), `pgid`/`start_identity` are indeed mandatory-non-null today, and `process_id` — left mandatory — is a claim identifier (not a raw PID), so it stays constructible by an opaque-handle supervisor. Determination 7 is confirmed. I now have everything needed. Writing the confirmation deliverable.

Let me confirm the deliverable is in place and no existing file was modified.

The confirmation is complete and written to [reviews/opus_officina_p1_watchdog_freeze_choice_v2_confirmation.md](reviews/opus_officina_p1_watchdog_freeze_choice_v2_confirmation.md). Both v2 targets are byte-unchanged (hashes re-confirmed), and I modified no existing file. The `sol_...v2_confirmation.md` alongside is the Y-line's parallel deliverable, not mine.

## Verdict: `REVISE_OFFICINA_P1_WATCHDOG_FREEZE_CHOICE_V2`

I recomputed all target, v1-review, and contract hashes (all match the closure's pins), treated the closure as untrusted, and verified every claim against the composite and correction bytes.

**Nine of ten v1 findings confirmed closed** (F2, F3, Y-C1, Y-C2, Y-C3, Y-M1, Y-M2, Y-M3, Y-m1), each against the cited bytes. The new §3 PCS classifier is structurally sound: `STAT_OBSERVE_G` stat-field indices are correct (state/ppid/pgrp/session = tokens 1–4 after `)`, starttime = token 20), `KV-1..6` and the `pgid_or_null` population fill a real v1.2 gap, deduplication/handle-state totality/sixteen tokens/three terminals all check out. Determinations 4, 5, 7 fully confirmed — including that the ABSENT amendment is serializable (biconditional nullable keys; `process_id` stays constructible because it's a claim identifier, not a raw PID; the fallback-id preimage is stable).

**Two concrete residual defects force REVISE:**

1. **R-A (determination 3):** the classifier's `freeze_ns := _clock(CLOCK_MONOTONIC)` (§3.6 C-4) needs the constant `CLOCK_MONOTONIC` — `_clock` is `time.clock_gettime_ns` (composite :636), which requires a clock-id argument — but that constant is **not** in the §P1-3.4 pinned set (:419-423) and is **not** disclosed (only `_MSG_EOR` is). So the answer to the bounded X-question is **NO**. Smallest repair: disclose `CLOCK_MONOTONIC` as a second binding-block addition.

2. **R-B (determination 6):** the "complete" twelve-site freezer/witness audit **misses at least two normative sites** — invariant 89 (line 2758: still names the watchdog as a permitted freeze writer, and requires freezes to go through `SIGNAL_GROUP`) and the §P1-13.2 row-4 rationale paragraph (2278-2287: "dedicated freezer watchdog as the normal witness," "two possible executing processes"). Beyond enumeration, the new §3 classifier freezes via the PCS's **autonomous `_killpg`**, which invariant 89 would reject as "not through SIGNAL_GROUP" — a contradiction the packet's own new verifier rule (`_killpg` in classifier + SIGNAL_GROUP handler, packet :1567) never reconciles. Smallest repair: add these as sites 13–15 and admit the autonomous classifier as a signed freeze-execution site.

Both repairs are mechanism-preserving and fall identically on W-A and W-B, so **W-B remains the mechanically preferable option after repair**. The verdict authorizes nothing. `T = NOT_ACTIVATED`, claim `OPEN`, identity-cell non-selection preserved.
