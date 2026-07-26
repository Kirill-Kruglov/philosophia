BLOCKED_OFFICINA_GENERIC_HARNESS_CONTRACT

# Officina generic-harness implementation — Y-line review

## Scope and outcome

The accounting amendment contains a useful pure post-cap primitive, and the
submitted tests are green. The four-file implementation is nevertheless not a
conforming implementation of the signed harness. Codex C1–C4 and M1–M6 are all
confirmed. In addition, the submitted batch constructor collapses multiple
streams into one stream per process, and the public batch authority can be
manufactured without a durable validated claim. Those are accounting and
admissibility defects, not stylistic omissions.

One repair cannot go directly to Cursor: §5 does not yet pin a mechanically
complete production supervisor/control-channel topology. Choosing how a
long-lived watchdog, the command-line invocations, confined temporary output,
and promotion communicate would create an unsigned control policy. A bounded
Fable contract closure must pin that one surface first. It need not choose a
learner, device, scientific endpoint, or outcome.

## Critical findings

### C1. The signed supervisor and isolation boundary is absent, and its production control surface is underspecified

At `src/philosophia/officina/generic_harness.py:407`,
`SubprocessProcessOps` can start a process, but no harness transition calls it.
`start()` (`:1265`) appends an event, installs a lease, and returns an in-memory
nominal capability without starting, owning, identifying, or watching the
claim's controller tree. There is no PID start-identity check, group/stream
reconciliation, deadline revocation, backend synchronization, or quiescence
proof.

`run_isolated_operation()` (`:2285`) invokes a caller-supplied Python callback
in the harness interpreter and returns its result hash before any settlement.
`promote_after_settlement()` (`:2297`) neither owns confined output nor proves
that the named charge belongs to the operation or even to the named process.
An old P1 heartbeat, or a P2 charge while P1 remains live, can release a P1
result. The committed positive test at
`tests/test_officina_generic_harness.py:1828` explicitly performs the heartbeat
*before* producing the result, then treats that unrelated earlier charge as the
operation's settlement.

This confirms Codex C1. The acceptance tests at `:1779–1845` use in-process
lambdas and exception stubs; they cannot detect shared mutable memory, inherited
descriptors, process-group escape, temporary-output visibility, backend queue
survival, watchdog death, or promotion before settlement.

The signed properties are clear, but a production implementation cannot be
derived without one further bounded cell: the persistent supervisor and its
control channel across separate `claim/start/heartbeat/close` CLI invocations.
The closure must pin:

- which process remains alive as supervisor/watchdog and its exact lifetime and
  restart disposition;
- the closed request/reply protocol and identity binding used by CLI,
  controller, worker, and supervisor;
- ownership and non-visibility of IPC descriptors, mutable memory, temporary
  output paths, and backend buffers;
- the exact operation-to-lease/meter/charge binding, atomic promotion point,
  one-use release delivery, and invalid-output disposal authority; and
- watchdog behavior when the CLI caller, supervisor, controller, worker, or
  backend disappears at each cut.

This is one engineering/control contract surface. It does not reopen a
scientific cell.

### C2. Ordinary execution can cross E1 without the required all-live batch, and numeric state can masquerade as a valid terminal

`heartbeat()` (`generic_harness.py:1314–1365`) always uses ordinary charging.
If the realized charge reaches or crosses E1 and `reservation_for()` returns
`None`, lines `1350–1351` manufacture a fresh full 60-second reservation. The
crossing process and every sibling lease therefore remain live; no frozen claim,
valid process records, lease removals, archive, or
`T_ENVELOPE_EXHAUSTED` event exists.

`derive_global_state()` (`:333–360`) then returns G7 from
`state.exhausted(envelope)` alone. Thus a numeric counter at the cap is enough
to narrate a valid global terminal without the signed event or process
terminals. The same defect can turn an invalid cap-consuming batch into G7
after its recovery dispositions are installed, even though the signed rule says
that later recovery cannot convert the invalid ending into valid exhaustion.

