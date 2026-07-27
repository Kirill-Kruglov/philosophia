# Officina supervisor and control-channel amendment — v2 draft

Status: `CANDIDATE_FOR_XY_REVIEW_NOT_AUTHORIZED`. Self-contained
replacement of
`successor/OFFICINA_GENERIC_HARNESS_SUPERVISOR_CONTROL_CHANNEL_V1_DRAFT.md`
(preserved unedited as evidence). Embeds the signed author selections
of `successor/OFFICINA_SUPERVISOR_AUTHOR_SELECTIONS_V1_SIGNATURE.md`
and every mechanical repair from the author-choice packet and the
Codex/Opus/Sol implementation reviews. Governing harness composite and
batch-settlement amendment remain unchanged.

```text
A: I_SELECT_SUPERVISOR_CONFINEMENT_A3_SAME_UID_PROCEDURAL_RESCOPE
B: I_SELECT_SUPERVISOR_IDEMPOTENCY_B1_DURABLE_JOURNAL_ACK_REDELIVERY
C: I_SELECT_SUPERVISOR_WATCHDOG_C1_DEDICATED_FREEZER
D: I_SELECT_SUPERVISOR_LIFETIME_D1_NO_IDLE_EXIT
```

Author token candidate (still **not signable** until fresh X/Y accept
this v2):

```text
I_ACCEPT_OFFICINA_SUPERVISOR_CONTROL_CHANNEL_AMENDMENT
```

Creates nothing executable. Edits no code. Starts no process. T remains
`NOT_ACTIVATED`. No new production root, allowlist delta, signed event,
runtime schema, scientific constant, or call-graph manifest is
authorized.

**Deleted v1 claims (do not survive):** same-UID `0700`/`0000` secrecy;
ephemeral replay tables; “at or before the deadline” as a physical
serial-loop guarantee; 60 s idle exit; parent-after-exec `SIGSTOP` as
sufficient bootstrap; durable-state-alone idempotency without a journal.

Engineering constants (control only):

```text
T_CONTROL_FRAME_MAX_BYTES = 4096
T_CONTROL_READ_TIMEOUT_SECONDS = 10
T_CLIENT_REPLY_TIMEOUT_SECONDS = 30
T_WATCHDOG_POLL_INTERVAL_NS = 100_000_000
T_WATCHDOG_UPDATE_ACK_TIMEOUT_NS = 1_000_000_000
SIGCONT = 18; SIGSTOP = 19; SIGKILL = 9; SIGTERM = 15; SIGNAL_0 = 0
```

---

## V2.0 Replacement index over signed composite + v1

| Locus | Action |
|---|---|
| Harness v2 §1 ownership (“supervisor process…”) | **completed** by §V2.1 |
| Harness v2 §2c.1–2c.6 | **completed** by §V2.1 / §V2.4 / §V2.8 |
| Harness v2 §5a “separate supervisor” sentence | **replaced** by §V2.1.1 (singleton supervisor; per-tree sessions) |
| Harness v2 §5b | **completed and A3-scoped** by §V2.2 / §V2.7 |
| Harness v2 §9 argv/import | **completed** by §V2.10 |
| Harness v2 §10 | **extended** by §V2.12 |
| Supervisor v1 entire draft | **superseded** by this document |
| Batch-settlement amendment / §S6 ledger | **referenced unchanged**; wiring in §V2.8 |

---

## V2.1 Topology, lifetime, bootstrap (A3 roles; D1; mechanical 1–5)

### V2.1.1 One topology

Exactly **one** persistent runtime supervisor process per repository
generation. It is the sole holder of `T_RUNTIME.lock` (per §3 epoch;
never at rest), sole writer of every durable `runtime/` artifact, sole
issuer/revoker of real-T capabilities, sole parent of every controller,
worker, and the dedicated freezer watchdog, and the sole runtime
settlement authority. Each controller tree occupies its **own session
and process group** owned by that supervisor. The six CLI commands and
two controller commands are clients of the control channel (§V2.4);
clients never take the lock, never write `runtime/` evidence, and never
hold a capability object.

**D1 — no idle exit.** The supervisor never exits because of idleness.
It persists until: durable pause (G3), terminal G6/G7, G5 awaiting
signed recovery, clean shutdown after those states with zero live
leases and zero unresolved batch/journal/operation records, process
crash/power-loss, or signed author stop. There is no
`T_SUPERVISOR_IDLE_EXIT_SECONDS` and no drain-for-idle protocol.

### V2.1.2 Creation and singleton lock

Endpoint directory (mode `0700`, control plane only):

```text
successor/officina/runtime_control/T_SUPERVISOR/
```

Contains: `SPAWN.lock`, `SUPERVISOR_IDENTITY.json`, `REQUEST.fifo`,
`REPLY/`, `CHILDREN/`, `JOURNAL/`, `WATCHDOG/`, `operations/`.
**Excluded from every signed archival set** together with
`runtime/T_PROMOTED/` (§V2.9.4).

