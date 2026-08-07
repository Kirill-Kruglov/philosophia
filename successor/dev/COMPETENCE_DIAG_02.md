# COMPETENCE_DIAG_02

NON-CITABLE engineering competence diagnostic only.
No confirmatory datum. Dev world only. Floor/scoring/panel/config reused verbatim from src/philosophia/level1; no src/ edits.

env: torch=2.7.0+cu128; device=NVIDIA GeForce RTX 4060 Laptop GPU; cuda_available=True.

## Dev world

- family: RANDOM-STATIC
- modulus: 66
- world_slot / pair_slot: 0
- public-root key label: `successor-dev-competence-diag-01` (same as DIAG_01; dummy_key SHA256 material; test_only)
- panel key label: `successor-dev-competence-diag-01` purpose=`panel`
- schedule: `random_static_schedule` length 2000 (sample_without_replacement over flat pool)

## Learner config

- architecture: ContactTransformer d_model=128, heads=4, layers=2, mlp=512, vocab=4, dtype=torch.float32, input_len=277
- committee: 4 members (replicate=1, members 0..3), block=world_slot
- objective: CLASS-BALANCED weighted full-history mean CE (w_i=0.5/freq(class_i); loss=Σ w_i·CE_i / Σ w_i); memory-safe sequential + microbatch=128 on CUDA
- optimizer: AdamW lr=1e-3 betas=(0.9, 0.98) eps=1e-8; weight_decay=0.01 on attention/MLP/head_W, 0.0 on embeddings/LN/biases
- budget B=2000, checkpoint every 50, persistence window=5 checkpoints
- device: NVIDIA GeForce RTX 4060 Laptop GPU; torch=2.7.0+cu128
- config diff vs DIAG_01: ONLY the loss weighting (plain mean CE → class-balanced weighted mean CE)

## Panel ⊥ training disjointness

`partition_cells(public_key)` splits every difference-class cell set into reserved (~30%) and acquisition (remainder). Training pairs are realized only from `partition.acquisition` via `realize_pool_index`. The held-out panel (`DummyPanelBuilder`) draws zone-2 cells exclusively from `partition.reserved` (and constructs zone-3 S4/edge cells outside the acquisition set). Frozen `verify_dummy_panel` rejects any panel item whose cell lies in acquisition. This run: acquisition∩panel_cells empty = True; realized training word-pair ∩ panel word-pair size = 0 (must be 0); panel size = 188 (frozen 188).

Wall-clock: 6111.0 s (1.70 h).

## Persistence against frozen floor

- `first_persistent_step(...)` = `None`
- longest consecutive qualifying checkpoints = 0 (none)
- qualifying checkpoints: none
- persistence requires 5 consecutive cadence hits; cadence grid = 0..2000 step 50.

## Best checkpoint (step 700)

qualifies_overall=False; strata_ok=1/5; total_correct=156; abstentions=0; confident_lies=28; mean_brier=0.344439.

| stratum | correct/expected | abstentions | confident_lies | brier | qualifies |
| --- | ---: | ---: | ---: | ---: | --- |
| S1 | 124/118 (of 124) | 0 | 0 | 0.012474 | True |
| S2 | 8/15 (of 16) | 0 | 6 | 0.401096 | False |
| S3 | 8/15 (of 16) | 0 | 8 | 0.450624 | False |
| S4 | 8/15 (of 16) | 0 | 8 | 0.450692 | False |
| S5 | 8/14 (of 16) | 0 | 6 | 0.407307 | False |

ACCURACY_MINIMUM (frozen): S1≥118, S2≥15, S3≥15, S4≥15, S5≥14.

## Mean p_equal by stratum × truth

Committee mean p_equal on panel items with truth=equal vs truth=unequal. Always-≠ collapse ≈ both columns near 0; recovery needs high eq / low neq.

