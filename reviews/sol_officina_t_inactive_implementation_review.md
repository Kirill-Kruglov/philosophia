REVISE_OFFICINA_T_INACTIVE_SCOPE

# Officina T inactive implementation Y-line review

The implementation is genuinely inactive in the real repository, and it creates no present route to a real T world or learner: the exact-type capability has no issuer. The public invalid-cause enum also correctly excludes learner exception/non-finiteness. The package is not yet a valid implementation of the signed activation/runtime boundary, however. Reproducible failures in activation provenance, active-state verification, concurrent-stream accounting, claim/lease linkage, and the pre-WP-6 E2 barrier must be repaired before the separate generic metered-harness gate.

## Critical findings

1. **The global four-stream boundary is not represented by the reservation input.** `reservation_for` treats each element of `live_liabilities_ns` as one live slot (`src/philosophia/officina/runtime.py:181-217`), although one existing multi-stream reservation is represented by one aggregate liability. The probe

   ```text
   live_liabilities_ns=(2,), requested_units=3
   ```

   returned `Reservation(units=3, liability_ns_per_unit=60000000000)`. If the existing aggregate belongs to two shortened streams, five live behavior-capable streams have been admitted. The 240-device-second check does not repair this near a shortened boundary. This violates the one-unit-per-simultaneous-stream rule in v2.1 section 2.

   **Mandatory repair R1:** Replace bare live-liability integers with a closed typed live-reservation object carrying at least `units`, `liability_ns_per_unit`, and checked aggregate liability. Sum live `units`, not records; reject total live units above four; and rederive aggregate liability from the typed fields. Test mixed one-/multi-stream reservations at ordinary and shortened E1/E3 boundaries, including five streams whose aggregate liability is below 240 seconds.

2. **Activation provenance is not closed over tracked reviewed bytes or the authorization HEAD.** `_preflight_git` checks only that the authorization is tracked and that Git reports no reviewed-path diff (`src/philosophia/officina/activation.py:216-235`). Git ignores an untracked reviewed path. In a disposable mirror I added an untracked `external_behavior.py` to `reviewed_source_paths` and its hash map; `activation_preflight` accepted it. I also added and committed an unrelated file after the authorization commit; preflight accepted that non-HEAD authorization. This contradicts v1 sections 3 and 6.

   The governing/protocol maps are merely required to be nonempty (`activation.py:145-155,184-185`), so the driver does not enforce v1 section 1's exact six governing pins or the accepted protocol chain. The selected envelope/device tokens are also accepted as arbitrary nonempty strings (`activation.py:193-195`). Finally, the required generic harness is reviewed but is omitted from `IMMUTABLE_CONTROL_PATHS` and therefore from the activation record's immutable-control map (`activation.py:55-70,179-185,384-386`), contrary to v2 section A.

   **Mandatory repair R2:** Require the authorization's introducing/modifying commit to equal current `HEAD`; require every reviewed, governing, and protocol path to be a tracked regular nonsymlink file present at the reviewed/current commit as applicable; require the exact signed governing/protocol path sets and exact selected tokens; and reject untracked or path-aliased reviewed bytes. Add the reviewed generic harness and active verifier to the exact immutable-control set, and require every process claim's immutable map to equal the activation record's complete map. Add disposable-mirror tests for the two reproduced cases and for missing/substituted governing pins.

3. **The active verifier is both fail-open on mutation and incompatible with an evolving valid ledger.** With a completed disposable-mirror activation, I changed `device_hour_cap` from 168 to 999 in the working tree and updated only the activation record's envelope hash. `verify_active_repository(..., require_activation_commit=True)` returned `[]`. The verifier checks an empty index but not a clean worktree/current-HEAD identity (`activation.py:493-502`), validates only the active envelope's schema and `activated` flag (`activation.py:447-448`), and does not rederive the record/claim cross-links.

   Conversely, appending one structurally valid `T_PROCESS_STARTED` event caused the verifier to report `activation record ledger_head_sha256 differs`, because it compares the activation-era head hash to the current mutable head (`activation.py:479-488`). A valid runtime therefore cannot evolve under this verifier without rewriting the immutable activation record.

   **Mandatory repair R3:** At the activation-commit boundary, require the exact six-path commit, current clean tracked worktree/index, and byte identity to that commit. Fully validate and cross-link authorization, claim, signed envelope values, activation record, activation entry, state, and immutable controls. Treat the activation record's head as a historical one-entry chain anchor and prove that the current externally headed ledger descends from it; do not compare that historical hash to the current head file. Define a separate active-runtime cleanliness rule permitting only the exact open-transaction paths under verified ownership.

