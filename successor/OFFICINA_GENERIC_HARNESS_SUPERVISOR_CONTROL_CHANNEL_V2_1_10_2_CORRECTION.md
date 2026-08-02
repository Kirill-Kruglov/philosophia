# Officina supervisor and control-channel amendment — v2.1.10.2 PCS transport correction

Status: `BLOCKED_ON_AUTHOR_CELL_P` — see §T7. **This layer does not request X/Y
review and does not declare readiness.** It specifies the transport and protocol
completely, and then stops at a decision that is not the author's to make.

Layer prefix: **§V211002**.

> ## WHAT THIS LAYER DOES, AND WHERE IT STOPS
>
> v2.1.10.1 made the Process-Control Server (PCS) normative but specified no
> implementable descriptor transport and no protocol capable of carrying its
> nine operations. Both defects are real and blocking. This layer:
>
> - **T1** — replaces the impossible "supply a `ctrl-fd pair` over the byte
>   pipe" with a real capability transport: a PCS-created `AF_UNIX`
>   `SOCK_SEQPACKET` control channel carrying descriptors as `SCM_RIGHTS`
>   ancillary data. **No numeric fd ever crosses the protocol again.**
> - **T2** — replaces the prose "nine operations are added to the existing
>   grammar" (false — the carried grammar is a fixed six-field
>   `SPAWN_SUPERVISOR` record) with a **fresh versioned protocol**,
>   `philosophia.officina.t-pcs.v1`, on its own channel, with one closed request
>   and one closed response per operation and an exact journal/ack/redelivery
>   automaton.
> - **T3** — replaces the role exec's `-P` + `PYTHONPATH=/proc/self/fd/8`, which
>   re-enabled `site`, `.pth` and user customization, with a **second
>   object-bound isolated root**, `scripts/officina_role_bootstrap.py`, run
>   `-I -S -E -P` with an empty environment. **`PYTHONPATH` is deleted from the
>   design**; the reviewed first stage inserts exactly one object-bound path.
> - **T4** — makes the PCS lifetime, fd and custody model total.
> - **T5** — updates the import closure to
>   `{os, sys, _signal, time, fcntl, _socket}` and replaces the invalid
>   zero-byte-write access-mode test with
>   `fcntl(fd, F_GETFL) & O_ACCMODE == O_RDONLY`.
> - **T6** — carries the fd-bound launcher and generalizes the hoist and
>   collision proof to every spawn in the tree.
>
> **And then it stops.** §T7 finds that the PCS is **not** a mechanical
> implementation of the already-selected policies. Parenting the watchdog to the
> PCS **deletes a signed supervisor-death detector** (v2.1 §W3.5's "watchdog's
> `getppid()` ≠ recorded") and removes the supervisor's `waitpid`-on-own-child
> watchdog-death detector; the PCS is a new mandatory resident process whose
> loss invalidates a generation; and B1's exactly-once discipline must be
> extended to a second control plane with its own durable journal. **Those are
> changes to signed cells, and at least one is a regression I introduced in my
> own v2.1.10.1 row 36, which claimed the exec'd watchdog "strengthens C1".
> That claim was wrong and is withdrawn here.**
>
> The correction therefore presents **one bounded author cell, P, with three
> exclusive fully-specified options**, and decides nothing. **No scientific or
> resource value is reached, proposed, or implied by any option.**

**Authorship.** Written by **Claude Code Opus 5 acting only as the specification
author**, because Claude Code Fable 5 was unavailable. The same author line
wrote v2.1 through v2.1.10.1. This is **not** an X-line or Y-line review of its
own bytes and must never be counted as one
(`reviews/officina_supervisor_v2_1_authorship_note.md`). Every author closure in
the chain, including this layer's, is an untrusted self-assessment.

**Review state.** v2.1.9 was revised by both independent lines. v2.1.10 and
v2.1.10.1 have received **no** independent review. This layer is a second
pre-review author correction. The bytes that must eventually be reviewed are
v2.1.10 as corrected by v2.1.10.1 and this layer — **after** cell P is signed.

Signed author cells embedded; **none reopened or reinterpreted by this layer's
engineering.** Cell P (§T7) is a **new** proposed cell and is **not signed**:

```text
A: I_SELECT_SUPERVISOR_CONFINEMENT_A3_SAME_UID_PROCEDURAL_RESCOPE
B: I_SELECT_SUPERVISOR_IDEMPOTENCY_B1_DURABLE_JOURNAL_ACK_REDELIVERY
C: I_SELECT_SUPERVISOR_WATCHDOG_C1_DEDICATED_FREEZER
D: I_SELECT_SUPERVISOR_LIFETIME_D1_NO_IDLE_EXIT
K: I_SELECT_SUPERVISOR_OUTPUT_CAPACITY_K1_SUPERVISOR_MEDIATED_TRANSPORT_FIXED_CEILING
```

`I_ACCEPT_OFFICINA_SUPERVISOR_CONTROL_CHANNEL_AMENDMENT` remains **not
signable**, and §T7 shows why it does not, by itself, truthfully cover the PCS
architecture.

Creates nothing executable. Edits no code, verifier, manifest, test, contract,
signature, review, prompt, or runtime artifact. Starts no process, socket, or
channel. Creates no entropy, activation, capability, world, learner, candidate,
datum, Q/C object, capacity artifact, custody disposition, result manifest, or
outcome. T remains `NOT_ACTIVATED`; the programme claim remains `OPEN`.

## Governing hashes (recomputed)

```text
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
ae9c440acaaba90f2cb669e5a8212082f4c0f25b5b7e31ebc906b9cbc0ad6132  reviews/officina_supervisor_v2_1_authorship_note.md
c494ef8884948bd0e737373d2d57a3ab74bbd456db2c3463711c4405f2fdf86a  successor/OFFICINA_SUPERVISOR_AUTHOR_SELECTIONS_V1_SIGNATURE.md
4918a208bb94549ba3e7c38571265e723cc51a0a3394e291a62a85c333d864a6  successor/OFFICINA_SUPERVISOR_OUTPUT_CAPACITY_SELECTION_V1_SIGNATURE.md
8c47da352ef5954406964647a32e97939c404806bdf9b3d3ff5bc70866e6369a  successor/OFFICINA_GENERIC_HARNESS_SIGNATURE.md
724d633a55668013b78058eed1c76e12e9bbaf487f71ea94b7a4568ea1ced8a0  successor/OFFICINA_GENERIC_HARNESS_CONTRACT_V2_3_1_CORRECTION.md
b5a1523290b6b8417a7b3288329cc4a4e5ff80214c8f28e6ea1ae51a450a94c9  successor/OFFICINA_BATCH_SETTLEMENT_CORE_AMENDMENT_V1_1_1_CORRECTION.md
327b1bb222173407772836a2fdc4e92f89595508aff8b77f68f65816cafbec1e  src/philosophia/officina/verification.py
```

`verification.py` unamended; neither `scripts/officina_process_control_bootstrap.py`
nor `scripts/officina_role_bootstrap.py` exists.

---

## V211002.0. Literal v2.1.10.1 → v2.1.10.2 replacement index

**Nothing else moves.** Everything in v2.1.10.1 and v2.1.10 not named below
carries verbatim — in particular §V21101.1 (the `_signal` inventory and the
per-primitive identity table), §V21101.2 (object-bound source and interpreter),
§V21101.3 (the `posix_spawn` launcher), §V21101.4 (the launcher disjunction),
§V21101.5.2 (the fd 6 ↔ fd 7 binding), §V2110.2.3 (the process-boundary reaping
proof), §V2110.4 (`WAIT_ONE`, `STRUCTURAL_VIOLATION`), §V2110.6 (the pinned
platform and mask rules), §V219.3, §V218.2.2, §V218.3, §V218.4, §V218.5,
§V217.1, §V217.4, and the whole carried chain.

| # | v2.1.10.1 / v2.1.10 locus, quoted | Action |
|---|---|---|
| 1 | §V21101.6.3's operation table rows `SPAWN_ROLE` ("role token …, ctrl-fd pair, spawn-intent id") and `SPAWN_WATCHDOG` ("sealed update/ack pipe descriptors") | **replaced** by §T1 and §T2 — descriptors are transferred as `SCM_RIGHTS` ancillary data and never named as integers in any field |
| 2 | §V21101.6.3's preamble "Added to the already-introduced closed wire enum of §V2110.2.5; the record grammar, field character classes, and framing are unchanged." | **deleted as false**, replaced by §T2's fresh `t-pcs.v1` protocol on its own channel |
| 3 | §V2110.2.5's request/reply grammar | **retained, scoped**: it governs the **caller↔PCS pipe** and the single `SPAWN_SUPERVISOR` operation only (§T2.1) |
| 4 | §V21101.5.3's `g0'`/`_execve` block, in particular `b"-P"` alone and `{ b"PYTHONPATH": b"/proc/self/fd/8" }` | **replaced** by §T3 — a second isolated root, `-I -S -E -P`, **empty environment**, and a reviewed `sys.path` insertion. **`PYTHONPATH` is deleted from this design** |
| 5 | §V21101.6.4's role descriptor table | **replaced** by §T4.2's role tables (one per role class) |
| 6 | §V21101.6.5's watchdog paragraph, in particular "**This strengthens C1 rather than weakening it.**" | **replaced** by §T7.2 — the address-space half was right, but the paragraph **omitted that the `getppid()` supervisor-death detector is deleted**. The strengthening claim is **withdrawn** |
| 7 | §V21101.6.6's call/ownership table and its "Consequence" paragraph | **replaced** by §T4.1–§T4.4 |
| 8 | §V21101.6.2's bounding principle sentence "this is a **relocation of the primitive, not a change of semantics**" | **qualified** by §T4.5 — it holds for every primitive that has a named PCS operation with a unique carried consumer, and §T4.5 proves that mapping; it does **not** hold for the two watchdog detectors of §T7.2, which is why cell P exists |
| 9 | §V21101.1.1's five-module inventory | **replaced** by §T5.1 (`_socket` added; six modules) |
| 10 | §V21101.2.2's `P-s5` ("a `_read` of zero bytes must succeed and a `_write` must raise `OSError`") | **replaced** by §T5.3 (`fcntl(fd, F_GETFL) & O_ACCMODE`) |
| 11 | §V21101.3.3's hoist and file-action block | **generalized** by §T6.1 to an arbitrary target set, so PCS→role spawns reuse the identical proof |
| 12 | §V21101.8.1's CHANGE 2 map and S-1/S-3/S-5/S-7 | **replaced** by §T5.4 |
| 13 | §V21101.8.2's rows and §V2110.7.4's rows | **extended** by §T8; rows 353–404 added |
| 14 | §V21101.11's weakest-point list | **extended** by §T9 |
| 15 | §V21101.10's supersession table | **extended** by §T7.4 rows 37–44 |
| 16 | v2.1.10.1's `READY_FOR_OFFICINA_SUPERVISOR_V2_1_10_1_FINAL_XY_CONFIRMATION` closure verdict | **superseded**: readiness is withdrawn pending cell P. The engineering of v2.1.10.1 stands; its governance conclusion does not |

---

## T1. The descriptor transport

### T1.1 The defect, stated exactly

> **`SPAWN_ROLE` and `SPAWN_WATCHDOG` as written are unimplementable.** A
> descriptor integer is an index into a per-process descriptor table. Writing
> the integer `7` into an anonymous pipe conveys no capability whatsoever; the
> reader's descriptor `7`, if any, is an unrelated object. v2.1.10.1 specified
> no `SCM_RIGHTS`, no proxy, and no preallocation. The two operations could not
> have been implemented as written, and the fault is the author's.

### T1.2 The chosen transport, single-valued

> **One `AF_UNIX` / `SOCK_SEQPACKET` / protocol `0` socket pair per
> supervisor generation, created by the PCS, carrying descriptors as
> `SCM_RIGHTS` ancillary data. No proxy. No preallocation. No alternative.**

`SOCK_SEQPACKET` is chosen over `SOCK_DGRAM` and `SOCK_STREAM` because it is
connection-oriented **and** message-boundary-preserving **and** reliable: a
`sendmsg` of one record is delivered as exactly one record or not at all, so
**partial reads and partial writes are impossible at the record level** (§T2.5),
and peer death is observable as an EOF-equivalent rather than as silence.

| Property | Value |
|---|---|
| family / type / protocol | `AF_UNIX` / `SOCK_SEQPACKET` / `0` |
| creation | `_socketpair(AF_UNIX, SOCK_SEQPACKET, 0)` **in the PCS**, before the `c4` fork that leads to the supervisor |
| PCS endpoint | retained in a module-level slot for the generation's life; never closed while any handle is live |
| peer endpoint | inherited through `c4` → `m7` → the role `execve`, `dup2`'d to `T_ROLE_FD_PCS` (§T4.2) |
| socket objects | held in module-level slots only; **every received descriptor is handled as a plain `int`** and closed with `_close`, never wrapped in a socket object |
| max record payload | `T_CONTROL_FRAME_MAX_BYTES` (4096, carried) |
| **max descriptors per message** | **3** — the largest legal vector (§T1.4) |
| ancillary buffer size | `_CMSG_SPACE(3 * 4)` — three 4-byte native `int`s on the pinned x86_64 platform |
| credentials | **none.** `SO_PASSCRED` is never enabled; `SCM_CREDENTIALS` is never sent and any received ancillary item whose `(level, type)` is not exactly `(SOL_SOCKET, SCM_RIGHTS)` is a violation (§T1.6) |

### T1.3 The exact calls and the integer packing rule

```text
SEND (PCS → supervisor, the only direction that carries descriptors):
  payload := the t-pcs.v1 response record of §T2, one bytes object, <= 4096
  fds     := the ordered descriptor vector for this response (0..3 entries)
  anc     := b"".join(fd.to_bytes(4, "little") for fd in fds)
  n := _sendmsg(sock, [payload],
                [(_SOL_SOCKET, _SCM_RIGHTS, anc)] if fds else [])
  require n == len(payload)                       # SEQPACKET: all or nothing
    otherwise ⇒ TRANSPORT_STRUCTURAL (§T1.6)

RECEIVE (supervisor side):
  data, anc, flags, _addr := _recvmsg(sock,
                                      T_CONTROL_FRAME_MAX_BYTES,
                                      _CMSG_SPACE(12),
                                      _MSG_CMSG_CLOEXEC)
  fds := []
  for (level, type_, cdata) in anc:
      if (level, type_) != (_SOL_SOCKET, _SCM_RIGHTS):
          ⇒ collect nothing from it, mark ANCILLARY_UNEXPECTED
      else:
          require len(cdata) % 4 == 0 and len(cdata) <= 12
          fds += [ int.from_bytes(cdata[i:i+4], "little")
                   for i in range(0, len(cdata) - (len(cdata) % 4), 4) ]
  require (flags & _MSG_CTRUNC) == 0 and (flags & _MSG_TRUNC) == 0
```

**The packing rule, pinned and justified.** `SCM_RIGHTS` ancillary data is an
array of native `int`. On the pinned platform (`Linux x86_64`, §V2110.6,
carried) a native `int` is **4 bytes, little-endian**, so
`int.to_bytes(4, "little")` and `int.from_bytes(…, "little")` are **exactly**
the native representation. `int.to_bytes` / `int.from_bytes` are builtin
methods of `int` and require **no import at all** — which is why neither
`array` nor `struct` is added (§T5.1). Any other architecture is already
refused at `P-a` before this code is reachable.

**Truncated ancillary data is never partially trusted.** A `cdata` whose length
is not a multiple of 4 yields the truncated remainder being **discarded from the
fd list**, but the kernel may nonetheless have installed a descriptor for it;
this is precisely why `MSG_CTRUNC` is checked and why §T1.6 closes **every**
descriptor found in `/proc/self/fd` above the pinned set before routing.

**`MSG_CMSG_CLOEXEC` is mandatory on every `recvmsg`.** It sets `FD_CLOEXEC` on
received descriptors **atomically with their installation**, so there is no
window in which a received descriptor could leak across an `exec`. A receiver
that omits it is a contract violation, not a route (statically checked, §T5.4
rule `S-15`).

### T1.4 The only legal descriptor vector per operation

| Operation / result | fd count | fd types, in this exact order |
|---|---|---|
| every **request** (supervisor → PCS) | **0** | — |
| `SPAWN_ROLE` ok | **3** | ctrl request write end (`S_ISFIFO`), ctrl reply read end (`S_ISFIFO`), status read end (`S_ISFIFO`) |
| `SPAWN_WATCHDOG` ok | **2** | update write end (`S_ISFIFO`), ack read end (`S_ISFIFO`) |
| `SPAWN_ROLE` / `SPAWN_WATCHDOG` refused | **0** | — |
| `AWAIT_STOP`, `SIGNAL_ROLE`, `SIGNAL_GROUP`, `REAP_ROLE`, `RELEASE_HANDLE`, `SHUTDOWN`, `PING` — every status | **0** | — |

> **Any message whose actual descriptor count or type vector differs from the
> row its opcode and status select is `ANCILLARY_VIOLATION`.** The receiver
> **closes every received descriptor**, in ascending numeric order, with
> `_close`, tolerating `EBADF`, **before** any other action, and then routes to
> §T4.7's invalidity path. No descriptor is ever retained from a violating
> message, and no partially-accepted vector exists.

### T1.5 Ownership at every point

| Point | PCS holds | Supervisor holds | Rule |
|---|---|---|---|
| before `sendmsg` | the role's ends **and** the supervisor's ends | nothing | the PCS created both ends of every pipe |
| `sendmsg` returns full length | both still | nothing yet (kernel holds copies in the socket buffer) | `SCM_RIGHTS` **duplicates**; the send does not transfer |
| immediately after a successful `sendmsg` | closes its copies of the **supervisor's** ends, unconditionally, in a pinned order; keeps the **role's** ends | — | prevents a PCS-side leak; the role's ends are the PCS's own business |
| `sendmsg` raises, or returns short | still holds the supervisor's ends and closes them | nothing | `TRANSPORT_STRUCTURAL`; the handle is destroyed by §T2.7 |
| after the supervisor's `recvmsg` | — | the duplicated descriptors, `FD_CLOEXEC` set | ownership has transferred |
| after the supervisor's `ACK` | — | same | the PCS marks `FD_DELIVERY_CONFIRMED` |
| ack times out | — | unknown | **the PCS never re-sends descriptors** (§T2.6); the handle is marked `FD_DELIVERY_UNCONFIRMED` and the operation is **inconclusive** ⇒ §T4.7 |
| duplicate request for the same `request_id` | the journalled outcome | — | the PCS replies with the recorded record and **zero** descriptors, `fds_redelivered = 0` (§T2.6) |
| malformed packet, either direction | — | — | receiver closes every received fd, then §T4.7 |
| supervisor dies with descriptors in the socket buffer | — | — | Linux releases buffered `SCM_RIGHTS` descriptors when the socket is closed; **no leak**, and the PCS observes the peer close |
| PCS dies | kernel closes everything it held | keeps what it received | the supervisor's channel reaches EOF ⇒ §T4.6 |

**No fd leak and no double close, at any cut:** every descriptor has exactly one
owning slot in exactly one process at any instant; every close is performed by
the slot's owner exactly once with `EBADF` tolerated; and the two paths that
could double-close — a PCS-side close after a failed send, and a receiver-side
close after a violation — are disjoint by construction because they act on
descriptors in different processes.

### T1.6 Transport violations, closed enumeration

```text
TRANSPORT_RESULT := OK | TRANSPORT_STRUCTURAL | ANCILLARY_VIOLATION
                  | PEER_EOF | PEER_RESET | TIMEOUT

  sendmsg short / non-int return / any BaseException      ⇒ TRANSPORT_STRUCTURAL
  recvmsg returns b"" with no ancillary                   ⇒ PEER_EOF
  ECONNRESET / EPIPE                                      ⇒ PEER_RESET
  MSG_CTRUNC or MSG_TRUNC set                             ⇒ ANCILLARY_VIOLATION
  an ancillary item that is not (SOL_SOCKET, SCM_RIGHTS)  ⇒ ANCILLARY_VIOLATION
  cdata length not a multiple of 4, or > 12               ⇒ ANCILLARY_VIOLATION
  fd count or type vector ≠ the §T1.4 row                 ⇒ ANCILLARY_VIOLATION
  a received fd whose fstat fails or has the wrong type   ⇒ ANCILLARY_VIOLATION
  EINTR                                                   ⇒ retry the same call
                                                            at T_SUPERVISOR_POLL_INTERVAL_NS
                                                            within the operation
                                                            deadline; on expiry
                                                            ⇒ TIMEOUT
  any other OSError                                       ⇒ TRANSPORT_STRUCTURAL
  any other BaseException                                 ⇒ TRANSPORT_STRUCTURAL

EVERY non-OK result:
  1. close every descriptor received in the offending message, ascending, EBADF
     tolerated — BEFORE anything else;
  2. additionally, scan /proc/self/fd and close every descriptor outside this
     process's pinned set (this catches a descriptor installed by a truncated
     ancillary item that never appeared in the parsed vector);
  3. then route to §T4.7. It is NEVER a success, NEVER a resource fact, and
     NEVER a scientific fact.
