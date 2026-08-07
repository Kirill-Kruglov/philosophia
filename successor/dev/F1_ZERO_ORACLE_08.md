# F1_ZERO_ORACLE_08

NON-CITABLE dev falsifier. No src/ edits. No confirmatory datum.

## Zero-oracle boundary

The training sampler signature is `sample_unlabeled_word(stream)`; it cannot accept n, residue, oracle state, labels, panel state, or a candidate period. `_assert_zero_oracle_training_surface` inspects the sampler, batch builder, generator, and MLM trainer for forbidden names and signatures before training. Training imports/uses no `oracle_eq` or `fold`; it sees only right/left token sequences. Candidate periods and `d % p` labels exist only after training inside read-only probes.

## n-independence control

The nominal n=66 and n'=67 streams are coupled through the same sampler and seed. Because n is not an argument, the streams must be byte-identical (stronger than equal empirical marginals over arrangement/displacement).

| seed | nominal periods | words each | byte-identical | (length,d) marginal identical | digest |
| ---: | --- | ---: | --- | --- | --- |
| 0 | 66 vs 67 | 10000 | True | True | `53b3369393da9f0f` |
| 1 | 66 vs 67 | 10000 | True | True | `a8b7b0bf21a0d005` |

**Control result: PASS — no mod-n structure is baked into generation.**

## Objective and activation

- Seeds: [0, 1]; CUDA device: NVIDIA GeForce RTX 4060 Laptop GPU.
- Objective: bidirectional masked-token reconstruction over single R/L words, 15% positions masked with token id 3; predict R vs L. 1000 updates, batch=64, AdamW lr=1e-3. Four-member ContactTransformer committee trained sequentially; equality heads frozen.
- Stream: displacement uniform on fixed [-125,125], admissible padding uniform, arrangement rank uniform. Support is fixed independently of n.
- Activation: exactly REPRPROBE_07's committee-mean pre-head `final_ln(x)[:, -1, :]` on `word⊕SEP⊕word` (128 dimensions).
- Probe corpus: 24000 distinct words absent from unsupervised training; 70/30 disjoint-word split.
- Probe: one-vs-all linear ridge. Macro accuracy makes chance exactly `1/p`; no backprop into the base committee.

## Residue-mod-66 linear probe

| seed | init test macro-acc | post-MLM test macro-acc | chance | post normalized lift |
| ---: | ---: | ---: | ---: | ---: |
| 0 | 17.51% | 12.57% | 1.52% | 0.112 |
| 1 | 19.00% | 16.67% | 1.52% | 0.154 |
| **mean** | **18.26%** | **14.62%** | **1.52%** | — |

## Period-search probe (p=2..125, no period supplied to training)

Periods are ranked by chance-normalized lift `(macro_acc - 1/p)/(1 - 1/p)` so different class counts are comparable. A supervised fixed-p probe alone is not treated as recovery; F1 fires only if the blind search selects p=66 and post-training materially improves it over init.

| seed | best period | best macro-acc | chance | normalized lift | rank of p=66 | fires |
| ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 0 | 2 | 61.31% | 50.00% | 0.226 | 60 | False |
| 1 | 2 | 65.39% | 50.00% | 0.308 | 57 | False |

Top candidates:
- seed 0: p=2 acc=61.31% lift=0.226, p=124 acc=15.52% lift=0.148, p=122 acc=15.02% lift=0.143, p=125 acc=14.83% lift=0.141, p=120 acc=14.76% lift=0.140, p=123 acc=14.74% lift=0.140, p=105 acc=14.75% lift=0.139, p=117 acc=14.61% lift=0.139, p=95 acc=14.68% lift=0.138, p=93 acc=14.66% lift=0.137
- seed 1: p=2 acc=65.39% lift=0.308, p=121 acc=20.47% lift=0.198, p=119 acc=20.44% lift=0.198, p=124 acc=20.25% lift=0.196, p=125 acc=20.22% lift=0.196, p=122 acc=19.92% lift=0.193, p=117 acc=19.76% lift=0.191, p=118 acc=19.75% lift=0.191, p=123 acc=19.71% lift=0.190, p=120 acc=19.70% lift=0.190

## Clocks

- seed 0: unsupervised wall=218.2s, final MLM loss=0.1541
- seed 1: unsupervised wall=234.3s, final MLM loss=0.1593
- total wall=549.9s (9.2 min).

## Verdict

**WALL-NOT-MANUFACTURABLE**

WALL-NOT-MANUFACTURABLE: the coupled stream was exactly n-independent; neither seed met the registered recovery condition (search must select 66, improve ≥5 points over init, and have ≥0.10 chance-normalized lift). A supervised p=66 probe may decode incidental displacement structure, but because the search was not specifically attracted to 66, that is not recovery of the world's modulus from words. Within this model/objective/horizon, the empirical spine holds.

Interpretive caution: a post-hoc supervised probe is given `d % p` labels and can exploit any displacement information already present. Therefore above-chance p=66 accuracy by itself is not evidence that the unsupervised learner inferred 66; period specificity in the blind search is required for the falsifier.

## Permutation-calibrated period-rank null

NON-CITABLE addendum. Fix the post-MLM activations and train/test split; destroy the activation↔displacement pairing by shuffling the joint label vector; re-run the blind search over p∈[2,125] and record the 1-based rank of the true modulus 66. Repeat K times. Two-sided p-value uses the +1-corrected Monte Carlo extremity test `p = (1 + #{|R_k − μ| ≥ |R_obs − μ|}) / (K+1)` with μ = null mean.

### Seed 0

- K = 1000; candidates = 124; device = `cpu`; perm_seed = 20260808.
- Reported GPU observed rank of p=66: **60**.
- Reconstructed observed rank on this rebuild: **61** (lift=0.1372).
- Null rank of p=66: mean=62.73, median=63.0, sd=32.29, range=[1, 122].
- Two-sided p-value for reported rank 60: **0.9500** (doubled one-sided = 0.9391; left=0.4695, right=0.5425).
- Two-sided p-value for reconstructed rank 61: **0.9690**.

### Headline

**Two-sided p-value for observed rank 60 (seed 0): 0.9500.**

Interpretation: under label-shuffle, p=66's period-rank is not extreme — the middle-of-pack placement is consistent with a null that has no activation↔residue association. "No specificity for 66" is quantified, not eyeballed.

- perm-null wall=1399.8s (23.3 min).
