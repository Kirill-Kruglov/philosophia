REVISE_OFFICINA_GENERIC_HARNESS_CONTRACT_XLINE

# Opus 4.8 X-line — Officina generic metered harness contract v1 review

Reviewer: Opus 4.8 (X-line, adversarial engineering-contract implementability).
Repository: `/home/master/llm_projects/philosophia`. Bounded mandate: one X-line
review of `successor/OFFICINA_GENERIC_HARNESS_CONTRACT_V1_DRAFT.md` and its
closure `reviews/fable_officina_generic_harness_contract_v1_closure.md` against
the signed activation protocol (v1 + v2 + v2.1), the WP-3 signature and WP-4
boundary, and the current inactive schemas/code at HEAD (C4-confirmed, commit
`6ba2d23`; residual confirmations of `2277331` noted pending).

**I edited no existing file, created exactly one file (this review), committed
nothing, implemented nothing, created no `generic_harness.py`, no CLI, no
manifest, no authorization, no capability, no world/process/lease, no draft
manifest instance, spent no E1/E2/E3, and activated no T state.** All work was
reading the contract, the three protocol files, WP-3/WP-4 records, and the
inactive sources (`runtime.py`, `activation.py`, `accounting.py`, `checkpoint.py`,
`ledger.py`, `verification.py`) plus `git log`/`git show` (read-only). The real
tree remains pristine and `NOT_ACTIVATED`. This is an **X-line engineering
review**; it asserts no scientific outcome and predicts nothing about any learner.

## Verdict

**REVISE.** The contract is close and mostly faithful, but it is **not yet
bit-exactly implementable** and it contains contradictions — with itself, with
the pinned inactive code, and in three places with the *signed* v2.1 — that would
make two independent Cursor implementations diverge or fail the immutable-control
verifier. Four are Critical (C-1..C-4). None is a scientific/authority defect;
all are mechanical. The no-amendment claim (closure §2) does **not** hold as
drafted: two clauses are silent policy/control changes, not clarifications.

A corrected v1.1 that applies R1–R12 below is expected to be X-line acceptable
without reopening the protocol chain.

---

## A. Answers to Fable's four X-line questions

**Q1 — Totality (every reachable runtime condition has exactly one row, liability
preserved): NO, not yet.** Three reachable conditions have no correct row:
(a) the voluntary/resource close is ordered so `T_PROCESS_STOPPED` precedes the
process record it must hash — impossible (C-1); (b) a process-scoped invalid
close never creates the `t-process-record.v1` that v2 §B requires it to archive,
and the contract does not separate process-scoped invalidity from global no-
process invalidity (C-2); (c) when one process forces `G1→G5`, the **other** live
leases (up to three) are left unspecified — running, uncharged, under a global
fail-closed state (R6). Compound faults (crash during quiescence settlement,
reboot between ledger append and head replace, watchdog during a close commit)
are otherwise handled by §3, once C-1..C-3 and R5/R6 are fixed.

**Q2 — Capability containment (no usable capability / no uncharged interval,
incl. supervisor death after issuance before first settlement): PARTIAL.** The
issuerless design is sound — the inactive `runtime.py:RealTCapability`/
`issue_real_t_capability` raise, issuance is supervisor-held and lease-bound, and
settle-before-release is enforced by §7 plus the `T_DEVICE_TIME_CHARGED`-gated
`build_process_record`. **But the "no uncharged liability" guarantee is
undercut by C-3:** for supervisor death / watchdog-without-quiescence the
contract charges "the full outstanding liability" (the ≤60 s reservation),
whereas signed v2.1 §1 charges the *actual* interval through verified quiescence
(which may exceed the reservation) or, when unknowable, *all remaining lease-
eligible E1*. As drafted, a controller that ignores the heartbeat and runs past
the deadline (the exact adversary v2.1 §1 names) is undercharged. Fix C-3 and the
containment answer becomes YES.

