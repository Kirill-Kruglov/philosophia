# Officina supervisor and control-channel amendment — v2.1.10.3 Cell P completion

Status: **author-cell completion only.** This layer does **not** request
independent X/Y review, does **not** select an option, and authorizes nothing.

Layer prefix: **§V21103**.

> ## RESULT, STATED FIRST
>
> **P4 is a real architecture. It is implementable, and it dominates P2 on
> every property P2 claimed to preserve.** Cell P is therefore repaired: **P2 is
> withdrawn** and the surviving option set is **P1, P3, P4**.
>
> P4 works because the isolated `SUPERVISOR` role bootstrap has, before it
> imports any project code, exactly the primitives it needs — `os.pipe2`,
> `os.posix_spawn`, `os.waitpid` — and because **importing a module does not
> change the process**: the process that creates the watchdog is the same
> process that later becomes the supervisor, so it remains the watchdog's parent
> for the whole generation. Both signed C1 detectors survive, and the watchdog
> additionally gains a fresh isolated address space by construction.
>
> **The trace also refuted four things v2.1.10.2 asserted**, and each is
> corrected here rather than carried:
>
> 1. the role bootstrap's import set `{os, sys}` is **insufficient** — step
>    `A-6` performs the `F_GETFL` test, so `fcntl` is required (§R4.5);
> 2. every descriptor the role bootstrap received arrived through
>    `POSIX_SPAWN_DUP2`, which **clears close-on-exec**, so **all of them leak
>    into a spawned watchdog** unless explicitly closed — including
>    `SPAWN.lock`, which would give the watchdog a fork-shared singleton
>    reference (§R1.5);
> 3. §T1.6's "sweep `/proc/self/fd` and close every descriptor outside the
>    pinned set" would **close legitimate previously-received controller
>    authority descriptors**; it is replaced by a bounded exact rule (§R4.1);
> 4. under P4 the supervisor holds `waitpid` **and** `kill` authority over the
>    watchdog after it is contaminated; kill-by-PID is therefore withdrawn
>    post-import and replaced by EOF-driven termination (§R1.7).
>
> **P4 does not erase the B1 and D1 changes.** The PCS remains mandatory and
> unrecoverable for controller/worker authority; `t-pcs.v1` remains a second
> durable control-plane journal; fd-bearing replies remain non-redeliverable as
> capabilities; `_socket`/`SCM_RIGHTS`, five roots and Linux-specific capability
> transfer remain; and the supervisor retains a **narrow, signed, one-child PID
> trust surface** over the watchdog. §R3 states all of it without discount.

**Authorship.** Written by **Claude Code Opus 5 acting only as the specification
author**. This line wrote v2.1 through v2.1.10.2 and **cannot** serve as the
independent X or Y line for its own bytes, exactly as
`reviews/officina_supervisor_v2_1_authorship_note.md` records. **Every prior
author closure in this chain, including v2.1.10.2's, is treated here as an
untrusted self-assessment**; §R4 re-audits four of its claims and refutes one.

**Signed cells preserved.** A3, B1, C1, D1, K1 are carried verbatim and are not
reopened by this layer's engineering. **Cell P is the only new author choice**,
it is presented and not decided, and no option in it decides a scientific or
resource value.

```text
A: I_SELECT_SUPERVISOR_CONFINEMENT_A3_SAME_UID_PROCEDURAL_RESCOPE
B: I_SELECT_SUPERVISOR_IDEMPOTENCY_B1_DURABLE_JOURNAL_ACK_REDELIVERY
C: I_SELECT_SUPERVISOR_WATCHDOG_C1_DEDICATED_FREEZER
D: I_SELECT_SUPERVISOR_LIFETIME_D1_NO_IDLE_EXIT
K: I_SELECT_SUPERVISOR_OUTPUT_CAPACITY_K1_SUPERVISOR_MEDIATED_TRANSPORT_FIXED_CEILING
```

Creates nothing executable. Edits no existing file, code, test, verifier,
manifest, signature, prompt, or runtime artifact. Starts no process, socket,
fork, or signal. Creates no entropy, activation, capability, world, learner,
candidate, datum, Q/C object, capacity artifact, custody disposition, result
manifest, or outcome. T remains `NOT_ACTIVATED`; the programme claim remains
`OPEN`.

## Governing hashes (recomputed for this correction)

```text
2b4f9cad7be7a69527e828c73928a399209fcd8151780b9b4c839934893e0dc8  successor/OFFICINA_GENERIC_HARNESS_SUPERVISOR_CONTROL_CHANNEL_V2_1_10_CORRECTION.md
2d4d4b189e460605ce95f8f464d7ef1c6d0c8ce317ad26033a91b4d2c556759b  successor/OFFICINA_GENERIC_HARNESS_SUPERVISOR_CONTROL_CHANNEL_V2_1_10_1_CORRECTION.md
c7ff27775fd1b394b850be1be3e1d361d95f5e12af251949f8363980bd2900ec  successor/OFFICINA_GENERIC_HARNESS_SUPERVISOR_CONTROL_CHANNEL_V2_1_10_2_CORRECTION.md
0016452d3033146976b9dc779455f448c9fd690302ff4879d0d2b949e0fd429a  reviews/opus5_officina_supervisor_control_channel_v2_1_10_2_closure.md
f7a866f9100cae1abf80623cd6a7d689cbdca1001fb33dffe98966a727582008  reviews/opus5_officina_supervisor_control_channel_v2_1_10_1_closure.md
4cc19fc914f5908f069cb7b8aa09297dece424943f8a876974105e575d09c47d  reviews/opus5_officina_supervisor_control_channel_v2_1_10_closure.md
ae9c440acaaba90f2cb669e5a8212082f4c0f25b5b7e31ebc906b9cbc0ad6132  reviews/officina_supervisor_v2_1_authorship_note.md
1468c9ab1806c1eb25523e6a9fd8567592076f0dc74418ca698a52f933c7f3b0  successor/OFFICINA_GENERIC_HARNESS_SUPERVISOR_CONTROL_CHANNEL_V2_1_9_CORRECTION.md
f49dcbf9900c0d3fe2e45abbc28193d8b4b4c20c8640dfab508aff15dcc90984  reviews/opus_officina_supervisor_control_channel_v2_1_9_final_confirmation.md
1970986325c75e8f4c2dd72e57e0640ae88b165f3556920e85cae7efc8cc93be  reviews/sol_officina_supervisor_control_channel_v2_1_9_final_confirmation.md
33b0b91621439bdc42b4c41b3d00741b8c20d014a686097d2bc63c001db0ed50  successor/OFFICINA_GENERIC_HARNESS_SUPERVISOR_CONTROL_CHANNEL_V2_1_8_CORRECTION.md
9f1d018e7630d00da954910fa92cacc8005e0ecff90372e513f2fcec8593818b  successor/OFFICINA_GENERIC_HARNESS_SUPERVISOR_CONTROL_CHANNEL_V2_1_CORRECTION.md
ee3171724c89bd7e8f890141f42bf478838608c6f1908f9284218f1e940be635  successor/OFFICINA_GENERIC_HARNESS_SUPERVISOR_CONTROL_CHANNEL_V2_1_1_CORRECTION.md
72bfcc3f088ba538157145aed0bccc95a9ff2e1ad6c41f0579f32c9926274888  successor/OFFICINA_GENERIC_HARNESS_SUPERVISOR_CONTROL_CHANNEL_V2_1_3_CORRECTION.md
c494ef8884948bd0e737373d2d57a3ab74bbd456db2c3463711c4405f2fdf86a  successor/OFFICINA_SUPERVISOR_AUTHOR_SELECTIONS_V1_SIGNATURE.md
4918a208bb94549ba3e7c38571265e723cc51a0a3394e291a62a85c333d864a6  successor/OFFICINA_SUPERVISOR_OUTPUT_CAPACITY_SELECTION_V1_SIGNATURE.md
8c47da352ef5954406964647a32e97939c404806bdf9b3d3ff5bc70866e6369a  successor/OFFICINA_GENERIC_HARNESS_SIGNATURE.md
724d633a55668013b78058eed1c76e12e9bbaf487f71ea94b7a4568ea1ced8a0  successor/OFFICINA_GENERIC_HARNESS_CONTRACT_V2_3_1_CORRECTION.md
b5a1523290b6b8417a7b3288329cc4a4e5ff80214c8f28e6ea1ae51a450a94c9  successor/OFFICINA_BATCH_SETTLEMENT_CORE_AMENDMENT_V1_1_1_CORRECTION.md
327b1bb222173407772836a2fdc4e92f89595508aff8b77f68f65816cafbec1e  src/philosophia/officina/verification.py
```