```

---

## T2. The `t-pcs.v1` protocol

### T2.1 Two channels, two protocols, no overlap

| Channel | Endpoints | Kind | Protocol | Operations |
|---|---|---|---|---|
| **caller channel** | contaminated caller ↔ PCS | two anonymous pipes (fds 3, 4) | the **carried** six-field request / five-field reply of §V2110.2.5, **unchanged** | exactly one: `SPAWN_SUPERVISOR` |
| **supervisor channel** | supervisor ↔ PCS | one `AF_UNIX` `SOCK_SEQPACKET` pair | **new**: `philosophia.officina.t-pcs.v1` | the nine of §T2.3 |

The carried caller grammar is neither extended nor reinterpreted; §V21101.0
row 3 scopes it. The new protocol is a **separate versioned schema on a
separate channel**, which is why v2.1.10.1's "the record grammar … remain
unchanged" was false and is deleted.

### T2.2 Record grammar

One `SOCK_SEQPACKET` message is exactly one record. ASCII, no NUL, fields
separated by exactly one `0x20`, terminated by exactly one `0x0A`, total length
≤ `T_CONTROL_FRAME_MAX_BYTES`. Parsed with `bytes.split(b" ")` only — no `json`,
no `re`.

```text
REQUEST  field 0  b"philosophia.officina.t-pcs.v1"          literal
         field 1  b"1"                                      protocol version
         field 2  generation_id      exactly 64 bytes [0-9a-f]
         field 3  request_id         1..19 bytes [0-9], no leading zero,
                                     strictly increasing within a generation
         field 4  opcode             one of the nine closed tokens
         field 5+ per-opcode operands (§T2.3), each from a closed class
         terminator b"\n"

