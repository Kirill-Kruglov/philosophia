REVISE_OFFICINA_SUPERVISOR_CONTROL_CHANNEL_V2_1

# Independent Y-line final check

I treated v2.1 as an untrusted candidate authored by Claude Code Opus 5. The
candidate is substantially more complete than v2, but it is not yet a total
exactly-once, validity-first control contract. The defects below are bounded
engineering/governance defects. They do not reopen A3, B1, C1, D1, K1, any
scientific estimand, or any resource value.

## Critical findings

### C1. W1 cannot distinguish a new semantic occurrence from a retry and is not generation-total for STATUS

The client algorithm infers intent solely from whether the highest local slot
has a `.done.json`: an unfinished slot makes every later invocation a retry
(`OFFICINA_GENERIC_HARNESS_SUPERVISOR_CONTROL_CHANNEL_V2_1_CORRECTION.md:
167-207`). This fails the required traces:

- Two concurrent clients sharing one heartbeat scope both select the same
  unfinished occurrence. A legitimate second heartbeat is collapsed into the
  first rather than receiving a new occurrence.
- A client that observed a reply but crashed before writing `.done.json`
  permanently retries the already-observed occurrence.
- W7 permits both the slot and terminal to be removed by the client
  (:1389-1390). After deletion, the allocator has no stated way to recover
  `high_water + 1`; reuse is then refused by the supervisor tombstone
  (:452-466).
- Admission of occurrence `n+1` implicitly acknowledges `n` even when the
  successor carries no matching prior-reply hash (:389-398). Thus a genuinely
  new invocation can erase redelivery proof for a reply it never observed.

`OPERATION_STATUS(ack_delivery=false)` is worse: it has no journal entry and is
recomputed from current state (:382-385). A lost `PENDING` observation retried
after promotion returns `PROMOTED`; it is not a retry-stable reply. This directly
contradicts signed B1, which says all eight commands use the durable journal and
that replies and token bytes remain redeliverable until durable acknowledgement
(`OFFICINA_SUPERVISOR_AUTHOR_SELECTIONS_V1_SIGNATURE.md:29-31`).

The tombstone is also insufficiently defined. For any old occurrence below the
high water it retains only the *last* effect-reply hash, then asks whether the
incoming old key has an “equal recorded `last_effect_reply_sha256` scope”
(:431-460). An incoming retry does not carry the old effect-reply hash, and the
last hash need not be the hash for that old occurrence.

This affects all eight commands. For `CLAIM`, `START`, `HEARTBEAT`, `CLOSE`,
`PAUSE`, `RESUME`, and `OPERATION_ADMIT`, the per-command locators could support
one effect after a proper occurrence is fixed, but the shared allocation and
ack rules do not fix that occurrence. For observation-form `OPERATION_STATUS`,
there is not even a cached occurrence. Ack-form `OPERATION_STATUS` has a plan,
but inherits the same allocation defect.

Mandatory bounded repair:

1. Make “new occurrence” versus “retry occurrence” an explicit client API
   choice. A first invocation atomically allocates and returns a durable
   occurrence handle; only an invocation naming that handle is a retry.
   Unfinished state alone must not silently convert a new invocation into a
   retry.
2. Make allocation recover the next index from supervisor-authoritative journal
   and tombstone state as well as the compact client counter. Client deletion or
   relabelling must not permit reuse or permanently prevent `high_water + 1`.
   Client files remain convenience state, never runtime authority.
3. Journal and cache observation-form `OPERATION_STATUS` like the other seven
   commands, with an empty effect tuple. A new poll gets a new occurrence; a
   retry gets the byte-identical cached effect reply and token.
4. Permit successor-occurrence acknowledgement only when the successor carries
   the exact cached prior `effect_reply_sha256`. Otherwise the prior occurrence
   remains unacknowledged. Keep the separate delivery acknowledgement.
5. Either retain a per-occurrence replay commitment or define a contiguous,
   supervisor-derived high-water tombstone whose classification needs no
   unavailable old reply hash. GC may advance only over a contiguous
   acknowledged prefix.

### C2. The reducer turns ordinary later history into G5 and takeover is not validity-first

W1.5 requires the *current* ledger head to equal the plan's pre-head or one of
the plan's event hashes before it even checks whether `reply.json` exists
(:345-365). Therefore an acknowledged completed request followed by any normal
later event has a current head outside that small set. A restart before GC
routes the old completed journal to record-first invalidity. Ordinary history,
not a scientific/process fault, can thereby create G5.

The takeover order compounds this. The new supervisor runs every open effect
reducer before settling streams affected by the prior supervisor's death
(:681-691). An accepted `START`, `HEARTBEAT`, or `OPERATION_ADMIT` may therefore
append, install, spawn, or resume before the process-loss/watchdog invalid route
and all-live batch have been made durable. That violates validity-first
dominance and can make an effect survive a failure that should invalidate the
live set.

