I need to flag something before I start: **I authored all four of these documents in the previous turn.** The closure itself states the author "cannot be its independent X or Y reviewer." I'll do the most adversarial audit I can and report findings honestly, but this is a self-review, not an independent X line — the verdict must not be recorded as genuine independent confirmation.

Let me recompute everything.

All four hashes reproduce; zero historical files modified. Now the omitted-restatement checklist — the core question.

Confirmed first gap. Let me check the rest of the checklist systematically.

Now the decisive test: do these rules live in the **accepted** (live) harness chain, or only in the immutable historical chain?

Both gaps confirmed as blocking. Let me complete items 3, 5–8.

Found a second unambiguous blocker. Let me verify the remaining items and recompute the counts.

**`REVISE_OFFICINA_P1_WATCHDOG_V2_3`** — written to [opus_officina_p1_watchdog_v2_3_final_x_confirmation.md](reviews/opus_officina_p1_watchdog_v2_3_final_x_confirmation.md). No files modified, nothing committed. All four hashes reproduce; zero historical files changed.

## First, the thing that matters most

**I wrote these four documents in the previous turn.** This is a self-review, and the closure under audit says the author "cannot be its independent X or Y reviewer." I did the audit and it found real blockers, so the findings are worth having — but had it come out clean, the honest output would have been a refusal to certify, not a confirmation. A reviewer who did not author these bytes still has to do this pass.

## Answer to the bounded question: yes, restatement created the defect

Four rules now exist **only in immutable history**, which your standard defines as blocking:

**`X23-B1` — quiescence constants.** §A3.3 and §A3.4 *use* `T_WATCHDOG_QUIESCE_MAX_PASSES` and `T_WATCHDOG_QUIESCE_PASS_INTERVAL_NS`. Their values (8, 100 ms) appear in neither governing file, neither the accepted harness chain nor the batch-settlement amendment — only at historical `V2_1:60-61` and `V2_1_1:89-90`. The strict-progress branch isn't constructible.

**`X23-B2` — forbidden dispositions.** The worst one. Historical §W3.4 forbade `T_PROCESS_CLOSED`, `T_PROCESS_VOLUNTARY_STOP`, `T_PROCESS_E1_EXHAUSTED`, `T_PROCESS_E3_DUE` and — explicitly closing X-C4.1 — `T_PROCESS_RESOURCE_STOP` on a deadline freeze. Zero occurrences in governing bytes. Meanwhile the **live, accepted** harness contract at `V2_DRAFT:140-142` positively assigns `T_PROCESS_RESOURCE_STOP` to an overrun-bearing transition. So an implementer reading only permitted files sees permission and no prohibition: **a valid terminal becomes reachable from an overrun, silently reversing a prior X closure.**

**`X23-B3` — ack semantics.** Both route triggers turn on "acked"/"not acked". The `t-watchdog-ack.v1` key set, `healthy()`, `dead`, `T_WATCHDOG_UPDATE_ACK_TIMEOUT_NS` and `updated_monotonic_ns` are defined nowhere live. Route selection isn't evaluable.

**`X23-B4` — `G-10` is unsatisfiable**, independent of restatement. Its definition sits in the BODY region and contains the literal `[W-A]`/`[W-B]` strings it forbids there. After resolution deletes all 28 blocks, G-10 still matches itself — fires forever, no build ever passes. This violates §P1-17's own stated rationale that guard patterns live in a separate region "so that they are never matched against themselves." Fix: move the patterns into GUARDDATA alongside G-1..G-5.

Plus three non-blocking: §A7's swap-only carve-out isn't constructible (no key sets, no resume predicate), §N5.5's cross-class consumption order is absent, and **112 is not reproducible** — it double-counts the C1 masthead edit (which is R1, inside the 23) and omits four other governance edits; correct total is 114. Root cause is `Y22-2` recurring: v2.3 states a valid *membership* rule but no *counting* rule.

## What held up

Mechanical derivation verified — 37 anchors, 31 diff hunks, six sentinels intact, every v1.2 watchdog-executor original at zero occurrences, and the corrected action alphabet finds exactly one hit (a `WATCHDOG_UNREAPED` reap sentence, no authority). The document-level authority proof reproduces step by step. `ROUTE-D`/`ROUTE-W` are exhaustive, both `SIGNAL_GROUP`-mediated, one writer, consistent across row 4, `SW-2`, §P1-13.7, §P1-13.8, §P1-13.9, invariant 89 and test 95. `G-11` leaves no partial runnable state. All prior accepted W-A/W-B content, the four verbatim identity reads, the recommendation and negative space are unchanged.

Exact repair text for all seven findings is in the report, landing only in the two governing surfaces.
