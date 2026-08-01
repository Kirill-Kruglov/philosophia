# Prompt for Claude Code Opus 5: bounded Officina supervisor v2.1.9 repair

Act as the **specification author, not an independent reviewer**. Your v2.1.8
received one independent X confirmation and one independent Y `REVISE`. The Y
counterexamples govern the next bounded repair. Do not defend v2.1.8 by appeal
to the X verdict; close the concrete schedules mechanically.

Work in `philosophia` at or after commit
`64cf100df585db40b347ada3b21a0b692d250d3b`. Treat all existing files as
immutable evidence. Read the complete supervisor v2 through v2.1.8 chain, the
signed generic-harness and batch-settlement composites, author signatures, and
both v2.1.8 reviews.

Pin and independently recompute:

```text
33b0b91621439bdc42b4c41b3d00741b8c20d014a686097d2bc63c001db0ed50  successor/OFFICINA_GENERIC_HARNESS_SUPERVISOR_CONTROL_CHANNEL_V2_1_8_CORRECTION.md
663184378fc6fa48c5d83e96cf659d2d9eb58f67a18fd8c7ba0efcb528caea34  reviews/sol_officina_supervisor_control_channel_v2_1_8_final_confirmation.md
e879b39cf6e22c93bcf309ed4a15a7a1f56e00fbcc17fd8cfc2398b04aec099a  reviews/opus_officina_supervisor_control_channel_v2_1_8_final_confirmation.md
```

Static authoring only. Read-only inspection, literal hashing, and reasoning
from pinned Linux/CPython interfaces are allowed. Run no repository code,
tests, probes, signal/fork/subprocess experiments, smoke command, or Officina
process. Change no code, verifier, runtime state, activation artifact, entropy,
T/Q/C object, datum, or existing document. Create only the two deliverables
named below.

## Governing verdict

The Y-line `REVISE_OFFICINA_SUPERVISOR_V2_1_8` is binding. Close exactly:

- **C218-1 Critical:** an inherited same-process thread can wildcard-reap the
  child between identity observation and signal; the stale `OWNED` label can
  then signal a reused PID.
- **M218-1 Major:** W-2 through W-5 lack total result automata.
- **M218-2 Major:** the sole-root/importer rules simultaneously require and
  forbid `signal` in `generic_harness.py`.
- **M218-3 Major:** reachable `B-CONTRADICTED` has no lawful progress action.
- **m218-1 Minor:** short `/proc/self/status` signal masks can pass as verified.

Preserve the repairs independently accepted by both lines: the CPython/Linux
`SIGCHLD := SIG_DFL` full-disposition replacement; `ECHILD` and `ESRCH` never
proving death; total ten-row identity table; ownership-gated signals; deletion
of T3; T1/T2/B no-discard invariant; stage-M proof at `m0`/`rel1` and the
fork-shared lock; object-bound observation/barriers; bound-language sweep; all
signed A3/B1/C1/D1/K1 and harness/batch-settlement science/resource boundaries.

## Required repairs

### R1 — mechanically exclusive reaping, not a prose prohibition

Choose one implementable supported topology and make the safety proof close at
every instruction boundary. The preferred minimal route may restrict production
to a fresh, single-task CLI process, but it is acceptable only if the contract
mechanically establishes and preserves the premise from immediately before the
first fork through final reap. It must address:

1. inherited same-process tasks (`/proc/self/task`, including malformed,
   unreadable, changing, or more-than-one membership);
2. the race between task enumeration and `fork`;
3. asynchronous signal callbacks or any other path capable of creating a
   thread/waiter in that interval;
4. every public/in-process entry point: unsupported topology must refuse before
   fork, not silently inherit the production authority;
5. the complete source/call-graph rule excluding wildcard waits, another
   targeted waiter, `subprocess` ownership, finalizers, handlers, and thread
   creation for the whole ownership lifetime;
6. restart and long-lived CLI behavior.

A check that merely observes one task and then executes ordinary Python before
fork is not automatically a closed race. If the minimal topology cannot prove
this under the pinned interfaces, use a reviewed pinned-handle/pidfd design and
state its exact imports, syscalls, ownership, signal, wait, close, crash, and
PID-reuse semantics. Do not leave a design fork or hidden author choice in the
deliverable. Do not add a new scientific cell.

State a complete counterexample replay showing why the v2.1.8 schedule cannot
occur under the chosen topology. The proof must not depend on a detector that
runs only after a potentially wrong signal.

### R2 — one shared total wait automaton for W-1 through W-5

Define a single result classifier over at least:

- `waitpid == pid_mid`;
- `(0, 0)`;
- `EINTR` before and at the deadline;
- `ECHILD`;
- every other `OSError`;
- invocation after `REAPED`;
- stop/continue and the W-5 `m8`-reported-before-`m9` race.

