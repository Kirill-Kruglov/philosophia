# Stage-R author ratification record V1

Status: `RATIFIED_FOR_CONTRACT_V2_DRAFTING_ONLY`

Input proposal:
`STAGE_R_AUTHOR_DECISION_PROPOSAL_V2.md`, SHA-256
`b1262a7a1e20b3e0773702cf8cbfb50a9408832ee9a815002f61897cee8d7fe8`.

This is the final bounded verification of statistical decision support. It is
not a third statistical-design pass and does not reopen the route.

## Closed findings

V2 closes R1–R7 and R9 in principle:

- the positive-control sample has attainable sign-flip resolution;
- the symmetric-location assumption is explicit;
- disposable dispersion uses 12 complete excluded blocks;
- cap selection has a declared chronology;
- the cap-hit contrast is theorem-level and symmetric;
- scientific `N` is rounded to complete four-block Latin-square cycles;
- material numerical choices are identified as author choices;
- one S1–S4 frame is shared by every block and inference is frame-conditional.

R8 is structurally closed but its bootstrap implementation still needs the
mechanical specification below. No new scientific choice is required.

## Mandatory bounded corrections carried into the contract

### B1 — injected-coupling control uses the known increment

V2 D8 defines `D_inj,j = D_disp,j + 2*delta` but tests the total injected value
against a window centred on `2*delta`. This is baseline-confounded. Two bounded
counterexamples are sufficient:

- if `D_disp,j=-delta`, a correct `+2*delta` injection yields `D_inj,j=delta`
  and cannot put its lower interval endpoint above `delta`;
- if `D_disp,j=+delta`, it yields `D_inj,j=3*delta`, outside V2's
  `[1.25*delta,2.75*delta]` point-estimate window.

The contract must instead form paired complete-block increments
`Q_j = D_inj,j - D_base,j`. The positive control passes only if the frozen
90% interval for the symmetric location of `Q` has lower endpoint above
`delta`, its point estimate lies in `[1.75*delta,2.25*delta]`, and all accounting
and deterministic-replay controls pass. The same 12 block identities and
counter-keyed treatment variates are used in base and injected runs. This tests
recovery of the known `+2*delta` coupling rather than an unknown disposable
baseline. Failure remains `R_POSITIVE_CONTROL_FAILURE`.

The exact p-value attainability proof remains valid: for constant
`Q_j=2*delta`, `2/2^12 < 0.10` and the confidence set is `{2*delta}`.

### B2 — exact sign-flip inversion must be an event sweep

V2 D3's literal instruction to evaluate every sign vector on every interval
between up to `2 * 2^N` breakpoints would be quadratic in `2^N`. The statistical
law is retained, but the implementation contract must specify one sort-and-
sweep pass over equality events, updating the exceedance count at each event,
with exact rational/integer comparisons where possible. It must never perform a
Cartesian evaluation of all sign vectors by all intervals.

Before disposable data exist, the analysis code gate must compare the sweep to
literal brute-force evaluation for every integer vector of lengths `1..8` over
the bounded alphabet `{-2,-1,0,1,2}` and for boundary/tie cases. It must also
benchmark the ratified `N_max`; inability to complete inside the analysis
resource sub-envelope returns `R_ANALYSIS_INFEASIBLE`, not permission to change
the interval after data. This is an engineering totality condition, not a new
statistical review.

### B3 — selector bootstrap is mechanically frozen

For V2 D7 gates, use exactly 100,000 counter-keyed resamples of whole
rule-skeleton clusters, stratified by S1–S4. A resampled cluster carries all its
items. Use the percentile 90% interval; the incremental-AUC comparison uses the
same resample indices for selector and statement-only predictions. Folds are
assigned by rule-skeleton identity before fitting and are reused by both
predictors. Missing classes, fewer than the ratified cluster/item minima, or a
non-finite AUC returns `R_SELECTOR_QUALIFICATION_INADEQUATE`; it never triggers a
different resampling rule.

### B4 — lower caps are derived only from replayable evaluation prefixes

