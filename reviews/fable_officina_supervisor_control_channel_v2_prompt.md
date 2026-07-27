# Task for Claude Code Fable 5: close Officina supervisor v2 after author selection

Work in `/home/master/llm_projects/philosophia`.

This is a specification-repair task. Do not edit code, tests, existing
contracts, signatures, reviews, or runtime artifacts. Do not start a
supervisor, controller, worker, FIFO, watchdog, journal, or disposable smoke.
Do not create entropy, authorization, manifest, capability, world, learner,
datum, or outcome. T remains `NOT_ACTIVATED`.

## Read first

At minimum:

- `successor/OFFICINA_GENERIC_HARNESS_SUPERVISOR_CONTROL_CHANNEL_V1_DRAFT.md`
- `reviews/fable_officina_supervisor_control_channel_v1_closure.md`
- `reviews/codex_officina_generic_harness_implementation_review.md`
- `reviews/opus_officina_supervisor_control_channel_v1_confirmation.md`
- `reviews/sol_officina_supervisor_control_channel_v1_confirmation.md`
- `successor/OFFICINA_SUPERVISOR_AUTHOR_CHOICE_PACKET_V1_DRAFT.md`
- `reviews/fable_officina_supervisor_author_choice_packet_v1.md`
- `successor/OFFICINA_SUPERVISOR_AUTHOR_SELECTIONS_V1_SIGNATURE.md`
- `successor/OFFICINA_GENERIC_HARNESS_SIGNATURE.md`
- the governing generic-harness v2 + v2.1 + v2.2 + v2.3 + v2.3.1 composite
- the current uncommitted Cursor implementation, read-only, only to ensure the
  contract is implementable and to name superseded behavior precisely

Use the author-selection record as the sole authority for A/B/C/D:

```text
A: I_SELECT_SUPERVISOR_CONFINEMENT_A3_SAME_UID_PROCEDURAL_RESCOPE
B: I_SELECT_SUPERVISOR_IDEMPOTENCY_B1_DURABLE_JOURNAL_ACK_REDELIVERY
C: I_SELECT_SUPERVISOR_WATCHDOG_C1_DEDICATED_FREEZER
D: I_SELECT_SUPERVISOR_LIFETIME_D1_NO_IDLE_EXIT
```

Do not reopen those selections and do not choose a different option.

## Deliverables

Write exactly two new files:

1. `successor/OFFICINA_GENERIC_HARNESS_SUPERVISOR_CONTROL_CHANNEL_V2_DRAFT.md`
2. `reviews/fable_officina_supervisor_control_channel_v2_closure.md`

The v2 draft must be self-contained. It supersedes v1 rather than requiring an
implementer to assemble scattered corrections.

## Mandatory content

### 1. Embed all four selected meanings

Carry A3/B1/C1/D1 into normative executable prose, not by reference alone.
Delete every contradicted v1 statement: same-UID mode-bit secrecy, ephemeral
retry state, serial-loop deadline protection, and idle exit.

A3 must be scoped honestly:

- same-UID confinement protects against accidental/contract-following misuse,
  not a deliberate controller inspecting its own UID's state;
- endpoint-role separation is still mechanically enforced;
- this is a T-development procedural boundary only and may not be cited or
  inherited as Q/C confidentiality.

### 2. Close the complete mechanical ledger

Apply every mechanical repair numbered 1-15 in
`OFFICINA_SUPERVISOR_AUTHOR_CHOICE_PACKET_V1_DRAFT.md`, plus every §S6 repair
from the Codex implementation review. Include at least:

- spawn-before-claim and spawn-before-stop closure;
- singleton bootstrap and takeover;
- own-child, reparented-zombie, and process-group identity rules;
- exact byte schemas and endpoint roles for all eight commands;
- durable B1 request/reply/ack journal across supervisor generations;
- `OPERATION_ADMIT` retry without a second worker, cursor, or charge;
- watchdog/supervisor death and restart automata;
- safe output grammar, descriptor hashing, atomic promotion, and its single
  commit point;
