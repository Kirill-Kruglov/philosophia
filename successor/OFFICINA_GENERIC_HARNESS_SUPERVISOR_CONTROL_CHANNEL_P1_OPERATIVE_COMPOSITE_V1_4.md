# Officina supervisor and control channel — P1 operative composite, version 1.4

**This document is the single, complete, self-contained and authoritative
operative specification of the Officina supervisor/control-channel architecture
under the signed selection
`I_SELECT_SUPERVISOR_PROCESS_AUTHORITY_P1_FULL_PCS_MEDIATION`.**

It is a **full replacement** for version 1.3. It is not a delta over version
1.3, it does not require version 1.3 to be read or applied, and after
acceptance it is the only operative implementation object. Every implementable
value, sequence, table and rule appears literally in a normative region below.

## BLOCKING NOTICE — two author cells are unresolved and neither is filled here

**This version is not acceptable as an operative object until BOTH author cells
below are signed.** Neither is filled here and neither is predicted.

### Cell 1 — `AUTHOR_CELL_P1_PROCESS_CLAIM_IDENTITY_FIELDS`, carried unchanged from v1.2

**This version is not acceptable as an operative object until the author cell
`AUTHOR_CELL_P1_PROCESS_CLAIM_IDENTITY_FIELDS` is signed.** Literal
reconstruction of the peer interface surfaced a conflict between two accepted,
separately signed contracts, stated in full at §P1-13.2 row 2:

> The signed process-claim record `philosophia.officina.t-process-claim.v1`
> mandates the literal integer keys `controller_pid` and `process_group_id`.
> Under the signed P1 selection the supervisor holds opaque handles only, and
> the signed nine-opcode response set of `t-pcs.v1` returns **no pid and no
> process-group number** — `AWAIT_STOP` returns `pgid_is_leader` as `0` or `1`,
> which is a predicate, not a group id. **The layer that must write those two
> keys therefore cannot obtain their values.**

Two coherent repairs exist. They differ in what they cost, and choosing between
them changes signed meaning. **This document chooses neither and invents no
value.** The cell is stated exactly at §P1-13.2 row 2 and named again in the
companion closure.

### Cell 2 — `AUTHOR_CELL_P1_WATCHDOG_FREEZE_MECHANISM`, new in v1.3

**This version is not acceptable as an operative object until the
watchdog-freeze mechanism cell is signed.** The watchdog freezer/witness role is
reassigned to the supervisor throughout this version — that reassignment is
common to both options and is NOT itself a choice. What remains open is the
mechanism by which a freeze becomes reachable when the peer control endpoint is
lost:

> **`W-A`** — `I_SELECT_P1_WATCHDOG_FREEZE_A_WATCHDOG_REQUESTS_PCS_EXECUTES`.
> The watchdog holds one single-opcode, target-free freeze-request socket at
> slot 6 and may emit exactly one constant `t-wd-freeze.v1` transport frame; the
> PCS opens a bounded service window and runs the freeze classifier only on an
> `ACCEPTED` request.
>
> **`W-B`** — `I_SELECT_P1_WATCHDOG_FREEZE_B_PCS_FREEZES_ON_PEER_ENDPOINT_LOSS`.
> The watchdog holds two sealed pipes and no socket; slot 6 is explicitly
> closed. The PCS runs the freeze classifier record-first on peer-control-endpoint
> loss.

**This document selects neither and predicts neither.** Where the two differ,
the text below carries BOTH variants inside an explicitly delimited block:

```text
    [W-A]   … text operative only if W-A is signed …
    [W-B]   … text operative only if W-B is signed …
```

**A `[W-A]`/`[W-B]` block is not operative text in either direction until the
cell is signed.** At signature exactly one branch of every such block is
retained and the other is deleted, in the single atomic step of the companion
closure's handoff; the resulting file carries no variant block at all. A build
extracted from a file that still contains a variant block is **not conforming**
and the verifier refuses it (`G-10`, §P1-14.3).

Every other part of the interface repair is complete, and the rest of this
composite is a finished replacement for v1.2, so that the signed decisions —
whichever way they go — land in a document that is otherwise ready.

## Authority hierarchy — four levels

1. **Author signatures are the source of accepted choices.** The signed
   selections A3, B1, C1, D1, K1 and P1 are the only source of *what* was
   chosen. This document may not change them.
2. **This composite is the sole operative specification of how those choices
   are implemented.** Where it and any other document differ on an executable
   rule, **this document governs**.
3. **Every earlier supervisor/control-channel document — the two drafts, the
   corrections v2.1 through v2.1.10.7, the v2.1.10.4 P1 binding, and versions 1,
   1.1, 1.2 and 1.3 of this composite, together with version 1 of the watchdog
   freeze-authority amendment — is immutable historical and provenance
   evidence only.** No implementer, verifier or reviewer opens any of them for
   behaviour or for verification. They appear in §P1-18's provenance region by
   path and digest and nowhere else.

   **This rule attaches to DOCUMENTS, not to paragraphs.** There is no
   file-internal split by which some sections of a historical document remain
   operative while others are provenance, and a cross-reference from one
   historical document to another does not reactivate either. In particular, the
   historical §W, §Z, §N, §U and §P1B sections — including historical §W6.5 and
   its ten carrying references — are provenance in whole. Their meaning is
   superseded, without any edit to their bytes, by §A2 of the peer amendment
   named at level 3a and by §P1-10.6, §P1-13.2 row 4 and §P1-13.9 of this
   document. **No historical byte is edited by this version or by its handoff.**

   3a. **One new peer amendment is a live authority surface and is not a
   predecessor:**
   `successor/OFFICINA_GENERIC_HARNESS_WATCHDOG_FREEZE_AUTHORITY_AMENDMENT_V1_1_DRAFT.md`.
   It is an addition to the accepted generic-harness chain, owns peer-layer
   freeze behaviour, and is accepted jointly and indivisibly with this document.
   Neither is operative alone.
4. **Any future change requires a new signed and reviewed version of this
   file.** No prose elsewhere overrides it and no implicit supersession exists.

**Peer contracts** are a different thing from a predecessor: they are
separately accepted or jointly accepted with this version, currently in force or
becoming so, and own functionality outside the P1 boundary. There are three: the
accepted generic-harness chain, the accepted batch-settlement amendment, and the
watchdog freeze-authority amendment of level 3a. §P1-13 states the exact typed
interface to them, including the logical-ownership map that separates which
layer owns a decision from which operating-system process executes it. P1 never
opens a historical P1 predecessor for anything.

Status:
`BLOCKED_ON_AUTHOR_CELLS_P1_PROCESS_CLAIM_IDENTITY_FIELDS_AND_P1_WATCHDOG_FREEZE_MECHANISM_NOT_ACCEPTED`.
`I_ACCEPT_OFFICINA_SUPERVISOR_CONTROL_CHANNEL_AMENDMENT` is **not signable** and
is not made signable here. Neither watchdog-freeze option is selected and no
watchdog-freeze token is signable. This version is furthermore not acceptable
except JOINTLY AND INDIVISIBLY with
`successor/OFFICINA_GENERIC_HARNESS_WATCHDOG_FREEZE_AUTHORITY_AMENDMENT_V1_1_DRAFT.md`
under the single atomic handoff stated IN FULL at §P1-14.8 of this file and
identically at §A9 of that amendment — NEITHER COPY DEFERS TO ANY AUTHOR
CLOSURE; neither document is operative alone. This document creates nothing executable, edits no
file, starts no process, and authorizes no implementation. T is
`NOT_ACTIVATED`; the programme claim is `OPEN`.

**Authorship.** Written by **Claude Code Opus 5 acting only as the
specification author**, which authored the historical chain and therefore
**cannot** be its independent X or Y reviewer. Every author closure, including
this document's companion closure, is an untrusted self-assessment.

---

## Region scheme (read this before extracting anything)

This file contains **three delimited regions**. Two are normative; one is not.

| Region | Authority | Contents |
|---|---|---|
| `BODY` | **normative contract** | every executable rule, every verifier rule definition, the full test matrix, and the negative space |
| `GUARDDATA` | **normative verifier data** | the exact guard-pattern strings the verifier reads. These bytes change verifier pass/fail behaviour and are therefore normative, not an appendix |
| `PROVENANCE` | **non-normative** | historical digests, never read for behaviour or verification |

### Sentinel construction

Sentinel lines are **not written out literally anywhere in a normative region**,
so no example can collide with a real delimiter. The verifier builds each one by
concatenating fixed byte fragments:

```text
FRAG_OPEN   := the four bytes   0x3C 0x21 0x2D 0x2D
FRAG_SP     := the one byte     0x20
FRAG_TAG    := the eleven bytes "OFFICINA" 0x2D "P1"
FRAG_DASH   := the one byte     0x2D
FRAG_CLOSE  := the three bytes  0x2D 0x2D 0x3E

SENTINEL(region, edge) :=
    FRAG_OPEN + FRAG_SP + FRAG_TAG + FRAG_DASH + region + FRAG_DASH + edge
              + FRAG_SP + FRAG_CLOSE

region in { "BODY", "GUARDDATA", "PROVENANCE" }
edge   in { "BEGIN", "END" }
```

Six sentinel lines exist. A line **is** a sentinel only if the whole line,
after stripping a trailing `0x0A` and with no other leading or trailing bytes,
equals a constructed value.

### Extraction algorithm — total and fail-closed

```text
EXTRACT(file_bytes):
  L := the list of lines of file_bytes, split on 0x0A, each retaining its 0x0A
       except possibly the last
  for each of the six SENTINEL values S:
      n[S] := the number of i with line_i (minus a trailing 0x0A) == S
      if n[S] != 1: FAIL "sentinel cardinality"           (0 or >1 both fail)
  let b_R, e_R be the indices of BEGIN and END for region R
  if not ( b_BODY < e_BODY
           and e_BODY < b_GUARDDATA
           and b_GUARDDATA < e_GUARDDATA
           and e_GUARDDATA < b_PROVENANCE
           and b_PROVENANCE < e_PROVENANCE ):
      FAIL "sentinel order"
  REGION(R) := the concatenation of lines with index strictly greater than b_R
               and strictly less than e_R, each including its 0x0A
  return REGION(BODY), REGION(GUARDDATA), REGION(PROVENANCE)

H_BODY       := SHA-256( REGION(BODY) )
H_GUARDDATA  := SHA-256( REGION(GUARDDATA) )
H_NORMATIVE  := SHA-256( REGION(BODY) || REGION(GUARDDATA) )   ordered
                                                                concatenation
H_FILE       := SHA-256( file_bytes )
```

`H_BODY`, `H_GUARDDATA`, `H_NORMATIVE` and `H_FILE` are reported by the author
closure, confirmed by the independent reviews, and then recorded in the
production manifest, which the verifier enforces. **This file contains none of
its own digests**, so the custody chain is acyclic (§P1-14.5).

### The authority of this preamble, stated rather than left implicit

Everything above this paragraph — the authority hierarchy, the region table, the
sentinel construction and the extraction algorithm — is **normative**. It lies
outside all three delimited regions, because a reader must be able to apply it
before any region exists, so it is **not** covered by `H_BODY` or
`H_GUARDDATA`. It is covered by `H_FILE`, which guard `G-7` enforces against the
manifest, so no byte of it can change undetected. The operative form of the
same rules is additionally restated inside the body region at §P1-14.0 and is
therefore also covered by `H_BODY`; where the two statements are compared they
must agree, and guard `G-9` requires the verifier's own compiled fragment
constants to equal the fragments above.

<!-- OFFICINA-P1-BODY-BEGIN -->

---

## §P1-1. Scope, threat model, signed choices

### §P1-1.1 Scope

This contract specifies the construction, authority, communication, failure and
termination of the Officina supervisor control plane: the process-control
server (**PCS**), the middle process, the supervisor, the watchdog, controllers
and workers, and the two channels connecting them. It specifies no scientific
procedure, no resource envelope, and no activation.

### §P1-1.2 Threat model

The contract defends against accidental contamination and ordinary failure of
processes it does not control, and against its own ability to record something
false. It does **not** defend against a hostile actor at the same UID.

| Assumed hostile or contaminated | Assumed sound |
|---|---|
| the caller process in any runtime state: threads, monkeypatched primitives, `.pth` / site customization, audit, import and trace hooks, at-fork callbacks, retained callables, native extensions | the Linux kernel of the platform of §P1-2.1 |
| any ancestor of the caller, including one that has set `PR_SET_CHILD_SUBREAPER` | the documented interfaces of the CPython build of §P1-2.1 |
| the supervisor process from the instant it imports the project package | the bytes of the five production roots, established at deploy time by digest |
| any same-UID process, which may signal, stop, kill, or — if it has adopted them — reap this contract's processes, and may create, replace or remove files this contract reads | the filesystem's atomicity primitives: `rename`, `O_EXCL`, `flock` |

### §P1-1.3 The six signed choices in operative form

**A3 — `I_SELECT_SUPERVISOR_CONFINEMENT_A3_SAME_UID_PROCEDURAL_RESCOPE`.**
Confinement of a same-UID actor is procedural and is not enforced. This
contract asserts no same-UID confinement mechanism and defines none.
`T_RUNTIME.lock` and `SPAWN.lock` serialize contract actors only; neither is a
filesystem or process exclusion mechanism. Every residual in §P1-12.4 that
depends on a same-UID actor's forbearance is permanently non-citable: forbidden
from selection, from Q, from C, from C1 through C6, from any blinding claim,
and from any scientific or resource interpretation.

**B1 — `I_SELECT_SUPERVISOR_IDEMPOTENCY_B1_DURABLE_JOURNAL_ACK_REDELIVERY`.**
Effects are made exactly-once by a durable journal, an acknowledgement, and
retry-stable redelivery of a recorded reply. Two journals exist: the peer
contract's client journal (§P1-13, outside the P1 boundary) and the
process-control journal of §P1-8.6. On the process-control channel the **byte
record** of a reply is redeliverable and a **descriptor capability is never
re-sent** (§P1-8.6). That narrowing of B1 on that channel is accepted and is
stated wherever it applies.

**C1 — `I_SELECT_SUPERVISOR_WATCHDOG_C1_DEDICATED_FREEZER`, AMENDED.** A
dedicated watchdog process witnesses the supervisor control channel and signals
its loss. **The supervisor executes every freeze and writes every freeze
observation; the PCS executes every group stop.** The signed selection is not
revoked, re-run or reopened — it retains a dedicated watchdog PROCESS — and its
freezer and witness content is amended by
`P1_WATCHDOG_FREEZER_ROLE_REASSIGNMENT_V1`.
`[W-A]` The watchdog additionally signals the loss by requesting the freeze the
PCS executes. `[W-B]` The watchdog requests nothing. Its complete set of operative
properties is enumerated in §P1-9.2. Supervisor death is detected by **exactly
one** mechanism, update-pipe EOF; the direct-parent `getppid()` detector is
deliberately absent. That is the author's selected trade and is not a
mechanically identical re-implementation of the pre-P1 watchdog.

**D1 — `I_SELECT_SUPERVISOR_LIFETIME_D1_NO_IDLE_EXIT`.** No supervisor idle
exit exists. D1's ground is that no supervisor ever waits on `SPAWN.lock`, so a
running supervisor's lifetime never depends on any client. Under P1 the
availability model additionally depends on a mandatory resident PCS whose loss
is an unrecoverable whole-generation invalidity with no adoption (§P1-11.4).

**K1 —
`I_SELECT_SUPERVISOR_OUTPUT_CAPACITY_K1_SUPERVISOR_MEDIATED_TRANSPORT_FIXED_CEILING`.**
Worker output crosses the supervisor under the fixed ceiling of §P1-2.3 with
one-write and one-hash accounting and no replenishment. P1 determines which
process creates the pipes; it does not determine who mediates or accounts,
which is the peer boundary of §P1-13.

**P1 — `I_SELECT_SUPERVISOR_PROCESS_AUTHORITY_P1_FULL_PCS_MEDIATION`.** One
clean, constructed PCS holds the numeric identity of every process it creates
and all numeric process authority for the middle process, controllers, workers
and every watchdog. The supervisor receives opaque handles only, cannot express
a PID, and calls `fork`, `Popen`, `waitpid`, `kill` and `killpg` on no path.
Every watchdog is a PCS-created isolated role. PCS loss is unrecoverable
generation invalidity, and no new PCS may adopt a live generation.

---

## §P1-2. Platform and constants

### §P1-2.1 Supported platform, verified at run time

```text
os.uname().sysname       == "Linux"
os.uname().machine       == "x86_64"
sys.implementation.name  == "cpython"
sys.version_info[:3]     == (3, 12, 3)
plus the exact reviewed interpreter build identity recorded in the
implementation review
```

Any mismatch is a fail-closed refusal before any fork, lock acquisition or
record install. No other architecture is supported: MIPS, ARM64, i386, Alpha,
SPARC and every non-Linux system are refused at this check, before any signal
mask is parsed.

Inside this scope `_NSIG` is 64, so `/proc/<pid>/status` renders each signal
mask as exactly 16 hexadecimal digits, and a native `int` is 4 bytes,
little-endian.

### §P1-2.2 Control-plane constants

```text
T_SUPERVISOR_POLL_INTERVAL_NS      =         50_000_000
T_CONTROL_FRAME_MAX_BYTES          =              4_096
T_CONTROL_READ_TIMEOUT_SECONDS     =                 10
T_CLIENT_REPLY_TIMEOUT_SECONDS     =                 30
T_SPAWN_LOCK_ACQUIRE_TIMEOUT_NS    =     30_000_000_000
T_SPAWN_IDENTITY_WAIT_TIMEOUT_NS   =     10_000_000_000
T_SPAWN_SELF_STOP_TIMEOUT_NS       =     10_000_000_000
T_SPAWN_BOOTSTRAP_MAX_AGE_NS       =     60_000_000_000
T_WATCHDOG_ACK_ABSENCE_TIMEOUT_NS  =     60_000_000_000
```

`T_SUPERVISOR_POLL_INTERVAL_NS` is 50_000_000. A value of 100_000_000 appears
in no rule of this contract.

### §P1-2.3 Output-capacity constants

```text
T_OUTPUT_PER_STREAM_MAX_BYTES      =         67_108_864
T_OUTPUT_AGGREGATE_MAX_BYTES       =     34_359_738_368
T_OUTPUT_FS_SAFETY_MARGIN_BYTES    =      8_589_934_592
T_OUTPUT_COPY_CHUNK_BYTES          =          4_194_304
T_OUTPUT_PATH_MAX_BYTES            =              1_024
T_OUTPUT_PATH_COMPONENT_MAX_BYTES  =                255
```

### §P1-2.4 Descriptor indices

```text
PCS process, created by the caller:
  T_PCB_FD_REQUEST_R    = 3      T_PCB_FD_PACKAGE_ROOT = 6
  T_PCB_FD_REPLY_W      = 4      T_PCB_FD_SOURCE       = 7
  T_PCB_FD_RUNTIME_ROOT = 5      T_PCB_FD_INTERPRETER  = 8

Role processes:
  slot 3 and slot 4 are role-class specific (§P1-6.2)
  T_ROLE_FD_ROLESRC = 5     slot 6 is role-class specific
  T_ROLE_FD_SELF    = 7     T_ROLE_FD_SRCDIR  = 8
  T_ROLE_FD_INTERP  = 9     T_ROLE_FD_PKGROOT = 10

Controller and worker control descriptors:
  T_CTRL_FD_LOW  = 3         T_CTRL_FD_HIGH = 4
```

### §P1-2.5 Signal numbers as integer literals

```text
SIGKILL = 9   SIGTERM = 15   SIGCONT = 18   SIGSTOP = 19   SIGNAL_0 = 0
```

`_signal.SIGCHLD` is the only symbolic signal name used anywhere, because
`SIGCHLD`'s number is not uniform across Linux architectures while the five
above are fixed by the platform of §P1-2.1.

### §P1-2.6 The closed failure-token set

Every refusal carries exactly one token from this set. The set is closed and no
token is composed at run time.

```text
Construction and preflight:
  PLATFORM_UNSUPPORTED        INTERPRETER_UNSUPPORTED     ISOLATION_NOT_PINNED
  TOPOLOGY_MULTITASK          INHERITED_CHILD             FD_TOPOLOGY
  SIGNAL_MASK_INHERITED       MASK_MALFORMED              NORMALIZE_INCONCLUSIVE
  PRIMITIVE_NOT_GENUINE       LOCK_FD_NOT_CLOEXEC         SOURCE_FD_UNUSABLE
  SOURCE_NOT_REGULAR          SOURCE_WRITABLE             SOURCE_NOT_READONLY
  ROOT_CANONICAL_UNREADABLE   ROOT_SOURCE_MISMATCH        ROLE_SOURCE_UNREADABLE
  ROLE_PATH_UNREADABLE        CHDIR_FAILED                REQUEST_MALFORMED
  REQUEST_TRUNCATED           GRANDCHILD_FD_HOIST_FAILED
  GRANDCHILD_FD_NOT_INHERITABLE
Caller launcher:
  LAUNCH_FD_HOIST_FAILED      LAUNCH_CONSTANT_MISMATCH    LAUNCH_SPAWN_FAILED
  LAUNCH_STRUCTURAL           LAUNCH_PRIMITIVE_NOT_GENUINE
Transport:
  TRANSPORT_STRUCTURAL        ANCILLARY_VIOLATION         PEER_EOF
  PEER_RESET                  TIMEOUT
Protocol:
  WRONG_GENERATION            UNKNOWN_OPCODE              UNKNOWN_HANDLE
  HANDLE_STATE                OPERATION_INCONCLUSIVE      HANDLES_LIVE
  GENERATION_NOT_ADOPTABLE
Process control:
  STRUCTURAL_VIOLATION        WATCHDOG_UNREAPED           FD_DELIVERY_UNCONFIRMED
Exit status token:
  T_PCS_EXIT_RECV_UNENUMERABLE
```

`REFUSED` and `BLOCKED` are the two outcome words of the caller reply;
`SUPERVISOR_LIVE` is the third. `OK`, `REFUSED`, `INVALID` and `REPLAYED` are
the four protocol statuses. No other outcome word exists.

---

## §P1-3. Roots, imports, primitives

### §P1-3.1 The five production roots

```text
scripts/officina_activate_t.py
scripts/verify_officina_active.py
src/philosophia/officina/generic_harness.py
scripts/officina_process_control_bootstrap.py
scripts/officina_role_bootstrap.py
```

### §P1-3.2 Import allowlists

```text
ALLOWED_ABSOLUTE_IMPORTS, the global default, 19 members:
  __future__ ast dataclasses datetime enum fcntl hashlib hmac json os pathlib
  re subprocess time typing weakref sys _signal _socket

MODULE_SCOPED_ABSOLUTE_IMPORTS. A file with an entry gets EXACTLY that entry
and never the union with the default:
  scripts/officina_process_control_bootstrap.py
      -> { os, sys, _signal, time, fcntl, _socket }                     6
  scripts/officina_role_bootstrap.py
      -> { os, sys, fcntl }                                            3
  src/philosophia/officina/generic_harness.py
      -> { __future__, ast, dataclasses, datetime, enum, fcntl, hashlib,
           hmac, json, os, pathlib, re, subprocess, time, typing, weakref,
           _socket }                                                   17
```

`signal`, the pure-Python wrapper, is permitted in no file: its import closure
pulls `functools` and hence `_thread`. The built-in `_signal` is used instead.
`sys` and `_signal` are permitted only in a file with a scoped entry.
`threading`, `_thread`, `multiprocessing`, `concurrent`, `asyncio`, `ctypes`,
`select`, `selectors`, `socket`, `array`, `struct`, `atexit`, `gc` and any
`prctl` binding are permitted in no file.

### §P1-3.3 The PCS import closure, audited

| Module | Kind | Transitive Python closure at import | Starts a task? | Registers an at-fork callback? | Installs a handler or hook? |
|---|---|---|---|---|---|
| `os` | Python wrapper over built-in `posix` | `sys`, `abc`, `stat`, `_collections_abc`, `posixpath`, `genericpath` | no | it defines `register_at_fork` and never calls it | no |
| `sys` | built-in | none | no | no | no |
| `_signal` | built-in | none | no | no | no |
| `time` | built-in | none | no | no | no |
| `fcntl` | built-in | none | no | no | no |
| `_socket` | built-in | none | no | no | no |

Disclosure: a `_socket.socket` object carries a finalizer that closes its
descriptor. Two rules contain it. Every socket object lives in a module-level
slot for the whole generation. Every received descriptor is handled as a plain
`int`, closed exactly once with the bound close primitive, and never wrapped in
a socket object.

### §P1-3.4 Primitive binding

Immediately after the imports, at module scope, before any other statement:

```text
_BUILTIN = type(len)                    the type anchor; len is never called

from os      : _fork _waitpid _kill _killpg _getpid _getppid _open _read
               _write _close _fstat _stat _listdir _unlink _fsync _rename
               _pipe2 _dup2 _dup _execve _setsid _exit_ _uname _chdir
               _get_inheritable _posix_spawn
from fcntl   : _flock _fcntl
from time    : _clock
from _signal : _sigsignal _getsignal
from _socket : _socketpair _CMSG_SPACE _CMSG_LEN
from the _socket.socket type : _sendmsg _recvmsg

integer constants: _SIGCHLD _SIG_DFL _WNOHANG _O_RDONLY _O_WRONLY _O_RDWR
  _O_CREAT _O_EXCL _O_DIRECTORY _O_NOFOLLOW _O_CLOEXEC _O_NONBLOCK _LOCK_EX
  _LOCK_NB _F_GETFL _F_GETFD _O_ACCMODE _FD_CLOEXEC _AF_UNIX _SOCK_SEQPACKET
  _SOL_SOCKET _SCM_RIGHTS _MSG_CMSG_CLOEXEC _MSG_CTRUNC _MSG_TRUNC
  _POSIX_SPAWN_OPEN _POSIX_SPAWN_CLOSE _POSIX_SPAWN_DUP2
string constant : _devnull
value objects   : _flags _version_info _implementation   from sys
```

### §P1-3.5 Primitive identity validation, four kinds

There is no single universal predicate: a uniform
`builtin_function_or_method` test would reject a genuine pure-Python wrapper,
so each kind carries its own rule.

