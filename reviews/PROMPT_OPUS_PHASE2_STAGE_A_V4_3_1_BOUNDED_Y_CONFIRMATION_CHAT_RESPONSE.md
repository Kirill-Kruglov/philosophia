I'll verify integrity first, then work through the five bounded questions.

# `CONFIRM_STAGE_A_V4_3_1_Y`

Patch SHA-256 recomputed as `38afd4233e94fb479954ae2f4902188b72732e9f293c640094d8de69a1c2e571` — matches. Fresh detached clone at `6066f482c6752915ad21119f93dc162f4cb9db72`; `git apply --check`, apply, `git diff --check` (exit 0), `py_compile` all pass. 23 changed/new paths, **all** `learning/*.py`; no theory, Rust/Peano, yaml, `util.py`, or Phase-1 artifacts.

---

## Disposition, questions 1–5

### 1. `PEANO_PANIC` / forged envelope / `IsolatedChildCrash` — **CONFIRMED**

| Probe | Result |
|---|---|
| Real free-variable nat-add goal `[('n : nat) -> (= (+ n z) n)]`, budget 6 | `PeanoPanicRefusal`, `exception_module='pyo3_runtime'`, `exception_class='PanicException'` |
| — is `ActionHandlingError` / is `IsolatedChildCrash` | `True` / `False` |
| Forged `fake.module`/`FakePanic` | `IsolatedJobError` |
| Forged `pyo3_runtime`/`Other` | `IsolatedJobError` |
| Forged `other`/`PanicException` | `IsolatedJobError` |
| Genuine `pyo3_runtime`/`PanicException` envelope | `PeanoPanicRefusal` |
| `crash_no_result_test_only` (`os._exit(3)`) | `IsolatedChildCrash`, `exitcode=3` |

Surfaces: `phase2_timeout.py:150` now catches `BaseException` (re-raising `SystemExit`/`KeyboardInterrupt`/`GeneratorExit`); `phase2_actions.py:117` `is_pyo3_panic` pins the concrete identity; `phase2_isolated.py:245-256` enforces it on reconstruction; `phase2_timeout.py:219` raises the distinct crash terminal. Envelope branch ordering is correct — `ArtifactIdLimitRefusal` (:151) and `PeanoPanicRefusal` (:158) both precede the generic `ActionHandlingError` (:183).

### 2. Preserved boundaries — **CONFIRMED (5/5)**

- **Deadline/result-file ordering:** `phase2_timeout.py:210` checks `os.path.exists(result_path)` *before* the timeout branch; a still-alive child is killed as cleanup, not misclassified. Result-less + alive → `IsolatedJobTimeout`; result-less + dead → `IsolatedChildCrash`.
- **Peano-proxy containment:** my exact V4.2 M-1 counterexample (non-`TreeSearchNode` wrapper over a real `HolophrasmNode`) now raises `UncontainedPeanoError` both through public `root.run()` and through direct `expand_leaf_canonical`, with `proxy._children` unchanged. Enforced at three layers — `phase2_root.py:36`, `phase2_search.py:93` and `:111`, `phase2_actions.py:295` — via `is_real_peano_state_node`. The `:111` per-leaf call now precedes `leaf._index` assignment, closing my m-3 as a side effect.
- **Explicit synthetic enumeration boundary:** the `leaf.state_node.actions` fallback is gone; `phase2_actions.py:385` requires `scientific_enumeration_job()` and refuses otherwise.
- **Positive-finite `action_timeout_s`:** all of `None`, `nan`, `inf`, `-1.0`, `0`, `True`, `"x"` raise `IsolatedInvalidTimeout` **at construction** (previously accepted or raw `TypeError`/`ValueError`).
- **Dedicated artifact-ID terminal:** overflow emits `code='ARTIFACT_ID_LIMIT'` and round-trips to `ArtifactIdLimitRefusal`, distinct from semantic action refusal. `bos=False` with empty preamble now raises `QueryCodecError` instead of wrapping to index −1.

### 3. Scoped construction / ambient identity — **CONFIRMED**

```
CPU-debug spec hash : b2fd8e4887909dfdf269123dc484a876d6a826c650a7098f6abdc852215c6b09  (matches declared)
spec key count      : 26        parameter count : 478720
ambient float32 -> state=0fa58f6727b770644db32d456f39bbc9
ambient float64 -> state=0fa58f6727b770644db32d456f39bbc9
model+optimizer manifests equal across ambient dtypes : PASS
torch RNG restored on success / on exception          : PASS / PASS
default dtype restored on success / after exception   : PASS / PASS
```

