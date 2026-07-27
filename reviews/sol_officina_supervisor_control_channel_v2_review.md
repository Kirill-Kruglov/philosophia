REVISE_OFFICINA_SUPERVISOR_CONTROL_CHANNEL_V2

# Officina supervisor/control-channel v2 — Y-line review

## Critical findings

### C1. B1 is not generation-total and its durable effect automaton is not representable

The v2 frame hashes the complete request, including
`supervisor_generation_sha256`, client identity, monotonic freshness and reply
FIFO
(`successor/OFFICINA_GENERIC_HARNESS_SUPERVISOR_CONTROL_CHANNEL_V2_DRAFT.md:299-325`).
The journal then accepts a retry only when that complete
`request_sha256` is byte-identical (:371-407). A retry after takeover must name
the new generation and normally has a new client PID/start identity, monotonic
value and reply endpoint. It therefore has different bytes and is routed to
`REPLAY_BYTES`, despite being the exact B1 retry the journal is supposed to
complete. Keeping the old generation bytes instead produces a
`STALE_GENERATION` refusal. Thus no permitted frame can perform a
generation-total retry.

The reply has the same contradiction. Its generation and `request_sha256` must
change after takeover, so the whole reply cannot remain byte-identical.
What can remain identical is the cached semantic effect reply
(`status`/`detail`, including release-token bytes), carried in a fresh,
current-generation delivery envelope.

There is a second representation contradiction. Section V2.3 says every
control-plane JSON is atomic no-replace unless noted (:258-276), but the one
journal pathname is required to change
`ACCEPTED -> COMMITTED -> REPLY_CACHED`. No replacement or immutable phase-file
layout is specified. More importantly, `ACCEPTED` contains no deterministic
effect locator. If the underlying effect becomes durable before `COMMITTED`,
takeover cannot safely decide between resuming and reapplying:

- a claim may exist without the journal naming its spawn intent or claim;
- a start, heartbeat, close, pause or resume may have one or more ledger and
  artifact steps after the saved pre-head;
- an admitted operation may already own its first meter cursor, output bound,
  worker or charge, while `ACCEPTED` has no `operation_id`; and
- `effect_event_sha256_or_null` plus one
  `effect_artifact_sha256_or_null` cannot describe the multi-artifact close,
  pause, resume, admit or promotion automata.

The assertion “resume effect from phase” in the crash matrix (:666-686) is
therefore not derivable from the journal bytes.

**Mandatory bounded repair.**

1. Define a `semantic_request_sha256` over exactly the stable command,
   canonical arguments, idempotency key and durable authorization scope.
   Explicitly exclude transport generation, current peer PID/start identity,
   monotonic freshness and reply path. Every delivery must still authenticate
   those current transport fields. A journal hit compares the semantic hash;
   changed semantic bytes are `REPLAY_BYTES`.
2. Cache immutable `effect_reply` bytes. A takeover re-wraps those bytes in a
   fresh reply envelope containing the current generation and current transport
   request hash. B1 “identical reply” means identical effect-reply and token
   bytes, not an impossible stale transport envelope.
3. Replace the mutable one-file phase with an exact immutable predecessor-bound
   layout, for example one no-replace record per `ACCEPTED`, `COMMITTED` and
   `REPLY_CACHED` phase. Give every phase a predecessor hash and directory
   fsync rule.
4. Add an eight-row recovery reducer. At `ACCEPTED`, each command must already
   bind a deterministic effect plan/locator; takeover must prove from the
   authoritative ledger, head, state and named control artifacts whether the
   next unique action is apply-first-step, finish-existing-step, cache-reply or
   remain blocked. No scan by approximate time/arguments and no second effect
   is allowed.
5. Specify how each CLI/controller obtains and durably retains its retry-stable
   key before first send. The present CLI tables expose no key input and a
   short-lived retry process cannot regenerate a PID/clock-derived key across
   takeover. Key allocation may not introduce entropy or a ninth scientific
   action.

These are mechanical completions of signed B1; B1 itself is not reopened.

### C2. Acknowledgement, token redemption and journal retention are internally inconsistent

`OPERATION_STATUS` has arguments `{operation_id, ack_delivery}` (:338-346).
A first request with `ack_delivery=false` and a later acknowledgement with
`ack_delivery=true` cannot reuse the same idempotency key because its bytes and
semantic arguments differ. Reuse is `REPLAY_BYTES`; using a new key does not
identify which prior token delivery is being acknowledged. If
`ack_delivery=true` writes the ack before sending the token, a lost reply is
mistaken for observed delivery and B1 redelivery is defeated.