| step | S1_eq | S1_neq | S2_eq | S2_neq | S3_eq | S3_neq | S4_eq | S4_neq | S5_eq | S5_neq |
| ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 0 | n/a | 0.4817 | 0.4841 | 0.4827 | 0.4846 | 0.4824 | 0.5493 | 0.5509 | 0.5579 | 0.4770 |
| 50 | n/a | 0.0862 | 0.0694 | 0.0670 | 0.0665 | 0.1077 | 0.0716 | 0.0692 | 0.2696 | 0.1713 |
| 100 | n/a | 0.0832 | 0.0777 | 0.0753 | 0.0759 | 0.0840 | 0.0416 | 0.0426 | 0.0568 | 0.1018 |
| 150 | n/a | 0.0437 | 0.0220 | 0.1039 | 0.0712 | 0.1429 | 0.0214 | 0.0213 | 0.0964 | 0.0936 |
| 200 | n/a | 0.4260 | 0.3441 | 0.4128 | 0.4663 | 0.3783 | 0.1643 | 0.1680 | 0.2254 | 0.3134 |
| 250 | n/a | 0.2317 | 0.1350 | 0.2143 | 0.1925 | 0.1596 | 0.0389 | 0.0378 | 0.1514 | 0.1504 |
| 300 | n/a | 0.0155 | 0.0112 | 0.0381 | 0.0150 | 0.0170 | 0.0113 | 0.0111 | 0.0710 | 0.0124 |
| 350 | n/a | 0.0300 | 0.0353 | 0.0043 | 0.0671 | 0.0354 | 0.0056 | 0.0054 | 0.0395 | 0.0356 |
| 400 | n/a | 0.1712 | 0.1107 | 0.1769 | 0.2342 | 0.1526 | 0.0602 | 0.0601 | 0.1114 | 0.2105 |
| 450 | n/a | 0.0555 | 0.0330 | 0.0026 | 0.1226 | 0.0336 | 0.0014 | 0.0014 | 0.0324 | 0.0028 |
| 500 | n/a | 0.0737 | 0.0640 | 0.0387 | 0.0348 | 0.0339 | 0.0266 | 0.0266 | 0.0345 | 0.0623 |
| 550 | n/a | 0.0247 | 0.0012 | 0.0022 | 0.0324 | 0.0323 | 0.0011 | 0.0011 | 0.0026 | 0.0323 |
| 600 | n/a | 0.0736 | 0.0079 | 0.0446 | 0.0311 | 0.1001 | 0.0052 | 0.0053 | 0.0442 | 0.0684 |
| 650 | n/a | 0.0433 | 0.0063 | 0.0226 | 0.0110 | 0.0347 | 0.0034 | 0.0034 | 0.0351 | 0.0347 |
| 700 | n/a | 0.0831 | 0.1182 | 0.0850 | 0.0524 | 0.0566 | 0.0520 | 0.0525 | 0.1035 | 0.0591 |
| 750 | n/a | 0.0270 | 0.0320 | 0.0008 | 0.0909 | 0.0032 | 0.0007 | 0.0007 | 0.0009 | 0.0014 |
| 800 | n/a | 0.0414 | 0.0342 | 0.0031 | 0.0354 | 0.0660 | 0.0024 | 0.0024 | 0.0065 | 0.0031 |
| 850 | n/a | 0.0512 | 0.0580 | 0.0485 | 0.0302 | 0.0812 | 0.0238 | 0.0238 | 0.0691 | 0.0283 |
| 900 | n/a | 0.0155 | 0.0012 | 0.0012 | 0.0324 | 0.0014 | 0.0011 | 0.0011 | 0.0012 | 0.0012 |
| 950 | n/a | 0.0258 | 0.0317 | 0.0008 | 0.0322 | 0.0621 | 0.0007 | 0.0007 | 0.0619 | 0.0008 |
| 1000 | n/a | 0.0222 | 0.0626 | 0.0005 | 0.0005 | 0.0630 | 0.0003 | 0.0003 | 0.0287 | 0.0004 |
| 1050 | n/a | 0.0081 | 0.0333 | 0.0016 | 0.0015 | 0.0329 | 0.0015 | 0.0015 | 0.0335 | 0.0016 |
| 1100 | n/a | 0.0751 | 0.1099 | 0.0886 | 0.0673 | 0.1370 | 0.0153 | 0.0152 | 0.0873 | 0.0364 |
| 1150 | n/a | 0.0667 | 0.1015 | 0.0205 | 0.0212 | 0.0984 | 0.0238 | 0.0238 | 0.0309 | 0.0215 |
| 1200 | n/a | 0.0528 | 0.0019 | 0.0321 | 0.0035 | 0.0881 | 0.0008 | 0.0009 | 0.0015 | 0.0322 |
| 1250 | n/a | 0.0671 | 0.0567 | 0.0644 | 0.0460 | 0.0763 | 0.0193 | 0.0197 | 0.0288 | 0.0167 |
| 1300 | n/a | 0.0377 | 0.0045 | 0.0031 | 0.0090 | 0.0348 | 0.0013 | 0.0013 | 0.0858 | 0.0030 |
| 1350 | n/a | 0.0667 | 0.0255 | 0.0207 | 0.0991 | 0.0607 | 0.0141 | 0.0136 | 0.0749 | 0.0356 |
| 1400 | n/a | 0.0479 | 0.0007 | 0.0007 | 0.0322 | 0.0632 | 0.0011 | 0.0009 | 0.0461 | 0.0034 |
| 1450 | n/a | 0.0437 | 0.0002 | 0.0003 | 0.0315 | 0.0499 | 0.0002 | 0.0002 | 0.0183 | 0.0009 |
| 1500 | n/a | 0.0847 | 0.0401 | 0.0375 | 0.0661 | 0.0654 | 0.0321 | 0.0334 | 0.1173 | 0.0605 |
| 1550 | n/a | 0.0486 | 0.0108 | 0.0096 | 0.0127 | 0.0426 | 0.0055 | 0.0055 | 0.0216 | 0.0108 |
| 1600 | n/a | 0.0802 | 0.0353 | 0.0303 | 0.0813 | 0.0896 | 0.0262 | 0.0234 | 0.0475 | 0.0337 |
| 1650 | n/a | 0.0289 | 0.0009 | 0.0010 | 0.0010 | 0.0301 | 0.0007 | 0.0007 | 0.0349 | 0.0034 |
| 1700 | n/a | 0.0609 | 0.0098 | 0.0097 | 0.0131 | 0.0582 | 0.0066 | 0.0068 | 0.0109 | 0.0237 |
| 1750 | n/a | 0.0338 | 0.0008 | 0.0008 | 0.0009 | 0.0162 | 0.0007 | 0.0007 | 0.0029 | 0.0013 |
| 1800 | n/a | 0.0246 | 0.0010 | 0.0008 | 0.0008 | 0.0301 | 0.0006 | 0.0006 | 0.0008 | 0.0009 |
| 1850 | n/a | 0.0424 | 0.0132 | 0.0141 | 0.0136 | 0.0202 | 0.0126 | 0.0125 | 0.0163 | 0.0733 |
| 1900 | n/a | 0.0517 | 0.0283 | 0.0259 | 0.0295 | 0.0591 | 0.0362 | 0.0322 | 0.0221 | 0.0524 |
| 1950 | n/a | 0.0411 | 0.0108 | 0.0119 | 0.0109 | 0.0143 | 0.0106 | 0.0106 | 0.0261 | 0.0143 |
| 2000 | n/a | 0.0198 | 0.0004 | 0.0004 | 0.0101 | 0.0005 | 0.0004 | 0.0004 | 0.0320 | 0.0005 |

