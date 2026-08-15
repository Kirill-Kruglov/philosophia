# STAGE_R_AUTHOR_DECISION_PROPOSAL_V1

Paper-only prospective proposal. No execution authorized.

## Summary recommendation

Use raw capped entered MCTS-loop iterations as the primary block-level scale. Freeze a practical margin as `delta = 0.05 * C`, where `C` is the registered per-theorem entered-iteration cap. Use complete learner-twin blocks only. Size `N` from one complete disposable block by a closed variance rule, with `N_min=8`, `N_max=24`, target power 80% for a true effect of `2*delta`, and 90% two-sided block-level confidence intervals. If the rule requires `N > N_max` or exceeds the signed compute ceiling, the route terminates as `R_RESOURCE_INFEASIBLE`, not as science.

`STAGE_R_AUTHOR_DECISIONS_READY=YES`, conditional on the author accepting the fixed maximum scientific block count `N_max=24` and the resource-infeasibility terminal.

---

## D1 — Primary analysis scale

Recommendation: primary statistic is raw capped entered MCTS-loop iterations.

For theorem `g` in stratum `s`, branch work is:

`X_{r←q,g} = min(entered_mcts_iterations_{r←q,g}, C)`

For each block `j` and stratum `s`:

`D_{j,s} = mean_{g in s}[(X_A←B,g - X_A←A,g + X_B←A,g - X_B←B,g)/2]`

Primary block statistic:

`D_j = sum_s w_s * D_{j,s}`

Recommended stratum weights: equal weights across registered structural strata that are present in every complete block: `w_s = 1/S`.

Units: entered MCTS-loop iterations per theorem. Sign: positive `D_j` means mismatched/donated selection costs more work, so own-state selection helps.

Rationale: the driver fixed capped entered MCTS-loop iterations as the primary assigned-work endpoint. Normalization is not mathematically necessary if one cap `C` applies to all branches and strata.

Evidence allowed: driver decision, Phase-1 counter repair as endpoint-definition context only, disposable compile/search timing only for choosing `C`.

Freeze time: before first scientific block; stratum definitions and weights freeze when reservoir/held-out frame is sealed.

Classification: `FIX_NOW` for raw scale and sign; `FIX_BY_CLOSED_DISPOSABLE_RULE` for `C`.

---

## D2 — Practical margin

Recommendation: `delta = 0.05 * C` raw entered iterations.

If `C=8000`, then `delta=400` entered iterations per theorem. If a different cap is frozen by D5/D11, `delta` follows mechanically.

Rationale: a 5% cap-scale saving is large enough to exclude trivial nonzero effects and small enough that both positive and bounded-negative terminals are reachable in a thin design. The Phase-1 ck1 difference, 882.87 entered iterations on a different post-hoc artifact, may be cited only as context that hundreds of entered iterations are not a meaningless scale; it must not size the expected Stage-R effect or variance.

Evidence allowed: the frozen cap `C`; Phase-1 only for scale intuition, not estimation.

Freeze time: immediately after `C` is frozen and before any scientific block.

Classification: `FIX_BY_CLOSED_DISPOSABLE_RULE`.

---

## D3 — Interval procedure

Recommendation: two-sided 90% confidence interval on the mean of block-level `D_j`.

Algorithm:

1. Compute one `D_j` per complete scientific twin block.
2. Primary interval is the exact sign-flip randomization interval for a one-sample paired-location mean under symmetric block-level errors, constructed by inverting the sign-flip test over candidate means `m`.
3. For each candidate `m`, evaluate all `2^N` sign flips of centered values `(D_j - m)` when `N <= 20`; for `N > 20`, use a fixed sealed Monte Carlo sign-flip schedule of at least 1,000,000 sign vectors generated before outcomes are unsealed.
4. The 90% CI is the set of `m` not rejected at two-sided alpha `0.10`.
5. Ties are retained as exact zeros in the sign-flip distribution.
6. Degenerate variance:
   - if all `D_j` are identical, CI collapses to that value;
   - if all `D_j=0`, CI is `[0,0]`;
   - terminal follows the same delta rule.

Assumptions: independent complete twin blocks; exchangeable symmetric block-level errors after fixed design and randomization; no theorem-level independence assumption.

Rationale: avoids theorem-row pseudoreplication and avoids normal approximation at small `N`.

Evidence allowed: no outcome evidence except scientific block `D_j` values at final analysis.

Freeze time: before first scientific block.