| Kind | Members | Requirements |
|---|---|---|
| module built-in callable | every `os`, `fcntl`, `time`, `_signal`, `_socket` function of §P1-3.4 | `type(f) is _BUILTIN`; `getattr(f, "__self__", None)` is not `None`; `f.__self__.__name__` equals the expected module name, one of `"posix"`, `"fcntl"`, `"time"`, `"_signal"`, `"_socket"`; `f.__qualname__` equals the exact bare name, and `_exit_` expects `"_exit"` |
| method descriptor | `_sendmsg`, `_recvmsg` | a method descriptor whose `__objclass__` is `_socket.socket` and whose `__qualname__` is `"socket.sendmsg"` or `"socket.recvmsg"` |
| integer constant | every constant of §P1-3.4 | `type(x) is int`; `_SIGCHLD == 17`; `_SIG_DFL == 0`; `_F_GETFL == 3`; `_O_ACCMODE == 3`; `_O_RDONLY == 0`; `{_POSIX_SPAWN_OPEN, _POSIX_SPAWN_CLOSE, _POSIX_SPAWN_DUP2} == {0, 1, 2}` and pairwise distinct; every other constant equals the value recorded in the implementation review |
| string constant | `_devnull` | `type(x) is str` and the value `"/dev/null"` |

`_flags`, `_version_info` and `_implementation` are consumed only by §P1-7.2's
field comparisons; this contract makes no identity claim about those container
objects.

Any failure is `PRIMITIVE_NOT_GENUINE`: fail-closed refusal, no fork, no lock
acquisition, no record installed.

### §P1-3.6 No rebinding and no indirection

Every later use goes through the local name. The module names `os`, `sys`,
`_signal`, `time`, `fcntl` and `_socket` appear as an attribute value only
inside the §P1-3.4 binding block. Each bound name is assigned exactly once at
module scope and never appears as an augmented-assignment target, a `del`
target, a function parameter, a comprehension target, an `as` target, or a
`setattr` argument. `getattr`, `setattr`, `delattr`, `vars`, `globals`,
`locals`, `eval`, `exec`, `compile`, `__import__`, `importlib`, subscripted
call targets, and calls to expressions that are not a plain name are forbidden.

---

## §P1-4. Process topology and authority

### §P1-4.1 The process tree

```text
[0] caller — generic_harness.py __main__, any runtime state, assumed
     │        contaminated
     │ os.posix_spawn, §P1-7.1
     ▼
[1] PCS — scripts/officina_process_control_bootstrap.py, flags -I -S -E -P,
     │     empty environment. Owns SPAWN.lock, the four singleton records, the
     │     four bootstrap channels, the supervisor socket, the handle table,
     │     the process-control journal, and the numeric identity of every
     │     process it creates.
     ├─ fork at c4 ─▶ [2] middle, pid_mid
     │                   └─ fork at m7 ─▶ [3] grandchild ─ execve ─▶
     │                                       [3'] role bootstrap: SUPERVISOR
     │                   └─ _exit(0) at m9 ; [3'] becomes an orphan
     ├─ posix_spawn ─▶ [4] role bootstrap: WATCHDOG          setsid = False
     ├─ posix_spawn ─▶ [5] role bootstrap: CONTROLLER × n    setsid = True
     └─ posix_spawn ─▶ [6] role bootstrap: WORKER × n        setsid = True
```

### §P1-4.2 Orphan adoption

When a process is orphaned it is re-parented to the **nearest still-living
ancestor subreaper** — a process that has set `PR_SET_CHILD_SUBREAPER` — and to
the PID namespace's init process only if no such ancestor exists. That adopting
process is the one that may reap it, `getppid()` in the orphan returns the
adopter, and the adopter receives `SIGCHLD`.

This contract sets `PR_SET_CHILD_SUBREAPER` nowhere and observes no adopter.
Its own abstention proves nothing about its ancestors: the caller, or any
process above it, may already be a subreaper. **No rule in this document
depends on which process adopts an orphan.**

### §P1-4.3 Dynamic parent, adopter, wait and authority table

`A*` denotes an arbitrary higher ancestor of the caller. A process appears in
the adopted column only while it is the nearest living ancestor subreaper.

| Process | Initial direct children | Initial wait-set | Set of processes it may dynamically adopt | Wait-set after adoption | Officina authority |
|---|---|---|---|---|---|
| `A*` | whatever the host gave it | its own initial direct children | the supervisor after `m9`; and after PCS death `pid_mid`, every controller, every worker and every watchdog | the union of its initial direct children and its adopted set; a wildcard wait ranges over that union | none |
| caller | the PCS | the PCS | the same set as `A*`, when the caller is the nearer living subreaper | the union of `{the PCS}` and its adopted set; a wildcard wait ranges over that union | none beyond §P1-7.1's launch and the four-step pipe exchange |
| PCS | `pid_mid`, controllers, workers, watchdogs | exactly those | the empty set — it sets no subreaper attribute, and its own descendants are orphaned only once it is already dead | exactly its initial direct children | full: the only holder of numeric process authority |
| middle, `pid_mid` | the grandchild until `m9` | the empty set — it executes no wait-family call | the empty set | the empty set | none |
| supervisor | the empty set | the empty set — a wildcard wait returns `ECHILD` | the empty set | the empty set | opaque handles only, never a PID |
| watchdog | the empty set | the empty set | the empty set | the empty set | none |
| controller or worker | the target processes it creates, if its target program creates any | the target processes it creates, if any | the empty set | the target processes it creates, if any | none |

**State retention rule, stated locally so no cell is a placeholder.** For any
process whose adopted set is the empty set, its wait-set after adoption is
exactly its initial wait-set, and its Officina authority is exactly the value in
its authority cell. No cell in this table inherits a value from any other
document.

**Wildcard waits of an adopter range over its adopted direct children.** This is
stated affirmatively; nothing in this contract prevents it.

### §P1-4.4 What adoption adds

A same-UID actor may already signal, stop or kill any process of this contract
without adopting anything, per §P1-1.2 and A3. Adoption adds exactly two
powers:

1. **reaper status** — the adopter may reap the adopted process, including by a
   wildcard wait, thereby observing its wait status and controlling when the
   zombie clears;
2. **`getppid()` visibility** — `getppid()` in the adopted process returns the
   adopter. **No rule in this contract reads `getppid()` in any process**, so
   this confers nothing.

Adoption adds no signalling power, no descriptor or capability, since reaping
conveys none, and no Officina handle, opcode, journal entry or control-plane
participation.

### §P1-4.5 Death proofs by target

| Target | The only accepted proof |
|---|---|
| `pid_mid`, any controller, any worker, any watchdog | the PCS's own targeted `os.waitpid(pid, WNOHANG)` returning that pid, per §P1-10.2. Only a returned pid proves death |
| the supervisor | never by a wait. Loss is observed by channel EOF on the protocol socket. Where a route requires a death proof for the supervisor's process group, the accepted proofs are `/proc` absence, or state `Z` with a matching start identity, or live with a different start identity, which means not live and never kill |
| any recorded process at a later attempt's preflight | the same three `/proc` predicates |

**No proof anywhere consumes an orphan's reaped status or exit code.**

### §P1-4.6 The group anchor

The process-group id used by the post-`c11` `killpg` route is `pid_mid`'s pid.
`pid_mid` is a direct child of the PCS and is therefore never orphaned while the
PCS lives, so adoption semantics cannot touch the anchor. If the PCS dies,
`pid_mid` is orphaned, but the generation is by then unrecoverable invalidity
per §P1-11.4 and no `killpg` decision is taken.

---

## §P1-5. Durable records

### §P1-5.1 The four singleton attempt records

All four live in the runtime root's `T_SUPERVISOR/` directory, are installed
atomically with no replacement, and are durable by write, `fsync` of the file,
`rename`, then `fsync` of the parent directory.

```text
SPAWNING.json
  schema value : philosophia.officina.t-supervisor-spawning.v1
  keys exactly : schema, scientific_outcome, spawning_id, cli_pid,
                 cli_start_identity, boot_identity, created_utc

SPAWNING_MIDDLE.json
  schema value : philosophia.officina.t-supervisor-spawning-middle.v1
  keys exactly : schema, scientific_outcome, spawning_id, cli_pid,
                 cli_start_identity, middle_child_pid,
                 middle_child_start_identity, boot_identity, created_utc

SPAWNING_GROUP.json
  schema value : philosophia.officina.t-supervisor-spawning-group.v1
  keys exactly : schema, scientific_outcome, spawning_id, cli_pid,
                 cli_start_identity, middle_child_pid,
                 middle_child_start_identity, session_id, process_group_id,
                 group_verified, boot_identity, created_utc

SPAWNING_CHILD.json
  schema value : philosophia.officina.t-supervisor-spawning-child.v1
  keys exactly : schema, scientific_outcome, spawning_id, supervisor_pid,
                 supervisor_start_identity, supervisor_pgid, boot_identity,
                 created_utc
```

### §P1-5.2 Field meanings, stated once and literally

| Key | Meaning |
|---|---|
| `schema` | the exact schema value of §P1-5.1 for that record |
| `scientific_outcome` | the JSON literal `false` in all four records. These are control-plane records and are never a scientific outcome |
| `spawning_id` | the 64-lowercase-hex attempt identifier: SHA-256 of the canonical record without this field |
| `cli_pid` | the process id of the **PCS**, which is the process that holds `SPAWN.lock` and performs the first fork |
| `cli_start_identity` | the kernel start-time identity of that same PCS process, read from `/proc/<pid>/stat` per §P1-10.3 |
| `middle_child_pid` | the pid the PCS's `c4` fork returned |
| `middle_child_start_identity` | that process's kernel start-time identity |
| `session_id` | the middle's session id after its `setsid`, equal to `middle_child_pid` |
| `process_group_id` | the middle's process-group id after its `setsid`, equal to `middle_child_pid` |
| `group_verified` | the JSON literal `true`. This key is installable only after `c10`'s kernel proof succeeds |
| `supervisor_pid` | the pid the middle's `m7` fork returned |
| `supervisor_start_identity` | that process's kernel start-time identity |
| `supervisor_pgid` | that process's process-group id, equal to `process_group_id` |
| `boot_identity` | the contents of `/proc/sys/kernel/random/boot_id` |
| `created_utc` | the record's creation instant, in the canonical timestamp grammar the peer contract of §P1-13 defines for durable records |

The field names `cli_pid` and `cli_start_identity` denote the PCS. The names
and the schema values are exactly as written above; §P1-5.2 is the sole
definition of their meaning under this contract.

### §P1-5.3 The two in-flight bootstrap records

Neither is persisted, archived, hashed into a signed set, or given a durable
path. Each is one canonical ASCII JSON line of at most
`T_CONTROL_FRAME_MAX_BYTES`.

```text
group report, written by the middle at m4 on the boot pipe
  schema value : philosophia.officina.t-supervisor-group-report.v1
  keys exactly : schema, scientific_outcome, spawning_id, middle_child_pid,
                 middle_child_start_identity, session_id, process_group_id,
                 boot_identity, reported_monotonic_ns

bootstrap report, written by the middle at m8 on the boot pipe
  schema value : philosophia.officina.t-supervisor-bootstrap.v1
  keys exactly : schema, scientific_outcome, spawning_id, supervisor_pid,
                 supervisor_start_identity, supervisor_pgid, boot_identity,
                 reported_monotonic_ns
```

`reported_monotonic_ns` is the writer's `time.clock_gettime_ns` sample on the
monotonic clock at the instant of writing.

---

## §P1-6. Descriptors

### §P1-6.1 PCS-side descriptors

| Name | Number | Contents | `FD_CLOEXEC` | Closed when |
|---|---|---|---|---|
| `T_PCB_FD_REQUEST_R` | 3 | caller request pipe, read end | clear | after the caller reply is written |
| `T_PCB_FD_REPLY_W` | 4 | caller reply pipe, write end | clear | after the caller reply is written |
| `T_PCB_FD_RUNTIME_ROOT` | 5 | runtime root directory | clear | PCS exit |
| `T_PCB_FD_PACKAGE_ROOT` | 6 | package root directory | clear | PCS exit |
| `T_PCB_FD_SOURCE` | 7 | the PCS's own source object | clear | PCS exit |
| `T_PCB_FD_INTERPRETER` | 8 | the interpreter object | clear | PCS exit |
| `lock_fd` | kernel-chosen | `SPAWN.lock` held under `flock(LOCK_EX)` | **set** | at `c18` or PCS exit |
| `sv_sock` | kernel-chosen | protocol socket, PCS end | set | at shutdown or PCS exit |
| `journal_fd` | kernel-chosen | the process-control journal | set | PCS exit |
| per handle | kernel-chosen | the role-side ends the PCS retains | set | when that handle reaches state `REAPED` |
| opened under fd 6 | kernel-chosen | role-bootstrap source, harness source, `src` directory | set | PCS exit |

Descriptors 3 through 8 have `FD_CLOEXEC` clear because `POSIX_SPAWN_DUP2`
cleared it on each destination. Every other PCS descriptor has `FD_CLOEXEC` set
by construction: `_open` with `_O_CLOEXEC`, `_pipe2` with `_O_CLOEXEC`,
`_socketpair`, whose descriptors CPython creates non-inheritable, and `_dup`,
which returns a non-inheritable descriptor.

### §P1-6.2 Role-side descriptor maps, literal for every class

| Slot | `SUPERVISOR` | `WATCHDOG` | `CONTROLLER` and `WORKER` |
|---|---|---|---|
| 3 | `SPAWN.lock`, retained until the supervisor's identity record is live-verified | watchdog update pipe, **read** end | control request pipe, **read** end, the value of `T_CTRL_FD_LOW`, which is 3 |
| 4 | boot pipe, **write** end | watchdog ack pipe, **write** end | control reply pipe, **write** end, the value of `T_CTRL_FD_HIGH`, which is 4 |
| 5 | the harness source object | the harness source object | the harness source object |
| 6 | the protocol socket peer | **not used; explicitly closed by a file action** | status pipe, **write** end |
| 7 | the role-bootstrap source object | the role-bootstrap source object | the role-bootstrap source object |
| 8 | the object-bound `src` directory | the object-bound `src` directory | the object-bound `src` directory |
| 9 | the interpreter object | the interpreter object | the interpreter object |
| 10 | the package-root directory | the package-root directory | the package-root directory |

After its `execve` a role's `/proc/self/fd` is exactly `{0, 1, 2}` together
with its slot set: `{3,4,5,6,7,8,9,10}` for `SUPERVISOR` and for
`CONTROLLER`/`WORKER`, and `{3,4,5,7,8,9,10}` for `WATCHDOG`.

**Descriptors the supervisor receives over the protocol socket are not in any
fixed numeric set.** They arrive at kernel-chosen numbers with `FD_CLOEXEC`
already set, and the supervisor records them in its handle-to-descriptor table.
The supervisor's legitimate descriptor set therefore grows with every live
handle, which is why no rule in this contract ever sweeps it (§P1-6.5).

### §P1-6.3 The hoist, for any target set

```text
HOIST(logical_fds, target_set):
  let T := max(target_set)
  for each logical descriptor L, in a fixed order:
      while h[L] <= T:  n := _dup(h[L]); retain the old value; h[L] := n
  close every retained intermediate and every original whose number is <= T
  POSTCONDITION: every h[L] > T, and the values are pairwise distinct
    violated ⇒ LAUNCH_FD_HOIST_FAILED in the caller, or
               GRANDCHILD_FD_HOIST_FAILED in the grandchild; no spawn, no exec
```

### §P1-6.4 File actions for a spawned role, and the leak proof

```text
FILE_ACTIONS := [ (DUP2, h[slot], slot)  for slot in ascending slot order ]
              + [ (CLOSE, h[slot])       for slot in the same order ]
              + [ (CLOSE, d)             for every number d in 3..10 that the
                                          role's slot set does not contain ]
For WATCHDOG the last group is exactly {6}. For CONTROLLER and WORKER it is
empty. No file action ever names lock_fd.
```

**Leak proof.** After a spawned role's `execve` its descriptor set is exactly
`{0,1,2}` together with its slot set, because: every PCS descriptor other than
3 through 8 has `FD_CLOEXEC` set and is closed by the `execve`, and that
includes `lock_fd`, `sv_sock`, `journal_fd`, every per-handle end and every
object opened under fd 6; descriptors 3 through 8 have `FD_CLOEXEC` clear but
all lie in the range 3 to 10, so each is either overwritten by a `DUP2` or named
by an explicit `CLOSE`; and hoisted duplicates come from `_dup`, are
non-inheritable, and are additionally closed by explicit actions. **No role
other than the supervisor ever holds a `SPAWN.lock` reference.** The role's own
`/proc/self/fd` check at step `A-5` verifies this property; it is not the
mechanism that establishes it, and no production path may depend on a
post-`exec` refusal.

### §P1-6.5 `/proc/self/fd` phases and permissions

| Root | Phase | Enumerate | May close | Rule |
|---|---|---|---|---|
| PCS | `P-f`, pre-fork preflight | yes | **no, read-only** | require exactly `{0,1,2,3,4,5,6,7,8}` plus the transient listing descriptor; any deviation is `FD_TOPOLOGY` and no fork occurs |
| role bootstrap | `A-5`, before any project import | yes | **no, read-only** | require exactly `{0,1,2}` together with the role's slot set; any deviation is `os._exit(3)` with nothing written |
| grandchild | `G-5`, after `G-4` and before `G-6`'s `execve` | yes | **yes, bounded** | close every inherited descriptor not in `{0,1,2}` together with slots 3 through 10; ascending, once each, tolerating `EBADF` |
| supervisor | the protocol receive path and its error path | no | no | cleanup is exactly §P1-8.7's parser-local rule |
| supervisor | any runtime remediation, handle release, or shutdown step | no | no | forbidden |
| any root | any phase in which unrelated live role handles coexist | no | no | forbidden |
| PCS | any phase after the first role handle exists | no | no | forbidden; `P-f` is pre-fork and is the PCS's only enumeration |

**`G-5` cannot touch a live supervisor handle.** It executes in the grandchild
before `G-6`'s `execve`, therefore before the project import at `A-10` and
before the role entry at `A-13`. At that instant the process is not the
supervisor, no descriptor received over the protocol socket can exist in it, and
it acts only on its own inherited descriptor table. `P-f` likewise runs before
the PCS's first fork, therefore before any role or handle exists. The two
enumerate-and-close phases and the set of live role handles are temporally and
structurally disjoint.

---

## §P1-7. Construction sequences

### §P1-7.1 The caller launch

The caller is assumed contaminated. Its entire permitted interaction is:

```text
L-0. bind and identity-check every launcher primitive by §P1-3.5's rules
       failure ⇒ LAUNCH_PRIMITIVE_NOT_GENUINE, no spawn
     validate {_POSIX_SPAWN_OPEN, _POSIX_SPAWN_CLOSE, _POSIX_SPAWN_DUP2}
       == {0,1,2} and pairwise distinct
       failure ⇒ LAUNCH_CONSTANT_MISMATCH, no spawn
L-1. create two anonymous pipes with _pipe2(_O_CLOEXEC): request and reply.
     open the runtime root and the package root with
       _O_RDONLY | _O_DIRECTORY | _O_CLOEXEC
     open the bootstrap source with _O_RDONLY | _O_NOFOLLOW | _O_CLOEXEC
     open the interpreter with _O_RDONLY | _O_CLOEXEC
     No pathname of any of these is used again, and none is ever readlink'ed.
L-2. HOIST the six descriptors to the target set {3,4,5,6,7,8}, then

     _posix_spawn(
        b"/proc/self/fd/8",
        [ b"/proc/self/fd/8", b"-I", b"-S", b"-E", b"-P",
          b"/proc/self/fd/7" ],
        {},
        file_actions = the twelve entries of §P1-6.4 for that target set,
        setsigmask   = () )

     setpgroup, resetids, setsid, scheduler and setsigdef are not passed.
     a return that is not an int, or is <= 0  ⇒ LAUNCH_STRUCTURAL
     OSError                                  ⇒ LAUNCH_SPAWN_FAILED
     any other BaseException                  ⇒ LAUNCH_STRUCTURAL
     then close every hoisted duplicate and every original the caller still
     holds for the six roles.
L-3. write exactly one canonical request line on the request pipe; close the
     request write end.
L-4. read the reply pipe to EOF; parse exactly one canonical reply line; close
     the reply read end.

Forbidden to the caller, normatively:
  sending any signal to the PCS, ever, for any reason;
  relying on the PCS's exit status for any decision;
  performing any wait whose result changes a decision;
  using subprocess, Popen, os.fork, os.system, preexec_fn, a shell, or any
  mutable high-level wrapper on the launch path.
```

`/proc/self/fd/<N>` names the object the descriptor refers to; the kernel does
not re-walk the original path, so the interpreter and the source cannot be
replaced between the caller's open and the exec. `readlink` is used nowhere and
`sys.executable` is used for nothing.

> **The launcher property.** For any caller, in any runtime state: either it
> constructs exactly the process of `L-2`, or no authorized PCS comes into
> existence. The launcher's own identity checks are diagnostic, not the safety
> mechanism — a fully hostile caller can defeat them, which is why the property
> is a disjunction. All load-bearing safety is the PCS's own preflight, executed
> where the caller cannot reach. A caller that launches a different program
> creates no authority: that program is not this contract's PCS and can do only
> what the caller could already do.

Why each isolation flag: `-S` prevents the `site` module, so no `.pth`
executable line, no `sitecustomize` and no `usercustomize` runs; `-I` removes
user site-packages and the script directory from `sys.path` and implies `-E` and
`-s`; `-E` makes every `PYTHON*` variable ignored; `-P` prevents prepending a
path to `sys.path`.

### §P1-7.2 The PCS preflight

Executed after the six imports, the binding block and §P1-3.5's identity check,
and before any name is opened.

```text
P-cwd. _chdir("/")                                OSError ⇒ CHDIR_FAILED
       Every later filesystem operation is dir_fd-relative to fd 5 or fd 6, or
       acts on an already-open descriptor, or is an absolute /proc name, so the
       inherited working directory affects nothing; this step is defence in
       depth and additionally releases a possibly-unlinked inherited directory.
P-a.   u := _uname(); require u.sysname == "Linux" and u.machine == "x86_64"
                                                  else PLATFORM_UNSUPPORTED
P-b.   require _implementation.name == "cpython"
       require _version_info[:3] == (3, 12, 3)    else INTERPRETER_UNSUPPORTED
       require _flags.isolated, _flags.no_site, _flags.ignore_environment,
               _flags.safe_path and _flags.no_user_site all truthy
                                                  else ISOLATION_NOT_PINNED
       This is a readback of effect from the interpreter, never of argv. argv is
       read nowhere in the PCS and is evidence of nothing.
P-c.   _listdir("/proc/self/task") equals exactly [str(_getpid())]
                                                  else TOPOLOGY_MULTITASK
P-d.   /proc/self/status field "Threads:" equals "1"
                                                  else TOPOLOGY_MULTITASK
P-e.   the one permitted wildcard wait in this contract, at exactly this place,
       before any fork:  _waitpid(-1, _WNOHANG)
         raises OSError with errno ECHILD ⇒ correct: no children exist
         returns any value                ⇒ INHERITED_CHILD. That call has
                                            reaped an inherited child; the
                                            route refuses precisely because it
                                            must not proceed in a process it
                                            does not understand.
         any other error                  ⇒ INHERITED_CHILD
P-f.   _fstat descriptors 3 through 8: 3 and 4 are S_ISFIFO; 5 and 6 are
       S_ISDIR; 7 and 8 are S_ISREG, neither group- nor other-writable, and
       _fcntl(fd, _F_GETFL) & _O_ACCMODE == _O_RDONLY for each;
       _get_inheritable is true for exactly 3 through 8; and /proc/self/fd
       contains exactly {0,1,2,3,4,5,6,7,8} plus the transient listing
       descriptor
         else FD_TOPOLOGY, SOURCE_NOT_REGULAR, SOURCE_WRITABLE or
              SOURCE_NOT_READONLY
       record SOURCE_IDENTITY      := (st_dev, st_ino) of descriptor 7
       record INTERPRETER_IDENTITY := (st_dev, st_ino) of descriptor 8
P-g.   signal state:
       g-1. read /proc/self/status in full; parse SigIgn, SigCgt, SigBlk and
            Threads under §P1-7.3's grammar. Name the parsed values
            SIGIGN_BEFORE, SIGCGT_BEFORE, SIGBLK_BEFORE.
       g-2. require SIGBLK_BEFORE == 0            else SIGNAL_MASK_INHERITED
       g-3. reset pass: for each bit index i set in SIGCGT_BEFORE, ascending,
            let n := i + 1 and call _sigsignal(n, _SIG_DFL)
              ValueError, RuntimeError, OSError, or any other exception
                                                 ⇒ NORMALIZE_INCONCLUSIVE
            The signal numbers come from the kernel's own mask, so no
            additional _signal member is used. SIGKILL and SIGSTOP can never
            carry a SigCgt bit; if one appears, _sigsignal raises and the route
            refuses.
       g-4. call _sigsignal(_SIGCHLD, _SIG_DFL) unconditionally. This one call
            is a full sigaction replacement: sa_handler is SIG_DFL, the mask is
            empty, and sa_flags contains neither SA_NOCLDWAIT nor SA_NOCLDSTOP.
            It therefore clears both an inherited SIG_IGN and an inherited
            SA_NOCLDWAIT, whatever their provenance: execve preserves SIG_IGN
            while clearing sa_flags, and a fork without exec inherits both.
       g-5. re-read /proc/self/status and parse the same four fields. Name them
            SIGIGN_AFTER, SIGCGT_AFTER, SIGBLK_AFTER, THREADS_AFTER. Require,
            as exact relations over 64-bit unsigned integers:
              SIGCGT_AFTER == 0
              SIGIGN_AFTER == SIGIGN_BEFORE & ~(1 << (int(_SIGCHLD) - 1))
              SIGBLK_AFTER == 0
              THREADS_AFTER == 1
            The second relation says exactly this: every bit of SigIgn keeps
            the value it had before the reset pass, except the SIGCHLD bit,
            which is 0 afterwards whatever value it held previously. Any other
            difference in any bit is a failure.
       g-6. re-list /proc/self/task and require exactly one entry equal to
            str(_getpid())
       g-7. require type(_getsignal(_SIGCHLD)) is int and
            _getsignal(_SIGCHLD) == _SIG_DFL. This is corroboration from
            CPython's own table and is never load-bearing.
       Two consequences follow from the g-5 relation and are stated here as
       operative facts. First, if the SIGPIPE bit was set in SIGIGN_BEFORE it is
       still set in SIGIGN_AFTER, so CPython's ignored SIGPIPE disposition
       survives, and a broken-pipe write raises rather than terminating the
       process. Second, if the SIGINT bit was set in SIGCGT_BEFORE it is 0 in
       SIGCGT_AFTER, so no SIGINT handler remains and a delivered SIGINT
       terminates the PCS by default action; for a lock-holding process this is
       the safer behaviour, and the reset is never undone.
P-h.   read descriptor 3 to EOF; validate the request against §P1-8.2's grammar
                                    else REQUEST_MALFORMED or REQUEST_TRUNCATED
P-p.   package-root binding:
       p-1. self_fd := _open("scripts/officina_process_control_bootstrap.py",
                             _O_RDONLY | _O_NOFOLLOW | _O_CLOEXEC, dir_fd = 6)
                                    any OSError ⇒ ROOT_CANONICAL_UNREADABLE
       p-2. require (st_dev, st_ino) of self_fd == SOURCE_IDENTITY
                                    mismatch    ⇒ ROOT_SOURCE_MISMATCH
       p-3. close self_fd
       p-4. role_fd := _open("src/philosophia/officina/generic_harness.py",
                             _O_RDONLY | _O_NOFOLLOW | _O_CLOEXEC, dir_fd = 6)
                                    any OSError ⇒ ROLE_SOURCE_UNREADABLE
       p-5. require S_ISREG and neither group- nor other-writable; record
            ROLE_IDENTITY := (st_dev, st_ino)
       p-6. rb_fd := _open("scripts/officina_role_bootstrap.py",
                           _O_RDONLY | _O_NOFOLLOW | _O_CLOEXEC, dir_fd = 6)
       p-7. src_dir_fd := _open("src", _O_RDONLY | _O_DIRECTORY | _O_CLOEXEC,
                                dir_fd = 6)
                                    any OSError ⇒ ROLE_PATH_UNREADABLE

Only after every step above may c1 acquire SPAWN.lock.
```

