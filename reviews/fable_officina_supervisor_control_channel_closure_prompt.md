# Fable 5 task: close the one blocked Officina supervisor/control-channel cell

Work in:

```text
/home/master/llm_projects/philosophia
```

Write exactly two new files:

```text
successor/OFFICINA_GENERIC_HARNESS_SUPERVISOR_CONTROL_CHANNEL_V1_DRAFT.md
reviews/fable_officina_supervisor_control_channel_v1_closure.md
```

Do not edit any existing file. Do not modify the uncommitted Cursor
implementation. Do not commit. Do not create entropy, an authorization,
production call-graph manifest, runtime artifact, process, capability, world,
learner, device spend, Q/C object, datum, or outcome. T must remain
`NOT_ACTIVATED`.

## Authority and evidence

Read the signed composite and its implementation review:

```text
successor/OFFICINA_GENERIC_HARNESS_SIGNATURE.md
successor/OFFICINA_BATCH_SETTLEMENT_CORE_AMENDMENT_V1_DRAFT.md
successor/OFFICINA_BATCH_SETTLEMENT_CORE_AMENDMENT_V1_1_CORRECTION.md
successor/OFFICINA_BATCH_SETTLEMENT_CORE_AMENDMENT_V1_1_1_CORRECTION.md
successor/OFFICINA_GENERIC_HARNESS_CONTRACT_V2_DRAFT.md
successor/OFFICINA_GENERIC_HARNESS_CONTRACT_V2_1_CORRECTION.md
successor/OFFICINA_GENERIC_HARNESS_CONTRACT_V2_2_CORRECTION.md
successor/OFFICINA_GENERIC_HARNESS_CONTRACT_V2_3_CORRECTION.md
successor/OFFICINA_GENERIC_HARNESS_CONTRACT_V2_3_1_CORRECTION.md
successor/OFFICINA_T_ACTIVATION_PROTOCOL_V2_CORRECTION.md
reviews/codex_officina_generic_harness_implementation_review.md
reviews/opus_officina_generic_harness_implementation_review.md
reviews/sol_officina_generic_harness_implementation_review.md
```

Audit the four uncommitted Cursor files only as evidence:

```text
src/philosophia/officina/accounting.py
src/philosophia/officina/generic_harness.py
tests/test_officina_accounting.py
tests/test_officina_generic_harness.py
```

The converged conclusion is binding for this task:

```text
review-evidence commit:
5c00d5ffa9f67b6907bd370b9efccaf542646ba4
```

- all Codex C1-C4 and M1-M6 are confirmed;
- Sol additionally identified stream enumeration/`device_units > 1`, authority
  provenance/forgery, semantic parent validation, and event-backed terminal
  defects;
- all defects except one are direct Cursor repairs against signed text;
- the one `BLOCKED_CONTRACT` surface is the persistent
  supervisor/watchdog/control channel and confined worker-to-supervisor result
  channel across the signed CLI model.

Do not reopen the batch-settlement science, resource constants, events, runtime
schemas, T/Q/C boundaries, or any already signed cell.

## Required bounded correction

Produce one complete, bit-exact engineering/control correction for signed v2
sections 1, 2c.3-2c.6, 5a, 5b, 9, and the corresponding section-10 tests.
Select one topology. Do not leave alternatives for Cursor.

The correction must pin all of the following.

### 1. Process topology and lifetime

- Which OS process is the persistent supervisor and watchdog.
- When it is created relative to `claim`, `T_PROCESS_STARTED`, and lease
  installation.
- Whether `claim`, `start`, `heartbeat`, `close`, `pause`, and `resume` are
  separate short-lived clients, commands within one foreground supervisor
  session, or another exact topology.
- Exact controller and worker parentage, process-group/session ownership, PID
  plus kernel start-identity acquisition, boot binding, and immutable argv.
- The supervisor's lifetime, clean exit, crash, restart, orphan, PID-reuse, and
  power-loss routes.
- Who holds the real-T capability and `T_RUNTIME.lock`; controller and worker
  must never hold an independently usable capability or lock.
- How the watchdog remains effective at or before the deadline even when no
  later CLI command arrives. Lazy detection on the next invocation is
  forbidden unless you prove it satisfies the already-signed "at or before the
  deadline" rule; otherwise choose a genuinely persistent watchdog.

### 2. Closed control channel

- Exact transport using only explicitly authorized imports and OS primitives.
- Closed message schemas, framing, canonical byte encoding, sequence/nonces if
  any, request/reply order, maximum sizes, EOF/partial/duplicate/replay rules,
  and identity binding.
- Which endpoints/FDs/paths each of supervisor, controller, worker, and
  short-lived CLI client can access.
- Descriptor inheritance and `CLOEXEC` rules; socket/pipe/FIFO/temp-path
  custody; permissions; cleanup only where signed recovery permits it.
- Behavior when either endpoint disappears, a partial frame arrives, the
  channel blocks, the peer is substituted, or an old client reconnects.
- No hidden entropy and no result-bearing field in any durable control artifact.

