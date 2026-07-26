REVISE_OFFICINA_SUPERVISOR_CONTROL_CHANNEL_V1

# Officina supervisor/control-channel v1 — Y-line confirmation

## Critical findings

### C1. The stated same-UID information boundary and endpoint-role boundary do not exist

The draft explicitly acknowledges a same-user filesystem residual and relies on
directory modes plus post-worker `chmod 0000`
(`successor/OFFICINA_GENERIC_HARNESS_SUPERVISOR_CONTROL_CHANNEL_V1_DRAFT.md:347-367`,
:369-404). Those mechanisms do not exclude another process running under the
owning UID. After receiving `operation_id`, the controller knows the repository
root and can derive
`runtime_control/T_SUPERVISOR/operations/<operation_id>/`; it can inspect path
existence, entries, sizes, timestamps and logs, and as owner can restore
permissions and read output. A worker has the same underlying authority. The
statement that the controller has no “path grant” is therefore not a mechanical
boundary.

The global request FIFO has the same defect. The request authenticates a live
PID/start identity, not an endpoint role (:236-294). A controller or worker can
open `REQUEST.fifo`, create a correctly named reply FIFO, and identify itself
truthfully. Nothing in the byte protocol proves that its command originated
from an authorized CLI role. Conversely, `OPERATION_ADMIT` and
`OPERATION_STATUS` are listed in the common command enum even though controller
pipes are separately inherited. Descriptor custody does not revoke pathname
access available to the same UID.

This is a load-bearing contract defect, not an implementation test to defer.
The author must select and sign one concrete mechanical compartment and
endpoint-role mechanism. It must:

1. make operation output, worker logs, supervisor endpoints and other
   controllers' state unreadable and unmodifiable by controller/worker
   principals before settlement, including filesystem metadata that can encode
   a result;
2. authorize CLI commands and controller commands by the endpoint and durable
   process/claim binding, not by a caller-supplied live identity alone;
3. give workers no path to any control command; and
4. state the required process credential, namespace, broker, or equivalent
   kernel-enforced boundary and any resulting import/allowlist/control-file
   delta.

The amendment cannot simultaneously promise a same-UID adversary, ordinary
same-UID filesystem ownership, predictable paths, and mechanical secrecy merely
through mode bits. Choosing the replacement boundary is an author choice; it is
not available to Cursor.

### C2. Pre-settlement observables are not closed

The controller is permitted to learn `operation_id`, and the draft exposes or
leaves observable reply timing/status, operation-directory existence,
output/log file existence, file count, size and metadata, worker exit timing,
FIFO backpressure, and refusal timing/class. Several depend on worker execution
or output and can encode result direction or magnitude even if no result hash is
placed in JSON. The acceptance claim “no residual field, path, or timing
channel” is therefore false.

The bounded replacement must define the pre-settlement observation contract:

- permitted facts may be only request admission/refusal facts determined before
  behavior starts, a fixed-shape opaque operation handle, and a fixed closed
  pending response independent of worker progress and output;
- no output/log pathname or metadata is visible outside the compartment;
- pre-settlement status timing, response shape and refusal class cannot depend
  on output bytes, output count, worker-reported paths, learner state, worker
  exit reason, or a result-derived branch;
- promoted bytes and their already-settled binding become visible only after
  the signed charge, promotion and release transition; and
- invalid/process routing may expose only the already-signed closed process
  facts after the relevant durable terminal, never a result-bearing surrogate.

This need not claim that a human author is blind. It must mechanically prevent
the controller and worker from obtaining or signaling result information before
settlement.

### C3. Anti-replay is not durable idempotency, and token delivery is not total

The pair `(client_start_identity, client_monotonic_ns)` only rejects a duplicate
within one live supervisor generation (:267-294). A lost reply retried with a
larger monotonic value has a different request hash and is a new request. The
assertion that durable state makes all commands idempotent is unproved and false
for commands whose input includes a newly read clock/cursor or whose first
attempt may be between durable cuts.

Representative traces are:

- lost `CLAIM` reply: retry can attempt another spawn/claim;
- lost `START` reply: state may prevent a second start, but no durable reply
  identifies the first success;