Mandatory bounded repair:

- For a committed or replied plan, validate that its recorded post-head and
  event hashes occur in the exact durable chain; allow the current head to be a
  verified descendant. Do not require equality with an old head.
- For an accepted-only plan, validate the exact legal prefix and require there
  to be no conflicting intervening suffix. A mismatch is process invalidity
  only when it is genuinely an impossible durable layout, never merely later
  valid history.
- At takeover, first establish process death/freeze facts, settle every affected
  live stream through the signed all-live invalid route, and resolve the batch.
  Only then may reducers finish non-behavioral archival/cache work. No reducer
  may spawn, `SIGCONT`, renew, admit, or otherwise continue behavior across the
  old supervisor's loss.

### C3. The spawn identity and bootstrap protocol is not constructible or total

Four independent contradictions remain:

1. `spawn_intent_id` hashes `argv_sha256` (:542-558), while the complete argv
   itself contains that same `spawn_intent_id` and `argv_sha256` is over the
   complete argv (:565-576). This is a self-referential fixed-point
   specification, not a deterministic construction.
2. The supervisor grandchild enters in-process and never execs or gets new argv
   (:482-504), but timeout and takeover claim to discover that half-initialized
   grandchild by a dynamically created `spawning_id` in `/proc/*/cmdline`
   (:529-533, :583-593). That marker cannot appear in its inherited cmdline.
   The retained `SPAWN.lock` prevents a second supervisor but can leave every
   later client blocked forever if the grandchild wedges before identity
   installation.
3. The spawn-intent schema includes role `WATCHDOG` and requires a nonempty
   complete argv (:544-552), but the watchdog is an in-process fork with no
   exec and no new argv (:491-496).
4. Appending tokens to a client-supplied controller/worker argv does not ensure
   those programs interpret the tokens or self-stop before arbitrary target
   behavior. W2.6 describes a reviewed adapter (:616-635), but W2.4 does not
   require the executable root to be that adapter.

Mandatory bounded repair:

- Hash an exact argv template containing a typed placeholder, derive
  `spawn_intent_id` from that template plus generation/role/sequence/time, then
  substitute the id and hash the resulting complete argv separately. The two
  hashes and their domains must be explicit.
- Give pre-identity supervisor creation a kernel-verifiable, non-circular
  binding. For example, keep the new session/PGID and use a sealed bootstrap
  pipe to report the grandchild PID/start identity before initialization; on
  timeout kill the recorded process group and prove it dead. Do not claim a
  cmdline marker for a process that never execs.
- Remove the in-process watchdog from the exec-child spawn-intent schema and
  give it its already-defined lease-table/pipe identity, or define a separate
  exact fork-child record without argv.
- Require a pinned, reviewed supervisor-owned bootstrap adapter as the actual
  controller/worker executable root. It must parse and validate the inherited
  tokens, close forbidden descriptors, self-stop, and only after `SIGCONT`
  dispatch the target. An arbitrary target executable may not be the bootstrap
  root.

### C4. OPERATION_ADMIT can cache success before the worker is runnable

The admission transaction writes `committed.json`, then caches
`OK/ADMITTED`, and only afterwards sends `SIGCONT` (:917-936). If the
supervisor crashes after the cached reply but before `SIGCONT`, W1.5 returns the
cached reply immediately because `reply.json` exists (:350-356); it never
performs step 9. The worker can remain stopped indefinitely behind a durable
success. W8 has no row for this cut.

Mandatory bounded repair: make “worker release attempted for the exact bound
identity” part of the deterministic effect plan before a success reply becomes
cacheable. `SIGCONT` is idempotent, but after a supervisor loss the
validity-first takeover rule in C2 must freeze/settle rather than resume the
worker. A cached `ADMITTED` reply may exist only after the same-generation
supervisor has completed the release step; otherwise the cached terminal must
be the closed invalid/refusal route.

### C5. v2.1 replenishes capacity at settlement contrary to signed K1

Signed K1 says aggregate custody includes live reservations, pending settlement,
quarantine, and promoted custody; “rename, promotion, settlement, and failure do
not replenish capacity,” and only an authorized custody-absence disposition
releases it
(`OFFICINA_SUPERVISOR_OUTPUT_CAPACITY_SELECTION_V1_SIGNATURE.md:28-36`).

v2.1 instead changes an operation's contribution from `bytes_reserved` to
`actual_bytes` at settlement and labels the difference released
(:1024-1045, :1118-1127). A one-byte promoted result from a 256 MiB reservation
therefore replenishes almost 256 MiB without any custody-absence disposition.
The earlier choice-packet draft used that remeasurement, but the later signed
selection states the controlling no-replenishment rule explicitly. The v2.1
closure also represents settlement as releasing nothing, so the packet is
internally inconsistent.