V2's single max-cap disposable run may derive a lower-cap candidate only for a
held-out evaluation search whose complete state, action ordering and trace
prefix are identical up to that lower cap. Training/acquisition searches,
examples and updates may not be counterfactually truncated from a max-cap run.
If `C` affects any upstream branch state, every candidate cap requires its own
counter-keyed disposable branch execution. Failure of the prefix identity check
returns `R_DISPOSABLE_SIZING_INADEQUATE`.

### B5 — planning assumptions join author ratification

The V2 compact table omitted the normal-model chi-square scale bound, 12-block
disposable count and `1.5` dispersion inflation. These are not algebraically
derived. They are included in the author bundle below.

## Author bundle recommended for ratification

Ratification accepts the following as one indivisible prospective design bundle:

| Item | Recommended value |
|---|---:|
| practical margin | `delta = 0.10*C` |
| confidence/model | two-sided 90%; symmetric block-location sign-flip law |
| disposable sizing/control set | 12 complete, permanently excluded twin blocks |
| planning scale | V2 chi-square 80% upper scale; `1.5` inflation |
| power planning | 80% at true location `2*delta` |
| scientific blocks | `N_min=8`, `N_max=24`, round upward to multiple of four |
| cap candidates | `{4000,8000,12000,16000}` |
| sealed held-out panel | 32 theorems, 8 per S1–S4 |
| selected treatment batch | 16 tasks, 4 per S1–S4 |
| sealed reservoir minimum | 64 tasks, 16 per S1–S4 |
| selector qualification set | at least 240 items and 30 skeleton clusters, with V2 class minima |
| selector gates | V2 AUC, incremental-AUC, raw-signal and divergence thresholds |
| censoring gates | V2 symmetric `H`, branch and total cap-hit thresholds |
| attrition | V2 whole-block retry, `>10%` or `>2` failed blocks invalid |
| positive control | B1 paired `Q_j` rule at injected `+2*delta` |
| bootstrap | B3 fixed clustered procedure |
| cap derivation | B4 evaluation-prefix rule |

The final author-supplied compute envelope must additionally name:

1. allowed machine/CPU class;
2. process and thread count;
3. device policy;
4. total wall-time ceiling covering qualification, 12 disposable blocks,
   positive control and at most 24 scientific blocks plus the frozen reserve;
5. RAM and durable-storage ceilings;
6. analysis sub-envelope for exact sign-flip inversion.

## Ratification alternatives

There are only two valid next states:

1. Ratify the bundle and supply the compute envelope. This authorizes drafting
   the standalone Stage-R contract V2, but no implementation or execution.
2. Reject any value. State its replacement now, before contract drafting, or
   close the MINIMO Stage-R route. There is no third statistical-agent pass.

Suggested ratification statement:

```text
I_RATIFY_STAGE_R_AUTHOR_BUNDLE_V1_WITH_B1_TO_B5
COMPUTE_MACHINE_CLASS=<value>
COMPUTE_PROCESSES=<integer>
COMPUTE_THREADS_PER_PROCESS=<integer>
COMPUTE_DEVICE_POLICY=<value>
COMPUTE_TOTAL_WALL_HOURS=<integer>
COMPUTE_RAM_GIB=<integer>
COMPUTE_DURABLE_STORAGE_GIB=<integer>
COMPUTE_ANALYSIS_WALL_HOURS=<integer>
```

## Author ratification — 2026-08-15

The author supplied the following literal statement:

```text
I_RATIFY_STAGE_R_AUTHOR_BUNDLE_V1_WITH_B1_TO_B5
COMPUTE_MACHINE_CLASS=AMD_RYZEN_AI_MAX_PLUS_395_PRIMARY_WORKSTATION
COMPUTE_PROCESSES=1
COMPUTE_THREADS_PER_PROCESS=1
COMPUTE_DEVICE_POLICY=CPU_ONLY
COMPUTE_TOTAL_WALL_HOURS=168
COMPUTE_RAM_GIB=96
COMPUTE_DURABLE_STORAGE_GIB=100
COMPUTE_ANALYSIS_WALL_HOURS=8
```

This ratifies the indivisible bundle, B1–B5 and the administrative maximum
compute envelope. It authorizes only assembly and bounded confirmation of the
standalone Stage-R contract V2. It does not itself authorize implementation,
disposable execution or scientific execution.

This record authorizes no code, data generation, key/root minting, selector
execution, learner training or scientific run.
