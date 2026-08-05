# Officina supervisor and control channel — P1 operative composite, version 1.10

**This document is the single, complete, self-contained and authoritative
operative specification of the Officina supervisor/control-channel architecture
under the signed selection
`I_SELECT_SUPERVISOR_PROCESS_AUTHORITY_P1_FULL_PCS_MEDIATION`.**

It is a **full replacement** for version 1.8. It is not a delta over version
1.8, it does not require version 1.8 to be read or applied, and after
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
value.** The cell is stated exactly at §P1-13.2 row 2 and nowhere else in this
document. No author closure states it and none may.

**Current external author state, recorded and not treated as authority.** On
2026-08-04 Kirill signed
`successor/OFFICINA_P1_PROCESS_CLAIM_IDENTITY_SELECTION_V1_SIGNATURE.md`
(`7a8ab2da…`), selecting identity Option A,
`I_SELECT_P1_PROCESS_CLAIM_IDENTITY_A_OBSERVATION_ONLY`. **That signature does
not unblock this cell and does not make this version operative.** Its own
outstanding-gates section states that the separately named token
`P1_IDENTITY_OBSERVATION_BOUNDED_WEAKENING_V1` is **not accepted** and must be
reviewed and accepted separately before Option A can become operative. The
signature is **not** a member of `M1`..`M7`, is recorded in no install record,
and is not scientific evidence. §P1-14.4 `XS-1` states exactly what it is, why
it is not a member, and what the later combined binding must do with it. **This
blocking notice therefore stands unchanged.** Version 1.9 does not accept
`P1_IDENTITY_OBSERVATION_BOUNDED_WEAKENING_V1`, does not make it signable, does
not predict it, and does not accept any bounded weakening of the identity
observation under any other name.

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
retained and the other is deleted, in step `OR-4` of the atomic handoff stated
in full at §P1-14.8 of this file and identically at §A9 of the peer amendment;
**no author closure states that step or any other.** The resulting file carries
no variant block at all. A build
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
   1.1, 1.2, 1.3, 1.4, 1.5, 1.6, 1.7 and 1.8 of this composite, together with
   versions 1, 1.1, 1.2, 1.3, 1.4 and 1.5 of the watchdog freeze-authority
   amendment — is immutable historical and provenance evidence only.** No implementer, verifier or reviewer opens any of them for
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
   `successor/OFFICINA_GENERIC_HARNESS_WATCHDOG_FREEZE_AUTHORITY_AMENDMENT_V1_7_DRAFT.md`.
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
`successor/OFFICINA_GENERIC_HARNESS_WATCHDOG_FREEZE_AUTHORITY_AMENDMENT_V1_7_DRAFT.md`
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
manifest. **What that gives, stated as a proper-subset claim and no more:**
while the matching production manifest and the authorization chain of
`§P1-14.4` `TS-1`..`TS-6` remain the ones this generation installed, a change to
any byte of this preamble makes `H_FILE` differ from the manifest's recorded
value and `G-7` refuses. **It does not give more than that.** If the manifest,
Stage A, Stage B, the detached signature, the members and the sole install
record are ALSO replaced together — the complete coherent rollback of `TR-2`
clause (b) — this file's bytes change and no check refuses. No sentence here
claims that an arbitrary byte change is detected. The operative form of the
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
           hmac, json, os, pathlib, re, time, typing, weakref,
           _socket }                                                   16
