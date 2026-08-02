# Officina supervisor and control channel — P1 operative composite, version 1

**This document is the single, complete, self-contained and authoritative
operative specification of the Officina supervisor/control-channel architecture
under the signed selection
`I_SELECT_SUPERVISOR_PROCESS_AUTHORITY_P1_FULL_PCS_MEDIATION`.**

It is **not** a correction layer. It requires no reader or implementer to apply
any historical replacement index, and it cites no predecessor for any
executable rule. Every implementable value, sequence, table and rule appears
literally below.

## Authority hierarchy (exact, four levels)

1. **Author signatures remain the source of accepted choices.** The signed
   selections A3, B1, C1, D1, K1 (output capacity) and P1 (process authority)
   are the only source of *what* was chosen. This document may not change them.
2. **This composite is the sole operative specification of how those choices are
   implemented.** Where this document and any other document differ on an
   executable rule, **this document governs**.
3. **`OFFICINA_GENERIC_HARNESS_SUPERVISOR_CONTROL_CHANNEL_V1_DRAFT` through
   `…_V2_1_10_7_PRE_XY_CONSISTENCY_REPAIR` are immutable historical and
   provenance evidence only.** They are **not** scanned, parsed, or interpreted
   for operative behaviour by any implementer, verifier, or reviewer. Their
   contents are listed in §C15's non-normative provenance table by path and
   digest, and nowhere else.
4. **Any future change to this composite requires a new signed and reviewed
   version of this file.** No prose in any other document may override it, and
   no implicit supersession exists.

Status: `CANDIDATE_FOR_INDEPENDENT_X_AND_Y_REVIEW_NOT_ACCEPTED`.
`I_ACCEPT_OFFICINA_SUPERVISOR_CONTROL_CHANNEL_AMENDMENT` is **not signable** and
is not made signable by this document. This document creates nothing
executable, edits no file, starts no process, and authorizes no implementation.
T is `NOT_ACTIVATED`; the programme claim is `OPEN`.

**Authorship.** Written by **Claude Code Opus 5 acting only as the
specification author**. This line authored the historical chain and **cannot**
serve as its independent X or Y reviewer. Every author closure in the chain,
including this document's companion closure, is an untrusted self-assessment.

<!-- OFFICINA-P1-NORMATIVE-BEGIN -->

---

## §C1. Scope, threat model, and the signed choices

### §C1.1 Scope

This contract specifies the construction, authority, communication, failure and
termination of the Officina supervisor control plane: the process-control
server, the middle process, the supervisor, the watchdog, controllers and
workers, and the two channels that connect them. It specifies **no** scientific
procedure, **no** resource envelope, and **no** activation.

### §C1.2 Threat model

The contract defends against **accidental contamination and ordinary failure**
of the process it cannot control, and against **its own** ability to record
something false. It does **not** defend against a hostile actor at the same UID.

| Assumed hostile or contaminated | Assumed sound |
|---|---|
| the caller process, in any runtime state: threads, monkeypatched primitives, `.pth`/site customization, audit/import/trace hooks, at-fork callbacks, retained callables, native extensions | the Linux kernel of the pinned platform |
| any ancestor of the caller, including one that has set `PR_SET_CHILD_SUBREAPER` | the pinned CPython build's documented interfaces |
| the supervisor process after it imports the project package | the reviewed bytes of the production roots, established at deploy time |
| any same-UID process, which may signal, stop, kill, or (if it has adopted them) reap this contract's processes, and may create, replace or remove files this contract reads | the filesystem's atomicity primitives (`rename`, `O_EXCL`, `flock`) |

### §C1.3 The signed choices, in their operative meaning

**A3 — `I_SELECT_SUPERVISOR_CONFINEMENT_A3_SAME_UID_PROCEDURAL_RESCOPE`.**
Confinement of a same-UID actor is **procedural, not enforced**. This contract
asserts no same-UID confinement mechanism and invents none. `T_RUNTIME.lock`
and `SPAWN.lock` serialize *contract actors*; they are not filesystem or
process exclusion mechanisms. Every residual named in this document that
depends on a same-UID actor's forbearance is permanently **non-citable**:
forbidden from selection, Q, C, C1–C6, any blinding claim, and any scientific or
resource interpretation.

**B1 — `I_SELECT_SUPERVISOR_IDEMPOTENCY_B1_DURABLE_JOURNAL_ACK_REDELIVERY`.**
Effects are made exactly-once by a durable journal, an acknowledgement, and
retry-stable redelivery of a recorded reply. In this contract that discipline
applies to **two** journals: the client journal of the harness control plane,
and the process-control journal of §C7.6. **On the process-control channel the
byte record of a reply is redeliverable but a descriptor capability is never
re-sent** (§C7.6), which is an accepted narrowing of B1 on that channel and is
stated as such.

**C1 — `I_SELECT_SUPERVISOR_WATCHDOG_C1_DEDICATED_FREEZER`.** A dedicated
watchdog process witnesses and freezes; it holds no lock and no capability,
writes nothing under `runtime/`, appends no ledger, and settles nothing. Under
P1 the watchdog is created by the PCS as an isolated role, and **supervisor
death is detected by exactly one mechanism — update-pipe EOF.** The
direct-parent `getppid()` detector is **deliberately absent**. This is the
author's selected trade and is not a mechanically unchanged C1 implementation.

**D1 — `I_SELECT_SUPERVISOR_LIFETIME_D1_NO_IDLE_EXIT`.** No supervisor idle
exit exists. D1's ground is that **no supervisor ever waits on `SPAWN.lock`**,
so a running supervisor's lifetime never depends on any client. Under P1 the
availability model additionally depends on a **mandatory resident PCS whose
loss is an unrecoverable whole-generation invalidity with no adoption**
(§C10.4).

**K1 —
`I_SELECT_SUPERVISOR_OUTPUT_CAPACITY_K1_SUPERVISOR_MEDIATED_TRANSPORT_FIXED_CEILING`.**
Worker output crosses the supervisor with a fixed ceiling and one-write /
one-hash accounting, with no replenishment. The constants are §C2.3's. P1
changes **who creates the pipes**, not who mediates or accounts.

**P1 — `I_SELECT_SUPERVISOR_PROCESS_AUTHORITY_P1_FULL_PCS_MEDIATION`.** One
clean, constructed Process-Control Server holds the numeric identity of every
process it creates, and all numeric process authority for the middle process,
controllers, workers and every watchdog. The supervisor receives opaque handles only, cannot express a PID, and
calls `fork`, `Popen`, `waitpid`, `kill` and `killpg` on no path. Every watchdog
is a PCS-created isolated role. PCS loss is unrecoverable generation
invalidity; no new PCS may adopt a live generation.

---

## §C2. Platform, interpreter, and constants

### §C2.1 Supported platform — checked at run time, refused otherwise

```text
os.uname().sysname          == "Linux"
os.uname().machine          == "x86_64"
sys.implementation.name     == "cpython"
sys.version_info[:3]        == (3, 12, 3)
plus the exact reviewed build identity recorded in the implementation review
```

Any mismatch is a fail-closed refusal **before any fork, lock acquisition or
record install**. No other architecture is supported; MIPS, ARM64, i386, Alpha,
SPARC and every non-Linux system are refused at this check, before any signal
mask is parsed.

Inside this scope `_NSIG == 64`, so `/proc/<pid>/status` renders each signal
mask as exactly **16** hexadecimal digits, and a native `int` is **4 bytes,
little-endian**.

### §C2.2 Control-plane constants

```text
T_SUPERVISOR_POLL_INTERVAL_NS           =         50_000_000
T_CONTROL_FRAME_MAX_BYTES               =              4_096
T_CONTROL_READ_TIMEOUT_SECONDS          =                 10
T_CLIENT_REPLY_TIMEOUT_SECONDS          =                 30
T_SPAWN_LOCK_ACQUIRE_TIMEOUT_NS         =     30_000_000_000
T_SPAWN_IDENTITY_WAIT_TIMEOUT_NS        =     10_000_000_000
T_SPAWN_SELF_STOP_TIMEOUT_NS            =     10_000_000_000
T_SPAWN_BOOTSTRAP_MAX_AGE_NS            =     60_000_000_000
T_WATCHDOG_ACK_ABSENCE_TIMEOUT_NS       =     60_000_000_000
```

> **Resolved supersession, recorded because the delta chain hid it.**
> `T_SUPERVISOR_POLL_INTERVAL_NS` is **50_000_000**. An earlier draft value of
> `100_000_000` does not govern and appears nowhere in this contract.

### §C2.3 Output-capacity constants (K1, unmoved)

```text
T_OUTPUT_PER_STREAM_MAX_BYTES           =         67_108_864
T_OUTPUT_AGGREGATE_MAX_BYTES            =     34_359_738_368
T_OUTPUT_FS_SAFETY_MARGIN_BYTES         =      8_589_934_592
T_OUTPUT_COPY_CHUNK_BYTES               =          4_194_304
T_OUTPUT_PATH_MAX_BYTES                 =              1_024
T_OUTPUT_PATH_COMPONENT_MAX_BYTES       =                255
```

### §C2.4 Descriptor-index constants

```text
PCS process (created by the caller):
  T_PCB_FD_REQUEST_R    = 3     T_PCB_FD_PACKAGE_ROOT = 6
  T_PCB_FD_REPLY_W      = 4     T_PCB_FD_SOURCE       = 7
  T_PCB_FD_RUNTIME_ROOT = 5     T_PCB_FD_INTERPRETER  = 8

Role processes (created by the PCS, or by the grandchild for SUPERVISOR):
  slots 3 and 4 are role-class specific (§C5.2)
  T_ROLE_FD_ROLESRC = 5   T_ROLE_FD_SELF  = 7   T_ROLE_FD_INTERP  = 9
  slot 6 is role-class specific  T_ROLE_FD_SRCDIR = 8   T_ROLE_FD_PKGROOT = 10

Controller and worker control descriptors, unchanged from the signed adapter:
  T_CTRL_FD_LOW  = 3            T_CTRL_FD_HIGH = 4
```

### §C2.5 Signal numbers — integer literals, not module constants

```text
SIGKILL = 9   SIGTERM = 15   SIGCONT = 18   SIGSTOP = 19   SIGNAL_0 = 0
```

`signal.SIGCHLD` is the **only** symbolic signal name used anywhere, because
`SIGCHLD`'s number is not uniform across Linux architectures while the five
above are pinned by §C2.1's platform.

### §C2.6 Closed failure-token set

Every refusal in this contract carries exactly one of these tokens. The set is
closed; no other token exists, and no token is composed at run time.

```text
Pre-fork / construction:
  PLATFORM_UNSUPPORTED        INTERPRETER_UNSUPPORTED     ISOLATION_NOT_PINNED
  TOPOLOGY_MULTITASK          INHERITED_CHILD             FD_TOPOLOGY
  SIGNAL_MASK_INHERITED       MASK_MALFORMED              PRIMITIVE_NOT_GENUINE
  LOCK_FD_NOT_CLOEXEC         SOURCE_FD_UNUSABLE          SOURCE_NOT_REGULAR
  SOURCE_WRITABLE             SOURCE_NOT_READONLY         ROOT_CANONICAL_UNREADABLE
  ROOT_SOURCE_MISMATCH        ROLE_SOURCE_UNREADABLE      ROLE_PATH_UNREADABLE
  CHDIR_FAILED                REQUEST_MALFORMED           REQUEST_TRUNCATED
  GRANDCHILD_FD_HOIST_FAILED  GRANDCHILD_FD_NOT_INHERITABLE
Launcher (caller side):
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

`REFUSED` and `BLOCKED` are the two outcome words of the caller reply; `INVALID`
is the third protocol status. No other outcome word exists.

---

## §C3. Production roots, imports, and primitive identity

### §C3.1 The five production roots

```text
scripts/officina_activate_t.py
scripts/verify_officina_active.py
src/philosophia/officina/generic_harness.py
scripts/officina_process_control_bootstrap.py       # the PCS
scripts/officina_role_bootstrap.py                  # the four-role entry
```

### §C3.2 Import allowlists

```text
ALLOWED_ABSOLUTE_IMPORTS (global default, 19 members):
  __future__ ast dataclasses datetime enum fcntl hashlib hmac json os pathlib
  re subprocess time typing weakref sys _signal _socket

MODULE_SCOPED_ABSOLUTE_IMPORTS (a file with an entry gets EXACTLY that entry,
never the union with the default):
  scripts/officina_process_control_bootstrap.py -> {os, sys, _signal, time,
                                                   fcntl, _socket}      (6)
  scripts/officina_role_bootstrap.py            -> {os, sys, fcntl}     (3)
  src/philosophia/officina/generic_harness.py   -> the sixteen original
        members {__future__, ast, dataclasses, datetime, enum, fcntl, hashlib,
        hmac, json, os, pathlib, re, subprocess, time, typing, weakref}
        plus {_socket}                                                  (17)
```

`signal` (the Python wrapper) is **never** permitted anywhere: it is a
pure-Python module whose import closure pulls `functools` and hence `_thread`.
`_signal` is the built-in C module and is used instead. `sys` and `_signal`
are permitted **only** in a file with a scoped entry. `threading`, `_thread`,
`multiprocessing`, `concurrent`, `asyncio`, `ctypes`, `select`, `selectors`,
`socket`, `array`, `struct`, `atexit`, `gc` and `prctl` are permitted nowhere.

### §C3.3 The PCS import closure, audited

| Module | Kind | Transitive Python closure at import | Starts a task? | Registers an at-fork callback? | Installs a handler or hook? |
|---|---|---|---|---|---|
| `os` | Python wrapper over built-in `posix` | `sys`, `abc`, `stat`, `_collections_abc`, `posixpath`, `genericpath` | no | defines `register_at_fork`, never calls it | no |
| `sys` | built-in | none | no | no | no |
| `_signal` | built-in | none | no | no | no |
| `time` | built-in | none | no | no | no |
| `fcntl` | built-in | none | no | no | no |
| `_socket` | built-in | none | no | no | no |

Disclosure: `_socket.socket` objects carry a finalizer that closes the
descriptor. Two rules contain it: every socket object lives in a module-level
slot for the generation's life, and **every received descriptor is handled as a
plain `int`**, closed once with the bound close primitive and never wrapped in a
socket object.

### §C3.4 Primitive binding

Immediately after the imports, at module scope, before any other statement:

```text
_BUILTIN = type(len)                      # the type anchor; len is never called

_fork _waitpid _kill _killpg _getpid _getppid _open _read _write _close
_fstat _stat _listdir _unlink _fsync _rename _pipe2 _dup2 _dup _execve
_setsid _exit_ _uname _chdir _get_inheritable _posix_spawn        from os
_flock _fcntl                                                     from fcntl
_clock                                                            from time
_sigsignal _getsignal                                             from _signal
_socketpair _CMSG_SPACE _CMSG_LEN                                 from _socket
_sendmsg _recvmsg                            from the _socket.socket type

integer constants: _SIGCHLD _SIG_DFL _WNOHANG _O_RDONLY _O_WRONLY _O_RDWR
  _O_CREAT _O_EXCL _O_DIRECTORY _O_NOFOLLOW _O_CLOEXEC _O_NONBLOCK _LOCK_EX
  _LOCK_NB _F_GETFL _F_GETFD _O_ACCMODE _FD_CLOEXEC _AF_UNIX _SOCK_SEQPACKET
  _SOL_SOCKET _SCM_RIGHTS _MSG_CMSG_CLOEXEC _MSG_CTRUNC _MSG_TRUNC
  _POSIX_SPAWN_OPEN _POSIX_SPAWN_CLOSE _POSIX_SPAWN_DUP2