Classification: `FIX_NOW`.

---

## D4 — Scientific block count

Recommendation: closed sizing rule using exactly one complete disposable block set.

Disposable sizing rule:

1. Run one fixed disposable set of `B_disp = 4` complete twin blocks after implementation passes projection/replay and selector qualification. These blocks, their items and seeds are permanently excluded from science.
2. Compute disposable block contrasts `D^disp_j`.
3. Estimate dispersion by robust scale:

`sd0 = 1.4826 * median_j |D^disp_j - median(D^disp)|`

If `sd0=0`, set `sd0 = delta`. Then inflate:

`sd_plan = max(2*sd0, delta)`

4. Size for 80% power at true mean `2*delta` using normal-planning approximation only for sizing:

`N_req = ceil(((z_0.95 + z_0.80) * sd_plan / delta)^2)`

with `z_0.95=1.644854`, `z_0.80=0.841621`.

5. Freeze:

`N = min(max(N_req, 8), 24)`

6. If `N_req > 24`, terminal is `R_RESOURCE_INFEASIBLE_FOR_REGISTERED_MARGIN`, unless the author explicitly signs a larger `N_max` before any scientific run. No Stage-R outcome may alter `N`.

Rationale: the disposable blocks measure operational variance without using scientific outcomes. `N_min=8` prevents a single lucky low-variance disposable set from creating a non-informative tiny experiment. `N_max=24` keeps the route bounded.

Evidence allowed: only the fixed disposable set; no scientific outcomes.

Freeze time: after disposable sizing and before first scientific block.

Classification: `FIX_BY_CLOSED_DISPOSABLE_RULE`; author may override only `N_max`, before implementation.

---

## D5 — Cap and censoring

Recommendation:

`C =` the largest per-theorem entered-MCTS cap that fits the signed compute envelope while allowing `N_max=24` complete blocks, all four branches, all held-out items, and one retry reserve of 20%.

Closed rule: after the complete disposable block set, compute observed per-block wall time at candidate cap. Select the largest candidate cap from the preregistered set `{4000, 8000, 12000, 16000}` satisfying the envelope above. If none satisfy, terminal is `R_RESOURCE_INFEASIBLE`.

Per-branch summaries: cap-hit rate by branch, recipient, source, stratum and block.

Differential-censoring guard:

- Let `h_{r←q,j}` be the held-out cap-hit fraction in block `j`.
- Define matched-minus-mismatched cap differential:

`H_j = mean_g[(h_A←B - h_A←A + h_B←A - h_B←B)/2]`

Rules:

- If `mean(H_j) > +0.05`, censoring favors positive `D`; terminal cannot be `R_POSITIVE`; if interval would otherwise be positive, report `R_INFORMATIVE_BOUNDARY_CENSORING`.
- If any branch has cap-hit rate > 0.80 in more than 25% of blocks, terminal is `R_INVALID_CENSORING_DEGENERATE`.
- If total cap-hit rate is > 0.60 across all branches, terminal is `R_INFORMATIVE_BOUNDARY_CAP_DOMINATED`.

Why: capping is nonlinear. It can compress high-work branches unequally and manufacture or hide an interaction.

Evidence allowed: disposable timing for selecting `C`; scientific cap-hit diagnostics for terminal guard only.

Freeze time: cap before scientific block; censoring rules before scientific block.

Classification: `FIX_BY_CLOSED_DISPOSABLE_RULE`.

---

## D6 — Frame and repeated measurements

Recommendation for minimum valid frame:

- structural strata: `S=4`, defined by sealed theorem-complexity bands available after generator/compile yield;
- held-out theorem count per block: `8` per stratum, `32` total;
- reservoir size per block: at least `4 * batch_size` per stratum after exclusions;
- batch size: `4` selected tasks per stratum, `16` total per branch update;
- within-stratum theorem aggregation: mean over the same held-out theorem identities for all four branches.

Reservoir-local disjointness required:

- no theorem identity overlap;
- no public projection overlap;
- no reservoir/held-out rule-skeleton overlap;
- exclusion import for all L0–L2 fixtures, disposable sizing blocks, selector qualification items, replay/projection tests and injected-coupling fixtures.

Values that may be fixed only after excluded generator/compile yield: exact stratum cutpoints and whether all four strata are feasible. If fewer than four strata can be produced under the timed L4 boundary, terminal is `R_FRAME_INFEASIBLE`, not a redesign into a richer Stage-B programme.