Every result of `P-cwd` through `P-p` other than success takes the same body:
execute no fork; close the bootstrap ends; remove no record, since no record of
this attempt exists yet; write the reply of §P1-8.2 with the corresponding
failure token if descriptor 4 is usable; and exit.

### §P1-7.3 The signal-mask grammar

Applied to `SigIgn`, `SigCgt` and `SigBlk` before any integer conversion.

```text
M-1. split /proc/self/status on 0x0A
M-2. select every line beginning exactly with the field name followed by ":"
       zero such lines, or two or more                ⇒ MASK_MALFORMED
M-3. after the colon: one or more space or tab bytes, then a maximal run of
     hexadecimal digits, then end of line
       an empty run; a byte outside [0-9a-fA-F] in the run; a "0x" or "0X"
       prefix; a sign; internal whitespace; any trailing byte before the newline
                                                      ⇒ MASK_MALFORMED
M-4. let d be the number of hexadecimal digits. Require both:
       4 * d >= int(_SIGCHLD)      the architecture-independent minimum
       d == 16                     the exact width of the platform of §P1-2.1
       either failing                                 ⇒ MASK_MALFORMED
M-5. value := int(digit_run, 16)                      only now is conversion
                                                      permitted
```

Worked cases: an empty value fails; `0` fails; `0000` fails; a 13-digit value
fails; a 20-digit value fails as a rendering this contract has not reviewed; a
16-digit value with leading zeros is the expected form and passes.
`signal.NSIG` is used nowhere and no architecture is silently added.

### §P1-7.4 The role bootstrap

`scripts/officina_role_bootstrap.py` is the executable root of all four roles.
It imports exactly `os`, `sys` and `fcntl` — three modules — because step `A-6`
performs the `F_GETFL` access-mode test.

Its argv is fixed by index. Indices 0 through 11 are common to all four roles;
indices 12 and above exist only for `CONTROLLER` and `WORKER`.

```text
 0  "/proc/self/fd/9"                    the object-bound interpreter
 1  "-I"
 2  "-S"
 3  "-E"
 4  "-P"
 5  "/proc/self/fd/7"                    the object-bound role-bootstrap source
 6  "--officina-role"
 7  "SUPERVISOR" | "WATCHDOG" | "CONTROLLER" | "WORKER"
 8  "--officina-generation"
 9  <64 lowercase hexadecimal characters>
10  "--officina-fdmap"
11  a comma-separated ascending decimal list of the role's slot numbers:
      SUPERVISOR                 "3,4,5,6,7,8,9,10"
      WATCHDOG                   "3,4,5,7,8,9,10"
      CONTROLLER and WORKER      "3,4,5,6,7,8,9,10"
CONTROLLER and WORKER only:
12  "--officina-spawn-intent"
13  <64 lowercase hexadecimal characters>
14  "--officina-ctrl-fds"
15  "3,4"                                the values of T_CTRL_FD_LOW and
                                          T_CTRL_FD_HIGH, in that order
16  "--officina-target-argc"
17  <decimal N, N >= 1>
18  "--"
19 .. 18+N                                the target argv, exactly N elements

environment = {} exactly. No PYTHONPATH is set by any process of this contract,
and the name appears in no launch path.
```

Refusal order, executed exactly in this sequence. Any failure is
`os._exit(3)` with nothing written, nothing unlinked, and no descriptor closed
except its own.

```text
A-1  bind and identity-check every primitive by §P1-3.5's rules
A-2  read back sys.flags: isolated, no_site, ignore_environment, safe_path and
     no_user_site all true
A-3  os.environ must be empty
A-4  argv must match the fixed shape above exactly, and argv[7] must be one of
     the four literals
A-5  _fstat every descriptor named in argv[11]; each has the type its slot
     requires per §P1-6.2; /proc/self/fd contains exactly {0,1,2} together with
     the slot set. Read-only: no close derived from this listing.
A-6  _fstat T_ROLE_FD_SELF: a regular file, neither group- nor other-writable,
     and _fcntl(fd, _F_GETFL) & _O_ACCMODE == _O_RDONLY
A-7  open "scripts/officina_role_bootstrap.py" under T_ROLE_FD_PKGROOT with
     _O_RDONLY | _O_NOFOLLOW | _O_CLOEXEC and require its (st_dev, st_ino) to
     equal T_ROLE_FD_SELF's
A-8  _fstat T_ROLE_FD_SRCDIR and require a directory
A-9  sys.path[:] = ["/proc/self/fd/8"]
     The entire path list is replaced by exactly one object-bound entry naming
     T_ROLE_FD_SRCDIR: no append, no insert into an existing list, and no
     environment involvement.
A-10 import philosophia.officina.generic_harness            the only import
A-11 _fstat the imported module's __file__ and require its (st_dev, st_ino) to
     equal T_ROLE_FD_ROLESRC's
A-12 for CONTROLLER and WORKER only: verify that argv[12], argv[14], argv[16]
     and argv[18] equal their literals above; that argv[13] is 64 lowercase
     hexadecimal characters; that argv[15] equals "3,4"; that argv[17] is a
     decimal N >= 1 and that exactly N elements follow argv[18]; that
     descriptors 3, 4 and 6 have the types §P1-6.2 requires; then self-stop by
     os.kill(os.getpid(), 19) before any target behaviour
A-13 call exactly one pinned entry function, selected by argv[7] from a closed
     four-entry mapping, with the validated descriptors
```

**Role isolation by class.** `SUPERVISOR` and `WATCHDOG` are fully isolated:
after `A-9` their `sys.path` is exactly the object-bound `src` directory and
they import only the project package. `CONTROLLER` and `WORKER` are not fully
isolated, by design, because their target program is client-supplied. That is
safe, and the proof is:

| Vector | Why a contaminated controller or worker cannot affect it |
|---|---|
| process | it holds no PID authority: the PCS created it, is its parent, and is its only reaper; it can name no PID of any other process and can signal, wait for or reap nothing of this contract |
| lock | it never receives the `SPAWN.lock` descriptor, per §P1-6.2 and §P1-6.4 |
| capacity | the ceiling of §P1-2.3 is installed before it runs and is enforced on the supervisor-mediated output path with one-write and one-hash accounting, per the peer boundary of §P1-13 |
| custody | the custody proof and the object-bound observation with both revalidation barriers are performed by the supervisor under `T_RUNTIME.lock`, over objects the worker cannot make the supervisor mis-observe, per §P1-13 |
| scientific validity | a result reaches science only through a durable settlement bound by hash to a result manifest; a malformed or absent object is malformed-dominant or absent, never a result |
| residual | a worker that consumes wall-clock or writes garbage produces invalidity or a quarantined output, both infrastructure facts and neither a scientific outcome |

### §P1-7.5 The bootstrap sequence

```text
PCS side:
 c1.  lock_fd := _open("SPAWN.lock", _O_RDWR | _O_CREAT | _O_CLOEXEC, 0o600,
                       dir_fd = T_PCB_FD_RUNTIME_ROOT)
      _flock(lock_fd, _LOCK_EX | _LOCK_NB), retried at
      T_SUPERVISOR_POLL_INTERVAL_NS until T_SPAWN_LOCK_ACQUIRE_TIMEOUT_NS; on
      expiry take the stuck-holder route of §P1-11.2
      readback, mandatory: require type(_fcntl(lock_fd, _F_GETFD)) is int and
      (_fcntl(lock_fd, _F_GETFD) & _FD_CLOEXEC) != 0
        otherwise ⇒ LOCK_FD_NOT_CLOEXEC: fail-closed refusal, no fork, no
                    record installed, lock released
      There is no F_SETFD repair path, so the mechanism is single-valued.
      Then run the singleton preflight of §P1-11.1 for all four records.
 c2.  install SPAWNING.json per §P1-5.1
 c3.  create the four channels rel1, rel2, rel3 and boot with
      _pipe2(_O_NONBLOCK | _O_CLOEXEC)
 c4.  pid_mid := _fork()
        a return that is not an int, or is <= 0, or any BaseException ⇒
        ownership is never established and the pre-fork fail-closed body applies
      OWNERSHIP(pid_mid) := OWNED
 c5.  in the PCS close rel1 read, rel2 read, rel3 read and boot write
 c6.  read /proc/<pid_mid>/stat for the kernel start identity per §P1-10.3
 c7.  install SPAWNING_MIDDLE.json per §P1-5.1
 c8.  write exactly one byte b"\x01" on rel1 write; close rel1 write
 c9.  read one group-report line from boot read, bounded by
      T_SPAWN_IDENTITY_WAIT_TIMEOUT_NS at T_SUPERVISOR_POLL_INTERVAL_NS
 c10. verify from the kernel: /proc/<middle_child_pid>/stat is live and its
      start identity equals the recorded one; getsid and getpgid of that pid
      both equal middle_child_pid; and the reported session_id and
      process_group_id both equal middle_child_pid
 c11. install SPAWNING_GROUP.json with group_verified true, installable only
      after c10 succeeds
 c12. write exactly one byte b"\x02" on rel2 write; close rel2 write
 c13. read one bootstrap-report line from boot read, bounded as at c9
 c14. verify the reported supervisor_pid is live, its start identity equals the
      reported value, and getpgid of it equals process_group_id
 c15. install SPAWNING_CHILD.json per §P1-5.1
 c16. write exactly one byte b"\x01" on rel3 write; close rel3 write
 c17. poll for a live-verified SUPERVISOR_IDENTITY.json, bounded by
      T_SPAWN_IDENTITY_WAIT_TIMEOUT_NS
 c18. release SPAWN.lock. The supervisor's retained descriptor keeps the flock
      until it closes slot 3.

Middle side:
 m0.  the literal first instruction: read one byte from rel1 read, which is
      already O_NONBLOCK, in a loop paced at T_SUPERVISOR_POLL_INTERVAL_NS and
      bounded by T_SPAWN_IDENTITY_WAIT_TIMEOUT_NS
        b"\x01"                   ⇒ m1
        b"" meaning EOF           ⇒ os._exit(3)
        any other byte            ⇒ os._exit(3)
        the bound expires         ⇒ os._exit(3)
      Nothing else executes before this read. The loop performs no filesystem
      write and changes no shared state.
 m1.  close rel1 read, rel1 write, rel2 write, rel3 write and boot read
 m2.  os.setsid()
 m3.  verify getsid(0) == getpgid(0) == getpid(); any inequality ⇒ os._exit(3)
 m4.  write exactly one group-report line per §P1-5.3 on boot write. It cannot
      block: one line of at most 4096 bytes into an empty pipe is under
      PIPE_BUF. A raised EPIPE ⇒ os._exit(3)
 m5.  read one byte from rel2 read with the same bounded loop:
        b"\x02" ⇒ m6 ; EOF, any other byte, or bound expiry ⇒ os._exit(3)
 m6.  close rel2 read
 m7.  pid_gc := _fork()
 m8.  read /proc/<pid_gc>/stat and /proc/sys/kernel/random/boot_id; write
      exactly one bootstrap-report line per §P1-5.3 on boot write; close boot
      write. A raised EPIPE ⇒ os._exit(3)
 m9.  os._exit(0)

The middle performs no filesystem write, holds no lock epoch, executes no
wait-family call, and every wait it performs is bounded.
```

### §P1-7.6 The grandchild pre-exec sequence

```text
G-1. HOIST the eight descriptors the supervisor must retain — lock_fd, the boot
     write end, the harness source, the protocol socket peer, the
     role-bootstrap source, the src directory, the interpreter and the package
     root — to the target set {3,4,5,6,7,8,9,10}. Postcondition: eight pairwise
     distinct numbers, all greater than 10.
                                   violated ⇒ GRANDCHILD_FD_HOIST_FAILED
G-2. for slot s in ascending order 3,4,5,6,7,8,9,10:
         _dup2(h[s], s, inheritable=True)
     Slot 3's source is the hoisted lock_fd. The keyword inheritable=True is
     passed explicitly, never left to a default, and it is what clears
     FD_CLOEXEC on the destination.
G-3. readback, mandatory, for every slot:
       require (_fcntl(s, _F_GETFD) & _FD_CLOEXEC) == 0
                                   otherwise ⇒ GRANDCHILD_FD_NOT_INHERITABLE
G-4. close every hoisted source, ascending, tolerating EBADF. In particular the
     original lock_fd copy is closed here, so the grandchild holds exactly one
     lock descriptor, at slot 3.
G-5. close every remaining inherited descriptor outside {0,1,2} together with
     slots 3 through 10, ascending, once each, tolerating EBADF; redirect stdio
     to _devnull
G-6. _execve("/proc/self/fd/9", the SUPERVISOR argv of §P1-7.4, {})
     failure ⇒ os._exit(3), nothing written, nothing unlinked
```

**The lock across the whole tree.** The PCS holds `lock_fd` with `FD_CLOEXEC`
set, so it never enters a spawned role. `fork` copies the descriptor together
with its flag, and `FD_CLOEXEC` is consulted only at `execve`, so the middle's
and the grandchild's fork-shared references are live and the `flock` persists
while either lives. `G-2` creates a second descriptor onto the same open file
description at slot 3 with the flag clear, and `G-4` closes the original, so the
supervisor retains exactly one lock reference across its `execve`. The `flock`
releases only when the PCS, the middle and the supervisor have all closed. No
role other than the supervisor ever holds a reference.

---

## §P1-8. The protocol

### §P1-8.1 Two channels

| Channel | Endpoints | Kind | Operations |
|---|---|---|---|
| caller | caller and PCS | two anonymous pipes at descriptors 3 and 4 | exactly one: `SPAWN_SUPERVISOR` |
| supervisor | supervisor and PCS | one `AF_UNIX`, `SOCK_SEQPACKET`, protocol 0 pair created by the PCS before the `c4` fork, its peer inherited to slot 6 | the nine of §P1-8.3 |

`SOCK_SEQPACKET` is chosen because it is connection-oriented,
message-boundary-preserving and reliable: one `sendmsg` of a payload of at most
4096 bytes is delivered as exactly one record or not at all, so partial reads
and partial writes are impossible at the record level and no partial-record
state exists.

### §P1-8.2 The caller-channel records

One line each, newline-terminated, ASCII, no NUL, at most
`T_CONTROL_FRAME_MAX_BYTES`, fields separated by exactly one `0x20`, parsed with
a byte split on `0x20` only: no JSON parser, no regular expressions, no hashing.

```text
REQUEST, exactly six fields:
  0  b"philosophia.officina.t-process-control-request.v1"   literal
  1  b"1"                                                   protocol version
  2  operation, from the closed one-element set {b"SPAWN_SUPERVISOR"}
  3  spawning_id_nonce: exactly 64 bytes from [0-9a-f]
  4  caller_pid: decimal, 1 to 7 digits, no leading zero
  5  caller_start_identity: decimal, 1 to 20 digits
REPLY, exactly five fields:
  0  b"philosophia.officina.t-process-control-reply.v1"     literal
  1  b"1"
  2  outcome, from {b"SUPERVISOR_LIVE", b"REFUSED", b"BLOCKED"}
  3  detail: one token from §P1-2.6's closed set
  4  retryable: b"0" or b"1"
```

No field is a path, a module or symbol name, a callable, a signal number, a pid
to signal, a file descriptor, a timeout, a resource value, or a format string.
Neither record is persisted, archived, hashed into a signed set, or given a
durable path.

**The reply pipe is the sole authoritative result.** A competing waiter inside
the caller may reap the PCS before the caller's own wait, in which case the exit
status is lost; the status is therefore advisory diagnostics only. A caller that
reads EOF without a complete reply line has learned nothing: it must not infer
success, failure, retryability or liveness, and it routes to §P1-11.6.

### §P1-8.3 The nine operations

Common request prefix: the literal schema `philosophia.officina.t-pcs.v1`,
version `b"1"`, `generation_id` of 64 lowercase hexadecimal characters, and
`request_id`, a decimal of 1 to 19 digits with no leading zero, strictly
increasing within a generation, followed by the opcode. Common response prefix:
the same schema and version, the echoed `generation_id` and `request_id`,
`status` from `{OK, REFUSED, INVALID, REPLAYED}`, `detail` from §P1-2.6,
`handle_id` as a decimal or `b"-"`, and `fds_redelivered` as `b"0"` or `b"1"`.

| Opcode | Request operands | Preconditions | Response operands | Descriptors |
|---|---|---|---|---|
| `SPAWN_ROLE` | `role` in `{CONTROLLER, WORKER}`; `argv_template_id`, 64 hex; `spawn_intent_id`, 64 hex | the durable spawn-intent record named in §P1-13.2 exists, is well-formed, and its `argv_template_sha256` matches; the generation is live | `handle_id` | **3** |
| `AWAIT_STOP` | `handle_id`; `deadline_ticks`, decimal of 1 to 6 digits, in units of `T_SUPERVISOR_POLL_INTERVAL_NS`, at most `T_SPAWN_SELF_STOP_TIMEOUT_NS` | handle state `SPAWNED` | `outcome` in `{STOPPED, EXITED, TIMEOUT}`; `start_identity`; `pgid_is_leader` in `{0,1}` | 0 |
| `SIGNAL_ROLE` | `handle_id`; `sig` in `{CONT, TERM, KILL, STOP, PROBE}` | ownership `OWNED`; **role is not `WATCHDOG`** | `result` in `{SENT, GONE, DENIED, STRUCTURAL_VIOLATION}` | 0 |
| `SIGNAL_GROUP` | `handle_id`; `sig` in `{CONT, TERM, KILL, STOP, PROBE}` | a kernel-verified group is recorded for the handle; role is not `WATCHDOG` | `result` in `{SENT, GONE, DENIED, STRUCTURAL_VIOLATION}` | 0 |
| `REAP_ROLE` | `handle_id` | ownership is not `REAPED` | the six-result token of §P1-10.2 | 0 |
| `SPAWN_WATCHDOG` | none | no live watchdog handle exists in this generation | `handle_id` | **2** |
| `RELEASE_HANDLE` | `handle_id` | handle state `REAPED` | none | 0 |
| `SHUTDOWN` | none | no handle is live | none | 0 |
| `PING` | none | none | `pcs_uptime_ticks` | 0 |

**`SPAWN_WATCHDOG` has exactly one meaning.** Its precondition, the absence of a
live watchdog handle, is satisfied both at generation start and after a previous
watchdog's death has been proved. The first watchdog and every replacement are
created by the same operation with the same semantics, the same isolation and
the same one-detector model. No replacement-specific opcode, handle role or
degradation flag exists.

Target argv never crosses the wire: the PCS reads the spawn-intent record named
in §P1-13.2 from the runtime root and builds the argv of §P1-7.4 itself.

**No field of any request or response carries a PID, a descriptor number, a
path, a target argv, a signal number, a symbol, a callback, or an unbounded
integer.**

### §P1-8.4 Correlation and ordering

A `generation_id` that does not match the PCS's current generation yields
`INVALID` with `WRONG_GENERATION`, no action taken and no state destroyed. A
`request_id` less than or equal to the highest journalled id is a replay per
§P1-8.6; a gap is permitted and is recorded. Exactly one response is emitted per
request, correlated by the pair of `generation_id` and `request_id`. **The
supervisor issues one outstanding request at a time**, which removes all
interleaving; an out-of-order or unmatched response is `TRANSPORT_STRUCTURAL`.
An unknown opcode, field count, handle, or handle state yields `INVALID` with
the corresponding token, with no side effect, no descriptor, and no journal
entry beyond the rejection record.

### §P1-8.5 The handle model

```text
handle_id -> { pid, start_identity, pgid_or_null, role, generation_id,
               fd_bundle, state, ownership, fd_delivery }
  role        in { CONTROLLER, WORKER, WATCHDOG }
  state       in { SPAWNED, STOPPED, RUNNING, REAPED }
  ownership   in { OWNED, CONTRADICTED, REAPED }
  fd_delivery in { PENDING, CONFIRMED, UNCONFIRMED }
  fd_bundle   is the set of role-side descriptors the PCS retains for it
```

Invariants: handle ids are never reused, within or across generations;
`SIGNAL_ROLE` and `SIGNAL_GROUP` require ownership `OWNED`; `SIGNAL_GROUP`
additionally requires a kernel-verified group; both signal opcodes are refused
when the handle's role is `WATCHDOG`; `RELEASE_HANDLE` requires state `REAPED`;
no wait site runs after ownership becomes `REAPED`; and every handled process is
a direct child of the PCS.

### §P1-8.6 Journal, acknowledgement, replay

```text
J1. receive and validate the request
      crash ⇒ nothing happened; a redelivery is a fresh request
J2. append { generation_id, request_id, opcode, operands, state: ACCEPTED } and
    fsync
      crash ⇒ the entry is ACCEPTED with no result: the operation is
              inconclusive, and because no PCS may adopt a live generation this
              is a whole-generation invalidity and never a silent retry
J3. perform the syscall
      crash ⇒ as J2, and additionally a possibly-live orphan role, routed by
              §P1-11.4
J4. append { ..., state: COMPLETED, outcome, handle_id, fd_vector_len } and
    fsync
      crash ⇒ the result is durable and a redelivery replays it
J5. send the response, with descriptors if and only if §P1-8.7's vector table
    says so
      crash ⇒ durable but undelivered; a redelivery replays it without
              descriptors
J6. on receiving the acknowledgement append { ..., state: ACKED } and fsync

REPLAY of an already-journalled pair of generation_id and request_id:
  ACCEPTED  ⇒ INVALID with OPERATION_INCONCLUSIVE; no syscall is ever
              re-performed
  COMPLETED ⇒ the recorded status, detail and handle, with status REPLAYED,
              fds_redelivered 0, and no descriptors
  ACKED     ⇒ the recorded status, detail and handle, with status REPLAYED,
              fds_redelivered 0, and no descriptors
```

> **Descriptors are never re-sent.** Re-sending would install a second,
> independent copy of a capability that no accounting in this contract could
> reconcile. A supervisor that loses the descriptors of a `SPAWN_ROLE` or
> `SPAWN_WATCHDOG` response cannot recover them; the handle is marked
> `FD_DELIVERY_UNCONFIRMED` and the generation routes to §P1-11.6. An
> acknowledgement lost on a descriptor-bearing reply therefore invalidates the
> generation rather than retrying the transfer. This is the accepted narrowing
> of B1 named in §P1-1.3, and it applies to exactly two of the nine operations.

### §P1-8.7 Descriptor passing

```text
SEND, from the PCS to the supervisor, the only direction carrying descriptors:
  anc := b"".join(fd.to_bytes(4, "little") for fd in fds)
  n := _sendmsg(sock, [payload],
                [(_SOL_SOCKET, _SCM_RIGHTS, anc)] if fds else [])
  require n == len(payload)              otherwise TRANSPORT_STRUCTURAL
  int.to_bytes and int.from_bytes are builtin int methods requiring no import,
  and width 4 with byte order "little" is exactly the native int representation
  on the platform of §P1-2.1. Neither array nor struct is used.

The only legal descriptor vectors:
  every request                                  0
  SPAWN_ROLE with status OK                      3, in this order: control
                                                 request write end, control
                                                 reply read end, status read
                                                 end; all S_ISFIFO
  SPAWN_WATCHDOG with status OK                  2, in this order: update write
                                                 end, ack read end; both
                                                 S_ISFIFO
  every refusal and every other operation        0
  maximum per message                            3
  ancillary buffer                               _CMSG_SPACE(12)

RECEIVE, supervisor side:
 B-1. r := _recvmsg(sock, T_CONTROL_FRAME_MAX_BYTES, _CMSG_SPACE(12),
                    _MSG_CMSG_CLOEXEC)
      _MSG_CMSG_CLOEXEC is mandatory: it sets FD_CLOEXEC atomically with
      installation, so no received descriptor can leak across an exec.
      If B-1 raises any BaseException, the contract-authored handler body is
      exactly one statement:
            _exit_(T_PCS_EXIT_RECV_UNENUMERABLE)
      What is specified and provable: the handler is a single
      `except BaseException:` clause whose body is that one call, with no other
      statement, call, attribute access, name binding, else clause or finally
      clause; the contract authorises no cleanup, callback, unwind, flush,
      close or logging logic there; and the contract installs no interpreter
      exit handlers of its own.
      What is NOT claimed: that no Python trace, profile or audit hook, no
      signal handler, no finalizer, no exception-machinery step and no other
      same-process callback can execute between the C call's failure and that
      statement. In a contaminated interpreter this contract cannot establish
      that and does not assert it. §P1-12.4 names the resulting exposure.
 B-2. non-aborting parse. violation_flags := the empty set
      for every returned control item, in order, without early exit:
        if (level, type) is not (_SOL_SOCKET, _SCM_RIGHTS):
              add ANCILLARY_UNEXPECTED_ITEM to violation_flags; the item
              carries no payload of this kind and contributes no descriptor;
              the loop continues
        else:
              if len(cdata) % 4 != 0: add ANCILLARY_RAGGED
              if len(cdata) > 12:     add ANCILLARY_OVERLONG
              n := len(cdata) - (len(cdata) % 4)
              received += [int.from_bytes(cdata[i:i+4], "little")
                           for i in range(0, n, 4)]
      `received` is now the complete parsed vector.
 B-3. also non-aborting: add to violation_flags for MSG_CTRUNC, for MSG_TRUNC,
      for a count that differs from this opcode and status, and for any element
      whose _fstat type differs from the expected slot type.
 B-4. if violation_flags is non-empty: close exactly the descriptors in
      `received`, de-duplicated by numeric value, in ascending numeric order,
      once each, with _close, tolerating EBADF. Close nothing else. Never
      enumerate /proc/self/fd. Never touch another message's descriptors or any
      live handle's descriptor bundle. Then route to §P1-11.6.
 B-5. on success the descriptors become the handle's descriptor bundle; they
      already carry FD_CLOEXEC.
```