- lost `HEARTBEAT` reply: retry may take a later cursor reading and charge or
  renew again;
- lost `CLOSE`, `PAUSE`, or `RESUME` reply: retry observes a later state and can
  refuse, create a second transition, or leave the caller unable to distinguish
  success from failure;
- lost `OPERATION_ADMIT` reply: retry changes
  `pre_operation_reading_ns`, hence `operation_id`, and may admit a second
  worker; and
- lost `OPERATION_STATUS` reply: in-memory consumption can make a promoted
  token permanently unavailable even though delivery was not observed.

Supervisor restart discards the replay table and every release token
(:395-404, :423-429). “Delivered exactly once” has no acknowledgement boundary.
A promoted-but-undelivered result is durable while its only release authority is
destroyed; a charged-but-unpromoted result is forced to quarantine, which is
conservative but does not repair request replay.

Add a durable, non-result-bearing request journal with a stable idempotency key
and exact phases. The same key plus byte-identical semantic request must resume
or return the same closed reply; reuse with different bytes is invalid. The
journal must bind the expected pre-head, process/lease, command, generation
handoff rule, durable transition/event identity, and reply class. It must cover
all eight commands. For release, specify a durable one-use redemption protocol:
either repeated delivery of the identical token until a durable acknowledgement
with one-use effect, or an explicitly fail-closed at-most-once rule with a
single signed recovery destination. Two supervisor generations must derive the
same continuation without inspecting output.

### C4. Spawn-before-stop and spawn-before-claim are behavior and recovery races

`subprocess.Popen` completes an exec before the parent sends `SIGSTOP`
(:105-134). The child can execute arbitrary behavior between exec and the
parent's stop. The resulting stopped window is not proven behavior-incapable or
free of E1 exposure. A child must enter a reviewed bootstrap that stops itself
before any behavior-capable import, input access, thread/backend initialization
or controller code, and the supervisor must observe `WIFSTOPPED` and the exact
identity before writing the claim. An equivalent kernel-enforced no-exec
handshake may be selected, but parent-after-exec `SIGSTOP` is insufficient.

The draft also admits that a crash between spawn and durable claim leaves an
unrecorded child that takeover cannot identify and assigns it to “the operator
route or dies at boot” (:123-134). That is neither deterministic recovery nor a
closed process terminal. Add a durable spawn intent before creation, binding a
unique discoverable process/session identity and exact kill-before-admission
continuation, or an exact parent-death/no-escape mechanism. Recovery may not
guess, wait for reboot, or use operator discretion.

Finally, the double-forked supervisor closes inherited descriptors, including
the spawn lock unless a different lifecycle is stated (:71-103). If the
spawning CLI dies before the identity record is installed, a second CLI can
start a second generation while the first grandchild is still initializing.
The chosen protocol must keep a generation-unique lock or equivalent durable
startup claim through identity installation and for the serving lifetime, with
an exact handoff/takeover rule.

### C5. A serial loop cannot supply the stated watchdog deadline guarantee

The firing arithmetic at :157-185 is correct only if loop latency is itself
bounded. The same serial process performs request validation, filesystem I/O,
fsync-like durable transactions, process creation/reaping, backend
synchronization, settlement and archival. A long request or blocking operation
can occupy it beyond 100 ms. Nonblocking FIFO I/O alone does not prove the
watchdog initiates action at or before the deadline.

Select one exact topology that makes the guarantee true: a separately scheduled
watchdog/control component with a closed handoff, or a rule that no unbounded or
blocking operation begins while a live liability exists unless the relevant
processes have first been revoked/quiesced and conservatively settled. The rule
must cover lock wait, filesystem and Git operations, backend synchronization,
process waits and settlement. This topology choice requires author acceptance;
it is not an ordinary implementation detail.

## Major findings

### M1. The byte protocol is not exact

The six CLI command argument schemas are referred to as their “signed CLI
arguments” but are not enumerated, and `OPERATION_STATUS` has no exact argument
schema. `input_spec` is described only as a closed object, without its keys and
types. `detail` lacks an exhaustive status-by-command schema. Moreover,
`status` is declared to be only `OK`, `REFUSED`, or `INVALID` (:250-265), while
token delivery requires a reply whose status is `PROMOTED` (:395-400).

