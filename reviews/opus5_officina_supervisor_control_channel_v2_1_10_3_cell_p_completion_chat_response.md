All governing hashes pinned. Writing the P4 trace and the corrected cell.

Custody verified: exactly two new files; all governing inputs unchanged at their pinned digests; `verification.py` unmodified.

## Done — Cell P completed, P4 confirmed real

| Deliverable | SHA-256 |
|---|---|
| [OFFICINA_GENERIC_HARNESS_SUPERVISOR_CONTROL_CHANNEL_V2_1_10_3_CORRECTION.md](successor/OFFICINA_GENERIC_HARNESS_SUPERVISOR_CONTROL_CHANNEL_V2_1_10_3_CORRECTION.md) | `02d862e7…3143` |
| [opus5_officina_supervisor_control_channel_v2_1_10_3_closure.md](reviews/opus5_officina_supervisor_control_channel_v2_1_10_3_closure.md) | `d4641438…a18c` |

Closure line 1: `READY_FOR_OFFICINA_SUPERVISOR_CELL_P_AUTHOR_SELECTION`. No option selected.

**P4 is implementable.** The isolated `SUPERVISOR` role bootstrap has exactly the primitives it needs before `sys.path` gains any project entry, and *importing a module does not change the process* — so the creator stays the watchdog's parent and sole reaper for the whole generation. Both signed C1 detectors survive, and the watchdog gets a fresh isolated address space. Insertion point is `A-8a`–`A-8h`, between `A-8` and `A-9`.

**The trace refuted four things v2.1.10.2 asserted**, and each is corrected rather than carried:

- The role bootstrap's `{os, sys}` is insufficient — its own `A-6` uses `F_GETFL`, so `fcntl` is required.
- Every descriptor at 3–10 arrived via `POSIX_SPAWN_DUP2`, which **clears close-on-exec** — so all of them, including `SPAWN.lock`, would leak into a spawned watchdog. Fixed by explicit overwrite/close actions.
- §T1.6's `/proc/self/fd` sweep would **close legitimate authority descriptors of live roles**, since the supervisor's pinned set grows with every `SPAWN_ROLE`. Replaced by "close exactly the parsed vector", safe in both directions if the kernel truncation fact is wrong.
- Post-import `kill(wd_pid)` reintroduces C218-1 on one PID. Withdrawn; termination is EOF-driven, `waitpid`-only, with a stated fail-closed stall.

**P2 is withdrawn** as strictly dominated — P4 matches it on both detectors and beats it on address space, creation-time state, lock inheritance, and kill authority. Surviving set: **P1, P3, P4**, with a bounded two-dimensional exhaustiveness argument that I explicitly do not claim is absolute.

`SPAWN_WATCHDOG` survives with a proved different purpose — replacement after a proved death, which the contaminated supervisor must not fork itself — so the operation count stays nine. Its cost is stated: replacements are PCS-parented and have **one** detector, not two.

The B1/D1 costs are unchanged and stated without discount, including that the supervisor retains a narrow one-child PID trust surface — "P4 removes PID authority from the supervisor" would be false and is not claimed.

Eight weakest points are written against my own proposal, including that three of my layers have now needed a governance correction. Next gate: your selection of exactly one token, then a binding correction, then fresh X/Y. T `NOT_ACTIVATED`; claim `OPEN`; amendment token unavailable.
