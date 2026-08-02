# Officina supervisor and control-channel amendment — v2.1.10.5 P1 pre-X/Y repair

Status: `P1_BOUND_REPAIRED_CANDIDATE_FOR_FINAL_XY_CONFIRMATION_NOT_AUTHORIZED`.
Layer prefix: **§P1R**.

> ## WHAT THIS LAYER REPAIRS
>
> Four concrete contradictions in the v2.1.10.4 P1 binding, found by a static
> check before any reviewer time was spent, plus a literal consistency sweep.
> **The P1 author selection is fixed and is not reopened; P3 and P4 are not
> revisited.** This is a bounded correction, not a new architecture and not a
> new author choice.
>
> **F1 — the `SPAWN.lock` leak proof was false.** The binding's PCS-side
> descriptor table has **no `SPAWN.lock` row at all**, so the lock lives on a
> kernel-chosen number outside 3–8. Being non-`CLOEXEC`, it would survive every
> controller, worker and watchdog `execve` **at its original number**, and the
> role's `A-5` check would refuse *after* the leak rather than prevent it.
> §P1R.1 makes the PCS's lock descriptor `O_CLOEXEC` with an `F_GETFD` readback,
> and gives the supervisor its slot-3 copy by an exact grandchild-side
> `dup2(lock_fd, 3, inheritable=True)` immediately before the `execve`. The
> carried fork-shared-lock theorem is **preserved**, and §P1R.1.5 proves it.
>
> **F2 — "the PCS holds every PID" was false.** The binding's own tree makes the
> supervisor grandchild a child of `pid_mid` until `m9` and of `init`
> afterwards. The PCS is **not** the supervisor's parent and cannot
> `waitpid(supervisor_pid)`. §P1R.2 replaces every universal phrase with the
> exact boundary.
>
> **F3 — a watchdog-signalling contradiction.** Replacement-index row 16 said the
> carried first-ack-timeout route becomes a `SIGNAL_ROLE + REAP_ROLE` pair, while
> the operative text and three tests say **no signal reaches a watchdog on any
> path**. §P1R.3 keeps the operative rule and corrects the index row.
>
> **F4 — "no callback before `_exit`" is not mechanically true.** Making
> `_exit_` the first statement of an `except` body proves nothing about what the
> interpreter runs between the C call's failure and that statement. The absolute
> theorem is **withdrawn**; §P1R.4 states what is actually provable and names the
> rest as a transient capability exposure inside the signed A3 procedural
> residual.
>
> **F5 — a parse/cleanup ambiguity.** `B-2`'s inline `⇒ ANCILLARY_VIOLATION`
> read as aborting the parse, while `B-4` requires the **complete** vector to
> have been collected first; an aborting parse would leave installed descriptors
> unclosed. §P1R.5 makes `B-2` non-aborting.
>
> **No new architecture, no proxy process, no confinement mechanism, no new
> author cell, no new import, and no change to the 5 / 6 / 3 / 17 / 9 / 3
> counts.**

**Authorship.** Written by **Claude Code Opus 5 acting only as the specification
author**. This line wrote v2.1 through v2.1.10.4 and **cannot** serve as the
independent X or Y line for its own bytes, exactly as
`reviews/officina_supervisor_v2_1_authorship_note.md` records. **Every author
closure in this chain, including the v2.1.10.4 binding closure, is an untrusted
self-assessment — and three of the four defects repaired here were in my own
bytes.** This layer does not self-confirm.

**Signed cells unchanged.** A3, B1, C1, D1, K1 carried; **P** signed and bound:

```text
P: I_SELECT_SUPERVISOR_PROCESS_AUTHORITY_P1_FULL_PCS_MEDIATION
```

`I_ACCEPT_OFFICINA_SUPERVISOR_CONTROL_CHANNEL_AMENDMENT` remains **not
signable**. Creates nothing executable. Edits no existing file, code, test,
verifier, manifest, signature, prompt, prior review, or runtime artifact. Starts
no process, socket, pipe, fork, exec, or signal. T remains `NOT_ACTIVATED`; the
programme claim remains `OPEN`.

## Governing hashes (recomputed)

