REVISE_OFFICINA_T_ACTIVATION_PROTOCOL_V2

# Bounded conclusion

V2 closes R1, R2, R5's scientific-field exclusions, and R7, and it correctly keeps E2/Q/C and actual activation inaccessible. The four-lease liability is globally additive on paper. It is not yet a durable upper bound on real-T work, however, because deadline handling revokes capability without mechanically quiescing the behavior-capable process tree. The correction also exposes learner non-finiteness to the recovery decision despite declaring learner observations unavailable, leaves arbitrary behavior-capable child parallelism inside a one-unit lease, and does not give reservation-boundary slack or the new lock file a total state transition. These are bounded protocol defects; no scientific design reopening is required.

# Findings

## Critical

1. **Sixty seconds is not an upper bound unless the complete process tree is durably quiesced.** Section D.280-294 reserves 60 device-seconds per lease and says a watchdog “revokes capability” at the deadline. Capability revocation stops a new oracle admission, but it does not stop a controller or child that already holds T observations from continuing behavior-capable learner computation. It also does not establish when CPU/off-CPU activity actually ceased. The subsequent rule charges exactly the outstanding 60-device-second liability on deadline/process loss. If the process continues for 61 seconds or an hour, E1 is undercharged.

   Likewise, `MAX_AGGREGATE_LIABILITY_DEVICE_SECONDS=240` is a true global bound only if all four trees are mechanically prevented from behavior-capable execution by their respective deadlines. Refusing release of an answer/checkpoint is useful quarantine, but E1 owns active training time itself, not only exported results. The current text therefore retains a free T-compute route after lease expiry and does not close R3.

2. **One unit per process tree permits undeclared parallel behavior-capable work.** Section D.197-200 charges one unit for a controller tree “regardless of CPU/off-CPU backend or physical sharing,” and lines 301-306 allow every child worker to remain under that lease. Nothing restricts the tree to one behavior-capable execution stream. One controller can therefore run multiple concurrent learner/oracle workers while paying one device-unit, contrary to the signed additive-concurrency meaning and R4. Merely placing all workers in one process group establishes custody, not the E1 unit count.

## Major

3. **Recovery can still condition on a learner observation.** Section E.323-325 makes `NONFINITE_DEVELOPMENT` a public exact invalid cause for `T_PROCESS_INVALID`. Section F.338-340 then says recovery packets contain process-validity facts but learner observations are unavailable. Those clauses conflict: the public invalid cause tells the recovery decision that the learner became non-finite. A signed recovery can consequently distinguish an unfavorable learner behavior from a filesystem/process fault. Non-finite development is allowed adaptive T information, but it must remain quarantined and must not control an infrastructure recovery or one-shot disposition.

4. **Reservation refusal is not a total E1/E3 state.** Section D.280-285 refuses renewal when a full 60-second liability would cross E1 or the 40-device-hour E3 threshold, and accepts that less than 60 seconds may remain unused. It does not say what state owns that remainder. At E1, actual charge is below 168 hours, so section E.326 does not license `T_ENVELOPE_EXHAUSTED`; no later lease can consume the remainder. At E3, actual charge may be below 40 hours, so an early `T_REVIEW_COMPLETED` would improperly reset E3. The protocol needs either a shorter final liability/deadline or an exact nonterminal/terminal forfeit rule that preserves the signed meaning. Silent deadlock is not a total state machine.

5. **The dedicated runtime lock has no authorized creation or path identity.** Section B introduces `successor/officina/runtime/T_RUNTIME.lock`, opened without `O_CREAT`, but it is absent from the exact authorization `canonical_paths` keys in section C.151-154 and from the v1 runtime outputs. If absent, activation cannot acquire it; if newly created, it is an unenumerated activation artifact; if pre-existing, v1's absent-output preflight is ambiguous. Since all concurrent liability correctness depends on this lock, its immutable lifetime and canonical identity must be explicit.

## Minor

None.

# R1-R7 closure table

| Repair | Status | Confirmation |
|---|---|---|
| R1 functional E1/test exclusion | Closed | Section A.13-26 makes ownership functional, limits free tests to fixed nonadaptive assertions, and forbids every WP-4 test-world/contact symbol in production call graphs. |
| R2 immutable controls | Closed | Section A.28-55 gives an exact runtime allowlist, use-time byte verification, disjoint adaptive paths, and reviewed amendment on control changes. |
| R3 durable liability/concurrency | Not closed | Claims, cursors, reservations, global locking, boot identity, and settlement are present, but 60 seconds is not a bound without enforced process-tree quiescence; reservation slack also lacks a terminal. |
| R4 process/stack/device invariants | Not closed | Hashes and mutation refusal are exact, but unlimited behavior-capable workers may share one charged unit. |
| R5 closed T reporting | Closed for scientific semantics | Closed schemas and prohibited scientific fields are exact. `NONFINITE_DEVELOPMENT` must move out of public invalid/recovery facts as the bounded R6 interaction repair below. |
| R6 clock/recovery facts | Not closed | UTC/monotonic/boot and pre-claim rules are exact, but the recovery packet can observe non-finite learner behavior. |
| R7 lineage-only `H_preC` | Closed | Section G.351-359 limits hashes to conditioning/lineage and makes draft manifests unregistered, Q-ineligible, order-free, and nonauthoritative for E2. |

