# STAGE_R_AUTHOR_DECISION_PROPOSAL_V2

Paper-only bounded repair. This repairs only R1–R9 against V1. No route reopened. No Stage H design added.

## Total chronology

1. Author ratifies the compact table in D14 or closes the route.
2. Projection/replay, public identity, reservoir-local theorem identity and rule-skeleton identity are fixed on excluded material only.
3. Selector qualification runs on split-disjoint disposable data only.
4. One fixed disposable sizing/control set of 12 complete twin blocks is run at the maximum ratified candidate cap, with enough logging to derive every lower candidate cap.
5. For every candidate cap, compute `C`, `delta`, censoring summaries, disposable dispersion, rounded `N`, positive-control recoverability and resource feasibility by the closed rules below.
6. Select the largest candidate cap satisfying all closed feasibility rules.
7. Freeze frame, reservoir, held-out panel, exclusions, selector, randomization, `C`, `delta`, interval law, `N`, retries, censoring, analysis hash and compute envelope.
8. Run Stage R once.
9. Analyze complete planned block vector only under the frozen terminal precedence.

No third statistical design pass is authorized. Remaining disagreement is resolved by author ratification or route closure.

## R1–R9 repair map

| Finding | Repaired sections |
|---|---|
| R1 positive-control impossible at 4 blocks | D3, D8 |
| R2 sign-flip estimand/degenerate behavior | D3, proofs |
| R3 disposable variance unstable | D4, D11 |
| R4 cap/margin/N/envelope circularity | chronology, D2, D4, D5, D11 |
| R5 censoring notation/direction | D5, proofs |
| R6 Latin-square balance/arbitrary N | D4, D9, D10 |
| R7 author choices mislabeled | D14 |
| R8 selector qualification not closed | D7 |
| R9 frame terminology/bands | D1, D6, D13 |

---

## D1 — Primary analysis scale

Recommended rule: preserve raw capped entered MCTS-loop iterations.

For theorem `g` in accepted band `s ∈ {S1,S2,S3,S4}`:

`X_{r←q,g} = min(entered_mcts_loop_iterations_{r←q,g}, C)`

`Y_{j,s,g} = (X_A←B,g - X_A←A,g + X_B←A,g - X_B←B,g) / 2`

`D_{j,s} = mean_g Y_{j,s,g}`

`D_j = (D_{j,S1}+D_{j,S2}+D_{j,S3}+D_{j,S4}) / 4`

Units: capped entered MCTS-loop iterations per held-out theorem. Positive `D_j` favours own-state selection.

The primary estimand is the mean of `D_j` over independent complete twin blocks, conditional on one sealed frame, one learner class, one selector, one prover and one compute envelope.

Evidence allowed: driver decision only for endpoint/sign; accepted S1–S4 band definitions; excluded disposable data only for `C`.

Freeze time: before first scientific block.

Classification: `DERIVED_FIXED` except `C`, which is `CLOSED_DISPOSABLE_RULE`.

---

## D2 — Practical margin

Recommended author-ratified rule:

`delta = 0.10 * C`

This replaces V1’s `0.05*C`. A 10% cap-scale saving is the recommended practical margin because the bounded design must be able to distinguish useful work reduction from a merely nonzero interaction with low block count.

If `C=8000`, `delta=800`.

Phase-1’s post-hoc 882.87 entered-iteration difference may be cited only as scale context. It is not a Stage-R effect estimate and supplies no precision.

Evidence allowed: ratified margin fraction and selected cap only.

Freeze time: after disposable cap selection, before scientific block 1.

Classification: `AUTHOR_RATIFICATION_REQUIRED` for the `0.10` fraction; `CLOSED_DISPOSABLE_RULE` for the numeric `delta` once `C` is chosen.

---

## D3 — Interval procedure

Recommended interval: two-sided 90% inverted sign-flip confidence set for the block-level location parameter under a symmetric block-error model.