```text
6197d2a4073d35fc978119db32128c50d12594343ac87731640a1d8e19f09e84  successor/OFFICINA_GENERIC_HARNESS_SUPERVISOR_CONTROL_CHANNEL_V2_1_10_4_P1_BINDING.md
5889461b86870c357a61e1b7327c1285773c4263dd9640bf3e2da202b9bde302  reviews/opus5_officina_supervisor_control_channel_v2_1_10_4_p1_binding_closure.md
6ef98132990f8c686fa9678509bb07ba8259f3d6e4cbc483861edfc03ea8e3ef  successor/OFFICINA_SUPERVISOR_PROCESS_AUTHORITY_SELECTION_V1_SIGNATURE.md
02d862e76f76a57cd154ecfd8a67f88abb02c2ce324e4026e4145069cee63143  successor/OFFICINA_GENERIC_HARNESS_SUPERVISOR_CONTROL_CHANNEL_V2_1_10_3_CORRECTION.md
d46414389187bb87068e5105a0a914a56f5f49f1244bdb5b527ccea89acba18c  reviews/opus5_officina_supervisor_control_channel_v2_1_10_3_closure.md
c7ff27775fd1b394b850be1be3e1d361d95f5e12af251949f8363980bd2900ec  successor/OFFICINA_GENERIC_HARNESS_SUPERVISOR_CONTROL_CHANNEL_V2_1_10_2_CORRECTION.md
2d4d4b189e460605ce95f8f464d7ef1c6d0c8ce317ad26033a91b4d2c556759b  successor/OFFICINA_GENERIC_HARNESS_SUPERVISOR_CONTROL_CHANNEL_V2_1_10_1_CORRECTION.md
2b4f9cad7be7a69527e828c73928a399209fcd8151780b9b4c839934893e0dc8  successor/OFFICINA_GENERIC_HARNESS_SUPERVISOR_CONTROL_CHANNEL_V2_1_10_CORRECTION.md
1468c9ab1806c1eb25523e6a9fd8567592076f0dc74418ca698a52f933c7f3b0  successor/OFFICINA_GENERIC_HARNESS_SUPERVISOR_CONTROL_CHANNEL_V2_1_9_CORRECTION.md
33b0b91621439bdc42b4c41b3d00741b8c20d014a686097d2bc63c001db0ed50  successor/OFFICINA_GENERIC_HARNESS_SUPERVISOR_CONTROL_CHANNEL_V2_1_8_CORRECTION.md
789732476938ca8c1436eebb49e54a1f994c2c000b7689e1eb9aad082f6871a8  successor/OFFICINA_GENERIC_HARNESS_SUPERVISOR_CONTROL_CHANNEL_V2_1_7_CORRECTION.md
9f1d018e7630d00da954910fa92cacc8005e0ecff90372e513f2fcec8593818b  successor/OFFICINA_GENERIC_HARNESS_SUPERVISOR_CONTROL_CHANNEL_V2_1_CORRECTION.md
ee3171724c89bd7e8f890141f42bf478838608c6f1908f9284218f1e940be635  successor/OFFICINA_GENERIC_HARNESS_SUPERVISOR_CONTROL_CHANNEL_V2_1_1_CORRECTION.md
72bfcc3f088ba538157145aed0bccc95a9ff2e1ad6c41f0579f32c9926274888  successor/OFFICINA_GENERIC_HARNESS_SUPERVISOR_CONTROL_CHANNEL_V2_1_3_CORRECTION.md
c494ef8884948bd0e737373d2d57a3ab74bbd456db2c3463711c4405f2fdf86a  successor/OFFICINA_SUPERVISOR_AUTHOR_SELECTIONS_V1_SIGNATURE.md
4918a208bb94549ba3e7c38571265e723cc51a0a3394e291a62a85c333d864a6  successor/OFFICINA_SUPERVISOR_OUTPUT_CAPACITY_SELECTION_V1_SIGNATURE.md
8c47da352ef5954406964647a32e97939c404806bdf9b3d3ff5bc70866e6369a  successor/OFFICINA_GENERIC_HARNESS_SIGNATURE.md
724d633a55668013b78058eed1c76e12e9bbaf487f71ea94b7a4568ea1ced8a0  successor/OFFICINA_GENERIC_HARNESS_CONTRACT_V2_3_1_CORRECTION.md
b5a1523290b6b8417a7b3288329cc4a4e5ff80214c8f28e6ea1ae51a450a94c9  successor/OFFICINA_BATCH_SETTLEMENT_CORE_AMENDMENT_V1_1_1_CORRECTION.md
ae9c440acaaba90f2cb669e5a8212082f4c0f25b5b7e31ebc906b9cbc0ad6132  reviews/officina_supervisor_v2_1_authorship_note.md
327b1bb222173407772836a2fdc4e92f89595508aff8b77f68f65816cafbec1e  src/philosophia/officina/verification.py
```

---

## §P1R.0. Literal replacement index over v2.1.10.4

**Everything not named carries verbatim from the binding and the whole carried
chain.**

| # | v2.1.10.4 locus, quoted | Action |
|---|---|---|
| 1 | §P1B.3.1's PCS-side descriptor table | **replaced** by §P1R.1.2 — it gains the missing `SPAWN.lock` row, `CLOEXEC` = **yes** |
| 2 | §P1B.3.3's five-step leak proof, in particular step 5's clause "It reaches the **`SUPERVISOR`** role only, at slot 3, where the map places it deliberately" and "if its number were ever outside the destination range, the receiving role's `A-5` … would refuse, so the failure mode is fail-closed rather than silent" | **replaced** by §P1R.1.3–§P1R.1.6. The old proof was **false**: the lock is at a kernel-chosen number outside every destination range, so no `DUP2` closes it and it leaks at its original number |
| 3 | §P1B.3.2's `SUPERVISOR` slot-3 cell "`SPAWN.lock` (retained, non-`CLOEXEC`, carried §W2.2)" | **replaced** by §P1R.1.4 — the descriptor at slot 3 is created non-`CLOEXEC` **by the grandchild's own `dup2`**, not inherited non-`CLOEXEC` from the PCS |
| 4 | §P1B.1 clause 1 "**One clean, constructed Process-Control Server (PCS) holds every PID in the system**" | **replaced** by §P1R.2.1 |
| 5 | §P1B.2's tree comment "sole holder of every PID" | **replaced** by §P1R.2.2 |
| 6 | §P1B.2's direct-parent/reaper table and §P1B.12's authority rows | **extended** by §P1R.2.3 (an explicit supervisor row) |
| 7 | §P1B.0.1 row 16 ("the route becomes a PCS `SIGNAL_ROLE` + `REAP_ROLE` pair") | **replaced** by §P1R.3.1 — **no signal reaches a watchdog on any path** |
| 8 | §P1B.6.3 `B-1`'s clause "an immediate process exit with NO callback, NO finalizer, NO atexit handler, NO buffer flush, and NO unwinding" | **replaced** by §P1R.4.2 — the absolute theorem is **withdrawn** |
| 9 | §P1B.6.5's residual paragraph | **replaced** by §P1R.4.3 |
| 10 | §P1B.11 CHANGE 3 rule `S-19` | **replaced** by §P1R.4.4 — it now asserts only the AST property it can prove |
| 11 | §P1B.6.3 `B-2`'s clause "`(level, type) != (_SOL_SOCKET, _SCM_RIGHTS)` ⇒ `ANCILLARY_VIOLATION`, and the item contributes no descriptor" | **replaced** by §P1R.5.1 — the parse is **non-aborting**; it records flags and always collects the complete vector |
| 12 | §P1B.14 rows **442**, **443**, **447**, **456** | **replaced** by §P1R.7.2 |
| 13 | §P1B.15 weakest points | **extended** by §P1R.8 |
| 14 | §P1B.17 / the binding's review questions | **replaced** by §P1R.9 — the reviewed bytes are now the binding **as corrected by this layer** |

