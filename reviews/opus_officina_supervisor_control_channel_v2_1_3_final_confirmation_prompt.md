# Prompt for Claude Code Opus 4.8: independent Officina supervisor v2.1.3 X-line confirmation

Act as the **independent clean-context X-line reviewer**. Claude Code Opus 5
authored v2.1.3; its closure is not review evidence. Re-derive the result from
the actual bytes.

Work in `philosophia` at or after commit `45f30f6`. Read the complete
v2/v2.1/v2.1.1/v2.1.2/v2.1.3 supervisor chain, both author signatures,
inherited generic-harness/batch-settlement contracts, and your own and Sol's
v2.1.2 reviews. Treat
`reviews/opus5_officina_supervisor_control_channel_v2_1_3_closure.md` only as
an untrusted author claim.

Recompute the v2.1.3 correction SHA-256; expected:

```text
72bfcc3f088ba538157145aed0bccc95a9ff2e1ad6c41f0579f32c9926274888
```

Static review only. Read-only inspection and literal-example hashing are
allowed. Run no repository code/test/probe or Officina process, and modify no
existing file/runtime state.

## Required question

Is X212-M1 closed by a truthful detection boundary that preserves literal
hash-once; is X212-m1 recorded so no later layer can silently re-violate it;
are Sol C1/C2/M1–M4/m1/m2 closed where they intersect X-line process/crash/
object semantics; and does v2.1.3 introduce no new Critical/Major, weaken no
fail-closed behavior by a new v2.1.3 choice, promote no watchdog/replacement
fact into a second runtime authority, and reopen no A3/B1/C1/D1/K1 cell?

Attack at least:

1. **Hash truthfulness:** search the entire carried chain for any surviving
   equal-size same-inode detection or future-immutability claim. Verify §U1's
   mechanical checks and three residual windows exactly match §N4 behavior.
2. **Two-stage spawn:** every CLI/middle/grandchild scheduling and crash cut;
   nonblocking bounded gates; inherited write-end EOF subtleties; pre/post
   `setsid`; pid/start/sid/pgid verification; record durability; permitted
   `kill` versus `killpg`; lock release and deliberately stopped A3 residuals.
3. **Watchdog replacement:** prove overdue versus swap-only paths are disjoint;
   no swap witness; I-before-S precedence; `ACK_PENDING`, `RESUMABLE`,
   `INVALID` totality; every deadline/ack/crash race; no healthy group forced
   invalid and no supervisor-loss resume.
4. **GC:** eligibility before deletion, exact accepted→committed→reply→ack
   order, fsyncs, every crash prefix, retry concurrency, empty-directory
   completion, and proof no owed reply or eligibility witness is lost.
5. **Result manifest:** exact schema/order/hash DAG, manifest-before-settlement,
   sole-pass in-memory tuple origin, zero content rereads, settlement binding,
   empty/quarantined cases, disposition verification and L2 custody-set
   reconciliation. Reproduce documented illustrative hashes where possible.
6. **Singleton records:** preflight over spawning/middle/group/child; every
   EEXIST branch; live/dead/PID-reused/malformed states; child→group→middle→
   spawning removal; fsync/crash prefixes; no live unlink or stale wedge.
7. **Authority summaries:** timestamp equality, canonical proof classes/root/
   enumeration hashes, non-narrowing custody proof and scientific-field
   exclusion.
8. **No regression:** every independently closed prior repair, constants,
   imports, nine events, E1/E2/E3, Q/C boundary and T inactivity.

Do not accept worked examples in place of total governing rules.

## Deliverable

Create exactly one file and alter nothing else:

`reviews/opus_officina_supervisor_control_channel_v2_1_3_final_confirmation.md`

Line 1 exactly:

- `CONFIRM_OFFICINA_SUPERVISOR_V2_1_3_X`, or
- `REVISE_OFFICINA_SUPERVISOR_V2_1_3`.

Include hashes/base, one-to-one disposition of X212-M1/m1 and all Sol v2.1.2
findings, the eight attack traces, new findings by severity with exact loci and
smallest repair, no-regression table, author-cell determination and exact
authorization boundary.

If confirmed, authorize only Kirill's signature token
`I_ACCEPT_OFFICINA_SUPERVISOR_CONTROL_CHANNEL_AMENDMENT`; not implementation,
activation, entropy, runtime construction or science. If revised, keep it
unavailable and require another X/Y check.

Confirm no process/test/probe ran, no existing file changed, no artifact was
created, T remains `NOT_ACTIVATED`, and the programme claim remains `OPEN`.
