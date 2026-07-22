# Officina generic metered harness contract — v2 draft (complete replacement)

Status: `CANDIDATE_FOR_XY_CONFIRMATION_NOT_AUTHORIZED`. This document
wholly replaces the v1 draft
(`successor/OFFICINA_GENERIC_HARNESS_CONTRACT_V1_DRAFT.md`, preserved
unedited as review evidence) after the convergent X-line
(`REVISE…_XLINE`, C-1..C-4, R5..R12) and Y-line (`REVISE…_YLINE`,
repairs 1..14) reviews. It inherits the signed activation protocol
(v1 + v2 + v2.1), the WP-3 signature, and the WP-4 inactive boundary
unchanged; every constant, schema, event, and phase rule below is the
signed one. The C4 namespace repair at `38ea2f3` is engineering
context only; **no implementation hash, reviewed HEAD, or production
manifest is pinned here.**

It creates nothing executable and selects no learner, architecture,
optimizer, training rule, certificate numeric, Q predicate, alpha,
margin, candidate, device winner, or scientific endpoint. T remains
`NOT_ACTIVATED` at genesis; E2 and every Q/C gate are untouched.

---

## 1. Scope and authority

The harness is the **only future issuer and revoker of exact real-T
capabilities**. After activation, every behavior-capable operation
(the v2 §A functional boundary: instantiating/querying a signed
T-band world, evaluating/training a behavior-capable learner, creating
a behavior-bearing checkpoint, or using a T observation to alter
learner/optimizer/policy/interface/stack/numerical mode/config) exists
only inside a harness-issued, leased, metered capability.

**Ownership pins (X-R12):** the production `RealTCapability` exact
type is defined and *solely* issued inside
`src/philosophia/officina/generic_harness.py` via a private token; the
inactive `runtime.py:RealTCapability` / `issue_real_t_capability`
remain **unmodified raising decoys**. The supervisor process is the
sole holder of `T_RUNTIME.lock` and the sole writer of
`runtime/T_PROCESS_CLAIMS/`, `runtime/T_ACTIVE_LEASES/`, and
`runtime/T_PROCESS_RECORDS/`, and performs every §3-template
transaction. Fake clock/meter/world types are test-only and never
importable by any production-graph module.

Activation authorizes only: starting the E3 calendar clock and
admitting harness-supervised, E1-metered, ledgered, permanently
non-citable T development in the signed T-dev bands
`[10,25] ∪ [166,205]`. It does not authorize: candidate registration
or E2 (impossible before the signed WP-6 Q contract — the inactive E2
barrier stands); Q attempts, entropy roots, Q/C capabilities (types
remain issuerless); breathing-check qualification (WP-6); any
scientific specification, lock, escrow, or C activity (WP-9/WP-10);
any claim movement. T is adaptive, open, permanently non-citable for
C1–C6; no T event, log, checkpoint, or ending can become Q/C evidence;
no object, enum, or schema here implies execution authority —
authority exists only as a live, valid, harness-issued lease.

## 2. Lifecycle state machine

### 2a. Global states and dominance

| State | Entered by | Work admission |
|---|---|---|
| G0 `GENESIS_INACTIVE` | — | none |
| G1 `ACTIVE` | `T_ACTIVATED` | admissible |
| G2 `E3_DUE` (nonterminal) | either E3 clock due | refused until `T_REVIEW_COMPLETED` |
| G3 `PAUSED` | valid `T_OPERATIONAL_PAUSE` (§6) | refused until valid resume |
| G4 `RESUME_REVIEW_PENDING` | overdue-resume pause entry (§6) | refused until durable review |
| G5 `RUNTIME_INVALID` | `T_RUNTIME_INVALID` | refused until signed recovery disposition (§6c) |
| G6 `AUTHOR_STOPPED` (terminal) | `T_AUTHOR_STOP` | never |
| G7 `ENVELOPE_EXHAUSTED` (terminal) | `T_ENVELOPE_EXHAUSTED` | never (E1; E2 only after WP-6 exists) |