Any CLI needing a live supervisor acquires exclusive `flock` on
`SPAWN.lock` (`O_RDWR|O_CREAT|O_CLOEXEC`) and **holds it until**
`SUPERVISOR_IDENTITY.json` is atomically installed and live-verified
(`os.kill(pid,0)` ∧ start-identity match ∧ boot-identity match). Only
then is the lock released. Double-fork from the CLI (same module image;
no new argv command, script, or daemon executable): child `setsid`,
grandchild is supervisor; grandchild closes **every** inherited
descriptor including the spawn-lock fd **before** writing the identity
record; redirects stdio to `os.devnull`; creates endpoints; spawns the
freezer watchdog (§V2.6); enters serve.

Live check: identity record present ∧ PID live ∧
`start_identity(pid)` equals recorded ∧ boot id equals recorded.
Stale → takeover (§V2.1.6) then spawn.

### V2.1.3 Kernel start identity

`start_identity(pid)` = the 20th whitespace-separated token after the
**final** `)` in `/proc/<pid>/stat` (kernel `starttime`), then `:`,
then `/proc/sys/kernel/random/boot_id` text. Compared at every
admission, settlement, freeze, takeover kill, and control-frame
validation. Path encoding of identities uses lowercase hex of the
UTF-8 identity bytes; component lengths and full path length must fit
the filesystem; reject otherwise.

### V2.1.4 Claim / start / lease (spawn-before-claim; self-stop)

**Spawn intent (before any child).** Under the lock or spawn lock as
applicable, write
`CHILDREN/<spawn_intent_id>.json` (atomic no-replace), schema
`philosophia.officina.t-spawn-intent.v1`, keys exactly:

```text
schema, scientific_outcome, supervisor_generation_sha256,
spawn_intent_id, role (CONTROLLER|WORKER|WATCHDOG), argv_sha256,
created_utc
```

`spawn_intent_id` = lowercase hex SHA-256 of the canonical intent
bytes without the id field circularity: compute id from
`{generation, role, argv_sha256, created_utc}` once. Pre-claim
controller logs live at
`CHILDREN/<spawn_intent_id>/controller.stdout.log` (and `.stderr.log`).

**Controller bootstrap (race-free).** Reviewed adapter
`controller_argv(...)` entry’s **first** executable actions, before any
behavior-capable import, input read, thread, backend, or controller
logic: install signal dispositions only as required to not defeat stop,
then `os.kill(os.getpid(), SIGSTOP)` (self-stop). Supervisor uses
`subprocess.Popen(..., start_new_session=True, shell=False,
pass_fds=(ctrl_req_w, ctrl_rep_r))`, then `os.waitpid(pid, WUNTRACED)`
and requires `WIFSTOPPED`; then reads start identity; only then writes
the durable `t-process-claim.v1` with observed
`controller_pid`, `controller_start_identity`, `process_group_id`
(= session leader pid), exact `argv`, boot id. Parent-after-exec
`SIGSTOP` alone is **forbidden**. After durable claim, optional rename
of log dir to `CHILDREN/<process_id>/` (atomic). Crash after spawn
intent + child, before claim: takeover kills by registry identity
(§V2.1.6). Crash after claim, before start: signed orphan-claim route;
registry retains the binding.

**Start / lease.** Validate claim and frozen identity; append
`T_PROCESS_STARTED`; reserve; install lease (seed =
start-event hash); construct in-memory `RealTCapability` **supervisor-
held only**; then `SIGCONT` the controller. Controller and worker never
receive the capability, lock fd, or write authority to durable
`runtime/` evidence paths (procedural under A3 for deliberate
same-UID; mechanical for wrong FD inheritance).

### V2.1.5 Process / FD inheritance table

| Process | Parent | Session | Holds lock? | Capability? | Control endpoints | Inherited FDs |
|---|---|---|---|---|---|---|
| Supervisor | CLI double-fork / service image | own | yes (epochs) | issuer | owns FIFO + all pipes | scrubbed at start |
| Freezer watchdog | Supervisor | own | **no** | **no** | sealed update/ack pipes only | those pipes only |
| Controller | Supervisor | own | no | no | inherited ctrl pipes only | req-write, rep-read |
| Worker | Supervisor | own | no | no | **none** | status-write only |
| CLI client | user shell | caller | no | no | `REQUEST.fifo` + own reply FIFO | none of supervisor’s |

Every supervisor-created FD is `O_CLOEXEC` except the exact `pass_fds`
cleared for the child. Workers cannot open `REQUEST.fifo` as an
authorized role even if the pathname is reachable under A3 residual
(§V2.2.2): frames from worker PIDs are refused by role check.

### V2.1.6 Takeover

