# Prompt for Claude Code Opus 5: Officina supervisor v2.1.10.2 PCS transport repair

Act as the **specification author**. Do not request X/Y review yet. v2.1.10.1
fixed the launcher but made the Process-Control Server (PCS) normative without
specifying an implementable descriptor transport or operation protocol. Produce
one bounded transport correction over v2.1.10 + v2.1.10.1.

Work in `philosophia` at or after commit
`2660a056e0434c6ff433066c0c43a9e885d71bc1`. Existing files are immutable.
Recompute:

```text
2d4d4b189e460605ce95f8f464d7ef1c6d0c8ce317ad26033a91b4d2c556759b  successor/OFFICINA_GENERIC_HARNESS_SUPERVISOR_CONTROL_CHANNEL_V2_1_10_1_CORRECTION.md
f7a866f9100cae1abf80623cd6a7d689cbdca1001fb33dffe98966a727582008  reviews/opus5_officina_supervisor_control_channel_v2_1_10_1_closure.md
```

Static authoring only. Run no code, tests, spawn/socket/fork/signal experiment,
or Officina process. Change no implementation, verifier, activation, entropy,
T/Q/C object, datum, claim, or prior document. Create only the two deliverables.

## Blocking defects

### T1 — byte pipes cannot transfer file descriptors

The PCS operation table says the supervisor supplies a `ctrl-fd pair` and
watchdog pipe descriptors over the existing pipe wire. Descriptor integers are
process-local; writing them to an anonymous pipe transfers no capability. No
`SCM_RIGHTS`, proxy, preallocation or other mechanism exists. Therefore
`SPAWN_ROLE` and `SPAWN_WATCHDOG` are unimplementable.

Choose exactly one real transport. Preferred route: a clean-PCS-created
`AF_UNIX` `SOCK_SEQPACKET` control channel with `SCM_RIGHTS`, using a minimal
audited built-in import surface such as `_socket` plus `array` (or an equally
small exact packing mechanism). The PCS must create the supervisor channel
before spawning the supervisor and pass one endpoint by inheritance. Every
later descriptor transfer must use ancillary data, never numeric fd fields.

Specify exactly:

- socket type/protocol, creation owner, endpoint fd numbers and inheritance;
- `sendmsg`/`recvmsg` calls, ancillary tuple layout, integer packing/native
  endian rule, `CMSG_SPACE`/`CMSG_LEN`, `MSG_CMSG_CLOEXEC`, truncation flags,
  credentials if any, and maximum frame/descriptor counts;
- the only legal fd-count and fd-type vector for each operation/result;
- sender/receiver ownership before send, after successful send, after ack,
  timeout, duplicate, malformed packet, peer death and PCS death;
- closing every received extra/unknown fd before invalidity routing;
- no fd leak or double close at any crash cut.

If you select proxying or fixed preallocation instead, make the data plane and
slot/generation reuse bit-exact; do not leave a design alternative.

### T2 — the old one-operation grammar cannot carry nine operations

v2.1.10's original request had a fixed six-field
`SPAWN_SUPERVISOR`-only schema. v2.1.10.1 says nine operations are “added” while
the record grammar/field classes/framing remain unchanged. That is false.

Define a fresh versioned PCS protocol, not a prose extension:

- one closed request and one closed response variant per operation;
- exact ordered fields, byte grammar, bounds, ancillary-fd vector and semantic
  preconditions;
- generation id, monotonically unique request/operation id, handle id where
  applicable, and response correlation;
- partial read/write impossibility or exact handling under the selected socket
  type;
- duplicate request, duplicate response, ack loss, redelivery and replay rules
  integrated literally with the signed B1 journal/idempotency choice;
- request → durable journal → syscall → durable result → response → ack order,
  including every crash cut;
- unknown opcode/field/handle/state and out-of-order operation routes;
- clean shutdown and EOF semantics.

No free text, path, PID, arbitrary argv, signal number, callback, code name or
unbounded integer may cross the protocol. The supervisor still receives opaque
handles, never PIDs.

### T3 — role execution reintroduces startup contamination

The role exec uses only `-P` and sets `PYTHONPATH=/proc/self/fd/8`. It therefore
enables system/user `site`, `.pth`, site/user customization and environment-like
path injection again. That contradicts the stated process isolation, even if
the role holds no numeric PID authority.

Construct an exact isolated role entry. Preferred route: a second minimal,
object-bound root such as `scripts/officina_role_bootstrap.py`, executed with
the same `-I -S -E -P`, empty environment and fd-bound interpreter/source. Its
reviewed first-stage code may insert exactly the object-bound source directory
into `sys.path` and import exactly the role module/token only after validating
all inherited fds and manifest identities. Pin its imports, transitive closure,
source hash, argv, role enum, path insertion, package import and refusal order.

