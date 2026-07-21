# Opus 4.8 X-line — Officina T activation protocol v2.1 final confirmation

**`READY_FOR_OFFICINA_T_ACTIVATION_IMPLEMENTATION`**

Reviewer: Opus 4.8 (X-line, final bounded confirmation). Repository:
`/home/master/llm_projects/philosophia`. **I edited/committed/implemented/activated
nothing; created no authorization, runtime artifact, world, lease, learner,
candidate, entropy, Q/C object, datum, or outcome; no spend occurred. T is pristine
and `NOT_ACTIVATED` (`activated:false`, ledger genesis, no `runtime/` directory).**

v2.1 closes Sol's five bounded repairs and my three wording reconciliations
one-to-one; it changes no scientific cell, envelope numeric, or phase boundary,
reopens no accepted cell, and introduces no new implementer ambiguity in the
**inactive** state machine. Two independent implementers can build the same
inactive activation/runtime state machine; the behavior-capable quiescence and
stream-reconciliation enforcement is correctly deferred (with its rule pinned) to
the separately reviewed generic metered harness.

---

## Closure of the eight items

1. **Actual quiescence (§1) — CLOSED.** The liability interval is an **enforced
   maximum**, not a heartbeat target. At/before the deadline a per-tree supervisor
   must revoke authority, freeze/terminate every group member, **synchronize the
   backend** (submitted work complete or cancelled), **prove quiescence** from
   group membership + process states + backend-sync result + monotonic reading +
   unchanged boot id, and **durably settle actual E1 through that quiescence
   reading before any result/checkpoint/close/recovery/new work** — "capability
   refusal alone is not quiescence." Later-but-known → charge the full actual
   interval; unknowable → conservatively consume all remaining lease-eligible E1;
   the 240-device-second aggregate bound is assertable only with four timely
   quiescence proofs. The inactive harness must test controllers/children that
   ignore heartbeat, retain a response, keep computing, resist termination, and
   cross the deadline; a backend without a reviewed testable quiescence adapter is
   ineligible. This closes the runaway-behavior-past-deadline gap; capability
   revocation no longer stands in for actual work cessation.

2. **Stream accounting (§2) — CLOSED.** One device-unit = **one concurrent
   behavior-capable execution stream**, not one process tree. Behavior-inert
   children (orchestration/storage/comms) share the unit; any child that
   independently queries/evaluates/trains/updates/checkpoints is another stream
   needing its own liability and slot; a multi-stream controller consumes one unit
   per simultaneous stream, total ≤ 4; "process-group membership never collapses
   multiple streams into one unit," and excess/unclassifiable parallelism revokes
   the group and invokes the conservative unknown-interval charge. This closes the
   parallel-worker under-metering.

3. **Non-finite quarantine (§3) — CLOSED.** `NONFINITE_DEVELOPMENT` is removed from
   the public invalid-cause enum (public causes are exactly `PROCESS`, `RESOURCE`,
   `HASH`, `CLOCK`, `FILESYSTEM`). A learner exception/non-finiteness is quarantined
   adaptive T information; public closure is `T_PROCESS_VOLUNTARY_STOP` after full
   E1 settlement, carrying no learner-behavior cause or metric, and is **not**
   runtime invalidity, censoring, competence failure, or learner impossibility,
   invoking no infrastructure recovery. Detailed learner behavior stays only in the
   dev-non-citable quarantine, unavailable to recovery/E3/breathing/Q/C. This keeps
   learner behavior out of the public runtime surface.

4. **Total final liability (§4) — CLOSED.** The reserved (hence maximum-uncharged)
   interval is `min(60 device-seconds, positive E1 remaining after other live
   liabilities, positive E3-device remaining after other live liabilities)`, with
   the watchdog deadline shortened to that exact positive value — so the reservation
   can never overshoot E1 or the E3-device boundary. Zero-E1 liability appends the
   actual `T_ENVELOPE_EXHAUSTED` state; zero-E3-device liability routes to the
   nonterminal E3-due gate; reservation refusal alone never sets exhaustion,
   completes a review, or strands a remainder; both-zero records exhaustion first
   while preserving E3-due, neither clock resetting the other. A deterministic,
   boundary-respecting rule.

5. **Immutable runtime lock (§5) — CLOSED.** `runtime/T_RUNTIME.lock` is a
   **tracked, immutable, non-state-bearing** infrastructure file created only by the
   reviewed inactive implementation, canonical content `OFFICINA_T_RUNTIME_LOCK_V1`,
   path + SHA-256 in the authorization `canonical_paths` (`runtime_lock`) and the
   claim/record immutable-control maps; permitted by pristine preflight, never an
   activation output, never in a staged set, never deleted/replaced/truncated/
   written; every read opens it `O_RDWR|O_CLOEXEC|O_NOFOLLOW`, validates canonical
   path/content/held-descriptor identity, then `flock(LOCK_EX)`. V1's absent-output
   check is scoped to claim/state/record/process artifacts, not this pre-existing
   lock. (It lives in the `runtime/` subdirectory, so it does not disturb the
   top-level `successor/officina/` set the WP-1/WP-2 verifier checks; post-activation
   `verify_officina_active` governs.) This resolves the lock-file lifecycle vs
   pristine-preflight tension.