Instantiate it for W-1, W-2, W-3, W-4, and W-5 with exact entry condition,
existing/derived deadline, state transition, record cleanup/handoff, lock
behavior, and continuation. Only the positive targeted-pid return may set
`REAPED`. No wait site may run after `REAPED`; no `ECHILD` may mean death. Reuse
existing signed constants where possible. If a new numeric constant or
scientific/resource choice is truly unavoidable, emit a loud
`BLOCKED_..._AUTHOR_CELL` verdict instead of choosing it.

### R3 — one real importer topology

Adopt the smaller Y repair unless it is provably impossible:

- `src/philosophia/officina/generic_harness.py` remains the sole executable
  root and is the exact permitted importer of `signal`;
- explicitly supersede the signed harness §9 no-`signal` sentence and every
  supervisor sentence that forbids `signal` in the generic harness;
- keep the exact four-member surface (`SIGCHLD`, `SIG_DFL`, `signal`,
  `getsignal`) and the exact normalization/verification call sites;
- permit no separate unnamed module, dynamic import, handler, extra API,
  importer, dependency, executable root, or call-graph edge.

Make the future verifier delta mechanically single-valued. This document still
must not edit `verification.py` or implementation code.

### R4 — make `B-CONTRADICTED` honest and total

After R1, prove whether `B-CONTRADICTED` is mechanically unreachable in every
supported execution and reachable only after a stated platform/kernel or
implementation-contract contradiction. If so, classify it explicitly as a
non-returning safety sink outside supported history and prove that this is not a
normal liveness route. If R1 still permits a competing reaper or any valid
supported path into it, provide a reviewed durable handoff/pinned-handle
resolver with exactly one lawful next action. Do not call `s5`, operator notice,
or indefinite retry a resolver. Do not delete a handle to a possibly live child
or authorize a signal after ownership is uncertain.

### R5 — fail closed on short signal masks

Before integer conversion/bit testing, require a bit representation that
actually contains the `SIGCHLD` position. At minimum pin and justify:

```text
4 * hexadecimal_digit_count >= int(signal.SIGCHLD)
```

or a stricter exact-width rule valid on the pinned platform. Empty, one-digit,
and just-below-required-width masks must route to `VERIFY_INCONCLUSIVE`; no fork.
Specify leading-zero, prefix, whitespace, duplicate-field, over-width, and
architecture behavior and add exact future test rows.

## Totality and regression obligations

Provide:

1. a literal v2.1.8 → v2.1.9 replacement index;
2. one-to-one disposition of C218-1, M218-1, M218-2, M218-3, m218-1;
3. a supported-entry topology table and complete pre-fork state machine;
4. the shared wait classifier plus five site-instantiation tables;
5. a signal/import/call-graph allowlist table;
6. an ownership × identity × wait × terminal product check;
7. schedules for inherited thread/wildcard wait, fork race, W-2…W-5, PID reuse,
   short masks, T2 zombie, and B-CONTRADICTED;
8. static future tests sufficient to distinguish the repair from v2.1.8;
9. a no-regression table over every carried signed surface;
10. exact code/control files a later implementation review may change, while
    preserving the current Cursor work and frozen runtime surfaces unless the
    normative repair explicitly requires otherwise.

Resolve the X/Y disagreement explicitly: record why the X confirmation was
reasonable on the disposition-reset facts but insufficient against Y's
same-process waiter/importer/wait-totality counterexamples. Do not count either
review as author support for your new bytes.

## Deliverables

Create exactly:

1. `successor/OFFICINA_GENERIC_HARNESS_SUPERVISOR_CONTROL_CHANNEL_V2_1_9_CORRECTION.md`
2. `reviews/opus5_officina_supervisor_control_channel_v2_1_9_closure.md`

Alter nothing else. The closure line 1 must be exactly one of:

- `READY_FOR_OFFICINA_SUPERVISOR_V2_1_9_FINAL_XY_CONFIRMATION`
- `BLOCKED_OFFICINA_SUPERVISOR_V2_1_9_AUTHOR_CELL`
- `BLOCKED_OFFICINA_SUPERVISOR_V2_1_9_CONTRACT_CONFLICT`

Use `READY` only if one bit-exact, implementable route closes all five findings
without a new author choice. Ask each independent line no more than three
bounded confirmation questions, concentrated on R1, R2/R4, and R3/R5.

Confirm explicitly: no implementation, test execution, signal/fork experiment,
entropy, activation, T process, spend, Q/C, datum, outcome, or claim movement;
T remains `NOT_ACTIVATED`, claim remains `OPEN`; the amendment token remains
unavailable pending fresh independent confirmation of the new identical bytes.