Mandatory bounded repair: retain `bytes_reserved` as the accounted contribution
for every admitted, running, pending, quarantined, or promoted operation until
the authorized disposition proves custody absent. `actual_bytes` remains a
diagnostic custody fact and may never reduce the 32 GiB accounted total.
Remove every “over-declaration release” transition. This implements K1 as
signed; changing it would reopen K1 and is not authorized by this review.

## Major findings

### M1. The author-disposition authority is not an executable closed contract

The candidate says disposal requires a signed author artifact and lists broad
content restrictions (:1063-1073), but it does not define the artifact's
canonical path, schema, exact key set, signer/token representation, parent/hash
binding, durability, single-use rule, or verifier. W7 defines only the
supervisor-produced `.disposed.json` (:1394-1396). Two implementations can
therefore accept different objects as “signed author disposition,” and a stale
or substituted authority can release capacity.

Mandatory bounded repair: before signature, define one immutable canonical
author-disposition object with an exact path grammar, schema/key set, author
token/signature encoding, activation and operation bindings, recorded reserved
and actual byte facts, custody destination, parent hashes, no-replace/single-use
semantics, and a fail-closed verifier. The supervisor-produced disposition must
hash that exact object and may be written only after descriptor-safe proof that
the named custody is absent. Every mismatch remains blocked. This closes K1's
already-selected authority; it does not choose a new resource cell.

### M2. W5 correctly fixes response bytes but falsely claims timing secrecy

The candidate fixes all official preterminal response bodies to `PENDING`
(:1133-1148), which closes result-field leakage for contract-following clients.
It nevertheless says the transport path does not branch on output and that
transition time “reveals nothing.” The same serial supervisor performs
output-dependent reads, copies, hashes, filesystem operations, settlement, and
control service (:979-1009). Reply latency, FIFO backpressure, path metadata,
worker exit timing, and refusal timing can vary with that work.

Mandatory bounded replacement:

> Official preterminal reply bytes are fixed to `PENDING`. Scheduling latency,
> endpoint/filesystem metadata, worker timing, and same-UID observations are not
> mechanically confidential under signed A3; they are T-process facts only,
> are permanently non-citable, and may not enter selection, Q/C, C1-C6, or any
> scientific interpretation.

This is the honest A3 boundary and requires no new author choice.

### M3. The strictly-positive overrun assertion lacks a total equality case

W3 triggers when `now_ns >= deadline_ns`, later samples `freeze_ns`, and asserts
`freeze_ns - deadline_ns > 0 “by construction”` while deleting the zero branch
(:744-765, :792-804). Integer monotonic samples can be equal. This may not
silently become a valid terminal.

Mandatory bounded repair: if a proved-quiescent sample is not strictly greater
than the deadline, take a bounded later monotonic sample while the group remains
quiescent; if strict progress cannot be established, use the existing
`UNKNOWN`/all-live invalid route. Never restore a valid zero-overrun branch.

## Required attack results

### B1 traces

| Trace | Required result | v2.1 result |
|---|---|---|
| Lost request before `accepted.json` | same explicit occurrence may retry; no effect | representable only if the local slot survives |
| Lost reply after `reply.json` | identical cached effect reply across generations | representable for seven planned forms |
| Client crash after seeing reply, before `.done` | cached old reply remains available; a separately declared new occurrence remains possible | new intent is silently treated as old retry |
| Generation change | same semantic occurrence, new transport wrapper | correctly designed |
| Effect before `committed.json` | one command-specific reducer continuation | locators exist, but C2/C3/C4 make several continuations invalid |
| Ack then GC then old retry | no reapplication; closed acknowledged response | tombstone classification is under-specified for older occurrences |
| Concurrent same-scope clients | distinct new occurrences, same occurrence only for explicit retry | both collapse onto highest unfinished slot |
| Repeated STATUS | new observation gets a new occurrence; retry of one observation is stable | observation is unjournaled and can change on retry |

`CLAIM`, `START`, `HEARTBEAT`, `CLOSE`, `PAUSE`, `RESUME`, and
`OPERATION_ADMIT` all inherit the shared failures. Ack-form
`OPERATION_STATUS` is planned; observation-form is not. Protocol/schema/replay
errors themselves correctly avoid G5 at W1.2, but the normal-head mismatch in
W1.5 can still create G5 and must be removed.

### C1 validity and evidence authority

- Lease-table publication and exact watchdog acknowledgement precede
  `SIGCONT`, capability use, and admission (:707-717). The old deadline remains
  binding until acknowledgement.
- Lost freeze evidence becomes `UNKNOWN`; no earlier freeze time is invented
  (:784-790).
