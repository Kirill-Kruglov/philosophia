# Prompt for Claude Code Opus 5: Officina supervisor/control-channel v2.1.8 bounded repair

You are **Claude Code Opus 5 acting only as the specification author**, not an
independent reviewer. Work in `philosophia` at or after commit
`2b25d690acbd122fc94cb58f617bb27e56308e78`.

Read the complete supervisor v2 through v2.1.7 chain, author signatures,
inherited generic-harness/batch-settlement contracts, and both independent
v2.1.7 reviews:

- `reviews/opus_officina_supervisor_control_channel_v2_1_7_final_confirmation.md`
- `reviews/sol_officina_supervisor_control_channel_v2_1_7_final_confirmation.md`

Pinned hashes:

```text
789732476938ca8c1436eebb49e54a1f994c2c000b7689e1eb9aad082f6871a8  v2.1.7 correction
2e4bee2305bafb5825a6ac1cca4d131dcbdf730aa048f29c7023cf679c9936e6  Opus X review
5c82f7c1894d3e76239ee26a611731d102a2891486a9c2d667ce9738956d533b  Sol Y review
```

Both lines returned `REVISE_OFFICINA_SUPERVISOR_V2_1_7`. All findings govern:
Sol C217-1/M217-1/m217-1 and Opus X217-M1/X217-m1. Treat author closures as
untrusted. Static authoring only: no code/test/probe/process execution and no
runtime modification.

## Deliverables

Create exactly two new files and alter nothing else:

1. `successor/OFFICINA_GENERIC_HARNESS_SUPERVISOR_CONTROL_CHANNEL_V2_1_8_CORRECTION.md`
2. `reviews/opus5_officina_supervisor_control_channel_v2_1_8_closure.md`

The correction must be a narrow replacement layer over v2.1.7 with an exact
replacement index. Closure line 1 exactly one of:

- `READY_FOR_OFFICINA_SUPERVISOR_V2_1_8_FINAL_XY_CONFIRMATION`
- `BLOCKED_OFFICINA_SUPERVISOR_V2_1_8_AUTHOR_CELL`
- `BLOCKED_OFFICINA_SUPERVISOR_V2_1_8_CONTRACT_CONFLICT`

No scientific author cell is expected. This repair **does** amend a signed
engineering surface: the absolute-import allowlist. Name that delta loudly;
the prior “zero import delta” claim is superseded and must not survive.

## Mandatory repairs

### R1. Mechanically normalize child-reaping state before fork (C217-1/X217-M1)

Add exactly `signal` to `ALLOWED_ABSOLUTE_IMPORTS`, with no broader import
expansion. Before the first `os.fork` of every attempt, in the CLI main thread
and while the bootstrap owns its signed lock/state, execute and verify the
pinned Linux/CPython operation that installs `SIGCHLD = SIG_DFL` and clears an
inherited `SIG_IGN`/`SA_NOCLDWAIT` disposition. State the exact `signal` API,
return/error handling, main-thread premise, and fail-closed pre-fork route.
No fork may occur if normalization or verification is inconclusive.

Pin a sole-reaper/single-thread contract for this child: no handler,
`subprocess`, helper thread, other `wait*`, or external component in the CLI
may reap `pid_mid`; enumerate every permitted wait site. Reset/verify on every
attempt rather than inheriting trust from process startup.

Even after normalization, map **`ECHILD` to INCONCLUSIVE**, never directly to
`PROVED_DEAD`. This removes safety dependence on a subtle premise and handles
contract violation/prior reaping conservatively. Delete every test/prose row
asserting `ECHILD ⇒ PROVED_DEAD` or zombie pin without its mechanically
established scope.

Document precisely why `signal.signal(SIGCHLD, SIG_DFL)` on the pinned
Linux/CPython stack clears the relevant inherited disposition/flags; require
independent reviewers to verify that platform fact. No new timeout/resource
constant or author choice.

### R2. Fork ownership pins PID until authoritative reap (C217-1/X217-m1)

After a successful first fork under normalized reaping state, define the
parent's own-child relationship as the primary identity authority. Until this
sole reaper obtains `waitpid(pid_mid, ...) == pid_mid`, the child's PID cannot
be reused under the pinned premise. `/proc` identity remains useful for durable
handoff/T2 but is not required to signal the still-owned child.

Rebuild `IDENTITY_SAFE` as a total decision table. Include explicitly:

- PRESENT_VALID with captured matching identity;
- PRESENT_VALID with no captured identity and matching ppid;
- PRESENT_VALID with no captured identity and ppid mismatch;
- ABSENT, UNREADABLE, UNPARSABLE, ERROR;
- child already reaped by this route;
- ECHILD/contract-violation state.

No branch may signal a PID after authoritative reap or under an inconclusive
ownership premise. Pin capture-to-signal races and every signal result. Remove
the false assumption that inherited signal state is harmless.

### R3. Eliminate T3 as a returning live-child terminal (M217-1)

No route may return, release the lock, remove `SPAWNING.json`, or discard every
durable/in-process handle while `pid_mid` may remain live and unreaped. Delete
T3's “install nothing and return” semantics and the contradictory “DENIED
signals” membership.

Under the normalized sole-reaper premise, stage M must safely terminate and
authoritatively reap its own child even when `/proc` is unreadable. SIGTERM,
SIGKILL and wait results remain fully enumerated. A stopped child must be
SIGKILLed and reaped. If host faults keep proof inconclusive, choose one exact
safe continuation:

- remain an explicit non-returning/blocking reaper state while retaining the
  lock and in-process fork handle until authoritative reap; or
- install a truthful durable identity handle with a total reviewed resolver.

Do not silently pick a resource deadline, rely on caller exit/GC/operator, or
return after dropping the handle. Prefer the no-new-object route if it is total.
Any explicit host-fault blocked state is process control, not science/resource
evidence, and must not falsely free the singleton.

T2 may remain only when its existing `SPAWNING_MIDDLE.json` is truthfully
constructible and its predicate is disjoint from every other terminal. Prove
the existing s4 resolver is total for it. T1 requires `waitpid == pid_mid`, not
ECHILD.

### R4. Correct stage-M causal proof (m217-1)

For c5/c6/c7, state the actual sequence: no c8 release byte was written; the
middle remains at m0 and owns `rel1_w`; its own m0 bound or the parent's
identity-safe signal/reap route controls exit. The fork-shared lock prevents a
new CLI from acquiring until the middle exits. Remove the m5/rel2 argument from
all stage-M prose, tests and closure claims; retain it only for routes that can
actually reach m5.

Re-run stopped/resumed middle, queued-byte, writer-copy, timeout and immediate-
new-CLI schedules. This causal repair does not substitute for R3.

### R5. Preserve already closed repairs

Carry v2.1.7's object-bound observation and both barriers, A3 residual, complete
bound-language replacement, `CLOSE_OWNED`, MALFORMED dominance, branch bodies,
K1 custody and all other closed surfaces byte-for-byte except exact references
affected by R1-R4. Do not reopen them or claim the reaper repair also proves
filesystem exclusion.

## Required proof obligations

1. Exact v2.1.7-to-v2.1.8 replacement index and one-to-one disposition of all
   five X/Y findings.
2. Loud allowlist delta: only `signal` added; exact pre-fork normalization,
   verification, errors, main-thread and sole-reaper table.
3. Complete `waitpid` table with ECHILD inconclusive and proof only on returned
   `pid_mid`; complete fork-ownership/PID-reuse proof.
4. Total `IDENTITY_SAFE` table including ppid mismatch and every stat result.
5. T1/T2 plus no-return host-fault automaton; T3 removed; stopped-child and
   long-lived-CLI crash/restart traces; no handle discarded while child may act.
6. Correct c5-c7 m0/rel1/lock causal trace; no m5 claim at stage M.
7. No-regression for v2.1.7 C1/bound fixes, A3/B1/C1/D1/K1, bootstrap, GC,
   watchdog, custody, generic harness, batch settlement, events, E1/E2/E3,
   Q/C and T.
8. Exact future implementation/tests including inherited SIG_IGN and
   SA_NOCLDWAIT fixtures, but no implementation now.
9. One fresh bounded confirmation question each for Opus 4.8 X and GPT-5.6 Sol
   Y, requiring SHA recomputation and adversarial reaper/T3 review.

## Prohibitions and authorization boundary

Do not edit prior artifacts, code, tests, runtime trees, Cursor's dirty files,
or unrelated changes. Do not run anything or create runtime/scientific data.

Do not authorize
`I_ACCEPT_OFFICINA_SUPERVISOR_CONTROL_CHANNEL_AMENDMENT`. It remains unavailable
until fresh X and Y reviews confirm the exact v2.1.8 bytes. Do not authorize
implementation, T activation, entropy, spend, Q/C or later gates.

Confirm exactly two deliverables, T `NOT_ACTIVATED`, claim `OPEN`, no artifact.
