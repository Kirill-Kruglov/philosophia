READY_FOR_OFFICINA_SUPERVISOR_P1_V2_1_10_5_XY_REVIEW

# Author closure — Officina supervisor/control-channel v2.1.10.5 P1 pre-X/Y repair

Date: 2026-08-02
Author line: **Claude Code Opus 5, specification author only.** Not an
independent reviewer of this chain.

**This closure is an untrusted self-assessment**, as
`reviews/officina_supervisor_v2_1_authorship_note.md` requires. **Three of the
four contradictions repaired here were in my own v2.1.10.4 bytes, and the
fourth was too.** This layer does not self-confirm; it hands corrected bytes to
two independent lines.

The **P1 author selection is fixed**. This is a bounded pre-review repair. **P3
and P4 are not reopened**, and no new author choice is proposed.

## Byte and hash custody

Repository base: commit `c9f883d98375c0d961dae4821b44e0a2a818bd65`. The working
tree was already dirty at handover; every pre-existing tracked modification and
untracked path is preserved byte-for-byte.

Governing inputs, recomputed and matching:

```text
6197d2a4073d35fc978119db32128c50d12594343ac87731640a1d8e19f09e84  successor/OFFICINA_GENERIC_HARNESS_SUPERVISOR_CONTROL_CHANNEL_V2_1_10_4_P1_BINDING.md
5889461b86870c357a61e1b7327c1285773c4263dd9640bf3e2da202b9bde302  reviews/opus5_officina_supervisor_control_channel_v2_1_10_4_p1_binding_closure.md
6ef98132990f8c686fa9678509bb07ba8259f3d6e4cbc483861edfc03ea8e3ef  successor/OFFICINA_SUPERVISOR_PROCESS_AUTHORITY_SELECTION_V1_SIGNATURE.md
02d862e76f76a57cd154ecfd8a67f88abb02c2ce324e4026e4145069cee63143  successor/OFFICINA_GENERIC_HARNESS_SUPERVISOR_CONTROL_CHANNEL_V2_1_10_3_CORRECTION.md
327b1bb222173407772836a2fdc4e92f89595508aff8b77f68f65816cafbec1e  src/philosophia/officina/verification.py
```

This closure's companion:

```text
798d0cbd51e93cc1f4c0a443785f90d90a2e121d35738189cbee9c61acf557cc  successor/OFFICINA_GENERIC_HARNESS_SUPERVISOR_CONTROL_CHANNEL_V2_1_10_5_P1_PRE_XY_REPAIR.md
```

**Exactly two files were created and nothing else was touched.** The binding,
its closure, the P1 signature, v2.1.10.3, every earlier layer, the A3/B1/C1/D1/K1
signatures, the harness and batch composites, the authorship note, and
`verification.py` are all unedited and match their digests.
`scripts/officina_process_control_bootstrap.py` and
`scripts/officina_role_bootstrap.py` do not exist. No code, test, verifier,
manifest, prompt, prior review, or runtime artifact was edited, staged, or
committed. Method: static authoring only — read-only file and `git` inspection,
literal search, `sha256sum`, and reasoning from pinned Linux/CPython interfaces.

## Verdict

`READY_FOR_OFFICINA_SUPERVISOR_P1_V2_1_10_5_XY_REVIEW`.

F1–F5 close mechanically. No new author decision was reached and no signed
conflict was found, so no `BLOCKED_…` verdict is emitted. In particular **F1's
repair does not conflict with the carried fork-shared-lock theorem** — §P1R.1.5
proves it row by row — so the "stop and name the conflict" branch does not
apply. `I_ACCEPT_OFFICINA_SUPERVISOR_CONTROL_CHANNEL_AMENDMENT` remains
**unavailable** until both lines confirm identical corrected bytes.

## Literal replacement index over v2.1.10.4