Assumption stated explicitly: blocks are independent, and `D_j = theta + e_j`, where the joint distribution of block errors is exchangeable under sign flips around `theta`. This is not distribution-free inference for an arbitrary population mean. No low-`N` distribution-free mean interval over bounded `D_j ∈ [-C,C]` is thin enough for this route; using this method is a ratified modelling assumption.

Algorithm:

1. Inferential input is only the vector `(D_1,...,D_N)`.
2. Candidate parameter domain is bounded: `theta ∈ [-C,C]`.
3. For candidate `m`, define centered values `Z_j(m)=D_j-m`.
4. Enumerate all `2^N` sign vectors exactly. `N_max` is capped at 24, so exact enumeration remains the frozen law.
5. Test statistic is absolute mean: `T_obs(m)=|mean_j Z_j(m)|`.
6. Randomization distribution is `T_b(m)=|mean_j b_j Z_j(m)|` for all sign vectors `b`.
7. Two-sided p-value: `p(m)=#{b: T_b(m) >= T_obs(m)} / 2^N`.
8. The 90% confidence set is `{m ∈ [-C,C]: p(m) > 0.10}` with boundary inclusion fixed by this strict rule.
9. Report interval endpoints as `L=inf accepted set`, `U=sup accepted set`.

Endpoint computation without grid: enumerate sign vectors, form all equality breakpoints solving
`(mean_j b_j(D_j-m))^2 = (mean_j(D_j-m))^2`, add `-C` and `C`, sort breakpoints, evaluate `p(m)` on each open interval and boundary, then take exact infimum/supremum of accepted regions. If the accepted set is disconnected, terminal decisions still use `L` and `U`.

Degenerate behavior:

- If all `D_j=d`, then for `m=d`, `p=1`.
- For any `m≠d`, the smallest attainable two-sided p-value is `2/2^N`.
- Therefore if `2/2^N <= 0.10`, the confidence set collapses to `{d}`.
- If `2/2^N > 0.10`, the accepted set is the whole bounded domain `[-C,C]`.
- All-zero samples are the special case `d=0`, not a different rule.

Attainable p-value resolution: minimum nonzero two-sided p-value is `2/2^N`.

Evidence allowed: scientific block `D_j` values only at final analysis.

Freeze time: before scientific block 1.

Classification: `AUTHOR_RATIFICATION_REQUIRED` for 90% and the symmetry model; otherwise `DERIVED_FIXED`.

---

## D4 — Scientific block count

Recommended closed rule uses one fixed disposable sizing/control set of 12 complete twin blocks. All disposable blocks, items and seeds are permanently excluded from science.

Candidate cap set, ratified before disposable execution:

`C_candidates = {4000, 8000, 12000, 16000}`

For each candidate `C`, derive `D^disp_j(C)`, `delta(C)=0.10*C`, cap-hit summaries and timing from the same excluded max-cap traces.

Dispersion rule for each candidate:

- require 12 valid disposable contrasts;
- compute sample standard deviation `s(C)`;
- compute one-sided 80% normal-model upper scale:

`s_upper(C) = s(C) * sqrt(11 / chi2_0.20,df=11)`

- planning scale:

`s_plan(C) = max(1.5*s_upper(C), 1.5*delta(C))`

If fewer than 12 disposable contrasts are valid, or accounting prevents deriving all candidate caps, terminal is `R_DISPOSABLE_SIZING_INADEQUATE`.

Sizing rule:

`N_raw(C)=ceil(((z_0.95 + z_0.80) * s_plan(C) / delta(C))^2)`

with `z_0.95=1.644854`, `z_0.80=0.841621`.

Rounding and balance:

`N(C)=4 * ceil(max(N_raw(C), 8) / 4)`

Candidate passes sizing iff `N(C) <= 24`.

Candidate selection: choose the largest candidate cap satisfying sizing, censoring prechecks and compute envelope. If none pass, terminal is `R_RESOURCE_INFEASIBLE_FOR_REGISTERED_MARGIN`.

No Stage-R outcome may alter `N`.

Evidence allowed: fixed disposable set only.

Freeze time: after disposable sizing, before scientific block 1.