**Q3 — Call-graph closure (test-only/predecessor code cannot reach production,
incl. the harness CLI root and off-CPU adapters): NO, not as drafted.** The
symbol ban itself is sound (`verification.py` `PRODUCTION_TEST_SURFACE_SYMBOLS`,
`FORBIDDEN_IMPORT_PREFIXES`, entropy/dynamic/random-device lints, now C4-hardened
over the whole reachable closure). **But (i)** the contract's own root/CLI set
(§9, §11: `scripts/officina_t_process.py`) contradicts the pinned, C4-confirmed
`verification.py:PRODUCTION_ROOTS = {officina_activate_t.py,
verify_officina_active.py, generic_harness.py}` and the manifest-equality check
`manifest["roots"] == list(PRODUCTION_ROOTS)` (C-4); **(ii)** off-CPU adapters
cannot be *dynamically* discovered because `verify_source_quarantine` bans
`importlib.import_module`/`__import__`/`getattr`/`eval`/`exec` — adapters must be
statically imported, reviewed modules (R10); **(iii)** any real off-CPU adapter
imports a backend library outside `verification.py:ALLOWED_ABSOLUTE_IMPORTS`, so
its admission necessarily amends the pinned import allowlist — a reviewed control
change, not a side effect (R11).

**Q4 — No-amendment claim (closure §2): REJECTED as drafted.** I accept that the
**release token** (§7), the **quiescence proof object** (§4, contents verbatim
from v2.1 §1), the **meter-adapter interface** (§4), and even the **draft-
manifest key list** (§8) are clarifications within signed semantics — none adds a
constant, event, phase rule, or eligibility. **But two items are not
clarifications:** (a) §2.12/§4/§5's flat "charge the full outstanding liability"
recovery rule is a *silent replacement* of the signed v2.1 §1 quiescence-charge
rule (C-3); (b) §9/§11's new production entry point and root set is either
unimplementable against the pinned verifier or an *undisclosed amendment* to the
immutable-control file `verification.py` (C-4). Until R3/R4 land, "no proposed
clause requires a protocol amendment" is false.

---

## B. Signed-compatibility findings by mandate attack vector

### C-1 (Critical) — Event-before-record inversion in the voluntary/resource close

Mandate 1 ("reject any … event-before-record inversion"). §2.6 orders:
`T_DEVICE_TIME_CHARGED → T_PROCESS_STOPPED → final process record`. This is
impossible. The `T_PROCESS_STOPPED` payload **must contain**
`process_record_sha256`:

```785:817:src/philosophia/officina/runtime.py
    "T_PROCESS_STOPPED": {
        "process_id", "process_record_sha256", "scientific_outcome", "t_state",
    },
```

and the record is produced by `build_process_record`, which itself depends only
on the prior `T_DEVICE_TIME_CHARGED` and final state (for a **valid** disposition
the record's `final_charge_event_sha256` is the *charge* event, never the stopped
event). So the only realizable order is **charge → record → stopped**, exactly
what §3's own template says (dependent artifact at step 3, ledger event at step
4). §2.6/§2.7 therefore contradict both the schema and §3. Two implementations
diverge: one follows the prose (unimplementable — no record hash exists yet), one
follows §3/the schema. **Repair R1.**

### C-2 (Critical) — Missing INVALID process record; process- vs global-invalidity conflated

Mandate 1 & 2. §2.12/§2.13 describe only the `t-runtime-invalidity.v1` detail
record and the `T_RUNTIME_INVALID` event. But v2 §B archival for an "invalid
process close" stages "that process claim and **final record**," and the code's
`build_process_record` supports `ProcessDisposition.INVALID`, whose record
references the `T_RUNTIME_INVALID` event as `final_charge_event_sha256` (i.e. the
INVALID process record is built **after** that event). The contract never creates
it, so the invalid-close archival set cannot be assembled. Separately, transition
12 writes "P3→P5; G1→G5" as if every process fault is global and every global
fault has a process — but a filesystem/hash fault during an E3 review or during
activation has **no** live process and no process record (cf.
`activation.py:_record_activation_invalidity`, which stages none). The two cases
need distinct, ordered specifications. **Repair R2.**