`verification.py` unamended; `scripts/officina_process_control_bootstrap.py` and
`scripts/officina_role_bootstrap.py` do not exist. This layer creates none of
them.

---

## V21103.0. Literal replacement index over v2.1.10.2

**Everything not named carries verbatim**, including v2.1.10.2 §T1 (except
§T1.6 step 2), §T2 (except the one operation row named), §T3.2–§T3.4, §T4.1's
tree shape, §T5.1–§T5.4 (except the role-bootstrap set), §T6, §T9's platform
pin, and the whole carried v2.1.10 / v2.1.10.1 / v2.1.9 / … chain.

| # | v2.1.10.2 (or carried) locus, quoted | Action in v2.1.10.3 |
|---|---|---|
| 1 | §T7.5's cell-P option block, option **P2** `…_P2_PCS_WITH_SUPERVISOR_PARENTED_WATCHDOG` in full | **withdrawn** — strictly dominated by P4 (§R5.2) |
| 2 | §T7.5's option block generally | **replaced** by §R5.3's three-option block `{P1, P3, P4}` with exact tokens |
| 3 | §T2.3's operation row `SPAWN_WATCHDOG` ("— \| no live watchdog handle in this generation \| `handle_id` \| **2**") | **replaced** by §R2.1 — under P4 the operation survives **only** as `SPAWN_REPLACEMENT_WATCHDOG`, reachable only after the first watchdog's death is proved, with the degraded-detector consequence stated. Under P1 it is unchanged; under P3 it does not exist |
| 4 | §T1.4's descriptor-vector row `SPAWN_WATCHDOG ok \| 2` | **replaced** by §R2.2 (same vector, new opcode name and precondition) |
| 5 | §T4.1's tree branch "`├─ posix_spawn(setsid=True) ─▶ [4] role bootstrap (WATCHDOG)`" | **replaced** by §R1.9 — under P4 the watchdog is a child of the **supervisor role bootstrap**, not of the PCS |
| 6 | §T4.2's PCS-side "per handle" row and §T4.3's handle record, insofar as they cover a watchdog handle | **replaced** by §R2.3 |
| 7 | §T4.5's primitive→operation row "`os.fork` of the watchdog (§W2.1) \| `SPAWN_WATCHDOG` \| C1's registration and ack" | **replaced** by §R2.4 — under P4 the consumer is the supervisor bootstrap's own `posix_spawn`, and the PCS has no watchdog primitive on the first-construction path |
| 8 | §T1.6's remediation step 2 "additionally, scan `/proc/self/fd` and close every descriptor outside this process's pinned set" | **deleted as unsafe**, replaced by §R4.1's bounded exact received-fd cleanup rule |
| 9 | §T3.2's "imports : exactly `os` and `sys`. Nothing else." and §T5.1's "The role bootstrap root imports exactly two: `{os, sys}`" | **replaced** by §R4.5 — `{os, sys, fcntl}`, because `A-6` performs the `F_GETFL` test |
| 10 | §T5.4's `MODULE_SCOPED_ABSOLUTE_IMPORTS` entry `role_bootstrap → {os, sys}` and rule `S-1'`'s "the role root exactly two" | **replaced** by §R4.5 (three imports) |
| 11 | §T3.3's refusal order `A-1`…`A-13` | **extended** by §R1.2's steps `A-8a`…`A-8h`, inserted between `A-8` and `A-9`, executed **only** for `argv[7] == SUPERVISOR` |
| 12 | §T7.2's statement of the C1 loss | **retained as the analysis of P1**, and **scoped**: it describes P1 only. Under P4 neither detector is lost on the first watchdog (§R1.7) |
| 13 | §T7.3's cell table row for **C1** | **replaced** by §R3.5 — the C1 change is an attribute of P1, not of the PCS as such |
| 14 | carried v2.1.3 §U2.6 row "grandchild first-ack wait expires \| … \| kill the watchdog by `WATCHDOG_CHILD.json`, prove death, remove records per §U6.3, `os._exit(3)`" | **retained verbatim under P4**, because at that instant the process is still the clean pre-import bootstrap (§R1.7); it is **not** available post-import |
| 15 | carried v2.1 §W3.5 row "Ack absent past `T_WATCHDOG_ACK_ABSENCE_TIMEOUT_NS` \| … \| **forks a new watchdog**, awaits its ack, …" | **replaced under P4** by §R2.1 — a **replacement** watchdog is obtained from the PCS, not forked by the contaminated supervisor; the pre-import case keeps the carried clean route |
| 16 | §T8's test rows referencing `SPAWN_WATCHDOG` (354, 356, 362, 381) and row 374's two-import assertion | **replaced** by §R6's rows 405–436 |
| 17 | §T9's weakest-point list | **extended** by §V21103.7 |
| 18 | v2.1.10.2's closure verdict `BLOCKED_OFFICINA_SUPERVISOR_V2_1_10_2_AUTHOR_CELL` | **discharged** by this layer: the cell is now complete enough for an informed selection. The block on *acceptance* remains until an option is selected **and** the composite passes fresh X/Y review |

---

## R1. Is P4 a real architecture? — the literal trace

**Conclusion: yes.** The trace below is mechanical, single-valued, and ends at
normal shutdown. Every step names the primitive, the process, and the parent
relation.

### R1.1 The exact step before the first project import

The insertion point is **between `A-8` and `A-9`** of the carried role-bootstrap
refusal order (§T3.3), i.e.:

- **after** `A-1` (primitive binding and per-primitive identity check), `A-2`
  (`sys.flags` readback), `A-3` (empty `os.environ`), `A-4` (argv shape),
  `A-5` (descriptor types and `/proc/self/fd` exactness), `A-6` (self source
  `fstat` + `F_GETFL`), `A-7` (mutual `(st_dev, st_ino)` binding of the role
  bootstrap against the package root), `A-8` (`src` directory `fstat`);
- **before** `A-9` (`sys.path[:] = [...]`), `A-10`
  (`import philosophia.officina.generic_harness`), `A-11` (module inode
  re-verification), `A-13` (entry into the role).

At that instant the process has executed **only**: CPython startup under
`-I -S -E -P` with an empty environment; three imports (`os`, `sys`, `fcntl`);
the binding block; and eight validation steps composed of `fstat`, `listdir`,
`read`, `close`, `fcntl` and integer comparisons. `sys.path` still contains no
project directory, so **no project or client module is importable, let alone
imported**.

### R1.2 Steps `A-8a` … `A-8h`, executed only for `argv[7] == SUPERVISOR`

```text
A-8a. create the two watchdog channels:
        wd_upd_r, wd_upd_w := _pipe2(_O_CLOEXEC)      # supervisor → watchdog
        wd_ack_r, wd_ack_w := _pipe2(_O_CLOEXEC)      # watchdog → supervisor
      any OSError ⇒ WATCHDOG_CHANNEL_FAILED ⇒ §R1.8 cleanup, os._exit(3)

A-8b. HOIST(wd_upd_r, wd_ack_w, T_ROLE_FD_ROLESRC, T_ROLE_FD_SELF,
            T_ROLE_FD_SRCDIR, T_ROLE_FD_INTERP, T_ROLE_FD_PKGROOT)
      by the generalized §T6.1 algorithm, target set {3,4,5,7,8,9,10},
      so every source is > 10 and pairwise distinct.
      postcondition violated ⇒ WATCHDOG_FD_HOIST_FAILED ⇒ §R1.8

