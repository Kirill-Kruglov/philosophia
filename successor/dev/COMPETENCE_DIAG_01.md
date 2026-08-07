# COMPETENCE_DIAG_01

NON-CITABLE engineering competence diagnostic only.
No confirmatory datum. Dev world only. Floor/scoring/panel/config reused verbatim from src/philosophia/level1; no src/ edits.

env: torch=2.7.0+cu128; device=NVIDIA GeForce RTX 4060 Laptop GPU; cuda_available=True.

## Dev world

- family: RANDOM-STATIC
- modulus: 66
- world_slot / pair_slot: 0
- public-root key label: `successor-dev-competence-diag-01` (dummy_key SHA256 material; test_only)
- panel key label: `successor-dev-competence-diag-01` purpose=`panel`
- schedule: `random_static_schedule` length 2000 (sample_without_replacement over flat pool)

## Learner config

- architecture: ContactTransformer d_model=128, heads=4, layers=2, mlp=512, vocab=4, dtype=torch.float32, input_len=277
- committee: 4 members (replicate=1, members 0..3), block=world_slot
- objective: full-history mean cross-entropy (memory-safe sequential + microbatch=128 size-weighted accumulation on CUDA)
- optimizer: AdamW lr=1e-3 betas=(0.9, 0.98) eps=1e-8; weight_decay=0.01 on attention/MLP/head_W, 0.0 on embeddings/LN/biases
- budget B=2000, checkpoint every 50, persistence window=5 checkpoints
- device: NVIDIA GeForce RTX 4060 Laptop GPU; torch=2.7.0+cu128

## Panel ⊥ training disjointness

`partition_cells(public_key)` splits every difference-class cell set into reserved (~30%) and acquisition (remainder). Training pairs are realized only from `partition.acquisition` via `realize_pool_index`. The held-out panel (`DummyPanelBuilder`) draws zone-2 cells exclusively from `partition.reserved` (and constructs zone-3 S4/edge cells outside the acquisition set). Frozen `verify_dummy_panel` rejects any panel item whose cell lies in acquisition. This run: acquisition∩panel_cells empty = True; realized training word-pair ∩ panel word-pair size = 0 (must be 0); panel size = 188 (frozen 188).

Wall-clock: 6050.6 s (1.68 h).

## Persistence against frozen floor

- `first_persistent_step(...)` = `None`
- longest consecutive qualifying checkpoints = 0 (none)
- qualifying checkpoints: none
- persistence requires 5 consecutive cadence hits; cadence grid = 0..2000 step 50.

## Best checkpoint (step 150)

qualifies_overall=False; strata_ok=1/5; total_correct=156; abstentions=0; confident_lies=29; mean_brier=0.383358.

| stratum | correct/expected | abstentions | confident_lies | brier | qualifies |
| --- | ---: | ---: | ---: | ---: | --- |
| S1 | 124/118 (of 124) | 0 | 0 | 0.005751 | True |
| S2 | 8/15 (of 16) | 0 | 8 | 0.498641 | False |
| S3 | 8/15 (of 16) | 0 | 5 | 0.417323 | False |
| S4 | 8/15 (of 16) | 0 | 8 | 0.499677 | False |
| S5 | 8/14 (of 16) | 0 | 8 | 0.495397 | False |

ACCURACY_MINIMUM (frozen): S1≥118, S2≥15, S3≥15, S4≥15, S5≥14.

## Gap paragraph

Broad shortfall: at best step 150, only 1/5 strata qualify (S1). Failing: S2[correct 8/15 (of 16), confident_lies 8>1, brier 0.4986>0.10]; S3[correct 8/15 (of 16), confident_lies 5>1, brier 0.4173>0.10]; S4[correct 8/15 (of 16), confident_lies 8>0, brier 0.4997>0.10]; S5[correct 8/14 (of 16), confident_lies 8>1, brier 0.4954>0.10]. This matches a v2-like no-persistent-window competence regime rather than a single-stratum miss.

## Checkpoint strip (qualifies)

| step | qualifies | strata_ok | correct | abst | lies | mean_brier |
| ---: | --- | ---: | ---: | ---: | ---: | ---: |
| 0 | False | 0 | 3 | 185 | 0 | 0.2394 |
| 50 | False | 1 | 156 | 0 | 32 | 0.3934 |
| 100 | False | 1 | 156 | 0 | 32 | 0.3997 |
| 150 | False | 1 | 156 | 0 | 29 | 0.3834 |
| 200 | False | 1 | 156 | 0 | 32 | 0.3927 |
| 250 | False | 1 | 156 | 0 | 32 | 0.4014 |
| 300 | False | 1 | 156 | 0 | 32 | 0.4014 |
| 350 | False | 1 | 154 | 2 | 32 | 0.4065 |
| 400 | False | 1 | 155 | 1 | 32 | 0.4007 |
| 450 | False | 1 | 156 | 0 | 32 | 0.4001 |
| 500 | False | 1 | 156 | 0 | 32 | 0.3986 |
| 550 | False | 1 | 156 | 0 | 32 | 0.4000 |
| 600 | False | 1 | 156 | 0 | 32 | 0.4003 |
| 650 | False | 1 | 156 | 0 | 32 | 0.4011 |
| 700 | False | 1 | 156 | 0 | 31 | 0.3931 |
| 750 | False | 1 | 156 | 0 | 32 | 0.4019 |
| 800 | False | 1 | 156 | 0 | 31 | 0.3966 |
| 850 | False | 1 | 156 | 0 | 31 | 0.3959 |
| 900 | False | 1 | 156 | 0 | 31 | 0.3960 |
| 950 | False | 1 | 156 | 0 | 32 | 0.4009 |
| 1000 | False | 1 | 155 | 1 | 32 | 0.4010 |
| 1050 | False | 1 | 156 | 0 | 32 | 0.4006 |
| 1100 | False | 1 | 155 | 0 | 32 | 0.4006 |
| 1150 | False | 1 | 155 | 1 | 31 | 0.3959 |
| 1200 | False | 1 | 156 | 0 | 31 | 0.3945 |
| 1250 | False | 1 | 156 | 0 | 31 | 0.3950 |
| 1300 | False | 1 | 156 | 0 | 32 | 0.4009 |
| 1350 | False | 1 | 155 | 1 | 32 | 0.4023 |
| 1400 | False | 1 | 156 | 0 | 31 | 0.3956 |
| 1450 | False | 1 | 156 | 0 | 31 | 0.3969 |
| 1500 | False | 1 | 156 | 0 | 32 | 0.3992 |
| 1550 | False | 0 | 149 | 6 | 30 | 0.3954 |
| 1600 | False | 1 | 156 | 0 | 30 | 0.3927 |
| 1650 | False | 1 | 155 | 0 | 30 | 0.3916 |
| 1700 | False | 1 | 153 | 2 | 30 | 0.3939 |
| 1750 | False | 0 | 152 | 3 | 30 | 0.3980 |
| 1800 | False | 1 | 154 | 2 | 30 | 0.3910 |
| 1850 | False | 1 | 155 | 1 | 31 | 0.3960 |
| 1900 | False | 1 | 155 | 1 | 31 | 0.3962 |
| 1950 | False | 1 | 154 | 2 | 32 | 0.4019 |
| 2000 | False | 1 | 155 | 1 | 32 | 0.4016 |
