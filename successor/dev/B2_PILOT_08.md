# B2_PILOT_08

NON-CITABLE Stage-1 pilot (design-validation only). NOT the 6-block call.
Implements `B2_PATH_VS_DESTINATION_DESIGN_V2.md` Stage 1. No src/ edits.
No confirmatory datum.

## Locked constants

- N_max (DIAG_04 curated distinct labeled pairs) = **2000**
- K = floor(N_max/8) = **250** (not swept)
- H_DEST (oracle-stage horizon) = 500
- M_PATH (path updates) = 600
- PATH_BATCH=32, M_ROADS=4, VICReg (inv=25.0, var=25.0, cov=1.0)
- Path d-support = [-80,80] independent of n=66; empty word (d=0,p=0) excluded from batches.
- Pilot seeds = [0, 1]
- Total wall = 40.5 min

## Path firewall

Path sampling/loss assert via `_assert_path_clean` that kwargs never include modulus/n/residue/fold/oracle/panel/truth. Path uses only `unrank_word` + `admissible_paddings` + token-count/`displacement` sameness checks. Oracle_eq and MODULUS appear only in destination K-set construction, panel scoring, and read-only residue probes.

## Panel ⊥ train + displacement-class overlap

- K-set intersect panel word-pairs = 0 (asserted per seed).
- Displacement-class overlap: {'path_abs_d_count': 81, 'panel_diff_count': 72, 'abs_d_intersect_panel_diff': [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68], 'n_overlap': 69, 'note': 'word-level intersect=0 does not establish content independence: path road-pool and panel can still share displacement classes.'}
- word-level intersect=0 does not establish content independence: path road-pool and panel can still share displacement classes.

## Per-arm per-stratum floor table

correct/need with `*` if stratum qualifies. `first_persistent_step` on oracle-stage clock (censored if never); P0/P0-neg have no oracle stage.

| arm | seed | S1 | S2 | S3 | S4 | S5 | first_persistent_step | scoring |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| D | 0 | 56/118 | 3/15 | 5/15 | 8/15 | 8/14 | censored | committee_head |
| P0 | 0 | 2/118 | 8/15 | 8/15 | 8/15 | 5/14 | censored | path_exact_d_linear_readout |
| P0-neg | 0 | 0/118 | 8/15 | 8/15 | 8/15 | 6/14 | censored | path_exact_d_linear_readout |
| P+ | 0 | 2/118 | 1/15 | 1/15 | 3/15 | 0/14 | censored | committee_head_frozen_trunk |
| P_shuf | 0 | 28/118 | 2/15 | 3/15 | 8/15 | 7/14 | censored | committee_head_frozen_trunk |
| D | 1 | 25/118 | 6/15 | 7/15 | 8/15 | 7/14 | censored | committee_head |
| P0 | 1 | 120/118 | 7/15 | 7/15 | 8/15 | 10/14 | censored | path_exact_d_linear_readout |
| P0-neg | 1 | 0/118 | 8/15 | 6/15 | 8/15 | 6/14 | censored | path_exact_d_linear_readout |
| P+ | 1 | 2/118 | 1/15 | 1/15 | 8/15 | 0/14 | censored | committee_head_frozen_trunk |
| P_shuf | 1 | 1/118 | 4/15 | 1/15 | 8/15 | 3/14 | censored | committee_head_frozen_trunk |

## M3 check (positive-path P0 read-only readout)

**M3_PASS = False**

seed0: S1=False S2=False S3=False S4=False S5=False (want S1&S3=True, S2/S4/S5=False) — DESIGN BUG FLAG; seed1: S1=False S2=False S3=False S4=False S5=False (want S1&S3=True, S2/S4/S5=False) — DESIGN BUG FLAG

Pre-registered: S1 & S3 qualify; S2/S4/S5 fail. ANY deviation = design bug flag.

## P0-neg false wall on 20 wrap items

- P0-neg seed0: anti-correct on wrap equals = 10/20
- P0-neg seed1: anti-correct on wrap equals = 10/20
- P0 seed0: anti-correct on wrap equals = 8/20
- P0 seed1: anti-correct on wrap equals = 17/20

## Mechanism probes

| arm | seed | tag | exact_d | length_only | d_within_len | sign(d) | residue(disjoint-d) |
| --- | ---: | --- | ---: | ---: | ---: | ---: | ---: |
| D | 0 | init | 0.398 | 0.526 | nan | 1.000 | 0.009 |
| D | 0 | D | 0.387 | 0.554 | nan | 1.000 | 0.012 |
| P0 | 0 | P0 | 0.238 | 0.145 | nan | 1.000 | 0.007 |
| P+ | 0 | P0pre | 0.213 | 0.130 | nan | 1.000 | 0.014 |
| P+ | 0 | P+ | 0.246 | 0.126 | nan | 1.000 | 0.014 |
| D | 1 | init | 0.455 | 0.667 | nan | 1.000 | 0.013 |
| D | 1 | D | 0.330 | 0.505 | nan | 1.000 | 0.012 |
| P0 | 1 | P0 | 0.269 | 0.100 | nan | 1.000 | 0.015 |
| P+ | 1 | P0pre | 0.284 | 0.107 | nan | 1.000 | 0.008 |
| P+ | 1 | P+ | 0.284 | 0.155 | nan | 1.000 | 0.010 |

### P+-over-P0 residue

- seed 0: P0 residue=0.007, P+ residue=0.014, P+-over-P0 Δ=+0.008
- seed 1: P0 residue=0.015, P+ residue=0.010, P+-over-P0 Δ=-0.005

## Clocks

- Oracle-stage clock: destination CE steps (0..H_DEST), cadence 50.
- Total-compute clock: path wall + dest wall (reported per arm in JSON).
- Device: cuda; runner: gpu_committee_runner (patched forward).

## Verdict (pilot / design-validation)

M3 DEVIATION — treat as design bug; fix before Stage-2 call.

### Design-bug notes (pilot)

1. **M3 never matched on either seed.** Closest near-miss: P0 seed1 S1 had
   correct=120/118, abst=1, brier=0.05 but lies=2 > lie_cap=1 so S1 still
   failed qualify; S3 stayed at 7/15 (need 15). Seed0 P0 collapsed (S1=2/118).
   Positive-path readout did not produce S1&S3-qualify / S2/S4/S5-fail.
2. **P0-neg wrap instrument:** anti-correct on only 10/20 wrap equals (both
   seeds) — false wall incomplete, not saturated.
3. **sign(d)=1.0 even at init:** R/L counts are displacement; last-token
   pre-head already carries sign. Length-only drops under P0 (~0.10-0.15) while
   sign stays 1.0 — not evidence of learned path structure. `d_within_len` was
   nan (stratum too thin after filtering).
4. **VICReg path loss stayed ~15-18** after 600 steps (P_shuf ~22): objective
   may be under-powered/mis-scaled; investigate before Stage 2.
5. Word-level K intersect panel = 0 holds; displacement-class overlap n=69.