4. **E2 is not mechanically unavailable before WP-6.** An activated `TState` exposes a public `register_candidate` transition that immediately adds a candidate ID (`src/philosophia/officina/accounting.py:126-139`), and `exhausted` already treats that count as E2 (`accounting.py:141-145`). The in-memory probe accepted `"a" * 64`. No durable caller exists yet, but the activation/runtime package makes the state transition callable before the separately signed WP-6 registry exists. This violates v1 section 9 and v2 section G's sole-route rule.

   **Mandatory repair R4:** Make candidate mutation require an exact, unforgeable WP-6 registry authority that does not exist in this package, or replace the public transition with a fail-closed stub until WP-6 installs its reviewed transaction. Activation/runtime tests must prove that no state or ledger transition can change `candidate_ids` and that E2 cannot contribute an exhaustion event.

## Major findings

5. **Claim, lease, reservation, and final-record linkage is incomplete.** `validate_active_lease` checks positive fields but not

   ```text
   outstanding_liability_ns == device_units * (heartbeat_deadline_ns - last_charged_reading_ns)
   ```

   (`runtime.py:407-428`). `build_process_record` requires only equal `process_id` between claim and lease (`runtime.py:466-525`). Because controller PID, controller-start identity, process-group ID, timestamps, start cursor, and immutable-control map are not in that ID, I changed an issued lease's `controller_pid` from 100 to 999 and still obtained `VALID_PROCESS_RECORD`. The supplied `claim_sha256` is format-checked but never recomputed from the claim.

   **Mandatory repair R5:** Require the lease's embedded claim projection to be byte-exact to the durable claim; recompute `process_claim_sha256`; enforce the liability/deadline equation and all exact field types/timestamp order; and bind the final record to the final settled lease, charge event, and post-state. Process-ID/sequence nonreuse, boot/current-clock comparison, and process/lease file ancestry must be enforced transactionally by the future harness, but these pure validators must not accept contradictory inputs.

6. **The signed validity-first ledger contract is not enforced.** The active verifier only checks that a state-bearing event has a key named `t_state`; it neither parses every post-state nor rejects `t_state` on `T_PROCESS_STARTED` (`activation.py:455-474`). It has no closed event-payload validators and no recursive scientific-field rejection, so a hash-valid ledger can carry prohibited scientific keys despite v2 section E. `reject_scientific_fields` itself omits named forbidden concepts including `pass`, `fail`, `INSUFFICIENT`, `equivalence`, and `boundary` (`runtime.py:54-71,585-597`); current exact claim/lease/record schemas happen to reject extra keys, but arbitrary ledger payloads do not.

   Runtime invalidity is also only a record validator. The activation failure handler durably creates a standalone invalidity record (`activation.py:270-293,419-422`) and, even after `T_ACTIVATED` exists, never appends the required hash-bound, full-post-state `T_RUNTIME_INVALID` event. No record-before-event runtime-invalidity transaction exists.

   **Mandatory repair R6:** Add exact payload validators for all nine events; parse a complete `TState` in every state-bearing event; prohibit `t_state` on `T_PROCESS_STARTED`; recursively reject every signed forbidden scientific/reporting concept; and implement the v2.1 record-first, hash-bound `T_RUNTIME_INVALID` event and cache post-state for every post-activation invalidity. Preserve v1's distinct fail-closed recovery treatment for failures before a valid `T_ACTIVATED` anchor, and test every activation failure step without inventing completion or retry.

7. **The static production/test boundary is not a call-graph proof.** `verify_production_boundary` scans only explicitly supplied files and literal AST names/attributes (`src/philosophia/officina/verification.py:195-224`). It returned `[]` for a reviewed behavior source that resolved `evaluate_test_query` through `getattr(w, "evaluate_" + "test_query")`; omitted transitive source paths are not discovered. The stricter bootstrap quarantine helps for modules physically under `src/philosophia/officina`, but does not establish closure for adaptive behavior/config modules elsewhere. Therefore the implementation document's statement that the boundary rejects test-world capability symbols (`successor/officina/T_ACTIVATION_IMPLEMENTATION.md:21`) is too broad.

   **Mandatory repair R7:** Before activation can be eligible, the generic-harness package must install a complete reviewed production source/call-graph manifest, reject omitted or untracked transitive code, and apply alias/reflective/dynamic-source rejection to every production-reachable module. Every capability issue/use and behavior admission must revalidate that manifest and the immutable pins. Until then, describe this function only as a direct-symbol lint, not proof of the functional E1 boundary.

## Minor findings

8. `validate_process_record` does not validate `process_sequence`, `device_units`, device identity, or UTC fields beyond fields copied by its builder (`runtime.py:528-554`). R5's closed-validator repair should cover these types and ranges explicitly, including bool-as-int rejection.

9. The implementation document should distinguish implemented pure constructors/validators from absent runtime transactions. At present, process start and lease installation, heartbeat settlement/renewal, deadline revocation, process-loss reconciliation, invalidity record/event, E1 exhaustion, E3 due/review, pause/resume, voluntary stop, author stop, and archival transactions are unimplemented. Their enums and record builders are not evidence that those terminal branches are complete.