Under `SPAWN.lock`, before a new supervisor serves: load durable
claims, leases, `CHILDREN/*` intents, journal, freeze observations.
For each recorded controller/worker/watchdog identity: if start
identity matches live PID, `killpg`/`kill` SIGTERM then SIGKILL; prove
dead by `/proc/<pid>/stat` absence or state `Z` (zombie counts as
dead for emptiness); **`os.waitpid` only for own-generation children**.
Never use `kill(0)` alone as group-empty proof on reparented groups.
On PID reuse (identity mismatch): do not kill; treat stream lost.
Unlink only stale control endpoints (not durable `runtime/` evidence,
not quarantined outputs). Settle affected streams per §4c/§4d and
honor unresolved batch + journal. Then spawn.

### V2.1.7 Global sequence and ids

Next `process_sequence` = 1 + max sequence over **complete durable
history** (all claims and process records), never live leases alone.
Process ids are claim content hashes as signed; non-reuse of sequence
and id is enforced at claim validation.

---

## V2.2 Confinement A3 and observation contract

### V2.2.1 Normative A3 meaning

Under one login UID, §5b “neither readable nor writable by the
adaptive controller” is:

- **Mechanical** against accidental and contract-following misuse:
  wrong FD inheritance, escaped children, endpoint-role violations,
  symlink/hardlink escapes in output grammar, promoting without
  settlement, CLI commands from a controller endpoint, controller
  commands from the CLI FIFO.
- **Procedural only** against a **deliberate** same-UID controller
  that inspects or `chmod`s supervisor-owned paths, `/proc`, or
  memory. That residual is exactly the signed §5a residual for a
  principal privileged over its own UID’s files; it is **not** a
  kernel compartment.
- **T-development only.** This boundary **must not** be cited,
  inherited, or relied upon as Q/C confidentiality, blinding, or
  candidate secrecy. Q/C reject whole T artifacts as already signed.

v1 mode-bit secrecy claims are void. Named operation directories may
exist for engineering convenience; they do not create a secrecy
obligation beyond A3.

### V2.2.2 Endpoint roles (mechanical under A3)

| Command set | Authorized endpoint | Peer proof |
|---|---|---|
| `CLAIM` `START` `HEARTBEAT` `CLOSE` `PAUSE` `RESUME` | `REQUEST.fifo` only | client PID+start-identity live; PID **not** a live controller/worker/watchdog in `CHILDREN`/claims |
| `OPERATION_ADMIT` `OPERATION_STATUS` | per-controller inherited pipe only | peer is the claimed controller identity for that pipe |
| (none) | workers | any control frame from a worker identity → `INVALID` |

A controller opening `REQUEST.fifo` with a truthful identity still
fails the role check. CLI frames on a controller pipe fail. Workers
have no control FD and are role-refused if they forge pathname access
(A3 residual may allow the open attempt; the supervisor still refuses).

### V2.2.3 Pre-settlement observation (A3-honest)

The channel and schemas expose only: admission/refusal of the request,
opaque `operation_id` / handles, and fixed closed pending status
shapes that do **not** encode output bytes, file counts, sizes, or
worker exit reasons in refusal classes. Under A3, the contract
**does not claim** mechanical blindness of a deliberate same-UID
inspector to path existence or `/proc` metadata. Promoted bytes and
release-token fields become channel-visible only after settlement +
promotion commit (§V2.7). Invalid/process terminals expose only signed
closed process facts.

---

## V2.3 Durable objects (paths, schemas, owners, cuts)

All control-plane JSON: canonical ASCII + trailing newline; atomic
no-replace unless noted; `scientific_outcome: false`;
`reject_scientific_fields` recursive; `type(x) is int` for every
integer field (`bool` refused).

| Object | Path | Schema | Owner | Lifecycle / archival |
|---|---|---|---|---|
| Supervisor identity | `T_SUPERVISOR/SUPERVISOR_IDENTITY.json` | `t-supervisor-identity.v1` | supervisor | generation; not archived |
| Spawn intent | `T_SUPERVISOR/CHILDREN/<id>.json` | `t-spawn-intent.v1` | supervisor | until process terminal + ack; not archived |
| Request journal entry | `T_SUPERVISOR/JOURNAL/<idempotency_key_hex>.json` | `t-request-journal.v1` | supervisor | until owning transition archived ∧ ack; not archived |
| Reply ack | `T_SUPERVISOR/JOURNAL/<idempotency_key_hex>.ack.json` | `t-request-ack.v1` | supervisor | retained with journal; not archived |
| Watchdog lease table | `T_SUPERVISOR/WATCHDOG/LEASES.json` | `t-watchdog-lease-table.v1` | supervisor | replace per update; not archived |
| Freeze observation | `T_SUPERVISOR/WATCHDOG/FREEZE/<process_id>.json` | `t-freeze-observation.v1` | supervisor | until settlement consumes; not archived |
| Output bound | `T_SUPERVISOR/operations/<op>/BOUND.json` | `t-operation-output-bound.v1` | supervisor | with operation; not archived |
| Admission | `…/OPERATION.json` | `t-operation-admission.v1` | supervisor | with operation; not archived |
| Settlement commit | `…/SETTLEMENT.json` | `t-operation-settlement.v1` | supervisor | commit point; not archived |
| Promoted tree | `runtime/T_PROMOTED/<operation_id>/` | (bytes) | supervisor | T-dev data; **archival-excluded** |
| Batch claim / override | signed amendment paths | signed | supervisor | archived per amendment |