Rationale: 32 held-out items per block stabilizes within-block averaging without pretending theorems are independent. Four strata preserves the driver’s stratum-weight discipline while keeping the route thin.

Evidence allowed: permanently excluded generator/compile yield only; no scientific outcomes.

Freeze time: frame before selector qualification and before first scientific block.

Classification: `FIX_NOW` for counts; `FIX_BY_CLOSED_DISPOSABLE_RULE` for stratum cutpoints.

---

## D7 — Selector qualification

All qualification uses split-disjoint disposable data only.

Rules:

1. Stable elaboration: exact public `d.elaborate(g)` bytes must be byte-identical across two clean replays for every qualification item. Failure: `R_IMPLEMENTATION_INVALID`.
2. Identical-state equality: identical serialized state plus identical reservoir must produce identical scores, rank-normalized scores and selected batches. Failure: `R_IMPLEMENTATION_INVALID`.
3. Sign: equal-prior posterior log-odds must predict the registered hard/useful label in the correct direction with lower 90% CI for AUC > 0.55 on disposable data. Failure: `R_SELECTOR_ROUTE_CLOSED`.
4. Scale parity: within every stratum, normalized selector scores must have median 0 and IQR in `[0.8,1.2]` after rank/quantile normalization. Failure: `R_IMPLEMENTATION_INVALID` if normalization code violates rule; `R_SELECTOR_ROUTE_CLOSED` if raw signal is unusable.
5. Acquired-state divergence: after the registered disposable acquisition/update, twin selected batches must have Jaccard overlap ≤ 0.70 in at least 3 of 4 disposable blocks, while cold same-state overlap must be exactly 1.00. Failure of acquired divergence: `CELL_CANNOT_HOST_ESTIMAND_FOR_THIS_LEARNER_CLASS`.
6. Incremental predictive value beyond statement-only surface features: selector score must improve held-out disposable prediction over the statement-only regressor by at least `ΔAUC >= 0.03`, with lower 90% bootstrap CI > 0. Failure: `R_SELECTOR_ROUTE_CLOSED`.
7. No leakage: selector inputs are public projection only. Any plan, root, witness, source, branch or held-out identity leakage: `R_IMPLEMENTATION_INVALID`.

Evidence allowed: disposable split-disjoint data only.

Freeze time: before scientific reservoir sealing.

Classification: `FIX_NOW`.

---

## D8 — Injected-coupling positive control

Recommendation:

Injected magnitude: add a synthetic deterministic branch interaction equivalent to `+2*delta` on the block-level `D_j` scale, implemented only in the analysis fixture, never in scientific data.

Recovery criterion:

- Run the full frozen analysis pipeline on `B_disp=4` disposable complete blocks with injected interaction.
- Pass iff the 90% interval lower bound for injected `D` is > `delta`.
- Also require recovered point estimate in `[1.25*delta, 2.75*delta]`.

Failure: `R_POSITIVE_CONTROL_FAILURE`; no scientific run may start, and no null/bounded-negative terminal is interpretable.

Rationale: tests the full estimator, block aggregation, interval, censoring and terminal machinery.

Evidence allowed: disposable injected fixture only.

Freeze time: before final scientific `N`, randomization and first block.

Classification: `FIX_NOW`.

---

## D9 — Retries, attrition and missing blocks

Whole-block retry triggers, outcome-blind only:

- projection/replay mismatch;
- branch isolation/key collision;
- deterministic replay failure;
- environment interruption before all four branches complete;
- manifest/hash mismatch;
- accounting conservation failure.

Maximum retries: one retry per planned scientific block, with no replacement seed. The retry uses the predeclared retry seed paired to that block; failed original remains in attrition ledger.

A branch may never be replaced alone.

Attrition ceiling: if more than `10%` of planned blocks or more than `2` blocks total require retry/fail, terminal is `R_INVALID_ATTRITION`.

Missing-`D_j` sensitivity:

- Compute primary interval on complete valid blocks only.
- Then impute every missing block as worst-case `D=-C` for positive claim and `D=+C` for bounded-negative claim.
- `R_POSITIVE` requires lower bound > `delta` under worst-case negative imputation.
- `R_BOUNDED_NEGATIVE` requires upper bound < `delta` under worst-case positive imputation.
- Otherwise `R_INFORMATIVE_BOUNDARY_MISSINGNESS`.

Evidence allowed: control/status logs, not treatment outcomes.

Freeze time: before first scientific block.