| # | Locus | Action |
|---|---|---|
| 1 | §P1B.3.1 PCS-side descriptor table | replaced — gains the missing `SPAWN.lock` row, `FD_CLOEXEC` **set** |
| 2 | §P1B.3.3's five-step leak proof, incl. step 5 and its "`A-5` would refuse, so the failure mode is fail-closed" clause | **replaced as false** — the lock is at a kernel-chosen number outside every destination range, so no `DUP2` closes it |
| 3 | §P1B.3.2 `SUPERVISOR` slot-3 cell "retained, non-`CLOEXEC`, carried §W2.2" | replaced — the non-`CLOEXEC` copy is **created by the grandchild's own `dup2`** |
| 4 | §P1B.1 clause 1 "holds every PID in the system" | replaced by the exact boundary |
| 5 | §P1B.2 tree comment "sole holder of every PID" | replaced |
| 6 | §P1B.2 parent/reaper table and §P1B.12 authority rows | extended with an explicit supervisor row |
| 7 | §P1B.0.1 row 16 ("`SIGNAL_ROLE` + `REAP_ROLE` pair") | replaced — **no signal reaches a watchdog on any path** |
| 8 | §P1B.6.3 `B-1`'s "NO callback, NO finalizer, NO atexit handler, NO buffer flush, and NO unwinding" | **withdrawn as unprovable** |
| 9 | §P1B.6.5 residual paragraph | replaced by the named capability exposure |
| 10 | §P1B.11 rule `S-19` | replaced by an AST-only property |
| 11 | §P1B.6.3 `B-2`'s inline `⇒ ANCILLARY_VIOLATION` | replaced — the parse is **non-aborting** |
| 12 | §P1B.14 rows 442, 443, 447, 456 | replaced by 442R/443R/447R/456R |
| 13 | §P1B.15 weakest points | extended |
| 14 | §P1B.17 review questions | replaced; the reviewed bytes are the binding **as corrected** |

Unchanged and re-asserted: the P1 selection; nine opcodes with one uniform
`SPAWN_WATCHDOG`; five roots; 6 / 3 / 17 imports; `CMSG_SPACE(12)` and max 3
descriptors; no global `/proc/self/fd` sweep; §P1B.6.2's `scm_detach_fds()`
fact; §P1B.13's four cell statements.

## One-to-one F1–F5 disposition