string constant: _devnull
value objects: _flags _version_info _implementation                from sys
```

### §C3.5 Primitive identity validation — four kinds, no universal predicate

Executed once, immediately after the binding. **There is no single universal
predicate**: a uniform `builtin_function_or_method` test would reject a genuine
pure-Python wrapper, so each kind has its own rule.

| Kind | Members | Requirements |
|---|---|---|
| module built-in callable | every `os`/`fcntl`/`time`/`_signal`/`_socket` function above | `type(f) is _BUILTIN`; `getattr(f, "__self__", None)` is not `None`; `f.__self__.__name__` is the expected module name (`"posix"`, `"fcntl"`, `"time"`, `"_signal"`, `"_socket"`); `f.__qualname__` is the exact bare name (`_exit_` expects `"_exit"`) |
| method descriptor | `_sendmsg`, `_recvmsg` | a method descriptor whose `__objclass__` is `_socket.socket` and whose `__qualname__` is `"socket.sendmsg"` / `"socket.recvmsg"` |
| integer constant | every constant above | `type(x) is int`; `_SIGCHLD == 17`; `_SIG_DFL == 0`; `_F_GETFL == 3`; `_O_ACCMODE == 3`; `_O_RDONLY == 0`; `{_POSIX_SPAWN_OPEN, _POSIX_SPAWN_CLOSE, _POSIX_SPAWN_DUP2} == {0, 1, 2}` and pairwise distinct; every other constant equals the value recorded in the implementation review |
| string constant | `_devnull` | `type(x) is str`; `== "/dev/null"` |

`_flags`, `_version_info` and `_implementation` are consumed only by §C6.2's
field comparisons; no identity claim is made about the container objects.

Any failure is `PRIMITIVE_NOT_GENUINE`: fail-closed refusal, **no fork, no lock
acquisition, no record installed**.

### §C3.6 No rebinding, no indirection

Every later use goes through the local `_name`. The module names `os`, `sys`,
`_signal`, `time`, `fcntl`, `_socket` appear as an attribute value **only**
inside the binding block. Each `_name` is assigned exactly once at module
scope and never appears as an `AugAssign` target, a `del` target, a parameter, a
comprehension target, an `as` target, or a `setattr` argument. `getattr`,
`setattr`, `delattr`, `vars`, `globals`, `locals`, `eval`, `exec`, `compile`,
`__import__`, `importlib`, subscripted call targets, and calls to non-`Name`
expressions are forbidden.

---

## §C4. Process topology and authority

### §C4.1 The process tree

```text
[0] caller — generic_harness.py __main__, ANY runtime state, assumed contaminated
     │ os.posix_spawn, §C6.1
     ▼
