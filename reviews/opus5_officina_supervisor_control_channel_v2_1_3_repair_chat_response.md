All three pinned hashes match. Reading both independent v2.1.2 reviews.

Custody verified: exactly two new files, all governing artifacts byte-unchanged, pre-existing dirty set untouched.

**[successor/OFFICINA_GENERIC_HARNESS_SUPERVISOR_CONTROL_CHANNEL_V2_1_3_CORRECTION.md](successor/OFFICINA_GENERIC_HARNESS_SUPERVISOR_CONTROL_CHANNEL_V2_1_3_CORRECTION.md)** — 1428 lines, `72bfcc3f…`. §U0 names 38 superseded clauses and lists the frozen carry-forwards by name; §U1–§U8 map onto R1–R8.

**[reviews/opus5_officina_supervisor_control_channel_v2_1_3_closure.md](reviews/opus5_officina_supervisor_control_channel_v2_1_3_closure.md)** — line 1 `READY_FOR_OFFICINA_SUPERVISOR_V2_1_3_FINAL_XY_CONFIRMATION`, all 12 proof obligations.

Judgment calls worth surfacing:

- **R1 is a reduction, and I said so in the verdict rather than burying it.** Deleting the detection claim removes a fail-closed `HASH` quarantine v2.1.1 had. That loss was already caused by v2.1.2's K1-compliant deletion of the second hash; v2.1.3 only stops mis-describing it. §U1.5 makes this normative: no later layer may restore detection via a second content hash or a content-derived stored reference **without a new author decision on K1**. That's where the tradeoff would live if the author ever prefers detection over hash-once — I didn't make or default that choice.
- **R2's "literal first instruction" required one deviation with a reason.** A truly-first *blocking* read can't give the EOF-exit property, because the forked middle child inherits its own copy of the write end, so EOF never arrives. I made the stage pipes `O_NONBLOCK` at creation, so the middle child's literal first instruction is a *bounded* gate read: EOF still exits it early, and the bound exits it even if a write end leaks. That is strictly stronger than the EOF-only design and makes the `c4`→`c7` window total with no record at all.
- **R5 forced a reconciliation neither review named:** adding `RESULT_MANIFEST.json` to the operation directory would have made §N2.3's subset test refuse *every* promoted operation's own disposition. §U5.5 adds it to the closed allowed L2 set.
- **R7:** I bound `authorized_utc == signed_utc` byte-for-byte rather than renaming the field, because renaming would alter a key list both reviewers verified in place — the prompt's "if that does not create a wider schema change" condition isn't met.

Zero new constants, zero new tokens, zero import delta, no author cell reopened. T remains `NOT_ACTIVATED`; the programme claim remains `OPEN`; the amendment token stays unsignable pending independent v2.1.3 X/Y confirmation on hash `72bfcc3f…`.
