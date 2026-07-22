REVISE_OFFICINA_T_INACTIVE_REPAIR

# Officina T inactive repair Y-line confirmation

The bounded repair closes R1, R3, and R6, substantially closes R2/R5/R7, and accurately labels the remaining runtime objects as pure validators rather than completed transactions. It does not close the complete R1-R7 mandate. Four reproducible residuals remain: governing/protocol files need not exist at the reviewed commit; an active `TState` can still be directly constructed with E2 registrations; the public final-record composition accepts contradictory settlement/validity semantics and can skip activation-control validation; and the production graph accepts an omitted repository-local dependency outside `philosophia.officina`.

## Critical findings

1. **R4 remains open: pre-WP-6 E2 is still representable and can drive `exhausted()`.** `register_candidate` now always refuses (`src/philosophia/officina/accounting.py:126-130`), and the active repository verifier rejects a persisted nonempty candidate list (`src/philosophia/officina/activation.py:663-670`). But `TState.__post_init__` still accepts nonempty `candidate_ids` in an active state, while `TState.exhausted()` still treats their count as E2 exhaustion (`accounting.py:63-105,132-136`). The exact replay constructed an active state with 12 candidate IDs; it returned `exhausted=True`, and `reservation_for` still admitted a one-unit reservation.

   **Mandatory repair C1:** While WP-6 is absent, reject every nonempty `candidate_ids` value in `TState.__post_init__`/`from_mapping`, and make `TState.exhausted()` depend only on the E1 device-time cap. Retain the field as an exactly empty schema placeholder if needed. Add constructor, `from_mapping`, `exhausted`, reservation, and event-verifier tests proving that no callable pre-WP-6 path can create or interpret E2 consumption.

2. **R5 remains open: final-record validity is not coupled to the settlement event, and activation-control validation is optional.** `validate_active_lease_against_claim` correctly rejects the original controller-PID substitution and `validate_active_lease` enforces the liability equation. But `build_process_record` accepts either `T_DEVICE_TIME_CHARGED` or `T_RUNTIME_INVALID` without coupling the event kind to `ProcessDisposition`/`invalid_cause` (`src/philosophia/officina/runtime.py:567-640`). Two exact probes succeeded:

   - a `T_RUNTIME_INVALID` event produced `VALID_PROCESS_RECORD` with `T_PROCESS_CLOSED`;
   - an ordinary `T_DEVICE_TIME_CHARGED` event produced `INVALID_PROCESS_RECORD` with `T_PROCESS_INVALID:CLOCK`.

   In addition, `validate_process_claim_against_activation` is a separate optional function (`runtime.py:447-464`); `build_active_lease` and `build_process_record` accept a claim carrying any nonempty syntactically valid immutable-control map. The committed round-trip test itself uses `{"control.py": ...}` rather than the activation record's exact map.

   **Mandatory repair C2:** Make the public composition path require an activation-validated claim (or require the exact activation-record hash and immutable-control map and invoke the validator internally). A valid process close must be backed by the exact permitted settlement event for that disposition. An invalid close must require the corresponding typed invalidity record/event and matching public cause in addition to a process-specific settled charge; it may not turn a generic runtime invalidity into a valid close or an ordinary charge into invalidity. Bind process ID, lease hash, post-state, event ancestry, and cause through one closed validator. Add both reproduced cross-kind probes and an arbitrary-control-map probe.

## Major findings

3. **R2 is incomplete at the reviewed-commit provenance boundary.** Authorization-last-modified-at-HEAD, tracked regular nonsymlink single-link in-repository paths, exact six governing hashes, exact protocol hashes, exact tokens, untracked source refusal, hard-link refusal, generic harness, active verifier, and manifest pins are all implemented (`src/philosophia/officina/activation.py:228-342`). The original untracked-source, later-unrelated-commit, hard-link, missing-pin, and self-rehashed-governing counterexamples now refuse.

   However, the `git cat-file` presence check at `reviewed_code_head` applies only to `reviewed_source_paths` (`activation.py:333-341`), not `GOVERNING_PATHS` or `PROTOCOL_PATHS`. In a disposable mirror I committed a reviewed HEAD with one governing file absent, restored the exact file in the later authorization commit, pointed `reviewed_code_head` at the deficient commit, and `activation_preflight` accepted it.

   **Mandatory repair C3:** Apply the reviewed-commit tracked-blob/presence check to the union of reviewed source, exact governing, and exact protocol paths. Add the reproduced remove-at-reviewed-HEAD/restore-at-authorization test for both a governing and a protocol path.

4. **R7 is incomplete: the manifest checker does not compute a closed repository-local graph.** The implementation note now correctly calls the old surface a direct-symbol lint and withholds the complete E1 claim (`successor/officina/T_ACTIVATION_IMPLEMENTATION.md:21-24`). The real tree contains neither generic harness nor production manifest, so activation remains blocked. The exact constructed `getattr(w, "evaluate_" + "test_query")` case now refuses for dynamic resolution, omitted `world.py`, and absent manifest.

   But dependency extraction recognizes only imports beginning with `philosophia.officina` (`src/philosophia/officina/verification.py:231-277`), and `reachable_sources` is compared to every reviewed Python path rather than graph reachability from the declared roots (`verification.py:279-304`). In a disposable mirror, a reviewed external `behavior.py` imported tracked repository-local `local_helper.py`; the helper was omitted from the reviewed set/manifest and directly referenced `evaluate_test_query`. `activation_preflight` accepted the graph.

   **Mandatory repair C4:** Resolve every import against canonical repository/module search roots; if it resolves to repository-local source, require that canonical file in the reviewed set and import-edge map. Compute reachability from the declared executable roots rather than equating reachability with all reviewed Python files; reject unreachable asserted sources, undeclared executable roots, ambiguous resolution, and omitted local dependencies. Apply the dynamic/entropy/test-surface quarantine to every reachable source. Add the reproduced external-module/helper case without executing either source.