# Exact bounded repairs

R3a. Replace the watchdog/liability sentence with:

> The liability interval is an enforced maximum of behavior-capable execution, not merely a heartbeat target. Every controller tree executes under a supervisor that can durably freeze or terminate the entire declared process group and prevent further CPU/off-CPU learner work. At or before the recorded deadline, the supervisor first establishes quiescence, records the monotonic quiescence reading, revokes oracle/output authority, and settles actual charge through that reading. A capability refusal alone is not quiescence. If timely quiescence cannot be proven, 60 seconds ceases to be an upper bound: recovery charges at least the actual interval through verified quiescence, or, when that interval is unknowable, conservatively consumes the remaining lease-eligible E1 rather than charging a fixed 60 seconds. No work or recovery resumes until this charge is durable.

Add implementation tests in disposable mirrors where a controller and child ignore heartbeat, retain a prior T response, continue computation, resist normal termination, and cross the deadline. The supervisor must prevent further behavior-capable execution or route to the conservative unknown-interval charge; `240` may be asserted as the maximum only when all four quiescence proofs succeed.

R4. Add one exact ownership rule, without choosing a learner or device:

> A one-unit lease admits exactly one concurrent behavior-capable execution stream. Child processes may perform behavior-inert orchestration, storage, and communication under that lease, but any child that independently queries a T world, evaluates/trains a learner, or creates a behavior-bearing checkpoint is another behavior-capable unit and requires its own liability and concurrent slot. Alternatively, an explicitly declared multi-unit tree consumes one unit per simultaneous behavior-capable stream; the aggregate remains capped at four. Process-group membership never collapses multiple active streams into one E1 unit.

R6. Remove `NONFINITE_DEVELOPMENT` from the public invalid-cause enum and recovery inputs. Replace it with:

> Learner exception or non-finiteness is quarantined adaptive T information. Public process closure uses a generic valid development-stop disposition with no learner-behavior cause, after full E1 settlement. It is not runtime invalidity, censoring, competence failure, or learner impossibility and invokes no infrastructure recovery. Detailed learner behavior remains only in dev-non-citable quarantine and is unavailable to recovery, E3, breathing, Q numerics, and C.

R3b. Make the reservation boundary total by choosing one pre-T engineering rule in the protocol. The smallest rule is:

> A lease's final liability is `min(60 seconds, positive E1 time remaining, positive E3-device time remaining)` and its watchdog deadline is shortened to that exact liability. Zero remaining liability routes to actual E1 exhaustion or actual E3 due as appropriate. Reservation refusal alone never sets exhaustion, completes an early E3 review, or silently strands state.

This changes no numeric envelope, scientific cell, or result-dependent choice.

R3c. Either return to v1's already named locked runtime-directory descriptor, or add `runtime_lock` to the exact canonical-path schemas and state:

> `T_RUNTIME.lock` is a tracked, immutable, non-state-bearing infrastructure file created only by the reviewed inactive implementation. Its canonical path and hash are in the authorization, activation claim, and activation record; it is permitted by pristine preflight, never deleted/replaced, and opened/anchored before any activation or runtime read. It is not an activation output or scientific artifact.

# Confirmed boundaries

E2 remains mechanically absent: pre-WP-6 drafts are unregistered, Q-ineligible, and order-free, and only the future WP-6 registry may recompute identity and charge E2. No Q attempt, competence predicate, entropy, Q root, promotion, C root, lock, estimator, or C1-C6 field is authorized or created by v2.

T reporting is otherwise validity-first and non-scientific. Valid T closure proves only process/resource history; it cannot establish learner competence, construct difficulty, censoring, `INSUFFICIENT`, efficacy, an arm ordering, programme evidence, or falsification. `H_preC` and `selection_scope_id` carry hashes solely to identify the adaptive history conditioned on, never as analysis inputs.

Actual activation remains correctly blocked by section G.361-366 until a concrete generic metered harness and its complete oracle, subprocess, device, update, checkpoint, watchdog/quiescence, and test-surface call graph receive separate bounded X/Y review. That review chooses no learner, optimizer, stack, candidate, or expected result.

# Gate and negative space

This verdict authorizes only the bounded protocol corrections above and another focused confirmation. It does not authorize inactive implementation yet.

I performed only read-only inspection. T remains pristine and `NOT_ACTIVATED`. I created no code, authorization artifact, activation claim/state/record, runtime lock or other runtime artifact, capability, lease, process, real world, learner, checkpoint, draft manifest, candidate, registration, E1/E2/E3 spend, breathing check, entropy, Q/C object, lock, escrow, datum, outcome, terminal, or claim movement. No qualification, contrast direction, competence, or programme success is predicted.