A-8c. build the file_actions sequence, in exactly this order:
        (DUP2, h[wd_upd_r],           3)     # watchdog update READ end
        (DUP2, h[wd_ack_w],           4)     # watchdog ack WRITE end
        (DUP2, h[T_ROLE_FD_ROLESRC],  5)
        (DUP2, h[T_ROLE_FD_SELF],     7)
        (DUP2, h[T_ROLE_FD_SRCDIR],   8)
        (DUP2, h[T_ROLE_FD_INTERP],   9)
        (DUP2, h[T_ROLE_FD_PKGROOT], 10)
        (CLOSE, h[...]) × 7, in the same order
        (CLOSE, 6)     # ← THE PCS SOCKET. see A-8d.
        (CLOSE, T_ROLE_FD_LOCK == 3 in the PARENT) — NOT expressible as a
        parent-numbered close; see A-8d for why no such action is needed.

A-8d. THE CLOSE-ON-EXEC AUDIT, which v2.1.10.2 omitted (§R1.5).
      Every descriptor this process holds at 3…10 arrived through
      POSIX_SPAWN_DUP2, which CLEARS close-on-exec on the destination.
      Therefore NONE of 3…10 would be closed by the watchdog's execve.
      The file_actions above overwrite 3,4,5,7,8,9,10 by DUP2 — which is
      itself the close of whatever those numbers held — and the ONE remaining
      number, 6 (the PCS seqpacket socket in the SUPERVISOR map), is closed by
      the explicit (CLOSE, 6) action.
      RESULT: the watchdog inherits exactly {0,1,2,3,4,5,7,8,9,10} and
      **does not inherit SPAWN.lock**, because SPAWN.lock is the supervisor's
      fd 3 and fd 3 is overwritten by the update-read DUP2.
      This is asserted as a REQUIREMENT, not an accident: §R6 row 409 checks
      that the watchdog's /proc/self/fd contains no descriptor whose
      (st_dev, st_ino) equals SPAWN.lock's.

A-8e. spawn, using the SAME object-bound mechanism as every other role:
        wd_pid := _posix_spawn(
            b"/proc/self/fd/9",                       # object-bound interpreter
            [ b"/proc/self/fd/9", b"-I", b"-S", b"-E", b"-P",
              b"/proc/self/fd/7",                     # object-bound role source
              b"--officina-role", b"WATCHDOG",
              b"--officina-generation", <64 hex>,
              b"--officina-fdmap", b"3,4,5,7,8,9,10" ],
            {},                                       # EXACTLY empty
            file_actions = A-8c's sequence,
            setsigmask   = (),
            setsid       = False )                    # see A-8f
      type(wd_pid) is not int, or wd_pid <= 0, or any BaseException
        ⇒ WATCHDOG_SPAWN_FAILED ⇒ §R1.8

A-8f. setsid is FALSE, deliberately: the watchdog must remain in the
      supervisor's session so it is not a session leader and cannot be
      confused with any controller/worker group. It is never a killpg target
      and never a group leader. This preserves the carried §U2.5 tier
      discipline, under which killpg is permitted only against a
      kernel-verified controller/worker group.

A-8g. close the parent's copies of the watchdog's ends (wd_upd_r, wd_ack_w)
      and every hoisted intermediate, unconditionally, in a pinned order.
      RETAIN wd_upd_w and wd_ack_r for the generation's life.

A-8h. C1 REGISTRATION, carried verbatim from §W3.1–§W3.2 and §Z4.1:
      poll wd_ack_r for the watchdog's FIRST ACK, bounded by the carried
      T_WATCHDOG_ACK_ABSENCE_TIMEOUT_NS at T_SUPERVISOR_POLL_INTERVAL_NS.
        first ack received and well-formed  ⇒ proceed to A-9
        EOF, malformed, or bound expiry     ⇒ the carried v2.1.3 §U2.6 route
              applies UNCHANGED and is SAFE HERE (§R1.7): kill the watchdog by
              its recorded identity, prove death, remove records per §U6.3,
              os._exit(3). At this instant the process is still the clean
              pre-import bootstrap, so the executor-set theorem of §V2110.3.8
              holds and kill-by-PID is sound.
```

Only after `A-8h` does the process execute `A-9`/`A-10` and become
contaminated.

### R1.3 Parent and reaper relations, before and after the import

| Relation | Before `A-10` | After `A-10` | Why |
|---|---|---|---|
| watchdog's parent | the role-bootstrap process | **the same process**, now running the supervisor | `import` and a function call do not change the process; the pid, the parent link, and the descriptor table are identical |
| watchdog's only possible reaper | that process's thread group | **the same thread group** | Linux: a `wait` reaps only a direct child of the calling thread group |
| `getppid()` in the watchdog | the supervisor process | the supervisor process, until it dies, at which point `init` adopts and `getppid()` **changes** | **this is the C1 supervisor-death detector, preserved intact** |
| supervisor's `waitpid` on the watchdog | its own direct child | **its own direct child** | **this is the C1 watchdog-death detector, preserved intact** |
| controller / worker parent and reaper | the PCS | the PCS | unchanged from §T4.1 |
| `pid_mid` parent and reaper | the PCS | the PCS | unchanged |

### R1.4 Who knows the watchdog PID, and which code can exercise it

| Process | Knows `wd_pid`? | Authority it may exercise |
|---|---|---|
| PCS | **no** — `wd_pid` is never sent on `t-pcs.v1`, never journalled by the PCS, and never a handle under P4's first construction | none |
| supervisor bootstrap, **pre-import** (clean) | yes | `waitpid`, and `kill` under the carried §U2.6 first-ack route. Sound: the executor-set theorem holds in this process at this instant |
| supervisor, **post-import** (contaminated) | yes | **`waitpid` only.** `kill(wd_pid, …)` is **withdrawn** (§R1.7) |
| watchdog | its own pid only | none over any other process |
| controller / worker | no | none |

### R1.5 Descriptor maps, `CLOEXEC`, and ownership transfer

**The defect v2.1.10.2 missed.** `POSIX_SPAWN_DUP2` clears `FD_CLOEXEC` on the
destination. Consequently **every** descriptor in the role bootstrap's map
(3…10) is non-close-on-exec, and a naive spawn would leak all of them into the
watchdog — including `T_ROLE_FD_LOCK` (fd 3), which is the fork-shared
`SPAWN.lock` reference. A watchdog holding that reference would keep the
singleton held for its entire life, which no carried route contemplates and
which would silently break §U2.5's lock discipline. `A-8c`/`A-8d` close it by
construction: fd 3 is overwritten by the update-read `DUP2`, and fd 6 (the PCS
socket) is closed explicitly.

| Descriptor | Supervisor after `A-8g` | Watchdog after exec | Transfer |
|---|---|---|---|
| `SPAWN.lock` | fd 3, retained until the carried `g3`-equivalent close | **absent** (fd 3 is the update-read end) | none |
| `boot` write end | fd 4 | **absent** (fd 4 is the ack-write end) | none |
| role source | fd 5 | fd 5 (its own, re-`DUP2`'d) | inherited object |
| PCS socket | fd 6 | **absent** (explicit `CLOSE`) | none |
| self source / srcdir / interp / pkgroot | 7, 8, 9, 10 | 7, 8, 9, 10 | inherited objects |
| watchdog update | write end retained by the supervisor | read end at fd 3 | created at `A-8a`, split at `A-8c`/`A-8g` |
| watchdog ack | read end retained by the supervisor | write end at fd 4 | same |

Both channel ends are created `O_CLOEXEC` in the parent and become
non-close-on-exec **only** in the child, and **only** for the two the child
must have, by `DUP2`. No descriptor is ever transferred by number over any
wire; the watchdog channels are inherited, exactly as C1 already requires.

### R1.6 C1 sequences under P4

| C1 sequence | Under P4 | Signed text |
|---|---|---|
| registration and first ack | `A-8h`, before any project import | §W3.1–§W3.2, §Z4.1 — **unchanged** |
| lease-table publication and ack liveness | supervisor writes on `wd_upd_w`, reads `wd_ack_r` | §Z4.1–§Z4.3 — **unchanged** |
| freeze, quiescence proof, freeze observations | unchanged; the watchdog writes `WATCHDOG/FREEZE/<witness_id>.json` and settles nothing | §W3.3, §Z4.4–§Z4.6 — **unchanged** |
| **supervisor death** | `getppid() != recorded` **or** update-pipe EOF — **both live** | §W3.5 — **unchanged** |
| **watchdog death** | supervisor `waitpid` on its own child **or** ack absence past the carried timeout | §W3.5 — **unchanged** |
| watchdog replacement after death | §R2.1 — obtained from the PCS, with a stated degraded detector | §W3.5's "forks a new watchdog" **superseded post-import only** |
| shutdown | §R1.10 | — |

### R1.7 Post-import kill authority, withdrawn

> **Finding.** After `A-10` the supervisor process is contaminated, so the
> executor-set theorem does not hold in it. A contaminated helper thread or a
> monkeypatched `os.waitpid` could reap the watchdog; the pid could then be
> recycled; and a subsequent `kill(wd_pid, …)` would be the exact C218-1 harm on
> one PID. **P4 does not automatically escape the defect it was designed around
> — it narrows it to one process, and the narrowing must be completed by
> removing the kill.**

```text
POST-IMPORT WATCHDOG AUTHORITY, normative under P4:
  PERMITTED : _waitpid(wd_pid, WNOHANG), through the carried WAIT_ONE
              classifier (§V2110.4.1) including STRUCTURAL_VIOLATION.
              SAFE under contamination: a stolen reap yields ECHILD, which the
              carried rules map to CONTRADICTED_ECHILD — never death, and it
              authorizes nothing. The failure mode is fail-closed, not a wrong
              action.
  FORBIDDEN : kill(wd_pid, …) or any signal to wd_pid, for any reason.
  TERMINATION instead: close wd_upd_w through CLOSE_OWNED. The watchdog
              observes EOF on its update read end and exits by the carried
              §W3.3/§Z4 route, having written its observations. The supervisor
              then reaps it by _waitpid.
  IF the watchdog does not exit within the carried
     T_WATCHDOG_ACK_ABSENCE_TIMEOUT_NS after the EOF: the supervisor does NOT
     escalate to a signal. It records WATCHDOG_UNREAPED, refuses every
     admission, and routes the generation through the signed T_PROCESS_INVALID
     and §4c(c)/§4d unknowable path (§T4.7, carried). This is a fail-closed
     stall, and it is stated as a cost of P4 rather than repaired by a kill
     whose safety cannot be established.
