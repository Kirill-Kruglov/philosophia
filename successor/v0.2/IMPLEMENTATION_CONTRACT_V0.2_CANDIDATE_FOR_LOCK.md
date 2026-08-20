# Implementation contract v0.2 — candidate for lock

**Status:** CANDIDATE FOR LOCK — part of preregistration v0.2

This document closes implementation choices capable of silently changing the scientific manipulation.

---

## 1. Configuration is single-source and explicit

No trajectory-relevant value may come from an implicit default.

Final machine-visible config must contain at minimum:

- preregistration version/root hash;
- git SHA;
- environment hash;
- `MODEL_CONFIG_REF` + SHA256;
- selected M/module pool;
- train fraction;
- B_history;
- tau;
- evaluation interval/criterion;
- arm/stage;
- replicate seed and namespace roots;
- batch size/LR/WD/optimizer/dtype;
- positional encoding type/max-position handling;
- batch policy (full batch / explicit size), gradient accumulation, drop-last semantics;
- CPU thread count/device/backend/deterministic flags;
- heavy-cap threshold;
- conditional SHUFFLED_TAG policy.

---

## 2. P-1 model config provenance

`MODEL_CONFIG_REF` resolves to an **ordered file set** inside the Level 0 subtree `src/philosophia/level0/`, not to a single file, because the architecture is not in `config.py`:

1. `config.py` — widths, optimizer constants, frozen class definitions;
2. `model.py` — block structure, parameter set, initialization draw order;
3. `data.py` — dataset construction and the inherited batch policy;
4. `train.py` — the optimization step and any inherited accumulation rule.

Record, in this order, each file's repository path and the SHA256 over its raw bytes, and record the reference root

`MODEL_CONFIG_REF_ROOT = SHA256(UTF8("model-config-ref-v0.2\n" + concatenation over the four files in order of "<name> <sha256>\n"))`

where `<name>` is the path relative to `src/philosophia/level0/`. The preregistration §6.1 form `<path>@<SHA256>` denotes the subtree root `src/philosophia/level0/` and this reference root.

Each implementation vendors the four files byte-for-byte into its own worktree and verifies the vendored copies against these hashes before building anything.

Resolve this before P0. If any of the four files cannot be recovered exactly, stop with `BLOCKED_CONFIG_PROVENANCE`.

No numerical reconstruction from prose or remembered settings is allowed.

Inherited numeric values are taken from the **paper-mainline arm**: `paper_mainline_arm()` in `config.py`, i.e. `weight_decay = 1.0`, together with the architecture and optimizer constants of `ModelConfig` / `RunConfig`. The artifact-fidelity arm (`artifact_fidelity_arm()`, `weight_decay = 0.1`) is not inherited and must not appear in any v0.2 configuration, artifact, or log. The Level 0 fixed-epoch schedules of either arm are replaced by the v0.2 budgets under preregistration §6.3 item 5.

The frozen Level 0 dataclasses `ModelConfig`, `RunConfig`, and `ArmConfig` are **not instantiated** by v0.2. Inheritance is by value: v0.2 reads the numeric field defaults and constructs its own configuration object around them. This is the single authorized route. Subclassing a frozen class, relaxing or monkey-patching a validator, and constructing with a frozen value that is then neutralized downstream are all forbidden, because they record different provenance for an identical trajectory. `configure_canonical_torch_runtime()` is likewise never invoked (preregistration §6.3 item 7).

---

## 3. Deterministic seed derivation

Canonical primitive:

`seed64(namespace, *fields) = first_8_bytes(SHA256(UTF8(preimage)))`, interpreted unsigned little-endian and masked to 63 bits, where

`preimage = "philosophia-alias-v0.2|" + namespace + "|" + "|".join(str(int(f)) for f in fields)`

All integers are rendered base-10, unpadded, with no sign. The separator is `|` in both positions. There is no trailing separator.

Derivation is two-level and this is mandatory.

**Stage namespaces** (level 1): `calibration`, `power-pilot`, `confirmatory`, `deterministic-replay`.

**Role namespaces** (level 2): `world-order`, `pair-split`, `batch-order`, `model-init`, `context-code`, `shuffled-tag`.