Classification: `AUTHOR_RATIFICATION_REQUIRED` for 80% power, true-effect planning point `2*delta`, `N_min=8`, `N_max=24`; `CLOSED_DISPOSABLE_RULE` for final `N`.

---

## D5 — Cap and censoring

The primary estimand is capped work. Uncapped work is not observed beyond `C` and is only a companion/sensitivity target.

Theorem-level cap indicator:

`I_{r←q,g}=1` iff branch `r←q` reaches cap `C` on theorem `g`; otherwise `0`.

For block `j`, stratum `s`:

`H_{j,s}=mean_g[(I_A←B,g - I_A←A,g + I_B←A,g - I_B←B,g)/2]`

Block censoring contrast:

`H_j=(H_{j,S1}+H_{j,S2}+H_{j,S3}+H_{j,S4})/4`

Symmetric guard:

- If `abs(mean_j H_j) > 0.05`, no directional scientific terminal is allowed; report `R_INFORMATIVE_BOUNDARY_CENSORING`.
- If any branch has cap-hit rate > 0.80 in more than 25% of planned blocks, terminal is `R_INVALID_CENSORING_DEGENERATE`.
- If total cap-hit rate across all branches exceeds 0.60, terminal is `R_INFORMATIVE_BOUNDARY_CAP_DOMINATED`.

Rationale: more cap hits in mismatched branches can attenuate a true positive by compressing high latent work; more cap hits in matched branches can distort the other way. Because overshoot is unobserved, direction is not inferred from cap-hit sign. The guard is symmetric.

Evidence allowed: disposable cap selection and scientific cap indicators only.

Freeze time: before scientific block 1.

Classification: `AUTHOR_RATIFICATION_REQUIRED` for thresholds; `CLOSED_DISPOSABLE_RULE` for final `C`.

---

## D6 — Frame and repeated measurements

Stage R uses one sealed theorem frame shared by all scientific blocks:

- one sealed reservoir;
- one fixed held-out panel;
- accepted structural bands `S1–S4`;
- fixed reservoir/held-out public projections;
- fixed reservoir-local theorem and rule-skeleton disjointness.

Recommended minimum frame:

- `S1–S4` exactly as accepted Stage-B bands;
- held-out panel: 8 theorems per band, 32 total;
- selected task batch per branch update: 4 tasks per band, 16 total;
- reservoir: at least 4 selectable tasks per branch per band after exclusions, i.e. minimum 16 per band and 64 total; larger reservoir allowed only if fixed before science.

Repeated use of the held-out panel across blocks means inference is conditional on this one sealed frame. It does not estimate frame-level or theorem-population generalization. Theorems are repeated measurements.

Evidence allowed: excluded generator/compile yield only for whether the minimum frame can be filled in S1–S4 without excluded identities or skeleton collisions.

Freeze time: frame sealed before scientific block 1.

Classification: `AUTHOR_RATIFICATION_REQUIRED` for 32 held-out, 16 batch, 64 minimum reservoir; `DERIVED_FIXED` for one sealed frame and S1–S4.

---

## D7 — Selector qualification

All qualification uses disposable split-disjoint data only. Scientific reservoir and held-out items are never used.

Independent qualification unit: reservoir item identity, clustered by reservoir-local rule skeleton for interval resampling.

Minimum qualification set:

- at least 60 disposable items per band, 240 total;
- at least 20 positive and 20 negative registered labels per band for AUC gates;
- at least 30 rule-skeleton clusters total.

If these minima cannot be met, terminal is `R_SELECTOR_QUALIFICATION_INADEQUATE`, not a scientific result.

Rules:

1. Stable elaboration: exact public `d.elaborate(g)` bytes are identical across two clean replays for every qualification item. Failure: `R_IMPLEMENTATION_INVALID`.
2. Identical-state equality: identical serialized state plus identical reservoir produces identical raw scores, normalized scores and selected batches. Failure: `R_IMPLEMENTATION_INVALID`.
3. Sign: equal-prior posterior log-odds predicts the registered hard/useful label in the correct direction with point AUC ≥ 0.55 and lower 90% stratified cluster-bootstrap CI > 0.50. Failure: `R_SELECTOR_ROUTE_CLOSED`.
4. Raw signal nondegeneracy: before rank/quantile normalization, every band/state has finite raw scores, raw IQR ≥ 0.10 natural-log units, and no more than 5% tied raw scores. Failure from NaN/inf or serialization inconsistency: `R_IMPLEMENTATION_INVALID`; failure from flat model signal: `R_SELECTOR_ROUTE_CLOSED`.
5. Normalization implementation parity: after rank/quantile normalization, each band has the sealed deterministic target rank distribution and identical output for identical input. This is an implementation equality check, not a signal-strength gate.
6. Acquired-state divergence: in 8 disposable acquired-state twin probes, selected-batch Jaccard overlap must be ≤ 0.70 in at least 6 probes. Cold same-state overlap must be exactly 1.00 in 8/8. Failure of cold identity: `R_IMPLEMENTATION_INVALID`; failure of acquired divergence with cold identity passing: `CELL_CANNOT_HOST_ESTIMAND_FOR_THIS_LEARNER_CLASS`.
7. Incremental value beyond statement-only surface features: using out-of-fold disposable predictions, selector score must improve AUC over the statement-only regressor by point `ΔAUC ≥ 0.03`, with lower 90% paired stratified cluster-bootstrap CI > 0. Failure: `R_SELECTOR_ROUTE_CLOSED`.
8. Leakage: selector input is public projection only. Any plan, witness, root, source branch, held-out identity or sealed metadata leakage: `R_IMPLEMENTATION_INVALID`.
9. CI failure: if a required bootstrap CI cannot be computed because class balance, cluster count or finite-score requirements fail, use the relevant inadequacy or selector-closed terminal above; do not waive the gate.

Evidence allowed: disposable qualification data only.

Freeze time: before final frame sealing.

Classification: thresholds and minima are `AUTHOR_RATIFICATION_REQUIRED`; public-projection-only and identical-state equality are `DERIVED_FIXED`.

---

## D8 — Injected-coupling positive control

Use the same fixed 12 disposable complete blocks from D4, with synthetic injection applied only in the analysis fixture.

Injected magnitude:

`D^inj_j = D^disp_j + 2*delta`

Recovery criterion:

- run the full frozen block aggregation, censoring guard and sign-flip interval pipeline;
- pass iff the 90% interval lower endpoint for injected `D` is > `delta`;
- point estimate must lie in `[1.25*delta, 2.75*delta]`.

Exact feasibility proof: with 12 blocks, the smallest attainable two-sided sign-flip p-value is:

`2 / 2^12 = 0.00048828125`

This is below `alpha=0.10`. In the favourable constant case `D^inj_j=2*delta` for all 12 blocks, the inverted sign-flip confidence set collapses to `{2*delta}`, so the lower endpoint is `2*delta > delta`. Therefore the positive-control gate is attainable under the frozen interval law. V1’s 4-block gate was impossible because `2/2^4=0.125 > 0.10`.

Failure: `R_POSITIVE_CONTROL_FAILURE`. No scientific run may start, and no bounded negative is interpretable.

Evidence allowed: disposable set only.

Freeze time: before scientific block 1.

Classification: `DERIVED_FIXED` for needing at least 5 blocks under alpha 0.10; `AUTHOR_RATIFICATION_REQUIRED` for using 12 and `2*delta`.

---

## D9 — Retries, attrition and missing blocks

Whole-block retry triggers are control-based and outcome-blind:

- projection/replay mismatch;
- deterministic replay failure;
- branch isolation/key collision;
- environment interruption before all four branches complete;
- manifest/hash mismatch;
- accounting conservation failure.

A branch is never replaced alone.

Planned scientific `N` is divisible by 4. Branch order is balanced over complete four-block cycles.

Retry rule:

- each planned block has one predeclared retry seed;
- retry preserves the same Latin-square cycle/position assignment;
- original failed block remains in attrition ledger;
- no replacement seed beyond the single paired retry.

Attrition ceiling:

- if more than 10% of planned blocks, or more than 2 blocks total, fail after retry, terminal is `R_INVALID_ATTRITION`;
- if any unrepaired missingness breaks a complete four-block order cycle, terminal is `R_INVALID_ORDER_BALANCE` unless worst-case imputation is applied to the full planned cycle.

Missing-`D_j` sensitivity:

- primary vector has length equal to planned `N`;
- valid blocks use observed `D_j`;
- missing blocks are imputed as `-C` for testing `R_POSITIVE`;
- missing blocks are imputed as `+C` for testing `R_BOUNDED_NEGATIVE`;
- directional terminal requires success under its adverse imputation;
- otherwise report `R_INFORMATIVE_BOUNDARY_MISSINGNESS`.

Evidence allowed: control logs only, not branch outcomes.

Freeze time: before scientific block 1.

Classification: attrition thresholds are `AUTHOR_RATIFICATION_REQUIRED`; whole-block-only retry is `DERIVED_FIXED`.

---

## D10 — Randomization and order

Use counter-keyed deterministic randomization with independent namespaces for:

- block;
- twin initialization;
- branch;
- reservoir draw;
- selector Gumbel;
- evaluation theorem order;
- retry.

`N` must be divisible by four. Branch execution order uses repeated sealed Latin-square cycles over the four branch labels. Evaluation order is counter-keyed and balanced within held-out theorem panel.

Sealed before execution:

- key commitments, not actual keys;
- seed commitments;
- block schedule;
- branch/evaluation order schedule;
- public projections;
- theorem identities;
- rule-skeleton identities;
- reservoir/held-out membership;
- environment and analysis hashes.

Independent unit for every inferential calculation: complete twin block.

Freeze time: before scientific block 1.

Classification: `DERIVED_FIXED`.

---

## D11 — Compute envelope chronology

Author first ratifies total available compute: CPU model class or allowed machine class, thread count, process count, maximum wall-time, storage ceiling and whether CUDA is forbidden or only validated. CUDA may never choose the learner.

Disposable set is run once at `C_max=max(C_candidates)` and logs enough to reconstruct every candidate cap:

- entered iterations by theorem/branch;
- cap-hit indicators for every candidate cap;
- timestamps or iteration-time records sufficient to compute candidate-cap wall time;
- LM-query counts;
- update time;
- realized example volume;
- retry/control failures;
- RAM and output size.

For each candidate cap, compute `delta`, censoring, `s_plan`, rounded `N`, expected wall-time and retry reserve. Candidate resource requirement:

`RequiredWall(C)=1.2 * N(C) * T95(C)`

where `T95(C)` is `1.5 * max observed disposable complete-block wall time at cap C`.

Select the largest candidate satisfying:

- sizing `N(C) <= 24`;
- `RequiredWall(C)` within ratified envelope;
- storage/output within envelope;
- no censoring precheck terminal.

If none pass: `R_RESOURCE_INFEASIBLE_FOR_REGISTERED_MARGIN`.

Freeze CPU/thread/process/device policy, wall-time, draw/search/update limits, batch size, held-out size, output limits, `C`, `delta` and `N` before scientific block 1.

Classification: compute ceiling is `AUTHOR_RATIFICATION_REQUIRED`; selected values are `CLOSED_DISPOSABLE_RULE`.

---

## D12 — Terminal precedence

