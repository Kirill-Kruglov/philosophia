# GROKKING_PROBE_09

NON-CITABLE grokking probe. Dev world only. No confirmatory datum. No src/ edits (world.py / scoring.py / encode_pair / oracle_eq / floor / panel / config reused verbatim).

env: torch=2.7.0+cu128; device=NVIDIA GeForce RTX 4060 Laptop GPU; cuda_available=True.

## Question

Was the Level-1 competence block a self-imposed design artifact (full-history O(B^2) committee), or something deeper? Test whether a STANDARD single-model learner GROKS the Z/n equality task (modulus 66) without full history.

## Learner / training

- architecture: a SINGLE ContactTransformer (d_model=128, heads=4, 2 layers) -- NOT the 4-member full-history committee.
- objective: class-balanced CE via BALANCED minibatches (128 equal + 128 unequal per step; equal pairs are ~1.5% of the pool, so balanced sampling prevents majority collapse per DIAG_01).
- optimizer: AdamW lr=0.001 betas=(0.9, 0.98) eps=1e-08; weight_decay ON attention/MLP/head_W, 0.0 on embeddings/LN/biases (mirrors build_optimizer grouping). weight_decay is the grokking driver -- swept [0.0, 0.01, 0.1, 1.0].
- budget: NO full history -> O(steps); 50000 minibatch steps per run, checkpoint every 2500. seeds [0].
- forward: cropped-leading-pad + fused SDPA (self-consistent; train==eval) -- mathematically standard attention; the SAME forward is used for training and for every evaluation (residue probe, panel floor, held-out), so the learner is internally consistent. Parameters and initialization are the frozen ContactTransformer's.

## Panel <-> train disjointness

- train pairs (acquisition only): 2512 (1256 equal + 1256 unequal).
- held-out pairs (reserved, balanced): 536 equal + 536 unequal.
- panel pairs: 188 (frozen PANEL_SIZE=188).
- train ∩ panel = 0; train ∩ held-out = 0; held-out ∩ panel = 0; panel-cell-in-acquisition = False (all must be 0/False).
- residue-probe novel words: train=1848, test=792 (disjoint, stratified by residue).

Total wall-clock (all runs): 13279.4 s (3.69 h).

## Sweep summary

| weight_decay | seed | best held-out acc | best residue probe | ever cleared floor | wall (min) |
| ---: | ---: | ---: | ---: | --- | ---: |
| 0.0 | 0 | 55.32% | 6.69% | False | 55.1 |
| 0.01 | 0 | 54.85% | 7.07% | False | 55.5 |
| 0.1 | 0 | 54.85% | 7.83% | False | 55.4 |
| 1.0 | 0 | 58.77% | 10.73% | False | 55.3 |

chance: held-out equality = 50.00%; residue-mod-66 probe = 1.52%. Frozen floor (stringent, per stratum): S1>=118/124, S2>=15/16, S3>=15/16, S4>=15/16, S5>=14/16, abstain<=2, brier<=0.10.

## Grokking curve (best run: weight_decay=1.0, seed=0)

| step | train acc | held-out acc | held eq | held neq | gap | residue probe | panel strata_ok | panel qualifies | mean brier |
| ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: |
| 0 | 51.04% | 54.85% | 55.41% | 54.29% | -0.0382 | 6.69% | 1/5 | False | 0.2271 |
| 2500 | 67.71% | 52.52% | 82.65% | 22.39% | +0.1520 | 7.58% | 0/5 | False | 0.3394 |
| 5000 | 80.18% | 48.23% | 70.90% | 25.56% | +0.3195 | 6.82% | 0/5 | False | 0.4270 |
| 7500 | 76.07% | 50.28% | 75.56% | 25.00% | +0.2579 | 10.10% | 0/5 | False | 0.4318 |
| 10000 | 78.38% | 49.53% | 73.13% | 25.93% | +0.2885 | 8.21% | 0/5 | False | 0.4842 |
| 12500 | 78.90% | 50.47% | 82.84% | 18.10% | +0.2843 | 8.96% | 0/5 | False | 0.4347 |
| 15000 | 78.22% | 53.36% | 79.29% | 27.43% | +0.2487 | 8.59% | 0/5 | False | 0.3958 |
| 17500 | 77.31% | 49.53% | 76.31% | 22.76% | +0.2778 | 7.83% | 0/5 | False | 0.4114 |
| 20000 | 74.32% | 58.77% | 84.89% | 32.65% | +0.1555 | 9.72% | 0/5 | False | 0.3836 |
| 22500 | 81.33% | 48.51% | 81.53% | 15.49% | +0.3282 | 10.48% | 0/5 | False | 0.4879 |
| 25000 | 79.86% | 50.47% | 76.49% | 24.44% | +0.2939 | 10.48% | 0/5 | False | 0.4187 |
| 27500 | 79.90% | 47.67% | 74.25% | 21.08% | +0.3223 | 9.97% | 0/5 | False | 0.3953 |
| 30000 | 76.91% | 53.17% | 81.16% | 25.19% | +0.2374 | 9.60% | 0/5 | False | 0.3747 |
| 32500 | 81.89% | 48.32% | 71.83% | 24.81% | +0.3357 | 10.73% | 0/5 | False | 0.4012 |
| 35000 | 82.48% | 46.55% | 72.01% | 21.08% | +0.3594 | 9.34% | 0/5 | False | 0.4124 |
| 37500 | 76.63% | 54.66% | 82.46% | 26.87% | +0.2197 | 8.59% | 0/5 | False | 0.3642 |
| 40000 | 85.75% | 51.77% | 84.14% | 19.40% | +0.3398 | 9.72% | 0/5 | False | 0.4616 |
| 42500 | 85.23% | 45.99% | 70.71% | 21.27% | +0.3924 | 9.22% | 0/5 | False | 0.4584 |
| 45000 | 82.56% | 48.60% | 76.31% | 20.90% | +0.3396 | 8.33% | 0/5 | False | 0.4824 |
| 47500 | 83.76% | 52.43% | 78.92% | 25.93% | +0.3133 | 9.97% | 0/5 | False | 0.4966 |
| 50000 | 83.32% | 45.52% | 67.72% | 23.32% | +0.3780 | 10.73% | 0/5 | False | 0.4409 |