### C-3 (Critical) — Recovery charge contradicts signed v2.1 §1 (undercount)

Mandate 2 & 3; Sol Y-Q1 undercount direction. v2.1 §1 **replaced** v2 §D's flat
"charge the full outstanding 60-second liability" with three cases: (a) timely
quiescence proven → actual interval, liability as *upper bound*; (b) quiescence
later but monotonic reading known → **full actual interval through verified
quiescence, recorded in full even where it exceeds the reservation and crosses
E1**; (c) interval/backend cessation unknowable → **all remaining lease-eligible
E1** at the last durable cursor. The harness contract re-introduces the deleted
rule: §2.12 "the lease's outstanding liability is charged in full," §5 "the
outstanding reservation is charged by the recovery path," and §4 lists "process
loss, watchdog expiry without provable quiescence, reboot, … backend sync
failure → charge the full outstanding liability" as a distinct branch. This
**undercharges** the v2.1 §1 case (b) adversary — a controller that ignores the
heartbeat, resists termination, and overruns the deadline — by capping its charge
at the ≤60 s reservation. It is a silent amendment of a signed rule, not a
clarification. **Repair R3.**

### C-4 (Critical) — Production roots / CLI contradict the pinned immutable-control verifier

Mandate 6. The C4-confirmed verifier pins:

```56:60:src/philosophia/officina/verification.py
PRODUCTION_ROOTS = (
    "scripts/officina_activate_t.py",
    "scripts/verify_officina_active.py",
    "src/philosophia/officina/generic_harness.py",
)
```

and requires `manifest["roots"] == list(PRODUCTION_ROOTS)` (line 398) with every
reviewed source reachable by BFS from those roots (lines 357–377). The contract
instead declares (§9) roots = two scripts + "the harness CLI added by the
authorization," and (§11) that CLI = a **new** file `scripts/officina_t_process.py`
with `generic_harness.py` as a mere module. That file does not exist and is not a
root; an implementation following §11 produces a manifest whose `roots` differ
from `PRODUCTION_ROOTS` (hard fail) and a `scripts/officina_t_process.py` that is
"unreachable from roots" (hard fail). Adding it would require editing
`verification.py`, which is on the immutable-control allowlist (v2 §A) — a
reviewed amendment the contract does not authorize and whose existence
contradicts §1's "inherits [the protocol] unchanged … no core change." **Repair
R4.** (`generic_harness.py` is already the pinned root; the clean fix is to make
its `__main__` the CLI, invoked `python -m philosophia.officina.generic_harness`,
and delete the separate script.)

### R5 (Major) — §3 self-contradiction: silent cache re-derive vs record-first invalidity