**Not changed by this layer**, and re-asserted: the P1 selection; the nine-opcode
enum with one uniform `SPAWN_WATCHDOG`; five production roots; the 6 / 3 / 17
import counts; `CMSG_SPACE(12)` and the 3-descriptor maximum; the absence of any
global `/proc/self/fd` sweep; §P1B.6.2's `scm_detach_fds()` fact; §P1B.13's four
cell statements; and every carried surface.

---

## §P1R.1. F1 — the `SPAWN.lock` descriptor, repaired exactly

### §P1R.1.1 The defect, stated literally

The binding's §P1B.3.1 table lists six numbered PCS descriptors (3–8: caller
request, caller reply, runtime root, package root, PCS source, interpreter) plus
`sv_sock`, `journal_fd`, per-handle ends, and the objects opened under fd 6.
**`SPAWN.lock` appears in no row.** It is opened by the PCS at `c1` and lives at
a kernel-chosen number, which is neither in 3–8 nor in any role's destination
range. §P1B.3.3's proof therefore fails at its own step 3: **no `DUP2` overwrites
it and no `CLOSE` action names it**, so a non-`CLOEXEC` lock descriptor survives
every controller, worker and watchdog `execve` at its original number. The
role's `A-5` `/proc/self/fd` check would then refuse — **after** the leak, and
on the normal production path, which is not an exact descriptor map and not an
acceptable primary mechanism.

### §P1R.1.2 Corrected PCS-side descriptor table

| Constant / name | # | Contents | `FD_CLOEXEC` | Closed when |
|---|---|---|---|---|
| `T_PCB_FD_REQUEST_R` | 3 | caller request read | **clear** (arrived by `POSIX_SPAWN_DUP2`) | after the `SPAWN_SUPERVISOR` reply is written |
| `T_PCB_FD_REPLY_W` | 4 | caller reply write | **clear** | same |
| `T_PCB_FD_RUNTIME_ROOT` | 5 | runtime root directory | **clear** | PCS exit |
| `T_PCB_FD_PACKAGE_ROOT` | 6 | package root directory | **clear** | PCS exit |
| `T_PCB_FD_SOURCE` | 7 | the PCS's own source object | **clear** | PCS exit |
| `T_PCB_FD_INTERPRETER` | 8 | the interpreter object | **clear** | PCS exit |
| **`lock_fd`** | **kernel-chosen** | **`SPAWN.lock`, held under `flock(LOCK_EX)`** | **SET** (§P1R.1.3) | `c18` / PCS exit, through `CLOSE_OWNED` |
| `sv_sock` | kernel-chosen | supervisor `SOCK_SEQPACKET` PCS end | set | `SHUTDOWN` or PCS exit |
| `journal_fd` | kernel-chosen | the `t-pcs.v1` journal | set | PCS exit |
| per handle | kernel-chosen | the role-side ends the PCS retains | set | when the handle reaches `REAPED` |
| opened under fd 6 | kernel-chosen | role-bootstrap source, `generic_harness.py` source, `src` directory | set | PCS exit |

### §P1R.1.3 The PCS acquires the lock close-on-exec, with a readback

```text
c1 (amended, single route):
  lock_fd := _open("SPAWN.lock",
                   _O_RDWR | _O_CREAT | _O_CLOEXEC, 0o600,
                   dir_fd = T_PCB_FD_RUNTIME_ROOT)
  _flock(lock_fd, _LOCK_EX | _LOCK_NB)   with the carried bounded retry
  READBACK, mandatory:
     require type(_fcntl(lock_fd, _F_GETFD)) is int
     require (_fcntl(lock_fd, _F_GETFD) & _FD_CLOEXEC) != 0
       otherwise ⇒ LOCK_FD_NOT_CLOEXEC ⇒ fail-closed refusal, NO fork, NO
                   record installed, lock released through CLOSE_OWNED
```

`_F_GETFD` and `_FD_CLOEXEC` are integer constants of the already-imported
`fcntl` module, covered by the existing integer row of the carried
per-primitive identity table (v2.1.10.1 §V21101.1.4). **No import changes; the
6 / 3 / 17 counts are unaffected.**

**One route only.** If the readback fails, the attempt **refuses**; there is no
`F_SETFD` repair path, so the mechanism is single-valued.

### §P1R.1.4 The supervisor's slot-3 copy is created by the grandchild

The supervisor is **not** `posix_spawn`ed and therefore has **no
`file_actions`**: it is reached by `c4` fork → `m7` fork → `execve` in the
grandchild. The binding's §P1B.3.3 conflated that path with the `posix_spawn`
role path; they are now separated.

```text
GRANDCHILD PRE-EXEC SEQUENCE, ordered, immediately before the reviewed
supervisor execve (this replaces the "retained, non-CLOEXEC, carried §W2.2"
cell of §P1B.3.2 slot 3):

 G-1. HOIST every descriptor the supervisor must retain — lock_fd, the boot
      write end, the role source, the sv_sock peer, the role-bootstrap source,
      the srcdir, the interpreter, the package root — above 10, by the carried
      generalized hoist (v2.1.10.2 §T6.1). Postcondition: eight pairwise
      distinct numbers, all >= 11. Violation ⇒ GRANDCHILD_FD_HOIST_FAILED
      ⇒ os._exit(3), nothing written, nothing unlinked.
 G-2. for slot s in ascending order 3,4,5,6,7,8,9,10:
          _dup2(h[s], s, inheritable=True)
      Slot 3's source is h[lock_fd]. `inheritable=True` is passed EXPLICITLY,
      never left to a default, and it is what clears FD_CLOEXEC on the
      destination.
 G-3. READBACK, mandatory, for every slot:
          require (_fcntl(s, _F_GETFD) & _FD_CLOEXEC) == 0
        otherwise ⇒ GRANDCHILD_FD_NOT_INHERITABLE ⇒ os._exit(3)
 G-4. close every hoisted source h[s], ascending, EBADF tolerated. In
      particular the ORIGINAL lock_fd copy is closed here, so the grandchild
      holds exactly ONE lock descriptor, at slot 3.
 G-5. the carried §W2.2/§Z3.5 scrub closes every remaining inherited
      descriptor except slots 3–10 and stdio; stdio is redirected to
      os.devnull.
 G-6. _execve of the object-bound interpreter and role-bootstrap source, with
      the SUPERVISOR argv and an exactly empty environment.
```

