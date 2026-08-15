# PHILOSOPHIA_NOVELTY_SCAN_V1

## 1. Executive finding

As of 15 August 2026, Philosophia’s broad thesis is not novel.

Answers to the required questions:

1. **Yes.** Improvement from self-generated, verifier-accepted tasks is established directly by MINIMO, AlphaProof, STP, Absolute Zero, and related formal-proving systems.
2. **Yes.** Learned weights reducing later search is established particularly clearly by AlphaProof’s checkpoint-by-search-budget experiment.
3. **Yes, in broad form.** Human yoked-learning experiments replay exactly the selector’s observations to another learner; yoked machine learning directly compares a model using its own uncertainty against the same student trained on selections donated by another model. What I did not find is Philosophia’s exact reciprocal, identical-learner \(2\times2\) estimator in a formal world.
4. **Yes, in adjacent forms.** Fixed-weight memory studies compare relevant history against matched random content; false-memory experiments modify memory while keeping the question and agent architecture fixed. Explanation-training studies compare meaningful rationales with shuffled/random substitutes. None combines this control with inherited weights, self-generated verified derivations, and cross-family proof-work transfer.
5. **No located work jointly contains all five requested elements.** MINIMO supplies the small scratch learner and verifier-grounded axiomatic world; AlphaProof supplies verified learning, held-out transfer, and work reduction; yoked learning supplies donated-selection controls; memory studies supply corruption controls. Their conjunction remains untested.
6. **“Fractal world” is currently not a scientific variable.** Recursive conjecturing, theorem composition, subgoal curricula, growing difficulty and reusable structural hierarchy are already operationalized. Unless “fractal” is assigned an independently varied quantity—dependency depth, reusable-library growth, cross-scale invariance, or compression rate—it is a metaphor.
7. The narrow residue is a **joint causal claim**: recipient-state-specific selection under a reciprocal yoke, plus truth-specific retained-history value beyond weights, demonstrated through verifier-call reduction on held-out families and a semantics-preserving representation change.

That residue is genuine but fragile. It is an unrun protocol, not yet a result: the local record explicitly marks ACTIVE/YOKED as unrun and defines `PROOF_CORE`/`PROOF_STRONG` accordingly ([registered programme](</home/master/llm_projects/philosophia/essay/climbing-the-wall-of-experience.md:479>), [current reciprocal decision](</home/master/llm_projects/philosophia/successor/dev/PHASE2_POST_REVIEW_DRIVER_DECISION_19.md:31>)).

## 2. Prior-art comparison matrix