Mandatory repair: give an eight-row request schema and an exhaustive reply
matrix containing exact keys, primitive types, bounds, enum values and
`detail` variants. Either `PROMOTED` must be a closed `detail` variant under an
allowed status or the status enum must be normatively amended. No free text,
arbitrary mapping, result-derived refusal token or unspecified extension is
permitted.

### M2. FIFO encoding and I/O cuts are underspecified

`client_start_identity_hex` is not defined although the source identity contains
digits, a colon and a boot UUID. Pin the source byte encoding, lowercase hex
encoding, component length and full path-length bound. At endpoint creation,
verify `fpathconf(fd, PC_PIPE_BUF) >= 4096`; do not assume the platform value.
Require one `write` call for a complete frame and define partial write/EAGAIN as
no action plus a closed retry state. Define bounded read buffering across
writers.

The client must open its reply FIFO read end nonblocking before publishing the
request; the supervisor must open/write it nonblocking. Otherwise open order can
deadlock or return `ENXIO`. Every endpoint component needs directory-descriptor,
no-follow, inode/type and ownership validation before use.

### M3. Worker-supplied output paths are not a safe manifest

`output_relative_paths` is an unrestricted worker field (:347-358). Add exact
canonical relative-path grammar, unique deterministic ordering, maximum
count/depth/total bytes, and rejection of empty, absolute, dot, `..`, duplicate,
symlink, hard-link, device, FIFO and socket cases. Hash by descriptor using
directory-relative no-follow traversal after the worker and its group are
proved dead; require regular single-link files wholly beneath the operation
root. Any bounds not already owned by a signed envelope are bounded author
cells, not Cursor choices.

### M4. Multi-stream ownership needs a closed table

Section S4 correctly carries known/unknown and all-live settlement semantics,
but “`device_units = k` implies `k` declared streams” is not enough to prevent
two concurrent operations from naming the same stream or omitting a live
stream. Define canonical stream indexes, the exact claim table, sorted unique
nonempty operation subsets, exclusive live ownership, release points, and
per-stream adapter readings. For `device_units > 1`, every stream must be
measured or conservatively unknown and the all-live batch must use the complete
frozen live set.

### M5. The 60-second idle exit adds an unresolved generation cut

Exit is allowed in G1/G2 after 60 seconds (:95-103), but the protocol does not
define a drain state relative to clients that have read the identity, opened
FIFOs, or are about to publish a request. It also discards the generation replay
table. Either remove idle exit or define a closed drain handshake: cease new
admission, resolve or refuse every opened/pending request, unlink endpoints only
after the generation lock proves no eligible client remains, and give stale
clients one deterministic no-action result. Exit must remain impossible with a
live lease, pending request/operation, unresolved batch/recovery/request journal
or frozen claim. Retaining versus removing this avoidable lifecycle is an
author choice.

## Minor findings

1. Deterministic endpoint and operation identifiers introduce no entropy and
   are acceptable only after the access and observation boundaries above are
   mechanically closed. Determinism itself is not authentication or secrecy.
2. The carried S4/S6 rules are directionally exact: author/authorization
   parents, pre-review-head acyclicity, strict integers, private claim-backed
   batch authority, D1 raw-head completion, archival-before-resolution and G5
   epoch ownership remain required
   (`successor/OFFICINA_GENERIC_HARNESS_SUPERVISOR_CONTROL_CHANNEL_V1_DRAFT.md:435-450`,
   :480-537). No new scientific or resource cell is needed for those carried
   obligations.

## Direct answers to Fable's Sol questions

1. **No.** Section S2 is not Y-line closed. Same-UID pathname authority,
   self-asserted endpoint identity, worker/log metadata, status timing,
   incomplete schemas, nondurable replay and ambiguous release delivery leave
   concrete pre-settlement information and mutation paths.