## Direct answers to the Y-line questions

1. **Functional E1 boundary:** There is no present real-work capability: `RealTCapability` cannot be constructed and `issue_real_t_capability` always refuses (`runtime.py:627-643`). Thus labels, dummy seeds, or temporary paths cannot presently instantiate real T work. The claimed future boundary is not yet fail-closed because reviewed-source tracking/call-graph closure is incomplete; this remains a repair plus generic-harness obligation.

2. **Reservation:** The primitive correctly subtracts charged E1, E3 device time, and aggregate live liability, and it shortens the final positive interval. It does not correctly count live multi-stream units, and it proves nothing about actual process trees, deadline revocation, backend synchronization, timely quiescence, or conservative unknown-interval charge. No 240-second claim is licensed without the future supervisor proving all four timely quiescences.

3. **Invalidity/reporting:** `InvalidCause` is exactly `PROCESS`, `RESOURCE`, `HASH`, `CLOCK`, `FILESYSTEM`; learner exception and non-finiteness are absent. Closed process schemas cannot carry loss/accuracy/competence/censoring/effect/margin/outcome fields as extra keys, but the ledger verifier and generic recursive rejector are incomplete. No public learner-behavior recovery fact is currently created.

4. **Evidence and phase separation:** Activation records are marked non-scientific and no real activation output exists. No breathing result, Q/C entry, or scientific terminal is produced. Nevertheless the callable candidate mutation is an E2 path and the ledger's arbitrary payload surface does not recursively guarantee `scientific_outcome:false`; R4/R6 are required.

5. **Lifecycle:** Atomic file primitives and the held runtime lock are useful, but the total process lifecycle is not implemented. Partial activation is fail-closed against rerun, yet post-anchor invalidity lacks its authoritative ledger pair. Process loss, clock failure, unknown quiescence, resource boundary, voluntary stop, final settlement, E3 review, and pause/recovery remain unimplemented—not valid or complete terminals.

6. **`H_preC`:** No `H_preC` or `selection_scope_id` construction exists in this package. The implemented hashes are lineage facts only and expose no T observation. Adaptive observations therefore cannot presently enter activation, recovery, E3, Q numerics, or C analysis. The future harness/Q contracts must retain that one-way exclusion.

7. **Repository state and verification:** The load-bearing implementation bytes at current HEAD are unchanged from `77c5a63`. After all checks, `T_ENVELOPE.json`, `T_LEDGER.md`, `T_LEDGER.md.head.json`, and the tracked immutable `T_RUNTIME.lock` had no diff; the runtime directory contained only that lock. The inactive verifier passed and the active verifier refused for absent authorization, as required.

8. **Next gate:** The generic metered-harness gate may not begin as an accepted downstream gate yet. Bounded repair and focused X/Y confirmation of R1-R7 must come first. After that confirmation, the separately reviewed harness must add: independent whole-process-tree supervision; exact per-stream admission and global reconciliation; watchdog deadline revocation; CPU/off-CPU backend synchronization and positive quiescence proof; full actual late charge or conservative all-remaining-E1 charge when cessation/time is unknown; atomic record-before-ledger invalidity; settlement before release of oracle answers, update completion, checkpoints, close, recovery, or new work; and a complete forbidden-test-source call graph. It must select no learner, device, stack, candidate, metric, or scientific threshold.

## Checks run

- `.venv/bin/python -m pytest -q tests/test_officina_activation.py tests/test_officina_runtime.py` — **15 passed**.
- `.venv/bin/python -m pytest -q` — **251 passed**.
- `.venv/bin/python scripts/verify_inheritance.py` — **OK, 71 inherited files**.
- `.venv/bin/python scripts/verify_all.py` — **VALID** for both admitted scientific decisions.
- `.venv/bin/python scripts/verify_officina_wp12.py` — **OK**, inactive/quarantined.
- `.venv/bin/python scripts/verify_officina_active.py` — expected **FAIL** because the activation authorization is absent.
- Read-only/disposable probes reproduced the five-stream reservation, mismatched claim/lease final record, pre-WP-6 candidate mutation, dirty self-rehashed active-envelope acceptance, non-HEAD authorization acceptance, untracked reviewed-source acceptance, reflective test-symbol false negative, and evolving-ledger head mismatch described above.

The passing committed tests do not cover these load-bearing counterexamples.

## Negative space

This review authorizes only bounded repair of R1-R7 and a focused confirmation. It does not authorize a generic harness package yet, an activation candidate, authorization, activation, runtime output, capability, process, lease, real world, learner, oracle contact, checkpoint, candidate or registration, breathing check, E1/E2/E3 spend, entropy, Q/C activity, lock or escrow, datum, outcome, scientific terminal, `H_preC` use, selection input, or claim movement. No such object or event was created in the real repository; all positive activation and runtime constructor probes were confined to disposable temporary mirrors or in-memory non-production values. No scientific outcome or programme prediction is made.
