I'll start by reading the specification documents and verifying patch integrity.

## Verification of base and integrity

Fresh detached clone at `6066f482c6752915ad21119f93dc162f4cb9db72`; patch SHA-256 recomputed as `8eba7e14651c7604b72ce3f447462359b74d38119782c29541005b8136dc2bf7` — matches. `git apply --check`, apply, `git diff --check` all pass. Changed/new paths are exactly the 23 declared `learning/*.py` files: no theory, no Rust/Peano, no yaml, no `util.py`, no Phase-1 artifacts. The 104-test gate reproduces **104/104 in 30.8 s** in the clean tree. All review below is against that tree, not the live dirty checkout.

---

# Findings

## Critical

### C-1 — Rust/PyO3 panics escape the closed error envelope entirely and collapse into the "child wrote no result" terminal

`pyo3_runtime.PanicException` derives from `BaseException`, **not** `Exception`:

```
MRO: ['PanicException', 'BaseException', 'object']
isinstance Exception     : False
```

`_isolated_child_main` catches only `Exception` ([`phase2_timeout.py:137`](/tmp/claude-1000/.../minimo_clean/learning/phase2_timeout.py)), so `scientific_error_envelope` is never invoked. The child dies with exit 1 and writes no result file, and the parent raises the generic untyped error at `phase2_timeout.py:196-199`.

Minimal counterexample — every declared pre-spawn validation passes (closed descriptor, valid spec, valid budget, valid artifact ID, valid timeout):

```bash
cd <clean-tree>/learning && python -c "
import phase2_isolated as I
from phase2_spec import tiny_scientific_spec
I.run_isolated_scientific_item(
  {'theory_text': open('theories/nat-add.p').read(),
   'premises': ['+_z','+_s','nat_ind','eq_symm','rewrite'],
   'goal': \"[('n : nat) -> (= (+ n z) n)]\"},
  tiny_scientific_spec(512), budget=6, timeout_s=300.0, artifact_id='item')"
```

Observed:

```
thread '<unnamed>' panicked at src/universe/term.rs:797:17: 'n' undeclared
...
phase2_timeout.IsolatedJobError: isolated child exit 1 wrote no result
```

The panic occurs inside `stage_children_from_actions` → `action.execute` → Peano, i.e. after the search has legitimately started. `parse_item_descriptor` structurally cannot prevent it: only Peano can decide goal well-formedness.

Consequence: a **formal-world terminal** (Peano panic) is byte-for-byte indistinguishable at the parent boundary from an infrastructure terminal (segfault, OOM-kill, spawn failure). Stage B's whole purpose is to "record every rejection by enumerated cause"; this class cannot be enumerated. It also contradicts contract §B/§C's requirement that refusals not become raw exceptions.

**Repair (bounded, ~15 lines).** In `_isolated_child_main`, catch `BaseException` for `kind in ('scientific_item', ...)` and add one envelope code, e.g. `PEANO_PANIC` with keys `('code','panic_message')`, mapping to a new `PeanoPanicRefusal(ActionHandlingError)`. Separately, at `phase2_timeout.py:196`, raise a distinct `IsolatedChildCrash(IsolatedJobError)` carrying `proc.exitcode` so a genuinely dead child is not conflated with an envelope failure. Add a test that drives the free-variable goal above through `run_isolated_scientific_item` and asserts the typed class.

**Why the 104 tests miss it.** `test_isolated_real_nat_add_expansion_primitive_evidence` uses the single well-formed goal `(= (+ z z) z)` at `budget=1`. No fixture supplies a descriptor that panics Peano, and `run_isolated_internal_error_test_only` raises a Python `RuntimeError`, which *is* an `Exception` — so the envelope path is exercised only for the class that already works.

---

### C-2 — The production whole-item search record is not reproducible across fresh processes; contract F "deterministic construction" is contradicted

`construct_scientific_lm` calls `transformers.GPT2LMHeadModel(cfg)` at `phase2_spec.py:366` with no seeding, and `run_scientific_item_in_worker` (`phase2_isolated.py:346-368`) never seeds the spawn child.

Counterexample 1 — construction is nondeterministic inside one process:

```bash
python -c "
from phase2_spec import tiny_scientific_spec, construct_scientific_lm
s = tiny_scientific_spec(64)
a, b = construct_scientific_lm(s), construct_scientific_lm(s)
print('spec_hash equal      :', a.spec_hash == b.spec_hash)
print('state_dict_hash equal:', a.manifest['state_dict_hash'] == b.manifest['state_dict_hash'])"
```

