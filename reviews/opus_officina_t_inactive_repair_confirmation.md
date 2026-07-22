# Opus 4.8 X-line — Officina T inactive repair confirmation

**`OFFICINA_T_INACTIVE_REPAIR_CONFIRMED`**

Reviewer: Opus 4.8 (X-line, adversarial transaction/runtime). Repository:
`/home/master/llm_projects/philosophia`. Bounded diff reviewed:
`77c5a63..82e265e` (HEAD `ed5201b8` differs from `82e265e` only by review-prompt
files). **I edited nothing, committed nothing, activated nothing, implemented no
generic harness, created no manifest, authorization, real world, process, lease,
candidate, entropy, Q/C object, datum, or outcome, and spent no E1/E2/E3.
Positive activation/runtime constructor probes ran only as read-only,
in-memory, non-production values; no disposable mirror was mutated for this
confirmation.** The real tree is pristine after every check:
`T_ENVELOPE.json activated:false`, `runtime/` contains only the reviewed
immutable lock (`T_RUNTIME.lock`), and there is **no** `generic_harness.py`, no
`runtime_control/PRODUCTION_CALL_GRAPH.json`, no `runtime_control/` directory, no
`OFFICINA_T_ACTIVATION_AUTHORIZATION.json`, and no claim/record/lease/state/
process artifact. `git diff --check` clean; HEAD unchanged at `ed5201b8`.

The diff touches exactly `src/philosophia/officina/{accounting,activation,
checkpoint,runtime,verification}.py`, `successor/officina/
T_ACTIVATION_IMPLEMENTATION.md`, and the review/prompt files — no scientific
cell, envelope numeric, phase boundary, signed frame, or governing/protocol pin
is changed. The repair closes Sol's R1–R7 (and minors 8–9) and my T-m1/T-m2
one-to-one, transactionally and within scope, while keeping the package genuinely
**inactive** and fail-closed.

---

## Reconciliation of Sol R1–R7 and my T-m1/T-m2

**R1 — global four-stream boundary (CLOSED; also my §5 concern).**
`reservation_for` now consumes `live_reservations: Iterable[Reservation]`, a
closed typed object with `__post_init__` bounds (`1 ≤ units ≤ 4`,
`0 < liability_ns_per_unit ≤ 60·10⁹`). Concurrency is checked on
`sum(units)`, not record count, and aggregate liability is re-derived from the
typed fields. Independently reproduced Sol's probe: one live
`Reservation(units=2,…)` plus `requested_units=3` now **refuses**
(`RuntimeContractError`, 2+3 > 4); bare-int and `bool`-unit inputs are rejected
by the exact-type guard; the `__post_init__` boundary rejects
`units∈{0,5}` and `liability∉(0,60s]`. The five-stream-below-240s leak is gone.
No signed constant moved (cap 4, 60 s, 168 h, 40 h intact).

**R2 — activation provenance closure (CLOSED).** `validate_authorization` now
pins the **exact six governing paths + hashes** and the **exact five-item
protocol chain + hashes** (`GOVERNING_SHA256`/`PROTOCOL_SHA256`, set- and
byte-equality), and the exact `ENVELOPE_TOKEN`/`DEVICE_POLICY_TOKEN` (no longer
arbitrary nonempty strings). `_preflight_git` now requires the authorization's
introducing commit to equal current `HEAD`, and requires **every** reviewed,
governing, and protocol path to be a tracked, regular, non-symlink, single-link
(`st_nlink == 1`) file resolving inside the repo and present at the reviewed
commit — so Sol's untracked `external_behavior.py` and post-authorization
non-HEAD commit are both refused. The reviewed generic harness **and** the
production manifest are added to `REQUIRED_IMMUTABLE_CONTROL_PATHS`, and the
activation record's immutable-control map plus each process claim's map are bound
to that complete set (`validate_process_claim_against_activation`). No unreviewed
or path-aliased byte can reach activation.

**R3 — active verifier fail-open and evolving-ledger incompatibility (CLOSED;
also my T-m2).** The active envelope is now checked by **full canonical equality**
to the signed resource contract (`device_hour_cap:168`, caps, schema,
`scientific_outcome:false`, …), so Sol's `168→999` self-rehash is rejected.
Authorization/claim/record/entry/state/immutable cross-links are re-derived
(`expected_claim_links`, record⇄claim field identity, initial-T-state anchor).
The activation record's ledger head is treated as a **historical one-entry chain
anchor** (`entry_count:1` head over `entries[0].entry_sha256`) rather than
compared to the mutable current head file (that stale `pairs` entry was removed),
so a valid ledger may evolve without rewriting the immutable record while
`AppendOnlyLedger` + the first-entry `T_ACTIVATED` anchor prove descent.
`_active_cleanliness_failures` adds the separate active-runtime rule: a dirty
worktree is permitted **only** for ledger/head/state plus verified open-lease and
its byte-exact durable claim, everything else refused; a `git diff --quiet HEAD`
over the immutable tracked set and an exact commit path-set/trailer check guard
the committed boundary. No fail-open reproduced.