[1] PCS — scripts/officina_process_control_bootstrap.py, -I -S -E -P, env {}
     │   owns SPAWN.lock, the four singleton records, the four bootstrap
     │   channels, the supervisor socket, the handle table, the PCS journal,
     │   and every PID it creates
     ├─ fork at c4 ─▶ [2] middle (pid_mid)
     │                    └─ fork at m7 ─▶ [3] grandchild ─ execve ─▶
     │                                        [3'] role bootstrap: SUPERVISOR
     │                    └─ _exit(0) at m9 ; [3'] is then orphaned
     ├─ posix_spawn ─▶ [4] role bootstrap: WATCHDOG            setsid = False
     ├─ posix_spawn ─▶ [5] role bootstrap: CONTROLLER × n      setsid = True
     └─ posix_spawn ─▶ [6] role bootstrap: WORKER × n          setsid = True
```

### §C4.2 Orphan adoption — exact semantics

When a process is orphaned it is re-parented to the **nearest still-living
ancestor subreaper** — a process that has set `PR_SET_CHILD_SUBREAPER` — and to
the PID namespace's init process **only if no such ancestor exists**. That
adopting process, whichever it is, is the one that may reap it, `getppid()` in
the orphan returns the adopter, and the adopter receives `SIGCHLD`.

**This contract sets `PR_SET_CHILD_SUBREAPER` nowhere and observes no adopter.**
Its own abstention proves nothing about its ancestors: the caller, or any
process above it, may already be a subreaper. **No rule in this document
depends on which process adopts an orphan.**

### §C4.3 Dynamic parent / adopter / wait / authority table

`A*` denotes an arbitrary higher ancestor of the caller. Adoption applies **iff**
that process is the nearest living ancestor subreaper at that moment.

| Process | Initial direct children | Initial wait-set | Dynamically adopted | Wait-set after adoption | Officina authority |
|---|---|---|---|---|---|
| `A*` | host-given | its own children | the supervisor after `m9`; after PCS death `pid_mid`, controllers, workers, watchdogs | its own children **∪** adopted; wildcard waits range over the union | **none** |
| caller | the PCS | the PCS | the same set, if it is the nearer living subreaper | the PCS **∪** adopted; wildcard waits range over the union | none beyond §C6.1's launch and the four-step pipe exchange |
| **PCS** | `pid_mid`, controllers, workers, watchdogs | exactly those | nothing — it sets no subreaper attribute, and its descendants are orphaned only when it is already dead | unchanged | **full**: sole holder of numeric process authority |
| middle (`pid_mid`) | the grandchild until `m9` | **nothing** — it never waits | nothing | nothing | none |
| **supervisor** | **none** | nothing — a wildcard wait returns `ECHILD` | nothing | nothing | **opaque handles only, never a PID** |
| watchdog | none | nothing | nothing | nothing | none |
| controller / worker | per §C8.1 | unchanged | nothing | unchanged | none |

**Wildcard waits of an adopter range over its adopted direct children.** This is
stated affirmatively; nothing in this contract prevents it.

### §C4.4 What adoption adds, exactly

A same-UID actor may already signal, stop or kill any process of this contract
**without** adopting anything (§C1.2, A3). Adoption therefore adds exactly two
powers:

1. **reaper status** — the adopter may reap the adopted process, including by
   wildcard wait, thereby observing its wait status and controlling when the
   zombie clears;
2. **`getppid()` visibility** — `getppid()` in the adopted process returns the
   adopter. **No rule in this contract reads `getppid()` in any process**, so
   this confers nothing.

Adoption adds **no** signalling power, **no** descriptor or capability (reaping
conveys none), and **no** Officina handle, opcode, journal or control-plane
participation.

### §C4.5 Death proofs, by target

| Target | Proof |
|---|---|
| `pid_mid`, any controller, worker, watchdog | the PCS's own targeted `os.waitpid(pid, WNOHANG)` returning that pid (§C9.2). **Only a returned pid proves death.** |
| the supervisor | **never by wait.** Loss is observed by `t-pcs.v1` channel EOF. Where a route requires a death proof for the supervisor's group, it uses `/proc` absence, or state `Z` with a matching start identity, or live-with-a-different-start-identity (which means **not live**, and **never kill**) |
| any recorded process at a later attempt's preflight | the same three `/proc` predicates |

**No proof anywhere consumes an orphan's reaped status or exit code.**

### §C4.6 The group anchor

The process-group id used by the post-`c11` `killpg` route is `pid_mid`'s pid.
`pid_mid` is a **direct child of the PCS** and is therefore never orphaned while
the PCS lives, so adoption semantics cannot touch the anchor. If the PCS dies,
`pid_mid` is orphaned — but the generation is by then unrecoverable invalidity
(§C10.4) and no `killpg` decision is taken.

---

## §C5. Descriptors

### §C5.1 PCS-side descriptor table

| Name | Number | Contents | `FD_CLOEXEC` | Closed when |
|---|---|---|---|---|
| `T_PCB_FD_REQUEST_R` | 3 | caller request pipe, read end | **clear** | after the caller reply is written |
| `T_PCB_FD_REPLY_W` | 4 | caller reply pipe, write end | **clear** | same |
| `T_PCB_FD_RUNTIME_ROOT` | 5 | runtime root directory | **clear** | PCS exit |
| `T_PCB_FD_PACKAGE_ROOT` | 6 | package root directory | **clear** | PCS exit |
| `T_PCB_FD_SOURCE` | 7 | the PCS's own source object | **clear** | PCS exit |
| `T_PCB_FD_INTERPRETER` | 8 | the interpreter object | **clear** | PCS exit |
| `lock_fd` | kernel-chosen | `SPAWN.lock`, held under `flock(LOCK_EX)` | **SET** | at `c18` or PCS exit |
| `sv_sock` | kernel-chosen | supervisor `SOCK_SEQPACKET` PCS end | set | at shutdown or PCS exit |
| `journal_fd` | kernel-chosen | the `t-pcs.v1` journal | set | PCS exit |
| per handle | kernel-chosen | the **role-side** ends the PCS retains | set | when the handle reaches `REAPED` |
| opened under fd 6 | kernel-chosen | role-bootstrap source, `generic_harness.py` source, `src` directory | set | PCS exit |

Descriptors 3–8 have `FD_CLOEXEC` **clear** because `POSIX_SPAWN_DUP2` cleared
it on each destination. **Every other PCS descriptor is `CLOEXEC` by
construction**: `_open(..., _O_CLOEXEC)`, `_pipe2(_O_CLOEXEC)`, `_socketpair`
(CPython creates sockets non-inheritable), and `_dup` (returns a non-inheritable
descriptor).

### §C5.2 Role-side descriptor maps

| Slot | `SUPERVISOR` | `WATCHDOG` | `CONTROLLER` / `WORKER` |
|---|---|---|---|
| 3 | `SPAWN.lock`, retained | watchdog update **read** | ctrl request read (`T_CTRL_FD_LOW`) |
| 4 | `boot` write end | watchdog ack **write** | ctrl reply write (`T_CTRL_FD_HIGH`) |
| 5 | `generic_harness.py` source object | same | same |
| 6 | the `SOCK_SEQPACKET` peer | **unused; explicitly closed** | status write end |
| 7 | role-bootstrap source object | same | same |
| 8 | the object-bound `src` directory | same | same |
| 9 | the interpreter object | same | same |
| 10 | the package-root directory | same | same |

Post-`execve` a role's `/proc/self/fd` is exactly `{0,1,2}` ∪ its slot set.

**Descriptors the supervisor receives over `SCM_RIGHTS` are not in any pinned
numeric set.** They arrive at kernel-chosen numbers with `FD_CLOEXEC` already
set, and the supervisor records them in its handle→fd table. **The supervisor's
legitimate descriptor set therefore grows with every live handle**, which is why
no rule anywhere sweeps it (§C5.5).

### §C5.3 The hoist, for any target set

```text
HOIST(logical_fds, target_set):
  let T := max(target_set)
  for each logical fd L, in a fixed order:
      while h[L] <= T:  n := _dup(h[L]); retain the old; h[L] := n
  close every retained intermediate and every original whose number is <= T
  POSTCONDITION: every h[L] > T and the values are pairwise distinct
    violated ⇒ LAUNCH_FD_HOIST_FAILED (caller) or
               GRANDCHILD_FD_HOIST_FAILED (grandchild); no spawn, no exec
```

### §C5.4 File actions, for every `posix_spawn`ed role

```text
FILE_ACTIONS := [ (DUP2, h[slot], slot)  for slot in ascending slot order ]
              + [ (CLOSE, h[slot])       for slot in the same order ]
              + [ (CLOSE, d)             for every destination number in 3..10
                                          the role does NOT use ]
For WATCHDOG the last group is exactly {6}; for CONTROLLER and WORKER it is
empty. NO file action ever names lock_fd.
```

**Leak proof.** After any `posix_spawn`ed role's `execve` its descriptor set is
exactly `{0,1,2}` ∪ its slot set, because: (i) every PCS descriptor other than
3–8 is `CLOEXEC` and is closed by the `execve` — including `lock_fd`, `sv_sock`,
`journal_fd`, every per-handle end and every object opened under fd 6;
(ii) descriptors 3–8 have `FD_CLOEXEC` clear but all lie in `3..10`, so each is
either overwritten by a `DUP2` or named by an explicit `CLOSE`; (iii) hoisted
duplicates come from `_dup`, are non-inheritable, and are additionally closed by
explicit actions. **No role other than the supervisor ever holds a `SPAWN.lock`
reference.** The role's own `/proc/self/fd` check (§C6.4 step A-5) is a
**verification of this property, not the mechanism by which it holds**, and no
production path may depend on a post-`exec` refusal.

### §C5.5 `/proc/self/fd` — the complete phase and permission table

| Root | Phase | Enumerate | May close | Rule |
|---|---|---|---|---|
| PCS | `P-f`, pre-fork preflight | **yes** | **no — read-only** | require exactly `{0,1,2,3,4,5,6,7,8}` plus the transient listing descriptor; deviation ⇒ `FD_TOPOLOGY`, no fork |
| role bootstrap | `A-5`, before any project import | **yes** | **no — read-only** | require exactly `{0,1,2}` ∪ the role's slot set; deviation ⇒ `os._exit(3)`, nothing written |
| grandchild | `G-5`, after `G-4` and before `G-6`'s `execve` | **yes** | **yes, bounded** | close every inherited descriptor **not** in `{0,1,2}` ∪ slots `3..10`; ascending, once each, `EBADF` tolerated |
| supervisor | the `SCM_RIGHTS` receive path and its error path | **no** | **no** | cleanup is §C7.7's parser-local rule only |
| supervisor | any runtime remediation, handle-release, or shutdown step | **no** | **no** | forbidden |
| any root | any phase in which unrelated live role handles coexist | **no** | **no** | forbidden |
| PCS | any phase after the first role handle exists | **no** | **no** | forbidden — `P-f` is pre-fork and is the PCS's only enumeration |

**`G-5` cannot touch a live supervisor handle.** It executes in the grandchild
before `G-6`'s `execve`, therefore before the project import and before the role
entry: at that instant the process is not the supervisor, no `SCM_RIGHTS`
descriptor can exist in it, and it acts only on its own inherited descriptor
table. `P-f` is likewise before the PCS's first fork, therefore before any role
or handle exists. The two enumerating-and-closing phases and the set of live
role handles are temporally and structurally disjoint.

---

## §C6. Construction sequences

### §C6.1 The caller launch

The caller is assumed contaminated. Its entire permitted interaction is:

```text
L-0. bind and identity-check every launcher primitive by §C3.5's rules
       failure ⇒ LAUNCH_PRIMITIVE_NOT_GENUINE ⇒ NO SPAWN
     validate {_POSIX_SPAWN_OPEN, _POSIX_SPAWN_CLOSE, _POSIX_SPAWN_DUP2}
       == {0,1,2} and pairwise distinct
       failure ⇒ LAUNCH_CONSTANT_MISMATCH ⇒ NO SPAWN
L-1. create two anonymous pipes with _pipe2(_O_CLOEXEC): request and reply.
     open the runtime root and the package root with
       _O_RDONLY|_O_DIRECTORY|_O_CLOEXEC
     open the bootstrap source with _O_RDONLY|_O_NOFOLLOW|_O_CLOEXEC
     open the interpreter with _O_RDONLY|_O_CLOEXEC
     Its pathname is used for nothing else and is never readlink'ed.
L-2. HOIST the six descriptors to a target set of {3,4,5,6,7,8}; then

     _posix_spawn(
        b"/proc/self/fd/8",                       # object-bound interpreter
        [ b"/proc/self/fd/8", b"-I", b"-S", b"-E", b"-P",
          b"/proc/self/fd/7" ],                   # object-bound source; no argv
                                                  # parameter follows
        {},                                       # EXACTLY the empty environment
        file_actions = the twelve entries of §C5.4 for the target set,
        setsigmask   = () )
     setpgroup, resetids, setsid, scheduler and setsigdef are NOT passed.
     r is not an int, or r <= 0        ⇒ LAUNCH_STRUCTURAL
     OSError                           ⇒ LAUNCH_SPAWN_FAILED
     any other BaseException           ⇒ LAUNCH_STRUCTURAL
     then close every hoisted duplicate and every original the caller still
     holds for the six roles.
L-3. write EXACTLY ONE canonical request line on the request pipe; close the
     request write end.
L-4. read the reply pipe to EOF; parse exactly one canonical reply line; close
     the reply read end.

FORBIDDEN to the caller, normatively:
  sending ANY signal to the PCS, ever, for any reason;
  relying on the PCS's exit status for any decision;
  performing any wait whose result changes a decision;
  using subprocess, Popen, os.fork, os.system, preexec_fn, a shell, or any
  mutable high-level wrapper on the launch path.
```

`/proc/self/fd/<N>` names the **object** the descriptor refers to; the kernel
does not re-walk the original path, so the interpreter and source cannot be
replaced between the caller's open and the exec. `readlink` is used nowhere,
and `sys.executable` is used for nothing.

> **The launcher property.** For any caller, in any runtime state: either it
> constructs **exactly** the process of `L-2`, or **no authorized PCS comes into
> existence.** The launcher's own identity checks are **diagnostic, not the
> safety mechanism** — a fully hostile caller can defeat them, which is why the
> property is a disjunction. All load-bearing safety is the PCS's own preflight,
> executed where the caller cannot reach. A caller that launches a *different*
> program creates no authority: that program is not this contract's PCS and can
> do only what the caller could already do.

Why each isolation flag: `-S` prevents `site`, so no `.pth` executable line,
`sitecustomize` or `usercustomize` runs; `-I` removes user site-packages and the
script directory from `sys.path` and implies `-E` and `-s`; `-E` ignores every
`PYTHON*` variable; `-P` prevents prepending a path to `sys.path`.

### §C6.2 The PCS preflight

Executed after the six imports, the binding block and §C3.5's identity check,
and before any name is opened.

```text
P-cwd. _chdir("/")                                  OSError ⇒ CHDIR_FAILED
       Every later filesystem operation is dir_fd-relative to fd 5 or fd 6, on
       an already-open descriptor, or an absolute /proc name, so the inherited
       cwd is irrelevant; this is defence in depth.
P-a.   u := _uname(); require sysname == "Linux" and machine == "x86_64"
                                                    else PLATFORM_UNSUPPORTED
P-b.   require _implementation.name == "cpython"
       require _version_info[:3] == (3, 12, 3)      else INTERPRETER_UNSUPPORTED
       require _flags.isolated, _flags.no_site, _flags.ignore_environment,
               _flags.safe_path, _flags.no_user_site  all truthy
                                                    else ISOLATION_NOT_PINNED
       This is a readback of EFFECT from the interpreter, never of argv. argv is
       read nowhere in the PCS and is evidence of nothing.
P-c.   _listdir("/proc/self/task") == exactly [str(_getpid())]
                                                    else TOPOLOGY_MULTITASK
P-d.   /proc/self/status "Threads:" == "1"          else TOPOLOGY_MULTITASK
P-e.   the ONE permitted wildcard wait in this contract, at exactly this place,
       before any fork:  _waitpid(-1, _WNOHANG)
         raises OSError ECHILD ⇒ correct: this process has no children
         returns any value     ⇒ INHERITED_CHILD  (the call has reaped an
                                  inherited child; the route refuses precisely
                                  because it must not proceed in a process it
                                  does not understand)
         any other error       ⇒ INHERITED_CHILD
P-f.   descriptor preflight: _fstat fds 3..8; 3 and 4 are S_ISFIFO, 5 and 6 are
       S_ISDIR, 7 and 8 are S_ISREG and neither group- nor other-writable;
       _fcntl(7, _F_GETFL) & _O_ACCMODE == _O_RDONLY and the same for 8;
       _get_inheritable is true for exactly 3..8; and /proc/self/fd contains
       exactly {0,1,2,3,4,5,6,7,8} plus the transient listing descriptor
                                                    else FD_TOPOLOGY,
                                                         SOURCE_NOT_REGULAR,
                                                         SOURCE_WRITABLE, or
                                                         SOURCE_NOT_READONLY
       record SOURCE_IDENTITY := (st_dev, st_ino) of fd 7
       record INTERPRETER_IDENTITY := (st_dev, st_ino) of fd 8
P-g.   SIGNAL STATE:
       g-1. read /proc/self/status in full; parse SigIgn, SigCgt, SigBlk and
            Threads under §C6.3's mask grammar
       g-2. require SigBlk == 0                     else SIGNAL_MASK_INHERITED
       g-3. RESET PASS: for each bit index i set in SigCgt, ascending,
            n := i + 1 ; _sigsignal(n, _SIG_DFL)
              ValueError / RuntimeError / OSError / anything else
                                                    ⇒ NORMALIZE_INCONCLUSIVE
            The signal numbers come from the kernel's own mask; no additional
            _signal member is used. SIGKILL and SIGSTOP can never carry a
            SigCgt bit; if one appears, _sigsignal raises and the route refuses.
       g-4. _sigsignal(_SIGCHLD, _SIG_DFL), unconditionally. This one call is a
            full sigaction replacement: sa_handler = SIG_DFL, an empty mask, and
            sa_flags containing neither SA_NOCLDWAIT nor SA_NOCLDSTOP. It
            therefore clears BOTH an inherited SIG_IGN and an inherited
            SA_NOCLDWAIT, whatever their provenance — exec preserves SIG_IGN
            while clearing sa_flags, and fork-without-exec inherits both.
       g-5. re-read /proc/self/status; require SigCgt == 0; require the SIGCHLD
            bit clear in SigIgn; require SigIgn otherwise unchanged from g-1
            except that the SIGCHLD bit may have gone from 1 to 0; require
            Threads == 1
       g-6. re-list /proc/self/task; require exactly one entry == str(_getpid())
       g-7. require type(_getsignal(_SIGCHLD)) is int and
            _getsignal(_SIGCHLD) == _SIG_DFL        (corroboration only)
       Consequences, stated: CPython's SIGPIPE = SIG_IGN is preserved, because
       an ignored signal carries no SigCgt bit and g-5 proves no ignored
       disposition moved. CPython's SIGINT handler is removed, so a delivered
       SIGINT terminates the PCS by default action; for a lock-holding process
       this is safer, and the reset is never undone.
P-h.   read fd 3 to EOF; validate the request against §C7.2's grammar
                                     else REQUEST_MALFORMED / REQUEST_TRUNCATED
P-p.   PACKAGE-ROOT BINDING:
       p-1. self_fd := _open("scripts/officina_process_control_bootstrap.py",
                             _O_RDONLY|_O_NOFOLLOW|_O_CLOEXEC, dir_fd = 6)
                                     any OSError ⇒ ROOT_CANONICAL_UNREADABLE
       p-2. require (st_dev, st_ino) of self_fd == SOURCE_IDENTITY
                                     mismatch    ⇒ ROOT_SOURCE_MISMATCH
       p-3. close self_fd
       p-4. role_fd := _open("src/philosophia/officina/generic_harness.py",
                             _O_RDONLY|_O_NOFOLLOW|_O_CLOEXEC, dir_fd = 6)
                                     any OSError ⇒ ROLE_SOURCE_UNREADABLE
       p-5. require S_ISREG and not group/other writable; record ROLE_IDENTITY
       p-6. rb_fd := _open("scripts/officina_role_bootstrap.py",
                           _O_RDONLY|_O_NOFOLLOW|_O_CLOEXEC, dir_fd = 6)
       p-7. src_dir_fd := _open("src", _O_RDONLY|_O_DIRECTORY|_O_CLOEXEC,
                                dir_fd = 6)
                                     any OSError ⇒ ROLE_PATH_UNREADABLE

Only after every step above may c1 acquire SPAWN.lock.
```

**Every non-`OK` result of `P-cwd` through `P-p` takes the same body:** perform
no fork; close the bootstrap ends; remove nothing (no record of this attempt
exists yet); write the reply of §C7.2 with the corresponding failure token if
fd 4 is usable; and exit.

### §C6.3 The signal-mask grammar

Applied to `SigIgn`, `SigCgt` and `SigBlk`, **before** any integer conversion.

```text
M-1. split /proc/self/status on b"\n"
M-2. select every line beginning exactly with the field name + b":"
       zero such lines, or two or more            ⇒ MASK_MALFORMED
M-3. after the colon: one or more space or tab bytes, then a maximal run of
     hexadecimal digits, then end of line
       empty run; a byte outside [0-9a-fA-F] in the run; a "0x"/"0X" prefix; a
       sign; internal whitespace; any trailing non-newline byte
                                                  ⇒ MASK_MALFORMED
M-4. let d be the number of hexadecimal digits. Require BOTH:
       4 * d >= int(_SIGCHLD)          architecture-independent minimum
       d == 16                         the pinned platform's exact width
       either failing                              ⇒ MASK_MALFORMED
M-5. value := int(digit_run, 16)                   ONLY now is conversion legal
```

Worked cases: an empty value, `0`, `0000` and a 13-digit value all fail; a
20-digit value fails as an unreviewed rendering; a 16-digit value with leading
zeros is the expected form and passes. `signal.NSIG` is used nowhere and no
architecture is silently added.

### §C6.4 The role bootstrap

`scripts/officina_role_bootstrap.py` is the executable root of all four roles.
It imports exactly `os`, `sys`, `fcntl` — **three** modules — because step `A-6`
performs the `F_GETFL` access-mode test. Its argv:

```text
argv[0]  "/proc/self/fd/9"                  the object-bound interpreter
argv[1..4]  "-I" "-S" "-E" "-P"
argv[5]  "/proc/self/fd/7"                  the object-bound role source
argv[6]  "--officina-role"
argv[7]  SUPERVISOR | WATCHDOG | CONTROLLER | WORKER
argv[8]  "--officina-generation"     argv[9]  <64 lowercase hex>
argv[10] "--officina-fdmap"          argv[11] a fixed comma-separated decimal
                                              list determined solely by argv[7]
for CONTROLLER and WORKER only, the fixed target-argv tail
env = {} exactly — PYTHONPATH is used nowhere in this contract
```

Refusal order, executed exactly in this sequence; any failure is `os._exit(3)`
with nothing written, nothing unlinked, and no descriptor closed except its own:

```text
A-1  bind and identity-check every primitive by §C3.5's rules
A-2  read back sys.flags: isolated, no_site, ignore_environment, safe_path,
     no_user_site all true
A-3  os.environ must be EMPTY
A-4  argv must match the fixed shape above; argv[7] one of the four literals
A-5  fstat every fd named in argv[11]; each has the type its slot requires;
     /proc/self/fd contains exactly {0,1,2} ∪ the slot set          (read-only)
A-6  fstat T_ROLE_FD_SELF: a regular file, not group- or other-writable, and
     _fcntl(fd, _F_GETFL) & _O_ACCMODE == _O_RDONLY
A-7  open the canonical role-bootstrap path under T_ROLE_FD_PKGROOT with
     _O_NOFOLLOW|_O_RDONLY and require (st_dev, st_ino) == T_ROLE_FD_SELF's
A-8  fstat T_ROLE_FD_SRCDIR; require a directory
A-9  sys.path[:] = ["/proc/self/fd/<T_ROLE_FD_SRCDIR>"]
     The ENTIRE path is replaced by exactly one object-bound entry: no append,
     no insert into an existing list, and no environment involvement.
A-10 import philosophia.officina.generic_harness                the ONLY import
A-11 fstat the imported module's __file__ and require
     (st_dev, st_ino) == T_ROLE_FD_ROLESRC's
A-12 for CONTROLLER and WORKER only: verify the fixed target-argv index layout,
     the per-role descriptor order, and the target preflight; then self-stop
     with os.kill(os.getpid(), 19) before any target behaviour
A-13 call exactly one pinned entry function, selected by argv[7] from a closed
     four-entry mapping, with the validated descriptors
```

**Role isolation, by class.** `SUPERVISOR` and `WATCHDOG` are fully isolated:
after `A-9` their `sys.path` is exactly the object-bound `src` directory, and
they import only the project package, which is stdlib-only. `CONTROLLER` and
`WORKER` are **not** fully isolated by design, because their target program is
client-supplied. That is safe, and here is the proof:

| Vector | Why a contaminated controller or worker cannot affect it |
|---|---|
| process | it holds **no PID authority**: the PCS created it, is its parent, and is its only reaper; it can name no PID and can signal, wait for or reap nothing |
| lock | it never receives the `SPAWN.lock` descriptor (§C5.2, §C5.4) |
| capacity | the K1 ceiling is installed before it runs and enforced on the supervisor-mediated output path with one-write / one-hash accounting |
| custody | the complete-custody proof and the object-bound observation with both revalidation barriers are performed by the supervisor under `T_RUNTIME.lock`, over objects the worker cannot make the supervisor mis-observe |
| scientific validity | a result reaches science only through a durable settlement bound by hash to a result manifest; a malformed or absent object is malformed-dominant or absent, never a result |
| residual | a worker that consumes wall-clock or writes garbage produces invalidity or a quarantined output — both infrastructure facts, neither a scientific outcome |

### §C6.5 The bootstrap sequence `c1`–`c18` and `m0`–`m9`

```text
PCS side:
 c1.  lock_fd := _open("SPAWN.lock", _O_RDWR|_O_CREAT|_O_CLOEXEC, 0o600,
                       dir_fd = T_PCB_FD_RUNTIME_ROOT)
      _flock(lock_fd, _LOCK_EX|_LOCK_NB), retried at
      T_SUPERVISOR_POLL_INTERVAL_NS until T_SPAWN_LOCK_ACQUIRE_TIMEOUT_NS; on
      expiry take the stuck-holder route of §C10.2
      READBACK, mandatory: require type(_fcntl(lock_fd, _F_GETFD)) is int and
      (_fcntl(lock_fd, _F_GETFD) & _FD_CLOEXEC) != 0
        otherwise ⇒ LOCK_FD_NOT_CLOEXEC ⇒ fail-closed refusal, NO fork, NO
                    record installed, lock released
      There is no F_SETFD repair path; the mechanism is single-valued.
      Then run the singleton preflight of §C10.1 for all four records.
 c2.  install SPAWNING.json (atomic no-replace; §C10.3's durability)
 c3.  create the four channels rel1, rel2, rel3, boot with
      _pipe2(_O_NONBLOCK|_O_CLOEXEC)
 c4.  pid_mid := _fork()
        not an int, or <= 0, or any BaseException ⇒ ownership is never
        established and the pre-fork fail-closed body applies
      OWNERSHIP(pid_mid) := OWNED
 c5.  in the PCS: close rel1 read, rel2 read, rel3 read, boot write
 c6.  read /proc/<pid_mid>/stat for the kernel start identity (§C9.3)
 c7.  install SPAWNING_MIDDLE.json with the exact key set: schema,
      scientific_outcome, spawning_id, cli_pid, cli_start_identity,
      middle_child_pid, middle_child_start_identity, boot_identity, created_utc
      (`cli_pid` and `cli_start_identity` denote the PCS, which is the process
      that holds the lock; the field names and schema are unchanged)
 c8.  write exactly one byte b"\x01" on rel1 write; close rel1 write
 c9.  read one group-report line from boot read, bounded by
      T_SPAWN_IDENTITY_WAIT_TIMEOUT_NS at T_SUPERVISOR_POLL_INTERVAL_NS
 c10. verify from the kernel: /proc/<middle_child_pid>/stat is live and its
      start identity matches; getsid == getpgid == middle_child_pid; the
      reported session_id and process_group_id both equal middle_child_pid
 c11. install SPAWNING_GROUP.json with group_verified: true — installable ONLY
      after c10's kernel proof
 c12. write exactly one byte b"\x02" on rel2 write; close rel2 write
 c13. read one bootstrap line from boot read, bounded as c9
 c14. verify the reported supervisor_pid is live, its start identity matches,
      and getpgid(supervisor_pid) == process_group_id
 c15. install SPAWNING_CHILD.json
 c16. write exactly one byte b"\x01" on rel3 write; close rel3 write
 c17. poll for a live-verified SUPERVISOR_IDENTITY.json, bounded by
      T_SPAWN_IDENTITY_WAIT_TIMEOUT_NS
 c18. release SPAWN.lock; the supervisor's retained fd keeps the flock until it
      closes slot 3

Middle side:
 m0.  THE LITERAL FIRST INSTRUCTION: read one byte from rel1 read, already
      O_NONBLOCK, in a loop paced at T_SUPERVISOR_POLL_INTERVAL_NS and bounded
      by T_SPAWN_IDENTITY_WAIT_TIMEOUT_NS
        b"\x01" ⇒ m1 ; b"" (EOF) ⇒ os._exit(3) ; any other byte ⇒ os._exit(3) ;
        bound expires ⇒ os._exit(3)
      Nothing else executes before this read. It performs no filesystem write
      and changes no shared state.
 m1.  close rel1 read, rel1 write, rel2 write, rel3 write, boot read
 m2.  os.setsid()
 m3.  verify getsid(0) == getpgid(0) == getpid(); any inequality ⇒ os._exit(3)
 m4.  write EXACTLY ONE canonical ASCII JSON line <= T_CONTROL_FRAME_MAX_BYTES
      on boot write: the group report. It cannot block (one line <= 4096 <=
      PIPE_BUF into an empty pipe). EPIPE ⇒ os._exit(3)
 m5.  read one byte from rel2 read with the same bounded loop:
        b"\x02" ⇒ m6 ; EOF, other byte, or bound expiry ⇒ os._exit(3)
 m6.  close rel2 read
 m7.  pid_gc := _fork()
 m8.  read /proc/<pid_gc>/stat and /proc/sys/kernel/random/boot_id; write
      EXACTLY ONE bootstrap line on boot write; close boot write;
      EPIPE ⇒ os._exit(3)
 m9.  os._exit(0)

The middle performs NO filesystem write, holds no lock epoch, executes no
wait-family call, and every wait it performs is bounded.
```

### §C6.6 The grandchild pre-exec sequence

```text
G-1. HOIST the eight descriptors the supervisor must retain — lock_fd, the boot
     write end, the role source, the sv_sock peer, the role-bootstrap source,
     the srcdir, the interpreter, the package root — to a target set of
     {3,4,5,6,7,8,9,10}. Postcondition: eight pairwise distinct numbers, all
     >= 11.                       violated ⇒ GRANDCHILD_FD_HOIST_FAILED
G-2. for slot s in ascending order 3,4,5,6,7,8,9,10:
         _dup2(h[s], s, inheritable=True)
     Slot 3's source is the hoisted lock_fd. `inheritable=True` is passed
     EXPLICITLY, never left to a default, and it is what clears FD_CLOEXEC on
     the destination.
G-3. READBACK, mandatory, for every slot:
       require (_fcntl(s, _F_GETFD) & _FD_CLOEXEC) == 0
                                  otherwise ⇒ GRANDCHILD_FD_NOT_INHERITABLE
G-4. close every hoisted source, ascending, EBADF tolerated. In particular the
     ORIGINAL lock_fd copy is closed here, so the grandchild holds exactly ONE
     lock descriptor, at slot 3.
G-5. close every remaining inherited descriptor outside {0,1,2} ∪ slots 3..10,
     ascending, once each, EBADF tolerated; redirect stdio to _devnull
G-6. _execve("/proc/self/fd/9", the SUPERVISOR argv of §C6.4, {})
     failure ⇒ os._exit(3), nothing written, nothing unlinked
```

**The lock across the whole tree.** The PCS holds `lock_fd` with `FD_CLOEXEC`
**set**, so it never leaks into a `posix_spawn`ed role. `fork` copies the
descriptor and its flag, and `FD_CLOEXEC` is consulted only at `execve`, so the
middle's and the grandchild's fork-shared references are live and the `flock`
persists while either lives. `G-2` creates a **second descriptor onto the same
open file description** at slot 3 with the flag clear, and `G-4` closes the
original, so the supervisor retains exactly one lock reference across its
`execve`. The `flock` releases only when the PCS, the middle and the supervisor
have all closed. **No role other than the supervisor ever holds a reference.**

---

## §C7. The `t-pcs.v1` protocol

### §C7.1 Two channels

| Channel | Endpoints | Kind | Operations |
|---|---|---|---|
| caller | caller ↔ PCS | two anonymous pipes at fds 3 and 4 | exactly one: `SPAWN_SUPERVISOR` |
| supervisor | supervisor ↔ PCS | one `AF_UNIX` / `SOCK_SEQPACKET` / protocol `0` pair, created by the PCS **before** the `c4` fork, its peer inherited to slot 6 | the nine of §C7.3 |

`SOCK_SEQPACKET` is chosen because it is connection-oriented, message-boundary
preserving and reliable: one `sendmsg` of a ≤ 4096-byte payload is delivered as
exactly one record or not at all, so **partial reads and partial writes are
impossible at the record level** and there is no partial-record state.

### §C7.2 The caller-channel records

One line each, `\n`-terminated, ASCII, no NUL, ≤ `T_CONTROL_FRAME_MAX_BYTES`,
fields separated by exactly one `0x20`, parsed with `bytes.split(b" ")` only —
no `json`, no `re`, no `hashlib`.

```text
REQUEST, exactly six fields:
  0  b"philosophia.officina.t-process-control-request.v1"        literal
  1  b"1"                                                        version
  2  operation, from the CLOSED one-element enum {b"SPAWN_SUPERVISOR"}
  3  spawning_id_nonce: exactly 64 bytes from [0-9a-f]
  4  caller_pid: decimal, 1..7 digits, no leading zero
  5  caller_start_identity: decimal, 1..20 digits
REPLY, exactly five fields:
  0  b"philosophia.officina.t-process-control-reply.v1"          literal
  1  b"1"
  2  outcome, from {b"SUPERVISOR_LIVE", b"REFUSED", b"BLOCKED"}
  3  detail: one token from §C2.6's closed set
  4  retryable: b"0" or b"1"
```

No field is a path, a module or symbol name, a callable, a signal number, a pid
to signal, a file descriptor, a timeout, a resource value, or a format string.
Neither record is ever persisted, archived, hashed into a signed set, or given a
durable path.

**The reply pipe is the sole authoritative result.** A competing waiter inside
the caller may reap the PCS before the caller's own wait, in which case the exit
status is lost; the status is therefore advisory diagnostics only. The caller
reading EOF **without** a complete reply line is `NO_REPLY`: it has learned
nothing, must not infer success, failure, retryability or liveness, and routes
to §C10.6.

### §C7.3 The nine operations

Common request prefix: schema literal
`philosophia.officina.t-pcs.v1`, version `b"1"`, `generation_id` (64 lowercase
hex), `request_id` (decimal, 1..19 digits, no leading zero, strictly increasing
within a generation), opcode. Common response prefix: the same schema and
version, the echoed `generation_id` and `request_id`, `status` ∈
{`OK`,`REFUSED`,`INVALID`,`REPLAYED`}, `detail` from §C2.6, `handle_id`
(decimal or `b"-"`), `fds_redelivered` (`b"0"` or `b"1"`).

| Opcode | Request operands | Preconditions | Response operands | fds |
|---|---|---|---|---|
| `SPAWN_ROLE` | `role` ∈ {`CONTROLLER`,`WORKER`}; `argv_template_id` (64 hex); `spawn_intent_id` (64 hex) | the durable spawn-intent record exists, is well-formed, and its `argv_template_sha256` matches; generation `LIVE` | `handle_id` | **3** |
| `AWAIT_STOP` | `handle_id`; `deadline_ticks` (1..6 digits, in `T_SUPERVISOR_POLL_INTERVAL_NS` units, ≤ `T_SPAWN_SELF_STOP_TIMEOUT_NS`) | handle state `SPAWNED` | `outcome` ∈ {`STOPPED`,`EXITED`,`TIMEOUT`}; `start_identity`; `pgid_is_leader` ∈ {`0`,`1`} | 0 |
| `SIGNAL_ROLE` | `handle_id`; `sig` ∈ {`CONT`,`TERM`,`KILL`,`STOP`,`PROBE`} | ownership `OWNED`; **`role != WATCHDOG`** | `result` ∈ {`SENT`,`GONE`,`DENIED`,`STRUCTURAL_VIOLATION`} | 0 |
| `SIGNAL_GROUP` | `handle_id`; `sig` | a **kernel-verified** group is recorded; `role != WATCHDOG` | as above | 0 |
| `REAP_ROLE` | `handle_id` | ownership ≠ `REAPED` | the six-result token of §C9.2 | 0 |
| `SPAWN_WATCHDOG` | — | **no live watchdog handle exists in this generation** | `handle_id` | **2** |
| `RELEASE_HANDLE` | `handle_id` | state `REAPED` | — | 0 |
| `SHUTDOWN` | — | no handle is live | — | 0 |
| `PING` | — | — | `pcs_uptime_ticks` | 0 |

**`SPAWN_WATCHDOG` has exactly one meaning.** Its precondition — the absence of
a live watchdog handle — is satisfied both at generation start and after a
previous watchdog's death has been proved. The first watchdog and every
replacement are created by the same operation with the same semantics, the same
isolation and the same one-detector model. There is no replacement-specific
opcode, handle role, or degradation flag.

`argv` never crosses the wire: the PCS reads the already-signed spawn-intent
record from the runtime root and rebuilds the fixed adapter layout itself.

**No field in any request or response carries a PID, a descriptor number, a
path, argv, a signal number, a symbol, a callback, or an unbounded integer.**

### §C7.4 Correlation and ordering

`generation_id` mismatch ⇒ `INVALID`/`WRONG_GENERATION`, no action, no state
destroyed. A `request_id` ≤ the highest journalled id is a replay (§C7.6); a gap
is permitted and recorded. Exactly one response per request, correlated by
`(generation_id, request_id)`. **The supervisor issues one outstanding request
at a time**, which removes all interleaving; an out-of-order or unmatched
response is `TRANSPORT_STRUCTURAL`. Unknown opcode, field count, handle, or
handle state ⇒ `INVALID` with the corresponding token, **no side effect, no
descriptor, no journal entry beyond the rejection record**.

### §C7.5 The handle model

```text
handle_id -> { pid, start_identity, pgid_or_null, role, generation_id,
               fd_bundle (the PCS-side role ends), state, ownership,
               fd_delivery }
  role       in CONTROLLER | WORKER | WATCHDOG
  state      in SPAWNED | STOPPED | RUNNING | REAPED
  ownership  in OWNED | CONTRADICTED | REAPED
  fd_delivery in PENDING | CONFIRMED | UNCONFIRMED
```

Invariants: handle ids are never reused, within or across generations;
`SIGNAL_ROLE` and `SIGNAL_GROUP` require ownership `OWNED`; `SIGNAL_GROUP`
additionally requires a kernel-verified group; **both signal opcodes are refused
for `role == WATCHDOG`**; `RELEASE_HANDLE` requires state `REAPED`; no wait site
runs after ownership `REAPED`; every handled process is a direct child of the
PCS.

### §C7.6 Journal, acknowledgement, replay

```text
J1. receive and validate the request
      crash ⇒ nothing happened; a redelivery is a fresh request
J2. append { generation_id, request_id, opcode, operands, state: ACCEPTED } and
    fsync
      crash ⇒ ACCEPTED with no result: the operation is INCONCLUSIVE, and
              because no PCS may adopt a live generation this is a
              whole-generation invalidity, never a silent retry
J3. perform the syscall
      crash ⇒ as J2, plus a possibly-live orphan role, routed by §C10.4
J4. append { ..., state: COMPLETED, outcome, handle_id, fd_vector_len } and
    fsync
      crash ⇒ the result is durable; a redelivery replays it
J5. send the response, with descriptors iff §C7.7's vector table says so
      crash ⇒ durable but undelivered; a redelivery replays it WITHOUT
              descriptors
J6. on ACK append { ..., state: ACKED } and fsync

REPLAY of an already-journalled (generation_id, request_id):
  ACCEPTED  ⇒ INVALID / OPERATION_INCONCLUSIVE; NO syscall is ever re-performed
  COMPLETED ⇒ the recorded status, detail and handle, with status := REPLAYED,
              fds_redelivered := 0, and NO descriptors
  ACKED     ⇒ identical to COMPLETED
```

> **Descriptors are never re-sent.** Re-sending would install a second,
> independent copy of a capability that no accounting in this contract could
> reconcile. A supervisor that loses the descriptors of a `SPAWN_ROLE` or
> `SPAWN_WATCHDOG` response cannot recover them; the handle is marked
> `FD_DELIVERY_UNCONFIRMED` and the generation routes to §C10.6. **An ACK loss
> on an fd-bearing reply therefore invalidates the generation rather than
> retrying the transfer.** This is the accepted B1 narrowing, and it applies to
> exactly two of the nine operations.

### §C7.7 `SCM_RIGHTS`

```text
SEND (PCS -> supervisor, the only direction carrying descriptors):
  anc := b"".join(fd.to_bytes(4, "little") for fd in fds)
  n := _sendmsg(sock, [payload],
                [(_SOL_SOCKET, _SCM_RIGHTS, anc)] if fds else [])
  require n == len(payload)                 otherwise TRANSPORT_STRUCTURAL
  int.to_bytes/int.from_bytes are builtin int methods requiring NO import, and
  "little" with width 4 is exactly the native int representation on the pinned
  platform. Neither `array` nor `struct` is used.

LEGAL DESCRIPTOR VECTORS — the only ones:
  every request                                   0
  SPAWN_ROLE, status OK                           3: ctrl request write,
                                                     ctrl reply read,
                                                     status read (all S_ISFIFO)
  SPAWN_WATCHDOG, status OK                       2: update write, ack read
                                                     (both S_ISFIFO)
  every refusal and every other operation         0
  maximum per message                             3
  ancillary buffer                                _CMSG_SPACE(12)

RECEIVE (supervisor side):
 B-1. r := _recvmsg(sock, T_CONTROL_FRAME_MAX_BYTES, _CMSG_SPACE(12),
                    _MSG_CMSG_CLOEXEC)
      _MSG_CMSG_CLOEXEC is MANDATORY: it sets FD_CLOEXEC atomically with
      installation, so no received descriptor can leak across an exec.
      IF B-1 RAISES ANY BaseException, the contract-authored handler body is
      EXACTLY ONE STATEMENT:
            _exit_(T_PCS_EXIT_RECV_UNENUMERABLE)
      What is specified and provable: the handler is a single
      `except BaseException:` clause whose body is that one call, with no other
      statement, call, attribute access, name binding, `else` or `finally`; the
      contract authorises no cleanup, callback, unwind, flush, close or logging
      logic there; and the contract installs no interpreter exit handlers of its
      own.
      What is NOT claimed: that no Python trace, profile or audit hook, no
      signal handler, no finalizer, no exception-machinery step and no other
      same-process callback can execute between the C call's failure and that
      statement. In a contaminated interpreter this contract cannot establish
      that and does not assert it. §C11.3 names the resulting exposure.
 B-2. NON-ABORTING parse. violation_flags := empty
      for EVERY returned control item, in order, without early exit:
        (level, type) != (_SOL_SOCKET, _SCM_RIGHTS)
              ⇒ violation_flags += {ANCILLARY_UNEXPECTED_ITEM}; the item
                carries no SCM_RIGHTS payload and contributes no descriptor;
                the loop CONTINUES
        otherwise: len(cdata) % 4 != 0 ⇒ += {ANCILLARY_RAGGED}
                   len(cdata) > 12     ⇒ += {ANCILLARY_OVERLONG}
                   n := len(cdata) - (len(cdata) % 4)
                   received += [int.from_bytes(cdata[i:i+4], "little")
                                for i in range(0, n, 4)]
      `received` is now the COMPLETE parsed vector.
 B-3. also non-aborting: flag MSG_CTRUNC, MSG_TRUNC, a wrong count for this
      opcode and status, and a wrong _fstat type for any element.
 B-4. if violation_flags is non-empty: close EXACTLY the descriptors in
      `received`, de-duplicated by numeric value, in ascending numeric order,
      once each, with _close, tolerating EBADF. Close NOTHING ELSE. Never
      enumerate /proc/self/fd. Never touch another message's descriptors or any
      live handle's fd bundle. Then route to §C10.6.
 B-5. on success the descriptors become the handle's fd bundle; they already
      carry FD_CLOEXEC.
```

> **Why the parsed vector is exactly the installed set.** On Linux, when a
> `recvmsg` control buffer is too small for all queued `SCM_RIGHTS` descriptors,
> the kernel installs exactly
> `min(space_available / sizeof(int), queued_count)` descriptors, writes their
> numbers into the returned control data, sets the returned `cmsg_len` to
> `CMSG_LEN(i * sizeof(int))` for the number `i` actually installed, sets
> `MSG_CTRUNC`, and **releases every queued descriptor it did not install**.
> Therefore an installed-but-unreported descriptor cannot exist at the kernel
> boundary. This is a **reviewer-verifiable** interface fact, not an
> author-proven one.

**Ownership across the transfer.** Before `sendmsg` the PCS holds both ends of
every pipe. `SCM_RIGHTS` **duplicates**; the send does not transfer. Immediately
after a successful `sendmsg` the PCS closes its copies of the **supervisor's**
ends unconditionally, in a pinned order, and keeps the role's ends. If
`sendmsg` raises or returns short, the PCS still holds the supervisor's ends and
closes them. After the supervisor's `recvmsg` the descriptors are its own; after
its ACK the PCS marks `FD_DELIVERY_CONFIRMED`. If the supervisor dies with
descriptors buffered in the socket, Linux releases them when the socket closes,
so there is no leak. **Every descriptor has exactly one owning slot in exactly
one process at any instant, every close is performed once by the slot's owner
with `EBADF` tolerated, and the two remediation paths act in different
processes, so no double close exists at any cut.**

---

## §C8. Role lifecycles

### §C8.1 Controller and worker

Created only by `SPAWN_ROLE`: the PCS reads the durable spawn-intent record,
rebuilds the fixed adapter argv, creates the ctrl request, ctrl reply and status
pipes with `_pipe2(_O_CLOEXEC)`, hoists, and `_posix_spawn`s the role bootstrap
with `setsid=True`, `env={}` and the isolation flags. The role's ends are
inherited at slots 3, 4 and 6; the supervisor's ends are returned as the
three-descriptor ancillary vector.

The role self-stops at `A-12` before any target behaviour. `AWAIT_STOP` performs
the bounded `waitpid(pid, WNOHANG|WUNTRACED)` loop and requires `WIFSTOPPED`;
its result is what permits the durable process-claim write. Termination uses
`SIGNAL_ROLE` with `TERM` then `KILL` on the pinned schedule of §C9.5, and
`SIGNAL_GROUP` only after a kernel-verified group exists. Death is proved by
`REAP_ROLE`.

### §C8.2 Watchdog

Created only by `SPAWN_WATCHDOG`, as an isolated role with `setsid=False` — it
must not be a session leader and is never a `killpg` target. The two-descriptor
vector gives the supervisor the update **write** end and the ack **read** end.
An `execve`'d watchdog has a fresh address space and therefore contains no
capability **by construction**.

```text
Supervisor death        : detected ONLY by EOF on the watchdog's update read
                          end. The watchdog MUST NOT use getppid() to infer
                          supervisor death and must not treat a getppid()
                          change as any signal about the supervisor: its parent
                          is the PCS, so a change means the PCS died, which is
                          a distinct condition in which the supervisor may
                          still be alive. Treating it as supervisor death would
                          produce a FALSE FREEZE.
Watchdog death          : detected by the ack-absence rule at
                          T_WATCHDOG_ACK_ABSENCE_TIMEOUT_NS, and by REAP_ROLE.
                          Only a positive targeted return proves it.
Replacement             : SPAWN_WATCHDOG, uniform with the first.
Termination             : the supervisor closes the update WRITE end; the
                          watchdog observes EOF, writes its final observations
                          and exits; the PCS reaps it on REAP_ROLE.
                          NO SIGNAL OF ANY NUMBER IS SENT TO A WATCHDOG ON ANY
                          PATH. If a positive reap is not obtained within
                          T_WATCHDOG_ACK_ABSENCE_TIMEOUT_NS after the close,
                          the route records WATCHDOG_UNREAPED and takes §C10.6.
```

Every other C1 property holds unchanged: the watchdog holds no lock and no
capability, writes nothing under `runtime/`, appends no ledger, settles nothing,
uses sealed pipes only, and writes freeze observations under its own witness id.

### §C8.3 Supervisor

Reached by `c4` fork → `m7` fork → `G-6` `execve`. It holds `SPAWN.lock` at
slot 3 until its identity is live-verified, then closes it. It is the direct
parent of nothing and the reaper of nothing; a wildcard wait in it returns
`ECHILD`. It holds opaque handles and cannot express a PID.

### §C8.4 Shutdown

```text
S-1. stop admitting; drain and settle through the signed generic-harness
     settlement rules, which §C12 names as a composition point of this contract
     (a signed peer contract, not a superseded predecessor layer)
S-2. for every live controller/worker handle: SIGNAL_ROLE / SIGNAL_GROUP per
     §C9.5, then REAP_ROLE until a positive reap, then RELEASE_HANDLE
S-3. close the watchdog update write end
S-4. the watchdog observes EOF, writes its final observations, os._exit(0)
S-5. REAP_ROLE(watchdog_handle) until, bounded by
     T_WATCHDOG_ACK_ABSENCE_TIMEOUT_NS:
       REAPED_POSITIVE       ⇒ death proved; RELEASE_HANDLE; go to S-6
       CONTRADICTED_ECHILD   ⇒ death NOT proved ⇒ §C10.6; the supervisor may
                               still proceed, because it removes no record on a
                               false death proof and the watchdog, if alive,
                               exits at its own update-EOF route
       STRUCTURAL_VIOLATION  ⇒ identical to the ECHILD row
       NOT_YET at the bound  ⇒ WATCHDOG_UNREAPED ⇒ §C10.6
S-6. SHUTDOWN
       HANDLES_LIVE ⇒ clear the offending handle first
       OK           ⇒ the PCS closes its ends, releases SPAWN.lock, and exits
S-7. the supervisor closes its remaining descriptors and exits
```

**Watchdog death is observed and reaped before the supervisor exits, or the
generation is explicitly invalid. There is no third branch.**

---

## §C9. Ownership, waiting, signalling, identity

### §C9.1 Ownership

```text
OWNERSHIP(pid) in { OWNED, CONTRADICTED, REAPED }
  OWNED        set at exactly one place: a fork or posix_spawn returning a
               value > 0 in the PCS, in a generation whose P-g returned
               NORMALIZED. MEANING: pid denotes this PCS's own child — running,
               stopped or zombie — or nothing at all; it can denote NO OTHER
               PROCESS. AUTHORIZES os.kill and os.waitpid on that pid.
  CONTRADICTED set IRREVERSIBLY on the first of: a wait returning ECHILD; a
               signal returning ESRCH; a /proc read that is PRESENT_VALID with
               no captured identity and ppid != getpid(); or a captured start
               identity that mismatches. AUTHORIZES a targeted wait only. NO
               SIGNAL, EVER AGAIN. No start identity may be captured after it.
  REAPED       set at exactly one place: a targeted wait returning that pid.
               AUTHORIZES nothing; the pid may now be reused.
Transitions: OWNED -> CONTRADICTED, OWNED -> REAPED, CONTRADICTED -> REAPED.
os.kill executes IF AND ONLY IF OWNERSHIP == OWNED.
```

**PID-reuse proof.** Linux allocates a pid only when no task holds it. The
child holds its pid from the moment the create call returns. On termination the
kernel auto-reaps only if the parent's `SIGCHLD` action is `SIG_IGN` or carries
`SA_NOCLDWAIT`; `P-g` made it `SIG_DFL` with neither **before** the create, and
verified the ignore/handler half against the kernel's own masks. The task
therefore becomes and stays a zombie holding its pid until a targeted wait from
this process returns it — at which instant `REAPED` forbids every further use.
The capture-to-signal window is therefore closed by a property established
before the child existed, not by a `/proc` read.

**The sole-reaper premise is a process-boundary fact, not a prohibition.** A
wait reaps only a direct child of the calling thread group. Every process this
contract signals or waits on is a direct child of the **PCS**, and the PCS is
constructed by `execve` with `-I -S -E -P` so that no user code ran before its
module body, verified single-tasked by two independent kernel readbacks, and
verified free of catching handlers. No entity outside it can reap its children.

### §C9.2 The wait classifier — one for all sites

```text
WAIT_ONE(pid, site) -> REAPED_POSITIVE | NOT_YET | CONTRADICTED_ECHILD
                     | RETRY_EINTR | INCONCLUSIVE_OTHER | STRUCTURAL_VIOLATION
  PRECONDITION: OWNERSHIP(pid) != REAPED. An invocation after REAPED is a
  contract violation, not a route: perform no syscall, send no signal, and
  treat the site as complete.

  r := _waitpid(pid, _WNOHANG)

  STRUCTURAL CLASSIFICATION of the returned object, in this order:
    not a tuple; len != 2; type(r[0]) is not int or type(r[1]) is not int
      (bool is rejected: the test is `type(x) is int`, not isinstance);
      r[0] < 0; r[0] != 0 and r[0] != pid; r[0] == 0 and r[1] != 0;
      r[1] < 0 or r[1] > 0xFFFF                    ⇒ STRUCTURAL_VIOLATION
    r == (pid, status)                             ⇒ REAPED_POSITIVE;
                                                     OWNERSHIP := REAPED
    r == (0, 0)                                    ⇒ NOT_YET

  EXCEPTION CLASSIFICATION, total over every BaseException:
    OSError errno ECHILD        ⇒ CONTRADICTED_ECHILD; OWNERSHIP := CONTRADICTED
    OSError errno EINTR         ⇒ RETRY_EINTR: re-issue the SAME targeted call
                                   at T_SUPERVISOR_POLL_INTERVAL_NS within the
                                   site's deadline
    OSError, any other errno    ⇒ INCONCLUSIVE_OTHER
    OSError with errno None or non-int, SystemExit, KeyboardInterrupt,
      GeneratorExit, MemoryError, RecursionError, any other BaseException
                                ⇒ STRUCTURAL_VIOLATION
  A stop or continue status can NEVER be returned: WNOHANG without WUNTRACED
  reports neither.
```

**Only `REAPED_POSITIVE` sets `REAPED`, and it is the only proof of death
anywhere in this contract. `ECHILD` is never death.** `STRUCTURAL_VIOLATION`
means the running primitive is not the genuine one; its single continuation at
every site is: never death, never `REAPED`, `OWNERSHIP := CONTRADICTED`
irreversibly, no signal ever again, no record installed, modified or removed,
and the site's `CONTRADICTED_ECHILD` continuation.

The same six-way classification applies to `_kill` and `_killpg` (the return
must be `None`; any other object or any `BaseException` outside the errno set of
§C9.5 is `STRUCTURAL_VIOLATION` ⇒ `CONTRADICTED`, no further signal) and to
`_fork`/`_posix_spawn` (the return must be an `int > 0`; anything else means
ownership is never established).

### §C9.3 The `/proc` observation

```text
STAT_OBSERVE(pid) -> ABSENT | PRESENT_VALID | UNREADABLE | UNPARSABLE | ERROR
  read /proc/<pid>/stat in full:
    ENOENT / ESRCH   ⇒ ABSENT
    EACCES / EPERM   ⇒ UNREADABLE
    EINTR            ⇒ bounded retry at T_SUPERVISOR_POLL_INTERVAL_NS until the
                       step's deadline; on expiry ⇒ ERROR
    any other OSError⇒ ERROR
  parse the 20th whitespace-separated token after the FINAL ')' (the kernel
  start time), plus the state field and ppid:
    no final ')', a short token list, a non-integer field, or any parse failure
                     ⇒ UNPARSABLE
    success          ⇒ PRESENT_VALID with (start_identity, ppid, state)
Only ABSENT and PRESENT_VALID may contribute to an identity or death
conclusion. UNREADABLE, UNPARSABLE and ERROR authorize no kill, no unlink and
no death conclusion.
```

### §C9.4 The identity decision table

`IDENTITY_OBSERVE` decides two things only: whether a start identity may be
**captured**, and whether the observation **contradicts** ownership. It does not
gate signalling — ownership does.

| # | `STAT_OBSERVE` | Captured identity | `ppid` vs `getpid()` | Verdict | Capture? | Ownership after | Continuation |
|---|---|---|---|---|---|---|---|
| I-1 | `PRESENT_VALID` | present | not consulted | matches | no | `OWNED` | signal per §C9.5 |
| I-2 | `PRESENT_VALID` | present | not consulted | **mismatches** | no | **`CONTRADICTED`** | no further signal; the earlier truthful capture stands |
| I-3 | `PRESENT_VALID` | absent | `==` | confirmed by parentage | **yes** | `OWNED` | signal per §C9.5 |
| I-4 | `PRESENT_VALID` | absent | `≠` | **contradiction** — an owned unreaped child necessarily has `ppid == getpid()`; this is the last line of defence against a failed normalization | **no** — capturing would fabricate another process's identity into a durable record | **`CONTRADICTED`** | no signal, ever; no capture |
| I-5 | `ABSENT` | either | — | not identity-bearing; **absence is never death** | no | unchanged | `WAIT_ONE` decides |
| I-6 | `UNREADABLE` | either | — | not identity-bearing | no | unchanged | **ownership still authorizes the signal**; only the durable identity is unavailable |
| I-7 | `UNPARSABLE` | either | — | as I-6 | no | unchanged | as I-6 |
| I-8 | `ERROR` | either | — | as I-6 | no | unchanged | as I-6 |
| I-9 | any | either | — | `REAPED` on entry | no | `REAPED` | contract violation; no signal |
| I-10 | any | either | — | `CONTRADICTED` on entry | **no** | `CONTRADICTED` | no signal |

### §C9.5 Signalling

```text
SIGNAL_ATTEMPT(pid, sig) -> SENT | GONE | INTERRUPTED | DENIED | ERROR
  PRECONDITION: OWNERSHIP == OWNED. Any other state is a contract violation and
  no signal is sent.
  sig in {15, 9} for the termination schedule; killpg is used only against a
  kernel-verified group.
  _kill(pid, sig)
    success        ⇒ SENT — delivered, or discarded because the target is
                     already a zombie. Signalling a zombie is safe: an unreaped
                     zombie still holds the pid. SENT alone proves nothing.
    ESRCH          ⇒ GONE. Under OWNED this is a CONTRADICTION, not a race: an
                     owned unreaped child is a task in some state and kill
                     would succeed. OWNERSHIP := CONTRADICTED; send no further
                     signal.
    EINTR          ⇒ INTERRUPTED: retry the SAME signal at
                     T_SUPERVISOR_POLL_INTERVAL_NS within the step's deadline;
                     on expiry ⇒ ERROR
    EPERM          ⇒ DENIED: send no further signal in this schedule; ownership
                     is NOT contradicted; the reaper loop continues
    any other OSError ⇒ ERROR: as DENIED

TERMINATION SCHEDULE, inside the one existing deadline, no new constant:
  t0 := the step's monotonic start ; D := T_SPAWN_IDENTITY_WAIT_TIMEOUT_NS
  1. if OWNED: SIGNAL_ATTEMPT(pid, 15)
  2. poll WAIT_ONE at T_SUPERVISOR_POLL_INTERVAL_NS until t0 + D/2
  3. if not reaped by t0 + D/2 and OWNED: SIGNAL_ATTEMPT(pid, 9)
  4. poll WAIT_ONE until t0 + D
  5. at t0 + D without a positive reap ⇒ the terminal selection of §C10.5
  A poll sample exactly at t0 + D/2 or t0 + D is treated as EXPIRED (>=), so no
  edge is ambiguous. SIGKILL cannot be caught, blocked or ignored and
  terminates a stopped process, so a stopped child is reached without any /proc
  dependence.
```

---

## §C10. Records, crash cuts, terminals, invalidity

### §C10.1 Singleton preflight

Under `SPAWN.lock`, before `c2`, for each record in the order
**child → group → middle → spawning**:

```text
P0. absent ⇒ nothing to do
P1. present but MALFORMED (schema id, key set, type, enum, hex or timestamp
    grammar fails; or it is not a regular file, has st_nlink != 1, or resolves
    through a symlink)
    ⇒ FAIL-CLOSED: REFUSED / BOOTSTRAP, retryable = false; unlink NOTHING; kill
      NOTHING. The contract never guesses at an ambiguous singleton record.
P2. present, well-formed, recorded process LIVE by pid + start identity:
    P2a. same spawning_id AND byte-identical to what this attempt would install
         ⇒ adopt it; do not rewrite; continue at the corresponding step
    P2b. otherwise ⇒ REFUSED / BOOTSTRAP, retryable = true; unlink NOTHING;
         kill NOTHING
P3. present, well-formed, recorded process NOT live — /proc absent, or state Z
    with a matching identity, or live with a DIFFERENT start identity (PID
    reuse ⇒ treat as not live and NEVER kill)
    ⇒ prove that exact state, remove per §C10.3's order, and continue
```

### §C10.2 The stuck-holder route

Taken by a later PCS **without** the lock after `T_SPAWN_LOCK_ACQUIRE_TIMEOUT_NS`
expires, in this order, each step obeying §C10.1's malformed and PID-reuse rules:

```text
s1. SUPERVISOR_IDENTITY.json present and live-verified ⇒ a live supervisor
    exists; kill nothing; proceed as an ordinary client
s2. SPAWNING_CHILD.json well-formed, its recorded process live by pid + start
    identity, and older than T_SPAWN_BOOTSTRAP_MAX_AGE_NS ⇒ killpg the
    supervisor pgid, prove death, remove per §C10.3, retry the acquisition once
s3. SPAWNING_GROUP.json well-formed with group_verified: true, its group live,
    and older than the same bound ⇒ killpg the process group, prove death,
    remove, retry once
s4. SPAWNING_MIDDLE.json well-formed, its process live, and older than the same
    bound ⇒ kill(middle_child_pid) ONLY, never killpg, after start-identity
    validation; prove death; remove; retry once
s5. otherwise ⇒ REFUSED / BOOTSTRAP, retryable = true
```

`s5` is a **consequence**, never a resolver: it resolves no held lock and no
surviving record, and this contract nowhere describes it as forward progress.

### §C10.3 Record removal

Every death-proved failure route removes records in exactly this order, each
`unlink` followed by an `fsync` of the parent directory, `ENOENT` tolerated:

```text
1. SPAWNING_CHILD.json   -> fsync
2. SPAWNING_GROUP.json   -> fsync
3. SPAWNING_MIDDLE.json  -> fsync
4. SPAWNING.json         -> fsync
```

`SPAWNING_CHILD`, `SPAWNING_GROUP` and `SPAWNING_MIDDLE` name processes other
than the PCS and are **protected by death-before-unlink**. `SPAWNING.json` names
the PCS itself, so removing it can orphan nothing: **every *returning* terminal
removes it while still holding the lock.** A non-returning state has not
abandoned the attempt and retains it.

### §C10.4 PCS loss — unrecoverable, no adoption

```text
On PCS death at ANY point:
  - the kernel closes every descriptor it held: its lock reference, the
    supervisor socket, the journal, and every role-side end;
  - pid_mid and every role are adopted by the nearest living ancestor
    subreaper, else namespace init, and reaped by that adopter;
  - the supervisor observes channel EOF and has lost ALL process authority: it
    can create, signal, wait for and reap nothing;
  - the watchdog's getppid() changes, which under §C8.2 means the PCS died and
    is NOT a supervisor-death signal; the watchdog continues until its own
    update EOF;
  - the journal's last entry may be ACCEPTED, so an operation may or may not
    have happened: that is the inconclusive case;
  - the four singleton records survive under §C10.1; no record naming a
    possibly-live process is removed without a proof.

PROHIBITION: A NEW PCS MUST NEVER ADOPT A LIVE GENERATION. It is not the parent
of any surviving process, so it can neither wait for nor safely signal one. A
PCS that starts and finds a journal whose generation is not terminal MUST
respond GENERATION_NOT_ADOPTABLE, take no action, and exit.

SUPERVISOR CONTINUATION on channel EOF:
  1. refuse every admission and every command requiring a role operation;
  2. FREEZE IS UNAVAILABLE — the quiescence proof needs SIGNAL_GROUP, a PCS
     operation — so no live stream has a valid continuation;
  3. close the watchdog update write end; the watchdog writes its observations
     for the groups it knows and exits; its adopter reaps it;
  4. route the generation through §C10.6.
```

### §C10.5 Stage-M terminals

Used by any abandonment at `c5`, `c6` or `c7`, after `c4` returned `pid_mid > 0`
under a normalized `P-g`.

```text
M0. OWNERSHIP := OWNED; captured := the c6/c7 start identity if one exists
M1. t0 := monotonic now ; D := T_SPAWN_IDENTITY_WAIT_TIMEOUT_NS
M2. IDENTITY_OBSERVE(pid_mid)
M3. if OWNED: SIGNAL_ATTEMPT(pid_mid, 15)
M4. loop at T_SUPERVISOR_POLL_INTERVAL_NS:
      a. WAIT_ONE(pid_mid)
           REAPED_POSITIVE     ⇒ leave the loop
           NOT_YET             ⇒ continue
           CONTRADICTED_ECHILD ⇒ leave the loop immediately: no later wait can
                                 return this pid
           INCONCLUSIVE_OTHER / STRUCTURAL_VIOLATION ⇒ continue
      b. if OWNED and now >= t0 + D/2: SIGNAL_ATTEMPT(pid_mid, 9)
      c. if captured is absent and OWNED: IDENTITY_OBSERVE, at most once per
         poll interval
      d. if now >= t0 + D: leave the loop
M5. TERMINAL SELECTION — total, and the three predicates are pairwise disjoint:
      REAPED                         ⇒ T1
      not REAPED and captured        ⇒ T2
      not REAPED and not captured    ⇒ B     (does not return)

T1  cleanup of the bootstrap ends; ordered removal of ALL FOUR records per
    §C10.3 while holding the lock; release the lock; REFUSED / BOOTSTRAP,
    retryable = true. No record survives; the child is reaped, so no
    fork-shared lock reference survives.
T2  cleanup; install SPAWNING_MIDDLE.json if not already durable, with the
    exact key set, every field an OBSERVED value; remove ONLY SPAWNING.json;
    retain pid_mid in memory as an unreaped own child so a later attempt in
    this process reaps it at §C10.1's P3; release the lock; REFUSED /
    BOOTSTRAP, retryable = true. The surviving record is resolved by
    §C10.1/§C10.2.
B   no truthful record is constructible, so nothing is installed and nothing is
    returned. B RETAINS SPAWN.lock, SPAWNING.json, the in-process pid handle
    and the bootstrap ends; installs NOTHING; emits NO refusal, reply, event or
    artifact; and loops at T_SUPERVISOR_POLL_INTERVAL_NS on WAIT_ONE plus an
    ownership-gated SIGKILL plus re-observation. Its ONLY exits are a positive
    reap into T1 and a valid capture into T2.
```

**No route may return, release the lock, remove `SPAWNING.json`, or discard
every durable and in-process handle while the child may remain live and
unreaped.**

**Why the middle cannot become a second supervisor at `c5`–`c7`.** Execution is
`c1 → … → c4 → c5 → c6 → c7 → c8`, and the stage-1 release byte is written at
`c8`. At any abandonment at `c5`, `c6` or `c7` **no `c8` byte was ever written**:
`rel1` is a fresh pipe and `c8` is its only writer. The middle is at `m0`, still
owns its own inherited `rel1` **write** end, so EOF at `m0` is impossible in
principle no matter what the PCS closes. It exits by its own `m0` bound or by
the parent's ownership-authorized signal and reap. It can never reach `m1`,
hence never `m2`, `m4`, `m5` or `m7`: **no grandchild is forked and no
supervisor identity is installed.** The fork-shared `SPAWN.lock` reference is
what prevents a new PCS from acquiring until the middle exits.

### §C10.6 Invalidity routing

```text
An operation whose control outcome cannot be established, or a generation whose
PCS is gone, is a PROCESS fact:
  - it settles through the signed T_PROCESS_INVALID recovery disposition and the
    signed unknowable route, with invalidity dominance;
  - it is NEVER a completion, never a capacity fact, never a custody
    disposition, never an E1/E2/E3 fact, and never a Q/C input;
  - no resource value is inferred from it and no scientific outcome is produced
    or predicted.
A caller that misreports a truthful reply changes nothing durable: the record
set, the journal, the capacity ledger and the custody dispositions are written
by processes the caller does not control, and B1's idempotency rules make a
retry converge on the recorded truth rather than on the caller's account of it.
No route may treat "the caller's own user was misinformed" as a disposition.
```

### §C10.7 Crash and cut matrix

| Cut | Single continuation |
|---|---|
| any `P-cwd`…`P-p` failure | the named token; **no fork, no lock, no record** |
| `c1` lock readback shows `FD_CLOEXEC` clear | `LOCK_FD_NOT_CLOEXEC`; no fork; lock released |
| `c4` fork returns a non-`int`, `<= 0`, or raises | ownership never established; the pre-fork body applies |
| crash between `P-p` and `c4` | no child; `SPAWNING.json` names a **crashed** PCS, so the next attempt's `P3` proves its death by absence and removes it |
| `G-1` hoist violated, or `G-3` shows a `CLOEXEC` slot | `os._exit(3)`; nothing written; the PCS's `c13` read sees `boot` EOF ⇒ §C10.2's stage routes |
| `G-6` `execve` fails | `os._exit(3)`, nothing written, nothing unlinked |
| role `A-1`…`A-13` failure | identical |
| a `posix_spawn`ed role's `A-5` finds an unexpected descriptor | refusal — a **verification failure**, not the mechanism |
| caller crash, or it stops reading, or closes the reply pipe early | the reply write yields `EPIPE`, which `SIGPIPE = SIG_IGN` turns into an exception; it is recorded and **changes no record, custody, ownership or terminal decision** |
| a competing waiter in the caller reaps the PCS | only the exit status is lost; the pipe reply is authoritative |
| the caller kills the PCS | §C10.4 |
| `_recvmsg` raises | the single-statement `_exit_`; §C11.3 names the exposure |
| any ancillary violation | the full vector is parsed, then exactly it is closed; §C10.6 |
| ACK lost on an fd-bearing reply | `FD_DELIVERY_UNCONFIRMED`; **no re-send**; §C10.6 |
| replay of `ACCEPTED` / `COMPLETED` / `ACKED` | §C7.6's three rows; no syscall is ever re-performed |
| supervisor death, PCS alive | the watchdog sees update EOF and freezes, observes, exits; the PCS holds every live handle in the non-returning reaper state and frees the singleton for no one; §C10.1 governs the records at the next attempt |
| **PCS death** | §C10.4 |
| watchdog death | §C8.2 detection, then `SPAWN_WATCHDOG` |
| wedged watchdog (no exit after EOF) | `WATCHDOG_UNREAPED`; **no signal**; §C10.6 |
| controller or worker stopped | `AWAIT_STOP`/`REAP_ROLE` see `(0,0)`; §C9.5's schedule via `SIGNAL_ROLE`; a stopped role holding a fork-shared reference is the named A3 residual |
| `STRUCTURAL_VIOLATION` at any wait site | never death; `CONTRADICTED`; no further signal; no record touched |
| `SHUTDOWN` with a live handle | `HANDLES_LIVE`; nothing released |
| a second launcher concurrently | it spawns its own PCS; both contend for `SPAWN.lock` under §C10.1/§C10.2; the singleton property is the lock and the records, never a process identity |
| crash between any ordered unlink and its `fsync` | `ENOENT`-tolerant; the order resumes |
| restart before or after the middle's `m0` bound | the records survive; the middle exits at its bound; §C10.1 governs |

---

## §C11. Guarantees, residuals, and the exposure

### §C11.1 Safety — guaranteed and claimed

```text
S1. No false-positive death proof. No live process is ever recorded dead, and
    no record naming a possibly-live process is removed without an object-bound
    proof or an authoritative reap by its own parent.
S2. No capability transfer to any unauthorized actor. No descriptor, handle,
    opcode or journal authority reaches a process outside the PCS/supervisor
    control plane.
S3. No unauthorized decision. No interference is accepted as an Officina
    decision, and no adopter-observed value is consumed by one.
S4. Fail-closed routing. Every perturbed or unestablished control outcome
    settles through §C10.6, never as a completion, capacity fact, custody
    disposition, E1/E2/E3 fact, Q/C input or scientific evidence.
```

### §C11.2 Liveness — explicitly NOT guaranteed

```text
L1. That any generation completes.
L2. That a death proof ever becomes available for a stopped process.
L3. That a sealed channel ever reaches EOF.
L4. That a fail-closed stall ever terminates.
L5. That a same-UID actor is confined, detected or prevented in any way.
```

**A3 is a procedural rescope. It is not confinement and not adversarial
same-UID or same-process security, and nothing in this contract upgrades it.**
Every liveness loss above is permanently non-citable.

### §C11.3 What an adopter or same-UID actor can and cannot do

| It can | Detail |
|---|---|
| become the parent of orphans | the supervisor after `m9`; after PCS death `pid_mid`, controllers, workers and watchdogs |
| reap them, including by wildcard wait | its wildcard waits range over everything it has adopted |
| observe each orphan's pid and **wait status** | the status is an **untrusted operating-system fact**. It may reflect same-UID interference, including a signal the actor itself delivered. **This contract does not enumerate or bound the values it may take.** It carries no authorized programme meaning and is consumed by no decision, record, journal entry, settlement, capacity accounting, custody disposition or Q/C input |
| delay reaping, or reap promptly | the first prolongs `/proc` state `Z`; the second makes `/proc` absence true sooner. Both are already accepted death proofs |
| stop, kill, or delay any same-UID process, with or without adoption | already true under A3; adoption adds no signalling power |
| **deny proof availability indefinitely** | a stopped process stays alive, shows state `T`, and keeps every open descriptor — so **no death proof ever becomes available and a sealed channel it holds never reaches EOF**, including the supervisor socket and the watchdog update pipe |

| It cannot | Why |
|---|---|
| create a **false-positive** object-bound death proof for a live process | the predicates are `/proc` absence, or state `Z` with a matching start identity, or live-with-a-different-identity. A live or stopped process with a matching identity satisfies none, and absence cannot be fabricated |
| obtain any descriptor or capability | reaping conveys none; capabilities move only by `SCM_RIGHTS` on the sealed point-to-point socket or by inheritance the PCS controls |
| participate in the control plane | it holds no channel endpoint, so no opcode is reachable to it; it appears in no journal as an actor; it can issue no request, receive no response and hold no handle |
| turn interference into a valid Officina decision or a scientific or resource outcome | every route it can perturb fails closed into §C10.6 |

**Kernel power is admitted; Officina authorization is not conferred.** Those are
different statements and this contract makes only the second.

### §C11.4 Named residuals

1. **The unreaped-zombie residual.** A `T2` termination leaves one zombie: one
   pid slot, **no descriptors and no lock reference**, `/proc` state `Z` with a
   matching identity — which is itself an accepted death proof for any other
   process. It is reaped at a later attempt in the same PCS or by its adopter
   after the PCS exits. It is bounded by the PCS's own lifetime.
2. **`B`-state non-termination.** With ownership sound, `SIGKILL` or the
   middle's own `m0` bound ordinarily produces a positive reap. Non-termination
   requires a deliberately stopped child conjoined with a persistent signal
   fault.
3. **The receive-path exposure.** From the instant the kernel may have installed
   descriptors inside `_recvmsg` until the process actually exits, those
   descriptors are present in the supervisor's table, and same-process hooks,
   finalizers or threads that the host installed may run and reach them. **This
   is a transient capability exposure, not a resource fact.** Its length is not
   under this contract's control; it is terminated with certainty by the
   kernel's closure of the descriptor table at exit. It lies inside A3.

All three are permanently non-citable.

---

## §C12. Composition with the generic harness and batch settlement

This contract composes with, and changes nothing in, the signed generic-harness
contract and the signed batch-settlement amendment. The composition points are
exactly these:

| Point | Rule |
|---|---|
| durable process claim | written by the supervisor **after** `AWAIT_STOP` returns `STOPPED` with a start identity — the same fact, obtained by the same syscall, in a clean process |
| spawn intent | written by the supervisor **first**; `SPAWN_ROLE` then names it by id and the PCS rebuilds the adapter argv from it. The signed record's schema, key set and template hash are unchanged |
| lease, start, heartbeat, close, pause, resume | unchanged; they never name a PID |
| watchdog registration, table publication, ack liveness, freeze observation | unchanged; the descriptors arrive by `SCM_RIGHTS` instead of by fork inheritance |
| output capacity | unchanged: supervisor-mediated transport, the §C2.3 ceiling, one-write / one-hash accounting, no replenishment. The PCS creates the pipes; the supervisor still mediates and accounts |
| custody proof, object-bound observation, both revalidation barriers, malformed dominance | unchanged and performed by the supervisor under `T_RUNTIME.lock` |
| settlement, quarantine, promotion, batch prefix automaton, head/cache authority, inline meter evidence, archival order | unchanged |
| the nine signed events, E1/E2/E3, invalidity dominance | unchanged; every fact this contract adds is control-plane, T-development-only and non-citable |

**No scientific or resource rule is created, moved, widened or narrowed by this
contract.**

---

## §C13. The verifier

### §C13.1 The guard target — mechanically decidable

```text
CONTRACT_GUARD_TARGET := the byte range of THIS FILE strictly between the first
occurrence of the line

    <!-- OFFICINA-P1-NORMATIVE-BEGIN -->

and the first subsequent occurrence of the line

    <!-- OFFICINA-P1-NORMATIVE-END -->

called NORMATIVE_BODY.

The guard rules read EXACTLY ONE FILE: this one. They read NO other file, ever.
There is no allowlist, no exclusion list, no supersession inference, and no
adjective such as "operative" for a verifier to interpret. Historical documents
are categorically outside the domain because they are never opened.
```

### §C13.2 Normalization

```text
NORMALIZE(bytes) :=
  decode UTF-8; apply Unicode NFC; map every ASCII uppercase letter to
  lowercase; delete every occurrence of the characters * _ ` and the sequences
  <!-- and -->; replace every maximal run of whitespace (space, tab, newline,
  carriage return) with a single space; strip leading and trailing spaces.
```

### §C13.3 The guard rules

Each rule holds a closed list of **forbidden normalized patterns** and a paired
**permitted form**. The pattern data lives in §C16's delimited, non-normative
appendix, which is **outside** `NORMATIVE_BODY` and is therefore never matched
against itself.

```text
G-1  no forbidden pattern of class ADOPTION appears in NORMALIZE(NORMATIVE_BODY)
     Class ADOPTION forbids asserting that an orphan is re-parented to, or
     reaped by, init or pid 1 without the nearest-living-ancestor-subreaper
     qualification.        ⇒ "guard G-1: absolute init adoption claim"
G-2  class ANCESTOR_WAIT_SET: no exclusive wait-set is asserted for the caller
     or any ancestor without the dynamically-adopted-orphan qualification.
                           ⇒ "guard G-2: exclusive ancestor wait-set"
G-3  class STATUS_SET: no enumeration, bound or closure of the set of
     wait-status values an adopter may observe.
                           ⇒ "guard G-3: closed adopter status set"
G-4  class LIVENESS: in the adopter or same-UID context, no assertion that the
     actor cannot block, delay, prevent or deny a death proof, a channel EOF or
     progress; and no unqualified assertion that it cannot gain process
     authority. The permitted forms are exactly: that it cannot create a
     false-positive object-bound death proof, and §C11.3's four authorization
     clauses.            ⇒ "guard G-4: adopter liveness or authority overclaim"
G-5  class LIVENESS_GUARANTEE: no assertion that this contract guarantees
     completion, eventual proof availability, eventual EOF, stall termination,
     or same-UID confinement.
                           ⇒ "guard G-5: liveness or confinement guarantee"

DECISION RULE: a violation is reported iff a forbidden normalized pattern of
that class occurs as a substring of NORMALIZE(NORMATIVE_BODY). Because the
target is one file with no exclusions, the result is a total function of this
file's bytes.
```

### §C13.4 The closed invariant — stronger than wording

```text
G-6  NORMATIVE_BODY_SHA256 := SHA-256 of the exact bytes of NORMATIVE_BODY.
     The verifier recomputes it and compares it with the value recorded in
     PRODUCTION_CALL_GRAPH.json under `p1_composite_normative_sha256`.
     A mismatch ⇒ "guard G-6: normative body digest differs".

     ANY edit to the normative body changes this digest and therefore requires
     a new signed and reviewed version. Even if a wording guard failed to match
     a novel phrasing of a withdrawn overclaim, the edit itself cannot pass
     unnoticed.
```

### §C13.5 The acyclic custody rule

```text
This file CANNOT contain its own SHA-256 without a cycle, and does not.
The custody chain is a DAG with four links and no back edge:

  1. this composite file                     — contains no digest of itself
  2. the author closure                      — pins sha256(this file) and
                                               sha256(NORMATIVE_BODY)
  3. the independent X and Y reviews         — recompute and confirm both
  4. PRODUCTION_CALL_GRAPH.json              — records the reviewed
                                               p1_composite_sha256 and
                                               p1_composite_normative_sha256,
                                               which the verifier then enforces
                                               (G-6)

No step reads a digest from a document that contains it. Verification order is
1 → 2 → 3 → 4, and the verifier at step 4 depends only on step 4's manifest and
step 1's bytes.
```

### §C13.6 The code rules

```text
CHANGE 1  PRODUCTION_ROOTS = the five paths of §C3.1
CHANGE 2  the allowlists of §C3.2, with the scoped map exact, not a union
CHANGE 3  the AST grammar over each root:
  S-1  the PCS root has exactly six Import nodes (os, sys, _signal, time, fcntl,
       _socket); the role root exactly three (os, sys, fcntl); module scope,
       unaliased, no ImportFrom, none conditional or nested
  S-2  no Global, Nonlocal, AsyncFunctionDef, Await, Yield, YieldFrom, Lambda,
       ClassDef, decorator, or Starred argument to a bound primitive
  S-3  the binding block is §C3.4's exact list, in order, at module scope, each
       target a plain Name, each value an Attribute of one of the permitted
       modules
  S-3b the first executable statement is _BUILTIN = type(len); len appears
       nowhere else
  S-4  every bound name is assigned exactly once and never rebound, deleted,
       parameterized or setattr'd
  S-5  the module names appear as an Attribute value ONLY inside the binding
       block
  S-6  every Call func is a plain Name, a bound name, or a whitelisted builtin
       from the closed set {len,int,str,bytes,range,enumerate,sorted,min,max,
       abs,tuple,list,dict,set,frozenset,isinstance,type,repr,ord,chr,divmod,
       bool}; never a Subscript, never an arbitrary expression
  S-7  forbidden names anywhere: signal, functools, enum, _thread, threading,
       multiprocessing, concurrent, asyncio, ctypes, subprocess (in the PCS and
       role roots), atexit, gc, hashlib, json, re, array, struct, socket,
       prctl, PR_SET_CHILD_SUBREAPER, register_at_fork, start_new_thread,
       settrace, setprofile, addaudithook, set_wakeup_fd, pthread_sigmask,
       pthread_kill, siginterrupt, alarm, setitimer, pidfd_send_signal, SIG_IGN,
       readlink, PYTHONPATH, putenv, SO_PASSCRED, SCM_CREDENTIALS, getattr,
       setattr, delattr, vars, globals, locals, eval, exec, compile, __import__,
       importlib, open (the builtin)
  S-8  wait forms: every _waitpid call's first argument is either the literal
       -1 at EXACTLY ONE call site, whose enclosing function is the P-e
       preflight and which is lexically before every create call, or a plain
       Name bound from a create return. No _wait, _wait3, _wait4 or _waitid
       binding exists.
  S-9  every _sigsignal second argument is _SIG_DFL; every _getsignal argument
       is _SIGCHLD
  S-10 no __del__, weakref finalizer, or context-manager exit calls a bound
       primitive
  S-11 every _posix_spawn call passes the argument shape of §C6.1 or §C8.1,
       with a file_actions literal in the pinned order and no preexec_fn,
       shell or cwd keyword
  S-12 subprocess, Popen, fork, waitpid, kill, killpg and system appear on no
       path of generic_harness.py
  S-13 no "/proc/self/fd/" string literal is concatenated with a non-constant
       expression; the fd paths are exact constants
  S-14 every _recvmsg call passes _MSG_CMSG_CLOEXEC
  S-15 every _recvmsg ancillary buffer argument is exactly _CMSG_SPACE(12)
  S-16 no wire-record field is derived from a descriptor: fileno, detach and
       .fileno() are forbidden in the record builders
  S-17 the role root contains exactly one sys.path assignment, of the form
       sys.path[:] = [<one literal-prefixed /proc/self/fd/ string>]
  S-18 a /proc/self/fd enumeration appears ONLY at the three sites of §C5.5,
       with that site's permission; an enumeration at P-f or A-5 followed by a
       close whose argument derives from the listing is a violation
  S-19 the _recvmsg exception handler body is EXACTLY ONE Expr whose value is a
       Call to _exit_ with the single constant T_PCS_EXIT_RECV_UNENUMERABLE; no
       other statement, no else, no finally. S-19 asserts an AST property and
       NOTHING about interpreter behaviour before the handler runs.
  S-20 the SPAWN.lock open passes _O_CLOEXEC and is followed by an
       _fcntl(_F_GETFD) readback whose failure branch refuses; no _F_SETFD call
       exists anywhere
  S-21 no file_actions literal names the lock descriptor; the grandchild
       contains exactly one _dup2(..., 3, inheritable=True) whose source is the
       hoisted lock descriptor
  S-22 no signal call site is reachable with a watchdog handle or a watchdog pid
  S-23 prctl, PR_SET_CHILD_SUBREAPER and ctypes appear in no production root
  S-24a STATIC: exactly one decision branch consumes a wait-status word, and it
       is the named WIFSTOPPED site in the AWAIT_STOP handler
       ⇒ "S-24a: wait status consumed outside the single named site"
  S-24b TOPOLOGY: every controller and worker creation site is a _posix_spawn
       call in the PCS root, and no create call for either role appears in any
       other root. This is what makes the WIFSTOPPED target a live-custody,
       non-orphan direct PCS child; a future topology change fails HERE even if
       S-24a still counts exactly one branch.
       ⇒ "S-24b: role creation outside the PCS"
CHANGE 4  generic_harness.py contains no `import signal`, no `signal.` or
          `_signal.` attribute, and no `sys` import
CHANGE 5  the manifest records root_source_sha256 for all FIVE roots plus
          p1_composite_sha256 and p1_composite_normative_sha256; the verifier
          recomputes and compares each; a mismatch is fail-closed
```

### §C13.7 Runtime preflight — what static analysis cannot decide

`P-a` platform; `P-b` interpreter identity and the four isolation flags; `P-c`
and `P-d` single task; `P-e` no inherited children; `P-f` descriptor topology
and source/interpreter object properties; `P-g` signal state including
`SigBlk == 0` and `SigCgt == 0`; `P-h` request grammar; `P-p` package-root
binding; §C3.5's primitive identity check; `G-3`'s inheritability readback; and
`A-1`…`A-11`. Each is fail-closed with no fork, no lock acquisition and no
record installed.

> **TI-1, the topology invariant, stated separately from any AST rule.** Every
> process whose wait status is consumed by a decision is a **direct child of
> the PCS at the moment of consumption**. `S-24a` checks the count of
> status-consuming branches; `S-24b` checks that role creation lives only in
> the PCS; and the behavioural test of §C14 row 33 checks that the
> `AWAIT_STOP` target is a non-orphan direct PCS child at the moment the status
> is read. **No single rule carries TI-1 alone**, and no rule is described as if
> it did.

---

## §C14. The test matrix

Every row is a future obligation. **Nothing here is authorized to run.**

| # | Test |
|---|---|
| 1 | the launch is byte-exact: seven-element argv, `env == {}`, `setsigmask=()`, twelve file actions in the pinned order, no `preexec_fn`/`shell`/`cwd`/`close_fds`/`pass_fds` keyword |
| 2 | `readlink` appears nowhere; the exec targets are the two literal `/proc/self/fd/<N>` constants; `sys.executable` is used for nothing |
| 3 | source-object binding: unlink, rename, replace-at-name, truncate, hardlink and symlink-at-name each behave as §C6.1 requires |
| 4 | the hoist terminates, yields pairwise-distinct descriptors above the target maximum, and closes every intermediate; a forced collision refuses |
| 5 | `POSIX_SPAWN_DUP2` clears close-on-exec on the destination; the mapped slots are inheritable and every other `CLOEXEC` descriptor is closed by the exec |
| 6 | the `_POSIX_SPAWN_*` set-equality and distinctness validation rejects a rebound constant |
| 7 | `posix_spawn` failure modes: raise, non-`int`, `<= 0`, and a failing file action each route as §C6.1 and §C10.7 state |
| 8 | the launcher performs no fork, no `Popen`, no `preexec_fn`, no shell — static and dynamic |
| 9 | a caller that defeats its own launcher checks produces a process the PCS's preflight refuses |
| 10 | `P-a`…`P-p` each return exactly one named result; no exception escapes; every non-`OK` result reaches the fail-closed body with **no fork** |
| 11 | `P-b` refuses when any one of `-I`, `-S`, `-E`, `-P` is dropped; assert the refusal is read from `sys.flags` and that argv is consulted nowhere |
| 12 | with `-S`, a `.pth` line, a `sitecustomize` and a `usercustomize` present on the host each execute in the caller and **not** in the PCS or any role |
| 13 | the PCS import set is exactly the six of §C3.2; `signal`, `functools`, `enum` and `_thread` are absent from the closure |
| 14 | every row of §C3.5's identity table passes for a genuine binding and fails for its stated substitution: Python function, `partial`, bound method, callable instance, foreign-module builtin, wrong `__qualname__`, wrong constant value |
| 15 | `P-e`'s single wildcard wait raises `ECHILD` in a correct launch; a fixture handing the PCS an inherited child makes it return, and the route refuses `INHERITED_CHILD` with no fork |
| 16 | `P-g`: after the reset pass `SigCgt == 0`; the `SIGCHLD` `SigIgn` bit is clear; `SigIgn` is otherwise unchanged; an inherited `SIG_IGN` and an inherited `SA_NOCLDWAIT` are both cleared; `SIGPIPE = SIG_IGN` survives |
| 17 | `P-g0`/`g-2` refuses a non-zero `SigBlk` |
| 18 | the mask grammar rejects the empty value, `0`, `0000`, a 13-digit value, a 20-digit value, a `0x` prefix, a sign, internal whitespace, a trailing byte, a missing field and a duplicated field; conversion happens only after both width conjuncts pass |
| 19 | the platform table: `x86_64` accepted; MIPS, ARM64, i386, Alpha, SPARC and non-Linux each refused **at `P-a`, before any mask is parsed** |
| 20 | `c1`'s lock is created `_O_CLOEXEC` and the `F_GETFD` readback holds; a fixture clearing the flag makes `c1` refuse with no fork; no `F_SETFD` call exists |
| 21 | `G-1`…`G-6`: eight hoisted sources above 10, ascending `DUP2`s, the `G-3` readback proving the flag clear on every slot, the original lock copy closed at `G-4` |
| 22 | the fork-shared-lock trace: the `flock` persists while the middle lives, survives the grandchild's `execve` on slot 3, and releases only when the PCS, the middle and the supervisor have all closed |
| 23 | no controller, worker or watchdog holds a descriptor whose `(st_dev, st_ino)` equals `SPAWN.lock`'s at any instant after its `execve` |
| 24 | after every `posix_spawn`ed role's `execve`, `/proc/self/fd` is exactly `{0,1,2}` ∪ its slot set — **by construction**; `A-5` is asserted to be a verification |
| 25 | the `WATCHDOG` file actions contain the explicit `(CLOSE, 6)`; no file-action vector for any role names the lock |
| 26 | the role bootstrap imports exactly `{os, sys, fcntl}`; a two-import build fails at `A-6` |
| 27 | `A-1`…`A-13` refuse in order with nothing written; `A-9` sets exactly one object-bound path entry; `A-11` rejects a role module substituted after `A-7` |
| 28 | `os.environ` is empty in every role; `PYTHONPATH` appears nowhere in the repository's launch paths |
| 29 | the §C6.4 controller/worker proof holds for each of its six vectors |
| 30 | `WAIT_ONE` is total over every returned object and every raised object: non-tuple, wrong arity, `bool` elements, negative pid, wrong positive pid, `(0, nonzero)`, out-of-range status, `ECHILD`, `EINTR`, other errno, `errno is None`, `SystemExit`, `KeyboardInterrupt`, `GeneratorExit`, `MemoryError`, `RecursionError`, arbitrary `BaseException` |
| 31 | `STRUCTURAL_VIOLATION`'s continuation at every site: never death, `CONTRADICTED` set, no signal ever again, no record touched |
| 32 | `WAIT_ONE` invoked after `REAPED` performs no syscall and is a contract violation |
| 33 | **TI-1**: at the moment `AWAIT_STOP` reads a status, its target is a live-custody, non-orphan direct PCS child; assert `S-24a` and `S-24b` both hold and that neither alone is described as carrying TI-1 |
| 34 | the identity table I-1…I-10 is total over the product of the five `STAT_OBSERVE` results × captured/uncaptured × `ppid` equal/unequal × the three ownership states |
| 35 | I-4 captures nothing, sends no signal, and writes no durable record from a contradicted observation |
| 36 | `os.kill` executes iff `OWNERSHIP == OWNED`; injected `REAPED` and `CONTRADICTED` states make every signal site unreachable |
| 37 | `SIGNAL_ATTEMPT` returns exactly one of five results; `ESRCH` under `OWNED` sets `CONTRADICTED`; `EPERM` does not |
| 38 | the PID-reuse window: with normalization in place, inject a child exit at every instruction boundary between `STAT_OBSERVE` and `os.kill`; the pid is never reassigned before this route's own reap |
| 39 | `/proc` fully unreadable, live child: the route terminates and reaps; `/proc` fully unreadable, stopped child: `SIGKILL` under ownership alone reaches it |
| 40 | the `T1`/`T2`/`B` predicates are pairwise disjoint and exhaustive; `B` returns nothing, retains lock, record and handle, installs nothing, and exits only by a positive reap or a valid capture |
| 41 | the stage-M causal trace: at `c5`, `c6`, `c7` no `c8` byte exists, the middle is at `m0` owning its `rel1` write end, EOF at `m0` never occurs, `m1`/`m2`/`m4`/`m5`/`m7` are unreachable, no grandchild is forked, and the next PCS cannot acquire the lock until the middle exits |
| 42 | the socket pair is created before the `c4` fork; the peer reaches the `SUPERVISOR` role at slot 6 and nowhere else |
| 43 | a 4096-byte payload is delivered whole; a 4097-byte payload is refused before send |
| 44 | the fd vector for each opcode and status equals §C7.7's row exactly; every other count or type is `ANCILLARY_VIOLATION` |
| 45 | `MSG_CMSG_CLOEXEC` is passed on every `recvmsg`; received descriptors carry `FD_CLOEXEC` with no window |
| 46 | `MSG_CTRUNC`, `MSG_TRUNC`, a non-`SCM_RIGHTS` item, a ragged `cdata` and an over-long `cdata` each route as §C7.7 states |
| 47 | `B-2` is **non-aborting**: a message whose first control item is not `SCM_RIGHTS` and whose second carries descriptors still yields the complete vector, and `B-4` closes every one of them |
| 48 | `B-4` closes exactly the parsed vector, de-duplicated, ascending, once each; a concurrent live role's ctrl and status descriptors survive |
| 49 | `/proc/self/fd` is enumerated at exactly the three sites of §C5.5 and nowhere else; `P-f` and `A-5` perform no close derived from the listing |
| 50 | no double close and no leak at every ownership cut, including sender death mid-send and receiver death with descriptors buffered |
| 51 | the `_recvmsg` handler body is exactly one `_exit_` call; **no test and no contract sentence claims that no callback can run before it** |
| 52 | replay of `ACCEPTED` yields `OPERATION_INCONCLUSIVE` with no syscall; replay of `COMPLETED`/`ACKED` yields the recorded record with `fds_redelivered = 0` and no descriptors |
| 53 | the `J1`–`J6` order holds and every crash cut behaves as §C7.6 tabulates |
| 54 | one outstanding request at a time; an out-of-order or unmatched response is `TRANSPORT_STRUCTURAL` |
| 55 | unknown opcode, field count, handle, state and generation each yield `INVALID` with no side effect |
| 56 | the protocol has exactly nine operations and no field carrying a pid, descriptor, path, argv, signal number, symbol or unbounded integer |
| 57 | `SIGNAL_ROLE` and `SIGNAL_GROUP` are refused for `role == WATCHDOG` at every state; **no signal reaches a watchdog on any path** |
| 58 | `SPAWN_WATCHDOG` has one uniform meaning; no replacement-specific opcode, handle role or degradation flag exists |
| 59 | handle ids are never reused; `RELEASE_HANDLE` requires `REAPED`; `SHUTDOWN` refuses while a handle is live |
| 60 | the watchdog never uses `getppid()`; a PCS-death fixture with the supervisor alive produces **no** freeze |
| 61 | supervisor death produces update-pipe EOF and the freeze/observe/exit route |
| 62 | watchdog termination is EOF-driven; `WATCHDOG_UNREAPED` routes to §C10.6 with no signal |
| 63 | `S-1`…`S-7` shutdown ordering; each `S-5` branch behaves as tabulated |
| 64 | PCS death: adoption by the nearest living subreaper else namespace init, `ACCEPTED` journal state, supervisor authority lost, freeze unavailable, watchdog closed out, generation invalid |
| 65 | a PCS started against a non-terminal generation responds `GENERATION_NOT_ADOPTABLE`, acts on nothing, and exits |
| 66 | the supervisor is **not** in the PCS's child set; a wildcard wait in it returns `ECHILD`; no `waitpid(supervisor_pid)` exists in any source |
| 67 | the PCS may signal the supervisor's group only after `c11` has made the group record durable with `group_verified: true` |
| 68 | with a **non-interfering** ancestor subreaper the contract produces identical **decisions and durable records** to a run with none; timing and lifetimes are **not** asserted equal |
| 69 | with an **interfering** adopter (it stops an adopted process) the run **fails closed**: no fabricated death proof, no record removed, generation invalid. **Identical behaviour is not asserted** |
| 70 | a promptly reaped orphan yields `/proc` absence and a recycled pid yields live-with-a-different-identity; both route with **no kill** |
| 71 | an injected `SIGKILL`-terminated adopted process yields a status outside any previously claimed set and changes no decision |
| 72 | no descriptor, handle, opcode or journal authority reaches any adopter |
| 73 | guards `G-1`…`G-5` each reject a bit-exact negative fixture inserted into a copy of `NORMATIVE_BODY` and accept the real one; assert the guards open exactly one file |
| 74 | `G-6`: a one-byte edit inside `NORMATIVE_BODY` changes the digest and fails against the manifest |
| 75 | `S-1`…`S-24b` each reject a bit-exact negative fixture and accept a positive one |
| 76 | `PRODUCTION_ROOTS` has five entries; the scoped map gives each root exactly its set; `generic_harness.py` imports none of `signal`, `_signal`, `sys` |
| 77 | `root_source_sha256` covers all five roots and a one-byte change fails |
| 78 | every §C11.1 safety property S1–S4 is asserted; every §C11.2 liveness item L1–L5 is asserted **as not guaranteed**; no text claims any of L1–L5 |
| 79 | every unknown control outcome settles through §C10.6 and produces no success, capacity, custody, E1/E2/E3 or Q/C fact |
| 80 | the §C12 composition points hold and no scientific or resource rule is changed |

All tests use disposable roots, fake clocks and meters, no production-compatible
real-T artifact, and create no capability, world, learner, entropy, capacity
artifact, custody disposition, result manifest or scientific object. Fixtures
requiring an inherited `SA_NOCLDWAIT` may use `ctypes`, which the runtime
allowlist forbids but which does not govern test fixtures.

---

## §C15. Negative space

This contract creates nothing executable and authorizes no implementation,
commit, host change, verifier edit, manifest, process, socket, pipe, FIFO, fork,
exec, signal, wait, `prctl`, supervisor, controller, worker, watchdog, adapter,
middle child, endpoint, journal instance, spawn record, lease, capability,
operation, framed transport, result manifest, quarantine record, promoted
object, capacity artifact, custody disposition, freeze witness, entropy,
E1/E2/E3 spend, world, learner, candidate, Q attempt, Q/C object, datum,
outcome, Proof, or claim movement. It predicts no qualification and no C1–C6
outcome. Process invalidity, resource exhaustion, missing evidence, the `B`
residual and the receive-path exposure are infrastructure facts and are nowhere
scientific evidence. No example in this document was written to any file.

<!-- OFFICINA-P1-NORMATIVE-END -->

---

## §C16. Non-normative appendices

**Everything below this line is outside `NORMATIVE_BODY` and carries no
operative force.**

<!-- OFFICINA-P1-GUARD-PATTERNS-BEGIN -->

### §C16.1 Guard pattern data (read by the verifier, applied to `NORMATIVE_BODY`)

Each entry is a normalized forbidden substring. The verifier normalizes
`NORMATIVE_BODY` per §C13.2 and reports a violation for any entry that occurs.
This appendix is deliberately outside the target so it is never matched against
itself.

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
G-4 LIVENESS/AUTHORITY:
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
```

<!-- OFFICINA-P1-GUARD-PATTERNS-END -->

### §C16.2 Provenance — complete transitive hash table

**Non-normative.** These documents are historical evidence. **None is read,
parsed, or interpreted for operative behaviour.** They are listed so that a
reviewer can verify that the composite was derived from a byte-intact chain.

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

Every author closure accompanying the documents above is an **untrusted
self-assessment** and none is evidence for anything in this composite.

### §C16.3 Future edit surface

| Path | Permitted change | Status today |
|---|---|---|
| `scripts/officina_process_control_bootstrap.py` | the PCS and its protocol server | **does not exist** |
| `scripts/officina_role_bootstrap.py` | the four-role isolated entry | **does not exist** |
| `src/philosophia/officina/verification.py` | CHANGES 1–5 and rules `S-1`…`S-24b`, `G-1`…`G-6`, and nothing else | unmodified |
| `successor/officina/runtime_control/PRODUCTION_CALL_GRAPH.json` | five roots, the closure, `root_source_sha256`, `p1_composite_sha256`, `p1_composite_normative_sha256` | does not exist |
| `src/philosophia/officina/generic_harness.py` | the launcher, the protocol client, the four role entries, and removal of every `Popen`/`fork`/`waitpid`/`kill`/`killpg` | untracked work in progress — **preserved unmodified** |
| test modules | §C14 | untracked work in progress — **preserved unmodified** |
| everything else | **no change** | byte-unchanged |