The draft also offers two incompatible ack objects (“`t-request-ack.v1`” or a
dedicated delivery ack), gives no exact schema or transport for ordinary reply
acks, and omits `ALREADY_DELIVERED` from the purportedly exhaustive
`OPERATION_STATUS` phase set while using it in the same row. Journal GC requires
an ack, but no command can acknowledge the other seven command replies.
Deleting a journal would also make its idempotency key reusable unless a
permanent tombstone remains. Retaining every polling status key forever is
unbounded because `OPERATION_STATUS` polling itself spends no E1.

**Mandatory bounded repair.**

- Separate request-effect acknowledgement from release delivery redemption.
  A token-returning STATUS request has one stable key and redelivers the same
  token. Only after observing and validating it may a distinct acknowledgement
  frame/request name the original delivery key, original effect-reply hash,
  `operation_id` and release-token hash. The ack transition is durable before
  `ALREADY_DELIVERED`.
- Pin exactly one ack schema/path/protocol for all replies and one exact
  delivery-ack schema; do not leave “or a dedicated” alternatives.
- Add `ALREADY_DELIVERED` to the closed status result or represent it as a
  separate closed delivery state, not an undeclared operation phase.
- Define a bounded status protocol. It may use one pending request through the
  terminal rather than unbounded polling, or another exact finite rule, but it
  may not grow an unlimited journal outside E1/E2/E3 accounting.
- GC may remove detailed records only after the signed conditions and must
  retain a compact immutable used-key/semantic-hash tombstone, or an equivalent
  permanent replay proof. No TTL, outcome-derived pressure, or success-
  conditioned deletion is allowed.

### C3. The output-bound protocol is circular and does not bound host or quarantine use

The only authorized input carrying `max_total_output_bytes` and the proposed
bound hash is `OPERATION_ADMIT`, yet the supervisor requires `BOUND.json` to
exist before that command and says the controller supplies the value “after
bound install” (:338-346, :497-522). The file is located below an undefined
`<pending_op_key>`, while the final `operation_id` cannot be computed until the
bound, its hash and the first meter cursor exist. No authorized command can
create the prerequisite without either a controller writing supervisor control
state or an undeclared extra command.

A positive caller-selected integer is also not an aggregate resource bound.
Four arbitrarily large positive integers remain arbitrarily large. Recording
`bytes_reserved` does not create disk capacity, and that field is absent from
the exact admission schema. Enforcement only after the worker exits permits the
worker to exhaust storage first. Worse, an oversized tree is quarantined but
its reservation is released at `FAILED`; retained quarantine bytes then consume
unaccounted storage while later operations reserve the same capacity again.
Logical/allocated checks and sparse-file treatment are individually correct,
but too late to establish the claimed resource guarantee.

`FAILED` is itself undefined. There is no closed failed-record schema or path;
the journal phase enum contains only request phases, and `OPERATION.json` is
no-replace, so “`phase=FAILED` journal/admission update” cannot occur. Nor does
the draft say whether bound excess, unsafe output, worker failure or hashing
failure produces the signed process invalidity/G5 route or permits the lease to
continue. A control-plane `FAILED` label cannot replace the signed
record-first invalidity terminal.

**Mandatory bounded repair.**

1. Make `OPERATION_ADMIT` itself the sole creator transaction: after the
   journal's immutable accepted plan, the supervisor writes `BOUND.json`, then
   captures the meter cursor, derives `operation_id`, and writes
   `OPERATION.json`, all with exact pending-key-to-operation-directory binding.
   No controller/worker writes either artifact and no ninth command exists.
2. Add one outcome-independent hard aggregate capacity policy enforced before
   behavior and at write time, not merely checked afterward. It must bind the
   total of live reservations and retained quarantine. The policy may be a
   fixed total byte envelope or an exact deployment quota/preallocation
   mechanism, but its value/provider, failure rule and concurrency accounting
   must be selected before implementation.
3. Quarantined bytes continue consuming the reservation until the signed
   disposal/archive action actually removes or transfers their accounted
   custody. A `FAILED` label alone never releases capacity.
4. Define the closed failed-operation artifact and map every failure class to
   one existing signed process/global route. Unsafe/excess output with a valid
   clock is a process invalidity unless a more-precedent independently verified
   HASH/FILESYSTEM/CLOCK/RESOURCE cause exists; it must use the all-live
   invalidity batch, G5, record-first ordering and no valid exhaustion/stop
   event. No live process silently resumes after an invalid operation.
5. Add component/full-path and encoded-status-frame length bounds. Retain the
   existing no-follow, regular-single-link, logical-plus-allocated, sorted
   bounded-chunk and no-content-hash-on-excess rules.

