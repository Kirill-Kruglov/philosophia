# Officina supervisor and control-channel amendment — v2.1.10.4 P1 binding

Status: `P1_BOUND_CANDIDATE_FOR_FINAL_XY_CONFIRMATION_NOT_AUTHORIZED`.
Layer prefix: **§P1B**.

> ## WHAT THIS LAYER IS
>
> Kirill signed exactly one option of Cell P:
>
> ```text
> P: I_SELECT_SUPERVISOR_PROCESS_AUTHORITY_P1_FULL_PCS_MEDIATION
> ```
>
> — recorded in
> `successor/OFFICINA_SUPERVISOR_PROCESS_AUTHORITY_SELECTION_V1_SIGNATURE.md`,
> digest `6ef98132…`, whose three governing hashes all reproduce byte-for-byte
> against this repository.
>
> **This layer binds that selection into one operative architecture.** It is not
> a choice, not a review, and not a self-assessment of the chain's earlier work.
> **No operative P3 or P4 branch survives**: every unselected token, conditional
> count, conditional tree, conditional verifier rule, conditional test, and every
> phrase of the form "under P4" is deleted from the operative contract. P2, P3
> and P4 appear only in the provenance/rejection table of §P1B.0.2 and nowhere
> else.
>
> **The three engineering corrections v2.1.10.3 found while tracing P4 are
> carried, because they are P1-applicable**: the role bootstrap imports
> `{os, sys, fcntl}` (three, never two); `generic_harness.py` must have
> `_socket` in its scoped allowlist because it is the supervisor-side
> `t-pcs.v1` client; and the global `/proc/self/fd` remediation sweep is
> **deleted as unsafe**, because the supervisor's legitimate descriptor set
> grows with every live role handle.
>
> **One statement of v2.1.10.3 is corrected here**: it said an installed but
> unparsed `SCM_RIGHTS` descriptor would be "a resource fact, not an authority
> fact". **That is false — an installed `SCM_RIGHTS` descriptor is a
> capability.** §P1B.6 replaces it with a rule grounded in the pinned kernel
> interface, plus a fail-closed `_exit` for the one interval the interface
> cannot cover, named honestly as a possible transient **capability leak**.

**Authorship.** Written by **Claude Code Opus 5 acting only as the specification
author**. This line wrote v2.1 through v2.1.10.3 and **cannot** serve as the
independent X or Y line for its own bytes, exactly as
`reviews/officina_supervisor_v2_1_authorship_note.md` records. **Every prior
author closure in this chain is an untrusted self-assessment and none is used as
evidence here.** The governing inputs are the signed selection and the operative
bytes of the carried chain.

**Signed cells.** A3, B1, C1, D1, K1 are carried; §P1B.13 states exactly what
P1 does and does not change in each, without softening. Cell P is now **signed**
and closed; this layer proposes **no** new author choice.

```text
A: I_SELECT_SUPERVISOR_CONFINEMENT_A3_SAME_UID_PROCEDURAL_RESCOPE
B: I_SELECT_SUPERVISOR_IDEMPOTENCY_B1_DURABLE_JOURNAL_ACK_REDELIVERY
C: I_SELECT_SUPERVISOR_WATCHDOG_C1_DEDICATED_FREEZER
D: I_SELECT_SUPERVISOR_LIFETIME_D1_NO_IDLE_EXIT
K: I_SELECT_SUPERVISOR_OUTPUT_CAPACITY_K1_SUPERVISOR_MEDIATED_TRANSPORT_FIXED_CEILING
P: I_SELECT_SUPERVISOR_PROCESS_AUTHORITY_P1_FULL_PCS_MEDIATION
```

`I_ACCEPT_OFFICINA_SUPERVISOR_CONTROL_CHANNEL_AMENDMENT` remains **not
signable**. Creates nothing executable. Edits no existing file, code, test,
verifier, manifest, signature, prompt, prior review, or runtime artifact. Starts
no process, socket, pipe, fork, exec, or signal. Creates no entropy, activation,
capability, world, learner, candidate, datum, Q/C object, capacity artifact,
custody disposition, result manifest, or outcome. T remains `NOT_ACTIVATED`; the
programme claim remains `OPEN`.

## Governing hashes (recomputed for this binding)

```text
6ef98132990f8c686fa9678509bb07ba8259f3d6e4cbc483861edfc03ea8e3ef  successor/OFFICINA_SUPERVISOR_PROCESS_AUTHORITY_SELECTION_V1_SIGNATURE.md
02d862e76f76a57cd154ecfd8a67f88abb02c2ce324e4026e4145069cee63143  successor/OFFICINA_GENERIC_HARNESS_SUPERVISOR_CONTROL_CHANNEL_V2_1_10_3_CORRECTION.md
d46414389187bb87068e5105a0a914a56f5f49f1244bdb5b527ccea89acba18c  reviews/opus5_officina_supervisor_control_channel_v2_1_10_3_closure.md
0b9b67f7d57892012df3ad44e6f943a8c8ccf0eb8ed71d966d88b694b8ca5163  reviews/opus5_officina_supervisor_control_channel_v2_1_10_3_cell_p_completion_chat_response.md
c7ff27775fd1b394b850be1be3e1d361d95f5e12af251949f8363980bd2900ec  successor/OFFICINA_GENERIC_HARNESS_SUPERVISOR_CONTROL_CHANNEL_V2_1_10_2_CORRECTION.md
0016452d3033146976b9dc779455f448c9fd690302ff4879d0d2b949e0fd429a  reviews/opus5_officina_supervisor_control_channel_v2_1_10_2_closure.md
2d4d4b189e460605ce95f8f464d7ef1c6d0c8ce317ad26033a91b4d2c556759b  successor/OFFICINA_GENERIC_HARNESS_SUPERVISOR_CONTROL_CHANNEL_V2_1_10_1_CORRECTION.md
f7a866f9100cae1abf80623cd6a7d689cbdca1001fb33dffe98966a727582008  reviews/opus5_officina_supervisor_control_channel_v2_1_10_1_closure.md
2b4f9cad7be7a69527e828c73928a399209fcd8151780b9b4c839934893e0dc8  successor/OFFICINA_GENERIC_HARNESS_SUPERVISOR_CONTROL_CHANNEL_V2_1_10_CORRECTION.md
4cc19fc914f5908f069cb7b8aa09297dece424943f8a876974105e575d09c47d  reviews/opus5_officina_supervisor_control_channel_v2_1_10_closure.md
1468c9ab1806c1eb25523e6a9fd8567592076f0dc74418ca698a52f933c7f3b0  successor/OFFICINA_GENERIC_HARNESS_SUPERVISOR_CONTROL_CHANNEL_V2_1_9_CORRECTION.md
f49dcbf9900c0d3fe2e45abbc28193d8b4b4c20c8640dfab508aff15dcc90984  reviews/opus_officina_supervisor_control_channel_v2_1_9_final_confirmation.md
1970986325c75e8f4c2dd72e57e0640ae88b165f3556920e85cae7efc8cc93be  reviews/sol_officina_supervisor_control_channel_v2_1_9_final_confirmation.md
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

`verification.py` is unamended. `scripts/officina_process_control_bootstrap.py`
and `scripts/officina_role_bootstrap.py` do not exist. This layer creates none
of them.

---

## §P1B.0. Replacement index and provenance

### §P1B.0.1 Literal replacement over v2.1.10.3 and earlier

**Everything not named carries verbatim**, including v2.1.10.2 §T1 (except
§T1.6 step 2), §T2, §T3, §T4, §T5, §T6; v2.1.10.1 §V21101.1–§V21101.6;
v2.1.10 §V2110.2–§V2110.6; and the whole carried
§V219/§V218/§V217/§V216/§V215/§V214/§U/§N/§Z/§W/§V2 chain.

| # | Locus, quoted | Action in v2.1.10.4 |
|---|---|---|
| 1 | v2.1.10.3 §R5.3's three-token block and §R5.1's option definitions | **deleted**. Cell P is signed; §P1B.1 is the single operative architecture |
| 2 | v2.1.10.3 §R1 in full (the P4 trace `A-8a`…`A-8h`), §R2.1's `SPAWN_REPLACEMENT_WATCHDOG` rename, §R2.3's `WATCHDOG_REPLACEMENT` handle role, §R2.4's P4 rows, §R2.5's P4 EOF route, §R5.2, §R5.4 | **deleted as operative text.** They described the unselected P4. Retained only as history in §P1B.0.2 |
| 3 | v2.1.10.3 §R2.1's sentence "the operation survives, renamed and re-preconditioned" and every "first-versus-replacement" asymmetry statement | **deleted.** Under P1 the opcode is `SPAWN_WATCHDOG` with **uniform** semantics for the first watchdog and every replacement (§P1B.5.2) |
| 4 | v2.1.10.3 §R4.1's clause "If it installed MORE than reported, the unreported ones leak — **a resource fact, not an authority fact**" | **replaced** by §P1B.6 — an installed `SCM_RIGHTS` descriptor is a **capability** |
| 5 | v2.1.10.2 §T1.6 remediation step 2 ("scan `/proc/self/fd` and close every descriptor outside this process's pinned set") | **deleted as unsafe** (carried from v2.1.10.3 §R4.1); replaced by §P1B.6 |
| 6 | v2.1.10.2 §T3.2's "imports : exactly `os` and `sys`", §T5.1's "exactly two: `{os, sys}`", §T5.4's map entry `role_bootstrap → {os, sys}`, and rule `S-1'`'s "the role root exactly two" | **replaced** by `{os, sys, fcntl}`, three (§P1B.10.2) |
| 7 | v2.1.10.2 §T5.4's `generic_harness` scoped set "containing neither `signal` nor `_signal` nor `_socket` nor `sys`" | **replaced** by §P1B.10.3 — it gains `_socket` and still excludes `signal`, `_signal`, `sys` |
| 8 | v2.1.10.2 §T7 in full (the governance finding and the cell) | **discharged**: the cell is signed. §P1B.13 states the bound consequences |
| 9 | v2.1.10.3 §R6 test rows 405–436 (P4-specific) | **replaced** by §P1B.14's rows 437–486 |
| 10 | v2.1.10.2 §T8 rows 354, 356, 362, 381 | **replaced** by §P1B.14 |
| 11 | v2.1.10.2 §T4.2's PCS-to-role descriptor statement, insofar as it did not enumerate the `POSIX_SPAWN_DUP2` non-`CLOEXEC` consequence for PCS-created roles | **replaced** by §P1B.3.3's leak proof |
| 12 | carried v2.1 §W3.5 row "Supervisor death \| watchdog's `getppid()` ≠ recorded, **or** update pipe EOF" | **replaced** by §P1B.7.2 — under P1 the `getppid()` conjunct is **deliberately absent** and the watchdog must **ignore** `getppid()` for supervisor-death purposes |
| 13 | carried v2.1 §W3.5 row "Watchdog exits / identity mismatch \| **`waitpid` on own child**, or parent-check failure" | **replaced** by §P1B.7.3 — the supervisor observes watchdog death through `REAP_ROLE` and the carried ack-absence rule; it performs no `waitpid` |
| 14 | carried v2.1 §W3.5 row "Ack absent … \| … **forks a new watchdog** …" | **replaced** by §P1B.7.4 — replacement is `SPAWN_WATCHDOG`, uniform with the first |
| 15 | carried v2.1 §W2.1's watchdog bullet ("the supervisor calls `os.fork()`; the child calls the watchdog function in-process") | **replaced** by §P1B.7.1 — the watchdog is a PCS-created isolated `execve`'d role |
| 16 | carried v2.1.3 §U2.6 row "grandchild first-ack wait expires \| … kill the watchdog by `WATCHDOG_CHILD.json` …" | **replaced** by §P1B.7.5 — the supervisor never signals a watchdog PID; the route becomes a PCS `SIGNAL_ROLE` + `REAP_ROLE` pair |

