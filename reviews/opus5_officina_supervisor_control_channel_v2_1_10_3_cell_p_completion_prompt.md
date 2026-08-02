# Prompt for Claude Code Opus 5: complete Officina supervisor Cell P

You are **Claude Code Opus 5 acting only as the specification author**. You are
not an independent X-line or Y-line reviewer of this chain. Work in the local
`philosophia` repository. Do not edit any existing file. Do not implement code,
run tests, execute a probe, create a process/socket/fork/signal experiment, or
move T/Q/C state. T must remain `NOT_ACTIVATED`; the programme claim remains
`OPEN`.

## Governing input

Read the full carried supervisor chain, especially:

- `successor/OFFICINA_GENERIC_HARNESS_SUPERVISOR_CONTROL_CHANNEL_V2_1_10_CORRECTION.md`
- `successor/OFFICINA_GENERIC_HARNESS_SUPERVISOR_CONTROL_CHANNEL_V2_1_10_1_CORRECTION.md`
- `successor/OFFICINA_GENERIC_HARNESS_SUPERVISOR_CONTROL_CHANNEL_V2_1_10_2_CORRECTION.md`
- `reviews/opus5_officina_supervisor_control_channel_v2_1_10_2_closure.md`
- `reviews/officina_supervisor_v2_1_authorship_note.md`

Recompute and pin their hashes. Treat every prior author closure as an untrusted
self-assessment. Preserve the signed A3/B1/C1/D1/K1 cells and every unrelated
negative route unless this correction explicitly presents a new author choice.

## Why v2.1.10.2 is not yet a complete author-choice packet

The stop at Cell P is correct: the PCS changes signed C1/B1/D1 surfaces and no
existing acceptance token silently covers it. But P1/P2/P3 is not exhaustive.
There is a fourth architecture that appears to dominate P2 on every property
P2 claims to preserve:

```text
P4: CLEAN-BOOTSTRAP-PARENTED WATCHDOG

The already-isolated SUPERVISOR role-bootstrap, while it still has the exact
reviewed `{os, sys}` closure and BEFORE importing `generic_harness.py`, any
project module, or any client code:

1. creates the watchdog update/ack pipes;
2. creates the watchdog as its own direct child through the same object-bound,
   `-I -S -E -P`, empty-environment role-bootstrap mechanism;
3. completes watchdog registration/ack under signed C1;
4. only then imports/enters the supervisor role in the SAME process, so that
   process remains the watchdog's parent for the whole generation.

The PCS remains the process authority for controller/worker roles. It does not
spawn, reap, signal, or hold a handle for the watchdog.
```

This route appears to preserve both signed C1 detectors:

- watchdog observes supervisor death by `getppid() != recorded` or update-pipe
  EOF;
- supervisor observes watchdog death with `waitpid` on its own direct child.

It also gives the watchdog a fresh isolated address space by construction,
unlike P2's contaminated in-process fork. Its explicit cost is narrow and
already close to the original C1 surface: after the bootstrap imports the
supervisor role, that supervisor retains process authority over exactly one
child, the watchdog. It must never gain PID authority over controllers/workers.

Do not assume this route works merely because it is attractive. Trace it
against every carried process, fd, isolation, signal, reaping, custody,
idempotency, crash, and verifier invariant. If it is impossible, prove the
contradiction precisely. If it is implementable, Cell P must be repaired before
any author selection.

## Required work

Create exactly two new files:

1. `successor/OFFICINA_GENERIC_HARNESS_SUPERVISOR_CONTROL_CHANNEL_V2_1_10_3_CORRECTION.md`
2. `reviews/opus5_officina_supervisor_control_channel_v2_1_10_3_closure.md`

Do not modify v2.1.10, v2.1.10.1, v2.1.10.2, their closures, code, tests,
verifiers, manifests, signatures, prompts, or runtime artifacts.

### R1. Decide only whether P4 is a real architecture

Give a literal, mechanical trace beginning at the isolated SUPERVISOR
role-bootstrap and ending at normal shutdown. Pin:

- the exact step before the first project/client import at which the watchdog
  pipes and child are created;
- whether creation uses `posix_spawn`, `fork+exec`, or another already-allowed
  primitive, with one route only and an object-bound executable/source proof;
- exact parent/reaper relations before and after the supervisor imports its
  role module;
- which process knows the watchdog PID and which code can exercise that
  authority;
- all descriptor maps, `CLOEXEC` behavior, and ownership transfers;
- C1 registration, heartbeat/freeze, supervisor-death, watchdog-death, and
  shutdown sequences;
- PCS death, supervisor death, watchdog death, and crash cuts during watchdog
  construction;
- why controllers/workers remain PCS-only and cannot be reaped or signalled by
  the supervisor;