For a replicate at index `i` of stage `S`:

1. `replicate_seed = seed64(S, i)`;
2. every role seed derives from that replicate seed, never from `i`:
   - `world_order_seed = seed64("world-order", replicate_seed)`;
   - `pair_split_seed = seed64("pair-split", replicate_seed)`;
   - `model_init_seed = seed64("model-init", replicate_seed)`;
   - `context_code_seed(n) = seed64("context-code", replicate_seed, n)`;
   - `batch_order_seed(history_position, epoch) = seed64("batch-order", replicate_seed, history_position, epoch)`;
   - `shuffled_tag_seed(history_position) = seed64("shuffled-tag", replicate_seed, history_position)`.

Index conventions, binding wherever these names appear in the bundle:

- `replicate_index` is 0-based; the first replicate of a stage is 0;
- `history_position` is **1-based**: H1 = 1, H6 = 6. It is used with this numbering in `batch_order_seed`, in `shuffled_tag_seed`, in the SHUFFLED_TAG block labels, and in every log field of that name;
  The 1..6 range covers history worlds only. Values outside it are reserved for forked probes and are fixed in §12: `0` for every fresh-C probe and `7` for H1 reacquisition. No other value is authorized;
- `epoch` is 0-based; the first epoch of a history block is 0. Under the inherited full-batch policy one epoch is one optimizer update, so within a block of `B_history` updates the epoch runs 0..B_history-1;
- probe index `k` retains its own meaning (number of completed history worlds before the probe) and is unaffected by the above.

An implementation that numbers any of these differently produces a different trajectory. The published schedule digest and its negative controls in `TEST_VECTORS_V0.2.json` enforce the `history_position` convention mechanically; the others are enforced by the k=1 and D0 acceptance items.

Consequence, and the reason the two-level form is required: replicate 0 of `calibration` and replicate 0 of `confirmatory` receive different allocations, splits, initializations, and context vectors. A one-level scheme keyed on `replicate_index` would make development and confirmatory replicates identical and would violate the stage disjointness required by the calibration protocol.

The conditional `SHUFFLED_TAG` diagnostic reuses the confirmatory `replicate_seed` unchanged and differs only in the `shuffled-tag` role stream, as its protocol requires.

Commit the implementation and the published test vectors (`TEST_VECTORS_V0.2.json`) before P0.

---

## 4. World function and scale

Authorized scales only:

- M=96; pool `[131,132,133,134,135,136,137,138]`;
- M=128; pool `[176,177,178,179,180,181,182,183]`.

Operands `a,b in [0,M-1]`; target `y=(a+b)%n`.

Numeric input/output vocabulary must cover integer tokens `0..2*M-2`. No modulus token exists.

The inherited Level 0 relation between vocabulary and output head carries over verbatim with "numeric range" replacing "modulus":

- `numeric_tokens = 2M-1` (ids `0..2M-2`);
- `equals_token = 2M-1`, a real input token, as in Level 0;
- `vocabulary_size = training_classes = 2M` (192 at M=96, 256 at M=128);
- `reporting_classes = 2M-1`;
- `W_U` has shape `[d_model, vocabulary_size]`; the `=` column remains a trained but never-correct class exactly as at Level 0;
- training loss is cross-entropy over the first `training_classes` logits at the readout position; evaluation argmax is taken over the first `reporting_classes` logits.

Narrowing `W_U` to `2M-1` is not authorized: it is an architecture change absent from preregistration §6.3.

Exhaustive unit tests must verify all M^2 operand pairs for every authorized modulus against integer reference arithmetic.

---

## 5. Exact disagreement audit

For this restricted regime and n<n':

`p_flip(n,n') = P[a+b >= n]`.

Required exact M=96 counts over 9216 pairs:

| n | count | p_flip |
|---:|---:|---:|
|131|1830|0.19856770833333334|
|132|1770|0.19205729166666666|
|133|1711|0.18565538194444445|
|134|1653|0.17936197916666666|
|135|1596|0.17317708333333334|
|136|1540|0.16710069444444445|
|137|1485|0.1611328125|
|138|1431|0.1552734375|

Required M=128 counts over 16384 pairs:

