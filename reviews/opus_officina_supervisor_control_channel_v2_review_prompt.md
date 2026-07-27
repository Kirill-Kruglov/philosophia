# Opus 4.8 X-line review: Officina supervisor/control-channel v2

Work in `/home/master/llm_projects/philosophia`.

Perform a bounded, adversarial Linux/process/crash-semantics review. Do not edit
code, tests, contracts, signatures, existing reviews, or runtime artifacts. Do
not start any Officina supervisor, controller, worker, watchdog, FIFO, journal,
or smoke. Static/read-only inspection only. T remains `NOT_ACTIVATED`.

## Read first

- `successor/OFFICINA_GENERIC_HARNESS_SUPERVISOR_CONTROL_CHANNEL_V2_DRAFT.md`
- `reviews/fable_officina_supervisor_control_channel_v2_closure.md`
- `successor/OFFICINA_SUPERVISOR_AUTHOR_SELECTIONS_V1_SIGNATURE.md`
- `successor/OFFICINA_SUPERVISOR_AUTHOR_CHOICE_PACKET_V1_DRAFT.md`
- `successor/OFFICINA_GENERIC_HARNESS_SUPERVISOR_CONTROL_CHANNEL_V1_DRAFT.md`
- `reviews/opus_officina_supervisor_control_channel_v1_confirmation.md`
- `reviews/sol_officina_supervisor_control_channel_v1_confirmation.md`
- `reviews/codex_officina_generic_harness_implementation_review.md`
- `successor/OFFICINA_GENERIC_HARNESS_SIGNATURE.md`
- the signed batch-settlement amendment and generic-harness composite
- current uncommitted `src/philosophia/officina/generic_harness.py` and tests,
  read-only, only to distinguish an implementable contract from a paper design

The author selections A3/B1/C1/D1 are closed. Do not reopen them. The question
is whether v2 makes them executable, total, and single-valued.

## Required attacks

### 1. Spawn, stop, identity, and takeover

Trace every crash cut from spawn intent through self-stop, PID/start-identity
capture, claim, start, lease, and `SIGCONT`.

In particular test the apparent gap that `t-spawn-intent.v1` is written before
the child exists and contains no child PID/start identity, while takeover later
claims it can kill a pre-claim child “by registry identity.” Determine whether
the v2 bytes provide any durable, race-free bridge. Also test whether a Python
adapter can make self-`SIGSTOP` its first behavior-capable action when interpreter
startup and module imports precede the adapter function.

Check singleton double-fork ownership, who retains `SPAWN.lock` until the
grandchild identity is durable, PID reuse, process-group membership/fork races,
own-child versus reparented zombies, and exact takeover authority.

### 2. Durable-object executability

For every object in §V2.3 require a byte-exact schema, path, installation and
mutation rule, owner, hash binding, retention/removal rule, and recovery cut.
Challenge the blanket “atomic no-replace unless noted” against objects whose
phase/table must change (`JOURNAL`, `LEASES`, operation state). Check that no
schema is merely named but undefined, including admission, FAILED/quarantine,
spawn-registry successor, settlement, ack, and freeze artifacts.

### 3. Watchdog C1

Try to construct schedules where a controller remains runnable after deadline,
the watchdog event is lost, group membership changes, the supervisor blocks in
hash/fsync/Git work, an update ack is stale, or either process dies. Verify that
the contract can establish the actual freeze time and group quiescence rather
than infer them from a later stopped/dead sample. Check that a positive overrun
has one exact existing invalidity cause/event route, not the unresolved
`PROCESS or CLOCK` wording.

The watchdog must never become a runtime writer. Ordinary Linux is not a
real-time scheduler; do not demand an impossible physical guarantee, but do
demand fail-closed detection and a single continuation.

### 4. Output custody and promotion

Verify that the manifest-owned bound is installed before behavior through a
reachable command path, that storage is actually reserved rather than merely
named, and that an arbitrarily large declared bound cannot create unbounded
hash/copy/disk work. Test sparse files, hardlinks, directory replacement,
cross-filesystem behavior, descriptor lifetime, restart offsets, quarantine,
reservation release, and every `SETTLEMENT.json`/rename crash cut.

### 5. Control transport and entry surface

Check FIFO open order, PIPE_BUF framing, concurrent clients, partial reads and
writes, reply-path substitution, peer identity, and endpoint-role enforcement.
Review the private `--supervisor-serve` / `--watchdog-serve` argv surface: decide
whether parentage checks can make it closed under A3 or whether in-process
post-fork function entry is the smaller mechanically safe implementation. Treat
this as an implementation-contract issue, not a new author choice unless no
single repair is possible.

### 6. Non-regression

Confirm every F3-F15, Sol mechanical repair, and Codex §S6 repair is present and
does not weaken the signed batch-settlement or generic-harness composite.
Separate contract defects from deviations in the dirty Cursor implementation.

## Deliverable

Write exactly one new file:

`reviews/opus_officina_supervisor_control_channel_v2_review.md`

Its first verdict line must be exactly one of:

- `OFFICINA_SUPERVISOR_V2_XLINE_CONFIRMED_FOR_AUTHOR_SIGNATURE`
- `REVISE_OFFICINA_SUPERVISOR_CONTROL_CHANNEL_V2`
- `BLOCKED_OFFICINA_SUPERVISOR_CONTROL_CHANNEL_V2`

Lead with Critical/Major findings, each tied to exact sections and a minimal
repair. State which prior findings are genuinely closed. Answer Fable’s three
Opus questions explicitly. If `REVISE`, say whether the repair is bounded and
whether it needs a new author choice. If confirmed, state the exact token made
eligible conditional on the Y-line.

Confirm no code or runtime action occurred and that T remains
`NOT_ACTIVATED`.