```

**`subprocess` was removed from the `generic_harness.py` scoped entry in version
1.8, and the reduction is stated in full at `§P1-14.4` `MS-11.5`.** It is not a
new decision: `S-12` of `§P1-14.6` already requires that `subprocess`, `Popen`,
`fork`, `waitpid`, `kill`, `killpg` and `system` appear on no path of that file;
test 8 already requires the launcher to perform no `Popen` statically and
dynamically; and the future-edit surface already requires "removal of every
subprocess, fork, wait, kill and group-kill call" there. A name no conforming
build may use may not remain in the allowlist that authorizes its import. **The
nineteen-member global default above is UNCHANGED and still contains
`subprocess`**, so `scripts/officina_activate_t.py` and
`scripts/verify_officina_active.py`, which have no scoped entry, are unaffected.
**The two bootstrap scoped entries are unchanged.** The launcher reaches
`posix_spawn` through the bound primitive of `§P1-3.4`, never through
`subprocess`, exactly as `S-11` and `S-12` already require.

**The history, stated in order, because the v1.8 note read as if `subprocess`
had never been permitted.** (1) The accepted generic-harness chain DOES grant a
CPU launcher capability that uses `subprocess` with `start_new_session=True`
together with `os.killpg`; that grant is real and is not denied here. (2) The
later signed P1 architecture SUPERSEDED that launch route: `§P1-7.1` launches
through the bound `_posix_spawn` primitive of `§P1-3.4`, `S-11` fixes its
argument shape, `S-12` forbids `subprocess`, `Popen`, `fork`, `waitpid`, `kill`,
`killpg` and `system` on every path of `generic_harness.py`, and test 8 forbids
the fork/`Popen`/shell route dynamically as well as statically. (3) Removing
`subprocess` from this one scoped allowlist is therefore **a bookkeeping
consequence of the earlier P1 rescope, not the source of it, and not a
retroactive claim that the capability was never granted.** No P1-conforming
implementation could have used the removed name, so no admissible
implementation, option, acceptance predicate or scientific cell changes.

**Why the reduction is load-bearing rather than tidy.** `generic_harness.py` is
imported inside every role at `§P1-7.4` `A-10`. With `subprocess` in its
allowlist, the modules `threading`, `signal`, `select` and `selectors` — four
names this section itself calls permitted in no file — become transitively
resident in every role process, **and `threading`'s module-level code calls
`os.register_at_fork`**. `MS-11.5` records that finding and the eight modules
the reduction removes.

`signal`, the pure-Python wrapper, is permitted in no file. **The rationale
printed here through version 1.8 — that its import closure "pulls `functools`
and hence `_thread`" — is withdrawn as factually obsolete on the pinned build,
and is replaced rather than left standing with a later contradiction.** On the
pinned interpreter `_thread` is already resident in the start-up module table
before any file of this contract is imported, so no allowlist choice makes it
absent from a process, and `functools` is in any case reached by permitted
seeds. **The operative reason `signal` is excluded is the one that survives
measurement:** importing it replaces module-level bindings for handler
installation and enum conversion in a role process, the contract installs and
inspects signal disposition only through the built-in `_signal` and the §P1-7.2
`P-g` preflight, and a second route to that state is a second writer. `_signal`
is used instead.
`sys` and `_signal` are permitted only in a file with a scoped entry.
`threading`, `_thread`, `multiprocessing`, `concurrent`, `asyncio`, `ctypes`,
`select`, `selectors`, `socket`, `array`, `struct`, `atexit`, `gc` and any
`prctl` binding are permitted in no file. **That rule is unchanged and is not
weakened by the correction above:** none of those names is in any allowlist, and
`§P1-14.4` `MS-11.3` records that `_thread`'s residency is a property of the
interpreter rather than of any allowlist.

### §P1-3.3 The PCS import closure, audited

| Module | Kind | Transitive Python closure at import | Starts a task? | Registers an at-fork callback? | Installs a handler or hook? |
|---|---|---|---|---|---|
| `os` | Python wrapper over built-in `posix` | `sys`, `abc`, `stat`, `_collections_abc`, `posixpath`, `genericpath` | no | it defines `register_at_fork` and never calls it | no |
| `sys` | built-in | none | no | no | no |
| `_signal` | built-in | none | no | no | no |
| `time` | built-in | none | no | no | no |
| `fcntl` | built-in | none | no | no | no |
| `_socket` | built-in | none | no | no | no |

**This table is a human-readable audit aid, it covers the PCS bootstrap root
only, and it is not the canonical value.** The canonical value is `§P1-14.4`
`MS-11.1`, which carries EIGHTY-NINE modules: the closed transitive closure of
all THREE scoped allowlists of `§P1-3.2` — the six above, the role bootstrap's
three, and the sixteen of `generic_harness.py`, which `§P1-7.4` `A-10` imports
inside every role. The six rows above and the eight modules they reach —
`_abc`, `_collections_abc`, `_stat`, `abc`, `genericpath`, `posix`, `posixpath`
and `stat` — appear in `MS-11.1` with byte-identical `kind` and
`transitive_imports` values. `MS-11.1` also maps this table's human "Kind"
vocabulary onto the four `kind` literals of `MS-4`: "built-in" here is `BUILTIN`
there, and `os`'s "Python wrapper over built-in `posix`" describes its
implementation and delegation, while its `kind` records its load origin on the
pinned build, which is `FROZEN`. The three columns "Starts a task?", "Registers
an at-fork callback?" and "Installs a handler or hook?" are the three booleans
`MS-11` derives and pins; every one of them is false, and `os` "defines
`register_at_fork` and never calls it" is exactly `MS-11`'s
defining-is-not-calling rule. **Where this table and `MS-11.1` differ in any
respect, `MS-11.1` governs**, and `MS-11.1` is complete where this table is not:
the modules named in the closure column above are not rows of this table, which
is why `MS-4`'s self-closure rule could not be satisfied from this table alone.
**This table says nothing about the role import surface**, which is what
`A-10` creates and what `MS-11` now covers. **It likewise says nothing about the
four PROJECT modules that `A-10` necessarily executes before the role module** —
`philosophia`, `philosophia.officina`, `philosophia.officina.canonical` and
`philosophia.officina.interlock` — which are digest-bound, effect-asserted and
order-pinned at `§P1-14.4` `MS-13` — where each of the four carries an
eight-key `import_time_effects` object whose booleans are all false — are
**not** production roots, **not** members and **not** rows of `MS-11.1`.

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

**`G-11` IS THE ONE EXPLICIT EXCEPTION, AND ITS INPUT SET IS A LITERAL CLOSED
SET.** The joint-install guard cannot be a one-file guard, because what it
checks is precisely that a SET of files was installed together. Its input set is
enumerated exhaustively at §P1-14.4 `MS-1` through `MS-7` as **fifty-seven
literal repository paths in seven pairwise-disjoint classes**, each with an
exact cardinality, each identified by a path string that appears verbatim in
these governing bytes. It contains **no wildcard, no glob, no directory scan, no
adjective, no path supplied by the install record or the manifest, and no
future-edit table entry**. `MS-9` proves the seven classes pairwise disjoint by
path. `G-11` reads those bytes ONLY to hash them and never interprets any of
them as a rule, so the categorical exclusion of historical documents from
BEHAVIOUR is not weakened: **verifying a digest is not opening a document for
behaviour.**

**The two author-authorization artifacts are not inputs of any other guard.**
Stage A and Stage B (§P1-14.4 `TS-1`, `TS-3`) are read by `G-11` alone, are
outside `M1`..`M7`, and are read only to validate their bytes and verify one
detached signature — never for behaviour.

**`G-11` is a FINAL-STATE verifier and claims nothing about history.** It
evaluates a predicate over the bytes present when it runs. §P1-14.4 `FS-1`
states exactly what a passing run proves; `FS-2` states what it cannot prove and
withdraws every earlier claim that it reconstructs construction order; `FS-3`
keeps `OR-1`..`OR-11` a mandatory operator obligation regardless; `FS-4` fails
closed on a contemporaneously observed violation; and `FS-5` places an
unobserved violation inside the declared residual of `TR-2`. **No hardware
security module, external service, timestamp oracle, notary or transparency log
is introduced, permitted or implied.**

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
     requires a new signed and reviewed version.
     THE SCOPE OF THIS GUARD, STATED AS A PROPER SUBSET. G-6 compares this
     file's live regions with THE VALUES THE CURRENT MANIFEST RECORDS. It
     therefore refuses an edit to either normative region WHILE the matching
     manifest and the TS-1..TS-6 authorization chain remain the ones this
     generation installed. It does NOT refuse an edit made together with a
     matching replacement of the manifest, Stage A, Stage B, the detached
     signature, the members and the sole install record: that is TR-2 clause
     (b), complete coherent rollback, which reaches a runnable state and is not
     refused. Even if a wording guard failed to match a novel phrasing of a
     withdrawn overclaim, the region edit alone changes a digest and is refused
     under that condition. NO STRONGER CLAIM IS MADE HERE, AND VERSION 1.6'S
     UNQUALIFIED "cannot pass unnoticed" IS WITHDRAWN.
G-7  Recompute H_FILE and compare it with the manifest's p1_composite_sha256.
     Any mismatch ⇒ "guard G-7: composite file digest differs".
     This covers the non-normative provenance region as well, so a change to
     any byte of this file — preamble, either normative region, or provenance —
     is refused UNDER THE SAME CONDITION AS G-6: that the matching manifest and
     authorization chain are not replaced along with it. Under complete
     coherent rollback (TR-2 clause (b)) they are replaced along with it and
     nothing refuses. VERSION 1.6'S UNQUALIFIED "no byte of the file can change
     without detection" IS WITHDRAWN as exceeding TR-2.
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
G-11 JOINT INSTALL COMPLETENESS AND TWO-STAGE AUTHOR AUTHORIZATION — THE
     FAIL-CLOSED GATE. This is the P1 statement of the install record and of
     the author authorization of §A10 of the peer amendment. THE TWO ARE ONE
     RULE WITH TWO STATEMENTS. The normative block delimited below is carried
     BYTE-IDENTICALLY in §A10 of the peer amendment; a reviewer may extract the
     two spans and compare them directly, and any difference between them is a
     defect in this indivisible pair.
     `G-11` is the ONE exception to the one-file rule of §P1-14.1. Its input
     set is the literal closed set of `MS-1`..`MS-7` below and nothing else.
     `G-11` is INDEPENDENT of `G-10`: neither is a precondition of the other,
     and each fails closed on its own.
     `G-11` DEFINES NO WATCHDOG MECHANISM, NO TREATMENT, NO EVIDENCE CLASS AND
     NO AUTHOR OPTION. It is process integrity only.
     `G-11` IS A FINAL-STATE VERIFIER. `FS-1` below states exactly what it
     proves; `FS-2` states what it cannot prove and withdraws every version-1.2
     claim to the contrary; `TR-2` states the two residual clauses it does not
     close. No sentence of this guard, of the peer amendment, of any packet or
     of any closure may claim more than `FS-1` and `TR-2` allow.

--- BEGIN JOINT INSTALL AND AUTHORIZATION BLOCK - BYTE-IDENTICAL IN BOTH GOVERNING FILES ---

MS-0  CANONICAL ENCODING, ONE DEFINITION, USED BY EVERY ARTIFACT BELOW.
      CANON(v) := the bytes obtained by serializing the JSON value v with
        object keys sorted ascending by Unicode code point;
        no whitespace anywhere outside string literals;
        the one-character separators "," between items and ":" between a key
        and its value;
        every character outside printable ASCII escaped as \uXXXX, so the
        output is pure ASCII;
        no NaN, no Infinity and no floating-point number of any kind;
        every integer written in decimal with no exponent and no decimal
        point;
      followed by exactly one 0x0A byte and nothing after it.
      ARRAY ORDER IS PART OF THE VALUE AND IS NEVER SORTED BY CANON. Wherever
      an array appears below, its required order is stated with it; a
      differently ordered array is a DIFFERENT value with a different digest.
      THIS INTRODUCES NO NEW ENCODING. It reproduces exactly the canonical
      form Officina already uses for every hashed artifact.
      A file whose bytes are required to be canonical is REJECTED unless its
      bytes are byte-identical to CANON of the value they parse to. Parsing a
      file and re-serializing it is not a repair: the bytes on disk are the
      artifact.
      Every SHA-256 value in every artifact below is written as exactly 64
      characters, each one of 0123456789abcdef. Every path is
      repository-relative, uses the 0x2F separator, and is compared byte for
      byte. Every boolean is the JSON literal true or false. Every integer is
      a JSON number with no fractional part and no exponent.

MS-1  M1 GOVERNING SPECIFICATION. CARDINALITY EXACTLY 2. The two literal
      paths, and no others:
        successor/OFFICINA_GENERIC_HARNESS_WATCHDOG_FREEZE_AUTHORITY_AMENDMENT_V1_7_DRAFT.md
        successor/OFFICINA_GENERIC_HARNESS_SUPERVISOR_CONTROL_CHANNEL_P1_OPERATIVE_COMPOSITE_V1_10.md
      Both are taken in their POST-SELECTION bytes: the composite after every
      variant block has been resolved to the signed branch and the other
      branch deleted (OR-4), the amendment as installed. The digest of each is
      the SHA-256 of the whole file's bytes as found on disk, with no
      normalization and no exclusion of any region.
      NO OTHER PATH IS IN M1, AND NEITHER OF THESE TWO PATHS IS IN ANY OTHER
      CLASS.

MS-2  M2 IMMUTABLE PROVENANCE SET. CARDINALITY EXACTLY 55. THE LIST BELOW IS
      LITERAL, EXHAUSTIVE, AND IS THE ONLY SOURCE OF M2. The provenance region
      of the composite is NOT read to construct M2, no directory is scanned,
      no adjective is interpreted, and no path is taken from the install
      record, from the manifest or from any future-edit table. An omission and
      an extra member are equally fatal. Each row is a recorded SHA-256
      followed by two spaces followed by the literal path; the recorded digest
      is the value that member MUST still have on disk.
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
        4afca93172a39cb8924b48285965a791707cec71330b2a8f81328961f92ec01a  successor/OFFICINA_BATCH_SETTLEMENT_CORE_AMENDMENT_V1_DRAFT.md
        3ce629ed5afe567b5aba936906c114008df989acb1a946443a6ede1e31dca7de  successor/OFFICINA_BATCH_SETTLEMENT_CORE_AMENDMENT_V1_1_CORRECTION.md
        ae9c440acaaba90f2cb669e5a8212082f4c0f25b5b7e31ebc906b9cbc0ad6132  reviews/officina_supervisor_v2_1_authorship_note.md
        70df01e8af25303600425434353a707571354e385fff78e1663f30494cf4b7ac  reviews/opus_officina_supervisor_p1_final_xy_review.md
        75002efea91c3960adb5bc2bfa4dcdacecdb45a1add14f3f2fc1dd300e591b1b  reviews/sol_officina_supervisor_p1_final_xy_review.md
        daeef9b3a349aba48b126957ff027d946b7ad094e5c03c3c2ede717f27a660e6  successor/officina/T_ENVELOPE.json
        ec5ddff8f8d09c1574a56d173579a6b585a8f9de230afb86e43d9415fb7a4390  successor/OFFICINA_GENERIC_HARNESS_WATCHDOG_FREEZE_AUTHORITY_AMENDMENT_V1_1_DRAFT.md
        c904ec4318485acd49a6128ca32f9e52fe523c3703b730351f8ad98adb3e60f1  successor/OFFICINA_GENERIC_HARNESS_SUPERVISOR_CONTROL_CHANNEL_P1_OPERATIVE_COMPOSITE_V1_4.md
        bd8147a5085096c6a08ec0fec40ad22df23d55f23f77e3349218b3da93b6b2ba  reviews/fable_officina_p1_watchdog_v2_4_independent_x_confirmation.md
        3fab1b09e2724534b2b5a080fbfeb98cc861cbe3b9764790084dfec050944a05  reviews/sol_officina_p1_watchdog_v2_4_final_y_confirmation.md
        058c119c5de770dc537fd16962723063d2c3d4dad5da17d1431d4402927ebd1b  successor/OFFICINA_GENERIC_HARNESS_WATCHDOG_FREEZE_AUTHORITY_AMENDMENT_V1_2_DRAFT.md
        8751317511a3f738de35402b3c67ab9786e7fe1c95ea12d1e175ddd6540ddb20  successor/OFFICINA_GENERIC_HARNESS_SUPERVISOR_CONTROL_CHANNEL_P1_OPERATIVE_COMPOSITE_V1_5.md
        c2e9ddb2e6270f2b870986b01d1114ea68d5f3e1db466f165ee2f47a0f256427  reviews/fable_officina_p1_watchdog_v2_5_independent_x_confirmation.md
        80d42229b2e9b32e51a5448c10af410640e2088f777334fa4431f29e4e840c81  reviews/sol_officina_p1_watchdog_v2_5_final_y_confirmation.md
        c3da2a7d24d0cea025f014f9231c0b856318b4a4c11ffc40c66972e7f905b3d1  successor/OFFICINA_GENERIC_HARNESS_WATCHDOG_FREEZE_AUTHORITY_AMENDMENT_V1_3_DRAFT.md
        6283d081df3eb3978bf963820859a5ebbf125689a4a3e249d3e85c1ca8d3d49d  successor/OFFICINA_GENERIC_HARNESS_SUPERVISOR_CONTROL_CHANNEL_P1_OPERATIVE_COMPOSITE_V1_6.md
        e334d7e4a93979f07a8d651a1dd32039027d0536e2d6259ae5a6ec36dc09a363  reviews/fable_officina_p1_watchdog_v2_6_independent_x_confirmation.md
        283666b75dc7fee8af7cde90ab761a734cc554aceca1f5b124c318d2ce8115b9  reviews/sol_officina_p1_watchdog_v2_6_final_y_confirmation.md
        f845b98dcef0edc415420fec1103f7adad4f905c21380a0dddcba0d3b370b794  successor/OFFICINA_GENERIC_HARNESS_WATCHDOG_FREEZE_AUTHORITY_AMENDMENT_V1_4_DRAFT.md
        5301f7e987b768cc3acd9641f6f00400a74b453773299cbd379473c7db569beb  successor/OFFICINA_GENERIC_HARNESS_SUPERVISOR_CONTROL_CHANNEL_P1_OPERATIVE_COMPOSITE_V1_7.md
        4855020e522228eeb0625fba1efb78941bc547c124da2d1dbb754b548d3057cc  reviews/fable_officina_p1_watchdog_v2_7_independent_x_confirmation.md
        0b33108e885fec97ab11e2de5c6ac3ba6ceeb8e98283bb29a09c70ce1c574780  reviews/sol_officina_p1_watchdog_v2_7_final_y_confirmation.md
        28b57c47f89f775199095717111e37a4e588628aa64b2801812f30814711efd4  successor/OFFICINA_GENERIC_HARNESS_WATCHDOG_FREEZE_AUTHORITY_AMENDMENT_V1_5_DRAFT.md
        6b867790707ae7999b31c1ad3dd56a1d4b195efd8f7a8b2bda4c2b065a352176  successor/OFFICINA_GENERIC_HARNESS_SUPERVISOR_CONTROL_CHANNEL_P1_OPERATIVE_COMPOSITE_V1_8.md
        ddd6d63aac69a6e3003fe7880ac7e5cbfe9f74cdb64b6f1d0716750795d8e8e9  reviews/fable_officina_p1_watchdog_v2_8_independent_x_confirmation.md
        88efa91dcb9142483cab6f832088ee3d19c51eb79ba20335deb84e005ea90a46  reviews/sol_officina_p1_watchdog_v2_8_final_y_confirmation.md
      M2 CONTAINS NONE OF THE SEVEN M3 PATHS AND DOES NOT CONTAIN
      src/philosophia/officina/verification.py. M2 IS A LITERAL LIST, NOT THE
      PROVENANCE REGION MINUS AN EXCEPTION, so no later provenance row can
      silently enter it.

MS-3  M3 ACCEPTED PEER CHAIN. CARDINALITY EXACTLY 7. The five generic-harness
      contract files, the generic-harness signature and the effective
      batch-settlement amendment, as literal paths with recorded digests:
        64b8d3f63594b79a6abc767a032383c5704beaf09b32a1e0c58fdc444bb0af71  successor/OFFICINA_GENERIC_HARNESS_CONTRACT_V2_DRAFT.md
        6bbaf4d17295a8a4d4fa0f42a9347707e4e2319ea5183163c756b94008764077  successor/OFFICINA_GENERIC_HARNESS_CONTRACT_V2_1_CORRECTION.md
        624dfc9b34c8009ee4c1610bfff91f5cfceea128e84d850c3e90ffb1e7be9e2f  successor/OFFICINA_GENERIC_HARNESS_CONTRACT_V2_2_CORRECTION.md
        b2288b0a9fb44d23c19d853aeb6d57edd4de888c6058af8001a379f9237d3154  successor/OFFICINA_GENERIC_HARNESS_CONTRACT_V2_3_CORRECTION.md
        724d633a55668013b78058eed1c76e12e9bbaf487f71ea94b7a4568ea1ced8a0  successor/OFFICINA_GENERIC_HARNESS_CONTRACT_V2_3_1_CORRECTION.md
        8c47da352ef5954406964647a32e97939c404806bdf9b3d3ff5bc70866e6369a  successor/OFFICINA_GENERIC_HARNESS_SIGNATURE.md
        b5a1523290b6b8417a7b3288329cc4a4e5ff80214c8f28e6ea1ae51a450a94c9  successor/OFFICINA_BATCH_SETTLEMENT_CORE_AMENDMENT_V1_1_1_CORRECTION.md
      THE EFFECTIVE BATCH-SETTLEMENT AMENDMENT IS v1.1.1 AND ONLY v1.1.1. The
      v1 and v1.1 batch-settlement documents are provenance and are in M2, not
      in M3.

MS-4  M4 PRODUCTION MANIFEST. CARDINALITY EXACTLY 1. Literal path:
        successor/officina/runtime_control/PRODUCTION_CALL_GRAPH.json
      ENCODING: the file bytes are exactly CANON of the object (MS-0).
      The top-level value is a JSON object whose key set is EXACTLY the
      twenty-one keys below — no extra key, no missing key — with exactly these
      types and value grammars:

        schema              STRING, exactly
                            "philosophia.officina.t-production-call-graph.v1"
        version             INTEGER, exactly 1
        roots               ARRAY of exactly 5 STRINGS, each a literal
                            production-root path of §P1-3.1 of the composite,
                            IN THAT SECTION'S ORDER, pairwise distinct. The
                            array is NOT sorted; its order is §P1-3.1's order.
        root_source_sha256  OBJECT whose key set is EXACTLY the five strings
                            of "roots" and whose every value is a 64-character
                            lowercase hexadecimal STRING
        reachable_closure   ARRAY, see the canonical shape below
        p1_composite_sha256            64-char lowercase hex STRING
        p1_composite_body_sha256       64-char lowercase hex STRING
        p1_composite_guarddata_sha256  64-char lowercase hex STRING
        p1_composite_normative_sha256  64-char lowercase hex STRING
        peer_amendment_sha256          64-char lowercase hex STRING
        pre_selection_packet_path      STRING, exactly TS-1's packet path
        pre_selection_packet_sha256    64-char lowercase hex STRING
        pre_selection_amendment_path   STRING, exactly TS-1's amendment path
        pre_selection_amendment_sha256 64-char lowercase hex STRING
        pre_selection_composite_path   STRING, exactly TS-1's composite path
        pre_selection_composite_sha256 64-char lowercase hex STRING
        stage_a_path        STRING, exactly TS-1's Stage-A path
        stage_a_sha256      64-char lowercase hex STRING
        stage_a_key_id      64-char lowercase hex STRING
        project_import_dependencies
                            OBJECT, the closed project-import dependency
                            surface of MS-13. Its exact shape, its four
                            SIX-KEY elements, their eight-key boolean
                            import_time_effects objects and their required
                            values are MS-13's; the structural phase checks the
                            shape at every depth and CK-10 checks the values.
                            ADDED IN VERSION 1.6; ITS ELEMENT GAINED THE SIXTH
                            KEY IN VERSION 1.7.
        created_utc         STRING satisfying MS-10

      THE TABLE ABOVE IS THE STRUCTURAL PHASE AND IS NOT THE WHOLE PREDICATE.
      It fixes JSON types, lexical grammars and the two mandatory literals
      (schema, version) and NOTHING ELSE. EVERY OTHER VALUE ABOVE ALSO HAS A
      SEMANTIC SOURCE, and a value that is well typed but factually wrong is
      NOT admissible: MS-12 states the semantic source of every one of the
      TWENTY-ONE keys field by field, VP-3 names its single owning clause and
      its single failure code, and CK-9 and CK-10 evaluate them. Version 1.3
      stated the types and left five of THE TWENTY SEMANTIC RELATIONS IT THEN
      HAD unchecked; those five are peer_amendment_sha256, the three
      pre_selection_*_sha256 values and reachable_closure, and MS-11, MS-12,
      CK-9 and CK-10 close all five.
      THE LIVE KEY SET HAS BEEN TWENTY-ONE SINCE VERSION 1.6 ADDED
      project_import_dependencies. Version 1.6 nevertheless still called the
      live manifest a twenty-key object here and at VP-3; BOTH SENTENCES ARE
      CORRECTED IN VERSION 1.7 AND NO SENTENCE OF THIS PAIR NOW DESCRIBES THE
      LIVE MANIFEST AS HAVING TWENTY KEYS.

      reachable_closure — ONE CANONICAL JSON SHAPE, REPLACING THE PROSE TABLE.
      Composite §P1-3.3 is a human-readable audit table and is NOT a canonical
      value; this is. reachable_closure is an ARRAY of OBJECTS. It is
      non-empty. Every element has EXACTLY these six keys:
        module              STRING, a Python module name as it appears in an
                            import, of one or more characters from
                            0-9 A-Z a-z _ . and beginning with a letter or _
        kind                STRING, exactly one of the four literals
                            "BUILTIN", "FROZEN", "EXTENSION", "PURE_PYTHON"
        transitive_imports  ARRAY of STRINGS, each a module name of the same
                            grammar, SORTED ASCENDING by Unicode code point,
                            PAIRWISE DISTINCT, possibly empty
        starts_task         BOOLEAN
        registers_at_fork   BOOLEAN
        installs_handler    BOOLEAN
      ARRAY ORDER: the elements are SORTED ASCENDING by the "module" value
      compared byte for byte. UNIQUENESS: the "module" values are pairwise
      distinct across the array. CLOSURE: every string occurring in any
      element's transitive_imports also occurs as the "module" value of some
      element of the same array — the closure is closed under itself.
      Two independent implementations given the same audited closure therefore
      emit the same bytes, because the element key set, the element order, the
      inner array order and the canonical encoding are all fixed.
      THE SHAPE ABOVE IS NOT THE VALUE, AND VERSION 1.3 PINNED ONLY THE SHAPE.
      A structurally valid, internally closed, sorted array whose modules,
      kinds, transitive imports or booleans are factually wrong satisfied every
      version-1.3 rule. MS-11 fixes THE ONE CANONICAL EXPECTED VALUE, literally
      and completely, and CK-10 — NOT CK-7 — REQUIRES EQUALITY WITH IT.
      VERSION 1.6 STILL SAID CK-7 IN THIS SENTENCE, AND THE SENTENCE IS
      WITHDRAWN AS AN UNDEFINED PREREQUISITE. CK-7 runs BEFORE CK-8 has proved
      M4 parseable, an object, exactly keyed and correctly typed, so at CK-7
      there is no M4 field to read and no closure value to compare. CK-7
      ESTABLISHES M4's EXISTENCE AS A MEMBER AND RECOMPUTES ITS MEMBER-BYTE
      DIGEST, AND DOES NOTHING ELSE TO M4: it does not parse M4, does not read
      any M4 key, and value-compares no M4 field, reachable_closure included.
      The single owner of the closure equality is CK-10, and VP-3, VP-4
      position 10, MS-11.4 and IR-13 already said so; only this sentence
      disagreed.

      THE MANIFEST CARRIES NO DIGEST OF ITSELF. The four p1_composite_* fields
      carry exactly the meanings CHANGE 5 already assigns them and nothing
      about them moves; the three pre_selection_* path/digest pairs and the
      three stage_a_* fields are the bindings TS-2 checks.

MS-5  M5 POST-HANDOFF VERIFIER. CARDINALITY EXACTLY 1. Literal path:
        src/philosophia/officina/verification.py
      DIGEST RULE: the SHA-256 of the entire file's bytes exactly as found on
      disk — no normalization, no line-ending translation, no whitespace
      stripping, no comment stripping, no compilation, and no exclusion of any
      region. The digest is of bytes, never of an abstract syntax tree.
      The bytes at this path BEFORE the handoff are the non-enforced
      pre-install baseline named in the provenance region; they are NOT M5.
      M5 is the bytes at this path after OR-5. The baseline digest appears in
      MS-2 nowhere and is compared by nothing.

MS-6  M6 TEST BUNDLE. CARDINALITY EXACTLY 2, IN THIS FIXED ORDER, which is not
      sorted and is not re-derived:
        1. tests/test_officina_p1_freeze_authority.py     carries rows 92..103
        2. tests/test_officina_p1_install_integrity.py    carries rows 104..115
      MEMBERSHIP RULE FOR ROWS 92..115, EXACT AND MECHANICAL:
        for every integer r with 92 <= r <= 115 there is EXACTLY ONE
        module-scope function, in EXACTLY ONE of the two modules, whose name
        begins with "test_p1_row_" followed by r written as three decimal
        digits with a leading zero where needed, followed by "_";
        rows 92 through 103 occur only in module 1;
        rows 104 through 115 occur only in module 2;
        no function name of that form exists for any integer outside 92..115;
        no row number occurs twice within a module or across the two;
        the count of such functions is therefore exactly 24, twelve per module.
      Each module is its own member with its own SHA-256 over its whole bytes,
      so M6 contributes exactly two entries to the member list.
      CANONICAL BUNDLE DIGEST — used only by M7 and never as a member digest:
        test_bundle_digest = SHA-256( CANON( {
          "schema": "philosophia.officina.t-p1-test-bundle-digest.v1",
          "modules": [ {"path": <module 1 path>, "sha256": <module 1 digest>},
                       {"path": <module 2 path>, "sha256": <module 2 digest>} ]
        } ) )
      "modules" is an ARRAY of exactly two OBJECTS, each with EXACTLY the two
      keys path and sha256, both STRINGS, in the order above. Swapping them
      produces a different digest and is a refusal, not a normalization.

MS-7  M7 PASSING ATTESTATION. CARDINALITY EXACTLY 1. Literal path:
        successor/officina/runtime_control/INSTALL/T_WATCHDOG_AUTHORITY_TEST_ATTESTATION_V1.json
      ENCODING: the file bytes are exactly CANON of the object (MS-0).
      The top-level value is a JSON object whose key set is EXACTLY the ten
      keys below, with exactly these types and value grammars:

        schema               STRING, exactly
                             "philosophia.officina.t-watchdog-authority-test-attestation.v1"
        version              INTEGER, exactly 1
        verifier_path        STRING, exactly MS-5's literal path
        verifier_sha256      64-char lowercase hex STRING, the digest of the
                             M5 bytes FOUND ON DISK
        test_bundle_modules  ARRAY of exactly 2 OBJECTS, each with EXACTLY the
                             two keys path and sha256, both STRINGS, the
                             sha256 being 64 lowercase hex characters. The
                             array order is MS-6's fixed order: element 0 is
                             module 1, element 1 is module 2. It is NOT sorted.
                             Each path equals MS-6's corresponding literal
                             path; each sha256 is the digest of that module's
                             bytes FOUND ON DISK.
        test_bundle_digest   64-char lowercase hex STRING, equal to MS-6's
                             canonical bundle digest recomputed from the two
                             entries of test_bundle_modules
        rows_attested        ARRAY of exactly 24 INTEGERS, strictly ascending,
                             first element 92, last element 115, each element
                             one greater than its predecessor — that is,
                             exactly 92,93,94,...,115
        row_count            INTEGER, exactly 24, and equal to the length of
                             rows_attested
        all_rows_passed      BOOLEAN, exactly true. The value false is not
                             installable and no other value validates.
        created_utc          STRING satisfying MS-10

      THE ATTESTATION CARRIES NO DIGEST OF ITSELF AND NAMES NO INSTALL RECORD.
      It therefore cannot attest the set that contains it.

MS-8  TOTAL MEMBER CARDINALITY, EXACT:
        M1 2 + M2 55 + M3 7 + M4 1 + M5 1 + M6 2 + M7 1 = 69
      The install record's member list has exactly 69 entries. A list of any
      other length fails before a single digest is compared.

MS-9  PAIRWISE DISJOINTNESS, PROVED BY PATH RATHER THAN ASSERTED.
      Every member is identified by one repository-relative path. Two classes
      are disjoint if and only if their path sets share no element. Write
      P(Mi) for the path set of class Mi:
        P(M1) the two literal strings of MS-1
        P(M2) the 55 literal strings of MS-2
        P(M3) the 7 literal strings of MS-3
        P(M4) { successor/officina/runtime_control/PRODUCTION_CALL_GRAPH.json }
        P(M5) { src/philosophia/officina/verification.py }
        P(M6) { tests/test_officina_p1_freeze_authority.py ,
                tests/test_officina_p1_install_integrity.py }
        P(M7) { successor/officina/runtime_control/INSTALL/T_WATCHDOG_AUTHORITY_TEST_ATTESTATION_V1.json }
      There are twenty-one unordered pairs. They are settled in three groups.
        GROUP 1, twelve pairs, {M1,M2,M3} against {M4,M5,M6,M7}.
          Every element of P(M1), P(M2) and P(M3) begins with the eight bytes
          "reviews/" or with the nineteen bytes "successor/OFFICINA_" or is
          exactly the string successor/officina/T_ENVELOPE.json. No other form
          occurs in those three lists, and this is checkable by inspecting the
          64 literal strings above.
          Every element of P(M4) and P(M7) begins with the thirty-five bytes
          "successor/officina/runtime_control/". That prefix is not
          "successor/OFFICINA_" — their eleventh bytes are 0x6F and 0x4F and
          differ — is not "reviews/", and is not the T_ENVELOPE string, which
          has no runtime_control component.
          Every element of P(M5) begins with "src/" and every element of P(M6)
          begins with "tests/"; neither prefix occurs in the first three lists.
          All twelve pairs are therefore disjoint.
        GROUP 2, six pairs, among {M4,M5,M6,M7}.
          P(M5) begins with "src/", P(M6) with "tests/", P(M4) and P(M7) with
          "successor/", so M5 and M6 are disjoint from each other and from M4
          and M7 — five of the six pairs.
          For the sixth, M4 against M7: after the shared prefix
          "successor/officina/runtime_control/" the M4 remainder begins with
          the byte 0x50 ("P") and the M7 remainder with the byte 0x49 ("I"),
          so the two strings differ at that position and the sets are
          disjoint.
        GROUP 3, three pairs, among {M1,M2,M3}.
          M1 against M2: M1's two strings end in _V1_7_DRAFT.md and
          _COMPOSITE_V1_10.md. MS-2's list carries the amendment at
          _V1_DRAFT.md, _V1_1_DRAFT.md, _V1_2_DRAFT.md, _V1_3_DRAFT.md,
          _V1_4_DRAFT.md and _V1_5_DRAFT.md, and the composite at _V1, _V1_1,
          _V1_2, _V1_3, _V1_4, _V1_5, _V1_6, _V1_7 and _V1_8, and carries no
          _V1_7_DRAFT amendment and no _V1_10 composite. Disjoint.
          M1 against M3: MS-3's seven strings are the harness contract chain,
          the harness signature and the batch-settlement amendment v1.1.1;
          none is an amendment-v1.7 or composite-v1.10 path. Disjoint.
          M2 against M3: MS-2 and MS-3 are two literal lists, and the
          intersection of the 55 strings with the 7 strings is empty.
      Twelve plus six plus three is twenty-one, so every pair is settled. The
      union of the seven sets has 2+55+7+1+1+2+1 = 69 distinct paths, equal to
      MS-8, so no path is counted twice and no member is unassigned. THE SEVEN
      CLASSES ARE PAIRWISE DISJOINT AND THEIR UNION IS THE COMPLETE INSTALLED
      SET. There is no eighth class.
      THE PACKET IS NOT A MEMBER AND DOES NOT DISTURB THIS PROOF. TS-2 A16(b)
      recomputes the SHA-256 of the bytes at TS-1's literal packet path. That
      path is in none of the seven literal lists above, it is added to none of
      them, and hashing a file is not making it a member (IR-12, N-14). CK-4
      still enumerates 69 members from MS-1..MS-7 alone.
      THE FOUR PROJECT-IMPORT DEPENDENCIES OF MS-13 ARE LIKEWISE NOT MEMBERS AND
      DO NOT DISTURB THIS PROOF. They are bound by digest inside the M4 manifest,
      which is itself a member; their paths are in none of the seven literal
      lists, they are added to none of them, they supply no path to CK-4, and
      MS-8's cardinality is unaffected. N-16 says so.

MS-10 THE created_utc GRAMMAR AND ITS VALIDATOR, ONE DEFINITION USED WHEREVER
      THE FIELD APPEARS — MS-4, MS-7, IR-3, TS-1 and TS-3.
      GRAMMAR, exact: the value is a STRING of EXACTLY 20 ASCII characters
      matching
        YYYY "-" MM "-" DD "T" hh ":" mm ":" ss "Z"
      where YYYY is four decimal digits and MM, DD, hh, mm and ss are each two
      decimal digits, and the six literal separators are exactly the bytes
      0x2D, 0x2D, 0x54, 0x3A, 0x3A and 0x5A in those positions. THERE IS NO
      FRACTIONAL PART, no offset other than the literal Z, no lowercase t or
      z, no space, and no leading or trailing byte.
      SEMANTIC VALIDATOR, exact:
        2000 <= YYYY <= 2999
        1 <= MM <= 12
        1 <= DD <= the number of days in month MM of year YYYY under the
          proleptic Gregorian calendar, where YYYY is a leap year if and only
          if it is divisible by 4 and not by 100, or is divisible by 400
        0 <= hh <= 23
        0 <= mm <= 59
        0 <= ss <= 59 — NO LEAP SECOND IS ACCEPTED; ss equal to 60 is invalid
      A value failing the grammar or the validator makes its artifact invalid
      and is refused with that artifact's own failure code.
      created_utc IS PROVENANCE ONLY AND IS NOT TRUSTED TEMPORAL-ORDER
      EVIDENCE. NO CHECK ANYWHERE compares two created_utc values, orders
      artifacts by them, derives a construction sequence from them, refuses on
      their relative values, or treats one as earlier or later than another.
      A verifier that ordered artifacts by created_utc would be trusting an
      unauthenticated author-supplied string. FS-1 and FS-2 state exactly what
      the final bytes do and do not prove.

MS-11 THE CANONICAL reachable_closure VALUE — LITERAL, COMPLETE, AND THE ONLY
      ADMISSIBLE ONE. This closes the content, not merely the shape, and in
      version 1.5 it closes the ROLE import surface as well.

      WHAT THE FIELD DENOTES, RESTATED AND WIDENED. reachable_closure is the set
      of Python modules resident, by direct or transitive module-scope import,
      in a ROLE PROCESS of this contract at the instant §P1-7.4 `A-10` returns,
      on the platform of §P1-2.1 under the launch of §P1-7.1, together with the
      three audited per-module properties. It is the import-time closure of the
      union of THREE literal scoped allowlists of §P1-3.2:
        scripts/officina_process_control_bootstrap.py  os sys _signal time
                                                       fcntl _socket
        scripts/officina_role_bootstrap.py             os sys fcntl
        src/philosophia/officina/generic_harness.py    the sixteen names of
                                                       MS-11.5, after the
                                                       reduction stated there
      THE UNION OF THE THREE DIRECT SETS IS EIGHTEEN NAMES.

      WHY generic_harness.py IS INCLUDED, AND WHY VERSION 1.4 WAS WRONG TO
      EXCLUDE IT. Version 1.4 said that root "runs under the nineteen-member
      global allowlist in the caller context". THAT STATEMENT IS WITHDRAWN AS
      FALSE OF THIS CONTRACT'S OWN OPERATIVE TEXT. §P1-3.2 gives
      generic_harness.py its OWN scoped entry, and a file with an entry gets
      EXACTLY that entry and never the union with the default; and §P1-7.4
      `A-10` imports philosophia.officina.generic_harness INSIDE the SUPERVISOR,
      WATCHDOG, CONTROLLER and WORKER role bootstraps, after the `A-9` sys.path
      replacement and before any pinned entry function runs. That module is
      therefore role code on every role path, and the import-time task, at-fork,
      handler, signal-state and origin effects of everything it pulls are
      directly material to the watchdog and control claims. root_source_sha256
      proves only WHICH ROOT BYTES were installed; `S-1`..`S-24b` constrain root
      ASTs and selected call and topology properties; NEITHER enumerates or pins
      the transitive standard-library modules executed during that role import,
      and the role path does not repeat `P-c`, `P-d` or `P-g` after `A-10`.

      WHAT IT STILL DOES NOT DENOTE, and the argument is stated accurately this
      time: it is NOT the closure of scripts/officina_activate_t.py or
      scripts/verify_officina_active.py. Those two execute ONLY in caller
      tooling — they are never imported by any role bootstrap, appear at no step
      of §P1-7.4, and hold no descriptor, handle, capability or lock of this
      contract. They are pinned by root_source_sha256 and by `S-1`..`S-24b`, and
      they take the nineteen-member global default of §P1-3.2 because neither
      has a scoped entry. NO CLOSURE CLAIM IS MADE FOR THEM AND NONE IS NEEDED,
      because no process that this contract creates ever imports them.

      THE KIND MAPPING, EXACT AND TOTAL. kind records the module's IMPORT-SYSTEM
      ORIGIN on the pinned interpreter build, and nothing else:
        BUILTIN      the module is compiled into the interpreter binary and is
                     listed in sys.builtin_module_names; its import-system
                     origin is the exact string "built-in"
        FROZEN       the module's code object is frozen into the interpreter
                     binary; its origin is the exact string "frozen". A .py
                     file of the same name may also exist on disk; it is NOT
                     what is loaded, and its presence does not make the module
                     PURE_PYTHON
        EXTENSION    the origin is a filesystem path whose final component ends
                     in the platform's dynamic-extension suffix
        PURE_PYTHON  the origin is a filesystem path whose final component ends
                     in ".py"
      The four are mutually exclusive and, on the pinned build, total over the
      closure. ALL FOUR ARE NOW IN USE. §P1-3.3's human vocabulary is NOT the
      kind vocabulary: "built-in" there means BUILTIN here, and os's "Python
      wrapper over built-in posix" describes its implementation and delegation,
      not its load origin, which on the pinned build is FROZEN.

      THE transitive_imports RULE, EXACT. transitive_imports is the TRANSITIVE
      closure of module-scope import EDGES THAT ARE ACTUALLY EXECUTED on the
      pinned build, EXCLUDING the element's own module name. An import written
      inside a function body, a method body or a class body is NOT a module-scope
      import and is excluded; a module-scope import inside a branch that does not
      execute is excluded and is listed at MS-11.3. Import cycles are permitted
      and are resolved by the exclusion of self.
      A `from __future__ import ...` STATEMENT IS BOTH A COMPILER DIRECTIVE AND
      A REAL RUNTIME IMPORT of the ordinary module `__future__`, which is why
      `__future__` is row 1 and not an omission; the compiler directive it also
      carries has no import-time effect of any kind.

      THE THREE BOOLEANS, DERIVED AND PINNED. Each is true if and only if
      EXECUTING THE MODULE'S TOP-LEVEL CODE does the named thing:
        starts_task        creates a thread, a task, a process or an
                           interpreter-level concurrent execution context
        registers_at_fork  CALLS os.register_at_fork or any equivalent at-fork
                           registration. DEFINING such a function is not
                           calling it: os defines register_at_fork and never
                           calls it at import, so its value is false
        installs_handler   installs or replaces a process-wide signal handler,
                           an atexit hook, an audit hook, a trace or profile
                           function, an import hook or a sys hook
      INTERPRETER-STARTUP INITIALIZATION IS EXCLUDED BY DEFINITION. Whatever
      Py_Initialize does before any production root executes is not an
      import-time effect of any module below, and §P1-7.2 `P-g` governs
      inherited and startup signal state separately. IN THE CANONICAL VALUE ALL
      TWO HUNDRED AND SIXTY-SEVEN BOOLEANS ARE false. Their audit basis is
      MS-11.3, and `P-c`, `P-d` and `P-g` independently re-establish the
      corresponding runtime facts before any fork.

MS-11.1 THE CANONICAL VALUE. reachable_closure has EXACTLY the eighty-nine
      elements below, in exactly this order, with exactly these values. Every
      element's starts_task, registers_at_fork and installs_handler is the JSON
      literal false and is not repeated per row. Line wrapping inside a
      transitive_imports cell is presentation only and introduces no element.

        #   module                          kind      transitive_imports
        1   __future__                      PURE_PYTHON (empty)
        2   _abc                            BUILTIN   (empty)
        3   _ast                            BUILTIN   (empty)
        4   _blake2                         BUILTIN   (empty)
        5   _codecs                         BUILTIN   (empty)
        6   _collections                    BUILTIN   (empty)
        7   _collections_abc                FROZEN    _abc abc sys
        8   _datetime                       BUILTIN   (empty)
        9   _frozen_importlib               FROZEN    (empty)
       10   _frozen_importlib_external      FROZEN    _imp _io _warnings marshal posix sys
       11   _functools                      BUILTIN   (empty)
       12   _hashlib                        EXTENSION (empty)
       13   _imp                            BUILTIN   (empty)
       14   _io                             BUILTIN   (empty)
       15   _json                           EXTENSION (empty)
       16   _opcode                         BUILTIN   (empty)
       17   _operator                       BUILTIN   (empty)
       18   _signal                         BUILTIN   (empty)
       19   _socket                         BUILTIN   (empty)
       20   _sre                            BUILTIN   (empty)
       21   _stat                           BUILTIN   (empty)
       22   _thread                         BUILTIN   (empty)
       23   _tokenize                       BUILTIN   (empty)
       24   _typing                         BUILTIN   (empty)
       25   _warnings                       BUILTIN   (empty)
       26   _weakref                        BUILTIN   (empty)
       27   _weakrefset                     PURE_PYTHON _weakref sys types
       28   abc                             FROZEN    _abc
       29   ast                             PURE_PYTHON _abc _ast _collections _collections_abc _functools _operator
                                                        _sre _stat _thread _weakref abc builtins collections
                                                        contextlib copyreg enum functools genericpath itertools
                                                        keyword operator os posix posixpath re re._casefix
                                                        re._compiler re._constants re._parser reprlib stat sys types
       30   builtins                        BUILTIN   (empty)
       31   codecs                          FROZEN    _codecs builtins encodings encodings.aliases sys
       32   collections                     PURE_PYTHON _abc _collections _collections_abc _operator _thread
                                                        _weakref abc builtins itertools keyword operator reprlib sys
       33   collections.abc                 PURE_PYTHON _abc _collections_abc abc sys
       34   contextlib                      PURE_PYTHON _abc _collections _collections_abc _functools _operator
                                                        _stat _thread _weakref abc builtins collections functools
                                                        genericpath itertools keyword operator os posix posixpath
                                                        reprlib stat sys types
       35   copy                            PURE_PYTHON _abc _collections_abc _weakref _weakrefset abc copyreg
                                                        itertools sys types weakref
       36   copyreg                         PURE_PYTHON (empty)
       37   dataclasses                     PURE_PYTHON _abc _ast _codecs _collections _collections_abc
                                                        _frozen_importlib _frozen_importlib_external _functools _imp
                                                        _io _opcode _operator _sre _stat _thread _tokenize _warnings
                                                        _weakref _weakrefset abc ast builtins codecs collections
                                                        collections.abc contextlib copy copyreg dis encodings
                                                        encodings.aliases enum functools genericpath importlib
                                                        importlib.machinery inspect io itertools keyword linecache
                                                        marshal opcode operator os posix posixpath re re._casefix
                                                        re._compiler re._constants re._parser reprlib stat sys token
                                                        tokenize types warnings weakref
       38   datetime                        PURE_PYTHON _datetime
       39   dis                             PURE_PYTHON _abc _collections _collections_abc _io _opcode _operator
                                                        _thread _weakref abc builtins collections io itertools
                                                        keyword opcode operator reprlib sys types
       40   encodings                       PURE_PYTHON _codecs builtins codecs encodings.aliases sys
       41   encodings.aliases               PURE_PYTHON (empty)
       42   encodings.utf_8                 PURE_PYTHON _codecs builtins codecs encodings encodings.aliases sys
       43   enum                            PURE_PYTHON _abc _collections _collections_abc _functools _operator
                                                        _thread _weakref abc builtins collections functools
                                                        itertools keyword operator reprlib sys types
       44   errno                           BUILTIN   (empty)
       45   fcntl                           BUILTIN   (empty)
       46   fnmatch                         PURE_PYTHON _abc _collections _collections_abc _functools _operator _sre
                                                        _stat _thread _weakref abc builtins collections copyreg enum
                                                        functools genericpath itertools keyword operator os posix
                                                        posixpath re re._casefix re._compiler re._constants
                                                        re._parser reprlib stat sys types
       47   functools                       PURE_PYTHON _abc _collections _collections_abc _functools _operator
                                                        _thread _weakref abc builtins collections itertools keyword
                                                        operator reprlib sys types
       48   genericpath                     FROZEN    _abc _collections_abc _stat abc os posix posixpath stat sys
       49   hashlib                         PURE_PYTHON _hashlib
       50   hmac                            PURE_PYTHON _hashlib _operator _warnings hashlib sys warnings
       51   importlib                       PURE_PYTHON _frozen_importlib _frozen_importlib_external _imp _io
                                                        _warnings marshal posix sys warnings
       52   importlib.machinery             FROZEN    _frozen_importlib _frozen_importlib_external _imp _io
                                                      _warnings importlib marshal posix sys warnings
       53   inspect                         PURE_PYTHON _abc _ast _codecs _collections _collections_abc
                                                        _frozen_importlib _frozen_importlib_external _functools _imp
                                                        _io _opcode _operator _sre _stat _thread _tokenize _warnings
                                                        _weakref abc ast builtins codecs collections collections.abc
                                                        contextlib copyreg dis encodings encodings.aliases enum
                                                        functools genericpath importlib importlib.machinery io
                                                        itertools keyword linecache marshal opcode operator os posix
                                                        posixpath re re._casefix re._compiler re._constants
                                                        re._parser reprlib stat sys token tokenize types warnings
       54   io                              FROZEN    _abc _io abc
       55   ipaddress                       PURE_PYTHON _abc _collections _collections_abc _functools _operator
                                                        _thread _weakref abc builtins collections functools
                                                        itertools keyword operator reprlib sys types
       56   itertools                       BUILTIN   (empty)
       57   json                            PURE_PYTHON _abc _codecs _collections _collections_abc _functools _json
                                                        _operator _sre _thread _weakref abc builtins codecs
                                                        collections copyreg encodings encodings.aliases enum
                                                        functools itertools json.decoder json.encoder json.scanner
                                                        keyword operator re re._casefix re._compiler re._constants
                                                        re._parser reprlib sys types
       58   json.decoder                    PURE_PYTHON _abc _codecs _collections _collections_abc _functools _json
                                                        _operator _sre _thread _weakref abc builtins codecs
                                                        collections copyreg encodings encodings.aliases enum
                                                        functools itertools json json.encoder json.scanner keyword
                                                        operator re re._casefix re._compiler re._constants
                                                        re._parser reprlib sys types
       59   json.encoder                    PURE_PYTHON _abc _collections _collections_abc _functools _json
                                                        _operator _sre _thread _weakref abc builtins collections
                                                        copyreg enum functools itertools keyword operator re
                                                        re._casefix re._compiler re._constants re._parser reprlib
                                                        sys types
       60   json.scanner                    PURE_PYTHON _abc _collections _collections_abc _functools _json
                                                        _operator _sre _thread _weakref abc builtins collections
                                                        copyreg enum functools itertools keyword operator re
                                                        re._casefix re._compiler re._constants re._parser reprlib
                                                        sys types
       61   keyword                         PURE_PYTHON (empty)
       62   linecache                       PURE_PYTHON _abc _codecs _collections _collections_abc _functools _io
                                                        _operator _sre _stat _thread _tokenize _weakref abc builtins
                                                        codecs collections copyreg encodings encodings.aliases enum
                                                        functools genericpath io itertools keyword operator os posix
                                                        posixpath re re._casefix re._compiler re._constants
                                                        re._parser reprlib stat sys token tokenize types
       63   marshal                         BUILTIN   (empty)
       64   math                            BUILTIN   (empty)
       65   ntpath                          FROZEN    _abc _collections_abc _stat abc genericpath os posix
                                                      posixpath stat sys
       66   opcode                          PURE_PYTHON _opcode
       67   operator                        PURE_PYTHON _operator builtins
       68   os                              FROZEN    _abc _collections_abc _stat abc genericpath posix posixpath
                                                      stat sys
       69   pathlib                         PURE_PYTHON _abc _collections _collections_abc _functools _io _operator
                                                        _sre _stat _thread _warnings _weakref abc builtins
                                                        collections copyreg enum errno fnmatch functools genericpath
                                                        io ipaddress itertools keyword math operator os posix
                                                        posixpath re re._casefix re._compiler re._constants
                                                        re._parser reprlib stat sys types urllib urllib.parse
                                                        warnings
       70   posix                           BUILTIN   (empty)
       71   posixpath                       FROZEN    _abc _collections_abc _stat abc genericpath os posix stat
                                                      sys
       72   re                              PURE_PYTHON _abc _collections _collections_abc _functools _operator _sre
                                                        _thread _weakref abc builtins collections copyreg enum
                                                        functools itertools keyword operator re._casefix
                                                        re._compiler re._constants re._parser reprlib sys types
       73   re._casefix                     PURE_PYTHON (empty)
       74   re._compiler                    PURE_PYTHON _abc _collections _collections_abc _functools _operator _sre
                                                        _thread _weakref abc builtins collections copyreg enum
                                                        functools itertools keyword operator re re._casefix
                                                        re._constants re._parser reprlib sys types
       75   re._constants                   PURE_PYTHON _sre
       76   re._parser                      PURE_PYTHON _abc _collections _collections_abc _functools _operator _sre
                                                        _thread _weakref abc builtins collections copyreg enum
                                                        functools itertools keyword operator re re._casefix
                                                        re._compiler re._constants reprlib sys types
       77   reprlib                         PURE_PYTHON _thread builtins itertools
       78   stat                            FROZEN    _stat
       79   sys                             BUILTIN   (empty)
       80   time                            BUILTIN   (empty)
       81   token                           PURE_PYTHON (empty)
       82   tokenize                        PURE_PYTHON _abc _codecs _collections _collections_abc _functools _io
                                                        _operator _sre _thread _tokenize _weakref abc builtins
                                                        codecs collections copyreg encodings encodings.aliases enum
                                                        functools io itertools keyword operator re re._casefix
                                                        re._compiler re._constants re._parser reprlib sys token
                                                        types
       83   types                           PURE_PYTHON sys
       84   typing                          PURE_PYTHON _abc _collections _collections_abc _functools _operator _sre
                                                        _stat _thread _typing _warnings _weakref abc builtins
                                                        collections collections.abc contextlib copyreg enum
                                                        functools genericpath itertools keyword operator os posix
                                                        posixpath re re._casefix re._compiler re._constants
                                                        re._parser reprlib stat sys types warnings
       85   urllib                          PURE_PYTHON (empty)
       86   urllib.parse                    PURE_PYTHON _abc _collections _collections_abc _functools _operator _sre
                                                        _thread _warnings _weakref abc builtins collections copyreg
                                                        enum functools ipaddress itertools keyword math operator re
                                                        re._casefix re._compiler re._constants re._parser reprlib
                                                        sys types warnings
       87   warnings                        PURE_PYTHON _warnings sys
       88   weakref                         PURE_PYTHON _abc _collections_abc _weakref _weakrefset abc itertools sys
                                                        types
       89   zipimport                       FROZEN    _frozen_importlib _frozen_importlib_external _imp _io
                                                      _warnings marshal posix sys time

      CARDINALITY 89. KIND COUNTS: BUILTIN 29, FROZEN 13, EXTENSION 2,
      PURE_PYTHON 45. The 76 distinct names occurring in any transitive_imports
      are each themselves a module row, so the CLOSURE rule of MS-4 is satisfied
      BY THIS VALUE; 39 rows have an empty transitive_imports array.
      THE FOURTEEN-ROW BOOTSTRAP SUBSET OF VERSION 1.4 IS PRESERVED EXACTLY.
      Rows _abc, _collections_abc, _signal, _socket, _stat, abc, fcntl,
      genericpath, os, posix, posixpath, stat, sys and time carry the SAME kind
      and the SAME transitive_imports array, element for element, that the
      independent X line reproduced from scratch against version 1.4. Widening
      the denotation adds rows; it changes no confirmed row, because an
      element's transitive_imports depends only on that element's own outgoing
      edges, which no new root can alter.

MS-11.2 THE SCOPED-ALLOWLIST REDUCTION THIS VALUE DEPENDS ON — see MS-11.5.
      Without it the closure additionally contains subprocess, threading,
      signal, select, selectors, _posixsubprocess, locale and _locale, and
      threading's module-level code CALLS os.register_at_fork, which would make
      registers_at_fork TRUE for a module resident in every role process
      including the WATCHDOG. THE REDUCTION IS NOT COSMETIC AND IS NOT OPTIONAL.

MS-11.3 HOW EVERY ROW WAS AUDITED, AND AGAINST WHAT.
      THE AUDIT BASIS IS THREE MUTUALLY INDEPENDENT DERIVATIONS THAT AGREE, NONE
      OF WHICH IMPORTS, EXECUTES OR COMPILES ANY PHILOSOPHIA PRODUCTION MODULE —
      none of the five roots is opened for behaviour by the audit, and at the
      reviewed commit three of the five do not exist as tracked files:
        (a) RESIDENCY. In a fresh interpreter launched with the exact isolation
            flags of §P1-7.1 and an empty environment, the eighteen union
            allowlist names are imported and the resulting module table is
            recorded. This is the operative question — what is resident in a
            role process after A-10 — answered directly.
        (b) STATIC SOURCE AND CODE-OBJECT PARSE. For every resident module with
            a Python top-level code object, every module-scope IMPORT_NAME
            operand, its relative-import level and its fromlist are read from
            the code object ACTUALLY LOADED, resolving relative imports against
            the package. Function, method and class bodies are not descended
            into.
        (c) RUNTIME DIFFERENTIAL FOR THE BOOLEANS. Signal dispositions for every
            signal number, the live thread-frame count, sys.gettrace and
            sys.getprofile are sampled before and after the eighteen imports.
            RESULT: NO SIGNAL DISPOSITION CHANGED; THE THREAD-FRAME COUNT WAS 1
            BEFORE AND 1 AFTER; NO TRACE OR PROFILE FUNCTION WAS INSTALLED. A
            module-level scan for register_at_fork, start_new_thread, Thread,
            Popen, fork, posix_spawn, system, signal, setitimer, set_wakeup_fd,
            settrace, setprofile, addaudithook, excepthook, unraisablehook and
            atexit across all 89 top-level code objects returned ZERO hits.
      THREE NORMALIZATIONS ARE APPLIED, AND THEY ARE THE ONLY THREE:
        ALIAS ENTRIES. A module table key that denotes the SAME module object
          under a second name is not a second row. There are exactly three:
          os.path is posixpath, importlib._bootstrap is _frozen_importlib, and
          importlib._bootstrap_external is _frozen_importlib_external. The
          canonical name is the module's own spec name, which is why
          _collections_abc is a row under that name even though its __name__
          attribute is rebound to collections.abc.
        PSEUDO-MODULE ENTRIES. A module-table key whose value is not a module
          object is not a row. There are exactly two: typing.io and typing.re,
          which on the pinned build are deprecated class objects registered in
          the module table by typing.
        UNEXECUTED MODULE-SCOPE BRANCHES. SEVEN, each with its reason. VERSION
        1.5 SAID SIX AND OMITTED THE LAST ONE; the omission was factual, was
        found by the independent X line, and is corrected here. IT CHANGES NO
        ROW, NO KIND, NO EDGE, NO BOOLEAN, NO NORMALIZATION AND NEITHER THE
        CANONICAL LENGTH NOR THE DIGEST OF MS-11.1, because every one of these
        branches was already correctly excluded from the value:
          os --> nt          the Windows branch; the posix branch is taken
          os --> ntpath      the same Windows branch. ntpath IS a row, because
                             pathlib imports it unconditionally, but the edge
                             from os does not exist
          ntpath --> nt, _winapi                    Windows-only
          _frozen_importlib_external --> nt, winreg Windows-only
          abc --> _py_abc    the try importing _abc succeeds, so the except
                             branch never runs
          hashlib --> logging  reached only from an except ValueError handler
                             taken when a hash constructor is unavailable; on
                             the pinned build every constructor is available
          datetime --> _pydatetime  THE SEVENTH, ADDED IN VERSION 1.6.
                             datetime.py is `try: from _datetime import * /
                             except ImportError: from _pydatetime import *`.
                             _datetime is in sys.builtin_module_names on the
                             pinned build, so the try succeeds and the except
                             branch never runs. _pydatetime is a genuine
                             top-level IMPORT_NAME in datetime's loaded code
                             object and is correctly ABSENT from MS-11.1;
                             datetime's transitive_imports is [_datetime] and is
                             unchanged. This is the same class of branch as
                             abc --> _py_abc.
      ONE DISCLOSURE, RECORDED RATHER THAN OMITTED. The module-level code of
      _collections_abc performs many calls to the abstract-base-class virtual
      subclass registration method, and io, collections, encodings, pathlib and
      weakref do the same. That is abstract-base-class bookkeeping inside those
      modules' own class objects. It is not an at-fork registration, not an
      atexit registration and not a handler installation.
      A SECOND DISCLOSURE, AND IT CORRECTS A RATIONALE IN §P1-3.2. The built-in
      module _thread is a row. It is reached by an executed edge from functools
      and from reprlib, AND IT IS ALSO RESIDENT BEFORE ANY CONTRACT IMPORT RUNS:
      on the pinned build the interpreter's own start-up module table already
      contains it. §P1-3.2's sentence explaining that signal is permitted in no
      file "because its import closure pulls functools and hence _thread" is
      therefore factually obsolete as a REASON. THE RULE IS UNCHANGED AND IS NOT
      WEAKENED: signal, threading, _thread, select, selectors, socket,
      multiprocessing, concurrent, asyncio, ctypes, array, struct, atexit and gc
      remain permitted in NO allowlist, and none of them is in any. What changes
      is only that no honest reader may now infer that _thread's absence from a
      process is achievable by an allowlist choice. Importing _thread starts no
      thread: its three booleans are false, and derivation (c) measured the
      thread-frame count as 1 before and 1 after.
      THE AUDITED BUILD:
        CPython 3.12.3, x86_64 Linux, GCC 13.3.0, build stamp
        "Python 3.12.3 (main, Jun 19 2026, 12:46:00)"
      on which fcntl and _socket are compiled into the interpreter binary rather
      than loaded as dynamic extensions, and on which 13 rows are frozen.
      THE LAUNCH FLAGS ARE ALREADY CLOSED: §P1-7.1's argv is the exact
      six-element vector -I -S -E -P with no -X option, the environment is empty,
      §P1-7.2 P-b reads the flags back, and test 1 is byte-exact on the argv, so
      the frozen-module set cannot be altered by an interpreter option.

MS-11.4 THE EQUALITY REQUIREMENT — VALUE, NOT SHAPE.
      M4's reachable_closure must EQUAL the value of MS-11.1 as a JSON value:
      the same eighty-nine elements, the same order, the same module strings,
      the same kind literals, the same transitive_imports arrays in the same
      order, and all 267 booleans false. A DIFFERENT VALUE THAT SATISFIES EVERY
      MS-4 SHAPE RULE IS REFUSED.
      THE MECHANICAL FORM OF THE CHECK, so that two implementations cannot
      differ: let CLOSURE_BYTES be CANON(M4.reachable_closure) as MS-0 defines
      CANON, INCLUDING its single trailing 0x0A byte. Then
        len(CLOSURE_BYTES) is exactly 20534, and
        SHA-256(CLOSURE_BYTES) is exactly
          aa974e0c91e5c9afd0aceefa6b0e47ef42b5ad7b71dc4de690a4873232dc20ee
      Both conjuncts are required, AND NEITHER REPLACES THE JSON-VALUE
      COMPARISON: the direct comparison with the MS-11.1 literal is the primary
      check and the length and digest are corroboration, so that the predicate
      does not rest on collision resistance alone. THIS IS NOT A SELF-HASH: it
      is the digest of a VALUE carried by a generated artifact, it appears in no
      file whose own digest it is, and no file below hashes itself.
      THE OWNING CLAUSE IS CK-10 AND THE CODE IS MANIFEST_VALUE_MISMATCH. A
      malformed closure — wrong JSON type, wrong element key set, unsorted,
      duplicated, or not closed under itself — is a STRUCTURAL failure, is owned
      earlier by CK-8, and is refused with MEMBER_SUBSTITUTED. The two cases
      never contend: VP-3 gives each exactly one owner.

MS-11.5 THE SCOPED-ALLOWLIST REDUCTION, STATED IN FULL WITH ITS AUTHORITY.
      §P1-3.2's scoped entry for src/philosophia/officina/generic_harness.py
      LOSES EXACTLY ONE NAME, subprocess, and gains none. It becomes the SIXTEEN
      names
        __future__ ast dataclasses datetime enum fcntl hashlib hmac json os
        pathlib re time typing weakref _socket
      THE REMOVED NAME AND THE REASON, and this is not a new author decision:
      THIS CONTRACT ALREADY FORBIDS subprocess IN THAT FILE, in three operative
      places that version 1.4's allowlist contradicted.
        `S-12` of §P1-14.6 CHANGE 3: "subprocess, Popen, fork, waitpid, kill,
          killpg and system appear on no path of generic_harness.py";
        test 8 of §P1-15: "the launcher performs no fork, no Popen, no
          preexec_fn and no shell, statically and dynamically";
        the future-edit surface row for that path: "removal of every subprocess,
          fork, wait, kill and group-kill call".
      A name that no conforming build may use cannot remain in the allowlist
      that authorizes its import. THE REDUCTION RECONCILES §P1-3.2 WITH RULES
      ALREADY IN THESE GOVERNING BYTES; it decides nothing new.
      WHAT IT REMOVES FROM THE CLOSURE, exactly eight modules: subprocess,
      threading, signal, select, selectors, _posixsubprocess, locale and
      _locale. FOUR OF THE EIGHT — threading, signal, select and selectors —
      are named by §P1-3.2 itself as permitted in no file, and version 1.4's
      denotation concealed the fact that they were transitively resident in
      every role process. threading's module-level code CALLS
      os.register_at_fork.
      WHAT IT DOES NOT TOUCH. The nineteen-member global default of §P1-3.2 is
      UNCHANGED and still contains subprocess, so scripts/officina_activate_t.py
      and scripts/verify_officina_active.py are unaffected. The two bootstrap
      scoped entries are UNCHANGED. No other allowlist, no other root and no
      other rule moves.
      WHAT IT COSTS THE FUTURE IMPLEMENTATION. Nothing that this contract does
      not already require: §P1-7.1 launches through the bound `_posix_spawn`
      primitive of §P1-3.4, never through subprocess, and `S-11`, `S-12` and
      test 8 already require exactly that. A build of generic_harness.py that
      imports subprocess was already nonconforming; after this reduction it is
      also outside the allowlist and is refused earlier.
      IT MOVES NO SCIENTIFIC CELL. It adds, removes and renames no watchdog
      option, treatment, evidence class, covariate, endpoint, qualification
      input, comparison input, Q fact or C fact; it is option-independent and
      identical under W-A and W-B; and it opens no author cell.

MS-11.6 A CHANGED GRAPH IS A NEW REVIEWED GENERATION, NEVER A RECOMPUTATION.
      If the standard library, the interpreter build, the allowlists of §P1-3.2
      or any production root changes so that any row of MS-11.1 becomes false,
      THE MANIFEST IS NOT SILENTLY REGENERATED AGAINST THE NEW GRAPH. MS-11.1 is
      a constant of these governing bytes; changing it changes M1, and a new M1
      requires a new independently reviewed generation of this pair, a new
      install record and a new Stage-B authorization. NO BUILD, SCRIPT, TEST OR
      VERIFIER MAY RECOMPUTE A DIFFERENT ACCEPTED VALUE AT INSTALL TIME. A
      verifier that derived the closure from the live interpreter and accepted
      whatever it found would defeat the check entirely and is expressly
      forbidden.
      THIS VALUE IS A PROSPECTIVE CONFORMANCE CONSTRAINT AND IS NOT EVIDENCE
      THAT AN IMPLEMENTATION EXISTS. At the reviewed commit three of the five
      production roots are absent as tracked files. The root-level import sets
      come from §P1-3.2's literal allowlists, not from files; the transitive
      edges, kinds and booleans are audited against the extant standard library
      and the pinned interpreter; and correspondence to the eventual root bytes
      is enforced later, by the scoped-allowlist rule, by root_source_sha256, by
      `S-1`..`S-24b`, by the matrix, by M7 and by CK-10 at install.

MS-13 THE PROJECT-IMPORT DEPENDENCY SURFACE — CLOSED, DIGEST-BOUND, ADDED IN
      VERSION 1.6 AND MADE SERIALIZABLE IN VERSION 1.7. It repairs a real gap:
      MS-11 bound the STANDARD-LIBRARY
      closure of the role import and bound nothing about the PROJECT code that
      the same import necessarily executes first.

      WHAT PYTHON ACTUALLY EXECUTES AT §P1-7.4 A-10, DERIVED FROM THE IMPORT
      SEMANTICS AND THE MODULE-SCOPE STATEMENT ORDER OF EACH FILE, NOT ASSUMED:
        1. philosophia                      — the parent package initializer
                                              runs to completion first
        2. philosophia.officina             — the sub-package initializer BEGINS
        3.   philosophia.officina.canonical — executed FROM INSIDE step 2, by
                                              that initializer's FIRST
                                              module-scope statement after its
                                              docstring, and run to completion
        4.   philosophia.officina.interlock — executed FROM INSIDE step 2, by
                                              the SECOND such statement, and run
                                              to completion
        5. philosophia.officina             — the initializer COMPLETES
        6. philosophia.officina.generic_harness — the role module executes, and
                                              its sixteen scoped seeds bring the
                                              standard-library closure of
                                              MS-11.1
        7. control returns to A-10
      THE ORDER ABOVE IS NOT THE ILLUSTRATIVE CHAIN IT MIGHT BE MISTAKEN FOR.
      Steps 3 and 4 are NESTED INSIDE step 2, not sequential after it; canonical
      strictly precedes interlock because the initializer's statements are in
      that order; and the parent package contributes NO import of any kind.
      A-11 identity-checks ONLY the imported generic_harness file, so before
      version 1.6 nothing bound steps 1 through 5 at all.

      THE CLOSED SURFACE. project_import_dependencies is a JSON OBJECT with
      EXACTLY the two keys modules and execution_order.
        modules          ARRAY of EXACTLY 4 OBJECTS, sorted ascending by the
                         "module" value compared byte for byte, module values
                         pairwise distinct. Every element has EXACTLY these
                         SIX keys.
                         WHY SIX AND NOT FIVE, STATED AT THE LOCUS THAT WAS
                         WRONG: version 1.6 declared an exact FIVE-key element
                         and then required, at MS-13.1, that every module assert
                         eight named booleans that CK-10 must compare and that
                         row 111 must toggle. No JSON value satisfied both — a
                         conforming element had nowhere to carry the assertions,
                         and any element that carried them failed S4's
                         exact-key-set rule at CK-8. THE SIXTH KEY IS THAT
                         LOCATION. It is the whole of the repair, it renames no
                         predicate, and it adds no assertion: the eight names
                         and the thirty-two false values are exactly version
                         1.6's.
                           module            STRING, the canonical dotted module
                                             name
                           path              STRING, the repository-relative
                                             path, 0x2F separated
                           sha256            64-char lowercase hex STRING, the
                                             SHA-256 of the whole bytes at that
                                             path
                           project_imports   ARRAY of STRINGS, the module-scope
                                             imports of OTHER project modules,
                                             IN EXECUTION ORDER, possibly empty.
                                             THIS ARRAY IS NOT SORTED: its order
                                             is the order the statements run,
                                             and a differently ordered array is
                                             a different value
                           stdlib_seeds      ARRAY of STRINGS, the module-scope
                                             standard-library imports, SORTED
                                             ascending and pairwise distinct,
                                             possibly empty
                           import_time_effects
                                             OBJECT whose key set is EXACTLY the
                                             EIGHT literal predicate names of
                                             MS-13.1 — no extra key, no missing
                                             key, no renamed key — and whose
                                             EVERY value is a JSON BOOLEAN. The
                                             eight names, which are version
                                             1.6's own names and are NOT renamed
                                             here, are
                                               starts_process_or_task
                                               creates_thread
                                               registers_at_fork
                                               installs_handler
                                               mutates_environment
                                               writes_filesystem
                                               opens_descriptor_or_socket
                                               performs_other_forbidden_effect
                                             CANON sorts object keys, so the
                                             serialized order is fixed and no
                                             implementation may choose another.
                                             A value that is null, 0, 1, "false",
                                             "true", a number or any non-boolean
                                             is a TYPE failure; an added,
                                             removed or renamed key is an
                                             EXACT-KEY-SET failure; BOTH ARE
                                             STRUCTURAL, BOTH ARE OWNED BY CK-8
                                             ALONE, AND BOTH REFUSE WITH
                                             MEMBER_SUBSTITUTED. The REQUIRED
                                             VALUE of each of the eight — false
                                             for every module — is SEMANTIC and
                                             is owned by CK-10 alone, refusing
                                             with MANIFEST_VALUE_MISMATCH. The
                                             two cases never contend: CK-8
                                             precedes CK-9 and CK-10, and a
                                             boolean that is well typed and
                                             true reaches CK-10 while a
                                             malformed key set never does.
        execution_order  ARRAY of EXACTLY 4 STRINGS, the module names in the
                         order their top-level code BEGINS executing. NOT
                         SORTED.

      THE CANONICAL VALUE — four modules, and these exact digests are the
      PROSPECTIVE REVIEWED BYTES:

        1  philosophia
           src/philosophia/__init__.py
           96833596f81831b51ba63cf2d71cd78cae5a778f0929e09a531c5af785ddf684
           project_imports []            stdlib_seeds []
           import_time_effects  all eight false
        2  philosophia.officina
           src/philosophia/officina/__init__.py
           2bb45ebf58c735795a4cea8e2d33fa8d174c16d889e01b4a85e99673ca831e1f
           project_imports ["philosophia.officina.canonical",
                            "philosophia.officina.interlock"]
           stdlib_seeds []
           import_time_effects  all eight false
        3  philosophia.officina.canonical
           src/philosophia/officina/canonical.py
           a95cad3e4e97f51504b9e7e0ffc4be869d415a8555ef7a4d6769297817978a54
           project_imports []
           stdlib_seeds ["__future__","hashlib","json","os","pathlib","typing"]
           import_time_effects  all eight false
        4  philosophia.officina.interlock
           src/philosophia/officina/interlock.py
           8b464f525ae794e4c8f56903683853ae9d9782fd3034b11eda3cd1159d24ecc8
           project_imports []
           stdlib_seeds ["__future__","dataclasses"]
           import_time_effects  all eight false

        execution_order  ["philosophia", "philosophia.officina",
                          "philosophia.officina.canonical",
                          "philosophia.officina.interlock"]

      ONE COMPLETE ELEMENT, SERIALIZED, SO THAT NO IMPLEMENTATION HAS TO INFER
      THE BYTES. This is CANON of the fourth element above, without the single
      trailing 0x0A that CANON appends only to a whole hashed artifact. It is
      489 bytes. It is presented as ONE logical line; the line breaks below are
      presentation only and are NOT part of the value, and there is no space
      anywhere outside a string literal:
        {"import_time_effects":{"creates_thread":false,"installs_handler":
        false,"mutates_environment":false,"opens_descriptor_or_socket":false,
        "performs_other_forbidden_effect":false,"registers_at_fork":false,
        "starts_process_or_task":false,"writes_filesystem":false},"module":
        "philosophia.officina.interlock","path":
        "src/philosophia/officina/interlock.py","project_imports":[],"sha256":
        "8b464f525ae794e4c8f56903683853ae9d9782fd3034b11eda3cd1159d24ecc8",
        "stdlib_seeds":["__future__","dataclasses"]}
      THE ASSERTIONS ARE THEREFORE REPRESENTABLE IN BYTES, AND THAT IS THE
      POINT OF THE SIXTH KEY. Setting exactly one of the thirty-two booleans to
      true changes the serialized bytes of project_import_dependencies and
      therefore of the whole manifest; the mutated value still satisfies every
      structural rule — object, exact key set, exact types — so CK-8 ACCEPTS it
      and CK-10 REFUSES it with MANIFEST_VALUE_MISMATCH naming
      project_import_dependencies. THIS IS THE STATE VERSION 1.6 COULD NOT
      EXPRESS AND ROW 111 COULD NOT BUILD.
      NO DIGEST OF project_import_dependencies IS DEFINED, PINNED OR COMPARED.
      The serialization above is an EXAMPLE fixing the encoding, not a new
      constant: CK-10's check is the direct value comparison of MS-13's parts,
      exactly as version 1.6 defined it, and no new hashed quantity enters this
      pair.

      THE modules ARRAY IS SORTED BY module, WHICH IS NOT EXECUTION ORDER. Both
      orders are pinned, separately, because they differ: sorted order puts
      canonical before interlock before officina, while execution begins with
      philosophia, then philosophia.officina, then canonical, then interlock.
      execution_order carries the second, and its four strings are exactly the
      four module values of modules.

MS-13.1 THE IMPORT-TIME EFFECT ASSERTIONS, AND THE EXACT PLACE THEY LIVE.
      THE EIGHT ASSERTIONS OF EACH MODULE ARE THE EIGHT KEYS OF THAT MODULE
      ELEMENT'S import_time_effects OBJECT, AND OF NO OTHER KEY. EVERY ONE OF
      THE FOUR MODULES ASSERTS ALL EIGHT AS the JSON literal false, SO THE
      VALUE CARRIES THIRTY-TWO BOOLEANS, EACH ONE ADDRESSABLE AS
      project_import_dependencies.modules[k].import_time_effects.<name>:
        starts_process_or_task        creates a process, task or interpreter
                                      level execution context at import
        creates_thread                creates a thread at import
        registers_at_fork             CALLS os.register_at_fork or any
                                      equivalent at-fork registration at import
        installs_handler              installs or replaces a process-wide signal
                                      handler, an atexit hook, an audit hook, a
                                      trace or profile function, an import hook
                                      or a sys hook at import
        mutates_environment           writes os.environ, putenv or unsetenv at
                                      import
        writes_filesystem             creates, writes, renames, links or removes
                                      any filesystem object at import
        opens_descriptor_or_socket    opens a file descriptor, socket, pipe or
                                      FIFO at import
        performs_other_forbidden_effect
                                      performs at import any other effect this
                                      contract forbids in a role process
      THESE ARE THE ALREADY-GOVERNING NAMES OF VERSION 1.6, CARRIED FORWARD
      UNRENAMED. Version 1.7 changes WHERE they live, not WHAT they are: no
      predicate is added, removed, split, merged or given a new meaning, and
      the count is thirty-two before and after.
      THE ROUTING, STATED ONCE AND EXHAUSTIVELY, SO THAT ONE BYTE STATE HAS ONE
      ANSWER:
        an added key, a removed key, a renamed key, a duplicated key, a
          non-object import_time_effects, an absent import_time_effects, or a
          value that is null, a number, a string or any non-boolean
                                      CK-8, S4 or S5, MEMBER_SUBSTITUTED
        an object with exactly the eight keys, every value a boolean, and any
          one of the thirty-two true
                                      CK-10, MANIFEST_VALUE_MISMATCH
      NOTHING ELSE CAN HAPPEN TO THIS OBJECT, and the two owners are disjoint
      because CK-8 strictly precedes CK-10 in VP-4.
      DEFINING IS NOT CALLING, and this matters for one of the four:
      philosophia.officina.canonical DEFINES functions that create, fsync,
      rename and replace files. NONE OF THEM RUNS AT IMPORT. Its module-scope
      statements are one __future__ statement, FIVE non-__future__ import
      statements — hashlib, json, os, pathlib and typing — and eight function
      definitions, and there is no module-scope call of any kind. VERSION 1.6
      SAID FOUR IMPORT STATEMENTS; the count was wrong by one, was found by the
      independent X line, and is corrected here. THE BOUND VALUE IS UNAFFECTED:
      stdlib_seeds already carried the six names __future__, hashlib, json, os,
      pathlib and typing, and the operative conclusion — no module-scope call —
      is unchanged. The same defining-is-not-calling rule already governs os,
      which defines register_at_fork and never calls it.
      philosophia.officina.interlock HAS MODULE-SCOPE CALLS, AND VERSION 1.6
      UNDERSTATED THEM. Its module scope evaluates the builtin object() that
      creates its private sentinel, AND ALSO the decorator-factory call
      dataclass(frozen=True) together with the application of the decorator that
      call returns to its frozen dataclass. That is three call evaluations, not
      one. THE ASSERTIONS ARE UNCHANGED AND REMAIN CORRECT: none of the three
      creates a process, task, thread or at-fork registration, none installs a
      handler or hook, none writes the environment or the filesystem, none opens
      a descriptor or socket, and none performs any other effect this contract
      forbids in a role process. The correction is factual and narrows nothing.
      The two package initializers have no module-scope call at all.

MS-13.2 HOW THIS SURFACE WAS AUDITED, AND WHAT IT DOES NOT CLAIM.
      THE AUDIT PARSED SOURCE ONLY. Each of the four files was parsed to an
      abstract syntax tree; its module-scope Import and ImportFrom nodes were
      read with their relative levels resolved against the package; and every
      module-scope Call node was enumerated, not descending into function,
      method or class bodies. NO PROJECT MODULE WAS IMPORTED, EXECUTED OR
      COMPILED, and the untracked working-tree file named generic_harness.py was
      neither read for behaviour, adopted, nor edited.
      THE STANDARD-LIBRARY CLOSURE IS UNCHANGED BY THIS SURFACE, AND THIS IS A
      CHECKABLE FACT RATHER THAN A HOPE. The union of the four modules'
      stdlib_seeds is exactly
        __future__ dataclasses hashlib json os pathlib typing
      SEVEN NAMES, EVERY ONE OF WHICH IS ALREADY ONE OF THE SIXTEEN SCOPED
      SEEDS OF generic_harness.py IN §P1-3.2. The project dependencies therefore
      introduce NO standard-library module that MS-11.1 does not already carry,
      and MS-11.1's eighty-nine rows, its canonical length 20534 and its digest
      aa974e0c91e5c9afd0aceefa6b0e47ef42b5ad7b71dc4de690a4873232dc20ee ARE
      UNCHANGED BY VERSION 1.6. THE FOUR PROJECT MODULES ARE NOT FOLDED INTO
      MS-11.1 AND ARE NOT ROWS OF IT.
      WHAT THESE FOUR ARE NOT. They are NOT production roots — §P1-3.1's five
      roots are unchanged and none of these four is added to them. They are NOT
      members of M1..M7 — MS-8's cardinality is 69 and none of these four is in
      it. They are NOT rows of MS-11.1. They are NOT covered by
      root_source_sha256. They are a DEPENDENCY SURFACE bound by digest inside
      the manifest, and that is a weaker and different thing than membership,
      stated as such.
      WHAT IS AND IS NOT CLAIMED ABOUT THEIR CONTENT. The eight assertions of
      MS-13.1 are about IMPORT TIME ONLY. They say nothing about what these
      modules do when their functions are later CALLED, which the root AST
      rules, the primitive-identity rules and the §P1-7.2 preflight govern
      separately, and they are not a runtime monitor.

MS-13.3 THE BINDING, AND THE ACYCLIC CHAIN, STATED EXPLICITLY.
      CK-8 checks the SHAPE of project_import_dependencies structurally, AND
      THAT SHAPE NOW INCLUDES THE SIX-KEY ELEMENT AND THE EXACT EIGHT-KEY
      BOOLEAN import_time_effects OBJECT: an element key set other than the six,
      an import_time_effects key set other than the eight, and a non-boolean
      under any of the eight are each an S4 or S5 failure refused at CK-8 with
      MEMBER_SUBSTITUTED, and NO STAGE_A_ OR MANIFEST_VALUE_MISMATCH CODE IS
      AVAILABLE FOR ANY OF THEM. CK-10 then RECOMPUTES, FROM THE BYTES INSTALLED
      AT EACH LITERAL PATH, the SHA-256 of each of the four modules and requires
      equality with the recorded value, and requires the four paths, the two
      import-edge arrays per module, the execution_order array and all
      thirty-two effect booleans to equal the values of MS-13 exactly. ANY
      INEQUALITY REFUSES WITH MANIFEST_VALUE_MISMATCH BEFORE ANY PRODUCTION
      ENTRY POINT RUNS.
      THE CHAIN IS ACYCLIC AND HAS NO NEW ROOT:
        the four project modules' BYTES
          --SHA-256 recomputed at CK-10-->  the M4 manifest's
                                            project_import_dependencies
        the M4 manifest --is member M4, digest recomputed at CK-7-->
                                            the 69-member enumeration
        the 69 members  --IR-1-->           install_record_id
        install_record_id --TS-3, TS-4-->   the signed Stage-B bytes
        Stage B --Ed25519 under the Stage-A key pin-->  the author's selection
      NO FILE IN THAT CHAIN CONTAINS ITS OWN DIGEST, and the manifest still
      carries no digest of itself. THE INSTALL RECORD BINDS M4, AND M4 BINDS
      THESE BYTES.
      THIS IS A PROSPECTIVE SOURCE CONTRACT. The four files exist as tracked
      bytes at the reviewed commit and their digests above are those bytes.
      FUTURE IMPLEMENTATION BYTES MUST MATCH THEM. Any change to any of the
      four — content, path, project import edge, stdlib seed or effect
      assertion — CHANGES MS-13, WHICH CHANGES M1, AND THEREFORE REQUIRES A NEW
      INDEPENDENTLY REVIEWED GENERATION, a new install record and a new Stage-B
      authorization. NO BUILD, SCRIPT, TEST OR VERIFIER MAY RECOMPUTE A
      DIFFERENT ACCEPTED VALUE AT INSTALL TIME.
      IF A FUTURE IMPLEMENTATION AVOIDS EXECUTING THESE MODULES ENTIRELY — by an
      import construction that reaches the role module without running parent
      package code — THAT IS ALSO CONFORMING ONLY THROUGH A NEW REVIEWED
      GENERATION that states the construction and re-derives this surface. It is
      not something a build may decide for itself.

MS-12 THE M4 FIELD-BY-FIELD SEMANTIC SOURCE. Twenty-one keys, twenty-one
      sources. No key is satisfied by presence, by type, or by agreement with
      another copy of itself.
        KEY                            SEMANTIC SOURCE OF ITS VALUE
        schema                         the literal string at MS-4 (structural)
        version                        the integer 1 at MS-4 (structural)
        roots                          the five literal paths of §P1-3.1, in
                                       that section's order
        root_source_sha256             key set equal to those five paths; each
                                       value the SHA-256 of that root's bytes
                                       on disk (CHANGE 5)
        reachable_closure              the canonical value of MS-11.1, by the
                                       equality of MS-11.4
        p1_composite_sha256            H_FILE of the M1 composite on disk (G-7)
        p1_composite_body_sha256       H_BODY of the M1 composite (G-6)
        p1_composite_guarddata_sha256  H_GUARDDATA of the M1 composite (G-6)
        p1_composite_normative_sha256  H_NORMATIVE of the M1 composite (G-6)
        peer_amendment_sha256          the SHA-256 of the whole bytes of the M1
                                       AMENDMENT at MS-1's first literal path,
                                       recomputed from disk. IT IS NOT MERELY
                                       64 HEX CHARACTERS, and an arbitrary
                                       well-formed value does not pass. It must
                                       additionally equal Stage B's
                                       governing_amendment_sha256 (B18) and the
                                       manifest's own
                                       pre_selection_amendment_sha256
        pre_selection_packet_path      the literal packet path of TS-1
        pre_selection_packet_sha256    the SHA-256 of the whole bytes found at
                                       that literal path, recomputed from disk
        pre_selection_amendment_path   the literal amendment path of TS-1
        pre_selection_amendment_sha256 the SHA-256 of the whole bytes found at
                                       that literal path, recomputed from disk;
                                       equal to peer_amendment_sha256 because
                                       OR-4 does not change the amendment
        pre_selection_composite_path   the literal composite path of TS-1
        pre_selection_composite_sha256 THE ONE VALUE THAT CANNOT BE RECOMPUTED
                                       FROM ANY SURVIVING BYTES, and this is
                                       stated rather than disguised: it is the
                                       digest of the composite AS REVIEWED,
                                       before OR-4 deleted one branch of every
                                       variant block, and those bytes exist
                                       nowhere after OR-4. It is anchored
                                       instead to the PRE-SELECTION COMPOSITE
                                       ANCHOR LINE of §A0.4 of the M1
                                       amendment, whose own bytes are pinned by
                                       peer_amendment_sha256, by the install
                                       record and by Stage B's signature. The
                                       extraction rule is TS-2B A16(d). It is
                                       not a literal of the composite, because
                                       a file cannot carry its own digest
                                       (§P1-14.5, IR-4)
        stage_a_path                   TS-1's literal Stage-A path (A17)
        stage_a_sha256                 the SHA-256 of the Stage-A file (A17)
        stage_a_key_id                 Stage A's key_id (A17)
        project_import_dependencies    the closed surface of MS-13: four modules,
                                       four literal paths, four SHA-256 values
                                       RECOMPUTED FROM THE BYTES INSTALLED AT
                                       THOSE PATHS, the project import edges in
                                       execution order, the sorted stdlib seeds,
                                       the execution_order array and the
                                       thirty-two booleans of the four
                                       import_time_effects objects, all false
        created_utc                    MS-10 grammar and validator; compared
                                       with no other timestamp, orders nothing
      OWNERSHIP, STATED AS A PARTITION OF THE TWENTY-ONE KEYS. THREE keys —
      schema, version and created_utc — are settled ENTIRELY by the structural
      phase at CK-8 and are NOT re-evaluated anywhere; version 1.5 wrongly
      listed them inside CK-10's range, which contradicted VP-2's own
      no-re-evaluation rule even though they could never have become a later
      first failure. NINE keys — the six pre_selection_* and the three
      stage_a_* — are owned by TS-2B, evaluated at CK-9, and CK-10 DOES NOT
      EVALUATE THEM. The remaining NINE keys — roots, root_source_sha256,
      reachable_closure, the four p1_composite_* digests, peer_amendment_sha256
      and project_import_dependencies — are CK-10's entire range. 3 + 9 + 9 = 21. Version 1.4 told CK-7
      to evaluate "every MS-12 relation" while VP-3 assigned nine of them to
      CK-2; the two sentences contradicted each other.
      CK-10 EVALUATES EXACTLY NINE M4 SEMANTIC RELATION FAMILIES AND NO OTHER
      NUMBER. VERSION 1.6's CONCLUDING SENTENCE HERE SAID "EXACTLY THE ELEVEN
      ROWS THAT TS-2B DOES NOT OWN", WHICH CONTRADICTED THIS SECTION'S OWN
      3 + 9 + 9 = 21 PARTITION, CK-10's OWN NINE-ITEM LIST, VP-2, VP-3 AND
      VP-4. THAT SENTENCE IS WITHDRAWN. Eleven was the count before schema,
      version and created_utc were removed from CK-10's range; the removal was
      made and the count was not. NINE IS THE ONLY COUNT THIS PAIR STATES, and
      VP-3 remains the single authority on which key belongs to which owner.

IR-1  IDENTITY OF THE INSTALL RECORD.
        install_record_id = SHA-256( CANON( {
          "schema": "philosophia.officina.t-watchdog-authority-install-id.v1",
          "members": [ {"class": ..., "path": ..., "sha256": ...}, ... ]
        } ) )
      The preimage object has EXACTLY the two keys schema and members. "schema"
      is the STRING "philosophia.officina.t-watchdog-authority-install-id.v1",
      exactly. "members" is an ARRAY of exactly the 69 entries of MS-8. Each
      entry is an OBJECT with EXACTLY the three keys class, path and sha256,
      all three STRINGS. "class" is one of the seven literals "M1", "M2", "M3",
      "M4", "M5", "M6", "M7". "path" is the member's literal repository-
      relative path. "sha256" is 64 lowercase hexadecimal characters.
      ARRAY ORDER, and it is part of the value: ascending by "class" compared
      byte for byte, then by "path" compared byte for byte. The order is NOT
      re-derived by CANON, which sorts object keys only.
      The result is 64 lowercase hexadecimal characters.

IR-2  PATH.
        successor/officina/runtime_control/INSTALL/<install_record_id>.json
      THE RECORD IS CONTENT-ADDRESSED: its name IS a function of its members,
      so it cannot misdescribe them without changing its own name.

IR-3  THE INSTALL RECORD OBJECT. Installed atomic no-replace; file bytes
      exactly CANON of the object (MS-0). The top-level value is a JSON object
      whose key set is EXACTLY the five keys below, with exactly these types
      and value grammars:
        schema             STRING, exactly
                           "philosophia.officina.t-watchdog-authority-install.v1"
        version            INTEGER, exactly 1
        install_record_id  64-char lowercase hex STRING
        members            ARRAY of exactly 69 OBJECTS, each with EXACTLY the
                           three keys class, path and sha256 as IR-1 defines
                           them, IN IR-1's ORDER
        created_utc        STRING satisfying MS-10
      THE ABOVE IS THE STRUCTURAL PHASE ONLY. VERSION 1.3 ALSO WROTE INTO THIS
      VALUE GRAMMAR that install_record_id equals the IR-1 digest of the
      object's own members array and equals the filename stem. THAT SENTENCE IS
      WITHDRAWN FROM THE GRAMMAR — not from the gate. Those two equalities are
      SEMANTIC, CROSS-OBJECT relations; BOTH ARE OWNED BY CK-12, AND BY NO
      OTHER CHECK, and are refused with INSTALL_RECORD_NAME_MISMATCH, exactly as
      test row 105
expects. Version 1.3 made them part of a value grammar that a single
      structural check was told to enforce with MEMBER_SUBSTITUTED, so two
      conforming verifiers could return different first codes for one record;
      VP-1, VP-2 and VP-3 remove that ambiguity. Equality of the record's
      members array with the enumerated set is likewise semantic and is owned
      by CK-13.
      VERSION 1.5 STILL NAMED CK-8 AND CK-9 HERE WHILE ITS OWN VP-2, VP-3,
      CK-12, CK-6 and rows 105 and 106(e) NAMED CK-12. THE STALE NAMES ARE
      WITHDRAWN. They were not a mere labelling slip: at CK-8 the CK-11
      recomputation does not yet exist, so an implementation following IR-3
      literally had either an undefined prerequisite or a different first
      position. CK-12 IS THE SINGLE OWNER OF BOTH EQUALITIES, and it runs after
      CK-11 has produced the value it compares.
      THE RECORD IS NOT A MEMBER, AND VERSION 1.4 LEFT ITS STRUCTURAL POSITION
      UNSTATED. It is structurally validated at CK-6, which runs AFTER CK-5 has
      established that exactly one record exists and BEFORE any member is
      touched at CK-7. VP-4 states that order literally and VP-3 gives every
      record field its single owner.
      IT CARRIES DIGESTS AND NO RULES. It is a generated artifact, never a
      specification surface, never scientific evidence, never a covariate, and
      never an input to any acceptance predicate.

IR-4  THE INTEGRITY BINDING SUMMARY — EXPLICITLY NON-EXHAUSTIVE BY
      CONSTRUCTION, AND NOT THE NORMATIVE RELATION SURFACE.
      VERSION 1.5 CALLED THIS DIAGRAM COMPLETE. IT WAS NOT, AND THE CLAIM IS
      WITHDRAWN. Its derivation ranged over MS-4, MS-7, IR-1, IR-3, TS-1, TS-3
      and TS-4 and did NOT range over TS-2 or TS-5, which is where the verifier
      actually evaluates several cross-object equalities. B18 requires Stage B's
      governing_amendment_sha256 to equal M4's peer_amendment_sha256, and the
      diagram showed only a Stage-B digest edge to the M1 amendment. A15, A16
      and A17 compare Stage A DIRECTLY with named M4 fields, and the diagram
      showed only parallel bindings to a common input. IR-2 makes the record's
      id its filename, and the diagram named no id-to-path edge.
      THIS DIAGRAM IS THEREFORE A SUMMARY. It groups relations by their common
      target so that a reader can see the shape of the binding; it is a
      QUOTIENT of the real relation set under that grouping, and a quotient is
      not the thing it quotients. IT IS NOT NORMATIVE FOR OWNERSHIP, FOR
      COMPLETENESS OR FOR ANY REFUSAL. THE NORMATIVE, EXHAUSTIVE SURFACE IS
      IR-13, and where the two differ IR-13 governs.
      THE SUMMARY, STATED AS IT ACTUALLY IS.
      VERSION 1.2 SAID "EVERY MEMBER IS ATTESTED BY EXACTLY ONE OTHER OBJECT",
      AND ITS TEST ROW 115 SAID "BY THE RECORD AND BY NOTHING ELSE". BOTH
      STATEMENTS WERE FALSE AND ARE WITHDRAWN. M4 carries the two M1 digests
      and the Stage-A binding; M7 carries the M5 and M6 digests; and the
      record carries every member digest. There are therefore members with more
      than one inbound integrity edge.
      VERSION 1.3 THEN CALLED ITS OWN GRAPH COMPLETE WHILE OMITTING THREE REAL
      EDGES. Stage A's governing_pre_selection carries a path and a digest for
      the packet, the amendment and the composite; those are three directed
      integrity edges from Stage A, parallel to M4's three, and neither IR-4,
      nor the packet's summary, nor §P1-14.5, nor row 115 listed them. They are
      added below. A fourth edge, from the M1 amendment's anchor line to the
      pre-selection composite bytes, is new in version 1.4 and is listed too.
      THE SUMMARY GRAPH — A QUOTIENT, EXPLICITLY NOT COMPLETE, with every
      edge it does draw labelled by what it binds. VERSION 1.6 STILL HEADED
      THIS LIST WITH A SENTENCE CALLING IT THE ACTUAL AND COMPLETE GRAPH, WHILE
      THE SAME SECTION HAD ALREADY WITHDRAWN THE COMPLETENESS CLAIM ABOUT
      ITSELF; THAT HEADING IS WITHDRAWN TOO. Nothing may be inferred from what this list
      does not draw. IR-13 is the exhaustive surface, under the exact relation
      class IR-13 states:
        install record  --digest-->  each of the 69 members
                                     (M1 2, M2 55, M3 7, M4 1, M5 1, M6 2, M7 1)
        M4 manifest     --digest-->  the M1 composite, by p1_composite_sha256
                        --digest-->  the M1 amendment, by peer_amendment_sha256.
                                     THIS EDGE WAS CLAIMED IN VERSION 1.3 AND
                                     ENFORCED BY NOTHING; MS-12 and CK-10 make it
                                     real
                        --digest-->  the five production roots
                        --digest-->  the three composite region digests and the
                                     composite file digest
                        --path+digest-->  the three pre-selection inputs
                        --path+digest+key id-->  Stage A
        Stage A         --path+digest-->  the pre-selection packet
                        --path+digest-->  the pre-selection amendment
                        --path+digest-->  the pre-selection composite
                                     (THE THREE EDGES VERSION 1.3 OMITTED)
                        --key pin-->  the one key under which Stage B verifies
        M1 amendment    --anchor line digest-->  the pre-selection composite
                                     bytes, per §A0.4 and TS-2 A16(d)
        M7 attestation  --digest-->  M5
                        --digest-->  each of the two M6 modules
                        --digest-->  the M6 canonical bundle digest
                        --assertion-->  that the matrix ran and every row of
                                     92..115 passed
        Stage B         --path+digest+key id-->  Stage A
                        --selected_option_token equality (B14)-->  Stage A
                                     (THE EDGE VERSION 1.4 OMITTED. It is the
                                     link that makes the option token inside the
                                     SIGNED Stage-B bytes agree with the option
                                     the author selected in Stage A, and TR-2
                                     lists an option mismatch between the two
                                     stages as a closed proper-subset case. A
                                     graph that carries the key pin, the member
                                     count and the M7 assertions cannot exclude
                                     an option equality and still call itself
                                     complete.)
                        --id+path+count-->  the install record and the member set
                        --digest-->  the two M1 members
        detached sig    --Ed25519-->  the exact canonical Stage-B bytes
      THE SUMMARY ABOVE IS DERIVED FROM IR-13 BY ONE STATED QUOTIENTING RULE
      AND BY NO OTHER: relations that bind the SAME PAIR OF OBJECTS are drawn as
      one labelled edge, and relations whose subject is a clause of TS-2 or TS-5
      are drawn at the object they ultimately constrain rather than at the
      clause that evaluates them. THAT RULE LOSES INFORMATION ON PURPOSE, WHICH
      IS WHY THIS DIAGRAM IS NOT CALLED COMPLETE AND WHY NOTHING MAY BE INFERRED
      FROM ITS SILENCE. IR-13 is the surface a reviewer audits.
      ONE RELATION IS DELIBERATELY NOT AN EDGE AND IS NAMED SO THAT ITS ABSENCE
      IS NOT MISTAKEN FOR AN OMISSION: A9's pairing of Stage A's
      selected_option_amendment_token with its own selected_option_token is an
      INTRA-OBJECT consistency constraint inside Stage A, not a relation between
      two objects, so it is a clause of TS-2A and not an edge of this graph.
      THESE ADDITIONAL EDGES ARE INTENTIONAL AND ARE NOT SELF-ATTESTATION.
      Redundant inbound edges make a partial substitution fail in more than one
      place; they never let an object vouch for itself.
      WHAT REMAINS TRUE, AND IS THE ACTUAL PROPERTY: NO OBJECT ATTESTS ITSELF.
      The record is not a member of itself and install_record_id is not in its
      own preimage; no member carries its own digest; Stage A carries no digest
      of itself; Stage B carries no signature of itself; the manifest carries
      no digest of itself; the attestation does not attest itself; the
      composite carries none of its own digests.
      NO UNIQUENESS OF ATTESTER IS CLAIMED, AND NO RULE DEPENDS ON ONE. NO
      UNIQUENESS OF EXTERNAL ATTESTER IS CLAIMED EITHER: Stage A is the only
      key pin these bytes define, and nothing here asserts that it is the only
      object that could ever vouch for a member.

IR-13 THE NORMATIVE CROSS-OBJECT AND EXTERNAL INTEGRITY-BINDING REGISTER —
      EXHAUSTIVE UNDER THE EXACT RELATION CLASS STATED BELOW, AND THE SURFACE
      THAT REPLACES THE WITHDRAWN COMPLETENESS CLAIM OF IR-4.
      WHY THE VERSION-1.6 BOUNDARY IS WITHDRAWN. It defined this table by a LIST
      OF SECTIONS, called the table exhaustive over that list, and then mixed
      object-to-literal rows with at least one purely intra-object row. The two
      independent review lines read the same bytes and returned OPPOSITE answers
      about whether it was exhaustive: one found no omission, the other
      constructed a refusable object-to-literal relation the table did not
      carry. A boundary that produces two honest opposite answers is not a
      boundary. IT IS REPLACED, AND SECTION COUNTING IS ABANDONED: no count of
      sections — fifteen, sixteen or any other — appears in this definition or
      anywhere in this pair, and none may be reintroduced.
      THE INCLUSION RULE, MACHINE-CHECKABLE, APPLIED PREDICATE BY PREDICATE. For
      each refusal predicate P over an object O, let CODOMAIN(P) be the source
      of the value that P requires O's value to equal, to contain, to be one
      of, or to verify against. P IS A ROW OF THIS REGISTER IF AND ONLY IF
      CODOMAIN(P) IS OF AT LEAST ONE OF THESE FIVE KINDS:
        K1  THE BYTES OF A DIFFERENT DURABLE OBJECT, a field of one, or a digest
            recomputed from one;
        K2  A CONTENT ADDRESS — an identifier that is a digest over a set of
            durable objects rather than a value declared inside O;
        K3  A CANONICAL PATH OR FILENAME — of O itself or of a different durable
            object — including the requirement that a durable object EXIST at
            that path;
        K4  THE AUTHOR-SELECTED OPTION TOKEN SET, whose two members are defined
            by the author choice packet and bound across the two stages at B14;
        K5  A GOVERNING EXTERNAL CONSTANT whose value is fixed in a section
            OTHER THAN O's OWN SCHEMA TABLE — for example TR-2's threat-model
            string, MS-8's enumerated member count, MS-11.1's canonical closure,
            MS-13's four module values, §P1-3.1's root list, MS-2's and MS-3's
            recorded digests, MS-6's order and IR-2's INSTALL prefix.
      THE EXCLUSION RULE, ITS EXACT COMPLEMENT. P IS NOT A ROW IF CODOMAIN(P) IS
      OF NONE OF K1..K5, WHICH HAPPENS EXACTLY WHEN IT IS OF ONE OF THESE THREE
      KINDS:
        K6  O's OWN schema, version, author or signature-algorithm LITERAL, as
            declared in O's own schema table at MS-4, MS-7, IR-3, TS-1 or TS-3;
        K7  AN ADMISSIBILITY PREDICATE over O's own bytes — JSON parseability,
            object-ness, exact key set at any depth, value type, lexical
            grammar, array cardinality, element shape, order, sortedness,
            pairwise distinctness, self-closure, CANON identity, and the MS-10
            created_utc grammar and semantic validator;
        K8  AN INTRA-OBJECT DERIVED RELATION — a value computed from ANOTHER
            FIELD OF O ITSELF, naming no other durable object, no path and no
            constant defined outside O's own schema table.
      K1..K8 ARE TOTAL OVER THE REFUSAL PREDICATES OF MS-0, MS-4, MS-6, MS-7,
      MS-8, MS-9, MS-10, MS-11, MS-12, MS-13, IR-1, IR-2, IR-3, TS-1, TS-2A,
      TS-2B, TS-3, TS-4, TS-5 AND VP-1, so every predicate of this pair is
      either a ROW below or an AUDITED EXCLUSION in the coverage index at the
      foot, and NOTHING FALLS BETWEEN THEM. Where more than one of K1..K5
      applies, the row records the most specific kind; the recorded kind is a
      LABEL ONLY and never decides membership, which depends solely on whether
      any of K1..K5 applies.
      WHAT EXCLUSION DOES AND DOES NOT MEAN. AN EXCLUDED PREDICATE REMAINS FULLY
      NORMATIVE IN ITS OWNING TS, VP OR CK CLAUSE, REFUSES EXACTLY AS THAT
      CLAUSE SAYS, AND IS WEAKENED BY NOTHING HERE. Exclusion says only that the
      predicate is not a cross-object or external integrity BINDING and
      therefore is not accounted for in this register. THE COVERAGE INDEX IS
      NON-BINDING BOOKKEEPING: where it and an owning clause differ, the owning
      clause governs and the index is the defect.
      TWO CLAIMS THIS REGISTER DOES NOT MAKE, STATED SO THAT NO READER INFERS
      THEM: it is NOT exhaustive over "every validator predicate", and it is NOT
      exhaustive "over a list of sections". It is exhaustive over the K1..K5
      relation class and over nothing else.
      EVERY ROW HAS EXACTLY ONE EARLIEST OWNER AND EXACTLY ONE CODE, AND NO ROW
      MAPS ONE PREDICATE TO TWO CODES. Version 1.6's single record-cardinality
      row mapped one predicate to INSTALL_RECORD_ABSENT and
      INSTALL_RECORD_REPLAYED; it is SPLIT into rows 7 and 8, which preserve the
      executable CK-5 distinction between absence and replay exactly and change
      no behaviour.

        #   RELATION                                        OWNER   CODE
        1   record.members[i].sha256 = digest of that
            member's bytes on disk                          CK-13   MEMBER_STALE
                                                            K1
        2   record.members[i].(class,path) = the enumerated
            (class,path) at index i                         CK-13   MEMBER_SUBSTITUTED
                                                            K5
        3   every enumerated member EXISTS at its literal
            path                                            CK-7    MEMBER_OMITTED
                                                            K3
        4   every M2 and M3 member's recomputed digest =
            the literal digest at MS-2 or MS-3              CK-7    HISTORICAL_BYTE_MOVED
                                                            K5
        5   record.install_record_id = IR-1 recomputation
            over the members found on disk                  CK-12   INSTALL_RECORD_NAME_MISMATCH
                                                            K2
        6   record.install_record_id = the record's own
            filename stem  (IR-2)                           CK-12   INSTALL_RECORD_NAME_MISMATCH
                                                            K3
        7   AT LEAST ONE hex-named record exists directly
            under the INSTALL directory                     CK-5    INSTALL_RECORD_ABSENT
                                                            K3
        8   AT MOST ONE hex-named record exists directly
            under the INSTALL directory                     CK-5    INSTALL_RECORD_REPLAYED
                                                            K3
        9   M4.roots = the five literal paths of §P1-3.1 in
            that order                                      CK-10   MANIFEST_VALUE_MISMATCH
                                                            K5
       10   M4.root_source_sha256 key set = those five
            paths; each value = that root's byte digest     CK-10   MANIFEST_VALUE_MISMATCH
                                                            K1
       11   M4.reachable_closure = MS-11.1's canonical
            eighty-nine-row value                           CK-10   MANIFEST_VALUE_MISMATCH
                                                            K5
       12   M4.p1_composite_sha256 = H_FILE of the M1
            composite                                       CK-10   MANIFEST_VALUE_MISMATCH
                                                            K1
       13   M4.p1_composite_body_sha256 = H_BODY            CK-10   MANIFEST_VALUE_MISMATCH
                                                            K1
       14   M4.p1_composite_guarddata_sha256 = H_GUARDDATA  CK-10   MANIFEST_VALUE_MISMATCH
                                                            K1
       15   M4.p1_composite_normative_sha256 = H_NORMATIVE  CK-10   MANIFEST_VALUE_MISMATCH
                                                            K1
       16   M4.peer_amendment_sha256 = the M1 amendment's
            byte digest                                     CK-10   MANIFEST_VALUE_MISMATCH
                                                            K1
       17   M4.project_import_dependencies.modules[k].sha256
            = the digest of the bytes at that literal path,
            for each of the four modules of MS-13           CK-10   MANIFEST_VALUE_MISMATCH
                                                            K1
       18   M4.project_import_dependencies.modules[k].path,
            .project_imports, .stdlib_seeds and the EIGHT
            BOOLEANS OF .import_time_effects = MS-13's
            values, the thirty-two booleans all false       CK-10   MANIFEST_VALUE_MISMATCH
                                                            K5
       19   M4.project_import_dependencies.execution_order
            = MS-13's literal array                         CK-10   MANIFEST_VALUE_MISMATCH
                                                            K5
       20   StageA.governing_pre_selection.*.path = M4's
            three pre_selection_*_path fields               CK-9    STAGE_A_PRESELECTION_MISMATCH
                                                            (A15)   K1
       21   StageA.governing_pre_selection.*.sha256 = M4's
            three pre_selection_*_sha256 fields             CK-9    STAGE_A_PRESELECTION_MISMATCH
                                                            (A16(a))  K1
       22   StageA packet digest = the digest of the bytes
            at TS-1's literal packet path                   CK-9    STAGE_A_PRESELECTION_MISMATCH
                                                            (A16(b))  K1
       23   StageA amendment digest = the digest of the
            bytes at TS-1's literal amendment path          CK-9    STAGE_A_PRESELECTION_MISMATCH
                                                            (A16(c))  K1
       24   StageA composite digest = the unique §A0.4
            anchor value of the M1 amendment, extracted by
            the A16(d) rule on the V2_10 token              CK-9    STAGE_A_PRESELECTION_MISMATCH
                                                            (A16(d))  K1
       25   SHA-256(Stage A file) = M4.stage_a_sha256       CK-9    STAGE_A_BINDING_MISMATCH
                                                            (A17)   K1
       26   TS-1's literal Stage-A path = M4.stage_a_path   CK-9    STAGE_A_BINDING_MISMATCH
                                                            (A17)   K3
       27   StageA.key_id = M4.stage_a_key_id               CK-9    STAGE_A_BINDING_MISMATCH
                                                            (A17)   K1
       28   a file EXISTS at TS-1's exact literal Stage-A
            path                                            CK-2    STAGE_A_ABSENT
                                                            (A1)    K3
       29   the Stage-B .json EXISTS at TS-3's exact
            literal .json path                              CK-3    STAGE_B_ABSENT
                                                            (B1)    K3
       30   the detached .sig EXISTS at TS-3's exact literal
            .sig path, the .json being present               CK-3    STAGE_B_SIGNATURE_ABSENT
                                                            (B1)    K3
       31   StageB.stage_a_path = TS-1's literal path       CK-3    STAGE_B_STAGE_A_MISMATCH
                                                            (B13)   K3
       32   StageB.stage_a_sha256 = SHA-256 of the Stage-A
            file on disk                                    CK-3    STAGE_B_STAGE_A_MISMATCH
                                                            (B13)   K1
       33   StageB.key_id = StageA.key_id                   CK-3    STAGE_B_STAGE_A_MISMATCH
                                                            (B13)   K1
       34   the detached .sig verifies under StageA's
            32-byte public key and no other, over the exact
            Stage-B bytes                                   CK-3    STAGE_B_SIGNATURE_INVALID
                                                            (B12)   K1
       35   StageB.selected_option_token =
            StageA.selected_option_token                    CK-14   STAGE_B_OPTION_MISMATCH
                                                            (B14)   K1
       36   StageB.install_record_id = the CK-11
            recomputation                                   CK-14   STAGE_B_INSTALL_ID_MISMATCH
                                                            (B15)   K2
       37   StageB.install_record_path names the record
            file established at CK-5 and matched at CK-12   CK-14   STAGE_B_INSTALL_ID_MISMATCH
                                                            (B16)   K3
       38   StageB.member_count = the enumerated count 69   CK-14   STAGE_B_INSTALL_ID_MISMATCH
                                                            (B17)   K5
       39   StageB.governing_amendment_sha256 = the M1
            amendment's digest on disk                      CK-14   STAGE_B_GOVERNING_MISMATCH
                                                            (B18)   K1
       40   StageB.governing_composite_sha256 = the M1
            composite's digest on disk                      CK-14   STAGE_B_GOVERNING_MISMATCH
                                                            (B18)   K1
       41   StageB.governing_amendment_sha256 =
            M4.peer_amendment_sha256   THE DIRECT STAGE-B
            TO M4 EQUALITY THE IR-4 SUMMARY DID NOT SHOW    CK-14   STAGE_B_GOVERNING_MISMATCH
                                                            (B18)   K1
       42   M7.verifier_path = MS-5's literal path          CK-15   ATTESTATION_MISMATCH
                                                            K3
       43   M7.verifier_sha256 = the M5 digest found at
            CK-7                                            CK-15   ATTESTATION_MISMATCH
                                                            K1
       44   M7.test_bundle_modules = MS-6's two literal
            paths in MS-6's order, with the two M6 digests
            found at CK-7                                   CK-15   ATTESTATION_MISMATCH
                                                            K1
       45   M7.test_bundle_digest = MS-6's canonical bundle
            digest recomputed from those two entries        CK-15   ATTESTATION_MISMATCH
                                                            K1
       46   M7.rows_attested = the 24 integers 92..115;
            row_count = 24; all_rows_passed = true          CK-15   ATTESTATION_MISMATCH
                                                            K5
       47   StageA.selected_option_token is one of TS-1's
            two literal option tokens                       CK-2    STAGE_A_OPTION_INVALID
                                                            (A8)    K4
       48   StageA.threat_model = the exact string quoted
            at TR-2                                         CK-2    STAGE_A_MALFORMED
                                                            (A14)   K5
       49   StageA.governing_pre_selection's three paths =
            TS-1's three literal path strings, which are
            the canonical paths of three durable objects    CK-2    STAGE_A_MALFORMED
                                                            (A13)   K3
       50   StageB.install_record_path = the literal
            concatenation of IR-2's INSTALL prefix,
            install_record_id and ".json"                   CK-3    STAGE_B_MALFORMED
                                                            (B9)    K3

      FIFTY RELATIONS, EACH WITH EXACTLY ONE EARLIEST OWNER AND EXACTLY ONE
      CODE. Rows 47 through 50 relate an object to a value fixed OUTSIDE its own
      schema table — the author-selected option set, TR-2's threat-model string,
      three governing canonical paths and IR-2's INSTALL prefix — and they are
      rows for that reason and for no other; they are also the rows the IR-4
      summary has no way to draw.

      EVERY CHANGE FROM THE 47 ROWS OF VERSION 1.6, WITH ITS REASON:
        SPLIT   version 1.6 row 7, one predicate with two codes, becomes rows 7
                and 8. Zero records under the INSTALL directory and two or more
                records are DIFFERENT predicates with DIFFERENT codes, and CK-5
                already executes them separately; the register now records them
                separately. No behaviour changes and no state loses an answer.
        MOVED   version 1.6 row 44 — StageA.key_id = SHA-256 of the 32 raw bytes
                OUT     of its own public_key_hex — is REMOVED from the register
                and recorded in the coverage index as K8. Its codomain is a
                digest of ANOTHER FIELD OF STAGE A ITSELF: it names no other
                durable object, no path and no constant defined outside TS-1's
                own schema table. IT REMAINS FULLY NORMATIVE AT TS-2A A11,
                refused at CK-2 with STAGE_A_KEY_MALFORMED, and row 106(b) still
                tests it. NOTHING IS WEAKENED; the register stops carrying an
                intra-object relation that made its own boundary incoherent.
        ADDED   rows 28, 29 and 30. TS-2A A1 and TS-5 B1 require three durable
                objects to EXIST at three governing canonical paths, which is
                kind K3 — the same class as row 3, which version 1.6 already
                carried for members, and rows 7 and 8, which it carried for the
                record. Version 1.6 carried the member and record existence
                relations and omitted the Stage-A and Stage-B ones. B1 carries
                two codes and is therefore split at the same time: an absent
                .json is STAGE_B_ABSENT, and an absent .sig beside a present
                .json is STAGE_B_SIGNATURE_ABSENT, exactly as B1 already
                executes.
        KEPT    every other row, with its owner and code unchanged. Row 18 gains
                the words that name where the eight booleans live; the relation
                it states is the one version 1.6 stated.
      47 - 1 + 1 + 3 = 50.

      THE COVERAGE INDEX — NON-BINDING, AND EXHAUSTIVE OVER THE EXCLUSIONS.
      Every refusal predicate of this pair that is NOT a row above appears here
      with its kind, its owning clause and its code. It exists so that a
      reviewer can verify totality mechanically rather than by search.
        TS-2A A2   CANON identity of the Stage-A bytes        K7  CK-2 STAGE_A_MALFORMED
        TS-2A A3   exact eleven-key set                        K7  CK-2 STAGE_A_MALFORMED
        TS-2A A4   schema literal                              K6  CK-2 STAGE_A_MALFORMED
        TS-2A A5   version literal                             K6  CK-2 STAGE_A_MALFORMED
        TS-2A A6   author = "Kirill Kruglov"                   K6  CK-2 STAGE_A_MALFORMED
        TS-2A A7   signature_algorithm = "Ed25519"             K6  CK-2 STAGE_A_MALFORMED
        TS-2A A9   amendment token paired with A8's value      K8  CK-2 STAGE_A_OPTION_INVALID
        TS-2A A10  public_key_hex length and alphabet          K7  CK-2 STAGE_A_KEY_MALFORMED
        TS-2A A11  key_id = SHA-256 of its own 32 raw key
                   bytes                                       K8  CK-2 STAGE_A_KEY_MALFORMED
        TS-2A A12  governing_pre_selection nested shape        K7  CK-2 STAGE_A_MALFORMED
        TS-2A A14  created_utc grammar and validator           K7  CK-2 STAGE_A_MALFORMED
        TS-5  B2   CANON identity of the Stage-B bytes         K7  CK-3 STAGE_B_MALFORMED
        TS-5  B3   exact thirteen-key set                      K7  CK-3 STAGE_B_MALFORMED
        TS-5  B4   schema literal                              K6  CK-3 STAGE_B_MALFORMED
        TS-5  B5   version literal                             K6  CK-3 STAGE_B_MALFORMED
        TS-5  B6   created_utc grammar and validator           K7  CK-3 STAGE_B_MALFORMED
        TS-5  B7   member_count is the INTEGER 69, as TS-3's
                   own key table declares it                   K7  CK-3 STAGE_B_MALFORMED
        TS-5  B8   five 64-hex lexical grammars                K7  CK-3 STAGE_B_MALFORMED
        TS-5  B10  signature_algorithm = "Ed25519"             K6  CK-3 STAGE_B_ALGORITHM_INVALID
        TS-5  B11  the .sig is exactly 128 lowercase hex
                   characters and nothing else (TS-4)          K7  CK-3 STAGE_B_MALFORMED
        VP-1  S1   existence of the record                     — rows 7 and 8
        VP-1  S1   existence of M4 and of M7                   — row 3; both are members
        VP-1  S2..S8  parse, object-ness, exact key set at
                   every depth, types, CANON identity, schema
                   and version literals, array cardinality,
                   element shape, order, sortedness, pairwise
                   distinctness, self-closure and lexical
                   grammars, for the record at CK-6 and for
                   M4 and M7 at CK-8                           K6, K7  MEMBER_SUBSTITUTED
        MS-0       CANON as a requirement on any hashed
                   artifact's own bytes                        K7  the owning object's structural check
        MS-8       total member cardinality                    — a property of the literal enumeration,
                                                                 not of any installed object
        MS-9       pairwise disjointness of the seven classes  — the same
        MS-10      the created_utc grammar and validator       K7  the owning object's structural check
        FS-4       PROCEDURE_VIOLATION_OBSERVED                — a contemporaneous observation of DRIVER
                                                                 state, not a relation over durable
                                                                 objects; FS-2 states its limits
        CK-11      the id recomputation itself                 — not a refusal predicate; its two
                                                                 consumers are rows 5 and 36
        CK-7       the member digest recomputation itself      — not a refusal predicate; its two
                                                                 refusals are rows 3 and 4
      THE INDEX IS COMPLETE AGAINST TS-2A A1..A14, TS-2B A15..A17, TS-5 B1..B18,
      VP-1 S1..S8 AS APPLIED AT CK-6 AND CK-8, AND CK-5, CK-7, CK-10, CK-12,
      CK-13 AND CK-15: every clause of those tables is either a row above or an
      entry here, and no clause is in both.
      SPECIFICALLY, AND BECAUSE THE Y LINE CONSTRUCTED THESE EXACT CASES: a
      Stage A whose author is "Mallory" is refused at A6 with
      STAGE_A_MALFORMED; a Stage A whose signature_algorithm is not "Ed25519"
      is refused at A7; a Stage B whose signature_algorithm is not "Ed25519" is
      refused at B10 with STAGE_B_ALGORITHM_INVALID; a Stage B whose
      member_count is not the integer 69 is refused at B7 with
      STAGE_B_MALFORMED. NONE OF THE FOUR IS A ROW OF THIS REGISTER, EACH IS AN
      AUDITED K6 OR K7 EXCLUSION ABOVE, AND EACH STILL REFUSES EXACTLY WHERE ITS
      OWNING CLAUSE SAYS. The register no longer claims to carry them, so the
      counterexample no longer exists: it was a claim defect, not a missing
      refusal, and the claim is what changed. Note that member_count is ALSO row
      38, at B17 and CK-14, where it is compared with the ENUMERATED count
      rather than with TS-3's own declared literal; the earlier clause owns a
      malformed value and the later clause owns a well-formed but disagreeing
      value, exactly as VP-3 already states for every twice-appearing field.
      NO UNIQUENESS OF ATTESTER IS CLAIMED BY THIS REGISTER AND NO RULE DEPENDS
      ON ONE. Several objects appear as the subject of more than one row and
      several as the object of more than one; that redundancy is intentional, is
      what makes a partial substitution fail in more than one place, and is not
      self-attestation.
      NO OBJECT ATTESTS ITSELF, STATED EXACTLY. No row makes an object's
      acceptance depend on a digest or a signature CARRIED BY THAT SAME OBJECT.
      Rows 6 and 50 relate a field of an object to a NAME — a filename stem and
      a path — and a name is not an attestation and carries no digest of what it
      names; the record's name is determined by row 5 from the members, and
      Stage B's install_record_path is checked against the real record at row 37.

IR-5  THE TRUST ROOT IS EXTERNAL TO THE INSTALLED SET AND IS THE TWO-STAGE
      AUTHENTICATED PROTOCOL OF TS-1..TS-6. Version 1.1's formulation — "the
      author signature file that carries the watchdog-freeze selection" — is
      WITHDRAWN as underspecified: it named no path, no schema, no key set, no
      signature algorithm, no signer-key identifier and no verification rule,
      so a substituted file could authorize a different internally consistent
      record. Nothing replaces it except TS-1..TS-6, and no other object of any
      kind authorizes an install. What that protocol does and does not achieve
      is stated exactly at TR-1, TR-2 and FS-1..FS-5, and no section may claim
      more.

IR-6  CREATION ORDER is exactly OR-1 through OR-11 and no other order is
      CONFORMING. CONFORMING IS NOT THE SAME AS MECHANICALLY DISTINGUISHABLE:
      FS-1 states what the final-state gate proves, FS-2 states what it cannot
      prove, and FS-3 keeps the order a mandatory obligation regardless.

IR-7  NO-REPLACE. An EEXIST at the record path means an identical installed set
      is already recorded. THE RECORD IS NEVER OVERWRITTEN, TRUNCATED, RENAMED
      OR DELETED. A changed installed set produces a DIFFERENT name, so a new
      install never collides with an old one and an old one is never silently
      reinterpreted.

IR-8  WHEN THE CHECK RUNS is exactly CK-1.

IR-9  THE CHECK is exactly CK-2 through CK-15, executed in that order,
      fail-closed at the first failure. THE MEMBER ENUMERATION IS CK-4 AND
      DRAWS ONLY ON MS-1..MS-7. The checks are partitioned into the two phases
      of VP-1 and VP-2; VP-3 gives every field and every cross-object relation
      of every generated object exactly one owning clause and exactly one code;
      and VP-4 states the literal topological order in which the prerequisites
      of every predicate are established before that predicate runs.

IR-10 FAIL-CLOSED RECOVERY is exactly FC-1.

IR-11 MIXED GENERATIONS ARE REJECTED BY CONSTRUCTION. MS-1 names two literal
      paths. The v1.6 amendment installed with composite v1.10, the v1.7
      amendment installed with composite v1.9, and any other mixture of a
      v2.9-era with a v2.10-era governing file, leave one of MS-1's two literal
      paths absent or carrying bytes that produce a different digest, so the
      set fails at CK-7 or CK-13 and, if a record is rebuilt around the
      mixture, at B15 of TS-5.

IR-12 VERIFYING A DIGEST IS NOT OPENING A DOCUMENT FOR BEHAVIOUR. The
      document-level authority rule is not weakened by M2 or M3: the check
      reads those bytes to hash them and never interprets any of them as a
      rule.

TS-1  STAGE A — WATCHDOG OPTION SELECTION AND KEY PIN. Literal path:
        successor/officina/authorization/P1_WATCHDOG_FREEZE_SELECTION_V1.json
      ENCODING: the file bytes are exactly CANON of the object (MS-0).
      The top-level value is a JSON object whose key set is EXACTLY the eleven
      keys below, with exactly these types and value grammars:

        schema       STRING, exactly
                     "philosophia.officina.t-p1-watchdog-freeze-selection.v1"
        version      INTEGER, exactly 1
        author       STRING, exactly "Kirill Kruglov"
        selected_option_token
                     STRING, EXACTLY ONE of the two EXISTING option tokens,
                     and no other value validates:
                       I_SELECT_P1_WATCHDOG_FREEZE_A_WATCHDOG_REQUESTS_PCS_EXECUTES
                       I_SELECT_P1_WATCHDOG_FREEZE_B_PCS_FREEZES_ON_PEER_ENDPOINT_LOSS
                     NO THIRD OPTION EXISTS AND NONE IS CREATED HERE.
        selected_option_amendment_token
                     STRING, the EXISTING option-specific amendment token
                     paired with the value above, and no other:
                       P1_WATCHDOG_SINGLE_OPCODE_CAPABILITY_V1 pairs with the
                         token whose name contains _FREEZE_A_
                       P1_WATCHDOG_SENSOR_ONLY_PCS_FREEZE_V1   pairs with the
                         token whose name contains _FREEZE_B_
                     A crossed pair does not validate.
        signature_algorithm
                     STRING, exactly "Ed25519"
        public_key_hex
                     STRING of EXACTLY 64 characters, each one of
                     0123456789abcdef, decoding to the 32-byte Ed25519 public
                     key of RFC 8032
        key_id       STRING of EXACTLY 64 characters, each one of
                     0123456789abcdef, equal to the SHA-256 of the 32 RAW key
                     bytes — not of the hexadecimal text
        governing_pre_selection
                     OBJECT with EXACTLY the three keys packet, amendment and
                     composite. Each value is an OBJECT with EXACTLY the two
                     keys path and sha256, both STRINGS, the sha256 being 64
                     lowercase hexadecimal characters. THE THREE path VALUES
                     ARE THESE EXACT LITERAL REPOSITORY-RELATIVE STRINGS:
                       packet
                         successor/OFFICINA_P1_WATCHDOG_FREEZE_AUTHOR_CHOICE_PACKET_V2_10_CORRECTION.md
                       amendment
                         successor/OFFICINA_GENERIC_HARNESS_WATCHDOG_FREEZE_AUTHORITY_AMENDMENT_V1_7_DRAFT.md
                       composite
                         successor/OFFICINA_GENERIC_HARNESS_SUPERVISOR_CONTROL_CHANNEL_P1_OPERATIVE_COMPOSITE_V1_10.md
                     THESE THREE PATHS ARE THE CURRENT GENERATION'S, AND VERSION
                     1.6 LEFT THEM AT THE PREVIOUS GENERATION'S. There they
                     named the v2.8 packet, the v1.5 amendment and composite
                     v1.8 while MS-1 named the v1.6 amendment and composite
                     v1.9 and §A0.4 anchored composite v1.9's digest, so
                     A16(c) required Stage A's amendment digest to equal BOTH
                     the digest of the v1.5 bytes AND, through
                     peer_amendment_sha256, the digest of the v1.6 bytes, which
                     no byte state satisfies, and A16(d) compared a v1.8 path
                     against a v1.9 anchor value. THAT IS THE SAME
                     INCOMPLETE-RE-SCOPE DEFECT THE INDEPENDENT X LINE
                     DEMONSTRATED AT A16(d), AT A SECOND LOCUS, AND IT IS
                     REPAIRED HERE: the amendment path is MS-1's first literal
                     path, the composite path is MS-1's second, and the packet
                     path is the packet of this generation.
                     THE THREE sha256 VALUES ARE THE PRE-SELECTION DIGESTS:
                     the bytes the independent X and Y lines confirmed BEFORE
                     any variant block was resolved. The amendment path and the
                     composite path are the same literal strings as MS-1's two
                     paths, but the composite's PRE-SELECTION digest is not its
                     M1 digest, because OR-4 changes the composite's bytes; the
                     amendment's two digests are equal only because OR-4 does
                     not change the amendment.
                     EACH OF THE THREE HAS AN EXTERNAL ANCHOR, AND VERSION 1.3
                     HAD NONE. Version 1.3 required only that Stage A's three
                     digests equal the manifest's three, so a coordinated
                     arbitrary triple written into both artifacts passed. TS-2
                     A16, now a clause of TS-2B, requires each of the three to
                     equal a value derived from named repository bytes at
                     validation time:
                     A16(b) recomputes the packet digest from the bytes at the
                     literal packet path; A16(c) recomputes the amendment
                     digest from the bytes at the literal amendment path; and
                     A16(d) reads the composite's pre-selection digest from the
                     unique anchor line of §A0.4 of the M1 amendment, because
                     the pre-selection composite bytes do not survive OR-4 and
                     no file may carry its own digest. EQUALITY OF STAGE A WITH
                     M4 ALONE IS NO LONGER SUFFICIENT FOR ANY OF THE THREE.
        threat_model STRING equal, byte for byte, to the exact string quoted
                     at TR-2
        created_utc  STRING satisfying MS-10

      STAGE A IS CREATED ONLY AFTER KIRILL HAS EMITTED ONE EXPLICIT OPTION
      TOKEN. NEITHER THE KEY PAIR, NOR THE ENTROPY THAT PRODUCES IT, NOR THIS
      ARTIFACT IS AUTHORIZED BY THE DRAFTING ROUND THAT PRODUCED THESE BYTES.

TS-2  STAGE A VERIFICATION — AN EXHAUSTIVE FIELD-BY-FIELD ALGORITHM IN TWO
      STAGES, SPLIT BY WHAT EACH CLAUSE IS ALLOWED TO READ. EVERY MANDATORY
      LITERAL AND EVERY DERIVED RELATION IS CHECKED. NO FIELD IS SATISFIED BY
      MERE PRESENCE. Each stage is executed in the order written, fail-closed at
      the first failure.
      TS-2A, THE SELF-CONTAINED STAGE, clauses A1..A14. IT READS ONLY THE
        STAGE-A FILE AND THE LITERAL CONSTANTS OF THESE GOVERNING BYTES. It
        reads no manifest, no member, no record and no Stage-B artifact, so
        every prerequisite it needs is a constant or a byte it has itself
        validated. It is evaluable from OR-3 onward and is evaluated at CK-2.
      TS-2B, THE M4-DEPENDENT STAGE, clauses A15..A17. EVERY CLAUSE OF THIS
        STAGE READS THE M4 MANIFEST. IT MAY THEREFORE RUN ONLY AFTER M4 HAS BEEN
        PROVED TO EXIST, TO PARSE AS JSON, TO BE AN OBJECT, TO CARRY EXACTLY
        MS-4's KEY SET WITH EXACTLY MS-4's TYPES, AND TO SATISFY EVERY
        STRUCTURAL PREDICATE OF VP-1. It is evaluable from OR-7 onward and is
        evaluated at CK-9, which VP-4 places after CK-7 and CK-8.
      WHY THE SPLIT EXISTS, STATED PLAINLY. Version 1.4 ran A1..A17 as one stage
      at CK-2, BEFORE any check had established that M4 exists or parses. A15,
      A16(a) and A17 read manifest fields, so on a state with a valid Stage A
      and an absent, unparseable, non-object or missing-key M4 those clauses had
      no defined value to read: one implementation could map the failed read to
      STAGE_A_PRESELECTION_MISMATCH, another could defer to the member checks
      and return MEMBER_OMITTED, and a third had no specified mapping at all.
      ORDERING PREDICATES IS NOT THE SAME AS CREATING THE OBJECT THEY NEED. The
      split creates it. NO CLAUSE OF TS-2B MAY READ AN ABSENT, INVALID-JSON,
      NON-OBJECT, MISSING-KEY OR WRONGLY TYPED M4, because every one of those
      states is fatal at CK-7 or CK-8 with its own single code before TS-2B is
      reached.
      --- TS-2A, SELF-CONTAINED: READS ONLY THE STAGE-A FILE ---
        A1   a file exists at TS-1's exact literal path. No other path is
             consulted, and a well-formed selection artifact anywhere else is
             not Stage A.                            else STAGE_A_ABSENT
        A2   the file bytes parse as JSON and are byte-identical to CANON of
             the parsed value, trailing 0x0A included.
                                                     else STAGE_A_MALFORMED
        A3   the top-level value is an OBJECT whose key set is EXACTLY TS-1's
             eleven keys — no extra key, no missing key.
                                                     else STAGE_A_MALFORMED
        A4   schema is a STRING equal to
             "philosophia.officina.t-p1-watchdog-freeze-selection.v1".
                                                     else STAGE_A_MALFORMED
        A5   version is the INTEGER 1 — not the string "1", not 1.0.
                                                     else STAGE_A_MALFORMED
        A6   author is a STRING equal to "Kirill Kruglov".
                                                     else STAGE_A_MALFORMED
        A7   signature_algorithm is a STRING equal to "Ed25519".
                                                     else STAGE_A_MALFORMED
        A8   selected_option_token is a STRING equal to one of TS-1's two
             literal option tokens and to no other value.
                                                     else STAGE_A_OPTION_INVALID
        A9   selected_option_amendment_token is a STRING equal to the token
             TS-1 pairs with the value found at A8, and to no other value.
                                                     else STAGE_A_OPTION_INVALID
        A10  public_key_hex is a STRING of exactly 64 characters, each one of
             0123456789abcdef, decoding to exactly 32 bytes.
                                                     else STAGE_A_KEY_MALFORMED
        A11  key_id is a STRING of exactly 64 characters, each one of
             0123456789abcdef, and equals the SHA-256 of the 32 raw bytes
             decoded at A10.                         else STAGE_A_KEY_MALFORMED
        A12  governing_pre_selection is an OBJECT whose key set is EXACTLY
             {packet, amendment, composite}; each value is an OBJECT whose key
             set is EXACTLY {path, sha256}; each sha256 is a STRING of exactly
             64 characters, each one of 0123456789abcdef.
                                                     else STAGE_A_MALFORMED
        A13  the three path values equal, respectively, TS-1's three literal
             pre-selection path strings, byte for byte.
                                                     else STAGE_A_MALFORMED
        A14  threat_model is a STRING equal, byte for byte, to the exact
             string quoted at TR-2, and created_utc satisfies the grammar AND
             the semantic validator of MS-10. THE created_utc VALUE IS NOT
             COMPARED WITH ANY OTHER TIMESTAMP AND ORDERS NOTHING.
                                                     else STAGE_A_MALFORMED
      --- TS-2B, M4-DEPENDENT: EVERY CLAUSE BELOW READS THE MANIFEST, AND
          RUNS ONLY AFTER CK-7 AND CK-8 HAVE PROVED M4 PRESENT, PARSEABLE, AN
          OBJECT, EXACTLY KEYED, EXACTLY TYPED AND STRUCTURALLY VALID ---
        A15  the three path values of governing_pre_selection equal,
             respectively, the manifest's pre_selection_packet_path,
             pre_selection_amendment_path and pre_selection_composite_path.
                                            else STAGE_A_PRESELECTION_MISMATCH
        A16  THE THREE PRE-SELECTION DIGESTS ARE ANCHORED, NOT MERELY MUTUALLY
             EQUAL. Four sub-clauses, evaluated in this order, each fail-closed,
             each raising STAGE_A_PRESELECTION_MISMATCH:
             A16(a) the three sha256 values of governing_pre_selection equal,
                    respectively, the manifest's pre_selection_packet_sha256,
                    pre_selection_amendment_sha256 and
                    pre_selection_composite_sha256. THIS CONJUNCT ALONE IS NOT
                    SUFFICIENT AND NEVER WAS: it compares two author-written
                    copies of one value with each other and anchors neither.
             A16(b) the packet value equals the SHA-256 of the whole bytes
                    found at TS-1's literal packet path, recomputed at
                    validation time. If no file exists at that path the clause
                    FAILS; there is no absent-file exemption.
             A16(c) the amendment value equals the SHA-256 of the whole bytes
                    found at TS-1's literal amendment path, recomputed at
                    validation time, and therefore also equals the M1 amendment
                    digest and the manifest's peer_amendment_sha256.
             A16(d) the composite value equals the PRE-SELECTION COMPOSITE
                    ANCHOR of the M1 amendment, extracted by this exact rule
                    and no other: split the M1 amendment's bytes on 0x0A; a
                    line is an ANCHOR LINE if and only if the whole line, after
                    stripping a trailing 0x0A and with no other leading or
                    trailing byte, consists of the literal token
                    P1_WATCHDOG_V2_10_PRE_SELECTION_COMPOSITE_SHA256 followed by
                    exactly one 0x20, one 0x3D, one 0x20, and then exactly 64
                    characters each one of 0123456789abcdef. THAT TOKEN IS THE
                    ONLY ONE THIS GENERATION USES, AND IT IS THE SAME LITERAL
                    STRING §A0.4 DESCRIBES AND THE §A0.4 ANCHOR LINE CARRIES.
                    VERSION 1.6 RE-SCOPED §A0.4 TO A V2_9 TOKEN AND LEFT THIS
                    CONSUMING CLAUSE BOUND TO THE RETIRED V2_8 TOKEN, SO A
                    CONFORMING IMPLEMENTATION FOUND ZERO ANCHOR LINES ON EVERY
                    LEGITIMATE AMENDMENT AND REFUSED EVERY LEGITIMATE STAGE A
                    WITH STAGE_A_PRESELECTION_MISMATCH. The independent X line
                    demonstrated it; the token is unified here and appears in
                    exactly one generation-scoped form throughout this pair.
                    THE COUNT OF ANCHOR LINES MUST BE EXACTLY ONE — zero and two or more
                    both FAIL, exactly as the sentinel-cardinality rule of the
                    composite's extraction algorithm fails — and the 64
                    characters of that one line are the anchor value. A prose
                    mention of the token that is not followed by that exact
                    separator and exactly 64 hexadecimal characters is not an
                    anchor line and is not counted.
                    WHY THIS ONE IS ANCHORED DIFFERENTLY, STATED PLAINLY: OR-4
                    deletes one branch of every variant block, so the reviewed
                    pre-selection composite bytes exist NOWHERE on disk after
                    OR-4 and cannot be recomputed by anyone; and the composite
                    cannot carry the value as a literal, because a file cannot
                    contain its own digest without a fixed point and §P1-14.5
                    forbids it. The amendment can and does, because OR-4 does
                    not change the amendment, and the amendment's own bytes are
                    pinned by peer_amendment_sha256, by its M1 membership in
                    the install record, and through install_record_id by Stage
                    B's signature. THIS IS AN ANCHOR, NOT A PROOF OF
                    FRESHNESS, AND TR-2(b) IS UNCHANGED BY IT: when an entire
                    coherent generation is restored, the amendment, its anchor
                    line, the packet, the manifest, Stage A, Stage B, the
                    signature and the record are all restored together and
                    every clause here passes on the restored bytes.
        A17  the SHA-256 of the whole Stage-A file equals the manifest's
             stage_a_sha256; TS-1's path equals the manifest's stage_a_path;
             and key_id equals the manifest's stage_a_key_id.
                                            else STAGE_A_BINDING_MISMATCH
      NO CLAUSE OF TS-2B READS AN ABSENT, INVALID-JSON, NON-OBJECT,
      MISSING-KEY OR WRONGLY TYPED MANIFEST. Each of those five states is
      already fatal, with its own single code, at CK-7 (MEMBER_OMITTED for an
      absent M4) or at CK-8 (MEMBER_SUBSTITUTED for an M4 that does not parse,
      is not an object, has the wrong key set or has a wrongly typed value).
      A17 IS WHAT MAKES A SUBSTITUTED STAGE-A FILE FAIL WITHOUT A MATCHING
      SUBSTITUTION OF M4, and M4 is a member whose digest enters
      install_record_id, which Stage B signs. TR-1 and TR-2 state exactly how
      far that reaches.

TS-3  STAGE B — INSTALL-ID AUTHORIZATION. TWO literal paths:
        successor/officina/authorization/P1_WATCHDOG_AUTHORITY_INSTALL_AUTHORIZATION_V1.json
        successor/officina/authorization/P1_WATCHDOG_AUTHORITY_INSTALL_AUTHORIZATION_V1.sig
      ENCODING: the .json file bytes are exactly CANON of the object (MS-0).
      The top-level value is a JSON object whose key set is EXACTLY the
      thirteen keys below, with exactly these types and value grammars:

        schema                     STRING, exactly
                                   "philosophia.officina.t-p1-watchdog-authority-install-authorization.v1"
        version                    INTEGER, exactly 1
        stage_a_path               STRING, exactly TS-1's literal path
        stage_a_sha256             64-char lowercase hex STRING, the SHA-256 of
                                   the whole Stage-A file
        key_id                     64-char lowercase hex STRING, equal to
                                   Stage A's key_id
        selected_option_token      STRING, equal to Stage A's
                                   selected_option_token
        install_record_id          64-char lowercase hex STRING, the id
                                   computed at OR-9
        install_record_path        STRING, exactly IR-2's path for that id:
                                   the literal prefix
                                   successor/officina/runtime_control/INSTALL/
                                   followed by install_record_id followed by
                                   the five bytes ".json"
        member_count               INTEGER, exactly 69
        governing_amendment_sha256 64-char lowercase hex STRING, the digest of
                                   the M1 amendment bytes
        governing_composite_sha256 64-char lowercase hex STRING, the digest of
                                   the M1 composite bytes AFTER variant
                                   resolution
        signature_algorithm        STRING, exactly "Ed25519"
        created_utc                STRING satisfying MS-10
      THE STAGE-B ARTIFACT CARRIES NO SIGNATURE INSIDE ITSELF. The signature is
      detached, at the .sig path, and is TS-4.

TS-4  CANONICAL SIGNED MESSAGE, ALGORITHM AND DETACHED SIGNATURE ENCODING.
      THE SIGNED MESSAGE IS EXACTLY THE BYTE SEQUENCE OF THE STAGE-B .json
      FILE, which MS-0 requires to equal CANON of its object, the trailing 0x0A
      included. There is no prefix, no suffix, no domain separator added at
      signing time, no re-serialization, and no hash applied before signing:
      Ed25519 of RFC 8032 in its pure form is applied to those bytes directly.
      The pre-hashed variant is not permitted and does not validate.
      THE DETACHED SIGNATURE FILE at the .sig path contains EXACTLY 128
      characters, each one of 0123456789abcdef — the 64-byte Ed25519 signature
      — with NO trailing newline and no other byte. Any other length, any
      uppercase character, any other encoding and any trailing byte is a
      malformed signature and fails closed. THE SIGNATURE FILE CONTAINS NO KEY,
      NO IDENTIFIER AND NO ALGORITHM NAME: the algorithm is fixed by TS-3 and
      the key by TS-1.

TS-5  STAGE B VERIFICATION — AN EXHAUSTIVE FIELD-BY-FIELD ALGORITHM. EVERY
      MANDATORY LITERAL AND EVERY DERIVED RELATION IS CHECKED. NO FIELD IS
      SATISFIED BY MERE PRESENCE. Executed in this order, fail-closed at the
      first failure. Clauses B1..B13 run at CK-3 and are SELF-CONTAINED: they
      read only the two Stage-B paths and the Stage-A file, which CK-2 has
      already validated, and no manifest, member or record. Clauses B14..B18 run
      at CK-14, because they depend on the recomputed id, the member digests and
      the matched record.
        B1   both TS-3 paths exist.                  else STAGE_B_ABSENT
             If the .json exists and the .sig does not,
                                                     STAGE_B_SIGNATURE_ABSENT
        B2   the .json bytes parse as JSON and are byte-identical to CANON of
             the parsed value, trailing 0x0A included.
                                                     else STAGE_B_MALFORMED
        B3   the top-level value is an OBJECT whose key set is EXACTLY TS-3's
             thirteen keys — no extra key, no missing key.
                                                     else STAGE_B_MALFORMED
        B4   schema is a STRING equal to
             "philosophia.officina.t-p1-watchdog-authority-install-authorization.v1".
                                                     else STAGE_B_MALFORMED
        B5   version is the INTEGER 1.               else STAGE_B_MALFORMED
        B6   created_utc satisfies the grammar AND the semantic validator of
             MS-10. ITS VALUE IS NOT COMPARED WITH ANY OTHER TIMESTAMP AND
             ORDERS NOTHING.                         else STAGE_B_MALFORMED
        B7   member_count is the INTEGER 69.         else STAGE_B_MALFORMED
        B8   install_record_id, stage_a_sha256, key_id,
             governing_amendment_sha256 and governing_composite_sha256 are
             each a STRING of exactly 64 characters, each one of
             0123456789abcdef.                       else STAGE_B_MALFORMED
        B9   install_record_path is a STRING equal to the concatenation of the
             literal prefix
             successor/officina/runtime_control/INSTALL/ , the value of
             install_record_id, and ".json".         else STAGE_B_MALFORMED
        B10  signature_algorithm is a STRING equal to "Ed25519".
                                                     else STAGE_B_ALGORITHM_INVALID
        B11  the .sig bytes are exactly 128 characters, each one of
             0123456789abcdef, and nothing else.
                                                     else STAGE_B_MALFORMED
        B12  Ed25519 verification of that 64-byte signature over the exact
             .json bytes SUCCEEDS AGAINST THE 32-BYTE PUBLIC KEY OF STAGE A
             AND AGAINST NO OTHER KEY. There is no key list, no key discovery,
             no fallback key, no unsigned acceptance, no algorithm negotiation
             and no downgrade.                       else STAGE_B_SIGNATURE_INVALID
        B13  stage_a_path is a STRING equal to TS-1's literal path;
             stage_a_sha256 equals the SHA-256 of the Stage-A file found at
             that path; and key_id equals Stage A's key_id.
                                                     else STAGE_B_STAGE_A_MISMATCH
        B14  selected_option_token equals Stage A's selected_option_token.
                                                     else STAGE_B_OPTION_MISMATCH
        B15  install_record_id equals the id recomputed at CK-11 from the
             members found on disk.                  else STAGE_B_INSTALL_ID_MISMATCH
        B16  install_record_path names the one record file established at CK-5
             and matched at CK-12.                   else STAGE_B_INSTALL_ID_MISMATCH
        B17  member_count equals the enumerated member count, 69.
                                                     else STAGE_B_INSTALL_ID_MISMATCH
        B18  governing_amendment_sha256 and governing_composite_sha256 equal
             the digests of the two M1 members found on disk at CK-7, and
             governing_amendment_sha256 additionally equals the manifest's
             peer_amendment_sha256, which CK-10 has already anchored to the same
             bytes.                                  else STAGE_B_GOVERNING_MISMATCH

TS-6  STAGE A, STAGE B, THE DETACHED SIGNATURE AND THE PUBLIC KEY ARE OUTSIDE
      M1..M7, AND NEITHER STAGE IS SELF-ATTESTED.
      The three artifact paths all begin with the thirty-five bytes
      "successor/officina/authorization/P1", which is a prefix of no member
      path and equals no literal member path, so by the same argument as MS-9
      none of them is a member of any class. The public key exists only inside
      Stage A and has no path of its own.
      Stage A is attested by the manifest binding of TS-2 A17 and by the
      author's act of creating it; it does not attest itself. Stage B is
      attested by the Stage-A key, which Stage B does not contain; it does not
      attest itself.
      NEITHER STAGE IS A SPECIFICATION SURFACE. Both carry values and no rules,
      exactly as the install record does.
      THE PRIVATE KEY IS NEVER STORED IN THIS REPOSITORY, IS NEVER A MEMBER,
      AND IS NAMED BY NO PATH IN ANY GOVERNING BYTE.
      THE PRE-SELECTION PACKET IS LIKEWISE OUTSIDE M1..M7. TS-2 A16(b) reads
      the bytes at TS-1's literal packet path in order to hash them. That makes
      the packet a HASH-READ TARGET of one clause and nothing else: it adds no
      member, adds no class, changes no cardinality, supplies no path to CK-4,
      and is not opening a document for behaviour (IR-12, N-14). Its integrity
      requirement is discharged by the clause itself — a changed packet fails
      A16(b) with STAGE_A_PRESELECTION_MISMATCH.
      NO PERMANENT FALLBACK AND NO UNSIGNED PROCEDURAL SHORTCUT EXISTS. There
      is no mode, flag, environment variable, build profile, migration path,
      recovery path, grace period or test hook in which the gate admits a state
      with Stage A absent, Stage B absent, the signature absent, the signature
      unverified, or the signature verified against any key other than Stage
      A's.

OR-1   THE ORDER BELOW IS THE SOLE CONFORMING CONSTRUCTION PROCEDURE AND IS A
       MANDATORY OPERATOR OBLIGATION. A step may not begin before every earlier
       step is complete and verified. NO STEP IS OPTIONAL, REORDERABLE OR
       SKIPPABLE, AND NO STEP HAS AN ALTERNATE PATH. There is exactly one
       conforming sequence and it is OR-2 through OR-11.
       IT IS AN OBLIGATION ON THE OPERATOR AND THE PROCEDURAL DRIVER, NOT A
       PROPERTY THE FINAL-STATE GATE VERIFIES. G-11 checks the exact final
       state and nothing else. FS-1 states what that proves, FS-2 states what
       it cannot prove, FS-3 keeps this obligation binding regardless, FS-4
       states what happens when a violation is observed while it occurs, and
       FS-5 places an unobserved violation inside the declared residual of
       TR-2. NO CLAUSE ANYWHERE MAY ASSERT THAT G-11 RECONSTRUCTS THE ORDER IN
       WHICH IDENTICAL FINAL BYTES CAME TO EXIST.

OR-2   KIRILL EMITS EXACTLY ONE OF THE TWO EXISTING OPTION TOKENS. This precedes
       everything else. It is authorized by nothing in these bytes and is
       predicted by nothing in them.

OR-3   STAGE A IS CREATED — including generation of the Ed25519 key pair — and
       is verified per TS-2A, clauses A1 through A14, which read only the
       Stage-A file. TS-2B's clauses A15 through A17 are not yet evaluable
       because M4 does not exist; they are evaluated at OR-7 and, at every
       production entry point thereafter, at CK-9.

OR-4   EVERY VARIANT BLOCK IN THE COMPOSITE IS RESOLVED to the signed branch and
       the other branch is DELETED; the v1.3 amendment is installed. After this
       step G-10 finds zero markers. M1 is now final and its two digests are
       fixed.

OR-5   THE M5 VERIFIER AND THE TWO M6 MODULES ARE INSTALLED at their literal
       paths of MS-5 and MS-6.

OR-6   THE M4 MANIFEST IS WRITTEN at MS-4's literal path, with all twenty-one
       keys,
       the canonical eighty-nine-row reachable_closure VALUE of MS-11.1, the
       closed project-import dependency surface of MS-13, the semantic source
       of
       every field per MS-12 — including peer_amendment_sha256 recomputed from
       the M1 amendment bytes — the three pre-selection path and digest pairs
       anchored as TS-2 A16 requires, and the three Stage-A binding fields.

OR-7   THE FULL TEST MATRIX RUNS against the M5 verifier and the M6 bundle and
       EVERY row passes. The placeholder audit and the guard fires are run; the
       required placeholder count and guard-fire count are ZERO. TS-2B is now
       evaluable and TS-2A and TS-2B are together evaluated in full, A1 through
       A17.

OR-8   THE M7 ATTESTATION IS WRITTEN at MS-7's literal path, binding the M5
       digest and the two M6 digests found on disk and the bundle digest
       recomputed from them.

OR-9   THE CANONICAL 69-MEMBER LIST IS BUILT FROM MS-1..MS-7 ALONE and
       install_record_id is computed per IR-1.

OR-10  THE STAGE-B ARTIFACT AND ITS DETACHED SIGNATURE ARE CREATED and are
       verified per TS-5, all eighteen clauses, BEFORE anything is written under
       the INSTALL directory other than the M7 attestation of OR-8.

OR-11  THE INSTALL RECORD IS INSTALLED no-replace at its content-addressed path,
       LAST; then every M2 and M3 member is verified byte-identical to the
       digest recorded at MS-2 and MS-3.
       VERSION 1.2 ADDED HERE THAT "a record installed before OR-10 completes is
       an ordering violation and is refused at CK-3 or CK-9". THAT SENTENCE IS
       WITHDRAWN AS FALSE OF THE FINAL STATE. It holds only while Stage B is
       still absent, which is a contemporaneous fact covered by FS-4; once the
       exact valid final bytes exist, FS-2 applies and no final-state check
       distinguishes the two histories. Writing the record early remains a
       violation of OR-1; it is simply not one this gate can detect after the
       fact. THE WITHDRAWAL IS UNCHANGED IN VERSION 1.4 AND IS NOT NARROWED BY
       ANY REPAIR IN IT.

VP-1  THE STRUCTURAL VALIDATION PHASE, AND ITS EXACT RANGE. A STRUCTURAL
      PREDICATE IS ONE THAT CAN BE DECIDED FROM THE OBJECT'S OWN BYTES ALONE,
      WITHOUT READING ANY OTHER OBJECT AND WITHOUT RECOMPUTING ANY DIGEST.
      Exactly these, in exactly this order, for the install record, M4 and M7:
        S1  the file exists at its literal path;
        S2  its bytes parse as JSON;
        S3  the top-level value is an OBJECT;
        S4  its key set is EXACTLY the key set that IR-3, MS-4 or MS-7 states —
            no extra key, no missing key;
        S5  the JSON type of every value is the type stated for its key;
        S6  the bytes are byte-identical to CANON of the parsed value, the
            trailing 0x0A included (MS-0);
        S7  the mandatory schema literal equals the exact string stated for that
            object, and version is the INTEGER 1 — not "1", not 1.0. THESE TWO
            ARE THE ONLY MANDATORY LITERALS THE STRUCTURAL PHASE OWNS. Every
            other literal in those sections names a value belonging to some
            other object or to §P1-3.1, and is therefore semantic;
        S8  every array satisfies its stated CARDINALITY, its stated element
            SHAPE, its stated ORDER or sortedness, and its stated pairwise
            distinctness; every lexical grammar holds — a digest string is
            exactly 64 characters each one of 0123456789abcdef, a created_utc
            value satisfies BOTH the grammar and the semantic validator of
            MS-10, and every enumerated literal is one of its stated literals;
            and every string required to be a literal CONCATENATION of constants
            and another field of the SAME object satisfies that concatenation;
            AND EVERY NESTED OBJECT WHOSE KEY SET THIS PAIR STATES EXACTLY HAS
            EXACTLY THAT KEY SET, with no extra key, no missing key and no
            renamed key, and every value inside it has the JSON type stated for
            it. S4's exact-key-set rule applies at every stated depth and not
            only at the top level: root_source_sha256, reachable_closure's
            elements, project_import_dependencies, each of its four module
            elements and each module element's import_time_effects object are
            all exactly keyed, and a violation at any depth is one structural
            failure with one code.
      S1 THROUGH S5 ARE THE PREREQUISITE SUB-PHASE. They are stated separately
      and ordered first because every later predicate over that object — S6, S7,
      S8, and every semantic clause of VP-2 — presupposes that the object exists,
      parses, is an object, and has a value of the right type under the key it
      is about to read. VERSION 1.4 DID NOT SEPARATE THEM, WHICH IS WHY TS-2's
      M4-DEPENDENT CLAUSES COULD BE ORDERED BEFORE THE OBJECT THEY READ EXISTED.
      NOTHING ELSE IS STRUCTURAL. In particular the structural phase does NOT
      decide whether a digest equals anything, whether an id equals a filename or
      a recomputation, whether a path equals another section's literal path,
      whether reachable_closure equals MS-11.1, or whether rows_attested,
      row_count or all_rows_passed agree with the bundle installed. Every one of
      those is semantic and is owned in VP-2.
      MEMBER EXISTENCE AND MEMBER DIGESTS ARE NOT PART OF THIS PHASE. They are
      CK-7, which runs between the record's structural validation and the
      members' structural validation, and which owns MEMBER_OMITTED and
      HISTORICAL_BYTE_MOVED.
      STAGE A AND STAGE B ARE NOT VALIDATED HERE AND ARE NOT MEMBERS. Their
      clauses are single-owner chains — TS-2A A1..A14, TS-2B A15..A17 and TS-5
      B1..B18 — with their own codes, run at CK-2, CK-9, CK-3 and CK-14, and no
      clause of theirs is restated in this phase.

VP-2  THE SEMANTIC AND CROSS-OBJECT VALIDATION PHASE. A SEMANTIC PREDICATE IS
      ONE THAT REQUIRES READING ANOTHER OBJECT, READING A LITERAL OF THESE
      GOVERNING BYTES, OR RECOMPUTING A DIGEST. Its owners and codes are exactly:
        CK-9   TS-2B A15, A16(a)..(d), A17 — Stage A against M4
                                                  STAGE_A_PRESELECTION_MISMATCH,
                                                  STAGE_A_BINDING_MISMATCH
        CK-10  the NINE M4 relations enumerated at CK-10, and no other
                                                  MANIFEST_VALUE_MISMATCH
        CK-12  the record's id equals its filename and equals the IR-1
               recomputation of CK-11             INSTALL_RECORD_NAME_MISMATCH
        CK-13  the record's members array equals the enumerated set, under the
               total two-clause partition D1/D2   MEMBER_SUBSTITUTED (D1),
                                                  MEMBER_STALE (D2)
        CK-14  TS-5 B14..B18                      the STAGE_B_ codes named
        CK-15  every M7 relation                  ATTESTATION_MISMATCH
      NO SEMANTIC PREDICATE IS EVALUATED IN THE STRUCTURAL PHASE, AND NO
      STRUCTURAL PREDICATE IS RE-EVALUATED IN THE SEMANTIC PHASE. NO RELATION
      APPEARS UNDER TWO OWNERS. Version 1.4 broke that twice — CK-7 claimed
      "every MS-12 relation" while VP-3 gave nine of them to CK-2, and CK-13
      re-asserted an M2/M3 byte identity already fatal at CK-6 — and both
      duplications are removed here: MS-12's nine Stage-A-owned rows are excised
      from CK-10's range by name, and the M2/M3 recorded-digest relation is owned
      once, at CK-7, where it raises HISTORICAL_BYTE_MOVED.
      VERSION 1.5 LEFT TWO FURTHER OVERLAPS AND BOTH ARE CLOSED HERE. CK-10's
      stated range included schema, version and created_utc, which CK-8 settles
      structurally; CK-10's range is now the nine relations it actually owns.
      And CK-13 offered three reason codes with no order among them, so a record
      carrying both an unenumerated path and a wrong digest had two defensible
      answers; CK-13 is now a TOTAL TWO-CLAUSE PARTITION with a literal
      sub-order, and the redundant code MEMBER_EXTRA is RETIRED.

VP-3  THE ORDERED RELATION-TO-OWNER-TO-CODE TABLE. Every field of every
      generated object, and every cross-object relation, appears exactly once.
      The OWNER column names the ONE EARLIEST clause that can refuse it; the
      CODE column names the ONE code it raises.

      INSTALL RECORD — five keys, validated at CK-6, BEFORE any member is read
        existence and uniqueness of the file  CK-5 / INSTALL_RECORD_ABSENT,
                                              INSTALL_RECORD_REPLAYED
        parse, object, key set, types         CK-6 S2,S3,S4,S5 / MEMBER_SUBSTITUTED
        schema, version                       CK-6 S7 / MEMBER_SUBSTITUTED
        CANON identity                        CK-6 S6 / MEMBER_SUBSTITUTED
        members array shape/order/64-hex      CK-6 S8 / MEMBER_SUBSTITUTED
        created_utc grammar                   CK-6 S8 / MEMBER_SUBSTITUTED
        install_record_id 64-hex              CK-6 S8 / MEMBER_SUBSTITUTED
        install_record_id = IR-1 digest       CK-12 / INSTALL_RECORD_NAME_MISMATCH
        install_record_id = filename stem     CK-12 / INSTALL_RECORD_NAME_MISMATCH
        members (class,path) sequence         CK-13 D1 / MEMBER_SUBSTITUTED
        members recorded digests              CK-13 D2 / MEMBER_STALE

      PROJECT-IMPORT DEPENDENCIES — MS-13, four modules, not members
        shape of project_import_dependencies,
          including the six-key module element
          and the eight-key boolean
          import_time_effects object          CK-8 S4,S5,S8 / MEMBER_SUBSTITUTED
        each module's recomputed SHA-256      CK-10 / MANIFEST_VALUE_MISMATCH
        each module's path, project_imports
          and stdlib_seeds                    CK-10 / MANIFEST_VALUE_MISMATCH
        each module's eight import_time_effects
          booleans, all required false        CK-10 / MANIFEST_VALUE_MISMATCH
        the execution_order array             CK-10 / MANIFEST_VALUE_MISMATCH

      MEMBERS — existence and bytes
        a member absent from its literal path CK-7 / MEMBER_OMITTED
        an M2 or M3 member whose recomputed
          digest differs from the value
          recorded literally at MS-2 or MS-3  CK-7 / HISTORICAL_BYTE_MOVED
        every other member digest             recomputed at CK-7, compared at
                                              CK-11 through CK-13

      M4 PRODUCTION MANIFEST — twenty-one keys
        FIELD                          STRUCTURAL   SEMANTIC OWNER / CODE
        schema                         CK-8 S4,S7   — (NOT re-evaluated at CK-10)
        version                        CK-8 S4,S7   — (NOT re-evaluated at CK-10)
        roots                          CK-8 S5,S8   CK-10 / MANIFEST_VALUE_MISMATCH
        root_source_sha256             CK-8 S5,S8   CK-10 / MANIFEST_VALUE_MISMATCH
        reachable_closure              CK-8 S5,S8   CK-10 / MANIFEST_VALUE_MISMATCH
        p1_composite_sha256            CK-8 S8      CK-10 / MANIFEST_VALUE_MISMATCH
        p1_composite_body_sha256       CK-8 S8      CK-10 / MANIFEST_VALUE_MISMATCH
        p1_composite_guarddata_sha256  CK-8 S8      CK-10 / MANIFEST_VALUE_MISMATCH
        p1_composite_normative_sha256  CK-8 S8      CK-10 / MANIFEST_VALUE_MISMATCH
        peer_amendment_sha256          CK-8 S8      CK-10 / MANIFEST_VALUE_MISMATCH
        pre_selection_packet_path      CK-8 S5      CK-9 A15 / STAGE_A_PRESELECTION_MISMATCH
        pre_selection_packet_sha256    CK-8 S8      CK-9 A16 / STAGE_A_PRESELECTION_MISMATCH
        pre_selection_amendment_path   CK-8 S5      CK-9 A15 / STAGE_A_PRESELECTION_MISMATCH
        pre_selection_amendment_sha256 CK-8 S8      CK-9 A16 / STAGE_A_PRESELECTION_MISMATCH
        pre_selection_composite_path   CK-8 S5      CK-9 A15 / STAGE_A_PRESELECTION_MISMATCH
        pre_selection_composite_sha256 CK-8 S8      CK-9 A16 / STAGE_A_PRESELECTION_MISMATCH
        stage_a_path                   CK-8 S5      CK-9 A17 / STAGE_A_BINDING_MISMATCH
        stage_a_sha256                 CK-8 S8      CK-9 A17 / STAGE_A_BINDING_MISMATCH
        stage_a_key_id                 CK-8 S8      CK-9 A17 / STAGE_A_BINDING_MISMATCH
        project_import_dependencies    CK-8 S5,S8   CK-10 / MANIFEST_VALUE_MISMATCH
        created_utc                    CK-8 S8      — (compared with nothing)
      THE NINE STAGE-A-OWNED ROWS ARE OWNED AT CK-9 AND ARE NOT RE-RAISED AT
      CK-10, AND schema, version AND created_utc ARE OWNED ONLY AT CK-8. CK-9 PRECEDES CK-10, AND BOTH PRECEDE NOTHING THAT READS M4 EARLIER,
      BECAUSE CK-7 AND CK-8 HAVE ALREADY MADE M4 PRESENT AND STRUCTURALLY VALID.
      That is the whole of the version-1.4 prerequisite defect and its repair.

      M7 PASSING ATTESTATION — ten keys
        schema                         CK-8 S4,S7   —
        version                        CK-8 S4,S7   —
        verifier_path                  CK-8 S5      CK-15 / ATTESTATION_MISMATCH
        verifier_sha256                CK-8 S8      CK-15 / ATTESTATION_MISMATCH
        test_bundle_modules            CK-8 S5,S8   CK-15 / ATTESTATION_MISMATCH
        test_bundle_digest             CK-8 S8      CK-15 / ATTESTATION_MISMATCH
        rows_attested                  CK-8 S5,S8   CK-15 / ATTESTATION_MISMATCH
        row_count                      CK-8 S5      CK-15 / ATTESTATION_MISMATCH
        all_rows_passed                CK-8 S5      CK-15 / ATTESTATION_MISMATCH
        created_utc                    CK-8 S8      —

      STAGE A — eleven keys
        TS-2A: schema A4 · version A5 · author A6 · signature_algorithm A7 ·
          selected_option_token A8 · selected_option_amendment_token A9 ·
          public_key_hex A10 · key_id A11 · governing_pre_selection shape A12
          and literal paths A13 · threat_model A14 · created_utc A14.
        TS-2B: governing_pre_selection against the manifest A15, A16(a)..(d);
          the Stage-A binding fields A17.
        Codes exactly as those clauses name them.

      STAGE B — thirteen keys
        TS-5 B1..B13 at CK-3; B14..B18 at CK-14. schema B4 · version B5 ·
        created_utc B6 · member_count B7 then B17 · stage_a_path B13 ·
        stage_a_sha256 B8 then B13 · key_id B8 then B13 ·
        selected_option_token B14 · install_record_id B8 then B15 ·
        install_record_path B9 then B16 · governing_amendment_sha256 B8 then
        B18 · governing_composite_sha256 B8 then B18 · signature_algorithm B10.
        The detached signature is B1, B11 and B12. Where a field appears twice
        the EARLIER clause owns a malformed value and the LATER clause owns a
        well-formed but disagreeing value; the two cases are disjoint.

VP-4  THE LITERAL TOPOLOGICAL PREDICATE ORDER. Every predicate's prerequisites
      are established by an EARLIER check, not merely ordered before it.
        1.  CK-1   no predicate
        2.  CK-2   Stage A alone            (TS-2A A1..A14, in order)
        3.  CK-3   Stage B alone            (TS-5 B1..B13, in order)
        4.  CK-4   the member enumeration, a constant of these bytes
        5.  CK-5   exactly one install record EXISTS
        6.  CK-6   that record is STRUCTURALLY VALID   (S1..S8, in order)
        7.  CK-7   every member EXISTS and its digest is recomputed, members
                   visited in IR-1 order — ascending by class, then by path
        8.  CK-8   M4 then M7 are STRUCTURALLY VALID   (S1..S8, in order)
        9.  CK-9   Stage A against M4        (TS-2B A15, A16(a)..(d), A17)
        10. CK-10  M4 semantics              (the NINE relations enumerated at
                   CK-10, in MS-12's top-to-bottom order)
        11. CK-11  recompute install_record_id
        12. CK-12  id equalities
        13. CK-13  the record's members array against the enumerated set
        14. CK-14  Stage B cross-object      (TS-5 B14..B18, in order)
        15. CK-15  M7 semantics              (MS-7's key order)
      NO IMPLEMENTATION MAY HOIST A LATER CLAUSE EARLIER AS AN OPTIMIZATION OR
      DEFER AN EARLIER ONE, and one that does is nonconforming even if it accepts
      and refuses the same sets.
      THE SIX MULTI-FAULT STATES THAT VERSION 1.4 LEFT UNDEFINED, EACH NOW WITH
      EXACTLY ONE FIRST CODE:
        valid Stage A + absent M4
          CK-7  MEMBER_OMITTED          (CK-2 no longer touches M4 at all)
        valid Stage A + M4 that is not valid JSON
          CK-8  MEMBER_SUBSTITUTED      (S2; CK-9 is not reached)
        malformed sole install record + absent member
          CK-6  MEMBER_SUBSTITUTED      (the record is validated before members)
        malformed sole install record + stale member
          CK-6  MEMBER_SUBSTITUTED      (same reason)
        M4 semantic mismatch + Stage-A binding mismatch
          CK-9  STAGE_A_BINDING_MISMATCH (CK-9 precedes CK-10)
        changed M2/M3 bytes + coordinated record and member mismatch
          CK-7  HISTORICAL_BYTE_MOVED   (CK-7 precedes CK-11..CK-13)
        malformed M4 + a semantic Stage-A mismatch
          CK-8  MEMBER_SUBSTITUTED      (CK-8 precedes CK-9; no STAGE_A_ code is
                                        reachable while M4 is malformed)
        a record naming an unenumerated path in place of an expected one
          CK-13 D1  MEMBER_SUBSTITUTED  (one disagreement at one index, not two
                                        facts; D1 owns every (class,path)
                                        disagreement whatever its shape)
        a record whose (class,path) sequence is exact but one recorded digest
        is wrong
          CK-13 D2  MEMBER_STALE        (D2 runs only when D1 found nothing)
        a record with BOTH a replaced path and a wrong recorded digest
          CK-13 D1  MEMBER_SUBSTITUTED  (D1 strictly precedes D2)
        a record with a 70th entry, with or without a stale digest
          CK-6  MEMBER_SUBSTITUTED      (cardinality is STRUCTURAL and CK-6
                                        precedes every member predicate)
        a project-import dependency whose bytes, path, import edge or effect
        assertion differs from MS-13
          CK-10 MANIFEST_VALUE_MISMATCH
        a module element whose import_time_effects has an added, removed,
        renamed or non-boolean key
          CK-8  MEMBER_SUBSTITUTED      (an exact-key-set or type failure is
                                        STRUCTURAL; CK-10 is not reached)
        THE MULTI-FAULT STATE THAT DECIDES THE CK-9 / CK-10 ORDER, STATED AS AN
        EXECUTABLE FIXTURE because version 1.6's MS-4 sentence claimed CK-7
        owned the closure and made the order arguable:
        an M4 that is STRUCTURALLY PERFECT — CANON bytes, object, exactly the
        twenty-one keys, every type and grammar correct, reachable_closure a
        sorted, distinct, self-closed array of eighty-nine six-key elements —
        whose reachable_closure is FACTUALLY WRONG in exactly one row's kind,
        AND whose stage_a_sha256 disagrees with the digest of the Stage-A file
        on disk
          CK-9  STAGE_A_BINDING_MISMATCH (A17)
                                        CK-7 established only that M4 exists
                                        and recomputed its member-byte digest;
                                        CK-8 accepted the structure because the
                                        closure is well formed; CK-9 precedes
                                        CK-10, so the STAGE_A_ code is the
                                        first code and the wrong closure is
                                        NEVER REACHED. Remove the Stage-A fault
                                        and the same manifest is refused at
                                        CK-10 with MANIFEST_VALUE_MISMATCH.
                                        A FIXTURE EXPECTING MANIFEST_VALUE_MISMATCH
                                        FOR THE TWO-FAULT STATE, OR EXPECTING ANY
                                        CODE AT CK-7 FOR EITHER STATE, FAILS.
      TWO CONFORMING IMPLEMENTATIONS PRESENTED WITH THE SAME BYTES RETURN THE
      SAME FIRST FAILURE AND THE SAME REASON CODE, IN THESE SIX STATES AND IN
      EVERY OTHER, BECAUSE VP-3 GIVES EVERY RELATION EXACTLY ONE OWNER AND THE
      ORDER ABOVE GIVES EVERY OWNER EXACTLY ONE POSITION.

CK-1   WHEN. Before ANY production entry point — before any process is created,
       any handle is allocated, any freeze route is reachable, any evidence is
       accepted and any settlement runs. This check is the FIRST thing a
       production entry point does; nothing precedes it and no work is performed
       in parallel with it.

CK-2   VERIFY STAGE A, SELF-CONTAINED STAGE: TS-2A, clauses A1 through A14, in
       order. THIS CHECK READS NO MANIFEST, NO MEMBER AND NO RECORD. Codes:
       STAGE_A_ABSENT, STAGE_A_MALFORMED, STAGE_A_OPTION_INVALID,
       STAGE_A_KEY_MALFORMED.

CK-3   VERIFY STAGE B, SELF-CONTAINED STAGE: TS-5, clauses B1 through B13, in
       order. Codes: STAGE_B_ABSENT, STAGE_B_SIGNATURE_ABSENT,
       STAGE_B_MALFORMED, STAGE_B_ALGORITHM_INVALID, STAGE_B_SIGNATURE_INVALID,
       STAGE_B_STAGE_A_MISMATCH.

CK-4   ENUMERATE THE 69 MEMBERS FROM MS-1 THROUGH MS-7 ALONE. No wildcard, no
       directory scan, no glob, no adjective, no path taken from the install
       record, no path taken from the manifest, no path taken from the
       provenance region and no path taken from any future-edit table. THE
       ENUMERATION IS A CONSTANT OF THESE GOVERNING BYTES, reads no file, and is
       identical in the two governing files.

CK-5   THE INSTALL RECORD EXISTS AND IS UNIQUE. Require that EXACTLY ONE file
       directly under successor/officina/runtime_control/INSTALL/ has a name
       consisting of 64 lowercase hexadecimal characters followed by ".json".
       Zero fails with INSTALL_RECORD_ABSENT; two or more fail with
       INSTALL_RECORD_REPLAYED, and a retained record from an earlier install
       generation ALONGSIDE the current one is exactly that case. THIS IS NOT A
       MEMBER ENUMERATION: it reads no member and takes no path into the member
       set.
       A RECORD FROM AN EARLIER GENERATION PRESENTED ALONE AGAINST THE CURRENT
       MEMBERS STILL FAILS, later, at CK-12 and B15.
       WHAT THIS DOES NOT CATCH: a COMPLETE COHERENT ROLLBACK, in which the
       members themselves are also restored to the earlier generation. TR-2
       clause (b) states that case exactly and does not claim to refuse it.

CK-6   THE INSTALL RECORD IS STRUCTURALLY VALID. Apply VP-1's S1 through S8 to
       the one record established at CK-5, in that order, and refuse a violation
       with MEMBER_SUBSTITUTED naming the record path.
       THIS CHECK RUNS BEFORE ANY MEMBER IS READ, AND VERSION 1.4 DID NOT SAY SO.
       There, the record and the members were validated inside one check whose
       internal order was stated only for the members, so a state with a
       malformed record AND an absent or stale member had two defensible first
       codes. The record is not one of the 69 members; it is the object the
       member checks are about to be compared against, so it is made
       well formed first. NO SEMANTIC RELATION IS DECIDED HERE: the id
       equalities are CK-12 and the members-set equality is CK-13.

CK-7   EVERY MEMBER EXISTS, AND EVERY MEMBER DIGEST IS RECOMPUTED. Visit the 69
       enumerated members in IR-1's order — ascending by class compared byte for
       byte, then by path compared byte for byte. For each: require a file at
       the literal path, else refuse with MEMBER_OMITTED; recompute the SHA-256
       of its bytes. For M2 and M3 additionally require the recomputed digest to
       equal the digest recorded literally at MS-2 and MS-3, and refuse a
       difference with HISTORICAL_BYTE_MOVED.
       WHAT CK-7 DOES NOT DO, STATED BECAUSE ONE VERSION-1.6 SENTENCE AT MS-4
       SAID OTHERWISE. CK-7 ESTABLISHES MEMBER EXISTENCE AND RECOMPUTES THE
       MEMBER-BYTE DIGEST, AND NOTHING ELSE. It does not parse M4 or M7, does
       not decide that either is JSON, an object or exactly keyed, does not read
       any field of either, and VALUE-COMPARES NO M4 FIELD — not
       reachable_closure, not roots, not root_source_sha256, not any
       p1_composite_* digest, not peer_amendment_sha256, not
       project_import_dependencies and not any pre_selection_* or stage_a_*
       field. Every one of those is owned later: structure at CK-8, the
       Stage-A-facing nine at CK-9, the remaining nine at CK-10. A verifier that
       value-compares any M4 field here is NONCONFORMING, because at this point
       no check has proved that the field exists or carries a value of the
       stated type.
       HISTORICAL_BYTE_MOVED IS OWNED HERE AND NOWHERE ELSE. Version 1.4 raised
       the same relation twice — once as MEMBER_STALE inside its structural
       check and again as HISTORICAL_BYTE_MOVED in a later check that re-asserted
       it — which contradicted VP-2's own no-re-evaluation rule. The relation is
       evaluated once, here, with one code. MEMBER_STALE now has exactly one
       meaning and one owner: a digest recorded IN THE RECORD that differs from
       the digest recomputed here, refused at CK-13.

CK-8   M4 AND M7 ARE STRUCTURALLY VALID. Apply VP-1's S1 through S8 to the M4
       manifest and then to the M7 attestation, in that order, and refuse a
       violation with MEMBER_SUBSTITUTED naming the offending path.
       EVERY MISSING M4 KEY IS SETTLED HERE AND ONLY HERE. S4 requires EXACTLY
       MS-4's twenty-one-key set, so an omitted key — including any stage_a_*
       key, any pre_selection_* key and project_import_dependencies — is an
       exact-key-set failure refused at CK-8 with MEMBER_SUBSTITUTED. NO LATER
       STAGE_A_ CODE IS AVAILABLE FOR A MISSING KEY, and version 1.5's test
       matrix, which additionally offered STAGE_A_BINDING_MISMATCH and
       STAGE_A_PRESELECTION_MISMATCH for exactly that state, is corrected: the
       same byte state had two normative answers and now has one. A Stage-A
       semantic or binding clause may read an M4 key only after CK-8 has proved
       that the key EXISTS and carries a value of the stated type and grammar.
       CK-8 IS THE SOLE OWNER OF EVERY M4 AND M7 JSON, OBJECT, EXACT-KEY-SET,
       TYPE, SHAPE AND GRAMMAR PREDICATE, AT EVERY STATED DEPTH. No earlier
       check evaluates any of them and no later check re-evaluates any of them.
       This includes the nested exactness of root_source_sha256, of every
       reachable_closure element, of project_import_dependencies, of each of its
       four module elements and of each module element's eight-key
       import_time_effects object: an added, removed, renamed or duplicated key
       and a non-boolean effect value are S4 or S5 failures refused HERE with
       MEMBER_SUBSTITUTED, and NO MANIFEST_VALUE_MISMATCH AND NO STAGE_A_ CODE
       IS AVAILABLE FOR ANY OF THEM.
       AFTER THIS CHECK, AND ONLY AFTER IT, THE MANIFEST IS KNOWN TO EXIST, TO
       PARSE, TO BE AN OBJECT, TO CARRY EXACTLY MS-4's KEY SET AND TO CARRY A
       VALUE OF THE STATED TYPE UNDER EVERY KEY, AT EVERY DEPTH. That is the
       prerequisite TS-2B needs and version 1.4 never established.

CK-9   VERIFY STAGE A AGAINST THE MANIFEST: TS-2B, clauses A15, A16(a) through
       A16(d), and A17, in that order. Codes: STAGE_A_PRESELECTION_MISMATCH,
       STAGE_A_BINDING_MISMATCH.

CK-10  THE M4 SEMANTIC CHECK, AND ITS RANGE IS EXACTLY NINE RELATIONS. Evaluate
       these and no others, in this order:
         1. roots equals the five literal paths of §P1-3.1, in that order;
         2. root_source_sha256's key set equals those five paths and each value
            equals that root's recomputed byte digest;
         3. reachable_closure equals MS-11.1's canonical eighty-nine-row value,
            by the direct value comparison of MS-11.4 with its length and digest
            as corroboration;
         4. p1_composite_sha256 equals the recomputed H_FILE;
         5. p1_composite_body_sha256 equals the recomputed H_BODY;
         6. p1_composite_guarddata_sha256 equals the recomputed H_GUARDDATA;
         7. p1_composite_normative_sha256 equals the recomputed H_NORMATIVE;
         8. peer_amendment_sha256 equals the SHA-256 of the M1 amendment bytes;
         9. project_import_dependencies equals MS-13's value in every part — the
            four recomputed module digests, the four paths, the project import
            edges in execution order, the sorted stdlib seeds, the
            execution_order array and the thirty-two booleans carried by the
            four import_time_effects objects, every one of which must be false.
       Any failure refuses with MANIFEST_VALUE_MISMATCH naming the offending
       key. THE NINE STAGE-A-OWNED ROWS ARE NOT EVALUATED HERE, AND NEITHER ARE
       schema, version OR created_utc: those three are settled entirely by CK-8
       and version 1.5 wrongly listed them in this range, which contradicted
       VP-2's no-re-evaluation rule. 9 CK-10 + 9 CK-9 + 3 CK-8-only = 21 keys.
       NINE IS THE COUNT, AND NO SENTENCE OF THIS PAIR SAYS ELEVEN. Version
       1.6's concluding sentence at MS-12 did; it is withdrawn there. CK-10
       OWNS NO STRUCTURAL PREDICATE AT ANY DEPTH: an import_time_effects object
       with the wrong key set or a non-boolean value never reaches this check,
       because CK-8 has already refused it.

CK-11  RECOMPUTE install_record_id per IR-1 from the member paths and digests
       found at CK-7.

CK-12  REQUIRE THE RECOMPUTED ID TO EQUAL THE INSTALL RECORD'S FILENAME STEM AND
       TO EQUAL THE record's own install_record_id FIELD. Either inequality
       refuses with INSTALL_RECORD_NAME_MISMATCH.

CK-13  REQUIRE THE RECORD'S MEMBERS LIST TO EQUAL THE ENUMERATED SET, UNDER A
       TOTAL TWO-CLAUSE PARTITION WITH A LITERAL SUB-ORDER.
       WHAT IS ALREADY TRUE WHEN THIS CHECK BEGINS, and it is what makes the
       partition total: CK-6 has proved the record structurally valid, so the
       members array has EXACTLY 69 entries, each with exactly the keys class,
       path and sha256, each class one of the seven literals, each sha256 64
       lowercase hexadecimal characters, and the array sorted ascending by class
       then path. CK-4 has produced the enumerated set, also 69 entries in that
       same order. CK-7 has recomputed every member's actual digest.
       D1  THE (class, path) SEQUENCE. Compare the record's ordered sequence of
           (class, path) pairs with the enumerated sequence, index by index,
           ascending from 0. At the FIRST index where they differ, refuse with
           MEMBER_SUBSTITUTED naming the index, the expected pair and the found
           pair.
           D1 OWNS EVERY (class, path) DISAGREEMENT, WHATEVER ITS SHAPE. A path
           the enumeration does not contain, an enumerated path the record does
           not contain, a moved class label, and a replacement of one by the
           other are ALL one disagreement at one index. A replacement is not two
           facts competing for two codes; version 1.5 described the same state
           in two ways and mapped the descriptions to different codes, and that
           is the ambiguity this clause removes.
       D2  THE RECORDED DIGESTS. Evaluated ONLY if D1 found no disagreement, so
           the record's (class, path) sequence is exactly the enumerated one.
           Compare each entry's sha256 with the digest recomputed at CK-7, in
           the same ascending index order. At the FIRST inequality, refuse with
           MEMBER_STALE naming the index and the path.
       D1 AND D2 ARE DISJOINT BY CONSTRUCTION — D2 is unreachable unless D1
       passes — AND TOGETHER THEY ARE TOTAL over the states this check can
       receive, because a structurally valid 69-entry sorted array either agrees
       with the enumeration on every (class, path) or does not, and if it does,
       either agrees on every digest or does not.
       WHAT CANNOT FIRST APPEAR HERE, and where it appears instead: an ABSENT
       member is already fatal at CK-7 with MEMBER_OMITTED; a member whose bytes
       differ from an MS-2 or MS-3 literal is already fatal at CK-7 with
       HISTORICAL_BYTE_MOVED; and a members array of any length other than 69 is
       already fatal at CK-6 with MEMBER_SUBSTITUTED, because cardinality is a
       STRUCTURAL predicate.
       MEMBER_EXTRA IS RETIRED, AND THIS IS WHY. With cardinality fixed at 69 by
       CK-6, an entry outside the enumerated set NECESSARILY displaces an
       enumerated one, so every state MEMBER_EXTRA could have named is a D1
       disagreement. The code had no state of its own; keeping it would have
       preserved exactly the overlap this partition removes. FC-1's closed set
       therefore has 25 codes, not 26.

CK-14  COMPLETE STAGE B VERIFICATION: TS-5 clauses B14 through B18, in order.

CK-15  THE M7 SEMANTIC CHECK. REQUIRE THE M7 ATTESTATION to name MS-5's literal
       verifier path, the M5 digest and the two M6 digests found at CK-7, in
       MS-6's order, and to carry the bundle digest recomputed from them per
       MS-6, with rows_attested exactly the 24 integers 92..115 ascending,
       row_count exactly 24 and all_rows_passed exactly the boolean true. Any
       failure refuses with ATTESTATION_MISMATCH. A passing attestation produced
       against a different verifier or a different test bundle is rejected here,
       and so is a well-typed attestation carrying the wrong 24 integers.
       THE WHOLE CHECK, CK-1 THROUGH CK-15, IS FAIL-CLOSED AT THE FIRST FAILURE
       AND HAS NO PARTIAL MODE, NO WARNING MODE AND NO OVERRIDE.

FC-1  THE CLOSED FAILURE-CODE SET. On ANY failure of CK-1 through CK-15, or on
      an observed procedure violation under FS-4, REFUSE with
      "WATCHDOG_AUTHORITY_INSTALL_INCOMPLETE" and exactly one reason code
      naming the first failing check and the offending path. VP-3 makes "the
      first failing check" single-valued and VP-4 makes it implementation-
      independent by establishing every prerequisite before its dependent. The
      set has 25 codes, is closed, and no build may add, rename or merge one.
      VERSION 1.5 HAD 26; MEMBER_EXTRA IS RETIRED BY CK-13's total partition,
      which left it with no state of its own:
        STAGE_A_ABSENT                 STAGE_A_MALFORMED
        STAGE_A_OPTION_INVALID         STAGE_A_KEY_MALFORMED
        STAGE_A_PRESELECTION_MISMATCH  STAGE_A_BINDING_MISMATCH
        STAGE_B_ABSENT                 STAGE_B_MALFORMED
        STAGE_B_SIGNATURE_ABSENT       STAGE_B_SIGNATURE_INVALID
        STAGE_B_ALGORITHM_INVALID      STAGE_B_STAGE_A_MISMATCH
        STAGE_B_OPTION_MISMATCH        STAGE_B_INSTALL_ID_MISMATCH
        STAGE_B_GOVERNING_MISMATCH
        INSTALL_RECORD_ABSENT          INSTALL_RECORD_NAME_MISMATCH
        INSTALL_RECORD_REPLAYED
        MEMBER_OMITTED                 MEMBER_STALE
        MEMBER_SUBSTITUTED
        MANIFEST_VALUE_MISMATCH        ATTESTATION_MISMATCH
        HISTORICAL_BYTE_MOVED          PROCEDURE_VIOLATION_OBSERVED
      EVERY ONE OF THE 25 HAS EXACTLY ONE OWNING CHECK: HISTORICAL_BYTE_MOVED
      only at CK-7; MEMBER_OMITTED only at CK-7; MEMBER_SUBSTITUTED at CK-6 and
      CK-8 for structural violations of the record, M4 and M7 and at CK-13 D1
      for a (class, path) disagreement, which are disjoint objects and disjoint
      clauses; MEMBER_STALE only at CK-13 D2; MANIFEST_VALUE_MISMATCH only at
      CK-10; INSTALL_RECORD_NAME_MISMATCH only at CK-12.
      PROCEDURE_VIOLATION_OBSERVED is the FS-4 code and is the only code that
      can be raised by a contemporaneous observation rather than by a predicate
      over final bytes. It routes to the ordinary process/control invalidity
      disposition. Version 1.1's INSTALL_RECORD_UNAUTHORIZED remains WITHDRAWN,
      replaced by the nine STAGE_B_ codes.
      ON REFUSAL no process is created, no handle is allocated, no freeze route
      is reachable, no evidence is accepted, no settlement runs, and NOTHING
      DEGRADES TO A PRIOR BEHAVIOUR. Recovery is to complete OR-1 through OR-11
      and re-run the check; there is no other recovery.

FS-1  WHAT G-11 PROVES. G-11 IS A FINAL-STATE VERIFIER. On success it proves,
      of the bytes present on disk at the moment it runs, exactly this and no
      more:
        a. Stage A exists at its exact literal path, its bytes are canonical,
           and every one of its eleven fields satisfies TS-2 A1..A17;
        b. Stage B and its detached signature exist at their exact literal
           paths, the .json bytes are canonical, every one of its thirteen
           fields satisfies TS-5 B1..B18, and the signature verifies under the
           key pinned in Stage A and under no other key;
        c. all 69 members exist at their literal paths; every digest matches;
           every M2 and M3 digest additionally equals the value recorded
           literally at MS-2 and MS-3; and M4, M7 and the record satisfy both
           the structural predicates of VP-1 and the semantic relations of
           VP-2;
        d. install_record_id recomputed from those bytes equals the record's
           filename, equals the record's own install_record_id field, and
           equals Stage B's install_record_id;
        e. M7 binds the M5 digest and the two M6 digests actually found;
        f. exactly one content-addressed record exists directly under the
           INSTALL directory;
        g. the manifest's reachable_closure equals the canonical eighty-nine-row
           value of MS-11.1, which covers the standard-library role import
           surface of all three scoped allowlists including generic_harness.py;
           its project_import_dependencies equals the closed four-module surface
           of MS-13, each module's digest recomputed from the bytes installed at
           its literal path; its
           peer_amendment_sha256 equals the M1 amendment digest recomputed from
           disk; and its three pre-selection digests equal the values A16(b),
           A16(c) and A16(d) derive from named repository bytes, rather than
           merely equalling Stage A's copies of themselves.
      THAT IS THE WHOLE OF WHAT IT PROVES. It is a predicate over a byte state,
      evaluated at one instant.

FS-2  WHAT G-11 DOES NOT PROVE, STATED SO THAT NO SECTION MAY IMPLY OTHERWISE.
      G-11 OBSERVES NO EVENT AND RECONSTRUCTS NO HISTORY. The artifacts carry
      no trusted monotonic counter, no append-only predecessor chain, no
      externally checked sequence number, no notarized time, no witness outside
      this repository and no evidence of any kind about the order in which
      files came to exist. created_utc is author-supplied, unauthenticated and
      compared with nothing (MS-10).
      THEREFORE, GIVEN THE EXACT VALID FINAL BYTES, G-11 CANNOT DISTINGUISH
      ANY OF THE FOLLOWING PAIRS. In each pair the final bytes are identical,
      so no predicate over final bytes separates them:
        the record written at OR-11        the identical record written before
                                           Stage B existed
        an M7 written after the matrix ran the identical M7 written before the
                                           matrix ran
        an id computed after M4 was        the identical id computed from
          written                          planned M4 bytes before M4 existed
        a Stage A created before OR-4      the identical Stage A created after
                                           variant resolution
      EVERY VERSION-1.2 STATEMENT TO THE CONTRARY IS WITHDRAWN: OR-11's claim
      that an early record is refused at CK-3 or CK-9; test 106(h)'s claim that
      the gate refuses each forbidden ordering; and every summary sentence
      asserting that any deviation from OR-1..OR-11 is refused. What was true
      in each of those cases is the CONTEMPORANEOUS fact of FS-4, not a
      property of the final state.

FS-3  OR-1..OR-11 REMAINS A MANDATORY OPERATOR OBLIGATION AND THE SOLE
      CONFORMING CONSTRUCTION PROCEDURE. An operator or driver that departs
      from it has produced a NONCONFORMING installation whether or not any
      check can say so, and the departure is a governance violation on its own
      terms. FS-2 withdraws a false claim about detection; it withdraws no
      obligation, weakens no step and permits no alternate route.

FS-4  A CONTEMPORANEOUSLY DISCOVERED PROCEDURE VIOLATION FAILS CLOSED. If the
      procedural driver, an operator, a review, a crash-recovery pass or any
      check observes a departure from OR-1..OR-11 WHILE IT IS OCCURRING, or
      while an intermediate state still exhibits it — a hex-named record
      present under the INSTALL directory while Stage B is absent; an M7
      present with no recorded matrix run; a manifest written after the id was
      computed; a Stage A whose creation follows OR-4 in the driver's own
      recorded state; a driver whose own step counter is out of order — then
      the installation is REFUSED with PROCEDURE_VIOLATION_OBSERVED, routes to
      the ordinary process/control invalidity disposition, AND NO PRODUCTION
      ENTRY POINT RUNS.
      This refusal is a CONTROL-PLANE fact. It is never scientific evidence and
      enters no acceptance predicate, qualification, comparison, endpoint, Q or
      C fact.

FS-5  AN UNDISCOVERED PROCEDURE VIOLATION IS INSIDE THE DECLARED PROCEDURAL
      RESIDUAL OF TR-2 AND IS NOT CLAIMED TO BE CAUGHT. This is stated rather
      than hidden. It is the honest consequence of having no trusted external
      order anchor.
      NO SUCH ANCHOR IS INTRODUCED, PERMITTED OR IMPLIED BY THIS AMENDMENT: no
      hardware security module, no external service, no timestamp oracle, no
      notary, no transparency log, no monotonic counter device and no new
      scientific gate. Adding one would be a new design round with its own
      author cell, and it is out of scope here.

TR-1  NON-CIRCULARITY, PROVED BY THE ORDER OF DETERMINATION.
        the 69 members determine install_record_id            (IR-1)
        install_record_id determines the record's filename     (IR-2)
        Stage B names that id and is signed over its own canonical bytes
                                                               (TS-3, TS-4)
        the Ed25519 key that verifies Stage B is pinned in Stage A
                                                               (TS-1, TS-5 B12)
        Stage A is created at OR-3, before any M1 byte is final at OR-4, and is
        written by no later step
      THE CHECK ORDER IS ALSO ACYCLIC, AND VP-4 STATES IT AS A TOPOLOGICAL
      ORDER: no check reads an object that a later check is responsible for
      making well formed.
      NO OBJECT IN THIS CHAIN ATTESTS ITSELF. IR-4 is a NON-EXHAUSTIVE
      SUMMARY and states no complete graph; version 1.6's sentence here, which
      said that it did, is WITHDRAWN as a residue of the completeness claim
      IR-4 itself already gave up. The exhaustive surface is IR-13, under the
      relation class IR-13 defines, and it carries the intentional redundant
      edges from M4 and M7 and claims no uniqueness of attester. Each link is
      verified by a link above it, and the chain terminates OUTSIDE the
      installed set at an artifact the author created. THERE IS NO CYCLE.
      NON-CIRCULARITY IS A STATEMENT ABOUT THE DEPENDENCY GRAPH, NOT ABOUT
      TIME. It does not imply that the construction order is verifiable; FS-2
      governs that.

TR-2  THE NAMED RESIDUAL — PROCEDURAL, STATED, NOT CLOSED. It has TWO clauses
      and both are load-bearing.
      (a) FULL-CHAIN SUBSTITUTION AT OR BEFORE STAGE-A CREATION. Stage A's
          authenticity rests on author custody: it is a tracked repository file
          created by Kirill, its exact digest is bound into the manifest by
          TS-2 A17, and that digest is recorded by the independent X and Y
          confirmations of the selection round. An actor able to write this
          repository at or before Stage-A creation can substitute Stage A,
          Stage B, the signature, the manifest and the record together and
          produce an internally consistent install.
      (b) COMPLETE COHERENT ROLLBACK OF A PREVIOUSLY VALID GENERATION, AT ANY
          LATER TIME. After a newer generation exists, an actor able to replace
          the whole repository control set can RESTORE an earlier generation
          in full — its Stage A, all of its members, its Stage B, its detached
          signature and its sole content-addressed record. On those restored
          bytes every check of FS-1 passes: Stage A matches the restored M4;
          the old signature verifies under the restored Stage-A key; the old id
          matches the restored members and the sole record name; CK-5 sees
          exactly one hex-named record; every digest and the attestation match.
          NO NEW SIGNATURE AND NO PRIVATE KEY ARE NEEDED. THIS REACHES A
          RUNNABLE STATE AND IS NOT REFUSED. It is outside the guarantee, and
          the coherent-rollback fixture of test 106 classifies it as such
          rather than pretending it fails.
      WHAT THE TWO STAGES DO CLOSE — exactly these PROPER-SUBSET cases, and
      this list is the whole of the claim:
        Stage A replaced while the manifest is not          A17
        the manifest replaced while Stage A is not          A17, CK-8, CK-13
        the signature replaced, removed or malformed        B11, B12
        Stage B replaced while the signature is not         B12
        the record replaced while the members are not       CK-11, CK-12, B15
        the members replaced while the record is not        CK-7, CK-13
        M7 replaced while M5 or M6 is not                   CK-15
        an old record presented against current members     CK-12, B15
        an old record retained beside the current one       CK-5
        a mixed-generation pair of governing files          CK-7, CK-13, B15
        an option mismatch between the two stages           A9, B14, and the
                                                            B14 edge is now
                                                            carried by IR-4
        an unsigned install of any shape                    B1, B12 — no route
                                                            admits one
        a manifest whose peer_amendment_sha256 is a
          well-formed value that is not the M1 amendment
          digest                                            CK-10
        a manifest whose reachable_closure is structurally
          valid, self-closed and factually wrong, including
          one that omits the role import surface of
          generic_harness.py                                CK-10
        a project-import dependency whose installed bytes,
          path, import edge, stdlib seed or effect assertion
          differs from MS-13                                CK-10
        a record naming an unenumerated path in place of an
          enumerated one                                    CK-13 D1
        a record whose recorded digest differs from the
          recomputed one                                    CK-13 D2
        a manifest whose roots, root_source_sha256 or
          composite region digests are well formed and
          wrong                                             CK-10
        a coordinated arbitrary pre-selection triple
          written identically into Stage A and the
          manifest                                          A16(b), A16(c),
                                                            A16(d)
      THE FOUR NEW ROWS ARE PROPER-SUBSET CASES LIKE THE OTHERS, AND THEY
      NARROW NOTHING AND WIDEN NOTHING ABOUT CLAUSE (a) OR CLAUSE (b). Each of
      them was open in version 1.3 and each is closed in version 1.4; none of
      them was ever claimed closed by version 1.3, and the residual itself is
      unchanged.
      NO SENTENCE IN THESE GOVERNING BYTES, IN ANY PACKET AND IN ANY CLOSURE
      MAY CLAIM: that every post-hoc substitution is closed; that complete
      coherent rollback is resisted, detected or refused; that custody is
      immutable or external to this repository; or that any cryptographic
      freshness, monotonicity, recency or liveness property holds.
      THREE WORDS IN THAT PROHIBITION ARE ALSO USED ELSEWHERE IN A DIFFERENT
      AND PERMITTED SENSE, AND THE SENSES ARE SEPARATED HERE SO THAT NO LEXICAL
      SWEEP HAS TO GUESS:
        IMMUTABLE, in DA-1, DA-2, DA-3, MS-2 and §A7.2, is a DOCUMENT-AUTHORITY
          and RECORD-MUTATION word. It says that a historical document is not
          opened for behaviour and that a durable record is never overwritten,
          truncated, renamed or deleted by a conforming actor. IT IS NOT A
          CUSTODY CLAIM: it does not say that any byte is beyond the reach of an
          actor able to write this repository, and TR-2(a) and TR-2(b) say the
          opposite;
        MONOTONIC, in TIMING, QC, AK, RF, §A3.4 and every *_monotonic_ns field,
          names CLOCK_MONOTONIC samples inside one running generation. It is a
          runtime clock word and is NEVER a property of the install chain, of
          any digest, of any signature or of any ordering across generations;
        LIVENESS, in WA, AK, NS and the watchdog sections, names the watchdog's
          own acknowledgement health inside one generation. It is never a
          cryptographic liveness or freshness property of these artifacts.
      NO OCCURRENCE OF ANY OF THE THREE, ANYWHERE IN THIS PAIR, IS A CLAIM THE
      PROHIBITION ABOVE FORBIDS.
      THE ED25519 CHAIN AUTHENTICATES STAGE B RELATIVE TO THE STAGE-A KEY AND
      CLOSES PARTIAL SUBSTITUTION UNDER THE PROCEDURAL ROOT. IT CREATES NO
      FRESHNESS. A signature proves who signed a message, never when, and
      never that no earlier signed message is still available.
      Both residual clauses are procedural, are of the same kind as the A3
      same-UID residual already named in the composite's named-residuals
      section (§P1-12.4), are infrastructure facts and not scientific evidence,
      and are citable in no Q or C fact.
      THE EXACT threat_model STRING STAGE A MUST CARRY, byte for byte, is the
      following. It contains no newline: each line break in this presentation
      stands for exactly one space, and there is no leading or trailing space.
        Stage A is the external trust root for the P1 watchdog-freeze
        install. Its authenticity rests on author custody of this
        repository. An actor able to write this repository before Stage A
        exists can substitute the whole authorization chain, and an actor
        able to replace the whole repository control set at any later time
        can restore a complete earlier valid generation; both residuals are
        procedural, are named, and are not closed by these bytes.

XS-1  EXTERNAL AUTHOR STATE THAT IS NOT A MEMBER AND IS NOT AUTHORITY HERE.
        successor/OFFICINA_P1_PROCESS_CLAIM_IDENTITY_SELECTION_V1_SIGNATURE.md
        7a8ab2daefe9ad5d8d5bce74d7921a4fa600b44f17aa7a407acab26e472e3d1f
      WHAT IT IS. Kirill's signed selection of the P1 process-claim identity
      architecture, Option A, token
      I_SELECT_P1_PROCESS_CLAIM_IDENTITY_A_OBSERVATION_ONLY, dated 2026-08-04.
      It is recorded here as CURRENT AUTHOR STATE so that no reader has to
      infer it, and for no other purpose.
      WHAT IT IS NOT. Every clause here is load-bearing:
        it does NOT sign, accept or authorize the separately named token
          P1_IDENTITY_OBSERVATION_BOUNDED_WEAKENING_V1, which the identity
          packet requires to be reviewed and accepted SEPARATELY before Option
          A can become operative. That token is NOT ACCEPTED, and this
          amendment does not accept it, make it signable, or predict it;
        it does NOT select, move or influence the watchdog-freeze cell, which
          remains NOT SELECTED;
        it does NOT make this amendment, the composite, or any P1 composite
          operative, and it resolves no blocking notice;
        it is NOT a member of M1..M7 and its digest is in no install record;
        it is NOT scientific evidence, not a covariate, not an endpoint, not a
          qualification or comparison input, and not an input to any acceptance
          predicate. It is a control-plane author-state fact.
      WHY IT IS NOT A MEMBER. Binding it into M1..M7 would make the watchdog
      install depend on a selection whose own enabling token is unaccepted, and
      would import an unreviewed prerequisite into a gate whose entire point is
      that its inputs are literal, closed and reviewed.
      WHERE IT MUST BE ACCOUNTED FOR INSTEAD. The LATER COMBINED BINDING — the
      single reviewed specification that binds the signed identity selection
      together with the signed watchdog option, and which is what resolves the
      process-claim identity cell stated at composite §P1-13.2 row 2 — MUST:
        a. record this signature's literal path and its exact digest;
        b. record the separate review and acceptance of
           P1_IDENTITY_OBSERVATION_BOUNDED_WEAKENING_V1, or refuse to proceed;
        c. state whether this signature becomes a member of that binding's own
           closed set and, if so, in which class and with what cardinality;
        d. re-derive the identity fields of the process-claim record, which
           this amendment neither selects nor repairs (F-2, N-4).
      UNTIL THAT BINDING EXISTS AND HAS BEEN INDEPENDENTLY REVIEWED, THE
      IDENTITY CELL IS RECORDED AS SELECTED, THE IDENTITY BOUNDED-WEAKENING
      TOKEN AS NOT ACCEPTED, AND NEITHER FACT MOVES ANYTHING IN THIS PAIR.

--- END JOINT INSTALL AND AUTHORIZATION BLOCK ---
```