This confirms Codex C2 and is a validity-first blocker. The tests at
`tests/test_officina_generic_harness.py:1357` and `:1484` manually call the
batch API; they do not demonstrate that a real heartbeat/watchdog boundary
enters it.

### C3. The batch witness and authority do not preserve the signed stream-level accounting or durable provenance

The constructor at `generic_harness.py:1645–1716` emits exactly one stream per
process. For a lease with `device_units = k > 1`, a known coextensive interval
is charged once as `end - start`, not `k * (end - start)`. An unknowable
multi-stream process contributes one member to `m`, not one member per
unknowable stream. The API also accepts only `unknowable_process_ids`, so it
cannot express the signed mixed-known/unknown streams within one process.
Consequently `K`, `m`, `U`, shares, and process aggregates can all be wrong
while the generated claim validates against its own weakened shape.

The test named “multi-stream” at
`tests/test_officina_generic_harness.py:1318` starts four one-unit processes; it
never exercises one `k > 1` lease, mixed streams, or per-stream enumeration.

Separately, `BatchSettlementAuthority` has a public constructor and a public
`from_validated_claim()` that validates no claim
(`accounting.py:22–73`). The accounting tests manufacture every authority from
arbitrary hashes and tuples (`tests/test_officina_accounting.py:338–352`).
`execute_batch_step()` accepts a caller-provided mapping without proving that
the canonical claim file exists, matches that mapping, is unresolved, or was
fully validated at its pre-head. It then derives the authority from the same
mapping (`generic_harness.py:2243–2251`). An uninstalled fabricated claim can
therefore authorize the sole post-cap accounting path.

This rejects the required “cannot be forged, substituted, replayed, or advanced
against stale state/head” property despite the useful stale-state/head checks
inside `TState.charge_batch_settlement()`. The latter also needs an exact
`type(value) is int` check: `value=True` can compare equal to a claimed charge
of 1.

### C4. The batch registry, D1 cut, and archival terminal are not the signed state machine

The registry calls `validate_batch_claim()` without the pre-head state, durable
full lease snapshot, path/name identity, or recovery omission proofs
(`generic_harness.py:1199–1213`). For recovery claims, even the full validator
does not prove each `TERMINAL_RECORD_DURABLE` or
`ANCESTOR_CLAIM_ENUMERATED` omission against its referenced artifact. The test
at `tests/test_officina_generic_harness.py:1569` deliberately exploits this
weaker registry by installing a duplicate filename.

`next_batch_action()` returns `RESOLVED` immediately after runtime tuples and,
for E1, the exhaustion event (`generic_harness.py:1956–2009`).
`BatchAutomatonAction.ARCHIVE` is never returned or performed. This makes an
unarchived claim stop blocking admission, contrary to the signed
claim-resolution predicate. Ordinary close, review, and pause paths likewise
perform no required archival commit.

The D1 routine first invokes ordinary ledger and registry parsing
(`:1923–1952`). That parsing refuses the exact “ledger entry durable, external
head stale” cut before D1 can inspect it. The method repairs only the state
cache, has no old/new head-state authority binding, and does not itself perform
the mandatory immediate full-tree verification. Its docstring's claim that the
external head cannot lag contradicts the signed power-loss cut.

This confirms Codex C3 and C4. The crash tests at
`tests/test_officina_generic_harness.py:1445` inject only immediately before a
whole action; the D1 positive test at `:1516` makes the external head current
and only the cache stale. Neither covers the signed append-to-head crash or the
archival boundary.

## Major findings

### M1. G5 is not scoped to invalidities since the last admission

`_g5_admission_clear()` (`generic_harness.py:1543–1561`) rechecks every
historical invalidity and requires every old disposition to equal the *current*
head and state. A valid fresh `T_PROCESS_STARTED` advances the head, making the
old disposition stale; the next heartbeat is refused. The positive recovery
test at `tests/test_officina_generic_harness.py:1760` stops immediately after
the fresh start. Codex M1 is confirmed.

### M2. Ordinary crash recovery is observational, not implemented