```

The carried pre-import kill route (§U2.6's first-ack-timeout row) is
**unchanged**, because at that point the process is provably clean.

### R1.8 Refusal and partial-construction cleanup, without inventing an outcome

```text
WATCHDOG_CONSTRUCTION_CLEANUP(stage):
  after A-8a failure : nothing was created; close any channel end that exists,
                       in a pinned order; os._exit(3); nothing written,
                       nothing unlinked, no record installed
  after A-8b failure : close every channel end and every hoisted intermediate;
                       os._exit(3)
  after A-8e failure : no child exists; as above
  after A-8e success, before A-8h completes:
                       the child exists. Take the carried §U2.6 route: kill by
                       recorded identity (SOUND here, §R1.7), prove death by
                       _waitpid, then close every end, then os._exit(3)
  after A-8h failure with the child proved dead:
                       os._exit(3), nothing written, nothing unlinked
  after A-8h failure with death NOT proved:
                       the carried non-returning reaper state (§V2110.4.2 B),
                       which retains every handle and installs nothing. It does
                       NOT invent a refusal, a success, or a resource fact
  in EVERY case the supervisor bootstrap has installed NO durable record and
  written NO boot line, so the PCS's carried c13 read observes EOF and takes
  the carried §U2.5 stage-2 route. No outcome is fabricated anywhere.
```

### R1.9 The corrected process tree

```text
[0] contaminated caller
     │ posix_spawn (§V21101.3, carried)
     ▼