RESPONSE field 0  b"philosophia.officina.t-pcs.v1"          literal
         field 1  b"1"
         field 2  generation_id      echo, must equal the request's
         field 3  request_id         echo, must equal the request's
         field 4  status             OK | REFUSED | INVALID | REPLAYED
         field 5  detail             [A-Z_]{1,64} from a closed token set
         field 6  handle_id          decimal 1..19 digits, or b"-" when none
         field 7  fds_redelivered    b"0" or b"1"
         field 8+ per-opcode result operands (§T2.3)
         terminator b"\n"

ACK      field 0  b"philosophia.officina.t-pcs.v1"
         field 1  b"1"
         field 2  generation_id
         field 3  request_id
         field 4  b"ACK"
         terminator b"\n"
```

> **Closure property, checkable by reading the grammar.** No field can carry a
> path, a PID, a signal number, arbitrary argv, a module or symbol name, a
> callback, a file descriptor, a timeout, or an unbounded integer. Every operand
> class below is either a closed enum token, a fixed-length hex string, or a
> decimal integer with a pinned digit bound. **The supervisor receives opaque
> handles and never a PID.**

### T2.3 The nine operations

| Opcode | Request operands | Preconditions | Response operands | fds |
|---|---|---|---|---|
| `SPAWN_ROLE` | `role` ∈ {`CONTROLLER`,`WORKER`}; `argv_template_id` (64 hex, naming an entry the **supervisor already made durable** in the signed `t-spawn-intent.v1` record — the PCS reads it from the runtime root, so no argv crosses the wire); `spawn_intent_id` (64 hex) | the intent record exists, is well-formed, and its `argv_template_sha256` matches; the generation is `LIVE` | `handle_id` | **3** |
| `AWAIT_STOP` | `handle_id`; `deadline_ticks` (1..6 digits, in `T_SUPERVISOR_POLL_INTERVAL_NS` units, ≤ the carried `T_SPAWN_SELF_STOP_TIMEOUT_NS`) | handle state ∈ {`SPAWNED`} | `outcome` ∈ {`STOPPED`,`EXITED`,`TIMEOUT`}; `start_identity` (decimal); `pgid_is_leader` ∈ {`0`,`1`} | 0 |
| `SIGNAL_ROLE` | `handle_id`; `sig` ∈ {`CONT`,`TERM`,`KILL`,`STOP`,`PROBE`} | handle state ∈ {`SPAWNED`,`STOPPED`,`RUNNING`}; ownership `OWNED` | `result` ∈ {`SENT`,`GONE`,`DENIED`,`STRUCTURAL_VIOLATION`} | 0 |
| `SIGNAL_GROUP` | `handle_id`; `sig` as above | the handle records a **kernel-verified** group (the carried §U2.5 tier rule) | as above | 0 |
| `REAP_ROLE` | `handle_id` | ownership ≠ `REAPED` | the carried six-result `WAIT_ONE` token (§V2110.4.1) | 0 |
| `SPAWN_WATCHDOG` | — | no live watchdog handle in this generation | `handle_id` | **2** |
| `RELEASE_HANDLE` | `handle_id` | handle state = `REAPED` | — | 0 |
| `SHUTDOWN` | — | no handle is live | — | 0 |
| `PING` | — | — | `pcs_uptime_ticks` | 0 |

`argv` never crosses the wire: the PCS reads the already-signed
`t-spawn-intent.v1` record from the runtime root and rebuilds §Z3.3's fixed
layout itself, so the closed-grammar property survives and §Z3.3's
`argv_template_sha256` semantics are preserved rather than duplicated.

### T2.4 Correlation, generation, and ordering

- `generation_id` is the carried `spawning_id` of the live generation. A record
  whose `generation_id` does not match the PCS's current generation is
  `INVALID`/`WRONG_GENERATION`; the PCS does **not** act on it and does **not**
  destroy state.
- `request_id` is strictly increasing per generation. A request whose id is
  `<=` the highest **journalled** id is a **replay** (§T2.6). A gap is
  permitted (the supervisor may abandon an id it never sent) and is recorded.
- Exactly one response per request, correlated by `(generation_id, request_id)`.
  The supervisor issues **one outstanding request at a time** on this channel —
  a pinned, statically checkable rule that removes all interleaving and makes
  out-of-order responses a protocol violation rather than a case.
- An out-of-order or unmatched response ⇒ `TRANSPORT_STRUCTURAL` ⇒ §T4.7.
- Unknown opcode, unknown field count, unknown handle, or a handle in the wrong
  state ⇒ `INVALID` with the corresponding closed detail token; **no side
  effect, no descriptor, no journal entry beyond the rejection record.**

### T2.5 Partial reads and writes

Impossible at the record level, by the socket type: a `SOCK_SEQPACKET`
`sendmsg` of a ≤ 4096-byte payload either delivers the whole message or fails,
and a `recvmsg` with a 4096-byte buffer receives the whole message or sets
`MSG_TRUNC`. The contract therefore has **no partial-record state**, and
`MSG_TRUNC`/`MSG_CTRUNC` are the only signals of a size violation — both routed
by §T1.6. This is the reason the transport is not a byte stream.

### T2.6 Journal, idempotency, and redelivery — integrated with signed B1

The signed B1 cell is `DURABLE_JOURNAL_ACK_REDELIVERY`. Its discipline is
applied **literally** to this channel, with one exception that is stated rather
than hidden.

```text
ORDER, per request, with the crash cut after each step named:
  J1. receive the request; validate the grammar and preconditions
        crash ⇒ nothing happened; the supervisor's redelivery is a fresh request
  J2. append the durable PCS journal entry
        { generation_id, request_id, opcode, operands, state: ACCEPTED }
        and fsync it
        crash ⇒ on restart the entry is ACCEPTED with no result: the operation
                is INCONCLUSIVE. Under every option of cell P the PCS does not
                restart into a live generation (§T4.6), so this is a
                whole-generation invalidity, never a silent retry
  J3. perform the syscall (spawn / wait / signal / reap)
        crash ⇒ same as J2, plus a possibly-live orphan role, which §T4.6
                routes
  J4. append the durable result entry { ..., state: COMPLETED, outcome,
        handle_id, fd_vector_len } and fsync
        crash ⇒ the result is durable; a redelivery replays it (J6)
  J5. send the response, with descriptors if the §T1.4 row says so
        crash ⇒ the result is durable but undelivered; redelivery replays it
                WITHOUT descriptors
  J6. on ACK, append { ..., state: ACKED } and fsync
        crash before ⇒ redelivery replays the COMPLETED record