| n | count | p_flip |
|---:|---:|---:|
|176|3160|0.19287109375|
|177|3081|0.18804931640625|
|178|3003|0.18328857421875|
|179|2926|0.1785888671875|
|180|2850|0.1739501953125|
|181|2775|0.16937255859375|
|182|2701|0.16485595703125|
|183|2628|0.160400390625|

Mismatch = pre-run `BLOCKED_IMPLEMENTATION`.

---

## 6. Replicate world allocation

For each replicate:

1. permute the selected 8-value pool, in ascending order, as
   `numpy.random.Generator(numpy.random.PCG64(world_order_seed)).permutation(pool)`;
   the exact NumPy version is fixed by the environment lock and is part of the pre-calibration root;
2. perm[0] -> C;
3. perm[1:7] -> H1..H6;
4. perm[7] -> spare.

The allocation hash is `SHA256(UTF8("world-alloc-v0.2|M=<M>|stage=<stage>|i=<replicate_index>|" + ",".join(str(v) for v in permutation)))`.

Write allocation manifest before training.

C never enters main history.

---

## 7. Pair split

Split operand pairs, not generated world rows.

For each replicate:

1. enumerate all M^2 `(a,b)` lexicographically;
2. compute for each pair the full 32-byte digest
   `SHA256(UTF8("philosophia-alias-v0.2|pair-split|" + str(pair_split_seed) + "|" + str(a) + "|" + str(b)))`;
3. sort ascending by that digest compared as bytes, tie-broken by `(a,b)`;
4. first floor(0.70*M^2) -> train;
5. rest -> held-out.
6. the train and held-out arrays are materialized **in the ranked order produced by step 3** and are never re-sorted. The train array is the ranked prefix, the held-out array the ranked remainder, each kept in that order.

This ranked order is the index basis for every index into a split: the `batch-order` permutation of §12 permutes positions in the ranked train array, and the SHUFFLED_TAG schedule consumes presentations in the resulting order. Re-sorting either array — lexicographically or otherwise — before indexing changes which rows are presented in which order, and therefore changes every trajectory, while leaving `split_hash` unchanged, because that digest is deliberately order-insensitive. The `train_order_hash` below is the order-sensitive companion that detects it.

The split digest is
`split_hash = SHA256(b"pair-split-v0.2|M=<M>|train|" + train pairs in lexicographic order as two uint16 little-endian each + b"|held|" + held-out pairs likewise)`.
It is a set hash and is independent of the ranked order.
The lexicographic ordering in this preimage is a hashing convention that makes the digest order-insensitive; it does not describe how the arrays are materialized, which is fixed by step 6.

The order-sensitive companion digest is

`train_order_hash = SHA256(UTF8("pair-split-order-v0.2|M=<M>|train|") + train pairs in ranked order as two uint16 little-endian each + UTF8("|held|") + held-out pairs in ranked order as two uint16 little-endian each)`

`split_hash` witnesses which pairs are in each side; `train_order_hash` witnesses the ranked order those arrays are stored in. Both are logged and both are acceptance items.

Same pair split across all worlds and all arms for the replicate.

Expected sizes:

- M=96: 6451 train / 2765 held-out;
- M=128: 11468 train / 4916 held-out.

---

## 8. Context vectors

No trainable per-world parameter is allowed.

For each replicate/world:

1. derive context seed as `seed64("context-code", replicate_seed, n)`;
2. draw d_model float64 iid standard normal using locked NumPy/PCG64;
3. L2-normalize;
4. compute once at model initialization the median L2 norm of initialized numeric token embeddings; the median is taken over the numeric rows `W_E[0 : 2M-1]` only, excluding the `=` row, at initialization; `2M-1` is odd at both authorized scales, so the median is an exact order statistic;
5. scale every context vector to that same initial median norm;
6. cast to model input dtype;
7. freeze permanently.

### Context set digest

The per-world vector is hashed by the §19 tensor rule applied to the **frozen model-input dtype tensor**, that is after step 6's cast to float32 and not to the float64 draw. The replicate's context set digest is

