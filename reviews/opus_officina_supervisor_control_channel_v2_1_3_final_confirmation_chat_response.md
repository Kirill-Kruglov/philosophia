Let me verify the git state, recompute the v2.1.3 hash, confirm the target is absent, and check the inherited-surface hashes are unchanged.

Hash matches exactly; inherited surfaces are byte-identical to my v2.1.2 review. Now I need Sol's v2.1.2 findings (C1/C2/M1–M4/m1/m2 per the required question), which I haven't seen. Let me read it, then v2.1.3 in full.

Now I have Sol's v2.1.2 findings (C1, C2, M1–M4, m1, m2). Combined with my X212-M1/m1, these are what v2.1.3 must close. Note Sol's m2 is the honesty-of-post-verification-window issue closely related to my X212-M1. Now let me read v2.1.3 in full.

Let me continue reading the rest of v2.1.3.

This is a carefully targeted correction. Items 5 and 7 of the attack list ask me to reproduce the manifest and custody-proof digests. Let me independently recompute all documented illustrative hashes (§U5.6, §U8.3) from the literal bytes — a decisive check on the manifest hash-DAG and the custody-proof summary.

All four documented digests reproduce **exactly** (entries 265 B → `5359c361…`; manifest 638 B → `e4ec3182…`; the 7-name enumeration → `3f8e1c99…`; empty → `37517e5f…`). The result-manifest hash-DAG (§U5) and custody-proof summary (§U8) are forward and reproducible.

I've now traced the entire correction. Let me record my assessment before writing. v2.1.3 closes every targeted finding; I found only two Minors (both fail-closed), no new Critical/Major. Let me mark the chapter and write the deliverable.

Let me verify the deliverable's line 1 and that I created exactly one file, altering nothing else.

The deliverable is in place. Line 1 is exactly `CONFIRM_OFFICINA_SUPERVISOR_V2_1_3_X`, the only file I added is my review (the pre-existing handover-dirty and untracked files, including Sol's v2.1.3 confirmation, are untouched), and runtime negative-space is intact.

## Verdict: CONFIRM_OFFICINA_SUPERVISOR_V2_1_3_X

Written to [reviews/opus_officina_supervisor_control_channel_v2_1_3_final_confirmation.md](reviews/opus_officina_supervisor_control_channel_v2_1_3_final_confirmation.md). This is the first **CONFIRM** in the chain — after two REVISE rounds (v2.1.1's circular disposition-id, v2.1.2's hash-once over-claim), v2.1.3 closes everything.

The v2.1.3 hash matches the expected value exactly, and every inherited surface and both v2.1.2 review files are byte-identical to what v2.1.3 cites. I **reproduced all four documented digests from the literal bytes**: `result_sha256 = 5359c361…` (entries, 265 B), `result_manifest_sha256 = e4ec3182…` (manifest, 638 B), the operation-directory enumeration `3f8e1c99…`, and the empty value `37517e5f…`.

**Everything targeted is closed** with exact, executable, non-circular, reproducible text:
- **X212-M1** (my v2.1.2 Major) — §U1 deletes the false "equal-size defence fully retained" claim and replaces it with an honest detection truth table + three named A3 residuals, keeping literal hash-once. **X212-m1** — §U1.5 adds a normative bar forbidding any future layer from re-introducing a second content hash without a new K1 decision.
- **Sol C1** (middle-child/`setsid` race) — two-stage gate, `SPAWNING_MIDDLE.json` with no group claim, `killpg` forbidden until kernel-verified `setsid`, pre-record window covered by the bounded `m0` gate.
- **Sol C2** (swap-only resume) — swap-only freeze writes no witness; three mutually-exclusive states (`INVALID`/`RESUMABLE`/`ACK_PENDING`) with I-before-S precedence; no healthy group forced invalid.
- **Sol M1** (GC), **M2** (result manifest), **M3** (singleton records), **M4** (timestamp binding), **m1** (proof summary), **m2** (residual honesty) — all closed and verified.

**No new Critical or Major.** I found two **Minor**, non-blocking, fail-closed defects: X213-m1 (the result-manifest verifier doesn't cleanly cover a QUARANTINED terminal carrying an *orphan* manifest from a `SUPERVISOR_CRASH`-between-manifest-and-settlement — fail-closed, strands capacity, one-clause V6 fix) and X213-m2 (a prose imprecision in one `m0` crash-row: the governing bound is correct, the "sees EOF" mechanism is not). Neither weakens a fail-closed behavior, corrupts accounting, or reopens an author cell.

No fail-closed behavior is weakened by a new v2.1.3 choice, no watchdog/replacement fact becomes a second runtime authority, and no A3/B1/C1/D1/K1 cell is reopened.

**Authorization:** The X-line authorizes Kirill's informed signature token `I_ACCEPT_OFFICINA_SUPERVISOR_CONTROL_CHANNEL_AMENDMENT` — signable **once the independent Y-line (Sol) also confirms these same v2.1.3 bytes**. It authorizes nothing else: no implementation, activation, entropy, runtime construction, or scientific work; signing the amendment does not itself activate T or authorize any spend.

Confirmed: no process/test/probe ran (the recomputations were `hashlib`/`json` over literal documented bytes in the scratchpad), no existing file changed, no runtime or scientific artifact created, **T remains `NOT_ACTIVATED`, and the programme claim remains `OPEN`.**
