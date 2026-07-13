# Fable 5 prompt: Level 1 v3.1.4 panel-contract amendment

Write one loud, bounded, pre-data amendment that makes the non-S4 panel builder
bit-exact. Do not reopen S4, the scientific scope, population, endpoint,
inference, selector, learner, or gate order. Do not write code, draw entropy,
generate a panel, run data, or create a lock/escrow/outcome.

## Read

1. `experiments/level_1_contact/SCIENTIFIC_SPEC_V3_DRAFT.md` sections 3-4
2. `experiments/level_1_contact/SCIENTIFIC_SPEC_V3_1_ADDENDUM.md` A1/A3/A4
3. `experiments/level_1_contact/SCIENTIFIC_SPEC_V3_1_1_CORRECTION.md` C1-C3
4. `experiments/level_1_contact/SCIENTIFIC_SPEC_V3_1_2_CORRECTION.md` F-1/F-3
5. `experiments/level_1_contact/SCIENTIFIC_SPEC_V3_1_3_CORRECTION.md`
6. `experiments/level_1_contact/SCIENTIFIC_SPEC_SIGNATURES.md`
7. `reviews/opus_level1_panel_generator_readiness.md`
8. `src/philosophia/level1/{config,serialization,world,pool}.py`

Adopt Opus PG-1 through PG-4 and the bounded table, with the exact closures
below. Historical specs and the signed record remain untouched.

## Required table

Provide one normative table for S1/S2/S3/S5. S4 carries forward verbatim. For
every group pin: count, global panel ids, stratum-local ids, exact ordered `d`,
zone, exact cell selection, exact `cell_identity` components, padding/length
eligibility, label, collision registry, and realization order.

Use these closed repairs:

- S1: 124 NO; `d_i=1+((i-1) mod (n-1))`; lowest unused reserved cell of
  required `d` in canonical global cell-rank order.
- S2: 8 YES at `d=n`, 4 NO at `d=n-1`, 4 NO at `d=n+1`; zone 3 only for
  NO-high at `n=125`.
- S3: 8 YES at `d=0` with `u!=v`, then 4 NO at `d=1`, 4 NO at `d=2`.
- S5: 4 YES `d=0`; 4 YES `d=n`; 4 NO `d=n+2`; 4 NO at the exact ordered
  values `{3,5,7,9}`. Zone 3 only for `d=n+2` at `n in {124,125}`.
- Any required `d>125`: deterministic corner
  `(a,b)=(ceil(d/2),-floor(d/2))`, secret-realized, never a public word.
- Reserved selection: reserved cells are filtered by the exact eligibility,
  ordered by their **global A3 canonical cell rank**, and the lowest unused rank
  is consumed. Consumption is global across the current world's panel and occurs
  in ascending global panel id, so repeated-difference S1 items are unique and
  deterministic.
- Reserved `cell_identity` is that one global canonical integer rank. A zone-3
  `cell_identity` is two consecutive integer components `a`, then `b`; extend
  v3.1.3 B-2 explicitly from S4 to every zone-3 panel item.

## IDs and PRF surface

Remove the id ambiguity explicitly:

- global panel ids are zero-based and fixed:
  S1 `0..123`, S2 `124..139`, S3 `140..155`, S4 `156..171`, S5 `172..187`;
- stratum-local ids are one-based only as table labels;
- the F-3 `item_id` PRF component is always the **global zero-based panel id**;
- panel serialization and secret order bind the same global ids.

## Exact eligibility and padding

- S1/S2/S3-NO and S5-`d=n+2`: padding is drawn secret-keyed from the ascending
  admissible padding set, then word rank as already specified.
- S3-YES: the same draws, with `u!=v` as an additional rejection predicate.
- S5-`d=0`: eligible reserved cells satisfy `|a|>=95` (and `a=b`); fixed
  `(p_u,p_v)=(5,5)`, hence both side lengths are at least 100.
- S5-`d=n`: fixed `(p_u,p_v)=(5,0)`; a reserved cell is eligible iff
  `abs((|a|+10)-|b|)>=60`. Do not use the word "achievable" as a predicate.
- S5 locked `{3,5,7,9}`: eligible cells satisfy `|a|>=95` and `|b|>=95`;
  fixed `(p_u,p_v)=(5,5)`.
- Every fixed padding must also satisfy the global 138-token word cap; failure of
  the exhaustive availability verifier is design invalidity.

Withdraw S2 "NO length-matched to YES" and the generic S3/S5 "matched" wording
as mathematically unsatisfiable or non-executable. State loudly that S2/S3/S5
have no anti-lookup authority and that this relaxation does not touch S4's sole
operational-certificate tooth.

## Collision semantics

Make v3.1.3 B-1 operational without changing its redraw rule:

- each stratum owns an accepted-pair registry initially empty;
- a candidate `(u,v)` for the current item collides iff it is already in that
  stratum's registry; S3-YES additionally rejects `u==v`;
- on either rejection, hold `u` and both pads fixed and advance only the current
  item's `v`-rank domain, exactly as B-1; after acceptance add `(u,v)` to the
  registry;
- exhaustion routes to design invalidity.

If you find this registry inconsistent with the already-signed B-1 availability
claim, name the smallest correction rather than hiding it.

## Enumeration obligations

Require an exhaustive dummy-only verifier over all `n=66..125` proving: counts
and ids; labels; zone crossings; global-rank consumption without reuse;
eligibility and word caps; enough reserved cells and word ranks; `u!=v` for all
S3-YES; construction/serialization of all three edge crossings; exact schema
surface `188 = 124+16+16+16+16`; no public word reuse. Verifier failure is design
invalidity.

## Deliverables

Write:

1. `experiments/level_1_contact/SCIENTIFIC_SPEC_V3_1_4_PANEL_ADDENDUM.md`
2. `reviews/fable_level1_v3_1_4_panel_closure.md`

Closure verdict: `READY_FOR_LEVEL1_PANEL_AMENDMENT_REVIEW`. Disposition every
PG finding, list the exact superseded phrases, state that the prior three author
tokens remain valid for all unchanged science but this panel amendment needs its
own new author token after bounded Opus and Sol confirmation, and propose that
token. Confirm no code/panel/entropy/data/lock/escrow/outcome was created.
