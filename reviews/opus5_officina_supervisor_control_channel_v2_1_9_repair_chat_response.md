I'll verify the pinned hashes and read both v2.1.8 reviews.

All three hashes verify. Reading the Y-line review first, since its counterexamples govern.

Now gathering the exact loci the Y-line cites for the importer conflict (M218-2).

Custody verified: exactly two new files, the pre-existing dirty and untracked handover paths byte-identical, `verification.py` unmodified at `327b1bb2…`.

## Done — v2.1.9 bounded repair

| Deliverable | SHA-256 |
|---|---|
| [OFFICINA_GENERIC_HARNESS_SUPERVISOR_CONTROL_CHANNEL_V2_1_9_CORRECTION.md](successor/OFFICINA_GENERIC_HARNESS_SUPERVISOR_CONTROL_CHANNEL_V2_1_9_CORRECTION.md) | `1468c9ab…f3b0` |
| [opus5_officina_supervisor_control_channel_v2_1_9_closure.md](reviews/opus5_officina_supervisor_control_channel_v2_1_9_closure.md) | `c2ea6984…b583` |

All three pinned hashes verified before authoring. Closure line 1: `READY_FOR_OFFICINA_SUPERVISOR_V2_1_9_FINAL_XY_CONFIRMATION`.

**C218-1** — one supported topology (sole-root image, single task, no catching disposition, normalized `SIGCHLD`), gated by a new step `c3t` reading `/proc/self/cmdline`, `/proc/self/task`, and `Threads:`. `c3n` gains a reset pass that clears every caught signal using numbers **derived from the kernel's own `SigCgt` mask** — so no new `signal` member — and `V-4` verifies `SigCgt == 0`. The prohibition becomes an executor-set theorem: a task joins a thread group only via `clone(CLONE_THREAD)` from a task already in it; signal handlers are the only asynchronous entry and none exists; every other callback class is synchronous and therefore inside the reachable set where the **signed verifier** already rejects `threading`/`ctypes`/`sys`/`atexit`. The Y replay is closed at step 1, before any signal.

**M218-1** — one `WAIT_ONE` classifier instantiated for all five sites with exact entry condition, existing-constant deadline, signal policy, transition, cleanup/handoff, lock behaviour, continuation; plus a result × site product and a proof of mutual exclusivity. W-5's `m8`-before-`m9` race is two non-blocking attempts, no signal, no deadline, success unaffected; W-4's `ECHILD` cannot block P3, whose death proof rests on `/proc`.

**M218-2** — the smaller Y repair: `generic_harness.py` is sole root **and** sole importer; containment moves from file granularity to name-and-call-site granularity. Four sentences superseded with stated scope, including harness §9's `signal` conjunct only and §V2.10's byte-unchanged `verification.py` clause — which your finding implies but does not name.

**M218-3** — all four contradiction sources shown to require a platform, kernel, or implementation-contract contradiction; `B-CONTRADICTED` reclassified as a non-returning safety sink outside supported history, with `s5` named a consequence and explicitly not a resolver.

**m218-1** — `MASK_FIELD` fixes the grammar and imposes `4·d ≥ int(signal.SIGCHLD)` **and** `d == 16` before conversion; `SigIgn: 0` now routes to `VERIFY_INCONCLUSIVE`, no fork.

No new numeric constant or scientific/resource choice was reached, so no `BLOCKED_…_AUTHOR_CELL`. Six weakest points are stated against myself in the closure — chief among them that `SA_NOCLDWAIT` is still written but unreadable, and that the theorem's step 2 is a claim about CPython's execution model rather than a kernel fact. Three bounded questions per line. T `NOT_ACTIVATED`; claim `OPEN`; token unavailable pending fresh independent confirmation of digest `1468c9ab…`.