**R4 — E2 mechanically unavailable pre-WP-6 (CLOSED).** `TState.register_candidate`
now **raises `PermissionError`** ("requires the absent signed WP-6 registry
authority"); reproduced — `register_candidate("a"*64, …)` refuses. The active
verifier additionally fails on any `state.candidate_ids`, so no state or ledger
transition in this package can add a candidate or route E2 to an exhaustion
event.

**R5 — claim/lease/reservation/final-record linkage (CLOSED).**
`validate_active_lease` now enforces `outstanding_liability_ns == device_units ·
(heartbeat_deadline_ns − last_charged_reading_ns)`;
`validate_active_lease_against_claim` requires the lease's embedded projection to
be **byte-exact** to the durable claim; `build_process_record` no longer accepts
caller-asserted hashes — it validates the final settlement **event** (must be
`T_DEVICE_TIME_CHARGED`/`T_RUNTIME_INVALID`), binds it to the lease hash,
process id, and `final_state`, **recomputes** claim/charge/state hashes, and
enforces `closed ≥ started`. Sol's `controller_pid 100→999`-yet-VALID record is
therefore impossible.

**R6 — validity-first ledger contract and record-first invalidity event
(CLOSED).** New `validate_ledger_event` is a closed **nine-event payload
validator**: exact per-event `data` key sets, `scientific_outcome:false`,
recomputed entry hash, timestamp parse, recursive scientific-field rejection, a
full `TState.from_mapping` on every state-bearing event, and an explicit ban on
`t_state` in `T_PROCESS_STARTED` — independently confirmed
(`T_PROCESS_STARTED`+`t_state` refused; a tenth event refused). `reject_scientific_
fields` now matches **case-insensitively** and adds `pass/fail/insufficient/
equivalence/boundary` (confirmed: `Loss`, `PASS`, `equivalence`, `boundary`,
`C3`, and a nested `fail` all rejected; benign keys pass). The activation failure
handler now performs the record-first, hash-bound `T_RUNTIME_INVALID` **event**
under the lock **once `T_ACTIVATED` exists**, while a pre-anchor failure still
leaves only the standalone invalidity record — preserving v1's distinct
fail-closed pre-anchor treatment.

**R7 — production/test boundary is now honestly scoped (CLOSED).**
`verify_production_boundary` computes the reviewed Python **import-edge closure**,
fails on omitted local dependencies, rejects dynamic-resolution and entropy calls
(`getattr`/`eval`/`exec`/`import`/RNG) via `_resolved_symbol`, and requires the
canonical `PRODUCTION_CALL_GRAPH.json` manifest (schema, `roots`,
`reachable_sources`, `import_edges`) to equal the computed closure — so the
reflective `getattr(w,"evaluate_"+"test_query")` false-negative is caught and
omitted transitive code is rejected. The implementation doc is downgraded from
"static boundary that rejects test-world symbols" to a **direct-symbol lint**,
with the full functional E1 boundary explicitly deferred to the reviewed generic
harness. Because that manifest and harness are **absent**, the active path
requiring them cannot certify — consistent with the still-inactive tree.

**T-m1 — reservation terminal routing (CLOSED).** New `reservation_route`
returns `RESERVE | E1_EXHAUSTED | E3_DUE` and encodes §4 precedence exactly:
`e1_remaining ≤ 0 → E1_EXHAUSTED` is tested **before** `e3_remaining ≤ 0 →
E3_DUE`, so simultaneous zero records **exhaustion first** with E3 preserved.
Reproduced all four routes (E1-exhausted, E3-due, both-zero→`E1_EXHAUSTED`,
normal→`RESERVE`); no signed constant changed.

**T-m2 — lock scope (CLOSED without deadlock).** The pre-commit re-derive,
`_commit_activation`, and post-commit verify now run **inside** the `with
RuntimeLock` block (`return committed` at the with-body tail), and
`verify_active_repository(…, runtime_lock_held=True)` skips re-acquiring the lock
on that internal path. The external `verify_officina_active.py` calls with the
default `runtime_lock_held=False`, so external verification still runs
`verify_runtime_lock` — no fail-open. The `except BaseException` is on the outer
`try`, **outside** the `with`, so an in-block failure releases the flock via
`__exit__` before `_record_activation_invalidity` acquires its own lock — no
self-deadlock on the non-reentrant `flock`.

**Minors 8/9 — CLOSED.** `validate_process_record` now type/range-checks
`process_sequence`, `device_units`, `device_identity`, and parses/orders
`started_utc`/`closed_utc` (bool-as-int excluded via `type(x) is int`). The doc
distinguishes implemented pure constructors/validators from the absent runtime
transactions (process start, lease install, heartbeat/settlement, revocation,
reconciliation, exhaustion, review, pause/resume, stop, commit).

## Item-by-item audit (the seven points)

1. **Typed live reservations + `reservation_route`, signed constants intact —
   CONFIRMED.** Five-stream leak closed; E1-exhausted/E3-due/both-zero(exhaustion
   first)/RESERVE all reproduced; caps 4, 60 s, 168 h, 40 h unchanged.
2. **Provenance: hardcoded governing/protocol hashes, exact tokens, authorization
   -at-HEAD, absent harness+manifest in the immutable set — CONFIRMED.** Untracked/
   aliased/non-HEAD/wrong-token/wrong-pin inputs are all refused; suites exercise
   the git preflight.
3. **Active re-derive verify: no fail-open, no false rejection of a valid evolving
   ledger — CONFIRMED.** Canonical envelope equality, cross-link re-derivation,
   historical one-entry head anchor, and the cleanliness rule together reject the
   self-rehash mutation and accept a growing valid chain.
4. **T-m2 lock scope closed without deadlock — CONFIRMED** (verify/commit/
   post-verify under the held lock; external verifier unaffected; failure path
   releases before re-locking).
5. **Byte-exact claim/lease linkage + nine-event payload validator — CONFIRMED.**
   Liability equation, byte-exact claim projection, settlement-event/state binding
   with recomputed hashes, and the closed per-event validator (TState parse,
   `T_PROCESS_STARTED` t_state ban, tenth-event refusal) all hold.
6. **Record-first post-anchor invalidity + distinct pre-anchor route — CONFIRMED.**
   `T_RUNTIME_INVALID` appended record-first under the lock only when `T_ACTIVATED`
   exists; pre-anchor failure leaves the standalone fail-closed record. E2 is
   mechanically unavailable (`register_candidate` raises; verifier bars
   `candidate_ids`).
7. **E2 unavailable + honestly-scoped production verifier, supervisor/backend
   deferred — CONFIRMED.** Import-edge closure + manifest requirement + reflection/
   entropy rejection; doc reworded to a direct-symbol lint; harness and manifest
   absent, so activation stays blocked.

## Checks run

- `pytest tests/test_officina_activation.py tests/test_officina_runtime.py
  tests/test_officina_accounting.py` → **38 passed**.
- full `pytest` → **260 passed** (was 251; +9 repair tests, no regression).
- `scripts/verify_officina_wp12.py` → **OK: quarantined and inactive**.
- `scripts/verify_officina_active.py` → **FAIL / exit 1** (absent authorization),
  the required refusal of the inactive tree.
- Read-only/in-memory probes independently reproduced: R1 five-stream refusal and
  typed-guard, `reservation_route` four-way precedence, `register_candidate`
  `PermissionError`, `validate_ledger_event` `T_PROCESS_STARTED`/tenth-event
  refusals, and case-insensitive scientific-field rejection.
- Post-check tree: `activated:false`, `runtime/` = `{T_RUNTIME.lock}`, no
  harness/manifest/authorization/claim/record/lease/state, HEAD `ed5201b8`
  unchanged, no source/`successor` working changes.

## Scope opened by this verdict

A positive verdict opens **only the next generic metered harness scope/design
gate** (protocol v2.1 §7) — the supervisor, whole-process-tree supervision,
per-stream admission and global reconciliation, watchdog deadline revocation,
CPU/off-CPU backend synchronization and positive quiescence proof, conservative
unknown-interval charge, oracle/update/checkpoint metering, the real
`PRODUCTION_CALL_GRAPH.json` manifest, and the test-surface call graphs — subject
to its **own** bounded X/Y review. It authorizes **no** implementation or
execution by implication, and **no** activation or science: no `generic_harness.py`,
no manifest, no authorization, no activation, no real world/process/lease/stream,
no candidate/registration, no entropy, no breathing check, no Q/C activity, no
E1/E2/E3 spend, and no claim movement. Activation additionally still requires the
reviewed-and-pinned harness, an exact author-signed authorization committed at
HEAD, and Kirill's explicit `I_AUTHORIZE_OFFICINA_T_ACTIVATION`, before the driver
runs exactly once.

## Negative space

The predecessor line remains immutable, `OPEN`, and `BLOCKED_LEVEL1_FEASIBILITY`;
its records are non-citable and chose no value here. Officina's T and Q are
permanently non-citable for C1–C6; activation, leases, streams, tuning
observations, breathing checks, draft manifests, E3 reviews, non-finiteness, and
every T ending are non-scientific and move no claim; a future Q pass is a
spendability-gate fact only; S is unavailable; only a valid, independently locked
C execution may ever move an Officina claim, within its selection-conditional,
selected-frame, orientation, device, and learner-seed scope. Censored/`UNKNOWN`/
every invalid state is never success, equivalence, a boundary, or learner
impossibility. `PROOF_CORE`/`PROOF_STRONG` remain earned by nothing; the
programme claim stays `OPEN`.

I edited no existing file, created exactly one new file (this review), authorized
nothing, activated no T state, implemented no harness, created no manifest, and
committed nothing. `essay/OUTLINE.md` untouched. My actions were reading the
bounded diff, the Sol R1–R7 review, and the governing/protocol chain, and running
the read-only probes, suites, verifiers, and pristine-tree checks above. The real
repository remains `NOT_ACTIVATED`.

— Opus 4.8, X-line. No outcome is asserted or predicted in this document.
