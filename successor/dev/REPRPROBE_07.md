# REPRPROBE_07

NON-CITABLE representation probe. Base committee FROZEN — only linear probes are fit. No src/ edits. No confirmatory datum.

checkpoint: `capacity_diag_04_final.pt` (step=2000). device=cuda.

## Activation probed (exact)

ContactTransformer encodes pairs only. Forward computes
`readout = final_ln(x)[:, -1, :]` then `readout @ head_W + head_b`
(see `src/philosophia/level1/model.py`). We probe that **pre-head**
vector (`final_ln` at the last sequence position, dim=128),
averaged across the 4 frozen committee members.

- **Per-word residue probe:** encode `word ⊕ SEP ⊕ word` via
  `encode_pair(word, word)` so the last position is the word's last
  R/L token in a self-pair context (well-defined per-word vector;
  model has no single-word forward).
- **Pair equality probe:** encode `left ⊕ SEP ⊕ right` as in training;
  same pre-head last-position vector.

## Data / splits

- Train schedule reconstructed (curated DIAG_04); 3581 train words, 2000 train pairs.
- NOVEL words (not in any train pair): 44051 from panel + reserved-cell realizations.
- Residue probe split: DISJOINT novel-word sets, stratified by residue (~70/30); probe-train=30842 words, probe-test=13209 words; no word shared across split.
- Pair probe: held-out equals=568 + balanced held-out unequals=568 (reserved/panel, ∉ train); 70/30 pair split → train=795, test=341.
- panel∩train pairs = 0; probe never backprops into committee.

## Results

### 1. Residue linear probe (66-way softmax on novel words)

- chance = 1/66 = 1.52%
- probe train acc = 6.52% (n=30842)
- **probe test acc = 5.24%** (n=13209)

### 2. Pair-equality linear probe vs frozen head

- linear equal? test acc = **60.41%** (n=341; train=67.17%)
- frozen head acc on same pair-test set = **52.20%**
- frozen head equal-only acc on pair-test equals = **64.77%** (n=176; compare to GENFAIL ~63% on all held-out equals)

## Verdict

**NOT-REPRESENTED**

NOT-REPRESENTED: residue linear probe on NOVEL words is near chance (test acc=5.24% vs 1.52%). Pair-equality linear probe=60.41% vs head 52.20% (equal-only head=64.77%). The fold reduction is not linearly available in the probed activation; a gap-closer must induce an element representation, not merely retune the head.
