# Task for Claude Code Fable 5: Officina supervisor output-capacity author choice

Work in `/home/master/llm_projects/philosophia`.

This is a bounded author-choice task, not a v2.1 repair. Do not edit the v1/v2
supervisor drafts, code, tests, signatures, reviews, or runtime artifacts. Do
not start any Officina process, FIFO, watchdog, worker, journal, smoke, or test.
Do not create entropy, activation, capability, world, learner, output, datum,
or scientific outcome. Read-only platform/storage inspection is allowed. T
remains `NOT_ACTIVATED`.

## Read first

- `successor/OFFICINA_GENERIC_HARNESS_SUPERVISOR_CONTROL_CHANNEL_V2_DRAFT.md`
- `reviews/fable_officina_supervisor_control_channel_v2_closure.md`
- `reviews/opus_officina_supervisor_control_channel_v2_review.md`
- `reviews/sol_officina_supervisor_control_channel_v2_review.md`
- `successor/OFFICINA_SUPERVISOR_AUTHOR_SELECTIONS_V1_SIGNATURE.md`
- `successor/OFFICINA_SUPERVISOR_AUTHOR_CHOICE_PACKET_V1_DRAFT.md`
- `successor/AUTHOR_SELECTIONS_V1_SIGNATURE.md`
- `successor/OFFICINA_GENERIC_HARNESS_SIGNATURE.md`
- the signed T envelope, activation protocol, batch-settlement amendment, and
  generic-harness composite
- existing immutable timing/storage/feasibility reports only as engineering
  evidence; do not infer a scientific outcome or learner success from them

## Governing reconciliation

Both X and Y returned `REVISE_OFFICINA_SUPERVISOR_CONTROL_CHANNEL_V2`.
A3/B1/C1/D1 remain closed. All repairs except aggregate output capacity are
mechanical.

Opus says `statvfs` reservation can avoid a new author cell. Sol says a hard
aggregate capacity/quota policy requires one. Apply the stricter rule: a
dynamic free-space observation alone is not enough because it does not bound
hash/copy time, retained quarantine, or accumulated `T_PROMOTED` custody. Do
not let v2.1 choose a capacity provider, mechanism, or number silently.

## Deliverables

Write exactly two new files:

1. `successor/OFFICINA_SUPERVISOR_OUTPUT_CAPACITY_AUTHOR_CHOICE_PACKET_V1_DRAFT.md`
2. `reviews/fable_officina_supervisor_output_capacity_author_choice_packet_v1.md`

Do not write v2.1 yet.

## Required choice design

Present two or three mutually exclusive, executable options. Each option must
include one exact selection token and must pin all of the following:

1. **Enforcement architecture.** Explain how bytes are prevented or stopped
   during production, not merely counted after worker exit. Compare at least:
   supervisor-mediated bounded output transport versus a real kernel/filesystem
   quota or preallocated provider. A plain integer ledger or `statvfs` check is
   not enforcement.
2. **Numerical envelope.** Exact per-operation and aggregate byte limits, their
   units, scaling (if any) with `device_units`, and why the values are adequate
   for the signed learner/checkpoint surface. Values must come from an
   outcome-independent source: hardware/filesystem capacity, immutable
   engineering measurements, model-size arithmetic, or an explicit author
   resource commitment. No result-dependent adjustment.
3. **Complete custody set.** Aggregate accounting must include live output,
   pending settlement, failed/quarantined bytes, and retained
   `runtime/T_PROMOTED/**`. Moving or renaming bytes must not replenish the
   envelope.
4. **Reservation lifecycle.** Exact pre-admission reserve/refuse predicate,
   concurrent accounting, crash reconstruction, and the one durable event or
   artifact that releases capacity. Quarantine continues to consume capacity
   until an authorized deterministic disposal/archive transition actually
   removes or transfers custody.
5. **Retention/disposal.** State whether outputs are retained for all T, deleted
   under a deterministic class-based rule, or require a signed author/resource
   disposition. No deletion or quota increase may depend on whether an output
   looks promising, failed, or helps a desired candidate.
6. **Liveness.** Bound enumerate/hash/copy work and require watchdog-ack service
   during long supervisor loops. Include filesystem safety margin and behavior
   on `ENOSPC`, quota exhaustion, sparse files, and restart.
7. **A3 boundary.** State what is mechanical for contract-following workers and
   what remains procedural against a deliberate same-UID process. Do not
   over-claim kernel isolation and do not make this Q/C-citable.
8. **Deployment and code surface.** Required host setup, portability, import
   allowlist/frozen-file delta, and whether a power cycle preserves enforcement.
   Prefer zero new production root and no change to signed runtime events.

Do not recommend an option unless it is enforceable on the current host with a
fail-closed preflight. If an option requires root/system administration, say so
and give the exact prerequisite. If the current platform cannot support a
proposed kernel quota, do not present it as immediately executable.

The recommendation should minimize governance and implementation complexity
without creating unbounded output work. A fixed hard ceiling is acceptable;
the fact that a number is conservative is not a defect if Kirill signs it
before implementation.

## Platform audit

Perform only read-only checks needed to support the options: filesystem type,
free/total bytes, relevant mount/quota features, and immutable existing output
or checkpoint sizes. Separate current observations from portable guarantees.
Record exact commands/facts in the packet, but do not create a benchmark or
write probe data.

## Closure requirements

The closure must:

- start with exactly `READY_FOR_OFFICINA_SUPERVISOR_OUTPUT_CAPACITY_AUTHOR_SELECTION`
  or `BLOCKED_OFFICINA_SUPERVISOR_OUTPUT_CAPACITY_AUTHOR_SELECTION`;
- explain why this is the sole remaining author cell and why the remaining
  X/Y findings are mechanical;
- give a consolidated response template with exactly one option selected;
- state that selection authorizes only a later v2.1 correction;
- state that `I_ACCEPT_OFFICINA_SUPERVISOR_CONTROL_CHANNEL_AMENDMENT` remains
  not signable until v2.1 receives fresh bounded X/Y confirmation;
- confirm the complete negative authorization, T `NOT_ACTIVATED`, and programme
  claim `OPEN`.