> **Why the parsed vector is exactly the installed set.** On Linux, when a
> `recvmsg` control buffer is too small for all queued descriptors of this
> kind, the kernel installs exactly the number that fits, computed as the
> available space divided by the size of a native int and capped by the queued
> count; it writes their numbers into the returned control data; it sets the
> returned control length to the length for the number actually installed; it
> sets `MSG_CTRUNC`; and it releases every queued descriptor it did not
> install. An installed but unreported descriptor therefore cannot exist at the
> kernel boundary. **This is a reviewer-verifiable interface fact, not an
> author-proven one.**

**Ownership across the transfer.** Before the send the PCS holds both ends of
every pipe. The mechanism duplicates rather than transfers, so the send does not
move ownership. Immediately after a successful send the PCS closes its copies of
the supervisor's ends unconditionally, in a fixed order, and keeps the role's
ends. If the send raises or returns short, the PCS still holds the supervisor's
ends and closes them. After the supervisor's receive the descriptors are its
own; after its acknowledgement the PCS sets the handle's `fd_delivery` to
`CONFIRMED`. If the supervisor dies with descriptors still buffered in the
socket, Linux releases them when the socket closes, so no descriptor leaks.
**Every descriptor has exactly one owning slot in exactly one process at any
instant; every close is performed once by the slot's owner tolerating `EBADF`;
and the two remediation paths act in different processes, so no double close
exists at any cut.**

---

## §P1-9. Role lifecycles

### §P1-9.1 Controller and worker

Created only by `SPAWN_ROLE`. The PCS reads the spawn-intent record named in
§P1-13.2, builds the argv of §P1-7.4, creates the control request, control
reply and status pipes with `_pipe2(_O_CLOEXEC)`, hoists, and calls
`_posix_spawn` on the role bootstrap with `setsid=True`, an empty environment
and the isolation flags. The role's ends are inherited at slots 3, 4 and 6; the
supervisor's ends are returned as the three-descriptor vector of §P1-8.7.

The role self-stops at `A-12` before any target behaviour. `AWAIT_STOP`
performs the bounded `waitpid(pid, WNOHANG|WUNTRACED)` loop and requires
`WIFSTOPPED`; its result is what permits the durable process-claim write named
in §P1-13.3. Termination uses `SIGNAL_ROLE` with `TERM` then `KILL` on the
schedule of §P1-10.5, and `SIGNAL_GROUP` only after a kernel-verified group
exists. Death is proved by `REAP_ROLE`.

### §P1-9.2 The watchdog, with its complete operative property set

Created only by `SPAWN_WATCHDOG`, as an isolated role with `setsid=False`, so
it is not a session leader and is never a `killpg` target. The two-descriptor
vector gives the supervisor the update pipe write end and the ack pipe read end.
An `execve`'d watchdog has a fresh address space and therefore contains no
capability by construction.

**Every operative property of the watchdog under this contract, enumerated:**

1. it holds no lock of any kind, and receives no `SPAWN.lock` descriptor;
2. it holds no capability object;
3. it writes nothing under the runtime root's `runtime/` subtree;
4. it appends to no ledger;
5. it settles nothing, and produces no settlement, quarantine, promotion or
   capacity effect;
6. it communicates only over its two sealed pipes at slots 3 and 4;
7. it emits NO freeze observation and writes no record of any class. The
   freeze-witness record class of §P1-13.2 row 4 —
   `philosophia.officina.t-freeze-observation.v1`, installed under
   `WATCHDOG/FREEZE/` — is written ONLY by the supervisor role process, on the
   two routes of §P1-13.9, and by no other process on any path. SEPARATELY, AND
   IN A DIFFERENT CLASS: the peer amendment's `ABSENT` route writes
   `philosophia.officina.t-freeze-fallback-observation.v1` under
   `WATCHDOG/FREEZE_FALLBACK/`, written by the supervisor under `T_RUNTIME.lock`.
   That object is NOT a record of row 4's class, is NOT written by row 4's writer
   acting in row 4's capacity, and is NOT installed in row 4's namespace; it is
   one of the two adjacent peer artifacts named below and is outside §P1-13.2
   entirely;
8. it verifies the supervisor's identity against the supervisor identity record
   of §P1-13.2 row 3 and never by any parent relationship;
9. it acknowledges each published table on the ack pipe; the supervisor treats
   an absent acknowledgement past `T_WATCHDOG_ACK_ABSENCE_TIMEOUT_NS` as
   watchdog death;
10. it detects supervisor death by exactly one mechanism, EOF on its update read
    end, and by no other;
11. it must not use `getppid()` to infer supervisor death and must not treat a
    change in `getppid()` as any signal about the supervisor: its parent is the
    PCS, so a change means the PCS died, a distinct condition in which the
    supervisor may still be alive. **The prohibition is unchanged and is not
    weakened; only its rationale is corrected.**
    `[W-B]` The watchdog executes no freeze on any path, so no misuse of
    `getppid()` can produce a freeze at all; the prohibition stands because the
    inference is FALSE, not because of what it would trigger.
    `[W-A]` A watchdog that made that inference would send its one authorized
    `t-wd-freeze.v1` record against a generation whose peer control endpoint may
    still be live, which the `G-1` gate REFUSES with `PEER_ENDPOINT_LIVE` and no
    syscall, so no false freeze is reachable; the prohibition stands because the
    inference is FALSE, not because of what it would trigger;
12. on observing update-pipe EOF it WRITES NOTHING, FREEZES NOTHING, SIGNALS
    NOTHING, and exits, settling nothing.
    `[W-A]` Before exiting it sends exactly one constant `t-wd-freeze.v1` record
    on slot 6 and waits at most `T_WATCHDOG_ACK_ABSENCE_TIMEOUT_NS` for one reply
    record; that record is a P1 transport frame, is never a peer-owned record and
    is never evidence.
    `[W-B]` It sends nothing;
13. it is never sent a signal of any number by any process of this contract, on
    any path.

**Termination.** The supervisor closes the update pipe write end; the watchdog
observes EOF, WRITES NOTHING, and exits; the PCS reaps it on `REAP_ROLE`. If a positive reap is not obtained within
`T_WATCHDOG_ACK_ABSENCE_TIMEOUT_NS` after the close, the route records
`WATCHDOG_UNREAPED` and takes §P1-11.6.

### §P1-9.3 Supervisor

Reached by the `c4` fork, then the `m7` fork, then `G-6`'s `execve`. It holds
`SPAWN.lock` at slot 3 until its identity record is live-verified, then closes
it. It is the direct parent of nothing and the reaper of nothing; a wildcard
wait in it returns `ECHILD`. It holds opaque handles and cannot express a PID.

### §P1-9.4 Shutdown

```text
S-1. stop admitting; drain and settle through the settlement interface of
     §P1-13.4
S-2. for every live controller and worker handle: SIGNAL_ROLE or SIGNAL_GROUP
     per §P1-10.5, then REAP_ROLE until a positive reap, then RELEASE_HANDLE
S-3. close the watchdog update pipe write end
S-4. the watchdog observes EOF, writes nothing, os._exit(0)
S-5. REAP_ROLE on the watchdog handle until, bounded by
     T_WATCHDOG_ACK_ABSENCE_TIMEOUT_NS:
       REAPED_POSITIVE      ⇒ death proved; RELEASE_HANDLE; go to S-6
       CONTRADICTED_ECHILD  ⇒ death not proved ⇒ §P1-11.6. The supervisor may
                              still proceed, because it removes no record on a
                              false death proof and the watchdog, if alive,
                              exits at its own update-EOF route
       STRUCTURAL_VIOLATION ⇒ death not proved ⇒ §P1-11.6. The supervisor may
                              still proceed, on these two grounds: it removes
                              no record on a false death proof, and the
                              watchdog, if alive, exits at its own update-EOF
                              route
       NOT_YET at the bound ⇒ WATCHDOG_UNREAPED ⇒ §P1-11.6
S-6. SHUTDOWN
       HANDLES_LIVE ⇒ clear the offending handle first
       OK           ⇒ the PCS closes its ends, releases SPAWN.lock, and exits
S-7. the supervisor closes its remaining descriptors and exits
```

**Watchdog death is observed and reaped before the supervisor exits, or the
generation is explicitly invalid. There is no third branch.**

---

## §P1-10. Ownership, waiting, signalling, identity

### §P1-10.1 Ownership

```text
OWNERSHIP(pid) in { OWNED, CONTRADICTED, REAPED }

  OWNED         set at exactly one place: a fork or posix_spawn returning a
                value greater than zero in the PCS, in a generation whose P-g
                completed successfully. Meaning: pid denotes this PCS's own
                child, running, stopped or zombie, or nothing at all; it can
                denote no other process. Authorizes os.kill and os.waitpid on
                that pid.
  CONTRADICTED  set irreversibly on the first of: a wait returning ECHILD; a
                signal returning ESRCH; a /proc read that is PRESENT_VALID with
                no captured identity and a ppid that differs from getpid(); or
                a captured start identity that mismatches. Authorizes a
                targeted wait only. No signal, ever again. No start identity
                may be captured after it.
  REAPED        set at exactly one place: a targeted wait returning that pid.
                Authorizes nothing; the pid may now be reused.

Transitions: OWNED to CONTRADICTED, OWNED to REAPED, CONTRADICTED to REAPED.
os.kill executes if and only if OWNERSHIP is OWNED.
```

**PID-reuse proof.** Linux allocates a pid only when no task holds it. The child
holds its pid from the moment the create call returns. On termination the kernel
auto-reaps only if the parent's `SIGCHLD` action is `SIG_IGN` or carries
`SA_NOCLDWAIT`; step `P-g` made it `SIG_DFL` with neither before the create, and
verified the ignore and handler halves against the kernel's own masks by the
exact relations of `g-5`. The task therefore becomes and stays a zombie holding
its pid until a targeted wait from this process returns it, at which instant
`REAPED` forbids every further use. The window between an identity observation
and a signal is therefore closed by a property established before the child
existed, not by a `/proc` read.

**The sole-reaper premise is a process-boundary fact, not a prohibition.** A
wait reaps only a direct child of the calling thread group. Every process this
contract signals or waits on is a direct child of the PCS, and the PCS is
constructed by `execve` with the four isolation flags so that no user code ran
before its module body, is verified single-tasked by two independent kernel
readbacks at `P-c` and `P-d`, and is verified free of catching handlers by the
`g-5` relation. No entity outside it can reap its children.

### §P1-10.2 The wait classifier, one for all sites

```text
WAIT_ONE(pid, site) -> REAPED_POSITIVE | NOT_YET | CONTRADICTED_ECHILD
                     | RETRY_EINTR | INCONCLUSIVE_OTHER | STRUCTURAL_VIOLATION

  PRECONDITION: OWNERSHIP(pid) is not REAPED. An invocation after REAPED is a
  contract violation, not a route: perform no syscall, send no signal, and
  treat the site as complete.

  r := _waitpid(pid, _WNOHANG)

  structural classification of the returned object, in this order:
    not a tuple; length not 2; type(r[0]) is not int or type(r[1]) is not int,
      where the test is `type(x) is int` so that bool is rejected; r[0] < 0;
      r[0] != 0 and r[0] != pid; r[0] == 0 and r[1] != 0; r[1] < 0 or
      r[1] > 0xFFFF                              ⇒ STRUCTURAL_VIOLATION
    r == (pid, status)                           ⇒ REAPED_POSITIVE, and
                                                   OWNERSHIP := REAPED
    r == (0, 0)                                  ⇒ NOT_YET

  exception classification, total over every BaseException:
    OSError with errno ECHILD  ⇒ CONTRADICTED_ECHILD, and
                                 OWNERSHIP := CONTRADICTED
    OSError with errno EINTR   ⇒ RETRY_EINTR: re-issue the same targeted call
                                 at T_SUPERVISOR_POLL_INTERVAL_NS within the
                                 site's deadline
    OSError with any other errno ⇒ INCONCLUSIVE_OTHER
    OSError with errno None or a non-int errno, SystemExit, KeyboardInterrupt,
      GeneratorExit, MemoryError, RecursionError, or any other BaseException
                               ⇒ STRUCTURAL_VIOLATION

  A stop or continue status can never be returned: WNOHANG without WUNTRACED
  reports neither.
```

**Only `REAPED_POSITIVE` sets `REAPED`, and it is the only proof of death
anywhere in this contract. `ECHILD` is never death.** `STRUCTURAL_VIOLATION`
means the running primitive is not the genuine one; its single continuation at
every site is: never death, never `REAPED`, set `OWNERSHIP` to `CONTRADICTED`
irreversibly, send no signal ever again, install, modify or remove no record,
and take that site's `CONTRADICTED_ECHILD` continuation.

The same six-way classification applies to `_kill` and `_killpg`, where the
return must be `None` and any other object or any `BaseException` outside the
errno set of §P1-10.5 is `STRUCTURAL_VIOLATION` leading to `CONTRADICTED` and no
further signal; and to `_fork` and `_posix_spawn`, where the return must be an
`int` greater than zero and anything else means ownership is never established.

### §P1-10.3 The `/proc` observation

```text
STAT_OBSERVE(pid) -> ABSENT | PRESENT_VALID | UNREADABLE | UNPARSABLE | ERROR
  read /proc/<pid>/stat in full:
    ENOENT or ESRCH   ⇒ ABSENT
    EACCES or EPERM   ⇒ UNREADABLE
    EINTR             ⇒ bounded retry at T_SUPERVISOR_POLL_INTERVAL_NS until
                        the step's deadline; on expiry ⇒ ERROR
    any other OSError ⇒ ERROR
  parse the 20th whitespace-separated token after the final ")" , which is the
  kernel start time, together with the state field and the ppid field:
    no final ")", a short token list, a non-integer field, or any parse failure
                      ⇒ UNPARSABLE
    success           ⇒ PRESENT_VALID with (start_identity, ppid, state)
Only ABSENT and PRESENT_VALID may contribute to an identity or death
conclusion. UNREADABLE, UNPARSABLE and ERROR authorize no kill, no unlink and
no death conclusion.
```

### §P1-10.4 The identity decision table

`IDENTITY_OBSERVE` decides exactly two things: whether a start identity may be
captured, which is what makes a durable record truthfully constructible, and
whether the observation contradicts ownership. It does not gate signalling;
ownership does.

| # | Entry ownership | `STAT_OBSERVE` result | Captured identity | `ppid` compared with `getpid()` | Verdict | Capture? | Ownership after | Continuation |
|---|---|---|---|---|---|---|---|---|
| I-1 | `OWNED` | `PRESENT_VALID` | present | not consulted | the captured identity matches | no | `OWNED` | signal per §P1-10.5 |
| I-2 | `OWNED` | `PRESENT_VALID` | present | not consulted | the captured identity mismatches, which contradicts ownership | no | `CONTRADICTED` | send no further signal; the earlier truthful capture remains valid and a durable handoff record may still be built from it |
| I-3 | `OWNED` | `PRESENT_VALID` | absent | equal | identity confirmed by parentage | yes, capture `start_identity` | `OWNED` | signal per §P1-10.5 |
| I-4 | `OWNED` | `PRESENT_VALID` | absent | not equal | contradiction: an owned unreaped child necessarily has a ppid equal to `getpid()`, so this is the last line of defence against a failed normalization | no, because capturing would write another process's identity into a durable record | `CONTRADICTED` | send no signal, ever; capture nothing |
| I-5 | `OWNED` | `ABSENT` | present or absent | not consulted | not identity-bearing; absence is never death | no | `OWNED` | `WAIT_ONE` decides. Ownership still authorizes the signal schedule of §P1-10.5, and the absence of a `/proc` entry authorizes no unlink and no death conclusion |
| I-6 | `OWNED` | `UNREADABLE` | present or absent | not consulted | not identity-bearing | no | `OWNED` | ownership still authorizes the signal schedule of §P1-10.5; only the durable identity is unavailable, so a handoff record cannot be built from this observation |
| I-7 | `OWNED` | `UNPARSABLE` | present or absent | not consulted | not identity-bearing | no | `OWNED` | ownership still authorizes the signal schedule of §P1-10.5; only the durable identity is unavailable, so a handoff record cannot be built from this observation |
| I-8 | `OWNED` | `ERROR` | present or absent | not consulted | not identity-bearing | no | `OWNED` | ownership still authorizes the signal schedule of §P1-10.5; only the durable identity is unavailable, so a handoff record cannot be built from this observation |
| I-9 | `REAPED` | any | present or absent | not consulted | evaluating this function after a reap is a contract violation, not a route | no | `REAPED` | perform no syscall and send no signal |
| I-10 | `CONTRADICTED` | any | present or absent | not consulted | the entry state already forbids capture and signalling | no | `CONTRADICTED` | send no signal; a durable handoff record may be built only from an identity captured before the contradiction |

### §P1-10.5 Signalling

```text
SIGNAL_ATTEMPT(pid, sig) -> SENT | GONE | INTERRUPTED | DENIED | ERROR
  PRECONDITION: OWNERSHIP is OWNED. Any other state is a contract violation and
  no signal is sent.
  sig is 15 or 9 for the termination schedule; killpg is used only against a
  kernel-verified group.
  _kill(pid, sig)
    success  ⇒ SENT: delivered, or discarded because the target is already a
               zombie. Signalling a zombie is safe, because an unreaped zombie
               still holds the pid. SENT alone proves nothing.
    ESRCH    ⇒ GONE. Under OWNED this is a contradiction and not a race: an
               owned unreaped child is a task in some state and kill would
               succeed. Set OWNERSHIP to CONTRADICTED and send no further
               signal.
    EINTR    ⇒ INTERRUPTED: retry the same signal at
               T_SUPERVISOR_POLL_INTERVAL_NS within the step's deadline; on
               expiry ⇒ ERROR
    EPERM    ⇒ DENIED: send no further signal in this schedule; ownership is
               not contradicted; the reaper loop continues
    any other OSError ⇒ ERROR: as DENIED

Termination schedule, inside the one existing deadline, adding no constant:
  t0 := the step's monotonic start ; D := T_SPAWN_IDENTITY_WAIT_TIMEOUT_NS
  1. if OWNED: SIGNAL_ATTEMPT(pid, 15)
  2. poll WAIT_ONE at T_SUPERVISOR_POLL_INTERVAL_NS until t0 + D/2
  3. if not reaped by t0 + D/2 and OWNED: SIGNAL_ATTEMPT(pid, 9)
  4. poll WAIT_ONE until t0 + D
  5. at t0 + D without a positive reap ⇒ the terminal selection of §P1-11.5
  A poll sample exactly at t0 + D/2 or exactly at t0 + D is treated as expired,
  the comparison being greater-or-equal, so no edge is ambiguous. SIGKILL
  cannot be caught, blocked or ignored and terminates a stopped process, so a
  stopped child is reached without any /proc dependence.
```

### §P1-10.6 Watchdog freeze authority — the negative surface, asserted

```text
The watchdog role process is a control-plane LIVENESS SENSOR. On no path does
it execute a freeze, prove quiescence, send or receive a signal, call killpg or
kill, write freeze evidence, write anything under runtime/, append the ledger,
settle anything, hold a runtime lock, hold a capability, or exercise validity
authority.

It owns a deadline as a DATUM it publishes an acknowledgement for. It never owns
a deadline as an ACTION.

EXACTLY ONE PEER-LAYER OPERATION IS PERMITTED, AND IT IS REQUIRED: the read-only
verification of the supervisor identity record of §P1-13.2 row 3 (§P1-9.2
property 8, invariant 87). A read installs nothing, decides nothing, creates no
durable object, and is invisible to every acceptance predicate and to SW-1
through SW-5. It is not an authority.

[W-A] One further P1-layer operation is permitted: emitting exactly one constant,
      target-free t-wd-freeze.v1 transport frame on slot 6. It is a P1 transport
      frame, is never a peer-owned record, is never evidence, and names no target.
[W-B] No further operation of any kind is permitted.

THE WATCHDOG PRODUCES NO DURABLE OBJECT OF ANY CLASS. It is therefore not a
witness in any sense, because there is no object for it to be a witness in.

THE HISTORICAL CHAIN SAID OTHERWISE AND IS PROVENANCE. Historical sections that
made the watchdog the freezer, the quiescence prover or the evidence recorder —
including historical §W3.3, §W6.5 and their carried references — are immutable
provenance under authority level 3 and are superseded IN MEANING, without any
edit to their bytes, by this section, by §P1-13.2 row 4, by §P1-13.9, and by §A2
of the peer amendment. No reading of any historical document restores a watchdog
executor, a watchdog quiescence proof or a watchdog evidence writer.
```

### §P1-10.7 The PCS freeze classifier — the second signed execution site

```text
The PCS's own freeze classifier executes in the PCS root. It is the second of
the exactly two signed freeze-EXECUTION sites of invariant 89, and it is not a
second EVIDENCE WRITER: it installs no record of any peer class.

ACTOR        the PCS, in the PCS root
TRIGGER      [W-B] loss of the peer control endpoint, record-first
             [W-A] an ACCEPTED t-wd-freeze.v1 record inside the bounded service
                   window; on window end without one, NO freeze occurs
SCOPE        computed from the PCS's own handle table, under KV-1..KV-6
             re-evaluated before every _killpg
MEDIATION    none — it is not SIGNAL_GROUP-mediated, because it IS the PCS
EVIDENCE     none. It writes no t-freeze-observation.v1, no
             t-freeze-fallback-observation.v1, and no record of any peer class
JOURNAL      its terminal, its per-group tokens and its freeze_ns are P1-owned
             process-control journal facts

THE PUBLICATION BOUNDARY IS ABSOLUTE. The classifier's journal state is
OPERATIONAL AND AUDIT MATERIAL ONLY. It is never scientific evidence, never a
covariate, never an endpoint, never an input to any peer validity predicate, and
never repairs missing peer evidence. A build in which any of it reaches a peer
artifact, an acceptance predicate, a qualification, a comparison, a Q or C fact
or any published record FAILS (L8, ND-1..ND-3, invariant 89).

THE PCS REMAINS THE SOLE CALLER of fork, posix_spawn, kill, killpg and every
wait-family primitive. Both freeze-execution sites' _killpg executes in the PCS
root and nowhere else, so S-12 is retained unchanged. Two execution SITES are
not two CALLERS.
```

---

## §P1-11. Records, crash cuts, terminals, invalidity

### §P1-11.1 Singleton preflight

Under `SPAWN.lock`, before `c2`, for each record in the order child, group,
middle, spawning:

```text
P0. absent ⇒ nothing to do
P1. present but malformed, meaning the schema value, key set, a value type, an
    enum value, a hexadecimal grammar or a timestamp grammar fails; or it is
    not a regular file; or it has a link count other than 1; or it resolves
    through a symlink
    ⇒ fail-closed: REFUSED with retryable false; unlink nothing; kill nothing;
      release no live process. The contract never guesses at an ambiguous
      singleton record.
P2. present, well-formed, recorded process live by pid and start identity:
    P2a. the same spawning_id and byte-identical to what this attempt would
         install ⇒ adopt the existing record; do not rewrite it; continue the
         attempt at the corresponding step
    P2b. otherwise ⇒ REFUSED with retryable true; unlink nothing; kill nothing
P3. present, well-formed, recorded process not live, meaning /proc absent, or
    state Z with a matching identity, or live with a different start identity,
    which is pid reuse and is treated as not live and never killed
    ⇒ prove that exact state, remove per §P1-11.3, and continue
```

### §P1-11.2 The stuck-holder route

Taken by a later PCS without the lock after
`T_SPAWN_LOCK_ACQUIRE_TIMEOUT_NS` expires, in this order, each step obeying
§P1-11.1's malformed and pid-reuse rules:

```text
s1. the supervisor identity record is present and live-verified ⇒ a live
    supervisor exists; kill nothing; proceed as an ordinary client
s2. SPAWNING_CHILD.json is well-formed, its recorded process is live by pid and
    start identity, and it is older than T_SPAWN_BOOTSTRAP_MAX_AGE_NS ⇒ killpg
    the recorded supervisor_pgid, prove death, remove per §P1-11.3, retry the
    bounded acquisition exactly once
s3. SPAWNING_GROUP.json is well-formed with group_verified true, its group is
    live, and it is older than that bound ⇒ killpg the recorded
    process_group_id, prove death, remove, retry once
s4. SPAWNING_MIDDLE.json is well-formed, its process is live, and it is older
    than that bound ⇒ kill the recorded middle_child_pid only, never killpg,
    after start-identity validation; prove death; remove; retry once
s5. otherwise ⇒ REFUSED with retryable true
```

`s5` is a consequence and never a resolver: it resolves no held lock and no
surviving record, and this contract nowhere describes it as forward progress.

### §P1-11.3 Record removal order

Every death-proved failure route removes records in exactly this order, each
unlink followed by an `fsync` of the parent directory, with `ENOENT` tolerated:

```text
1. SPAWNING_CHILD.json   then fsync of the directory
2. SPAWNING_GROUP.json   then fsync
3. SPAWNING_MIDDLE.json  then fsync
4. SPAWNING.json         then fsync
```

`SPAWNING_CHILD`, `SPAWNING_GROUP` and `SPAWNING_MIDDLE` name processes other
than the PCS and are protected by death-before-unlink. `SPAWNING.json` names the
PCS itself, so removing it can orphan nothing: **every returning terminal
removes it while still holding the lock.** A non-returning state has not
abandoned the attempt and retains it.

### §P1-11.4 PCS loss