```
spec_hash equal      : True
state_dict_hash equal: False
```

Counterexample 2 — the production isolated item, same descriptor/spec/budget/artifact_id, two fresh processes at `budget=8`:

```
run0 entered=8 new_leaf=8 term=0 dead=0 solved=False nodes=8 sha=e7939408471da75468ef
run1 entered=8 new_leaf=8 term=0 dead=0 solved=False nodes=8 sha=dfc1c21bcd14b15d782f
byte-identical across fresh processes: False
```

Mechanism: random weights → different value/prior estimates in `ScientificLMPolicy.initialize` → different `_uct` selection → different expansion order → different `canonical_nodes`. The inherited `_uct`/`_policy`/`_backpropagate_reward`/`_tree_policy` contain no RNG (I checked), so the model init is the sole source.

This contradicts contract §F, whose own text says "Mutable global RNG call order is not an identity scheme" — yet the scientific learner's identity is currently a function of exactly the caller's ambient global torch RNG. It also weakens contract §A materially: because `state_dict_hash` is not a function of the spec, `assert_manifest_matches` can only ever validate a *transported* blob, and transport is explicitly not implemented — so the manifest mechanism has no currently satisfiable use.

**Repair (bounded, ~10 lines).** Add `init_seed` as a 26th required key in `SCIENTIFIC_SPEC_KEYS` (exact non-negative int), and in `construct_scientific_lm` build the model under `torch.Generator`-scoped or `torch.manual_seed(validated['init_seed'])` state before `GPT2LMHeadModel(cfg)`. The spec hash then covers it and the manifest becomes reconstructible. Add a test asserting two in-process constructions from one spec give equal `state_dict_hash`, and extend the fresh-process replay test to a `budget>=4` real item.

**Why the 104 tests miss it.** `test_two_fresh_processes_production_root_replay` (`test_phase2_root.py:774-826`) uses `ScientificFakeNode` at `budget=1`, and the compared payload contains only action serializations, child state strings, query strings and integer counters — **no LM-derived quantity at all**. At `budget=1` there is exactly one expansion and no `_uct` choice, so nondeterministic weights cannot influence the compared bytes. The test is correctly scoped to §F's "synthetic fixtures" wording, but its name and the report's "fresh-process canonical replay" language read as a production guarantee that does not hold.

---

## Major

### M-1 — Whole-item containment is bypassed from the **public** factory by a duck-typed proxy; real Peano runs in the parent and children are staged from strings

`is_real_tree_search_node` is `isinstance(leaf, TreeSearchNode)` (`phase2_actions.py:144-146`). Containment therefore keys on the *node type*, but the real Peano contact happens through `leaf.state_node` at `phase2_actions.py:337`:

```python
raw = leaf.enumerable_actions() if hasattr(leaf, 'enumerable_actions') else leaf.state_node.actions
```

Any object that is not a `TreeSearchNode` but exposes a real `state_node` takes the synthetic branch. Verified end-to-end through `make_scientific_search_root(...).run()` with `worker_capability=None`:

```
RESULT: PUBLIC root.run(proxy) SUCCEEDED end to end
  new_leaf_expansions    : 1
  serializations         : ['c +_z']
  child_state_strings    : ['c<c +_z>']
```

`'c +_z'` is a genuine Peano action serialization produced in the parent process. Children were then built from **strings** via `('explicit', [...])` — the exact "string-substituted semantic action" route contract §C exists to prevent.

This is not only an adversarial construction. A Stage-B/C harness that wraps nodes for instrumentation or logging would lose containment silently, with no error. The V4.2 repair closed the subclass case; the proxy case is the same family and is explicitly in scope for this review.

Forged capability tokens are properly contained — `True`, `1`, `object()`, `None`, `"cap"` all raise `UncontainedPeanoError`. The identity marker itself behaves as documented.

**Repair (bounded, ~6 lines).** Delete the `leaf.state_node.actions` fallback at `phase2_actions.py:337` and require the synthetic path to provide `scientific_enumeration_job()`; additionally assert in `_expand_synthetic_leaf_for_tests` that `type(leaf.state_node)` is not a `proofsearch.ProofStateNode`/`HolophrasmNode` (or that `leaf.state_node` exposes no `.actions` backed by `peano`), raising `UncontainedPeanoError`. Add a proxy fixture to `test_phase2_root.py` mirroring `test_public_root_refuses_real_node_subclass_before_search`.

