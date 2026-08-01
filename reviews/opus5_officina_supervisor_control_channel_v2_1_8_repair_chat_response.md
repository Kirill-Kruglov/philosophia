I'll start by reading the current state of the repository and the full supervisor chain.

All three pinned hashes verify. Reading the v2.1.7 correction and both reviews.

Every `m5`/`rel2` occurrence is either a deletion record or the scoped retention for cuts at or after `c8`; no stage-M claim rests on them.

## Done — exactly two files created, nothing else touched

**Deliverables**

| File | SHA-256 |
|---|---|
| [OFFICINA_GENERIC_HARNESS_SUPERVISOR_CONTROL_CHANNEL_V2_1_8_CORRECTION.md](successor/OFFICINA_GENERIC_HARNESS_SUPERVISOR_CONTROL_CHANNEL_V2_1_8_CORRECTION.md) | `33b0b916…0ed50` |
| [opus5_officina_supervisor_control_channel_v2_1_8_closure.md](reviews/opus5_officina_supervisor_control_channel_v2_1_8_closure.md) | `3dba0990…e113e` |

All three pinned hashes verified before authoring. Closure line 1: `READY_FOR_OFFICINA_SUPERVISOR_V2_1_8_FINAL_XY_CONFIRMATION`.

**The named engineering delta.** `ALLOWED_ABSOLUTE_IMPORTS` gains exactly one member, `signal` — the "zero import delta" claim is superseded, and §V218.1.4 enumerates all fourteen loci that carried it (including v1 draft §S5's §S7-probe claim and §W2.6's/§W6.4's justifying parentheticals, whose *claims* survive as directly-tested restrictions). `verification.py` is unmodified; only its future one-string amendment is specified.

**The five repairs.** R1: step `c3n` runs one `signal.signal(SIGCHLD, SIG_DFL)` — a full `sigaction` clearing an inherited `SIG_IGN` *and* `SA_NOCLDWAIT` — before every attempt's first fork, verified against `/proc/self/status`'s `SigIgn`/`SigCgt`, with no fork on any non-`NORMALIZED` result, plus a sole-reaper contract and a closed five-site wait table. `ECHILD` maps to inconclusive. R2: a three-valued `OWNERSHIP` label makes the fork the primary identity authority, gating every `os.kill` by one precondition, with `IDENTITY_SAFE` rebuilt as a ten-row total table (X217-m1's `ppid` gap becomes the premise-failure detector). R3: `T3` deleted; `T1`/`T2`/non-returning `B`, pairwise disjoint; ownership carries the kill so a stopped child is reaped with `/proc` entirely unreadable. R4: the `m0`/`rel1_w`/fork-shared-lock trace replaces the `m5`/`rel2` argument. R5: §V217.1 and §V217.4 carried byte-for-byte.

**Three things I flagged against myself** in §V218.4.5 and the closure's "weakest points": `SA_NOCLDWAIT` is written but not readable back (backed by three contradiction detectors); `B-CONTRADICTED` deliberately does not terminate under a violated sole-reaper contract; and the normalization creates a new unreaped-zombie residual for a long-lived CLI taking `T2`.

Custody: the pre-existing dirty and untracked handover paths are byte-identical. Nothing ran, no code or test was written, no artifact produced. `I_ACCEPT_OFFICINA_SUPERVISOR_CONTROL_CHANNEL_AMENDMENT` remains unavailable pending fresh X and Y reviews of digest `33b0b916…`. T `NOT_ACTIVATED`; claim `OPEN`.