```text
On PCS death at any point:
  - the kernel closes every descriptor it held: its lock reference, the
    protocol socket, the journal, and every role-side end;
  - pid_mid and every role are adopted per §P1-4.2 and reaped by that adopter;
  - the supervisor observes channel EOF and has lost all process authority: it
    can create, signal, wait for and reap nothing;
  - the watchdog's getppid() changes, which per §P1-9.2 property 11 means the
    PCS died and is not a supervisor-death signal; the watchdog continues until
    its own update-pipe EOF;
  - the journal's last entry may be ACCEPTED, so an operation may or may not
    have happened: that is the inconclusive case;
  - the four singleton records survive under §P1-11.1, and no record naming a
    possibly-live process is removed without a proof.

Prohibition: a new PCS must never adopt a live generation. It is not the parent
of any surviving process, so it can neither wait for nor safely signal one. A
PCS that starts and finds a journal whose generation is not terminal must
respond GENERATION_NOT_ADOPTABLE, take no action, and exit.

Supervisor continuation on channel EOF:
  1. refuse every admission and every command requiring a role operation;
  2. freeze is unavailable, because EVERY freeze-execution site in this
     contract requires a live PCS — the supervisor's freeze routes of §P1-13.9
     reach every group stop through SIGNAL_GROUP, which is a PCS operation, and
     the PCS's own freeze classifier of §P1-10.7 executes in the PCS root — so no
     live stream has a valid continuation;
  3. close the watchdog update pipe write end; the watchdog writes nothing and
     exits; its adopter reaps it;
  4. route the generation through §P1-11.6.
```

### §P1-11.5 Stage-M terminals

Used by any abandonment at `c5`, `c6` or `c7`, after `c4` returned a pid greater
than zero in a generation whose `P-g` completed successfully.

```text
M0. OWNERSHIP := OWNED; captured := the c6 or c7 start identity if one exists
M1. t0 := the monotonic now ; D := T_SPAWN_IDENTITY_WAIT_TIMEOUT_NS
M2. IDENTITY_OBSERVE(pid_mid)
M3. if OWNED: SIGNAL_ATTEMPT(pid_mid, 15)
M4. loop at T_SUPERVISOR_POLL_INTERVAL_NS:
      a. WAIT_ONE(pid_mid)
           REAPED_POSITIVE     ⇒ leave the loop
           NOT_YET             ⇒ continue
           CONTRADICTED_ECHILD ⇒ leave the loop immediately, because no later
                                 wait can return this pid
           INCONCLUSIVE_OTHER or STRUCTURAL_VIOLATION ⇒ continue
      b. if OWNED and the now is at or past t0 + D/2:
           SIGNAL_ATTEMPT(pid_mid, 9)
      c. if captured is absent and OWNED: IDENTITY_OBSERVE, at most once per
         poll interval
      d. if the now is at or past t0 + D: leave the loop
M5. terminal selection, total, with three pairwise disjoint predicates:
      REAPED                              ⇒ T1
      not REAPED and captured is present  ⇒ T2
      not REAPED and captured is absent   ⇒ B, which does not return

T1  clean up the bootstrap ends; remove all four records in the order of
    §P1-11.3 while holding the lock; release the lock; reply REFUSED with
    retryable true. No record survives; the child is reaped, so no fork-shared
    lock reference survives.
T2  clean up the bootstrap ends; install SPAWNING_MIDDLE.json per §P1-5.1 if it
    is not already durable, with every field an observed value; remove only
    SPAWNING.json; retain pid_mid in memory as an unreaped own child so that a
    later attempt in this process reaps it at §P1-11.1 step P3; release the
    lock; reply REFUSED with retryable true. The surviving record is resolved by
    §P1-11.1 and §P1-11.2.
B   no truthful record is constructible, so nothing is installed and nothing is
    returned. B retains SPAWN.lock, SPAWNING.json, the in-process pid handle and
    the bootstrap ends; installs nothing; emits no refusal, reply, event or
    artifact; and loops at T_SUPERVISOR_POLL_INTERVAL_NS on WAIT_ONE together
    with an ownership-gated SIGKILL and a re-observation. Its only exits are a
    positive reap into T1 and a valid capture into T2.
```

**No route may return, release the lock, remove `SPAWNING.json`, or discard
every durable and in-process handle while the child may remain live and
unreaped.**

**Why the middle cannot become a second supervisor at `c5` through `c7`.**
Execution runs `c1` through `c4`, then `c5`, `c6`, `c7`, then `c8`, and the
stage-1 release byte is written at `c8`. At any abandonment at `c5`, `c6` or
`c7` no `c8` byte was ever written: `rel1` is a fresh pipe and `c8` is its only
writer. The middle is at `m0` and still owns its own inherited `rel1` write end,
so EOF at `m0` is impossible in principle no matter what the PCS closes. It
exits by its own `m0` bound or by the parent's ownership-authorized signal and
reap. It can never reach `m1`, hence never `m2`, `m4`, `m5` or `m7`: no
grandchild is forked and no supervisor identity record is installed. The
fork-shared `SPAWN.lock` reference is what prevents a new PCS from acquiring
until the middle exits.

### §P1-11.6 Invalidity routing

```text
An operation whose control outcome cannot be established, or a generation whose
PCS is gone, is a process fact:
  - it settles through the process-invalidity recovery disposition and the
    unknowable settlement route named in §P1-13.5, with invalidity dominance;
  - it is never a completion, never a capacity fact, never a custody
    disposition, never a spend fact, and never an input to qualification or
    comparison;
  - no resource value is inferred from it and no scientific outcome is produced
    or predicted.
A caller that misreports a truthful reply changes nothing durable: the record
set, the journal, the capacity ledger and the custody dispositions are written
by processes the caller does not control, and the idempotency rules of B1 make
a retry converge on the recorded truth rather than on the caller's account of
it. No route may treat "the caller's own user was misinformed" as a
disposition.
```

### §P1-11.7 Crash and cut matrix

| Cut | Single continuation |
|---|---|
| any failure at `P-cwd` through `P-p` | the named token; no fork, no lock, no record |
| `c1` lock readback shows `FD_CLOEXEC` clear | `LOCK_FD_NOT_CLOEXEC`; no fork; lock released |
| `c4` returns a non-int, a value at most zero, or raises | ownership never established; the pre-fork fail-closed body applies |
| crash between `P-p` and `c4` | no child exists; `SPAWNING.json` names a crashed PCS, so the next attempt's step P3 proves its death by absence and removes it |
| `G-1` hoist postcondition violated, or `G-3` shows a slot still close-on-exec | `os._exit(3)`; nothing written; the PCS's `c13` read sees boot EOF and takes the stage routes of §P1-11.2 |
| `G-6` `execve` fails | `os._exit(3)`, nothing written, nothing unlinked |
| any role failure at `A-1` through `A-13` | `os._exit(3)`, nothing written, nothing unlinked |
| a spawned role's `A-5` finds an unexpected descriptor | refusal; this is a verification failure, not the mechanism of §P1-6.4 |
| caller crash, or it stops reading, or it closes the reply pipe early | the reply write raises on `EPIPE`, which the ignored `SIGPIPE` disposition of `g-5` turns into an exception; it is recorded and changes no record, custody, ownership or terminal decision |
| a competing waiter in the caller reaps the PCS | only the exit status is lost; the pipe reply is authoritative |
| the caller kills the PCS | §P1-11.4 |
| `_recvmsg` raises | the single-statement exit of §P1-8.7; §P1-12.4 names the exposure |
| any ancillary violation | the full vector is parsed, then exactly it is closed; §P1-11.6 |
| an acknowledgement is lost on a descriptor-bearing reply | `FD_DELIVERY_UNCONFIRMED`; no re-send; §P1-11.6 |
| replay of `ACCEPTED`, `COMPLETED` or `ACKED` | the three rows of §P1-8.6; no syscall is ever re-performed |
| supervisor death while the PCS lives | the watchdog sees update-pipe EOF, writes nothing, freezes nothing and exits; **no freeze occurs on this path, because the only freeze executor is the now-dead supervisor**; the PCS holds every live handle in the non-returning reaper state and frees the singleton for no one; §P1-11.1 governs the records at the next attempt; every affected group is settled by the next supervisor takeover through the signed invalid route |
| PCS death | §P1-11.4 |
| watchdog death | the detection of §P1-9.2, then `SPAWN_WATCHDOG` |
| a watchdog that does not exit after its update-pipe EOF | `WATCHDOG_UNREAPED`; no signal; §P1-11.6 |
| a controller or worker is stopped | `AWAIT_STOP` and `REAP_ROLE` observe `(0,0)`; the schedule of §P1-10.5 applies through `SIGNAL_ROLE`; a stopped role holding a fork-shared reference is the residual of §P1-12.4 item 2 |
| `STRUCTURAL_VIOLATION` at any wait site | never death; `CONTRADICTED`; no further signal; no record touched |
| `SHUTDOWN` with a live handle | `HANDLES_LIVE`; nothing released |
| a second launcher runs concurrently | it spawns its own PCS; both contend for `SPAWN.lock` under §P1-11.1 and §P1-11.2; the singleton property is the lock and the records, never a process identity |
| crash between any ordered unlink and its `fsync` | `ENOENT`-tolerant; the order resumes |
| restart before or after the middle's `m0` bound | the records survive; the middle exits at its bound; §P1-11.1 governs |

---

## §P1-12. Guarantees, absences, residuals

### §P1-12.1 Safety, guaranteed and claimed

```text
S1. No false-positive death proof. No live process is ever recorded dead, and
    no record naming a possibly-live process is removed without an object-bound
    proof or an authoritative reap by its own parent.
S2. No capability transfer to any unauthorized actor. No descriptor, handle,
    opcode or journal authority reaches a process outside the PCS and
    supervisor control plane.
S3. No unauthorized decision. No interference is accepted as an Officina
    decision, and no adopter-observed value is consumed by one.
S4. Fail-closed routing. Every perturbed or unestablished control outcome
    settles through §P1-11.6, never as a completion, a capacity fact, a custody
    disposition, a spend fact, an input to qualification or comparison, or
    scientific evidence.
```

### §P1-12.2 Liveness, explicitly not guaranteed

```text
L1. That any generation completes.
L2. That a death proof ever becomes available for a stopped process.
L3. That a sealed channel ever reaches EOF.
L4. That a fail-closed stall ever terminates.
L5. That a same-UID actor is confined, detected or prevented in any way.
```

A3 is a procedural rescope. It is not confinement and not adversarial same-UID
or same-process security, and no rule in this contract strengthens it. Every
liveness loss above is permanently non-citable.

### §P1-12.3 What an adopter or same-UID actor can and cannot do

| It can | Detail |
|---|---|
| become the parent of orphans | the supervisor after `m9`; and after PCS death `pid_mid`, controllers, workers and watchdogs |
| reap them, including by a wildcard wait | its wildcard waits range over everything it has adopted |
| observe each orphan's pid and wait status | the status is an untrusted operating-system fact. It may reflect same-UID interference, including a signal the actor itself delivered. **This contract does not enumerate or bound the values it may take.** It carries no authorized programme meaning and is consumed by no decision, record, journal entry, settlement, capacity accounting, custody disposition, or qualification input |
| delay reaping, or reap promptly | the first prolongs `/proc` state `Z`; the second makes `/proc` absence true sooner. Both are already accepted death proofs |
| stop, kill, or delay any same-UID process, with or without adoption | already true under A3; adoption adds no signalling power |
| **deny proof availability indefinitely** | a stopped process stays alive, shows state `T`, and keeps every open descriptor, so no death proof ever becomes available and a sealed channel it holds never reaches EOF, including the protocol socket and the watchdog update pipe |

| It cannot | Why |
|---|---|
| create a false-positive object-bound death proof for a live process | the predicates are `/proc` absence, or state `Z` with a matching start identity, or live with a different start identity. A live or stopped process with a matching identity satisfies none of them, and absence cannot be fabricated |
| obtain any descriptor or capability | reaping conveys none; capabilities move only over the sealed point-to-point socket or by inheritance the PCS controls |
| participate in the control plane | it holds no channel endpoint, so no opcode is reachable to it; it appears in no journal as an actor; it can issue no request, receive no response and hold no handle |
| turn interference into a valid Officina decision or a scientific or resource outcome | every route it can perturb fails closed into §P1-11.6 |

Kernel power is admitted; Officina authorization is not conferred. Those are
different statements and this contract makes only the second.

### §P1-12.4 Named residuals

1. **The unreaped-zombie residual.** A `T2` termination leaves one zombie: one
   pid slot, no descriptors and no lock reference, in `/proc` state `Z` with a
   matching start identity, which is itself an accepted death proof for any
   other process. It is reaped at a later attempt in the same PCS or by its
   adopter after the PCS exits. It is bounded by the PCS's own lifetime.
2. **`B`-state non-termination.** With ownership sound, `SIGKILL` or the
   middle's own `m0` bound ordinarily produces a positive reap. Non-termination
   requires a deliberately stopped child together with a persistent signal
   fault.
3. **The receive-path exposure.** From the instant the kernel may have installed
   descriptors inside `_recvmsg` until the process actually exits, those
   descriptors are present in the supervisor's table, and same-process hooks,
   finalizers or threads that the host installed may run and reach them. This is
   a transient capability exposure and not a resource fact. Its length is not
   under this contract's control; it is terminated with certainty by the
   kernel's closure of the descriptor table at exit. It lies inside A3.

All three are permanently non-citable.

---

## §P1-13. The typed peer interface

Two peer contracts are separately accepted and currently in force. They own
functionality **outside** the P1 boundary. This section states the complete
interface as a total ownership matrix. **No historical P1 predecessor is opened
for any of it.**

### §P1-13.0 Logical layers, process residence, and who owns what

The same operating-system process runs code belonging to more than one logical
contract. Every ownership statement in this document is about a **logical
layer**, never about which process happens to execute the instruction.

**The three logical layers.**

| Layer | Owns the decision for | Code roots | Contract that owns its schemas and semantics |
|---|---|---|---|
| **P1 control-plane layer** | process creation and destruction, all numeric process authority, handle allocation, the nine opcodes, the process-control journal, descriptor custody and transfer, the four singleton spawn records | `scripts/officina_process_control_bootstrap.py`; `scripts/officina_role_bootstrap.py` steps `A-1` through `A-12`; the P1 client and the four role entries inside `src/philosophia/officina/generic_harness.py` | **this document** |
| **generic-harness peer layer** | spawn intent, process claims and leases, watchdog lease tables and freeze-evidence acceptance, capacity, operations, settlement, quarantine, promotion, archival | the harness code inside `src/philosophia/officina/generic_harness.py` other than the P1 client and role entries | `successor/OFFICINA_GENERIC_HARNESS_CONTRACT_V2_3_1_CORRECTION.md` and its accepted chain |
| **batch-settlement peer layer** | batch settlement claims, the batch prefix automaton, head and cache authority | the settlement code reached from the harness layer | `successor/OFFICINA_BATCH_SETTLEMENT_CORE_AMENDMENT_V1_1_1_CORRECTION.md` |

**The five process kinds, and which layers execute inside each.**

| Process | Created by | Layers executing in it | Notes |
|---|---|---|---|
| PCS bootstrap process | the caller, per §P1-7.1 | **P1 layer only** | executes no peer-layer code and holds no peer-layer state; it reads exactly one peer-owned record, per §P1-13.2 row 1 |
| middle process | PCS `c4` fork | **P1 layer only** | executes `m0` through `m9` and nothing else |
| supervisor role process | PCS, then middle `m7`, then `G-6` `execve` | **P1 client layer and generic-harness peer layer, co-resident**; the batch-settlement layer is reached from the harness layer | this is the only process in which two layers are co-resident, and it is the reason this subsection exists |
| watchdog role process | PCS `SPAWN_WATCHDOG` | **P1 role-entry layer, plus exactly one read-only peer operation** | the watchdog runs the peer layer's supervisor-channel-liveness function. Within it the watchdog performs EXACTLY ONE peer-layer operation on a peer-owned object: the READ-ONLY verification of the supervisor identity record of §P1-13.2 row 3, required by §P1-9.2 property 8 and by invariant 87, and never by any parent relationship. It emits NO peer-owned record, owns NO peer decision, and performs no signal, no freeze, no quiescence proof, no evidence write and no settlement on any path. **"Role-entry only" means no write, no decision and no execution. It does not mean no read.** `[W-A]` It additionally holds one single-opcode, target-free freeze-request socket at slot 6 over which it may emit exactly one constant `t-wd-freeze.v1` record; that record is a P1 transport frame, not a peer-owned record, and is never evidence. `[W-B]` It holds no socket. |
| controller or worker role process | PCS `SPAWN_ROLE` | **P1 role bootstrap through `A-12` only**; after the self-stop the client's target program runs and belongs to neither layer | the target program is client-supplied and is trusted by nothing |

**The ownership rules, stated so no reader can infer authority from residence.**

```text
R-L1. A write performed by the supervisor process is NOT automatically a
      P1-layer write. The layer that owns the DECISION owns the write. Process
      residence is evidence of nothing.
R-L2. A peer-owned schema may be read, or physically emitted, by a P1-created
      role process. Every such case appears in §P1-13.2 as a row whose
      "executing process" differs from its "logical writer", and no such case
      exists outside that table.
R-L3. No durable artifact has two logical writers. Process residence never
      decides schema authority, and two layers never independently install the
      same no-replace record.
R-L4. Co-resident call direction is one-way: the generic-harness peer layer
      calls INTO the P1 layer, through the nine opcodes of §P1-8.3 and through
      nothing else. The P1 layer never calls into a peer layer, never inspects
      peer state, never opens a peer artifact except the one row 1 names, and
      never decides a peer disposition. P1 returns typed results; the peer
      layer decides what they mean.
R-L5. Where two different processes may execute the same logical writer's
      function, the record itself MUST carry a mandatory discriminator field
      whose value names the executing process, and the artifact's row in
      §P1-13.2 MUST name that field. A logical writer with two possible
      executing processes and no discriminator is a defect, not a design.
R-L6. "P1 reads X" means the P1 layer opens X. "P1 provides Y" means a P1
      opcode returns Y as a typed result. Neither phrase is ever used of a
      peer-layer action performed in a P1-created process.
```

### §P1-13.1 The peer contracts, by path and digest

```text
generic harness, accepted:
  successor/OFFICINA_GENERIC_HARNESS_CONTRACT_V2_3_1_CORRECTION.md
  sha256 724d633a55668013b78058eed1c76e12e9bbaf487f71ea94b7a4568ea1ced8a0
  signature: successor/OFFICINA_GENERIC_HARNESS_SIGNATURE.md
  sha256 8c47da352ef5954406964647a32e97939c404806bdf9b3d3ff5bc70866e6369a

batch settlement, accepted:
  successor/OFFICINA_BATCH_SETTLEMENT_CORE_AMENDMENT_V1_1_1_CORRECTION.md
  sha256 b5a1523290b6b8417a7b3288329cc4a4e5ff80214c8f28e6ea1ae51a450a94c9
```

### §P1-13.2 The four-artifact ownership matrix

These four durable artifacts sit on the interface: each is touched by at least
one P1-layer path and is owned by at least one contract. Each row below is
total — path rule, schema value, key set, logical schema owner, logical writer,
executing process, discriminator, readers, exact fields P1 reads, durability and
ordering, deletion authority, and the P1 invariant. **No row delegates a value
to another document.**

#### Row 1 — spawn intent

```text
path rule            successor/officina/runtime_control/T_SUPERVISOR/
                       CHILDREN/<spawn_intent_id>.json
schema value         philosophia.officina.t-spawn-intent.v1
key set, exactly     schema, scientific_outcome, supervisor_generation_sha256,
                     spawn_intent_id, role, process_sequence, argv_template,
                     argv_template_sha256, created_utc
                       role is one of CONTROLLER, WORKER — WATCHDOG is not a
                       member of this enum, because a watchdog is created by
                       SPAWN_WATCHDOG and has no argv template of this kind
                       argv_template is a nonempty list of str containing both
                       placeholders
logical schema owner generic-harness peer layer
logical writer       generic-harness peer layer
executing process    supervisor role process
discriminator        none required: one logical writer, one executing process
readers              (a) the PCS, P1 layer, at SPAWN_ROLE;
                     (b) the generic-harness peer layer, for its own reducer
fields P1 reads      spawn_intent_id, role, argv_template,
                     argv_template_sha256, supervisor_generation_sha256
durability/ordering  atomic no-replace under T_RUNTIME.lock, made durable by
                     the peer layer STRICTLY BEFORE the P1 client issues
                     SPAWN_ROLE naming it
deletion authority   generic-harness peer layer, after the process terminal and
                     the archival commit. P1 removes it never.
P1 invariant         the PCS rebuilds §P1-7.4's argv indices 19 through 18+N
                     from argv_template alone, and refuses with REQUEST_MALFORMED
                     unless the record is well-formed, its generation matches,
                     and argv_template_sha256 equals the digest of the template
                     it read. NO TARGET ARGV EVER CROSSES THE PROTOCOL WIRE:
                     SPAWN_ROLE carries only role and two 64-hex identifiers.
P1 writes            nothing. P1 creates no record of this schema and modifies
                     no field of one.
```

#### Row 2 — process claim — **BLOCKED, `AUTHOR_CELL_P1_PROCESS_CLAIM_IDENTITY_FIELDS`**

```text
path rule            successor/officina/runtime/T_PROCESS_CLAIMS/
                       <process_id>.json
schema value         philosophia.officina.t-process-claim.v1
key set, exactly     schema, scientific_outcome, activation_record_sha256,
                     process_id, process_sequence, controller_pid,
                     controller_start_identity, process_group_id, argv,
                     behavior_source_sha256, config_sha256, stack_sha256,
                     numerical_mode_sha256, device_identity, device_units,
                     created_utc, clock_kind, boot_identity, start_reading_ns,
                     immutable_control_sha256
logical schema owner the T activation protocol, consumed by the
                     generic-harness peer layer
logical writer       generic-harness peer layer
executing process    supervisor role process
discriminator        none required: one logical writer, one executing process
readers              the generic-harness peer layer; and the freeze-evidence
                     acceptance predicate, which compares a witness's pgid and
                     start identity against this record's process_group_id and
                     controller_start_identity
fields P1 reads      none. The P1 layer opens this record on no path.
durability/ordering  written only after AWAIT_STOP returns STOPPED
deletion authority   generic-harness peer layer
P1 provides          outcome in {STOPPED, EXITED, TIMEOUT}; start_identity;
                     pgid_is_leader in {0,1}
```

**The conflict, stated exactly.** Two of this record's mandatory keys cannot be
obtained by the layer that must write it:

```text
controller_start_identity  <- AWAIT_STOP's start_identity            AVAILABLE
argv                       <- argv_template plus the fixed control
                              descriptor numbers 3 and 4              AVAILABLE
controller_pid             <- no source                            UNAVAILABLE
process_group_id           <- no source                            UNAVAILABLE
```

The nine opcodes of §P1-8.3 return, in total: `handle_id` (`SPAWN_ROLE`,
`SPAWN_WATCHDOG`); `outcome`, `start_identity`, `pgid_is_leader` (`AWAIT_STOP`);
a `result` token (`SIGNAL_ROLE`, `SIGNAL_GROUP`); one of the six tokens of
§P1-10.2 (`REAP_ROLE`); nothing (`RELEASE_HANDLE`, `SHUTDOWN`);
`pcs_uptime_ticks` (`PING`). **None is a pid and none is a process-group
number.** `pgid_is_leader` is a predicate over `{0,1}`, so it decides whether
the group id equals the process id but names neither. The signed selection
states that the supervisor "receives opaque handles only" and "cannot express a
PID", and the P1 binding derives exactly that from `t-pcs.v1` having no PID
field. The P1 layer holds both values and does not emit them; the peer layer
must record both and cannot obtain them.

**This is a conflict between two separately signed contracts, not an
implementation gap.** The chain does not resolve it: no document from the P1
binding through the final pre-review repair addresses these two keys, and the
one sentence that touches the subject asserts the claim write still records
"the same fact, obtained by the same syscall in a clean process" without
reaching the two identity keys.

**Two coherent repairs exist, with different costs. This document selects
neither and invents no value.**

```text
OPTION A — extend the P1 response set with a read-only identity tuple.
  AWAIT_STOP additionally returns the target's pid and process-group number as
  data. The peer layer then writes the claim with its present key set intact.
  Cost: t-pcs.v1 acquires PID-valued response fields. The binding's derivation
  "t-pcs.v1 has no PID field, so the supervisor cannot express a PID" no longer
  holds as written and must be re-grounded on the weaker and separately
  arguable premise that receiving a number as data is not expressing it as an
  operation target. Every opcode's REQUEST side must still reject a PID, and
  that must be proved rather than assumed.

OPTION B — relocate the identity keys out of the supervisor's reach.
  The two keys are supplied to the peer layer by some means that does not put a
  pid in the supervisor, or the claim schema is amended so the pair travels
  by a P1 handle plus a PCS-side binding.
  Cost: t-process-claim.v1 is a signed schema of the T activation protocol and
  is read by the freeze-evidence acceptance predicate, which compares a
  witness's pgid against this record's process_group_id. Amending it reopens
  that predicate and every route that consumes it.

AUTHOR CELL: AUTHOR_CELL_P1_PROCESS_CLAIM_IDENTITY_FIELDS
  The bounded choice is exactly: which of Option A or Option B is taken, and
  under Option A whether a PID-valued RESPONSE field is compatible with the
  signed sentence "It cannot express a PID". No other question is open, and no
  other part of this composite depends on the answer.
```

Until that cell is signed, a conforming implementation cannot write a valid
process claim, and this document states that plainly rather than filling the
two keys with an invented source.

#### Row 3 — supervisor identity

```text
path rule            successor/officina/runtime_control/T_SUPERVISOR/
                       SUPERVISOR_IDENTITY.json
schema value         philosophia.officina.t-supervisor-identity.v1
key set, exactly     schema, scientific_outcome, activation_record_sha256,
                     supervisor_pid, supervisor_start_identity, boot_identity,
                     request_fifo, created_utc
                     supervisor_generation_sha256 is the SHA-256 of this
                     record's canonical bytes and is not itself a key
logical schema owner generic-harness peer layer
logical writer       generic-harness peer layer
executing process    supervisor role process, holding SPAWN.lock at slot 3
                     — this is an R-L2 case: a peer-owned record physically
                     emitted by a P1-created role
discriminator        none required: one logical writer, one executing process
readers              (a) the PCS, P1 layer, at c17, which polls for its
                         live-verified presence;
                     (b) the watchdog role process, per §P1-9.2 property 8,
                         which verifies the supervisor's identity against it
                         and never by any parent relationship;
                     (c) any freeze-evidence writer, which re-reads it and
                         refuses to write on generation mismatch;
                     (d) the generic-harness peer layer's takeover phase
fields P1 reads      supervisor_pid and supervisor_start_identity, for the
                     liveness predicate of §P1-4.5; and the record's canonical
                     digest, as the generation identifier
durability/ordering  atomic no-replace within a generation, installed while
                     SPAWN.lock is held. The P1 supervisor role closes its lock
                     descriptor at slot 3 only after this record is
                     live-verified, per §P1-9.3.
deletion authority   generic-harness peer layer, at takeover phase 1. P1
                     removes it never, on no route, including every terminal of
                     §P1-11.5.
P1 invariant         c17 polls for a live-verified record bounded by
                     T_SPAWN_IDENTITY_WAIT_TIMEOUT_NS and treats absence at the
                     bound as a stage failure, never as a death proof. P1 reads
                     this record and writes no field of it.
```

