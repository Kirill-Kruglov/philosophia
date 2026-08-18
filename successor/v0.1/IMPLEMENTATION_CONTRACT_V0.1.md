# Implementation contract v0.1

**Status:** DRAFT FOR EXTERNAL REVIEW — part of preregistration v0.1

This document closes implementation choices that could silently change the scientific manipulation.

---

## 1. Machine-visible configuration hierarchy

No value may be supplied from an implicit default if it affects the trajectory.

Configuration precedence must be single-source and logged. At minimum the final config contains:

- preregistration version;
- git commit;
- environment lock hash;
- `MODEL_CONFIG_REF` and SHA256;
- selected `M` and module pool;
- train fraction;
- `B_history`;
- `tau`;
- evaluation interval and competence threshold;
- arm;
- replicate seed;
- deterministic seed namespaces;
- batch size, LR, WD, optimizer family;
- number of CPU threads;
- deterministic-kernel flags.

---

## 2. Deterministic seed namespaces

Use a cryptographic derivation rather than ad hoc integer offsets.

Recommended canonical function:

`seed64(namespace, replicate_index, extra...) = first 8 bytes of SHA256(UTF8("philosophia-alias-v0.1|" + namespace + "|" + fields)), interpreted unsigned little-endian, masked to 63 bits.`

Namespaces must be disjoint for:

- `calibration`;
- `power-pilot`;
- `confirmatory`;
- `world-order`;
- `pair-split`;
- `batch-order`;
- `model-init`;
- `context-code`;
- `shuffled-tag` diagnostics.

The exact seed derivation implementation and first 20 values per namespace are hash-committed before calibration.

---

## 3. Scale and world function

Authorized scales:

- `M=96`, expected module pool `[131,132,133,134,135,136,137,138]`;
- one permitted escalation `M=128`, expected module pool `[176,177,178,179,180,181,182,183]`.

Operands:

`a,b in [0, M-1]`.

Target:

`y = (a + b) % n`.

Numeric vocabulary/output head must cover every integer token from `0` through `2*M-2`, even if some values are unused as targets. No modulus token is included.

Unit tests must exhaustively verify all `M^2` pairs for every authorized modulus against Python integer arithmetic.

---

## 4. Exact p_flip audit

For `n < n'` in this restricted regime:

`p_flip(n,n') = P_{a,b uniform}[a+b >= n]`.

The implementation must reproduce these exact `M=96` counts over 9216 pairs:

| n | count | p_flip |
|---:|---:|---:|
| 131 | 1830 | 0.19856770833333334 |
| 132 | 1770 | 0.19205729166666666 |
| 133 | 1711 | 0.18565538194444445 |
| 134 | 1653 | 0.17936197916666666 |
| 135 | 1596 | 0.17317708333333334 |
| 136 | 1540 | 0.16710069444444445 |
| 137 | 1485 | 0.1611328125 |
| 138 | 1431 | 0.1552734375 |

Expected `M=128` values over 16384 pairs:

| n | count | p_flip |
|---:|---:|---:|
| 176 | 3160 | 0.19287109375 |
| 177 | 3081 | 0.18804931640625 |
| 178 | 3003 | 0.18328857421875 |
| 179 | 2926 | 0.1785888671875 |
| 180 | 2850 | 0.1739501953125 |
| 181 | 2775 | 0.16937255859375 |
| 182 | 2701 | 0.16485595703125 |
| 183 | 2628 | 0.160400390625 |

Any mismatch is a pre-run implementation failure.

---

## 5. Replicate world allocation

For each replicate seed:

1. instantiate the selected fixed 8-value pool;
2. permute it with the `world-order` RNG;
3. `perm[0] -> C`;
4. `perm[1:7] -> H1..H6` in order;
5. `perm[7] -> spare`.

Write the allocation to the per-seed manifest before model training begins.

`C` must never appear in main history training.

---

## 6. Train/held-out split