REPLAY RULE (a request whose (generation_id, request_id) is already journalled):
  state ACCEPTED   ⇒ respond INVALID / OPERATION_INCONCLUSIVE. The PCS never
                     re-performs a syscall for a replayed id.
  state COMPLETED  ⇒ respond with the recorded status/detail/handle,
                     status := REPLAYED, fds_redelivered := 0, and NO descriptors
  state ACKED      ⇒ identical to COMPLETED
```

> **The one exception to B1's redelivery, stated loudly.** B1 promises a
> **retry-stable reply**. For fd-bearing responses the *record* is retry-stable
> but the *descriptors are not re-sent*, because re-sending would install a
> second, independent copy of a capability the supervisor may already hold —
> which no accounting in this contract could reconcile. Consequently a
> supervisor that loses the descriptors of a `SPAWN_ROLE`/`SPAWN_WATCHDOG`
> response **cannot recover them**; the handle is marked
> `FD_DELIVERY_UNCONFIRMED` and the generation routes to §T4.7's invalidity.
> **This is a genuine narrowing of B1's promise on this channel**, it applies to
> exactly two of the nine operations, and it is one of the reasons §T7 finds a
> signed cell affected rather than merely implemented.

### T2.7 Clean shutdown and EOF

- `SHUTDOWN` with any live handle ⇒ `REFUSED`/`HANDLES_LIVE`; the PCS does not
  exit and releases nothing.
- `SHUTDOWN` with every handle `REAPED` ⇒ `OK`; the PCS closes the supervisor
  socket, performs the carried `CLOSE_OWNED` cleanup, releases `SPAWN.lock`, and
  exits.
- The supervisor closing its endpoint ⇒ the PCS observes `PEER_EOF`. It does
  **not** exit and does **not** release anything while a handle is live: it
  enters the carried `B`-style non-returning reaper state for every live handle,
  because a live role with no controller is exactly the "possibly live child"
  case the no-discard invariant (§V2110.4.1, carried) forbids abandoning.
- The PCS closing its endpoint or dying ⇒ the supervisor observes `PEER_EOF`
  and has **lost all process authority** ⇒ §T4.6.

---

## T3. The isolated role entry

### T3.1 The defect

> `-P` alone leaves `site` enabled, so `.pth` executable lines, `sitecustomize`
> and `usercustomize` all run in the role process; and `PYTHONPATH` is an
> environment-driven path injection of exactly the class the isolation flags
> exist to remove. v2.1.10.1's role exec therefore reintroduced the
> contamination channel that v2.1.10 was built to close. **`PYTHONPATH` is
> deleted from this design and must not reappear as a workaround.**

### T3.2 The second isolated root

```text
canonical path : scripts/officina_role_bootstrap.py
owner          : Cursor (mechanical, from this contract)
invocation     : <object-bound interpreter> -I -S -E -P <object-bound source>
                 with env = {} exactly, and the argv of §T3.3
imports        : exactly `os` and `sys`. Nothing else. No project package at
                 stage 1.
```

It is the **executable root for every role**: `SUPERVISOR`, `WATCHDOG`,
`CONTROLLER`, `WORKER`. `PRODUCTION_ROOTS` therefore becomes **five** entries
(§T5.4 CHANGE 1'), superseding v2.1.10's four.

### T3.3 Argv, refusal order, and the path insertion

```text
argv[0] "/proc/self/fd/<T_ROLE_FD_INTERP>"
argv[1] "-I"   argv[2] "-S"   argv[3] "-E"   argv[4] "-P"
argv[5] "/proc/self/fd/<T_ROLE_FD_SELF>"      # the role bootstrap source
argv[6] "--officina-role"
argv[7] one of SUPERVISOR | WATCHDOG | CONTROLLER | WORKER
argv[8] "--officina-generation"
argv[9] <64 hex>
argv[10] "--officina-fdmap"
argv[11] a fixed comma-separated decimal list, whose length and meaning are
         determined solely by argv[7] (§T4.2)
… for CONTROLLER/WORKER only, the carried §Z3.3 tail from "--officina-target-argc"
env = {}                              # NO PYTHONPATH, NO variable of any kind

REFUSAL ORDER, executed exactly in this sequence; any failure ⇒ os._exit(3)
with nothing written, nothing unlinked, and no descriptor closed except its own:
  A-1  bind and identity-check `os` and `sys` primitives, per the carried
       §V21101.1.4 table
  A-2  read back sys.flags: isolated, no_site, ignore_environment, safe_path,
       no_user_site must all be true
  A-3  os.environ must be EMPTY
  A-4  argv must match the fixed shape above exactly; argv[7] must be one of the
       four literal tokens
  A-5  fstat every fd named in argv[11]; each must have the type its slot
       requires (§T4.2); /proc/self/fd must contain exactly {0,1,2} ∪ the slot
       set
  A-6  fstat T_ROLE_FD_SELF; require a regular file, not group/other writable,
       and O_RDONLY by the §T5.3 F_GETFL test
  A-7  open the canonical role-bootstrap path under T_ROLE_FD_PKGROOT with
       O_NOFOLLOW|O_RDONLY and require (st_dev, st_ino) == T_ROLE_FD_SELF's
       — the §V21101.5.2 mutual binding, applied to this root
  A-8  fstat T_ROLE_FD_SRCDIR; require a directory
  A-9  sys.path[:] = ["/proc/self/fd/<T_ROLE_FD_SRCDIR>"]
       — the ENTIRE path is replaced by exactly one object-bound entry; no
         append, no insert into an existing list, no environment involvement
  A-10 import philosophia.officina.generic_harness            (the ONLY import)
  A-11 fstat the imported module's __file__; require (st_dev, st_ino) ==
       T_ROLE_FD_ROLESRC's — the carried §V21101.5.3 R-1 check
  A-12 for CONTROLLER/WORKER only: perform the carried §Z3.3 adapter duties
       (index layout, target preflight, descriptor order, self-stop) unchanged
  A-13 call exactly one pinned entry function, selected by argv[7] from a closed
       four-entry mapping, with the validated descriptors
```

### T3.4 Role classes, and the proof for the two that cannot be fully isolated

| Role | `sys.path` after `A-9` | Isolated? | Basis |
|---|---|---|---|
| `SUPERVISOR` | exactly the object-bound `src` directory | **yes, fully** | it imports only the project package, which is stdlib-only by the signed harness §9 import discipline |
| `WATCHDOG` | the same | **yes, fully** | same |
| `CONTROLLER` | the same for `A-10`; the **target program** then runs under its own client-supplied argv after the self-stop, exactly as §Z3.3 already specifies | **no, by design** | §Z3.3: "only a controller's argv prefix is client-supplied". The target was never trusted |
| `WORKER` | the same for `A-10`; an off-CPU adapter's backend import happens in the target's own environment | **no, by design** | the signed harness's off-CPU adapter admission is its own bounded control review |

> **Proof that a contaminated controller or worker cannot affect process,
> capacity, custody or scientific validity.**
>
> | Vector | Why it is closed |
> |---|---|
> | process | it holds **no PID authority**: the PCS created it, the PCS is its parent, the PCS is its only reaper, and it can name no PID of any other process. It cannot signal, wait for, or reap anything in the tree |
> | lock | it never receives the `SPAWN.lock` descriptor (§T4.2); a controller/worker fd map contains only its own ctrl and status ends |
> | capacity | K1's ceiling is enforced by the **supervisor-mediated transport** on the signed output path with a fixed ceiling and one-write/one-hash accounting; a worker cannot write outside the bound it is given, and the bound is installed before it runs |
> | custody | the §N2.3 P1–P7 complete-custody proof and the §V217.1 object-bound observation with both revalidation barriers are performed by the supervisor under `T_RUNTIME.lock` over objects the worker cannot make the supervisor mis-observe |
> | scientific validity | every worker result reaches science only through a durable `SETTLEMENT.json` bound to a `RESULT_MANIFEST.json` by hash, under the carried selector; a malformed or absent object is `MALFORMED`-dominant or absent, never a result |
> | the residual | a worker that consumes wall-clock or writes garbage produces **invalidity or a quarantined output**, both of which are signed infrastructure facts and neither of which is a scientific outcome |
>
> This is the "explicitly proved unable to affect" branch T3 permits, and it is
> claimed **only** for controllers and workers.

---

## T4. PCS lifetime, fd and custody totality

### T4.1 The complete process tree

```text
[0] contaminated caller  (generic_harness.py __main__, any runtime state)
     │ posix_spawn, §V21101.3 (carried)
     ▼
