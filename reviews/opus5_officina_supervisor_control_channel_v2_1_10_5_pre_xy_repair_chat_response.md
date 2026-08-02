Confirmed both F1 and F5 mechanically: the PCS-side table has **no `SPAWN.lock` row at all**, and `B-2`'s inline verdict conflicts with `B-4`'s requirement that the full vector be collected first. Writing the repair.

Custody verified: exactly two new files; the binding, its closure, the P1 signature, and `verification.py` unchanged at their pinned digests.

## Done — P1 composite repaired

| Deliverable | SHA-256 |
|---|---|
| [OFFICINA_GENERIC_HARNESS_SUPERVISOR_CONTROL_CHANNEL_V2_1_10_5_P1_PRE_XY_REPAIR.md](successor/OFFICINA_GENERIC_HARNESS_SUPERVISOR_CONTROL_CHANNEL_V2_1_10_5_P1_PRE_XY_REPAIR.md) | `798d0cbd…57cc` |
| [opus5_officina_supervisor_control_channel_v2_1_10_5_p1_pre_xy_repair_closure.md](reviews/opus5_officina_supervisor_control_channel_v2_1_10_5_p1_pre_xy_repair_closure.md) | `68cf3b87…8041` |

Closure line 1: `READY_FOR_OFFICINA_SUPERVISOR_P1_V2_1_10_5_XY_REVIEW`.

**F1** — confirmed mechanically: the binding's PCS table has **no `SPAWN.lock` row at all**, so it sits at a kernel-chosen number, no `DUP2` overwrites it, no `CLOSE` names it, and it leaks into every `posix_spawn`ed role at its original number. Repaired by `O_CLOEXEC` creation with a mandatory `F_GETFD` readback (one route, no `F_SETFD` fallback), plus a grandchild-side `dup2(lock_fd, 3, inheritable=True)` with readback before the supervisor `execve`. **No conflict with the carried fork-shared-lock theorem** — §P1R.1.5 tables the holders and flag state at nine points. Tracing this also surfaced that the binding conflated the supervisor path with the `posix_spawn` path: the supervisor has **no `file_actions` at all**.

**F2** — "holds every PID" deleted; the PCS owns and reaps exactly `pid_mid`, controllers, workers and watchdogs, observes the supervisor only via `PEER_EOF`, and may reach it by signal only through the carried post-`c11` group route. `init` reaps the orphaned supervisor.

**F3** — index row 16 corrected to close-then-`REAP_ROLE`; an eight-locus sweep confirms **zero** watchdog signal paths remain.

**F4** — the absolute no-callback theorem is **withdrawn**. What survives is only the AST property (`S-19` narrowed): a single-statement `except` body. The interval is named a **transient capability exposure** under A3, with an explicit statement that this is procedural discipline, not adversarial same-process security. No proxy introduced, so no `BLOCKED` was needed.

**F5** — the `B-2`/`B-4` issue was a real ambiguity, not cosmetic: an aborting parse would have left later installed descriptors unclosed. `B-2` and `B-3` are now non-aborting; only `B-4` acts.

The sharpest thing to flag: **F1's repair introduces a worse failure mode if botched.** If an implementer omits `G-3`'s readback, a silently `CLOEXEC` slot 3 closes the lock at `execve` and releases the singleton while the supervisor lives — worse than the leak. `S-21` and test 489 are the only guards, and I put that first in my own weakest points and into Y-Q1 so a reviewer rules on it directly.

All four defects were in my own bytes and one static pass found them. Token unavailable until both lines confirm `6197d2a4…` as corrected by `798d0cbd…`. T `NOT_ACTIVATED`; claim `OPEN`.
