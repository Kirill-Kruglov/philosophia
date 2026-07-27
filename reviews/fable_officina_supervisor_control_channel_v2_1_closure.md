READY_FOR_OFFICINA_SUPERVISOR_V2_1_FINAL_XY_CONFIRMATION

# Fable 5 — Officina supervisor/control-channel v2.1 closure

Companion:
`successor/OFFICINA_GENERIC_HARNESS_SUPERVISOR_CONTROL_CHANNEL_V2_1_CORRECTION.md`.
Evidence commit: `75575c3` (working tree dirty exactly as handed over).

Governing inputs read in full: the v2 draft and its closure; the Opus
(X) and Sol (Y) v2 reviews; the signed supervisor author selections
(A3/B1/C1/D1); the output-capacity packet, its closure, and
`successor/OFFICINA_SUPERVISOR_OUTPUT_CAPACITY_SELECTION_V1_SIGNATURE.md`
(K1); the generic-harness signature; and the signed composite — harness
v2 as corrected by v2.1, v2.2, v2.3, v2.3.1, the batch-settlement
amendment chain, and the activation protocol's §B archival/clean-HEAD
rules. The uncommitted implementation was inspected read-only, for
implementability only.

Exactly two files created. No contract, code, test, signature, review,
or runtime artifact edited; nothing committed or staged. No Officina
process, test, smoke, supervisor, controller, worker, watchdog, FIFO,
journal, pipe, or output transport was run. T remains `NOT_ACTIVATED`.

## 1. Verdict

`READY_FOR_OFFICINA_SUPERVISOR_V2_1_FINAL_XY_CONFIRMATION`.

Not `BLOCKED_OFFICINA_SUPERVISOR_V2_1_AUTHOR_CELL`: the only cell both
reviewers identified — aggregate output capacity — is signed as K1 with
its exact envelope, and no other repair required a policy value or a
provider. Every remaining item resolved to schema keys, an ordering, a
locator, an `errno`, an actor, a bound, or a control-only constant.

Not `BLOCKED_OFFICINA_SUPERVISOR_V2_1_CONTRACT_CONFLICT`: exactly one
sentence of the signed composite is contradicted by the reviewed
non-real-time watchdog rule, and it is superseded **explicitly and by
name** rather than by silence (§W6.5). Nothing else in the composite
moves.

`I_ACCEPT_OFFICINA_SUPERVISOR_CONTROL_CHANNEL_AMENDMENT` remains **not
signable** until both fresh confirmations accept v2.1.

## 2. The five load-bearing surfaces, and what was actually pinned

**B1 without collapsing distinct intents (§W1).** The failure both
lines found is that v2 keyed the journal on the whole frame, so every
real retry became `REPLAY_BYTES` plus a client-triggerable G5. The fix
is not `SHA256(command, arguments)` — successive heartbeats and status
observations share arguments and are distinct effects. Identity is
therefore two-level: an `intent_scope_sha256` over
`{activation record, command, arguments}` and an `occurrence_index`,
with `idempotency_key = SHA-256(scope, occurrence)`. Both derivations
are **recomputed and checked by the supervisor**, so nothing about the
key is trusted and two client implementations are byte-identical.

A durable client intent slot, written and fsynced before the first
send, distinguishes intent from retry mechanically: an occurrence whose
`.done.json` terminal mark is absent is unfinished, so the next
invocation of the same command resends it; otherwise a new occurrence
is allocated. No PID, clock, generation, or entropy enters the key, so
a fresh short-lived CLI process and a supervisor takeover both
recompute it. The journal is four immutable predecessor-bound phase
files, never a mutated no-replace file, and each `accepted.json` binds
a per-command `effect_plan` of content-derived locators — including
`CLOSE`'s and `PAUSE`'s multi-artifact sets, which one
`effect_event_sha256` could not describe. Key reuse with changed
semantics is a plain `INVALID`/`REPLAY_BYTES` with no ledger append and
no G5.

Acknowledgement is split as required: ordinary effect replies are
acknowledged implicitly (successor occurrence, or the owning process's
durable terminal), and only the one-use release token needs an explicit
ack carrying both the token hash and the effect-reply hash — compared
for identity only, never selected on. Status **observation** is
effect-free and unjournaled, so polling grows nothing; GC is bounded by
a permanent per-**scope** tombstone holding one high-water integer,
which is why an entire process's heartbeat history is one small file.

**Spawn, singleton, takeover (§W2).** The pre-claim orphan is closed by
embedding `spawn_intent_id` as fixed argv and discovering it through
`/proc/*/cmdline`; the same predicate finds a half-initialized
grandchild through `spawning_id`. The grandchild now **retains** the
inherited `SPAWN.lock` fd through identity installation, so CLI death
cannot release singleton ownership early — safe precisely because the
`--supervisor-serve`/`--watchdog-serve` argv tokens are deleted and both
supervisor and watchdog use in-process post-fork entry, leaving no
`exec` for `O_CLOEXEC` to interfere with. The self-stop wait is bounded
and nonblocking with one `BOOTSTRAP` refusal and one kill/reap route.
Takeover is split into a client control-plane phase (read, identity-kill,
unlink stale endpoints only) and a supervisor runtime phase (reducer,
§4c/§4d settlement, unresolved batch) under `T_RUNTIME.lock`. The
bootstrap claim is stated as the true invariant — no capability exists
before `SIGCONT` — and the false claim that CPython executes nothing
before self-stop is withdrawn.