### §P1B.0.2 Provenance and rejection (history only; no operative force)

| Option | Status | Recorded reason (from the signature, not re-argued here) |
|---|---|---|
| **P1** | **SELECTED** | full PCS mediation |
| P2 | withdrawn before selection | dominated by P4 on address space, creation-time state, lock inheritance and kill authority (v2.1.10.3 §R5.2) |
| P3 | rejected | "leaves contaminated-supervisor process authority as an open Major defect" |
| P4 | not selected | "its hybrid authority model retains `waitpid` in the supervisor, cannot safely signal a wedged watchdog, and degrades replacement watchdogs to the same one-detector model as P1 while carrying additional first-versus-replacement asymmetry" |

**No sentence anywhere else in this document, and no future operative text, may
condition behaviour on P2, P3 or P4.**

---

## §P1B.1. The one operative architecture

> 1. **One clean, constructed Process-Control Server (PCS) holds every PID in
>    the system and all process-control authority** — for `pid_mid`, for every
>    controller, for every worker, for the first watchdog, and for every
>    replacement watchdog. It is the sole caller of `fork`, `posix_spawn`,
>    `kill`, `killpg` and every `wait`-family primitive.
> 2. **The supervisor holds opaque handles only.** `t-pcs.v1` has no PID field,
>    so the supervisor cannot express a PID, and it calls `fork`, `Popen`,
>    `waitpid`, `kill` and `killpg` on no path whatsoever.
> 3. **Every watchdog is a PCS-created isolated role and a direct child of the
>    PCS**, uniform for the first and every replacement.
> 4. **Supervisor death is detected by watchdog update-pipe EOF.** The
>    direct-parent `getppid()` detector is **deliberately absent**, and the
>    watchdog **must not** use `getppid()` to infer supervisor death.
> 5. **Watchdog death and replacement are observed and mediated through the
>    PCS.**
> 6. **PCS loss is an unrecoverable whole-generation process invalidity.** No
>    live-generation adoption exists; a new PCS that finds a non-terminal
>    generation refuses and exits.
> 7. **The second `t-pcs.v1` control-plane journal, and the non-redelivery of
>    descriptor capabilities, are accepted costs** — stated in §P1B.13, never
>    silently repaired.

---

## §P1B.2. Process tree and direct-parent/reaper table

```text
[0] contaminated caller — generic_harness.py __main__, any runtime state
     │ os.posix_spawn (v2.1.10.1 §V21101.3, carried verbatim)
     ▼
[1] PCS — scripts/officina_process_control_bootstrap.py, -I -S -E -P, env {}
     │   sole holder of every PID; owns SPAWN.lock, the four singleton records,
     │   the four bootstrap channels, the supervisor socket, the handle table,
     │   and the t-pcs.v1 journal
     ├─ c4 fork ──▶ [2] middle child (pid_mid)
     │                  └─ m7 fork ─▶ [3] grandchild ─ execve ─▶
     │                                    [3'] role bootstrap (SUPERVISOR)
     │                  └─ m9 _exit ; [3'] re-parented to init
     ├─ posix_spawn ─▶ [4] role bootstrap (WATCHDOG)          setsid = False
     ├─ posix_spawn ─▶ [5] role bootstrap (CONTROLLER) × n    setsid = True
     └─ posix_spawn ─▶ [6] role bootstrap (WORKER) × n        setsid = True
```

| Edge | Creator | Direct child of | May `wait` on it | May signal it |
|---|---|---|---|---|
| [0]→[1] | `posix_spawn` in the caller | [0] | **[0] only**; result irrelevant, the reply pipe is authoritative | **nobody** — the caller is forbidden to signal it (carried §V2110.2.4) |
| [1]→[2] | `os.fork` at `c4` in the PCS | **[1] only** | **[1] only** | **[1] only**, ownership-gated |
| [2]→[3] | `os.fork` at `m7` | [2] until `m9`, then `init` | `init` | the carried stage-2 routes, issued by [1] |
| [1]→[4] | `posix_spawn` in the PCS | **[1] only** | **[1] only** | **[1] only** |
| [1]→[5], [1]→[6] | `posix_spawn(setsid=True)` in the PCS | **[1] only** | **[1] only** | **[1] only** |

