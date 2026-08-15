I'll start by reading all the required files in parallel.

Now the audit-14b governing artifacts.

Now the implementation. Let me read the Python file and skim the results JSON structure.

Let me read the remaining context files.

I have everything needed. Producing the adjudication.

# AUDIT14B_ROUTE_ADJUDICATION_V1

Read-only. Every code claim cites `wallb_policy_channel_audit_14b.py` (abbrev. `14b.py`).

## 1. Existing versus assumed machinery

Decomposition of the audit-14b implementation against the seven requested primitives:

| Primitive | Status | Evidence |
|---|---|---|
| Learner state | **EXISTS (single, not twinned)** | `LinearRanker.weights` — a `FEATURE_DIM` float vector (`14b.py:384-395`). One ranker per presentation, `LinearRanker.zero()` then one `fit` (`14b.py:481-482`). |
| Search-ranking policy | **EXISTS** | `ranker_score_fn` (`14b.py:672-684`) feeds the candidate sort key `(-score, …)` inside `bidirectional_best_first` (`14b.py:606`, `647-651`). Ranks neighbor moves *within one goal's search*. |
| Task/contact selector | **MISSING** | No object selects which tasks a learner trains on. `train_ranker_from_panel` consumes the **entire** relevance panel unconditionally (`14b.py:477-480`). There is no reservoir scoring, no batch choice, no state-conditioned selection. |
| Source of training labels | **EXISTS (oracle path)** | `collect_examples` labels a neighbor `1` iff it is the next word on the goal's stored ground-truth witness path (`14b.py:465`); paths are generated at panel-build time by `sample_goal` (`14b.py:342-363`). Labels are oracle solution steps, not learner-discovered. |
| Acquired contact batch | **MISSING** | Nothing is acquired as a function of state. Training set is the fixed relevance panel (`14b.py:472-483`). |
| Learner update | **EXISTS as from-scratch fit only** | `LinearRanker.fit` runs SGD from zero once (`14b.py:397-435`). There is **no** aggregate update applied to an *inherited* twin state after a batch is selected. |
| Held-out endpoint | **EXISTS** | Evaluation-panel work: `evaluate_arm` on `panels["evaluation"]` returns ISWU costs (`14b.py:1218-1224`); disjointness enforced by `occupied_pairs` in `build_panels` (`14b.py:958-965`). Restricted-mean/solve-rate via `paired_metrics` (`14b.py:1032-1061`). |

So of the seven, **three are missing** (selector, acquired batch, inherited-state update) and the learner exists only as a solo, oracle-trained ranker. These are the load-bearing primitives of the reciprocal estimand.

## 2. Ranking-policy versus task-selection data flow

SCIENTIFIC_CONTRACT_V1 **conflates** the two. Data-flow proof by tracing the only path `weights` take:

`LinearRanker.weights` → `ranker_score_fn` (`14b.py:672`) → `score_fn(word, position, action, neighbor, root)` → consumed **only** by `run_search` candidate ordering (`14b.py:647-651`, `606`). The ranker output influences *the order in which neighbor words are expanded inside a single goal's bidirectional search*. It never touches panel membership: the training panel (`14b.py:477-480`) and the evaluation panel (`14b.py:1218-1224`) are fixed by `build_panels` before any ranker exists.

The contract's B — "one selected batch followed by one aggregate update … reciprocal block contrast `D_j` on held-out evaluation-panel search work" — requires an object that maps *learner state → choice of training tasks from a shared reservoir*. Audit-14b contains no such map. "Ranking candidate search actions inside one goal" (present) and "selecting training tasks for a learner from a reservoir" (absent) are distinct data-flow objects, and the contract silently treats the first as if it discharged the second. Confirmed conflation.

## 3. Twin-state feasibility

Two 14b rankers **cannot** serve as exact learner twins whose different acquired states drive meaningfully different task selections, for three compounding reasons:

1. **No selection channel to diverge on.** State reaches only within-goal move ordering (§2), not task choice. There is nothing for divergent states to select *differently*.
2. **Convex objective collapses divergence.** `fit` is L2-regularized logistic regression (`14b.py:397-435`); its optimum is unique. `seed` perturbs only minibatch order (`14b.py:409,414-417`). Two twins trained on the same relevance panel converge to essentially one weight vector — near-zero divergence by construction.
3. **The only divergence source is forbidden.** The sole training signal is oracle witness-path membership (`14b.py:465`) — i.e. the evaluation-witness the estimand must not leak. Any divergence a 14b ranker could show is divergence in fitting oracle path labels, exactly the leakage Q3 excludes. A zero-init ranker scores all candidates 0 (`14b.py:481`, `394-395`), which is the COLD-SELF identity-selection case (driver §COLD-SELF).

So state-divergence that is simultaneously *meaningful* and *not from witness leakage* is unavailable in this cell. This is the crux: 14b's learning signal *is* the oracle answer.

## 4. 12/40 conditioning

The 12 SCREEN_QUALIFIED presentations (`WALLB_POLICY_CHANNEL_AUDIT_14B.md:71`) were selected because TREATMENT (ranker order) beat CONTROL under Holm + bootstrap (`14b.py:1363-1374`), where TREATMENT ordering derives from a ranker trained on oracle path labels.