`context_set_hash = SHA256(UTF8("context-set-v0.2|M=<M>|stage=<stage>|i=<replicate_index>|") + concatenation over the eight worlds in allocation order C, H1, H2, H3, H4, H5, H6, spare of UTF8("<n>|" + tensor_hash(z_n) + "|"))`

where `<n>` is the modulus in base 10. Allocation order, not ascending modulus order, so the digest also witnesses the allocation.

Context is injected directly as input-position representation 0, not through a trainable world-embedding table.

Precisely: the input representation is constructed exactly as at Level 0, except that the position-0 row of the token-embedding term is the frozen context vector instead of an embedding lookup. The inherited positional term is then added at every position uniformly, so the position-0 representation is `z + W_pos[0]` and task positions 1..3 are `W_E[token] + W_pos[position]`. No positional term is omitted, rescaled, or duplicated at position 0, and the context vector is never added to a task position.

### Norm-drift rule

No dynamic rescaling is allowed. Two measurement points are logged and they are distinct fields, not one field measured at an implementation's choice of moment:

- `context_norm_ratio_at_init`, taken once at model initialization immediately after step 6's cast: the measured L2 norm of the **frozen float32** context vector divided by the float32 median numeric-token-embedding norm. It is not written as the constant 1.0. Because the vector is scaled in float64 and then cast, the measured value differs from 1 by a float32 rounding; an implementation must assert `|ratio - 1| <= 1e-6` and treat a larger deviation as `BLOCKED_IMPLEMENTATION`. The assertion, not the constant, is what detects a scaling error;
- `context_norm_ratio_at_block_end`, taken at the end of every history block, which is the drift diagnostic.

At each block end log:

- fixed context-vector norm;
- current median numeric-token-embedding norm;
- ratio `context_norm/current_token_median_norm`.

These values are diagnostic and cannot alter execution.

---

## 9. Positional/max-position semantics

The positional encoding **type and parameterization** inherit `MODEL_CONFIG_REF`.

The v0.2 sequence prepends context at position 0, so original task-token positions are shifted by +1.

Rules:

1. all arms/stages use the same shifted positions;
2. prediction readout is the inherited readout applied to the correspondingly shifted task position;
3. if inherited positional encoding is analytic/fixed or already supports the longer sequence, no parameter is added. For the inherited Level 0 learner this branch does not apply: `W_pos` is a learned `[sequence_length, d_model]` table that is exactly one row short, so rule 4 governs. Rule 3 covers only an analytic or fixed positional encoding, which this cell does not use, and is never a licence to skip rule 4;
4. a learned positional table is drawn **once**, as a single `[sequence_length, d_model] = [4, d_model]` tensor, at the inherited position in the initialization draw order and under the inherited positional-parameter initialization rule. It is **not** drawn as `[3, d_model]` and then extended by a separately drawn row: the two consume the random stream differently and would change every parameter drawn afterwards. The "one shared row only" constraint of this rule bounds how much the table may grow relative to the inherited task sequence; it does not describe the drawing procedure. The added row is shared across all worlds and arms and is declared in the config diff;
5. `max_position` may increase only by one relative to the inherited task sequence requirement. Resolved for this cell: the inherited task sequence is 3 positions, v0.2 has 4, and `max_position = sequence_length = 4`, counted as a number of positions and not as a zero-based index. The projection value in `TEST_VECTORS_V0.2.json` is this number;
6. no per-world or per-arm positional parameter is allowed.

A unit test must compare position IDs/readout indices against the declared shifted layout.

---

## 10. Arm context assignment

For a seed:

### SEPARABLE
H1->z_H1, ..., H6->z_H6.

### ALIASED
H1->z_H1; H2..H6->z_H1.

### Fresh C
Both primary arms use z_C.

### H1 reacquisition
Both use z_H1.

No other learner-visible field identifies n, history index, arm, or boundary.

---

## 11. Sequential history blocks

History is never interleaved.

Each world = one contiguous block of exactly B_history optimizer updates.

At every world boundary:

- keep model weights;
- discard optimizer and all moments/state;
- instantiate identical fresh optimizer;
- no replay;
- no early stopping.

No batch may mix two history worlds.

---

## 12. Batch ordering and arm matching

