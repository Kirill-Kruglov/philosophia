## Findings

### Critical — release blockers

1. **The public process boundary cannot represent the valid zero-budget terminal state.**

   `budget=0` is explicitly accepted ([phase2_isolated.py:256](/tmp/minimo_stagea_x_audit_20260814/learning/phase2_isolated.py:256)), and core MCTS correctly returns a zero-work record. The child then requires a canonical expansion to construct evidence and raises if none exists ([phase2_isolated.py:292](/tmp/minimo_stagea_x_audit_20260814/learning/phase2_isolated.py:292)). Consequently, a real public nat-add job with budget zero returned:

   ```text
   IsolatedJobError:
   isolated child INTERNAL_ERROR RuntimeError:
   isolated item produced no canonical expansion
   ```

   This collapses two admissible states—valid zero assigned work and an internal instrumentation fault—into the same terminal envelope. The existing test checks only job construction, not public execution ([test_phase2_root.py:651](/tmp/minimo_stagea_x_audit_20260814/learning/test_phase2_root.py:651)).

   Repair the evidence schema to permit a record with no canonical expansion, empty action/query evidence, `entered_tree_policy_iterations=0`, `new_leaf_expansions=0`, and the correct solved status. Test it through `run_isolated_scientific_item`, not merely `make_scientific_item_job`.

2. **The purportedly closed scientific spec accepts invalid and non-exact optimizer parameters before spawn.**

   The validator coerces learning rate, epsilon, weight decay, and betas with `float(...)`, but does not reject strings, booleans, NaN, infinity, negative values, or invalid beta ranges ([phase2_spec.py:172](/tmp/minimo_stagea_x_audit_20260814/learning/phase2_spec.py:172)). I independently supplied `optimizer_lr=NaN`:

   - `validate_scientific_spec` accepted it;
   - `make_scientific_item_job` accepted it and stored `nan`;
   - the public process spawned;
   - the child reconstructed `PyProofState` before model construction ([phase2_isolated.py:346](/tmp/minimo_stagea_x_audit_20260814/learning/phase2_isolated.py:346));
   - AdamW then rejected it, producing `INTERNAL_ERROR ValueError`, not `IsolatedInvalidSpec`.

   This directly contradicts full spec validation before spawn and before Peano. Require exact numeric types excluding bool, finiteness, and optimizer domains—at minimum \(lr\ge0\), \(\epsilon>0\), weight decay \(\ge0\), and \(0\le\beta_i<1\)—in `validate_scientific_spec`. Other constructor-semantic spec failures must likewise become typed pre-Peano spec refusals.

### Major

3. **The counter implementation is correct, but the success-boundary fixtures use non-Peano solved semantics.**

   Core accounting is sound: `entered` increments after the pre-iteration solved check; dead traversals, terminal hits, and successful nonterminal expansions are mutually distinguished ([phase2_search.py:90](/tmp/minimo_stagea_x_audit_20260814/learning/phase2_search.py:90)). However, `ScientificFakeNode.is_solved()` treats the mere existence of a terminal child as proof ([test_phase2_search.py:82](/tmp/minimo_stagea_x_audit_20260814/learning/test_phase2_search.py:82)). Real `TreeSearchNode` is not marked solved until the terminal child is traversed and propagates `mark_solved` ([proofsearch.py:349](/tmp/minimo_stagea_x_audit_20260814/learning/proofsearch.py:349), [proofsearch.py:417](/tmp/minimo_stagea_x_audit_20260814/learning/proofsearch.py:417)).

   Thus the named first/final-success tests ([test_phase2_search.py:223](/tmp/minimo_stagea_x_audit_20260814/learning/test_phase2_search.py:223)) are indirect for actual Peano success timing. Add a faithful production-control-flow fixture where expansion creating a terminal child does not itself solve the parent.

4. **Fresh-process replay evidence is only one-expansion canonicalization evidence.**

   Both replay tests use `ScientificFakeNode` and `budget=1` ([test_phase2_actions.py:95](/tmp/minimo_stagea_x_audit_20260814/learning/test_phase2_actions.py:95), [test_phase2_root.py:774](/tmp/minimo_stagea_x_audit_20260814/learning/test_phase2_root.py:774)). The random LM’s numeric outputs are omitted from the canonical record, and no policy-dependent second choice occurs. This proves canonical first expansion, not deterministic multi-step search construction.

   Section F remains `INDIRECT`. A bounded Stage-A repair is to use fixed model state/logits and enough iterations to force a policy-dependent choice, then compare state/manifest and record bytes across fresh processes. Full keyed training and optimizer/branch replay remain later harness obligations.

### Minor / non-blocking

5. **Collapsing `ArtifactIdLimitRefusal` to parent `ActionHandlingError` does not currently destroy required attrition evidence.**

   The child maps every `ActionHandlingError` subclass to `ACTION_HANDLING_REFUSAL` ([phase2_isolated.py:154](/tmp/minimo_stagea_x_audit_20260814/learning/phase2_isolated.py:154)); the parent reconstructs the generic class ([phase2_isolated.py:204](/tmp/minimo_stagea_x_audit_20260814/learning/phase2_isolated.py:204)). There is no present ambiguity between a valid result and a refusal: both artifact-hierarchy overflow and other action-handling failures invalidate the item/block under Stage A.

   It becomes insufficient only if the later attrition plan permits different retry, exclusion, or invalidation decisions for metadata-ID overflow versus semantic action-space failure. In that case, add a dedicated envelope code prospectively. Preserving the subclass now would be cleaner but is not itself a release blocker.