Identity keys exactly:
`schema, scientific_outcome, activation_record_sha256, supervisor_pid,
supervisor_start_identity, boot_identity, request_fifo, created_utc`.
`supervisor_generation_sha256` = SHA-256 of that file’s canonical bytes.

---

## V2.4 Control channel and eight-command schemas (B1; mechanical 6–8)

### V2.4.1 Transport

Named FIFOs + inherited pipes only. Supervisor keeps a keep-open
`O_WRONLY|O_CLOEXEC` on `REQUEST.fifo` so readers see `EAGAIN`, not
spurious EOF. Verify `fpathconf(fd, PC_PIPE_BUF) ≥ 4096` at endpoint
creation. One `write` of a complete frame ≤ 4096 bytes; partial write
or `EAGAIN` → no action + closed retry via journal. Client opens reply
FIFO read end nonblocking **before** publishing the request; supervisor
opens/writes reply nonblocking. Directory-fd, `O_NOFOLLOW`, type, and
ownership checks before every endpoint use.

### V2.4.2 Frame envelopes

Request keys exactly:

```text
schema ("philosophia.officina.t-control-request.v1"),
scientific_outcome, supervisor_generation_sha256, command,
idempotency_key, arguments, client_pid, client_start_identity,
client_boot_identity, client_monotonic_ns, reply_fifo
```

`idempotency_key`: 64 lowercase hex chars, client-generated,
retry-stable. `client_monotonic_ns`: freshness only; must be
non-decreasing per client start-identity within a generation for new
keys; journal key is `idempotency_key`, not monotonic.

Reply keys exactly:

```text
schema ("philosophia.officina.t-control-reply.v1"),
scientific_outcome, supervisor_generation_sha256, request_sha256,
status, detail
```

`status` ∈ {`OK`, `REFUSED`, `INVALID`}. Terminal promotion uses
`status=OK` with `detail.phase = PROMOTED` (no fourth status enum).
`request_sha256` = SHA-256 of the request’s canonical bytes.

### V2.4.3 CLI argument tables

| Command | `arguments` keys exactly |
|---|---|
| `CLAIM` | `device_units` (int 1..4), `behavior_source_sha256`, `config_sha256`, `stack_sha256`, `numerical_mode_sha256`, `device_identity`, `argv` (nonempty list[str]) |
| `START` | `process_id` |
| `HEARTBEAT` | `process_id` |
| `CLOSE` | `process_id` |
| `PAUSE` | `reason` ∈ {`OPERATOR`, `RESOURCE`}, `checkpoint_payload_sha256` |
| `RESUME` | `checkpoint_sha256` |

### V2.4.4 Controller argument tables

| Command | `arguments` keys exactly |
|---|---|
| `OPERATION_ADMIT` | `process_id`, `operation_kind` ∈ {`ORACLE_QUERY`,`LEARNER_UPDATE`,`CHECKPOINT_WRITE`}, `input_spec` (keys exactly: `input_sha256`), `declared_stream_indexes` (sorted unique nonempty ints in 1..device_units), `max_total_output_bytes` (positive int), `output_bound_sha256` |
| `OPERATION_STATUS` | `operation_id`, `ack_delivery` (bool; true redeems token when `phase=PROMOTED`) |

`output_bound_sha256` = SHA-256 of the durable `BOUND.json`
(§V2.7.1) already installed for this admit intent.

### V2.4.5 Reply `detail` matrix (exhaustive)

| status | command context | `detail` keys exactly |
|---|---|---|
| `REFUSED` | any | `token` ∈ closed refusal enum below, `retryable` (bool) |
| `INVALID` | any | `token` ∈ {`ROLE`,`SCHEMA`,`IDENTITY`,`REPLAY_BYTES`,`GENERATION`,`BOUND`} |
| `OK` | `CLAIM` | `process_id`, `process_claim_sha256`, `process_sequence` |
| `OK` | `START` | `process_id`, `lease_sha256`, `started` (true) |
| `OK` | `HEARTBEAT` | `process_id`, `charge_event_sha256`, `cumulative_charge_ns` |
| `OK` | `CLOSE` | `process_id`, `process_record_sha256`, `stopped_event_sha256` |
| `OK` | `PAUSE` | `pause_event_sha256`, `checkpoint_sha256` |
| `OK` | `RESUME` | `phase` ∈ {`G1`,`G4`}, `ledger_head_sha256` |
| `OK` | `OPERATION_ADMIT` | `operation_id`, `phase`=`ADMITTED` |
| `OK` | `OPERATION_STATUS` | `operation_id`, `phase` ∈ {`ADMITTED`,`RUNNING`,`PENDING_SETTLEMENT`,`PROMOTED`,`FAILED`}, and if `PROMOTED`: `release_token` (object keys exactly: `activation_record_sha256`,`process_id`,`lease_sha256`,`operation_id`,`result_sha256`,`charge_event_sha256`), `promoted_relative_paths` (sorted list[str]); if `ack_delivery` and already acked: `phase`=`ALREADY_DELIVERED` without `release_token` |