[1] PCS  scripts/officina_process_control_bootstrap.py, -I -S -E -P
     │   owns: SPAWN.lock, the four singleton records, all four bootstrap
     │         channels, the supervisor socket (PCS end), the handle table,
     │         and EVERY pid in the system
     ├─ c4 fork ─▶ [2] middle child (pid_mid)
     │                 │ m7 fork ─▶ [3] grandchild ─ execve ─▶ role bootstrap
     │                 │                                        (SUPERVISOR)
     │                 └ m9 _exit ; [3] re-parented to init
     ├─ posix_spawn(setsid=True) ─▶ [4] role bootstrap (WATCHDOG)
     ├─ posix_spawn(setsid=True) ─▶ [5] role bootstrap (CONTROLLER)  ×n
     └─ posix_spawn(setsid=True) ─▶ [6] role bootstrap (WORKER)      ×n

Direct-child / reaper relation, the load-bearing column:
   [1] is the direct parent and the SOLE reaper of [2], [4], [5], [6].
   [3] is a child of [2] until m9, then of init, which reaps it.
   [0] may reap only [1].
   NO other reaper relation exists anywhere in the tree.
```

§V2110.2.3's process-boundary proof therefore extends to **every** role: a
`wait` in the supervisor's contaminated interpreter ranges over the supervisor's
own children, which is the empty set.

### T4.2 Descriptor ownership at every state

**PCS-side, for the generation's life:**

| Slot | Contents | Closed when |
|---|---|---|
| 3, 4 | caller request read / reply write | after the `SPAWN_SUPERVISOR` reply is written |
| 5, 6, 7, 8 | runtime root, package root, own source, interpreter — carried | at PCS exit; 7 and 8 are retained because every later `execve` uses them |
| `sv_sock` | supervisor socket, PCS end | at `SHUTDOWN` or PCS exit |
| per handle | the **role's** ends of its ctrl/status/update/ack pipes | when the handle reaches `REAPED` |

**Role-side fd maps, by role, all pinned:**

| Role | 3 | 4 | 5 | 6 | 7 | 8 | 9 |
|---|---|---|---|---|---|---|---|
| `SUPERVISOR` | `SPAWN.lock` (non-`CLOEXEC`, carried) | `boot` write | `T_ROLE_FD_ROLESRC` | `T_ROLE_FD_PCS` (the seqpacket peer) | `T_ROLE_FD_SELF` | `T_ROLE_FD_SRCDIR` | `T_ROLE_FD_INTERP` |
| `WATCHDOG` | update read | ack write | `T_ROLE_FD_ROLESRC` | — | `T_ROLE_FD_SELF` | `T_ROLE_FD_SRCDIR` | `T_ROLE_FD_INTERP` |
| `CONTROLLER` / `WORKER` | ctrl request read (`T_CTRL_FD_LOW`, carried) | ctrl reply write (`T_CTRL_FD_HIGH`, carried) | `T_ROLE_FD_ROLESRC` | status write | `T_ROLE_FD_SELF` | `T_ROLE_FD_SRCDIR` | `T_ROLE_FD_INTERP` |

Also add `T_ROLE_FD_PKGROOT = 10` for `A-7` in every role. §Z3.3's
`T_CTRL_FD_LOW = 3` / `T_CTRL_FD_HIGH = 4` are **preserved exactly** for
controllers and workers, which is why those two roles use 3 and 4 for their ctrl
pair and the supervisor does not.

The supervisor's ends of a controller's ctrl/status pipes are **never inherited
by the supervisor**; they arrive as `SCM_RIGHTS` ancillary data (§T1.4).

### T4.3 The handle

```text
handle_id → { pid, start_identity, pgid_or_null, role, generation_id,
              fd_bundle (the PCS-side role ends), state, ownership,
              fd_delivery }
  state      ∈ SPAWNED | STOPPED | RUNNING | REAPED
  ownership  ∈ OWNED | CONTRADICTED | REAPED       (carried §V218.3.1)
  fd_delivery∈ PENDING | CONFIRMED | UNCONFIRMED
Invariants: ids are never reused; RELEASE_HANDLE requires REAPED; SIGNAL_*
requires ownership OWNED; SIGNAL_GROUP additionally requires a kernel-verified
group; no wait site runs after REAPED.
```

### T4.4 Mapping the signed objects onto handles, without changing their meaning

| Signed object | Before | Under the PCS | Scientific meaning |
|---|---|---|---|
| `t-spawn-intent.v1` | supervisor writes it, then `Popen`s | supervisor writes it **first**, then `SPAWN_ROLE` names it by id; the PCS reads and rebuilds §Z3.3's argv | **unchanged** |
| `t-process-claim.v1` | written after `waitpid(WUNTRACED)` proves the stop | written after `AWAIT_STOP` returns `STOPPED` + `start_identity` | **unchanged**: the same fact, obtained by the same syscall in a clean process |
| lease / `START` | unchanged | unchanged | unchanged |
| watchdog registration and freeze observations | unchanged | unchanged | unchanged |
| B1 client journal | unchanged | unchanged; the **PCS journal is a separate control-plane journal** (§T2.6) and carries no scientific field | unchanged |
| K1 accounting | unchanged | unchanged | unchanged |

### T4.5 What "relocate the primitive" does and does not cover

Every carried primitive has a named PCS operation with a unique carried consumer:

| Carried primitive | PCS operation | Unique carried consumer |
|---|---|---|
| `Popen` of a controller/worker (§W2.5) | `SPAWN_ROLE` | §Z3.3's adapter duties, then the claim |
| `waitpid(WNOHANG\|WUNTRACED)` self-stop (§W2.5) | `AWAIT_STOP` | the `t-process-claim.v1` write |
| `kill` on a role (§W2.4, §U2.5) | `SIGNAL_ROLE` | the death proof and §U6.3 removal |
| `killpg` on a verified group (§U2.5, §W3.3) | `SIGNAL_GROUP` | freeze and the stage-2 route |
| `waitpid` death proof | `REAP_ROLE` | `T1`/`T2`, §U6.1 P3 |
| `os.fork` of the watchdog (§W2.1) | `SPAWN_WATCHDOG` | C1's registration and ack |

> **Where the phrase does not hold, and this is the finding of §T7.** Two
> carried **detectors** have no PCS operation and are not relocations:
> §W3.5's "Supervisor death | watchdog's `getppid()` ≠ recorded" and
> §W3.5's "Watchdog exits / identity mismatch | `waitpid` on own child". Both
> depend on a parent–child relation the PCS removes. §T7.2 states the exact
> loss.

### T4.6 PCS crash, and the prohibition on unsafe restart

```text
PCS death (crash, kill, or default-action signal) at ANY point:
  - the kernel closes every descriptor it held: SPAWN.lock's reference, the
    supervisor socket, every role-side pipe end it retained;
  - every live role and pid_mid is re-parented to init, which reaps them;
  - the supervisor observes PEER_EOF on its channel and has lost ALL process
    authority: it can create nothing, signal nothing, wait for nothing;
  - the PCS journal's last entry may be ACCEPTED (a syscall may or may not have
    happened) — this is exactly the inconclusive case;
  - the four singleton records survive and are governed by the next attempt's
    carried §U6.1 P0–P3 preflight; NO record naming a possibly-live process is
    removed without a signed death proof.

PROHIBITION, normative:
  A NEW PCS MUST NEVER ADOPT A LIVE GENERATION. It cannot: it is not the parent
  of any surviving role, so it can neither wait for nor safely signal one, and
  the carried ownership rules forbid signalling under an inconclusive premise.
  A PCS that starts and finds a journal whose generation is not terminal MUST
  refuse with GENERATION_NOT_ADOPTABLE, take no action, and exit.
  The generation routes to §T4.7 whole-run invalidity.
```

> **This is a new mandatory single point of failure.** Before the PCS, a
> supervisor crash was recoverable by the signed §W2.9 two-phase takeover. A PCS
> crash is **not** recoverable, because process authority cannot be transferred
> to a process that is not the parent. This is stated plainly, is one of the
> reasons for cell P, and is **not** presented as an acceptable cost that the
> author may choose alone.

### T4.7 Invalidity routing — no invented success or resource fact

Every path in §T1.6, §T2.4, §T2.6, §T4.6 and the carried `NO_REPLY` route ends
here:

```text
An operation whose control outcome cannot be established, or a generation whose
PCS is gone, is a PROCESS fact:
  - it settles through the signed T_PROCESS_INVALID recovery disposition and the
    signed §4c(c)/§4d unknowable route, with invalidity dominance applying
    exactly as carried;
  - it is NEVER T_PROCESS_CLOSED, never a completion, never a capacity fact,
    never a custody disposition, never an E1/E2/E3 fact, and never a Q/C input;
  - no resource value is inferred from it, and no scientific outcome is
    produced or predicted;
  - the phrase "its own user" remains withdrawn (§V21101.7.5, carried).
