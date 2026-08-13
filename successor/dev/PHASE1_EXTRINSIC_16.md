# PHASE1_EXTRINSIC_16

NON-CITABLE Phase-1 instrument construction. Extrinsic evaluation of the
reproduced Minimo propositional-logic run on Kleene Theorem-41 statements.
No philosophia ACTIVE/YOKED claim. No scientific lock.

## VERDICT: FLAT

ck4 success rate (0.3667) does not exceed ck0 (0.3667).
Per stop protocol: report FLAT; do not retune expansions, agent, or problem set.

Run dir: `/home/master/llm_projects/minimo/learning/outputs/2026-08-10/00-14-33`.
Checkpoints: `0.pt`..`4.pt`. Agent: `mcts-lm` / `holophrasm`.
Budget: 2000 MCTS expansions per theorem. `accumulate_library=false`.
Seed: 0. `OMP_NUM_THREADS=16`, `nice -n 10`.
Wall clock: 2026-08-10T20:00:07+03:00 -> 2026-08-10T21:32:49+03:00
(~1 h 33 m for 150 searches).

Statement file `learning/extrinsic/propositional-logic.p` contains
**30** Peano statements (labels through 25 with a/b variants).
Paper main text says 35; Appendix E.2 explicitly notes there are 30 statements
under that numbering. This eval uses the on-disk file (N=30).
Background theory is `learning/theories/propositional-logic.p` with the training
premise names (`and_i`, ... `em`), not `lean-library-logic`.

Paper Fig. 4 reference (propositional logic): ~0.30 at ck0 to ~0.47 at ck4.

### Success rate by checkpoint

| checkpoint | solved / N | success rate | mean elapsed_s |
|---:|---:|---:|---:|
| 0 | 11 / 30 | 0.3667 | 42.11 |
| 1 | 11 / 30 | 0.3667 | 34.45 |
| 2 | 11 / 30 | 0.3667 | 32.24 |
| 3 | 10 / 30 | 0.3333 | 35.20 |
| 4 | 11 / 30 | 0.3667 | 40.69 |

Overall mean wall-clock search cost: **36.94 s/search**
(success mean 7.98 s; failure mean
53.23 s). Observed full-budget failures land near
~53 s at 2000 expansions on this CPU box — about 2.3x faster than the pre-run
~2 min/search estimate; total ~1.5 h vs ~6 h estimate.

### Solved-set movement (rate-flat but not identical)

- ck4 only (not ck0): `kleene_3`
- ck0 only (not ck4): `kleene_20`
- ck3 lost `kleene_20` relative to ck0/1/2; ck4 gained `kleene_3` and lost `kleene_20`.

### Theorems solved only starting at checkpoint 4

`kleene_3`

Note: `kleene_3` is solved at ck4 and not at ck0–ck3, so it is first-solved at 4.

### Never solved at any checkpoint

`kleene_2`, `kleene_4`, `kleene_5`, `kleene_6`, `kleene_7`, `kleene_8a`, `kleene_8b`, `kleene_9a`, `kleene_9b`, `kleene_12`, `kleene_13`, `kleene_14`, `kleene_15`, `kleene_21`, `kleene_22`, `kleene_23`, `kleene_24`, `kleene_25`

### Per-theorem matrix

| theorem | ck0 | ck1 | ck2 | ck3 | ck4 | first |
|---|:-:|:-:|:-:|:-:|:-:|---:|
| `kleene_1` | Y | Y | Y | Y | Y | 0 |
| `kleene_2` | . | . | . | . | . | - |
| `kleene_3` | . | . | . | . | Y | 4 |
| `kleene_4` | . | . | . | . | . | - |
| `kleene_5` | . | . | . | . | . | - |
| `kleene_6` | . | . | . | . | . | - |
| `kleene_7` | . | . | . | . | . | - |
| `kleene_8a` | . | . | . | . | . | - |
| `kleene_8b` | . | . | . | . | . | - |
| `kleene_9a` | . | . | . | . | . | - |
| `kleene_9b` | . | . | . | . | . | - |
| `kleene_10a` | Y | Y | Y | Y | Y | 0 |
| `kleene_10b` | Y | Y | Y | Y | Y | 0 |
| `kleene_11` | Y | Y | Y | Y | Y | 0 |
| `kleene_12` | . | . | . | . | . | - |
| `kleene_13` | . | . | . | . | . | - |
| `kleene_14` | . | . | . | . | . | - |
| `kleene_15` | . | . | . | . | . | - |
| `kleene_16` | Y | Y | Y | Y | Y | 0 |
| `kleene_17a` | Y | Y | Y | Y | Y | 0 |
| `kleene_17b` | Y | Y | Y | Y | Y | 0 |
| `kleene_18a` | Y | Y | Y | Y | Y | 0 |
| `kleene_18b` | Y | Y | Y | Y | Y | 0 |
| `kleene_19` | Y | Y | Y | Y | Y | 0 |
| `kleene_20` | Y | Y | Y | . | . | 0 |
| `kleene_21` | . | . | . | . | . | - |
| `kleene_22` | . | . | . | . | . | - |
| `kleene_23` | . | . | . | . | . | - |
| `kleene_24` | . | . | . | . | . | - |
| `kleene_25` | . | . | . | . | . | - |