The aggregate output-capacity/quota policy is one additional bounded author
choice foreshadowed by the author-choice packet's “hard byte cap” note. No
numeric value or mechanism is selected in this review.

### C4. Watchdog registration and freeze evidence can understate or invent the controlled interval

The live lease is installed, the capability constructed and the controller
continued in V2.1.4 (:160-166), while the watchdog table is updated and acked
only “after” claim-start/renew in V2.6.3 (:430-443). The text does not require a
current table acknowledgement before `SIGCONT` or behavior admission. A crash
or delayed update therefore leaves a behavior-capable stream absent from the
freezer's table.

The freeze timestamp is sampled immediately after sending `SIGSTOP`, before all
members are proved stopped (:445-464). Signal send completion is not whole-tree
quiescence. A still-runnable member may be killed later, yet the earlier
`freeze_ns` controls overrun classification and charging. This can understate
the interval or turn an actual positive overrun into a nominal zero. If the pipe
event is lost, a later observation that the group is stopped/dead cannot
reconstruct the earlier stop time at all; calling that time “re-derived” is
false.

Finally, `PROCESS or CLOCK` is not one closed deterministic public cause
(:466-479). Fixed precedence chooses among facts already established; it does
not decide which fact an ambiguous scheduling delay represents.

**Mandatory bounded repair.**

- Before the first `SIGCONT`, capability usability or operation admission, the
  supervisor must durably publish a table containing that lease and receive the
  matching `table_seq` ack. On renewal, the old watchdog deadline remains
  authoritative until the successor table is acked; no unacknowledged update
  extends behavior.
- `freeze_ns` must be the conservative monotonic observation at which every
  declared process-tree member and backend stream is proved stopped/dead and
  synchronized, not the signal-send time. Unknown membership or delayed proof
  forces kill/lost-stream conservative settlement.
- A lost freeze event cannot recreate its timestamp. Record a separately typed
  later conservative observation or route directly to the signed unknowable/
  process-invalid recovery. Never synthesize an earlier `freeze_ns`.
- With a valid monotonic clock, a positive confirmed watchdog overrun has
  public cause `PROCESS`. `CLOCK` applies only to a separately verified clock
  failure/non-monotonicity; other co-observed causes follow the existing fixed
  precedence. This is a mechanical mapping, not a new cause or author choice.
- Every positive or unknowable overrun follows the all-live record-first
  invalidity route, retains the full conservative E1 charge and numeric E1/E3
  facts, creates no valid close/exhaustion/review terminal, and authorizes no
  automatic retry, scheduling tweak or device switch. Platform scheduling
  variability is transparent process validity, not a tunable scientific cell.

### C5. Pre-claim takeover and singleton creation remain unclosed

The pre-child spawn intent has no PID, start identity or PGID
(:124-158), yet takeover claims it can kill a stopped child “by registry
identity” (:183-195). The exact atomic no-replace schema cannot later acquire
that identity. A supervisor crash after `Popen` and before the claim therefore
still leaves an unidentifiable stopped child.

The CLI alone holds `SPAWN.lock`, while the grandchild explicitly closes its
copy before installing the identity (:86-108). If that CLI dies during
initialization, the lock is released while the first grandchild remains alive
but undiscoverable; a second CLI can spawn another supervisor. The claimed
singleton is not total under the very crash cut it must govern.

Add an exact pre-behavior child binding mechanism whose durable identity is
discoverable even if the supervisor dies at every spawn cut. The child may not
run behavior until that binding is durable. Add a supervisor-held generation
startup/lifetime lock or an equivalent durable handoff that survives spawning
CLI death and makes a second generation impossible. Also pin the reviewed
controller bootstrap/module mode that self-stops before behavior: the allowed
implementation surface presently names internal supervisor/watchdog modes but
no controller bootstrap mode. These are mechanical repairs; they do not reopen
A3/B1/C1/D1.

## Major findings

### M1. Official status and role paths still leak or misclassify under A3

A3 is now honest about deliberate same-UID inspection and does not promise a
kernel compartment (:206-229). That genuinely closes the v1 mode-bit
overclaim. It does not, however, authorize the official channel to reveal
worker-progress timing to a contract-following controller.
`OPERATION_STATUS` exposes `ADMITTED`, `RUNNING` and
`PENDING_SETTLEMENT`, although V2.2.3 promises fixed pending shapes. The
transition time between those values reveals worker exit/progress before
settlement. Collapse every preterminal response to one fixed `PENDING` detail
whose construction and reply path do not branch on worker output, path count,
size, exit reason or intermediate operation phase. `PROMOTED` becomes visible
only after commit; `FAILED` only after the complete signed invalid terminal is
durable.

