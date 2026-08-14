# `CONFIRM_STAGE_A_V4_3_2_Y`

Patch SHA-256 recomputed as `e08a8d29d67d82297216722b3e13e6c1a3f4bd354962a2865b1cfc57a9980bbd` — matches. Fresh detached clone at `6066f482c6752915ad21119f93dc162f4cb9db72`; `git apply --check`, apply, `git diff --check` (exit 0), `py_compile` all pass. 23 changed/new paths, 0 outside `learning/*.py`.

First, the correction to my own record: my V4.3.1 question-4 disposition tested only the boundary values the builder declared (`2**63`, `2**64-1`) and did not independently sweep for aliases *inside* the accepted range. X's finding is correct and I reproduce it below; that cell of my prior confirmation is superseded.

---

## 1. Accepted `init_seed` domain — **CONFIRMED `[0, 2**32-1]`, exact non-bool int**

`phase2_spec.py:52` `TORCH_INIT_SEED_MAX = (1 << 32) - 1` = `4294967295`; `:203-208` enforces `type(v) is bool` rejection, `type(v) is not int` rejection, then range.

| Value | Result | | Value | Result |
|---|---|---|---|---|
| `0`, `1`, `2**31`, `2**32-1` | accept | | `2**32`, `2**32+1`, `2**62`, `2**63-1` | reject |
| `-1` | reject | | `True`, `False` | reject (bool) |
| `1.0`, `"7"` | reject | | `int` subclass instance | reject (exact-int) |

14/14 as expected.

## 2. `2**32-1` accepted, `2**32` typed-rejected before spawn — **CONFIRMED**

Through the public `run_isolated_scientific_item`, with `multiprocessing.get_context` instrumented by a read-only spy:

```
public init_seed=2**32    IsolatedInvalidSpec, mp.get_context=0
public init_seed=2**32+1  IsolatedInvalidSpec, mp.get_context=0
public init_seed=2**62    IsolatedInvalidSpec, mp.get_context=0
public init_seed=2**63-1  IsolatedInvalidSpec, mp.get_context=0
public init_seed=-1       IsolatedInvalidSpec, mp.get_context=0
public init_seed=True     IsolatedInvalidSpec, mp.get_context=0
public init_seed=2**32-1  ACCEPTED, ran real nat-add item, new_leaf=1, mp.get_context=1
```

No multiprocessing context is requested for any rejected seed; the accepted upper bound reaches a real Peano item.

## 3. Backend alias probe — **CONFIRMED, reproduced independently**

Read-only `torch.Generator(device='cpu')` streams:

```
stream(0)       == stream(2**32)    : True     <- the alias that invalidated [0, 2**63-1]
stream(0)       == stream(2**62)    : True
stream(1)       == stream(2**32+1)  : True
stream(2**32-1) == stream(0)        : False    <- new upper bound is not itself an alias
collisions among 14 probed seeds inside [0, 2**32-1] : 0
```

Learner-level consequence, matching the driver table exactly (seed `0` → spec `5d4b11c2…`, state `0fa58f6727b770…`):

```
init_seed=0           spec=5d4b11c2ca81  state=0fa58f6727b77064
init_seed=4294967295  spec=9dce56ef2260  state=a8a73a52a778dc87
```

Distinct spec hash now implies distinct learner state hash. The generator truncates to the low 32 bits, so `[0, 2**32-1]` is the exact bijective domain — the restriction is canonical, not merely conservative.

## 4. Full gate and unchanged V4.3.1 cells — **CONFIRMED**

```
Ran 126 tests in 48.776s — OK    (125 V4.3.1 + 1 new public pre-spawn; matches declared)
CPU-debug spec hash : b2fd8e4887909dfdf269123dc484a876d6a826c650a7098f6abdc852215c6b09  (unchanged)
spec key count      : 26          parameter count : 478720  (unchanged)
ambient float32/float64 model+optimizer manifest identity : stable
```

All other cells I confirmed in V4.3.1 — typed spec/dtype boundary, ambient dtype/device/RNG restoration, real zero-budget evidence, exact search accounting, faithful terminal traversal, codec `bos=False` causality, Peano-proxy containment, deadline/result-file ordering, explicit synthetic enumeration boundary, dedicated `ARTIFACT_ID_LIMIT`, real PyO3 panic vs forged panic vs `IsolatedChildCrash`, budget-8 fresh-process replay — are untouched by this patch's diff surface and remain closed.

**No contradiction of questions 1–4 reproduced.** No finding sought or reported outside this numerical boundary.

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
| Patch SHA-256 | matches `e08a8d29…` |
| apply / `--check` / `diff --check` / `py_compile` | pass (exit 0) |
| Changed paths | 23, all `learning/*.py` |
| Combined Stage-A gate, fresh tree | **126/126 OK, 48.8 s** |
| Independent probes this round | 15 domain cases, 7 public-boundary cases, 4 alias comparisons + 14-seed sweep, 4 unchanged-cell checks — all pass |

---

**Negative authorization.** This confirmation authorizes no training job, no carrier generation, no selector qualification, no SELF/YOKED branches, no Phase-2 outcome, no Phase-1 checkpoint rerun, no commit, and no push. Deferred obligations remain open and unchanged: byte-identical optimizer / full training-branch replay, deterministic keyed batch sampling, checkpoint transport with manifest verification before Peano reconstruction, and the underscore capability token as in-tree call-graph discipline rather than a sandbox.