If the chosen protocol requires adding an import or changing
`verification.py`'s allowlist, state the smallest exact allowlist delta and
classify it as an explicit control amendment requiring the author token below.
Do not pretend the present allowlist already permits it. Do not add another
production root or `scripts/*.py` entry point.

### 3. Confined operation and promotion

- Exact controller request for an oracle/learner/checkpoint operation without
  exposing the result before settlement.
- How the supervisor creates the worker, confines memory, IPC, descriptors,
  temporary paths, and output buffers, and prevents a worker/controller escape.
- Exact operation identity and binding to activation, process, lease, adapter,
  stream(s), pre-operation meter cursor, result bytes/hash, and the one
  post-operation charge event.
- Order: admit under lock -> execute confined -> revoke output authority ->
  quiesce/terminate -> backend synchronize -> hash -> settle under lock ->
  atomically promote -> issue/deliver one-use release.
- The promoted object location/ownership and what the controller actually
  receives. A pre-settlement result hash is information and must remain hidden.
- Rejection of an old, unrelated, sibling-process, or pre-operation charge.
- Disposal authority after failure, without inspecting the result.
- Every crash cut before and after result production, hash, charge, promotion,
  and release delivery. No cut may expose a result without its own durable
  settlement or charge twice.

### 4. Metering and boundary integration

- Watchdog/heartbeat ownership of CPU monotonic readings and declared streams.
- Per-stream enumeration for `device_units > 1`, including mixed
  known/unknown streams in one process.
- Exact transition from ordinary heartbeat/watchdog/close to the already-signed
  all-live frozen batch for E1, E3, invalidity, and recovery.
- No fabricated successor reservation, no counter-only valid terminal, and no
  live sibling after a boundary.

Do not redesign the existing batch arithmetic or automaton. Reference it.

### 5. CLI and production boundary

- Keep the sole harness root:
  `src/philosophia/officina/generic_harness.py`.
- Keep exactly the signed commands:
  `claim`, `start`, `heartbeat`, `close`, `pause`, `resume`.
- Pin the real `python -m philosophia.officina.generic_harness` argv parsing
  rule without importing an unapproved parser by accident.
- State whether commands communicate with a persistent supervisor and how a
  command proves it is addressing the right generation.
- No additional script, daemon executable, dynamic import, plugin discovery,
  test capability, predecessor dependency, or production manifest now.

### 6. Deterministic repair ledger

Carry every non-blocked implementation repair forward as a mechanical Cursor
obligation, with no new design choice:

- automatic E1/E3/invalid boundary batch routing;
- event-backed global terminal states;
- exact stream witness and private claim-backed batch authority;
- mandatory `ARCHIVE` before `RESOLVED`;
- raw-ledger D1 head/cache completion;
- G5 "since last admission";
- ordinary crash-cut recovery and one lock epoch for close;
- global process-sequence/id non-reuse and kernel start identity;
- full claim/registry/omission/parent validation;
- locked reads/capability/promotion;
- real module CLI parsing;
- pre-review-head acyclicity regression;
- strict integer rejection (`bool` is not a charge).

Confirm explicitly:

- both review-record ledger fields bind the durable pre-review head;
- caller-supplied current durable head remains required by
  `charge_batch_settlement`;
- archival needs implementation, not another contract cell.

## Acceptance tests

Give a finite executable matrix for the new topology, including:

- supervisor/controller/worker/CLI death at every cut;
- watchdog firing with no later client invocation;
- PID reuse and wrong start identity;
- request framing partial/duplicate/replay/substitution;
- inherited FD, pipe/socket, mutable-memory, filesystem, temp-output, and
  process-group escape;
- result produced but not settled; settled by wrong/old/sibling charge;
- crash around atomic promotion and one-use release delivery;
- one- and multi-stream E1/E3 boundaries;
- all already-required X/Y repair tests.

All tests must use disposable roots and test-only processes. No test may create
a production-compatible real-T artifact.

## Closure memo

`reviews/fable_officina_supervisor_control_channel_v1_closure.md` must contain:

1. verdict;
2. exact replacement/addition index over the signed composite;
3. one-to-one disposition of Opus and Sol findings;
4. proof that only the blocked engineering surface changed;
5. exact import/allowlist/control-file delta, or an explicit proof that none is
   needed;
6. Cursor handoff with allowed files and forbidden files;
7. the complete new-test matrix;
8. two bounded questions each for Opus and Sol;
9. an author token candidate:

```text
I_ACCEPT_OFFICINA_SUPERVISOR_CONTROL_CHANNEL_AMENDMENT
```

The token must not be declared signable until both bounded X/Y confirmations
accept the correction.

## Required verdict

First line of the closure exactly one:

```text
READY_FOR_OFFICINA_SUPERVISOR_CONTROL_CHANNEL_XY_REVIEW
BLOCKED_OFFICINA_SUPERVISOR_CONTROL_CHANNEL
```

Do not use `READY` unless two independent implementers can now produce the same
process topology, channel bytes, watchdog behavior, promotion visibility, and
crash route without choosing policy inline.
