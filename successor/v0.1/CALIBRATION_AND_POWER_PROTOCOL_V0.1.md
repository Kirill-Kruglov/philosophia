# Calibration and power protocol v0.1

**Status:** DRAFT FOR EXTERNAL REVIEW — development procedure fixed before outcome-bearing development.

Calibration is allowed to determine engineering scale and sample size only through the rules below. It may not redefine the arms, hypothesis, SESOI, model family, primary estimator, or interpretation.

---

## 1. Separation of development and confirmation

Use disjoint deterministic seed namespaces:

- P0 calibration seeds;
- P2/P3 paired power-pilot seeds;
- confirmatory seeds.

No development seed may appear in confirmation.

The confirmatory seed sequence may be pre-generated up to 128 seeds but only the first mechanically selected `N` are authorized.

---

## 2. Pre-calibration lock requirements

Before P0, hash-commit:

- all v0.1 documents;
- implementation code and tests;
- exact `MODEL_CONFIG_REF` + hash;
- environment lock;
- seed derivation implementation and test vectors;
- calibration script;
- power-N script;
- analysis implementation against synthetic fixtures;
- deterministic-prefix replay report.

If any of these change after P0 begins, v0.1 calibration is void unless a new preregistration version is declared.

---

## 3. Fixed competence definition for all stages

Held-out accuracy >= 0.95 at three consecutive evaluations.

Evaluation steps: `0, 100, 200, ...`.

`T` is the first evaluation step of the earliest fully observed qualifying three-evaluation run.

---

## 4. P0 — single-world scale/headroom calibration

### 4.1 Start scale

Always start at `M=96`, module pool `[131..138]`.

### 4.2 P0 sample

Use exactly 16 development-only fresh-model runs.

For each run:

- choose one modulus deterministically from the pool using the calibration seed;
- fresh model initialization;
- one fixed non-trainable context code for that world;
- train on the locked 70% split;
- no prior history;
- fresh optimizer;
- evaluate every 100 steps;
- calibration hard cap = 20,000 optimizer updates.

### 4.3 P0 acceptance at a scale

A scale is single-world admissible only if:

1. no more than 2 of 16 runs are censored at 20,000; and
2. defining `T20 = min(T, 20000)` (20,000 for a censored run), the median of all 16 `T20` values is between 2,000 and 8,000 optimizer updates inclusive.

Interpretation:

- median < 2,000: transfer floor risk / world too easy;
- median > 8,000 or >2/16 censored: world/learner too hard for this cell.

### 4.4 Authorized scale transition

If `M=96` is too easy, v0.1 permits exactly one escalation:

`M=128`, pool `[176..183]`, rerun P0 from scratch with a disjoint calibration sub-namespace.

If `M=128` is also too easy: terminal `INADMISSIBLE_SUBSTRATE_TOO_EASY`.

If an attempted scale is too hard under 4.3, do not search other hyperparameters or a smaller custom world; terminal `INADMISSIBLE_SUBSTRATE_TOO_HARD` for v0.1.

If M=96 passes, M=128 must not be tried “for comparison”.

---

## 5. P1 — mechanically derive history and probe budgets

Once a scale passes P0, lock it permanently for v0.1.

For each of the 16 P0 runs define `T20 = min(T, 20000)`, using 20,000 for a censored run. Because at most two runs may be censored, the median is not driven by the right boundary. Compute:

### 5.1 History budget

`B_history = ceil_to_100(median(T20))`.

Every history world in every arm receives exactly this many optimizer updates.

### 5.2 Fresh-probe cap

Compute the empirical 90th percentile using the preregistered NumPy `method="linear"` quantile convention on the 16 `T20` values.

`tau = ceil_to_100(min(30000, 3 * Q0.90))`.

`tau` is then frozen for the power pilot and confirmation.

The restricted estimator explicitly handles the cap. Reaching the cap is logged and interpreted as saturation, not as an uncensored event time.

### 5.3 P1 artifact

Write and hash `CALIBRATION_DECISION.json` containing:

- selected M and pool;
- all 16 P0 T/censor values;
- median;
- Q0.90;
- B_history;
- tau;
- code/config/environment hashes.

No human-selected rounding or override is permitted beyond the formulas above.

---

## 6. P2 — paired endpoint/headroom pilot