### Wiring (only new code)

Confirmed unmodified: training loop, `learning/config/` defaults, and
`learning/theories/propositional-logic.p`. Minimo dirty set after the gate is
exactly `learning/problems.py` and `learning/proofsearch.py`
(unexpected dirty: none).

Loader-only Peano surface fix: statements 23 and 24 in the extrinsic file use
`(not (not ['A -> 'B]))` forms the current Peano parser rejects. The loader
rewrites them to the equivalent `[[[...] -> false] -> false]` encoding so they
are searched (not skipped as parse errors). Theory file untouched.

Orchestration only (philosophia tree, no search logic):
`successor/dev/run_phase1_extrinsic_16.sh`,
`successor/dev/aggregate_phase1_extrinsic_16.py`.
Run log: `successor/dev/phase1_extrinsic_16_run.log`
(also copied to `PHASE1_EXTRINSIC_16_run.log`).

#### Diff: `minimo/learning/problems.py`

```diff
diff --git a/learning/problems.py b/learning/problems.py
index ea36a05..7ef8e45 100644
--- a/learning/problems.py
+++ b/learning/problems.py
@@ -1,10 +1,13 @@
 #!/usr/bin/env python3

 import collections
+from pathlib import Path

 import peano


+_LEARNING_DIR = Path(__file__).resolve().parent
+
 TheoremStatement = collections.namedtuple('TheoremStatement', ['name', 'statement', 'premises'])


@@ -367,9 +370,72 @@ empty : type.
     )


+def _normalize_kleene_statement(statement: str) -> str:
+    """Peano surface fix for two Kleene encodings that do not parse as written.
+
+    Double-negation of an implication written as (not (not ['A -> 'B])) is
+    rejected by the current Peano parser. The equivalent encoding
+    [[[...] -> false] -> false] parses. Same Kleene proposition; loader-only.
+    """
+    exact = {
+        (
+            "[('A : prop) -> ('B : prop) -> [(not (not ['A -> 'B']))] -> "
+            "[(not (not 'A)) -> (not (not 'B))]]"
+        ).replace("['A -> 'B']", "['A -> 'B]"): (
+            "[('A : prop) -> ('B : prop) -> [[['A -> 'B] -> false] -> false] -> "
+            "[(not (not 'A)) -> (not (not 'B))]]"
+        ),
+        (
+            "[('A : prop) -> ('B : prop) -> ('C : prop) -> [(not (not ['A -> 'B']))] -> "
+            "[(not (not ['B -> 'C']))] -> [(not (not ['A -> 'C']))]]"
+        ).replace("['A -> 'B']", "['A -> 'B]").replace(
+            "['B -> 'C']", "['B -> 'C]"
+        ).replace("['A -> 'C']", "['A -> 'C]"): (
+            "[('A : prop) -> ('B : prop) -> ('C : prop) -> "
+            "[[['A -> 'B] -> false] -> false] -> "
+            "[[['B -> 'C] -> false] -> false] -> "
+            "[[['A -> 'C] -> false] -> false]]"
+        ),
+    }
+    return exact.get(statement, statement)
+
+
+def load_kleene_propositional_logic_extrinsic():
+    """Kleene Theorem-41 statements on the training propositional-logic theory.
+
+    Uses learning/theories/propositional-logic.p (same axiom names the agent
+    trained on) and learning/extrinsic/propositional-logic.p. This is not the
+    Lean-library logic problemset, whose action names differ.
+    """
+    theory = (_LEARNING_DIR / 'theories' / 'propositional-logic.p').read_text(encoding='utf-8')
+    premises = [
+        'and_i', 'and_el', 'and_er', 'or_il', 'or_ir', 'or_e', 'not_i', 'not_e',
+        'exfalso', 'iff_i', 'iff_el', 'iff_er', 'em',
+    ]
+    statements: list[TheoremStatement] = []
+    for line in (_LEARNING_DIR / 'extrinsic' / 'propositional-logic.p').read_text(
+        encoding='utf-8'
+    ).splitlines():
+        line = line.strip()
+        if not line or '. ' not in line:
+            continue
+        label, statement = line.split('. ', 1)
+        statement = _normalize_kleene_statement(statement)
+        statements.append(TheoremStatement(f'kleene_{label}', statement, []))
+    if not statements:
+        raise RuntimeError('no Kleene extrinsic statements loaded')
+    return ProblemSet(theory, premises, statements)
+
+
 def load_problemset(problemset_id) -> ProblemSet:
     if problemset_id in ('lean-library-logic', 'logic'):
         return load_lean_library_logic_problemset()
     elif problemset_id in ('natural-number-game', 'nng'):
         return load_natural_number_game_problemset()
+    elif problemset_id in (
+        'kleene',
+        'propositional-logic-extrinsic',
+        'kleene-propositional-logic',
+    ):
+        return load_kleene_propositional_logic_extrinsic()
     raise ValueError(f'Unknown problem set {problemset_id}')
```

