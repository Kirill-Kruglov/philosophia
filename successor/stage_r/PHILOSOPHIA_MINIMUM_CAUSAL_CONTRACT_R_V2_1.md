# PHILOSOPHIA_MINIMUM_CAUSAL_CONTRACT_R_V2_1

Status: `DRAFT_FOR_ONE_BOUNDED_CONFIRMATION`. Standalone. This document supersedes `PHILOSOPHIA_MINIMUM_CAUSAL_CONTRACT_R_V2` and `PHILOSOPHIA_MINIMUM_CAUSAL_CONTRACT_V1` in full and is readable without amendment history. Where an earlier draft, proposal, review or correction record differs from a clause below, this clause governs.

---

## 0. Authority, pins and authorization state

### 0.1 Repository and base pins

| Pin                                                                 | Value                                                              |
| ------------------------------------------------------------------- | ------------------------------------------------------------------ |
| Philosophia recovery authority commit (authority for this contract) | `e7f7610f0a8c61f3730de829f102a07e653bca92`                         |
| Philosophia accepted Stage-A commit                                 | `41adcaa96e3281746a6e59247d0fed5d1c42260c`                         |
| MINIMO base commit                                                  | `6066f482c6752915ad21119f93dc162f4cb9db72`                         |
| Durable Stage-A patch SHA-256                                       | `e08a8d29d67d82297216722b3e13e6c1a3f4bd354962a2865b1cfc57a9980bbd` |
| Recovered-tree manifest SHA-256 (both patch routes)                 | `566ec1e597311b1e9291c8cd1ae51141159314cc7079cb52b0b4153a28cdd88c` |

Durable recovery root: `successor/recovery/phase2_stage_b_20260815/`. All hashes below are the pinned values in that directory's `SHA256SUMS`.

Historical provenance only: the earlier evidence-checkpoint commit `865b7c853ade3ef72d80f6425909693c7003298a` preceded recovery of the durable charter and is **not** the current recovery authority. It may be cited as history and may never be used to resolve a pin.

### 0.2 Accepted Stage-B objects (byte-exact, durable)

| Path under the recovery root                                                           | SHA-256                                                            |
| -------------------------------------------------------------------------------------- | ------------------------------------------------------------------ |
| `accepted_authority/PHASE2_STAGE_B_DEV_CORE_CHARTER_V1_1_1_BOUNDARY_CORRECTION.md`     | `703bf39cfe8f875f9be3781659a7365c1bc99c42f7523e43fef2c0a2c47b8311` |
| `accepted_l2/PHASE2_STAGE_B_L2_GENERATOR_ANNEX_FINAL_XY_REVIEW.md`                     | `3a78a53ecb8e5275f433bc03c50b7b93746c597e3d2d1fcf0bedd4249f102da8` |
| `accepted_l2/PHASE2_STAGE_B_L2_CODE_GATE_V1.json`                                      | `8961b5a97ee0972d83a071e1b1c82869a9841f5f01c45add12a88dbfee1010f0` |
| `accepted_l2/PHASE2_STAGE_B_L2_RAW_FIXTURE_EXCLUSIONS_V3.json`                         | `a1f907ad6665b7c96d91496c5a91d32f0f0cae63da48b6b26da6b292d48f528d` |
| `accepted_l2/learning/phase2_stageb_generator.py`                                      | `de9b05d6732dfe07c5303439a1fd533f9d6053a62a04480db0659075b16d2a34` |
| `accepted_l2/learning/test_phase2_stageb_generator.py`                                 | `01adece50de5dc4cece3acfed80b21725ca7400e5d375204d5010eaae0dca4e8` |
| `archive/accepted_l01/PHASE2_STAGE_B_L01_RAW_FIXTURE_EXCLUSIONS_V2.json`               | `31e319bdbfc7b17c65ac7c8698022c761f4f05790e1f044e692f736cf99d680a` |
| `archive/accepted_l01/learning/phase2_stageb_canonical.py`                             | `4f1c2490801a05236caa1a10193eeb5c7f8e03ba70a0263e6e12374d304fe7a0` |
| `archive/accepted_l01/learning/phase2_stageb_causes.py`                                | `574a81b75e98fbccc1f8e0344cf8fefd1ccb9e83043ac72e321d49798cb88c2e` |
| `archive/accepted_l01/learning/phase2_stageb_checker.py`                               | `1cedff634a60955a05e88a437f8100b70783b1900e523385a4da48e822673d2b` |
| `archive/accepted_l01/learning/phase2_stageb_render.py`                                | `c56073d0c4718aa5a95c48e5c58522937a935ca637d68687770126564a6d6621` |
| `archive/accepted_l01/learning/phase2_stageb_schema.py`                                | `00df17136fe8acfe53f9a56a1ff9d56c39c2c6a3cf7121dc722cf3978279e4a7` |
| `archive/accepted_l01/learning/test_phase2_stageb_checker.py`                          | `f107d87c687efa119a92d12cce93f23a9de51a863b0f68ab71acfc6f065dc03c` |
| `archive/accepted_l01/learning/test_phase2_stageb_l0.py`                               | `5ef47d7e69b289c36957272779c4168b2c701edd0f1ab500df3fb2f843307e55` |
| `archive/accepted_l01/learning/test_phase2_stageb_theory_enumerability.py`             | `6a75207e182ee2b24f306275f36b95d5583cf63f30c0f3d9152fc729759ef19e` |
| `archive/accepted_l01/learning/theories/propositional-logic-intuitionistic-fragment.p` | `2056deaf9c12a81dcb047e60154e8a473ffe235b5e48bb9433eb1d9f70afb507` |

Four accepted patch routes:

| Patch                                                                       | SHA-256                                                            |
| --------------------------------------------------------------------------- | ------------------------------------------------------------------ |
| `patches/minimo_phase2_stageb_l01_v1_1_1_repair_v3_delta.patch`             | `1a67b09fb63784662cce56359c5cff897023cceec2f3dd445739d0a04cf00736` |
| `patches/minimo_phase2_stagea_stageb_l01_v1_1_1_repair_v3_cumulative.patch` | `c0b0e9ab79a66696231e356a92f6ccace67911d2bbe5906918ca6f4cbbe9a065` |
| `patches/minimo_phase2_stageb_l2_v5_delta.patch`                            | `299114e32cbf59edced992a94cdf5c1e03e322cb32dbdb7a3f94f63dc4276b95` |
| `patches/minimo_phase2_stagea_stageb_l01_l2_v5_cumulative.patch`            | `3a570b2e35b15dc796d86cd8a997230c00bbf5aed3b5c06f3b14dca78b46b683` |

Route A (Stage A → L0/L1 V3 delta → L2 V5 delta) and Route B (final cumulative) converge byte-for-byte on the manifest hash in §0.1; the recovered tree runs `67/67` Stage-B tests. That is engineering feasibility, never Stage-R evidence.

### 0.3 Statistical authority pins

| Object                                                        | SHA-256                                                            |
| ------------------------------------------------------------- | ------------------------------------------------------------------ |
| `successor/stage_r/STAGE_R_AUTHOR_DECISION_PROPOSAL_V2.md`    | `b1262a7a1e20b3e0773702cf8cbfb50a9408832ee9a815002f61897cee8d7fe8` |
| `successor/stage_r/STAGE_R_AUTHOR_RATIFICATION_V1.md`         | `8a1c60cee27af132abdd14af268e904f9fd0409b821a9470d8d4db7cee190074` |
| `successor/stage_r/STAGE_R_AUTHOR_ASSEMBLY_CORRECTIONS_V1.md` | `6fb7128c846cac6d6f1668f80b2d782f56da833e50a1ab83ac63c6e4a38d416f` |
| `successor/stage_r/STAGE_R_AUTHOR_A6_REASON_PRECEDENCE_V1.md` | `33fac185a13b38ac25ba3bc035ae69feb0b8db69d4ddd61a19bcba3fd52c804d` |

