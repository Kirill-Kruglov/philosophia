# Officina supervisor and control-channel amendment — v1 draft

Status: `CANDIDATE_FOR_XY_REVIEW_NOT_AUTHORIZED`. This is the one
bounded engineering/control correction that the implementation reviews
(Codex `REVISE_IMPLEMENTATION`; Opus `REVISE…` with a `BLOCKED_CONTRACT`
sub-finding; Sol `BLOCKED_OFFICINA_GENERIC_HARNESS_CONTRACT`, R0)
required before Cursor may implement §5 of the signed composite. It
corrects **exactly** the persistent supervisor/watchdog topology, the
closed control channel, and the confined worker→supervisor result and
promotion protocol — signed v2 §1 (ownership pins), §2c.1–2c.6, §5a,
§5b, §9 (argv/import discipline), and the corresponding §10 rows.
Review-evidence base: uncommitted Cursor work audited at
`5c00d5ffa9f67b6907bd370b9efccaf542646ba4`.

It reopens **no** batch-settlement science, resource constant, signed
event, runtime schema, T/Q/C boundary, or any signed cell. It selects
exactly **one** topology; no alternative is left for Cursor. It
implements nothing, edits no code, creates no runtime artifact,
manifest, authorization, capability, process, entropy, or spend; T
remains `NOT_ACTIVATED`. Author token candidate (not yet signable):

```text
I_ACCEPT_OFFICINA_SUPERVISOR_CONTROL_CHANNEL_AMENDMENT
```

**Replacement/addition index over the signed composite (everything
else carries forward verbatim):**

| Signed locus | Action |
|---|---|
| v2 §1 ownership paragraph ("The supervisor process is the sole holder …") | **completed** by §S1 (which OS process; creation; lifetime) |
| v2 §2c.1–2c.3 (claim/start/lease) | **completed** by §S1.3 (controller spawned stopped before the claim; real identities and argv in the signed claim keys) |
| v2 §2c.4–2c.5 (operation admission; heartbeat) | **completed** by §S1.5/§S3 (autonomous supervisor settlement; channel-admitted operations) |
| v2 §2c.6 (close) | **completed** by §S1.5 (one lock epoch, supervisor-executed) |
| v2 §5a sentence "Each controller tree runs under a separate supervisor" | **replaced** by §S1.1 (one singleton runtime supervisor owning every controller tree; per-tree sessions) |
| v2 §5b | **completed** by §S3 (exact confined channel, promotion order, crash cuts, token delivery) |
| v2 §9 argv/import paragraphs | **completed** by §S5 (exact `-m` parsing rule; proof of zero allowlist delta) |
| v2 §10 matrix | **extended** by §S7 rows |
| — (new) | §S2 closed control channel; §S4 boundary integration; §S6 deterministic repair ledger |

Engineering control constants introduced here (not scientific
choices): `T_SUPERVISOR_POLL_INTERVAL_NS = 100_000_000`,
`T_CONTROL_FRAME_MAX_BYTES = 4096`,
`T_CONTROL_READ_TIMEOUT_SECONDS = 10`,
`T_CLIENT_REPLY_TIMEOUT_SECONDS = 30`,
`T_SUPERVISOR_IDLE_EXIT_SECONDS = 60`. Integer Linux signal numbers
used (no `signal` import): `SIGCONT = 18`, `SIGSTOP = 19`,
`SIGKILL = 9`, `SIGTERM = 15`, liveness probe `0`.

---

## S1. Process topology and lifetime

### S1.1 The one topology

There is exactly **one persistent runtime supervisor process per
repository generation**. It is simultaneously the §1 sole
`T_RUNTIME.lock` holder (per §3 transaction epoch; never held at
rest), the sole writer of every durable runtime artifact, the sole
issuer/revoker of real-T capabilities, the watchdog for every lease,
and the sole parent of every controller and worker. The signed §5a
sentence "each controller tree runs under a separate supervisor" is
**replaced**: each controller tree runs in its **own session and
process group owned by the one supervisor**. `claim`, `start`,
`heartbeat`, `close`, `pause`, and `resume` are **separate short-lived
CLI client processes**: each verifies the supervisor generation, sends
exactly one request frame, waits for exactly one reply, prints the
refusal-first result, and exits. Clients never take `T_RUNTIME.lock`,
never write a runtime artifact, and never hold a capability.