Use exactly 6 new paired replicate seeds.

For each seed run both arms through all six history worlds using frozen `B_history` and `tau`.

The pilot must at minimum execute C probes at `k=1` and `k=6`. It may also emit the already specified k=2,4 probes, but those cannot affect decisions below.

### 6.1 k=1 integrity

Because arms are identical through H1, all k=1 checkpoint and C-probe hashes/trajectories must match exactly.

Any mismatch: `INVALID_K1_ARM_DIVERGENCE`; stop and repair implementation under a new preregistration version if necessary.

### 6.2 k=1 headroom gate

Use the single unique k=1 C trajectory per paired seed (arms are identical).

Headroom is admissible only if:

- median `T_C,k=1 >= 1000` updates;
- at most 1 of 6 seeds has `T=0`;
- at most 1 of 6 seeds is censored at `tau`.

If M=96 passed P0 but fails because it is too easy at k=1, the only authorized response is the one-time escalation to M=128 followed by a complete restart of P0, P1, and P2 with fresh development seeds.

If M=128 fails the same floor: terminal `INADMISSIBLE_TRANSFER_FLOOR`.

If k=1 is too hard (>1/6 censored), terminal `INADMISSIBLE_TRANSFER_CEILING`; no larger scale or hyperparameter search is authorized.

---

## 7. P3 — variance-only power pricing

For each of the 6 paired pilot seeds compute the exact preregistered paired differential `d_i` using only k=1 and k=6.

The pilot **mean effect is not an input to sample-size selection**.

The power script consumes only:

- the six `d_i` values for their sample variance;
- `delta_SESOI = ln(1.20)`;
- fixed alpha/power constants below.

### 7.1 Conservative variance estimate

Let `m=6`, sample standard deviation `s_d`, `df=m-1`.

Use the one-sided 80% upper confidence bound on the population standard deviation:

`sigma_U = s_d * sqrt(df / chi2_ppf(0.20, df))`.

This intentionally prices uncertainty in a six-seed variance estimate upward.

### 7.2 Target power

Target:

- two-sided alpha = 0.05 for a paired mean difference versus zero;
- power = 0.90 at absolute effect size `delta_SESOI`.

Normal-approximation required N:

`N_raw = ceil(((z_0.975 + z_0.90) * sigma_U / delta_SESOI)^2)`.

Then:

`N = max(20, N_raw)`.

If `N > 128`: terminal `BLOCKED_POWER`; no smaller confirmatory sample is authorized.

If `s_d = 0`, `N=20` by the minimum rule.

### 7.3 No observed-effect powering

The pilot mean, sign, p-value, or curve shape may not reduce/increase N or alter the hypothesis. The power-decision script should omit the mean from its decision output if practical, even though raw pilot logs remain immutable artifacts.

---

## 8. Confirmatory lock after P3

After N is derived and before any confirmatory training:

1. instantiate the first N seeds from the `confirmatory` seed namespace;
2. generate every world allocation and split manifest for those seeds;
3. write final `CONFIRMATORY_CONFIG.json`;
4. hash runner, analysis script, config, seed list, allocation manifests, environment, and preregistration root;
5. run deterministic-prefix verification again;
6. publish/commit the lock root according to project governance;
7. only then start confirmatory execution.

No further calibration is permitted.

---

## 9. Confirmatory runtime scope

Each confirmatory paired seed runs:

- ALIASED full 6-world history;
- SEPARABLE full 6-world history;
- disposable C probes after k=1,2,4,6;
- secondary H1 reacquisition after k=6.

The independent scientific unit remains the paired seed.

---

## 10. Technical failures

A transient machine/process crash may be rerun only from the beginning of the **same seed and same arm** under the same locked config. It may not be replaced with a new seed because its outcome looked inconvenient.

If a seed cannot be completed validly under the locked environment, record it as platform-invalid. If the final valid paired-seed count is below locked N, the confirmatory decision is `INVALID_INCOMPLETE_CONFIRMATION`; do not silently analyze a smaller sample.

Non-finite parameters/loss caused by the locked scientific trajectory are scientific/feasibility observations only if the preregistered runner remains valid; a code/environment violation is platform-invalid. The reason classification must be machine-recorded before aggregate outcome analysis.