- stream ownership and subset settlement for `k>1`;
- event-backed terminals and `ARCHIVE` before `RESOLVED`;
- raw-ledger D1 repair, G5 scoped since last admission, and ordinary crash
  cuts;
- one lock epoch for close; global id/sequence non-reuse; complete unresolved
  registry validation;
- locked reads, capability issuance, promotion, and real `python -m` CLI
  parsing;
- pre-review-head acyclicity and strict `type(x) is int` validation.

For each durable object pin: canonical path, exact schema and closed enums,
no-replace/atomicity rule, hash inputs, owner, lifecycle, crash cuts, retry
behavior, and archival/exclusion rule.

### 3. Make C1 truthful on a non-real-time Linux host

Do not claim that an ordinary scheduled userspace watchdog can physically
guarantee execution exactly at or before a monotonic deadline under every host
schedule.

Preserve the selected C1 topology: an independently scheduled freezer that is
never a runtime writer, and a sole supervisor that settles later. Define the
strongest implementable contract:

- exact clock and deadline representation;
- watchdog health/readiness and update acknowledgement;
- identity-safe group freeze/kill sequence;
- a durable measured freeze observation or a re-derivable witness;
- any positive deadline overrun routes fail-closed to the already-authorized
  process/platform invalidity destination and can never become a valid T
  operation;
- watchdog death, supervisor death, stale updates, PID reuse, and restart are
  total and deterministic.

If reconciling this validity rule with the signed predecessor requires a new
author choice rather than a mechanical correction, say so explicitly and emit
`BLOCKED_OFFICINA_SUPERVISOR_V2_AUTHOR_CELL`; do not silently over-claim.

### 4. Bound output processing before behavior starts

The existing file-count/path-depth formulas do not bound logical bytes. A
worker can create a huge sparse file quickly and make post-stop hashing or
promotion unbounded. Close this without inventing a post-outcome or global
numerical constant:

- require each canonical candidate/operation manifest to freeze a positive
  `max_total_output_bytes` before admission;
- reserve/refuse that declared amount before spawning behavior;
- count logical bytes and allocated bytes with symlink/hardlink/sparse-file
  rules pinned;
- refuse or invalidate before hashing/copying content beyond the frozen bound;
- make every read/hash/promotion loop bounded and restartable;
- release the reservation on exactly one durable terminal route.

If the existing signed surfaces cannot support a manifest-owned byte budget
without a new author selection, expose one bounded author cell and stop. Do not
invent a universal GiB value.

### 5. Executability and non-regression

Supply:

- a total state/transition table;
- process topology and FD inheritance table;
- request/reply and journal tables;
- watchdog timing/failure table;
- output custody/promotion table;
- crash-cut matrix;
- exact implementation surface and frozen-file list;
- a test matrix that catches each prior Opus/Sol/Codex finding;
- a disposition table mapping every prior finding to exact v2 sections.

Do not weaken the signed batch-settlement amendment or generic-harness
contract. Do not modify signed events, scientific constants, roots, frame,
worlds, T envelope, or claim semantics. Do not authorize a new entry point,
production call-graph manifest, activation, or execution.

## Verdict and review handoff

The closure's first line must be exactly one of:

- `READY_FOR_OFFICINA_SUPERVISOR_V2_XY_REVIEW`
- `BLOCKED_OFFICINA_SUPERVISOR_V2_AUTHOR_CELL`
- `BLOCKED_OFFICINA_SUPERVISOR_V2_CONTRACT_CONFLICT`

If ready, include no more than three bounded questions each for Opus and Sol.
Ask Opus to attack Linux/process/crash executability and Sol to attack
idempotency, observation leakage, validity, and scientific non-regression.

State explicitly that
`I_ACCEPT_OFFICINA_SUPERVISOR_CONTROL_CHANNEL_AMENDMENT` remains **not
signable** until both fresh X/Y reviews accept this v2. Confirm the complete
negative authorization and that T remains `NOT_ACTIVATED`.