- Every proved-positive or unknown freeze maps to one invalid all-live route
  with full E1 facts; it cannot become close, resource stop, E1/E3 exhaustion,
  pause, or review (:792-823).
- The watchdog-written freeze object is compatible with selected C1 only as a
  raw freezer observation: it holds no capability/lock, appends no ledger event,
  and cannot choose a valid terminal; the supervisor alone settles. Missing,
  malformed, conflicting, or unverifiable evidence must always degrade to
  `UNKNOWN` invalidity. It must never be treated as a second settlement or
  validity authority.
- Process-tree escape and deliberate same-UID inspection remain honestly
  procedural A3 residuals (:1197-1202, :1314-1329); they are not Q/C security
  or evidence claims.

### K1 trace

The intended order from plan through reserve/bound/admission/bootstrap,
settlement, promotion, delivery acknowledgement, and disposal is otherwise
single-valued. The exact selected constants are embedded unchanged:
67,108,864 bytes per stream, 268,435,456 per four-stream operation,
34,359,738,368 aggregate, 8,589,934,592 safety margin, and 4,194,304 chunk
(:49-78). The parser is bounded and contract-following workers receive only the
framed pipe. Live, pending, quarantine, and promoted custody are enumerated.

The trace fails at two load-bearing points: cached `ADMITTED` precedes
`SIGCONT` (C4), and settlement reduces reserved capacity (C5). Disposal is not
closed enough to be authoritative (M1). Quarantine and promoted bytes otherwise
remain T-only, `scientific_outcome:false`, and unavailable to Q/C.

### Spawn/takeover and control artifacts

The one `SPAWN.lock` is a sound safety device against a second serving
generation, but it is not a total liveness/recovery identity for the in-process
grandchild. The spawn hash is circular, and the watchdog/controller/worker
bootstrap identities are mixed. Client intent slots remain convenience state
and must not become hidden runtime authority. The corrections in C1-C4 are
required before the crash reducer or immutable-object table is deterministic.

## Direct answers to Fable's three Sol questions

1. **No.** W1 is not exactly-once for all eight commands: new-versus-retry
   intent is inferred incorrectly, observation STATUS is unjournaled, successor
   acknowledgement can occur without proof of receipt, tombstone recovery is
   incomplete, and the reducer rejects legitimate descendant heads.
2. **No.** Failure classes mostly point to the correct signed invalid routes,
   but v2.1 replenishes reserved capacity at settlement, can strand a stopped
   worker behind cached success, and lacks a closed author-disposition
   authority. Invalidity dominance also requires the takeover-order repair.
3. **No, as written.** Official preterminal reply *bytes* are fixed and the
   endpoint roles are honest, but timing and same-UID metadata can vary with
   worker activity. They must be stated as procedural, non-citable A3
   residuals. W6.5's bounded supersession of the impossible real-time deadline
   sentence is otherwise honest and does not weaken another scientific or
   resource cell.

## Genuinely closed prior findings

The semantic request excludes generation-specific transport bytes; cached
effect replies are rewrapped under the current generation; changed bytes under
one key are a protocol error rather than G5; phase files are immutable and
predecessor-bound; command arguments/reply enums are closed; release-token
delivery acknowledgement is distinct from ordinary reply acknowledgement; D1
has no idle exit; the lease table is acknowledged before behavior; lost freeze
time is not reconstructed; all watchdog freezes are invalid; official
preterminal response fields are fixed; endpoint-role limitations and A3 are
stated honestly; the signed nine-event surface, E1/E2/E3 constants, all-live
batch authority, capability custody, Q/C exclusion, and scientific negative
destinations are not intentionally changed.

Those closures do not cure C1-C5/M1-M3.

## Repair and signature disposition

The repair is bounded and may be made without reopening A3, B1, C1, D1, or K1:
it must implement those selected cells literally. A correction that retains
v2.1's settlement replenishment would instead reopen K1 and would require a new
author selection; that route is not authorized here. The corrected contract
requires another focused X/Y confirmation.

The token

```text
I_ACCEPT_OFFICINA_SUPERVISOR_CONTROL_CHANNEL_AMENDMENT
```

is **not eligible** for signature.

## Static custody and negative space

This was a static/read-only contract review. I did not run code, tests, an
Officina command, FIFO/pipe, journal, watchdog, smoke, controller, worker, or
supervisor. I created no authorization, manifest, capability, entropy, lease,
world, learner, T/Q/C artifact, resource spend, datum, outcome, or claim
movement. I did not modify the dirty implementation/tests or any existing file.
The uncommitted implementation remains the earlier facade and does not implement
the candidate supervisor contract.

The real runtime contains only the tracked immutable `T_RUNTIME.lock`; T remains
`NOT_ACTIVATED`. The programme claim remains `OPEN`.