Refusal tokens (closed): `STALE_GENERATION`, `UNRESOLVED_BATCH`,
`UNRESOLVED_JOURNAL`, `G5_BLOCKED`, `E3_DUE`, `NO_CAPACITY`,
`NOT_LIVE`, `DEADLINE_FREEZE`, `BUSY`, `NOT_FOUND`.

No free text. No result hash before `PROMOTED`. No learner fields.

---

## V2.5 Idempotency journal B1

Schema `t-request-journal.v1` keys exactly:

```text
schema, scientific_outcome, idempotency_key, request_sha256,
command, arguments_sha256, supervisor_generation_sha256_at_accept,
pre_ledger_head_sha256, process_id_or_null, lease_sha256_or_null,
phase, effect_event_sha256_or_null, effect_artifact_sha256_or_null,
reply_status, reply_detail, created_utc, committed_utc
```

`phase` ∈ {`ACCEPTED`,`COMMITTED`,`REPLY_CACHED`}.

Rules:

1. On request: if journal hit with same key and **byte-identical**
   `request_sha256` → return cached reply; no re-apply.
2. Same key, different bytes → `INVALID` / `REPLAY_BYTES` +
   record-first invalidity naming the journal path.
3. Miss → write `ACCEPTED` (binds pre-head, command, args hash), apply
   effect once, write `COMMITTED` with effect identities, cache reply
   (`REPLY_CACHED`).
4. Survives supervisor generations; takeover reloads journal before
   admission.
5. `OPERATION_ADMIT` retry: same key returns same `operation_id`; **no
   second worker, no new meter cursor, no second charge**.
6. Release token bytes redeliver on `OPERATION_STATUS` until
   `t-request-ack.v1` exists for that idempotency key (or a dedicated
   `delivery_ack` keyed by `operation_id` — exactly:
   `schema, scientific_outcome, operation_id, idempotency_key,
   request_sha256, redeemed_utc`). Acknowledgement consumes one-use
   **effect**; further STATUS returns `ALREADY_DELIVERED` without token.
7. Blind re-execution after timeout is forbidden; clients must reuse
   `idempotency_key`.
8. Retention: delete/GC only after owning transition archived ∧ ack
   present (no TTL tunable).

---

## V2.6 Watchdog C1 — honest non-RT contract

### V2.6.1 What is not claimed

This contract does **not** claim that an ordinary scheduled userspace
process can physically execute at or before a monotonic deadline under
every host schedule, cgroup throttle, or runnable-queue delay. v1’s
serial-loop physical guarantee is deleted.

### V2.6.2 Topology

Supervisor spawns exactly one freezer watchdog (role `WATCHDOG` in
spawn intent). Watchdog holds **no** lock, **no** capability, **no**
right to write `runtime/` or append the ledger. Communication: two
`pipe2(O_CLOEXEC)` pairs — supervisor→watchdog updates,
watchdog→supervisor acks/events. Watchdog polls at most every
`T_WATCHDOG_POLL_INTERVAL_NS` using
`time.clock_gettime_ns(CLOCK_MONOTONIC)`.

### V2.6.3 Lease table and ack

Supervisor, after every locked renew/remove/claim-start, atomically
replaces `WATCHDOG/LEASES.json` keys exactly:

```text
schema, scientific_outcome, supervisor_generation_sha256,
table_seq (int, strictly increasing), updated_monotonic_ns,
leases (list of {process_id, pgid, start_identity, deadline_ns})
```

and writes the same payload on the update pipe. Watchdog must
acknowledge `table_seq` within `T_WATCHDOG_UPDATE_ACK_TIMEOUT_NS` or
is treated dead (§V2.6.6). Stale `table_seq` updates are ignored.

### V2.6.4 Freeze sequence (identity-safe)

When watchdog’s clock shows `now_ns >= deadline_ns` for a lease row:

1. verify `/proc/<leader>/stat` start identity matches;
2. `killpg(pgid, SIGSTOP)`; sample `freeze_ns =
   clock_gettime_ns(CLOCK_MONOTONIC)`;
3. if still runnable/unknown, `killpg(pgid, SIGKILL)`;
4. emit freeze event on the event pipe; supervisor persists
   `t-freeze-observation.v1`:

```text
schema, scientific_outcome, process_id, pgid, start_identity,
deadline_ns, freeze_ns, overrun_ns, killer (WATCHDOG|SUPERVISOR),
table_seq, created_utc
```

`overrun_ns = max(0, freeze_ns - deadline_ns)`. Observation hash binds
those fields. If the pipe event is lost, supervisor re-derives by
sampling stopped/dead group vs durable deadline (re-derivable witness).

### V2.6.5 Positive overrun → invalidity (not a valid T ending)

If `overrun_ns > 0`, the sole supervisor **must** settle that process
(and apply sibling rules as signed) on the **invalid / recovery**
route already authorized by the harness + batch amendment
(`T_PROCESS_INVALID` / `RECOVERY_SETTLEMENT` / infrastructure cause
`PROCESS` or `CLOCK` per §2a precedence) — **never** as
`T_PROCESS_VOLUNTARY_STOP`, `T_PROCESS_CLOSED`,
`T_PROCESS_E1_EXHAUSTED`, or `T_PROCESS_E3_DUE` from that overrun.
E1 charge still follows signed §4c (actual interval retained in full).
Numeric cap facts may be retained; no valid exhaustion event is
fabricated from an overrun freeze. This is a mechanical validity pin
to the already-signed invalidity destinations — **not** a new author
cell and **not** a physical scheduling guarantee.

Zero overrun (`freeze_ns <= deadline_ns`) may still continue ordinary
watchdog settlement (heartbeat renew or §4c as signed) without forcing
invalidity solely from the freeze.

### V2.6.6 Death / restart automata

| Event | Continuation |
|---|---|
| Watchdog death / ack timeout / identity mismatch | Supervisor freezes all live groups itself, persists freeze observations, refuses new admissions until a new watchdog is spawned and has acked `table_seq`, then settles any overdue per §V2.6.5 / §4c |
| Supervisor death | Watchdog freezes all known groups and exits; does **not** settle; next CLI takeover settles |
| Stale update / wrong generation | Watchdog ignores; supervisor treats missing ack as death |
| PID reuse on controller | Freeze skipped; stream lost → §4c(c)/batch |
| Watchdog spawn failure | No admissions; refuse `CLAIM`/`START`/`OPERATION_ADMIT` |

---

## V2.7 Operations, output bound, promotion

### V2.7.1 Output bound before behavior (no global GiB)

Signed `t-draft-manifest.v1` keys are **not** amended. Before any
worker is spawned, the supervisor requires a durable
`t-operation-output-bound.v1` at
`operations/<pending_op_key>/BOUND.json` keys exactly:

```text
schema, scientific_outcome, process_id, active_lease_sha256,
operation_kind, input_sha256, declared_stream_indexes,
max_total_output_bytes, created_utc
```

`max_total_output_bytes` is a **positive** `int` declared per
operation (controller-supplied via the admit path after bound
install). No universal constant is invented. Admission refuses if
bound missing, non-positive, or `type is not int`.

**Reserve/refuse:** under the lock, record
`bytes_reserved = max_total_output_bytes` on the admission; refuse if
concurrent reserved bytes across live ops would be unbounded only by
count — concurrency already ≤ `MAX_CONCURRENT_LEASES`; each op carries
its own frozen bound. Spawn occurs only after `BOUND.json` +
`OPERATION.json` are durable.

### V2.7.2 Byte accounting rules

After worker+group proved dead, before hashing content:

- Enumerate `out/` with directory-fd + `O_NOFOLLOW`;
- Accept only regular files, nlink==1, no symlink/device/FIFO/socket;
- Path grammar: relative, no empty, no `.`/`..`, no absolute, no NUL,
  unique, depth ≤ 2, count ≤ `16 * device_units`;
- **Logical bytes** = sum of `st_size`; **allocated bytes** = sum of
  `st_blocks * 512`;
- If either sum > `max_total_output_bytes` → **invalidate** the
  operation (no content hash of the excess; quarantine; no promotion);
  settle streams per §4c; release reservation on that terminal only;
- Sparse files count full logical `st_size` toward the bound (fail-
  closed against cheap huge sparse files);
- Hardlinks (nlink≠1) refused before read;
- Read/hash in bounded chunks; loop restartable from descriptor
  offset after crash without re-spawning the worker;
- Reservation releases on exactly one durable terminal:
  `SETTLEMENT.json` commit, or `FAILED` quarantine record
  (`phase=FAILED` journal/admission update).

### V2.7.3 Admission and confined execute

`operation_id` = SHA-256 of canonical
`{activation_record_sha256, process_id, active_lease_sha256,
operation_kind, input_spec, declared_stream_indexes,
max_total_output_bytes, pre_operation_reading_ns,
output_bound_sha256}`.

Worker: supervisor child, `start_new_session=True`, status pipe only,
writes only under `operations/<operation_id>/out/`. No control
endpoint. Status schema
`t-worker-status.v1` keys:
`schema, scientific_outcome, operation_id, output_relative_paths,
exit_reason` ∈ {`COMPLETED`,`FAILED`} — paths still subject to
supervisor grammar; worker claims are not trusted for hashing.

