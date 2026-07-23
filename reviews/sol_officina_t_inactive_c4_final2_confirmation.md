OFFICINA_T_INACTIVE_C4_YLINE_CONFIRMED

The bounded repair `e703a2b..fbac49309de4b4ebc26a0e82e73432a875e15d91` closes the ordinary `__builtins__.<name>` namespace spelling without changing the declared capability inventory or reopening any design cell. The reviewed verifier and tests are byte-identical at the later prompt-only HEAD.

## Confirmation

1. **Exact sibling spellings:** direct `__builtins__.eval`, direct `__builtins__.getattr`, and `namespace = __builtins__; resolver = namespace.eval` all refuse in both `verify_source_quarantine` and `verify_production_boundary`. The disposable probes were parsed statically; no probe module was imported or executed.

2. **Bounded normalization:** `_normalized_capability_name` now recognizes the two ordinary namespaces `builtins.` and `__builtins__.`. In either case it removes the prefix only when the suffix is already in the derived five-name `BUILTIN_DYNAMIC_IMPORT_CALLS` set: `__import__`, `compile`, `eval`, `exec`, or `getattr`. No primitive was added. Loaded references, true calls, direct/module aliases, multi-hop aliases, and `from builtins import ...` entries remain covered in both verifier entry points for all five names.

3. **Inherited C4 checks:** the exact reachable graph
   `scripts/officina_activate_t.py -> external_behavior.py -> local_helper.py`, with `draw = os.urandom` in the helper, refuses as an entropy reference. The declared matrix has no miss across all nine entropy capabilities, all six dynamic entries, and statically composed `/dev/random` and `/dev/urandom`. Omitted local dependencies, ambiguous resolution, unreachable reviewed sources, altered or missing exact roots, and graph/manifest disagreement remain fail-closed.

4. **Residual search:** I found no ordinary reproducible namespace/import/assignment alias spelling of a currently declared primitive that bypasses the repaired checks. As required, computed subscription and additional reflective mechanisms were not treated as part of this bounded gate.

## Checks run

- Static two-verifier namespace matrix for all five built-ins: no misses across `__builtins__` reference, call, and multi-hop forms or the inherited `builtins` and `ImportFrom` forms.
- Static declared entropy/dynamic/random-device matrix and exact three-file reachability probe: no misses.
- Focused bootstrap/accounting/activation/runtime suite: `75 passed in 6.20s`.
- Full suite: `279 passed in 30.48s`.
- `scripts/verify_inheritance.py`: `OK`, 71 inherited files match.
- `scripts/verify_all.py`: both admitted decisions `VALID`.
- `scripts/verify_officina_wp12.py`: `OK`, quarantined and inactive.
- `scripts/verify_officina_active.py`: refused only because `OFFICINA_T_ACTIVATION_AUTHORIZATION.json` is absent, as required.
- `git diff --check e703a2b..fbac49309de4b4ebc26a0e82e73432a875e15d91`: clean.

## Negative space and scope

The real Officina tree remains `NOT_ACTIVATED`. The committed envelope, ledger, external head, and runtime lock are unchanged; `successor/officina/runtime/` contains only `T_RUNTIME.lock`. No activation authorization, production manifest, generic harness implementation, runtime output, process, lease, capability, entropy, E1/E2/E3 spend, T/Q/C datum, outcome, or scientific interpretation was created.

This verdict closes only the inactive C4 verifier gate. It authorizes no implementation, production artifact, activation, process, capability, entropy, resource spend, T/Q/C datum, scientific interpretation, or claim movement.
