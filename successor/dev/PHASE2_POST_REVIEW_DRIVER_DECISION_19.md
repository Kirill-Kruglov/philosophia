# Philosophia Phase 2 post-review driver decision 19

Status: driver decision after independent Sol 5.6 and Opus 5 review,
2026-08-13. This narrows and supersedes conflicting parts of the earlier `/tmp`
drafts. It does not authorize scientific training or outcomes.

## 1. Phase 1 is terminal

Accepted commit: `philosophia@b0b9adf`.

The Builder's first terminal table was not accepted: the historical MINIMO
field stored the zero-based MCTS loop index on every exit, so every one of the
150 records required `raw+1`, not only `7999 -> 8000`. The accepted package:

- reconstructs exact entered MCTS-loop iterations for every record;
- does not call them exact new-leaf expansions;
- checks the one-invocation route and `_max_searches=1`;
- reports the bounded Peano action-order variation without assigning sole
  causality;
- makes no interval, population, SELF/YOKE, or Philosophia claim.

The live MINIMO checkout remains a disposable dirty research dependency. Its
reproducible Phase-1 delta is committed as a patch against upstream commit
`6066f482c6752915ad21119f93dc162f4cb9db72`; it is not pushed to the upstream
MINIMO repository.

## 2. Phase-2 verdict

`REVISE_BEFORE_IMPLEMENTATION`, not `KILL_ROUTE`.

The admissible core is a reciprocal parallel 2x2 factorial block on exact
learner twins. For recipient state `r` and task-batch source `q`, the primary
block contrast is

`D_j = mean_g[(X_A<-B - X_A<-A + X_B<-A - X_B<-B)/2]`,

with registered stratum weights. Positive `D_j` favors state-matched task
selection. Additive recipient competence and additive batch quality cancel
algebraically. One independently initialized twin pair with all four valid
branches is one independent unit; theorems are repeated measurements.

The construct is **self-calibrated task selection from a supplied verified
reservoir**. It is not autonomous conjecture invention, theorem discovery,
information acquisition, or physical sensor learning. The claim is conditional
on one sealed finite theorem frame and the frozen learner/selector/prover.

The MINIMO-compatible treatment is one frozen-state selected task batch followed
by one aggregate update. It is not an ordered sequential curriculum. Arms have
equal assigned proof budgets and update ceilings; realized proof work and
example volume may differ and must be reported as protocol mediators.

## 3. Accepted review findings

1. A separate scientific harness is required. The repository runner is not
   branch-isolated or deterministically keyed.
2. Architecture is pinned twice: required fail-closed config fields and a
   checkpoint/manifest fingerprint. CUDA availability may validate a requested
   device but never choose the learner.
3. All policy, value, action, conjecture, selector and training strings use one
   exact ASCII encoder. No silent truncation or surface action deletion survives
   on the scientific path.
4. Unique action identities are canonically sorted before children are built.
   Raw Peano order need not be stable; semantic set equality plus canonicalized
   downstream bytes must be stable.
5. Search records both entered MCTS iterations and successful new-leaf
   expansions. Before calibration, v2 fixes capped entered MCTS iterations as
   primary because they are the algorithm's assigned budget unit; leaf
   expansions, exact LM-query work and solve rate are mandatory companions and
   cannot replace the primary after outcomes.
6. Fix the upstream hindsight statement bug (`h.statement`) before any Phase-2
   learner is trained. Phase-1 checkpoints cannot qualify the repaired selector.
7. Replace the proposed mean-logprob selector with proper equal-prior label
   posterior log-odds on the exact public `d.elaborate(g)` bytes, including EOS:
   total `L_hard - logsumexp(L_triv,L_easy,L_fail)`. Rank/quantile normalize
   within structural stratum before item-addressed Gumbel selection.
8. Qualify that selector only on disposable, split-disjoint data: correct sign,
   predictive value beyond statement-only surface features, stable elaboration,
   scale parity, identical-state equality, and nondegenerate acquired-state
   divergence. Failure closes this selector route; no post-outcome replacement.
9. Carrier splits are canonical rule-skeleton-disjoint. Run a complete
   subformula-bounded normal-form prover and a statement-only difficulty
   regressor before accepting a frame. The claim remains instrument-relative if
   a complete prover makes the generated fragment cheap.
10. Whole-block retry, attrition ledger, no replacement seeds, worst-case missing
    `D_j` bounds, balanced branch/evaluation order, sealed outputs, and block-level
    inference are mandatory.
11. A synthetic injected-coupling fixture must prove that the harness and
    analysis can recover a known positive interaction before a null can support
    a bounded kill.
12. Pin a signed total compute envelope only after measuring one complete
    disposable block. Phase-1 post-hoc ck1 magnitude/variance does not size Phase 2.

## 4. Findings not adopted as extra scientific arms

### NOISE-YOKE

Not added. The primary route requires deterministic algorithms, isolated
counter-keyed randomness, and the metamorphic invariant: same serialized state
plus same task batch yields byte-identical examples, optimizer state, weights,
and evaluation. Under that contract there is no independent optimizer/dropout
noise arm to estimate. If exact replay fails, the current design is invalid and
returns to statistical review; it is not repaired by adding an arm.

### COLD-SELF

Not added. Exact cold twins score the same common reservoir under the same
treatment variates and therefore select the same batch; the reciprocal
interaction is identically zero. This is retained as an executable
zero-divergence control, not an additional scientific treatment.

### SURFACE-YOKE

Not added as a fifth treatment arm. Surface explanations are handled before the
scientific run by structural-stratum matching, a statement-only predictor, and
the selector's required incremental predictive value beyond length/connective/
n-gram features. Failure closes the selector.

### Data-driven classical-versus-intuitionistic choice

Not adopted. The primary world remains the standalone declared intuitionistic
fragment because it is the prospectively chosen constructive-composition
construct and excludes unused declarations from substitutions. The old 490-byte
failure is not its justification. Classical logic may be reported as a boundary
probe, but no performance comparison selects the primary theory after outcomes.

## 5. Immediate execution order

1. **Stage A:** strict model/query/action/accounting/hindsight instrument repair,
   tests only. No training and no carrier.
2. Independent code review of the Stage-A patch; one scoped repair if a concrete
   counterexample survives.
3. **Stage B:** erased-proof-plan carrier generator/compiler/checker and public
   shortcut audits, using only uniform/cold calibration.
4. **Stage C:** repaired-from-scratch learner and selector qualification on
   disposable blocks.
5. Only then freeze the reciprocal harness, margins, frame, block count and
   statistical analysis.

The Kleene loader rewrite is Phase-1-only and is not a Phase-2 parser prerequisite.
