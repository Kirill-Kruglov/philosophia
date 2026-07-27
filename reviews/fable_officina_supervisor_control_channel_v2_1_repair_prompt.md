# Task for Claude Code Fable 5: Officina supervisor/control-channel v2.1 closure

Work in `/home/master/llm_projects/philosophia`.

Produce a bounded specification correction only. Do not edit code, tests,
existing contracts, signatures, reviews, or runtime artifacts. Do not run any
Officina process, test, smoke, supervisor, controller, worker, watchdog, FIFO,
journal, or output transport. Do not create entropy, activation, capability,
world, learner, datum, or outcome. T remains `NOT_ACTIVATED`.

## Governing inputs

Read in full:

- `successor/OFFICINA_GENERIC_HARNESS_SUPERVISOR_CONTROL_CHANNEL_V2_DRAFT.md`
- `reviews/fable_officina_supervisor_control_channel_v2_closure.md`
- `reviews/opus_officina_supervisor_control_channel_v2_review.md`
- `reviews/sol_officina_supervisor_control_channel_v2_review.md`
- `successor/OFFICINA_SUPERVISOR_AUTHOR_SELECTIONS_V1_SIGNATURE.md`
- `successor/OFFICINA_SUPERVISOR_OUTPUT_CAPACITY_AUTHOR_CHOICE_PACKET_V1_DRAFT.md`
- `reviews/fable_officina_supervisor_output_capacity_author_choice_packet_v1.md`
- `successor/OFFICINA_SUPERVISOR_OUTPUT_CAPACITY_SELECTION_V1_SIGNATURE.md`
- `successor/OFFICINA_GENERIC_HARNESS_SIGNATURE.md`
- the full signed batch-settlement and generic-harness composite
- current dirty implementation/tests read-only, only for implementability

Closed author choices, not to be reopened:

```text
A3 SAME_UID_PROCEDURAL_RESCOPE
B1 DURABLE_JOURNAL_ACK_REDELIVERY
C1 DEDICATED_FREEZER
D1 NO_IDLE_EXIT
K1 SUPERVISOR_MEDIATED_TRANSPORT_FIXED_CEILING
```

## Deliverables

Write exactly two new files:

1. `successor/OFFICINA_GENERIC_HARNESS_SUPERVISOR_CONTROL_CHANNEL_V2_1_CORRECTION.md`
2. `reviews/fable_officina_supervisor_control_channel_v2_1_closure.md`

The correction must carry v2 forward except through an explicit replacement
index. Every replacement must be complete and byte-executable; do not say only
“apply reviewer finding.” If the resulting composite is still ambiguous to two
independent implementers, use a blocked verdict.

## Mandatory repairs

Disposition every Critical, Major, and Minor finding from both formal reviews.
At minimum, close the following load-bearing surfaces.

### 1. Generation-total B1 without collapsing distinct intents

Separate stable semantic intent from the current transport envelope. A retry
after supervisor takeover uses current generation/client/reply fields but
resumes the same semantic effect and returns identical cached effect-reply and
release-token bytes in a fresh envelope.

Do **not** blindly define the idempotency key as only
`SHA256(command, arguments)`: repeated legitimate intents such as successive
heartbeats or status observations can have identical command arguments but are
distinct effects/observations. Pin a durable, retry-stable semantic-intent
identity and allocation rule that:

- distinguishes a new intended heartbeat/status from a retry of a lost one;
- survives a short-lived CLI process and supervisor generation change;
- is durably retained before first send;
- introduces neither outcome-dependent entropy nor a ninth scientific/control
  command;
- cannot let key reuse with changed semantics drive global G5.

Use immutable predecessor-bound journal phase records, not mutation of one
no-replace file. Give all eight commands a deterministic recovery reducer from
`ACCEPTED` through effect, reply cache, and acknowledgement. Bind each accepted
plan to all multi-artifact effect locators needed for takeover.

Separate ordinary effect-reply acknowledgement from release-token delivery
acknowledgement. Pin one exact protocol and schemas, a bounded STATUS mechanism,
`ALREADY_DELIVERED`, compact permanent replay tombstones, and GC that cannot
erase replay proof or grow without bound.

### 2. Spawn, singleton, and takeover

Close every cut before claim:

- a durable spawn intent must lead to a discoverable PID/start/session binding
  even if the supervisor dies between any two steps;
- no behavior/capability exists before the child is durably bound and the
  watchdog has acknowledged its lease;
- self-stop wait is bounded, nonblocking, and has one timeout/exit refusal and
  kill/reap route;
- the grandchild must retain the inherited `SPAWN.lock` through durable
  supervisor identity installation so CLI death cannot release singleton
  ownership early;
- split client takeover (control-plane kill/read only) from new-supervisor
  takeover (runtime settlement under `T_RUNTIME.lock`).

Delete internal `--supervisor-serve` and `--watchdog-serve` argv tokens. Use
in-process post-fork function entry for supervisor and watchdog. Pin the one
reviewed controller bootstrap/exec convention, including how its inherited FDs
and spawn-intent marker are learned. State the true invariant: no capability or
behavior authorization before `SIGCONT`; do not claim CPython executes no
interpreter/import code before self-stop.

### 3. Watchdog C1

Require durable lease-table publication and matching watchdog ack before first
`SIGCONT`, capability usability, or operation admission. Until a renewal is
acked, the old deadline remains authoritative.