A start event durable without its lease can be followed by another `start()`,
which appends a second start event rather than entering record-first
invalidity. A heartbeat charge durable with stale state/lease can be followed
by another heartbeat using the old cursor, duplicating the charged interval.
Tests at `:1238–1296` merely assert that the broken intermediate artifacts
exist; they do not invoke the required next-admission recovery.

`close()` also releases the runtime lock between reading its pre-close
claim/lease and performing the final heartbeat (`generic_harness.py:1380–1389`),
then reacquires it for the record/event/removal. That is not one signed
transaction epoch. Codex M2 is confirmed.

### M3. Process identity and global sequence are not durable invariants

`claim()` records the harness CLI's PID, uses `str(os.getpid())` as kernel start
identity, and uses its current process group without starting the claimed
controller (`generic_harness.py:1239–1257`). It computes the next sequence from
live leases only, so after a close the next claim can reuse sequence zero. A
same-input/same-clock claim may collide with the retained claim path; a changed
input may create a distinct process with a reused global sequence. No consumer
checks liveness, kernel start identity, group membership, immutable behavior
inputs, or declared streams. Codex M3 is confirmed.

### M4. Claim validation is internally consistent but not durably complete

In addition to C3/C4, `validate_batch_claim()` does not require the filename to
equal `pre_ledger_head_sha256`, does not verify `created_utc` against the
pre-head timestamp, does not bind `adapter_identity` to the admitted adapter,
and does not prove recovery omissions. Revalidation after lease removal cannot
simply omit all pre-head inputs; it needs a retained pre-head snapshot and
artifact ancestry proof. Codex M4 is confirmed.

### M5. The actual signed module invocation is unparsable

`main()` drops only one `/proc/self/cmdline` element
(`generic_harness.py:2336–2347`). Under
`python -m philosophia.officina.generic_harness …`, the next element is `-m`,
so the command exits 2. This was reproduced without creating an artifact. The
tests call `main(argv)` directly (`tests/test_officina_generic_harness.py:1985`)
and never exercise the module invocation. Codex M5 is confirmed.

### M6. Public reads and promotion are not lock-bound

`global_state()`, `process_state()`, and `promote_after_settlement()` read
ledger/state/leases and, in the last case, issue a release token without
`T_RUNTIME.lock` (`generic_harness.py:1160–1195`, `:2297–2319`). They can
observe mutually inconsistent generations or promote across an unrelated
concurrent transition. Codex M6 is confirmed.

### M7. Closed decision shape is present, but semantic authorization is not

The exact-key validators and recursive forbidden-field checks are useful and
cover their nested mappings. However, `complete_overdue_review()` overwrites
many caller fields after initially validating a caller-supplied facade and
never proves the authorization, activation, or author-decision hashes against
durable governing artifacts (`generic_harness.py:1495–1539`).
`install_recovery_disposition()` likewise accepts an arbitrary syntactically
valid `author_decision_sha256` without verifying a tracked signed decision
(`:1563–1605`). Closed schemas are not sufficient if the load-bearing parents
are unverified.

## Minor findings

1. The recursive `reject_scientific_fields` call in `_exact()` correctly
   reaches inline meter evidence, claim omissions, decisions, checkpoints, and
   overrides. This accepted surface must be retained while semantic parent
   validation is added.
2. Ordinary `charge_device_nanoseconds` is textually unchanged. The new
   caller-supplied `current_ledger_head_sha256` keyword is not a defect; it is
   required to realize the signed prose's stale-head comparison in a pure
   accounting method.
3. `verify_conservation_at_rest()` checks only ledger charge sum and current
   lease liability. It is not a substitute for process-record conservation,
   full batch witness validation, archival resolution, or event-backed global
   state.

## Required reachable traces

