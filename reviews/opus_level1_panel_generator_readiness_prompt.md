# Opus 4.8 prompt: signed Level 1 panel-generator readiness audit

Perform a bounded pre-data implementation-readiness audit of the signed Level 1
panel generator. The scientific scope, S4 operational certificate, population,
endpoint, inference, selector, and gate order are closed. Do not write code,
draw entropy, generate a panel, run data, or create a lock/escrow/outcome.

## Read

1. `experiments/level_1_contact/SCIENTIFIC_SPEC_V3_DRAFT.md` sections 3-4
2. `experiments/level_1_contact/SCIENTIFIC_SPEC_V3_1_ADDENDUM.md` A1, A3, A4
3. `experiments/level_1_contact/SCIENTIFIC_SPEC_V3_1_1_CORRECTION.md` C1-C3
4. `experiments/level_1_contact/SCIENTIFIC_SPEC_V3_1_2_CORRECTION.md` F-1/F-3
5. `experiments/level_1_contact/SCIENTIFIC_SPEC_V3_1_3_CORRECTION.md`
6. `experiments/level_1_contact/SCIENTIFIC_SPEC_SIGNATURES.md`
7. `src/philosophia/level1/world.py`, `pool.py`, and `serialization.py`

No Level 1 entropy or datum exists. Neutral substrate code uses dummy keys only;
the real panel builder has deliberately not been implemented.

## Known implementation contradiction

v3.1 classifies these edge items as zone 3:

- S2 `d=n+1=126` at `n=125`;
- S5 `d=n+2` at `n in {124,125}`, hence `d in {126,127}`.

But v3.1.2 F-3 says S1/S2/S3/S5 use a reserved cell's canonical rank. Reserved
cells exist only for `|d|<=125`. The signed contract therefore supplies no
`cell_identity` or selection rule for those edge items, and v3.1.3 B-2 cannot
serialize them as written.

## Audit the complete non-S4 panel contract

Do not stop after confirming the known contradiction. Determine whether one
independent implementation can derive identical panel bytes for every world
`n=66..125`, checking:

1. exact cell selection and identity for every S1/S2/S3/S5 item, including all
   repeated-difference items and zone-3 edge crossings;
2. the exact meaning and satisfiability of S2 "NO items length-matched to YES".
   Note the parity obstruction: total raw pair length is congruent to `d mod 2`,
   so `d=n` and `d=n+/-1` cannot have identical total lengths;
3. S3's "matched" length rule and distinctness/collision scope;
4. S5's exact four "locked d" values, their provenance/domain, item order, and
   the cell eligibility predicates for `>=100` side lengths and `>=60` length
   imbalance;
5. padding selection, word-rank selection, collision redraw, and canonical item
   ordering under the final secret-keyed domains;
6. whether every chosen cell has enough admissible word realizations under the
   pinned constraints;
7. whether public reservation geometry plus secret raw realization remains the
   intended confidentiality boundary.

Treat a phrase as closed only if two independent implementers must produce the
same cell identity, labels, lengths/padding eligibility, PRF inputs, and bytes.

## Required repair shape

If revision is needed, give one bounded addendum table for S1/S2/S3/S5 with, per
item group: count, ordered ids, exact `d`, zone, exact cell-selection rule,
`cell_identity` encoding, padding/length eligibility, label, and collision scope.
Preserve S4 verbatim. Prefer deterministic canonical rules and existing secret
domains; introduce no outcome-dependent value and no new scientific claim. Any
unavoidable relaxation of "matched" must be named honestly and shown not to
weaken S4's sole anti-lookup role.

## Output

Write `reviews/opus_level1_panel_generator_readiness.md`. Use exactly one:

- `LEVEL1_PANEL_GENERATOR_IMPLEMENTATION_READY`
- `REVISE_LEVEL1_PANEL_GENERATOR_CONTRACT`
- `BLOCKED_LEVEL1_PANEL_CONSTRUCTION`

Lead with findings and provide the smallest bit-exact repair. This audit may
authorize no execution; a correction would require a loud signed pre-data
amendment and bounded confirmation before panel implementation.
