# Opus 4.8 X-line — Officina T activation protocol v2 confirmation

**`READY_FOR_OFFICINA_T_ACTIVATION_IMPLEMENTATION`**

Reviewer: Opus 4.8 (X-line, bounded v2 confirmation). Repository:
`/home/master/llm_projects/philosophia`. **I implemented and activated nothing;
created no authorization artifact, runtime artifact, real world, lease, learner,
candidate, entropy, Q/C object, datum, or outcome; no E1/E2/E3 spend occurred. T
is pristine and `NOT_ACTIVATED` (`activated:false`, ledger at genesis, no
`runtime/` directory). Nothing committed; no existing file edited.**

v1 P-1..P-7 (and Sol R1..R7) are closed **one-to-one and comprehensively**: the
correction pins the durability/commit model, the exact runtime lock, the
state-bearing event set, the held-fd anchors, the `CLOCK_MONOTONIC`/boot
semantics, the active schema and verifier transition, and the literal staged
sets/trailers, plus every runtime schema, key set, disposition, invalid cause,
process/liability contract, and recovery rule. Two independent implementers can
now build the same **inactive** state machine without selecting a deferred cell.
Three Minor wording reconciliations remain and are non-blocking (implementation
must honor them; the implementation review will verify).

---

## One-to-one closure of P-1..P-7

- **P-1 (durability/commit + clean-HEAD) — CLOSED (§B).** Activation commits
  immediately; during an open lease metering artifacts are **working-tree-durable
  and may be dirty** (file + parent `fsync`), with git archival at fixed
  boundaries; the "clean HEAD" check **excludes exactly** the five active runtime
  paths while their lease is verified under the lock, and no source/config/
  manifest/authorization path may be dirty or staged. The exact staged set is
  enumerated per boundary (activation / process close / E3 review / pause /
  author-stop-or-exhaustion), each rejecting a nonempty prior index and checking
  order-independent set equality.
- **P-2 (lock mechanism/scope) — CLOSED (§B).** A dedicated
  `runtime/T_RUNTIME.lock`, opened `O_RDWR|O_CLOEXEC|O_NOFOLLOW`, regular-file
  checked, held `flock(LOCK_EX)` across the complete read → anchor-validate →
  verify → append → cache/lease update → fsync → post-verify; "no state is read
  for admission outside this lock."
- **P-3 (state-bearing events) — CLOSED (§C).** Exactly eight state-bearing events
  enumerated (`T_ACTIVATED`, `T_DEVICE_TIME_CHARGED`, `T_REVIEW_COMPLETED`,
  `T_OPERATIONAL_PAUSE`, `T_PROCESS_STOPPED`, `T_RUNTIME_INVALID`, `T_AUTHOR_STOP`,
  `T_ENVELOPE_EXHAUSTED`); `T_PROCESS_STARTED` non-state-bearing; the cache must
  equal the last state-bearing event and no other event may carry/advance
  `t_state`.
- **P-4 (held-fd anchors) — CLOSED (§B).** The runtime dir, ledger, head, state
  cache, process claim, active lease, and process record use the WP-4
  held-descriptor `samestat` discipline; the descriptor opened by ledger append
  must equal the held ledger anchor; atomic head/state successors are opened and
  verified before prior anchors are released; pathname hashes / recyclable inode
  tuples are declared insufficient.
- **P-5 (clock) — CLOSED (§D).** UTC = `datetime.now(timezone.utc)` in canonical
  whole seconds, never preceding activation/last-review/last-ledger; elapsed work
  = `time.clock_gettime_ns(CLOCK_MONOTONIC)` (excludes suspend); boot identity
  from `/proc/sys/kernel/random/boot_id` stored per lease; **a lease cannot span
  reboot/power-off**, and missing/changed boot id, unavailable clock, or a
  non-increasing cursor invokes the outstanding-liability rule.
- **P-6 (active schema + verifier transition) — CLOSED (§C).** Active envelope
  schema `philosophia.officina.t-envelope-active.v1` (inactive fields + `activated
  =true`, `activated_utc`, resource values byte-equal); activation supersedes
  `verify_officina_wp12.py` for the real tree (which must then refuse
  `ACTIVE_TREE_REQUIRES_ACTIVE_VERIFIER`), with `verify_officina_active.py`
  governing.
- **P-7 (staged sets + trailers) — CLOSED (§B).** The per-boundary staged sets are
  literal and the three exact `Co-Authored-By` trailers are given.

## Attack on the new mechanisms

- **60 s × 4 liability — sound (§D).** `HEARTBEAT_LIABILITY_SECONDS=60`,
  `MAX_CONCURRENT_LEASES=4`, `DEVICE_UNITS_PER_LEASE=1`,
  `MAX_AGGREGATE_LIABILITY_DEVICE_SECONDS=240`, amendment-locked and not
  outcome-tunable. Each capability issue/renew **reserves** the lease's 60
  device-seconds and refuses if charged-E1 + live liabilities would exceed 168
  device-hours, or E1-since-last-E3 + liabilities would exceed 40 device-hours, or
  a fifth concurrent lease. A heartbeat settles the actual cursor delta and renews
  the liability; a missed deadline / process loss / reboot / clock ambiguity
  charges the **full** 60 device-seconds (never zero) before any recovery; the
  crossing charge is retained. This never under-charges and bounds overshoot by
  the aggregate liability — a conservative, single-valued model.