### Best-run per-stratum held-out (panel) accuracy vs step (S1-S5)

| step | S1 | S2 | S3 | S4 | S5 |
| ---: | ---: | ---: | ---: | ---: | ---: |
| 0 | 100.00% | 43.75% | 50.00% | 50.00% | 87.50% |
| 2500 | 16.94% | 37.50% | 31.25% | 50.00% | 62.50% |
| 5000 | 34.68% | 50.00% | 56.25% | 50.00% | 43.75% |
| 7500 | 42.74% | 25.00% | 56.25% | 50.00% | 50.00% |
| 10000 | 38.71% | 43.75% | 43.75% | 50.00% | 37.50% |
| 12500 | 37.90% | 37.50% | 50.00% | 50.00% | 43.75% |
| 15000 | 62.10% | 43.75% | 37.50% | 50.00% | 43.75% |
| 17500 | 45.97% | 25.00% | 56.25% | 50.00% | 56.25% |
| 20000 | 54.03% | 50.00% | 56.25% | 50.00% | 50.00% |
| 22500 | 28.23% | 43.75% | 50.00% | 50.00% | 43.75% |
| 25000 | 46.77% | 56.25% | 50.00% | 50.00% | 31.25% |
| 27500 | 43.55% | 31.25% | 50.00% | 50.00% | 56.25% |
| 30000 | 37.90% | 50.00% | 62.50% | 50.00% | 56.25% |
| 32500 | 50.81% | 50.00% | 62.50% | 50.00% | 43.75% |
| 35000 | 56.45% | 50.00% | 50.00% | 50.00% | 37.50% |
| 37500 | 57.26% | 43.75% | 50.00% | 50.00% | 56.25% |
| 40000 | 33.87% | 18.75% | 50.00% | 50.00% | 43.75% |
| 42500 | 26.61% | 31.25% | 56.25% | 50.00% | 50.00% |
| 45000 | 37.10% | 37.50% | 56.25% | 50.00% | 56.25% |
| 47500 | 44.35% | 18.75% | 43.75% | 50.00% | 50.00% |
| 50000 | 29.84% | 37.50% | 56.25% | 50.00% | 50.00% |

## Verdict

**NO-COMPETENCE / PRE-MEMORIZATION** — under this learner (single ContactTransformer
d=128/2L), this raw-walk encoding, this optimizer, and a 50k-step budget, no run
reached competence and no run entered the grokking regime.

Bounded engineering fact only: held-out equality stayed near chance (best 58.77%,
chance 50%) while train rose to ~83% at wd=1.0. Crucially, **the grokking window was
never entered**: at wd=0.0 full-train fit capped at 92.56% (grokking_probe_09_results.json),
never ~100%. Grokking (Power et al.) is delayed generalization *after* a train fit is
reached; this run is pre-memorization and therefore uninformative about it.

**No causal attribution.** The earlier wording — "the block is deeper (floor/world/
task), not merely the O(B²) design" — is withdrawn as an overclaim: this run cannot
distinguish "a deeper wall" from "this learner simply did not fit the train set"
(ordinary optimization/capacity). Removing full-history changed the cost model, not
the outcome; the entry cost of competence is not measured by this run.

**MODULAR is NOT established as the wall.** The residue signal is not a clean learned
circuit: it decodes 6.69% already at step 0 (input geometry), peaking 10.73% — ~4
points over baseline — on a probe split by word (stratified by residue) but NOT by
displacement, so "decode d, then look up d→d mod 66 on seen d" would suffice with no
modular circuit. The only strict result is the *absence* of a clean modular factor
(B2's disjoint-d residue probe sits at chance); even that cannot be called "the wall
that blocked competence." At least three upstream walls remain unseparated by
existing probes: (i) displacement is only weakly represented (B2 exact_d ≈ 0.33–0.46
on ≤40 classes, and length decodes *better* than d — a shortcut, not a clean count);
(ii) two-operand binding / the difference d_L − d_R was never measured (all probes
use single-word self-pairs); (iii) the modular quotient.

**Scope — what this closes.** The specific branch `Z/n + raw walks + ContactTransformer`
is closed as NO-COMPETENCE; it did not yield a result and does not promise knowledge
proportional to further tuning (idea-gate §4/§5). This is NOT a result about
Philosophia's thesis: the Z/n path-credit *discovery* was already withdrawn by
structural analysis (manufacturable invariant trivial; author decision 2026-08-07),
not by this run; the never-run ACTIVE/YOKED contact question is untouched. The essay
stands unchanged and remains more precise than this note. Composition-bearing worlds
stay open; if ever resumed, split C1/contact (a competence-friendly representation,
ACTIVE vs YOKED) from path-manufacture (a world where the pre-quotient invariant
needs composition, not token-counting).