Driver-1 is closed: the float64 divergence (`83f96c81…`) is gone and identity is anchored to the float32 value the V4.3 audit recorded. Spec hash and parameter count are unchanged from the declared values.

### 4. Seed domain and exact-`str` dtype — **CONFIRMED, typed before spawn**

- Rejected with `ScientificSpecError`: `2**63` (the first aliasing seed), `2**64-1`, `-1`, `True`, `1.0`, `"0"`. Accepted: `0`, `2**63-1`.
- `dtype` ∈ {`[]`, `32`, `None`, `b'float32'`} → `IsolatedInvalidSpec` through the public `run_isolated_scientific_item`, with `multiprocessing.get_context` call count **0** (verified by spy) — no context requested, no spawn.
- Also re-confirmed the V4.3 optimizer-domain closure: `optimizer_lr=nan`, `optimizer_eps=True`, `weight_decay=-1`, `betas=[1.0, 0.9]` all refuse in the parent.

### 5. C-1, C-2, M-1, M-3 and bounded minors — **CLOSED, no contradiction in the repair surface**

| V4.2 finding | Status |
|---|---|
| C-1 PyO3 panic escapes envelope | Closed (Q1) |
| C-2 production item not reproducible | **Closed** — re-ran my exact counterexample below |
| M-1 proxy containment bypass | Closed (Q2) |
| M-2 `action_timeout_s` unvalidated | Closed (Q2) |
| M-3 envelope cannot distinguish terminals | Closed — `PEANO_PANIC`, `ARTIFACT_ID_LIMIT`, `IsolatedChildCrash` now separable |
| M-4 codec `bos=False` negative index | Closed (Q2) |
| m-1 deadline/result-file race | Closed (Q2) |
| m-3 `_index` before refusal | Closed (`phase2_search.py:111`) |
| m-4 `**_ignored` kwargs | Closed — no `_ignored` in any `phase2_*.py` |

C-2 re-run, same descriptor/spec/budget as my V4.2 counterexample, with ambient RNG **and** default dtype deliberately perturbed between the two fresh processes:

```
run0 entered=8 new_leaf=8 term=0 dead=0 solved=False nodes=8 sha=e7939408471da75468ef6d6c
run1 entered=8 new_leaf=8 term=0 dead=0 solved=False nodes=8 sha=e7939408471da75468ef6d6c
byte-identical across fresh processes: True
budget=0 -> entered=0 new_leaf=0 nodes=0 n_policy_q=0  (valid evidence, no INTERNAL_ERROR)
```

Under V4.2 these two runs produced `e793…` and `dfc1…`.

**No admissible new finding.** The only residuals I observed are cosmetic and contradict none of questions 1–5: `phase2_timeout.py:159-162` has an `elif`/`else` with identical bodies (dead branch), and `:151` uses exact-type membership for the `SystemExit`/`KeyboardInterrupt`/`GeneratorExit` re-raise, so a subclass of those would be enveloped rather than re-raised. Neither is a Peano-panic, containment, timing, construction, or spec-validation path. Recording only; not a repair request.

---

## Commands and counts

```bash
git clone --no-checkout <minimo> mc && cd mc && git checkout 6066f482c6752915ad21119f93dc162f4cb9db72
git apply --check <patch> && git apply <patch> && git diff --check
python -m py_compile bootstrap.py policy.py problems.py proofsearch.py phase2_*.py test_*.py
PYTHONHASHSEED=0 python -m unittest test_mcts_expansion_counter test_phase2_spec test_phase2_codec \
  test_phase2_search test_phase2_actions test_phase2_hindsight test_phase2_config \
  test_phase2_exclusions test_phase2_root
```

| Check | Result |
|---|---|
| Patch SHA-256 | matches `38afd423…` |
| apply / `--check` / `diff --check` / `py_compile` | pass (exit 0) |
| Combined Stage-A gate, fresh tree | **125/125 OK, 49.6 s** |
| Philosophia pytest | **416 passed, 43.2 s** |
| Changed paths | 23, all `learning/*.py` |
| Independent counterexamples run | 41 probes across Q1–Q5, all pass |

---

**Confirmation authorizes no training, no carrier generation, no selector qualification, no SELF/YOKED branches, no Phase-2 outcome, no Phase-1 checkpoint rerun, no commit, and no push.** Later obligations remain open and untouched: byte-identical optimizer / full training-branch replay, deterministic keyed batch sampling, checkpoint transport with manifest verification before Peano reconstruction, and treating the underscore capability token as anything more than trusted in-tree call-graph discipline.