The ratification record supersedes the V2 proposal wherever they differ. Its corrections B1–B5 are inlined in §5, §6, §7 and §8. The assembly-corrections record A1–A7 and the author-approved A6 boundary-reason precedence are inlined throughout this document. The baseline-confounded D8 total-value positive-control rule is void and may not be restored.

### 0.4 Non-authority

`archive/unaccepted_l3/PHASE2_STAGE_B_L3_IDENTITY_PROJECTION_ANNEX_V1_DRAFT.md` (`a3760d619f147ec083bcd7cab4b158d39f13bce963f12ff8db236c85a9c0601a`), `..._AUTHOR_CHOICES.md` (`f36e620e0a99a98f939f7ee2b1013fb59b45e022f56bbc15abe8f13c84f18ef4`) and `..._DRIVER_HANDOFF.md` (`4cc3bf9f98ae45c5e307a90a46fa10aaf004bd5b490f1601eb7d25734d38afdd`) are archival provenance only. They carry no implementation authority and cannot become authority by citation.

### 0.5 Pin resolution rule

Every pin above must resolve to its stated hash from a durable committed location. An unresolved, missing or mismatched pin **suspends this contract**: no dependent stage may begin, and the failure is recorded rather than worked around. `/tmp` and any disposable worktree are execution space only and are never the sole copy of an authoritative object.

This contract's own accepted bytes will be pinned by its future acceptance record. No self-referential hash for this document is asserted here, and no placeholder stands in for one.

### 0.6 Authorization state

This draft authorizes **nothing**. It does not authorize code, a generated plan or theorem, a fixture scan, a key or root, a selector execution, a learner instantiation, a disposable block, a scientific block, a commit or a push.

Acceptance of this contract may later authorize only the explicitly staged engineering work named in §4, in the order of §10. Disposable execution and scientific execution each require their own separate written authorization and their own freeze record; neither is granted here.

---

## 1. Claim and non-claims

### 1.1 The Stage-R claim

> In the single sealed Stage-R frame of §3, over the accepted Stage-B bands `S1–S4`, for the repaired-from-scratch Stage-A-compatible MINIMO learner class, under the frozen selector of §5, the frozen MCTS prover as configured, the frozen work cap `C`, and the frozen operational compute envelope of §7, recipient-state-matched task selection reduces the symmetric block-location parameter `theta` of the held-out capped entered-MCTS-work contrast `D_j` relative to reciprocal matched donated selection by more than the practical margin `delta = 0.10 * C`.

Formally the claim is `theta > delta`, where `theta` is the location parameter of §6.3 and `D_j` is the complete-twin-block contrast of §2.4.

The selected treatment batch and the held-out evaluation panel are disjoint under all three identities of §3.2. The endpoint is therefore always work on theorems the treatment did not contain.

### 1.2 Symmetric-location assumption, stated plainly

Inference assumes blocks are independent and `D_j = theta + e_j`, where the joint law of block errors is exchangeable under sign flips about `theta`. This is a **ratified modelling assumption**, not distribution-free inference for an arbitrary population mean. No low-`N` distribution-free mean interval over the bounded domain `D_j ∈ [-C, C]` is narrow enough for this route. If the symmetry assumption is rejected, the route closes; it is not replaced after data exist.

### 1.3 Programme context E and the exact transfer scope

The unrestricted programme claim E — *there exists some world family, learner class and finite budget for which self-selected contact yields transferable reduction of future work* — is existential. No finite set of bounded negatives can falsify E. The asymmetry is stated so that a bounded negative is legible as exactly what it is: the closure of one named cell, not a refutation of the programme. Because no finite negative touches E, "try a larger model, longer budget, richer world or a new proof-DAG" after a negative terminal is not repair; it is an unbounded search for a witness, and §11.5 refuses it prospectively.

**What `R_POSITIVE` would witness, exactly.** Because the treatment batch and the held-out panel are identity-disjoint under §3.2, a positive terminal supports **within-frame held-out transfer of task value**: tasks selected from the recipient's own state change subsequent work on *other*, identity-disjoint theorems inside the one sealed frame, more than reciprocal matched donated tasks do. That, and only that, is the sense in which one bounded positive can witness the weak existential E.

**What it never licenses.** Within-frame held-out transfer licenses no cross-frame transfer, no cross-family or cross-domain transfer, no representation-change invariance, no truthful-history or retained-record effect, no weights-versus-record decomposition, and no general transfer claim of any kind. Those are outside this contract entirely (§1.7, §1.8, §12.1).

This bounded transfer statement does not weaken §1.5 or §1.6: the mechanism remains undetermined between difficulty-by-competence matching and any epistemic account, and the result remains instrument-relative to the frozen prover.

### 1.4 Scope conditions

The claim is conditional on **one** sealed frame, **one** learner class, **one** selector, **one** prover configuration, **one** cap `C` and **one** compute envelope. The held-out panel is reused across blocks, so the design estimates block-level variability only. It does **not** estimate frame-level or theorem-population variability and licenses no generalization over frames, theorem populations, provers, caps or learner classes.

### 1.5 Named residual confound

A positive interaction is consistent with the selector matching item difficulty to recipient competence. Stage R does not distinguish that mechanism from any epistemic one. A positive terminal establishes **state-dependent task value in this cell**, transferring within the frame to identity-disjoint held-out theorems, and nothing about epistemic content, knowledge, understanding or acquired representation. This confound is not removed by the reciprocal design, because difficulty-by-competence is itself an interaction and does not cancel in §2.5.

### 1.6 Instrument relativity

The complete-prover (G4ip / subformula-bounded normal-form) frame audit is deferred by §4.2. Consequently **every** Stage-R result is explicitly instrument-relative to the frozen MCTS prover as configured. No claim about theorem difficulty, about provers in general, or about the intrinsic hardness of the generated fragment is authorized under any terminal.

### 1.7 Stage H is a separate possible later study

Truthful-history, false-history, ledger-form and representation-transfer questions are **removed from the active claim**. There is no Stage-H arm, endpoint, margin, control, sample size or terminal in this contract, and none is registered, pre-approved or sized here.

Stage H is a genuinely separate possible future study. If a Stage-R result is positive after unsealing, that outcome may **motivate** authoring a new Stage-H contract. Any such contract must pass its own idea gate and must be prospective to **its own** data and execution; it inherits no implementation, execution or resource authority from this contract, and this contract grants none. Stage H is not part of the Stage-R claim stack, and Stage R and Stage H may never be reported as one pre-registered combined experiment.

### 1.8 Non-claims

This contract authorizes no claim about: autonomous conjecture invention, theorem discovery or mathematical creativity; open-ended or indefinitely compounding self-improvement; manufacture of experience; physical-world or sensor grounding; general intelligence of the learner; novelty of self-generated verified learning, of active or curriculum selection, of learned-weight transfer, of useful relevant memory, or of work reduction from learned prover weights — all of which are occupied by prior work; cross-frame, cross-family or representation-invariant transfer; truthful history, retained records or ledger form; theorem-level `N`; uncapped latent work; scientific evidence from Stage A, Stage-B L0–L2, any accepted fixture, any gate artifact, or MINIMO Phase 1. The only transfer statement in scope is the within-frame held-out transfer of §1.3. Phase 1's post-hoc `882.866667` entered-iteration difference is scale context only and supplies no effect estimate and no precision.