### §P1-14.5 Acyclic hash custody

```text
This file contains none of its own digests, so there is no cycle. The custody
chain is a directed acyclic graph with six links and no back edge:

  1. this composite file                — contains no digest of itself
  2. the author closure                 — reports H_FILE, H_BODY, H_GUARDDATA
                                          and H_NORMATIVE, and is normative for
                                          NOTHING
  3. the independent X and Y reviews    — recompute and confirm all four
  4. the Stage-A selection artifact      — pins the option token and the
                                          Ed25519 verification key, and carries
                                          the PATH AND DIGEST OF ALL THREE
                                          pre-selection inputs — the author
                                          choice packet, the peer amendment and
                                          1 — each anchored by TS-2 A16(b),
                                          A16(c) and A16(d) to named repository
                                          bytes rather than to Stage A's own
                                          copy; contains no digest of itself
  5. the production manifest            — records the reviewed values, which
                                          G-6 and G-7 then enforce against the
                                          live bytes, and binds Stage A's path,
                                          digest and key id; contains no digest
                                          of itself
  6. the Stage-B authorization and its   — names the install-record id and is
     detached signature                   signed over its own canonical bytes
                                          with the key pinned at 4; contains no
                                          signature of itself

No step reads a digest from a document that contains it. Verification order is
1, then 2, then 3, then 4, then 5, then 6; the verifier depends only on the
manifest, this file's bytes, the two authorization artifacts and the member
bytes on disk. `TR-1` states the same acyclicity as a proof over the
determination order.

**This is a statement about the dependency graph, not about time.** The chain is
acyclic; it is not a proof that the links were created in this order, and
`FS-2` governs that distinction. **This subsection and `IR-4` are SUMMARIES and
are explicitly NON-EXHAUSTIVE; NEITHER OF THEM IS COMPLETE AND NEITHER MAY BE
CALLED COMPLETE. The normative register is `IR-13`, which is exhaustive over the
K1..K5 cross-object and external relation class it defines and over nothing
else, carries FIFTY rows, and governs wherever a summary and it differ.**
**The graph is also not a tree**, and the edges neither summary should be read
as bounding include: `M4` binds the two `M1` digests, the three pre-selection
inputs and Stage A; **Stage A itself binds the same three pre-selection inputs
by path and digest — three edges version 1.6 omitted while calling its graph
complete**; **Stage B binds Stage A by `selected_option_token` equality at
`B14`**; **and Stage B binds `M4` directly by the `B18` equality of
`governing_amendment_sha256` with `peer_amendment_sha256`, which version 1.8's
diagram did not draw**; the `M1` amendment's `§A0.4` anchor line binds the
pre-selection composite bytes; and `M7` binds `M5` and `M6`. Those redundant
inbound edges are intentional. **No uniqueness of attester is claimed
anywhere**, and version 1.2's assertion that every member is attested by exactly
one other object remains withdrawn as false. **VERSION 1.9 STILL SAID HERE, AND
AT `TR-1`, THAT `IR-4` STATES THE COMPLETE DIRECTED INTEGRITY GRAPH, WHILE
`IR-4` HAD ALREADY WITHDRAWN THAT CLAIM ABOUT ITSELF. BOTH SENTENCES ARE
WITHDRAWN. Nothing in this pair now calls `IR-4`, this subsection or any other
reduced view complete, and nothing may be inferred from what a summary does not
draw.**
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
H-1  ONE UNIT. The v1.7 peer amendment and this composite v1.10 are ONE
     indivisible acceptance unit. Neither is operative alone. Accepting one
     without the other is NOT a conforming state and NOT a partial success. The
     v1.6 amendment and composite v1.9 are WHOLLY REPLACED, not amended, and
     every earlier amendment and composite remains wholly replaced.

H-2  THE ORDERED STEPS ARE `OR-1` THROUGH `OR-11` OF §P1-14.4, STATED THERE IN
     FULL, AND THEY ARE NOT RESTATED IN A SECOND FORM ANYWHERE. There is
     exactly ONE statement of the ordering in these governing bytes, carried
     byte-identically in this file and in §A10 of the peer amendment, so no two
     statements of it can disagree.
     THE ORDER IS A MANDATORY OPERATOR OBLIGATION, NOT A VERIFIED PROPERTY.
     `OR-1` and `FS-3` state the obligation; `FS-2` states that the final-state
     gate cannot distinguish identical final bytes produced in a forbidden
     order; `FS-4` fails closed when a violation is observed while it occurs;
     `FS-5` places an unobserved violation inside the residual of `TR-2`.
     ALL STEPS LAND TOGETHER OR NONE DOES.

H-3  NO PARTIAL LANDING IS CONFORMING OR OPERATIVE. `G-11` is the enforcement
     point for the FINAL STATE and it runs before any production entry point,
     as `CK-1` requires. Its fifteen checks run in the literal topological order
     of `VP-4`, in which every predicate's prerequisites are established by an
     earlier check. A partial landing that is still partial when the gate
     runs is refused by a named check; a violation of ORDER that leaves the
     exact valid final bytes is a governance violation the gate cannot see, and
     `FS-2` says so rather than pretending otherwise.

H-4  EXISTING HISTORY REMAINS BYTE-IDENTICAL. Zero historical bytes are edited
     by any step of `OR-1`..`OR-11`. `OR-11` and `CK-12` verify this and refuse
     on any difference with HISTORICAL_BYTE_MOVED.
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
| 13 | the PCS import set is exactly the six of §P1-3.2, and `signal`, `functools`, `enum` and `_thread` are absent from **the transitive at-import closure of those six**, which is the fourteen-row subset of `MS-11.1`. **This row is about the import-edge closure of the PCS root and not about process residency**: on the pinned build the interpreter's own start-up module table already contains `_thread` before any contract import runs, as `MS-11.3` discloses, and no allowlist choice can alter that. A fixture asserting that `_thread` is absent from a live PCS process **fails this row**, and so does a build in which any of the four is reached by an import edge from the six |
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
| 80 | the five production roots are exactly those of §P1-3.1; the scoped map gives each root exactly its set; `generic_harness.py` imports none of `signal`, `_signal`, `sys` or **`subprocess`**, its scoped set is exactly the **sixteen** names of `§P1-3.2` after the `MS-11.5` reduction, and a build importing `subprocess` there is refused both by that allowlist and by `S-12` |
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
| 103 | **historical bytes unmoved.** Every `M2` member and every `M3` member carries the digest recorded literally at `MS-2` and `MS-3`. A build in which any of the 62 recorded digests differs, or in which either `M1` member is absent or carries different bytes, is refused with `WATCHDOG_AUTHORITY_INSTALL_INCOMPLETE` before any process is created |
| 104 | **install record absent.** With all 69 `M1`..`M7` members present and correct, Stage A and Stage B valid, but no file directly under the `INSTALL` directory whose name is 64 lowercase hexadecimal characters followed by `.json`, `G-11` refuses at `CK-5` with `INSTALL_RECORD_ABSENT` and no production entry point runs. **`CK-5` establishes the record's existence and uniqueness before `CK-6` validates its bytes and before `CK-7` reads any member**, so this refusal is the first one reachable and no other code contends for it |
| 105 | **install record name mismatch, and every field of `IR-3`.** A record whose filename is not the `IR-1` digest of its own member list is refused with `INSTALL_RECORD_NAME_MISMATCH`: the fixture perturbs one member digest inside the record while leaving the filename intact, and separately renames a correct record. **The same row exhausts the record schema, and it exhausts it ON BOTH SIDES OF THE `VP-1`/`VP-2` BOUNDARY, with exactly one expected code per case.** **STRUCTURAL, refused at `CK-6` with `MEMBER_SUBSTITUTED`:** a `schema` value other than the exact literal `philosophia.officina.t-watchdog-authority-install.v1`; a `version` that is `"1"`, `1.0` or any integer but 1; a missing key; an extra key; bytes that are valid JSON but not `CANON`; a `members` array of other than 69 entries; an entry whose key set is not exactly `{class, path, sha256}`; a `class` outside the seven literals `M1`..`M7`; a `members` array not sorted ascending by `class` then `path`; an `install_record_id` that is not 64 lowercase hexadecimal characters; and a `created_utc` violating the grammar or the semantic validator of `MS-10`. **SEMANTIC:** a record that satisfies every structural predicate above and whose `install_record_id` is a well-formed 64-hex value that does not equal the `IR-1` digest of its own `members` array, or does not equal its filename stem, **reaches `CK-12` and is refused with `INSTALL_RECORD_NAME_MISMATCH` — never with `MEMBER_SUBSTITUTED`**, and a fixture expecting `MEMBER_SUBSTITUTED` for that case **fails this row**. **`IR-3` no longer names `CK-8` or `CK-9` for either equality; a fixture asserting either of those owners fails this row.** A record whose `members` array is structurally valid but disagrees with the enumerated set reaches `CK-13`, whose total two-clause partition row 107 exercises. **MULTI-FAULT, and this is what version 1.7 left undefined:** a state carrying a MALFORMED sole record together with an ABSENT member, and a second state carrying a malformed sole record together with a STALE member, are each refused at **`CK-6` with `MEMBER_SUBSTITUTED`** — because the record is structurally validated at `CK-6`, before any member is read at `CK-7` — and a fixture expecting `MEMBER_OMITTED` or `MEMBER_STALE` for either state **fails this row**. The row additionally asserts that `IR-3`'s value grammar no longer contains either equality |
| 106 | **two-stage author authorization — ten fixture groups. Groups (a) through (g) and (j) are refused with the named codes; group (h) tests the procedural driver only; group (i) is classified OUTSIDE THE GUARANTEE and is NOT falsely refused.** **(a) wrong path**: a well-formed Stage-A artifact at any path other than `TS-1`'s exact path — including a plausible sibling under the same directory — yields `STAGE_A_ABSENT` at `A1`; the same for Stage B at any path other than `TS-3`'s, at `B1`. **(b) wrong key**: Stage B signed by a different Ed25519 key yields `STAGE_B_SIGNATURE_INVALID` at `B12`; a Stage A whose `key_id` is not the SHA-256 of the 32 raw bytes of its own `public_key_hex`, or whose `public_key_hex` is not 64 lowercase hexadecimal characters, yields `STAGE_A_KEY_MALFORMED` at `A10`/`A11`; a fixture offering a second key as a permitted alternative fails, because `B12` admits exactly one key. **(c) wrong signature**: a bit-flipped signature; a signature over a re-serialized non-canonical variant of the same object; a signature over the parsed value rather than the file bytes; a pre-hashed Ed25519 signature; an absent `.sig`; a `.sig` with a trailing newline or an uppercase hexadecimal character — refused at `B12`, `B12`, `B12`, `B12`, `B1` and `B11` respectively. **(d) wrong Stage-A hash**: a Stage B whose `stage_a_sha256` is not the digest of the Stage-A file on disk yields `STAGE_B_STAGE_A_MISMATCH` at `B13`; a Stage-A file substituted after the manifest was written yields `STAGE_A_BINDING_MISMATCH` at `A17`; a Stage A whose `governing_pre_selection` paths or digests do not equal the manifest's six `pre_selection_*` fields yields `STAGE_A_PRESELECTION_MISMATCH` at `A15`/`A16(a)`. **And the case version 1.6 admitted:** a Stage A and a manifest carrying the SAME arbitrary well-formed 64-hex triple, agreeing perfectly with each other and with nothing else, is refused at `A16(b)`, `A16(c)` and `A16(d)` respectively — the packet digest recomputed from the bytes at the literal packet path, the amendment digest recomputed from the bytes at the literal amendment path, and the composite pre-selection digest read from the unique `§A0.4` anchor line of the `M1` amendment. **All four sub-clauses run at `CK-9`, after `CK-7` and `CK-8` have proved the manifest present, parseable, an object, exactly keyed, exactly typed and structurally valid**; a fixture presenting a valid Stage A with an ABSENT manifest must be refused at `CK-7` with `MEMBER_OMITTED`, and one presenting a valid Stage A with an INVALID-JSON manifest at `CK-8` with `MEMBER_SUBSTITUTED`, and a fixture expecting any `STAGE_A_` code for either state **fails this row**. A state carrying BOTH an `M4` semantic mismatch and a Stage-A binding mismatch is refused at `CK-9` with `STAGE_A_BINDING_MISMATCH`, because `CK-9` precedes `CK-10`. Separate fixtures present an amendment carrying zero anchor lines and one carrying two, and each is refused at `A16(d)`; a fixture in which a prose mention of the anchor token is miscounted as an anchor line also fails. **(e) replay against current members**: a record and a Stage-B artifact from an earlier install generation, each internally consistent and validly signed, presented against the CURRENT member set, yield `INSTALL_RECORD_NAME_MISMATCH` at `CK-12` and `STAGE_B_INSTALL_ID_MISMATCH` at `B15`; the earlier record retained alongside the current one yields `INSTALL_RECORD_REPLAYED` at `CK-5`. **(f) option mismatch**: a Stage B whose `selected_option_token` differs from Stage A's yields `STAGE_B_OPTION_MISMATCH` at `B14`; a Stage A pairing one option token with the other option's amendment token, or carrying a token that is neither of the two literal strings, yields `STAGE_A_OPTION_INVALID` at `A8`/`A9`. **(g) substituted authorization, proper subset**: the fixture enumerates the fifteen proper-subset cases listed at `TR-2`, including the four added in version 1.7 — a well-formed `peer_amendment_sha256` that is not the `M1` amendment digest, a structurally valid but factually wrong `reachable_closure`, well-formed but wrong `roots`/`root_source_sha256`/region digests, and the coordinated arbitrary pre-selection triple. In each case a subset of {Stage A, Stage B, the signature, the manifest, the record, the members} is replaced under an attacker key while the rest is genuine, and the fixture asserts the specific named clause and code for each. **(h) procedural driver state, contemporaneous only**: this group drives the `OR` sequence and asserts transitions and crash cuts **while they occur** — a driver step counter that advances out of order; a hex-named record present under `INSTALL` while Stage B is still absent; an `M7` present with no recorded matrix run; a manifest written after the id was computed; a Stage A created after `OR-4` in the driver's own recorded state. Each is refused with `PROCEDURE_VIOLATION_OBSERVED` under `FS-4` and routes to process/control invalidity with no production entry. **This group asserts nothing about the final state, and it must NOT assert that `G-11` distinguishes byte-identical forbidden history**: `FS-2` states that it cannot, and a fixture claiming otherwise fails this row. **(i) complete coherent rollback — OUTSIDE THE GUARANTEE**: the fixture builds generation *N*, then generation *N+1*, then restores generation *N* in full — its Stage A, all 69 of its members, its Stage B, its detached signature and its sole content-addressed record — and asserts that `G-11` **PASSES** on the restored bytes. **That is the expected result, and the row fails if the fixture asserts a refusal.** The fixture is labelled `OUTSIDE_GUARANTEE_COHERENT_ROLLBACK`, cites `TR-2` clause (b), and asserts that no governing sentence claims the case is closed. **(j) exhaustive field validation, no field passing on presence alone**: for each of the eleven `TS-1` keys and each of the thirteen `TS-3` keys in turn, a fixture presents an artifact in which that one field carries a wrong literal, a wrong JSON type, a wrong length or a wrong derived relation while every other field is correct, and requires exactly the code that `TS-2` or `TS-5` names for that clause. A companion fixture presents each field with the correct type but an incorrect value and requires the same refusal. `created_utc` is validated by `MS-10` in both artifacts — including `2026-02-30T00:00:00Z`, `2026-01-01T24:00:00Z`, `2026-01-01T00:00:60Z`, a fractional second, an offset other than `Z`, and a lowercase `t` or `z` — and a build in which any `created_utc` value influences an ordering decision fails |
| 107 | **member omission, and the total `CK-13` partition.** For each of `M1`..`M7` in turn, one member is removed from disk, taking the enumerated set from 69 to 68. Each removal fails at `CK-7` and is refused with `MEMBER_OMITTED`. **No partial subset runs**: seven separate fixtures, seven refusals. The `M2` fixture removes one of the 55 literal provenance paths and the `M6` fixture removes one of the two literal test modules. **The same row exercises `CK-13`'s two-clause partition with six decisive fixtures, each requiring exactly one first code:** (i) a record carrying a 70th entry — an unenumerated extra path — is refused at **`CK-6` with `MEMBER_SUBSTITUTED`**, because cardinality is structural; (ii) a record in which one expected `(class, path)` is replaced by another path is refused at **`CK-13` D1 with `MEMBER_SUBSTITUTED`**; (iii) a record whose `(class, path)` sequence is exactly the enumerated one but one recorded digest is wrong is refused at **`CK-13` D2 with `MEMBER_STALE`**; (iv) a missing member is refused at **`CK-7` with `MEMBER_OMITTED`**; (v) a 70th entry **plus** a stale digest is refused at **`CK-6` with `MEMBER_SUBSTITUTED`**; (vi) a replaced path **plus** a stale digest is refused at **`CK-13` D1 with `MEMBER_SUBSTITUTED`**, because D1 strictly precedes D2. **`MEMBER_EXTRA` is retired and appears in no expected result; a fixture expecting it fails this row**, and so does any fixture in which D2 is reached while D1 has an outstanding disagreement |
| 108 | **extra member, and the v2.4 overlap.** For each of `M1`..`M7` in turn, one extra file is added to the class and to the record's member list, taking the record to 70 entries while `CK-4` still enumerates 69 from the constants; **each is refused at `CK-6` with `MEMBER_SUBSTITUTED`, because a members array of any length other than 69 is a STRUCTURAL failure and `MEMBER_EXTRA` no longer exists.** Additionally, a verifier that constructs `M2` by reading the provenance region rather than `MS-2`'s literal list enumerates **62** provenance paths instead of **55** — the seven `M3` paths reappear — and is refused, because its enumerated sequence disagrees with the record's at the first differing index (`CK-13` D1, `MEMBER_SUBSTITUTED`) or, if it also miscounts, at `CK-6`. **That fixture is the exact v2.4 class-overlap defect and it must fail** |
| 109 | **stale member, every class.** For each of `M1`..`M7` in turn, one member is replaced by an earlier version of itself at the same literal path. Each is refused with `MEMBER_STALE` at `CK-13` D2; **for `M2` and `M3` the refusal fires earlier and with a different code — `HISTORICAL_BYTE_MOVED` at `CK-7`, against the digest recorded literally at `MS-2` and `MS-3`, without consulting the record at all.** A state carrying changed `M2`/`M3` bytes together with a coordinated record-and-member mismatch is therefore refused at `CK-7` with `HISTORICAL_BYTE_MOVED`, and a fixture expecting `MEMBER_STALE` for that state **fails this row**. `HISTORICAL_BYTE_MOVED` is owned at `CK-7` and nowhere else; `MEMBER_STALE` is owned at `CK-13` and nowhere else |
| 110 | **substituted verifier.** A verifier at `MS-5`'s literal path implementing only `S-1`..`S-24b` and `G-1`..`G-9` — the pre-install baseline — is refused with `MEMBER_SUBSTITUTED`. A verifier implementing `G-10` but not `G-11`, and one implementing `G-11` but not `G-10`, are each refused. A correct verifier installed at any other path leaves `MS-5`'s path stale or absent and is refused with `MEMBER_STALE` or `MEMBER_OMITTED`. **The baseline verifier can never satisfy the gate** |
| 111 | **substituted or malformed manifest — every field of `MS-4`, on both sides of the `VP-1`/`VP-2` boundary.** **STRUCTURAL, refused with `MEMBER_SUBSTITUTED` at `CK-8`:** an absent manifest, refused earlier at `CK-7` with `MEMBER_OMITTED`; and, at `CK-8`, a `schema` value other than the exact literal `philosophia.officina.t-production-call-graph.v1`; a `version` that is `"1"`, `1.0` or any integer but 1; a missing key; an extra key; bytes that are valid JSON but not `CANON`; a `roots` array of other than five strings, with a duplicate, or in an order other than §P1-3.1's; a `root_source_sha256` whose key set is not exactly those five paths; any digest field that is not 64 lowercase hexadecimal characters; a `reachable_closure` that is not an array, whose element key set is not exactly the six keys, whose `kind` is outside the four literals, whose `transitive_imports` is unsorted or contains a duplicate, whose elements are not sorted ascending by `module`, whose `module` values are not pairwise distinct, or which names in some `transitive_imports` a module that is not itself an element of the same array; and a `created_utc` violating the grammar or the semantic validator of `MS-10`; and a manifest omitting ANY of the twenty-one keys — including any `stage_a_*` key, any `pre_selection_*` key and `project_import_dependencies`; **and, new in version 1.10 and reaching the nested depth that version 1.9 could not express:** a `project_import_dependencies.modules` element whose key set is the five keys of version 1.9 — that is, one from which `import_time_effects` is ABSENT; one carrying a NINTH effect key; one from which one of the eight effect keys has been REMOVED; one in which an effect key is RENAMED, for example `starts_thread` in place of `creates_thread` or `opens_network` in place of `opens_descriptor_or_socket`; one in which `import_time_effects` is not an object but an array, a string or `null`; and one in which any effect value is `null`, `0`, `1`, `"false"`, `"true"` or any non-boolean — **each is an `S4` or `S5` exact-key-set or type failure refused at `CK-8` with `MEMBER_SUBSTITUTED`, and a fixture expecting `MANIFEST_VALUE_MISMATCH` or any `STAGE_A_*` code for any of them fails this row.** **A MISSING KEY HAS EXACTLY ONE ANSWER, `MEMBER_SUBSTITUTED` AT `CK-8`.** Version 1.8 additionally offered `STAGE_A_BINDING_MISMATCH` or `STAGE_A_PRESELECTION_MISMATCH` for that same state, giving one byte state two normative answers; **that second answer is withdrawn, and a fixture expecting any `STAGE_A_*` code for a missing M4 key fails this row.** **SEMANTIC, refused with `MANIFEST_VALUE_MISMATCH` at `CK-10`:** a manifest that satisfies EVERY structural predicate above and carries a well-formed `peer_amendment_sha256` that is not the SHA-256 of the `M1` amendment bytes on disk; a `roots` array of five well-formed distinct strings that are not the five literal paths of `§P1-3.1` in that order; a `root_source_sha256` whose five values are well-formed hex that is not the digest of those roots' bytes; any of the four `p1_composite_*` values well formed and unequal to the recomputed `H_FILE`, `H_BODY`, `H_GUARDDATA` or `H_NORMATIVE`; and — **the fixture `MS-11.3` exists for** — a `reachable_closure` that is a non-empty array of objects with exactly the six keys, `kind` inside the four literals, `transitive_imports` sorted and distinct, the array sorted by `module` with distinct `module` values, and closed under itself, **and factually wrong**: one row's `kind` changed from `FROZEN` to `PURE_PYTHON`; one row's `starts_task`, `registers_at_fork` or `installs_handler` set true; a fifteenth self-consistent row added; the `posix` row removed together with every reference to it, leaving a smaller self-closed array; `os`'s `transitive_imports` reduced to the six names of the `§P1-3.3` prose table; and the whole array replaced by a self-closed array of unrelated module names. **And the project-import fixtures, new in version 1.9:** a manifest whose `project_import_dependencies` is structurally well formed but in which one of the four modules of `MS-13` carries a digest that is not the SHA-256 of the bytes installed at its literal path; one in which a module's `path` differs; one in which `philosophia.officina`'s `project_imports` array is reordered so that `interlock` precedes `canonical`; one in which a module's `stdlib_seeds` array gains or loses a name; **one in which exactly one of the thirty-two `import_time_effects` booleans is `true` while its object still carries exactly the eight keys and eight boolean values — a state version 1.9 could not build at all, which now PASSES `CK-8` and is refused at `CK-10`**; and one in which `execution_order` is replaced by the sorted `module` order — **each is refused at `CK-10` with `MANIFEST_VALUE_MISMATCH`**. **The row additionally asserts that each of the thirty-two booleans is individually addressable as `project_import_dependencies.modules[k].import_time_effects.<name>`, that toggling exactly one of them changes the manifest bytes, and that a build in which the effect assertions are absent from the serialized value fails.** **Each passes every `MS-4` shape rule and each MUST be refused at `CK-10`.** **And the fixture version 1.7 could not have had:** a `reachable_closure` carrying exactly the fourteen-row bootstrap value of version 1.4 — structurally perfect, self-closed, and covering only the two bootstrap allowlists — is **refused at `CK-10`**, because it omits the role import surface that `§P1-7.4` `A-10` creates; so is one that carries the eighty-nine rows but restores `subprocess`, `threading`, `signal`, `select`, `selectors`, `_posixsubprocess`, `locale` and `_locale`; and so is one that sets `registers_at_fork` true for any row. The row additionally asserts that `CANON` of an accepted `reachable_closure` is exactly **20534** bytes and hashes to `aa974e0c91e5c9afd0aceefa6b0e47ef42b5ad7b71dc4de690a4873232dc20ee`, that the primary check is a direct comparison with the `MS-11.1` literal value with the length and digest as corroboration, and that the check is **never** a recomputation from the live interpreter — a verifier that derives the closure at install time and accepts what it finds **fails this row**. **The 89-row value, its 20534-byte canonical length and its digest are UNCHANGED in version 1.10**; the four `MS-13` modules are bound separately and are not rows of it. **And the fixture that decides the `CK-9`/`CK-10` order, new in version 1.10:** a manifest that is structurally perfect at every depth and whose `reachable_closure` is factually wrong in exactly one row's `kind`, presented together with a Stage A whose digest disagrees with `stage_a_sha256`, is refused at `CK-9` with `STAGE_A_BINDING_MISMATCH` and **never reaches the wrong closure**; remove the Stage-A fault and the same manifest is refused at `CK-10` with `MANIFEST_VALUE_MISMATCH`. **A fixture expecting any code at `CK-7` for either state fails this row**, because `CK-7` establishes only that `M4` exists and recomputes its member-byte digest |
| 112 | **substituted or omitted test bundle.** Against `MS-6`'s two literal module paths and its exact row-membership rule: a module missing any row of 92..115; a row implemented in the wrong module; a row number implemented twice; a function of the row-name form for a row outside 92..115; the two modules swapped in `MS-6`'s order; and bytes differing from the attested digest — each refused with `MEMBER_SUBSTITUTED`. A bundle that contains all 24 rows but was never run produces no `M7` and is refused with `MEMBER_OMITTED` |
| 113 | **attestation malformed or mismatched — every field of `MS-7`, with one code per case and no undefined boundary.** **STRUCTURAL, refused with `MEMBER_SUBSTITUTED` at `CK-8`:** a `schema` other than the exact literal `philosophia.officina.t-watchdog-authority-test-attestation.v1`; a `version` other than the integer 1; a missing or extra key; non-`CANON` bytes; a `test_bundle_modules` value that is not an array of exactly two objects each with exactly the keys `{path, sha256}` of type string; a `rows_attested` that is not an array of exactly 24 integers, strictly ascending; a `row_count` that is not an integer; an `all_rows_passed` that is not a boolean; a digest field that is not 64 lowercase hexadecimal characters; or a `created_utc` violating `MS-10`. **SEMANTIC, refused with `ATTESTATION_MISMATCH` at `CK-15`:** a `verifier_path` other than `MS-5`'s literal path; a `verifier_sha256` naming a different verifier; a `test_bundle_modules` whose two well-formed paths are wrong or in the wrong order; a `test_bundle_digest` not recomputable from its own two entries; a well-formed strictly ascending `rows_attested` of 24 integers that are not exactly 92..115; a `row_count` that is an integer other than 24 or unequal to the array length; and `all_rows_passed` equal to the boolean `false`. **The undefined phrase "when the schema itself is violated" is withdrawn**, and a fixture that expects `MEMBER_SUBSTITUTED` for any case in the semantic list, or `ATTESTATION_MISMATCH` for any case in the structural list, **fails this row** |
| 114 | **mixed generation.** The v1.6 peer amendment installed with this composite v1.10; the v1.7 amendment installed with composite v1.9; and any other mixture of a v2.9-era with a v2.10-era governing file. Because `MS-1` names two literal paths, each mixture leaves one of them absent or bearing different bytes and is refused with `MEMBER_OMITTED` or `MEMBER_STALE`; a record rebuilt around the mixture is additionally refused with `STAGE_B_INSTALL_ID_MISMATCH` at `B15` |
| 115 | **no object attests itself, and the normative relation register is exactly `IR-13` — NOT `IR-4`, which is a non-exhaustive summary and states no complete graph.** A fixture in which any object carries its own digest or its own signature fails: the composite carrying its own `H_FILE`; the verifier carrying its own digest; the manifest carrying its own digest; the attestation attesting itself; Stage A carrying its own digest; Stage B carrying its own signature; the install record listing itself among its members. **This row asserts NO uniqueness of attester.** Version 1.2's wording — that every member is attested by the record "and by nothing else" — is WITHDRAWN as false. The fixture positively asserts EVERY edge of `IR-4`, and version 1.6's fixture omitted three of them: that `M4` carries the `M1` composite digest, the `M1` amendment digest by `peer_amendment_sha256`, the five root digests, the three composite region digests and the file digest, the three pre-selection path/digest pairs and the Stage-A binding; **that STAGE A ITSELF carries a path and a digest for each of the three pre-selection inputs — the packet, the amendment and the composite — which are three directed edges parallel to `M4`'s and which version 1.6's "complete" graph, its `§P1-14.5` summary, its packet summary and this row all omitted**; that the `M1` amendment carries the `§A0.4` anchor line binding the pre-selection composite bytes; that `M7` carries the `M5` digest, the two `M6` digests and the bundle digest; and that the record carries all 69 member digests; **and that Stage B carries the `selected_option_token` equality edge to Stage A enforced at `B14`.** A build in which Stage B does not carry that equality fails this row. **This row is audited against `IR-13`, not against the `IR-4` diagram, and in version 1.10 `IR-13` is the FIFTY-row cross-object and external integrity-binding register whose inclusion rule `K1`..`K5` and exclusion rule `K6`..`K8` it states exactly.** A build omitting any of the fifty rows fails; a fixture asserting that the `IR-4` diagram, the `§P1-14.5` summary or any other reduced view is COMPLETE **fails this row**, because all of them are explicitly non-exhaustive quotients and no sentence of this pair calls any of them complete; **a fixture asserting that `IR-13` is exhaustive over "all validator predicates" or over a LIST OF SECTIONS also fails this row**, because it is exhaustive over the `K1`..`K5` relation class and over nothing else; **a fixture asserting that a `K6`, `K7` or `K8` predicate — `A6`'s author literal, `A7`'s and `B10`'s algorithm literal, `A11`'s intra-object `key_id` derivation, `B7`'s `member_count` literal, or any `VP-1` `S1`..`S8` admissibility predicate — is a row of `IR-13` fails, and so does one asserting that any of them has ceased to refuse at its owning clause**; and a fixture asserting a unique attester, or a unique EXTERNAL attester, still fails. A build in which any of those edges is ABSENT fails this row; a fixture presenting a Stage A whose `governing_pre_selection` omits the packet entry fails; and a fixture asserting a unique attester, or a unique EXTERNAL attester, also fails |

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
record was created. **No key pair, no entropy, no Stage-A selection artifact, no
Stage-B authorization artifact and no detached signature was generated,
requested or predicted**; the two-stage protocol of `TS-1`..`TS-6` is specified
and is authorized by nothing here. **The signed process-claim identity selection
recorded at `XS-1` is control-plane author state**: it is a member of no class,
enters no acceptance predicate, is no covariate, endpoint, qualification input,
Q or C fact, and unblocks neither author cell — its own bounded-weakening token
remains unaccepted. **`G-11` verifies a final byte state and reconstructs no
history** (`FS-1`, `FS-2`); the residual it does not close, including complete
coherent rollback of an earlier valid generation, is stated at `TR-2` and is an
infrastructure fact, never scientific evidence. The install record, when created, is a generated
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

**THIS REGION IS NOT THE SOURCE OF `M2`.** `M2` is the **literal 55-path list at
§P1-14.4 `MS-2`** and is constructed from that list alone. This region carries
63 rows: the 55 `M2` members, the 7 `M3` members, and the one non-enforced
verifier baseline. Adding a row here does not add a member to any class, and
removing one does not remove a member. **This is the structural repair of the
v2.4 defect in which `M2` was defined as this region minus one exception and
therefore overlapped `M3` on seven paths.**

**ONE FILE HERE IS A BASELINE AND IS ENFORCED BY NOTHING:
`src/philosophia/officina/verification.py`.** Its digest below is a
**NON-ENFORCED PRE-INSTALL BASELINE**. It records what the verifier was before
the handoff and is evidence of derivation only. It is **not** in `MS-2`'s list,
is in no member class, and is compared by nothing. The verifier that `G-11` does
enforce is the POST-HANDOFF verifier at the same path, pinned as member `M5` by
`MS-5` with its own digest recomputed from disk. Without this separation the
gate would forbid its own installation: `G-11` requires every `M2` digest to be
exact, while `OR-5` requires the verifier bytes to change in order to implement
`G-11` at all. **The separation resolves that circularity.**

**The two live authority surfaces are NOT in this region.** They are P1
operative composite v1.10 — this file — and
`successor/OFFICINA_GENERIC_HARNESS_WATCHDOG_FREEZE_AUTHORITY_AMENDMENT_V1_7_DRAFT.md`,
accepted jointly and indivisibly per authority level 3a. **The v1.6 amendment
and composite v1.9 that this pair wholly replaces are NOT added to this region
and NOT added to `MS-2` by this round**, which is a bounded surgical correction
and not a generational round; `N-14` of the peer amendment names the four rows a
later generational round must add and states that this round adds none.

**One further file is deliberately NOT in this region and is a member of no
class:** the author choice packet named at `§P1-14.4` `TS-1` as the
pre-selection packet. `TS-2` `A16(b)` recomputes its digest from the bytes at
its literal path, which makes it a hash-read target of one clause and nothing
more. It is not provenance of this composite, not an `M2` row, not counted in
the 63, and supplies no path to `CK-4`.

**The four project-import dependencies of `§P1-14.4` `MS-13` are likewise NOT in
this region and are members of no class.** They are bound by digest inside the
`M4` manifest, which is itself a member; they are not provenance of this
composite, not `M2` rows, not counted in the 63, and supply no path to `CK-4`.

**One external author-state file is deliberately NOT in this region and is a
member of no class:**
`successor/OFFICINA_P1_PROCESS_CLAIM_IDENTITY_SELECTION_V1_SIGNATURE.md`,
digest `7a8ab2daefe9ad5d8d5bce74d7921a4fa600b44f17aa7a407acab26e472e3d1f`. It is
Kirill's signed identity Option A selection of 2026-08-04. It is recorded here
so that its digest is on record and nowhere else in these bytes; it is **not**
provenance of this composite, **not** an `M2` row, and **not** counted in the
51. §P1-14.4 `XS-1` states why it is not a member and what the later combined
binding must do with it. It is
not counted in the 63. The accepted
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
ec5ddff8f8d09c1574a56d173579a6b585a8f9de230afb86e43d9415fb7a4390  successor/OFFICINA_GENERIC_HARNESS_WATCHDOG_FREEZE_AUTHORITY_AMENDMENT_V1_1_DRAFT.md
c904ec4318485acd49a6128ca32f9e52fe523c3703b730351f8ad98adb3e60f1  successor/OFFICINA_GENERIC_HARNESS_SUPERVISOR_CONTROL_CHANNEL_P1_OPERATIVE_COMPOSITE_V1_4.md
bd8147a5085096c6a08ec0fec40ad22df23d55f23f77e3349218b3da93b6b2ba  reviews/fable_officina_p1_watchdog_v2_4_independent_x_confirmation.md
3fab1b09e2724534b2b5a080fbfeb98cc861cbe3b9764790084dfec050944a05  reviews/sol_officina_p1_watchdog_v2_4_final_y_confirmation.md
058c119c5de770dc537fd16962723063d2c3d4dad5da17d1431d4402927ebd1b  successor/OFFICINA_GENERIC_HARNESS_WATCHDOG_FREEZE_AUTHORITY_AMENDMENT_V1_2_DRAFT.md
8751317511a3f738de35402b3c67ab9786e7fe1c95ea12d1e175ddd6540ddb20  successor/OFFICINA_GENERIC_HARNESS_SUPERVISOR_CONTROL_CHANNEL_P1_OPERATIVE_COMPOSITE_V1_5.md
c2e9ddb2e6270f2b870986b01d1114ea68d5f3e1db466f165ee2f47a0f256427  reviews/fable_officina_p1_watchdog_v2_5_independent_x_confirmation.md
80d42229b2e9b32e51a5448c10af410640e2088f777334fa4431f29e4e840c81  reviews/sol_officina_p1_watchdog_v2_5_final_y_confirmation.md
c3da2a7d24d0cea025f014f9231c0b856318b4a4c11ffc40c66972e7f905b3d1  successor/OFFICINA_GENERIC_HARNESS_WATCHDOG_FREEZE_AUTHORITY_AMENDMENT_V1_3_DRAFT.md
6283d081df3eb3978bf963820859a5ebbf125689a4a3e249d3e85c1ca8d3d49d  successor/OFFICINA_GENERIC_HARNESS_SUPERVISOR_CONTROL_CHANNEL_P1_OPERATIVE_COMPOSITE_V1_6.md
e334d7e4a93979f07a8d651a1dd32039027d0536e2d6259ae5a6ec36dc09a363  reviews/fable_officina_p1_watchdog_v2_6_independent_x_confirmation.md
283666b75dc7fee8af7cde90ab761a734cc554aceca1f5b124c318d2ce8115b9  reviews/sol_officina_p1_watchdog_v2_6_final_y_confirmation.md
f845b98dcef0edc415420fec1103f7adad4f905c21380a0dddcba0d3b370b794  successor/OFFICINA_GENERIC_HARNESS_WATCHDOG_FREEZE_AUTHORITY_AMENDMENT_V1_4_DRAFT.md
5301f7e987b768cc3acd9641f6f00400a74b453773299cbd379473c7db569beb  successor/OFFICINA_GENERIC_HARNESS_SUPERVISOR_CONTROL_CHANNEL_P1_OPERATIVE_COMPOSITE_V1_7.md
4855020e522228eeb0625fba1efb78941bc547c124da2d1dbb754b548d3057cc  reviews/fable_officina_p1_watchdog_v2_7_independent_x_confirmation.md
0b33108e885fec97ab11e2de5c6ac3ba6ceeb8e98283bb29a09c70ce1c574780  reviews/sol_officina_p1_watchdog_v2_7_final_y_confirmation.md
28b57c47f89f775199095717111e37a4e588628aa64b2801812f30814711efd4  successor/OFFICINA_GENERIC_HARNESS_WATCHDOG_FREEZE_AUTHORITY_AMENDMENT_V1_5_DRAFT.md
6b867790707ae7999b31c1ad3dd56a1d4b195efd8f7a8b2bda4c2b065a352176  successor/OFFICINA_GENERIC_HARNESS_SUPERVISOR_CONTROL_CHANNEL_P1_OPERATIVE_COMPOSITE_V1_8.md
ddd6d63aac69a6e3003fe7880ac7e5cbfe9f74cdb64b6f1d0716750795d8e8e9  reviews/fable_officina_p1_watchdog_v2_8_independent_x_confirmation.md
88efa91dcb9142483cab6f832088ee3d19c51eb79ba20335deb84e005ea90a46  reviews/sol_officina_p1_watchdog_v2_8_final_y_confirmation.md
```