Mandate 2 ("verify 'ledger authority' does not silently repair a … head/cache
inconsistency contrary to record-first invalidity"). §3's crash-cut row *after 5,
before 6* says "cache stale → re-derive from ledger under lock; cache replacement
is idempotent and non-authoritative," while §3's closing sentence says "a
cache/ledger disagreement **at any entry** is record-first invalidity, not a
repair-in-place." A stale cache **is** a cache/ledger disagreement, so the two
clauses conflict, and the signed verifier fail-closes on it:

```696:699:src/philosophia/officina/activation.py
        elif canonical_json(last_state_entry["data"].get("t_state")) != canonical_json(state_value):
            failures.append("state cache differs from last state-bearing event")
```

Two implementations diverge (liberal re-derive vs universal invalidity). The
boundary must be pinned exactly. **Repair R5.**

### R6 (Major) — G5 with concurrent live leases

Mandate 1 & 3. `T_RUNTIME_INVALID` is a *global* state-bearing event, so any
process-scoped invalidity forces the whole runtime fail-closed. The contract
charges only "the lease's outstanding liability" (singular) and never states that
entering G5 must revoke, quiesce, conservatively charge, and close **every other
live lease** (up to three). As drafted, siblings can keep executing behavior-
capable work under a fail-closed global state — an uncharged interval. **Repair
R6.**

### R7 (Major) — Unpinned initial `prior_charge_event_sha256`

Mandate 1 & 5 (claim/start/lease ordering, bit-exactness). At lease installation
(P2→P3) no `T_DEVICE_TIME_CHARGED` yet exists, but `build_active_lease` requires a
valid `prior_charge_event_sha256`. The contract never fixes the seed, so two
implementations produce different lease bytes → different lease hashes →
different `active_lease_sha256` throughout the chain. Pin it. **Repair R7.**

### R8 (Minor) — Exhaustion append vs realized E1 with concurrent liabilities

Mandate 1. §2.8/§4 "Zero E1 liability at reservation appends the actual exhaustion
state." With live sibling liabilities, `reservation_route` can return
`E1_EXHAUSTED` while realized `device_nanoseconds < 168 h`; but the event schema
forbids that:

```896:899:src/philosophia/officina/runtime.py
    elif event == "T_ENVELOPE_EXHAUSTED" and (
        parsed_state.device_nanoseconds < 168 * NANOSECONDS_PER_HOUR
    ):
        raise ValueError("E1 exhaustion event precedes the signed E1 cap")
```

and v2.1 §4 says "reservation refusal alone never sets exhaustion." **Repair R8:**
append `T_ENVELOPE_EXHAUSTED` only when realized `device_nanoseconds ≥ 168 h`
(a crossing settlement); a reservation refused with live leases present refuses
the new stream only.

### R9 (Minor) — Draft-manifest `created_utc` vs the "order-free" claim

Mandate 4; Sol Y-Q4. §8 asserts the schema is "order-free (no sequence, queue, or
priority field exists)," yet `created_utc` is an implicit total order. It is
legitimate provenance and WP-6's recompute-from-bytes neutralizes it, but the
absolute wording is false. **Repair R9** (state it is provenance-only, or drop
it; neutrality proof deferred to Y-line).

### R10 (Major) — Adapters must be statically imported, not discovered

Mandate 3 & 4. §4's adapter admission must state adapters are statically imported
reviewed modules added to `reviewed_source_paths`/immutable-control by their own
authorization; no reflective/plugin discovery, since `verify_source_quarantine`
refuses `importlib.import_module`/`__import__`/`getattr`/`eval`/`exec`. **Repair
R10.**

### R11 (Major) — Harness must fit the pinned import allowlist

Mandate 5. `generic_harness.py` will be scanned by `verify_source_quarantine`
(glob of `src/philosophia/officina/*.py`), constrained to
`ALLOWED_ABSOLUTE_IMPORTS` (no `signal`, `threading`, `multiprocessing`, `select`,
`resource`, `ctypes`, or backend libs) and `ALLOWED_RELATIVE_IMPORTS` (which does
**not** yet contain `generic_harness`). The supervisor/watchdog is implementable
CPU-only within the allowlist (`subprocess(start_new_session=True)`,
`os.killpg(pgid, 9|15)` with integer signals, `time.clock_gettime_ns`, `fcntl`),
but the contract must commit to that and state that (i) any cross-module import of
`generic_harness` and (ii) any off-CPU adapter's backend import each require a
reviewed amendment to `verification.py`'s allowlist. **Repair R11.**

### R12 (Major) — Ownership, durable paths, fake-vs-production types

Mandate 5. §11 is too coarse for bit-exactness. Pin: the production
`RealTCapability` exact type is defined and *solely* issued inside
`generic_harness.py` via a private token; `runtime.py:RealTCapability` /
`issue_real_t_capability` remain **unmodified raising decoys**; the supervisor is
the sole holder of `T_RUNTIME.lock` and sole writer of
`runtime/T_PROCESS_CLAIMS/`, `runtime/T_ACTIVE_LEASES/`,
`runtime/T_PROCESS_RECORDS/`; the fake clock/meter/world types are test-only and
never importable by any production-graph module. **Repair R12.**