```

### T4.8 The remaining cuts

| Cut | Continuation |
|---|---|
| supervisor crash / channel EOF, PCS alive | the PCS holds every handle; it enters the carried non-returning reaper state for each live role rather than abandoning it; the singleton is not freed; the next attempt sees the records under §U6.1 |
| caller crash | the PCS is unaffected (§V21101.7.2, carried); its reply write yields `EPIPE`, changing no record or decision |
| watchdog crash | the PCS's `REAP_ROLE` observes it; the supervisor learns through the ack-absence rule of §W3.5, unchanged in its **timeout** half; its `waitpid`-on-own-child half is gone (§T7.2) |
| role crash | `REAP_ROLE` returns `REAPED_POSITIVE`; the carried claim/lease/settlement routes govern |
| `SHUTDOWN` with live handles | `REFUSED`/`HANDLES_LIVE`; nothing released |
| resource stop (`SIGSTOP` on a role) | `AWAIT_STOP`/`REAP_ROLE` see `(0,0)`; the carried TERM→KILL schedule applies through `SIGNAL_ROLE`; a stopped role holding a fork-shared reference is the carried §U2.7 A3 residual |
| `STRUCTURAL_VIOLATION` at any PCS wait site | carried §V2110.4.1: never death, `CONTRADICTED`, no further signal, no record touched |

---

## T5. Imports, primitives, and the verifier

### T5.1 The corrected closure

> **The PCS root imports exactly six modules: `{os, sys, _signal, time, fcntl,
> _socket}`.** The role bootstrap root imports exactly two: `{os, sys}`.

| Module | Kind | Python import closure | Task? | At-fork? | Handler/hook? |
|---|---|---|---|---|---|
| `os` | wrapper over built-in `posix` | `sys`, `abc`, `stat`, `_collections_abc`, `posixpath`, `genericpath` | no | defines `register_at_fork`, never calls it | no |
| `sys`, `time`, `fcntl`, `_signal` | built-in | none | no | no | no |
| **`_socket`** | **built-in C** | **none** | **no** | **no** | **no** — it defines socket types and constants and starts nothing at import |

**`array` and `struct` are deliberately not added.** `int.to_bytes` and
`int.from_bytes` are builtin `int` methods requiring no import, and the byte
order is pinned `"little"` because the platform is pinned `x86_64` (§T1.3).

> **Disclosure: `_socket.socket` has a finalizer that closes its descriptor.**
> That is a *close*, never a wait, a signal, or a task creation, so it cannot
> reap or mis-signal. It is nonetheless a finalizer in the closure, and it is
> managed by two pinned rules: every socket object lives in a module-level slot
> for the whole generation, and **every received descriptor is handled as a
> plain `int`** and closed exactly once with `_close`, never wrapped.

### T5.2 Added primitive bindings

Appended to §V21101.1.3's block, each validated by the §V21101.1.4 table's
built-in-callable row with `__self__.__name__ == "_socket"`:

```text
_socketpair = _socket.socketpair   _sendmsg  = _socket.socket.sendmsg
_recvmsg    = _socket.socket.recvmsg
_CMSG_SPACE = _socket.CMSG_SPACE   _CMSG_LEN = _socket.CMSG_LEN
_AF_UNIX, _SOCK_SEQPACKET, _SOL_SOCKET, _SCM_RIGHTS,
_MSG_CMSG_CLOEXEC, _MSG_CTRUNC, _MSG_TRUNC            # int constants
_fcntl = fcntl.fcntl               # §T5.3
_F_GETFL, _O_ACCMODE               # int constants
```

`_sendmsg`/`_recvmsg` are unbound method descriptors of the `_socket.socket`
type; their identity row requires `type(x) is type(type(len).__call__)`-class
method-descriptor semantics — pinned in the table as "`method_descriptor` whose
`__objclass__` is `_socket.socket` and whose `__qualname__` is
`socket.sendmsg` / `socket.recvmsg`". This is a **fourth kind** added to the
three of §V21101.1.4, and it exists precisely because a single universal
predicate was already shown to be invalid.

### T5.3 The corrected read-only test

> **Deleted:** §V21101.2.2's `P-s5` — "a `_read` of zero bytes must succeed and
> a `_write` must raise `OSError`". A zero-byte read succeeds on many
> descriptors regardless of access mode, and a failing write proves nothing
> about `O_ACCMODE`. It was not an access-mode test.

```text
P-s5'.  fl := _fcntl(fd, _F_GETFL)
          any OSError                        ⇒ SOURCE_FD_UNUSABLE
        require type(fl) is int
        require (fl & _O_ACCMODE) == _O_RDONLY
          otherwise                          ⇒ SOURCE_NOT_READONLY
  with _F_GETFL == 3, _O_ACCMODE == 3, _O_RDONLY == 0 on the pinned platform,
  each an int validated by the §V21101.1.4 constant row.
```

### T5.4 Verifier and manifest changes

```text
CHANGE 1'  PRODUCTION_ROOTS becomes FIVE entries:
             scripts/officina_activate_t.py
             scripts/verify_officina_active.py
             src/philosophia/officina/generic_harness.py
             scripts/officina_process_control_bootstrap.py
             scripts/officina_role_bootstrap.py            # ADDED here
CHANGE 2'  MODULE_SCOPED_ABSOLUTE_IMPORTS:
             process_control_bootstrap → {os, sys, _signal, time, fcntl, _socket}
             role_bootstrap            → {os, sys}
             generic_harness           → the sixteen signed members, containing
                                         neither `signal` nor `_signal` nor
                                         `_socket` nor `sys`
           ALLOWED_ABSOLUTE_IMPORTS gains `_socket`; it already gains `sys` and
           `_signal` from v2.1.10.1. It never gains `signal`.
CHANGE 3'  the closed AST grammar, amended:
  S-1'  the PCS root has exactly six Import nodes; the role root exactly two
  S-7'  forbidden-symbol list gains: `socket` (the wrapper), `array`, `struct`,
        `PYTHONPATH`, `putenv`, `environ` (as a store target), `execv`,
        `execvp`, `system`, `SO_PASSCRED`, `SCM_CREDENTIALS`
  S-14  (new) every `_recvmsg` call passes `_MSG_CMSG_CLOEXEC` in its flags
        argument                                ⇒ "recvmsg without CMSG_CLOEXEC"
  S-15  (new) every `_recvmsg` ancillary buffer argument is exactly
        `_CMSG_SPACE(12)`                       ⇒ "ancillary buffer differs"
  S-16  (new) no integer-valued field of any wire record is derived from a
        descriptor: `fileno`, `detach`, and any `.fileno()` call are forbidden
        in the record-building functions       ⇒ "fd number in wire record"
  S-17  (new) the role root contains exactly one `sys.path` assignment, of the
        form `sys.path[:] = [<one literal-prefixed /proc/self/fd/ string>]`,
        and no other `sys.path` mutation        ⇒ "role path insertion differs"
CHANGE 5'  the manifest's `root_source_sha256` covers all FIVE roots.
```

---

## T6. Launcher and object provenance, generalized

### T6.1 The hoist and collision proof, for an arbitrary target set

§V21101.3.3's algorithm is restated once, generally, and used by both the caller
(six descriptors → 3…8) and the PCS (per-role descriptor sets → the tables of
§T4.2).

```text
HOIST(logical_fds, target_set):
  let T := max(target_set)
  for each L in a fixed order:
      while h[L] <= T:  n := _dup(h[L]); retain the old; h[L] := n
  close every retained intermediate and every original <= T
  POSTCONDITION: all h[L] > T and pairwise distinct   ⇒ else LAUNCH_FD_HOIST_FAILED
FILE_ACTIONS := [ (DUP2, h[L], target[L]) for L in the fixed order ]
              + [ (CLOSE, h[L])           for L in the fixed order ]
