# SURFACE_PROBE_06

NON-CITABLE surface-token probe. No training. No src/ edits.
No confirmatory datum. Loads CAPACITY_DIAG_04 final committee only.

checkpoint: `capacity_diag_04_final.pt` (step=2000, schedule=curated_rich_equal).
device: cuda.

## Setup

- Held-out equals = panel equals (32) + reserved extras (536), same construction as GENFAIL_SHAPE_05.
- SEEN-WORD: ≥1 of the two words appears in ANY training pair (equal or unequal).
- NOVEL-WORD: BOTH words never appear in any training pair.
- panel∩train pairs = 0; extra∩train = 0; extra∩panel = 0.
- Train vocabulary: 3581 distinct words across 2000 distinct training pairs.

## Table (held-out equals)

| bucket | n | n_correct | accuracy | mean p_equal | n_panel | n_extra | both_sides_seen | one_side_seen |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| SEEN-WORD (i) | 158 | 99 | 62.7% | 0.7038 | 9 | 149 | 9 | 149 |
| NOVEL-WORD (ii) | 410 | 257 | 62.7% | 0.6806 | 23 | 387 | 0 | 0 |

### Source × bucket

| source | bucket | n | n_correct | accuracy | mean p_equal |
| --- | --- | ---: | ---: | ---: | ---: |
| panel | SEEN-WORD | 9 | 5 | 55.6% | 0.6620 |
| panel | NOVEL-WORD | 23 | 11 | 47.8% | 0.5262 |
| extra | SEEN-WORD | 149 | 94 | 63.1% | 0.7063 |
| extra | NOVEL-WORD | 387 | 246 | 63.6% | 0.6898 |

## Verdict

**NOT-PURELY-SURFACE**

NOT-PURELY-SURFACE: SEEN-WORD (n=158, acc=62.7%, mean p=0.7038) and NOVEL-WORD (n=410, acc=62.7%, mean p=0.6806) are comparable (Δacc=-0.000, Δp=+0.023). The weak held-out-equal signal is not explained by token reuse alone — some fragile structure already exists for novel words. A gap-closer should strengthen that weak per-word element representation (make fold equality explicit/robust), not rebuild token-latching; more contact of the same kind is unlikely to suffice at B=2000.