#### Row 4 — freeze observation

```text
path rule            successor/officina/runtime_control/T_SUPERVISOR/
                       WATCHDOG/FREEZE/<witness_id>.json
                     witness_id = SHA-256 of the canonical object
                       { supervisor_generation_sha256, process_id, table_seq }
schema value         philosophia.officina.t-freeze-observation.v1
key set, exactly     schema, scientific_outcome, supervisor_generation_sha256,
                     witness_id, process_id, pgid, start_identity, deadline_ns,
                     freeze_ns_or_null, quiescence, overrun_ns_or_null, killer,
                     unresolved_member_count, table_seq, created_utc
                       quiescence is one of PROVED, UNKNOWN
                       killer is one of WATCHDOG, SUPERVISOR
logical schema owner generic-harness peer layer
logical writer       generic-harness peer layer, freeze-witness function —
                     ONE logical writer
executing process    the SUPERVISOR ROLE PROCESS ONLY, on exactly the two
                     routes enumerated in §P1-13.9 and on no other path:
                       ROUTE-D  ordinary lease-deadline entry, taken when the
                                supervisor's own clock reaches a live lease
                                deadline and the watchdog is NOT declared dead
                       ROUTE-W  dead-watchdog recovery entry, taken when the
                                watchdog has been declared dead by ack absence
                                past T_WATCHDOG_ACK_ABSENCE_TIMEOUT_NS
                     Both routes are the same procedure, with the same actor,
                     the same SIGNAL_GROUP mediation, the same evidence class,
                     the same namespace, the same writer and the same killer
                     value. THIS IS ONE EXECUTING PROCESS, NOT TWO. The watchdog
                     role process executes no write of this class on any path.
                     The peer amendment's ABSENT fallback is a DIFFERENT
                     artifact, of a different schema, in a different namespace,
                     and is NOT an executing-process branch of this row.
discriminator        the mandatory in-record key `killer`, RETAINED from the
                     peer schema, whose value on every path reachable under this
                     contract is SUPERVISOR, because this row now has EXACTLY
                     ONE executing process. An observation carrying
                     killer == WATCHDOG has no admissible writer, fails the peer
                     acceptance predicate's conjunct 8, is permanently
                     non-evidence, and routes to the fallback with
                     rejection_conjunct = 8. The enum is NOT narrowed: both
                     values are retained so that a legacy, stale or forged object
                     is REJECTED rather than unparseable. This row is no longer
                     an R-L5 two-executing-process case. R-L5 itself is unchanged
                     and is instantiated by no row of this document.
readers              the generic-harness peer layer's acceptance predicate,
                     under T_RUNTIME.lock
fields P1 reads      none. The P1 layer opens this record on no path.
durability/ordering  atomic no-replace. The writer re-reads the supervisor
                     identity record of row 3 and refuses to write on
                     generation mismatch, then writes, then emits its pipe
                     event. A no-replace collision means an identical
                     (generation, process_id, table_seq) witness is already
                     durable: the writer emits the event and writes nothing
                     further.
deletion authority   generic-harness peer layer, after the settlement's
                     archival commit. P1 removes it never.
P1 invariant         [W-B] P1 provides the watchdog role process and its TWO
                     SEALED PIPES — the update read end at slot 3 and the ack
                     write end at slot 4 — for the supervisor-channel-liveness
                     function ONLY, and provides NO input to this record. Slot 6
                     is not used and is explicitly closed by a file action; the
                     watchdog holds no socket.
                     [W-A] P1 provides the watchdog role process and its THREE
                     SEALED ENDPOINTS — the update-pipe READ end at slot 3, the
                     ack-pipe WRITE end at slot 4, and the FREEZE-REQUEST SOCKET
                     at slot 6, one end of an AF_UNIX/SOCK_SEQPACKET socketpair
                     whose other end the PCS retains with FD_CLOEXEC set — for
                     the supervisor-channel-liveness function and the
                     single-opcode freeze request ONLY, and provides NO input to
                     this record. The slot-6 request carries one constant
                     t-wd-freeze.v1 record naming no target; it can reach no
                     other operation; it is a P1 transport frame, not a
                     peer-owned record, and no field of it appears in this
                     artifact.
                     BOTH VARIANTS, unchanged: on both executing routes P1
                     provides the SIGNAL_GROUP mediation without which the
                     supervisor could not stop a group at all. P1 decides nothing
                     about the content, the acceptance, or the consumption of
                     this record, and writes no field of it.
```

**Why one executing process on two routes does not break single-writer or C1.**
There is exactly **one** logical writer, the peer layer's freeze-witness
function, and under the amended C1 exactly **one** executing process: the
supervisor role process. It is entered on the two routes of §P1-13.9, which are
two TRIGGERS of one procedure and not two writers: same actor, same mediation,
same schema, same namespace, same `killer` value, same acceptance predicate. No
reader must infer authority from residence and no two writers ever race for the
same object, because there is only one. The mandatory `killer` key is retained
from the peer schema and carries `SUPERVISOR` on every reachable path. C1 is
**amended, not preserved**: the watchdog is no longer the freezer and no longer
the witness of record, and that reassignment is carried by
`P1_WATCHDOG_FREEZER_ROLE_REASSIGNMENT_V1`, which does not revoke, re-run or
reopen the signed selection token. Both routes require `SIGNAL_GROUP`, because
the supervisor holds no process authority of its own, so every freeze it performs
is PCS-mediated exactly like every other group stop. **The PCS's own freeze
classifier of §P1-10.7 is a separate, signed freeze-EXECUTION site**: it runs in
the PCS root, is not `SIGNAL_GROUP`-mediated, targets only the scope computed
from the PCS's own handle table, writes **no record of this or any peer class**,
and its journal terminal is a P1-owned fact that is never freeze evidence
(§P1-12.2 `L8`, `ND-1`..`ND-3`).

**What P1 replaced in that same signed route.** The dead-watchdog route
historically ended by having the supervisor **fork a new watchdog**. Under P1
that clause and only that clause is replaced: replacement is `SPAWN_WATCHDOG`,
uniform with the first watchdog, per §P1-8.3. The freeze-and-observe half of the
route is retained exactly, including the `SUPERVISOR` discriminator value.

**Two adjacent peer artifacts, named so their absence from this table is not
read as an omission.** The peer layer also owns a **freeze fallback** record and
a **replacement-freeze** record, written by the peer layer executing in the
supervisor process, in namespaces the watchdog has no path to and never writes.
Neither is read or written by any P1-layer path, neither is a P1 artifact, and
both are governed entirely by the peer contracts of §P1-13.1. They appear here
only to make explicit that the supervisor's freeze-side writes are not all of
one schema, so that no implementer collapses them.

### §P1-13.3 What P1 provides to the peer side

| P1 output | Consumer on the peer side | Exact content | Invariant P1 guarantees |
|---|---|---|---|
| `AWAIT_STOP` result | the peer layer's claim route, subject to the blocked cell of §P1-13.2 row 2 | `outcome` in `{STOPPED, EXITED, TIMEOUT}`; `start_identity`; `pgid_is_leader` in `{0,1}` | `STOPPED` is returned only when the PCS's own bounded `waitpid(pid, WNOHANG\|WUNTRACED)` on its own direct child reported a stop; the `start_identity` is the value `/proc` reported for that same pid under §P1-10.3 |
| the three descriptors of a `SPAWN_ROLE` reply | the peer layer's control and status channels to that role | control request write end, control reply read end, status read end | each is a pipe end whose peer end is held by exactly that role at slots 3, 4 and 6, and by no other process |
| the two descriptors of a `SPAWN_WATCHDOG` reply | the peer layer's watchdog channels | update write end, ack read end | each is a pipe end whose peer end is held by exactly that watchdog at slots 3 and 4, and by no other process |
| `REAP_ROLE` result | the peer layer's death-dependent routes | one of the six tokens of §P1-10.2 | only `REAPED_POSITIVE` is a death proof, and it is emitted only when the PCS's own targeted wait returned that pid |
| `SIGNAL_GROUP` mediation | the peer layer's freeze routes, including the supervisor-executed branch of §P1-13.2 row 4 | a `result` in `{SENT, GONE, DENIED, STRUCTURAL_VIOLATION}` | issued only against a kernel-verified group, and refused for a `WATCHDOG` handle at every state |
| the four singleton records of §P1-5.1 | the peer layer's takeover and preflight routes | the exact key sets of §P1-5.1 with the meanings of §P1-5.2 | installed atomically with no replacement, removed only in the order of §P1-11.3, and never removed while naming a possibly-live process without a proof |

### §P1-13.4 The settlement interface used at shutdown

Step `S-1` of §P1-9.4 drains and settles through the peer layers' settlement
rules. P1's obligation at that boundary is exactly this and nothing more: it
stops admitting before the drain begins; it makes no capacity, custody or
settlement decision itself; and it supplies only death proofs, descriptor
bundles and the mediation of §P1-13.3.

### §P1-13.5 The invalidity disposition used by §P1-11.6

The process-invalidity recovery disposition and the unknowable settlement route
are owned by the peer layers of §P1-13.1. P1's obligation is exactly this: every
control outcome it cannot establish is handed to that disposition, with
invalidity dominant over any other classification, and P1 emits no competing
classification of its own.

### §P1-13.6 The closed single-writer invariant

```text
SW-1. Every durable artifact visible at this interface has EXACTLY ONE logical
      schema owner and EXACTLY ONE authorized logical writer, even when reader
      and writer code share an operating-system process.
SW-2. Where one logical writer has more than one possible executing process,
      the record carries a mandatory discriminator key naming which process
      executed it, and §P1-13.2's row for that artifact names the key. **No
      artifact in this document is in that class.** Row 4 retains its
      peer-schema `killer` key, but it has exactly one executing process — the
      supervisor role process, entered on the two routes of §P1-13.9 — so that
      key is a carried schema field and not a live discriminator. Two ROUTES
      into one procedure are not two executing processes.
SW-3. Two layers never independently install the same no-replace record. For
      each of the four rows, the install site is exactly one function in exactly
      one root, per §P1-13.7.
SW-4. No conforming implementation may derive write authority from the identity
      of the executing process, from a module name, from a file path, or from
      the fact that a function is reachable from a given entry point. Authority
      comes only from §P1-13.2.
SW-5. A durable artifact that this document neither reads nor writes on any P1
      path, and that no P1 opcode's result is consumed to produce, is outside
      this interface and is governed solely by the peer contracts.
```

### §P1-13.7 The implementation surface for the interface

Every interface operation is assigned to exactly one root and one function, so
that no two layers can install the same no-replace record.

| Operation | Root | Layer | Install or read |
|---|---|---|---|
| write the spawn-intent record | `src/philosophia/officina/generic_harness.py`, the peer layer's intent-install function | peer | install, no-replace, under `T_RUNTIME.lock` |
| read and validate the spawn-intent record, rebuild argv | `scripts/officina_process_control_bootstrap.py`, the `SPAWN_ROLE` handler | P1 | read only |
| write the process claim | `src/philosophia/officina/generic_harness.py`, the peer layer's claim-install function | peer | install — **blocked by §P1-13.2 row 2 until the author cell is signed** |
| install the supervisor identity record | `src/philosophia/officina/generic_harness.py`, the peer layer's identity-install function, executing in the supervisor role while `SPAWN.lock` is held at slot 3 | peer | install, no-replace |
| poll and live-verify the supervisor identity record at `c17` | `scripts/officina_process_control_bootstrap.py`, the `c17` step | P1 | read only |
| read the supervisor identity record in the watchdog | `src/philosophia/officina/generic_harness.py`, the watchdog role entry | peer, executing in a P1-created role | read only |
| write a freeze observation | `src/philosophia/officina/generic_harness.py`, **one** freeze-witness function, called from the supervisor role process only, on the two routes of §P1-13.9 (`ROUTE-D` ordinary lease deadline, `ROUTE-W` dead-watchdog recovery) and from nowhere else, setting `killer` to the constant `SUPERVISOR` | peer | install, no-replace |
| every group stop the PEER freeze routes need | `scripts/officina_process_control_bootstrap.py`, the `SIGNAL_GROUP` handler | P1 | mediation only |
| every group stop the PCS's own freeze classifier performs | `scripts/officina_process_control_bootstrap.py`, the freeze classifier of §P1-10.7 | P1 | EXECUTION; installs no record of any class |

**No P1 root contains an install site for any of the four artifacts.** The PCS
root opens exactly two peer-owned artifacts, both read-only: the spawn-intent
record and the supervisor identity record.

### §P1-13.8 Declared out of scope for P1

The following are owned entirely by the peer layers, are **not** read, written
or produced by any P1 path, and no P1 opcode result is consumed to construct
them: the client control journal and its reducer; lease-table arithmetic; the
capacity ledger and its arithmetic; settlement, quarantine and promotion
decisions; the batch prefix automaton; head and cache authority; inline meter
evidence; archival ordering; the signed event set and its semantics; the
freeze-evidence acceptance predicate; the freeze fallback and replacement-freeze
records; and every spend, qualification and comparison rule.

**This list excludes only peer-internal state that no P1 path consumes or
produces.** It does **not** exclude, and must never be read as excluding, any of
the four artifacts of §P1-13.2: the spawn-intent record, which the PCS reads;
the process-claim record, which consumes `AWAIT_STOP`'s result; the supervisor
identity record, which `c17` and the watchdog read; or the freeze-observation
record, which the **supervisor role process** — a P1-created role — physically
emits on the two routes of §P1-13.9, and which both routes reach only through
`SIGNAL_GROUP`. The PCS's own freeze classifier emits no record of this or of any
peer class, and the peer amendment's freeze-fallback record remains outside this
table entirely, as §P1-13.2's adjacent-artifacts paragraph already states. A conflict between this list and a
peer contract is a peer matter and not a P1 matter; a conflict between this list
and §P1-13.2 is a defect in this document.

### §P1-13.9 The two freeze routes — total, explicit, and one writer

**This subsection exists because the reassignment of the freezer role to the
supervisor necessarily makes the ordinary lease deadline a supervisor entry.
Naming only the dead-watchdog route, as the withdrawn v2.2 packet did, left an
unaccounted writer route that both independent review lines rejected. The routes
are named here in full.**

```text
ROUTE-D  ORDINARY LEASE-DEADLINE ENTRY
  trigger      under T_RUNTIME.lock, the SUPERVISOR's own clock shows
               now_ns >= deadline_ns for a live lease row, and the watchdog is
               NOT declared dead
  actor        the supervisor role process
  precondition the mandatory ack drain: drain the ack pipe nonblocking, re-read
               the durable lease table, and if a strictly greater table_seq is
               durable AND acked, re-evaluate against the newest acked row and do
               not freeze against the superseded deadline
  mediation    every group stop through SIGNAL_GROUP
  killer       SUPERVISOR
  evidence     one t-freeze-observation.v1, supervisor-written, per §P1-13.2 row 4

ROUTE-W  DEAD-WATCHDOG RECOVERY ENTRY
  trigger      under T_RUNTIME.lock, the ack pipe has been drained and no ack for
               that table_seq has arrived within
               T_WATCHDOG_ACK_ABSENCE_TIMEOUT_NS — the watchdog is declared dead
               — and one or more groups are live
  actor        the supervisor role process
  precondition none beyond the declaration; the drain is vacuous because there is
               no live acknowledger
  mediation    every group stop through SIGNAL_GROUP
  killer       SUPERVISOR
  evidence     one t-freeze-observation.v1 per affected group, supervisor-written
  after        refuse admissions, obtain a replacement watchdog by SPAWN_WATCHDOG
               uniform with the first, await its acknowledgement, then settle
               every overdue lease. The overdue / non-overdue split is total: a
               group frozen SOLELY for watchdog replacement, whose deadline has
               NOT been reached, takes the swap-only carve-out and NO witness is
               written for it.

THESE TWO ROUTES ARE EXHAUSTIVE. There is no third entry and no other process
enters on any path.

THEY ARE ONE WRITER, NOT TWO. Same actor, same mediation, same evidence class,
same namespace, same schema, same acceptance predicate, same killer value. They
differ only in trigger and in what follows the freeze. A reader must not count
them as two executing processes (§P1-13.6 SW-2) and must not treat ROUTE-D as a
fallback from a normal watchdog route: THERE IS NO WATCHDOG ROUTE.

TIMING, STATED HONESTLY. No claim is made that an ordinary scheduled userspace
process physically executes at or before a monotonic deadline under every host
schedule, cgroup throttle or runnable-queue delay. What is guaranteed is that
the SUPERVISOR executes the sequence AS SOON AS IT IS SCHEDULED AFTER the
deadline is observed, records the conservative proved-freeze instant itself, and
never synthesizes a timestamp it did not sample. overrun_ns is strictly positive
by construction; there is no zero-overrun branch and no tolerance constant. Every
positive overrun routes to the signed invalid/recovery destinations with full
§4c charging. The supervisor may not defer the sequence, batch it, or let a
deadline pass unserved.

WHAT P1 REPLACED IN THE SIGNED ROUTE, restated. The historical dead-watchdog
route ended by having the supervisor FORK a new watchdog. Under P1 that clause
and only that clause is replaced: replacement is SPAWN_WATCHDOG, uniform with the
first watchdog, per §P1-8.3.
```

---

## §P1-14. The verifier

### §P1-14.0 The region scheme in operative form

This subsection restates the region scheme so that the operative rule is
covered by `H_BODY` and not only by the whole-file digest. It contains no
literal sentinel line, so nothing here can collide with a real delimiter.

```text
fragments:
  FRAG_OPEN   := the four bytes   0x3C 0x21 0x2D 0x2D
  FRAG_SP     := the one byte     0x20
  FRAG_TAG    := the eleven bytes "OFFICINA" 0x2D "P1"
  FRAG_DASH   := the one byte     0x2D
  FRAG_CLOSE  := the three bytes  0x2D 0x2D 0x3E

SENTINEL(region, edge) :=
    FRAG_OPEN + FRAG_SP + FRAG_TAG + FRAG_DASH + region + FRAG_DASH + edge
              + FRAG_SP + FRAG_CLOSE
  region in { "BODY", "GUARDDATA", "PROVENANCE" }
  edge   in { "BEGIN", "END" }

A line is a sentinel if and only if the whole line, after stripping a trailing
0x0A and with no other leading or trailing bytes, equals a constructed value.

EXTRACT fails closed unless every one of the six constructed values occurs on
exactly one line — a count of zero and a count above one both fail — and unless
the six indices satisfy
    b_BODY < e_BODY < b_GUARDDATA < e_GUARDDATA < b_PROVENANCE < e_PROVENANCE.
REGION(R) is the concatenation of the lines strictly between b_R and e_R, each
including its 0x0A.

H_BODY      := SHA-256( REGION(BODY) )
H_GUARDDATA := SHA-256( REGION(GUARDDATA) )
H_NORMATIVE := SHA-256( REGION(BODY) || REGION(GUARDDATA) )
H_FILE      := SHA-256( the whole file )
```

Region authority: `BODY` is the normative contract; `GUARDDATA` is normative
verifier data whose bytes change verifier pass and fail behaviour; `PROVENANCE`
is non-normative and is read for behaviour by nothing. The preamble above the
body region is normative and is covered by `H_FILE` through guard `G-7`.

### §P1-14.1 The guard target

**The one-file rule binds the BODY AND WORDING guards only.** The guard rules
`G-1` through `G-9`, and the authoring discipline `AD-1`, read exactly one file,
this one, and within it exactly the `BODY` region defined by the region scheme
at the head of this file, matched against the pattern data of §P1-17. They read
no other file, ever. There is no allowlist, no exclusion list, no supersession
inference, and no adjective for a verifier to interpret. Historical documents
are categorically outside their domain because they are never opened.

**`G-10` reads the same single file** — it searches this body region for the
`VARIANT_MARKER` patterns of §P1-17 — and is therefore also inside the one-file
rule.

**`G-11` IS THE ONE EXPLICIT EXCEPTION, AND ITS INPUT SET IS CLOSED.** The
joint-install guard cannot be a one-file guard, because what it checks is
precisely that a SET of files was installed together. Its input set is
enumerated exhaustively at §P1-14.4 `G-11` as the seven member classes
`M1`..`M7`, is closed by construction, and contains no wildcard, no directory
scan and no adjective. `G-11` reads those bytes ONLY to hash them and never
interprets any of them as a rule, so the categorical exclusion of historical
documents from BEHAVIOUR is not weakened: **verifying a digest is not opening a
document for behaviour.**

### §P1-14.2 Normalization

```text
NORMALIZE(bytes) :=
  decode as UTF-8; apply Unicode NFC; map every ASCII uppercase letter to
  lowercase; delete every occurrence of the characters asterisk, underscore and
  backtick, and every occurrence of the two-byte sequences that open and close
  an HTML comment; replace every maximal run of whitespace, meaning space, tab,
  newline and carriage return, with a single space; strip leading and trailing
  spaces.
```

### §P1-14.3 The guard rules

Each rule holds a closed list of forbidden normalized patterns and a paired
permitted form. The pattern strings are **normative verifier data** and live in
the `GUARDDATA` region, which the extraction algorithm delimits separately and
which is never itself a substring target.

```text
G-1  class ADOPTION. Forbids asserting that an orphan is re-parented to, or
     reaped by, the init process or process id 1 without the
     nearest-living-ancestor-subreaper qualification of §P1-4.2.
       ⇒ "guard G-1: absolute init adoption claim"
G-2  class ANCESTOR_WAIT_SET. Forbids asserting an exclusive wait-set for the
     caller or any ancestor without the dynamically-adopted-orphan
     qualification of §P1-4.3.
       ⇒ "guard G-2: exclusive ancestor wait-set"
G-3  class STATUS_SET. Forbids enumerating, bounding or otherwise closing the
     set of wait-status values an adopter may observe.
       ⇒ "guard G-3: closed adopter status set"
G-4  class LIVENESS_AUTHORITY. In the adopter or same-UID context, forbids
     asserting that the actor is unable to block, delay, prevent or deny a
     death proof, a channel EOF or progress; and forbids the unqualified form
     of the assertion that it is unable to obtain process authority. The
     permitted forms are exactly: that it cannot create a false-positive
     object-bound death proof, and the four clauses of §P1-12.3's second table.
       ⇒ "guard G-4: adopter liveness or authority overclaim"
G-5  class LIVENESS_GUARANTEE. Forbids asserting that this contract guarantees
     completion, eventual proof availability, eventual channel EOF, stall
     termination, or same-UID confinement.
       ⇒ "guard G-5: liveness or confinement guarantee"

Decision rule: a violation is reported if and only if a forbidden normalized
pattern of that class occurs as a substring of NORMALIZE(REGION(BODY)). Because
the target is one region of one file with no exclusions, the result is a total
function of this file's bytes.

**Standing constraint on this subsection, `AD-1`.** (This discipline was
labelled `G-10` in versions 1.2 and 1.3. **It is renamed to `AD-1` here**,
because `G-10` is now reserved uniquely for the unresolved-variant-block guard
of §P1-14.4. The discipline itself is unchanged.) No pattern string may be
reproduced in the body region, including inside the prose that describes the
rule that forbids it. The rule descriptions above therefore paraphrase their
classes and never quote a pattern; the pattern strings exist once, in the guard
data region, which is not itself a match target. A verifier run in which
`NORMALIZE(REGION(BODY))` contains any pattern of the guard data region reports
that pattern under its own class in the ordinary way — there is no exemption
for self-description, because an exemption would be an exclusion list and the
guard target admits none. `AD-1` is the authoring discipline that keeps the
body clean; it is checked by test 76.

**`AD-1` ranges over the `G-1` through `G-5` pattern classes only.** The
`VARIANT_MARKER` class of §P1-17 is OUTSIDE `AD-1`'s range and is the exclusive
target of `G-10`. The two never range over the same pattern class, so neither
can fire on the other's data.
```

### §P1-14.4 The closed invariants