**Watchdog C1 (§W3).** The lease table must be published and acked
before the first `SIGCONT`, before capability usability, and before any
admission; an unacked renewal leaves the old deadline authoritative.
`freeze_ns` is now the conservative instant at which every recorded
member and parent/session-chain descendant is proved stopped or dead —
never signal-send time — and the watchdog writes the observation
itself, which is consistent with C1 because `WATCHDOG/**` is control
plane and the watchdog still writes nothing under `runtime/` and never
appends the ledger. Lost evidence yields `freeze_ns = null` and the
unknowable all-live route; v2's "re-derives by sampling" is deleted
because a later sample cannot recover an earlier instant. Since
quiescence is proved strictly after the deadline, the zero-overrun
branch is unreachable and is deleted outright rather than replaced by a
tolerance. Cause is `PROCESS`; `CLOCK` only on an independently
verified fault. `T_PROCESS_RESOURCE_STOP` is named as forbidden, not
left to inference. Ack liveness is judged on the watchdog's own
monotonic sample, so a supervisor inside chunked work cannot kill a
healthy watchdog.

**K1 and the operation transaction (§W4).** `OPERATION_ADMIT` is the
sole installer: `output_bound_sha256` leaves both the arguments and the
`operation_id` preimage, the undefined `<pending_op_key>` is gone, and
nine ordered steps — accepted plan capturing the meter cursor and
deriving `operation_id`, capacity record, bound, admission, worker
spawn intent, bounded worker handshake, committed, reply, `SIGCONT` —
form one crash-reducible plan whose every step is probeable by a
content-derived path. The worker holds no writable output pathname or
descriptor; it emits newline-framed headers plus raw bytes on an
inherited pipe, and the supervisor validates the grammar before
creating anything, writes each file itself, and hashes in the **same
single pass**, servicing one watchdog step and one control step between
4 MiB chunks. At the ceiling it writes nothing further and closes the
read end, so the worker's next write takes `EPIPE`. There is no second
unbounded read anywhere, which is why X-C3's work cascade and X-M5's
mass-freeze cascade close at the source rather than by mitigation.

Capacity accounting spans live reservations, pending settlement,
quarantine, and retained `T_PROMOTED`; `SETTLEMENT`, `FAILED`, rename,
and promotion release nothing; the sole release is a disposition record
proving `custody_absent` under a signed author disposition.
Reconstruction takes `max(recorded, enumerated)`, counts an
unaccounted operation directory at the full per-operation ceiling, and
refuses admission rather than assuming zero. `FAILED` is now a closed
quarantine artifact with eight failure classes, each mapped to exactly
one already-signed process/global route; no live process resumes after
an invalid operation and no valid terminal survives one.

**Observation, transport, roles, schemas, promotion (§W5–§W7).** Every
pre-terminal status reply is one fixed `PENDING` shape whose
construction and path do not branch on output. `REQUEST.fifo` rejects
registered group members and descendants, with the deliberate untracked
escape stated as the A3 procedural residual rather than claimed closed.
Framing, buffering, the canonical `reply_fifo` path, the dead-reader
route, argv/path/frame bounds, and the controller FD convention are
pinned. Every previously named-but-undefined schema is enumerated in
one table with owner, lock, install mode, retention, and removal actor,
and there is exactly one legal on-disk layout. The
resume-hash-from-offset claim is deleted; held descriptors are
revalidated before the settle step with the TOCTOU residual named;
`st_dev` equality is a serve preflight so `EXDEV` cannot arise; and
`SETTLEMENT.json` remains the sole promotion commit.

## 3. Determinacy and completeness

Every Critical, Major, and Minor finding of both reviews is dispositioned
in §W9 — 6 X-Criticals, 11 X-Majors, 7 X-Minors, 5 Sol Criticals, 2 Sol
Majors with their seven sub-items, and Sol's eight-row B1 trace — each
to a named v2.1 locus. Rows 1–35 of the §W10 matrix include at least one
test for every Critical and Major. The required tables are present:
replacement index (§W0), durable-object/schema/path (§W7), eight-command
intent and reducer (§W1.4–§W1.5), process/FD/lock/topology (§W2.8),
watchdog state/failure (§W3.5), capacity/custody transitions (§W4.8),
crash-cut matrix (§W8), disposition (§W9), test matrix (§W10).

No clause resolves to "apply reviewer finding" or "as reviewed". Where
bytes are load-bearing the key sets are exact; where an ordering is
load-bearing the steps are numbered; where a failure is load-bearing the
`errno` and the single continuation are named.

## 4. Composite non-regression