### S1.2 Supervisor creation (no new command, no daemon executable)

Any CLI command needing a live supervisor ensures one exists, under an
exclusive `flock` on `successor/officina/runtime_control/T_SUPERVISOR/SPAWN.lock`
(`O_RDWR|O_CREAT|O_CLOEXEC`):

1. read `SUPERVISOR_IDENTITY.json` (§S2.2) if present; the recorded
   generation is **live** iff `os.kill(pid, 0)` succeeds **and** the
   recorded kernel start identity equals the current
   `/proc/<pid>/stat` start identity (§S1.4) **and** the recorded boot
   identity equals the current `/proc/sys/kernel/random/boot_id`;
2. if live: release the spawn lock and address that generation;
3. if absent/stale: perform the **takeover scan** (§S1.6), then spawn
   the new supervisor by **double fork** from the CLI client itself:
   `os.fork()` → child calls `os.setsid()` → `os.fork()` → grandchild
   is the supervisor (same module image; **no new argv command, no
   script, no daemon executable, no dynamic import**); intermediate
   exits; the supervisor closes every inherited descriptor except its
   freshly created endpoints, redirects stdin/stdout/stderr to
   `os.devnull`, creates the endpoints and identity record (§S2.2),
   and enters the serve loop; the CLI waits (bounded by
   `T_CLIENT_REPLY_TIMEOUT_SECONDS`) for the identity record to become
   live, then proceeds.

The supervisor's lifetime: it exits cleanly **only** when zero live
leases exist ∧ no unresolved batch claim ∧ no pending operation ∧
(global state ∈ {G3, G4, G5, G6, G7} ∨ it has been idle in G1/G2 for
`T_SUPERVISOR_IDLE_EXIT_SECONDS`). Clean exit order: unlink
`REQUEST.fifo` → unlink `SUPERVISOR_IDENTITY.json` → exit 0. Crash,
kill, orphan, and power loss all leave the identity record stale; the
next CLI invocation detects staleness (identity/liveness/boot check)
and performs takeover. The supervisor never restarts itself; restart
is always a fresh generation created by S1.2.

### S1.3 Claim/start/lease ordering (completes §2c.1–2c.3)