```text
G-6  Recompute H_BODY, H_GUARDDATA and H_NORMATIVE by the extraction algorithm
     at the head of this file and compare each with the value the production
     manifest records under p1_composite_body_sha256,
     p1_composite_guarddata_sha256 and p1_composite_normative_sha256.
     Any mismatch ⇒ "guard G-6: normative region digest differs".
     Any edit to either normative region changes a digest and therefore
     requires a new signed and reviewed version. Even if a wording guard failed
     to match a novel phrasing of a withdrawn overclaim, the edit itself cannot
     pass unnoticed.
G-7  Recompute H_FILE and compare it with the manifest's p1_composite_sha256.
     Any mismatch ⇒ "guard G-7: composite file digest differs".
     This covers the non-normative provenance region as well, so no byte of the
     file can change without detection.
G-8  Run the extraction algorithm's sentinel checks. A count other than one for
     any of the six sentinels, or an order violation, ⇒ "guard G-8: sentinel
     cardinality or order". This runs before any other guard and before any
     digest, and it fails closed.
G-9  The verifier's own compiled fragment constants must equal the five
     fragments of §P1-14.0 byte for byte, and its region and edge name sets must
     equal those two three-element and two-element sets exactly. Any difference
     ⇒ "guard G-9: verifier sentinel constants differ". This prevents a
     verifier from silently extracting a different region than the one this
     document delimits.
G-10 UNRESOLVED AUTHOR-CELL VARIANT BLOCKS. Match `NORMALIZE(REGION(BODY))`
     against every pattern of the `VARIANT_MARKER` class of §P1-17. A single
     occurrence of any of them ⇒ "guard G-10: unresolved watchdog-freeze variant
     block".
     **THE PATTERN STRINGS ARE NOT REPRODUCED HERE.** They exist once, in the
     guard data region, which is not itself a match target. This rule therefore
     CANNOT MATCH ITS OWN DEFINITION, and it obeys `AD-1` exactly as `G-1`
     through `G-5` do. (In version 1.3 this guard quoted its own patterns in the
     body and consequently could never be satisfied; that defect is repaired
     here.)
     `G-10` IS RESERVED UNIQUELY FOR THIS RULE. No other rule, discipline or
     constraint in this document carries the identifier `G-10`.
     Before the watchdog-freeze author cell is signed EVERY occurrence is
     expected and the document is NOT OPERATIVE; after signature exactly one
     branch of each block is retained inline and no marker remains. THERE IS NO
     STATE IN WHICH A MARKER IS PRESENT AND THE DOCUMENT IS OPERATIVE.
     `G-10` is INDEPENDENT of `G-11`: neither is a precondition of the other,
     and each fails closed on its own.
G-11 JOINT INSTALL COMPLETENESS, THE FAIL-CLOSED GATE. This is the P1 statement
     of the install record of §A10 of the peer amendment. The two are ONE RULE
     WITH TWO STATEMENTS and must agree byte-for-byte in their member classes.

     THE CLOSED INPUT SET — seven pairwise-disjoint member classes, exhaustive,
     with no wildcard and no directory scan:
       M1 GOVERNING SPECIFICATION, exactly two members: the peer amendment
          v1.1 and this composite v1.4, in its post-variant-resolution bytes
       M2 IMMUTABLE PROVENANCE SET: every path listed in §P1-18's provenance
          region, with its recorded digest. THE SET IS EXACT — an omission and
          an extra member are equally fatal
       M3 ACCEPTED PEER CHAIN: the five generic-harness contract files, the
          generic-harness signature, and the batch-settlement amendment
       M4 MANIFEST: its schema id, its version, and the digest of its bytes
       M5 POST-HANDOFF VERIFIER: the digest of the verifier bytes implementing
          S-1..S-24b, G-1..G-11 and AD-1
       M6 TEST BUNDLE: the digest of the test module bytes carrying rows 92..115
       M7 PASSING ATTESTATION: the digest of the attestation object recording
          that the full matrix ran against the M5 verifier and the M6 bundle and
          that every row passed
     There is no eighth class and no member outside a class.

     THE CHECK, before ANY production entry point — before any process is
     created, any handle is allocated, any freeze route is reachable, any
     evidence is accepted and any settlement runs — fail-closed at the first
     failure:
       1. enumerate the members FROM THE CLASS DEFINITIONS ABOVE, not from the
          install record;
       2. recompute the SHA-256 of every enumerated member;
       3. recompute install_record_id per §A10 IR-1 from what was found on disk;
       4. require it to EQUAL the install record's filename;
       5. require it to EQUAL the authorized id in the EXTERNAL TRUST ROOT — the
          author signature file, which is not a member of M1..M7 and is written
          by no handoff step;
       6. require the record's member list to EQUAL the enumerated set exactly:
          same cardinality, same paths, same digests;
       7. require the M7 attestation to reference the M5 and M6 digests found at
          step 2, so a passing attestation from a different verifier or a
          different test bundle is rejected.

     NO COMPONENT ATTESTS ITS OWN PRESENCE OR DIGEST. This composite does not
     carry H_FILE of itself; the verifier does not carry its own digest; the
     manifest does not carry its own digest; the attestation does not attest
     itself. Every member is attested by the install record, and the record is
     attested by its own content-addressed name and by the external trust root.
     THE BINDING IS THEREFORE NON-CIRCULAR.

     ON ANY FAILURE ⇒ REFUSE with "WATCHDOG_AUTHORITY_INSTALL_INCOMPLETE" and a
     reason code: INSTALL_RECORD_ABSENT, INSTALL_RECORD_NAME_MISMATCH,
     INSTALL_RECORD_UNAUTHORIZED, MEMBER_OMITTED, MEMBER_EXTRA, MEMBER_STALE,
     MEMBER_SUBSTITUTED, ATTESTATION_MISMATCH, HISTORICAL_BYTE_MOVED.
     On refusal NO process is created, NO handle is allocated, NO freeze route
     is reachable, NO evidence is accepted and NO settlement runs. There is no
     partial mode, no warning mode and no override. A PARTIALLY INSTALLED STATE
     NEVER SATISFIES THIS CONTRACT AND NEVER SILENTLY DEGRADES TO THE HISTORICAL
     BEHAVIOUR. A MIXED-GENERATION SET — the v1 amendment with this composite,
     or the v1.1 amendment with composite v1.3 — produces an id matching no
     authorized value and fails at step 5.
     Verifying a digest is not opening a document for behaviour.
```

### §P1-14.5 Acyclic hash custody

```text
This file contains none of its own digests, so there is no cycle. The custody
chain is a directed acyclic graph with four links and no back edge:

  1. this composite file                — contains no digest of itself
  2. the author closure                 — reports H_FILE, H_BODY, H_GUARDDATA
                                          and H_NORMATIVE
  3. the independent X and Y reviews    — recompute and confirm all four
  4. the production manifest            — records the reviewed values, which
                                          G-6 and G-7 then enforce against the
                                          live bytes

No step reads a digest from a document that contains it. Verification order is
1, then 2, then 3, then 4, and the verifier at step 4 depends only on the
manifest and this file's bytes.
```

### §P1-14.6 The code rules

```text
CHANGE 1  PRODUCTION_ROOTS is exactly the five paths of §P1-3.1
CHANGE 2  the allowlists of §P1-3.2, with the scoped map exact and never a
          union with the default
CHANGE 3  the AST grammar over each root:
  S-1  the PCS root has exactly six Import nodes naming os, sys, _signal, time,
       fcntl and _socket; the role root has exactly three naming os, sys and
       fcntl; all at module scope, unaliased, with no ImportFrom, and none
       conditional or nested
  S-2  no Global, Nonlocal, AsyncFunctionDef, Await, Yield, YieldFrom, Lambda
       or ClassDef node; no decorator; no starred argument to a bound primitive
  S-3  the binding block is exactly the list of §P1-3.4, in that order, at
       module scope, each target a plain Name and each value an Attribute of
       one of the permitted modules
  S-3b the first executable statement is the assignment of type(len) to
       _BUILTIN, and len appears nowhere else
  S-4  every bound name is assigned exactly once and never rebound, deleted,
       used as a parameter, or passed to setattr
  S-5  the six module names appear as an Attribute value only inside the
       binding block
  S-6  every Call func is a plain Name, a bound name, or a builtin from the
       closed set { len, int, str, bytes, range, enumerate, sorted, min, max,
       abs, tuple, list, dict, set, frozenset, isinstance, type, repr, ord,
       chr, divmod, bool }; never a Subscript and never an arbitrary expression
  S-7  forbidden names anywhere in the PCS and role roots: signal, functools,
       enum, _thread, threading, multiprocessing, concurrent, asyncio, ctypes,
       subprocess, atexit, gc, hashlib, json, re, array, struct, socket, prctl,
       PR_SET_CHILD_SUBREAPER, register_at_fork, start_new_thread, settrace,
       setprofile, addaudithook, set_wakeup_fd, pthread_sigmask, pthread_kill,
       siginterrupt, alarm, setitimer, pidfd_send_signal, SIG_IGN, readlink,
       PYTHONPATH, putenv, SO_PASSCRED, SCM_CREDENTIALS, getattr, setattr,
       delattr, vars, globals, locals, eval, exec, compile, __import__,
       importlib, and the builtin open
  S-8  every _waitpid call's first argument is either the literal -1 at exactly
       one call site, whose enclosing function is the P-e preflight and which is
       lexically before every create call, or a plain Name bound from a create
       return. No _wait, _wait3, _wait4 or _waitid binding exists.
  S-9  every _sigsignal call's second argument is _SIG_DFL; every _getsignal
       call's argument is _SIGCHLD
  S-10 no __del__ method, weakref finalizer, or context-manager exit calls a
       bound primitive
  S-11 every _posix_spawn call passes the argument shape of §P1-7.1 or §P1-9.1,
       with a file_actions literal in the order of §P1-6.4 and with no
       preexec_fn, shell or cwd keyword
  S-12 subprocess, Popen, fork, waitpid, kill, killpg and system appear on no
       path of generic_harness.py
  S-13 no "/proc/self/fd/" string literal is concatenated with a non-constant
       expression; the descriptor paths are exact constants
  S-14 every _recvmsg call passes _MSG_CMSG_CLOEXEC in its flags argument
  S-15 every _recvmsg ancillary buffer argument is exactly _CMSG_SPACE(12)
  S-16 no wire-record field is derived from a descriptor: fileno, detach and any
       call to a fileno method are forbidden in the record builders
  S-17 the role root contains exactly one assignment to a slice of sys.path,
       whose value is a one-element list holding a literal beginning with
       "/proc/self/fd/"
  S-18 a /proc/self/fd enumeration appears only at the three sites of §P1-6.5
       with that site's permission; an enumeration at P-f or A-5 followed by a
       close whose argument derives from the listing is a violation
  S-19 the _recvmsg exception handler body is exactly one Expr whose value is a
       Call to _exit_ with the single constant T_PCS_EXIT_RECV_UNENUMERABLE,
       with no other statement, no else clause and no finally clause. S-19
       asserts an AST property and asserts nothing about interpreter behaviour
       before the handler runs.
  S-20 the SPAWN.lock open passes _O_CLOEXEC and is followed by an _fcntl with
       _F_GETFD whose failure branch refuses; no _F_SETFD call exists anywhere
  S-21 no file_actions literal names the lock descriptor; the grandchild
       contains exactly one _dup2 with destination 3 and the keyword
       inheritable set to True, whose source is the hoisted lock descriptor
  S-22 no signal call site is reachable with a watchdog handle or a watchdog pid
  S-23 prctl, PR_SET_CHILD_SUBREAPER and ctypes appear in no production root
  S-24a static: exactly one decision branch consumes a wait-status word, and it
       is the named WIFSTOPPED site in the AWAIT_STOP handler
       ⇒ "S-24a: wait status consumed outside the single named site"
  S-24b topology: every controller and worker creation site is a _posix_spawn
       call in the PCS root, and no create call for either role appears in any
       other root. This is what makes the WIFSTOPPED target a live-custody
       non-orphan direct PCS child; a future topology change fails here even if
       S-24a still counts exactly one branch.
       ⇒ "S-24b: role creation outside the PCS"
CHANGE 4  generic_harness.py contains no import of signal, no attribute access
          on signal or _signal, and no import of sys
CHANGE 5  the manifest records root_source_sha256 for all five roots and the
          four fields p1_composite_sha256, p1_composite_body_sha256,
          p1_composite_guarddata_sha256 and p1_composite_normative_sha256; the
          verifier recomputes and compares each, and a mismatch is fail-closed
```

### §P1-14.7 Runtime preflight

The properties static analysis cannot decide, each fail-closed with no fork, no
lock acquisition and no record installed: `P-a` platform; `P-b` interpreter
identity and the four isolation flags; `P-c` and `P-d` single task; `P-e` no
inherited children; `P-f` descriptor topology and source and interpreter object
properties; `P-g` signal state including the exact `g-5` relations; `P-h`
request grammar; `P-p` package-root binding; §P1-3.5's primitive identity check;
`G-3`'s inheritability readback; and `A-1` through `A-11`.

> **TI-1, the topology invariant, stated separately from any single rule.**
> Every process whose wait status is consumed by a decision is a direct child of
> the PCS at the moment of consumption. `S-24a` checks the count of
> status-consuming branches; `S-24b` checks that role creation lives only in the
> PCS; and behavioural test 33 of §P1-15 checks that the `AWAIT_STOP` target is a
> non-orphan direct PCS child at the moment the status is read. **No single rule
> carries TI-1 alone, and no rule is described as if it did.**

---

### §P1-14.8 The complete atomic handoff

**Stated here IN FULL and identically at §A9 of the peer amendment. NEITHER COPY
DEFERS TO AN AUTHOR CLOSURE, and no closure adds a step.** Every author closure
is an untrusted self-assessment and is normative for nothing.

```text
H-1  ONE UNIT. The v1.1 peer amendment and this composite v1.4 are ONE
     indivisible acceptance unit. Neither is operative alone. Accepting one
     without the other is NOT a conforming state and NOT a partial success. The
     v1 amendment and composite v1.3 are WHOLLY REPLACED, not amended.

H-2  THE ORDERED STEPS. All of them land together or none does.
      1. install the v1.1 peer amendment
      2. install this composite v1.4
      3. resolve every variant block to the SIGNED branch and DELETE the other;
         after this step G-10 must find zero markers
      4. install the post-handoff verifier implementing S-1..S-24b, G-1..G-9,
         G-10, G-11 and the authoring discipline AD-1
      5. install the test bundle rows 92..103 and the install-integrity rows
         104..115
      6. run the full test matrix; ALL rows must pass; write the M7 passing
         attestation
      7. recompute H_FILE, H_BODY, H_GUARDDATA, H_NORMATIVE and the six sentinel
         counts; run the placeholder audit and the guard fires. Required
         placeholder count and guard-fire count are ZERO
      8. write the manifest naming every governing digest
      9. compute and install the §A10 install record, LAST, no-replace, at its
         content-addressed name
     10. verify by digest that EVERY historical file is byte-identical to its
         recorded value

H-3  NO PARTIAL LANDING IS CONFORMING OR OPERATIVE. G-11 is the enforcement
     point and it runs before any production entry point.

H-4  EXISTING HISTORY REMAINS BYTE-IDENTICAL. Zero historical bytes are edited
     by any step above. Step 10 verifies this and refuses on any difference.
```

---

## §P1-15. The test matrix

Every row is a future obligation. Nothing here is authorized to run.

| # | Test |
|---|---|
| 1 | the launch is byte-exact: the six-element argv of `L-2`, an empty environment, an empty signal mask argument, twelve file actions in the order of §P1-6.4, and no `preexec_fn`, shell, cwd, close-descriptors or pass-descriptors keyword |
| 2 | `readlink` appears nowhere; the exec targets are the two literal descriptor paths; `sys.executable` is used for nothing |
| 3 | source-object binding: unlink, rename, replace at the name, truncate, hardlink and symlink at the name each behave as §P1-7.1 requires |
| 4 | the hoist terminates, yields pairwise-distinct descriptors above the target maximum, and closes every intermediate; a forced collision refuses |
| 5 | `POSIX_SPAWN_DUP2` clears close-on-exec on the destination; the mapped slots are inheritable and every other close-on-exec descriptor is closed by the exec |
| 6 | the three spawn-action constants pass the set-equality and distinctness validation, and a rebound constant is rejected |
| 7 | spawn failure modes: a raise, a non-int return, a return at most zero, and a failing file action each route as §P1-7.1 and §P1-11.7 state |
| 8 | the launcher performs no fork, no `Popen`, no `preexec_fn` and no shell, statically and dynamically |
| 9 | a caller that defeats its own launcher checks produces a process the PCS preflight refuses |
| 10 | `P-a` through `P-p` each return exactly one named result; no exception escapes; every non-success result reaches the fail-closed body with no fork |
| 11 | `P-b` refuses when any one of the four isolation flags is dropped; the refusal is read from the interpreter's flags and argv is consulted nowhere |
| 12 | with the site module disabled, a `.pth` line, a `sitecustomize` and a `usercustomize` present on the host each execute in the caller and in no PCS or role process |
| 13 | the PCS import set is exactly the six of §P1-3.2, and `signal`, `functools`, `enum` and `_thread` are absent from the closure |
| 14 | every row of §P1-3.5's identity table passes for a genuine binding and fails for its stated substitution: a Python function, a partial, a bound method, a callable instance, a foreign-module builtin, a wrong qualified name, and a wrong constant value |
| 15 | `P-e`'s single wildcard wait raises `ECHILD` in a correct launch; a fixture handing the PCS an inherited child makes it return, and the route refuses `INHERITED_CHILD` with no fork |
| 16 | the `g-5` relations hold exactly: the caught mask is zero afterwards; the ignored mask afterwards equals the ignored mask before with only the `SIGCHLD` bit cleared; an inherited ignored `SIGCHLD` and an inherited no-wait flag are both cleared; and an ignored `SIGPIPE` bit set before is still set after |
| 17 | `g-2` refuses a non-zero blocked mask |
| 18 | the mask grammar rejects the empty value, `0`, `0000`, a 13-digit value, a 20-digit value, a hexadecimal prefix, a sign, internal whitespace, a trailing byte, a missing field and a duplicated field; conversion happens only after both width conjuncts pass |
| 19 | the platform check accepts x86-64 and refuses MIPS, ARM64, i386, Alpha, SPARC and every non-Linux system at `P-a`, before any mask is parsed |
| 20 | `c1`'s lock is created close-on-exec and the readback holds; a fixture clearing the flag makes `c1` refuse with no fork; no `F_SETFD` call exists |
| 21 | `G-1` through `G-6`: eight hoisted sources above 10, ascending duplications, the `G-3` readback proving the flag clear on every slot, and the original lock copy closed at `G-4` |
| 22 | the fork-shared lock trace: the lock persists while the middle lives, survives the grandchild's exec on slot 3, and releases only when the PCS, the middle and the supervisor have all closed |
| 23 | no controller, worker or watchdog holds a descriptor whose device and inode equal the lock's at any instant after its exec |
| 24 | after every spawned role's exec, `/proc/self/fd` is exactly `{0,1,2}` with its slot set, established by construction; `A-5` is asserted to be a verification |
| 25 | the watchdog file actions contain the explicit close of 6; no file-action vector for any role names the lock |
| 26 | the role bootstrap imports exactly three modules; a two-import build fails at `A-6` |
| 27 | `A-1` through `A-13` refuse in order with nothing written; `A-9` sets exactly one object-bound path entry; `A-11` rejects a role module substituted after `A-7`; `A-12` rejects each malformed controller and worker argv element |
| 28 | the environment is empty in every role, and `PYTHONPATH` appears in no launch path in the repository |
| 29 | the six-vector proof of §P1-7.4 holds for a contaminated controller and worker |
| 30 | `WAIT_ONE` is total over every returned object and every raised object: a non-tuple, a wrong arity, boolean elements, a negative pid, a wrong positive pid, a zero pid with a non-zero status, an out-of-range status, `ECHILD`, `EINTR`, another errno, a `None` errno, `SystemExit`, `KeyboardInterrupt`, `GeneratorExit`, `MemoryError`, `RecursionError`, and an arbitrary `BaseException` |
| 31 | the `STRUCTURAL_VIOLATION` continuation at every site: never death, `CONTRADICTED` set, no signal ever again, no record touched |
| 32 | `WAIT_ONE` invoked after a reap performs no syscall and is a contract violation |
| 33 | **TI-1**: at the moment `AWAIT_STOP` reads a status, its target is a live-custody non-orphan direct PCS child; `S-24a` and `S-24b` both hold, and neither alone is described as carrying TI-1 |
| 34 | the identity table I-1 through I-10 is total over the product of the five observation results, captured and uncaptured, equal and unequal ppid, and the three ownership entry states |
| 35 | row I-4 captures nothing, sends no signal, and writes no durable record from a contradicted observation |
| 36 | `os.kill` executes only when ownership is `OWNED`; injected `REAPED` and `CONTRADICTED` states make every signal site unreachable |
| 37 | `SIGNAL_ATTEMPT` returns exactly one of five results; `ESRCH` under `OWNED` sets `CONTRADICTED`; `EPERM` does not |
| 38 | the pid-reuse window: with normalization in place, inject a child exit at every instruction boundary between the observation and the kill; the pid is never reassigned before this route's own reap |
| 39 | `/proc` fully unreadable with a live child: the route terminates and reaps; `/proc` fully unreadable with a stopped child: `SIGKILL` under ownership alone reaches it |
| 40 | the three terminal predicates are pairwise disjoint and exhaustive; `B` returns nothing, retains lock, record and handle, installs nothing, and exits only by a positive reap or a valid capture |
| 41 | the stage-M causal trace: at `c5`, `c6` and `c7` no release byte exists, the middle is at `m0` owning its write end, EOF at `m0` never occurs, `m1`, `m2`, `m4`, `m5` and `m7` are unreachable, no grandchild is forked, and the next PCS cannot acquire the lock until the middle exits |
| 42 | the socket pair is created before the `c4` fork; the peer reaches the supervisor role at slot 6 and nowhere else |
| 43 | a 4096-byte payload is delivered whole; a 4097-byte payload is refused before the send |
| 44 | the descriptor vector for each opcode and status equals §P1-8.7's row exactly; every other count or type is an ancillary violation |
| 45 | the close-on-exec receive flag is passed on every receive; received descriptors carry the flag with no window |
| 46 | a truncated control buffer, a truncated payload, a non-rights ancillary item, a ragged control length and an over-long control length each route as §P1-8.7 states |
| 47 | `B-2` is non-aborting: a message whose first control item is not of the rights kind and whose second carries descriptors still yields the complete vector, and `B-4` closes every one of them |
| 48 | `B-4` closes exactly the parsed vector, de-duplicated, ascending, once each; a concurrent live role's control and status descriptors survive |
| 49 | `/proc/self/fd` is enumerated at exactly the three sites of §P1-6.5 and nowhere else; `P-f` and `A-5` perform no close derived from the listing |
| 50 | no double close and no leak at every ownership cut, including sender death mid-send and receiver death with descriptors buffered |
| 51 | the receive exception handler body is exactly one exit call; no test and no contract sentence claims that no callback can run before it |
| 52 | replay of an accepted entry yields `OPERATION_INCONCLUSIVE` with no syscall; replay of a completed or acknowledged entry yields the recorded record with no descriptors |
| 53 | the `J1` through `J6` order holds and every crash cut behaves as §P1-8.6 tabulates |
| 54 | one outstanding request at a time; an out-of-order or unmatched response is a transport structural violation |
| 55 | an unknown opcode, field count, handle, state and generation each yield `INVALID` with no side effect |
| 56 | the protocol has exactly nine operations and no field carrying a pid, descriptor, path, target argv, signal number, symbol or unbounded integer |
| 57 | both signal opcodes are refused for a watchdog handle at every state, and no signal reaches a watchdog on any path |
| 58 | `SPAWN_WATCHDOG` has one uniform meaning; no replacement-specific opcode, handle role or degradation flag exists |
| 59 | handle ids are never reused; release requires a reaped state; shutdown refuses while a handle is live |
| 60 | the watchdog never uses `getppid()`; a PCS-death fixture with the supervisor alive produces no freeze from the `getppid()` change — **and produces no freeze from the watchdog on any path, because the watchdog executes none** |
| 61 | supervisor death produces update-pipe EOF and the watchdog's **write-nothing exit** route; **no freeze and no observation occurs on that path**. `[W-B]` Loss of the peer control endpoint additionally produces the PCS's record-first §P1-10.7 classifier and its terminal. `[W-A]` Loss of the peer control endpoint additionally produces the PCS's bounded service window; an `ACCEPTED` `t-wd-freeze.v1` record produces the classifier and its terminal, and window end without one produces no freeze |
| 62 | watchdog termination is EOF-driven; `WATCHDOG_UNREAPED` routes to §P1-11.6 with no signal |
| 63 | every one of the thirteen watchdog properties of §P1-9.2 holds in a live generation. The properties remain **thirteen**; properties **7, 11 and 12** carry amended text under `P1_WATCHDOG_FREEZER_ROLE_REASSIGNMENT_V1`, and property 8 — the read-only identity verification — is carried **verbatim and unamended** |
| 64 | `S-1` through `S-7` shutdown ordering, and each `S-5` branch behaves as tabulated |
| 65 | PCS death: adoption per §P1-4.2, an accepted journal state, supervisor authority lost, freeze unavailable, watchdog closed out, generation invalid |
| 66 | a PCS started against a non-terminal generation responds `GENERATION_NOT_ADOPTABLE`, acts on nothing, and exits |
| 67 | the supervisor is not in the PCS's child set; a wildcard wait in it returns `ECHILD`; no wait on a supervisor pid exists in any source |
| 68 | the PCS may signal the supervisor's group only after `c11` has made the group record durable with the verified flag true |
| 69 | with a non-interfering ancestor subreaper the contract produces identical decisions and identical durable records to a run with none; timing and process lifetimes are not asserted equal |
| 70 | with an interfering adopter that stops an adopted process, the run fails closed: no fabricated death proof, no record removed, generation invalid. Identical behaviour is not asserted |
| 71 | a promptly reaped orphan yields `/proc` absence and a recycled pid yields live with a different identity; both route with no kill |
| 72 | an injected forcibly terminated adopted process yields a status outside any previously claimed set and changes no decision |
| 73 | no descriptor, handle, opcode or journal authority reaches any adopter |
| 74 | the four singleton records have exactly the schema values and key sets of §P1-5.1, and each field carries the meaning of §P1-5.2 |
| 75 | the two in-flight bootstrap records have exactly the schema values and key sets of §P1-5.3 |
| 76 | guards `G-1` through `G-5` each reject a bit-exact negative fixture inserted into a copy of the body region and accept the real one; the guards open exactly one file. `AD-1` (the authoring discipline formerly labelled `G-10`): every pattern of the `G-1` through `G-5` classes of the guard data region is searched against `NORMALIZE(REGION(BODY))` of the real file and the count is zero for every one of them, including the patterns whose classes §P1-14.3 describes in prose. The `VARIANT_MARKER` class is outside `AD-1`'s range and is exercised by test 102 instead |
| 77 | `G-6` and `G-7`: a one-byte edit inside either normative region changes a digest and fails against the manifest, and a one-byte edit in the provenance region fails the file digest |
| 78 | `G-8`: a duplicated sentinel, a missing sentinel, reordered sentinels, and a sentinel-shaped line appearing as an example each fail closed before any digest is computed. `G-9`: a verifier built with any altered fragment, region name or edge name is rejected, and the six constructed values occur exactly once each in the real file |
| 79 | `S-1` through `S-24b` each reject a bit-exact negative fixture and accept a positive one |
| 80 | the five production roots are exactly those of §P1-3.1; the scoped map gives each root exactly its set; `generic_harness.py` imports none of `signal`, `_signal` or `sys` |
| 81 | the manifest's five root digests and four composite digests are recomputed and compared, and a one-byte change fails |
| 82 | every safety property `S1` through `S4` is asserted, and every liveness item `L1` through `L5` is asserted as not guaranteed; no text claims any of `L1` through `L5` |
| 83 | every unknown control outcome settles through §P1-11.6 and produces no completion, capacity, custody, spend or qualification fact |
| 84 | the four-artifact matrix of §P1-13.2 holds exactly: for each row, the recorded path rule, schema value and key set match the artifact the implementation produces or reads; the P1 layer opens exactly two peer-owned artifacts, both read-only — the spawn-intent record and the supervisor identity record; the P1 layer opens the process-claim and freeze-observation records on no path; and the six P1 outputs of §P1-13.3 carry their stated invariants |
| 85 | nothing in the out-of-scope list of §P1-13.8 is read, written or produced by any P1 code path, **and** none of the four artifacts of §P1-13.2 appears in that list. A build in which the spawn-intent, process-claim, supervisor-identity or freeze-observation artifact has been moved into the out-of-scope list fails this test |
| 86 | **wrong logical writer**: a build in which a P1 root contains an install site for any of the four artifacts fails; a build in which the peer layer's spawn-intent install is reachable from the PCS root fails; a build in which the P1 client writes the process claim fails |
| 87 | **missing identity read**: a build in which `c17` does not read and live-verify the supervisor identity record fails; a build in which the watchdog does not read it, or infers supervisor identity from any parent relationship instead, fails |
| 88 | **duplicate claim write**: two layers independently installing the same no-replace record is rejected — for each of the four artifacts the install site is exactly one function in exactly one root per §P1-13.7, and a second install site anywhere in the reachable closure fails the test |
| 89 | **wrong freeze writer, and the two signed freeze-execution sites.** A freeze observation whose `killer` value is not the constant `SUPERVISOR` is rejected; a freeze observation written by a process that is **not the supervisor role process** is rejected — the watchdog role writes no record of this class on any path, and no other process may write one; and a group stop performed for a freeze is rejected unless it is one of **exactly two** signed execution sites: **(a)** the supervisor's freeze routes of §P1-13.9 — **both `ROUTE-D` and `ROUTE-W`** — which reach every group stop through the `SIGNAL_GROUP` opcode and may not bypass it; and **(b)** the PCS's own freeze classifier of §P1-10.7, executing in the PCS root, under `KV-1`..`KV-6` re-evaluated before every `_killpg`, against the scope computed from the PCS's own handle table, reachable only from its own trigger site (`[W-B]` the endpoint-loss site; `[W-A]` an `ACCEPTED` `t-wd-freeze.v1` record inside the bounded service window). Site (b) is request-driven by no peer opcode and is **not** `SIGNAL_GROUP`-mediated; site (a) is mediated and is not autonomous. Both sites' `_killpg` executes in the PCS root and nowhere else, so the PCS remains the **sole caller** of `killpg` and `S-12` is retained unchanged. Any other freeze-observation writer, and any other executor of a freeze group stop, is rejected. **Site (b) installs no record of any peer class:** its journal terminal, its per-group tokens and its `freeze_ns` are P1-owned process-control journal facts, are never a `t-freeze-observation.v1`, are never a field of a `t-freeze-fallback-observation.v1`, and are never an input to any peer validity predicate (`L8`, `ND-1`..`ND-3`). A build in which any of them reaches a peer artifact, an acceptance predicate, a qualification, a comparison, a Q or C fact or any published record fails this test |
| 90 | **process-name based ownership inference**: a build that derives write authority from the executing process's identity, from a module name, from a file path, or from reachability from an entry point, rather than from §P1-13.2, fails. The fixture presents a peer-owned write performed inside a P1-created role — the row 3 and row 4 cases — and requires the implementation to treat it as a peer-layer write |
| 91 | `SW-1` through `SW-5` hold over the four rows: exactly one schema owner and exactly one logical writer each; **no artifact carries a live multi-process discriminator, because row 4 now has exactly one executing process**, and its retained `killer` key is a carried peer-schema field; and no artifact has two install sites |