Classification: `FIX_NOW`.

---

## D10 — Randomization and order

Recommendation:

- Use counter-keyed deterministic randomness with independent namespaces for block, twin, branch, reservoir sampling, selector Gumbel, evaluation order and retry.
- Seal key commitments and seeds; do not reveal branch outcome labels until analysis lock.
- Balanced branch order: within each block, the four branches are assigned by a sealed Latin-square schedule so each branch appears equally often in each execution position across blocks.
- Balanced evaluation order: held-out theorem order is counter-keyed per branch but balanced so each theorem appears equally often in early/middle/late positions across branches.
- Seal all public projections, theorem IDs, skeleton IDs, reservoir/held-out membership, branch labels, seed commitments, environment hashes and analysis script hash.

Independent unit for every inferential calculation: complete twin block.

Evidence allowed: sealed randomization manifest only.

Freeze time: before first scientific block.

Classification: `FIX_NOW`.

---

## D11 — Compute envelope chronology

Disposable block measures:

- wall time per branch and per complete block;
- CPU model, thread count, process count, RAM peak;
- entered-iteration distributions;
- cap-hit rates;
- LM-query counts;
- update time;
- realized example volume;
- retry-trigger incidence;
- storage/output size.

Freeze rule:

1. After disposable set, choose `C` by D5.
2. Compute per-block time `T95` as max observed disposable complete-block time multiplied by 1.5.
3. Scientific envelope must reserve `N*T95*1.2` wall-time capacity, including retry reserve.
4. Freeze CPU/thread/process counts, device policy, wall-time limit, draw/search/update limits, batch size, held-out size and output-size limits.
5. If the signed envelope cannot support frozen `N` and `C`, terminal is `R_RESOURCE_INFEASIBLE`; do not shrink endpoint, expand budget, or change learner after outcomes.

Evidence allowed: one complete disposable set only.

Freeze time: after disposable sizing, before scientific block 1.

Classification: `FIX_BY_CLOSED_DISPOSABLE_RULE`, except available total compute is `AUTHOR_VALUE_REQUIRED` if not already administratively fixed.

---

## D12 — Terminal precedence

Total precedence order:

1. `R_IMPLEMENTATION_INVALID`: leakage, projection failure, replay failure, manifest/hash mismatch, accounting failure, non-determinism.
2. `R_FRAME_INFEASIBLE`: reservoir-local theorem/skeleton disjointness or minimum frame cannot be achieved.
3. `CELL_CANNOT_HOST_ESTIMAND_FOR_THIS_LEARNER_CLASS`: acquired-state divergence fails while cold identity passes.
4. `R_SELECTOR_ROUTE_CLOSED`: sign, surface-incremental value or selector qualification fails.
5. `R_POSITIVE_CONTROL_FAILURE`: injected coupling not recovered.
6. `R_RESOURCE_INFEASIBLE`: disposable timing/variance requires resources outside sealed ceiling.
7. `R_INVALID_CENSORING_OR_ATTRITION`: censoring degeneracy or attrition ceiling exceeded.
8. `R_POSITIVE`: all controls valid and interval lower bound > `delta`, including missingness guard.
9. `R_BOUNDED_NEGATIVE`: all controls valid and interval upper bound < `delta`, including missingness guard.
10. `R_INFORMATIVE_BOUNDARY`: all controls valid but neither scientific terminal reached, or censoring/missingness guard blocks stronger classification.

Scientific terminals are only 8–10. Items 1–7 are instrument/feasibility terminals.

Classification: `FIX_NOW`.

---

## D13 — Freeze record

Final preregistration must seal:

- recovered Stage-B artifact hashes and durable committed locations;
- exclusion-ledger import, including six frozen L2 rows and all disposable/calibration/qualification/injection items;
- L3 public projection rules and hashes;
- L4 compile/replay acceptance record and hashes;
- reservoir theorem identities, public projection hashes and rule-skeleton identities;
- held-out theorem identities, public projection hashes and rule-skeleton identities;
- stratum definitions, stratum weights and theorem counts;
- learner architecture/config fingerprint, checkpoint/manifest fingerprint and exact ASCII encoder;
- selector formula, features, equal-prior posterior log-odds rule, rank/quantile normalization and qualification outputs;
- `delta`, confidence level, interval algorithm, scientific `N`, `N_min`, `N_max`, power target and sizing record;
- cap `C`, cap-hit summaries and censoring terminal rules;
- primary and companion endpoints;
- injected-coupling magnitude and recovery result;
- retry, attrition and missing-block rules;
- randomization namespaces, seed commitments, branch/evaluation order schedule;
- compute envelope: CPU/thread/process/device policy, wall-time, search/update/draw limits, batch size, held-out size;
- analysis code/script hash;
- terminal precedence table;
- statement that Stage H is not registered and not authorized.