---

## 2. Experimental unit, arms and estimand

### 2.1 Twins

Each block `j` instantiates two learners `A` and `B`: exact, independently initialized twins from sealed fresh initializations, sharing architecture, configuration, exact ASCII encoder, checkpoint/manifest fingerprint and every fail-closed config field. Device policy is pinned by §7.4; hardware availability may validate a requested device but never selects the learner.

### 2.2 Common reservoir and selected batches

Both twins are advanced to their acquired states under the identical registered protocol, then **frozen**. Each frozen twin scores the *same* sealed reservoir with the selector of §5 and produces one batch of 16 tasks (4 per band): `b_A` from state `A`, `b_B` from state `B`.

### 2.3 The four branches

Each block contains all four branches, each starting from the **same** frozen recipient state and receiving one frozen selected batch followed by **one aggregate update**:

| Branch | Recipient state `r` | Batch source `q` |
| ------ | ------------------- | ---------------- |
| `A<-A` | `A`                 | `b_A`            |
| `A<-B` | `A`                 | `b_B`            |
| `B<-A` | `B`                 | `b_A`            |
| `B<-B` | `B`                 | `b_B`            |

All four branches receive equal assigned proof budgets and equal update ceilings. This is one selected batch and one aggregate update — not an ordered sequential curriculum. Realized proof work, LM-query work and realized example volume may differ and are reported as protocol mediators, never as endpoints. All four branches are then evaluated on the **same** sealed held-out panel of §3.1.

### 2.4 Estimand

For held-out theorem `g` in band `s ∈ {S1,S2,S3,S4}`:

```text
X_{r<-q,g}  = min(entered_mcts_loop_iterations_{r<-q,g}, C)

Y_{j,s,g}   = ( X_{A<-B,g} - X_{A<-A,g} + X_{B<-A,g} - X_{B<-B,g} ) / 2

D_{j,s}     = mean over g in band s of Y_{j,s,g}

D_j         = ( D_{j,S1} + D_{j,S2} + D_{j,S3} + D_{j,S4} ) / 4
```

Band weights are equal at `1/4` each. Units are capped entered MCTS-loop iterations per held-out theorem. Lower `X` is better, so **positive `D_j` favours recipient-state-matched selection**.

### 2.5 Cancellation derivation

Under the additive model for uncensored work `X_{rq} = mu + rho_r + beta_q + gamma_{rq} + error`:

```text
X_{A<-B} - X_{A<-A} = (beta_B - beta_A) + (gamma_AB - gamma_AA) + error
X_{B<-A} - X_{B<-B} = (beta_A - beta_B) + (gamma_BA - gamma_BB) + error

D = [ (gamma_AB - gamma_AA) + (gamma_BA - gamma_BB) ] / 2 + error
```

Additive recipient competence `rho_r` cancels **within** each recipient's difference. Additive batch/source quality `beta_q` cancels **between** the two recipients — that cancellation is a between-recipient cancellation and therefore requires additivity on the registered analysis scale. The registered scale is raw capped work (§6.1).

Capping is nonlinear: `min(W, C)` compresses differences wherever mass sits at the cap, and overshoot is unobserved. Capping may therefore break the *latent-work* interpretation of the cancellation. The registered estimand is explicitly **capped work**. The censoring guards of §7.2 exist to prevent over-interpretation, never to reconstruct uncapped work.

### 2.6 Independent unit

One independently initialized twin pair with all four valid branches is **one complete twin block**, and the complete twin block is the independent unit for every inferential calculation without exception. A branch is never an independent unit. Theorem rows are repeated measurements averaged inside band and block; more held-out theorems reduce within-block noise and never increase `N`. All four branches are required; an invalid or missing branch invalidates its whole block and is never replaced post hoc (§9.3).

---

## 3. Frame, projection and exclusions

### 3.1 One sealed frame

Stage R uses one sealed theorem frame shared by every block, over the accepted Stage-B bands `S1 = 8..11`, `S2 = 12..17`, `S3 = 18..25`, `S4 = 26..37` non-`ASSUME` plan nodes:

| Component                                  | Size        | Per band |
| ------------------------------------------ | ----------: | -------: |
| sealed scientific reservoir (minimum)      | 64 tasks    | 16       |
| sealed held-out panel (fixed)              | 32 theorems | 8        |
| selected treatment batch per branch update | 16 tasks    | 4        |

A larger reservoir is permitted only if fixed and sealed before the first scientific block. Reservoir tasks are presented as public sequents only.

### 3.2 Disjointness

Reservoir and held-out panel must be pairwise disjoint under **all three** identities simultaneously:

1. alpha-canonical theorem identity;
2. public projection bytes;
3. reservoir-local canonical rule-skeleton identity.

Skeleton disjointness is required, not optional: without it the "held-out" panel may be a re-skinned reservoir, `X` would measure frame memorization, and the within-frame held-out transfer statement of §1.3 would be vacuous. The obligation is scoped to the sealed frame only (§4.1), not to a universal collision economy. If one sealed `S1–S4` frame cannot be filled at the sizes of §3.1 under all three disjointness relations and the exclusions of §3.3, the terminal is `R_FRAME_INFEASIBLE`.

### 3.3 Imported permanent exclusions

The following are hash-pinned and **permanently ineligible** for the reservoir, the held-out panel and any later science:

- every fixture in `PHASE2_STAGE_B_L01_RAW_FIXTURE_EXCLUSIONS_V2.json` (`31e319bd…`): 17 enumerability fixtures, 5 valid-plan fixtures, 2 renderer-only fixtures, both sequent hash kinds `RAW_ASCII_BYTES` and `CANONICAL_JSON_STRING_BYTES`;
- every fixture in `PHASE2_STAGE_B_L2_RAW_FIXTURE_EXCLUSIONS_V3.json` (`a1f907ad…`): 17 enumerability fixtures, 11 valid-plan fixtures — including the six frozen L2 code-gate rows `l2_gate_00 … l2_gate_05` — and 2 renderer-only fixtures;
- the five permanently excluded fixture root keys listed in that ledger (`0000…00`, `ffff…ff`, `5555…55`, `aaaa…aa`, `000102…1f`), which may never be used as a scientific root key;
- every item used in any L3 or L4 code gate, any generator or compile calibration, any selector-qualification set (§5), any acquired-state divergence probe (§5.3 gate 6), any disposable sizing/control execution (§6.5, §7.3), and any injected-coupling run (§8).

The exclusion ledger is imported, merged and hash-pinned **before** frame sealing. Qualification scope, disposable scope and scientific scope are identity-disjoint under all three identities of §3.2; no item, seed, key namespace or block identity crosses between them.

### 3.4 Projection

The learner and the selector observe **only** public projection bytes. Any leakage of a proof plan, witness, band-as-metadata, root, root_id, draw index, scaffold, skeleton, source identity, branch identity, held-out identity or any sealed field into any learner- or selector-visible surface is `R_IMPLEMENTATION_INVALID`. The L2 draw record is dev-internal and is never fed to a public projection.

---

## 4. Minimum engineering boundary and time kills

### 4.1 Required for Stage R — and only these

1. **L3 alpha-canonical public theorem identity and sealed public projection**, projection-only scope.
2. **Reservoir-local theorem identity and rule-skeleton identity**, computed over the sealed reservoir and held-out panel only, sufficient to certify §3.2.
3. **Minimum semantic L4 compile plus fresh empty-goal replay**, sufficient for reservoir membership and solvability witness.
4. **Repaired-from-scratch Stage-A-compatible learner** (Phase-1 checkpoints are disqualified for the repaired selector and for all Stage-R work).
5. **The exact selector of §5 and its pre-science qualification.**
6. **Branch-isolated reciprocal harness, counter-keyed randomization, accounting and the frozen analysis.**