- why no client import, `.pth`, site customization, audit/import/trace hook,
  monkeypatch, retained callback, at-fork callback, helper thread, or finalizer
  exists before watchdog construction.

If the supervisor role-bootstrap cannot both remain the watchdog parent and
enter the supervisor role without reopening contamination, say exactly where
the contradiction occurs. Do not quietly fall back to P2.

### R2. Recompute the PCS design under P4

If P4 is implementable, do not append it as a prose-only option. Recompute every
v2.1.10.2 surface it changes:

- `SPAWN_WATCHDOG` must be removed from the PCS operation enum, protocol table,
  handle state machine, descriptor-vector table, process tree, fd-custody map,
  primitive-to-consumer map, crash matrix, import/primitive closure, verifier
  rules, and tests unless you prove it remains necessary for a different
  single-valued purpose;
- the new `t-pcs.v1` operation count and every field/count statement must agree;
- the PCS journal must contain no watchdog operation under P4;
- the supervisor-bootstrap watchdog path needs its own exact refusal and
  partial-construction cleanup automaton without inventing an outcome;
- PCS loss must not orphan an ungoverned watchdog or permit a false valid
  continuation; state the exact supervisor/watchdog continuation on PCS EOF;
- shutdown must prove that watchdog death is observed/reaped before the
  supervisor exits or state a fail-closed alternative;
- the role-bootstrap's import and primitive allowlists must reflect the actual
  clean pre-import construction surface, with no universal builtin-identity
  shortcut already refuted by the carried chain.

Carry P1 and P3 accurately. Evaluate whether P2 is strictly dominated by P4;
if it is, withdraw P2 rather than preserving a token alternative. If it is not,
name the property P2 uniquely supplies. Do not call the resulting options
exhaustive without a bounded argument.

### R3. Keep the remaining costs loud

P4 does not by itself erase the B1 and D1 author changes. State plainly that:

- the PCS is still a mandatory resident process and an unrecoverable
  whole-generation failure point for controller/worker authority;
- `t-pcs.v1` still introduces a second durable control-plane journal;
- fd-bearing `SPAWN_ROLE` replies remain non-redeliverable as capabilities even
  if their byte record is replayable;
- `_socket`/`SCM_RIGHTS`, five production roots, and Linux-specific capability
  transfer remain part of P4 unless exact recounting yields a different number;
- the supervisor's one-child watchdog PID authority is a narrow signed trust
  surface, not "no PID authority".

No option may be recommended by silently discounting those costs.

### R4. Engineering honesty checks

Re-audit, without executing a probe:

- the claim that a violating `recvmsg` may be repaired by sweeping every fd
  outside a pinned `/proc/self/fd` set: prove this cannot close a legitimate
  authority fd and that the scan itself is single-valued, or replace it with a
  bounded exact received-fd cleanup rule;
- all `SCM_RIGHTS` close/ACK/crash cuts after removing any watchdog messages;
- `SOCK_SEQPACKET` record assumptions, truncation flags, and `MSG_CMSG_CLOEXEC`;
- exact source/interpreter binding for the watchdog's isolated exec;
- all numeric statements such as operation count, root count, fd maxima, and
  test-row references.

These are author pre-review checks, not empirical validation.

### R5. Governance output

If P4 is implementable and the corrected option set is complete enough for an
author choice, closure line 1 must be exactly:

```text
READY_FOR_OFFICINA_SUPERVISOR_CELL_P_AUTHOR_SELECTION
```

Present exact mutually exclusive tokens and a compact gains/costs table, but
select none. The likely P4 token is:

```text
I_SELECT_SUPERVISOR_PROCESS_AUTHORITY_P4_CLEAN_BOOTSTRAP_PARENTED_WATCHDOG
```

Use a different exact token only if the final architecture materially differs.
`I_ACCEPT_OFFICINA_SUPERVISOR_CONTROL_CHANNEL_AMENDMENT` remains unavailable
until an author option is selected and the resulting composite passes fresh
independent X/Y review.

If P4 is impossible, line 1 must be:

```text
P4_REFUTED_OFFICINA_SUPERVISOR_CELL_P_REMAINS_BLOCKED
```

and the proof must be sufficient for Kirill to choose among the surviving
options. If the option set is still incomplete or another signed surface is
found, emit a precise `BLOCKED_...` verdict instead of `READY`.

## Required closure contents

- exact replacement index over v2.1.10.2;
- one-to-one R1-R5 disposition;
- byte/hash custody and confirmation that existing files were untouched;
- process/fd/authority table for each surviving option;
- weakest-points section written against your own proposal;
- exact next gate and explicit negative authorization;
- T `NOT_ACTIVATED`, programme claim `OPEN`, no code/test/probe/run/entropy/data.

Do not ask X/Y to accept the composite in this round. This is an author-cell
completion only. After an informed Kirill selection, a separate correction may
bind the selected option and only then request independent X/Y review.