- **Process-tree/device identity — sound (§D).** One lease = one behavior-capable
  controller **process tree**, one device-unit, additive across ≤4 trees; the
  process id is SHA-256 over the activation-record hash, monotone sequence, exact
  behavior-source/config/stack/numerical-mode hashes, argv, device identity, and
  boot id (never reused); every child must stay in the one declared process group
  under the same lease, checked at every admission; any behavior-relevant change
  closes-and-fully-charges the lease and requires a new claim.
- **Atomic head/state handoff — sound (§B).** New anchors opened and verified
  before old released — the confirmed WP-4 pattern extended to state/lease/all
  runtime artifacts.
- **Failure/recovery — sound (§F).** Recovery packets carry only filesystem/clock/
  lease/charge/hash/process-validity facts (learner observations/tuning metrics
  unavailable); recovery cannot delete/reuse a claim or process id, erase charge,
  reset E3, change constants, or resume before every outstanding liability and
  state/ledger discrepancy is reconciled; pre-claim failure consumes the one
  invocation and needs a new bounded disposition + newly committed one-shot
  authorization (no standing retry).
- **Capability issuance — sound (§A/§D).** Production activation/learner sources
  may not import/call/receive/reflectively-resolve the WP-4 test-only symbols, and
  the source verifier rejects them in every production call graph — walling the
  test-only oracle path off from production. The 12-file immutable runtime-control
  allowlist is hash-pinned in the activation record and revalidated at every claim/
  issue/use/heartbeat/admission/close ("a clean HEAD is necessary but
  insufficient"); the generic learner harness and active verifier are added only
  by the final authorization after their own review.
- **Deferred-cell discipline — clean.** No WP-6 scientific numeric is chosen (§G
  defers Q numerics, breathing-check, E2, and the generic harness to separate
  review; draft manifests are `unregistered`/`q_ineligible`/order-free;
  `H_preC`/`selection_scope_id` take only conditioning/lineage hashes, never
  evidence). The liability constants are activation-runtime engineering constants,
  not learner/Q numerics, and are amendment-locked.

## Minor wording reconciliations (non-blocking; implementation must honor)

- **V2-m1 — reconcile `T_INVALID_CLOCK` with the authoritative event set.** §D
  names a clock rollback/disagreement "`T_INVALID_CLOCK`," but §C's state-bearing
  list has `T_RUNTIME_INVALID` and §E's causes include `CLOCK`. State explicitly
  that a clock failure is a `T_RUNTIME_INVALID` event with `invalid_cause=CLOCK`
  (and its `t-runtime-invalidity.v1` record), so no implementer mints a distinct
  `T_INVALID_CLOCK` ledger event.
- **V2-m2 — declare the complete, closed production ledger-event vocabulary.** §C
  fixes the state-bearing eight and marks `T_PROCESS_STARTED` non-state-bearing;
  state that these **nine** are the complete production event set (no other ledger
  event exists), so the vocabulary is closed, not merely "no other is
  state-bearing."
- **V2-m3 — clarify the `T_RUNTIME_INVALID` event vs the `t-runtime-invalidity.v1`
  record relationship** (both required at an invalidity; the ledger event is the
  state-bearing marker, the record the detailed artifact; which is authority for
  the required-action route).

None of these changes a schema, event, durability point, or lock rule; they align
prose with the authoritative §C/§D/§E enumerations and would resolve identically
in a careful implementation.

## Eligible surface

A positive verdict authorizes **inactive implementation and disposable-mirror
tests only**: the activation driver, the metered-runtime state-machine library
(transaction sequencer, `T_RUNTIME.lock` + held-fd-anchor primitives, the
process-claim/lease/charge/liability/E3/pause/author-stop transitions, the
`verify_officina_active.py` active-state verifier, a **disabled** generic
learner/world interface), and the §10 test matrix — with **no** production
authorization JSON, activation output, real lease/world, concrete learner adapter,
candidate registration, breathing qualification, Q/C root, entropy, E1/E2/E3
spend, or scientific field. Implementation then needs its own X/Y review; the
generic metered harness needs a separate bounded review; only afterward may an
exact activation-authorization candidate be prepared for Kirill's explicit
`I_AUTHORIZE_OFFICINA_T_ACTIVATION`, before the driver runs exactly once.

## Negative space

No token authorizes activation, and none is signable from this correction. The
predecessor line remains immutable, `OPEN`, and `BLOCKED_LEVEL1_FEASIBILITY`; its
records are non-citable and chose no value here. Officina's T and Q are permanently
non-citable for C1–C6; activation, leases, tuning observations, breathing checks,
draft manifests, E3 reviews, and every T ending are non-scientific and move no
claim; a future Q pass is a spendability gate fact only; S is unavailable; only a
valid, independently locked C execution may ever move an Officina claim, within its
selection-conditional, selected-frame, orientation, device, and learner-seed scope.
Censored/`UNKNOWN`/every invalid state are never success, equivalence, a boundary,
or learner impossibility. `PROOF_CORE`/`PROOF_STRONG` remain earned by nothing; the
programme claim stays `OPEN`.

I edited no existing file, created exactly one new file (this confirmation),
authorized nothing, activated no T state, and committed nothing. `essay/OUTLINE.md`
untouched. My actions were reading the correction and confirming the pristine T
state and the P-1..P-7 closures above.

— Opus 4.8, X-line. No outcome is asserted or predicted in this document.