#### Diff: `minimo/learning/proofsearch.py` (`evaluate_agent` only)

```diff
diff --git a/learning/proofsearch.py b/learning/proofsearch.py
index d405156..98a8068 100644
--- a/learning/proofsearch.py
+++ b/learning/proofsearch.py
@@ -1321,13 +1321,29 @@ def evaluate_agent(config: DictConfig, agent=None):
     if agent is None:
         agent = make_agent(config)

+    # Extrinsic budgets: checkpoints are trained at 1000; override from config.
+    if config.agent.get('max_mcts_nodes') is not None:
+        agent._max_mcts_nodes = int(config.agent.max_mcts_nodes)
+    elif config.agent.get('expansions') is not None:
+        agent._max_mcts_nodes = int(config.agent.expansions)
+
+    if hasattr(agent, '_policy') and hasattr(agent._policy, '_lm'):
+        agent._policy._lm.eval()
+
+    seed = int(config.get('seed', 0))
+    random.seed(seed)
+    np.random.seed(seed)
+    torch.manual_seed(seed)
+
     problemset = problems.load_problemset(config.problemset)

     begin = config.get('begin', 0)
     end = config.get('end', len(problemset))
+    records = []

     for problem in problemset.problem_names()[begin:end]:
         print('Attempting problem:', problem)
+        t0 = time.time()
         try:
             result = agent.proof_search(problem, problemset.initialize_problem(problem))
         except KeyboardInterrupt:
@@ -1336,13 +1352,45 @@ def evaluate_agent(config: DictConfig, agent=None):
             print('Error!')
             import traceback; traceback.print_exc()
             result = ProofSearchResult(problem, False, None, [], 0)
+        elapsed = time.time() - t0
         print('Success?', result.success)
+        print('Elapsed_s', round(elapsed, 3))
+
+        records.append({
+            'problem': problem,
+            'success': bool(result.success),
+            'agent_iterations': int(result.iterations),
+            'elapsed_s': elapsed,
+            'mcts_budget': int(agent._max_mcts_nodes),
+        })

         if result.success:
-            problemset.mark_as_solved(problem, add_to_library=False)
+            problemset.mark_as_solved(problem, add_to_library=bool(config.get('accumulate_library', False)))

     print(f'Solved {len(problemset._solved)}/{len(problemset)}')
-    print(f'Solved problems: {", ".join(problemset._solved)}')
+    print(f'Solved problems: {", ".join(problemset.solved())}')
+
+    results_path = config.get('results_path')
+    if results_path:
+        payload = {
+            'problemset': str(config.problemset),
+            'agent_path': str(config.get('agent_path')),
+            'seed': seed,
+            'mcts_budget': int(agent._max_mcts_nodes),
+            'accumulate_library': bool(config.get('accumulate_library', False)),
+            'begin': int(begin),
+            'end': int(end),
+            'n_problems': len(records),
+            'n_solved': len(problemset._solved),
+            'success_rate': len(problemset._solved) / max(1, len(records)),
+            'mean_elapsed_s': float(np.mean([r['elapsed_s'] for r in records])) if records else 0.0,
+            'records': records,
+            'solved': problemset.solved(),
+        }
+        with open(results_path, 'w', encoding='ascii') as out:
+            json.dump(payload, out, indent=2, sort_keys=True)
+            out.write('\n')
+        print('Wrote results to', results_path)


 def test_preconditions():
```

### Negative authorization

No ACTIVE/YOKED, no philosophia thesis claim, no library-growth arm, no
retraining, no post-hoc expansion or problem-set edits after seeing outcomes.