### 4.2 Deferred, by explicit author ratification

Deferred from the Stage-R critical path: the eight-root quota terminal; universal `4x4` band quota fulfilment; rule-skeleton collision economy beyond the sealed frame; the full compiler-family catalogue; the complete-prover / G4ip audit; inverse, statement-model and alternative-proof audits; general L3/L4 extensibility; and Stage-B universality as a prerequisite for one reciprocal causal estimate.

The author has ratified these narrow deferrals as a boundary correction, not a silent override. The accepted L0–L2 predicates are unchanged and are not weakened; they remain feasibility inputs and never scientific evidence. Deferral of the complete-prover audit carries the price named in §1.6. If the author later refuses any deferral, that component returns to §4.1 as required work or the route closes; it cannot be silently ignored.

### 4.3 Time kills

- **L3 kill.** Projection-only L3 paper closure plus its code gate must close within **at most one focused implementation day** after contract acceptance.
- **L4 kill.** Minimum L4 paper closure plus semantic compile and fresh empty-goal replay on the frozen excluded valid plans must close within **at most three focused implementation days** after L3 closure.
- **One focused implementation day** is at most **eight working hours**.

Failure of either kill closes the MINIMO Stage-R route and returns to `IDEA_GATE`. It never expands scope, never converts into an open research programme, and never authorizes a substitute world. Every annex, closure record and gate artifact must exist in a durable committed location, at a stated hash, **before** its dependent stage begins.

These L3 and L4 focused-day deadlines are **engineering** kills. They are separate from the experimental compute envelope of §7.4 and are not charged against it.

---

## 5. Selector and pre-science qualification

### 5.1 Exact selector

For reservoir item `g`, take the exact public ASCII bytes of `d.elaborate(g)`, including the terminating EOS token. Under the frozen learner state, compute the total sequence log-likelihood `L_label` for each of the four registered labels `{hard, trivial, easy, fail}` over those exact bytes. The equal-prior label-posterior log-odds score is:

```text
s(g) = L_hard - logsumexp(L_triv, L_easy, L_fail)
```

Mean-logprob scoring and the legacy MINIMO bootstrap conjecturer are forbidden on the scientific path.

`s(g)` is then rank/quantile normalized **within** structural stratum `S1–S4` against the sealed deterministic target rank distribution, and the batch is drawn by **item-addressed Gumbel selection**: the Gumbel perturbation for each item is derived deterministically from that item's identity under the `selector_gumbel` counter-key namespace (§9.1), and the top 4 items per band are taken, giving the 16-task batch of §3.1.

### 5.2 Qualification scope

All qualification uses **disposable, split-disjoint** data only. No scientific reservoir item, held-out item, scientific outcome or scientific block identity participates. Every qualification item is added to the permanent exclusion ledger (§3.3).

Independent qualification unit: reservoir item identity, clustered by reservoir-local rule skeleton for interval resampling.

Minimum qualification set: **at least 60 disposable items per band, 240 total**; **at least 20 positive and 20 negative registered labels per band** for AUC gates; **at least 30 rule-skeleton clusters** in total. If these minima cannot be met, the terminal is `R_SELECTOR_QUALIFICATION_INADEQUATE`.

### 5.3 Qualification gates

1. **Stable elaboration.** Exact public `d.elaborate(g)` bytes identical across two clean replays for every qualification item. Failure: `R_IMPLEMENTATION_INVALID`.
2. **Identical-state equality.** Identical serialized state plus identical reservoir yields identical raw scores, identical normalized scores and identical selected batches. Failure: `R_IMPLEMENTATION_INVALID`.
3. **Sign.** `s(g)` predicts the registered hard/useful label in the correct direction with point `AUC >= 0.55` and lower 90% bootstrap bound `> 0.50`. Failure: `R_SELECTOR_ROUTE_CLOSED`.
4. **Raw-signal nondegeneracy.** Before normalization, every band and state has finite raw scores, raw `IQR >= 0.10` natural-log units, and at most `5%` tied raw scores. Failure from NaN/inf or serialization inconsistency: `R_IMPLEMENTATION_INVALID`; failure from flat model signal: `R_SELECTOR_ROUTE_CLOSED`.
5. **Normalization parity.** After normalization each band matches the sealed deterministic target rank distribution and is identical for identical input. This is an implementation-equality check, never a signal-strength gate. Failure: `R_IMPLEMENTATION_INVALID`.
6. **Acquired-state divergence.** In 8 disposable acquired-state twin probes, selected-batch Jaccard overlap must be `<= 0.70` in at least 6 probes. Cold same-state overlap must be exactly `1.00` in 8 of 8. Failure of cold identity: `R_IMPLEMENTATION_INVALID`. Failure of acquired divergence **while cold identity passes**: `CELL_CANNOT_HOST_ESTIMAND_FOR_THIS_LEARNER_CLASS` — a substantive, publishable statement about this learner class in this cell, not a bug and not a scientific result about selection.
7. **Incremental value beyond statement-only surface features.** Using out-of-fold disposable predictions, the selector must improve AUC over a registered statement-only difficulty regressor (length, connective and n-gram features) by point `dAUC >= 0.03` with lower 90% paired bootstrap bound `> 0`. Failure: `R_SELECTOR_ROUTE_CLOSED`.
8. **Leakage.** Selector input is public projection only, per §3.4. Any leakage: `R_IMPLEMENTATION_INVALID`.
9. **Uncomputable interval.** If a required bound cannot be computed because class balance, cluster count or finite-score requirements fail, return the relevant inadequacy or selector-closed terminal above. A gate is never waived and the resampling rule is never changed to rescue it.

### 5.4 Frozen bootstrap procedure (B3)

Every interval in §5.3 uses exactly: **100,000 counter-keyed resamples of whole rule-skeleton clusters**, stratified by `S1–S4`, each resampled cluster carrying all of its items; **percentile 90% interval**; the incremental-AUC comparison using the **same resample indices** for selector and statement-only predictions; folds assigned by rule-skeleton identity **before** fitting and reused by both predictors.

### 5.5 Terminal precedence inside qualification

Strictly in this order: `R_IMPLEMENTATION_INVALID` (gates 1, 2, 5, 8, and the NaN/serialization and cold-identity branches) → `R_SELECTOR_QUALIFICATION_INADEQUATE` (§5.2 minima unmet, or a required interval uncomputable for coverage reasons) → `CELL_CANNOT_HOST_ESTIMAND_FOR_THIS_LEARNER_CLASS` (gate 6 acquired divergence, cold identity passing) → `R_SELECTOR_ROUTE_CLOSED` (gates 3, 4-flat-signal, 7). A selector-route closure is final for this selector: no post-outcome replacement selector may be substituted.

---

## 6. Ratified endpoint, margin, interval and N

### 6.1 Primary endpoint

The primary endpoint is **raw capped entered MCTS-loop iterations** on the held-out panel, as defined by `X` in §2.4. It is the algorithm's assigned budget unit.

Mandatory companion endpoints, reported under every terminal: solve rate; successful new-leaf expansions; exact LM-query work; realized example volume; realized proof work; per-branch cap-hit rates. **Companions may never replace, rescue or reinterpret the primary endpoint after any outcome exists**, and no companion may be promoted to primary at any time.

### 6.2 Margin

```text
delta = 0.10 * C
```

Example only, not a selection: if `C = 8000` then `delta = 800`.

### 6.3 Interval procedure