**Dominance table (Y-4) for fault-free compound boundaries, fixed
order:** `E1 exhaustion > E3 due > signed author stop > operational
pause > ordinary process close`. Simultaneous E1/E3 records exhaustion
once and retains E3-due in the post-state; neither resets the other.
**Infrastructure invalidity dominates every valid ending:** the charge
and invalidity are recorded, exhausted/due resource facts are retained
in the post-state, but the ending is never reinterpreted as valid
exhaustion, pause, censoring, voluntary stop, or author stop — an
invalidity that conservatively consumes the last E1 **remains an
invalid ending**. **Public-cause precedence for simultaneous invalid
causes, fixed:** `HASH > FILESYSTEM > CLOCK > PROCESS > RESOURCE`
(integrity-first: the least recoverable, most evidence-destroying
cause names the event; the invalidity detail record lists every
observed cause). Every pair is tested (§10).

### 2b. Process states

P0 `ABSENT` → P1 `CLAIMED` → P2 `STARTED` → P3 `LIVE` →
{P4 `CLOSED_VALID`, P5 `CLOSED_INVALID`}. Exclusive and total; no
branch falls through, silently retries, erases liability, or
reinterprets an invalid run as a valid terminal.

### 2c. Transitions

1. **Process claim creation** (P0→P1): G1; no artifact for this
   process id; reservation per §4b admits the declared `k` streams.
   Durable: process claim (`…t-process-claim.v1`, exact v2 §D keys;
   immutable-control map = the activation record's map). Next: 2 only.
2. **`T_PROCESS_STARTED`** (P1→P2): claim durable and verified.
   Durable: the non-state-bearing start event carrying
   `process_claim_sha256`. A start without a subsequent lease is
   fail-closed invalidity at next admission. Next: 3 only.
3. **Lease installation** (P2→P3): under the lock, reserve per §4b;
   install the active lease with **`prior_charge_event_sha256` seeded
   to the process's `T_PROCESS_STARTED` entry hash** (there being no
   prior charge event; X-R7/Y-5); then and only then issue the
   capability bound to activation record, process id, source HEAD, T
   bands, and lease identity. Renewal is heartbeat settlement (5).
4. **Behavior-capable operation** (P3): every oracle admission,
   learner-update admission, and checkpoint creation revalidates
   pinned control bytes, lease currency, group membership, declared
   streams (reconciled against observed workers and backend queues),
   and both E3 clocks; every result reaches the controller only
   through the §5b isolation-and-promotion protocol.
5. **Heartbeat settlement** (P3→P3): under the lock — settle the
   monotonic cursor delta only; append `T_DEVICE_TIME_CHARGED` whose
   `active_lease_sha256` is the hash of the **exact pre-settlement
   lease** and whose `charge_ns` is the **only** increment to global
   E1 and that lease's cumulative charge; after the event is durable,
   install the successor lease (cursor = captured reading; cumulative
   += `charge_ns`; `prior_charge_event_sha256` = the event hash; new
   exact liability/deadline per §4b) — no cyclic post-lease/event hash
   exists (Y-5); replace state cache; renew the deadline. A missed
   deadline invokes §5a quiescence, never a silent extension.
6. **Voluntary stop** (P3→P4) **(X-R1/Y-6; the only valid-close
   order):** quiesce (§5a) → final charge through the close boundary
   (`T_DEVICE_TIME_CHARGED`, `charge_ns > 0`) → **durable final
   process record** (`…t-process-record.v1`; disposition
   `T_PROCESS_VOLUNTARY_STOP` or `T_PROCESS_CLOSED`;
   `final_charge_event_sha256` = that charge event;
   `final_t_state_sha256` = its post-state; cumulative charge includes
   the final event) → `T_PROCESS_STOPPED` state-bearing event carrying
   `process_id`, `process_record_sha256` **of that record**, and the
   full post-state → head, then state/lease cache → active lease
   removed only after post-verify of the record → archival commit of
   the exact v2 §B close set. Learner exception/non-finiteness closes
   by exactly this route with disposition
   `T_PROCESS_VOLUNTARY_STOP`, no learner-behavior cause or metric
   (v2.1 §3) — quarantined development fact, never invalidity.
7. **Resource stop** (P3→P4): identical order, disposition
   `T_PROCESS_RESOURCE_STOP`; actual overrun recorded in full, never
   clipped.