| Philosophia claim | Exact prior evidence | Assessment |
|---|---|---|
| Experience-driven agents are a new paradigm | Silver and Sutton describe continual learning from long experiential streams, but provide a position paper, not a causal experiment ([Era of Experience](https://storage.googleapis.com/deepmind-media/Era-of-Experience%20/The%20Era%20of%20Experience%20Paper.pdf)). | **Close but non-identical result**; not empirical priority. |
| Scratch learner bootstraps from verified, self-created mathematics | MINIMO starts an 8.45M-parameter Transformer randomly initialized, using only axioms in propositional logic, arithmetic and groups. Section 4/Figs. 2–4 show five conjecture/proof iterations and improvement on unseen human theorems ([paper, §§3.4–4.2](https://proceedings.neurips.cc/paper_files/paper/2024/file/4b8001fc75f0532827472ea5a16af9ca-Paper-Conference.pdf)). | **Direct prior result.** |
| Self-generated verified tasks improve a prover | AlphaProof’s main RL uses Lean-verified proofs/disproofs; Fig. 3b improves on held-out miniF2F-valid, formal-IMO and PutnamBench-test. STP Fig. 4 and §4.4 show generated conjectures provide denser signal and add about 2–3 points on miniF2F/ProofNet ([AlphaProof §§Training, Main RL](https://www.nature.com/articles/s41586-025-09833-y); [STP §4.4](https://arxiv.org/html/2502.00212)). | **Direct prior result.** |
| A learner creates tasks at its competence frontier | MINIMO scores conjecture difficulty under its current policy; STP trains on barely provable conjectures; Absolute Zero conditions proposals on historical examples and jointly trains proposer/solver; R-Zero rewards a challenger for problems near solver capability ([MINIMO §3.4](https://proceedings.neurips.cc/paper_files/paper/2024/file/4b8001fc75f0532827472ea5a16af9ca-Paper-Conference.pdf); [AZR Table 2](https://arxiv.org/html/2505.03335); [R-Zero §§2–4](https://arxiv.org/html/2508.05004)). | **Direct prior result.** |
| Learned weights reduce future work | AlphaProof Fig. 3c compares checkpoints at equal solve rate: the final agent solves about 30% with 300 simulations, a level earlier checkpoints cannot reach with much larger search ([Fig. 3c](https://www.nature.com/articles/s41586-025-09833-y)). | **Direct prior result.** |
| Knowledge amortizes across families/representations | Hamilton-Zero evaluates frozen weights on held-out topologies and sizes and reports transferred multiscale structure in §5.6. It does **not** provide a matched random-initialized/scratch optimizer arm; its §6 scratch-cost claim is therefore not itself a controlled result ([§§5.2, 5.6, 6](https://arxiv.org/html/2608.11911)). | Transfer: **direct**. Scratch work comparison: **unsupported inference**. |
| Own-state selection matters beyond random curricula | PLR prioritizes levels using current-policy TD error and improves sample efficiency/generalization; ALP-GMM selects by learning progress; MAGELLAN predicts the agent’s own competence and learning progress ([PLR experiments](https://proceedings.mlr.press/v139/jiang21b.html); [ALP-GMM Algorithm 1](https://proceedings.mlr.press/v100/portelas20a/portelas20a.pdf); [MAGELLAN](https://proceedings.mlr.press/v267/gaven25a.html)). | **Direct versus random/uniform**, but no yoke. |
| Own-state versus donated selection | Markant and Gureckis hold sequence and content identical across active/yoked human learners (§“Yoked Experiments”). Yoked machine learning uses the same student model with either its own uncertainty selection or another model’s selections; active wins 75 cases, ties 53, and loses 43 among comparisons where both beat random ([human yoke](https://www.gureckislab.org/publications/MarkantGureckisJEPGEN2013.pdf); [YoL Methods and Fig. 3](https://chemrxiv.org/engage/api-gateway/chemrxiv/assets/orp/resource/item/64d977544a3f7d0c0d1fedcb/original/yoked-learning-in-molecular-data-science.pdf)). | **Direct prior result** for the generic claim; no exact reciprocal formal-learner block. |
| Truthful history matters beyond having text | MemDelta Table 2 holds chunking, top-\(k\), and answer model fixed: random history obtains 3.2% versus 47.2% for relevant verbatim retrieval. False-memory attacks hold the later question fixed and produce 82/1,064 answer shifts. Random-token rationale training also underperforms coherent rationales ([MemDelta §§3–4.1](https://arxiv.org/html/2606.29914); [false-memory §§IV–V](https://arxiv.org/html/2606.29030); [rationale Table 4](https://arxiv.org/html/2511.02044)). | **Direct** for fixed-weight relevance/corruption; **close but non-identical** to a persistent proof ledger. |
| Process records add value beyond outcomes | Small-scale controlled experiments in *Let’s Verify Step by Step* find process-supervised reward models outperform outcome-supervised models; §4.2 reports 2.6× data efficiency from active selection ([§§2, 4](https://arxiv.org/html/2305.20050)). | **Direct prior result**; labels are external, not retained self-experience. |
| One system jointly tests scratch + verifier + reciprocal yoke + transfer + work | No located experiment contains all arms. | **Genuine residual novelty**, but presently novelty by conjunction. |

## 3. Claims already occupied

The following should not appear as Philosophia novelty claims:

- **“A model can improve by solving tasks it generated itself.”** MINIMO is decisive: random initialization, axioms only, self-generated conjectures, formal proof search and extrinsic held-out evaluation. Absolute Zero and R-Zero broaden the result to code-executed and pseudo-labelled reasoning.

- **“Verified outcomes can train better reasoning.”** DeepSeek-Prover V1.5 uses binary Lean verification in RL and improves held-out miniF2F/ProofNet over SFT ([§2.3 and Fig. 3](https://arxiv.org/html/2408.08152)). AlphaProof establishes the claim at much larger scale.

- **“Theorems/problems can form a progressively harder curriculum.”** Formal Mathematics Statement Curriculum Learning already shows expert iteration reaching composed inequalities inaccessible to search-only at equal compute ([§5 and Fig. 3](https://cdn.openai.com/papers/Formal_Mathematics_Statement_Curriculum_Learning__ICML_2022.pdf)). DeepSeek-Prover V2 turns decomposed subgoals into recursively solved lemmas and curriculum items ([§2.1](https://arxiv.org/html/2504.21801)).

- **“Weights store reusable experience that saves later work.”** AlphaProof’s checkpoint/search curves are a direct work-reduction result. Hamilton-Zero adds held-out topology, size and representation-structure transfer, although its claimed economics versus scratch lack the matched scratch arm.

- **“Matching tasks to the learner’s current state can matter.”** Active-learning, learning-progress and yoked-learning literatures already establish this, while also showing it is contingent: donated selection sometimes equals or exceeds self-selection.

- **“Reasoning history contains useful information beyond the final answer.”** Process supervision, relevant-memory controls and coherent-versus-random rationale experiments already occupy the generic version.

Formal Conjectures does not rescue novelty here. It supplies a Lean-kernel benchmark for verified discovery, but its exact FC100OpenSet1 evaluation reports a 0% baseline for all evaluated systems; it is a benchmark result, not evidence for Philosophia’s selector or ledger mechanism ([§4.1–4.2](https://arxiv.org/html/2605.13171)).

## 4. Claims only partially occupied

### Reciprocal selection

Prior work directly compares own and donated selection, but not the proposed reciprocal factorial on exact learner twins. The remaining estimand is narrower than “active learning works”: does batch utility depend specifically on the recipient state after cancelling recipient competence and intrinsic batch quality?

This is a methodological refinement of yoked learning, not a new learning paradigm.

### Truth-specific retained history

MemDelta already proves that relevant content beats equally sized random context with fixed weights. Absolute Zero’s Table 2 also shows that conditioning the proposer on historical reference triplets improves performance over a fixed prompt. Missing is the exact Philosophia contrast:

- identical inherited weights;
- identical record interface, size and access budget;
- truthful verified derivations versus permutation or semantic falsification;
- evaluation by verifier calls to threshold on unseen families;
- survival under algebra-to-Cayley re-encoding.

### Transfer

MINIMO transfers to unseen human-written statements within its trained domains. AlphaProof transfers to held-out competition sets. R-Zero reports transfer from self-generated mathematics to general-domain benchmarks. Hamilton-Zero transfers across topology, interaction type and scale.

What remains is therefore not “transfer,” but **truthful explicit history adding work reduction beyond transferred weights under both family and representation shift**.

## 5. Residual novelty

The narrow residue has two linked causal components:

1. **Recipient-specific task value:** within a reciprocal block, each learner benefits more—in subsequent verifier-call efficiency—from the batch selected using its own state than from the other learner’s matched batch.

2. **Semantic history value beyond weights:** holding inherited weights and ledger shape fixed, truthful verified history reduces work on unseen families and after semantics-preserving re-encoding more than false, permuted or content-destroyed history.

No located paper jointly tests these in a small scratch-trained formal learner. This is **genuine residual novelty**, provided the primary endpoint is work-to-held-out-truth and not training accuracy.

R-Zero’s collapse result makes finite-horizon wording essential: all tested model sizes eventually degraded over iterations, and a later analysis found self-play entropy collapse ([R-Zero §4.2](https://arxiv.org/html/2508.05004); [self-play analysis §3.3](https://arxiv.org/html/2510.27072)). Philosophia cannot infer open-ended or indefinitely compounding growth from a positive short run.

## 6. Strongest adversarial interpretation

Philosophia combines four established effects in a toy formal world:

- self-generated verified training;
- learner-conditioned curriculum selection;
- amortization in weights;
- useful relevant context.

The reciprocal yoke is cleaner causal bookkeeping, while the fake-ledger arm imports an established memory-corruption control. Their conjunction may improve identification without discovering a new learning principle.

“Fractal world” presently restates recursive conjecturing, composed statements, subgoal curricula or expert iteration. MINIMO explicitly identifies growing reusable definitions and lemmas as future cumulative learning; DeepSeek-Prover V2 already recursively converts subgoals into curriculum theorems. Without an intervention on a scale/dependency variable, “fractal” contributes no measurable construct.

A result where only inherited weights help would be entirely occupied. A ledger benefit restricted to familiar encodings would resemble retrieval. An ACTIVE advantage over random without the reciprocal yoke would resemble ordinary active curriculum learning.

## 7. Safest publishable claim wording

Until results exist, this should be described as a proposed test, not a discovery.

If both residual effects survive:

> In a scratch-trained formal learner, the utility of verified training tasks is recipient-state-specific: under a reciprocal matched-yoke design, tasks selected from the recipient’s own state reduce verifier work on preregistered held-out problems more than tasks selected from another learner’s state. Conditional on identical inherited weights, a truthful, shape-matched record of verified derivations provides additional work reduction that is not reproduced by false or permuted records and survives both held-out theorem families and a semantics-preserving representation change.

Do not claim autonomous mathematical discovery, open-ended self-improvement, manufacture of experience, theory building, or a new “fractal” learning regime.

## 8. Sources

Primary sources reviewed include: [Silver & Sutton](https://storage.googleapis.com/deepmind-media/Era-of-Experience%20/The%20Era%20of%20Experience%20Paper.pdf); [AlphaProof](https://www.nature.com/articles/s41586-025-09833-y); [MINIMO](https://proceedings.neurips.cc/paper_files/paper/2024/file/4b8001fc75f0532827472ea5a16af9ca-Paper-Conference.pdf); [formal statement curriculum learning](https://cdn.openai.com/papers/Formal_Mathematics_Statement_Curriculum_Learning__ICML_2022.pdf); [STP](https://arxiv.org/html/2502.00212); [Absolute Zero](https://arxiv.org/html/2505.03335); [R-Zero](https://arxiv.org/html/2508.05004); [self-play-collapse analysis](https://arxiv.org/html/2510.27072); [DeepSeek-Prover V1.5](https://arxiv.org/html/2408.08152); [DeepSeek-Prover V2](https://arxiv.org/html/2504.21801); [Formal Conjectures](https://arxiv.org/html/2605.13171); [Hamilton-Zero](https://arxiv.org/html/2608.11911); [Prioritized Level Replay](https://proceedings.mlr.press/v139/jiang21b.html); [ALP-GMM](https://proceedings.mlr.press/v100/portelas20a/portelas20a.pdf); [MAGELLAN](https://proceedings.mlr.press/v267/gaven25a.html); [Markant–Gureckis yoked learning](https://www.gureckislab.org/publications/MarkantGureckisJEPGEN2013.pdf); [yoked machine learning](https://chemrxiv.org/engage/api-gateway/chemrxiv/assets/orp/resource/item/64d977544a3f7d0c0d1fedcb/original/yoked-learning-in-molecular-data-science.pdf); [process supervision](https://arxiv.org/html/2305.20050); [MemDelta](https://arxiv.org/html/2606.29914); [false-memory intervention](https://arxiv.org/html/2606.29030); and [coherent-versus-random explanation training](https://arxiv.org/html/2511.02044).

NOVELTY_RESIDUE=RECIPROCAL_SELECTION_AND_TRUTHFUL_HISTORY