6. **Several cited tests are indirect evidence.**

   Source/AST assertions do not exercise production reachability: the no-truncation source scan, CUDA call-location scan, forbidden-import scans, hindsight bootstrap scan, ratio-resolver inclusion scan, capability-token scan, and textual before-Peano ordering checks. Mocked CUDA, parameter-count, logits, wandb, and process-context tests establish their local branch only. Synthetic node tests reach the production MCTS/action classes but not real Peano semantics.

   The real isolated nat-add test is direct production evidence for action-object identity, canonical ordering, child construction, preflight, and containment ([test_phase2_root.py:314](/tmp/minimo_stagea_x_audit_20260814/learning/test_phase2_root.py:314)).

## Work-quantity audit

| Boundary | Entered iterations | New-leaf expansions | Other category | Meaning |
|---|---:|---:|---:|---|
| Already solved before loop | 0 | 0 | 0 | No assigned iteration entered |
| Unsolved, budget 0 | 0 | 0 | 0 | Valid unsolved zero-work record |
| First iteration selects terminal leaf | 1 | 0 | terminal hit 1 | Proof recognized during traversal |
| First iteration expands nonterminal leaf | 1 | 1 | 0 | Successful expansion; not necessarily a proof |
| Terminal hit on final iteration \(B\) | \(B\) | Prior expansions only | terminal hit 1 | Solved at the cap |
| Exhaustion | \(B\) | At most \(B\) | remainder terminal/dead | Exactly assigned entered work |
| Dead traversal | +1 | +0 | dead +1 | Budget consumed without expansion |

For every successful record:

\[
\text{entered}
=
\text{new-leaf expansions}
+\text{terminal hits}
+\text{dead traversals}.
\]

Neither quantity is a substitute for the other. The public zero-budget defect occurs after this correct MCTS accounting.

## Codec and likelihood derivation

The codec constructs:

\[
[\mathrm{BOS}] + \text{ASCII payload bytes} + [\mathrm{EOS}],
\]

so an \(n\)-byte query has \(n+2\) tokens. A complete 767-byte historical query therefore requires 769 positions: it is admitted unchanged when `n_positions >= 769` and typed-refused at 512.

For preamble `AB`, completion `C`, uniform logits over 128 tokens, the included targets are exactly `C` and EOS. BOS and `A,B` are excluded. Therefore:

\[
L=\log(1/128)+\log(1/128)=-2\log 128
=-9.704060527839.
\]

The independent probe returned exactly that value and target-logit positions `(2, 3)`. Completion masking is correct ([phase2_codec.py:319](/tmp/minimo_stagea_x_audit_20260814/learning/phase2_codec.py:319)). Y/N scoring uses the last payload position, not EOS, and stable two-class `log_softmax` preserves float32/float64 dtype ([phase2_policy.py:15](/tmp/minimo_stagea_x_audit_20260814/learning/phase2_policy.py:15), [phase2_policy.py:34](/tmp/minimo_stagea_x_audit_20260814/learning/phase2_policy.py:34)).

## Contract classification

| Contract section | Grade | Basis |
|---|---|---|
| A. Explicit learner identity | `CONTRADICTED` | Architecture, dtype, parameter count, manifest and hashes work; optimizer-domain/type validation is not closed |
| B. One exact query codec | `PROVED` | Exact ASCII/BOS/EOS accounting, immutable callers, no truncation, correct completion mask, stable Y/N scoring and typed overflow |
| C. Full canonical action space | `PROVED` | Original Peano action objects are paired with unique serializations, sorted, staged, and fully preflighted before commit; duplicate/query/ID refusal is whole-item |
| D. Exact search accounting | `PROVED` | Production counter control flow is correct and quantities remain distinct; named real-success tests are indirect and need strengthening |
| E. Prospective correctness repairs | `PROVED` | `h.statement`, canonical ratio resolver, and scientific path exclusions are present; some exclusion evidence is source/call-graph based |
| F. Deterministic runtime preflight | `INDIRECT` | One-step synthetic replay does not exercise a policy-dependent fresh-process decision |
| G. Stage-A acceptance | `CONTRADICTED` | Patch integrity and 104-test gate pass, but A/public-boundary counterexamples survive |
| Public process boundary | `CONTRADICTED` | Deadline, file IPC, kill path, closed keys, real-node/subclass rejection and nat-add positive path work; zero budget and invalid optimizer specs are misclassified |

## Integrity and scope

- Base commit independently confirmed: `6066f482c6752915ad21119f93dc162f4cb9db72`.
- Patch SHA-256 independently confirmed: `8eba7e14651c7604b72ce3f447462359b74d38119782c29541005b8136dc2bf7`.
- `git apply --check`, application, `git diff --check`, and compilation succeeded in the clean `/tmp` clone.
- All 104 declared tests passed there using the existing dependency environment.
- CPU-debug identity independently reproduced: spec hash `80041c…057`, parameter count `478720`.
- No source, carrier, model, training data, or scientific outcome was created or changed.

Checkpoint transport and content-addressed verification before Peano for a future trained branch remain mandatory later-harness work. They are correctly not required from Stage A or carrier Stage B.

REVISE_STAGE_A_V4_2