6. **Nine-event closed vocabulary + `T_INVALID_CLOCK` (§6, my V2-m1/m2) — CLOSED.**
   The complete post-activation production ledger-event vocabulary is exactly the
   nine listed (`T_ACTIVATED`, `T_PROCESS_STARTED`, `T_DEVICE_TIME_CHARGED`,
   `T_REVIEW_COMPLETED`, `T_OPERATIONAL_PAUSE`, `T_PROCESS_STOPPED`,
   `T_RUNTIME_INVALID`, `T_AUTHOR_STOP`, `T_ENVELOPE_EXHAUSTED`); "no tenth event
   exists"; clock failure is `T_RUNTIME_INVALID` with `invalid_cause=CLOCK` and
   "`T_INVALID_CLOCK` is not an event"; pre-activation
   `T_NOT_ACTIVATED_AT_MAINTENANCE` is explicitly outside this vocabulary and cannot
   follow `T_ACTIVATED`.

7. **Invalidity record-before-event authority (§6, my V2-m3) — CLOSED.** Every
   invalidity requires **both** artifacts, in order: first the detailed canonical
   `t-runtime-invalidity.v1` record is durably created, then the state-bearing
   `T_RUNTIME_INVALID` event commits its hash, typed public cause, full post-state,
   and required action; the ledger event is authority that the runtime entered
   fail-closed invalidity, the hash-bound record is authority for recovery inputs,
   and missing/extra/mismatched/reversed-order artifacts are themselves
   unrecoverable without signed bounded disposition.

## Attack on new implementer ambiguity

No new ambiguity in the inactive state machine. The concrete per-backend
**quiescence/synchronization adapter** and the **stream reconciliation** against
observed workers/backend queues are the only under-determined pieces, and both are
explicitly deferred to the separately reviewed generic metered harness (§1, §2,
§7) with their **rules pinned** (revoke → freeze/terminate → backend-sync → prove
from the five inputs → settle-before-anything; one unit per concurrent stream, ≤4,
reconcile at each admission/heartbeat/quiescence, excess → revoke + conservative
charge). The inactive activation/runtime primitives — transaction sequencer,
`T_RUNTIME.lock` + held-fd anchors, the `min()` liability arithmetic, the closed
event vocabulary, the record-before-event invalidity order, and every schema/key
set from v2 — are fully pinned. No accepted cell is reopened: the correction only
replaces the named v2 paragraphs (the liability model and stream unit are Sol's
authorized repairs, not a reopening), and the envelope numerics (168/12/48-or-40)
and phase boundaries are unchanged.

## Eligible surface

A positive final confirmation authorizes **inactive implementation and
disposable-mirror tests only**: the activation driver and metered-runtime
state-machine library (sequencer, lock + anchors, process-claim/lease/stream/
charge/liability/E3/pause/author-stop transitions, `verify_officina_active`, the
tracked `T_RUNTIME.lock`, and a **disabled** generic learner/world interface) plus
the test matrix — with **no** authorization JSON, activation output, real
lease/world/stream, concrete learner adapter, candidate registration, breathing
qualification, Q/C root, entropy, or E1/E2/E3 spend. Implementation then needs its
own X/Y review; the generic metered harness (supervisor, process-tree,
backend-quiescence, watchdog, oracle, update, checkpoint, test-surface call graphs)
needs a separate bounded review; only afterward may an exact activation-
authorization candidate be prepared for Kirill's explicit
`I_AUTHORIZE_OFFICINA_T_ACTIVATION`, before the driver runs exactly once.

## Negative space

No token authorizes activation, and none is signable from this correction. The
predecessor line remains immutable, `OPEN`, and `BLOCKED_LEVEL1_FEASIBILITY`; its
records are non-citable and chose no value here. Officina's T and Q are permanently
non-citable for C1–C6; activation, leases, streams, tuning observations, breathing
checks, draft manifests, E3 reviews, non-finiteness, and every T ending are
non-scientific and move no claim; a future Q pass is a spendability gate fact only;
S is unavailable; only a valid, independently locked C execution may ever move an
Officina claim, within its selection-conditional, selected-frame, orientation,
device, and learner-seed scope. Censored/`UNKNOWN`/every invalid state are never
success, equivalence, a boundary, or learner impossibility. `PROOF_CORE`/
`PROOF_STRONG` remain earned by nothing; the programme claim stays `OPEN`.

I edited no existing file, created exactly one new file (this confirmation),
authorized nothing, activated no T state, and committed nothing. `essay/OUTLINE.md`
untouched. My actions were reading the correction and confirming the pristine T
state and the eight closures above.

— Opus 4.8, X-line. No outcome is asserted or predicted in this document.
