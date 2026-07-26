# Opus X-line review: Officina generic harness implementation

Date: 2026-07-27
Reviewer line: X (adversarial implementability / control-path)
Base HEAD: `2af5720` (uncommitted Cursor work audited in-tree)

## VERDICT

```text
REVISE_OFFICINA_GENERIC_HARNESS_IMPLEMENTATION
```

One load-bearing surface additionally carries a `BLOCKED_CONTRACT`
sub-finding (the persistent watchdog/supervision topology and the
confined worker→supervisor result channel, §5a/§5b under §9): that part
must **wait** for a bounded contract correction, not be designed inline
by Cursor. Everything else is a Cursor-repairable implementation defect
against already-signed text.

The four files are **not** eligible to commit.

## What was verified independently (not inferred from green tests)

- Governing contract hashes recomputed and matched the signature
  (`OFFICINA_GENERIC_HARNESS_SIGNATURE.md` §Governing hashes): v2 draft
  `64b8d3f6…`, v2.3.1 `724d633a…`, amendment v1.1.1 `b5a15232…` all
  equal. I audited the signed composite text, not a paraphrase.
- Suites run green: `tests/test_officina_generic_harness.py`
  + `tests/test_officina_accounting.py` = **152 passed** (Codex's 416
  full-suite figure not re-run here; not load-bearing for this verdict).
- Live reproductions (all in disposable `/tmp` dirs; no repo state
  touched): the D1 ledger-ahead-of-head cut (C4), the real
  `python -m` entry point (M5), and the post-recovery G5 re-block (M1).
- `runtime/` still contains only `T_RUNTIME.lock`; `T_ENVELOPE.json`
  has `"activated": false`; the working tree's unrelated dirty files
  are unmodified.

## Independent adjudication of Codex C1–C4 / M1–M6

### C1 — Supervisor, watchdog, isolation boundary absent — **CONFIRMED (Critical)**

Trace of the actual production path proves no controller/worker process
is ever started or owned:

- `SubprocessProcessOps` is assigned at `generic_harness.py:1089` and
  **read nowhere else** (`grep 'self.processes'` yields the one
  assignment). It spawns nothing.
- `start()` (`generic_harness.py:1265-1312`) appends `T_PROCESS_STARTED`
  and writes the lease, but never spawns a process, never checks PID
  start-identity, never reconciles group membership, and installs no
  watchdog — contradicting §1 ("supervisor … performs every
  §3-template transaction"), §2c.4 (revalidate group membership,
  declared streams, control bytes), and §5a.