---

## C. Positive confirmations (no change required)

- Nine-event vocabulary, liability constants (60/4/1/240), `min()` reservation,
  behavior-capable stream = concurrency unit, non-finite → voluntary-stop
  quarantine, record-first *invalidity-detail* ordering, lock discipline, archival
  sets/trailers, functional E1 boundary, immutable-control revalidation, pause-
  requires-zero-leases, powered-off advances E3 not E1: all inherited verbatim and
  consistent with `runtime.py`/`activation.py`/`accounting.py`/`checkpoint.py`.
- Claim/start ordering (claim durable before `T_PROCESS_STARTED`, which carries
  `process_claim_sha256`) is correct and non-circular (§2.1→§2.2).
- Settle-before-release and response gating (§7) match the code's
  `T_DEVICE_TIME_CHARGED`-gated close and the `scientific_outcome:false` /
  `reject_scientific_fields` recursion; no scientific field can enter any
  record/event.
- Mandate 7 (no executable authority / no scientific or learner choice):
  CONFIRMED. §12 "remaining author choices: none" holds — every constant is
  already signed; the draft selects no learner/optimizer/stack/candidate/device
  winner/Q predicate/alpha/margin/endpoint; enums confer no authority; the file
  creates nothing executable. (This is orthogonal to R1–R12, which are all
  mechanical.)
- Release token, quiescence-proof contents, and adapter interface are genuine
  clarifications (Q4), subject to R3/R10/R11.

---

## D. Mandatory repair list (finite; exact replacement text)

**R1 (C-1).** Replace §2 transition 6 with:

> 6. **Voluntary stop** (P3→P4): quiesce → final charge through the close
> boundary (`T_DEVICE_TIME_CHARGED`, `charge_ns>0`) → **final process record**
> (`philosophia.officina.t-process-record.v1`; disposition `T_PROCESS_VOLUNTARY_STOP`
> or `T_PROCESS_CLOSED`; `final_charge_event_sha256` = the close-boundary charge
> event; `final_t_state_sha256` = its post-state), written as the §3 step-3
> dependent artifact → `T_PROCESS_STOPPED` state-bearing event carrying
> `process_id`, `process_record_sha256` (of that record), and the full post-
> `t_state` (§3 step 4) → external head then state/lease cache (§3 steps 5–6) →
> active lease removed only after post-verify of the record → archival commit of
> the exact v2 §B close set. Learner exception/non-finiteness closes by exactly
> this route with `disposition=T_PROCESS_VOLUNTARY_STOP`, no learner-behavior
> cause or metric (v2.1 §3) — quarantined development fact, never invalidity.

Apply the identical record-before-event reordering to transition 7 (resource
stop, disposition `T_PROCESS_RESOURCE_STOP`, actual overrun recorded in full).

**R2 (C-2).** Replace §2 transitions 12–13 (invalid path) with an ordered,
case-split specification:

> 12. **Live-process invalidity** (P3→P5, which also drives G1→G5 because
> `T_RUNTIME_INVALID` is a global state-bearing event): conservative final charge
> (`T_DEVICE_TIME_CHARGED`, §4) → invalidity detail record
> (`t-runtime-invalidity.v1`, §13) → `T_RUNTIME_INVALID` event (hash of that
> record, typed public cause, full post-state,
> `SIGNED_BOUNDED_RECOVERY_NO_AUTOMATIC_RETRY`) → **INVALID final process record**
> (`t-process-record.v1`; disposition `T_PROCESS_INVALID`; validity
> `INVALID_PROCESS_RECORD`; `invalid_cause` = the event's cause;
> `final_charge_event_sha256` = the `T_RUNTIME_INVALID` event;
> `final_t_state_sha256` = its post-state) → archival commit of the v2 §B
> invalid-close set (claim, final record, state, ledger, head; active lease
> absent). Cause ∈ `PROCESS|CLOCK|FILESYSTEM|HASH|RESOURCE`.
>
> 12a. **Global invalidity with no live process** (G1→G5; e.g. filesystem/hash
> fault during an E3 review or activation): invalidity detail record →
> `T_RUNTIME_INVALID` event only; **no** process record is created or staged.
>
> 12b. **G5 with concurrent live leases (R6):** on entering G5 every supervisor
> first revokes authority for, conservatively settles (§4/v2.1 §1), and closes
> **every** live lease; no sibling lease is left running or uncharged while the
> global state is fail-closed. (Keep §13 unchanged as the invalidity-detail /
> event dual-artifact rule.)

**R3 (C-3).** Replace the §4 "Conservative charging" sentence and align §2.12 /
§5:

> **Conservative charging (v2.1 §1, the only recovery-charge rule):** the reserved
> per-stream liability is a reservation ceiling and watchdog deadline, never
> itself the recovery charge. On any deadline miss, process loss, reboot (boot-
> identity change), monotonic reset/backward motion, clock ambiguity, or backend-
> synchronization failure, recovery charges by exactly one signed case: (a) if
> timely quiescence is proven, the actual interval through that quiescence
> reading, with the liability as an upper bound; (b) if quiescence is later but
> its monotonic reading is known, the full actual interval through that verified
> reading, recorded in full **even where it exceeds the reservation and crosses
> E1**; (c) if the interval or backend cessation is unknowable, all remaining
> lease-eligible E1 at the last durable cursor. No path substitutes a flat
> reserved amount for (a)–(c); the sole floor is that a lost lease is never
> charged zero.

In §2.12 replace "the lease's outstanding liability is charged in full before any
recovery, never zero" with "each affected lease is charged by the §4 (v2.1 §1)
three-case rule — never zero, and never clipped to the reservation when a larger
actual interval is known or the interval is unknowable." In §5 replace "the
outstanding reservation is charged by the recovery path" with "each lost lease is
charged by the §4/v2.1 §1 three-case rule."

**R4 (C-4).** Replace §9's root clause with the pinned tuple and delete the
separate CLI in §11:

> Duties: exact executable roots equal to the immutable-control verifier's pinned
> `verification.py:PRODUCTION_ROOTS` — `scripts/officina_activate_t.py`,
> `scripts/verify_officina_active.py`, and `src/philosophia/officina/generic_harness.py`
> (the metered harness, whose `__main__` is the claim/start/heartbeat/close/pause/
> resume CLI, invoked `python -m philosophia.officina.generic_harness`). The
> manifest `roots` array MUST equal that tuple; no additional `scripts/*.py` entry
> point is introduced, since adding one would require a reviewed amendment to the
> immutable-control file `verification.py`, which this contract does not
> authorize.

§11 row edits: fold the CLI into the `generic_harness.py` row ("… + `__main__`
CLI entry: claim/start/heartbeat/close/pause/resume, refusal-first"); delete the
`scripts/officina_t_process.py` row.

**R5.** Replace the §3 crash-cut row *after 5, before 6* and reconcile the closing
sentence:

> | after 5, before 6 | cache exactly one state-bearing event behind an otherwise
> fully consistent ledger+head | the same lock epoch completes step 6 (idempotent
> cache write re-derived from the ledger) before releasing the lock; this is the
> **only** silent completion |
>
> …closing sentence: "The ledger is always the authority; the state cache is a
> checked, non-authoritative cache. The *sole* permitted silent action is
> completing an interrupted step 6 as above, under the lock, before release. Any
> other cache/ledger/head disagreement — a cache not derivable from the ledger, a
> broken chain, or a head/ledger mismatch — is record-first invalidity, never a
> repair-in-place. The active verifier (`verify_active_repository`) is
> authoritative only at rest (lock not held, no in-flight transaction)."

**R6.** Fold into R2 clause 12b (above).

**R7.** Amend §2.3: "install the active lease with `prior_charge_event_sha256`
seeded to the process's `T_PROCESS_STARTED` entry hash (there being no prior
charge event); heartbeat settlement (5) thereafter sets it to the just-appended
`T_DEVICE_TIME_CHARGED` entry hash."