**Collision-freedom** is the carried proof: every source is `>= 11`, every
destination is `<= 10`, all `DUP2`s precede all `CLOSE`s.

### §P1R.1.5 The carried fork-shared-lock theorem is preserved — proof

The suggested repair does **not** conflict with the carried theorem, and the
following is the trace that shows it.

| Point | Who holds a `SPAWN.lock` reference | `FD_CLOEXEC` | Effect on the `flock` |
|---|---|---|---|
| after `c1` | PCS | **set** | the PCS holds the lock |
| after `c4` fork | PCS + middle child | set in both | `fork` copies the descriptor **and its flag**; `FD_CLOEXEC` is consulted only at `execve`, so the middle's fork-shared reference is live. **The carried §V216.3.1 property — "the middle holds a fork-shared reference, so the `flock` persists until that reference is also closed" — is unchanged** |
| after `m7` fork | PCS + middle + grandchild | set in all three | same |
| grandchild `G-2` | the grandchild now also has slot 3, `CLOEXEC` **clear** | mixed | slot 3 is a second descriptor onto the **same open file description**; the `flock` is a property of that description, not of the descriptor |
| grandchild `G-4` | the grandchild's original copy is closed; slot 3 remains | clear | still one reference from this process |
| grandchild `execve` | **slot 3 survives**; every `CLOEXEC` descriptor is closed | clear | **the supervisor retains the lock reference across its `execve`, exactly as carried §W2.2 requires** |
| middle `m9` `_exit` | the middle's reference is released by the kernel | — | carried |
| PCS `c18` / exit | the PCS's reference is released through `CLOSE_OWNED` | — | carried |
| supervisor `g3` | the supervisor closes slot 3 after its identity is live-verified | — | **the `flock` releases only when every holder has closed** — the carried theorem, intact |
| controller / worker / watchdog `execve` | **none** — the PCS's `lock_fd` is `CLOEXEC` and is closed by their `execve` | — | no role but the supervisor ever holds a reference |

**What changed is only *which descriptor* is non-`CLOEXEC`.** Carried §W2.2's
property — that the grandchild's retained descriptor survives its `execve` — is
preserved and is now produced deliberately by `G-2` rather than inherited by
accident. v2.1.10 §V2110.9 row 24, which already replaced §W2.2's justifying
parenthetical, is further scoped by this section: **the non-`CLOEXEC` state
belongs to the grandchild's slot-3 copy alone, never to the PCS's descriptor.**
**No signed invariant is contradicted, and this layer improvises nothing.**

### §P1R.1.6 Corrected file actions for the three `posix_spawn`ed roles

```text
For CONTROLLER, WORKER and WATCHDOG the PCS builds:
  HOIST(the role's logical sources, target = its slot set)      ⇒ all >= 11
  (DUP2, h[slot], slot) for each slot in ascending order
  (CLOSE, h[slot])      for each, same order
  (CLOSE, d)            for every destination number the role does NOT use
                        — for WATCHDOG exactly {6}; for the others empty
NO file action names lock_fd, and none is needed: lock_fd is CLOEXEC and is
closed by the execve itself.
```

**Corrected claim.** After every `posix_spawn`ed role's `execve`, its descriptor
set is exactly `{0,1,2}` ∪ its slot set, because (i) every PCS descriptor other
than 3–8 — **including `lock_fd`, `sv_sock`, `journal_fd`, every per-handle end,
and every object opened under fd 6** — has `FD_CLOEXEC` set and is closed by the
`execve`; (ii) 3–8 have it clear but all lie inside the destination range and
are therefore overwritten by a `DUP2` or named by an explicit `CLOSE`; and
(iii) hoisted duplicates come from `_dup`, which returns non-inheritable
descriptors, and are additionally closed by explicit actions.

> **`A-5` is a verification, not the mechanism.** The role's `/proc/self/fd`
> check confirms the exact set; it is **not** the route by which correctness is
> achieved, and no production path may rely on a post-`exec` refusal. The
> binding's contrary sentence is deleted (§P1R.0 row 2).

---

## §P1R.2. F2 — the exact authority boundary

### §P1R.2.1 The corrected clause 1

> **Deleted:** "One clean, constructed Process-Control Server (PCS) holds every
> PID in the system and all process-control authority" and "sole holder of every
> PID".
>
> **Replacement.** The PCS **directly owns, directly reaps, and holds numeric
> process authority for exactly `pid_mid`, every controller, every worker, and
> every watchdog.** The **supervisor** receives no PID and exercises no numeric
> process authority of any kind. The PCS is **not** the supervisor's direct
> parent and **cannot** prove its death by `waitpid(supervisor_pid)`: it
> observes the supervisor **only** through the `t-pcs.v1` peer channel, and it
> may reach the supervisor by signal **only** through an already-proved
> `pid_mid` group route — the carried §U2.5 stage-2 discipline, under which
> `killpg(process_group_id)` is permitted only after `c11` has made
> `SPAWNING_GROUP.json` durable with `group_verified: true`, and death of a
> non-child member is proved by `/proc` absence or state `Z`, never by a wait.
> **The supervisor is not added to the PCS's direct-child set.** The caller
> owns and may reap **only** the PCS. The orphaned supervisor is reaped by
> `init`.

### §P1R.2.2 Corrected tree annotation

```text
[1] PCS — direct parent and sole reaper of pid_mid, every controller, every
          worker and every watchdog. Holds the numeric identity of exactly
          those processes. NOT the parent of the supervisor.
```

### §P1R.2.3 Corrected process / authority table