- `run_isolated_operation()` (`2285-2295`) runs the caller's
  `perform()` **in the harness interpreter** and returns
  `sha256_bytes(perform())` **before any settlement**. That shares all
  memory/FDs/temp paths with the caller (zero of §5b's confinement) and
  exposes the result hash pre-settlement, inverting §5b's mandated order
  ("capture the result hash → durably settle the charge → atomically
  promote → issue token").
- `promote_after_settlement()` (`2297-2319`) only checks a live lease
  plus a durable charge event and mints a token; it does **not** revoke,
  quiesce, synchronize, atomically promote confined output, and does not
  bind the token to the operation actually isolated (`result_sha256`,
  `operation_id` are caller-supplied, unbound to any confined execution).
- The tests confirm the facade: `test_officina_generic_harness.py`
  §10.25 drives isolation with in-process lambdas and
  `raise subprocess.SubprocessError(...)` stubs (`~1799-1845`); a
  "killed child" is a raised exception, not a killed OS child, so shared
  memory / inherited FDs / escaped groups / output visibility / a missing
  watchdog are structurally undetectable.

### C2 — E1/E3 boundary not connected to ordinary execution — **CONFIRMED (Critical)**

`heartbeat()` (`1314-1365`) charges via the ordinary path
(`charge_device_nanoseconds`, `1333`) and then, at
`1347-1351`, when `reservation_for(...)` returns `None` (the exact
budget-exhaustion / boundary signal of §4b), **fabricates a fresh
60-second `Reservation`** and renews the lease at `1363`. Consequences,
traced through all siblings:

- **E3-due crossing:** `charge_device_nanoseconds` does not refuse on
  E3 (E3 is a separate clock), so the fabricated reservation renews a
  behavior-capable lease *past E3-due* with a full 60 s liability — no
  batch settle, no revoke, no G2 handling. §2c.9/§4d require the E3
  boundary batch instead.
- **E1 headroom short of a full reservation:** the fabricated 60 s
  liability can exceed remaining E1, over-reserving past the cap
  (§4b forbids: reservation ≤ available budget; `ℓ=0` from budget must
  **refuse**, not renew).
- The signed boundary batch (§4d / v2.1 §A/§B) is exposed only as a
  separate manual API (`construct_and_install_batch_claim` …
  `run_batch_to_completion`); **no** heartbeat/close/watchdog path
  invokes it at a crossing. So an ordinary heartbeat can leave renewed,
  behavior-capable work live after the boundary without
  `T_ENVELOPE_EXHAUSTED`/E3-due settlement.

### C3 — Batch archival skipped; unarchived claim becomes "resolved" — **CONFIRMED (Critical)**

- `next_batch_action()` (`1956-2009`) returns `RESOLVED` immediately
  after the runtime suffix (and `X` for all-valid `E1_BOUNDARY`); it
  **never returns `ARCHIVE`**. `_perform_batch_action` has no `ARCHIVE`
  arm (falls through to "no batch action is pending"). The enum member
  `BatchAutomatonAction.ARCHIVE` (`171`) is dead (only referenced in an
  `install_batch_override` guard, `1885`).
- `_unresolved_batch_claims()` (`1199-1213`) deems a claim resolved when
  `next_batch_action` is `RESOLVED` — i.e., **before any archival commit
  exists**. This violates amendment §3a resolution predicate (all of:
  complete automaton **and** the archival commit exists) and the §4b
  prefix row "all tuples complete (+ X); archival absent → **archive** …
  capability blocked until done". The registry therefore stops blocking
  (`_refuse_if_unresolved_batch`) one whole boundary early, admitting new
  claims/leases/capability while the batch is unarchived — the §3a
  blocking rule forbids exactly this.

### C4 — Signed D1 ledger-head recovery unreachable — **CONFIRMED (Critical)**

Reproduced on disposable files: after appending an entry's bytes+fsync
but before the head is atomically replaced (`ledger.py:223` vs `225` are
**not** atomic), the head lags the ledger. Then **both**
`AppendOnlyLedger.entries()` and `.append()` call `_verify_head`
(`174-177`, `208`) and raise `LedgerIntegrityError: ledger external head
mismatch`.

```text
HEAD entry_count: 1   LEDGER lines: 2 (post-crash)
entries() RAISED: ledger external head mismatch
append()  RAISED: ledger external head mismatch
```

`complete_batch_head_cache_if_authorized()` (`1923-1952`) calls
`self._ledger().entries()` at `1938` **before** any repair, so in the
ledger-ahead-of-head state it raises before reaching completion logic.
Its docstring's claim that "ledger.py binds a ledger entry and its
external head atomically … the external head can never independently
lag" is **false**: the head is a separate `atomic_replace` after the
ledger fsync. The method completes only the state-cache lag, never the
head lag, so amendment §D1 precondition-2 ("the external head **and/or**
state cache lag it") and §4c ("Inside [a batch] … §4d applies") are
unimplemented for the head case. The v2 §3 crash row "after 4, before 5
| ledger ahead of head" is a real, reachable cut. The positive D1 test
(§10.22) writes via the raw `append` (which keeps the head consistent),
so it only ever exercises a state-cache lag — the head-lag case is
untested.

### M1 — G5 recovery evaluated against all history, not "since last admission" — **CONFIRMED (Major)**

`_g5_admission_clear()` (`1543-1561`) iterates **every**
`T_RUNTIME_INVALID` event and requires each disposition's
`ledger_head_sha256`/`state_sha256` to equal the **current** head/state.
Reproduced end-to-end:

```text
after disposition, phase: G1
fresh start succeeded
phase AFTER fresh start:  G5      ← regression
next heartbeat REFUSED -> "G5 runtime invalidity blocks admission …"
```

The first post-recovery `T_PROCESS_STARTED` advances the head, so the
disposition (bound to the recovery-time head/state) no longer matches
and G5 re-blocks; recovery admits exactly one claim/start and then
freezes forever. v2.1 §C.3 scopes the predicate to invalidity events
"**since the last admission**" and states readmission needs no event
("the next `T_PROCESS_STARTED` is the first post-recovery entry").
Test §10.24 stops immediately after the fresh start and misses it.

### M2 — Ordinary crash-cut recovery incomplete; close breaks the lock epoch — **CONFIRMED (Major)**

- `close()` (`1367-1423`) takes the lock **three** times: read block
  (`1380-1386`), then `self.heartbeat()` (its own lock, `1387`), then
  record/stop/remove block (`1389-1423`). The lock is released between
  the final settlement charge and the final process record / stop /
  removal — the §3 template mandates one lock epoch across
  read→append→cache/lease→post-verify. Any operation interleaving in
  those windows is admitted by construction (a batch could freeze the
  now-renewed lease; another admission could slip in).
- There is no admission-time routine implementing the v2 §3 crash table
  for ordinary transactions: start-event-without-lease (P2 with no
  lease → next-admission invalidity), orphan dependent artifact
  ("after 3, before 4"), ledger-ahead-of-head ("after 4, before 5"),
  or the §3a idempotent cache/lease-successor completion for
  non-batch epochs. Only the batch state-cache case is (partially)
  handled.

### M3 — Process identity and monotone sequence not enforced — **CONFIRMED (Major)**

`claim()` (`1245-1247`) records `controller_pid=os.getpid()`,
`controller_start_identity=str(os.getpid())`, `process_group_id=
os.getpgrp()` — the short-lived CLI's own PID, with start-identity
**equal to the PID string**, so §5a PID-reuse defeat ("start-identity
comparison at every admission and settlement") is a no-op. `sequence =
max(live-lease sequences) + 1` (`1239`) derives only from **currently
live** leases, so once every lease closes the sequence resets to 0 and a
closed sequence is reused — violating the amendment's global ascending
`process_sequence`. `start()`/`heartbeat()` verify no controller
liveness, kernel start-identity, group membership, declared streams, or
immutable behavior inputs.

### M4 — Batch registry revalidation weaker than the signed full validation — **CONFIRMED, narrowed (Major)**

`_unresolved_batch_claims()` (`1207`) calls `validate_batch_claim(...)`
with no `leases/state/ledger_head/pre_ledger_entry` (only internal
consistency, per that function's own contract at `617-632`). Creation
(`construct_and_install_batch_claim`, `1768-1770`) **does** enforce full
§1e/§1f completeness, so the gap is at *re-validation*, not creation.
Nuance: §3c restart reconstruction correctly forbids re-checking
pre-state against the mutated current state, and completeness against a
now-drained lease directory legitimately cannot re-run. But the scan
still admits a schema-self-consistent file into the registry without the
§1f duty-2 pre-anchor binding, and the test
`test_head_cache_completion_refuses_when_multiple_unresolved_claims_exist`
(§10.22) *relies on that weakness* to drop a hand-forged `duplicate.json`
claim. The registry should at minimum bind each retained claim's
`pre_ledger_entry/head` to the durable chain and re-prove its witness
integrity before treating it as an authority-bearing unresolved claim.

### M5 — Real module CLI does not parse its signed invocation — **CONFIRMED (Major)**

Reproduced: `OFFICINA_REPOSITORY=… python -m
philosophia.officina.generic_harness start <64 zeros>` → **exit 2**,
no artifact. `_argv()` (`2336-2338`) reads `/proc/self/cmdline`
(`['python3','-m','philosophia.officina.generic_harness','start',…]`)
and `main()` (`2344`) drops only element 0, so `arguments[0]` is `-m`
→ not a command → usage exit 2. The signed `__main__` entry point
(v2 §9) is entirely non-functional; every test calls `main(argv)`
directly and bypasses `_argv()`. (Note: the same defect makes even a
direct `python file.py …` invocation fail, since `[1:]` then starts at
the script path — but §9's entry point is `-m`, which is the governing
one.)

### M6 — Capability/promotion reads not lock-bound — **CONFIRMED for promotion (Major); read-views Minor**

`promote_after_settlement()` (`2297-2319`) reads activation, leases, and
the ledger and **issues a `ReleaseToken` with no `RuntimeLock`** — a
capability-adjacent issuance across an unprotected snapshot, contrary to
§1/§3a ("admission and capability issue/use … revalidate under the
global lock"). `global_state()` (`1160`) and `process_state()` (`1178`)
also read unlocked; these are read-only "at-rest" views (v2 §3a permits
the verifier to be authoritative only at rest), so they are the milder
half — but `global_state()` is invoked *inside* locked flows (e.g. end
of `resume`, `run_batch_to_completion`) where a consistent locked
snapshot is expected.

## Answers to the mandate's specific questions

1. **Does any production path start/own the controller, check
   start-identity/group, install a watchdog, revoke/quiesce/confine/
   settle, then promote?** No. `start()` writes durable artifacts and
   returns a capability without spawning/owning anything; the
   isolation-and-promotion methods are in-process facades (C1).
2. **Can `run_isolated_operation(lambda)` satisfy §5b, or is it
   necessarily a pre-settlement-exposing test facade?** Necessarily a
   facade: it executes `perform()` in the harness interpreter (no memory/
   FD/IPC/temp/buffer confinement) and returns the result hash
   **before** any settlement, inverting §5b's order. It cannot be a
   compliant §5b implementation.
3. **E1/E3 crossing from an ordinary heartbeat.** Traced: at a boundary
   `reservation_for` returns `None` and heartbeat fabricates a fresh
   60 s `Reservation` (`1351`) and renews the lease — leaving
   behavior-capable work live after E3-due (and potentially
   over-reserving past E1) with no boundary batch (C2).
4. **Batch automaton incl. archival; is `RESOLVED` reachable before
   the Git boundary?** Yes — `next_batch_action` returns `RESOLVED`
   after the runtime suffix with no `ARCHIVE` step, and the registry
   stops blocking there, before archival (C3). The already-signed sets
   (amendment §3a(2) as narrowed by §D2c: claim, override-if-any, tuple
   record/detail files, state, ledger, head — evidence artifacts
   deleted) **and** trailers (activation protocol §B, the three fixed
   `Co-Authored-By` lines) **are sufficient** to implement archival.
5. **D1 ledger-ahead-of-head cut (disposable repro).** Reproduced;
   normal parsing (`entries()`/`append()` → `_verify_head`) refuses on
   head mismatch, so the authorized §D1 head completion is unreachable
   (C4).
6. **Recovery → fresh start → heartbeat; "since last admission".**
   Reproduced; the scope is missing — the next heartbeat re-blocks on
   G5 (M1).
7. **Real `python -m …` entry point.** Exercised → exit 2, no artifact
   (M5).
8. **Signed transaction cuts.** Orphan dependent artifact and
   start-event-without-lease: no next-admission handling (M2). Ledger/
   head lag: unreachable/refused (C4). Cache/lease lag: only the batch
   state-cache arm exists; the ordinary §3a completion is absent (M2).
   Close interleaving: present, three lock epochs (M2).
9. **Full-live-set revalidation / sequence non-reuse / lock ownership /
   capability binding.** Full revalidation weakened at scan (M4);
   sequence reuse possible (M3); promotion issued unlocked (M6);
   capability unbound to any confined operation (C1).
10. **Are the missing supervisor/IPC/output-confinement mechanics fully
    determined?** Mostly yes — worker spawn (`subprocess`,
    `start_new_session=True`), identity (PID + kernel start-identity +
    boot, fields already in `runtime.py`), group control (`os.killpg`),
    the promotion **order** and the six token-binding fields, and the
    missed-deadline fallback (§4c recovery charge at next admission) are
    all pinned by §5a/§5b/§9. **BLOCKED_CONTRACT** applies to one
    narrow sub-surface only (see below): the persistent watchdog /
    supervision **topology** under the discrete-CLI + no-thread /
    no-signal / no-multiprocessing model, and the exact confined
    worker→supervisor **result-return channel**. Two compliant
    implementations could differ materially here (a self-watchdogging
    spawned worker vs. lazy §4c next-invocation deadline detection have
    different between-invocation safety), so it must not be chosen
    inline.

## Three Codex clarifications

1. **Is pre-review head the forced meaning of the review record's
   `ledger_entry_sha256`/`ledger_head_sha256`?** For
   `ledger_head_sha256`: yes — a post-review head is impossible without
   a hash cycle (the `T_REVIEW_COMPLETED` event carries the record's
   hash), so the pre-review head is forced, and Cursor's binding at
   `complete_overdue_review` (`1512-1517`) is correct. For
   `ledger_entry_sha256`: **not fully pinned.** The activation-protocol
   review-record schema (V2 §… keys at lines 262-267) lists two head
   fields but states no rule distinguishing them; binding both to the
   pre-review head is the only acyclic, deterministic reading and is
   consistent with the activation-record precedent, so it is acceptable
   — but the two-field redundancy is unexplained. Confirm the reading
   and **add a regression test asserting acyclicity + equality**; if a
   distinct meaning for `ledger_entry_sha256` was ever intended, that is
   a one-line contract note, not a blocker.
2. **Is the extra `current_ledger_head_sha256` keyword in
   `charge_batch_settlement` faithful?** Yes — **confirm, do not
   remove.** §3b prose requires "the caller-supplied current durable
   ledger-head hash equals `expected_ledger_head_sha256`"; the displayed
   signature omits the keyword but the comparison is mandatory. The
   implementation (`accounting.py`) checks both the head equality and
   `hash_mapping(self.to_mapping()) == expected_state_sha256`, exactly
   the two §3b stale refusals. The successor authority keeps the old
   head expectation, which is safe only because the harness reconstructs
   authority per step (`reconstruct_batch_authority`); direct chaining
   would refuse on the advanced head, as intended.
3. **Does archival need a contract correction or only implementation?**
   **Implementation only.** The staged set (amendment §3a(2) narrowed by
   §D2c) and the fixed trailers (activation protocol §B) are already
   signed; the per-boundary commit *subject* is unpinned uniformly
   across all archival boundaries, so it is existing latitude, not a
   missing rule. No correction is required to implement `ARCHIVE`.

## Findings by severity

**Critical (block commit; must be repaired):**
C1 supervisor/watchdog/isolation-and-promotion absent;
C2 boundary batch not wired into heartbeat/close/watchdog;
C3 archival step missing → premature `RESOLVED`/unblocking;
C4 §D1 head-lag completion unreachable (and a false docstring).

**Major:** M1 G5 "since last admission" scope; M2 ordinary crash-cut
recovery + close lock-epoch split; M3 identity/start-identity/sequence
non-reuse; M4 registry re-validation weaker than §1f; M5 `__main__`
argv; M6 unlocked promotion token issuance.

**Minor:** unlocked `global_state`/`process_state` read-views used
inside locked flows; dead `BatchAutomatonAction.ARCHIVE` reference in
`install_batch_override`; review-record two-field redundancy (clarify).

## Mandatory repairs and their gating

**Repairable immediately by Cursor against signed text** (no correction):
C2, C3, C4, M1, M2, M3, M4, M5, M6, and the *determined* portion of C1
(real `subprocess` worker with `start_new_session`, PID + kernel
start-identity + boot checks at every admission/settlement, `killpg`
group control, the §5b promotion order with the six-field one-use token
bound to the actually-isolated operation, output confined to a
supervisor-private path/FD, and missed-deadline settlement via §4c at
next admission).

**Must wait for a bounded contract correction (`BLOCKED_CONTRACT`
sub-surface):** the persistent watchdog / supervision **topology** and
the confined worker→supervisor **result channel** under §9's discrete
CLI + no-thread/no-signal/no-multiprocessing constraints. Smallest
bounded correction: pin (a) which process holds the deadline and
capability between CLI invocations and whether §5a "at or before the
deadline" is satisfied by lazy §4c next-admission detection or requires
a live self-watchdogging spawned supervisor; and (b) the exact confined
channel by which the worker's result hash reaches the supervisor without
controller visibility (e.g. a supervisor-owned `O_CLOEXEC` pipe or a
supervisor-private temp path), enough that the §10 "pipe/socket
inheritance" and "killed supervisor/controller/child" probes have a
single determined meaning. Cursor must route this back as a contract
question, per v2 §11 — not decide it inline.

## Tests that must be added (current matrix is green-but-incomplete)

- **Real-process isolation:** a spawned worker whose in-process mutation
  does **not** reach the controller; inherited-FD/pipe/socket escape
  refused; killed supervisor/controller/child exposes no result; escaped
  group terminated; crash before/after **each** promotion cut → no
  result exposed. (Current §10.25 uses in-process lambdas — replace.)
- **Boundary from ordinary execution:** a heartbeat that reaches E1 and
  one that reaches E3-due must enter the signed batch (settle all
  siblings; `T_ENVELOPE_EXHAUSTED`→G7 / G2), **not** fabricate a fresh
  reservation; assert no renewed lease survives the boundary.
- **Archival:** `next_batch_action` returns `ARCHIVE` (not `RESOLVED`)
  until the staged commit exists; the registry keeps blocking until then;
  crash injected at the archival substep resumes to `ARCHIVE`.
- **D1 head lag:** a genuine ledger-ahead-of-head crash (head file reset
  after a raw append) → §D1 completes the head under the six
  preconditions; a non-conforming suffix → record-first invalidity.
- **Recovery continuity (M1):** recovery → fresh start → **heartbeat →
  charge → close**, all admitted; a *new* post-admission invalidity still
  blocks (proves "since last admission" scoping, not "forever").
- **Close atomicity (M2):** the final charge and final record/stop occur
  in one lock epoch; no interleaving admission between them.
- **Identity/sequence (M3):** reused kernel PID with a different
  start-identity refused; `process_sequence` strictly increases across a
  fully-closed generation (no reuse).
- **Real CLI (M5):** `python -m philosophia.officina.generic_harness`
  drives claim/start/heartbeat/close/pause/resume (not `main(argv)`).
- **Locked promotion (M6):** token issuance under the lock; a concurrent
  state change between snapshot and issue is refused.

## Commit eligibility

**None of the four files may be committed.**
`generic_harness.py` carries four Criticals. `test_officina_generic_
harness.py` is green but encodes the facades (it would lock in the wrong
behavior) and lacks the rows above. `accounting.py`
(`BatchSettlementAuthority` + `charge_batch_settlement`) is faithful to
§3b and clean in isolation, but it is on the immutable-control allowlist
and, per the signature, is "eligible only after final X/Y confirmation
and the amendment token" — this X/Y review returns REVISE, and the
authority type has no correct consumer until the harness is fixed, so it
cannot land alone. `test_officina_accounting.py` rides with it.

## Custody confirmation

No activation, entropy, spend, real process, production call-graph
manifest, capability, world, learner, lease, claim, override, or
scientific outcome was created. T remains `NOT_ACTIVATED`
(`T_ENVELOPE.json: "activated": false`); `runtime/` still contains only
`T_RUNTIME.lock`. All checks ran in disposable `/tmp` directories; the
`python -m` probe used `OFFICINA_REPOSITORY=/tmp` and refused (exit 2)
without writing. Only this one review file is added; every unrelated
dirty and untracked file (including the concurrent `sol_*` review files)
is preserved unmodified. No implementation, contract, test, signature,
or runtime artifact was edited; nothing was committed.