[1] PCS — process authority for pid_mid, controllers, workers
     ├─ c4 fork ─▶ [2] middle (pid_mid)  ─ m7 fork ─▶ [3] grandchild
     │                                                  │ execve
     │                                                  ▼
     │                                        [3'] role bootstrap (SUPERVISOR)
     │                                             │ A-8e posix_spawn
     │                                             ▼
     │                                        [4] role bootstrap (WATCHDOG)
     │                                             parent AND sole reaper: [3']
     ├─ posix_spawn(setsid=True) ─▶ [5] role bootstrap (CONTROLLER) × n
     └─ posix_spawn(setsid=True) ─▶ [6] role bootstrap (WORKER) × n

Reaper relations, exhaustive:
  [0] may reap only [1].
  [1] is parent and sole reaper of [2], [5], [6].
  [2] is parent of [3] until m9; then init adopts and reaps [3]/[3'].
  [3'] is parent and SOLE reaper of [4] — and of nothing else, ever.
```

### R1.10 Shutdown, with the watchdog reaped before the supervisor exits

```text
S-1. supervisor stops admitting; drains and settles per the carried §W3.4/§4c
S-2. supervisor requests SHUTDOWN on t-pcs.v1
       HANDLES_LIVE ⇒ it must first REAP_ROLE every controller/worker handle
       OK           ⇒ the PCS has released the lock and exited
S-3. supervisor closes wd_upd_w through CLOSE_OWNED
S-4. watchdog observes EOF, writes its final observations, os._exit(0)
S-5. supervisor polls _waitpid(wd_pid, WNOHANG) at
     T_SUPERVISOR_POLL_INTERVAL_NS, bounded by the carried
     T_WATCHDOG_ACK_ABSENCE_TIMEOUT_NS:
       REAPED_POSITIVE      ⇒ watchdog death PROVED; proceed to S-6
       CONTRADICTED_ECHILD  ⇒ death NOT proved. The generation routes to
                              T_PROCESS_INVALID. The supervisor MAY still exit:
                              if the watchdog were somehow alive, the
                              supervisor's exit changes its getppid(), which
                              fires the carried C1 self-termination route, and
                              init reaps it. No record is removed on a false
                              death proof
       STRUCTURAL_VIOLATION ⇒ identical to the ECHILD row
       NOT_YET at the bound ⇒ WATCHDOG_UNREAPED (§R1.7): invalidity route; the
                              supervisor exits; init adopts and the watchdog
                              self-terminates on the ppid change
S-6. supervisor removes only records it may remove under §U6.3, closes its
     remaining descriptors through CLOSE_OWNED, and exits.
```

**The exit is safe in every branch** because the watchdog's own carried
supervisor-death route (`getppid()` change ⇒ freeze known groups, write
observations, exit) makes it self-terminating without any signal from anyone.

### R1.11 Crash cuts

| Cut | Continuation |
|---|---|
| crash between `A-8a` and `A-8e` | no watchdog; no record installed; the PCS's `c13` sees EOF ⇒ carried stage-2 route |
| crash after `A-8e`, before `A-8h` | the watchdog exists and is adopted by `init`; its `getppid()` changes ⇒ carried C1 route ⇒ it freezes the (empty) known set, writes observations, exits; `init` reaps it |
| crash after `A-8h`, before `A-10` | identical |
| crash after `A-10`, any time | identical for the watchdog; the PCS holds every controller/worker handle and enters the carried non-returning reaper state per handle (§T2.7) |
| **PCS death**, supervisor alive | §R2.5 |
| **supervisor death**, PCS alive | the watchdog fires both detectors; the PCS observes `PEER_EOF` on `t-pcs.v1` and holds every handle in the carried reaper state; the singleton is not freed; the next attempt's §U6.1 preflight governs |
| **watchdog death**, both alive | detected by `waitpid` or ack absence; §R2.1 governs replacement |
| watchdog spawn returns a structurally impossible value | `WATCHDOG_SPAWN_FAILED`; ownership never established; §R1.8 |

### R1.12 Why nothing contaminating exists before watchdog construction

| Vector | Why it is absent at `A-8a`…`A-8h` |
|---|---|
| client or project import | `sys.path` has no project entry until `A-9`; `-S` and `-I` remove site and user paths, so nothing importable exists beyond the three stdlib modules |
| `.pth`, `sitecustomize`, `usercustomize` | `-S` prevents `site` from being imported at all; `A-2` reads the flag back from `sys.flags` |
| environment injection | `-E` plus `A-3`'s assertion that `os.environ` is empty |
| audit / import / trace / profile hook | installing one requires `sys.addaudithook` / `sys.settrace` / `sys.setprofile` or a `.pth`; the first three are forbidden symbols under the carried `S-7'` grammar and none has executed |
| monkeypatch of a primitive | `A-1` binds and identity-checks every primitive by the carried per-primitive table (§V21101.1.4) **before** anything else; and no code has run that could have patched one |
| retained callback, finalizer | no object from any other program exists; the three stdlib modules register none |
| at-fork callback | `os.register_at_fork` is a forbidden symbol and has not been called by anything; `posix_spawn` runs no Python at-fork callback (carried §V21101.3.1, and non-load-bearing there and here) |
| helper thread | `threading`, `_thread`, `multiprocessing`, `concurrent`, `asyncio`, `ctypes` are outside the role root's scoped allowlist; `A-5`'s `/proc/self/fd` check and the carried single-task readbacks apply |

**Therefore the watchdog is created by a process in exactly the same verified
condition as the PCS itself** — which is the property P4 exists to obtain, and
which P2 cannot obtain at all.

### R1.13 Why controllers and workers stay PCS-only

The supervisor never learns a controller or worker PID: `t-pcs.v1` has **no pid
field** (carried §T2.2), and every operation names a target by an opaque handle.
It therefore cannot express `kill(pid)`, `killpg(pgid)`, or `waitpid(pid)`
against one. And it could not act even if it learned a number: those processes
are direct children of the **PCS**, so a `wait` in the supervisor's thread group
ranges over the supervisor's own children — which under P4 is the set
`{watchdog}` and nothing else. Both barriers are independent.

---

## R2. The PCS design, recomputed under P4

### R2.1 `SPAWN_WATCHDOG` — retained, re-scoped, and justified

The prompt requires removal unless a different single-valued purpose is proved.
**A purpose is proved: replacement.** Carried §W3.5 requires that on watchdog
death the supervisor obtain a new watchdog and continue; under P4 the supervisor
is contaminated by then and must not fork one itself (that would be P2 on the
replacement path). The operation therefore survives, renamed and re-preconditioned:

```text
SPAWN_REPLACEMENT_WATCHDOG
  request operands : none
  preconditions    : (i) the first watchdog's death is PROVED by the
                     supervisor's own REAPED_POSITIVE, or by the carried
                     ack-absence rule with a subsequent proved reap;
                     (ii) no live watchdog handle exists in this generation
  response operands: handle_id
  fds              : 2 — update write end, ack read end (unchanged vector)
  CONSEQUENCE, stated in the response and journalled: a replacement watchdog is
  a child of the PCS, so its getppid() does NOT change when the supervisor
  dies. The replacement therefore has ONE supervisor-death detector
  (update-pipe EOF), not two. The supervisor records
  WATCHDOG_DETECTOR_DEGRADED for the remainder of the generation.
```

> **This is a real cost of P4 and is not hidden**: P4 gives two detectors for
> the first watchdog and one for any replacement. P1 gives one for every
> watchdog. P3 gives two for every watchdog and repairs nothing else.

The `t-pcs.v1` operation count is therefore **unchanged at nine**:
`SPAWN_ROLE`, `AWAIT_STOP`, `SIGNAL_ROLE`, `SIGNAL_GROUP`, `REAP_ROLE`,
`SPAWN_REPLACEMENT_WATCHDOG`, `RELEASE_HANDLE`, `SHUTDOWN`, `PING`. Every
field and count statement in carried §T2.2–§T2.3 stands with that one row
re-worded.

### R2.2 Descriptor-vector table under P4

| Operation / result | fds | vector |
|---|---|---|
| every request | 0 | — |
| `SPAWN_ROLE` ok | 3 | ctrl request write, ctrl reply read, status read — all `S_ISFIFO` |
| `SPAWN_REPLACEMENT_WATCHDOG` ok | 2 | update write, ack read — both `S_ISFIFO` |
| every refusal, and every other operation | 0 | — |

Maximum descriptors per message remains **3**; the ancillary buffer remains
`CMSG_SPACE(12)`. **Unchanged by P4.**

### R2.3 Handle table under P4

The handle record is unchanged (§T4.3). Under P4 it contains **no entry for the
first watchdog**, which the PCS neither creates, signals, waits for, nor names.
A replacement watchdog does get a handle, and its `role` field is
`WATCHDOG_REPLACEMENT`, which is refused by `SIGNAL_ROLE` and `SIGNAL_GROUP`
(the PCS may create and reap a replacement watchdog but never signals it, for
the same reason the supervisor may not: the carried EOF-driven termination is
the only route).

### R2.4 Primitive → operation → consumer map under P4

| Carried primitive | Under P4 | Unique consumer |
|---|---|---|
| `Popen` of a controller/worker (§W2.5) | PCS `SPAWN_ROLE` | §Z3.3 adapter duties, then the claim |
| `waitpid(WNOHANG\|WUNTRACED)` self-stop (§W2.5) | PCS `AWAIT_STOP` | the `t-process-claim.v1` write |
| `kill` on a role (§W2.4, §U2.5) | PCS `SIGNAL_ROLE` | death proof, §U6.3 removal |
| `killpg` on a verified group (§U2.5, §W3.3) | PCS `SIGNAL_GROUP` | freeze, stage-2 route |
| `waitpid` death proof for a role | PCS `REAP_ROLE` | `T1`/`T2`, §U6.1 P3 |
| **`os.fork` of the watchdog (§W2.1)** | **the supervisor bootstrap's own `posix_spawn` at `A-8e`** | C1 registration and ack at `A-8h` |
| **`waitpid` on the watchdog (§W3.5)** | **the supervisor's own `_waitpid`** | C1 watchdog-death detection |
| watchdog replacement (§W3.5) | PCS `SPAWN_REPLACEMENT_WATCHDOG` | C1 re-registration, with the degraded detector recorded |

**"Relocate the primitive, preserve the semantics" now holds for every row**,
because the two detectors that had no operation under P1 are, under P4, not
relocated at all — they stay where the signed text put them.

### R2.5 PCS loss under P4 — no orphaned or ungoverned watchdog

```text
On PEER_EOF of t-pcs.v1 (PCS died or exited):
  1. the supervisor has lost ALL controller/worker authority: it can create,
     signal, wait for, and reap none of them;
  2. the supervisor RETAINS full authority over its own watchdog — the watchdog
     is neither orphaned nor ungoverned, because its parent is alive;
  3. the supervisor immediately refuses every admission and every command that
     would require a role operation;
  4. FREEZE IS UNAVAILABLE: the carried §W3.3 quiescence proof requires
     killpg(SIGSTOP)/SIGCONT against controller groups, which is a PCS
     operation. Therefore no valid continuation exists for any live stream;
  5. the supervisor closes wd_upd_w; the watchdog observes EOF, writes its
     observations for the groups it knows, and exits; the supervisor reaps it
     by _waitpid (S-5's branches apply);
  6. the generation routes through the signed T_PROCESS_INVALID recovery
     disposition and the §4c(c)/§4d unknowable route, with invalidity dominance
     exactly as carried;
  7. NO false valid continuation is permitted: no settlement, no capacity
     release, no custody disposition, and no result is produced from a stream
     whose freeze could not be proved.
```

### R2.6 The PCS journal under P4

The PCS journal contains **no watchdog operation** for the first watchdog. It
contains a `SPAWN_REPLACEMENT_WATCHDOG` entry only if a replacement was
requested. The supervisor's own watchdog construction is recorded in the carried
`WATCHDOG_CHILD.json` fork-child record (§Z3.6), unchanged — **not** in the PCS
journal, and not in a new durable object.

### R2.7 Role-bootstrap import and primitive surface, corrected

See §R4.5. `{os, sys, fcntl}`, three imports, with the carried **per-primitive
identity table** (§V21101.1.4) and explicitly **no universal
builtin-identity predicate**, which the chain already refuted at v2.1.10.1
§V21101.1.4 (it would reject a genuine pure-Python wrapper). The primitives the
watchdog construction adds — `_pipe2`, `_posix_spawn`, `_waitpid`, `_dup` — are
all `os` built-ins re-exported from `posix` and are covered by the table's
existing first row.

---

## R3. The remaining costs, stated loudly

**P4 does not erase the B1 and D1 author changes.** Every item below is true
under P4 exactly as it is under P1, and no option may be recommended by
discounting them.

1. **The PCS is still a mandatory resident process and an unrecoverable
   whole-generation failure point for controller/worker authority.** Its death
   cannot be repaired by adoption — a new PCS is not the parent of any surviving
   role and so can neither wait for nor safely signal one — and §R2.5 routes the
   whole generation to invalidity. This is strictly worse availability than the
   signed §W2.9 two-phase takeover it displaces. **D1's ground ("no supervisor
   waits on `SPAWN.lock`") is intact; the availability model around it is new.**
2. **`t-pcs.v1` still introduces a second durable control-plane journal**, with
   its own crash-cut surface, alongside the signed B1 client journal.
3. **fd-bearing `SPAWN_ROLE` replies remain non-redeliverable as capabilities.**
   The byte record is replayable; the descriptors are never re-sent, because a
   second copy of a capability cannot be reconciled by any accounting in this
   contract. A supervisor that loses them cannot recover them, and the
   generation routes to invalidity. **This is a genuine narrowing of B1's
   retry-stable-reply promise on this channel**, applying to two of the nine
   operations under P1 and to two under P4.
4. **`_socket` and `SCM_RIGHTS` capability transfer remain**, and remain
   Linux-specific. Exact recount: **five production roots**
   (`officina_activate_t.py`, `verify_officina_active.py`, `generic_harness.py`,
   `officina_process_control_bootstrap.py`, `officina_role_bootstrap.py`) —
   **unchanged by P4**, which adds no root. PCS import closure
   `{os, sys, _signal, time, fcntl, _socket}` — six, unchanged by P4. Role
   bootstrap `{os, sys, fcntl}` — three, **corrected upward from two** by §R4.5.
   `t-pcs.v1` operations — **nine**, unchanged. Max descriptors per message —
   **three**, unchanged.
5. **The supervisor's one-child watchdog PID authority is a narrow signed trust
   surface, not "no PID authority".** After `A-10` the supervisor holds
   `wd_pid` in a contaminated interpreter. §R1.7 removes the *signal* half, so
   the residual is exactly: a competing reaper inside the supervisor could steal
   the watchdog's reap, producing `ECHILD`, which is inconclusive and
   fail-closed — it can cost the generation, and it cannot cause a wrong-PID
   signal. **That is the honest description; "P4 removes PID authority from the
   supervisor" would be false and is not claimed.**
6. **P4 adds a detector asymmetry**: two supervisor-death detectors for the
   first watchdog, one for any replacement (§R2.1).
7. **P4 adds a fail-closed stall**: a watchdog that does not exit on EOF cannot
   be killed post-import, so the generation stalls into invalidity rather than
   being repaired (§R1.7).

---

## R4. Engineering honesty checks — author pre-review, no probe executed

### R4.1 The `/proc/self/fd` sweep is unsafe and is replaced

> **Refuted.** v2.1.10.2 §T1.6 remediation step 2 says: "additionally, scan
> `/proc/self/fd` and close every descriptor outside this process's pinned set".
> **In the supervisor, the pinned set is not static**: every successful
> `SPAWN_ROLE` adds three received controller/worker authority descriptors, and
> the number of live roles is unbounded at design time. A sweep would therefore
> **close legitimate authority descriptors of unrelated live roles**, silently
> breaking their ctrl and status channels. The rule is also not single-valued,
> because "the pinned set" is never defined for a process whose set grows. It is
> **deleted**.

```text
REPLACEMENT — bounded exact received-fd cleanup:
  On ANY non-OK transport result for a message, close EXACTLY the descriptors in
  that message's PARSED vector, in ascending numeric order, with _close,
  tolerating EBADF. Close nothing else. Never enumerate /proc/self/fd.

  WHY THE PARSED VECTOR IS EXACTLY THE INSTALLED SET. Linux installs SCM_RIGHTS
  descriptors at whole-`int` granularity: when the ancillary buffer is too
  small, it installs floor(space / sizeof(int)) descriptors and sets MSG_CTRUNC,
  and every descriptor it installed is reported in the returned control data.
  The parser's multiple-of-4 rule therefore enumerates precisely the installed
  set. This is a pinned platform fact and is marked REVIEWER-VERIFIABLE.

  WHY THE RULE IS SAFE EVEN IF THAT FACT IS WRONG. If the kernel installed FEWER
  descriptors than reported, the extra closes are EBADF and are tolerated. If it
  installed MORE than reported, the unreported ones leak — a resource fact, not
  an authority fact, and bounded because the message routes to §T4.7 invalidity
  and the process exits. In neither direction can the rule close a descriptor
  belonging to another message or another role.
```

### R4.2 `SCM_RIGHTS` close/ACK/crash cuts after removing the watchdog messages

The carried §T1.5 ownership table stands with one row deleted (the first
watchdog never appears on the wire) and one renamed
(`SPAWN_WATCHDOG` → `SPAWN_REPLACEMENT_WATCHDOG`). Re-checked:

| Cut | Under P4 |
|---|---|
| PCS sends a 3-fd `SPAWN_ROLE` reply, then crashes before the ACK | the supervisor holds the descriptors; the journal entry is `COMPLETED`; the PCS is gone ⇒ §R2.5's invalidity route. **No double-delivery**, because replacement PCS adoption is prohibited |
| supervisor crashes with descriptors buffered in the socket | Linux releases buffered `SCM_RIGHTS` descriptors when the socket is closed ⇒ **no leak**; the PCS observes `PEER_EOF` |
| ACK lost | `FD_DELIVERY_UNCONFIRMED`; **no re-send**; §T4.7 |
| replayed `SPAWN_REPLACEMENT_WATCHDOG` | the recorded record with `fds_redelivered = 0` and **no** descriptors; a supervisor that lost them routes to invalidity |
| a violating message that carried fds | §R4.1's bounded cleanup, then §T4.7 |

### R4.3 `SOCK_SEQPACKET`, truncation flags, `MSG_CMSG_CLOEXEC`

Re-audited and **unchanged**: one `sendmsg` of a ≤ 4096-byte payload is one
record or nothing, so no partial-record state exists; `MSG_TRUNC` and
`MSG_CTRUNC` are the only size-violation signals and both route to
`ANCILLARY_VIOLATION`; `MSG_CMSG_CLOEXEC` is mandatory on every `recvmsg` and
sets `FD_CLOEXEC` atomically with installation, so no received descriptor can
leak across an `exec`. **These remain reviewer-verifiable platform facts**, and
§R4.1 now states what happens if the truncation fact is wrong.

### R4.4 Source and interpreter binding for the watchdog's isolated exec

The watchdog exec uses **the same objects** the supervisor bootstrap is itself
running: `/proc/self/fd/9` (the interpreter object inherited from the PCS, which
inherited it from the caller) and `/proc/self/fd/7` (the role-bootstrap source
object, whose `(st_dev, st_ino)` the supervisor bootstrap already proved equal
to the canonical path under the package root at `A-7`). **No new path string, no
`readlink`, and no new provenance obligation is introduced by P4**; the watchdog
inherits exactly the object identities the carried chain already established,
and re-proves them itself at its own `A-6`/`A-7`.

### R4.5 The role-bootstrap import set was wrong

> **Refuted.** v2.1.10.2 §T3.2 and §T5.1 say the role bootstrap imports "exactly
> `os` and `sys`. Nothing else." But its own step `A-6` requires the descriptor
> to be read-only "by the §T5.3 `F_GETFL` test", and §T5.3's test is
> `_fcntl(fd, _F_GETFL) & _O_ACCMODE == _O_RDONLY`. **`fcntl` is therefore
> required and the two-module claim is false.**

```text
CORRECTED: the role bootstrap root imports exactly THREE modules:
    import os
    import sys
    import fcntl
  scoped allowlist entry: {os, sys, fcntl}
  grammar rule S-1' for the role root: exactly three Import nodes, module
  scope, unaliased, no ImportFrom, none conditional or nested
  `fcntl` is a built-in C module with an empty Python import closure, starts no
  task, registers no at-fork callback, and installs no hook — the audit carried
  from §T5.1's table row, unchanged.
```

`_socket` is **not** added to the role bootstrap: under P4 it creates only
pipes, and only the PCS speaks `t-pcs.v1`. The supervisor's `t-pcs.v1` client
runs **after** `A-10`, inside `generic_harness.py`, whose scoped allowlist is
unchanged and which therefore needs `_socket` **added to its own scoped entry**
— a consequence of P4 and P1 alike, recorded here as §R4.6.

### R4.6 One consequence the carried text did not state

Under both P1 and P4 the **supervisor role** must speak `t-pcs.v1`, so
`src/philosophia/officina/generic_harness.py`'s scoped allowlist must gain
`_socket`. v2.1.10.2 §T5.4 gave that file a set containing "neither `signal` nor
`_signal` nor `_socket` nor `sys`", which is **inconsistent with the supervisor
being the PCS client**. Corrected: `generic_harness.py`'s scoped set is the
sixteen signed members **plus `_socket`**, and still **neither** `signal`, nor
`_signal`, nor `sys`. Under P3 no change is required.

### R4.7 Numeric recount

| Statement | Value | Changed by P4? |
|---|---|---|
| production roots | 5 | no |
| `t-pcs.v1` operations | 9 | no (one renamed and re-preconditioned) |
| max descriptors per message | 3 | no |
| ancillary buffer | `CMSG_SPACE(12)` | no |
| PCS import closure | 6 — `{os, sys, _signal, time, fcntl, _socket}` | no |
| role-bootstrap import closure | **3** — `{os, sys, fcntl}` | **yes: corrected from 2** (§R4.5) |
| `generic_harness.py` scoped set | 16 signed + `_socket` | **yes: corrected** (§R4.6) |
| watchdog descriptor map | 7 entries: 3, 4, 5, 7, 8, 9, 10 | new under P4 |
| supervisor-death detectors, first watchdog | **2** | **yes: 1 under P1, 2 under P4** |
| supervisor-death detectors, replacement watchdog | 1 | — |
| test rows referenced | §T8's 353–404 stand; §R6 adds **405–436** | — |

---

## R5. The corrected Cell P

### R5.1 What each option is

- **P1 — full PCS mediation.** The PCS creates, signals, waits for and reaps
  every process including the watchdog. §T1–§T6 as written in v2.1.10.2.
- **P4 — clean-bootstrap-parented watchdog.** As P1 for `pid_mid`, controllers
  and workers; the **first** watchdog is created by the isolated supervisor role
  bootstrap before any project import, and the supervisor remains its parent and
  sole reaper for the generation. §R1–§R2 above.
- **P3 — defer supervisor authority.** No PCS beyond v2.1.10's scope. The
  supervisor keeps its own `Popen`/`waitpid`/`kill`/`killpg`/watchdog-fork, and
  that defect stays **open** as a named Major finding for its own signed layer.
  §T3's isolated role root and §T5's import/`fcntl` corrections may be adopted
  independently, since neither depends on the PCS.

### R5.2 P2 is strictly dominated and is withdrawn

| Property P2 claimed | P2 | P4 |
|---|---|---|
| `getppid()` supervisor-death detector | preserved | **preserved** |
| `waitpid`-on-own-child watchdog-death detector | preserved | **preserved** |
| watchdog address space | **inherited from a contaminated supervisor** | **fresh, isolated, `-I -S -E -P`, empty environment** |
| watchdog creation-time process state | contaminated | **verified clean** (§R1.12) |
| watchdog holds `SPAWN.lock`? | inherits the supervisor's fork-shared reference unless separately closed | **provably not** (§R1.5) |
| post-import kill authority | present and unsafe | **withdrawn** (§R1.7) |

P4 is at least as good on every row and strictly better on four. The only thing
P2 uniquely offers is that the watchdog starts with the supervisor's modules
already loaded — an operational convenience, not a property. **P2 is withdrawn
rather than kept as a token alternative**, exactly as the instruction requires.

### R5.3 The exact mutually exclusive tokens, and the gains/costs table

**Exactly one must be signed. None is selected here. No option decides a
scientific or resource value, moves a K1 constant, an E1/E2/E3 value, a T band,
a capacity ceiling, a custody rule, or a Q/C boundary.**

```text
I_SELECT_SUPERVISOR_PROCESS_AUTHORITY_P1_FULL_PCS_MEDIATION
I_SELECT_SUPERVISOR_PROCESS_AUTHORITY_P3_DEFER_SUPERVISOR_AUTHORITY
I_SELECT_SUPERVISOR_PROCESS_AUTHORITY_P4_CLEAN_BOOTSTRAP_PARENTED_WATCHDOG
```

| | **P1** | **P4** | **P3** |
|---|---|---|---|
| controller/worker PID authority | clean PCS | clean PCS | **contaminated supervisor — the open defect** |
| supervisor names PIDs? | never | only `wd_pid`, `waitpid` only | yes, all of them |
| C1 supervisor-death detectors (first watchdog) | **1** (pipe EOF) | **2** (ppid + pipe EOF) | 2 |
| C1 watchdog-death detector | PCS round trip | **supervisor `waitpid`, direct** | supervisor `waitpid`, direct |
| watchdog address space | fresh, isolated | **fresh, isolated** | inherited from a contaminated supervisor |
| replacement watchdog | PCS, 1 detector | PCS, 1 detector, **asymmetry recorded** | supervisor fork, 2 detectors |
| watchdog termination post-import | PCS `SIGNAL_ROLE` | **EOF only; no kill; fail-closed stall possible** | supervisor kill |
| B1 second journal | yes | yes | no |
| fd-bearing replies non-redeliverable | yes | yes | n/a |
| PCS unrecoverable single point of failure | yes | yes | no |
| `_socket` / `SCM_RIGHTS` / 5 roots | yes | yes | no (4 roots; role root optional) |
| known Major defect left open | none | none | **yes — supervisor process authority** |

### R5.4 Bounded exhaustiveness argument

The choice space is the product of two independent questions.

**(a) Who holds controller/worker PID authority?** Exactly two answers exist: a
clean constructed process (the PCS) or the contaminated supervisor. There is no
third, because the authority must live in *some* process and every process in
the tree is either constructed clean or reached by importing project code.

**(b) Who parents the first watchdog?** Exactly three answers exist: the PCS
(P1), the supervisor process **before** it imports project code (P4), or the
supervisor process **after** (P2). No fourth exists, because the watchdog's
parent is whichever process issues the creating primitive, and only those three
processes are in a position to issue it at the required point in the sequence.

The product is six cells; two are inconsistent (a contaminated supervisor
holding controller authority while a PCS parents the watchdog implies a PCS
that exists but is unused, which is P1 with extra cost); one is P2, dominated;
leaving **P1, P3, P4**. **This is a bounded argument over a two-dimensional
space, not a claim that no other architecture could ever exist** — a design that
changed *what* the watchdog is, or that eliminated the supervisor's role
entirely, would be outside this cell and would require its own.

---

## R6. Tests added by this layer

Replaced: §T8 rows **354**, **356**, **362**, **374**, **381** (watchdog
messages and the two-import assertion).

| # | Test |
|---|---|
| 405 | `A-8a`…`A-8h` execute **only** for `argv[7] == SUPERVISOR`, and **only** between `A-8` and `A-9`; assert no project module is importable at that point |
| 406 | the watchdog spawn uses `/proc/self/fd/9` and `/proc/self/fd/7`, empty environment, `-I -S -E -P`, `setsid=False`, and the exact seven-entry fd map |
| 407 | after `A-10`, `getppid()` in the watchdog still equals the supervisor's pid; after the supervisor exits, it changes and the carried C1 route fires |
| 408 | the supervisor's `_waitpid(wd_pid, WNOHANG)` returns the pid on watchdog exit; a stolen reap yields `ECHILD` → `CONTRADICTED` → fail-closed, never a death proof |
| 409 | **the watchdog holds no descriptor whose `(st_dev, st_ino)` equals `SPAWN.lock`'s**, and its `/proc/self/fd` is exactly `{0,1,2,3,4,5,7,8,9,10}` |
| 410 | the PCS socket (fd 6) is closed in the watchdog by the explicit `CLOSE` action |
| 411 | every descriptor at 3…10 in the role bootstrap is non-close-on-exec (a consequence of `POSIX_SPAWN_DUP2`), and the file-action set therefore closes or overwrites every one that must not be inherited |
| 412 | no `kill` to `wd_pid` appears on any post-import path; static over `generic_harness.py` |
| 413 | the pre-import first-ack-timeout kill route (carried §U2.6) is present and reachable **only** before `A-10` |
| 414 | EOF-driven watchdog termination: closing `wd_upd_w` makes the watchdog write its observations and exit; the supervisor reaps it |
| 415 | `WATCHDOG_UNREAPED` routes to `T_PROCESS_INVALID` and §4c(c)/§4d; no kill, no invented outcome |
| 416 | `S-1`…`S-6` shutdown ordering: the watchdog is reaped, or the generation is invalid, before the supervisor exits; every `S-5` branch behaves as tabulated |
| 417 | each `§R1.8` cleanup stage leaves nothing written, nothing unlinked, and no record installed |
| 418 | each `§R1.11` crash cut has exactly one continuation |
| 419 | `SPAWN_REPLACEMENT_WATCHDOG` is refused unless the first watchdog's death is proved and no live watchdog handle exists |
| 420 | a replacement watchdog's handle is `WATCHDOG_REPLACEMENT`; `SIGNAL_ROLE`/`SIGNAL_GROUP` refuse it; the supervisor records `WATCHDOG_DETECTOR_DEGRADED` |
| 421 | the PCS journal contains **no** watchdog entry for the first watchdog; `WATCHDOG_CHILD.json` is written by the supervisor bootstrap as carried |
| 422 | `t-pcs.v1` has exactly nine operations and no pid field; the supervisor cannot express a controller/worker PID |
| 423 | a wildcard wait in the supervisor reaches **only** the watchdog, and never `pid_mid`, a controller, or a worker |
| 424 | **§R4.1**: a violating message closes exactly its parsed vector and **nothing else**; assert that a live role's previously received descriptors survive a violation on an unrelated message |
| 425 | `/proc/self/fd` is never enumerated for remediation anywhere |
| 426 | the role bootstrap imports exactly `{os, sys, fcntl}`; a two-import build fails `A-6` |
| 427 | `generic_harness.py`'s scoped set is the sixteen signed members plus `_socket`, and contains neither `signal`, `_signal`, nor `sys` |
| 428 | the per-primitive identity table is used in the role bootstrap; **no universal builtin predicate appears anywhere** |
| 429 | `§R1.12`'s eight contamination vectors are each absent at `A-8a` |
| 430 | PCS `PEER_EOF`: the supervisor retains watchdog authority, loses role authority, refuses admissions, cannot freeze, and routes the generation to invalidity with no false continuation |
| 431 | the watchdog is never a session leader and never a `killpg` target |
| 432 | `SOCK_SEQPACKET` record, `MSG_TRUNC`/`MSG_CTRUNC`, and `MSG_CMSG_CLOEXEC` behaviours are unchanged from §T8's rows |
| 433 | numeric recount: 5 roots, 9 operations, 3 max fds, `CMSG_SPACE(12)`, 6/3 import closures |
| 434 | P2 appears nowhere as a selectable option; the three tokens of §R5.3 are the only ones present |
| 435 | no option in Cell P moves a K1 constant, an E1/E2/E3 value, a T band, a capacity ceiling, a custody rule, or a Q/C boundary |
| 436 | whole-chain no-regression diff over every carried surface named in §T9 and §V21101.9 |

---

## V21103.7. Weakest points, written against my own proposal

1. **P4's central claim rests on "importing a module does not change the
   process".** That is true and mechanical, but it is the single load-bearing
   step, and if a reviewer can name any way the role bootstrap's identity
   changes between `A-8e` and `A-13` — a re-exec, a fork in the entry function,
   a `daemonize` helper inside `generic_harness.py` — the whole option
   collapses. §R6 row 407 tests it; the contract forbids it; but the property
   lives in code the bootstrap imports and does not control.
2. **P4 narrows the C218-1 class to one PID; it does not eliminate it.** After
   `A-10` a competing reaper in the contaminated supervisor can steal the
   watchdog's reap. I removed the signal half, so the residual is fail-closed
   rather than harmful — but the residual is real and I have not claimed
   otherwise.
3. **P4 makes a wedged watchdog unrepairable.** No post-import kill means a
   watchdog that ignores EOF stalls the generation into invalidity. P1 can kill
   it through the PCS. Whether a fail-closed stall is better than a
   possibly-unsafe kill is precisely the kind of trade the author cell exists
   for, and I have not decided it.
4. **The detector asymmetry is inelegant.** Two detectors for the first
   watchdog, one for every replacement, with a `WATCHDOG_DETECTOR_DEGRADED`
   flag the supervisor must carry. A reviewer may reasonably prefer P1's uniform
   one-detector model over P4's non-uniform two-then-one.
5. **The `CLOEXEC` finding suggests more of its kind.** I found the
   `POSIX_SPAWN_DUP2` leak only by tracing P4; the same class of omission may
   exist in the carried PCS→controller and PCS→worker spawns, which I have
   asserted but not re-derived descriptor by descriptor in this layer.
6. **`§R4.1`'s replacement rests on a kernel truncation-granularity fact.** I
   have made the rule safe in both directions if the fact is wrong, but the
   fact itself is reviewer-verifiable and I did not verify it empirically —
   correctly, since no probe was permitted.
7. **The exhaustiveness argument is two-dimensional and therefore bounded by my
   framing of the two questions.** A reviewer who reframes the space — for
   example by asking whether the supervisor role needs to exist as a separate
   process at all — would find options outside this cell.
8. **I have now shipped three layers whose governance conclusion needed
   correction** (v2.1.10.1 declared `READY` over an unimplementable transport;
   v2.1.10.2 offered a dominated option and asserted a two-module role
   bootstrap). This layer's self-assessment should be weighted accordingly. It
   is why the verdict is a cell completion and not a readiness claim.

---

## V21103.8. Exact next gate, and explicit negative authorization

**Next gate, in order, with nothing skippable:**

1. **Kirill selects exactly one of** `…_P1_FULL_PCS_MEDIATION`,
   `…_P3_DEFER_SUPERVISOR_AUTHORITY`,
   `…_P4_CLEAN_BOOTSTRAP_PARENTED_WATCHDOG`. This layer selects none.
2. A **separate correction** binds the selected option, deletes the unselected
   branches from the operative text, and recomputes every count, table, and
   verifier rule against the single surviving architecture.
3. **Only then** is a fresh independent **X-line** and **Y-line** review of the
   resulting composite requested.
4. `I_ACCEPT_OFFICINA_SUPERVISOR_CONTROL_CHANNEL_AMENDMENT` becomes available
   **only** after both lines confirm the identical bytes of that composite.

**Explicit negative authorization.** This correction authorizes **no**
implementation, code, test, verifier, manifest, allowlist, signature, or
contract edit; no commit; no host change; no process, socket, pipe, FIFO, fork,
exec, or signal; no supervisor, controller, worker, watchdog, adapter, middle
child, grandchild, endpoint, journal instance, spawn record, lease, capability,
operation, capacity artifact, custody disposition, freeze witness, or result
manifest; no T activation; no entropy; no E1/E2/E3 spend; no Q/C work; no world,
learner, candidate, Q attempt, datum, outcome, or Proof; and no claim movement.
It predicts no qualification and no C1–C6 outcome. Every fact it adds is
control-plane, T-development-only, and non-citable.

`successor/officina/runtime/` contains only `T_RUNTIME.lock`;
`successor/officina/runtime_control/` does not exist;
`successor/officina/T_ENVELOPE.json` remains `"activated": false`. **T remains
`NOT_ACTIVATED`; the programme claim remains `OPEN`.**