Classification: `FIX_NOW` for fields; values freeze by their specific rules.

---

## D14 — Feasibility and author choices

| Decision | Classification |
|---|---|
| raw capped entered-iteration primary scale | `FIX_NOW` |
| block-level `D_j` with equal stratum weights | `FIX_NOW` |
| `delta = 0.05*C` | `FIX_BY_CLOSED_DISPOSABLE_RULE` |
| 90% sign-flip interval | `FIX_NOW` |
| `N_min=8`, `N_max=24`, 80% target power at `2*delta` | `FIX_NOW` |
| disposable variance-sizing rule | `FIX_NOW` |
| cap from `{4000,8000,12000,16000}` by envelope rule | `FIX_BY_CLOSED_DISPOSABLE_RULE` |
| 4 strata, 32 held-out theorems/block, 16 selected tasks/branch | `FIX_NOW` subject to compile-yield feasibility |
| exact stratum cutpoints | `FIX_BY_CLOSED_DISPOSABLE_RULE` |
| selector pass/fail thresholds | `FIX_NOW` |
| injected `+2*delta` and recovery criterion | `FIX_NOW` |
| retries/attrition/missingness rules | `FIX_NOW` |
| randomization/order/sealing fields | `FIX_NOW` |
| total available compute ceiling | `AUTHOR_VALUE_REQUIRED` if not administratively fixed |
| author acceptance of `N_max=24` as hard ceiling | `AUTHOR_VALUE_REQUIRED` |

Recommended author choice: accept `N_max=24` and the resource-infeasibility terminal. This keeps the route bounded and prevents the experiment from becoming an unbounded witness search.

---

## Required proofs and checks

### Reciprocal cancellation

Assume uncensored additive model:

`X_rq = mu + rho_r + beta_q + gamma_rq + error`

Then:

`X_A←B - X_A←A = beta_B - beta_A + gamma_AB - gamma_AA + error`

`X_B←A - X_B←B = beta_A - beta_B + gamma_BA - gamma_BB + error`

Averaging:

`D = [(gamma_AB - gamma_AA) + (gamma_BA - gamma_BB)]/2 + error`

Recipient competence `rho_r` cancels within recipient. Additive source/batch quality `beta_q` cancels across the reciprocal pair. Positive `D` means mismatched source has higher work.

Cap censoring can break this because `min(W,C)` is nonlinear. If one branch hits the cap more often, differences are compressed asymmetrically. Differential cap-hit guards therefore prevent censoring from manufacturing a positive reading.

### Blocks, not theorem rows

The interval receives only `{D_1, …, D_N}`. Theorem rows are averaged inside stratum and block before inference. Increasing held-out theorems stabilizes `D_j`; it does not increase independent `N`.

### All three scientific terminals are reachable

Example with `delta=400`:

- `R_POSITIVE`: `N=8`, all valid, CI `[450,900]`; lower > 400.
- `R_BOUNDED_NEGATIVE`: `N=8`, all valid, CI `[-100,300]`; upper < 400.
- `R_INFORMATIVE_BOUNDARY`: `N=8`, all valid, CI `[100,650]`; interval spans 400.

### Null cannot become bounded negative

A non-significant result such as CI `[-200,700]` is not negative because upper bound is not below `delta`. It is `R_INFORMATIVE_BOUNDARY`. `R_BOUNDED_NEGATIVE` requires evidence that any practical effect is below the registered margin.

### Scientific versus instrument terminals

`R_POSITIVE`, `R_BOUNDED_NEGATIVE` and `R_INFORMATIVE_BOUNDARY` are scientific only after all controls pass. Projection/replay failure, selector failure, positive-control failure, resource infeasibility, censoring degeneracy and attrition invalidity are instrument/feasibility terminals and say nothing about the Stage-R causal claim.

ROUTE_REOPENED=NO
STAGE_H_DEMOTED=YES
INDEPENDENT_UNIT=COMPLETE_TWIN_BLOCK
SCIENTIFIC_EXECUTION_AUTHORIZED=NO
STAGE_R_AUTHOR_DECISIONS_READY=YES