**Why the 104 tests miss it.** `test_public_entry_rejects_uncontained_real_peano` and the V4.2 subclass test both pass a genuine `TreeSearchNode` (or subclass). No fixture passes a non-`TreeSearchNode` object holding a real `state_node`.

---

### M-2 — `action_timeout_s` is an unvalidated public argument; refusals are late and outside the closed envelope

`make_scientific_search_root(..., action_timeout_s=...)` (`phase2_root.py:49`) is public and re-exported through `policy.make_scientific_search_root(spec, **kwargs)`. `phase2_search.py:75` does a bare `float(action_timeout_s)`:

```
action_timeout_s=None      -> TypeError: float() argument must be a string or a real number
action_timeout_s=nan       -> ACCEPTED, search._action_timeout_s = nan
action_timeout_s=-1.0      -> ACCEPTED, search._action_timeout_s = -1.0
action_timeout_s=0         -> ACCEPTED, search._action_timeout_s = 0.0
action_timeout_s=True      -> ACCEPTED, search._action_timeout_s = 1.0
action_timeout_s="x"       -> ValueError: could not convert string to float: 'x'
action_timeout_s=inf       -> ACCEPTED, search._action_timeout_s = inf
```

The kill loop is **not** disabled — `require_positive_finite_timeout` inside `run_isolated_job` catches all of them at spawn time. But it raises `IsolatedInvalidTimeout`, a `ValueError` that is neither an `ActionHandlingError` nor an envelope code, mid-search:

```
action_timeout_s=nan   -> IsolatedInvalidTimeout: timeout_s must be a positive finite number
action_timeout_s=inf   -> IsolatedInvalidTimeout
action_timeout_s=-1.0  -> IsolatedInvalidTimeout
action_timeout_s=0     -> IsolatedInvalidTimeout
```

So: `None`/`"x"` are raw `TypeError`/`ValueError` at construction; `nan`/`inf`/`0`/`-1`/`True` are accepted at construction and refused late outside the closed error set. The V4.2 adversarial table entry "inject / action_timeout_s | absent from public isolated API and production job" is true for the isolated API but does not cover this in-process public parameter.

**Repair (1 line).** Call `require_positive_finite_timeout(action_timeout_s)` in `make_scientific_search_root` before `_construct_scientific_search_root`, and in `ScientificMonteCarloTreeSearch.__init__` when unauthorized. Add the argument to the existing `test_timeout_nan_inf_zero_bool_do_not_spawn` pattern.

---

### M-3 — Envelope code set cannot distinguish future attrition terminals (direct answer to task 5)

Envelope keys and semantics are otherwise exact: `ENVELOPE_KEY_SETS` is closed, `raise_from_scientific_error_envelope` validates key-set equality, types, artifact-ID validity, and the `token_count > limit` / `byte_count <= token_count` invariants, and reconstruction never parses human-readable strings. Base and derived artifact IDs share the single `validate_artifact_id`/`ARTIFACT_ID_MAX_BYTES = 512` source. That part is sound.

But the generic parent `ActionHandlingError` is **not sufficient**. Three distinct terminals currently collapse or escape:

| Terminal | Current parent-side result | Distinguishable? |
|---|---|---|
| Derived artifact-ID hierarchy overflow | `ACTION_HANDLING_REFUSAL` → `ActionHandlingError` | No — `ArtifactIdLimitRefusal` subtype lost (declared known limit) |
| Peano/Rust panic (C-1) | `IsolatedJobError('… wrote no result')` | No — identical to a crashed worker |
| Invalid `action_timeout_s` (M-2) | `IsolatedInvalidTimeout` | Escapes the envelope entirely |

Only the first is disclosed in the V4.2 "known non-blocking limits". For a Stage-B carrier audit that must bin rejections by enumerated cause, and for a Stage-C attrition ledger with a whole-block retry rule, these must be separable **before** either exists.

**Repair.** Add `code` fields for the artifact-ID case (`ARTIFACT_ID_LIMIT`) and the panic case (`PEANO_PANIC`); route `IsolatedInvalidTimeout` to a pre-spawn refusal per M-2. Three new entries in `ENVELOPE_KEY_SETS` plus their reconstruction branches.