Every author closure accompanying the documents above is an untrusted
self-assessment and none is evidence for anything in this composite.

### Future edit surface

| Path | Permitted change | Status today |
|---|---|---|
| `scripts/officina_process_control_bootstrap.py` | the PCS and its protocol server | does not exist |
| `scripts/officina_role_bootstrap.py` | the four-role isolated entry | does not exist |
| `src/philosophia/officina/verification.py` | CHANGES 1 through 5 and rules `S-1` through `S-24b`, `G-1` through `G-9`, **`G-10`, `G-11` and the authoring discipline `AD-1`**, and nothing else. **The post-handoff verifier implementing `G-11` is expressly permitted and is REQUIRED by `OR-5`; it is pinned as member `M5` by `MS-5`, never by the baseline digest above** | present bytes are a **NON-ENFORCED PRE-INSTALL BASELINE** (see the provenance note) |
| `successor/officina/runtime_control/PRODUCTION_CALL_GRAPH.json` | the manifest of `MS-4`, at that exact path, with exactly that schema id, version and key set, canonically encoded | does not exist; **`MS-4`, not this row, is normative for it** |
| `tests/test_officina_p1_freeze_authority.py` | test-matrix rows 92..103 under the naming rule of `MS-6` | does not exist; **`MS-6` is normative for it** |
| `tests/test_officina_p1_install_integrity.py` | test-matrix rows 104..115 under the naming rule of `MS-6` | does not exist; **`MS-6` is normative for it** |
| `successor/officina/runtime_control/INSTALL/T_WATCHDOG_AUTHORITY_TEST_ATTESTATION_V1.json` | the `M7` attestation of `MS-7` | does not exist; **`MS-7` is normative for it** |
| `successor/officina/runtime_control/INSTALL/<install_record_id>.json` | the install record of `IR-1`..`IR-3` | does not exist; written LAST, at `OR-11` |
| `successor/officina/authorization/P1_WATCHDOG_FREEZE_SELECTION_V1.json` | the Stage-A artifact of `TS-1`, **created by Kirill only, after an explicit option token** | does not exist; **outside `M1`..`M7`**; **not authorized by this version** |
| `successor/officina/authorization/P1_WATCHDOG_AUTHORITY_INSTALL_AUTHORIZATION_V1.json` and its `.sig` | the Stage-B artifact and detached signature of `TS-3`, `TS-4` | do not exist; **outside `M1`..`M7`**; **not authorized by this version** |
| `src/philosophia/officina/generic_harness.py` | the launcher, the protocol client, the four role entries, removal of every subprocess, fork, wait, kill and group-kill call, and the eight single-install interface sites of §P1-13.7. **Its scoped allowlist is the sixteen names of §P1-3.2 after the `MS-11.5` reduction, and `MS-11.1` is the import-time closure that a conforming build must produce at `A-10`** | **does not exist as a tracked file.** A file of this name exists only as unrelated untracked work in the live worktree; it is not evidence, is not governing, is not adopted, and is not modified by this version |
| every other test module | §P1-15 rows 1..91 | untracked work in progress, preserved unmodified |
| everything else | no change | byte-unchanged |

