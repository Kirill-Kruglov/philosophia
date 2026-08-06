I'll start by verifying the pinned bytes and orienting myself in the repository.

All six pinned hashes match. Note: HEAD is `69b69aa` (the review-request commit), a descendant of `cb37808` — let me confirm the pinned surfaces are unchanged between them.

Only the review prompts differ between `cb37808` and HEAD; all pinned surfaces are byte-identical. Now let me locate the SC-9/SC-10 classifier spec in composite v1.14.

Now let me examine the transform surface (binding v5 §2.2.5) and check for the prior version to establish the regression baseline.

All six pinned hashes verify. Let me now implement SC-9/SC-10 independently and drive the required fixtures.

Now let me implement the full transform independently.

S6's last sentinel was mis-transcribed by hand. Let me extract sentinels programmatically from the binding instead.

X-Q2's transform verifies fully. Now MP-1, the delimited regions, and the detector/PO-0 behaviour.

MP-1 reproduces exactly. But the composite's own pinned `H_HANDOFF` does not match the block it describes. Let me investigate.

This is a substantive finding. Let me determine its exact reach and whether a guard enforces it.

The joint block carries no pinned digest — only `H_HANDOFF` is stale. Now X-Q1: the independent classifier.

Zero permutation-variant tables. Now the Phase-6 rechecks, Phases 1/2/3/5 terminals, and the `_killpg` reachability proof.

All X-Q1 drivers pass. Now the regression boundary — verifying the v2.13 repairs survive.

All checks are complete. Writing the review.

Review complete. Exactly one file created, nothing else touched, nothing committed.

## Verdict

**`OFFICINA_P1_WB_V2_14_X_CONFIRMED_FOR_AUTHOR_ACCEPTANCE`**

- Path: [reviews/fable_officina_p1_wb_v2_14_final_x_review.md](reviews/fable_officina_p1_wb_v2_14_final_x_review.md)
- SHA-256: `685bc98fa0912f78a57be2667881ee3679e9d85542d1e10839d31625049f6bea` (27,981 bytes)

All six pinned hashes recomputed and matched. HEAD is `69b69aa` rather than `cb37808`, but the only diff between them is the two review prompts — every pinned surface is byte-identical, so not `BLOCKED`.

## X-Q1 — answered YES, no counterexample

`(terminal, qualifier, per-entry token, signal sequence)` **is** a single permutation-invariant function. Implemented SC-9 P1..P6 and SC-10 from the composite prose alone. The Y-M1 table gives `T1`/`FREEZE_NOT_ATTEMPTED`/no token/site `a`/zero signals in **both** orders; all seven pair-matrix rows are order-invariant; 216 three-entry tables over six observation classes × all 6 permutations plus four-entry families produced **zero** permutation-variant results. A 1,584-table sweep over the signed value space found 0 violations of P6's six conjuncts, and zero signals ever followed a Phase-6 terminal. SC-7's 24+32+4+6+6=72 partition is exact.

## X-Q2 — every figure reproduces byte-exactly

All 11 spans verify in both directions; full output 624,840 bytes / `9904ff3b…`; all three region digests match; GUARDDATA byte-unchanged (1,816 B compared directly, not inferred); both delimited regions identical across composite, amendment and my resolved output. MP-1 built from its recipe alone: 195-byte payload, 625,035 bytes, `ba513ff0…`, PO-0 fails as required. S7 renders at exactly 277 bytes — my earlier X-L3 and X-L4 are both repaired.

## The one thing worth your attention

**X-1 (Major, defect of record).** Composite v1.14 line 8061 and amendment v1.11 line 1316 both pin `H_HANDOFF = 7c5cabe2…44a7`. That is v1.13's value (4,167 bytes). The actual block is 4,168 bytes, `7d5cd453…0084` — the value the binding and your own closure (lines 76–77) correctly report. The closure did the arithmetic; the repair wasn't propagated into the two governing files.

I did **not** return REVISE for it: nothing consumes `H_HANDOFF` — no guard, OR step, manifest field or verifier rule — and the property it witnesses (byte-identical handoff across the pair) holds, verified three ways. The witness is stale, the fact is true. But the files themselves say "ANY DIFFERENCE IS A DEFECT IN THIS INDIVISIBLE PAIR", so if you want to read that clause on its face it justifies a corrective generation. That's your call, and I said so in the review rather than grading it away.

Three Minors logged without forcing a generation: Phase 3 actually carries three terminal-bearing predicates (SC-10 says one), pre-existing from v1.13 and confined to the journal terminal name; a watchdog with a written `pgid_or_null` self-collides at Phase 3 and would permanently disable the classifier — latent, since v1.14's own lifecycle argument keeps that field NULL; and SC-9 P4's claim that the least-index site is "the same ENTRY under every permutation" is false for multi-member classes, with no effect on the invariant answer.
