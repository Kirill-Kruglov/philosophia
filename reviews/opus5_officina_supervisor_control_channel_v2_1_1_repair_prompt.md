# Prompt for Claude Code Opus 5: Officina supervisor/control-channel v2.1.1 bounded repair

You are **Claude Code Opus 5 acting as the specification author**, not as the
independent X-line reviewer. Fable 5 is temporarily unavailable. Preserve that
provenance literally in both deliverables: do not label your work as Fable 5,
and do not count your own closure as independent review evidence.

Work in the local `philosophia` repository. Read the governing artifacts in
full, at minimum:

- `successor/OFFICINA_GENERIC_HARNESS_SUPERVISOR_CONTROL_CHANNEL_V2_DRAFT.md`
- `successor/OFFICINA_GENERIC_HARNESS_SUPERVISOR_CONTROL_CHANNEL_V2_1_CORRECTION.md`
- `successor/OFFICINA_SUPERVISOR_AUTHOR_SELECTIONS_V1_SIGNATURE.md`
- `successor/OFFICINA_SUPERVISOR_OUTPUT_CAPACITY_SELECTION_V1_SIGNATURE.md`
- `successor/OFFICINA_GENERIC_HARNESS_CONTRACT_V2_3_1_CORRECTION.md`
- `successor/OFFICINA_BATCH_SETTLEMENT_CORE_AMENDMENT_V1_1_1_CORRECTION.md`
- `reviews/officina_supervisor_v2_1_authorship_note.md`
- `reviews/opus_officina_supervisor_control_channel_v2_1_final_confirmation.md`
- `reviews/sol_officina_supervisor_control_channel_v2_1_final_confirmation.md`

You may inspect the frozen/inactive implementation read-only where it is needed
to keep the contract implementable. Do not edit or run it.

## Task

Produce one bounded correction that dispositions **every** finding in both
independent v2.1 reviews. The two review lines converge: the remaining defects
are mechanical contract defects, not new scientific or resource choices.

Create exactly these two new files and do not alter existing files:

1. `successor/OFFICINA_GENERIC_HARNESS_SUPERVISOR_CONTROL_CHANNEL_V2_1_1_CORRECTION.md`
2. `reviews/opus5_officina_supervisor_control_channel_v2_1_1_closure.md`

The correction must be a precise replacement layer over v2 + v2.1, not an
informal commentary and not a silent rewrite. Include an exact replacement
index identifying every superseded v2.1 clause/sentence/table row. If a repair
requires a new schema, path, state, transition, constant, or verifier duty,
specify it bit-exactly.

The closure's first line must be exactly one of:

- `READY_FOR_OFFICINA_SUPERVISOR_V2_1_1_FINAL_XY_CONFIRMATION`
- `BLOCKED_OFFICINA_SUPERVISOR_V2_1_1_AUTHOR_CELL`
- `BLOCKED_OFFICINA_SUPERVISOR_V2_1_1_CONTRACT_CONFLICT`

Do not use `READY` unless all findings below are closed without discretion.

## Frozen author selections

These remain binding and must not be reopened, weakened, or reinterpreted:

- A3: procedural confinement, not a security boundary.
- B1: journaled exactly-once semantic effects and retry-stable replies.
- C1: watchdog may witness/freeze but never hold runtime authority or settle.
- D1: no idle supervisor exit.
- K1: supervisor-mediated output with fixed ceilings:
  - 64 MiB per stream;
  - 256 MiB per operation;
  - 32 GiB aggregate T custody;
  - 8 GiB filesystem safety margin;
  - 4 MiB chunks.
- K1 accounting is conservative: reservation remains counted through live,
  pending, quarantine, and promoted custody; **settlement, rename, promotion,
  failure, and unused reservation do not replenish capacity**. Only the signed,
  verified custody-absence disposition may release it.

No new author-choice token is expected. If you find one genuinely unavoidable,
stop with `BLOCKED_OFFICINA_SUPERVISOR_V2_1_1_AUTHOR_CELL` and state the exact
choice; do not default it.

## Mandatory repairs

### R1. Explicit occurrence allocation and total B1 semantics

Replace inference from the highest unfinished client slot with an explicit API
distinction:

- `NEW` atomically allocates and returns a durable occurrence handle;
- `RETRY(handle)` addresses exactly that occurrence;
- unfinished client state must never silently turn a new occurrence into a
  retry;
- two concurrent `NEW` calls in the same scope must get distinct occurrences;
- client slot/counter/done files are convenience state only and can never be
  runtime authority.

The supervisor-authoritative journal/tombstone state must reconstruct the next
index after client-file deletion, crash, or generation change. Define the
allocator, locks, atomicity, EEXIST continuations, and crash cuts.