8. **E1 exhaustion** (settlement crossing → G7): handled as a §4d
   boundary batch. **`T_ENVELOPE_EXHAUSTED` is appended only when
   realized durable `device_nanoseconds ≥ 168 device-hours`** (a
   crossing or conservative settlement); a reservation refused on E1
   while sibling leases are live refuses the new stream only and
   appends no exhaustion event (v2.1 §4; X-R8/Y-3).
9. **E3 due / completed** (G1→G2→G1): due at either clock — batch
   settle (§4d), revoke usability, quiesce; only a durable
   `T_REVIEW_COMPLETED` transaction advances `last_review_utc` and its
   device counter. E3-due caused only by sibling reservations does not
   arise: reservations never set E3-due (§4b); only durable charged
   device time or actual UTC does.
10. **Operational pause** (G1→G3): §6a.
11. **Author stop** (G1/G2→G6): only with the separately tracked
    Kirill signature bound to a just-completed E3 review and exact
    ledger/state head; distinct from exhaustion, pause, and
    invalidity. Honesty rule of §7 applies.
12. **Live-process invalidity** (P3→P5, driving G1→G5) **(X-R2/Y-6):**
    conservative final settlement per §4c (`T_DEVICE_TIME_CHARGED`
    events as computed there) → invalidity detail record
    (`…t-runtime-invalidity.v1`) → `T_RUNTIME_INVALID` event (hash of
    that record, typed public cause per §2a precedence, full
    post-state, `SIGNED_BOUNDED_RECOVERY_NO_AUTOMATIC_RETRY`) →
    **INVALID final process record** (`…t-process-record.v1`;
    disposition `T_PROCESS_INVALID`; validity
    `INVALID_PROCESS_RECORD`; `invalid_cause` = the event's cause;
    `final_charge_event_sha256` = the `T_RUNTIME_INVALID` event;
    `final_t_state_sha256` = its post-state) → lease removed only
    after verification → archival commit of the v2 §B invalid-close
    set (claim, final record, state, ledger, head; lease absent).
    12a. **Global invalidity with no live process** (G1→G5; e.g. a
    filesystem/hash fault during an E3 review or activation):
    invalidity detail record → `T_RUNTIME_INVALID` event only; **no
    process record is created or staged.**
    12b. **G5 with concurrent live leases (X-R6/Y-6):** entering G5,
    every supervisor first revokes authority for, conservatively
    settles (§4c), and invalid-closes **every** live sibling lease per
    12; no sibling continues or remains uncharged under a fail-closed
    global state; no new admission occurs during the batch.
13. **Record-first invalidity rule** (v2.1 §6, unchanged): detail
    record first, then the event binding its hash; missing, extra,
    mismatched, or reversed artifacts are themselves unrecoverable
    without signed disposition. Recovery packets contain only the v2
    §F fact classes; learner observations are unavailable to recovery
    decisions.
14. **Resume after ordinary power-off** (G3→G1 or G3→G4): §6b.

## 3. Durable transaction ordering

Discipline inherited exactly: canonical ASCII JSON with trailing
newline; same-directory temp write → file `fsync` → atomic install
(no-replace for creations; replace only where the protocol says
replace) → parent-directory `fsync`; the held-descriptor
`T_RUNTIME.lock` (`O_RDWR|O_CLOEXEC|O_NOFOLLOW`, canonical content,
`flock(LOCK_EX)`) across read → anchor validation → verify → append →
cache/lease update → fsync → post-verify; ledger append through the
descriptor equal to the held anchor; hash chain to the external head.
**No Git commit is a runtime safety precondition:** archival occurs
only at the fixed v2 §B boundaries with the exact staged sets and
trailers; commit failure preserves every durable working-tree fact,
blocks capability, and never erases charge or authorizes retry.

**Template with crash cut-points** (instantiated per transition; the
implementation enumerates each):

```text
 1. acquire lock; validate anchors, control bytes, state/ledger equality
 2. compute transition; capture clock readings once
 3. write+fsync dependent artifact(s) (claim / final process record /
    review record / invalidity detail / pause checkpoint) — atomic
    no-replace
 4. append ledger event (state-bearing events carry full post-state);
    fsync through held descriptor
 5. atomically replace external head; fsync
 6. atomically replace state cache (and successor lease); fsync
 7. post-verify: re-derive state from ledger; release lock
[8.] archival boundaries only: stage the exact set, commit with the
    fixed trailers
```