| F | Disposition |
|---|---|
| **F1 — `SPAWN.lock` leak proof false** | Confirmed mechanically: the binding's PCS table has **no lock row at all**, so the descriptor sits at a kernel-chosen number outside 3–8, no `DUP2` overwrites it, no `CLOSE` names it, and being non-`CLOEXEC` it survives every controller/worker/watchdog `execve` at its original number — with `A-5` refusing *after* the leak on the production path. **Repair, all five required elements:** (1) `c1` opens the lock with `_O_CLOEXEC` and a **mandatory `_fcntl(_F_GETFD)` readback**, refusing `LOCK_FD_NOT_CLOEXEC` on failure — one route, no `F_SETFD` fallback; (2) `fork` still copies the descriptor, so the middle's and grandchild's fork-shared references are live (`FD_CLOEXEC` is consulted only at `execve`); (3) on the unique supervisor-grandchild path, `G-1`…`G-6` hoist above 10, `_dup2(h[lock_fd], 3, inheritable=True)` with an explicit `_fcntl(_F_GETFD)` readback proving the flag clear, then close the original; (4) **no** controller, worker or watchdog file-action vector names the lock, and none needs to, because it is `CLOEXEC`; (5) the post-`execve` set is exact **by construction**, and `A-5` is demoted to a verification with the binding's contrary sentence deleted. **No conflict with the carried theorem** — §P1R.1.5 tables the lock's holders and `CLOEXEC` state at nine points and shows §W2.2's property (the grandchild's retained descriptor survives its `execve`) preserved, now produced deliberately rather than inherited by accident. The binding also conflated the supervisor path with the `posix_spawn` role path; §P1R.1.4 separates them — **the supervisor has no `file_actions` at all** |
| **F2 — authority overstated** | "Holds every PID in the system" and "sole holder of every PID" are **deleted**. The exact boundary: the PCS directly owns, reaps and holds numeric authority for `pid_mid`, every controller, every worker and every watchdog; the supervisor receives no PID and exercises no numeric authority; the PCS is **not** the supervisor's parent, cannot `waitpid(supervisor_pid)`, observes it only through the `t-pcs.v1` peer channel, and may reach it by signal only through the carried post-`c11` `killpg` group route with `/proc`-based death proof; **the supervisor is not added to the PCS's direct-child set**; the caller owns and reaps only the PCS; `init` reaps the orphaned supervisor. A six-row process/authority table and a per-target death-proof statement replace the universal phrasing. **The selected P1 meaning is unchanged — only the prose now matches the tree** |
| **F3 — watchdog signalling contradiction** | The operative rule is retained and index row 16 is corrected: close the update **write** end through `CLOSE_OWNED`, then `REAP_ROLE` until `REAPED_POSITIVE`, then §U6.3 removal; timeout ⇒ `WATCHDOG_UNREAPED` ⇒ process invalidity; **no TERM/KILL/STOP/CONT/PROBE to a watchdog on any path**. §P1R.3.2 sweeps all eight loci where a watchdog signal could hide and finds the corrected index row was the only one |
| **F4 — "no callback before `_exit`" not mechanically true** | The absolute theorem is **withdrawn**. §P1R.4.1 names what actually runs between a C-call failure and an `except` body in a contaminated interpreter — exception construction, traceback, unwinding, `__del__`, pending-signal checks, and any host `settrace`/`setprofile`/audit hook. What is retained and provable: the handler is a single `except BaseException` clause whose body is exactly one `_exit_` call, the contract authorises no cleanup/callback/unwind logic there, and the contract installs no exit handlers of its own. What is explicitly **not claimed** is enumerated. The interval from possible installation to actual exit is named a **transient capability exposure** in which same-process hooks or threads may run under A3, with the statement that the contract offers **procedural discipline, not adversarial same-process security**, and that the surface is non-citable and never Q/C evidence. `S-19` is narrowed to the AST property alone. §P1B.6.2's `scm_detach_fds()` claim keeps its reviewer-verifiable status. **No proxy process is introduced**, so no `BLOCKED_…_AUTHOR_CELL` is required |
| **F5 — literal sweep** | The `B-2`/`B-4` duplication is a real ambiguity, not a cosmetic one: `B-2`'s inline verdict read as aborting the parse, while `B-4` requires the **complete** vector first — an aborting parse would leave later installed descriptors unclosed. `B-2` is made **non-aborting**: it records violation flags and always collects the full vector; `B-3` likewise; only `B-4` acts. **One place decides, one place acts.** The nine-item sweep result is tabulated in §P1R.5.2 |

## Corrected process / fd / authority

| Process | Direct parent | Direct children | May `wait` on | May signal | Holds numeric PIDs of |
|---|---|---|---|---|---|
| caller | host | the PCS | the PCS only | nothing | the PCS |
| **PCS** | caller | `pid_mid`, controllers, workers, watchdogs | exactly those | exactly those, plus the supervisor's **group** only after `c11` | exactly those |
| middle (`pid_mid`) | PCS | grandchild until `m9` | nothing | nothing | none |
| **supervisor** | `pid_mid` until `m9`, then **`init`** | **none** | nothing (`ECHILD`) | **nothing** | **none — handles only** |
| watchdog | PCS | none | nothing | nothing | none |
| controller / worker | PCS | per carried contracts | unchanged | unchanged | none |

**`SPAWN.lock` `FD_CLOEXEC` at every boundary:** PCS **set**; middle **set**
(fork-shared, live); grandchild before `G-2` **set**, at slot 3 after `G-2`
**clear**; supervisor after `execve` **slot 3 only, clear**; controller, worker,
watchdog **absent**.

## Corrected crash table

| Cut | Continuation |
|---|---|
| `c1` lock readback shows `FD_CLOEXEC` clear | `LOCK_FD_NOT_CLOEXEC` ⇒ refuse; **no fork**, no record; lock released |
| grandchild `G-1` hoist violated / `G-3` readback shows a `CLOEXEC` slot | `os._exit(3)`, nothing written or unlinked; PCS sees `boot` EOF ⇒ carried stage-2 route |
| grandchild crash between `G-2` and `G-6` | its reference released by the kernel; PCS and middle still hold theirs; singleton unchanged |
| a `posix_spawn`ed role's `A-5` finds an unexpected descriptor | refusal, now a **verification failure** rather than the mechanism |
| supervisor death | `PEER_EOF` only — **never** `waitpid` |
| watchdog first-ack timeout | close, `REAP_ROLE`, §U6.3; else `WATCHDOG_UNREAPED` ⇒ invalidity. **No signal** |
| `_recvmsg` raises | single-statement `_exit_`; exposure interval named, not eliminated |
| ancillary violation on any item | full vector parsed first, then closed exactly; nothing else touched |
| every unknown control outcome | `T_PROCESS_INVALID` + §4c(c)/§4d, invalidity dominance; never a success, capacity, custody, E1/E2/E3 or Q/C fact |

## Verifier and test delta

**Verifier:** `S-19` replaced (AST-only); `S-20` added (lock created
`O_CLOEXEC` with readback, no `F_SETFD` anywhere); `S-21` added (no file-action
names the lock; exactly one `_dup2(..., 3, inheritable=True)` in the grandchild);
`S-22` added (no signal call site reachable with a watchdog handle or pid).
CHANGES 1, 2, 4, 5 and rules `S-1'`…`S-18` unchanged.

**Tests:** 442R, 443R, 447R, 456R replaced; 487–500 added, covering the lock
readback, the `G-1`…`G-6` sequence, the fork-shared-lock theorem row by row, the
absence of a lock reference in every non-supervisor role, the supervisor's
absence from the PCS child set, `init` reaping the supervisor, the post-`c11`
group-signal precondition, zero watchdog signal paths, the non-aborting parse,
the withdrawal of the no-callback claim, the absence of any proxy, and the
unchanged counts.

## Weakest points against my own repair

1. **F1 moves a load-bearing property from inheritance to an explicit two-step
   handoff.** If an implementer omits `G-3`'s readback, a silently `CLOEXEC`
   slot 3 would close the lock at `execve` and **release the singleton while the
   supervisor lives** — worse than the leak being fixed. `S-21` and row 489 are
   the only guards.
2. **The corrected proof still rests on "every other PCS descriptor is
   `CLOEXEC` by construction".** A future descriptor added without `O_CLOEXEC`
   reintroduces exactly this defect class, and no rule forbids adding one.
3. **F4 makes the composite honestly weaker.** The receive path now carries a
   named exposure with no upper bound the contract controls. A reviewer may
   judge that unacceptable on a capability-carrying channel — in which case the
   answer is a clean proxy receiver, a **new architecture** needing its own
   author cell.
4. **F2 is a wording repair over a real asymmetry**: the one component holding
   all process authority cannot directly prove the death of the component it
   serves.
5. **All four defects were in my own bytes and a single static pass found
   them**, which suggests the composite is at or past the size I can keep
   consistent without independent checking.
6. **`os.dup2`'s `inheritable` parameter and `os.open`'s `O_CLOEXEC` behaviour
   are pinned facts I state rather than verify.** Both are load-bearing and
   cheap for a reviewer to confirm.

## Bounded questions for the independent lines

Both review the **identical bytes** of the binding **as corrected by
v2.1.10.5**, recompute every governing hash, and treat every author closure —
including this one — as untrusted. §P1R.9 carries them verbatim.

**X = Claude Code Opus 4.8.** X-Q1: is the lock repair exact and complete, and
does §P1R.1.5 really preserve the carried fork-shared-lock theorem rather than
contradict it — with `A-5` now a verification rather than the mechanism? X-Q2:
does §P1R.2 make every parent, reaper, wait and signal claim match the actual
tree, and after §P1R.3 is there **any** surviving path on which a signal reaches
a watchdog? X-Q3: is §P1R.4 the right repair — theorem withdrawn, `S-19`
narrowed, exposure named as a capability exposure inside A3 without upgrading
A3, no proxy — and does the non-aborting `B-2` close the unclosed-descriptor
gap? Verify `scm_detach_fds()` independently. Verdict line 1 exactly
`CONFIRM_OFFICINA_SUPERVISOR_P1_V2_1_10_5_X` or
`REVISE_OFFICINA_SUPERVISOR_P1_V2_1_10_5`.

**Y = GPT-5.6 Sol.** Y-Q1: did the repair close F1–F4 everywhere they appeared,
and does F1 introduce the omitted-`G-3` failure mode item 1 names — with `S-21`
plus row 489 a sufficient guard? Y-Q2: are the corrected crash rows, the
grandchild pre-exec sequence and the non-aborting parse total, with every
unknown outcome reaching `T_PROCESS_INVALID` and §4c(c)/§4d? Y-Q3: is §P1R.4 an
honest statement of what the contract can and cannot prove about a contaminated
receiver, is the exposure correctly classified and correctly left inside A3 as
procedural discipline, and do you agree a clean proxy receiver would be a new
architecture outside the signed P1 selection — or is the composite unacceptable
without one? Verdict line 1 exactly
`CONFIRM_OFFICINA_SUPERVISOR_P1_V2_1_10_5_Y` or
`REVISE_OFFICINA_SUPERVISOR_P1_V2_1_10_5`.

Both lines: static review only — run no code, test, probe, or
process/socket/pipe/fork/exec/signal operation; create exactly one review file;
modify nothing; authorize no implementation, activation, entropy, spend, Q/C
work, datum, outcome, Proof, or claim movement.

## Authorization boundary

**`I_ACCEPT_OFFICINA_SUPERVISOR_CONTROL_CHANNEL_AMENDMENT` remains unavailable**
and is not made signable here. It becomes available **only** if **both** the
independent X line and the independent Y line confirm the identical corrected
bytes — the binding `6197d2a4…` as corrected by `798d0cbd…` — together with the
carried chain. **This closure does not self-confirm and asserts no X/Y verdict.**

No implementation, code/test/verifier/manifest edit, commit, host change,
process or probe, T activation, entropy, E1/E2/E3 spend, Q/C work, datum,
outcome, Proof, or claim movement is authorized.

**Confirmed: no code was written, no test or probe was run, and no
process/socket/pipe/fork/exec/signal operation was performed.**

`successor/officina/runtime/` contains only `T_RUNTIME.lock`;
`successor/officina/runtime_control/` does not exist;
`successor/officina/T_ENVELOPE.json` remains `"activated": false`. **T remains
`NOT_ACTIVATED`; the programme claim remains `OPEN`.**