---

### M-4 — Codec computes a silently wrong completion likelihood at `bos=False`

`completion_target_positions` returns a negative logit index, and `completion_logprobs_from_logits` indexes with it unguarded (`phase2_codec.py:317`, `343-348`):

```
completion_target_positions("", "ab", bos=False, eos=True) -> (-1, 0, 1)
completion_logprobs_from_logits(bos=False) -> [-104.15888977050781]
```

`logprobs[i, -1, target]` wraps to the final position — no exception, a plausible-looking float. `hand_computed_completion_logprob` has the identical defect.

Production `ScientificLMPolicy.completion_logprob` hardcodes `bos=True`, so this is not currently live. It matters because contract §B declares the codec accepts an "explicit BOS/EOS policy" and this codec is the single instrument the Phase-2 selector (label-posterior log-odds over `d.elaborate(g)`) will be built on in Stage C. A selector scoring a bare statement with no preamble is the natural way to hit it.

**Repair (2 lines).** Raise `QueryCodecError` when `first_completion - 1 < 0` in both functions. Add a `bos=False` case to `test_hand_computed_completion_likelihood_includes_eos_excludes_preamble`.

**Why the 104 tests miss it.** No codec test passes `bos=False`; the hand-computed reference is only exercised at the default.

---

## Minor

- **m-1 (control-flow proof only, no reproducible trace).** `run_isolated_job` never consults the result file before declaring a timeout: `phase2_timeout.py:193-195` raises `IsolatedJobTimeout` on `proc.is_alive()`, and `os.path.exists(result_path)` is first checked at line 196, reachable only when the process is already dead. A child that has completed `fsync` + `os.replace` but is still in interpreter teardown when the deadline lands is SIGKILLed and reported as a timeout. A 60-point sweep across ±15% of the measured 0.046 s completion time produced 57 ok / 3 timeout / 0 error, all at `t <` completion — I could not observe the misclassification, and its window is ~ms. It nonetheless converts a completed item into an attrition terminal, and branch runtimes differ between arms, so the channel is treatment-correlated. One-line repair: check `os.path.exists(result_path)` before raising.
- **m-2.** `_expand_real_leaf_in_isolated_worker` calls `stage_children_from_actions` (real Peano `expand` on every action) at `phase2_actions.py:301` *before* query preflight at :305. Contract §C only promises refusal "before search" and no sibling deletion, both of which hold — but the Peano side effects of full child construction are already paid. Worth stating explicitly in the contract rather than repairing.
- **m-3.** `phase2_search.py:101` sets `leaf._index` before the containment check inside `expand_leaf_canonical`. The V4.2 claim "leaves `_children` unchanged" is accurate; `_index` is not covered by `_leaf_unchanged`.
- **m-4.** `canonicalize_actions` and `expand_leaf_canonical` accept `**_ignored`, so a misspelled kwarg is silently dropped: `canonicalize_actions(['b','a'], timeout=0.0001, nonsense=True) -> ['a','b']` uses the default `timeout_s=1.0`. The public factory correctly rejects unknown kwargs (`TypeError`), so this is internal-surface only.
- **m-5.** `canonical_action_ascii` line 97 (`if not isinstance(text, str)`) is unreachable after `str(action)`. `canonicalize_actions` serializes twice (:124 then inside :123).
- **m-6.** Exclusion evidence is textual/AST source scanning of 10 files, not runtime call-graph reachability. `ScientificMonteCarloTreeSearch` inherits from `proofsearch.MonteCarloTreeSearch`, whose module imports `wandb`, `random`, `np.random` and `sample_batch`; `assertNotIn('wandb', source)` over `phase2_*.py` cannot see that. I manually confirmed the inherited `_tree_policy`/`_uct`/`_policy`/`_backpropagate_reward` use no RNG and never call `expand()`, so the substantive claim holds — but it is proved by my inspection, not by the tests.
- **m-7 (Phase-1 only).** `_normalize_kleene_statement` (`problems.py:373-399`) is a hand-maintained exact-match substitution table returning `exact.get(statement, statement)` — any whitespace drift in `extrinsic/propositional-logic.p` silently disables normalization and the item simply fails to parse. Not a Phase-2 prerequisite per decision 19 §5.
- **m-8 (legacy behavior change, correct but worth recording).** `resolve_max_pos_neg_ratio` is wired into legacy `LMPolicy.__init__` (`proofsearch.py:679`). The shipped `config/agent/mcts-lm.yaml` sets `max_pos_neg_ratio: 5` while stock code read `max_positive_negative_ratio` and silently used `10`. The repair is right and contract §E is satisfied — but it means the legacy route no longer reproduces the completed Phase-1 run's negative-sampling ratio. No shipped yaml uses the forbidden long key, so nothing breaks.