- **Legitimate for the bounded claim?** Only if preregistered as an explicit *conditioning event* and the claim is stated conditionally. It is not a fresh random draw.
- **Outcome-dependent carrier selection?** **Yes.** The family is chosen on a measured outcome of the policy channel (`solve_rate_difference`, bootstrap lower bound, `14b.py:1363-1372`). Any subsequent effect estimated on this subset is conditioned on prior policy responsiveness, and the 0.300 prevalence / Wilson interval (`WALLB_...14B.md:71-73`) cannot transfer to it.
- **Narrowest claim authorized:** "Conditional on presentations pre-screened for oracle-ranker responsiveness, …" — a conditional existence statement. No prevalence, no unconditional transfer, and — because 14b's screen responds to *oracle* ordering, not self-state — not even clean evidence that a *self-state* selector would be responsive on the same 12.

## 5. Selection / transfer / history capability table

| Capability | Verdict | Basis |
|---|---|---|
| A. Reciprocal own-state selection | **REQUIRES_NEW_DESIGN** | Selector, acquired batch, inherited-state update all MISSING (§1); twins cannot diverge without oracle leakage (§3). |
| B. Transfer to fresh presentations | **REQUIRES_NEW_DESIGN** | Within-presentation held-out exists (`14b.py:1218-1224`); cross-presentation transfer of an *acquired* state, under a retained record, is not built and presupposes A. |
| C. Truthful vs false history beyond weights | **IMPOSSIBLE_IN_THIS_CELL** | No ledger/record object exists anywhere in `14b.py`; the contract itself concedes the equational library carrier is closed sparse (2/40) and "cannot host S's retention arms" (TASK_A §5). |

None is EXISTS.

## 6. Incremental effort

To reach **one disposable reciprocal block**, the following must be built new (existing search-frame code is reused but does not count):

1. A task **reservoir with solvability witnesses** decoupled from the training-label source.
2. A **state-conditioned selector** scoring reservoir tasks — and, critically, one whose signal is *not* the oracle witness path (the driver's whole reason for routing to `elaborate(g)` log-odds selection in MINIMO, driver §3.7). In the equational cell the only demonstrated per-state signal is oracle path fit; a non-oracle selector here risks being a pure surface predictor, which the contract's own control closes (TASK_A §3 "statement-only surface predictor").
3. **Twin instantiation with inheritable state** and an **aggregate-update primitive** on inherited weights (neither exists; `fit` is from-zero, `14b.py:481-482`).
4. **Branch isolation** for the 2×2 (driver §3.1 — repo runner is not branch-isolated).
5. **Injected-coupling positive control** and **state-divergence gate** (driver §3.11; contract §7 Gate 0/1).
6. Reciprocal `D_j` estimator + attrition/worst-case bounds.

Estimate: **MEDIUM (4–10 days) at best, with a live risk of IMPOSSIBLE-in-cell** at item 2 — the selector is the scientific object, and the equational cell offers no self-state signal distinct from the oracle answer. The contract's "hours" figure (§7 Gate 0) is not reachable: a state-divergence probe presupposes twins + selector that do not exist, so it cannot be the *first, cheap* measurement.

## 7. Scientific value

Task B fixes the residual novelty as the **conjunction**: reciprocal own-state selection **and** truthful-history-beyond-weights, on held-out families (NOVELTY_RESIDUE line). This cell can host **none** of that conjunction: history is IMPOSSIBLE here (§5C), transfer and reciprocal selection both REQUIRE_NEW_DESIGN, and the reciprocal mechanism cannot even be exercised without a non-oracle selector the cell may not admit.

Versus Task C: Task C sizes the thin MINIMO min-slice at **MEDIUM if L4 closes / LARGE otherwise** and recommends STOP_UNTIL_SCIENTIFIC_CONTRACT (ENGINEERING_ROUTE line). The audit-14b reciprocal is **not** cheaper: it shares MINIMO's central unsolved risk — a state-conditioned selector with incremental value beyond surface features — while adding the specific handicap that 14b's existing signal is the oracle path itself. Sunk calibration (the sweep, the 12/40 screen) is not a decision criterion (IDEA_GATE rule 5/6) and is excluded here.

## 8. Final disposition

The existing cell cannot test the full Task-B residual: history is impossible, transfer and reciprocal selection require new design (§5). Cheap validation of even the reciprocal *interaction* is blocked because the selector, inherited-state update, and acquired batch are all MISSING (§1) and twin divergence is unachievable without evaluation-witness leakage (§3). Obtaining one preliminary reciprocal estimate therefore requires constructing a substantially new learner/selector system at MEDIUM cost with a genuine IMPOSSIBLE-in-cell risk on the selector (§6). This is not the DISPOSABLE_GATE_ONLY case (nothing reciprocal is *cheaply* validatable) and not SCIENTIFIC_PRIMARY (the residual is unhostable). It matches the third rule exactly.

AUDIT14B_ROUTE=NOT_CHEAP_OR_NOT_COHERENT