The FIFO peer rule rejects only PIDs directly registered as controller, worker
or watchdog (:231-242). A controller can spawn an unregistered child in its
process group and that child is not one of those PIDs. Mechanical role checking
must reject every member/descendant of a registered controller/worker group,
not merely the leader. A deliberate same-UID escape into a new untracked
session remains within signed A3's procedural residual; the contract must say
so rather than claim stronger endpoint authentication.

### M2. Several declared “exact” schemas still have missing states or fields

The correction must resolve these local inconsistencies:

- `ALREADY_DELIVERED` is used but absent from the exact phase enum;
- `bytes_reserved` is required but absent from the admission schema;
- no `FAILED` artifact schema/path exists;
- `t-request-ack.v1` has no exact keys;
- an operation's admission/control records do not bind the idempotency key or
  semantic request hash needed for C1 recovery;
- the spawn intent cannot bind its later child identity; and
- output path component/full-path/frame lengths are not bounded.

Every added value remains a control/T-development field with recursive
scientific-field rejection and strict non-bool integer validation. No signed
runtime event/schema may be changed.

## Eight-command B1 trace

| Command | Lost request | Effect durable before journal commit / lost reply | Takeover/retry under v2 | Required closure |
|---|---|---|---|---|
| `CLAIM` | No parsed frame, no effect; same semantic key may retry. | Child/claim may exist without a journal effect locator. | New generation bytes become `REPLAY_BYTES`; otherwise a second spawn is possible. | Bind key to spawn intent and claim; reducer returns the one claim/reply. |
| `START` | No effect. | Start event may exist without lease or reply cache. | Full request bytes differ; blind start can duplicate/refuse ambiguously. | Reducer proves start event and completes the signed lease cut once. |
| `HEARTBEAT` | No effect. | Charge event/state/lease may be at different durable cuts. | A new reading must never create a second charge for the accepted key. | Bind pre-lease/head/cursor plan and resume the existing settlement only. |
| `CLOSE` | No effect. | Charge, record, stopped event, lease removal and archive form a multi-step effect. | One event/artifact field cannot identify the cut. | Reuse the signed close automaton and cache only after archive/post-verify. |
| `PAUSE` | No effect. | Checkpoint/event/head/cache cuts may differ. | Retry cannot choose a new checkpoint or pause. | Bind exact checkpoint hash/pre-head and finish the existing pause only. |
| `RESUME` | No effect. | Pending checkpoint and next start/review state may be partial. | Retry must not create a second generation or review gate. | Bind the selected checkpoint and signed pending-resume generation reducer. |
| `OPERATION_ADMIT` | No effect. | Bound/cursor/admission/worker may already exist. | Current journal cannot recover `operation_id`; retry can take another cursor/worker. | Accepted plan creates bound once, binds cursor/admission/key, and returns one op. |
| `OPERATION_STATUS` | No effect unless it is an ack. | Token may have been written but not observed; ack may or may not be durable. | Changed ack flag is different bytes; restart loses the intended relation. | Separate delivery request from explicit prior-delivery ack; redeliver until durable ack. |

For every row, a lost reply after `REPLY_CACHED` returns the identical semantic
effect reply under a current transport envelope. An ack never authorizes
reapplication. No journal state or refusal may be selected using output bytes.

## Validity and scientific/resource non-regression

Subject to the repairs above, the following carried cells are correct and must
remain unchanged:

- E1 remains aggregate device nanoseconds with full actual/conservative
  charging; E2 remains unavailable before WP-6; E3 retains both signed clocks.
- The nine signed events and every signed runtime schema remain closed. Control
  objects and `T_PROMOTED` are T-development-only, not a tenth event or a
  scientific terminal.
- Capability custody remains solely with the supervisor; controller and worker
  operations receive no capability.
- Canonical stream indexes, exclusive subsets, per-stream known/unknown
  accounting and the complete all-live frozen batch are correctly carried in
  V2.7.5/V2.8.
- A valid E1 terminal requires its complete charge/record/archive sequence and
  the one existing exhaustion event. Numeric `device_nanoseconds >= E1`,
  including after an invalid batch, is never counter-only G7.
- Any invalid process/batch remains G5 with its one fixed public cause,
  complete numeric resource facts, no valid exhaustion/stop/pause/review event,
  archival before resolution and only signed author-parented recovery.