### V2.7.4 Promotion order and single commit

```text
bound+admit durable → spawn worker → worker exit+group-empty
→ revoke output authority → bound check (logical+allocated)
→ hash by descriptor (O_NOFOLLOW) in sorted path order
→ settle under lock (one §2c.5 charge for occupied streams)
→ write SETTLEMENT.json (atomic no-replace) = COMMIT POINT
→ idempotent os.replace of out/ into T_PROMOTED/<operation_id>/
→ deliver release token via journaled OPERATION_STATUS
```

`SETTLEMENT.json` keys exactly:
`schema, scientific_outcome, operation_id, charge_event_sha256,
result_sha256, promoted_relative_paths, bound_sha256, settled_utc`.

Crash with rename done but `SETTLEMENT.json` absent → **not**
promoted; quarantine; charge stands; §6c for disposal. Crash with
`SETTLEMENT.json` durable and rename incomplete → complete rename
idempotently; never re-charge. Wrong/old/sibling/caller-named charge
cannot promote: only the charge-event captured in the same settle step
is written into `SETTLEMENT.json`.

### V2.7.5 Stream ownership (`k>1`)

Claim declares `device_units = k` streams with canonical indexes
`1..k`. Live exclusive ownership table (supervisor memory + rebound
from admissions): each stream index owned by at most one live
operation. `declared_stream_indexes` must be sorted, unique, nonempty,
subset of `1..k`, and free. Release on operation terminal. Coextensive
known charge = `k * elapsed` only when the settlement covers all k; an
operation subset charges only its streams’ readings (sum into one
process event per signed aggregation). All-live E1/E3/invalidity batch
still freezes the **complete** live lease set (amendment F1).

---

## V2.8 Metering, boundaries, §S6 repair ledger (carried)

Supervisor owns monotonic readings and stream tables. Ordinary
heartbeat/watchdog/close that reach E1, E3-due, G5, or lost-stream
recovery **must** enter the signed all-live frozen batch — never
fabricate a successor reservation; never counter-only G7/G2.
Event/artifact-backed terminals only. `ARCHIVE` before `RESOLVED`;
registry blocks until archival commit. D1 head/cache completion from
**raw statically parsed** ledger suffix when external head lags, with
old/new bindings and immediate full verification. G5 scoped to
invalidities since last valid admission; disposition author parents
verified. Ordinary §3 cuts at next admission; **close in one lock
epoch**. Private claim-backed `BatchSettlementAuthority` only; strict
`type(x) is int`. Both review-record
`ledger_entry_sha256` and `ledger_head_sha256` bind the durable
pre-review head (acyclicity regression required). Caller-supplied
current head remains required by `charge_batch_settlement`. Archival
needs implementation, not another contract cell. Full-live-set /
omission proofs as signed amendment.

---

## V2.9 State / transition summary

### V2.9.1 Supervisor generation states

`ABSENT → SPAWNING(lock held) → LIVE(watchdog acked) → TAKEOVER →
LIVE | TERMINAL_DRAIN (G3/G5/G6/G7, zero leases, journal/batch quiet)`.
No `IDLE_EXIT`.

### V2.9.2 Process states

Signed P0…P5 with v2.1.4 bootstrap inserts: spawn-intent → stopped
child → claim → start → lease/capability → live ↔ heartbeat →
close/invalid/batch.

### V2.9.3 Operation states

`BOUND → ADMITTED → RUNNING → PENDING_SETTLEMENT → PROMOTED|FAILED`.

### V2.9.4 Archival exclusions

Never stage: `runtime_control/**`, `runtime/T_PROMOTED/**`. Signed
activation-protocol §B sets otherwise unchanged.

---

## V2.10 CLI and production boundary

Sole root: `src/philosophia/officina/generic_harness.py`. Commands:
`claim start heartbeat close pause resume` (CLI) plus internal serve /
watchdog entry points in the **same** module (no new `scripts/*.py`,
no seventh public command). Argv rule: read `/proc/self/cmdline`,
NUL-split, drop trailing empty; find first (`-m`,
`philosophia.officina.generic_harness`) pair; remainder is
`[command,*args]` or internal `--supervisor-serve` /
`--watchdog-serve` tokens used only by double-fork/spawn (not public
CLI; refusal-first if invoked without supervisor parentage checks).
Public unknown command → exit 2. Allowlist delta: **none**. Frozen
files (byte-unchanged): `runtime.py`, `ledger.py`, `checkpoint.py`,
`verification.py`, `activation.py`, signed events/schemas/constants,
roots tuple. Future edit surface after token+confirmation:
`generic_harness.py`, its tests, signed accounting amendment surface
only.

---

## V2.11 Crash-cut matrix (selected)

