**Item 2 stopped.** 16B/16C/16D records have no host-independent per-problem search-cost counter.

### 1. Cost counter
| field | where | unit | host-independent search cost? |
|---|---|---|---|
| `agent_iterations` | checkpoint JSON (`proofsearch.py`) | outer agent actions | **No** — always `0` on success, `1` on exhaustion |
| `elapsed_s` | checkpoint JSON | wall seconds | **No** |
| `mcts_budget` | checkpoint JSON | loop ceiling (8000) | **No** (cap, not used cost) |
| `mcts_expansions` | — | — | **Absent** from these artifacts |

**Smallest next instrumentation:** write `mcts_expansions` (= sum of `MonteCarloTreeSearch.evaluate`’s `n_entered`) into each JSON record. Do not use `elapsed_s` or tqdm.

### 2. Paired cost
`STOPPED` — no numerator/denominator available.

### 3. Solved sets @8000 (`[11, 19, 11, 11, 13]`)

| ck | n | solved |
|---:|---:|---|
| 0 | 11 | `1, 10a, 10b, 11, 16, 17a, 17b, 18a, 18b, 19, 20` |
| 1 | 19 | ck0 ∪ `{2, 3, 4, 5, 6, 7, 8b, 13}` |
| 2 | 11 | = ck0 |
| 3 | 11 | = ck0 |
| 4 | 13 | ck0 − `{20}` ∪ `{3, 6, 7}` |

**ck1 → ck2 losses (8):** `kleene_2, 3, 4, 5, 6, 7, 8b, 13`.

### 4. Clustering (16C run log only)
| thm | stmt chars | proof print lines | tqdm last /8000 |
|---|---:|---:|---:|
| 2 | 85 | 12 | 4157 |
| 3 | 87 | 10 | 4197 |
| 4 | 88 | 11 | 7854 |
| 5 | 88 | 12 | 2274 |
| 6 | 87 | 12 | 4733 |
| 7 | 87 | 12 | 4945 |
| 8b | 89 | 17 | 7007 |
| 13 | 68 | 12 | 6324 |

Only `kleene_4` has tqdm ≥7500 — not “all eight just under the cap.” No first-branching traces. **`NOT_DECIDED_BY_LOGS`** among the three readings. (tqdm is timer-refreshed, not a recorded counter.)

### Artifacts
- `successor/dev/phase1_17_paired_cost.py` (137 lines)
- `successor/dev/phase1_17_paired_cost_results.json`  
  Status: `DESCRIPTIVE_ONLY__NO_VERDICT_TOKEN`; raw/LF SHA-256 for all inputs + script inside the JSON.

**Questions**
1. Should the first real paired-cost table be built from Phase-17’s already-instrumented `mcts_expansions` JSONs, or only from a fresh 16B/C-style re-run?
2. For pipeline quality: pin a schema check that refuses any analysis claiming “search cost” unless `mcts_expansions` is present on every record?
