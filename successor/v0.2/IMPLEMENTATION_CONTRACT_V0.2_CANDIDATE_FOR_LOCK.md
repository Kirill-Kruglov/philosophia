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
- gradient accumulation/drop-last semantics;
- CPU thread count/device/backend/deterministic flags;
- heavy-cap threshold;
- conditional SHUFFLED_TAG policy.

---

## 2. P-1 model config provenance

Resolve `MODEL_CONFIG_REF` before P0. Record exact path and SHA256 over raw bytes.

If no exact Level 0 paper-mainline trajectory config can be recovered, stop with `BLOCKED_CONFIG_PROVENANCE`.

No numerical reconstruction from prose or remembered settings is allowed.

---

## 3. Deterministic seed derivation

Canonical seed derivation:

`seed64(namespace, replicate_index, extra...) = first_8_bytes(SHA256(UTF8("philosophia-alias-v0.2|" + namespace + "|" + fields)))`, unsigned little-endian, masked to 63 bits.

Disjoint namespaces include:

- calibration;
- power-pilot;
- confirmatory;
- deterministic-replay;
- world-order;
- pair-split;
- batch-order;
- model-init;
- context-code;
- shuffled-tag.

Commit implementation and first 20 values for each namespace before P0.

---

## 4. World function and scale

Authorized scales only:

- M=96; pool `[131,132,133,134,135,136,137,138]`;
- M=128; pool `[176,177,178,179,180,181,182,183]`.

Operands `a,b in [0,M-1]`; target `y=(a+b)%n`.

Numeric input/output vocabulary must cover integer tokens `0..2*M-2`. No modulus token exists.

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

1. deterministically permute selected 8-value pool with `world-order` seed;
2. perm[0] -> C;
3. perm[1:7] -> H1..H6;
4. perm[7] -> spare.

Write allocation manifest before training.

C never enters main history.

---

## 7. Pair split

Split operand pairs, not generated world rows.

For each replicate:

1. enumerate all M^2 `(a,b)` lexicographically;
2. hash with pair-split seed;
3. sort by hash then lexical tie-break;
4. first floor(0.70*M^2) -> train;
5. rest -> held-out.

Same pair split across all worlds and all arms for the replicate.

Expected sizes:

- M=96: 6451 train / 2765 held-out;
- M=128: 11468 train / 4916 held-out.

---

## 8. Context vectors

No trainable per-world parameter is allowed.

For each replicate/world:

1. derive context seed from `(replicate_seed,n)`;
2. draw d_model float64 iid standard normal using locked NumPy/PCG64;
3. L2-normalize;
4. compute once at model initialization the median L2 norm of initialized numeric token embeddings;
5. scale every context vector to that same initial median norm;
6. cast to model input dtype;
7. freeze permanently.

Context is injected directly as input-position representation 0, not through a trainable world-embedding table.

### Norm-drift rule

No dynamic rescaling is allowed. At the end of every history block log:

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
3. if inherited positional encoding is analytic/fixed or already supports the longer sequence, no parameter is added;
4. if a learned positional table is exactly too short, it may be extended by **one shared row only**, initialized with the inherited positional-parameter initialization rule; the extension is shared across all worlds/arms and must be declared in the config diff;
5. `max_position` may increase only by one relative to the inherited task sequence requirement;
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

---

## 13. Optimizer semantics

Optimizer family/base LR/WD/batch/initialization and any inherited accumulation rule come from `MODEL_CONFIG_REF`.

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
- nondeterministic kernels forbidden;
- Python/NumPy/PyTorch CPU/accelerator RNG explicitly seeded;
- no deterministic setting may be relaxed after outcome-bearing development.

### Two mandatory replay tests

**D0 pre-P0 smoke:** same short config executed twice -> exact init/batch/loss/final hashes.

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
- runtime fingerprint.

Raw logs are append-only after finalization.
