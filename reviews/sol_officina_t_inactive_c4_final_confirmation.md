REVISE_OFFICINA_T_INACTIVE_C4_FINAL

The bounded repair at `6ba2d23` closes the exact archived cross-module `os.urandom` counterexample and preserves the accepted graph-closure checks, but one concrete semantics-preserving dynamic-reference alias still bypasses the new check. The residual verifier gate therefore cannot close yet.

## Major finding — builtins-qualified declared primitives bypass membership

The new loaded-reference check compares `_resolved_symbol(...)` directly with `DYNAMIC_IMPORT_CALLS` (`src/philosophia/officina/verification.py:327-335`). The declared built-in primitives are stored under their bare names—`__import__`, `compile`, `eval`, `exec`, and `getattr`—so normal Python qualification through the `builtins` module changes the resolved spelling without changing the referenced callable.

This exact reachable-root probe is accepted with an empty failure list:

```python
# src/philosophia/officina/generic_harness.py
import builtins
runner = builtins.eval
alias = runner
```

The disposable fixture contained all three exact roots and a graph-complete manifest whose reachable set and edges exactly matched the computed closure. `verify_production_boundary(...)` returned `[]`. The equivalent `from builtins import eval as runner` and `import builtins as bi; runner = bi.getattr` variants also returned `[]`. No inspected source was imported or executed.

This is within the currently declared primitive set: `eval` and `getattr` are explicit members of `DYNAMIC_IMPORT_CALLS`; `builtins.eval` and `builtins.getattr` are ordinary references to those same callable objects, not newly proposed primitives.

### Smallest bounded correction

Normalize a resolved `builtins.<name>` reference to `<name>` when `<name>` is one of the declared bare built-in members of `DYNAMIC_IMPORT_CALLS`, then apply the existing loaded-reference and call checks. Add one static regression covering direct qualification, `from builtins import ... as ...`, and a multi-hop local alias. Do not broaden the primitive inventory, execute inspected source, or change graph, manifest, activation, or scientific contracts. Another literal C4 confirmation is required.

## Required checks

1. **Exact three-file graph:** **Closed.** The exact graph `scripts/officina_activate_t.py -> external_behavior.py -> local_helper.py`, with `draw = os.urandom` in the helper and `from local_helper import draw` in the caller, now refuses with `production source references entropy os.urandom`. The committed regression passes and operates by AST inspection only.
2. **Declared primitives and random-device paths:** **Partial.** Loaded/multi-hop references to all currently enumerated entropy primitives—`os.getrandom`, `os.urandom`, `random.SystemRandom`, all four listed `secrets` functions, and `torch.initial_seed`/`torch.seed`—refuse. Bare and multi-hop references to all declared dynamic primitives refuse, as does `importlib.import_module`. Statically composed `/dev/random` and `/dev/urandom`, including constant f-string composition, refuse. Builtins-qualified versions of the five declared bare dynamic primitives remain the blocker above.
3. **Reachability and graph closure:** **Closed and not regressed.** The checks operate over the reviewed source set and compare the manifest to reachability computed from the three exact roots. Omitted local dependencies, ambiguous local resolution, unreachable asserted sources, and a missing/undeclared exact executable root remain fail-closed.
4. **Concrete residual alias:** **Open.** The `builtins.eval` probe above is reproducible under the current declared set. I found no false negative among the directly spelled entropy primitives or either statically composed random-device path.

## Checks run

- `git diff --check f87477d..6ba2d23`: clean; the bounded commit changes only `src/philosophia/officina/verification.py` and `tests/test_officina_activation.py`.
- Focused accounting/activation/runtime suite: `48 passed in 4.97s`.
- Full suite: `270 passed in 29.86s`.
- `scripts/verify_inheritance.py`: `OK`, 71 inherited files match.
- `scripts/verify_all.py`: both admitted decisions `VALID`.
- `scripts/verify_officina_wp12.py`: `OK`, quarantined and inactive.
- `scripts/verify_officina_active.py`: refused only because the production activation authorization is absent, as required.
- Static disposable matrix: every directly enumerated entropy/dynamic reference and both random-device paths refused; the three builtins-qualified variants above produced empty failure lists.

## Negative space

The real Officina state remains `NOT_ACTIVATED`. The committed envelope, ledger, external head, and runtime lock are byte-unchanged; `successor/officina/runtime/` contains only `T_RUNTIME.lock`. No production harness, call-graph manifest, activation authorization, runtime output, process, lease, capability, entropy, E1/E2/E3 spend, T/Q/C datum, outcome, or scientific interpretation was created.

This verdict authorizes only the verifier normalization and regression test stated above, followed by another bounded confirmation. It authorizes no implementation beyond that repair, production artifact, activation, execution, resource spend, data, or claim movement.