- **`claim` (P0→P1):** inside the supervisor's one §3 lock epoch, it
  first spawns the controller — `subprocess.Popen` with
  `start_new_session=True`, `shell=False`, argv = the exact list
  returned by the reviewed adapter's pure `controller_argv(claim
  inputs)` function (interpreter path = `os.readlink("/proc/self/exe")`),
  env = the pinned minimal allowlist (`OFFICINA_REPOSITORY` plus
  locale/`PATH` fixed values), stdin `os.devnull`, stdout/stderr
  redirected to controller log files under the process's
  `runtime_control` operations directory, `pass_fds` = exactly the two
  controller-channel descriptors (§S2.3) — then immediately freezes it
  (`os.kill(pid, 19)`), captures the real `controller_pid`, kernel
  `controller_start_identity` (§S1.4), `process_group_id`
  (= the child pid, being a new session), boot identity, and writes
  the signed `t-process-claim.v1` with **exactly those observed values
  and that exact argv** (the signed keys `controller_pid`,
  `controller_start_identity`, `process_group_id`, `argv` — no schema
  change). The controller performs no work while stopped. Crash after
  spawn, before the durable claim: the frozen child is an
  unrecorded... it is recorded nowhere durable, so the takeover scan
  kills any session whose leader start identity is not bound by a
  durable claim only if it was spawned by a supervisor generation
  (session leaders are children of the dead supervisor and are
  reparented; they hold only CLOEXEC-scrubbed FDs and remain stopped —
  the scan enumerates durable claims/leases; a stopped spawn with no
  claim is terminated by the operator route or dies at boot; it can
  never acquire a capability). Crash after the durable claim, before
  `start`: the signed orphan-claim route governs; takeover kills the
  recorded group (identity-verified) before any admission.
- **`start` (P1→P2):** supervisor validates the durable claim,
  verifies the frozen controller's identity against it, appends
  `T_PROCESS_STARTED`. Next: lease only.
- **Lease (P2→P3):** in the same generation, supervisor reserves per
  §4b, installs the lease (seed rule unchanged), constructs the
  in-memory `RealTCapability` **held by the supervisor only** and
  bound to activation record, process id, source HEAD, T bands, and
  lease identity, and only then thaws the controller
  (`os.kill(pid, 18)`). The controller and worker never receive the
  capability object, the lock descriptor (`O_CLOEXEC`, never in
  `pass_fds`), or write access to durable runtime paths (procedural +
  §S3 confinement; §5a threat model unchanged).

### S1.4 Kernel start identity (exact acquisition)

`start_identity(pid)` = the 20th whitespace-separated token after the
**final** `)` in `/proc/<pid>/stat` (the kernel `starttime` field 22;
parsing after the final parenthesis survives spaces in `comm`),
concatenated with `:` and the boot identity. PID reuse is defeated by
comparing this string at every admission, settlement, watchdog action,
takeover kill, and control-frame validation.

### S1.5 Watchdog, heartbeat, close (completes §2c.5–2c.6)

The supervisor's serve loop sleeps at most
`T_SUPERVISOR_POLL_INTERVAL_NS` per iteration and on every iteration
compares `time.clock_gettime_ns(CLOCK_MONOTONIC)` against every live
lease deadline. **Firing rule:** when `now + T_SUPERVISOR_POLL_INTERVAL_NS ≥
deadline`, the supervisor acts, guaranteeing initiation **at or before
the deadline with no later CLI invocation** — the watchdog is
genuinely persistent, not lazy. Action: if every §2c.4 revalidation
passes (group membership via the identity-verified pgid, declared
streams reconciled, control bytes, clocks), it performs the ordinary
§2c.5 heartbeat settlement and renewal autonomously; otherwise it
executes the signed v2.1 §1 sequence — revoke (in-memory capability
invalidated; channel refuses further operations) → freeze
(`os.killpg(pgid, 19)`) → capture cursors → terminate
(`os.killpg(pgid, 9)`; reap via `os.waitpid`; group-empty proof =
`os.killpg(pgid, 0)` raising `ProcessLookupError`) → backend
synchronize (CPU adapter: group-empty is the proof) → durably settle
per §4c, routing to the §S4 boundary batch where required. The
`heartbeat` CLI command requests exactly the same settlement
immediately; it adds no alternative path. **`close`** executes the
entire signed §2c.6 sequence — quiesce → final charge → final record →
`T_PROCESS_STOPPED` → head/cache → verified lease removal → archival —
inside **one supervisor lock epoch** (no epoch split). If the
supervisor is dead and no CLI ever arrives, no process exists that
could act; that is precisely the signed §4c process-loss/reboot fault
class, and its conservative settlement at the next lock entry is the
signed disposition — the ordinary mechanism remains the persistent
in-process watchdog above.

### S1.6 Takeover scan (stale generation)

Under the spawn lock, before a new supervisor serves: enumerate
durable claims and active leases; for each recorded controller group,
compare the recorded start identity (§S1.4); on match, `os.killpg`
(15, then 9 after one poll interval), reap, prove group-empty; on
mismatch (PID reused), **do not kill** — record the fact and treat the
stream as lost. Unlink stale control endpoints (`REQUEST.fifo`, reply
FIFOs, `SUPERVISOR_IDENTITY.json`) — these are transient control
plane, never durable evidence; **no durable artifact is ever cleaned**.
Quarantined operation outputs (§S3.6) are preserved untouched. Then
settle every affected stream per §4c/§4d (the §S4 batch where
required), honor the unresolved-claim registry, and only then admit
new work. Every takeover action uses only durable facts plus the
identity checks; two implementers converge.

## S2. Closed control channel

### S2.1 Transport (allowlisted primitives only)

Named FIFOs and inherited pipes; no sockets, no `select`, no signals
for data. Endpoint directory:
`successor/officina/runtime_control/T_SUPERVISOR/` (mode `0700`),
containing exactly: `SPAWN.lock`, `SUPERVISOR_IDENTITY.json`,
`REQUEST.fifo` (`os.mkfifo`, mode `0600`), `REPLY/` (per-request
client FIFOs), and `operations/` (§S3). Nothing under
`runtime_control/T_SUPERVISOR/` is ever staged into an archival set or
hashed into a durable runtime artifact. The supervisor reads
`REQUEST.fifo` via a non-blocking descriptor (`os.open(…,
O_RDONLY|O_NONBLOCK|O_CLOEXEC)`) and polls; clients open write-only,
write one frame, close.

### S2.2 Generation identity record

`SUPERVISOR_IDENTITY.json`, schema
`philosophia.officina.t-supervisor-identity.v1`, canonical ASCII JSON,
keys exactly:

```text
schema, scientific_outcome, activation_record_sha256, supervisor_pid,
supervisor_start_identity, boot_identity, request_fifo, created_utc
```

Atomic no-replace within a generation (replaced only at S1.2/S1.6
takeover under the spawn lock). `supervisor_generation_sha256` =
SHA-256 of the record's canonical bytes. It carries **no result,
learner, or outcome field** and never enters a durable runtime
artifact; `reject_scientific_fields` applies.

### S2.3 Frames (exact)

One frame = one line of canonical ASCII JSON terminated by `\n`,
total ≤ `T_CONTROL_FRAME_MAX_BYTES` (4096 — within `PIPE_BUF`, so
every well-formed client write is atomic; interleaving cannot corrupt
frames). Request keys exactly:

```text
schema ("philosophia.officina.t-control-request.v1"),
scientific_outcome, supervisor_generation_sha256, command, arguments,
client_pid, client_start_identity, client_boot_identity,
client_monotonic_ns, reply_fifo
```

Reply keys exactly:

```text
schema ("philosophia.officina.t-control-reply.v1"),
scientific_outcome, supervisor_generation_sha256, request_sha256,
status, detail
```

`command` ∈ {`CLAIM`, `START`, `HEARTBEAT`, `CLOSE`, `PAUSE`,
`RESUME`} for CLI clients and ∈ {`OPERATION_ADMIT`,
`OPERATION_STATUS`} for controllers (§S3); `arguments` is the
command's exact closed key set (the six CLI commands take exactly
their signed CLI arguments); `status` ∈ {`OK`, `REFUSED`, `INVALID`};
`detail` contains only closed non-outcome fact classes (v2 §F) — never
a result hash before promotion, never free text beyond fixed refusal
tokens. `request_sha256` = SHA-256 of the request's canonical bytes.

**Rules (exact):** the supervisor handles requests strictly serially,
one reply per request, written to the request's `reply_fifo` then
closed. `reply_fifo` must be
`REPLY/<client_pid>-<client_start_identity_hex>-<client_monotonic_ns>.fifo`,
created by the client (mode `0600`) before sending and unlinked by the
client after reading — names are fully deterministic; **no entropy
exists anywhere in the channel**. Identity binding: the supervisor
verifies `client_pid`'s live start identity equals
`client_start_identity` and the boot identity matches before acting;
mismatch → `INVALID`, no action. Generation binding: a frame whose
`supervisor_generation_sha256` differs from the serving generation →
`REFUSED` (`STALE_GENERATION`), no action — an old client addressing
a new generation, or a substituted peer, is thereby excluded.
**Replay:** the pair (`client_start_identity`, `client_monotonic_ns`)
must strictly increase per client within a generation; a repeated or
non-increasing value → `REFUSED` (`REPLAY`), no action. **Partial
frame:** if no `\n` arrives within `T_CONTROL_READ_TIMEOUT_SECONDS` of
the first byte, or a frame exceeds the maximum, the buffered bytes are
discarded with no action. **EOF** on an empty buffer is normal
(writers come and go); EOF mid-frame discards the fragment.
**Disappearing endpoints:** a client whose reply FIFO cannot be opened
or written gets no reply (the transaction outcome stands — commands
are refusal-first and idempotence comes from the durable state, so a
retried request is re-validated, never re-applied); a client waiting
longer than `T_CLIENT_REPLY_TIMEOUT_SECONDS` exits with the refusal
exit code and takes no action. A blocked/full FIFO never blocks the
watchdog: all supervisor channel I/O is non-blocking with the poll
loop.

### S2.4 Descriptor custody

Every supervisor descriptor is `O_CLOEXEC`. Controller channel = two
`os.pipe2(os.O_CLOEXEC)` pairs created at spawn; only the child-side
ends are passed via `pass_fds` (their `CLOEXEC` cleared by
`subprocess` for exactly those fds). Controllers hold exactly:
request-write fd + reply-read fd. Workers hold exactly: one
status-pipe write fd (§S3.3). Neither ever holds the lock descriptor,
the request FIFO, another process's pipes, or an endpoint path
capability beyond these. CLI clients touch only `SPAWN.lock`, the
identity record (read), `REQUEST.fifo` (write), and their own reply
FIFO. Cleanup of endpoints occurs only at S1.2/S1.6 takeover or clean
exit; quarantined outputs only under the signed §6c disposition.

## S3. Confined operation and promotion (completes §5b)

### S3.1 Request and identity

A controller requests a behavior-capable operation with
`OPERATION_ADMIT`; `arguments` keys exactly: `process_id`,
`operation_kind` ∈ {`ORACLE_QUERY`, `LEARNER_UPDATE`,
`CHECKPOINT_WRITE`}, `input_spec` (closed object of exact input
hashes; no free text), `declared_stream_indexes` (the claim-declared
streams the operation occupies). The supervisor revalidates §2c.4
under the lock, then computes
`operation_id` = SHA-256 over the canonical JSON of
`{activation_record_sha256, process_id, active_lease_sha256,
operation_kind, input_spec, declared_stream_indexes,
pre_operation_reading_ns}` — where `pre_operation_reading_ns` is the
monotonic cursor captured at admission. That id binds activation,
process, lease, adapter streams, and the pre-operation meter cursor;
the result hash and the one post-operation charge event are bound at
promotion (§S3.4). The reply is `OK` with `operation_id` only — **no
result-bearing field**.

### S3.2 Admission record

Before spawning the worker the supervisor writes
`runtime_control/T_SUPERVISOR/operations/<operation_id>/OPERATION.json`
(atomic no-replace), keys exactly: `schema
("philosophia.officina.t-operation-admission.v1")`,
`scientific_outcome`, `operation_id`, `process_id`,
`active_lease_sha256`, `operation_kind`, `input_spec`,
`declared_stream_indexes`, `pre_operation_reading_ns`,
`supervisor_generation_sha256`, `created_utc`. It contains **no
result-bearing field, ever** (pre-settlement result information must
remain hidden; post-settlement binding lives in `SETTLEMENT.json`
below, which carries the charge-event hash and promoted path but
still no result hash — result identity is recomputed from promoted
bytes).

### S3.3 Confined execution

The worker is a **child of the supervisor** (never of the
controller): `subprocess.Popen`, `start_new_session=True`,
`shell=False`, argv = the adapter's pure `worker_argv(OPERATION.json)`
function, env pinned as in §S1.3, stdin `os.devnull`, stdout/stderr →
log files inside the operation directory, `pass_fds` = exactly one
status-pipe write fd. The worker writes its output bytes only inside
`operations/<operation_id>/out/` and, on completion, one status frame
(`schema "philosophia.officina.t-worker-status.v1"`, keys exactly:
`schema, scientific_outcome, operation_id, output_relative_paths,
exit_reason`) on the status pipe, then exits. The worker inherits no
capability, no channel endpoint, no lock, no controller pipe — it
**cannot** initiate another behavior-capable operation or reach the
controller; the controller holds no fd, path grant, or map into the
operation directory (same-user filesystem residual is the signed §5a
threat model, tightened by §S3.6's `0000` quarantine mode). The
supervisor monitors via non-blocking status-pipe reads plus
`os.waitpid(pid, os.WNOHANG)` in the poll loop; lease deadlines keep
running — an operation outliving its lease deadline triggers §S1.5
watchdog action on its group.

### S3.4 Promotion order (exact, single-valued)

```text
admit under lock (S3.1–S3.2)
→ execute confined (S3.3)
→ revoke output authority: close status pipe; prove worker exit
  (waitpid) and group-empty (killpg 0 → ProcessLookupError); chmod the
  operation directory 0000