**The supervisor [3'] is the direct parent of nothing and the reaper of
nothing.** A wildcard wait in its contaminated interpreter ranges over its own
children, which is the **empty set**. This is the carried process-boundary proof
(v2.1.10 §V2110.2.3) applied uniformly to every process in the tree, and it is
the property P1 buys.

`setsid=False` for the watchdog: it must not be a session leader and is never a
`killpg` target, preserving the carried §U2.5 tier discipline under which
`killpg` is permitted only against a kernel-verified controller/worker group.

---

## §P1B.3. Descriptors

### §P1B.3.1 PCS-side

| Constant | # | Contents | `CLOEXEC`? | Closed when |
|---|---|---|---|---|
| `T_PCB_FD_REQUEST_R` | 3 | caller request read | **no** (arrived by `POSIX_SPAWN_DUP2`) | after the `SPAWN_SUPERVISOR` reply is written |
| `T_PCB_FD_REPLY_W` | 4 | caller reply write | **no** | same |
| `T_PCB_FD_RUNTIME_ROOT` | 5 | runtime root directory | **no** | PCS exit |
| `T_PCB_FD_PACKAGE_ROOT` | 6 | package root directory | **no** | PCS exit |
| `T_PCB_FD_SOURCE` | 7 | the PCS's own source object | **no** | PCS exit |
| `T_PCB_FD_INTERPRETER` | 8 | the interpreter object | **no** | PCS exit |
| `sv_sock` | kernel-chosen | supervisor `SOCK_SEQPACKET` PCS end | **yes** | `SHUTDOWN` or PCS exit |
| `journal_fd` | kernel-chosen | the `t-pcs.v1` journal, `O_CLOEXEC` | **yes** | PCS exit |
| per handle | kernel-chosen | the **role-side** ends the PCS retains | **yes** | when the handle reaches `REAPED` |
| opened under fd 6 | kernel-chosen | role-bootstrap source, `generic_harness.py` source, `src` directory — all `O_RDONLY\|O_NOFOLLOW\|O_CLOEXEC` | **yes** | PCS exit |

### §P1B.3.2 Role-side maps, per role class

| Slot | `SUPERVISOR` | `WATCHDOG` | `CONTROLLER` / `WORKER` |
|---|---|---|---|
| 3 | `SPAWN.lock` (retained, non-`CLOEXEC`, carried §W2.2) | watchdog update **read** | ctrl request read (`T_CTRL_FD_LOW`, carried §Z3.3) |
| 4 | `boot` write end | watchdog ack **write** | ctrl reply write (`T_CTRL_FD_HIGH`, carried §Z3.3) |
| 5 | `T_ROLE_FD_ROLESRC` — the `generic_harness.py` source object | same | same |
| 6 | `T_ROLE_FD_PCS` — the `SOCK_SEQPACKET` peer | **unused; explicitly closed** | status write end |
| 7 | `T_ROLE_FD_SELF` — the role-bootstrap source object | same | same |
| 8 | `T_ROLE_FD_SRCDIR` — the object-bound `src` directory | same | same |
| 9 | `T_ROLE_FD_INTERP` — the interpreter object | same | same |
| 10 | `T_ROLE_FD_PKGROOT` — the package root directory | same | same |

Post-`exec` the role's `/proc/self/fd` is exactly `{0,1,2}` ∪ its slot set, and
step `A-5` of the carried role-bootstrap refusal order verifies it.

**Descriptors the supervisor receives over `SCM_RIGHTS` are not in any pinned
numeric set.** They arrive at kernel-chosen numbers with `FD_CLOEXEC` already
set by `MSG_CMSG_CLOEXEC`, and the supervisor records them in its handle→fd
table. **This is exactly why a `/proc/self/fd` sweep is unsafe** (§P1B.6).

### §P1B.3.3 The `POSIX_SPAWN_DUP2` leak proof, per role spawn

> **The fact.** `POSIX_SPAWN_DUP2` has `dup2(2)` semantics and therefore
> **clears `FD_CLOEXEC` on the destination**. Every destination in a role's map
> is inheritable across the `execve`; every other descriptor of the PCS is
> either closed by the `execve` (because it is `CLOEXEC`) or must be closed
> explicitly.

**Claim.** After a role `execve`, the role's descriptor set is exactly
`{0,1,2}` ∪ (its slot set), and **no** `SPAWN.lock`, supervisor socket,
journal, unrelated-role, source, interpreter, or package-root descriptor of the
PCS leaks into it.

**Proof.**

1. **Every PCS descriptor other than 3–8 is `CLOEXEC` by construction**:
   `sv_sock` from `_socketpair` (CPython creates sockets non-inheritable);
   every channel from `_pipe2(_O_CLOEXEC)`; the journal and every fd opened
   under fd 6 from `_open(..., _O_CLOEXEC)`; and every hoist duplicate from
   `_dup`, which returns a **non-inheritable** descriptor. Each is therefore
   closed by the `execve`.
2. **Descriptors 3–8 are non-`CLOEXEC`** and are the only ones that could leak.
   All six are `≤ 8`, hence `≤ 10`, hence inside the destination range of every
   role map.
3. The `file_actions` sequence performs a `DUP2` onto **every** slot the role
   uses. A `DUP2` onto a number **closes whatever that number held**, so each of
   3–8 is either overwritten by a slot or explicitly closed.
4. The one slot no role uses is `6` for the `WATCHDOG`, which held the PCS's
   package-root descriptor. The watchdog's `file_actions` therefore contain an
   explicit `(POSIX_SPAWN_CLOSE, 6)`. **Without it the watchdog would inherit
   the PCS's package-root directory descriptor**, which `A-5` would then reject
   — so the omission would be fail-closed rather than silent, but it is closed
   explicitly so the map is exact.
5. **`SPAWN.lock` specifically.** The PCS holds it on a descriptor that is
   deliberately **not** `CLOEXEC`, because the supervisor grandchild must retain
   it across its `execve` (carried §W2.2, whose justifying parenthetical
   v2.1.10 §V2110.9 row 24 already replaced). It is therefore the one descriptor
   that could survive a role `execve` by inheritance. It reaches the
   **`SUPERVISOR`** role only, at slot 3, where the map places it deliberately.
   For **controller, worker and watchdog** spawns it is **not** in the map, so
   it is closed by whichever `DUP2` targets its number (step 3) — and if its
   number were ever outside the destination range, the receiving role's `A-5`
   `/proc/self/fd` check would refuse, so the failure mode is fail-closed
   rather than silent. **No role other than the supervisor ever holds a
   `SPAWN.lock` reference.** ∎

**File actions, per role spawn, in exactly this order** (the generalized hoist
of v2.1.10.2 §T6.1, target set = the role's slot set):

```text
  HOIST every logical source above max(slot set)      ⇒ all sources ≥ 11
  (DUP2, h[slot_3],  3) … (DUP2, h[slot_10], 10)      in ascending slot order
  (CLOSE, h[slot_3]) … (CLOSE, h[slot_10])            same order
  (CLOSE, <every destination number the role does NOT use>)
        — for WATCHDOG this is exactly {6}; for the other roles it is empty
```

Collision-freedom: every source is `> 10` and every destination is `≤ 10`, so
no `DUP2` destination can overwrite a source a later action still needs; all
`CLOSE`s follow all `DUP2`s.

---

## §P1B.4. The handle model

```text
handle_id → { pid, start_identity, pgid_or_null, role, generation_id,
              fd_bundle (the PCS-side role ends), state, ownership, fd_delivery }
  role       ∈ CONTROLLER | WORKER | WATCHDOG
  state      ∈ SPAWNED | STOPPED | RUNNING | REAPED
  ownership  ∈ OWNED | CONTRADICTED | REAPED        (carried §V218.3.1)
  fd_delivery∈ PENDING | CONFIRMED | UNCONFIRMED
```

Invariants, each carrying a signed rule forward:

1. handle ids are never reused, within or across generations;
2. `SIGNAL_ROLE` and `SIGNAL_GROUP` require `ownership == OWNED` — the carried
   single-`os.kill` precondition, enforced where the PID actually lives;
3. `SIGNAL_GROUP` additionally requires a **kernel-verified** group — the
   carried §U2.5 tier rule, unchanged;
4. `SIGNAL_ROLE` is **refused for `role == WATCHDOG`**: a watchdog is
   terminated by closing its update pipe and is never signalled (§P1B.7.5);
5. `RELEASE_HANDLE` requires `state == REAPED`;
6. no wait site runs after `ownership == REAPED`;
7. every PCS-created process is a direct child of the PCS, so the
   process-boundary proof extends to all of them verbatim.

---

## §P1B.5. `t-pcs.v1`

### §P1B.5.1 Channels

| Channel | Endpoints | Kind | Protocol | Operations |
|---|---|---|---|---|
| caller | caller ↔ PCS | two anonymous pipes, fds 3 and 4 | the carried six-field request / five-field reply (v2.1.10 §V2110.2.5) | exactly one: `SPAWN_SUPERVISOR` |
| supervisor | supervisor ↔ PCS | one `AF_UNIX` `SOCK_SEQPACKET` pair, protocol `0` | `philosophia.officina.t-pcs.v1` | the nine below |

### §P1B.5.2 The nine operations — uniform, no watchdog asymmetry

| Opcode | Request operands | Preconditions | Response operands | fds |
|---|---|---|---|---|
| `SPAWN_ROLE` | `role` ∈ {`CONTROLLER`,`WORKER`}; `argv_template_id` (64 hex); `spawn_intent_id` (64 hex) | the signed `t-spawn-intent.v1` record exists and its `argv_template_sha256` matches; generation `LIVE` | `handle_id` | **3** |
| `AWAIT_STOP` | `handle_id`; `deadline_ticks` | state `SPAWNED` | `outcome` ∈ {`STOPPED`,`EXITED`,`TIMEOUT`}; `start_identity`; `pgid_is_leader` | 0 |
| `SIGNAL_ROLE` | `handle_id`; `sig` ∈ {`CONT`,`TERM`,`KILL`,`STOP`,`PROBE`} | `ownership == OWNED`; **`role != WATCHDOG`** | `result` ∈ {`SENT`,`GONE`,`DENIED`,`STRUCTURAL_VIOLATION`} | 0 |
| `SIGNAL_GROUP` | `handle_id`; `sig` | a kernel-verified group is recorded; `role != WATCHDOG` | as above | 0 |
| `REAP_ROLE` | `handle_id` | `ownership != REAPED` | the carried six-result `WAIT_ONE` token | 0 |
| **`SPAWN_WATCHDOG`** | — | no live watchdog handle exists in this generation | `handle_id` | **2** |
| `RELEASE_HANDLE` | `handle_id` | `state == REAPED` | — | 0 |
| `SHUTDOWN` | — | no handle is live | — | 0 |
| `PING` | — | — | `pcs_uptime_ticks` | 0 |

**`SPAWN_WATCHDOG` has one meaning.** Its precondition is the *absence of a live
watchdog handle*, which is satisfied both at generation start and after a
previous watchdog's death has been proved. **The first watchdog and every
replacement are created by the same operation with the same semantics and the
same one-detector process model.** No `SPAWN_REPLACEMENT_WATCHDOG` opcode
exists; no `WATCHDOG_REPLACEMENT` handle role exists; no
`WATCHDOG_DETECTOR_DEGRADED` flag exists.

Record grammar, correlation, single-outstanding-request rule, and the
impossibility of partial records are carried verbatim from v2.1.10.2 §T2.2,
§T2.4 and §T2.5. **No field carries a PID, a descriptor number, a path, argv, a
signal number, a symbol, a callback, or an unbounded integer.**

### §P1B.5.3 Ancillary descriptor vectors — the only legal ones

| Operation / status | fds | vector, in order |
|---|---|---|
| every request | 0 | — |
| `SPAWN_ROLE` ok | 3 | ctrl request write, ctrl reply read, status read — all `S_ISFIFO` |
| `SPAWN_WATCHDOG` ok | 2 | update write, ack read — both `S_ISFIFO` |
| every refusal and every other operation/status | 0 | — |

Maximum descriptors per message: **3**. Ancillary buffer: `CMSG_SPACE(12)`.
`MSG_CMSG_CLOEXEC` is mandatory on every `recvmsg`.

### §P1B.5.4 Journal and ACK automaton

```text
J1. receive and validate the request
      crash ⇒ nothing happened; a redelivery is a fresh request
J2. append { generation_id, request_id, opcode, operands, state: ACCEPTED }
    and fsync
      crash ⇒ ACCEPTED with no result ⇒ the operation is INCONCLUSIVE, and
              because no PCS may adopt a live generation (§P1B.8.2) this is a
              whole-generation invalidity, never a silent retry
J3. perform the syscall
      crash ⇒ as J2, plus a possibly-live orphan role, routed by §P1B.8.2
J4. append { …, state: COMPLETED, outcome, handle_id, fd_vector_len } and fsync
      crash ⇒ the result is durable; a redelivery replays it
J5. send the response, with descriptors iff §P1B.5.3 says so
      crash ⇒ durable but undelivered; a redelivery replays it WITHOUT
              descriptors
J6. on ACK append { …, state: ACKED } and fsync

REPLAY of an already-journalled (generation_id, request_id):
  ACCEPTED  ⇒ INVALID / OPERATION_INCONCLUSIVE; no syscall is ever re-performed
  COMPLETED ⇒ the recorded status/detail/handle, status := REPLAYED,
              fds_redelivered := 0, and NO descriptors
  ACKED     ⇒ identical to COMPLETED
```

**Descriptors are never re-sent.** A supervisor that loses the descriptors of a
`SPAWN_ROLE` or `SPAWN_WATCHDOG` response cannot recover them; the handle is
marked `FD_DELIVERY_UNCONFIRMED` and the generation routes to §P1B.8.4. This is
the accepted B1 narrowing (§P1B.13).

---

## §P1B.6. `SCM_RIGHTS` receive-side cleanup — the bound rule

### §P1B.6.1 The statement being corrected

> **Deleted:** v2.1.10.3 §R4.1's clause "If it installed MORE than reported, the
> unreported ones leak — **a resource fact, not an authority fact**".
> **That classification is false.** An installed `SCM_RIGHTS` descriptor is a
> **capability**: it is an open file description in this process's table,
> usable by any code that runs afterwards, and the fact that the generation is
> already invalid does not demote it.
>
> **Also deleted (carried from v2.1.10.3 §R4.1):** v2.1.10.2 §T1.6's remediation
> step 2, the global `/proc/self/fd` sweep. The supervisor's legitimate
> descriptor set **grows with every live role handle** and its members are at
> kernel-chosen numbers, so a sweep against a "pinned set" would close the ctrl
> and status channels of unrelated live roles. **No global sweep, proxy, or
> capability-recovery protocol is introduced in its place.**

### §P1B.6.2 The pinned primary interface fact

> **Linux, `net/core/scm.c`, `scm_detach_fds()`.** When a `recvmsg` control
> buffer is too small for all queued `SCM_RIGHTS` descriptors, the kernel
> computes `fdmax = min(space_available_in_control_buffer / sizeof(int),
> queued_count)`, **installs exactly those `fdmax` descriptors** into the
> receiving process's descriptor table, writes their numbers into the returned
> control data, sets the returned `cmsg_len` to `CMSG_LEN(i * sizeof(int))` for
> the number `i` actually installed, sets `MSG_CTRUNC`, and then **releases
> every queued descriptor it did not install** through the ordinary file-put
> path when the `scm_cookie` is destroyed.
>
> **Consequence, and the ground of the rule below: on a conforming Linux kernel
> every descriptor that is installed is reported in the returned control data,
> and every descriptor that is not reported is closed by the kernel. An
> installed-but-unreported descriptor cannot exist.**
>
> **This is the reviewer-verifiable primary interface fact of this section.**
> It rests on `scm_detach_fds()` and its callers, and both independent lines are
> asked to verify it against the kernel source rather than accept it here
> (§P1B.17, X-Q2 and Y-Q2).

### §P1B.6.3 The operative rule

```text
RECEIVE_AND_VALIDATE(sock, expected_vector_for_this_opcode):

 B-1. r := _recvmsg(sock, T_CONTROL_FRAME_MAX_BYTES, _CMSG_SPACE(12),
                    _MSG_CMSG_CLOEXEC)

      IF B-1 RAISES ANY BaseException:
        the receiver cannot enumerate what, if anything, the kernel installed,
        because the association between the kernel's control data and this
        process was lost inside the call. It therefore performs, as its VERY
        NEXT operation and with no intervening statement:

              _exit_(T_PCS_EXIT_RECV_UNENUMERABLE)

        an immediate process exit with NO callback, NO finalizer, NO atexit
        handler, NO buffer flush, and NO unwinding. The kernel then closes every
        descriptor this process holds, including any that were installed.
        THE INTERVAL between a possible installation inside _recvmsg and this
        _exit_ is named HONESTLY in §P1B.6.5 as a possible transient CAPABILITY
        LEAK. It is not called a resource fact.

 B-2. parse the returned control items. For each item:
        (level, type) != (_SOL_SOCKET, _SCM_RIGHTS)  ⇒ ANCILLARY_VIOLATION,
              and the item contributes no descriptor
        otherwise: n := len(cdata) - (len(cdata) % 4)
                   received += [ int.from_bytes(cdata[i:i+4], "little")
                                 for i in range(0, n, 4) ]
      `received` is now, by §P1B.6.2, EXACTLY the set the kernel installed for
      this message.

 B-3. require (flags & _MSG_CTRUNC) == 0 and (flags & _MSG_TRUNC) == 0
      require len(received) == the expected count for this opcode and status
      require every element's _fstat type equals the expected slot type
        any failure ⇒ ANCILLARY_VIOLATION

 B-4. ON ANY VIOLATION IN B-2 OR B-3:
        close EXACTLY the descriptors in `received`, de-duplicated by numeric
        value, in ascending numeric order, once each, with _close, tolerating
        EBADF. Close NOTHING ELSE. Do not enumerate /proc/self/fd. Do not touch
        any descriptor of any other message or any live role handle.
      then route to §P1B.8.4's invalidity path.

 B-5. ON SUCCESS: the descriptors in `received` become the handle's fd bundle;
      they already carry FD_CLOEXEC, set atomically with installation by
      MSG_CMSG_CLOEXEC.
```

`T_PCS_EXIT_RECV_UNENUMERABLE` is an **exit status token**, not a resource
value, a timeout, or a scientific quantity.

### §P1B.6.4 Why each required property holds

| Required property | How |
|---|---|
| every descriptor actually returned is closed exactly once | `B-4` de-duplicates by numeric value and closes in ascending order, tolerating `EBADF` |
| unrelated previously received role descriptors are never closed | `B-4` closes only `received`, which is this message's vector; live handles' bundles are not enumerated, not scanned, and not touched |
| the unenumerable case is fail-closed | `B-1`'s `_exit_` with no callback of any kind |
| `MSG_CMSG_CLOEXEC`, `MSG_CTRUNC`, `MSG_TRUNC`, fd-count and fd-type validation preserved | `B-1`, `B-3` |
| no-redelivery preserved | §P1B.5.4; `B-4` never requests a re-send |
| no global sweep, proxy, or recovery protocol | none is specified anywhere |

### §P1B.6.5 The named residual, and its A3 boundary

> **Possible transient capability leak.** If `_recvmsg` raises after the kernel
> has installed descriptors — which requires a failure inside the interpreter's
> own post-`recvmsg` handling, since §P1B.6.2 shows the kernel itself never
> installs without reporting — those descriptors exist in this process's table
> and are reachable by any code that executes before the `_exit_`. The interval
> is bounded to the instructions between the raise and the `_exit_`, and is
> terminated with certainty by the kernel's closure of the process's descriptor
> table at exit.
>
> **This is a capability leak for that interval, not a resource fact**, and it
> is recorded as such.
>
> **A3 boundary.** Concurrent same-UID code that could act inside that interval
> is exactly the threat the signed **A3 same-UID procedural rescope** covers.
> A3 is a **procedural** residual: it is permanently non-citable, forbidden from
> selection, Q, C, C1–C6, any blinding claim, and any scientific or resource
> interpretation. **Nothing here upgrades A3 into a security guarantee, and this
> contract asserts no same-UID confinement mechanism.** The leak is named,
> bounded, and left where A3 already puts it.

---

## §P1B.7. The watchdog under P1

### §P1B.7.1 Creation

The watchdog is created **only** by the PCS, through `SPAWN_WATCHDOG`, as an
isolated role: object-bound interpreter and role-bootstrap source
(`/proc/self/fd/9`, `/proc/self/fd/7`), `-I -S -E -P`, empty environment,
`setsid=False`, the `WATCHDOG` slot map of §P1B.3.2, and the file actions of
§P1B.3.3 including the explicit `(CLOSE, 6)`.

Carried §W2.1's justification that the watchdog is forked "before any
`RealTCapability` exists, so the inherited address space contains no
capability" is **replaced by a stronger construction**: an `execve`'d watchdog
has a fresh address space and therefore contains no capability **by
construction**. Every other C1 property — witness/freezer role, holds no lock
and no capability, writes nothing under `runtime/`, appends no ledger, settles
nothing, sealed update/ack pipes only, `WATCHDOG/FREEZE/<witness_id>.json`
observations — is carried byte-for-byte.

### §P1B.7.2 Supervisor-death detection — one mechanism, stated

> **Operative rule.** The watchdog detects supervisor death **only** by
> observing **EOF on its update read end** (slot 3). The supervisor holds the
> only write end; its death, by any cause, closes that end and produces the EOF.
>
> **The watchdog must not use `getppid()` to infer supervisor death, and must
> not treat a `getppid()` change as any signal about the supervisor.** Its
> parent is the PCS, so a `getppid()` change means the **PCS** died — a distinct
> condition handled by §P1B.8.2, in which the supervisor may still be alive.
> Treating it as supervisor death would produce a **false freeze**.
>
> The watchdog continues to verify the supervisor's identity against
> `SUPERVISOR_IDENTITY.json` exactly as carried §W2.1 requires; what is removed
> is the parent-link inference, not the identity check.

### §P1B.7.3 Watchdog-death detection

The supervisor performs **no** `waitpid`. It observes watchdog death by:

1. the carried **ack-absence** rule — no ack for the current `table_seq` past
   `T_WATCHDOG_ACK_ABSENCE_TIMEOUT_NS` (§W3.5, §Z4.3, unchanged); and
2. `REAP_ROLE(watchdog_handle)`, whose carried six-result `WAIT_ONE`
   classification the PCS performs on its own child.

Only `REAPED_POSITIVE` proves death. `CONTRADICTED_ECHILD` and
`STRUCTURAL_VIOLATION` are never death and route to §P1B.8.4.

### §P1B.7.4 Replacement

On proved watchdog death the supervisor takes the carried §W3.5 route —
freeze all live groups itself with `killer = SUPERVISOR` **through
`SIGNAL_GROUP`**, refuse admissions, obtain a new watchdog, await its ack, then
settle every overdue lease per §W3.4 — with one substitution: **"forks a new
watchdog" becomes `SPAWN_WATCHDOG`**. The replacement is created by the same
operation, with the same isolation, the same slot map, and the same
single-detector model as the first. **There is no first-versus-replacement
asymmetry and no degradation flag.**

### §P1B.7.5 Termination — never by signal

> `SIGNAL_ROLE` and `SIGNAL_GROUP` are **refused** for `role == WATCHDOG`
> (§P1B.4 invariant 4). A watchdog is terminated by the supervisor closing its
> update **write** end through `CLOSE_OWNED`; the watchdog observes EOF, writes
> its final observations, and exits; the PCS then reaps it on `REAP_ROLE`.

Carried §U2.6's "kill the watchdog by `WATCHDOG_CHILD.json`, prove death" is
**replaced**: the grandchild's first-ack-timeout route becomes *close the update
write end, then `REAP_ROLE` until `REAPED_POSITIVE`, then remove records per
§U6.3*. If the watchdog does not exit within
`T_WATCHDOG_ACK_ABSENCE_TIMEOUT_NS` after the EOF, the route records
`WATCHDOG_UNREAPED`, refuses every admission, and takes §P1B.8.4. **No signal is
sent to a watchdog on any path.**

---

## §P1B.8. Crash and invalidity

### §P1B.8.1 Supervisor death, PCS alive

The watchdog observes update-pipe EOF, freezes all known groups per §W3.3,
writes their observations, and exits; it settles nothing. The PCS observes
`PEER_EOF` on `t-pcs.v1`, holds every live handle in the carried non-returning
reaper state rather than abandoning any, and does not free the singleton. The
next attempt's §U6.1 P0–P3 preflight governs the records.

### §P1B.8.2 PCS death — unrecoverable, no adoption

```text
On PCS death, at ANY point:
  - the kernel closes every descriptor it held: its SPAWN.lock reference, the
    supervisor socket, the journal, and every role-side end it retained;
  - pid_mid and every role are re-parented to init, which reaps them;
  - the supervisor observes PEER_EOF and has lost ALL process authority: it can
    create, signal, wait for, and reap nothing;
  - the watchdog's getppid() changes — which under §P1B.7.2 means the PCS died
    and is NOT a supervisor-death signal; the watchdog continues until its own
    update-pipe EOF;
  - the journal's last entry may be ACCEPTED, so an operation may or may not
    have happened: that is the inconclusive case;
  - the four singleton records survive under the carried §U6.1 preflight; no
    record naming a possibly-live process is removed without a signed death
    proof.

PROHIBITION: A NEW PCS MUST NEVER ADOPT A LIVE GENERATION. It is not the parent
of any surviving process, so it can neither wait for nor safely signal one. A
PCS that starts and finds a journal whose generation is not terminal MUST
respond GENERATION_NOT_ADOPTABLE, take no action, and exit.

SUPERVISOR CONTINUATION on PEER_EOF:
  1. refuse every admission and every command requiring a role operation;
  2. FREEZE IS UNAVAILABLE — the carried §W3.3 quiescence proof needs
     SIGNAL_GROUP, which is a PCS operation — so no live stream has a valid
     continuation;
  3. close the watchdog update write end; the watchdog writes its observations
     for the groups it knows and exits; init reaps it;
  4. route the generation through §P1B.8.4.
```

### §P1B.8.3 The crash and invalidity matrix

Every carried v2.1.10.2 §T4.8 and v2.1.10 §V2110.7.1 row stands. Bound rows:

| Cut | Single continuation |
|---|---|
| caller crash / stops reading / closes the reply pipe | the reply write yields `EPIPE`; `SIGPIPE` is `SIG_IGN`; it changes **no** record, custody, ownership, or terminal decision |
| a competing waiter in the caller reaps the PCS | the caller loses only an exit status; the pipe reply is authoritative |
| `_recvmsg` raises | `_exit_(T_PCS_EXIT_RECV_UNENUMERABLE)`, no callback (§P1B.6.3 `B-1`) |
| ancillary violation | close exactly the parsed vector; §P1B.8.4 |
| ACK lost | `FD_DELIVERY_UNCONFIRMED`; **no re-send**; §P1B.8.4 |
| replay of `ACCEPTED` | `OPERATION_INCONCLUSIVE`; no syscall |
| replay of `COMPLETED`/`ACKED` | the recorded record, `fds_redelivered = 0`, no descriptors |
| supervisor death | §P1B.8.1 |
| PCS death | §P1B.8.2 |
| watchdog death | §P1B.7.3 → §P1B.7.4 |
| wedged watchdog (no exit after EOF) | `WATCHDOG_UNREAPED`; no signal; §P1B.8.4 |
| controller/worker stop | `AWAIT_STOP`/`REAP_ROLE` see `(0,0)`; the carried TERM→KILL schedule through `SIGNAL_ROLE`; a stopped role holding a fork-shared reference is the carried §U2.7 A3 residual |
| `STRUCTURAL_VIOLATION` at any PCS wait site | carried §V2110.4.1: never death, `CONTRADICTED`, no further signal, no record touched |
| `SHUTDOWN` with a live handle | `REFUSED`/`HANDLES_LIVE`; nothing released |
| role `execve` fails | `os._exit(3)`, nothing written, nothing unlinked; the carried `boot`-EOF route governs |
| role-side `A-1`…`A-13` failure | identical |

### §P1B.8.4 Invalidity routing

```text
An operation whose control outcome cannot be established, or a generation whose
PCS is gone, is a PROCESS fact:
  - it settles through the signed T_PROCESS_INVALID recovery disposition and the
    signed §4c(c)/§4d unknowable route, with invalidity dominance as carried;
  - it is NEVER T_PROCESS_CLOSED, never a completion, never a capacity fact,
    never a custody disposition, never an E1/E2/E3 fact, never a Q/C input;
  - no resource value is inferred from it and no scientific outcome is produced;
  - "its own user" remains withdrawn as a disposition.
```

---

## §P1B.9. Shutdown

```text
S-1. the supervisor stops admitting; drains and settles per carried §W3.4/§4c
S-2. for every live controller/worker handle: SIGNAL_ROLE/SIGNAL_GROUP per the
     carried routes, then REAP_ROLE until REAPED_POSITIVE, then RELEASE_HANDLE
S-3. close the watchdog update write end through CLOSE_OWNED
S-4. the watchdog observes EOF, writes its final observations, os._exit(0)
S-5. REAP_ROLE(watchdog_handle) until:
       REAPED_POSITIVE        ⇒ death proved; RELEASE_HANDLE; go to S-6
       CONTRADICTED_ECHILD    ⇒ death NOT proved ⇒ §P1B.8.4; the supervisor may
                                still proceed, because it removes no record on a
                                false death proof and the watchdog, if alive,
                                exits at its own update-EOF route
       STRUCTURAL_VIOLATION   ⇒ identical to the ECHILD row
       NOT_YET past the bound ⇒ WATCHDOG_UNREAPED ⇒ §P1B.8.4
S-6. SHUTDOWN
       HANDLES_LIVE ⇒ the supervisor must first clear the offending handle
       OK           ⇒ the PCS performs CLOSE_OWNED cleanup, releases SPAWN.lock,
                      and exits
S-7. the supervisor closes its remaining descriptors through CLOSE_OWNED and
     exits.
```

**Watchdog death is observed and reaped before the supervisor exits**, or the
generation is explicitly invalid — there is no third branch.

---

## §P1B.10. Imports and primitives

### §P1B.10.1 PCS root — six modules

`{os, sys, _signal, time, fcntl, _socket}`. Audit carried verbatim from
v2.1.10.2 §T5.1, including the disclosure that `_socket.socket` has a finalizer
which closes its descriptor, and the two pinned rules that contain it: every
socket object lives in a module-level slot for the generation, and **every
received descriptor is handled as a plain `int`**, closed once with `_close`,
never wrapped.

### §P1B.10.2 Role-bootstrap root — three modules

> **`{os, sys, fcntl}` — three, never two.** Carried from v2.1.10.3 §R4.5:
> the role bootstrap's own step `A-6` requires the descriptor to be read-only by
> the `F_GETFL` test, and that test is
> `_fcntl(fd, _F_GETFL) & _O_ACCMODE == _O_RDONLY`. **v2.1.10.2's two-module
> claim was false.** Every count and every verifier rule says **three**.

`fcntl` is a built-in C module with an empty Python import closure; it starts no
task, registers no at-fork callback, and installs no hook.

### §P1B.10.3 `generic_harness.py` — the supervisor-side `t-pcs.v1` client

> Its scoped allowlist is the sixteen signed members **plus `_socket`** —
> seventeen — because the supervisor role is the `t-pcs.v1` client and must
> call `_recvmsg`/`_sendmsg`. It still contains **neither `signal`, nor
> `_signal`, nor `sys`**: the role receives its interpreter, sources,
> directories and channels as descriptors and argv, installs no signal
> disposition, and reads no `sys` attribute for any decision. v2.1.10.2 §T5.4's
> contrary statement is superseded.

### §P1B.10.4 Identity classes

The carried per-primitive identity table (v2.1.10.1 §V21101.1.4) governs, with
the fourth kind added by v2.1.10.2 §T5.2 for `_sendmsg`/`_recvmsg` — method
descriptors whose `__objclass__` is `_socket.socket`. **No universal
builtin-identity predicate is used anywhere**; the chain already refuted it
(it would reject a genuine pure-Python wrapper), and the role bootstrap uses the
same per-primitive table.

### §P1B.10.5 Object binding and isolation, carried

The object-bound `/proc/self/fd/<N>` interpreter and source mechanism, the
`-I -S -E -P` invocation with an exactly empty environment, the deletion of
`PYTHONPATH`, and the role bootstrap's single object-bound `sys.path[:]`
assignment are all carried verbatim from v2.1.10.1 §V21101.2 and v2.1.10.2 §T3.

---

## §P1B.11. Verifier and manifest surface

```text
CHANGE 1  PRODUCTION_ROOTS = (
            "scripts/officina_activate_t.py",
            "scripts/verify_officina_active.py",
            "src/philosophia/officina/generic_harness.py",
            "scripts/officina_process_control_bootstrap.py",
            "scripts/officina_role_bootstrap.py",
          )                                                       # FIVE
CHANGE 2  ALLOWED_ABSOLUTE_IMPORTS gains `sys`, `_signal`, `_socket`.
          It NEVER gains `signal`.
          MODULE_SCOPED_ABSOLUTE_IMPORTS = {
            process_control_bootstrap → {os, sys, _signal, time, fcntl, _socket},
            role_bootstrap            → {os, sys, fcntl},          # THREE
            generic_harness           → the sixteen signed members + {_socket},
                                        and NOT signal, _signal, sys,
          }
          A file with a scoped entry gets EXACTLY that entry, never the union.
CHANGE 3  the closed AST grammar: S-1'…S-17 of v2.1.10.2 §T5.4, with
            S-1'  PCS root exactly six Import nodes; role root exactly THREE
            S-7'  forbidden-symbol list as carried, plus `readlink`, `socket`
                  (the wrapper), `array`, `struct`, `PYTHONPATH`, `putenv`,
                  `SO_PASSCRED`, `SCM_CREDENTIALS`
            S-14  every `_recvmsg` passes `_MSG_CMSG_CLOEXEC`
            S-15  every `_recvmsg` ancillary buffer is exactly `_CMSG_SPACE(12)`
            S-16  no wire field is derived from a descriptor; `fileno`, `detach`
                  and `.fileno()` are forbidden in record builders
            S-17  the role root has exactly one `sys.path` assignment, of the
                  form `sys.path[:] = [<one literal-prefixed /proc/self/fd/ string>]`
            S-18  (new) no `/proc/self/fd` directory enumeration appears anywhere
                  ⇒ "global fd sweep present"
            S-19  (new) the receive path's exception handler's first statement is
                  `_exit_(...)`, with no call between the handler entry and it
                  ⇒ "unenumerable-receive not fail-closed"
CHANGE 4  `generic_harness.py` contains no `import signal` and no `signal.`
          attribute.
CHANGE 5  the manifest gains `root_source_sha256`, a mapping from each of the
          FIVE roots to the SHA-256 of its exact bytes, recomputed and compared;
          a mismatch ⇒ "production root bytes differ".
RUNTIME PREFLIGHT (not statically decidable, bound by construction): P-a
          platform, P-b interpreter identity and the four isolation flags,
          P-c/P-d single task, P-e no inherited children, P-f descriptor
          topology, P-g SigCgt == 0 and the SIGCHLD disposition, P-g0
          SigBlk == 0, P-h request grammar, P-s source/interpreter objects,
          P-p package-root binding, and the §P1B.10.4 identity check.
```

---

## §P1B.12. Operative constants and counts — one table

| Statement | Value |
|---|---|
| production roots | **5** |
| PCS import closure | **6** — `{os, sys, _signal, time, fcntl, _socket}` |
| role-bootstrap import closure | **3** — `{os, sys, fcntl}` |
| `generic_harness.py` scoped set | **17** — the sixteen signed members + `_socket` |
| `t-pcs.v1` operations | **9** |
| max descriptors per `t-pcs.v1` message | **3** |
| ancillary buffer | `CMSG_SPACE(12)` |
| PCS descriptor constants | **6** — `T_PCB_FD_REQUEST_R`…`T_PCB_FD_INTERPRETER`, values 3–8 |
| role descriptor slots | **8** numbers, 3–10; the `WATCHDOG` map uses 7 of them and closes slot 6 |
| role classes | **4** — `SUPERVISOR`, `WATCHDOG`, `CONTROLLER`, `WORKER` |
| private argv tokens | **3** — `--officina-bootstrap` (carried §Z3.3), `--officina-role`, and the carried role operand set |
| supervisor-death detectors | **1** — watchdog update-pipe EOF |
| watchdog-death detectors | **2** — ack absence, and `REAP_ROLE`'s `REAPED_POSITIVE` |
| new numeric resource values, timeouts, K1 ceilings, E1/E2/E3 values, T bands | **0** |
| deadlines used | `T_SUPERVISOR_POLL_INTERVAL_NS`, `T_SPAWN_IDENTITY_WAIT_TIMEOUT_NS`, `T_SPAWN_SELF_STOP_TIMEOUT_NS`, `T_WATCHDOG_ACK_ABSENCE_TIMEOUT_NS`, `T_SPAWN_LOCK_ACQUIRE_TIMEOUT_NS`, `T_SPAWN_BOOTSTRAP_MAX_AGE_NS`, `T_CONTROL_FRAME_MAX_BYTES` — **all already signed** |
| platform | `Linux x86_64`, `CPython 3.12.3` |

---

## §P1B.13. The signed cells, bound honestly

**C1 — dedicated freezer watchdog.** P1 **retains** a dedicated freezer
watchdog with every carried property: witness/freezer role, holds no lock and no
capability, writes nothing under `runtime/`, appends no ledger, settles nothing,
sealed pipes only, `WATCHDOG/FREEZE/<witness_id>.json` observations, ack
liveness and the absence rule. **P1 intentionally reduces supervisor-death
detection from two mechanisms to one — the update-pipe EOF.** The direct-parent
`getppid()` detector is gone because the watchdog's parent is the PCS.
**This is the author's selected trade, recorded in the P1 signature, not a
mechanically unchanged C1 implementation, and this document does not describe it
as one.** The watchdog additionally gains a capability-free address space by
construction, which is a genuine strengthening of a different C1 property; the
two facts are stated separately and neither is used to obscure the other.

**B1 — durable journal, ack, redelivery.** The **client** journal is unchanged
as signed. `t-pcs.v1` adds a **separate** control-plane journal (§P1B.5.4).
Byte replies are replayable. **Descriptor-bearing replies cannot redeliver the
same capability**: re-sending would install a second independent copy that no
accounting in this contract could reconcile. **An ACK loss on a `SPAWN_ROLE` or
`SPAWN_WATCHDOG` reply therefore invalidates the generation rather than
retrying the descriptor transfer.** This is an explicitly accepted narrowing of
B1 on that channel, applying to exactly two of the nine operations.

**D1 — no idle exit.** No idle exit remains, and D1's ground is intact: **no
supervisor waits on `SPAWN.lock`**, and a running supervisor's lifetime never
depends on any client. **What changes is availability**: the PCS is a mandatory
resident process whose crash cannot be recovered by adoption (§P1B.8.2), and the
result is **accepted fail-closed whole-generation invalidity**. That invalidity
is a process fact routed through §P1B.8.4; it is **never** a scientific or
resource outcome.

**K1 — supervisor-mediated transport, fixed ceiling.** Carried exactly. The PCS
creates the pipes and transfers descriptors, but the **supervisor** remains the
mediator of the output path, the fixed ceiling is unmoved, and the
one-write/one-hash accounting, the no-replenishment rule, the three branch
bodies and the §N2.3 P1–P7 custody proof are unchanged. Nothing in P1 changes
what K1 selected.

**A3 — same-UID procedural rescope.** Carried exactly, and **not upgraded**.
Nothing in P1 creates Q/C confidentiality or same-UID adversarial confinement.
`T_RUNTIME.lock` still serializes contract actors and is still not a filesystem
exclusion mechanism. The §P1B.6.5 interval, the stopped-role residual, the
final observation-to-install selector window, and the object-name residuals all
remain procedural, bounded and permanently non-citable.

---

## §P1B.14. Test matrix

Carried rows through v2.1.10.2 §T8's 404 stand, except 354, 356, 362 and 381,
which are replaced below. **v2.1.10.3's rows 405–436 are deleted as P4-specific**
and replaced by 437–486.

| # | Test |
|---|---|
| 354R | the supervisor socket pair is created by the PCS before the `c4` fork; the peer end reaches the `SUPERVISOR` role at slot 6 and nowhere else |
| 356R | the fd vector for each opcode/status equals the §P1B.5.3 row exactly; every other count or type is `ANCILLARY_VIOLATION` |
| 362R | ACK timeout marks `FD_DELIVERY_UNCONFIRMED`; the PCS never re-sends descriptors; the generation routes to §P1B.8.4 |
| 381R | the PCS is the direct parent and sole reaper of `pid_mid`, every controller, every worker and every watchdog; a wildcard wait in the supervisor returns `ECHILD` because its child set is empty |
| 437 | **no operative text contains any Cell-P option token other than the selected one** — specifically not `I_SELECT_SUPERVISOR_PROCESS_AUTHORITY_P2_…`, `…_P3_…`, `…_P4_…` — and none of `SPAWN_REPLACEMENT_WATCHDOG`, `WATCHDOG_REPLACEMENT`, `WATCHDOG_DETECTOR_DEGRADED`, or a phrase of the form "under P2/P3/P4", except inside §P1B.0.2. **The carried §U6.1 preflight step names `P0`, `P1`, `P2a`, `P2b`, `P3` are unrelated identifiers with a name collision only, are untouched by Cell P, and are explicitly exempt from this assertion**; the test must match the option tokens and phrases, never the bare letters |
| 438 | the opcode enum has exactly nine members and `SPAWN_WATCHDOG` has one uniform meaning for the first watchdog and every replacement |
| 439 | `t-pcs.v1` has no field carrying a PID, descriptor number, path, argv, signal number, symbol, callback, or unbounded integer |
| 440 | `SIGNAL_ROLE` and `SIGNAL_GROUP` are refused for `role == WATCHDOG` at every state |
| 441 | the supervisor contains no `fork`, `Popen`, `waitpid`, `kill`, `killpg`, or `subprocess` object on any path; static over `generic_harness.py` |
| 442 | **§P1B.3.3 leak proof**: after every role `execve`, `/proc/self/fd` is exactly `{0,1,2}` ∪ the role's slot set; assert no descriptor equals `SPAWN.lock` by `(st_dev, st_ino)`, none is the supervisor socket, the journal, another role's end, a source, the interpreter, or the package root |
| 443 | the `WATCHDOG` file actions contain the explicit `(CLOSE, 6)`; removing it makes `A-5` refuse |
| 444 | every PCS descriptor other than 3–8 is `CLOEXEC`; `_dup` returns non-inheritable descriptors; the hoist postcondition holds for every role target set |
| 445 | **§P1B.6**: no `/proc/self/fd` enumeration exists anywhere (`S-18`) |
| 446 | a violating message closes exactly its parsed vector, de-duplicated, ascending, once each, `EBADF` tolerated; assert a concurrent live role's ctrl and status descriptors survive |
| 447 | `_recvmsg` raising makes the very next executed operation `_exit_(T_PCS_EXIT_RECV_UNENUMERABLE)`, with no callback, finalizer, `atexit`, flush, or unwinding (`S-19`) |
| 448 | truncation fixture: with an under-sized ancillary buffer the parsed vector equals the installed set and `MSG_CTRUNC` is set; assert no descriptor outside the parsed vector exists in the process |
| 449 | `MSG_CMSG_CLOEXEC` is passed on every `recvmsg`; received descriptors carry `FD_CLOEXEC` with no window |
| 450 | a non-`SCM_RIGHTS` ancillary item, a `cdata` length not a multiple of 4, an over-long `cdata`, `MSG_TRUNC`, and a wrong fd type each route as §P1B.6.3 states |
| 451 | the watchdog never uses `getppid()` for supervisor death; a PCS-death fixture with the supervisor alive produces **no** freeze from the `getppid()` change |
| 452 | supervisor death produces update-pipe EOF and the carried freeze/observe/exit route |
| 453 | watchdog death is observed by ack absence and by `REAP_ROLE`; only `REAPED_POSITIVE` proves it |
| 454 | replacement watchdogs are created by `SPAWN_WATCHDOG` with identical isolation, slot map, and detector model as the first |
| 455 | no signal is sent to any watchdog on any path; termination is update-EOF only; `WATCHDOG_UNREAPED` routes to §P1B.8.4 |
| 456 | the carried §U2.6 first-ack-timeout route is the close-then-`REAP_ROLE` form and contains no kill |
| 457 | `S-1`…`S-7` shutdown ordering; each `S-5` branch behaves as tabulated; the watchdog is reaped or the generation is invalid before the supervisor exits |
| 458 | PCS death: `init` adoption, `ACCEPTED` journal state, supervisor authority lost, freeze unavailable, watchdog governed then exited, generation invalid |
| 459 | a PCS started against a non-terminal generation responds `GENERATION_NOT_ADOPTABLE`, acts on nothing, and exits |
| 460 | the J1–J6 order and every crash cut behave as §P1B.5.4 tabulates |
| 461 | replay of `ACCEPTED` performs no syscall; replay of `COMPLETED`/`ACKED` returns the record with `fds_redelivered = 0` and no descriptors |
| 462 | one outstanding request at a time; out-of-order or unmatched responses are `TRANSPORT_STRUCTURAL` |
| 463 | unknown opcode, field count, handle, state, or generation yields `INVALID` with no side effect |
| 464 | `SHUTDOWN` with a live handle refuses and releases nothing |
| 465 | the role bootstrap imports exactly `{os, sys, fcntl}`; a two-import build fails `A-6` |
| 466 | `generic_harness.py`'s scoped set is the sixteen signed members plus `_socket`, and contains neither `signal`, `_signal`, nor `sys` |
| 467 | `PRODUCTION_ROOTS` has five entries; the manifest's `roots` matches; `root_source_sha256` covers all five and a one-byte change fails |
| 468 | `S-1'`…`S-19` each reject a bit-exact negative fixture and accept a positive one |
| 469 | the per-primitive identity table is used everywhere; **no universal builtin predicate appears**; the method-descriptor class covers `_sendmsg`/`_recvmsg` |
| 470 | the object-bound `/proc/self/fd/7` and `/proc/self/fd/8` mechanism, the `-I -S -E -P` invocation, the empty environment, and the absence of `PYTHONPATH` all hold for the PCS and every role |
| 471 | the role bootstrap's `A-1`…`A-13` refusal order, including `A-9`'s single object-bound `sys.path[:]` assignment and `A-11`'s inode re-verification |
| 472 | every runtime preflight of §P1B.11 refuses fail-closed with no fork, no lock acquisition, and no record installed |
| 473 | K1's ceiling, one-write/one-hash accounting, no-replenishment rule, three branch bodies, and §N2.3 P1–P7 custody are byte-unchanged |
| 474 | §V217.1's object-bound observation and both revalidation barriers are unchanged and operate `dir_fd`-relative to the runtime root |
| 475 | §V217.4's bound-language sweep, revised row 86, and D1's stated ground are unchanged |
| 476 | `ECHILD`/`ESRCH` never prove death; the ten-row identity table; ownership-gated signals; `T3` absent; the no-discard invariant |
| 477 | the stage-M `m0`/`rel1`/fork-shared-lock proof is unchanged and no stage-M text cites `m5`/`rel2` |
| 478 | `SIGPIPE = SIG_IGN` survives the `N-1` reset; `V-6` proves no ignored disposition moved; the carried `m4`/`m8` `EPIPE` route is unchanged |
| 479 | `T_CTRL_FD_LOW`/`T_CTRL_FD_HIGH` remain 3/4 for controllers and workers; §Z3.3's layout and §Z3.2's role enum are byte-unchanged |
| 480 | the platform pin refuses every non-`x86_64` and non-`3.12.3` host before fork; the mask width rule is applied only inside that scope |
| 481 | every §P1B.12 numeric statement is asserted literally |
| 482 | the §P1B.8.4 routing: every unknown control outcome settles through `T_PROCESS_INVALID` and §4c(c)/§4d and produces no success, capacity, custody, E1/E2/E3, or Q/C fact |
| 483 | no operative text describes the C1 detector reduction as "unchanged", "strengthened without qualification", or "mechanically preserved" |
| 484 | no text claims the A3 residual is a security guarantee, and the §P1B.6.5 interval is described as a capability leak, never as a resource fact |
| 485 | the caller never signals the PCS; the reply pipe is the sole authoritative result |
| 486 | whole-chain no-regression diff over every carried surface |

---

## §P1B.15. Weakest points of this composite

1. **The C1 detector reduction is a real loss.** P1 has one supervisor-death
   detector where the signed text had two. It is the selected trade, but if the
   update pipe's write end were ever duplicated into another process, EOF would
   not fire on supervisor death and the sole detector would be defeated.
   §P1B.3.3's leak proof is what prevents that, and it is therefore
   load-bearing for C1 in a way it was not under the two-detector design.
2. **The PCS is a single point of failure** whose loss is an unrecoverable
   whole-generation invalidity. Strictly worse availability than the signed
   §W2.9 two-phase takeover it displaces.
3. **§P1B.6.2 rests on a kernel-source fact.** I have made the rule fail-closed
   for the one interval the fact does not cover, but the fact itself is
   reviewer-verifiable and I did not and could not verify it empirically.
4. **The capability-leak interval is real.** Bounded and terminated by `_exit`,
   but real, and it lives inside the A3 threat model, which is procedural and
   not a guarantee.
5. **`_socket.socket`'s finalizer** remains a finalizer in a closure whose value
   is having none. It can only close, but it is there, and the two containment
   rules are conventions the AST grammar checks rather than properties of the
   type.
6. **Descriptor-bearing replies are not retry-stable**, so a lost ACK costs a
   generation. That is the accepted B1 narrowing, and it means an ordinary
   transient can produce an invalidity.
7. **The composite is large.** Five roots, two protocols, two journals, four
   role classes, nineteen AST rules, and a runtime preflight of eleven steps. A
   reviewer may reasonably judge the aggregate too large to verify in one pass
   even if each part is sound.
8. **Three of this author line's earlier layers needed governance correction.**
   That is a reason to weight this document's self-assessment low and to check
   §P1B.12's counts and §P1B.0.1's index literally rather than trusting them.

---

## §P1B.16. Future edit surface, next gate, negative authorization

| Path | Permitted change | Status today |
|---|---|---|
| `scripts/officina_process_control_bootstrap.py` | the PCS and its `t-pcs.v1` server | **does not exist** |
| `scripts/officina_role_bootstrap.py` | the four-role isolated entry | **does not exist** |
| `src/philosophia/officina/verification.py` | CHANGES 1–5 of §P1B.11, and nothing else | unmodified, `327b1bb2…` |
| `successor/officina/runtime_control/PRODUCTION_CALL_GRAPH.json` | five roots, the closure, `root_source_sha256` | does not exist |
| `src/philosophia/officina/generic_harness.py` | the `posix_spawn` launcher, the `t-pcs.v1` client, the four role entries; **removal** of every `Popen`/`fork`/`waitpid`/`kill`/`killpg` | **untracked Cursor work — preserved byte-for-byte** |
| `tests/test_officina_generic_harness.py` and new bootstrap/PCS test modules | §P1B.14 | untracked Cursor work — preserved |
| everything else | **no change** | byte-unchanged |

**Next gate:** fresh independent **X-line** (Claude Code Opus 4.8) and **Y-line**
(GPT-5.6 Sol) review of the **identical bytes** of this binding together with
the carried chain. `I_ACCEPT_OFFICINA_SUPERVISOR_CONTROL_CHANNEL_AMENDMENT`
becomes available **only** if both lines confirm those identical bytes.

**Negative authorization.** This binding authorizes no implementation; no code,
test, verifier, manifest, allowlist, signature or contract edit; no commit; no
host change; no process, socket, pipe, FIFO, fork, exec or signal; no
supervisor, controller, worker, watchdog, adapter, middle child, grandchild,
endpoint, journal instance, spawn record, lease, capability, operation, capacity
artifact, custody disposition, freeze witness or result manifest; no T
activation; no entropy; no E1/E2/E3 spend; no Q/C work; no world, learner,
candidate, Q attempt, datum, outcome or Proof; and no claim movement.

---

## §P1B.17. The bounded review questions

Both lines review the **identical bytes** of this binding and of the carried
chain, must recompute every governing hash, and must treat every author closure
in this chain — including this layer's — as untrusted.

### For the X line (Claude Code Opus 4.8, clean context)

> **X-Q1 — is P1 single-valued?** Does one operative architecture survive, with
> **no** P2/P3/P4 branch outside §P1B.0.2, a nine-member opcode enum whose
> `SPAWN_WATCHDOG` has one uniform meaning, and every count in §P1B.12 literally
> true across the whole composite? Attack the replacement index for a carried
> sentence that still conditions behaviour on an unselected option.
> **X-Q2 — the descriptor surfaces.** Is §P1B.3.3's leak proof correct — that
> `POSIX_SPAWN_DUP2` clears close-on-exec, that every PCS descriptor outside
> 3–8 is `CLOEXEC` by construction, and that no lock, socket, journal,
> unrelated-role, source, interpreter or package-root descriptor reaches any
> role? And is §P1B.6 right about `scm_detach_fds()` — that Linux installs only
> what fits, reports exactly what it installed, and releases the rest — so that
> the only unenumerable case is an interpreter-side raise, correctly handled by
> an immediate `_exit_`?
> **X-Q3 — the bound cells.** Are §P1B.13's four statements honest and
> complete: C1's reduction to one detector stated as a selected trade rather
> than an unchanged implementation; B1's descriptor non-redelivery stated as an
> ACK loss invalidating a generation; D1's availability change stated as
> accepted fail-closed invalidity; and A3/K1 carried without upgrade? Does any
> operative sentence soften one of them?
>
> Verdict line 1 exactly `CONFIRM_OFFICINA_SUPERVISOR_P1_COMPOSITE_X` or
> `REVISE_OFFICINA_SUPERVISOR_P1_COMPOSITE`. Static review only: run no code,
> test, probe, or process/socket/fork/signal operation; create exactly one
> review file; modify nothing; authorize no implementation, activation, entropy,
> spend, Q/C work, or claim movement.

### For the Y line (GPT-5.6 Sol, clean context)

> **Y-Q1 — totality.** Are §P1B.8's crash and invalidity matrix, §P1B.9's
> shutdown route, and §P1B.5.4's journal automaton total — every cut with one
> continuation, PCS death unrecoverable with no adoption, supervisor death,
> watchdog death and replacement, wedged watchdog, role stop and reap, and every
> handle-release path? Does any unknown control outcome reach a success, a
> capacity fact, a custody disposition, or a scientific claim rather than
> `T_PROCESS_INVALID` and the §4c(c)/§4d unknowable route?
> **Y-Q2 — the capability rule.** Is §P1B.6 the right repair: no global sweep;
> close exactly the parsed vector, de-duplicated and once each; never touch a
> live role's descriptors; and a fail-closed `_exit_` with no callback for the
> unenumerable case, named as a transient **capability leak** rather than a
> resource fact, and left inside A3 without upgrading A3? Verify the
> `scm_detach_fds()` claim independently.
> **Y-Q3 — the watchdog and the carried surfaces.** Is the one-detector
> watchdog model coherent — the watchdog ignoring `getppid()` so a PCS death
> cannot cause a false freeze, the supervisor performing no `waitpid`,
> termination by update-EOF only with no signal on any path, and replacement
> uniform with the first? And do §V217.1's barriers, §V217.4's bound sweep,
> `CLOSE_OWNED`, custody P1–P7, K1's accounting, §Z3.3's layout and §Z3.2's role
> enum all carry byte-unchanged?
>
> Verdict line 1 exactly `CONFIRM_OFFICINA_SUPERVISOR_P1_COMPOSITE_Y` or
> `REVISE_OFFICINA_SUPERVISOR_P1_COMPOSITE`. Static review only: run no code,
> test, probe, or process/socket/fork/signal operation; create exactly one
> review file; modify nothing; authorize no implementation, activation, entropy,
> spend, Q/C work, or claim movement.

---

`I_ACCEPT_OFFICINA_SUPERVISOR_CONTROL_CHANNEL_AMENDMENT` remains **not
signable** and is not made signable here. Cell P is signed; the composite is
not accepted. `successor/officina/runtime/` contains only `T_RUNTIME.lock`;
`successor/officina/runtime_control/` does not exist;
`successor/officina/T_ENVELOPE.json` remains `"activated": false`. **T remains
`NOT_ACTIVATED`; the programme claim remains `OPEN`.**