| Process | Direct parent | Direct children | May `wait` on | May signal | Holds numeric PIDs of |
|---|---|---|---|---|---|
| caller | the host | the PCS | **the PCS only** | nothing (forbidden by contract) | the PCS |
| **PCS** | the caller | `pid_mid`, controllers, workers, watchdogs | **exactly those** | exactly those, plus the supervisor's **group** through the carried post-`c11` `killpg` route only | exactly those |
| middle (`pid_mid`) | the PCS | the grandchild until `m9` | nothing (it never waits) | nothing | none it uses |
| **supervisor** | `pid_mid` until `m9`, then **`init`** | **none** | **nothing** — a wildcard wait returns `ECHILD` | **nothing** | **none** — handles only |
| watchdog | the PCS | none | nothing | nothing | none |
| controller / worker | the PCS | per the carried role contracts | unchanged | unchanged | none |

**Death proofs, by target:** `pid_mid`, controllers, workers and watchdogs — the
PCS's own targeted `waitpid` through the carried `WAIT_ONE` classifier, where
only `REAPED_POSITIVE` proves death. **Supervisor** — never by wait; by
`t-pcs.v1` `PEER_EOF` plus, where the carried route requires a death proof,
`/proc` absence or state `Z` under the signed §U2.5 stage-2 rules. `init` reaps
it.

---

## §P1R.3. F3 — one watchdog rule

### §P1R.3.1 The corrected index row

> **Replacement-index row 16, corrected.** Carried v2.1.3 §U2.6's row
> "grandchild first-ack wait expires … kill the watchdog by
> `WATCHDOG_CHILD.json`, prove death, remove records per §U6.3, `os._exit(3)`"
> becomes:
>
> ```text
> the supervisor closes the watchdog update WRITE end through CLOSE_OWNED;
> it then issues REAP_ROLE(watchdog_handle) until REAPED_POSITIVE;
> then it removes records per §U6.3 and os._exit(3);
> if REAPED_POSITIVE is not obtained within T_WATCHDOG_ACK_ABSENCE_TIMEOUT_NS
> after the close, it records WATCHDOG_UNREAPED and routes the generation to
> §P1B.8.4's invalidity path.
> NO SIGNAL OF ANY NUMBER IS SENT TO A WATCHDOG ON THIS OR ANY OTHER PATH.
> ```
>
> The binding's "`SIGNAL_ROLE` + `REAP_ROLE` pair" is **deleted**; it
> contradicted §P1B.4 invariant 4, §P1B.7.5, and tests 440, 455 and 456.

### §P1R.3.2 Whole-composite sweep for a surviving watchdog signal

| Locus | Signals a watchdog? |
|---|---|
| §P1B.4 invariant 4 | no — `SIGNAL_ROLE`/`SIGNAL_GROUP` refused for `role == WATCHDOG` |
| §P1B.5.2 opcode table | no — the refusal is a precondition of both signal opcodes |
| §P1B.7.4 replacement route | no — `SIGNAL_GROUP` there targets **controller/worker groups**, never the watchdog |
| §P1B.7.5 termination | no — update-EOF only |
| §P1B.8.3 wedged-watchdog row | no — `WATCHDOG_UNREAPED`, explicitly "no signal" |
| §P1B.9 `S-3`…`S-5` shutdown | no — close, then `REAP_ROLE` |
| §P1B.0.1 row 16 | **yes, before this repair** — corrected by §P1R.3.1 |
| carried §W3.3 freeze | no — it signals controller/worker groups |

**After §P1R.3.1 the composite contains no path on which any signal reaches a
watchdog.**

---

## §P1R.4. F4 — the withdrawn no-callback theorem

### §P1R.4.1 Why the claim was false

The receiver is the **contaminated supervisor**. Between the kernel's
`recvmsg` returning an error and the first statement of the contract's `except`
body, CPython constructs the exception and its traceback, may unwind frames,
may run `__del__` on objects released by that unwinding, checks for pending
signals at bytecode boundaries, and — if the host installed one — invokes a
`sys.settrace` function's `exception` event, a profile function, or an audit
hook. **None of that is under this contract's control, and the binding itself
places this process inside the signed A3 procedural residual.** Asserting "NO
callback, NO finalizer, NO unwinding" was therefore an unprovable absolute, and
it is withdrawn.

### §P1R.4.2 What is actually specified

```text
B-1 (amended). r := _recvmsg(sock, T_CONTROL_FRAME_MAX_BYTES,
                             _CMSG_SPACE(12), _MSG_CMSG_CLOEXEC)

  IF B-1 RAISES ANY BaseException, the contract-authored handler body is
  EXACTLY ONE STATEMENT:

        _exit_(T_PCS_EXIT_RECV_UNENUMERABLE)

  PROVABLE PROPERTIES, and only these:
    (a) the handler is a single `except BaseException:` clause whose body is
        that one call, with no other statement, no other call, no attribute
        access, no name binding, no `else`, and no `finally`;
    (b) the contract authorises NO cleanup, callback, unwind, flush, close, or
        logging logic in that handler;
    (c) `_exit_` is `os._exit`, bound and identity-checked at module scope, so
        it terminates the process without running interpreter exit handlers
        that the CONTRACT installed — the contract installs none.

  NOT CLAIMED, and explicitly withdrawn:
    that no Python trace, profile, or audit hook, no signal handler, no
    finalizer, no exception-machinery step, and no other same-process callback
    can execute between the C call's failure and (a)'s statement. In a
    contaminated interpreter the contract cannot establish that, and it does
    not assert it.
```

### §P1R.4.3 The named exposure, and its A3 boundary