| Crash cut | Durable at crash | Legal action |
|---|---|---|
| before 3 | nothing new | re-invoke admission; a live lease's liability rule (§4c) governs any lost interval |
| after 3, before 4 | orphan dependent artifact | fail-closed at next lock entry → record-first invalidity naming the orphan; no deletion, no id reuse |
| after 4, before 5 | ledger ahead of head | ledger is authority; **record-first invalidity** — head repair occurs only under the signed recovery disposition (§6c), never silently |
| after 5, before 6 | cache/lease one event behind consistent ledger+head | §3a sole idempotent completion |
| after 6, before 7 | consistent | post-verify at next entry |
| during 8 | runtime facts durable; archival incomplete | capability blocked; commit completed only under a signed process disposition; charge untouched |

**§3a — the one permitted silent action (X-R5/Y-14):** within one lock
epoch, an interrupted **state-cache/lease successor** whose remaining
step 6 is **fully derivable** from an otherwise fully consistent
durable ledger + head (cache exactly one state-bearing event behind)
may be completed idempotently before the lock is released. This is the sole
silent completion. Any other ledger/head/cache disagreement — a cache
not derivable from the ledger, a broken chain, a head/ledger mismatch —
is record-first invalidity, never repair-in-place. The ledger is
always the authority; the state cache is a checked, non-authoritative
cache; the active verifier is authoritative only at rest (lock not
held, no in-flight transaction).

## 4. Metering, reservation, and conserving settlement

### 4a. Constants and units (signed; unchanged)

`HEARTBEAT_LIABILITY_SECONDS = 60`, `MAX_CONCURRENT_LEASES = 4`,
`DEVICE_UNITS_PER_LEASE = 1` per behavior-capable stream,
`MAX_AGGREGATE_LIABILITY_DEVICE_SECONDS = 240` (assertable only when
all live trees have timely quiescence proofs). Units are
device-nanoseconds. One unit admits exactly one concurrent
behavior-capable execution stream (v2.1 §2); behavior-inert children
ride their stream's unit; an independently querying/training/
checkpoint-writing child is another stream requiring its own unit and
slot; unclassifiable parallelism revokes the group and routes to §4c.

### 4b. Reservation arithmetic (Y-3; exact, multi-stream)

For a request of `k` streams, after subtracting **all other live
aggregate liabilities** from both budgets:

```text
ℓ = min(60 s,
        floor(E1_available / k),
        floor(E3_device_available / k))
```

Reserve aggregate liability `k·ℓ`; every stream's watchdog deadline is
shortened to `ℓ`. `ℓ = 0` caused only by sibling reservations
**refuses the request** and triggers settlement/recomputation of those
siblings; it appends neither exhaustion nor an early review.
`T_ENVELOPE_EXHAUSTED` only per §2c.8; E3-due only from durable
charged device time or actual UTC. Total live units never exceed 4;
refusal happens before overspend; post-hoc truncation does not exist.

### 4c. Recovery charge — the signed three-case rule (X-R3/Y-1; the only rule)

The reserved per-stream liability is a reservation ceiling and
watchdog deadline, **never itself the recovery charge**. On deadline
miss, process loss, reboot (boot-identity change), monotonic
reset/backward motion, clock ambiguity, escaped/unclassifiable work,
or backend-synchronization failure, each affected stream is charged by
exactly one signed case (v2.1 §1):

- **(a) timely quiescence proven:** the actual interval
  `units × (quiescence_reading − last_durable_reading)`, with the
  reservation as an upper bound;
- **(b) quiescence later but its monotonic reading known:** that same
  complete actual formula, recorded in full **even where it exceeds
  the reservation and crosses E1**;
- **(c) interval or backend cessation unknowable:** the global
  unknown-pool rule of §4d.

No path substitutes a flat reserved amount; the sole floor is that a
lost stream is never charged zero. Reboot, boot-id change, clock
faults, process loss, escapes, and failed synchronization **select
among these cases only**.

### 4d. Global conserving settlement batch (Y-2)