Journal and cache observation-form `OPERATION_STATUS` too, with an empty effect
tuple. A new poll is a new occurrence; an explicit retry returns byte-identical
effect-reply and token bytes even if current operation state changed.

Successor-occurrence acknowledgement is legal only when the successor carries
the exact cached prior `effect_reply_sha256`. Exclude a command's own terminal
effect from `PROCESS_TERMINAL` acknowledgement: in particular, `CLOSE` cannot
acknowledge its own reply before observation. Require explicit delivery ack or
a successor carrying the exact prior reply hash.

Define either per-occurrence replay commitments or a contiguous,
supervisor-derived acknowledged-prefix tombstone. GC may advance only over a
contiguous acknowledged prefix, in the same lock epoch that installs the ack.
Post-GC classification must be decidable from the incoming frame and retained
authority; remove predicates that require an unavailable old hash.

Give a complete trace table for all eight commands across: lost request before
acceptance, lost reply, client crash after reply/before local done, generation
change, effect before commit, ack+GC+old retry, concurrent same-scope clients,
and repeated STATUS.

### R2. Descendant-aware reducer and validity-first takeover

For committed/replied plans, accept a current ledger head that is a verified
descendant of the exact recorded event/post-head chain. Later valid history is
not invalidity. For accepted-only plans, verify the exact legal prefix and the
absence of a conflicting intervening suffix. Define all mismatch routes.

On supervisor takeover, first prove/freeze old-generation process state and
settle every affected live stream through the signed all-live invalid route,
including completion of any unresolved batch authority. Only then may reducers
perform non-behavioral archival/cache work. Across supervisor loss, a reducer
must never spawn, `SIGCONT`, renew, admit, or otherwise continue behavior.

### R3. Constructible spawn/bootstrap identity

Remove the circular spawn id and generation-local-fd ambiguity. Specify either
the reviewers' template construction or an equally exact construction:

- hash an exact argv prefix/template that excludes the derived markers;
- derive `spawn_intent_id` from generation, role, sequence, creation time, and
  that prefix/template hash;
- substitute the id and fixed descriptor markers afterwards;
- hash the resulting complete argv separately;
- pin descriptor numbers using `dup2` and pin per-role descriptor order.

The in-process supervisor grandchild cannot be found by `/proc/.../cmdline`.
Give it a non-circular kernel-verifiable bootstrap identity, for example a
sealed pipe carrying pid/start identity plus an immediate no-replace
`SPAWNING_CHILD` record. Pin a bounded first-ack timeout, bounded nonblocking
`SPAWN.lock` acquisition/retry, exact kill/death proof, and every crash cut so a
hung pre-identity grandchild cannot wedge D1 indefinitely.

Remove `WATCHDOG` from an exec-child argv-bearing spawn-intent schema, or define
a separate exact fork-child record with no argv. Do not pretend an in-process
fork received new argv.

Make a fixed, reviewed supervisor-owned bootstrap adapter the actual executable
root for controllers/workers. The adapter must parse and verify inherited
tokens, close forbidden descriptors, self-stop before target behavior, and
dispatch the target only after `SIGCONT`. Arbitrary target programs cannot be
assumed to implement Officina tokens or self-stop.

### R4. Watchdog renewals and evidence acceptance

Restore atomic lease-table publication and ack after **every** successful
locked claim-start, renew, and remove. Add `watchdog_table_seq` to exact
`HEARTBEAT`, `CLOSE`, and `PAUSE` effect plans and reducers. The old deadline is
authoritative until the successor table is acked; timeout refuses with
`WATCHDOG_UNACKED`, never fabricates a later valid renewal.

Define the supervisor acceptance predicate for watchdog freeze observations:
generation, table sequence, deadline, pgid/start identity, freeze ordering,
quiescence, and member-count consistency must all match supervisor authority.
Any malformed, missing, conflicting, or unverifiable fact routes to
`UNKNOWN`/all-live invalidity; it can never become valid evidence.

Name freeze witnesses by generation-bound process id plus table sequence to
avoid stale no-replace collision. Pin production and consumption order. The
watchdog remains a control-plane witness only: no runtime lock/capability,
ledger write, settlement, or validity authority.

For `now_ns == deadline_ns`, take a bounded later monotonic sample while the
group stays proved quiescent. If strict positive progress cannot be proved,
route to `UNKNOWN`; never restore a valid zero-overrun branch.

### R5. Admission release is durable before success

`OPERATION_ADMIT` must not cache `ADMITTED` before the exact bound worker has a
durable same-generation release/start-attempt locator. Define its schema,
ordering, idempotent reducer, and crash table. A same-generation reducer may
complete an idempotent release before success is cacheable; after supervisor
loss R2 governs and the worker is frozen/settled, never resumed.