> **Transient capability exposure.** From the instant the kernel may have
> installed descriptors inside `_recvmsg` until the process actually exits,
> those descriptors are present in this process's table. During that interval
> **same-process hooks, finalizers, or threads that the host installed may run**
> and may reach them. The interval is bounded by the path from the raise to the
> `_exit_` call and is terminated with certainty by the kernel's closure of the
> descriptor table at process exit — but its length is **not** under this
> contract's control.
>
> **This is a capability exposure, not a resource fact.**
>
> **A3 boundary, stated without upgrade.** That interval lies inside the signed
> **A3 same-UID procedural rescope**. The contract offers **procedural
> discipline, not adversarial same-process security**: it does not confine a
> hostile in-process actor, asserts no same-UID confinement mechanism, and
> invents none here. The exposure is **permanently non-citable**, forbidden from
> selection, Q, C, C1–C6, any blinding claim, and any scientific or resource
> interpretation, and it is **never Q/C evidence**.
>
> **No proxy process is introduced.** Moving `recvmsg` into a clean proxy would
> be a new architecture that the signed P1 selection does not authorize; this
> layer therefore repairs the *claim* and leaves the *architecture* alone, which
> is the disposition the repair scope requires.

### §P1R.4.4 `S-19`, corrected to an AST-provable property

```text
S-19 (replacing the binding's): in the receive path, the `except BaseException`
     handler guarding the `_recvmsg` call has a body consisting of EXACTLY ONE
     `ast.Expr` node whose value is a `Call` to the bound name `_exit_` with one
     argument, the constant `T_PCS_EXIT_RECV_UNENUMERABLE`; the handler has no
     other statement, no `else`, and no `finally`.
     ⇒ "unenumerable-receive handler is not a single _exit_ call"
S-19 asserts an AST property of the reviewed source and NOTHING about
interpreter behaviour before the handler runs.
```

### §P1R.4.5 The kernel fact keeps its status

§P1B.6.2's `scm_detach_fds()` statement — Linux installs `min(space, queued)`
descriptors, reports **exactly** those in the returned control data, and
releases the rest — remains **reviewer-verifiable, not author-proven**. Both
lines are asked to check it against the kernel source (§P1R.9). This layer
neither strengthens nor weakens it.

---

## §P1R.5. F5 — the parse fix and the literal sweep

### §P1R.5.1 `B-2` is non-aborting

> **The defect.** `B-2`'s inline "`(level, type) != (_SOL_SOCKET, _SCM_RIGHTS)`
> ⇒ `ANCILLARY_VIOLATION`" read as a verdict that ends the parse, while `B-4`
> requires the **complete** vector to have been collected before it closes
> anything. An aborting parse would leave installed descriptors from later
> control items unclosed — the exact harm `B-4` exists to prevent.

```text
B-2 (amended, NON-ABORTING). violation_flags := empty set
    for EVERY returned control item, in order, without early exit:
        if (level, type) != (_SOL_SOCKET, _SCM_RIGHTS):
            violation_flags += {ANCILLARY_UNEXPECTED_ITEM}
            # the item carries no SCM_RIGHTS payload, so it contributes no
            # descriptor; the loop CONTINUES
        else:
            if len(cdata) % 4 != 0:  violation_flags += {ANCILLARY_RAGGED}
            if len(cdata) > 12:      violation_flags += {ANCILLARY_OVERLONG}
            n := len(cdata) - (len(cdata) % 4)
            received += [ int.from_bytes(cdata[i:i+4], "little")
                          for i in range(0, n, 4) ]
    `received` is now the COMPLETE parsed vector and, by §P1B.6.2, exactly the
    set the kernel installed for this message.

B-3 (unchanged in substance): flag MSG_CTRUNC, MSG_TRUNC, a wrong count, and a
    wrong fstat type into violation_flags. It also does not abort.

B-4 (unchanged): if violation_flags is non-empty, close EXACTLY the descriptors
    in `received`, de-duplicated by numeric value, ascending, once each, with
    _close, tolerating EBADF; close NOTHING ELSE; never enumerate
    /proc/self/fd; never touch another message's or a live handle's
    descriptors; then route to §P1B.8.4.
```

**There is now exactly one place that decides and one place that acts.**

### §P1R.5.2 Literal sweep result

| Sweep item | Result after this layer |
|---|---|
| exact P1-only option tokens | one token, `…_P1_FULL_PCS_MEDIATION`; P2/P3/P4 appear only in §P1B.0.2's provenance table; test row 437 matches option **tokens and phrases**, never bare letters, and exempts §U6.1's `P0`–`P3` preflight names |
| exact parent/reaper claims | corrected by §P1R.2; no universal "every PID" survives |
| exact lock `CLOEXEC` state at each process and exec boundary | tabulated in §P1R.1.5; PCS **set**, grandchild slot 3 **clear**, every other role **absent** |
| watchdog signal paths | **zero**, after §P1R.3.1; swept in §P1R.3.2 |
| nine uniform operations and their descriptor vectors | unchanged: 9 opcodes, `SPAWN_ROLE` 3 fds, `SPAWN_WATCHDOG` 2, all others 0, max 3, `CMSG_SPACE(12)` |
| five roots and 6 / 3 / 17 import counts | unchanged; this layer adds **no** import and **no** root |
| global `/proc/self/fd` remediation sweep | absent; `S-18` forbids it |
| absolute no-callback claim in the contaminated receiver | **withdrawn** (§P1R.4.2); `S-19` narrowed |
| exact test-row and replacement-index references | rows 442, 443, 447, 456 replaced (§P1R.7.2); index rows 1–14 above |

---

## §P1R.6. Crash-table deltas

Every carried §P1B.8.3 row stands except:

