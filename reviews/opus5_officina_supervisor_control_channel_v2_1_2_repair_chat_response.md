All inputs verified. Writing the v2.1.2 correction layer.

Custody verified: exactly two new files, all governing artifacts byte-unchanged, the pre-existing dirty set untouched.

**[successor/OFFICINA_GENERIC_HARNESS_SUPERVISOR_CONTROL_CHANNEL_V2_1_2_CORRECTION.md](successor/OFFICINA_GENERIC_HARNESS_SUPERVISOR_CONTROL_CHANNEL_V2_1_2_CORRECTION.md)** — 1547 lines, `2cd8b7b5…`. Narrow layer: §N0 index names 44 superseded sentences/clauses/rows and lists the 28 sections carrying forward verbatim; §N1–§N9 map one-to-one onto R1–R9.

**[reviews/opus5_officina_supervisor_control_channel_v2_1_2_closure.md](reviews/opus5_officina_supervisor_control_channel_v2_1_2_closure.md)** — line 1 `READY_FOR_OFFICINA_SUPERVISOR_V2_1_2_FINAL_XY_CONFIRMATION`, with all 12 required proof obligations.

Decisions worth your attention:

- **R1** — I applied *both* repairs the reviewers offered, not either/or: the decision path is now **derived** from `operation_id` (one legal path per operation, killing the wrong-path attack outright), the id preimage drops `author_decision_sha256`, and the file hash is a sink. The worked example's digests are real and forward-reproducible (`disposition_id = e330a384…`, `author_decision_sha256 = 0773f29c…`) from patterned synthetic inputs, labelled non-installable.
- **R3** — the requirement ("no instruction before a killable identity") is met by a **gated first instruction**: the grandchild's literal first act is a one-byte read on a release pipe whose only write end the CLI holds, so CLI death EOFs it into `_exit(3)` and releases the lock. Identity is produced by the *middle child* and recorded by the *CLI*, plus a new `SPAWNING_GROUP.json` written immediately after the **first** fork — a durable group kill handle that exists before the grandchild does.
- **R7** — I declined Opus's *optional* X211-m1 relaxation and said why: treating any at-or-above-prefix hash as a no-op ack would make several occurrences simultaneously acknowledgeable and weaken the contiguous-prefix proof R8 depends on. Instead the reply envelope now publishes the acknowledgement frontier and its hash, so no client ever has to guess, and the stale hash keeps one deterministic result.
- **R8** — beyond decoupling GC from the ack epoch, I made the **prefix test the first classification step**. That makes GC timing client-invisible, makes a crash mid-GC harmless in any deletion order, and is exactly signed B1's "redeliverable until a durable acknowledgement".

One defect neither reviewer raised, disclosed in §N9.2 rather than carried: v2.1.1's canonical-empty-result hash was `SHA-256(b"[]")`, but this repo's `canonical_json` appends a newline, so the correct value is `SHA-256(b"[]\n") = 37517e5f…`. Both values are shown so no implementer picks the wrong one.

Zero new constants, zero new refusal/`INVALID` tokens, zero import-allowlist delta, no author cell reopened — hence `READY` rather than `BLOCKED`. T remains `NOT_ACTIVATED`; the programme claim remains `OPEN`; the amendment token stays unsignable pending independent v2.1.2 X/Y confirmation on the bytes.
