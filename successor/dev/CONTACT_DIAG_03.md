# CONTACT_DIAG_03

NON-CITABLE equal-contact diagnostic. No confirmatory datum.
Exact DIAG_01/02 setup (modulus 66, same dummy keys, partition, random_static_schedule). No src/ edits. No new full training run.

Setup: public=`successor-dev-competence-diag-01`, panel=`successor-dev-competence-diag-01`, world_slot=0, B=2000, modulus=66.

## 1. Schedule equal-contact counts

- Total equal draws in schedule: **43** / 2000 (2.150%).
- Distinct equal word-pairs contacted by end of B: **43**.
- Distinct Z/66Z residues hit by those equals: **31**.

| step | distinct equals seen | cumulative equal draws |
| ---: | ---: | ---: |
| 0 | 0 | 0 |
| 50 | 1 | 1 |
| 100 | 2 | 2 |
| 150 | 3 | 3 |
| 200 | 4 | 4 |
| 250 | 6 | 6 |
| 300 | 7 | 7 |
| 350 | 9 | 9 |
| 400 | 11 | 11 |
| 450 | 11 | 11 |
| 500 | 13 | 13 |
| 550 | 13 | 13 |
| 600 | 14 | 14 |
| 650 | 14 | 14 |
| 700 | 17 | 17 |
| 750 | 18 | 18 |
| 800 | 18 | 18 |
| 850 | 19 | 19 |
| 900 | 19 | 19 |
| 950 | 19 | 19 |
| 1000 | 19 | 19 |
| 1050 | 21 | 21 |
| 1100 | 23 | 23 |
| 1150 | 26 | 26 |
| 1200 | 27 | 27 |
| 1250 | 29 | 29 |
| 1300 | 29 | 29 |
| 1350 | 30 | 30 |
| 1400 | 30 | 30 |
| 1450 | 30 | 30 |
| 1500 | 33 | 33 |
| 1550 | 34 | 34 |
| 1600 | 36 | 36 |
| 1650 | 36 | 36 |
| 1700 | 38 | 38 |
| 1750 | 38 | 38 |
| 1800 | 39 | 39 |
| 1850 | 40 | 40 |
| 1900 | 41 | 41 |
| 1950 | 43 | 43 |
| 2000 | 43 | 43 |

### Pool / panel equal upper bounds

- Acquisition pool: equal-cells (difference % 66 == 0) = **314**; distinct realizable equal word-pairs = **1256**; residues covered = **66**.
- Held-out panel equal half: **32** items (S1=0, S2=8, S3=8, S4=8, S5=8; S1 has 0 equals by construction); distinct pairs = **32**; residues = **19** ([1, 5, 10, 11, 13, 14, 16, 17, 18, 19, 20, 26, 28, 29, 30, 31, 59, 61, 65]).

## 2. Structure paragraph

Equal pairs are words (u,v) with fold(u)=fold(v)=e in Z/66Z — different roads to the same residue e. On the schedule, 31 residues receive at least one equal pair; only 9 have ≥2 distinct equal pairs (repeated multi-road evidence), while 22 are singleton-pair (idiosyncratic) contacts (mean distinct word-nets per contacted residue = 1.87, noting one pair already contributes two nets). Panel equals span residues [1, 5, 10, 11, 13, 14, 16, 17, 18, 19, 20, 26, 28, 29, 30, 31, 59, 61, 65]; overlap with schedule-equal residues = 5/19; panel-only residues = [1, 5, 10, 11, 13, 14, 17, 19, 20, 26, 30, 59, 61, 65]. Exact panel equal word-pairs also present in schedule distinct equals: 0/32. A learner could at best induce equality on sparsely sampled contacted residues; most panel equal residues are never seen as equals in training, so panel success would require extrapolation from an under-determined contact set.

## 3. Train-stream separation

Train-stream separation: checkpoints absent — DIAG_01/02 did not persist model weights under successor/dev/; not evaluated (no new full run launched).

## Verdict

**STARVATION**

STARVATION: the passive schedule contacts only 43 distinct equal pairs (43 equal draws, 2.15% of B) covering 31/66 residues — vs 1256 distinct equals available in acquisition and 32 panel equals on 19 residues. Panel residue overlap is 5/19 (panel-only residues: 14); exact panel equal pairs seen in training: 0/32. Only 9/31 contacted residues have ≥2 distinct equal pairs (repeated multi-road evidence); 22 are singleton-pair contacts. Equality is under-determined by RANDOM-STATIC passive contact; the always-≠ collapse is the expected response to near-absent equal exemplars, not a demonstrated capacity failure. GENERALIZATION cannot be tested without saved checkpoints.