The split is over operand pairs `(a,b)`, not over generated rows after world-specific labels.

For each replicate:

1. enumerate all `M^2` operand pairs in lexicographic order;
2. hash each pair with the `pair-split` seed;
3. sort by the hash plus lexicographic tie-break;
4. first `floor(0.70*M^2)` pairs are training;
5. the remainder are held out.

The **same operand split is reused across all history worlds and C within that replicate** and both arms.

Expected exact sizes:

- `M=96`: 6451 train, 2765 held out;
- `M=128`: 11468 train, 4916 held out.

This cell tests transfer of the world rule, not novelty of operand tuples; seeing a held-out-C operand pair under a different history modulus is allowed.

---

## 7. Context vector generation

No trainable per-world embedding row is allowed.

For every replicate/world pair:

1. derive a `context-code` RNG seed from `(replicate_seed, n)`;
2. instantiate `numpy.random.Generator(numpy.random.PCG64(seed64))` under the locked NumPy version and draw a `d_model`-length float64 vector iid standard normal;
3. L2-normalize it;
4. compute once, at model initialization, the median L2 norm of the initialized numeric token embeddings;
5. scale every context vector in that replicate to that median norm;
6. cast to the model input dtype;
7. freeze the vector permanently.

The context vector is injected directly as the first input-position representation. It is not looked up through a trainable embedding table and does not create world-specific parameters.

The numerical model input is therefore conceptually:

`[fixed_context_vector, embedding(a), embedding(b)]`.

The exact prediction readout and transformer internals inherit `MODEL_CONFIG_REF`, adjusted only for the prepended context position and output vocabulary.

---

## 8. Arm construction

For a given replicate:

### SEPARABLE

- H1 uses `z_H1`;
- H2 uses `z_H2`;
- ...;
- H6 uses `z_H6`.

### ALIASED

- H1 uses `z_H1`;
- H2..H6 also use `z_H1`.

### Fresh C

Every C probe in both arms uses `z_C`.

### Reacquisition H1

Both arms use `z_H1`.

No other model-visible field may identify `n`, history index, world boundary, or arm.

World boundaries are known to the training harness only because it must reset optimizer state; no boundary token is passed to the model.

---

## 9. Sequential blocks — never interleave

A history world is one contiguous block of exactly `B_history` optimizer updates.

The runner must not mix examples from different history worlds in one optimizer block.

At every world boundary:

- keep model weights;
- drop the optimizer and all optimizer moments/state;
- instantiate a new optimizer with identical locked hyperparameters;
- do not reset model weights;
- do not replay prior-world examples.

No early stopping is permitted in history.

---

## 10. Batch ordering

Within each world block, data order is deterministic and arm-matched.

Canonical procedure:

- generate a permutation of training-pair indices for each epoch from `(replicate_seed, history_position, epoch)` in the `batch-order` namespace;
- consume without replacement within an epoch;
- start a new deterministic permutation when the epoch ends;
- truncate the final batch only according to the inherited batch-size/drop-last rule, which must be explicit in final config.

For the same replicate and history position, ALIASED and SEPARABLE must have identical `(a,b,y)` batch hashes; only the context tensor may differ after H1.

At H1, the **entire input tensor** must also be identical.

---

## 11. Optimizer semantics

The optimizer family, base LR, weight decay, batch size, initialization, and other model-training constants come from the resolved Level 0 config unless explicitly excepted by preregistration.

Cell-specific rules:

- LR constant; no warmup;
- no LR scheduler;
- fresh optimizer at every history boundary;
- fresh optimizer for every C or reacquisition probe;
- no optimizer state transferred between worlds;
- no gradient accumulation unless present in the resolved base config and explicitly logged;
- no per-arm hyperparameters.

---

## 12. Fork-probe integrity

A probe is forbidden from mutating the main trajectory.

Required implementation pattern:

1. serialize/hash the main model state immediately before probe;
2. deep-clone or reload a separate probe model;
3. run probe training only on clone;
4. finalize probe logs;
5. destroy clone;
6. hash main model again;
7. assert equality with pre-probe hash.

Failure invalidates the run.

Fork probes occur after history positions 1, 2, 4, and 6. Main history always proceeds from the untouched checkpoint.

---

## 13. C probe

For every fork:

- use C training split only;
- use context `z_C`;
- new optimizer, empty state;
- evaluate held-out C at step 0 and every 100 updates;
- run no more than `tau` optimizer updates;
- competence = >=0.95 held-out accuracy at three consecutive evaluations;
- record raw first qualifying start `T` if it exists;
- otherwise record `T=null`, `censored=true` and cap `tau`.

The primary analysis converts this to restricted cost; runner code must not impute `T=tau` as an uncensored event.

---

## 14. H1 reacquisition probe

After H6, create a disposable fork exactly as for C, but train/evaluate on H1 and use `z_H1` in both arms.

This is secondary only.

---

## 15. k=1 exact-integrity gate

Because the arms are identical through H1, the following must match bit-for-bit for each paired seed:

- initialization hash;
- every H1 batch hash;
- H1 loss sequence (subject to exact deterministic-kernel contract);
- H1 final checkpoint hash;
- C-probe initialization hash at k=1;
- C-probe batch hashes;
- C-probe loss/evaluation sequence;
- k=1 C probe final hash and `T`/censor result.

Any mismatch yields `INVALID_K1_ARM_DIVERGENCE` and no scientific comparison.

---

## 16. Determinism and runtime

Pin the existing repository environment where possible; the supplied project README names CPython 3.12.3 and PyTorch 2.9.1 as canonical.

Additional v0.1 execution rules:

- one CPU thread for trajectory-sensitive training/data operations;
- deterministic PyTorch algorithms enabled;
- nondeterministic kernels forbidden;
- random seeds explicitly set for Python, NumPy, PyTorch CPU, and accelerator RNGs;
- record device model, driver/runtime, BLAS/backend versions, dtype, and deterministic flags;
- if an operation cannot execute deterministically under the locked environment, stop before confirmatory execution rather than silently relaxing determinism.

A short deterministic prefix replay must match initialization, batch, loss, and final-state hashes before calibration and again before confirmatory lock.

---

## 17. Minimum log schema

One record per evaluation plus boundary records. Required fields include:

- prereg_version;
- git_sha;
- config_sha256;
- environment_sha256;
- stage (`calibration`, `power_pilot`, `confirmatory`, diagnostic);
- replicate_index and derived seed;
- arm;
- selected M;
- module_pool;
- C modulus;
- history modulus list/order;
- current world position;
- probe_k if applicable;
- optimizer update count;
- global history update count;
- train loss;
- train accuracy if computed;
- held-out accuracy;
- qualifying-run state;
- raw T;
- censored flag;
- checkpoint SHA256 at every world boundary;
- main-checkpoint SHA256 before/after every fork;
- batch-sequence manifest SHA256;
- wall-clock seconds (diagnostic only).

Raw logs are append-only outcome artifacts.

---

## 18. Acceptance tests before calibration

The implementation is not allowed to run P0 until all tests pass:

1. exhaustive modular-table truth for all authorized worlds;
2. exact p_flip counts above;
3. exact split sizes and stable split hashes;
4. world allocation deterministic for known test seeds;
5. non-trainable context vectors have no optimizer parameters;
6. H1 batch hashes identical between arms;
7. H1 final checkpoint hash identical between arms in deterministic prefix/full block test;
8. probe fork leaves main checkpoint hash unchanged;
9. optimizer moments/state absent after reset;
10. main history cannot access C rows or C optimizer state;
11. SHUFFLED-TAG diagnostic, if implemented, assigns codes per example independently of world rather than permuting world labels;
12. analysis fixture with synthetic known T values reproduces the exact preregistered `delta`.

Test report and code commit are part of the pre-calibration lock.