```

**Collision-freedom, for any target set.** Every source is `> max(target_set)`
and every destination is `<= max(target_set)`, so no `DUP2` destination can
overwrite a source a later action still needs. All `CLOSE`s follow all `DUP2`s,
so no source is closed early. `POSIX_SPAWN_DUP2` clears close-on-exec on the
destination, so exactly the mapped descriptors survive the exec and every other
`O_CLOEXEC` descriptor is closed by it. A leaked non-`O_CLOEXEC` descriptor is
caught by the receiving root's `/proc/self/fd` check (`P-f`, `A-5`).

### T6.2 Identity and hash obligations

| Object | Run-time obligation | Deploy-time obligation |
|---|---|---|
| interpreter | object-bound `/proc/self/fd/<N>`, regular, not group/other writable, `O_RDONLY` by `F_GETFL` | pinned identity at `P-b` (`sys.version_info`, `sys.implementation`, `os.uname()`) |
| PCS source | `P-s` + the fd 6 ↔ fd 7 mutual `(st_dev, st_ino)` binding (carried) | `root_source_sha256` |
| **role-bootstrap source** | `A-6` + `A-7`'s mutual binding against the package root | `root_source_sha256` |
| role module (`generic_harness.py`) | `A-11`'s `(st_dev, st_ino)` check on the imported `__file__` | `root_source_sha256` |
| package root | `P-p1`–`P-p3` (carried) | the manifest's reachable-source closure |

**A wholly fabricated caller tree cannot produce an authorized response.** Such
a tree runs a program that is not the reviewed PCS, so it produces no
`t-pcs.v1` record any reviewed harness accepts: the supervisor role that would
consume one is itself reached only through `A-1`…`A-13`, which bind the role
module's inode to the package root that contains the executing role bootstrap.
A fabricated tree therefore yields a fabricated supervisor talking to a
fabricated PCS — a closed system with **no** authority under this contract and
no path into the signed journal, capacity ledger, custody dispositions, or
settlement objects, all of which are written only by a role reached through the
reviewed chain. Byte provenance remains the deploy-time obligation
(§V21101.5.4, carried), with its limit unchanged and unsoftened.

---

## T7. The governance boundary — and the cell this layer cannot decide

### T7.1 The question, answered

> **Is the PCS wire, descriptor transport, handle table, and isolated role root
> (1) a mechanical implementation of already-selected supervisor policies, or
> (2) a new architecture requiring its own signed engineering amendment?**
>
> **Answer: (2).** Three signed surfaces are changed in substance, not
> implemented. The engineering above is complete and bit-exact; the decision to
> adopt it is not the author's.

### T7.2 The regression I introduced, stated against myself

v2.1.10.1 §V21101.6.5 asserted that an `execve`'d, PCS-parented watchdog
"**strengthens C1 rather than weakening it**". **That claim was wrong and is
withdrawn.** It was right about the address space and silent about the parent.

Carried v2.1 §W3.5 gives supervisor death **two** independent detectors, and
watchdog death one:

| Signed row | Mechanism | Under the PCS |
|---|---|---|
| "Supervisor death \| watchdog's `getppid()` ≠ recorded, **or** update pipe EOF" | two detectors | the watchdog's parent becomes the **PCS**, so `getppid()` no longer changes when the supervisor dies. **One of the two detectors is deleted**; only pipe EOF survives |
| "Watchdog exits / identity mismatch \| `waitpid` on own child, or parent-check failure" | supervisor reaps its own watchdog | the supervisor can no longer `waitpid` the watchdog; it becomes a `REAP_ROLE` round trip, so watchdog-death detection now **depends on the PCS channel being alive** |

Deliberately halving a redundant safety detector on the **C1-selected** watchdog,
and making the remaining watchdog-death detector depend on a new component, is a
change to a signed cell. It may well be the right trade — the exec'd watchdog
genuinely gains a capability-free address space — but **it is a trade, and the
author must not make it unilaterally.**

### T7.3 The three signed surfaces affected

| Cell | Change | Why it is not mere implementation |
|---|---|---|
| **C1** (dedicated freezer watchdog) | the watchdog's parent, its death detector, and one of two supervisor-death detectors change | §T7.2 |
| **D1** (no idle exit) | the supervisor's ability to act is now bounded by the life of a **new mandatory resident process**, and a PCS crash is unrecoverable with an explicit no-adoption prohibition (§T4.6). D1's ground — "no supervisor waits on `SPAWN.lock`" — is intact, but the *availability* model it sits in is new | a new single point of failure that no signed cell contemplated |
| **B1** (durable journal, ack, redelivery) | a **second** control-plane journal is introduced, and **fd-bearing responses are explicitly not retry-stable** (§T2.6) | a narrowing of a signed promise plus a new durable object class |

Additionally, and as engineering rather than cells: `PRODUCTION_ROOTS` goes to
**five**; `_socket` joins the allowlist; **`SCM_RIGHTS` introduces capability
transfer**, a class of mechanism no prior layer's control channel had — every
earlier channel was a byte pipe or FIFO carrying no capability at all.

### T7.4 Superseded sentences (extending §V21101.10)

| # | Locus | Superseded wording | Scope |
|---|---|---|---|
| 37 | v2.1.10.1 §V21101.6.3 | the `ctrl-fd pair` and "sealed update/ack pipe descriptors" operands | replaced by `SCM_RIGHTS`; no fd integer in any field |
| 38 | v2.1.10.1 §V21101.6.3 | "the record grammar, field character classes, and framing are unchanged" | **deleted as false** |
| 39 | v2.1.10.1 §V21101.5.3 | `b"-P"` alone and `{ b"PYTHONPATH": … }` | replaced by the isolated role root; `PYTHONPATH` deleted |
| 40 | v2.1.10.1 §V21101.6.5 | "**This strengthens C1 rather than weakening it.**" | **withdrawn**; §T7.2 |
| 41 | v2.1.10.1 §V21101.2.2 | `P-s5`'s zero-byte-write access-mode test | replaced by `F_GETFL & O_ACCMODE` |
| 42 | v2.1.10 §V2110.9 row 20 / v2 §V2.10 | "Sole root: `generic_harness.py`" (already four roots) | **five** roots |
| 43 | v2.1.10.1 §V21101.6.2 | "relocation of the primitive, not a change of semantics" | **qualified**: true for the six primitives of §T4.5, false for the two detectors of §T7.2 |
| 44 | v2.1.10.1 closure | `READY_FOR_OFFICINA_SUPERVISOR_V2_1_10_1_FINAL_XY_CONFIRMATION` | **superseded**: the engineering stands, the readiness does not |

### T7.5 Cell P — the exact bounded choice, presented and not decided

> **A new author-choice cell is required before any of this may be reviewed for
> acceptance. Exactly one option must be signed. Every option is fully specified
> above; none decides a scientific or resource value; none moves a K1 constant,
> an E1/E2/E3 value, a T band, a capacity ceiling, a custody rule, or any Q/C
> boundary.**

```text
P1: I_SELECT_SUPERVISOR_PROCESS_AUTHORITY_P1_FULL_PCS_MEDIATION
    Adopt §T1–§T6 in full.
    Gains  : every PID in the system is held by a clean, constructed process;
             the supervisor holds handles only and cannot express a PID; the
             watchdog gains a capability-free address space by construction.
    Costs  : C1's `getppid()` supervisor-death detector is DELETED and
             watchdog-death detection depends on the PCS channel (§T7.2);
             the PCS is a mandatory resident process whose loss is an
             unrecoverable whole-generation invalidity (§T4.6);
             B1 gains a second journal and fd-bearing responses are not
             retry-stable (§T2.6);
             five production roots; `_socket` and SCM_RIGHTS capability
             transfer enter the contract.

P2: I_SELECT_SUPERVISOR_PROCESS_AUTHORITY_P2_PCS_WITH_SUPERVISOR_PARENTED_WATCHDOG
    Adopt §T1–§T6 for the supervisor, controllers and workers, but the WATCHDOG
    remains a supervisor in-process fork, exactly as signed §W2.1 specifies.
    Gains  : C1's `getppid()` detector and the supervisor's `waitpid`-on-own-
             child watchdog detector are BOTH PRESERVED unchanged.
    Costs  : the watchdog is created by a contaminated interpreter, so its
             creation is not clean-constructed. Bounded: the watchdog holds no
             lock, no capability, no PID authority over any other process, and
             writes only freeze observations under the signed C1 rules — but the
             bound is an argument, not a construction.

P3: I_SELECT_SUPERVISOR_PROCESS_AUTHORITY_P3_DEFER_SUPERVISOR_AUTHORITY
    Adopt NONE of §T1–§T4. The PCS scope stays exactly v2.1.10's: the isolated
    bootstrap owns pid_mid and the supervisor bootstrap only, and then exits.
    Gains  : no new signed surface, no new root beyond v2.1.10's fourth, no new
             journal, no single point of failure, no C1 change.
    Costs  : the supervisor's own Popen/waitpid/kill/killpg/watchdog-fork defect
             remains OPEN and must be carried as an explicitly named Major
             defect to its own signed layer. §T5's import/fcntl corrections and
             §T3's isolated role root MAY still be adopted independently, since
             neither depends on the PCS.