| Trace | Signed route | Reachable implementation route |
|---|---|---|
| 1a. One heartbeat crosses E1 | Freeze all live leases; full charge; valid E1 record → stopped → removal; one exhaustion event; archive; G7 | Ordinary charge, fabricated 60-second successor lease, no terminal event/archive; `global_state()` reports G7 from the counter |
| 1b. Crossing with siblings | Same batch covers every live lease before G7 | Only the named lease is charged/renewed; every sibling survives |
| 2. E1+E3 / invalidity | Fault-free E1 dominates and retains E3; any invalidity routes only G5, with no valid event | Numeric E1 check dominates without proving an event; after disposition a cap-consuming invalid route can be narrated G7 |
| 3. Signed 60/60/60 recovery batch | Claim; three global-sequence invalid tuples `C-D-E-R-L`; no exhaustion; archive; G5 | Pure post-cap arithmetic works, but integration test changes the reason to all-valid E1, and both routes become `RESOLVED` before archive |
| 4. Every batch crash prefix | Exactly one action at each C/D/E/R or C/V/S/L/X/A cut; D1 covers the one authorized head/cache lag | Tests cut before whole actions; no A state exists; external-head-stale D1 is unreachable |
| 5. Recovery → fresh admission → heartbeat | Dispositions for invalidities since last admission; fresh id/sequence; later heartbeat admissible | Fresh start succeeds, advances head, then makes every historical disposition stale; heartbeat refuses |
| 6. Start durable, lease absent | Next admission detects the cut and records invalidity; no id/event reuse | A second `start()` can append another start event and install a lease |
| 7. Charge durable, cache/lease stale | Sole idempotent successor completion; no second charge | Next heartbeat reads the stale cursor/state and can charge the same interval again |
| 8. Closed process → new claim | Archive first; fresh process id and globally increasing sequence | No archive; sequence is recomputed from live leases and can be reused |
| 9. Result before settlement | Output remains inaccessible until its own post-operation settlement and atomic promotion | Result hash returns immediately; an earlier or other-process charge can authorize promotion |
| 10. Module CLI | `python -m … <signed command>` parses refusal-first | Actual invocation exits 2 because `-m` is treated as the command |

## Answers to the four questions

1. **Review-record heads:** yes. Binding both `ledger_entry_sha256` and
   `ledger_head_sha256` to the durable pre-review head is the forced
   non-circular interpretation: the review record is written before the
   `T_REVIEW_COMPLETED` event that hashes it, so it cannot contain that event's
   hash. Add an exact regression proving both fields equal the pre-review head
   and that the event immediately succeeds that head and binds the record hash.

2. **Caller-supplied current head:** yes. The displayed §3b signature omitted
   the keyword, but the accompanying normative prose requires comparison with
   the current durable head. A pure `TState` cannot read the ledger; an exact
   caller-supplied current-head value, re-derived under the held lock, is the
   necessary implementation of that requirement. It must not be accepted from
   an untrusted public caller or paired with a forgeable authority.

3. **Archival contract:** the signed exact staged sets, no-prior-index rule,
   set equality, fixed trailers, retained claim/override/tuple bytes, and
   existing Git ancestry are sufficient to define a deterministic archival
   validity predicate. No new scientific or author cell is needed merely for a
   commit subject. The implementation must add the `ARCHIVE` action, verify the
   exact commit boundary and trailers, and keep admission blocked on commit
   failure. It must not declare runtime completion to be archival completion.

4. **Supervisor/isolation:** no. Section 5's invariants do not determine a
   complete implementation across independent CLI processes. Selecting a
   foreground versus persistent supervisor, IPC/control transport, temporary
   output custody, watchdog survival/restart, and release delivery changes
   admissibility and result visibility. The smallest missing surface is the
   single bounded supervisor/control-channel and confined-promotion protocol
   described in C1. It requires a bounded Fable contract closure before Cursor
   can implement it.

## Mandatory repair order

### Before Cursor: bounded Fable contract closure

**R0.** Add only the §5 supervisor/control-channel and confined-promotion
surface specified in C1, including exact lifecycle/crash semantics and the
accepted production import/control boundary. Confirm that it adds no new entry
point, scientific field, device choice, or execution authority. Return for
bounded X/Y confirmation.

### After that closure: Cursor implementation repairs