Two-sided **90%** inverted sign-flip confidence set for the symmetric block-location parameter `theta`, under the assumption of §1.2.

1. The only inferential input is the vector `(D_1, …, D_N)` of complete-twin-block contrasts.
2. Candidate domain is bounded: `theta ∈ [-C, C]`.
3. For candidate `m`, `Z_j(m) = D_j - m`.
4. All `2^N` sign vectors are enumerated exactly; `N_max = 24` keeps exact enumeration the frozen law.
5. Statistic: `T_obs(m) = |mean_j Z_j(m)|`.
6. Randomization distribution: `T_b(m) = |mean_j b_j Z_j(m)|` over all sign vectors `b`.
7. Two-sided p-value: `p(m) = #{b : T_b(m) >= T_obs(m)} / 2^N`.
8. The 90% confidence set is `{ m ∈ [-C, C] : p(m) > 0.10 }`, with this strict inequality fixing boundary membership.
9. Endpoints are `L = inf` and `U = sup` of the accepted set. If the accepted set is disconnected, terminal decisions still use `L` and `U`.

Degenerate cases: if all `D_j = d`, then `p(d) = 1`; for any `m != d` the smallest attainable two-sided p-value is `2 / 2^N`; hence if `2/2^N <= 0.10` the set collapses to `{d}`, and if `2/2^N > 0.10` the accepted set is the whole domain `[-C, C]`. An all-zero sample is the special case `d = 0`, not a different rule. Minimum attainable two-sided p-value is `2/2^N`: `0.000488…` at `N = 12`, `1.192e-7` at `N = 24`.

### 6.4 Frozen endpoint computation (B2)

Endpoints are computed by **one sort-and-sweep pass over equality events**, not on a grid and never by Cartesian evaluation of all sign vectors against all intervals. Breakpoints are the solutions of `(mean_j b_j (D_j - m))^2 = (mean_j (D_j - m))^2`, together with `-C` and `C`; they are sorted once, the exceedance count is updated at each event, and comparisons use exact rational or integer arithmetic wherever the inputs permit. The literal `2 * 2^N`-intervals-by-`2^N`-vectors evaluation is forbidden as quadratic in `2^N`.

Before any disposable data exist, the analysis code gate must (i) compare the sweep against literal brute-force evaluation for **every** integer vector of lengths `1..8` over the alphabet `{-2,-1,0,1,2}` and for boundary and tie cases, and (ii) benchmark the procedure at the ratified `N_max = 24`. Inability to complete inside the analysis resource sub-envelope of §7.4 returns `R_ANALYSIS_INFEASIBLE`. This is an engineering totality condition. It is never permission to change the interval law after data exist.

### 6.5 Disposable sizing and block count

The disposable sizing/control set is **12 complete, permanently excluded twin block identities, fixed once**. How those fixed identities are executed across candidate caps is governed entirely by the conditional law of §7.3 (B4); this contract contains no unconditional statement that they are run once at `C_max`.

For each candidate cap `C`, using the disposable contrasts obtained under §7.3:

```text
require 12 valid disposable contrasts D^disp_j(C)
s(C)       = sample standard deviation of the 12 contrasts
s_upper(C) = s(C) * sqrt( 11 / chi2_{0.20, df=11} )        # one-sided 80% normal-model upper scale
s_plan(C)  = max( 1.5 * s_upper(C), 1.5 * delta(C) )
N_raw(C)   = ceil( ( (z_0.95 + z_0.80) * s_plan(C) / delta(C) )^2 )
             with z_0.95 = 1.644854, z_0.80 = 0.841621
N(C)       = 4 * ceil( max(N_raw(C), 8) / 4 )
```

This targets **80% power at a true location of `2 * delta`**. A candidate passes sizing iff `N(C) <= 24`; `N_min = 8`; `N` is always a multiple of four. If fewer than 12 valid disposable contrasts exist for a candidate, or the §7.3 prefix proof or candidate accounting fails, the terminal is `R_DISPOSABLE_SIZING_INADEQUATE`.

No Stage-R scientific outcome may alter `N`, `delta`, `C`, the interval law or the analysis code.

### 6.6 Planning assumptions are ratified, not derived

The `0.10` margin fraction, the 90% level, the symmetric-location model, the 80% power target, the `2 * delta` planning point, `N_min = 8`, `N_max = 24`, the four-block rounding, the chi-square 80% upper-scale bound, the `1.5` dispersion inflation, the 12-block disposable count and the candidate cap set are **author-ratified prospective choices**. None is algebraically necessary, and this contract does not describe them as such. They were ratified as one indivisible bundle before any disposable or scientific data existed.

---

## 7. Cap selection, censoring and compute

### 7.1 Cap indicators

```text
I_{r<-q,g} = 1  iff branch r<-q reaches cap C on held-out theorem g, else 0

H_{j,s} = mean over g in band s of ( I_{A<-B,g} - I_{A<-A,g} + I_{B<-A,g} - I_{B<-B,g} ) / 2

H_j     = ( H_{j,S1} + H_{j,S2} + H_{j,S3} + H_{j,S4} ) / 4
```

### 7.2 Symmetric censoring guards

- If `abs(mean_j H_j) > 0.05`, no directional scientific terminal is allowed. The result is `R_INFORMATIVE_BOUNDARY` with `boundary_reason = CENSORING_DIFFERENTIAL`.
- If any branch has a cap-hit rate `> 0.80` in more than `25%` of planned blocks, the terminal is `R_INVALID_CENSORING_DEGENERATE` — a non-scientific terminal.
- If the total cap-hit rate across all branches exceeds `0.60`, the result is `R_INFORMATIVE_BOUNDARY` with `boundary_reason = CAP_DOMINATED`.

The guard is deliberately symmetric. More cap hits in mismatched branches can attenuate a true positive by compressing high latent work; more cap hits in matched branches can distort the other way. Because overshoot is unobserved, **direction is never inferred from the sign of the cap-hit contrast**. The primary target is capped work; cap diagnostics constrain interpretation and never reconstruct latent uncapped work.

### 7.3 Cap candidates and the conditional B4 execution law

Candidate set, ratified before any disposable execution:

```text
C_candidates = {4000, 8000, 12000, 16000}
```

The **twelve disposable block identities are fixed once** and are permanently excluded (§3.3). Their execution across candidates follows this conditional law and no other:

1. The fixed identities are executed at `C_max = 16000` **if and only if** complete held-out evaluation state, action ordering and trace-prefix identity is *proven* — so that every lower evaluation cap is exactly reconstructible from that execution, and no upstream branch state depends on `C`.
2. A lower candidate cap may be derived from such an execution **only** for a held-out evaluation search whose complete state, action ordering and trace prefix are proven identical up to that lower cap.
3. Training and acquisition searches, generated examples and updates may **never** be counterfactually truncated from a higher-cap execution.
4. If `C` affects any upstream branch state, or if the prefix identity of (1)–(2) is not proven, the **same twelve fixed identities** receive candidate-specific counter-keyed branch executions, one per candidate cap requiring it.
5. Failure of the prefix proof together with failure to complete the candidate-specific executions, or accounting insufficient to derive every candidate, returns `R_DISPOSABLE_SIZING_INADEQUATE`.

Whichever mode applies, logging must be sufficient to reconstruct every candidate quantity: entered iterations by theorem and branch; cap-hit indicators for every candidate cap; timestamps or iteration-time records sufficient to compute candidate-cap wall time; LM-query counts; update time; realized example volume; retry and control failures; RAM and output size. The mode actually used, and its prefix proof or its candidate-execution ledger, enter the freeze record (§10.1).

### 7.4 Administrative maximum compute envelope

