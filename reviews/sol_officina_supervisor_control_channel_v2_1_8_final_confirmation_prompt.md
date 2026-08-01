# Prompt for GPT-5.6 Sol: independent Officina supervisor v2.1.8 Y-line confirmation

Act as the **independent clean-context Y-line reviewer**. Claude Code Opus 5
authored v2.1.8. Treat its closure/chat response as untrusted and rerun your own
v2.1.7 counterexamples plus the X-line findings from that round.

Work in `philosophia` at or after commit
`6e158560a8bd452d6780d9e279a079f41f4b78fe`. Read the complete supervisor v2
through v2.1.8 chain, author selections/signatures, inherited generic-harness
and batch-settlement contracts, and both v2.1.7 final reviews.

Recompute the SHA-256 of
`successor/OFFICINA_GENERIC_HARNESS_SUPERVISOR_CONTROL_CHANNEL_V2_1_8_CORRECTION.md`;
expected:

```text
33b0b91621439bdc42b4c41b3d00741b8c20d014a686097d2bc63c001db0ed50
```

Static review only. Read-only file inspection and literal hashing/arithmetic are
allowed. Run no repository code, tests, probes, smoke commands, subprocess
experiments, signal experiments, forks, or Officina processes. Modify no
existing file or runtime state.

## Required question

Does v2.1.8 close your C217-1/M217-1/m217-1 and Opus X217-M1/X217-m1 exactly,
with a mechanically sound inherited-`SIGCHLD` repair, total reaper/ownership
automaton, no T3 orphan, no false `ECHILD`/`ESRCH` death claim, and no regression
or undeclared control-surface expansion?

Re-run independently:

1. **Allowlist containment and authority:** confirm the only signed engineering
   delta is `"signal"`, restricted to the CLI bootstrap, enumerated constants
   and two `c3n` functions. Audit every superseded zero-delta statement and the
   generic harness clause requiring a reviewed amendment. Reject any implicit
   extra API/importer, handler, durable object, schema, constant, token, operator
   action, or scientific choice.
2. **Inherited disposition counterexamples:** independently validate whether
   main-thread `signal.signal(SIGCHLD, SIG_DFL)` on the pinned stack clears a
   pre-existing `SIG_IGN` and the full `SA_NOCLDWAIT` flag. Distinguish the
   Python/kernel guarantee from `/proc`'s limited `SigIgn`/`SigCgt` observation.
   Attack fork-inherited and exec-inherited states. No fork may occur unless the
   complete required premise is actually established.
3. **`c3n` state machine:** enumerate old dispositions, return values,
   exceptions, wrong thread, `/proc` missing/unreadable/malformed/short masks,
   verification disagreement, retry and repeated attempts. Check main-thread,
   held-lock, immediately-pre-fork placement for every first fork and verify
   failure creates no process or partially authorized state.
4. **Reaper and wait table:** enumerate all five allowed wait sites and prove no
   other code can reap the child. Re-run `(pid,status)`, `(0,0)`, `EINTR`,
   `ECHILD`, arbitrary errors, stop/continue, deadline, prior reap, external
   reap, and auto-reap schedules. Only the targeted positive return proves
   death; every `ECHILD` route must remain inconclusive/contradicted.
5. **Identity and signals:** exhaust the ten-row identity table and all
   `/proc`/`ppid`/capture combinations. Confirm ownership rather than observation
   gates every TERM/KILL, `ESRCH` cannot become death under the premise, and
   contradiction irreversibly prevents another signal or capture. Attack PID
   reuse immediately after reap and under a failed normalization premise.
6. **T1/T2/B, no T3:** search the normative chain for every surviving T3 body,
   membership, test, or prose implication. Trace long-lived and stopped middles,
   no capture, later capture, authoritative reap, unreadable `/proc`, wait
   errors, process crash, restart, and second CLI. The three terminals must be
   disjoint/exhaustive and no returning route may abandon a possibly live child.
7. **Residual challenge:** decide explicitly whether B-CONTRADICTED's
   nontermination and T2's possible unreaped zombie are acceptable named
   process-control residuals under the chosen policy, or concrete blocking
   defects. Verify that existing `s4`/`s5`, wait ownership, lock lifetime, and
   record lifecycle give one lawful next action without a competing reaper or
   hidden manual repair.
8. **Full regression:** verify stage-M serialization at `m0`/`rel1` plus the
   fork-shared lock; then re-run object-bound observation and both barriers,
   mutation cuts, A3 residual, bound-language sweep, CLOSE_OWNED, malformed-first
   selection, branch/custody release, A3/B1/C1/D1/K1, GC/watchdog/singleton,
   generic harness/batch settlement, E1/E2/E3, Q/C and T inactivity.

Fail-closed is insufficient if a valid history is classified invalid, a live
process is untracked, or future progress silently wedges. Do not substitute the
author's examples, closure, or asserted Linux semantics for independent
reasoning from the pinned interface.

## Deliverable

Create exactly one file and modify nothing else:

`reviews/sol_officina_supervisor_control_channel_v2_1_8_final_confirmation.md`

Line 1 exactly one of:

- `CONFIRM_OFFICINA_SUPERVISOR_V2_1_8_Y`
- `REVISE_OFFICINA_SUPERVISOR_V2_1_8`

Include the recomputed hash and base, disposition of all five inherited
findings, all eight traces, new findings with severity/locus/counterexample/
smallest repair, no-regression table, explicit residual judgment,
author-cell/contract-conflict determination, and exact authorization boundary.

If confirmed, authorize only Kirill's token
`I_ACCEPT_OFFICINA_SUPERVISOR_CONTROL_CHANNEL_AMENDMENT`, conditional on X
confirming the same bytes. Authorize no implementation, commit, activation,
entropy, runtime construction, spend, Q/C, or science. If revised, keep it
unavailable.

Confirm no execution/change/artifact, T `NOT_ACTIVATED`, claim `OPEN`.