Freeze time is the conservative monotonic observation when every declared
process-tree member/backend stream is proved stopped/dead and synchronized,
not signal-send time. Unknown membership or lost evidence routes to unknowable
all-live invalid settlement; never synthesize an earlier timestamp. Choose one
mechanical evidence path consistent with C1. The watchdog remains no runtime or
ledger writer.

Positive confirmed overrun has public cause `PROCESS`; `CLOCK` applies only to
an independently verified clock fault. Forbid resource-stop and every valid
close/exhaustion/review terminal on watchdog overrun. Delete unreachable
zero-overrun/tolerance language. Preserve full conservative E1 facts and make
every death/restart/update/ack cut single-valued.

Ack liveness must use the watchdog's sample time rather than delayed supervisor
read time. Pin a supervisor poll cadence and service watchdog/control steps
inside every bounded long loop.

### 4. K1 output capacity and operation transaction

Embed K1 and the packet's exact constants/invariants. `OPERATION_ADMIT` is the
sole transaction that installs the bound: no circular pre-existing
`BOUND.json`, no ninth command, no undefined pending key. Bind the accepted
semantic intent, first meter cursor, capacity record, operation id, admission,
and worker spawn in one crash-reducible plan.

Worker receives no writable output pathname/descriptor. Define the exact
framed K1 pipe parser and EOF/partial/EPIPE/backpressure cuts. Supervisor alone
writes/hash-streams output, stops at the per-operation ceiling, services
watchdog/control between 4 MiB chunks, and never performs a second unbounded
read.

Aggregate accounting covers live reservations, pending settlement,
quarantine, and retained `T_PROMOTED`. `SETTLEMENT`, `FAILED`, rename, and
promotion release no retained capacity. Define exact capacity/admission/
settled/quarantine/disposition schemas, crash reconstruction, FS margin,
same-filesystem preflight, `errno` routes, custody transfer, and signed
disposition proof.

Use the selected exact constants:

```text
PER_STREAM = 67_108_864
PER_OPERATION = PER_STREAM * len(declared_stream_indexes) <= 268_435_456
AGGREGATE = 34_359_738_368
FS_MARGIN = 8_589_934_592
CHUNK = 4_194_304
PATH_MAX = 1_024
COMPONENT_MAX = 255
```

### 5. Observation, transport, roles, and schemas

- Collapse all preterminal official status replies to one fixed `PENDING`
  shape; reveal `PROMOTED` only after commit and `FAILED` only after the signed
  invalid terminal is durable.
- Reject registered controller/worker group members and descendants on the CLI
  endpoint; state the A3 procedural residual for deliberate untracked escape.
- Define newline framing, bounded buffering across writers, exact reply FIFO
  path derived from identity+intent, dead-reader continuation, argv/path/frame
  byte bounds, and fixed controller FD convention.
- Enumerate every previously named-but-undefined schema and state, including
  admission, journal phases, ordinary ack, delivery ack, FAILED/quarantine,
  spawn successor, capacity, freeze, and settlement relations.
- Use the signed durability sequence for every `runtime_control/**` object and
  name owner/lock/retention/removal actor. No optional on-disk layouts.

### 6. Promotion, hashing, process membership, and non-regression

Delete “resume hash from descriptor offset after crash”; restart from zero or
quarantine within K1's fixed bound. Pin held-descriptor revalidation and A3
TOCTOU residual. Require same-filesystem `st_dev` preflight and exact
`ENOENT`/`EEXIST`/`ENOTEMPTY`/`EXDEV` continuations.

Keep `SETTLEMENT.json` as the sole promotion commit. Prove group quiescence by
recorded membership/parent-chain scan; escaped/unclassifiable work becomes
unknown recovery, not a false mechanical `killpg` guarantee.

Explicitly supersede the signed predecessor's physical “at or before deadline”
sentence with the reviewed non-real-time validity rule. Keep all F3-F15, Sol
repairs, and Codex §S6 closures. Preserve A3's T-only/QC-noncitable boundary,
D1, E1/E2/E3, nine signed events, runtime schemas, roots, batch arithmetic,
capability custody, and programme claim `OPEN`. `runtime_control/**` and
`runtime/T_PROMOTED/**` remain untracked and archival-excluded.

## Required tables and proof obligations

Include:

- complete replacement index v2 -> v2.1;
- exact durable-object/schema/path table;
- eight-command semantic-intent and recovery-reducer table;
- process/FD/lock/topology table;
- watchdog state/failure table;
- K1 capacity/custody transition table;
- crash-cut matrix;
- full finding-disposition table for both X and Y reviews;
- finite implementation test matrix, with a test for every Critical/Major.

Do not rely on prose such as “as reviewed” where bytes or next actions are
load-bearing.

## Verdict and handoff

The closure's first line must be exactly one of:

- `READY_FOR_OFFICINA_SUPERVISOR_V2_1_FINAL_XY_CONFIRMATION`
- `BLOCKED_OFFICINA_SUPERVISOR_V2_1_AUTHOR_CELL`
- `BLOCKED_OFFICINA_SUPERVISOR_V2_1_CONTRACT_CONFLICT`

If ready, ask at most three literal bounded questions each of Opus and Sol.
`I_ACCEPT_OFFICINA_SUPERVISOR_CONTROL_CHANNEL_AMENDMENT` remains not signable
until both fresh confirmations accept v2.1. Confirm no code/runtime action,
full negative authorization, T `NOT_ACTIVATED`, and claim `OPEN`.
