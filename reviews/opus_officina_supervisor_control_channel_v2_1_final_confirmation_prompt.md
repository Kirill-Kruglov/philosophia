# Claude Opus 4.8 X-line: independent final check of Officina supervisor v2.1

Use a clean review context. Work in
`/home/master/llm_projects/philosophia`.

Important provenance: v2.1 was authored by **Claude Code Opus 5** while
executing a prompt whose filenames retained a historical `fable_` label. Read
`reviews/officina_supervisor_v2_1_authorship_note.md`. You are Opus 4.8 acting
as an independent X-line reviewer; do not treat the internal “Fable 5” heading
as independence evidence.

Static/read-only review only. Do not edit code, tests, contracts, signatures,
existing reviews, or runtime artifacts. Do not start any test, supervisor,
controller, worker, watchdog, pipe/FIFO, journal, or smoke. T remains
`NOT_ACTIVATED`.

## Read first

- `successor/OFFICINA_GENERIC_HARNESS_SUPERVISOR_CONTROL_CHANNEL_V2_DRAFT.md`
- `successor/OFFICINA_GENERIC_HARNESS_SUPERVISOR_CONTROL_CHANNEL_V2_1_CORRECTION.md`
- `reviews/fable_officina_supervisor_control_channel_v2_1_closure.md`
- `reviews/opus_officina_supervisor_control_channel_v2_review.md`
- `reviews/sol_officina_supervisor_control_channel_v2_review.md`
- `successor/OFFICINA_SUPERVISOR_AUTHOR_SELECTIONS_V1_SIGNATURE.md`
- `successor/OFFICINA_SUPERVISOR_OUTPUT_CAPACITY_SELECTION_V1_SIGNATURE.md`
- the output-capacity choice packet
- `successor/OFFICINA_GENERIC_HARNESS_SIGNATURE.md`
- the signed batch-settlement and generic-harness composite
- current dirty implementation/tests read-only, only to distinguish contract
  executability from implementation deviation

A3/B1/C1/D1/K1 are closed. Do not reopen them. Determine whether the v2+v2.1
composite gives one executable Linux continuation at every cut.

## Required attacks

Re-test every prior X Critical/Major and confirm its exact disposition. In
addition, attack these newly visible surfaces rather than trusting the closure.

### A. Durable intent allocation and GC

Trace client intent slots, `.done.json`, journal phase files, scope tombstones,
and GC across a fresh CLI, simultaneous clients, client crash, takeover, and
process terminal. The W7 table says client slot/terminal files may be removed;
W1 allocation finds the highest remaining slot. Determine whether deletion can
reuse an occurrence index, turn a new heartbeat into
`ALREADY_ACKNOWLEDGED`, lose forward progress, or collide with a tombstone.

Verify that implicit acknowledgement by successor occurrence proves the prior
effect reply was actually observed, and that client-owned control files cannot
create a second effect or global invalidity. Check whether the permanent
per-scope tombstone contains enough information for every old occurrence,
rather than only the last reply hash.

Do not accept `hash(command,args)` as an intent identity for repeated
heartbeats/status. Re-run the complete eight-command crash reducer.

### B. Spawn and singleton markers

The supervisor/watchdog now enter through in-process post-fork functions, so
their `/proc/*/cmdline` is not replaced by `exec`. Yet W2.2 says a CLI timeout
or next holder finds/kills a half-initialized grandchild by `spawning_id` using
the W2.4 cmdline-marker predicate. Determine whether that marker can actually
exist in the grandchild's cmdline. Trace CLI death while the grandchild retains
`SPAWN.lock`, grandchild hang, identity-install collision, and bounded recovery.

For controller/worker, verify the exact fixed bootstrap is compatible with
arbitrary registered learner argv: who parses the appended
`--officina-spawn-intent`/`--officina-ctrl-fds`, who self-stops, and what happens
between fork and exec or when the target program does not recognize those
arguments. No behavior/capability may begin before durable binding and
watchdog ack.

### C. Watchdog writer and evidence

The author-selected C1 described a freezer that was not a runtime writer. v2.1
lets the watchdog durably write `runtime_control/**/FREEZE/*.json`. Decide
whether that is a compatible control-plane witness or an unauthorized second
durable authority. If it is incompatible, test the fail-closed pipe-loss
alternative rather than opening a new author choice.

Check process-tree enumeration races, reparented/escaped descendants,
quiescence proof, freeze timestamp, old-deadline authority, ack sample time,
supervisor death, and the single PROCESS/unknown-invalid routes.

### D. K1 admission and start crash cuts

W4.4 writes committed journal and cached `ADMITTED` reply at steps 7-8, then
`SIGCONT`s the worker at step 9. Trace a crash after reply durability but before
`SIGCONT`: does the reducer have a durable locator proving whether start
occurred, or can it return `ADMITTED` forever for a stopped worker? Require one
single-valued repair if needed.

Attack the output frame parser, partial raw-content cuts, pipe backpressure,
multi-file hash state, zero-output completion, worker/status ordering,
supervisor crash mid-stream, capacity reconstruction, quarantine retention,
and disposition proof. Verify the signed author-disposition artifact itself has
an exact schema/path/verification rule rather than only a referenced hash.

### E. Schemas, transport, and promotion

Check every W7 object has exact keys, predecessor/hash binding, owner, lock,
retention, and crash semantics. Re-test newline framing, reply path, descendant
roles, fixed PENDING observation, frame/path bounds, same-filesystem preflight,
held descriptors, promotion errno routes, and §S6 non-regression. Flag duplicate
or contradictory headings only if they create normative ambiguity.

## Deliverable

Write exactly one new file:

`reviews/opus_officina_supervisor_control_channel_v2_1_final_confirmation.md`

First verdict line exactly one of:

- `OFFICINA_SUPERVISOR_V2_1_XLINE_CONFIRMED_FOR_AUTHOR_SIGNATURE`
- `REVISE_OFFICINA_SUPERVISOR_CONTROL_CHANNEL_V2_1`
- `BLOCKED_OFFICINA_SUPERVISOR_CONTROL_CHANNEL_V2_1`

Lead with Critical/Major findings and minimal exact repairs. State whether any
repair reopens an author cell. Answer the three Opus questions in the v2.1
closure explicitly. If confirmed, name the exact acceptance token made
eligible conditional on Y. Confirm no runtime action and T `NOT_ACTIVATED`.