Whenever a settlement reaches E1 or E3, or the runtime enters G5, or
recovery settles lost streams, one runtime-lock epoch performs the
**batch**: (1) revoke all affected capabilities; (2) freeze/terminate
all affected groups; (3) synchronize every backend; (4) snapshot every
live lease. Let `D0` = durable global E1 at entry. For each provably
quiesced stream compute its known charge once from its last durable
cursor (§4c a/b); let `K` = their sum and
`R = max(0, E1_cap − (D0 + K))`. If any stream is unknowable, debit
**exactly the one global pool `R`** — not `R` once per lease —
allocated over the `m` unknowable streams sorted by
`(process_sequence, stream_index)` as `floor(R/m)` each plus one
nanosecond to the first `R mod m`. Post-total is `D0 + K + R`; known
overrun is retained in full; the batch consumes all remaining E1
without multiplying it. A zero share after a prior crossing is
recorded as zero *additional* debit — never as evidence of zero work
and never as a valid close. Only positive-`charge_ns` events are
appended (a zero-share stream's invalidity record preserves its
liability facts without a zero charge event); every liability is
preserved in the invalidity/process records; **no new admission occurs
during the batch**; terminal/gate decisions follow §2a dominance only
after every live lease is settled.

### 4e. Conservation invariants (Y-5; checked at every rest state)

```text
global E1 (state.device_nanoseconds)
  = Σ durable per-process cumulative charges
live aggregate liability
  = Σ exact liabilities of installed active leases
every charge event: charge_ns > 0, and is the sole increment applied
  to exactly one lease and the global state
```

### 4f. Meter adapter contracts (Y-10; no device winner)

**CPU streams:** monotonic elapsed wall time (`CLOCK_MONOTONIC`) while
behavior-capable, including blocking/waiting, until proven quiescence.
**Off-CPU streams:** every submitted command holds one declared stream
and accrues liability **from submission until adapter-proven
completion or cancellation**; overlapping commands consume separate
units; merely queued nonexecuting commands are not free — they remain
liabilities. The adapter must prove: active/concurrent vs queued
state; completion/cancellation; output confinement (§5b); and the
exact monotonic interval per stream. Any of those facts not exactly
measurable ⇒ **the unknowable case** (§4c c / §4d) — never a
CPU-wall-time estimate. Adapters are **statically imported, reviewed
modules** added to `reviewed_source_paths` and the immutable-control
allowlist by their own bounded authorization; no reflective/plugin
discovery (the quarantine verifier refuses
`importlib`/`__import__`/`getattr`/`eval`/`exec`); an unreviewed
backend is ineligible (X-R10; v2.1 §1). UTC and boot-identity rules
are the signed v2 §D rules.

## 5. Supervisor, watchdog, and isolation

### 5a. Supervision (unchanged from signed semantics)

Each controller tree runs under a separate supervisor owning the
process group and capability. Controller identity = PID + kernel
start-identity + boot identity, all in the claim; PID reuse is
defeated by start-identity comparison at every admission and
settlement; group membership and declared streams are reconciled at
every admission, heartbeat, and quiescence proof. The watchdog owns
the deadline and executes the v2.1 §1 sequence at or before it
(revoke → freeze/terminate → backend synchronize → prove quiescence →
durably settle actual E1 per §4c). Capability refusal alone is never
quiescence. A dead controller leaves no usable capability (issuance is
supervisor-held and lease-bound) and no uncharged liability (§4c/§4d).
**Threat model:** this prevents accidental faults, process escapes,
crashes, clock/filesystem failures, and honest operator error — not a
privileged malicious operator; that residual is procedural (signed
records, review), as in every prior Officina custody statement.

### 5b. Isolation-and-promotion protocol (Y-9; replaces v1's response wrapper)

Every oracle result, learner update, and checkpoint operation runs in
a supervised worker/backend context whose **mutable memory, IPC
channels, file descriptors, temporary paths, and backend output
buffers are neither readable nor writable by the adaptive
controller**. The worker holds no independently usable T capability
and cannot initiate another behavior-capable operation before
promotion. Promotion sequence: revoke the worker's output authority →
quiesce → synchronize the backend → capture the result hash → durably
settle the charge (§4) → **atomically promote** the result or
checkpoint and issue a **one-use release token** bound to activation
record, process id, lease hash, operation id, result hash, and
charge-event hash. A settlement failure, killed child, escaped
process, queue ambiguity, or invalid close **exposes no result** and
cannot promote or reuse its temporary output; disposal of such output
is selected solely by the signed recovery artifact (§6c), never by
inspecting the result. Release tokens are non-exportable T
capabilities and never occur in candidate, Q, `H_preC`,
`selection_scope_id`, or C schemas (§8).