Controllers, workers, supervisor and watchdog must all enter through a declared
isolated role surface or be explicitly proved unable to affect process,
capacity, custody or scientific validity. `PYTHONPATH` must not be used with
`-I`/`-E` and must not remain as the hidden workaround.

### T4 — PCS lifetime and fd/custody totality

Make the long-lived PCS architecture total:

- exact process and fd tree for caller, PCS, supervisor, watchdog, controller
  and worker;
- which process owns each pipe/socket endpoint and role fd at every state;
- how the PCS creates role ctrl pipes, transfers the supervisor endpoints and
  inherits the role endpoints;
- how handles bind pid/start identity/pgid/role/generation/fd bundle/state;
- how the signed lease, claim, spawn-intent, watchdog and B1 journal map to the
  PCS handle without changing their scientific meaning;
- PCS crash: init adoption, live roles, journal state, lock/record disposition,
  whole-run invalidity and prohibition on unsafe PCS restart/adoption;
- supervisor crash/channel EOF, caller crash, watchdog crash, role crash,
  shutdown with live handles, and resource-stop paths;
- exact invalidity dominance and `NO_REPLY` routing without inventing a success
  or resource fact.

Do not say “relocate the primitive, preserve semantics” unless every carried
primitive has a named PCS operation and every response has a unique carried
consumer.

### T5 — clean import and primitive surface after transport

Update the bootstrap import closure exactly. If `_socket`/`array` are added,
audit native/pure transitive imports, task creation, at-fork registration,
handlers and hooks. Retain `_signal`, not the Python `signal` wrapper. Update
the module-scoped verifier algorithm and manifest hashes, with exact positive
and negative fixtures.

Correct the read-only-fd check as well: use locally bound genuine
`fcntl.fcntl(fd, F_GETFL) & O_ACCMODE == O_RDONLY` (with exact constants and
identity rules), rather than relying on a zero-byte write as access-mode proof.

### T6 — launcher and object provenance must remain exact

Carry the fd-bound `/proc/self/fd/7` and `/proc/self/fd/8` mechanism and genuine
`posix_spawn` file actions. Reconcile the additional PCS/role socket and role
bootstrap fds with the hoist algorithm and collision proof. Pin interpreter,
bootstrap, role-bootstrap, package-root and production-root identity/hash
obligations. A wholly fabricated caller tree must not produce a response that
the reviewed harness accepts as authorized.

### T7 — governance boundary

B6 is larger than a wording repair. State explicitly whether the new PCS wire,
descriptor transport, handle table and isolated role root are:

1. a mechanical implementation of the already selected supervisor policies; or
2. a new architecture requiring its own signed engineering amendment/token.

Do not decide a scientific/resource value. If an author signature is required
for the expanded trust/control surface, emit
`BLOCKED_OFFICINA_SUPERVISOR_V2_1_10_2_AUTHOR_CELL` with the exact bounded choice
instead of declaring `READY`. If no token is required, prove why the existing
`I_ACCEPT_OFFICINA_SUPERVISOR_CONTROL_CHANNEL_AMENDMENT` truthfully covers the
whole PCS architecture after X/Y review.

## Required contents

Provide a literal v2.1.10.1 → v2.1.10.2 replacement index; complete wire and
ancillary schemas; fd/process/ownership tables; operation/state/idempotency
automata; import/primitive/verifier changes; isolated role-entry contract;
crash/cut matrix; platform scope; no-regression; exact future edit surface and
tests. State the weakest points against yourself, especially SCM_RIGHTS
portability, received-fd CLOEXEC behavior, PCS single point of failure and
protocol/journal coupling.

## Deliverables

Create exactly:

1. `successor/OFFICINA_GENERIC_HARNESS_SUPERVISOR_CONTROL_CHANNEL_V2_1_10_2_CORRECTION.md`
2. `reviews/opus5_officina_supervisor_control_channel_v2_1_10_2_closure.md`

Closure line 1 exactly one of:

- `READY_FOR_OFFICINA_SUPERVISOR_V2_1_10_2_FINAL_XY_CONFIRMATION`
- `BLOCKED_OFFICINA_SUPERVISOR_V2_1_10_2_AUTHOR_CELL`
- `BLOCKED_OFFICINA_SUPERVISOR_V2_1_10_2_CONTRACT_CONFLICT`

Use `READY` only for one bit-exact implementable protocol. Ask each line at most
three bounded questions. Confirm no code/test/run, implementation, activation,
entropy, T/Q/C, datum, outcome or claim movement; T `NOT_ACTIVATED`, claim
`OPEN`, amendment token unavailable.