- T outputs, result hashes, journal replies, bounds, failure facts and A3
  leakage are adaptive, permanently non-citable T-development material. They
  cannot enter Q/C confidentiality, competence, C planning, C1-C6 evidence or
  programme interpretation.

The controller-supplied output bound must not become a hidden
success-conditioned resource policy. The eventual aggregate capacity rule is
fixed before behavior and may use only declared operation kind, frozen control
inputs and the author-selected capacity provider/value. It cannot be increased
after output, failure, candidate behavior or a desired T result.

## Direct answers to Fable's three Sol questions

1. **No.** B1 is selected and conceptually appropriate, but §§V2.4-V2.5 do not
   make the eight commands exactly-once-effect across generations. The
   generation-bound request hash, unrepresentable mutable phases, absent
   command-specific reducers, broken delivery acknowledgement and unsafe GC
   are concrete blockers.
2. **Mostly yes, with M1 required.** A3 accurately withdraws mode-bit secrecy
   against a deliberate same-UID controller and explicitly forbids Q/C
   inheritance. Mechanical endpoint roles remain incomplete for controller
   descendants, and official intermediate status phases leak progress to
   contract-following clients.
3. **No as a complete packet.** V2.8 correctly preserves E1/E2/E3, the nine
   events, runtime schemas, full-live batch and counter-terminal refusals.
   V2.7 nevertheless provides neither a reachable bound-creation transaction
   nor an aggregate/write-time capacity bound, releases retained quarantine
   accounting, and leaves `FAILED` outside the signed invalidity machine.

## Prior-finding closure

**Genuinely closed:** the false same-UID mode-bit secrecy claim; prohibition on
using A3 as Q/C confidentiality; D1 idle-exit removal; `PROMOTED` as an `OK`
detail rather than a fourth status; identity-to-path hex intent; FIFO
`PIPE_BUF` verification/open order/no-follow intent; basic relative-path,
sparse, hardlink and descriptor-hash rules; `SETTLEMENT.json` as the promotion
commit; canonical stream subsets and all-live batch wording; reparented zombie
handling; global process-sequence history; and the carried §S6 rules for
ARCHIVE, raw-head D1, G5 epoch, private authority, strict integers and locked
close.

**Not closed:** generation-total idempotency and acknowledgement; the durable
effect reducer; pre-claim child discoverability and supervisor singleton under
spawning-client death; aggregate output capacity and failed-operation routing;
watchdog registration-before-behavior and honest freeze timing; descendant role
proof; and fixed pre-settlement status.

## Dirty implementation distinction

The current uncommitted implementation is the earlier facade reviewed by
Codex, not an implementation of this v2. Static inspection confirms it has no
supervisor generation, durable request journal, freezer table, output-bound
transaction or v2 promotion automaton. It still executes a caller-supplied
in-process callback, accepts caller-named result/charge hashes for release,
renews through the old ordinary heartbeat behavior, and lacks the required
process/control topology. Those are dirty implementation deviations and remain
uncommittable; they do not cure, select or independently create the v2 contract
defects above. No implementation finding is used to reopen a signed scientific
cell.

## Disposition and signature

The repair is bounded to the supervisor/control-channel contract and requires
another focused X/Y review. A3, B1, C1 and D1 remain signed and are not reopened.
One new bounded author choice is required for the aggregate output-capacity
policy (fixed total byte envelope versus an exact hard quota/preallocation
provider, without choosing its value here). The remaining repairs are
mechanical consequences of the selected semantics.

`I_ACCEPT_OFFICINA_SUPERVISOR_CONTROL_CHANNEL_AMENDMENT` is **not eligible**
for signature.

## Checks and negative space

I read the v2/v1 supervisor chain, Fable closure, signed A3/B1/C1/D1 selection
and choice packet, both prior formal v1 confirmations, Codex's implementation
review, the signed batch-settlement/generic-harness composite, and the four
dirty implementation/test files. The signed composite hashes match
`OFFICINA_GENERIC_HARNESS_SIGNATURE.md`. The post-v2 commit changes only the two
review prompts. I performed static/read-only inspection only; no test, smoke,
module CLI or Officina code was executed.

This review created only this review file. No code, test, contract, signature,
existing review or runtime artifact was edited; no commit was made. No
activation, supervisor, controller, worker, watchdog, FIFO, journal, spawn
intent, operation, output bound, production manifest, capability, lease, batch,
entropy, E1/E2/E3 spend, world, candidate, Q/C object, datum, outcome or claim
movement was created. `successor/officina/runtime/` still contains only
`T_RUNTIME.lock`; the envelope remains `activated:false`
(`NOT_ACTIVATED`).