Ratified as a ceiling:

```text
machine=AMD_RYZEN_AI_MAX_PLUS_395_PRIMARY_WORKSTATION
processes=1
threads_per_process=1
device_policy=CPU_ONLY
total_wall_hours=168
RAM_GiB=96
durable_storage_GiB=100
analysis_wall_hours=8
```

The `total_wall_hours` ceiling is **total**: it covers selector qualification, the analysis code gate, all disposable candidate work required by §7.3, the injected counterpart of the positive control, at most 24 scientific blocks and the frozen retry reserve. The `analysis_wall_hours` sub-envelope governs §6.4. The L3 and L4 focused-day engineering kills of §4.3 are separate deadlines and are not charged here.

### 7.5 Closed selection rule with total-envelope accounting

For each candidate `C`, compute `delta(C)`, the censoring summaries, `s_plan(C)`, `N(C)`, and:

```text
T95(C)                    = 1.5 * max observed disposable complete-block wall time at cap C

FixedSpent(C)             = actual elapsed qualification
                          + actual elapsed analysis code-gate work
                          + actual elapsed disposable candidate work required by §7.3

PositiveControlReserve(C) = 12 * T95(C)
ScientificReserve(C)      = 1.2 * N(C) * T95(C)      # the 1.2 factor is the frozen retry reserve

TotalRequiredWall(C)      = FixedSpent(C) + PositiveControlReserve(C) + ScientificReserve(C)
```

A candidate is **time-feasible** only if `TotalRequiredWall(C) <= 168 hours`. It is not sufficient for the scientific component alone to fit inside 168 hours. `PositiveControlReserve(C)` is ring-fenced: the injected positive-control counterpart may never borrow wall time from `ScientificReserve(C)`, and exceeding its own reserve is `R_RESOURCE_INFEASIBLE_FOR_REGISTERED_MARGIN`.

Memory and storage are accounted the same total way:

```text
TotalRequiredRAM(C)     = max( measured peak pre-science RAM,
                               reserved peak RAM for the positive control and scientific blocks )
                          <= 96 GiB

TotalRequiredStorage(C) = measured durable output already written
                          + reserved durable output for the positive control and scientific blocks
                          <= 100 GiB
```

Select the **largest** candidate cap satisfying all of: `N(C) <= 24`; `TotalRequiredWall(C) <= 168 hours`; `TotalRequiredRAM(C)` and `TotalRequiredStorage(C)` within their ceilings; no censoring precheck terminal. If no candidate passes, the terminal is `R_RESOURCE_INFEASIBLE_FOR_REGISTERED_MARGIN` — Stage R closes as resource-infeasible rather than expanding.

The selected values fix the **provisional operational envelope**: CPU/thread/process/device policy, wall-time, draw/search/update limits, batch size, held-out size, output limits, `C`, `delta` and `N`. It becomes the final operational envelope on positive-control success (§8, §10.2) and is signed and frozen before scientific block 1. It is never larger than §7.4, and **no scientific outcome may enlarge or alter it**.

---

## 8. Injected-coupling positive control

### 8.1 Chronology and design (B1 and A5 — the void D8 rule is not restored)

The positive control runs **after** `C`, numeric `delta`, `N` and the provisional operational envelope have been selected by §6.5 and §7.5, and **before** final sealing. Resource feasibility therefore precedes it: without a selected `C` and a reserved `PositiveControlReserve(C)` the control cannot run at all.

Exactly **one** paired B1 control is run, at the selected `C` and `delta`, on the **same twelve fixed disposable block identities and counter-keyed treatment variates**:

- `D_base,j` is the disposable block contrast at the selected cap `C`, obtained under the §7.3 execution law, for `j = 1..12`;
- `D_inj,j` is the block contrast from **one** injected execution in which a frozen synthetic coupling of known magnitude **`+2 * delta`** is injected into the disposable reciprocal harness, targeting the mismatched branches at the block-contrast level, on those same identities and variates;
- the paired increment and its point estimate are

```text
Q_j               = D_inj,j - D_base,j        for j = 1..12
point_estimate(Q) = mean_j Q_j                # arithmetic mean, literally
```

The injected execution passes through the **entire** frozen pipeline under test: branch isolation, accounting, block aggregation, band weighting, censoring guards and the §6.3–6.4 interval computation. The control is a **harness-level** injected-coupling fixture. Implementing it by adding `2 * delta` to `Q` or to `D` inside the interval routine, or anywhere in the analysis fixture, is **forbidden**: that makes `Q_j` identically `2 * delta` by construction and tests nothing about the harness. Censoring applies to the injected execution exactly as to any other; realized deviation from `+2 * delta` is absorbed by the acceptance window below.

### 8.2 Recovery criterion

The positive control passes if and only if **all** of:

1. the frozen 90% confidence set for the symmetric location of `Q` has **lower endpoint above `delta`**;
2. `point_estimate(Q) = mean_j Q_j` lies in `[1.75 * delta, 2.25 * delta]`;
3. all deterministic-replay, branch-isolation and accounting-conservation controls pass on both the base and injected executions.

Final sealing (§9.5, §10.1) occurs only after the control passes.

### 8.3 Attainability proof

With 12 blocks the smallest attainable two-sided sign-flip p-value is

```text
2 / 2^12 = 0.00048828125 < 0.10
```

In the favourable constant case `Q_j = 2 * delta` for all 12 blocks, every `m != 2 * delta` has p-value `0.00048828125 <= 0.10` while `m = 2 * delta` has p-value `1`; the confidence set collapses to `{2 * delta}` and its lower endpoint `2 * delta` exceeds `delta`. The gate is therefore attainable under the frozen interval law. (A 4-block gate would be impossible, since `2/2^4 = 0.125 > 0.10`.)

### 8.4 Failure

Failure is `R_POSITIVE_CONTROL_FAILURE`. No scientific block may start. A failed positive control means the analysis cannot detect the effect it claims to test, so it **can never support a negative or boundary conclusion** and yields no Stage-R scientific statement of any kind.

---

## 9. Randomization, order, retry, attrition and sealing

### 9.1 Counter-keyed randomization

Deterministic counter-keyed randomization with fully independent namespaces for: `block`; `twin_init`; `branch`; `reservoir_draw`; `selector_gumbel`; `evaluation_order`; `retry`. No namespace shares state with another, and no global RNG is read on the scientific path.

Metamorphic invariant: the same serialized state plus the same task batch yields byte-identical generated examples, optimizer state, weights and evaluation. Failure of this invariant makes the design invalid (`R_IMPLEMENTATION_INVALID`); it is never repaired by adding an arm.

### 9.2 Order and balance

`N` is divisible by four. Branch execution order uses repeated sealed **Latin-square cycles** over the four branch labels `A<-A, A<-B, B<-A, B<-B`, so branch position is balanced over each complete four-block cycle. Held-out evaluation order is counter-keyed and balanced within the panel. Balanced branch order and balanced evaluation order are mandatory, not advisory.

### 9.3 Retry and attrition

Whole-block retry triggers are **control-based and evaluated blind to `X`**: projection or replay mismatch; deterministic-replay failure; branch-isolation or key collision; environment interruption before all four branches complete; manifest or hash mismatch; accounting-conservation failure. No outcome value may trigger a retry.

A branch is never replaced alone. Each planned block has exactly **one** predeclared retry seed; the retry preserves the same Latin-square cycle and position; the original failed block remains in the attrition ledger; there is no replacement seed beyond that single paired retry.