---

# Contract grades

| Row | Grade | Basis |
|---|---|---|
| **A** explicit learner identity | `PROVED` | Closed 25-key spec, extra/missing/type refusals, independent GPT-2 parameter formula cross-check, CUDA confined to `reject_unavailable_device` (AST-verified single call site), manifest with spec/param/state/optimizer/resolved-config hashes. Caveat: manifest is only usable for transported blobs while C-2 stands. |
| **B** exact query codec | `PROVED` | Every enumerated bullet holds: one codec, no truncation anywhere, caller-list mutation detection, typed `QueryOverflow` with all five fields, EOS included once, preamble/BOS excluded, padding excluded, hand-computed reference, training preflight before optimizer mutation. M-4 is a defect in an unexercised public option, not a violated bullet. |
| **C** full canonical action space | `PROVED` (isolated worker path) | Unique ASCII serialization, `DuplicateActionSerialization`, canonical sort before child construction, `MAX_ACTION_LENGTH` absent, whole-item refusal without sibling deletion, downstream-invariance under shuffled upstream enumeration, 755/767 admitted whole with no `[...]`. Its containment premise is separately contradicted — see the boundary row. |
| **D** exact search accounting | `PROVED` | `entered_tree_policy_iterations` incremented after the pre-iteration solved check; `new_leaf_expansions` only on successful expansion; `terminal_hits`/`dead_traversals`/`solved`/`assigned_cap` distinct; zero/first/final/exhaustion/dead-traversal fixtures present; `mcts_expansions` absent from the Phase-2 schema; the stock `max()`-on-empty-children crash is guarded. |
| **E** prospective correctness repairs | `INDIRECT` | Hindsight repair is a genuine differential fixture that fails on the upstream bug (`h.statement`, AST-asserted) — `PROVED`. Config single-source is `PROVED` and fixes a real 5-vs-10 mismatch. The wandb/Celery/RNG exclusion sub-claim is textual absence in `phase2_*.py`, not a runtime guarantee; `proofsearch` (imported by `phase2_search`) still imports `wandb` at module scope. |
| **F** deterministic Stage-A preflight | `CONTRADICTED` | "Deterministic construction" is explicitly in Stage-A scope and fails: two constructions from one spec give different `state_dict_hash` (C-2). Full optimizer/branch replay remains correctly deferred. |
| **G** cumulative fresh-tree acceptance | `INDIRECT` | G1 ✔ (I reproduced apply/`--check`/`diff --check`). G2 ✔ **as worded** (synthetic) but does not extend to production (C-2). G3 ✔. G4 source-only, not call-graph (m-6). G5 ✔ (104/104 reproduced independently). |
| **Public process boundary** | `CONTRADICTED` | M-1: `make_scientific_search_root(...).run(proxy)` enumerates real Peano in the parent and stages children from strings, with `worker_capability=None`. Forged tokens and real subclasses are correctly contained; the proxy family is not. |

---

# Disposition

**Blockers (must land before Stage-B authorization):** C-1, C-2, M-1, M-3.
Each has an exact, local repair surface — one envelope branch and one `BaseException` catch; one spec key and one seed call; one deleted fallback plus one assertion; three envelope codes. None requires redesign, a new protocol, or touching the declared formal world.

**Later obligations (correctly deferred, no false claim in current code):** byte-identical optimizer state and full branch replay; trained-checkpoint transport with manifest verification before Peano reconstruction; deterministic keyed batch sampling.

**Non-blocking cleanup:** M-2, M-4, m-1 through m-8.

One process note. The V4.2 report's "unhidden findings" list and the driver's boundary-limits section are accurate and unusually candid — the disclosed subtype-loss limit is real and correctly characterized. The gap this review found is not concealment; it is that the acceptance evidence is dominated by synthetic fixtures at `budget=1`, and both Criticals live precisely where the real Peano path and the real LM diverge from those fixtures.

`REVISE_STAGE_A_V4_2`
