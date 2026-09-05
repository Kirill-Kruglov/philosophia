# Level -1 literature map

Status: first-pass map for adversarial review; not a systematic review.

known means a primary source establishes the bounded proposition. partial means
an adjacent result exists but leaves a load-bearing condition open. open means no
source in this pass settles the operational claim.

## Cells

| Cell | Primary anchors | Established | Philosophia status |
|---|---|---|---|
| Grokking | [Power et al. 2022](https://arxiv.org/abs/2201.02177) | Small transformers can generalize on algorithmic tables long after fitting training data. | known anchor; reproduce, do not claim |
| Modular-addition mechanism | [Nanda et al. 2023](https://arxiv.org/abs/2301.05217), [Gromov 2023](https://arxiv.org/abs/2301.02679) | Grokked modular arithmetic admits Fourier-structured descriptions; Nanda et al. separate memorization, circuit formation, and cleanup. | known within studied worlds and architectures |
| Hidden progress | [Nanda et al. 2023](https://arxiv.org/abs/2301.05217), [Gu et al. 2025](https://arxiv.org/abs/2504.03162) | Mechanism-derived measures can precede the abrupt test transition; weight-decay-only explanations are disputed. | partial; measures need random-label and checkpoint-order nulls |
| Transfer after grokking | [Park et al. 2024](https://arxiv.org/abs/2405.16658), [Implicit Reasoners](https://arxiv.org/abs/2405.15071) | Selected arithmetic transfers accelerate grokking; extended training can still fail OOD. | partial; cross-world and algebra-to-geometry transfer remain open |
| Active contact | [Settles 2009](https://minds.wisconsin.edu/handle/1793/60660) | Query choice can reduce label complexity under assumptions. | Philosophia's comparison is unrun; `experience` E12A/C later isolate an exact null for authorship and a positive for transcript selection in another design |
| Single-view non-identifiability | [Hyvärinen & Pajunen 1999](https://doi.org/10.1016/S0893-6080(98)00140-3), [Locatello et al. 2019](https://arxiv.org/abs/1811.12359) | Unrestricted nonlinear ICA admits infinitely many non-trivially different solutions; unsupervised disentanglement requires inductive biases. | known under the papers' assumptions; not a theorem that one modality can never suffice |
| Multi-view identifiability | [Gresele et al. 2019](https://arxiv.org/abs/1905.06642), [von Kügelgen et al. 2021](https://arxiv.org/abs/2106.04619), [Yao et al. 2024](https://arxiv.org/abs/2311.04056) | Sufficiently different views can identify common sources or invariant content up to a stated invertible/smooth equivalence under stated assumptions. | known at population level; does not imply finite-sample optimisation success; the finite-field runs are an analogy in design, not theorem instances |
| Invariant/equivariant approximation | [Yarotsky 2022](https://arxiv.org/abs/1804.10306), [Geometric Deep Learning](https://arxiv.org/abs/2104.13478) | Complete neural approximators exist for continuous maps under supplied group actions. | known expressiveness result; silent on discovering the group from contact |
| Exact versus approximate symmetry enforcement | [Tahmasebi & Weber 2026](https://arxiv.org/abs/2512.11855) | Under finite-group black-box linear post-processing, exact enforcement has linear and approximate enforcement logarithmic averaging complexity in group size. | known in that mechanism; not a result about what gradient descent learns |
| Error consistency | [Geirhos et al. 2020](https://arxiv.org/abs/2006.16736) | Trial-level co-error is informative beyond accuracy and necessary for similar strategies. | partial; seed-versus-architecture effective-k remains open |
| Consolidation | [Kirkpatrick et al. 2017](https://arxiv.org/abs/1612.00796) | EWC can protect earlier tasks by slowing important parameters. | known method, not evidence of experience |
| Replay | [Rolnick et al. 2018](https://arxiv.org/abs/1811.11682), [Buzzega et al. 2020](https://arxiv.org/abs/2010.05595) | Replay can reduce catastrophic forgetting. | known baseline; exact old-world reproduction remains our obligation |
| Library learning | [DreamCoder](https://arxiv.org/abs/2006.08381) | Learned symbolic abstractions can compress and transfer compositionally. | partial precedent; different learner and supervision |
| Open-ended curricula | [POET](https://arxiv.org/abs/1901.01753), [PAIRED](https://arxiv.org/abs/2012.02096) | Generated environments and solution transfer can create curricula. | known precedent; adaptive primary curriculum excluded for Goodhart risk |
| Curriculum failure | [Jiang et al. 2022](https://arxiv.org/abs/2207.05219), [Beukman et al. 2024](https://arxiv.org/abs/2402.12284) | Adaptive curricula can induce covariate shift or regret stagnation. | known warning supporting a fixed primary curriculum |
| Derived geometry | [AlphaGeometry](https://www.nature.com/articles/s41586-023-06747-5) | Synthetic derivation and traceback can train geometry solving without human demonstrations. | existence precedent, not small-model transfer evidence |
| Verifiable reward | [AlphaProof and AlphaGeometry 2](https://deepmind.google/blog/ai-solves-imo-problems-at-silver-medal-level/), [Firsching et al. 2026 (Formal Conjectures)](https://arxiv.org/abs/2605.13171) | Formal verification and RL/search support strong mathematical systems; an evolving Lean-4 benchmark of 1,029 open and 836 solved conjectures makes verified discovery measurable, with AI proofs and disproofs auditing formalization fidelity. | known D-axis precedent; P-axis is not isolated. Where a complete cheap verifier exists it is the right instrument and ours is not; our domain is the remainder with no complete oracle. Their fidelity audit is an instance of our change-the-road criterion, not a result of ours |
| Emergence from interaction | [Computational Life 2024](https://arxiv.org/abs/2406.19108), [Agüera y Arcas 2025, *What Is Intelligence?*](https://mitpress.mit.edu/9780262049955/what-is-intelligence/) | Self-replicators arise from random program interaction with no imposed fitness function; prediction is argued to be fundamental to mind, brain, and life. | known existence precedent for structure arising unaided; silent on whether a given learner earned a given structure, which is the question here |
| Path over destination credit | [Uesato et al. 2022](https://arxiv.org/abs/2211.14275), [Lightman et al. 2023](https://arxiv.org/abs/2305.20050) | Rewarding intermediate steps outperforms rewarding only the final answer on mathematical reasoning. | known direction on the P-axis; the walk-world oracle-free path axis is void by construction, not an open experiment |
| Manufactured invariance | [Dangovski et al. 2022 (E-SSL)](https://arxiv.org/abs/2111.00899), [von Kügelgen et al. 2021](https://arxiv.org/abs/2106.04619) | Transformations determine what is treated as invariant content; under explicit augmentation assumptions, paired views can identify that content up to an invertible mapping. | known conditional positive and warning; self-generated transformations do not themselves establish that they preserve the world's relevant content |
| Cross-modal convergence | [Huh et al. 2024](https://arxiv.org/abs/2405.07987) | Representation spaces across objectives and modalities become more aligned as models scale. | empirical positive; convergence is agreement, not external correctness |
| Internal truth discrimination | [Azaria & Mitchell 2023](https://arxiv.org/abs/2304.13734), [Bürger et al. 2024](https://proceedings.neurips.cc/paper_files/paper/2024/hash/f9f54762cbb4fe4dbffdd4f792c31221-Abstract-Conference.html) | Hidden activations support classifiers that distinguish true/false statements and lies with substantial accuracy in the studied settings. | does not test a distortion shared by all evidence available to the model; the corpus-consistency reading is the author's interpretation |
| Broadcast representation | [Gurnee et al. 2026](https://transformer-circuits.pub/2026/workspace/) | A J-space concept vector can be used by several downstream functions, with a selective role in flexible computation. | multi-function evidence, not evidence that independent presentations converge upon one representation |
| Era of Experience | [Silver and Sutton 2025](https://storage.googleapis.com/deepmind-media/Era-of-Experience%20/The%20Era%20of%20Experience%20Paper.pdf) | Position paper argues for long-lived environmental experience beyond imitation. | framing, not empirical evidence |

## Corrected core

| Proposition | Status | Reason |
|---|---|---|
| Prediction, intervention stability, and transfer jointly define experience | partial | Components are standard; the conjunction is ours. |
| Correlated failures testify to shared derivation | partial | Error consistency supports necessity, not ancestry identification. |
| Independence is not inherited from seeds | partial | Architecture-insensitive co-error is a warning; Line 12 is the direct evidence. |
| Dependence has a stress window | open | No external anchor found for the claimed competence/noise window. |
| Vanishing severity is internally ambiguous | open | No source resolves blindness versus absent signal without changing representation. |
| Insight has no universal detector | partial | Bounded progress measures exist; they do not refute the narrowed statement. |
| Reality is intervention robustness | partial | The registered intervention family and dependence bounds remain ours. |
| A world may have one door | open | Line 12 H4 is direct evidence; no external generalization found. |

## Required anchors

1. Reproduce modular-addition grokking from a source-revision-pinned setup.
2. Reproduce Fourier progress measures with random-label and shuffled-order nulls.
3. Implement EWC and replay as named baselines, not inventions.
4. Include a semantics-preserving renaming/OOD negative anchor.

## Open literature debts carried into Level 1

- Active versus static learning under equal query count, with realized answer entropy reported as a mediator.
- Transfer into a genuinely different interface, not another arithmetic head.
- Seed-versus-architecture co-error decomposition on algorithmic tasks.
- Causal progress measures across multiple worlds.

Opus review attacks status strength, missing contradictory anchors, and novelty by
renaming. This map is not a preregistration.