### R6. K1 accounting and disposition authority

Remove every over-declaration/unused-reservation release at settlement.
`bytes_reserved` remains the accounted contribution until an authorized
custody-absence disposition is fully verified. `actual_bytes` is diagnostic
only and may never reduce the 32 GiB total.

Define the one immutable author-disposition authority completely:

- canonical path grammar outside the supervisor control plane;
- schema and exact key set;
- author token/signature representation and verifier;
- activation/generation/operation bindings;
- reserved and actual-byte facts;
- custody destination and parent/hash bindings;
- atomic no-replace durability and single-use semantics;
- recursive scientific-field prohibition;
- supervisor-produced disposition bound to its exact hash;
- same-lock descriptor-safe directory enumeration proving named custody absent;
- mismatch/stale/substitution/replay routes that release nothing.

This is a mechanical realization of signed K1, not a new author choice.

### R7. Worker status and output cuts

Define `t-worker-status.v1` exactly (`schema`, `scientific_outcome`,
`operation_id`, `exit_reason`, plus any strictly necessary bit-exact fields).
Do not restore worker-supplied output paths: the supervisor derives paths from
framed headers. Add a total route for EOF at a frame boundary with no status
frame (worker failure/quarantine), and explicitly decide within the already
signed failure semantics whether zero-frame `COMPLETED` is a canonical empty
result or failure. This is a contract completion, not an author cell unless it
would change K1 or scientific meaning.

### R8. Honest A3 leakage and TOCTOU boundary

Retain fixed official preterminal reply bytes, but replace every timing-secrecy
claim with the exact honest boundary: latency, filesystem/endpoint metadata,
worker timing, and same-UID observations are T-only procedural facts,
permanently non-citable and forbidden from selection, Q/C, C1-C6, or any
scientific interpretation.

For output substitution, either rehash through a held read-only descriptor
before settlement, or explicitly state that equal-size same-UID substitution
is an A3 residual. Do not claim inode/size/link checks detect it.

### R9. Remaining exactness repairs

Close every Opus Minor finding rather than silently carrying it:

- give `T_MIN_HEARTBEAT_INTERVAL_NS` a normative rule or remove it;
- make `T_ARGV_MAX_BYTES` satisfiable inside the full control-frame bound;
- pin role-specific `--officina-ctrl-fds` order;
- compare serve-preflight device identity against an existing `runtime/` root,
  not a lazily-created promoted directory;
- define concurrent client `.done` `EEXIST` continuation;
- qualify the inherited disposition table so it does not claim a finding is
  closed while v2.1.1 is still under confirmation.

Also reconcile exact immutable-object keys, maximum frame arithmetic, target
existence/executability preflight, watchdog/control artifact namespaces, and
all references affected by R1-R8. No free-form decision value may enter any
scientific, resource, or invalidity field.

## Required closure contents

The closure must include:

1. The exact verdict token on line 1.
2. A one-to-one disposition table for every Opus X21-C1..C5,
   X21-M1..M8, all seven Opus Minors, and every Sol C1..C5/M1..M3.
3. A replacement index v2.1 → v2.1.1.
4. A state/authority table showing which filesystem object is convenience,
   transport, control witness, runtime authority, or author authority.
5. Worked B1, reducer/takeover, spawn/bootstrap, watchdog, admission, and K1
   crash traces, including the counterexamples from both reviews.
6. A no-regression table for A3/B1/C1/D1/K1 and for the already-signed generic
   harness/batch-settlement surfaces.
7. Exact implementation and test obligations, but **no implementation
   authorization**.
8. One bounded literal yes/no prompt for an independent clean-context
   Claude Opus 4.8 X-line and one for GPT-5.6 Sol Y-line. They must review the
   actual v2.1.1 bytes, not trust this closure.
9. Confirmation that you created no code, process, supervisor, controller,
   worker, watchdog, endpoint, entropy, T activation, scientific datum, Q/C
   artifact, or outcome, and that T remains `NOT_ACTIVATED`.

## Prohibitions

- Do not edit v2, v2.1, signatures, code, tests, runtime trees, or prior reviews.
- Do not run tests, probes, supervisor processes, or smoke commands.
- Do not authorize implementation or the signature token.
- Do not silently weaken fail-closed behavior to obtain liveness.
- Do not turn watchdog evidence into a second runtime authority.
- Do not treat process invalidity, resource exhaustion, or missing evidence as
  scientific evidence.
- Do not predict qualification or any C1-C6 outcome.

If the correction closes the bounded defects, its only next authorization is
independent v2.1.1 X/Y confirmation. The author token remains unavailable until
both confirmations explicitly accept the corrected bytes.
