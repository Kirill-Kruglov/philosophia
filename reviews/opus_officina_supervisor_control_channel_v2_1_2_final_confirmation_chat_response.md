Let me verify the git state, recompute the v2.1.2 hash, and confirm the target file doesn't yet exist.

Hash matches exactly; target absent. Let me confirm the inherited-surface hashes are unchanged from my v2.1.1 review, then read the Sol v2.1.1 confirmation (which I have not seen — it holds the "new Sol findings") and the v2.1.2 correction.

Inherited surfaces are byte-identical to my v2.1.1 review. Now let me read the Sol v2.1.1 confirmation (its findings are inputs I must disposition), then the v2.1.2 correction in full.

Now I have Sol's full v2.1.1 findings (C1–C4, M1–M5, m1) — these plus my X211-C1/m1/m2 are what v2.1.2 must close. Notably Sol's C3 (grandchild hangs in descriptor-scrub *before* writing `SPAWNING_CHILD.json`) is a real residual in the X21-C2 area I had marked closed. Let me read v2.1.2 in full.

Let me continue reading the rest of v2.1.2.

This is a thorough repair. The headline claim is that §N1 makes the disposition authority acyclic. The task explicitly permits "hashing literal documented bytes," and item 1 asks me to reproduce the §N1.8 illustrative digests. Let me independently recompute both worked digests — a decisive test of forward-constructibility.

All four documented digests reproduce **exactly**: the disposition-id preimage (396 bytes → `e330a384…`), the decision-file hash (504 bytes = sum of line lengths + 8 → `0773f29c…`), and the canonical empty-result `SHA-256(b"[]\n") = 37517e5f…` (with the "NOT this" `SHA-256(b"[]")` also confirmed). This is decisive: the §N1 construction is genuinely acyclic and forward-computable — X211-C1 is closed.

I traced the remaining repairs (N2–N9) in full. They close Sol C1/C2/C3/M1–M5/m1 and my X211-m1/m2 soundly — **except** one: the N4 "hash-once" repair (for Sol C4) over-claims a substitution defense a single hash cannot provide. Let me mark this chapter and write the deliverable.

Let me verify the deliverable's line 1 and that I created exactly one file, altering nothing else.

The deliverable is in place. Line 1 is exactly `REVISE_OFFICINA_SUPERVISOR_V2_1_2`, and the only file I added is my review — every handover-dirty and untracked file (including the Sol v2.1.2 confirmation, which was already present) is untouched, and runtime negative-space is intact.

## Verdict: REVISE_OFFICINA_SUPERVISOR_V2_1_2

Written to [reviews/opus_officina_supervisor_control_channel_v2_1_2_final_confirmation.md](reviews/opus_officina_supervisor_control_channel_v2_1_2_final_confirmation.md). The v2.1.2 hash matches the expected value exactly, and every inherited surface and both v2.1.1 review files are byte-identical to what v2.1.2 cites.

**X211-C1 is genuinely closed.** I recomputed §N1.8 from the literal documented bytes: the 396-byte disposition-id preimage → `e330a384…` and the 504-byte decision file → `0773f29c…` **both reproduce exactly**, and the dependency DAG (`operation_id → derived path`; `{activation, path, operation_id} → disposition_id → file bytes → author_decision_sha256` as a downstream sink) is acyclic and forward-computable. §N9.2's `SHA-256(b"[]\n") = 37517e5f…` also verifies. X211-m1 (frontier-published ack priority), X211-m2 (non-overdue replacement-resume), and **all of Sol C1/C2/C3/C4/M1–M5/m1** close soundly on re-derivation.

**What blocks confirmation — one new Major, X212-M1:** the write-once/**hash-once** repair (§N4, satisfying Sol C4's literal-K1 demand) deletes v2.1.1's inline hash, leaving **no stored reference** — yet §N4.2 claims "the equal-size and inode substitution defences are **fully retained**." A single hash provably cannot detect a same-inode, equal-size, in-place content substitution:
- the held `r` descriptor is not a snapshot (it reads the current, possibly-substituted bytes),
- the worker counts are untrusted, and
- `result_sha256` is *produced by* the pass, so it can't be its own reference.

Inode substitution (via the held descriptor) and size/link anomalies *are* detected, but the equal-size same-inode case now **promotes silently** where v2.1.1 `HASH`-quarantined it. So the claim is false and a v2.1.1 fail-closed behavior is weakened — reintroducing the exact X21-M7/Sol-M2 over-claim class over a signed-A3 boundary. Since the required question forbids "a new Major" and "weakening fail-closed behavior," the answer is *no*.

It's Major, not Critical: capacity accounting is untouched, nothing wrongly releases, and `result_sha256` still describes the promoted tree. The fix is a **bounded truthfulness edit** in §N4.2 — state the case honestly as an A3 procedural residual, keep hash-once — reopening no author cell and needing no new author choice. The token `I_ACCEPT_OFFICINA_SUPERVISOR_CONTROL_CHANNEL_AMENDMENT` stays unavailable; a v2.1.3 layer with that one repair needs another independent X/Y check.

Confirmed: no process/test/probe ran (the two recomputations were `hashlib` over literal documented bytes in the scratchpad), no existing file changed, no runtime or scientific artifact created, T remains `NOT_ACTIVATED`, and the programme claim remains `OPEN`.