Attrition ceilings: if more than `10%` of planned blocks, or more than `2` blocks in total, fail after retry, the terminal is `R_INVALID_ATTRITION`. If unrepaired missingness breaks a complete four-block order cycle, the terminal is `R_INVALID_ORDER_BALANCE` unless worst-case imputation is applied to the full planned cycle.

### 9.4 Missing-`D_j` worst-case rule

The primary vector always has length equal to the planned `N`. Valid blocks contribute their observed `D_j`. Missing blocks are imputed at `-C` when testing `R_POSITIVE` and at `+C` when testing `R_BOUNDED_NEGATIVE`. A directional terminal requires success under its own adverse imputation; otherwise the result is `R_INFORMATIVE_BOUNDARY` with `boundary_reason = MISSINGNESS_ADVERSE_IMPUTATION`.

### 9.5 Sealing — what is secret, what is committed, when it is unsealed

**Committed publicly before execution (hash only, contents sealed):** key commitments (never the keys themselves — this contract mints no key and no root); seed commitments; the block schedule; the branch and evaluation order schedule; reservoir and held-out membership; public projections; theorem identities; rule-skeleton identities; the environment hash; the analysis script hash; the complete freeze record of §10.1.

**Secret until unsealing:** actual keys and seeds; per-branch raw outcomes; block contrasts; all companion endpoint values.

**Unsealed once, after the single scientific run completes and the planned block vector is complete:** the analysis is executed exactly once, by the committed analysis script, against the frozen terminal precedence of §11. All inference is at block level. No interim Stage-R outcome is inspected, and no partial Stage-R result may inform any remaining Stage-R execution.

---

## 10. Freeze record and chronology

### 10.1 Freeze record contents

The final preregistration seals, at stated hashes: the recovered Stage-B objects and their durable locations, including the durable charter path (§0.2); the merged exclusion ledger, including the six frozen L2 rows and every disposable, qualification, replay, sizing, injection and calibration item (§3.3); L3 public projection rules and hashes; the L4 compile/replay acceptance record and hashes; the sealed frame ID; the `S1–S4` band definitions; reservoir theorem identities, public projection hashes and rule-skeleton identities; held-out theorem identities, public projection hashes and rule-skeleton identities; the learner configuration, checkpoint and manifest fingerprint; the exact ASCII encoder; the selector formula, raw-score gates, normalization rule and qualification outputs; the statement-only regressor definition and its qualification outputs; the B3 bootstrap parameters; the margin fraction, `C` and numeric `delta`; the confidence level, sign-flip interval law, B2 event-sweep endpoint rule, its oracle-test record and bounded domain; the §7.3 disposable execution mode actually used, together with its prefix proof or its candidate-execution ledger; the twelve fixed disposable identities, `s(C)`, `s_upper(C)`, `s_plan(C)`, `N_raw(C)` and rounded `N`; the total-envelope accounting `FixedSpent(C)`, `PositiveControlReserve(C)`, `ScientificReserve(C)`, `TotalRequiredWall(C)`, `TotalRequiredRAM(C)` and `TotalRequiredStorage(C)`; the B1 injected-coupling magnitude, the paired `Q_j` rule, `point_estimate(Q)` and the recovery result; the censoring, retry, attrition, missingness and order-balance rules and the `boundary_reason` enumeration; randomization namespaces, key commitments, seed commitments and the Latin-square schedule; the administrative maximum envelope and the final operational envelope; the analysis script and hash; the terminal precedence; and the explicit statement that Stage H is not registered by this contract.

### 10.2 Total chronological state machine

```text
 1. contract acceptance (this document, after one bounded confirmation)
 2. L3 projection-only kill        — at most 1 focused day        (engineering)
 3. L4 minimum compile/replay kill — at most 3 focused days       (engineering)
 4. implementation and code gates, including the B2 analysis-sweep oracle gate
 5. selector qualification on excluded, split-disjoint disposable data
 6. disposable sizing/control work on the twelve fixed excluded identities,
    executed under the conditional §7.3 law (single proven-prefix C_max
    execution, or candidate-specific counter-keyed executions)
 7. closed computation of C, numeric delta, N and the provisional operational
    envelope, including the total 168-hour / 96-GiB / 100-GiB feasibility test
 8. exactly one B1 paired positive control at the selected C and delta
 9. final freeze and sealing, only after the positive control passes
10. separate written execution authorization
11. one Stage-R scientific run
12. single unsealing and one analysis pass under §11
```

Each step begins only after its predecessor has a durable committed closure record. Any change after step 9 either follows a predeclared invalid-run rule or creates a new experiment version; it may never be described as repair of the same experiment after seeing its answer.

### 10.3 Envelope chronology, resolved

The `168`-hour, `96`-GiB and `100`-GiB figures of §7.4 are the **administrative maximum**, ratified before any measurement, and they bound the whole experimental programme — qualification, analysis code gate, all disposable candidate work, the positive control and the scientific blocks with their retry reserve. The **operational** envelope — the specific frozen `C`, `delta`, `N`, wall-time and resource limits actually used — is computed by the closed rules of §6.5 and §7.5 after the disposable work is measured, becomes final on positive-control success, and is frozen before scientific block 1. The operational envelope can only be smaller than or equal to the administrative maximum, and no scientific outcome can change either. The L3/L4 focused-day kills are engineering deadlines outside this accounting (§4.3).

---

## 11. Total terminals and interpretation

### 11.1 Terminal precedence, in strict order

| #   | Terminal                                                                             | Fires when                                                                                                                                                  |
| --: | ------------------------------------------------------------------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 1   | `R_IMPLEMENTATION_INVALID`                                                           | leakage, projection failure, replay or determinism failure, manifest/hash mismatch, accounting-conservation failure, branch-isolation failure               |
| 2   | `R_FRAME_INFEASIBLE`                                                                 | one sealed `S1–S4` frame cannot be filled at §3.1 sizes under §3.2 disjointness and §3.3 exclusions                                                         |
| 3   | `R_SELECTOR_QUALIFICATION_INADEQUATE`                                                | §5.2 minima unmet, or a required interval uncomputable for coverage reasons                                                                                 |
| 4   | `CELL_CANNOT_HOST_ESTIMAND_FOR_THIS_LEARNER_CLASS`                                   | acquired-state divergence fails while cold identity passes                                                                                                  |
| 5   | `R_SELECTOR_ROUTE_CLOSED`                                                            | selector sign, flat raw signal, or surface-incremental value fails                                                                                          |
| 6   | `R_ANALYSIS_INFEASIBLE`                                                              | the B2 sweep fails its oracle comparison, or cannot complete at `N_max = 24` inside the 8-hour analysis sub-envelope                                        |
| 7   | `R_DISPOSABLE_SIZING_INADEQUATE`                                                     | fewer than 12 valid disposable contrasts for a candidate, §7.3 prefix proof and candidate executions both unavailable, or candidate accounting insufficient |
| 8   | `R_RESOURCE_INFEASIBLE_FOR_REGISTERED_MARGIN`                                        | no candidate cap satisfies sizing, censoring prechecks and the **total** §7.5 wall/RAM/storage tests, or the positive-control reserve is exceeded           |
| 9   | `R_POSITIVE_CONTROL_FAILURE`                                                         | the paired `Q_j` criterion of §8.2 is not met                                                                                                               |
| 10  | `R_INVALID_CENSORING_DEGENERATE` / `R_INVALID_ATTRITION` / `R_INVALID_ORDER_BALANCE` | §7.2 degenerate branch censoring; §9.3 attrition ceiling; §9.3 broken order cycle without worst-case imputation                                             |
| 11  | `R_POSITIVE`                                                                         | every control valid **and** confidence lower endpoint `L > delta` **and** all censoring and missingness guards pass                                         |
| 12  | `R_BOUNDED_NEGATIVE`                                                                 | every control valid **and** confidence upper endpoint `U < delta` **and** all censoring and missingness guards pass                                         |
| 13  | `R_INFORMATIVE_BOUNDARY`                                                             | the run is scientifically valid and no directional condition is reached, with `boundary_reason` recorded per §11.2                                          |