## 6. Physical pause, durable resume, and signed recovery

### 6a. Ordinary pause (Y-8; fail-closed at every cut)

A planned resumable pause exists **only** when all of: zero verified
live leases (voluntary closes per §2c.6 first); proven CPU/backend
quiescence; final durable charges; an **immutable checkpoint of the
exact claim-enumerated byte set** (model/optimizer/config/stack and
runtime artifacts), hashed; the state-bearing `T_OPERATIONAL_PAUSE`
event with full post-state; head and cache equality; directory
`fsync`; successful post-verification; and the exact pause archival
commit. **Power loss before any one condition** is process-loss/reboot
invalidity or the incomplete-archival signed-disposition route — never
a pause completed after the fact. E1 does not advance while off; E3
calendar does; neither clock resets.

### 6b. Resume (Y-7/Y-8; no tenth event)

Resume re-validates control bytes, ledger/head/state chain, checkpoint
hashes, boot identity, and clock monotonicity against the pause
record. A **changed** boot identity is accepted only because the pause
already proved zero work; a **missing/ambiguous** boot identity or UTC
rollback is record-first invalidity. Any mutation, deletion,
substitution, or stale lease refuses. E1 is restored exactly; only E3
calendar advanced. **If E3 became due while off:** the resume
transaction appends a **second `T_OPERATIONAL_PAUSE` entry** bound to
the same verified checkpoint, with fixed reason
`RESUME_E3_REVIEW_PENDING`, `resets_e3: false`, and a full post-state
with `resume_review_pending: true`, updating head and cache by the
standard §3 transaction — so the serialized cache equals the last
state-bearing event and the gate is durable, not in-memory. Only a
durable `T_REVIEW_COMPLETED` clears the flag; no capability, output,
checkpoint, or backend submission precedes it. This uses the existing
vocabulary; no tenth event exists.

### 6c. Signed recovery disposition (Y-7; closed, no automatic retry)

Recovery from G5 uses one closed artifact class: a signed
recovery-disposition record binding the invalidity detail record and
event hashes, exact ledger/head/state hashes, all charges, every
affected process id, and one fixed action token
(`SIGNED_BOUNDED_RECOVERY_NO_AUTOMATIC_RETRY` resolution); it contains
only v2 §F fact classes — learner observations are unavailable.
Admission leaves G5 only when every unresolved invalidity has exactly
one verified disposition and every discrepancy is durably reconciled;
the next process uses a fresh id; no failed operation is retried or
completed silently. The correction of any incomplete archival set
occurs only under this artifact.

## 7. Closed non-outcome inputs (Y-11)

E3 due/completion, resource-stop classification, recovery, pause, and
validity decisions are deterministic functions of **closed input
schemas** containing only clocks, charges, identities, integrity
hashes, and signed constants. Learner behavior, result hashes *as
values*, update/checkpoint completion *as a success signal*, losses,
competence, and free-text reasons are rejected recursively (the
existing `reject_scientific_fields` discipline). Learner-driven
stopping is public `T_PROCESS_VOLUNTARY_STOP`, never resource stop or
invalidity. **Stated honestly:** T is openly readable and adaptive, so
a human `T_AUTHOR_STOP` **may be T-informed** unless a separately
reviewed blinding procedure exists; it is therefore a quarantined T
decision whose timing and occurrence are conditioning history only —
never Q/C evidence, never a scientific destination, and mechanically
it still requires its signed, review-bound transaction (§2c.11). What
is mechanical is that every *infrastructure* decision path accepts
only the closed non-outcome inputs above.

## 8. Draft surface, labels, and the pre-WP-6 boundary (Y-12/Y-13)

**Draft manifest** schema `philosophia.officina.t-draft-manifest.v1`,
keys **exactly**:

```text
schema, scientific_outcome (false), t_quarantine ("dev-non-citable"),
q_eligible (false), behavior_source_sha256, config_sha256,
stack_sha256, numerical_mode_sha256, device_identity
```