→ quiesce/terminate: any survivor → killpg 19, cursor capture,
  killpg 9, reap, re-prove empty
→ backend synchronize (CPU adapter: group-empty proof)
→ hash: supervisor chmods 0700, opens and hashes the exact output
  bytes itself (never trusting a worker-reported hash)
→ settle under lock: one ordinary §2c.5 settlement charging this
  operation's stream cursor delta; the resulting T_DEVICE_TIME_CHARGED
  entry hash is captured in the same lock epoch
→ atomically promote: os.replace of the output set into
  successor/officina/runtime/T_PROMOTED/<operation_id>/ (supervisor-
  written durable T-development artifacts); write SETTLEMENT.json
  (keys exactly: schema
  ("philosophia.officina.t-operation-settlement.v1"),
  scientific_outcome, operation_id, charge_event_sha256,
  promoted_relative_paths, settled_utc) atomically no-replace
→ issue/deliver the one-use release token
```

The token binds exactly the signed six fields (activation record,
process id, lease hash, operation id, result hash, charge-event hash);
it exists **in supervisor memory only**, is delivered exactly once as
the `detail` of the first `OPERATION_STATUS` reply whose status is
`PROMOTED`, and is marked consumed on delivery; every later status
query returns `ALREADY_DELIVERED` without the token. Tokens are
generation-local: a new generation never re-issues one. What the
controller actually receives: the token fields plus
`promoted_relative_paths` — nothing earlier, and never a
pre-settlement result hash.

### S3.5 Rejection of wrong charges

Promotion consumes only the charge-event hash captured inside its own
settle-under-lock step of the same operation and generation. An old
charge, a pre-operation charge, a sibling-process charge, or any
caller-named event is structurally unusable: no API accepts an
external charge hash for promotion.

### S3.6 Failure, disposal, and crash cuts

Any of: settlement failure, killed/escaped worker, queue ambiguity,
invalid close, generation death — **exposes no result**: the
operation directory is set to mode `0000` (quarantine) and retained;
disposal or reuse of quarantined output is selected **only** by the
signed §6c recovery disposition, never by inspecting the result.
Cuts (exactly one continuation each):

| Durable at crash | Continuation |
|---|---|
| admission record only; worker never spawned or incomplete | takeover kills the group (identity-verified); interval settled per §4c; quarantine; no promotion |
| worker output complete; no settlement | same — §4c conservative settlement covers the interval; quarantine; the result is never exposed without its own settlement |
| settlement charge durable; `SETTLEMENT.json` absent or promotion rename incomplete | the charge stands (never re-charged); the operation follows the failure route: quarantine + §6c; no promotion outside the admitting generation |
| promotion durable; token undelivered at generation death | promoted artifacts are durable T-development data; the token is never re-issued; later use is governed by the T-development artifact rules |

No cut can double-charge (each charge is one §2c.5 settlement of a
monotonic cursor delta; recovery uses §4c, which settles the same
cursor once), and no cut exposes a result without its own durable
settlement.

## S4. Metering and boundary integration (references only; no redesign)

The supervisor owns every monotonic reading and the declared-stream
table: per-stream enumeration follows the signed claim
(`device_units = k` ⇒ `k` declared streams; coextensive known charge =
`k × elapsed`; non-coextensive and mixed known/unknown streams are
classified **per stream** per v2.2 A1 and witnessed inline per the
signed claim witness). When any autonomous or requested settlement
would reach/cross E1, reach E3-due, enter G5, or settle lost streams,
the supervisor does **not** renew: it constructs the signed all-live
frozen batch claim (amendment §1, full-live-set rule) and runs the
signed automaton through `ARCHIVE` under its own generation, exactly
as signed — no fabricated successor reservation exists anywhere; no
counter-only valid terminal exists (G7/G2 are event/artifact-backed);
no live sibling survives a boundary. The batch arithmetic, witness,
automaton, D1 completion, and override are referenced unchanged.

## S5. CLI and production boundary

- Sole harness root unchanged:
  `src/philosophia/officina/generic_harness.py`; commands exactly
  `claim start heartbeat close pause resume`; refusal-first.
- **Exact argv rule:** read `/proc/self/cmdline`, split on NUL,
  drop the trailing empty token; locate the **first adjacent pair**
  (`-m`, `philosophia.officina.generic_harness`); the tokens after the
  pair are `[command, *args]`. Any other invocation shape (no such
  pair, unknown command, wrong arity) exits 2 refusal-first with no
  artifact. No `sys` and no argument-parser import is used or needed.
- Commands communicate exclusively with the persistent supervisor via
  §S2; a command proves it addresses the right generation by embedding
  `supervisor_generation_sha256` read from the live-verified identity
  record, and the supervisor refuses any other generation's frames.
- **Import/allowlist proof (no delta):** every primitive used —
  `os.fork/setsid/pipe2/mkfifo/open/read/write/close/waitpid/killpg/
  kill/replace/chmod/readlink`, `fcntl.flock`,
  `subprocess.Popen(start_new_session=True, pass_fds=…)`,
  `time.clock_gettime_ns/sleep` — is a member of the already-pinned
  `ALLOWED_ABSOLUTE_IMPORTS` modules (`os`, `fcntl`, `subprocess`,
  `time`). No `socket`, `select`, `signal`, `sys`, `threading`,
  `multiprocessing`, or any new module is imported; **no
  `verification.py` change and no allowlist delta is required**, and
  none is smuggled: this claim is itself a §S7 probe (quarantine
  verifier over the implementation). No additional script, daemon
  executable, entry point, dynamic import, plugin discovery,
  test-capability symbol, predecessor dependency, or production
  manifest is created or authorized.

## S6. Deterministic repair ledger (mechanical Cursor obligations; no new design choice)

Carried forward one-to-one from the converged reviews; each is a
direct repair against signed text plus this correction:

1. route every realized E1/E3/invalidity/recovery boundary from
   heartbeat/watchdog/close into the signed batch automatically (§S4);
   never fabricate a successor reservation (Codex/Opus C2; Sol C2);
2. event/artifact-backed global terminals: G7 requires the durable
   `T_ENVELOPE_EXHAUSTED` event, G2/G5 their artifacts — never a
   counter alone (Sol C2);
3. exact per-stream witness incl. `device_units > 1`
   (`k × elapsed`), mixed known/unknown streams, per-stream `m`
   membership; batch authority **private and claim-backed**: no public
   constructor path, every step reloads the canonical installed claim
   file, path/name identity, pre-head snapshot, full live set or
   proved omissions, exact prefix, current head, current state
   (Sol C3);
4. mandatory `ARCHIVE` automaton action before `RESOLVED`; the
   registry blocks until the exact staged commit exists (Codex/Opus
   C3);
5. D1 head/cache completion reachable from a **raw statically parsed
   ledger suffix** when the external head lags, with exact old/new
   head+state authority bindings and immediate full verification
   (Codex/Opus C4);
6. G5 admission predicate scoped to invalidities **since the last
   valid admission**, each disposition's author parent verified
   against durable artifacts (Codex M1; Sol M7);
7. every ordinary §3 crash-cut continuation implemented at next
   admission (start-without-lease, orphan artifact, ledger-ahead-of-
   head, stale cache/lease) and `close` in one lock epoch (Codex M2);
8. global `process_sequence` and process-id non-reuse derived from the
   **complete durable history**, and real kernel start identity
   everywhere (Codex M3; §S1.4);
9. registry revalidation binds every retained claim's
   pre-entry/pre-head to the durable chain and re-proves witness
   integrity and omission proofs before authority (Codex M4; Sol M4);
10. all public reads, capability issue/use/revoke, settlement, and
    promotion under the runtime lock with generation checks
    (Codex M6);
11. real `python -m` CLI parsing per §S5, exercised by tests through
    the actual module invocation (Codex M5);
12. pre-review-head acyclicity regression: **both**
    `ledger_entry_sha256` and `ledger_head_sha256` of the review
    record bind the durable pre-review head (confirmed as the only
    acyclic reading); test asserts equality and that the
    `T_REVIEW_COMPLETED` event immediately succeeds that head and
    binds the record hash;
13. strict integer rejection everywhere (`type(x) is int`; `True` is
    not a charge) (Sol C3).

Confirmed explicitly: the caller-supplied current durable head keyword
of `charge_batch_settlement` **remains required** (the signed prose's
stale-head comparison; confirmed by both reviews); batch archival
needs **implementation, not another contract cell** (staged sets and
fixed trailers are already signed).

## S7. Acceptance-test additions (executable; disposable roots and test-only processes only)

No test creates a production-compatible real-T artifact; supervisor
generations under test run against disposable repository mirrors with
fake clocks/meters where applicable, and real OS processes where the
probe is about processes.

| Probe | Required behavior |
|---|---|
| supervisor death at every §S3.4/§S3.6 cut; controller death; worker death; CLI client death mid-request | no result exposed; no double charge; takeover per §S1.6; single pinned continuation |
| watchdog with **no** later CLI invocation | live supervisor initiates settlement/quiescence at or before every deadline (firing rule §S1.5) |
| PID reuse / wrong start identity (client, controller, worker, supervisor record) | refused/not killed per §S1.4/§S1.6; no misdirected kill |
| framing: partial, oversized, duplicate monotonic, replay, wrong generation, substituted peer, dead reply FIFO, blocked FIFO | discard/refuse exactly per §S2.3; watchdog never blocked |
| inherited fd / pipe / mutable memory / filesystem / temp-output / process-group escape | worker and controller reach nothing beyond §S2.4/§S3.3 custody; escapes revoke and route to §4c |
| result produced but not settled; settled by old/pre-operation/sibling/caller-named charge | never promoted; quarantine + §6c; §S3.5 structural rejection |
| crash around atomic promotion and one-use token delivery | §S3.6 table exactly; token at-most-once; never re-issued cross-generation |
| one- and multi-stream (`k > 1`, mixed known/unknown) E1/E3 boundaries from ordinary heartbeat/watchdog/close | automatic signed batch; no renewed lease survives; event-backed G7/G2/G5 |
| double-fork spawn, clean idle exit, takeover after kill −9, stale endpoints | §S1.2/§S1.6 exactly; durable artifacts untouched |
| real `python -m philosophia.officina.generic_harness` for all six commands | §S5 parsing; refusal-first; artifacts only via the supervisor |
| quarantine verifier over the implementation | zero new imports beyond the pinned allowlist; no entropy; no dynamic import |
| every already-required X/Y repair test (§S6 items 1–13) | as enumerated in the three reviews, verbatim |

## S8. Governance and negative space

This correction is an explicit **engineering/control amendment** to
the signed harness composite (it replaces one §5a sentence and
completes §1/§2c/§5b/§9); it therefore requires its own author token —
`I_ACCEPT_OFFICINA_SUPERVISOR_CONTROL_CHANNEL_AMENDMENT` — which is
declared **not signable** until one bounded X-line and one bounded
Y-line confirmation both accept it. It adds no signed event, no
runtime-schema change, no constant change, no root, no entry point, no
import, no entropy, and touches no scientific cell: no learner,
candidate, architecture, optimizer, device winner, Q predicate, alpha,
endpoint, margin, Q/C numeric, or claim movement. The new closed
control artifacts (`t-supervisor-identity.v1`, `t-control-request.v1`,
`t-control-reply.v1`, `t-operation-admission.v1`,
`t-worker-status.v1`, `t-operation-settlement.v1`) are transient or
control-plane generic-harness artifacts, never signed runtime schemas,
never archival members (except `T_PROMOTED/` artifacts, which are
T-development data), and carry no result-bearing field before
settlement and no entropy ever. T remains `NOT_ACTIVATED`; T and Q
remain permanently non-citable for C1–C6; the programme claim remains
`OPEN`.