Unmoved: E1/E2/E3 and their constants; the nine signed events; every
signed runtime schema; the roots tuple; batch arithmetic; the import
allowlist (**zero delta**) and the byte-frozen files; `runtime.py`,
`ledger.py`, `checkpoint.py`, `verification.py`, `activation.py`;
`MAX_CONCURRENT_LEASES = 4`; §V2.8's complete §S6 carry; §V2.7.5 stream
ownership; sole supervisor capability custody; A3's
T-development-only, Q/C-non-citable boundary; D1. `runtime_control/**`
and `runtime/T_PROMOTED/**` stay archival-excluded **and untracked**, so
the activation-protocol clean-HEAD rule holds; no `.gitignore` or
configuration change is authorized.

One signed sentence is superseded, named explicitly: harness §5a's
"executes the v2.1 §1 sequence **at or before it**". Its replacement is
strictly weaker and fail-closed. This is flagged for both lines as the
single compatibility item to attack.

## 5. Implementation-versus-contract distinction

The uncommitted implementation is unchanged and remains the earlier
facade: `src/philosophia/officina/generic_harness.py` (2 380 lines) has
no supervisor, control channel, FIFO, journal, operations tree,
watchdog, capacity ledger, or output transport — zero occurrences of
any of those terms — `SubprocessProcessOps`
(`src/philosophia/officina/generic_harness.py:407`) is the only process
primitive and `run_isolated_operation`
(`src/philosophia/officina/generic_harness.py:2285`) still executes a
caller-supplied callback in the harness interpreter. It neither cures
nor creates any contract defect above, and it remains uncommittable.
Implementability facts confirmed statically and relied on by v2.1:
`os.fork`, `os.pipe2`, `os.open` with `dir_fd`, `os.statvfs`,
`os.killpg`, `os.waitpid`, `flock`, `subprocess` with
`start_new_session`, `time.clock_gettime_ns`, and `hashlib` are all
inside the pinned allowlist, while `select`, `selectors`, `signal`,
`resource`, and `ctypes` are not — which is why the serve loop is a
`time`-paced nonblocking poll and why no `prctl` subreaper containment
is claimed.

## 6. Bounded questions

**Opus — Linux / process / crash executability (3)**

1. Is the argv-marker plus `/proc/*/cmdline` discovery predicate
   (§W2.4), combined with the retained `SPAWN.lock` fd (§W2.2), total
   over every crash cut between `SPAWNING.json` and a durable claim —
   including a grandchild that has forked its watchdog but not
   installed its identity, and a controller that reaches `exec` after
   its supervisor has already died?
2. Under §W3.2–§W3.4, is there any reachable schedule that yields a
   freeze observation with `quiescence = PROVED` while a declared
   member or backend stream is still runnable, or that leaves a lease
   past its deadline with neither an observation nor the unknowable
   route?
3. Is the §W4.5 framed transport single-valued on real Linux at every
   partial-read, EOF, `EPIPE`, full-pipe, and `ENOSPC` boundary, and
   does closing the read end at the ceiling reliably stop a
   contract-following worker without the supervisor itself ever taking
   `SIGPIPE`?

**Sol — idempotency, observation, validity, non-regression (3)**

1. Does §W1 make all eight commands exactly-once-effect and
   generation-total, including the intent-slot rule that separates a
   new heartbeat from a retry of a lost one, the per-command reducer
   locators for the multi-artifact automata, the two distinct
   acknowledgement mechanisms, and a GC that bounds growth without ever
   erasing replay proof?
2. Does §W4 bind the complete custody set with no path — `SETTLEMENT`,
   `FAILED`, rename, promotion, or crash reconstruction — by which
   capacity is replenished, and does every `failure_class` reach
   exactly one already-signed process/global route with no valid
   terminal surviving an invalid operation?
3. Do §W5.1/§W5.3 leave any official pre-settlement reply, refusal, or
   observable timing that varies with worker output, and does §W6.5's
   explicit supersession of harness §5a weaken any signed cell beyond
   the one named sentence?

## 7. Negative authorization

This closure authorizes only bounded X/Y confirmation of the v2.1
correction. It authorizes no implementation, no commit or staging of
the dirty Cursor files, no host change, no root command, no process,
endpoint, pipe, FIFO, journal instance, spawn intent, operation, output
bound, capacity artifact, promoted object, capability, lease, batch,
activation artifact, production call-graph manifest, entropy, E1/E2/E3
spend, world, learner, candidate, Q attempt, Q/C object, datum,
outcome, Proof, or claim movement. A3, B1, C1, D1, and K1 remain signed
and are not reopened.

`I_ACCEPT_OFFICINA_SUPERVISOR_CONTROL_CHANNEL_AMENDMENT` remains not
signable until both fresh confirmations accept v2.1.
`successor/officina/runtime/` contains only `T_RUNTIME.lock`;
`successor/officina/T_ENVELOPE.json` remains `"activated": false`; the
production call-graph manifest remains absent. T remains
`NOT_ACTIVATED` and the programme claim remains `OPEN`.
