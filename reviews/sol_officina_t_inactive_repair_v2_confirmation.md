REVISE_OFFICINA_T_INACTIVE_REPAIR_V2

The bounded repair closes C1, C2, and C3, and it closes the local-dependency, ambiguity, root, and reachability parts of C4. One reproducible C4 false negative remains: the production-boundary verifier does not reject an entropy primitive that is bound in one reachable local module and called through an imported alias in another. Therefore the generic metered-harness scope/design gate is not yet open.

## Major finding — C4 reachable-source quarantine is incomplete

`verify_production_boundary` computes the closed repository-local graph, but its entropy/dynamic quarantine is limited to resolved `ast.Call` expressions within each individual file (`src/philosophia/officina/verification.py:318-327`). It does not reject a loaded reference such as `draw = os.urandom`, and it does not propagate that binding across a local import edge. The stronger loaded-reference check at `verification.py:187` belongs to the separate bootstrap-source quarantine and is not applied to arbitrary reachable production sources.

I reproduced the following counterexample in a disposable static fixture without importing or executing any inspected source. The manifest contained the exact computed source set and edges from the exact activation root:

```python
# scripts/officina_activate_t.py (the exact root; appended import)
import external_behavior
```

```python
# external_behavior.py
from local_helper import draw
value = draw(32)
```

```python
# local_helper.py
import os
draw = os.urandom
```

The exact graph was `scripts/officina_activate_t.py -> external_behavior.py -> local_helper.py`. `verify_production_boundary(...)` returned an empty failure list. Thus an entropy-bearing helper can be reachable, declared, and graph-complete while passing the quarantine. This directly fails the required C4 condition that entropy routes refuse and that quarantine cover every reachable source. No entropy was generated: the probe parsed source only.

### Minimal bounded correction

For every source in the computed reachable closure, apply the loaded-symbol/reference and statically constructed random-device-path quarantine as well as the existing direct-call quarantine. At minimum, a reference resolving to any member of `ENTROPY_CALLS` or `DYNAMIC_IMPORT_CALLS` must refuse even when it is assigned rather than immediately called. The check must remain static and must not import or execute reviewed source. Add the exact three-file cross-module alias probe above as a regression test. This is a verifier-only closure; it must not add a manifest, harness, entropy source, execution authority, or any WP-3/WP-4/WP-6/WP-9 choice.

## C1-C4 disposition

| Residual | Disposition | Confirmation |
|---|---|---|
| C1 — pre-WP-6 E2 | **Closed** | Direct active `TState` construction and `from_mapping` with nonempty `candidate_ids` refuse at `accounting.py:70-77`; `exhausted()` is E1-only at `accounting.py:136-139`; reservation/exhaustion routing cannot name E2; and `validate_ledger_event` rejects pre-WP-6 E2 exhaustion. Exact E1 exhaustion remains the only signed exhaustion route. |
| C2 — closed process composition | **Closed** | `build_active_lease` and `build_process_record` require the exact activation-record hash and immutable control map (`runtime.py:470-479`, `576-599`). A close requires its process-specific `T_DEVICE_TIME_CHARGED` event and exact process/lease/state linkage (`runtime.py:607-623`). An invalid close additionally requires the immediately following hash-linked `T_RUNTIME_INVALID` and the matching canonical invalidity record, public cause, state, observation time, liability, and activation-bound process identity (`runtime.py:626-660`). Both original valid-as-invalid and invalid-as-valid cross-kind probes now refuse. The signed v1 process-record key set is unchanged. Durable ledger transactions remain explicitly unimplemented rather than silently claimed. |
| C3 — reviewed-commit provenance | **Closed** | The reviewed-commit presence check covers the union of reviewed source, governing, and protocol paths (`activation.py:319-352`). Disposable remove-at-reviewed-HEAD/restore-at-authorization cases for a governing file and a protocol file refuse before claim creation. |
| C4 — closed local graph | **Partial; blocker above** | Omitted local dependencies, ambiguous local resolution, an undeclared/missing exact root, and unreachable asserted sources refuse. The manifest is compared with reachability from the three exact roots rather than the caller's whole reviewed list. Test-world symbol checks cover the computed sources. Cross-module loaded entropy aliases remain a false negative. |

## Checks run

- Focused inactive runtime suite: `45 passed in 4.06s` for `tests/test_officina_accounting.py`, `tests/test_officina_activation.py`, and `tests/test_officina_runtime.py`.
- Full suite: `267 passed in 28.74s`.
- `scripts/verify_inheritance.py`: `OK` for 71 inherited files.
- `scripts/verify_all.py`: both admitted decisions `VALID`.
- `scripts/verify_officina_wp12.py`: `OK`, inactive and quarantined.
- `scripts/verify_officina_active.py`: refused only because the production activation authorization is absent, as required at this gate.
- `git diff --check 2d0cc0b..2277331`: clean.

## Negative space and authorization boundary

The real tree remains `NOT_ACTIVATED`. `successor/officina/runtime/` contains only the tracked `T_RUNTIME.lock`; no production call-graph manifest, activation authorization, generic harness implementation, capability, claim, lease, process record, runtime output, world, learner run, candidate, entropy, E1/E2/E3 spend, Q/C object, datum, outcome, or scientific interpretation was created. The committed envelope, ledger, head, and lock were not mutated.

This verdict authorizes only the bounded verifier correction above and another focused confirmation. It does not open the generic metered-harness gate and does not authorize implementation, a production manifest, activation, execution, entropy, resource spend, T/Q/C data, or claim movement.