2. **No.** The signed claim can validly carry the observed PID/start
   identity/PGID/argv without a schema change, but `Popen` followed by a parent
   `SIGSTOP` does not establish a behavior-incapable interval. The
   pre-claim-crash branch is also not total. A self-stop-before-behavior
   handshake and durable spawn/takeover binding are required.

## Attack disposition

| Case | Disposition |
|---|---|
| Controller derives output/log path | Concrete bypass under the same UID; C1/C2 repair required. |
| Controller/worker opens global FIFO | Concrete unauthorized command path; live PID identity proves identity, not role. |
| Pre-settlement observables | Only pre-input admission/refusal and an opaque handle may remain; all worker/output-dependent fields, metadata and timing require confinement. |
| `output_relative_paths` | Unsafe until M3 grammar, bounds and descriptor hashing are normative. |
| Eight command schemas/replies | Incomplete; `PROMOTED` contradicts the status enum. |
| Start-identity/path encoding | Undefined; M2 repair required. |
| `PIPE_BUF`, partial/EAGAIN/open order | Assumed rather than proved; M2 repair required. |
| Lost-reply retries | Not exactly once for any mutating command without C3's durable idempotency journal. |
| Supervisor restart/token state | Replay and token state are lost; continuation is not total. |
| Numeric E1 counter to G7 | Correctly forbidden by S4/S6: G7 must remain event/record/archive backed. |
| Invalid cap-consuming batch | Correctly remains G5; numeric resource facts persist and no valid exhaustion event is fabricated. |
| Stream subsets/concurrency | Intent is present, but the closed ownership table is missing. |
| Watchdog/heartbeat/close/process loss | Must enter the same full-live frozen batch; carried S4/S6 rule is acceptable, topology guarantee is not. |
| Decision parents/D1/archive/G5 | Carried correctly and must remain unchanged. |
| Parent-after-exec stop | Concrete behavior window; C4 repair required. |
| Crash before durable claim | Undiscoverable child; “operator route or boot” is not valid recovery. |
| Double-fork generation race | Lifetime ownership of the spawn/generation lock is incomplete. |
| 100 ms watchdog promise | False while the serial loop can block; C5 repair required. |
| 60-second idle exit | Non-scientific but adds unresolved request/replay/takeover cuts; M5 author choice required. |

## Required bounded repair and author boundary

One further bounded contract correction is required before implementation. It
must contain, and no implementation may choose:

1. the kernel-enforced result compartment and endpoint-role authorization;
2. the closed pre-settlement observation contract;
3. exact eight-command request/reply schemas and FIFO byte/I/O rules;
4. durable idempotency and release-redemption state across generations;
5. self-stop-before-behavior, durable spawn intent, takeover and singleton-lock
   lifecycle;
6. a watchdog topology that actually bounds scheduling while liabilities are
   live;
7. the safe output-manifest grammar and bounds;
8. the canonical multi-stream ownership table; and
9. removal of idle exit or its exact drain protocol.

Another author choice is required for the load-bearing isolation/role-auth
mechanism, watchdog topology, and idle-exit disposition. Those choices are
engineering/control choices, not scientific endpoints or outcomes, but they
alter the promised threat model and process topology. After a corrected,
author-selected draft, another bounded X/Y confirmation is necessary.

The token

```text
I_ACCEPT_OFFICINA_SUPERVISOR_CONTROL_CHANNEL_AMENDMENT
```

is **not ready for signature**.

## Verification and negative space

I verified the candidate commit and both supplied SHA-256 hashes, re-read the
signed composite and the Codex, Opus and Sol implementation reviews cited by
Fable, checked that the post-candidate HEAD adds only the two review prompts,
and ran `git diff --check` over that prompt-only delta. No inspected source was
executed and no Officina test process was started.

This review created only this review file. It created no code, activation,
supervisor, controller, worker, FIFO, process, entropy, runtime artifact,
production manifest, capability, claim, lease, batch, operation, promoted
artifact, E1/E2/E3 spend, world, candidate, Q/C object, datum, outcome or claim
movement. The committed envelope remains `activated:false`
(`NOT_ACTIVATED`), the production manifest remains absent, and
`successor/officina/runtime/` contains only `T_RUNTIME.lock`.