1. Make the supervisor the actual owner of controller process, group, streams,
   watchdog, capability, meter adapter, confined output, and promotion.
2. Route every realized E1/E3/invalid boundary from heartbeat, close, watchdog,
   and recovery through the one all-live frozen batch; make global terminal
   states event/artifact-backed, not counter-only.
3. Enumerate every stream; compute coextensive known charge as
   `k * elapsed`; preserve per-stream mixed known/unknown classification and
   the one global pool.
4. Make authority issuance private and claim-backed. Every step must reload the
   canonical installed claim, path, hash, pre-head snapshot, full live set or
   proved recovery omissions, exact prefix, current head, and current state.
   Reject booleans and subclasses for integer inputs.
5. Implement every canonical batch action including `ARCHIVE`; implement D1
   from a raw, statically parsed ledger suffix when the external head is stale,
   with exact old/new bindings and immediate full verification.
6. Scope G5 to the invalidity epoch since the most recent valid admission and
   verify each disposition's durable author parent; never derive a valid
   terminal from an invalid numeric state.
7. Implement each ordinary crash-cut continuation, retain one lock epoch across
   close, and prevent duplicate start/charge/id/sequence use.
8. Derive PID start identity, group membership, streams, and the next global
   sequence from the complete durable history, not live leases.
9. Put all public reads, capability use/issue/revoke, settlement, and promotion
   under the runtime lock and generation checks.
10. Parse the actual `python -m` invocation and verify the real CLI without
    creating production artifacts.

## Required new tests

- one- and multi-lease heartbeat/watchdog crossings that automatically enter
  the batch and prove all records/removals/event/archive;
- simultaneous E1/E3 and cap-consuming invalidity before and after recovery,
  proving no process-to-valid-terminal conversion;
- one `device_units > 1` known lease, one multi-unknowable lease, and one mixed
  known/unknown lease, with exact `K/m/U/share` recomputation;
- construction attempts using a public/manual authority, an uninstalled or
  substituted claim, `value=True`, stale head/state, duplicate/reordered entry,
  and a forged recovery omission;
- every *after-durable-substep* valid and invalid batch cut, including raw
  ledger/external-head lag and archive failure;
- start-event/lease cut followed by next admission; charge/state/lease cut
  followed by next heartbeat; both must recover or invalidate without replay;
- recovery disposition → fresh start → heartbeat/close, plus a second
  invalidity epoch;
- close/archive → new claim proving monotonically increasing global sequence
  and non-reused identity;
- operation result held in an isolated process until its own charge, with old
  and other-process charges rejected; process/group/FD/path/backend escape
  matrix and watchdog death at every cut;
- actual `python -m philosophia.officina.generic_harness` parsing;
- lock-race tests for global/process reads and promotion;
- review/recovery parent-hash verification and the pre-review-head
  non-circular regression; and
- acceptance-matrix tests that replace in-process lambdas with a real confined
  disposable supervisor/worker topology.

## Checks run and negative space

Executed read-only/disposable checks:

```text
tests/test_officina_accounting.py + tests/test_officina_generic_harness.py:
152 passed

full pytest:
416 passed

scripts/verify_inheritance.py:
OK — 71 inherited files

scripts/verify_all.py:
OK

scripts/verify_officina_wp12.py:
OK — quarantined and inactive

scripts/verify_officina_active.py:
expected refusal — production activation authorization absent

actual python -m CLI probe:
exit 2 — parsing defect reproduced

git diff --check for the four implementation files:
clean
```

The current HEAD differs from anchor `2af5720` only by review/prompt material;
the four audited implementation/test changes remain uncommitted. The production
call-graph manifest is absent. The real runtime still contains only
`T_RUNTIME.lock`; T remains `NOT_ACTIVATED`.

This review creates only this review file. It authorizes no implementation,
production manifest, activation, capability, process, world, learner, entropy,
E1/E2/E3 spend, candidate, Q/C object, datum, outcome, or scientific
interpretation. Every unrelated dirty file remains untouched.
