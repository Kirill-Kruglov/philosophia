# Phase-2 Stage A X/Y V4.2 disposition 19

Status: `STAGE_A_POST_XY_REPAIR_REQUIRED_V4_2`. Date: 2026-08-14.

Both independent reviewers returned `REVISE_STAGE_A_V4_2`. The driver
reproduced the five release-relevant counterexamples below in a fresh patched
tree. V4.2 is not accepted and Stage B remains closed.

## Reproduced blockers

1. **Zero assigned work is misclassified.** A valid real nat-add job with
   `budget=0` reaches a correct zero-work search record, then
   `primitive_item_evidence` requires an expansion and returns
   `INTERNAL_ERROR`. Zero is an explicitly admissible cap and needs a valid
   evidence record with empty expansion/query fields.
2. **The closed spec is numerically open.** `optimizer_lr=NaN`, boolean epsilon,
   negative weight decay, and betas outside `[0,1)` all pass
   `validate_scientific_spec`. Constructor failure then occurs after spawn and
   Peano reconstruction. Exact numeric types, finiteness and optimizer domains
   must be validated in the parent.
3. **Learner initialization has no identity.** Two constructions from one spec
   have equal spec hashes but different `state_dict_hash` values. A required
   exact `init_seed` must be spec-hashed, and model construction must use it in
   a scoped RNG context that restores ambient Torch RNG state. A real
   multi-iteration fresh-process item must replay byte-identically.
4. **PyO3 panic escapes the envelope.** The reviewed free-variable nat-add goal
   raises `pyo3_runtime.PanicException`, a `BaseException`, so the child writes
   no result and the parent cannot distinguish a formal Peano refusal from an
   infrastructure crash.
5. **A Peano-backed proxy bypasses containment.** The synthetic fallback reads
   `leaf.state_node.actions`; a non-`TreeSearchNode` wrapper around a real
   `HolophrasmNode` therefore enumerates Peano in the parent and stages strings.

## Adopted bounded strengthening

- Validate public synthetic `action_timeout_s` at construction with the same
  positive-finite rule.
- Preserve derived artifact-ID overflow as a dedicated closed envelope terminal
  because later attrition accounting must distinguish it from semantic action
  refusal.
- Reject completion likelihood when `bos=False` leaves no causal logit before
  the first completion token; never permit a negative wrapped index.
- Before reporting timeout, accept an already atomically installed result file
  even if the child is still in interpreter teardown; cleanup may then kill the
  remaining process. A genuinely result-less nonzero exit gets a distinct
  `IsolatedChildCrash` with exit code.
- Add a faithful search fixture in which creating a terminal child does not
  itself mark the root solved. Existing counter code is accepted; the fixture
  strengthens production-semantic evidence.
- Remove silent `**_ignored` internal scientific kwargs while touching the
  boundary.

## Findings not treated as new Stage-A blockers

- Full optimizer/training branch replay, keyed batch sampling and trained
  checkpoint transport remain later harness obligations.
- Source/AST exclusion tests remain indirect evidence; independent manual call
  graph inspection found no live RNG/network/distributed call on the current
  scientific route.
- Child construction before child-query preflight is necessary to obtain child
  states and remains allowed; mutation commits only after complete preflight.
- The Phase-1 Kleene normalization and legacy ratio behavior are recorded but
  are not Phase-2 repair surfaces.
- The underscore marker remains trusted in-tree call-graph discipline, not a
  sandbox against malicious Python imports or arbitrary caller code.

V4.3 is the one scoped post-X/Y repair allowed by the execution order. After
local verification it receives bounded confirmations against this disposition,
not a reopened design review.
