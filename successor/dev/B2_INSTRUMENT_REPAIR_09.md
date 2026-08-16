# B2_INSTRUMENT_REPAIR_09

status = `STOP_NO_CUDA`

## 1. Input hashes

- `B2_INSTRUMENT_REPAIR_09_TICKET.md`: `b8759ebdd7743239bf97238394cb267c091382469ac10dfc4308b5b53670cc85`
- `B2_PATH_VS_DESTINATION_DESIGN_V2.md`: `160726a6c06fed20b5aa554449c3f14c03f45b9ee52cdcf1ca49ff49ce238dd2`
- `B2_PILOT_08.md`: `107d8a6ed5dcf3e6dac9d4f43196f6c3bdf3d372ff5068e0df050bcceeb76d7f`
- `b2_path_pilot_08.py`: `d5099d56ec78911a8dfb451a94d34350a3b8060fe90a0d05687edcc458f1c03f`
- `b2_pilot_08_results.json`: `593b478811eea533428805f60f618d58df04de4fed2bd06aaae6fe767aa63052`
- `b2_instrument_repair_09.py`: `f5b23a9026111870d6cc93b858b807868f2fd072bbbcfab0802213cc4bb0a2e6`

## 2. Frozen constants (unchanged)

```text
N_MAX=2000
K=250
H_DEST=500
M_PATH=600
PATH_BATCH=32
M_ROADS=4
VICREG_INV=25.0
VICREG_VAR=25.0
VICREG_COV=1.0
CONTRAST_TEMP=0.1
PILOT_SEEDS=(0, 1)
_D_PATH_LO=-80
_D_PATH_HI=80
```

## 3. Held-out loss and components (interpretable)

NOT_PRODUCED — no CUDA; run not executed.

## 4. Training-loss curve (`not_interpretable`)

NOT_PRODUCED — no CUDA; run not executed.

## 5. road_gap table

NOT_PRODUCED — no CUDA; run not executed.

## 6. Mechanism probes with delta vs matched init

NOT_PRODUCED — no CUDA; run not executed.

Footnote chance columns (not the comparison): exact_d_chance≈1/n_classes, length_chance≈1/n_lengths, sign_d_chance=0.5, residue_chance=1/66.

## 7. d_within_len

NOT_PRODUCED — no CUDA; run not executed.

## 8. Per-arm per-stratum floor table and M3

NOT_PRODUCED — no CUDA; run not executed.

## 9. Section-3 conditional fix

- conditional_fix_fired = **not evaluated**
- mean_std at held-out step 600 (P0): NOT_PRODUCED

## 10. Wall time per arm

NOT_PRODUCED — no CUDA; run not executed.

Prior CPU attempt: ~29 min wall, halted seed0 arm D after dest ckpt 350.
