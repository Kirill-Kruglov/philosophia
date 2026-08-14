# Phase-2 strict MINIMO interface contract v2

Status: driver technical contract, 2026-08-13. Applies to a cumulative patch
against MINIMO commit `6066f482c6752915ad21119f93dc162f4cb9db72`. No scientific
training or evaluation is authorized by this file.

## A. Explicit learner identity

The scientific constructor requires explicit `device`, `dtype`, `n_layer`,
`n_head`, `n_embd`, `n_positions`, vocabulary/token IDs, optimizer type and all
optimizer parameters. Missing or extra fields fail closed. Device availability
may reject the request but cannot select architecture. Startup computes a
canonical spec hash and checks parameter count. A checkpoint manifest stores the
same spec, parameter count, state-dict hash and optimizer-state hash; load rejects
any mismatch. Phase-1 checkpoints are not converted.

## B. One exact query codec

Every scientific policy/value/action/conjecture/selector/training string passes
through one pure codec. It accepts immutable ASCII plus explicit BOS/EOS policy,
constructs exact byte tokens, and rejects non-ASCII or `token_count > n_positions`
with a typed record containing query kind, artifact ID, byte count, token count
and limit. It never truncates, clips, elides, mutates, retries or edits caller
lists. Batch padding does not enter likelihood or length accounting.

Artifact IDs use the same codec/transport contract: exact nonempty ASCII with a
maximum of 512 bytes, implemented by the single
`phase2_codec.ARTIFACT_ID_MAX_BYTES` constant. Base and derived hierarchical IDs
are checked by the same validator; hierarchy growth past the bound typed-refuses.

This replaces all scientific-path behavior at:

- `format_state_query` 490-character elision;
- `_strs_to_token_ids` 490-character elision;
- `goals_logprob` 400-character mutation and undefined `goal` reference;
- `completion_logprob` character-index preamble mask and missing EOS;
- the dead `<500` assertion;
- any hidden trim used for batch admission.

Completion likelihood includes every completion byte and EOS once, excludes BOS
and every preamble byte, and is checked against a hand-computed reference.

All training examples are preflighted before the first optimizer mutation.
Overflow invalidates the pending disposable item or follows the future registered
whole-block rule; it cannot be skipped treatment-dependently.

## C. Full canonical action space

The scientific path materializes every Peano-enumerated action under a reachable
typed timeout. Each action must have a unique canonical ASCII serialization.
Duplicate serialization fails closed. The complete unique set is sorted by that
serialization before child construction. The old `MAX_ACTION_LENGTH` prefix
filter is unreachable from the scientific path. If any complete policy query for
an enumerated action overflows, the whole item refuses before search; siblings are
never silently deleted.

Acceptance is downstream invariance, not raw Rust-order equality: shuffled or
fresh-process upstream enumerations with the same unique action set must yield
identical ordered actions, child states, policy queries and search record.

## D. Exact search accounting

Every MCTS call reports at least:

- `entered_tree_policy_iterations`: incremented once after the pre-iteration
  solved check for every entered budget iteration, including a dead traversal;
- `new_leaf_expansions`: incremented only when a previously unexpanded,
  nonterminal leaf is expanded successfully;
- `terminal_hits`, `dead_traversals`, `solved`, and the assigned cap.

Tests cover already-solved zero work, zero budget, first-iteration success,
success on the final allowed iteration, exhaustion exactly at `B`, dead traversal
without leaf expansion, and conservation of the diagnostic categories. The old
field name `mcts_expansions` is not used by the Phase-2 scientific schema.

## E. Prospective correctness repairs

- Hindsight conjecture examples use `d.elaborate(h.statement)`, never the parent
  problem. A fixture with distinct parent/hindsight statements must fail on the
  upstream bug and pass after repair.
- Config spelling is single-source and tested; `max_pos_neg_ratio` cannot silently
  fall back to `max_positive_negative_ratio=10`.
- `wandb` and all network effects are disabled on the scientific route.
- No Celery/distributed worker path is reachable.

These repairs mean Phase 2 is a prospective fork, not stock-MINIMO replication.

## F. Deterministic runtime preflight

The future scientific harness launches fresh single-process branch workers with
`PYTHONHASHSEED` set before interpreter start; Python/NumPy/Torch keys are
domain-separated and recorded; Torch deterministic algorithms and one BLAS/
OpenMP thread are required; unsupported kernels fail before data. Sets and dicts
that feed examples/actions are canonicalized. Mutable global RNG call order is
not an identity scheme.

Stage A need only prove deterministic construction, exact query/action behavior,
and fresh-process search replay on synthetic fixtures. Byte-identical optimizer
and full branch replay are later harness gates, after deterministic keyed batch
sampling exists.

## G. Stage-A acceptance

1. Unit/boundary tests for A-E all pass.
2. Two fresh processes reproduce a complete synthetic search record byte for
   byte despite deliberately shuffled upstream action enumeration.
3. The historical 755/767-character route is either admitted whole under an
   explicit large-enough test spec or typed-refused; never truncated.
4. Source/call-graph tests show the scientific path cannot reach CUDA-selected
   architecture, truncation, prefix action deletion, global mutable sampling,
   network logging or distributed execution.
5. The cumulative patch applies with ordinary `git apply --check` to the pinned
   clean commit and its complete test suite passes there.

Stage A does not select the final architecture/context, train a learner, generate
a carrier, qualify a selector, or expose a scientific outcome.