| Cut | Continuation |
|---|---|
| Spawn intent, no child | delete/refuse intent; no claim |
| Child stopped, no claim | takeover kills by intent identity |
| Claim durable, no start | orphan-claim invalidity; no id reuse |
| Journal ACCEPTED, effect incomplete | resume effect from phase; no double apply |
| Reply lost | return cached reply for same key |
| Freeze observed, settle pending | supervisor settles invalid if overrun>0 |
| Worker done, bound exceeded | FAILED; no hash beyond bound; reservation released |
| Hash done, no SETTLEMENT | quarantine; charge if already settled else §4c |
| SETTLEMENT durable, promote rename incomplete | complete rename; deliver token |
| Token delivered, no ack | redeliver identical token |
| Ack durable | `ALREADY_DELIVERED` |
| Watchdog dead mid-live | §V2.6.6 |
| Supervisor dead | takeover §V2.1.6 |
| Batch mid-automaton | signed prefix automaton + D1 |

No cut exposes promoted results without `SETTLEMENT.json`. No cut
double-charges a cursor.

---

## V2.12 Acceptance test matrix (finite)

Disposable roots only; no production-compatible real-T artifact.

1. Self-stop bootstrap vs parent-only SIGSTOP race (must use self-stop).
2. Pre-claim crash → automatic takeover kill via CHILDREN registry.
3. Double CLI spawn race → one supervisor (lock through identity).
4. Reparented zombie emptiness (`Z` and ECHILD paths).
5. Role: controller→REQUEST.fifo refused; CLI on controller pipe refused;
   worker control refused.
6. A3 honesty: document/test that mode bits alone are not secrecy;
   role/grammar still enforced.
7. Journal: lost CLAIM/START/HEARTBEAT/CLOSE/PAUSE/RESUME/ADMIT/STATUS
   reply → same key identical reply; different bytes → INVALID; ADMIT
   no second worker/cursor.
8. Token redelivery until ack; post-ack ALREADY_DELIVERED.
9. Watchdog freeze with supervisor busy in archival; overrun>0 →
   invalid route, not valid close.
10. Watchdog death; supervisor death; stale table_seq; PID reuse.
11. Sparse file > bound → FAILED before content hash.
12. Symlink/hardlink/`..` in out/ → refused.
13. SETTLEMENT commit vs rename cuts (single continuation each).
14. Wrong/old/sibling charge cannot promote.
15. `k>1` stream exclusive ownership; mixed known/unknown; all-live batch.
16. Heartbeat E1/E3 → automatic batch; no fabricated reservation;
    event-backed G7/G2; ARCHIVE before RESOLVED.
17. Raw D1 head-lag completion; G5 since last admission continuity.
18. Close one lock epoch; sequence non-reuse across closed generation.
19. Real `python -m philosophia.officina.generic_harness` six commands.
20. Locked promotion; strict int (`True` refused); pre-review-head
    acyclicity.
21. Quarantine verifier: zero new imports beyond allowlist.

---

## V2.13 Finding disposition → section map

| Finding | v2 locus |
|---|---|
| Opus F1 / Sol C3 idempotency | §V2.5, §V2.4.2 |
| Opus F2 / Sol C1/C2 confinement | §V2.2 (A3) |
| Opus F3 / Sol C4 self-stop | §V2.1.4 |
| Opus F4 pre-claim orphan | §V2.1.4–V2.1.6 |
| Opus F5 singleton lock | §V2.1.2 |
| Opus F6 / Sol C5 watchdog | §V2.6 (honest C1) |
| Opus F7 zombies | §V2.1.6 |
| Opus F8 pre-claim logs | §V2.1.4 |
| Opus F9 / Sol M1 schemas | §V2.4.3–V2.4.5 |
| Opus F10 roles | §V2.2.2 |
| Opus F11–F12 / Sol M3 promotion | §V2.7 |
| Opus F13–F15 FIFO/archival/subset | §V2.4.1, §V2.9.4, §V2.7.5 |
| Sol M2 FIFO encoding | §V2.1.3, §V2.4.1 |
| Sol M4 streams | §V2.7.5 |
| Sol M5 idle exit | §V2.1.1 D1 |
| Codex C1–C4 / M1–M6 | §V2.8 + topology/promotion |
| Output byte DoS | §V2.7.1–V2.7.2 |

---

## V2.14 Governance and negative space

This v2 is an engineering/control amendment surface over the signed
harness composite. It does not move E1/E2/E3 constants, nine events,
runtime schemas, roots, T/Q/C boundaries, batch arithmetic, or
scientific cells. New artifacts are control-plane /
T-development-only. `I_ACCEPT_OFFICINA_SUPERVISOR_CONTROL_CHANNEL_AMENDMENT`
remains **not signable** until both fresh X/Y reviews accept this v2.
No implementation, activation, manifest, capability, world, learner,
entropy, spend, or claim movement is authorized. T remains
`NOT_ACTIVATED`; the programme claim remains `OPEN`.