**THE FOUR PROJECT-IMPORT DEPENDENCIES, AND WHY THEY ARE NOT IN THIS TABLE AS
ROOTS.** `src/philosophia/__init__.py`,
`src/philosophia/officina/__init__.py`,
`src/philosophia/officina/canonical.py` and
`src/philosophia/officina/interlock.py` are TRACKED FILES at the reviewed
commit, are necessarily executed by the `A-10` import before the role module,
and are bound by digest, import edge, execution order and the thirty-two
booleans of their four eight-key `import_time_effects` objects at `§P1-14.4`
`MS-13`. **They are not production
roots, not members, not rows of `MS-11.1`, and not covered by
`root_source_sha256`.** Their permitted change is: none, except through a new
independently reviewed generation, because any change to their bytes changes
`MS-13`, which changes `M1`.

**REPOSITORY STATE, STATED EXACTLY.** Of the five production roots of §P1-3.1,
**two exist as tracked files** — `scripts/officina_activate_t.py` and
`scripts/verify_officina_active.py` — and **three do not**:
`scripts/officina_process_control_bootstrap.py`,
`scripts/officina_role_bootstrap.py` and
`src/philosophia/officina/generic_harness.py`. No untracked working-tree file is
evidence for any claim in this document, is adopted by it, or is edited by it.
`MS-11.1` is therefore a **prospective conformance constraint** that future root
bytes must satisfy, and is **not** evidence that an implementation exists;
`MS-11.6` says so in the governing bytes.

**THIS TABLE IS NON-NORMATIVE AND SUPPLIES NO PATH TO ANY CHECK.** `CK-4`
enumerates members from `MS-1`..`MS-7` alone; it never reads this table, and a
row here can neither add nor remove a member. The v2.4 Y line found the manifest
and test-module paths available only here, in non-normative text; they are now
literal at `MS-4` and `MS-6` and this table merely echoes them. **The manifest's
complete schema, including the canonical `reachable_closure` shape, is `MS-4`;
its one admissible `reachable_closure` VALUE is the eighty-nine-row
`MS-11.1`, which covers the role import surface of all three scoped allowlists;
and the prose import-closure table at §P1-3.3 is a human-readable audit aid,
covers the PCS bootstrap root only, and is not a canonical value.**

<!-- OFFICINA-P1-PROVENANCE-END -->