No `created_utc`, no lineage tuple, no sequence/queue/priority field —
the ordering and variable-length channels are **removed**, not
neutralized. Checkpoint lineage for T engineering lives in separately
closed, quarantined T-development schemas, never in the draft
manifest. The signed runtime schemas (claim/lease/record/review/
invalidity/state/envelope) retain **only their signed keys** — the
`t_quarantine` label belongs solely to separately closed
T-development artifact schemas (draft manifests, dev logs,
checkpoints, release-token records).

**Boundary rules:** Q/C entry points reject every T artifact **as a
whole** — there is no pre-WP-6 exception. A future WP-6 may
independently define and recompute only a narrowly defined **opaque
behavioral-identity/lineage digest** from exact bytes, as the charter
already requires; it must not accept the T artifact, its token, any
tuple order/length, eligibility claim, or creation order. Hash values
may be tested only for identity/equality — never decoded, ordered,
selected, or used as a statistic, covariate, margin input, resource
decision, or evidence. Release tokens never occur in candidate, Q,
`H_preC`, `selection_scope_id`, or C schemas. **The draft manifest is
not the charter's canonical candidate manifest and binds no future
candidate equivalence, admissibility, stack-family, breathing-check,
competence, attempt, promotion, seed, endpoint, horizon, or analysis
rule; reserved namespaces and transaction hooks confer no schema or
writer authority; WP-6 may replace the draft-adjacent surface entirely
and may require a newly reviewed metering-core change; WP-9 owns all
certificate/C numerics.** `Q_CAP_EXHAUSTED_NO_QUALIFIER`, invalidity,
author stop, and E1 exhaustion remain distinct negative/process
destinations with no success, equivalence, boundary, censoring, or
impossibility reading.

## 9. Immutable implementation boundary and call-graph duty (X-R4/R10/R11)

**Production roots are exactly the immutable-control verifier's pinned
tuple:**

```text
scripts/officina_activate_t.py
scripts/verify_officina_active.py
src/philosophia/officina/generic_harness.py
```

`generic_harness.py`'s **`__main__` is the CLI**
(claim/start/heartbeat/close/pause/resume, refusal-first), invoked
`python -m philosophia.officina.generic_harness`. **No additional
`scripts/*.py` entry point is introduced** — in particular no
`scripts/officina_t_process.py` — since adding one would require a
reviewed amendment to the immutable-control file `verification.py`,
which this contract does not authorize. The future
`runtime_control/PRODUCTION_CALL_GRAPH.json` (schema
`philosophia.officina.production-call-graph.v1`) must have
`roots` equal to that tuple, every repository-local transitive
dependency enumerated, all asserted sources reachable from roots and
nothing unreachable asserted, no ambiguous resolution, no dynamic
import/reflection, no hidden entropy, no test-only capability symbol,
no predecessor behavior dependency, and exact reviewed source bytes
with reviewed-commit provenance; **it remains absent until
implementation review authorizes its creation.**

**Import discipline:** the harness is implementable within the pinned
`ALLOWED_ABSOLUTE_IMPORTS`/`ALLOWED_RELATIVE_IMPORTS` (CPU-only:
`subprocess` with `start_new_session=True`, `os.killpg` with integer
signals, `time.clock_gettime_ns`, `fcntl`, `os`); it uses no
`signal`/`threading`/`multiprocessing`/backend import. Any
cross-module import of `generic_harness`, and any off-CPU adapter's
backend import, requires a reviewed amendment to that allowlist —
off-CPU adapter admission is its own bounded control review.

## 10. Executable acceptance matrix

All positive paths in disposable roots/mirrors with fake clocks/meters
and test-only worlds; no test creates a production-compatible real-T
artifact. Deterministic coverage required for **every** §2 transition,
**every** §3 cut, and at least:

| Probe class | Required behavior |
|---|---|
| valid close order | charge → durable record → `T_PROCESS_STOPPED` hashing it; event-before-record impossible |
| live-process vs no-process invalidity | 12 vs 12a artifact sets exact; no manufactured process record |
| G5 with 1–3 live siblings | all revoked, settled (§4c/§4d), invalid-closed; none continues; no admission during batch |
| three-case recovery charge | (a) ≤ reservation; (b) actual interval **exceeding** reservation and crossing E1, recorded in full; (c) unknown-pool |
| unknown-pool conservation | `m ∈ {1,2,3}` unknowable streams: total debit exactly `R`; `floor(R/m)` + remainder-nanoseconds allocation; zero-share after crossing = zero additional debit, still invalid ending |
| multi-stream reservation | `k > 1` at ordinary and shortened E1/E3 boundaries; `ℓ = 0` from siblings → refusal + sibling recomputation, no exhaustion/review event |
| exhaustion semantics | event only at realized ≥ 168 h; reservation refusal appends nothing |
| conservation invariants | §4e equalities at every rest state |
| lease/charge hash chain | seed = `T_PROCESS_STARTED` hash; per-settlement relation; final record includes final event |
| dominance | every fault-free compound pair; E1+E3 simultaneous; invalidity dominating each valid ending; each invalid-cause pair per precedence |
| §3a sole silent completion | interrupted head/cache successor completed; every other mismatch → record-first invalidity |
| isolation escapes | retained response, mutable in-process update, mmap/filesystem checkpoint escape, pipe/socket inheritance, killed supervisor/controller/child, escaped group, queued work after death, crash before/after each promotion cut → no result exposed |
| pause/resume | power cut after every §6a condition individually; changed vs missing boot id; UTC rollback; overdue resume second-pause entry; work refusal until durable review |
| recovery | disposition artifact required; fresh process id; no silent completion/retry |
| meters | CPU wall vs off-CPU submission-to-completion; queued-not-free; unmeasurable → unknowable case |
| information boundary | scientific/learner fields injected anywhere → recursive rejection; closed input schemas for E3/resource/recovery/pause |
| pre-WP-6 | E2/candidate attempts refuse; draft manifest with any extra field (timestamp/lineage/order) → schema rejection; Q/C rejects whole T artifacts; release token in any candidate/Q/`H_preC`/C schema → rejection |
| roots/graph | manifest roots ≠ pinned tuple → fail; unreachable/ambiguous/reflective/test-symbol source → fail |
| relabelling | proof that no invalid process or programme ending can be recorded as any valid terminal |

## 11. Cursor implementation handoff (after contract signature)

| Item | Content | Owner |
|---|---|---|
| `src/philosophia/officina/generic_harness.py` | supervisor, lifecycle tables (§2), §3 transaction helpers, §4 reservation/settlement/batch/conservation, §5 isolation-and-promotion, §6 pause/resume/recovery, CPU meter adapter, **`__main__` CLI** (claim/start/heartbeat/close/pause/resume, refusal-first) | **Cursor** (mechanical, from this contract) |
| `tests/test_officina_generic_harness.py` (+ fault-injection helpers) | the complete §10 matrix, rows verbatim | **Cursor** |
| schema/state-machine conformance review, integration, archival commits | | **Codex** |
| bounded X/Y confirmation | | **Opus / Sol** |
| contract signature; any future activation token | | **Kirill** |

Cursor receives no authority to choose scientific cells, alter
constants/schemas/events, weaken any refusal, add entry points or
imports, create author tokens, or activate T; ambiguities route back
as contract questions, never inline decisions.

## 12. Gate, compatibility, and author choices

Cadence: **one bounded X/Y confirmation of these repairs → Kirill's
signature** (`I_ACCEPT_OFFICINA_GENERIC_HARNESS_CONTRACT`); reopening
only for a concrete Critical contradiction. Not applicable to
WP-6/WP-9 scientific contracts or one-shot drivers.

**Compatibility classification** (completed in the closure, three-way:
inherited signed rule / deterministic clarification / amendment): this
v2 contains **no protocol amendment**. The v1 clauses that were silent
amendments — the flat recovery charge and the extra CLI root — are
**repaired back to the signed v2.1 rule and the pinned verifier
tuple**, which is not an amendment. Future items that *would* be
amendments and are **not** taken here: off-CPU adapter admission
(backend import + allowlist + immutable-control change), any
cross-module import of `generic_harness`, any new entry point.

**Remaining author choices: none.** Every constant is signed; the
harness adds mechanism, not policy.

---

After signature, the only authorized next step is §11 implementation
and its bounded review. Activation, worlds, learners, entropy,
candidates, draft-manifest instances, spend, Q/C artifacts, and every
scientific object remain absent and unauthorized. T and Q are
permanently non-citable for C1–C6; the programme claim remains `OPEN`.