| 92 | **peer writer singularity.** A build or fixture in which any path installs a `t-freeze-observation.v1` from the watchdog role process fails. The freeze-witness function has exactly one caller class — the supervisor role process on the two routes of §P1-13.9 — asserted in the same run as invariant 89 |
| 93 | **acceptance predicate.** An observation carrying `killer == WATCHDOG`, presented on any path, is REJECTED by the peer acceptance predicate's conjunct 8, is permanently non-evidence, and routes to the fallback with `rejection_conjunct = 8`. A fixture asserting that the schema enum was narrowed to `{SUPERVISOR}` also fails: the enum is retained |
| 94 | **no re-entry of `WATCHDOG`.** No default, migration, compatibility shim, recovery path, archival re-import, takeover re-derivation or fixture can set, coerce, infer or grandfather `killer == WATCHDOG` into an admissible object. The fixture attempts each in turn and each is rejected at conjunct 8 |
| 95 | **both routes, one writer.** A fixture drives `ROUTE-D` with a live healthy watchdog and `ROUTE-W` with a dead one. Both produce a supervisor-written observation with `killer = SUPERVISOR`, in the same namespace, accepted by the same predicate, with every group stop reaching `SIGNAL_GROUP`. A fixture in which `ROUTE-D` is unreachable while the watchdog is alive fails, and a fixture in which either route is entered by the watchdog role process fails |
| 96 | **`ROUTE-D` drain.** A renewed lease whose successor table is durable and acked is NOT frozen against the superseded deadline; a renewed lease whose successor table is not acked IS frozen against the old deadline |
| 97 | **strict progress.** A proved-quiescent sample equal to the deadline yields bounded later monotonic sampling with re-proved quiescence; exhaustion without strict progress yields `freeze_ns = null`, `overrun_ns = null`, `quiescence = UNKNOWN`; no valid zero-overrun branch is reachable |
| 98 | **watchdog negative surface.** In the watchdog role process: no signal is sent or received, no `killpg`, no `kill`, no quiescence proof, no evidence write, no settlement, no `runtime/` write and no ledger append occurs on any path. The single permitted peer operation is the read-only supervisor-identity verification, and a build omitting it fails invariant 87 |
| 99 | **endpoint count and type.** `[W-B]` the watchdog's `/proc/self/fd` is exactly `{0,1,2}` together with `{3,4,5,7,8,9,10}`, slot 6 explicitly closed — two sealed pipes. `[W-A]` exactly `{0,1,2}` together with `{3,4,5,6,7,8,9,10}`, with slot 6 `S_ISSOCK`, `O_RDWR`, `SOCK_SEQPACKET` — three sealed endpoints. In BOTH: no PCS descriptor is a write end of the watchdog update pipe, and update-pipe EOF remains reachable on supervisor death |
| 100 | **filename and object identity.** The witness path is `WATCHDOG/FREEZE/<witness_id>.json`; `witness_id` recomputes from the canonical `{supervisor_generation_sha256, process_id, table_seq}` and equals the filename; a fixture writing `<process_id>.json` fails; a fixture in which two distinct triples collide on one path fails |
| 101 | **PCS journal invisibility.** The §P1-10.7 classifier's terminal, per-group tokens and `freeze_ns` reach no peer artifact, no acceptance predicate, no qualification, no comparison, no Q or C fact and no published record. A build in which any of them does fails |
| 102 | **no variant block survives.** `G-10` is run against the accepted file and every pattern of the `VARIANT_MARKER` class of §P1-17 has count zero in `NORMALIZE(REGION(BODY))`. A build extracted from a file in which any of them has a non-zero count is refused by `G-10`. **This row paraphrases its patterns and never quotes one**, for the same reason `G-10` and `AD-1` do: a row that quoted a marker would place it in the body and make the guard fire on the test matrix itself |
| 103 | **historical bytes unmoved.** Every file of the provenance region has its recorded digest. A build in which any historical digest differs, or in which the peer amendment or this composite is absent or stale, is refused with `WATCHDOG_AUTHORITY_INSTALL_INCOMPLETE` before any process is created |
| 104 | **install record absent.** With every `M1`..`M7` member present and correct but no install record at its content-addressed path, `G-11` refuses with `INSTALL_RECORD_ABSENT` and no production entry point runs |
| 105 | **install record name mismatch.** A record whose filename is not the SHA-256 of its own member list is refused with `INSTALL_RECORD_NAME_MISMATCH`. The fixture perturbs one member digest inside the record while leaving the filename intact, and separately renames a correct record |
| 106 | **install record unauthorized.** A record that is internally consistent and correctly named, but whose id is not the authorized id in the external trust root, is refused with `INSTALL_RECORD_UNAUTHORIZED`. The trust root is not a member and is not written by any handoff step |
| 107 | **member omission, every class.** For each of `M1`..`M7` in turn, one member is removed. Each removal changes the recomputed id and is refused with `MEMBER_OMITTED`. **No partial subset runs**: seven separate fixtures, seven refusals |
| 108 | **extra member, every class.** For each of `M1`..`M7` in turn, one extra file is added to the class. Each addition changes the recomputed id and is refused with `MEMBER_EXTRA`. An extra provenance file is as fatal as a missing one |
| 109 | **stale member, every class.** For each of `M1`..`M7` in turn, one member is replaced by an earlier version of itself. Each is refused with `MEMBER_STALE` |
| 110 | **substituted verifier.** A verifier implementing only `S-1`..`S-24b` and `G-1`..`G-9` — the pre-install baseline — is refused with `MEMBER_SUBSTITUTED`. A verifier implementing `G-10` but not `G-11`, and one implementing `G-11` but not `G-10`, are each refused. **The baseline verifier can never satisfy the gate** |
| 111 | **substituted manifest.** A manifest of the correct schema but a different version, and a manifest of the correct version but different bytes, are each refused with `MEMBER_SUBSTITUTED` |
| 112 | **substituted or omitted test bundle.** A bundle missing any of rows 92..115, and a bundle whose bytes differ from the attested digest, are each refused with `MEMBER_SUBSTITUTED`. A bundle that contains the rows but was never run produces no `M7` and is refused with `MEMBER_OMITTED` |
| 113 | **attestation mismatch.** An `M7` attestation that references a different verifier digest or a different test-bundle digest than the ones found on disk is refused with `ATTESTATION_MISMATCH`, even when every other member is correct |
| 114 | **mixed generation.** The v1 peer amendment installed with this composite v1.4, and the v1.1 amendment installed with composite v1.3, are each refused. Neither combination's id matches an authorized value |
| 115 | **no self-attestation.** A fixture in which any member carries its own digest — the composite carrying its own `H_FILE`, the verifier carrying its own digest, the manifest carrying its own digest, or the attestation attesting itself — fails. Every member is attested by the install record and by nothing else, and the record is attested by its name and the external trust root |

All tests use disposable roots, fake clocks and meters, no
production-compatible real artifact of the activated kind, and create no
capability, world, learner, entropy, capacity artifact, custody disposition,
result manifest or scientific object. Fixtures requiring an inherited no-wait
signal flag may use `ctypes`, which the runtime allowlist forbids but which does
not govern test fixtures.

---

## §P1-16. Negative space

This contract creates nothing executable and authorizes no implementation,
commit, host change, verifier edit, manifest, process, socket, pipe, FIFO,
fork, exec, signal, wait, `prctl`, supervisor, controller, worker, watchdog,
adapter, middle child, endpoint, journal instance, spawn record, lease,
capability, operation, framed transport, result manifest, quarantine record,
promoted object, capacity artifact, custody disposition, freeze witness,
entropy, spend, world, learner, candidate, qualification attempt, comparison
object, datum, outcome, Proof, or claim movement. It predicts no qualification
and no comparison outcome. Process invalidity, resource exhaustion, missing
evidence, the `B` residual, the receive-path exposure and the §P1-10.7
classifier's journal state are infrastructure facts and are nowhere scientific
evidence.

**This version selects neither watchdog-freeze option and neither process-claim
identity repair, edits no historical byte, and predicts no outcome.** No install
record was created. The install record, when created, is a generated
control-plane artifact carrying digests and no rules; it is never scientific
evidence, never a covariate, and never an input to any acceptance predicate. No example in this document was
written to any file.

<!-- OFFICINA-P1-BODY-END -->

<!-- OFFICINA-P1-GUARDDATA-BEGIN -->

## §P1-17. Guard pattern data — normative verifier data

**These bytes are normative.** They are the exact strings guard rules `G-1`
through `G-5` and `G-10` of §P1-14.3 and §P1-14.4 match against the normalized
body region. The `G-1`..`G-5` classes are additionally the range of the
authoring discipline `AD-1`; the `VARIANT_MARKER` class is the exclusive target
of `G-10` and is OUTSIDE `AD-1`'s range. These bytes change verifier pass and
fail behaviour, so they carry operative authority. They live in their own region
so that they are never matched against themselves, and their digest is
`H_GUARDDATA`, recorded in the manifest and enforced by `G-6`.

```text
G-1 ADOPTION:
  "re-parented to init"        "reparented to init"      "adopted by init"
  "init reaps"                 "init adopts"             "its parent is 1"
  "re-parented to pid 1"       "reaped by init"
G-2 ANCESTOR_WAIT_SET:
  "may wait on: the pcs only"        "wait on the pcs only"
  "sole holder of every pid"         "holds every pid in the system"
  "holds every pid in this system"   "holder of every pid in the system"
G-3 STATUS_SET:
  "closed, small set"          "closed small set"
  "from a closed set of exit"  "exit tokens - and carry"
G-4 LIVENESS_AUTHORITY:
  "forge or block a death proof"   "cannot block a death proof"
  "cannot delay a death proof"     "cannot prevent a death proof"
  "cannot deny a death proof"      "cannot gain officina process authority"
  "cannot gain process authority"
G-5 LIVENESS_GUARANTEE:
  "guarantees that the generation completes"
  "a death proof will become available"
  "the channel will reach eof"
  "the stall terminates"
  "same-uid actors are confined"

VARIANT_MARKER:                      # G-10 only; outside AD-1's range
  "[W-A]"                            "[W-B]"
```

<!-- OFFICINA-P1-GUARDDATA-END -->

<!-- OFFICINA-P1-PROVENANCE-BEGIN -->

## §P1-18. Provenance — non-normative

**These bytes carry no operative force and are read for behaviour by nothing.**
The documents below are historical evidence. None is opened by any implementer,
verifier or reviewer to determine behaviour. They are listed so a reviewer can
confirm that this composite was derived from a byte-intact chain.

**Every digest below is verified BEFORE any process is created.** A mismatch,
an absence or an extra file refuses the launch with
`WATCHDOG_AUTHORITY_INSTALL_INCOMPLETE`. Verifying a digest is not opening a
document for behaviour.

**ONE EXCEPTION, AND IT IS NAMED: `src/philosophia/officina/verification.py`.**
Its digest below is a **NON-ENFORCED PRE-INSTALL BASELINE**. It records what the
verifier was before the handoff and is evidence of derivation only. It is
**excluded from `M2`** and is **not** compared by `G-11`. The verifier that
`G-11` does enforce is the POST-HANDOFF verifier, pinned as member `M5` with its
own digest in the install record. Without this exclusion the gate would forbid
its own installation: `G-11` requires every `M2` digest to be exact, while
§P1-14.8 step 4 requires the verifier to change in order to implement `G-11` at
all. **The exception resolves that circularity and is the only one.**

**The two live authority surfaces are NOT in this region.** They are P1
operative composite v1.4 — this file — and
`successor/OFFICINA_GENERIC_HARNESS_WATCHDOG_FREEZE_AUTHORITY_AMENDMENT_V1_1_DRAFT.md`,
accepted jointly and indivisibly per authority level 3a. The accepted
generic-harness chain and the batch-settlement amendment are peer contracts and
are likewise not predecessors.

```text
746bcf3694a67d04eacaec66190cf68cb92ac0070ec3d8cb24abf6eb22efee0c  successor/OFFICINA_GENERIC_HARNESS_SUPERVISOR_CONTROL_CHANNEL_V1_DRAFT.md
bed7033eab1fa123598f6d4b03a7b69cb81c040af4cec4b21ca0e2e074181b7e  successor/OFFICINA_GENERIC_HARNESS_SUPERVISOR_CONTROL_CHANNEL_V2_DRAFT.md
9f1d018e7630d00da954910fa92cacc8005e0ecff90372e513f2fcec8593818b  successor/OFFICINA_GENERIC_HARNESS_SUPERVISOR_CONTROL_CHANNEL_V2_1_CORRECTION.md
ee3171724c89bd7e8f890141f42bf478838608c6f1908f9284218f1e940be635  successor/OFFICINA_GENERIC_HARNESS_SUPERVISOR_CONTROL_CHANNEL_V2_1_1_CORRECTION.md
2cd8b7b53c8efc292535ef79f38aa5e33ce57c5834138cc3deb1700f7edae373  successor/OFFICINA_GENERIC_HARNESS_SUPERVISOR_CONTROL_CHANNEL_V2_1_2_CORRECTION.md
72bfcc3f088ba538157145aed0bccc95a9ff2e1ad6c41f0579f32c9926274888  successor/OFFICINA_GENERIC_HARNESS_SUPERVISOR_CONTROL_CHANNEL_V2_1_3_CORRECTION.md
cc5af143f7e4dd886e21ca9e6734618236c2cc32daf2d7a610943e731cb7cc62  successor/OFFICINA_GENERIC_HARNESS_SUPERVISOR_CONTROL_CHANNEL_V2_1_4_CORRECTION.md
7ef8e4d3ac8f281dd50191e81d2760ed4467648b45ed2b17f6ce2012e4d017d4  successor/OFFICINA_GENERIC_HARNESS_SUPERVISOR_CONTROL_CHANNEL_V2_1_5_CORRECTION.md
e4aa9ef4f0de2fe705d54cb7ac016212098cfe71b8575ef2b435e8c9b09f5609  successor/OFFICINA_GENERIC_HARNESS_SUPERVISOR_CONTROL_CHANNEL_V2_1_6_CORRECTION.md
789732476938ca8c1436eebb49e54a1f994c2c000b7689e1eb9aad082f6871a8  successor/OFFICINA_GENERIC_HARNESS_SUPERVISOR_CONTROL_CHANNEL_V2_1_7_CORRECTION.md
33b0b91621439bdc42b4c41b3d00741b8c20d014a686097d2bc63c001db0ed50  successor/OFFICINA_GENERIC_HARNESS_SUPERVISOR_CONTROL_CHANNEL_V2_1_8_CORRECTION.md
1468c9ab1806c1eb25523e6a9fd8567592076f0dc74418ca698a52f933c7f3b0  successor/OFFICINA_GENERIC_HARNESS_SUPERVISOR_CONTROL_CHANNEL_V2_1_9_CORRECTION.md
2b4f9cad7be7a69527e828c73928a399209fcd8151780b9b4c839934893e0dc8  successor/OFFICINA_GENERIC_HARNESS_SUPERVISOR_CONTROL_CHANNEL_V2_1_10_CORRECTION.md
2d4d4b189e460605ce95f8f464d7ef1c6d0c8ce317ad26033a91b4d2c556759b  successor/OFFICINA_GENERIC_HARNESS_SUPERVISOR_CONTROL_CHANNEL_V2_1_10_1_CORRECTION.md
c7ff27775fd1b394b850be1be3e1d361d95f5e12af251949f8363980bd2900ec  successor/OFFICINA_GENERIC_HARNESS_SUPERVISOR_CONTROL_CHANNEL_V2_1_10_2_CORRECTION.md
02d862e76f76a57cd154ecfd8a67f88abb02c2ce324e4026e4145069cee63143  successor/OFFICINA_GENERIC_HARNESS_SUPERVISOR_CONTROL_CHANNEL_V2_1_10_3_CORRECTION.md
6197d2a4073d35fc978119db32128c50d12594343ac87731640a1d8e19f09e84  successor/OFFICINA_GENERIC_HARNESS_SUPERVISOR_CONTROL_CHANNEL_V2_1_10_4_P1_BINDING.md
798d0cbd51e93cc1f4c0a443785f90d90a2e121d35738189cbee9c61acf557cc  successor/OFFICINA_GENERIC_HARNESS_SUPERVISOR_CONTROL_CHANNEL_V2_1_10_5_P1_PRE_XY_REPAIR.md
8f806e33d85c00933871072dadda30110f18ea6bf34b5ebc388f23f8b067143e  successor/OFFICINA_GENERIC_HARNESS_SUPERVISOR_CONTROL_CHANNEL_V2_1_10_6_PRE_XY_REPAIR.md
66dc6fdc26d8b27f50e8de9603e8ac217492a13385c04822a1450a938495d51a  successor/OFFICINA_GENERIC_HARNESS_SUPERVISOR_CONTROL_CHANNEL_V2_1_10_7_PRE_XY_CONSISTENCY_REPAIR.md
d2975d19c553d9f9338bacff9d0a2af1855af45881e305a8706c110820896935  successor/OFFICINA_GENERIC_HARNESS_SUPERVISOR_CONTROL_CHANNEL_P1_OPERATIVE_COMPOSITE_V1.md
90ddf3ff76a1d08994c06d9c7f938e45f32fdeb46f58251ebb162bc96cf01680  successor/OFFICINA_GENERIC_HARNESS_SUPERVISOR_CONTROL_CHANNEL_P1_OPERATIVE_COMPOSITE_V1_1.md
2c857fa8ad7be1c861eb8cf561f396e7d2339403c7714abc7958745bf34e5d5d  successor/OFFICINA_GENERIC_HARNESS_SUPERVISOR_CONTROL_CHANNEL_P1_OPERATIVE_COMPOSITE_V1_2.md
b510a7b504ddc370529a7d968d362ccff332538d6bb493b387a2bc0ae4e9db54  successor/OFFICINA_GENERIC_HARNESS_SUPERVISOR_CONTROL_CHANNEL_P1_OPERATIVE_COMPOSITE_V1_3.md
380b87f0524ac06ef2fb0173c83b234c3eedc34344c3c61ed9415bd2c1a63858  successor/OFFICINA_GENERIC_HARNESS_WATCHDOG_FREEZE_AUTHORITY_AMENDMENT_V1_DRAFT.md
40a26dc1a7d2e6a8b9c122b7e09599a7b03470b0e98c86964bc4389ea4b0e5b3  reviews/opus5_officina_supervisor_p1_operative_composite_v1_1_closure.md
6ef98132990f8c686fa9678509bb07ba8259f3d6e4cbc483861edfc03ea8e3ef  successor/OFFICINA_SUPERVISOR_PROCESS_AUTHORITY_SELECTION_V1_SIGNATURE.md
c494ef8884948bd0e737373d2d57a3ab74bbd456db2c3463711c4405f2fdf86a  successor/OFFICINA_SUPERVISOR_AUTHOR_SELECTIONS_V1_SIGNATURE.md
4918a208bb94549ba3e7c38571265e723cc51a0a3394e291a62a85c333d864a6  successor/OFFICINA_SUPERVISOR_OUTPUT_CAPACITY_SELECTION_V1_SIGNATURE.md
8c47da352ef5954406964647a32e97939c404806bdf9b3d3ff5bc70866e6369a  successor/OFFICINA_GENERIC_HARNESS_SIGNATURE.md
64b8d3f63594b79a6abc767a032383c5704beaf09b32a1e0c58fdc444bb0af71  successor/OFFICINA_GENERIC_HARNESS_CONTRACT_V2_DRAFT.md
6bbaf4d17295a8a4d4fa0f42a9347707e4e2319ea5183163c756b94008764077  successor/OFFICINA_GENERIC_HARNESS_CONTRACT_V2_1_CORRECTION.md
624dfc9b34c8009ee4c1610bfff91f5cfceea128e84d850c3e90ffb1e7be9e2f  successor/OFFICINA_GENERIC_HARNESS_CONTRACT_V2_2_CORRECTION.md
b2288b0a9fb44d23c19d853aeb6d57edd4de888c6058af8001a379f9237d3154  successor/OFFICINA_GENERIC_HARNESS_CONTRACT_V2_3_CORRECTION.md
724d633a55668013b78058eed1c76e12e9bbaf487f71ea94b7a4568ea1ced8a0  successor/OFFICINA_GENERIC_HARNESS_CONTRACT_V2_3_1_CORRECTION.md
4afca93172a39cb8924b48285965a791707cec71330b2a8f81328961f92ec01a  successor/OFFICINA_BATCH_SETTLEMENT_CORE_AMENDMENT_V1_DRAFT.md
3ce629ed5afe567b5aba936906c114008df989acb1a946443a6ede1e31dca7de  successor/OFFICINA_BATCH_SETTLEMENT_CORE_AMENDMENT_V1_1_CORRECTION.md
b5a1523290b6b8417a7b3288329cc4a4e5ff80214c8f28e6ea1ae51a450a94c9  successor/OFFICINA_BATCH_SETTLEMENT_CORE_AMENDMENT_V1_1_1_CORRECTION.md
ae9c440acaaba90f2cb669e5a8212082f4c0f25b5b7e31ebc906b9cbc0ad6132  reviews/officina_supervisor_v2_1_authorship_note.md
70df01e8af25303600425434353a707571354e385fff78e1663f30494cf4b7ac  reviews/opus_officina_supervisor_p1_final_xy_review.md
75002efea91c3960adb5bc2bfa4dcdacecdb45a1add14f3f2fc1dd300e591b1b  reviews/sol_officina_supervisor_p1_final_xy_review.md
327b1bb222173407772836a2fdc4e92f89595508aff8b77f68f65816cafbec1e  src/philosophia/officina/verification.py
daeef9b3a349aba48b126957ff027d946b7ad094e5c03c3c2ede717f27a660e6  successor/officina/T_ENVELOPE.json
```

Every author closure accompanying the documents above is an untrusted
self-assessment and none is evidence for anything in this composite.

### Future edit surface

| Path | Permitted change | Status today |
|---|---|---|
| `scripts/officina_process_control_bootstrap.py` | the PCS and its protocol server | does not exist |
| `scripts/officina_role_bootstrap.py` | the four-role isolated entry | does not exist |
| `src/philosophia/officina/verification.py` | CHANGES 1 through 5 and rules `S-1` through `S-24b`, `G-1` through `G-9`, **`G-10`, `G-11` and the authoring discipline `AD-1`**, and nothing else. **The post-handoff verifier implementing `G-11` is expressly permitted and is REQUIRED by §P1-14.8 step 4; it is pinned as member `M5` of `G-11`'s closed input set, not by the provenance digest below** | present bytes are a **NON-ENFORCED PRE-INSTALL BASELINE** (see the provenance note) |
| `successor/officina/runtime_control/PRODUCTION_CALL_GRAPH.json` | five roots, the reachable closure, five root digests, and the four composite digest fields | does not exist |
| `src/philosophia/officina/generic_harness.py` | the launcher, the protocol client, the four role entries, removal of every subprocess, fork, wait, kill and group-kill call, and the eight single-install interface sites of §P1-13.7 | untracked work in progress, preserved unmodified |
| test modules | §P1-15 | untracked work in progress, preserved unmodified |
| everything else | no change | byte-unchanged |

<!-- OFFICINA-P1-PROVENANCE-END -->