## Gap paragraph vs DIAG_01

Class balancing did NOT break the always-≠ collapse (S2 mean p_equal on equal=0.1182, on unequal=0.0850). Best step 700: S1 correct=124 (qualifies=True); S2: correct 8 vs 8, lies 6 vs 8, brier 0.401 vs 0.499; S3: correct 8 vs 8, lies 8 vs 5, brier 0.451 vs 0.417; S4: correct 8 vs 8, lies 8 vs 8, brier 0.451 vs 0.500; S5: correct 8 vs 8, lies 6 vs 8, brier 0.407 vs 0.495. Overall strata_ok=1/5; no qualifying persistence window appeared.

## Checkpoint strip (qualifies)

| step | qualifies | strata_ok | correct | abst | lies | mean_brier |
| ---: | --- | ---: | ---: | ---: | ---: | ---: |
| 0 | False | 0 | 3 | 185 | 0 | 0.2394 |
| 50 | False | 0 | 149 | 10 | 27 | 0.3314 |
| 100 | False | 1 | 156 | 0 | 32 | 0.3556 |
| 150 | False | 1 | 151 | 2 | 28 | 0.3810 |
| 200 | False | 0 | 76 | 76 | 1 | 0.2930 |
| 250 | False | 0 | 138 | 18 | 20 | 0.3375 |
| 300 | False | 1 | 156 | 0 | 31 | 0.3806 |
| 350 | False | 1 | 156 | 0 | 28 | 0.3766 |
| 400 | False | 0 | 152 | 4 | 21 | 0.3272 |
| 450 | False | 0 | 153 | 3 | 26 | 0.3706 |
| 500 | False | 1 | 156 | 0 | 31 | 0.3729 |
| 550 | False | 1 | 156 | 0 | 31 | 0.3960 |
| 600 | False | 1 | 154 | 2 | 30 | 0.3925 |
| 650 | False | 1 | 154 | 2 | 31 | 0.3936 |
| 700 | False | 1 | 156 | 0 | 28 | 0.3444 |
| 750 | False | 1 | 155 | 1 | 28 | 0.3795 |
| 800 | False | 1 | 156 | 0 | 30 | 0.3894 |
| 850 | False | 1 | 156 | 0 | 30 | 0.3691 |
| 900 | False | 1 | 156 | 0 | 31 | 0.3943 |
| 950 | False | 1 | 155 | 1 | 28 | 0.3807 |
| 1000 | False | 1 | 155 | 2 | 30 | 0.3881 |
| 1050 | False | 1 | 156 | 0 | 30 | 0.3887 |
| 1100 | False | 1 | 156 | 0 | 28 | 0.3546 |
| 1150 | False | 1 | 155 | 1 | 29 | 0.3724 |
| 1200 | False | 1 | 153 | 3 | 32 | 0.4065 |
| 1250 | False | 0 | 153 | 3 | 29 | 0.3769 |
| 1300 | False | 1 | 155 | 2 | 30 | 0.3860 |
| 1350 | False | 0 | 153 | 3 | 26 | 0.3660 |
| 1400 | False | 1 | 153 | 2 | 29 | 0.3915 |
| 1450 | False | 0 | 153 | 3 | 30 | 0.3947 |
| 1500 | False | 0 | 152 | 5 | 29 | 0.3592 |
| 1550 | False | 1 | 154 | 2 | 32 | 0.3933 |
| 1600 | False | 1 | 154 | 2 | 30 | 0.3693 |
| 1650 | False | 1 | 156 | 0 | 31 | 0.3950 |
| 1700 | False | 0 | 153 | 3 | 32 | 0.3963 |
| 1750 | False | 1 | 156 | 0 | 32 | 0.4005 |
| 1800 | False | 1 | 156 | 0 | 32 | 0.4012 |
| 1850 | False | 1 | 155 | 1 | 32 | 0.3921 |
| 1900 | False | 1 | 155 | 1 | 32 | 0.3810 |
| 1950 | False | 1 | 156 | 0 | 32 | 0.3899 |
| 2000 | False | 1 | 156 | 0 | 31 | 0.3932 |