| Cut | Corrected continuation |
|---|---|
| `c1` lock readback shows `FD_CLOEXEC` clear | `LOCK_FD_NOT_CLOEXEC` ⇒ fail-closed refusal; **no fork**, no record installed; the lock is released through `CLOSE_OWNED` |
| grandchild `G-1` hoist postcondition violated | `GRANDCHILD_FD_HOIST_FAILED` ⇒ `os._exit(3)`, nothing written, nothing unlinked; the PCS's `c13` read observes `boot` EOF ⇒ the carried §U2.5 stage-2 route |
| grandchild `G-3` readback shows a slot still `CLOEXEC` | `GRANDCHILD_FD_NOT_INHERITABLE` ⇒ identical |
| grandchild crash between `G-2` and `G-6` | the lock reference is released by the kernel at exit; the middle and the PCS still hold theirs, so the singleton is unchanged; the carried stage-2 route governs |
| a `posix_spawn`ed role's `A-5` finds an unexpected descriptor | still a refusal, but it is now a **verification failure**, not the normal mechanism; the mechanism is §P1R.1.6 |
| supervisor death | unchanged; the PCS learns of it by `PEER_EOF`, **never** by `waitpid` (§P1R.2.1) |
| watchdog first-ack timeout | close the update write end, `REAP_ROLE`, then §U6.3 removal; on failure `WATCHDOG_UNREAPED` ⇒ invalidity. **No signal** (§P1R.3.1) |
| `_recvmsg` raises | the single-statement `_exit_` handler; the exposure interval is named, not eliminated (§P1R.4.2–§P1R.4.3) |
| an ancillary violation on any item | the full vector is parsed first, then closed exactly (§P1R.5.1) |

---

## §P1R.7. Verifier and test delta

### §P1R.7.1 Verifier

```text
CHANGE 3, rule S-19  — replaced by §P1R.4.4 (AST-only property)
CHANGE 3, rule S-20  (new) the PCS's SPAWN.lock open passes _O_CLOEXEC and is
                     followed by an _fcntl(_F_GETFD) readback whose failure
                     branch refuses; no _F_SETFD call exists anywhere
                     ⇒ "lock fd not created close-on-exec"
CHANGE 3, rule S-21  (new) no `file_actions` literal in the PCS names the lock
                     descriptor; the grandchild's pre-exec sequence contains
                     exactly one `_dup2(..., 3, inheritable=True)` whose source
                     is the hoisted lock descriptor
                     ⇒ "lock fd handoff differs"
CHANGE 3, rule S-22  (new) no `SIGNAL_ROLE`, `SIGNAL_GROUP`, `_kill` or
                     `_killpg` call site is reachable with a watchdog handle or
                     a watchdog pid ⇒ "watchdog signal path present"
Everything else in §P1B.11 — CHANGES 1, 2, 4, 5, rules S-1'…S-18 — is unchanged.
```

### §P1R.7.2 Tests

Replaced:

- **442R** — after every `posix_spawn`ed role's `execve`, `/proc/self/fd` is
  exactly `{0,1,2}` ∪ its slot set; assert **by construction**, with `A-5`
  recorded as a verification and not the mechanism; assert **no descriptor
  whose `(st_dev, st_ino)` equals `SPAWN.lock`'s exists in any controller,
  worker or watchdog**.
- **443R** — the `WATCHDOG` file actions contain the explicit `(CLOSE, 6)`;
  and **no** file-action vector for any role names the lock descriptor.
- **447R** — the `_recvmsg` exception handler body is exactly one `_exit_` call
  (`S-19`); assert **only** that AST property, and assert that **no test and no
  contract sentence claims that no callback can run before it**.
- **456R** — the watchdog first-ack-timeout route is close-then-`REAP_ROLE`
  with no signal; assert the corrected index row 16 matches the operative text.

Added:

| # | Test |
|---|---|
| 487 | the PCS's lock descriptor is created with `_O_CLOEXEC` and the `_F_GETFD` readback holds; a fixture clearing the flag makes `c1` refuse with `LOCK_FD_NOT_CLOEXEC` and **no fork** |
| 488 | `S-20`/`S-21`/`S-22` each reject a bit-exact negative fixture and accept a positive one |
| 489 | the grandchild `G-1`…`G-6` sequence: eight hoisted sources `>= 11`, ascending `DUP2`s, the `G-3` readback proving `FD_CLOEXEC` clear on every slot, the original lock copy closed at `G-4` |
| 490 | **the fork-shared-lock theorem**: the `flock` persists while the middle lives, survives the grandchild's `execve` on slot 3, and releases only when the PCS, the middle and the supervisor have all closed — the §P1R.1.5 table, row by row |
| 491 | no controller, worker or watchdog holds a `SPAWN.lock` reference at any instant after its `execve` |
| 492 | the supervisor is **not** in the PCS's direct-child set; a `waitpid(supervisor_pid)` in the PCS is absent from the source and would return `ECHILD`; the PCS learns of supervisor death only by `PEER_EOF` |
| 493 | `init` reaps the orphaned supervisor; the caller reaps only the PCS |
| 494 | the PCS may signal the supervisor's **group** only after `c11` has made `SPAWNING_GROUP.json` durable with `group_verified: true`, and never before |
| 495 | **zero watchdog signal paths** across the whole composite, by the §P1R.3.2 sweep |
| 496 | `B-2` is non-aborting: a message whose **first** control item is not `SCM_RIGHTS` and whose **second** carries descriptors still yields the complete vector, and `B-4` closes every one of them |
| 497 | no operative sentence asserts that no callback, finalizer, or unwinding can occur before the `_exit_`; the exposure is described as a **capability exposure**, never as a resource fact |
| 498 | no proxy process, confinement mechanism, or capability-recovery protocol appears anywhere |
| 499 | the counts are unchanged: 5 roots, 6/3/17 imports, 9 opcodes, max 3 fds, `CMSG_SPACE(12)` |
| 500 | whole-composite no-regression diff over every surface the binding carried |

---

## §P1R.8. Weakest points of this repair

1. **F1's repair moves a load-bearing property from inheritance to an explicit
   two-step handoff.** `G-2`'s `inheritable=True` and `G-3`'s readback are now
   what keeps the supervisor's lock reference alive across its `execve`. If an
   implementer omits `G-3`, a silently `CLOEXEC` slot 3 would close the lock at
   `execve` and the singleton would be released while the supervisor lives —
   a **worse** failure than the leak this repair fixes. `S-21` and row 489 are
   the only guards.
2. **The corrected leak proof still rests on "every other PCS descriptor is
   `CLOEXEC` by construction".** I enumerated the creators (`_open` with
   `_O_CLOEXEC`, `_pipe2(_O_CLOEXEC)`, `_socketpair`, `_dup`), but a future
   descriptor added to the PCS without `O_CLOEXEC` would reintroduce exactly
   this class of defect, and no rule forbids adding one.