## Minor findings

No additional scientific or statistical cell is open. The four repairs above are mechanical governance/dataflow corrections. The no-op expressions at the end of `tests/test_officina_activation.py` are harmless but may be removed as test cleanup without broadening this repair.

## Closure of R1-R7

| Finding | Disposition | Confirmation |
|---|---|---|
| R1 typed live reservations | **Closed** | Exact `Reservation` objects are required; live units are summed. `Reservation(2,1)` plus three requested units refused. Aggregate liability is derived, and simultaneous E1/E3 zero routes deterministically to `E1_EXHAUSTED` first. |
| R2 durable provenance | **Partial — C3 required** | All originally reproduced mutation/alias/HEAD counterexamples refuse, and exact pins/tokens are present. Governing/protocol presence at reviewed HEAD is not enforced. |
| R3 active re-derivation | **Closed** | The self-rehashed 168-to-999 mutation refuses. The activation head is reconstructed as the historical one-entry anchor. A disposable owned claim+lease plus appended `T_PROCESS_STARTED` verified successfully under `require_activation_commit=True`; dirty paths without validated lease ownership refuse. Exact six paths and trailers are checked. |
| R4 pre-WP-6 E2 barrier | **Open — C1 required** | The mutator refuses and events accept only `resource_axis=E1`, but direct active-state construction and `exhausted()` still represent E2. |
| R5 claim/lease/final record | **Partial — C2 required** | PID substitution, contradictory liability, claim hash, lease projection, state, process ID, bool/int, and time-range checks are repaired. Settlement-event/disposition coupling and mandatory activation-control composition are not. Durable ledger membership remains a future transaction obligation and is not claimed by the implementation note. |
| R6 validity-first events | **Closed for the inactive event/activation surface** | All nine payloads have closed fields, hashes, recursive scientific rejection, and parsed full post-state where required; `T_PROCESS_STARTED` carries no state. Post-anchor injected failure creates the invalidity record before its hash-bound `T_RUNTIME_INVALID`; pre-anchor failure creates no runtime event and remains on the distinct recovery route. C2 is still needed for process-record composition. |
| R7 production graph | **Partial — C4 required** | Exact `getattr` resolution refuses and the absent canonical manifest blocks the real tree. General repository-local dependency/reachability closure is not implemented. |

The implementation note at `successor/officina/T_ACTIVATION_IMPLEMENTATION.md:32-39` now loudly and correctly distinguishes pure constructors/validators from the absent process-start, lease, watchdog, heartbeat, backend/quiescence, exhaustion, E3, close, stop, and commit transactions. Nothing in this confirmation treats their enums or schemas as executed terminals.

## Checks and counterexamples run

- `.venv/bin/python -m pytest -q tests/test_officina_accounting.py tests/test_officina_activation.py tests/test_officina_runtime.py` — **38 passed**.
- `.venv/bin/python -m pytest -q` — **260 passed**.
- `.venv/bin/python scripts/verify_inheritance.py` — **OK, 71 inherited files**.
- `.venv/bin/python scripts/verify_all.py` — both admitted scientific decisions **VALID**.
- `.venv/bin/python scripts/verify_officina_wp12.py` — **OK**, quarantined and inactive.
- `.venv/bin/python scripts/verify_officina_active.py` — expected **FAIL** because the production authorization is absent.
- `git diff --check 77c5a63..82e265e` — clean.
- Direct read-only/in-memory or disposable-mirror replays covered the shortened five-stream case, simultaneous-zero ordering, untracked reviewed source, later authorization commit, hard link, missing pin, self-rehashed governing mutation, signed-envelope self-rehash, owned evolving-ledger prefix, candidate construction/E2 exhaustion, controller substitution, liability and settlement contradictions, post-/pre-anchor invalidity, exact `getattr` resolution, and omitted local-helper graph.

The load-bearing implementation and test files at current HEAD are byte-identical to `82e265e`. After all tests, the committed `T_ENVELOPE.json`, ledger, external head, and immutable runtime lock were byte-identical to Git; `successor/officina/runtime` contained only `T_RUNTIME.lock`.

## Disposition and negative space

This verdict authorizes only bounded repairs C1-C4 and another focused confirmation. It does not authorize the generic metered-harness gate yet, creation of a production manifest or harness in the real tree, an activation candidate or authorization, activation, runtime output, capability, world, process or lease, learner, candidate registration, breathing check, E1/E2/E3 spend, entropy, Q/C object or execution, lock/escrow, datum, outcome, scientific interpretation, or claim movement.

No production authorization, activation claim/state/record, invalidity, process artifact, manifest, generic harness, real world, learner execution, E1/E2/E3 spend, datum, outcome, or scientific terminal was created. Positive activation and lifecycle probes were confined to disposable temporary Git mirrors or non-persistent in-memory values. The real tree remains pristine and `NOT_ACTIVATED`; no prediction is made.