**R8.** Amend §2.8/§4: "`T_ENVELOPE_EXHAUSTED` is appended only when realized
`device_nanoseconds ≥ 168 device-hours` (a crossing settlement); a reservation
refused on E1 while any sibling lease is live refuses the new stream only and
appends no exhaustion event (v2.1 §4: reservation refusal alone never sets
exhaustion)."

**R9.** Amend §8: delete "no sequence, queue, or priority field exists in the
schema" OR replace with "`created_utc` is provenance only; the schema carries no
sequence/queue/priority semantics, and WP-6 recompute-from-bytes ignores
`created_utc` and every draft-side claim."

**R10.** Amend §4: "Adapters are statically imported, reviewed modules added to
`reviewed_source_paths` and the immutable-control allowlist by the adapter's own
bounded authorization; no dynamic/reflective discovery is permitted
(`verify_source_quarantine` refuses `importlib`/`__import__`/`getattr`/`eval`/
`exec`)."

**R11.** Add to §9/§11: "The harness is implementable within
`verification.py:ALLOWED_ABSOLUTE_IMPORTS`/`ALLOWED_RELATIVE_IMPORTS` (CPU-only:
`subprocess(start_new_session=True)`, `os.killpg` with integer signals,
`time.clock_gettime_ns`, `fcntl`, `os`); it uses no `signal`/`threading`/
`multiprocessing`/backend import. Any cross-module import of `generic_harness`,
and any off-CPU adapter's backend import, requires a reviewed amendment to that
allowlist — reinforcing that off-CPU adapter admission is its own bounded control
review."

**R12.** Expand §11 ownership: "The production `RealTCapability` exact type is
defined and solely issued inside `generic_harness.py` via a private token; the
inactive `runtime.py:RealTCapability`/`issue_real_t_capability` remain unmodified
raising decoys. The supervisor process is the sole holder of `T_RUNTIME.lock` and
sole writer of `runtime/T_PROCESS_CLAIMS/`, `T_ACTIVE_LEASES/`, and
`T_PROCESS_RECORDS/`, and performs every §3-template transaction. Fake
clock/meter/world types are test-only and never importable by any production-
graph module."

---

## E. Gate and negative authorization

This is a REVISE. After R1–R12 are applied, one bounded confirmation of the
repairs (per the simplified §12 cadence) plus Sol's independent Y-line acceptance
would authorize **only** Kirill's later contract signature
(`I_ACCEPT_OFFICINA_GENERIC_HARNESS_CONTRACT`). This review authorizes **no**
implementation, no `generic_harness.py`, no CLI, no `runtime_control/` or
manifest, no activation authorization or activation, no capability issuance, no
world/learner/entropy, no candidate or draft-manifest instance, no E1/E2/E3
spend, no runtime/Q/C datum, and no scientific specification, lock, escrow,
outcome, or claim movement. No implementation hash, reviewed HEAD, or production
source set is pinned here.

T remains `NOT_ACTIVATED` at genesis; the predecessor line remains immutable,
`OPEN`, and `BLOCKED_LEVEL1_FEASIBILITY`; T and Q remain permanently non-citable
for C1–C6; only a valid, independently locked C execution may ever move an
Officina claim. No prediction is made that any learner will qualify or that
Philosophia will be proved, falsified, or bounded; the programme claim remains
`OPEN`.

— Opus 4.8, X-line. No scientific outcome is asserted or predicted in this
document.