1. `R_IMPLEMENTATION_INVALID`: leakage, projection failure, replay failure, manifest/hash mismatch, accounting failure, non-determinism.
2. `R_FRAME_INFEASIBLE`: one sealed S1–S4 frame cannot be filled with reservoir-local theorem/skeleton disjointness.
3. `R_SELECTOR_QUALIFICATION_INADEQUATE`: disposable qualification minima cannot be met.
4. `CELL_CANNOT_HOST_ESTIMAND_FOR_THIS_LEARNER_CLASS`: acquired-state divergence fails while cold identity passes.
5. `R_SELECTOR_ROUTE_CLOSED`: sign, raw signal, surface-incremental value or selector qualification fails.
6. `R_DISPOSABLE_SIZING_INADEQUATE`: fixed disposable sizing/control set fails adequacy.
7. `R_POSITIVE_CONTROL_FAILURE`: injected coupling not recovered.
8. `R_RESOURCE_INFEASIBLE_FOR_REGISTERED_MARGIN`: no cap/N combination fits ratified envelope.
9. `R_INVALID_CENSORING_OR_ATTRITION`: severe censoring, attrition or order-balance invalidity.
10. `R_POSITIVE`: all controls valid; interval lower endpoint > `delta`; censoring/missingness guards pass.
11. `R_BOUNDED_NEGATIVE`: all controls valid; interval upper endpoint < `delta`; censoring/missingness guards pass.
12. `R_INFORMATIVE_BOUNDARY`: controls valid but neither directional terminal is reached, or non-invalid censoring/missingness guard blocks direction.

Only 10–12 are scientific terminals.

Classification: `DERIVED_FIXED`.

---

## D13 — Freeze record

Final preregistration seals:

- recovered Stage-B hashes and durable locations;
- exclusion ledger: six frozen L2 rows plus every disposable qualification, replay, sizing, injection and calibration item;
- L3 public projection rules and hashes;
- L4 compile/replay acceptance record and hashes;
- one sealed frame ID;
- S1–S4 band definitions;
- reservoir theorem identities, public projection hashes and rule-skeleton identities;
- held-out theorem identities, public projection hashes and rule-skeleton identities;
- learner/config/checkpoint/manifest fingerprint;
- exact ASCII encoder;
- selector formula, raw-score gates, normalization rule and qualification outputs;
- statement-only regressor definition and qualification outputs;
- margin fraction, `C`, numeric `delta`;
- confidence level, sign-flip interval law, endpoint-computation rule and bounded domain;
- disposable sizing/control set identity, `s_plan`, `N_raw`, rounded `N`;
- injected-coupling magnitude and recovery result;
- censoring, retry, attrition, missingness and order-balance rules;
- randomization namespaces, key commitments, seed commitments, Latin-square schedule;
- compute envelope and selected resource limits;
- analysis script/hash;
- terminal precedence;
- statement that Stage H is demoted and not registered.

Freeze time: before scientific block 1.

Classification: fields are `DERIVED_FIXED`; values follow their specific class.

---

## D14 — Feasibility and author choices

Compact ratification table:

| Item | Recommended value | Consequence if rejected |
|---|---:|---|
| Margin fraction | `delta = 0.10*C` | Author must choose another fraction before disposable sizing or close route |
| Confidence level | two-sided 90% | Different level changes positive-control resolution and N rule; must be ratified now |
| Interval model | sign-flip symmetric block-location model | If not accepted, no low-N distribution-free replacement is feasible here; close or redesign under new contract |
| Power target | 80% at true effect `2*delta` | Different target changes N/resource rule; ratify now |
| `N_min`, `N_max` | `8`, `24`, rounded to multiples of 4 | If `N_max` raised, compute envelope must be ratified before disposable sizing |
| Candidate cap set | `{4000,8000,12000,16000}` | Alternate set must be fixed before disposable max-cap run |
| Held-out panel | 32 theorems: 8 per S1–S4 | Smaller panel weakens within-block stability; larger panel affects compute |
| Batch size | 16 tasks: 4 per S1–S4 | Different batch size changes treatment dose |
| Reservoir minimum | 64 tasks: 16 per S1–S4 | Smaller reservoir weakens selection; larger reservoir affects compute |
| Selector AUC gates | AUC ≥0.55, lower 90% CI >0.50; ΔAUC ≥0.03, lower 90% CI >0 | Different thresholds alter selector-route closure |
| Divergence gate | Jaccard ≤0.70 in ≥6/8 acquired probes; cold 8/8 identical | Different threshold changes hostability terminal |
| Censoring thresholds | `abs(mean H)>0.05`; branch >0.80 in >25%; total >0.60 | Different thresholds change directional terminal eligibility |
| Attrition threshold | >10% or >2 failed blocks invalid | Different threshold changes missingness sensitivity |
| Total compute ceiling | author supplied | Without it, cap/N cannot be frozen |