For each `(replicate,history_position,epoch)` derive deterministic `batch-order` permutation of train-pair indices.

Consume without replacement per epoch; subsequent epoch uses fresh deterministic permutation.

Drop-last/final-batch behavior inherits base config and must be explicit.

For a given seed/history position, ALIASED and SEPARABLE have byte-identical `(a,b,y)` batch sequences. Only context differs after H1.

At H1, complete input tensors must be identical.

Under the inherited full-batch policy the `batch-order` permutation fixes the row order **inside** the single full batch. It does not change which examples are seen, and affects the trajectory only through floating-point summation order; it is retained because it is logged, because it must be byte-identical between ALIASED and SEPARABLE at a given (replicate, history position, epoch), and because it defines the presentation order that the SHUFFLED_TAG schedule consumes.

Forked probes are not history worlds and take reserved `history_position` sentinels outside the 1..6 range, so no probe ever replays a history block's batch order:

- every fresh-C probe, at every k, in both primary arms and in the SHUFFLED_TAG diagnostic: `history_position = 0`;
- H1 reacquisition: `history_position = 7`.

Within a probe, `epoch` counts from 0 for the probe's first update. C probes at different k therefore share one batch-order stream over the same C training split, which is intended: it keeps the probes matched across k and across arms.

---

## 13. Optimizer semantics

Optimizer family/base LR/WD/batch/initialization and any inherited accumulation rule come from `MODEL_CONFIG_REF`.

The inherited batch policy is **full batch**: one optimizer update consumes every training pair of the replicate split (6451 at M=96, 11468 at M=128). It is resolved from the `MODEL_CONFIG_REF` subtree (`data.py` + `train.py`), whose SHA256 values are recorded in the P-1 provenance record alongside `config.py` and `model.py`. `drop_last=false`, `gradient_accumulation_steps=1`. One epoch is therefore one optimizer update, and `B_history`, `tau`, and the competence evaluation interval are all counted in these full-batch updates.

Cell-specific:

- constant LR;
- no warmup;
- no scheduler;
- new optimizer each history block;
- new optimizer each C/reacquisition/diagnostic probe;
- no optimizer state crosses world boundary;
- no per-arm hyperparameters.

---

## 14. Fork non-mutation

Every probe:

1. hash main state;
2. deep-clone/reload separate model;
3. train/evaluate clone;
4. finalize logs;
5. discard clone;
6. hash main state again;
7. require equality.

Mismatch=`INVALID_PROBE_MUTATION`.

Main history proceeds only from untouched checkpoint.

---

## 15. C probe semantics

For each fork:

- C train split only;
- z_C;
- fresh optimizer;
- eval at step 0,100,200,...;
- max tau updates;
- competence = held-out accuracy >=0.95 for 3 consecutive evals;
- raw T = first eval step starting earliest qualifying 3-eval run;
- otherwise T=null, capped/censored=true.

Runner must not relabel capped raw event time as uncensored T=tau. Analysis may use tau only in the explicitly defined restricted cost.

---

## 16. k=1 exact identity

For every paired seed, ALIASED and SEPARABLE must match bit-for-bit through H1 and k1 C probe:

- init hash;
- H1 batch/input hashes;
- H1 losses/evals;
- H1 checkpoint hash;
- k1 C fork init/batches/losses/evals/final hash;
- T/cap state.

Any mismatch=`INVALID_K1_ARM_DIVERGENCE`; seed is not silently dropped.

---

## 17. Determinism

Canonical repository environment is used when available; runtime/device/package/dtype/backend details are logged.

Rules:

- one CPU thread for trajectory-sensitive CPU operations;
- deterministic PyTorch algorithms enabled;
- exact package versions are pinned by the environment lock and are part of the pre-calibration root: CPython, PyTorch, NumPy, and SciPy are each recorded as a full version string, not a major or minor version. NumPy decides the world-order and SHUFFLED_TAG permutations and the `tau` quantile; SciPy decides the Clopper-Pearson bound and the chi-squared factor in the N rule. A version change in either is a change to the locked runtime and requires the same treatment as any other post-lock runtime change;
- the thread-count contract is set through the torch API and checked through `at::get_num_threads()`, `omp_get_max_threads()`, and `mkl_get_max_threads()`; the `OMP_NUM_THREADS` and `MKL_NUM_THREADS` environment variables are not part of the contract, but if set they must be set only to `1`;
- an acceptance test asserts, at process start, that the live CPython, PyTorch, NumPy, and SciPy versions equal the `locked_environment` block of `TEST_VECTORS_V0.2.json` exactly. Failure is `BLOCKED_IMPLEMENTATION` and no further stage may run;
- nondeterministic kernels forbidden;
- Python/NumPy/PyTorch CPU/accelerator RNG explicitly seeded;
- no deterministic setting may be relaxed after outcome-bearing development.

### Two mandatory replay tests

**D0 pre-P0 smoke:** the same short config executed twice from clean process state, with exact equality of init, batch, loss, eval and final hashes. The smoke config is fixed so the gate is comparable across implementations: stage `deterministic-replay`, replicate 0, M=96, arm ALIASED, `B_history = 20`, `tau = 200`, evaluation interval 100 — the same configuration as the k=1 identity case published in `TEST_VECTORS_V0.2.json`. Held-out evaluation inside a history block is logged at step 0 and at the end of the block, that is at epochs {0, B_history}, and nowhere else. It is diagnostic and enters no gate, but it is compared field by field in the k=1 identity case, so its cadence is fixed.

**D1 after P1, before P2:** one dedicated deterministic-replay seed executes the **full selected H1 block of B_history updates plus the full k1 C probe to tau/criterion twice independently**. Entire trajectory artifacts must match bit-for-bit.

D1 failure terminates v0.2 with `BLOCKED_DETERMINISM`; scientific code repair requires a new preregistration version and fresh calibration.

Repeat D1 once under the final confirmatory runtime before confirmatory root commit.

---

## 18. SHUFFLED_TAG implementation is pre-locked

Implementation details are fully specified in `CONDITIONAL_SHUFFLED_TAG_PROTOCOL_V0.2_CANDIDATE_FOR_LOCK.md` and must exist/hash before primary confirmation begins even though execution is outcome-conditional.

No fixed `world -> code` permutation is allowed.

---

## 19. Minimum log schema

At minimum:

- prereg/root/config/git/environment hashes;
- stage;
- replicate index/seed;
- arm;
- M/pool/C/history order;
- world position/probe k;
- optimizer update/global history update;
- train loss and held-out accuracy;
- competence-run state/raw T/capped flag;
- boundary model hash;
- optimizer-state-reset assertion;
- pre/post probe main hash;
- context code/hash or code-index schedule hash;
- context norm and current token-embedding median norm;
- batch hash;
- runtime fingerprint: the exact CPython, PyTorch, NumPy and SciPy versions, `torch.get_num_threads()`, `torch.get_num_interop_threads()`, `torch.backends.mkldnn.is_available()`, and the full text of `torch.__config__.parallel_info()`;

Under full batch the batch digest covers the whole update:

`batch_hash = tensor_hash(rows)` where `rows` is an int64 tensor of shape `[N,3]` whose columns are `(a, b, y)` and whose row order is the presentation order fixed by the `batch-order` permutation for that `(replicate, history_position, epoch)`. The §19 tensor rule already binds dtype and shape, so no separate prefix is added.

An implementation may additionally log `input_hash = tensor_hash(embedded)` over the `[N, 4, d_model]` float32 residual immediately after embedding and before attention. It is optional and diagnostic; it never enters a gate.

No aggregate `trajectory_hash` exists for the C probe; the probe is compared through its listed per-step fields.

Tensor and state hashing are inherited from Level 0 `model._hash_tensor`:
`SHA256(ascii(str(dtype)) || ascii(str(tuple(shape))) || detached.cpu().contiguous().numpy().tobytes())`.
`state_dict_hash = SHA256` over entries concatenated in the inherited parameter creation order `W_E, W_pos, W_Q, W_K, W_V, W_O, W_in, b_in, W_out, b_out, W_U`; entries are concatenated with no separator between them; each entry is itself the UTF-8 of `name + "|" + tensor_hash`.

Raw logs are append-only after finalization.