A higher-precedence terminal always fires first and suppresses everything below it. Terminals 1–10 are **feasibility or instrument terminals**: they make **no** Stage-R causal statement of any kind, in either direction. `R_RESOURCE_INFEASIBLE_FOR_REGISTERED_MARGIN` precedes `R_POSITIVE_CONTROL_FAILURE` because a selected `C`, a numeric `delta` and a reserved control budget must exist before the control can run at all.

### 11.2 Exactly three scientific terminals

`R_POSITIVE`, `R_BOUNDED_NEGATIVE` and `R_INFORMATIVE_BOUNDARY` are the only scientific terminals. There are no separate boundary terminals; non-invalid censoring, cap domination and adverse missingness imputation are **reasons attached to the single boundary terminal**:

```text
terminal = R_INFORMATIVE_BOUNDARY
boundary_reason in {
  INTERVAL_SPANS_MARGIN,
  CENSORING_DIFFERENTIAL,
  CAP_DOMINATED,
  MISSINGNESS_ADVERSE_IMPUTATION
}
```

If several non-invalid boundary conditions apply, `boundary_reason` is the
first applicable value in this strict order:

```text
CENSORING_DIFFERENTIAL
CAP_DOMINATED
MISSINGNESS_ADVERSE_IMPUTATION
INTERVAL_SPANS_MARGIN
```

`R_INFORMATIVE_BOUNDARY` is reached only when every control needed for a scientifically valid capped-work run has passed. Invalid censoring, attrition and order imbalance remain higher-precedence non-scientific terminals (row 10).

Worked illustration at `delta = 800`: `L=900, U=1400` is `R_POSITIVE`; `L=-100, U=700` is `R_BOUNDED_NEGATIVE`; `L=200, U=1000` is `R_INFORMATIVE_BOUNDARY` with `boundary_reason = INTERVAL_SPANS_MARGIN`.

### 11.3 Failure to reject is never a negative

A null or non-significant result — for example the interval `[-300, 1200]` — is `R_INFORMATIVE_BOUNDARY` with `boundary_reason = INTERVAL_SPANS_MARGIN`. `R_BOUNDED_NEGATIVE` requires the **upper endpoint to lie strictly below `delta`**, an equivalence-style decision. Absence of evidence for a positive effect is never, under any circumstance, recorded as a bounded negative.

### 11.4 Interpretation of each scientific terminal

- **`R_POSITIVE`.** Within the sealed frame, learner class, selector, prover, cap and envelope, recipient-state-matched selection reduces held-out capped work by more than `delta`. This is bounded state-dependent task value in this cell, and — because the treatment batch and the held-out panel are identity-disjoint under §3.2 — it supports **within-frame held-out transfer of that task value** and supplies one witness to the weak existential E (§1.3). It supports nothing about scale, cross-frame or cross-family transfer, representation change, retained history, theorem difficulty, prover generality, or epistemic content (§1.5, §1.6, §1.8). After unsealing, it may motivate authoring a separate Stage-H contract under §1.7; it confers no implementation or execution authority on that contract, and Stage R and Stage H may never be reported as one pre-registered combined experiment.
- **`R_BOUNDED_NEGATIVE`.** In this frame, learner class, budget and endpoint, own-state selection carries no practically useful advantage over reciprocal matched donated selection. E is untouched (§1.3). This closes the MINIMO own-state-selection line.
- **`R_INFORMATIVE_BOUNDARY`.** The effect, if present, is not resolvable against `delta` at the frozen `N` for the recorded `boundary_reason`. Publish the interval and the reason. Do not extend the run.

### 11.5 No automatic escalation

An `R_BOUNDED_NEGATIVE` or `R_INFORMATIVE_BOUNDARY` at the frozen `N` **ends this MINIMO own-state-selection line**. It may not be followed by a larger `N`, a larger model, a longer budget, a richer world, a new proof-DAG, additional blocks, a different selector, or a return "because the cell was too small". Any of those is a new line requiring its own idea-gate pass and its own contract. Every feasibility or instrument terminal (rows 1–10) says nothing scientific in either direction, and rerun authority exists only where this contract named the failure and its remedy in advance.

---

## 12. Claims prohibited and review-loop closure

### 12.1 Prohibited claims

No result under this contract authorizes any claim about:

- autonomous conjecture invention, theorem discovery, curriculum self-design or information acquisition — the construct is self-calibrated task selection from a supplied verified reservoir;
- open-ended or indefinitely compounding self-improvement;
- universal manufacture of experience;
- physical-world or sensor grounding;
- **epistemic interpretation beyond state-dependent task value** (§1.5);
- **transfer beyond the within-frame held-out sense of §1.3** — in particular no cross-frame, cross-family, cross-domain or representation-invariant transfer;
- **uncapped latent work, theorem difficulty, prover generality, frame generality, or any theorem-population parameter** (§1.4, §1.6, §7.2);
- **novelty** of self-generated verified learning, of active or learning-progress selection, of learned-weight transfer, of useful relevant memory, of process supervision, or of work reduction from learned prover weights — each is occupied by prior work;
- **Stage H in any form**: truthful history, retained records, false or permuted or content-destroyed records, ledger form, or representation change; and no combined pre-registered Stage-R-to-Stage-H experiment;
- theorem-level `N` inflation, or any inference whose unit is a branch, theorem, search attempt or seed row;
- Stage-B universality, eight-root quota fulfilment, or band-coverage completeness;
- **scientific evidence from any accepted engineering artifact**: Stage A, Stage-B L0–L2, the generator, the checker, the code gate, any fixture, the recovery checkpoint, or MINIMO Phase 1;
- any claim from audit-14b beyond its frozen `POLICY_CHANNEL_VIABLE` development verdict;
- essay slot discharge: no essay slot is filled or discharged by Stage R.

### 12.2 Review-loop closure

```text
GENERAL_REVIEWS_REMAINING=0
STATISTICAL_REPAIR_PASSES_REMAINING=0
```

The single permitted general scientific and architecture review of this contract is complete, and the single permitted statistical repair pass is complete. Exactly **one targeted confirmation** of this assembled text remains. That confirmation may check only the closure of the already enumerated findings — C1–C2, M1–M10, the nine Minors, B1–B5, A1–A7 and the deterministic A6 boundary-reason precedence — against the text above. It may not raise a new architecture finding, propose a new arm, request an annex, request additional literature review, or request another reviewer. Remaining disagreement is settled by explicit author ratification or by route closure, never by another general review.

A finding blocks a gate only if it can change typing, randomization, treatment contrast, independent unit, endpoint, leakage status, terminal classification or reproducibility. Style, hypothetical future generality and unclaimed extensions do not reopen a closed gate.

---

```text
CONTRACT_ROUTE=THIN_MINIMO_RECIPROCAL_STAGE_R_ONLY
STAGE_H_REGISTERED=NO
INDEPENDENT_UNIT=COMPLETE_TWIN_BLOCK
GENERAL_REVIEWS_REMAINING=0
STATISTICAL_REPAIR_PASSES_REMAINING=0
IMPLEMENTATION_AUTHORIZED=NO
SCIENTIFIC_EXECUTION_AUTHORIZED=NO
READY_FOR_BOUNDED_CONTRACT_CONFIRMATION=YES
```