Classification summary:

| Decision | Classification |
|---|---|
| reciprocal `D_j`, sign, complete-twin-block unit | `DERIVED_FIXED` |
| primary raw capped entered-iteration endpoint | `DERIVED_FIXED` |
| S1–S4 as strata | `DERIVED_FIXED` |
| one sealed frame, no frame-level generalization | `DERIVED_FIXED` |
| theorem rows as repeated measurements | `DERIVED_FIXED` |
| exact sign-flip enumeration once ratified | `DERIVED_FIXED` |
| final `C`, numeric `delta`, `N`, resource limits | `CLOSED_DISPOSABLE_RULE` |
| margin fraction, confidence, power, N bounds, cap candidates, frame counts, selector/censoring/attrition thresholds, compute ceiling | `AUTHOR_RATIFICATION_REQUIRED` |

Recommended author choice: ratify the table as written. If the disposable rule selects no feasible candidate cap or requires `N>24`, Stage R closes as resource-infeasible rather than expanding.

---

## Required proofs and checks

### Reciprocal cancellation

For uncensored additive work:

`X_rq = mu + rho_r + beta_q + gamma_rq + error`

Then:

`X_A←B - X_A←A = beta_B - beta_A + gamma_AB - gamma_AA + error`

`X_B←A - X_B←B = beta_A - beta_B + gamma_BA - gamma_BB + error`

So:

`D = [(gamma_AB - gamma_AA) + (gamma_BA - gamma_BB)]/2 + error`

Recipient competence cancels within recipient. Additive batch/source quality cancels across the reciprocal pair. A positive value means mismatched source has higher capped work.

Capping can break latent-work cancellation because `min(W,C)` is nonlinear and overshoot is unobserved. The registered estimand is therefore explicitly capped work; censoring guards prevent over-interpretation, not recovery of uncapped work.

### Interval assumptions and resolution

The interval targets the symmetric block-location parameter `theta`, not a fully distribution-free arbitrary mean. Minimum two-sided p-value is `2/2^N`. At `N=24`, resolution is `1.192e-7`; at the positive-control `N=12`, resolution is `0.000488`.

### Positive-control feasibility

At 12 injected blocks with all injected contrasts equal to `2*delta`, any `m≠2*delta` has p-value `2/2^12=0.000488 <=0.10`, while `m=2*delta` has p-value 1. The confidence set is `{2*delta}` and the lower endpoint exceeds `delta`. The gate can pass.

### Blocks, not theorem rows

The interval and sizing rules consume only block contrasts. Theorems are averaged inside band and block. More theorems reduce within-block noise but do not increase independent `N`.

### Scientific terminals are reachable

With `delta=800`:

- `R_POSITIVE`: CI `[900,1400]`;
- `R_BOUNDED_NEGATIVE`: CI `[-100,700]`;
- `R_INFORMATIVE_BOUNDARY`: CI `[200,1000]`.

All require valid controls and censoring/missingness guards.

### Null is not bounded negative

A null or non-significant result such as CI `[-300,1200]` is `R_INFORMATIVE_BOUNDARY`, not `R_BOUNDED_NEGATIVE`. Bounded negative requires upper endpoint `< delta`.

### Scientific versus feasibility terminals

`R_POSITIVE`, `R_BOUNDED_NEGATIVE` and `R_INFORMATIVE_BOUNDARY` are scientific. Projection/replay failure, selector non-hostability, positive-control failure, resource infeasibility, censoring invalidity and attrition invalidity are instrument/feasibility terminals and make no Stage-R causal claim.

ROUTE_REOPENED=NO
STAGE_H_DEMOTED=YES
INDEPENDENT_UNIT=COMPLETE_TWIN_BLOCK
GENERAL_REVIEWS_REMAINING=0
STATISTICAL_REPAIR_PASSES_REMAINING=0
SCIENTIFIC_EXECUTION_AUTHORIZED=NO
STAGE_R_AUTHOR_DECISIONS_READY=YES
