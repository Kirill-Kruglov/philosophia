# Codex integration review: Officina generic harness

Date: 2026-07-27

## VERDICT: REVISE_IMPLEMENTATION

The accounting primitive is directionally correct and the submitted suites are
green, but the implementation does not yet implement several load-bearing
signed behaviors. The green tests largely test pure facades and injected
fixtures around those missing behaviors. Do not commit the four Cursor files
and do not create the production call-graph manifest.

## Findings

### Critical

**C1 - The supervisor, watchdog, and isolation boundary is not implemented.**

`SubprocessProcessOps` is assigned to `self.processes` but is never used.
`GenericHarness.start()` writes the start event and lease without starting or
owning the claimed process, checking PID start identity, reconciling group
membership, or installing a watchdog. `run_isolated_operation()` executes a
caller-supplied callback in the harness interpreter and returns its result hash
before settlement. `promote_after_settlement()` only checks that some named
charge event exists; it does not revoke, quiesce, synchronize, atomically
promote confined output, or bind the settlement to the operation.

This contradicts v2 sections 1, 2c.4, 5a, and 5b. The corresponding tests use
in-process lambdas and exception stubs, so they cannot detect shared mutable
memory, inherited file descriptors, escaped process groups, output visibility,
or a missing watchdog.

Code: `generic_harness.py:407-488`, `1077-1090`, `1265-1312`,
`2285-2319`. Tests: `test_officina_generic_harness.py:1779-1845`.

**C2 - E1/E3 boundary settlement is not connected to ordinary execution.**

`heartbeat()` uses the ordinary charge path and, when no successor reservation
exists after the charge, fabricates a fresh 60-second `Reservation` instead of
freezing the live set and entering the signed batch route. A crossing can
therefore leave a renewed live lease after E1 without
`T_ENVELOPE_EXHAUSTED`. The batch constructor/automaton is exposed as a
separate manual API; no watchdog, heartbeat, or close path invokes it at the
boundary.

Code: `generic_harness.py:1314-1365`, especially `1347-1358`.

**C3 - Batch archival is skipped, so an unarchived claim becomes resolved.**

The signed automaton requires `ARCHIVE` after all tuples (and `X`, where
applicable), and the unresolved-claim registry must continue blocking until the
exact archival commit exists. `next_batch_action()` returns `RESOLVED`
immediately after the runtime suffix. `BatchAutomatonAction.ARCHIVE` is never
returned or executed. `_unresolved_batch_claims()` therefore stops blocking
before archival.

The existing activation protocol already fixes archival boundaries, staged
sets, and trailers. Whether one additional deterministic batch commit
message/path rule is needed should be answered by X/Y review; silently treating
runtime completion as archival is not allowed.

Code: `generic_harness.py:160-173`, `1198-1217`, `1920-2020`.

**C4 - The signed D1 ledger-head recovery case is unreachable.**

`complete_batch_head_cache_if_authorized()` calls normal ledger parsing before
repair. Normal parsing refuses an external-head mismatch, so the method cannot
inspect and complete the signed crash cut where the ledger contains the
authorized next entry but the external head lags. The method only replaces the
state cache and its docstring incorrectly claims that ledger/head lag cannot
occur. The contract explicitly includes the append-to-head power-loss cut.
Tests simulate stale cache only.

Code: `generic_harness.py:1850-1890`. Tests:
`test_officina_generic_harness.py:1516-1602`.

### Major

**M1 - G5 recovery is evaluated against all historical invalidities, not
"since the last admission."**

Every old disposition is required to match the current head/state forever.
After the first valid post-recovery `T_PROCESS_STARTED`, the old disposition is
stale and the next heartbeat is blocked. The current test stops immediately
after the fresh start and misses this regression.

Code: `generic_harness.py:1543-1561`. Test:
`test_officina_generic_harness.py:1760-1771`.

**M2 - Ordinary transaction crash recovery is incomplete.**

The implementation injects cuts only around whole helper calls. It does not
implement the signed next-admission handling for a start event without a lease,
an orphan dependent artifact, ledger ahead of head, or state/lease successor
behind the durable event. `close()` also releases the global lock between
reading the pre-close lease and its heartbeat/final record transaction, leaving
an interleaving window that the signed template does not permit.

Code: `generic_harness.py:1265-1425`.

**M3 - Process identity and monotone sequence invariants are not enforced.**

Claims record the short-lived harness CLI PID, use `str(os.getpid())` as the
kernel start identity, and derive the next process sequence only from currently
live leases. A closed sequence can therefore be reused. Start/heartbeat do not
verify controller liveness, kernel start identity, process group membership,
declared streams, or immutable behavior inputs.

Code: `generic_harness.py:1228-1263`, `1265-1365`.

**M4 - Batch registry revalidation is not the signed full validation.**

The registry calls `validate_batch_claim()` without the current leases, state,
pre-head, and full-live-set inputs. A schema-valid file can therefore enter the
registry without the completeness proof required before authority exists. A
test deliberately relies on this weaker path to fabricate a second claim.

Code: `generic_harness.py:1198-1213`. Test:
`test_officina_generic_harness.py:1569-1583`.

**M5 - The real module CLI does not parse its signed invocation.**

`_argv()` reads `/proc/self/cmdline`, but `main()` drops only the Python
executable. Under
`python -m philosophia.officina.generic_harness ...`, the next argument is
`-m`, so every real command returns usage code 2. Tests call `main(argv)`
directly and do not exercise the signed module entry point.

Reproduced:

```text
OFFICINA_REPOSITORY=<repo> python -m philosophia.officina.generic_harness \
  start 000...000
exit=2
```

Code: `generic_harness.py:2336-2379`. Tests:
`test_officina_generic_harness.py:1985-2006`.

**M6 - Capability and promotion reads are not consistently lock-bound.**

`global_state()`, `process_state()`, and `promote_after_settlement()` read
state, leases, and ledger without holding `T_RUNTIME.lock`.
`promote_after_settlement()` issues its release token across that unprotected
snapshot. The activation protocol requires admission and capability issue/use
to revalidate under the global lock.

Code: `generic_harness.py:1160-1193`, `2297-2319`.

### Clarifications for X/Y

1. The review-record event contains the review-record hash, so the record
   cannot also contain that event's hash without a cycle. Cursor binds both
   `ledger_entry_sha256` and `ledger_head_sha256` to the durable pre-review
   head. Confirm that this is the only intended reading and require a
   regression test, or name the missing rule.
2. `TState.charge_batch_settlement()` accepts a caller-supplied current head
   although the displayed §3b signature omits that keyword while its prose
   requires the comparison. The added keyword is a defensible implementation
   of the prose; confirm it rather than removing the check.
3. Batch archival is mandatory. Determine whether the already-signed v2
   archival sets/trailers are sufficient for implementation or whether a
   bounded correction must pin the final deterministic commit metadata.

## Verification repeated by Codex

```text
tests/test_officina_accounting.py + tests/test_officina_generic_harness.py:
152 passed

full pytest:
416 passed

verify_inheritance.py:
OK, 71 inherited files

verify_all.py:
OK

verify_officina_wp12.py:
OK, quarantined and inactive

verify_officina_active.py:
expected refusal: activation authorization absent

real python -m CLI refusal probe:
exit 2 (incorrect parsing; no artifact created)
```

T remains `NOT_ACTIVATED`; `runtime/` still contains only
`T_RUNTIME.lock`; the production call-graph manifest is absent. The four Cursor
implementation files remain uncommitted. Unrelated dirty files were not
modified.