3. **F4 makes the composite honestly weaker.** The receive path now carries a
   named exposure with no upper bound the contract controls. That is truthful,
   but a reviewer may judge that an unbounded in-process exposure on a
   capability-carrying channel is not acceptable at all — in which case the
   answer is a clean proxy receiver, which is a **new architecture** and would
   need its own author cell.
4. **F2 is a wording repair over a real asymmetry.** The PCS cannot prove the
   supervisor's death by wait, so supervisor-death detection rests on channel
   EOF and, where a death proof is required, on `/proc`. That is the carried
   design, but it means the one component that holds all process authority
   cannot directly prove the death of the component it serves.
5. **Three of the four defects were in my own bytes**, and the fourth
   (`B-2`/`B-4`) was too. A static check found them in one pass, which suggests
   the composite's size is at or past the limit of what I can keep consistent
   without independent checking.
6. **`os.dup2`'s `inheritable` parameter and `os.open`'s `O_CLOEXEC` behaviour
   are pinned platform/interpreter facts** that I state rather than verify.
   Both are cheap for a reviewer to confirm and both are load-bearing.

---

## §P1R.9. The bounded review questions

Both lines review the **identical bytes** of the v2.1.10.4 binding **as
corrected by this layer**, together with the carried chain. Both must recompute
every governing hash and treat every author closure in this chain — including
this one — as untrusted.

### For the X line (Claude Code Opus 4.8, clean context)

> **X-Q1 — the lock.** Is §P1R.1 exact and complete? Attack: that the PCS's
> `SPAWN.lock` descriptor is `O_CLOEXEC` with a mandatory `F_GETFD` readback and
> a single refuse-on-failure route; that `G-1`…`G-6` give the supervisor exactly
> one non-`CLOEXEC` lock descriptor at slot 3 and close the original; that no
> controller, worker or watchdog can hold a lock reference after its `execve`;
> and that §P1R.1.5's table really preserves the carried fork-shared-lock
> theorem rather than contradicting it. Is `A-5` now genuinely a verification
> rather than the mechanism?
> **X-Q2 — authority and the watchdog.** Does §P1R.2 make every parent, reaper,
> wait and signal claim match the actual tree — the supervisor a child of
> `pid_mid` then `init`, the PCS observing it only through the channel and
> reaching it only through the post-`c11` group route? And after §P1R.3, is
> there **any** surviving path on which a signal reaches a watchdog?
> **X-Q3 — the receive path.** Is §P1R.4 the right repair: the absolute
> no-callback theorem withdrawn, `S-19` narrowed to an AST-provable property,
> the exposure named as a **capability** exposure inside A3 without upgrading
> A3, and no proxy introduced? And does §P1R.5.1's non-aborting `B-2` close the
> gap where an early exit would have left installed descriptors unclosed?
> Verify §P1B.6.2's `scm_detach_fds()` claim independently.
>
> Verdict line 1 exactly `CONFIRM_OFFICINA_SUPERVISOR_P1_V2_1_10_5_X` or
> `REVISE_OFFICINA_SUPERVISOR_P1_V2_1_10_5`. Static review only: run no code,
> test, probe, or process/socket/pipe/fork/exec/signal operation; create exactly
> one review file; modify nothing; authorize no implementation, activation,
> entropy, spend, Q/C work, datum, outcome, or claim movement.

### For the Y line (GPT-5.6 Sol, clean context)

> **Y-Q1 — did the repair close the four defects without opening others?** Take
> each of F1–F4 and check the corrected text against every place the old claim
> appeared, including the crash table, the verifier rules and the test rows. In
> particular: does the F1 repair introduce the failure mode §P1R.8 item 1 names
> — an omitted `G-3` silently closing the lock at `execve` and releasing the
> singleton while the supervisor lives — and is `S-21` plus row 489 a sufficient
> guard?
> **Y-Q2 — totality after the repair.** Are the corrected crash rows, the
> grandchild pre-exec sequence, and the non-aborting parse total, with one
> continuation each and no unknown outcome reaching a success, capacity,
> custody, E1/E2/E3 or Q/C fact rather than `T_PROCESS_INVALID` and the
> §4c(c)/§4d unknowable route?
> **Y-Q3 — honesty of the withdrawal.** Is §P1R.4 an honest statement of what
> the contract can and cannot prove about a contaminated receiver, or does it
> still overclaim anywhere? Is the exposure correctly classified as a
> **capability** exposure and correctly left inside A3 as procedural discipline
> rather than security? And do you agree that a clean proxy receiver would be a
> new architecture outside the signed P1 selection — or do you judge that the
> composite cannot be accepted without one?
>
> Verdict line 1 exactly `CONFIRM_OFFICINA_SUPERVISOR_P1_V2_1_10_5_Y` or
> `REVISE_OFFICINA_SUPERVISOR_P1_V2_1_10_5`. Static review only: run no code,
> test, probe, or process/socket/pipe/fork/exec/signal operation; create exactly
> one review file; modify nothing; authorize no implementation, activation,
> entropy, spend, Q/C work, datum, outcome, or claim movement.

---

`I_ACCEPT_OFFICINA_SUPERVISOR_CONTROL_CHANNEL_AMENDMENT` remains **not
signable** and is not made signable here. It becomes available **only** if both
independent lines confirm the identical corrected bytes. This layer authorizes
no implementation, no code, test, verifier or manifest edit, no commit, no host
change, no process or probe, no T activation, no entropy, no E1/E2/E3 spend, no
Q/C work, no datum, no outcome, no Proof, and no claim movement.
`successor/officina/runtime/` contains only `T_RUNTIME.lock`;
`successor/officina/runtime_control/` does not exist;
`successor/officina/T_ENVELOPE.json` remains `"activated": false`. **T remains
`NOT_ACTIVATED`; the programme claim remains `OPEN`.**