```

**This layer selects none of them.** The closure emits
`BLOCKED_OFFICINA_SUPERVISOR_V2_1_10_2_AUTHOR_CELL`.

**Why `I_ACCEPT_OFFICINA_SUPERVISOR_CONTROL_CHANNEL_AMENDMENT` does not cover
this by itself.** That token was framed against an amendment whose control
channel carried **bytes and no capability**, whose watchdog was a supervisor
fork, and whose failure model had no unrecoverable resident component. Claiming
it silently extends to a capability-passing wire, a second journal, a new
mandatory process, and a deleted C1 detector would be exactly the over-reach the
last four review rounds rejected. After cell P is signed, that token remains the
right instrument for the resulting composite — but not before.

---

## T8. Tests

Replaced: §V21101.8.2 rows **273R** (argv/env now per-root), **293R**
(no `PYTHONPATH`), **315** (`F_GETFL` test), **329**–**332** (the handle and
channel rows now name the socket protocol). Added:

| # | Test |
|---|---|
| 353 | no wire record in either protocol contains a descriptor number, PID, path, argv, signal number, or symbol; static over the record builders and `S-16` |
| 354 | `_socketpair(AF_UNIX, SOCK_SEQPACKET, 0)` is created before the `c4` fork; the peer end reaches the role at `T_ROLE_FD_PCS` and nowhere else |
| 355 | a `sendmsg` of a 4096-byte payload is delivered whole; a 4097-byte payload is refused before send |
| 356 | the fd vector for each opcode/status equals the §T1.4 row exactly; every other count or type is `ANCILLARY_VIOLATION` |
| 357 | `MSG_CMSG_CLOEXEC` is passed on every `recvmsg`; received descriptors have `FD_CLOEXEC` set with no window |
| 358 | `MSG_CTRUNC`, `MSG_TRUNC`, a non-`SCM_RIGHTS` ancillary item, a `cdata` length not a multiple of 4, and an over-long `cdata` each close every received fd and route to invalidity |
| 359 | after a violation, `/proc/self/fd` contains exactly the pinned set: no leaked descriptor from a truncated ancillary item |
| 360 | no double close and no leak at every §T1.5 cut, including sender death mid-send and receiver death with descriptors buffered |
| 361 | the ownership table of §T1.5 holds at every point, including the unconditional post-send close of the supervisor's ends |
| 362 | ack timeout marks `FD_DELIVERY_UNCONFIRMED` and the PCS **never** re-sends descriptors |
| 363 | replay of an `ACCEPTED` id yields `OPERATION_INCONCLUSIVE` with no syscall; replay of `COMPLETED`/`ACKED` yields the recorded record with `fds_redelivered = 0` and no descriptors |
| 364 | the J1–J6 order holds and every crash cut behaves as §T2.6 tabulates |
| 365 | one outstanding request at a time; an out-of-order or unmatched response is `TRANSPORT_STRUCTURAL` |
| 366 | unknown opcode, field count, handle, state, and wrong generation each yield `INVALID` with no side effect |
| 367 | `SHUTDOWN` with a live handle refuses and releases nothing; with none, it closes, releases the lock, and exits |
| 368 | supervisor EOF puts the PCS into the non-returning reaper state for every live handle rather than abandoning one |
| 369 | the role bootstrap refuses at each of `A-1`…`A-13` with nothing written |
| 370 | `os.environ` is empty in every role; `PYTHONPATH` appears nowhere in the repository's launch paths |
| 371 | `sys.path[:]` is exactly one object-bound entry after `A-9`; `A-11` rejects a role module substituted after `A-7` |
| 372 | with `-S`, a `.pth`, `sitecustomize`, and `usercustomize` present on the host affect no role process |
| 373 | the controller/worker non-isolation proof of §T3.4 holds for each of its six vectors |
| 374 | `PRODUCTION_ROOTS` has five entries; the scoped map gives each root exactly its set; `generic_harness.py` imports none of `signal`, `_signal`, `_socket`, `sys` |
| 375 | `S-14`…`S-17` each reject a bit-exact negative fixture and accept a positive one |
| 376 | the `F_GETFL & O_ACCMODE` test rejects a write-open and read-write-open descriptor that the deleted zero-byte-write test would have accepted |
| 377 | `_socket`'s import closure is empty; no task, at-fork registration, or hook at import; the socket-object finalizer never closes a descriptor the bootstrap still owns |
| 378 | `int.to_bytes`/`from_bytes` round-trip the fd vector byte-identically to a native `int[3]` on the pinned platform; `array` and `struct` appear nowhere |
| 379 | the generalized hoist is collision-free for every arrangement, for both the caller's target set and every role target set |
| 380 | `T_CTRL_FD_LOW`/`T_CTRL_FD_HIGH` remain 3/4 for controllers and workers |
| 381 | the PCS is the direct parent and sole reaper of `pid_mid` and every role; a wildcard wait in the supervisor reaches none of them |
| 382 | PCS death: `init` adoption, journal `ACCEPTED` state, no record removed without proof, supervisor authority lost at EOF |
| 383 | a PCS started against a non-terminal generation refuses `GENERATION_NOT_ADOPTABLE` and acts on nothing |
| 384 | every §T4.7 path settles through `T_PROCESS_INVALID` and the §4c(c)/§4d unknowable route and produces no success, resource, or scientific fact |
| 385 | the §T4.4 mapping preserves the scientific meaning of every signed object |
| 386–404 | one row per §T7.4 supersession (37–44) and per cell-P option, asserting the exact scope and the paired preserved property |

---

## T9. No-regression, platform, and weakest points

**Platform.** Unchanged: `Linux x86_64, CPython 3.12.3` (§V2110.6, carried).
`AF_UNIX`/`SOCK_SEQPACKET`/`SCM_RIGHTS`/`MSG_CMSG_CLOEXEC` and the 4-byte
little-endian `int` packing are justified **only** inside that scope; every
other architecture is refused at `P-a` before any of this code is reachable.

**No-regression.** Everything listed in §V21101.9.1–§V21101.9.2 carries
unchanged, plus §V21101.1–§V21101.5 in full, with the four corrections named in
§V211002.0. The A3 same-UID filesystem residual is untouched and nothing here
claims filesystem exclusion. No scientific or resource boundary moves.

**Edit surface.** As §V21101.9.3, plus `scripts/officina_role_bootstrap.py`
(new, does not exist) and the five-root manifest.

**Weakest points, against myself.**

1. **`SCM_RIGHTS` portability.** The whole transport is Linux-specific;
   `SOCK_SEQPACKET` over `AF_UNIX` is a Linux extension, and
   `MSG_CMSG_CLOEXEC` is Linux-only. The platform pin makes this consistent, but
   it deepens the dependence on one kernel.
2. **Received-fd `CLOEXEC` behaviour** rests on `MSG_CMSG_CLOEXEC` being atomic
   with installation. If it were not, there is a window I do not otherwise
   close, and the static rule `S-14` cannot detect a kernel that ignores the
   flag.
3. **The PCS is a single point of failure** whose loss is an unrecoverable
   whole-generation invalidity, with an explicit no-adoption prohibition. That
   is the correct fail-closed direction, but it is strictly worse availability
   than the signed §W2.9 two-phase takeover it displaces.
4. **Protocol/journal coupling.** A second durable journal on a second control
   plane doubles the crash-cut surface, and fd-bearing responses are explicitly
   **not** retry-stable — a narrowing of B1's promise that I could not avoid
   without inventing capability accounting.
5. **`_socket.socket`'s finalizer** is a finalizer in a closure whose value is
   having none. It can only close, but it is there.
6. **The method-descriptor identity row** (`sendmsg`/`recvmsg`) is a fourth kind
   in a table that already exists because a universal predicate was wrong. A
   fifth kind would be a signal that the table approach is failing.
7. **I have now twice shipped a layer whose governance conclusion was wrong**
   (v2.1.10.1 claimed `READY` while carrying an unimplementable transport and a
   withdrawn C1 claim). A reviewer should weight this layer's own
   self-assessment accordingly, which is part of why it stops at a cell rather
   than declaring readiness.
8. **Cell P's options are not obviously exhaustive.** A fourth architecture — a
   short-lived clean process-control instance per operation — was considered and
   is not offered, because handles would not survive across instances and the
   PID-holding property would be lost between calls. If a reviewer sees a fifth
   option, the cell is under-specified.

---

## T10. The bounded questions

At most three per line. Both lines must recompute the digests of v2.1.10,
v2.1.10.1 and this file, and must treat all three author closures as untrusted.
**These questions are about whether the engineering is right and whether cell P
is correctly framed — not a request for acceptance review, which cannot begin
until P is signed.**

### For the X line

> **X-Q1 — transport.** Is §T1 implementable exactly as written on the pinned
> platform? Attack: `_socketpair(AF_UNIX, SOCK_SEQPACKET, 0)` and the
> `_socket`-only surface; the 4-byte little-endian `int` packing via
> `int.to_bytes`/`from_bytes` as a faithful native `int[]`; `CMSG_SPACE(12)`
> and the 3-descriptor cap; `MSG_CMSG_CLOEXEC` atomicity; the `MSG_CTRUNC`
> handling and the `/proc/self/fd` sweep; and the ownership table's claim of no
> leak and no double close at every cut, including buffered descriptors on peer
> death.
> **X-Q2 — protocol and isolation.** Is `t-pcs.v1` total — correlation, single
> outstanding request, the J1–J6 order and every crash cut, the replay rule, and
> the explicit non-retry-stability of fd-bearing responses? And does §T3's role
> bootstrap genuinely remove the `PYTHONPATH`/`site` contamination for
> `SUPERVISOR` and `WATCHDOG`, with §T3.4's six-vector proof actually holding for
> `CONTROLLER`/`WORKER`?
> **X-Q3 — governance.** Is §T7 correct that the PCS changes signed surfaces
> rather than implementing them — in particular that parenting the watchdog to
> the PCS deletes §W3.5's `getppid()` supervisor-death detector? Are cell P's
> three options exclusive, complete, and free of any scientific or resource
> decision? If you judge that no cell is needed, say so and say why the existing
> token truthfully covers a capability-passing wire, a second journal, and a new
> unrecoverable resident process.
>
> Verdict line 1 exactly `CONFIRM_OFFICINA_SUPERVISOR_V2_1_10_2_CELL_FRAMING_X`
> or `REVISE_OFFICINA_SUPERVISOR_V2_1_10_2`. Static review only; create exactly
> one review file; authorize nothing.

### For the Y line

> **Y-Q1 — single-valuedness.** Are T1–T6 each single-valued and implementable,
> with no surviving alternative, no prose extension of a closed grammar, and no
> field anywhere carrying a descriptor, PID, path, argv, or signal number? Check
> that the caller channel and the supervisor channel are cleanly separated and
> that the carried six-field grammar is scoped rather than reinterpreted.
> **Y-Q2 — totality and invalidity.** Is §T4 total — the process/fd tree, the
> handle bindings, PCS crash with the no-adoption prohibition, supervisor EOF,
> watchdog and role crashes, shutdown with live handles — and does every
> unknown outcome route through the **signed** `T_PROCESS_INVALID` and §4c(c)/§4d
> semantics without inventing a success or resource fact? Is the §T2.6 exception
> to B1's retry-stability stated honestly enough?
> **Y-Q3 — the cell.** Do you agree the PCS affects C1, D1 and B1 in substance?
> Is P1/P2/P3 the right bounded partition, and is P2's watchdog carve-out a
> genuine alternative rather than a token one? If you judge that this layer
> should have declared `READY` instead, say so; if you judge that even the cell
> is insufficient and the whole PCS needs a separate signed layer of its own,
> say that too.
>
> Verdict line 1 exactly `CONFIRM_OFFICINA_SUPERVISOR_V2_1_10_2_CELL_FRAMING_Y`
> or `REVISE_OFFICINA_SUPERVISOR_V2_1_10_2`. Static review only; create exactly
> one review file; authorize nothing.

---

`I_ACCEPT_OFFICINA_SUPERVISOR_CONTROL_CHANNEL_AMENDMENT` remains **not
signable**. Cell P is unsigned and no option is selected. No independent review
of v2.1.10, v2.1.10.1, or this layer has occurred.
`successor/officina/runtime/` contains only `T_RUNTIME.lock`;
`successor/officina/runtime_control/` does not exist;
`successor/officina/T_ENVELOPE.json` remains `"activated": false`. T remains
`NOT_ACTIVATED`; the programme claim remains `OPEN`.
