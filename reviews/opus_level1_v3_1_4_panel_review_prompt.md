# Opus 4.8 prompt: Level 1 v3.1.4 panel-amendment X-line review

Perform a bounded repair-fidelity and implementation-readiness review of the
v3.1.4 panel addendum. Do not reopen S4, scope, population, learner, endpoint,
inference, selector, or gate order. Do not write code, draw entropy, generate a
panel, or execute any gate.

## Read

1. `reviews/opus_level1_panel_generator_readiness.md`
2. `experiments/level_1_contact/SCIENTIFIC_SPEC_V3_1_4_PANEL_ADDENDUM.md`
3. `reviews/fable_level1_v3_1_4_panel_closure.md`
4. governing v3.1.1-v3.1.3 corrections as needed
5. `src/philosophia/level1/{config,serialization,world,pool}.py`

## Checks

1. Confirm PG-1 through PG-4 are adopted exactly: ids, global cell rank,
   consumption order, edge corners, two-component identities, S5 values and
   eligibility, withdrawn matching claims, and S4 preservation.
2. Independently enumerate the table algebraically for `n=66..125`: counts,
   labels, zones, caps, availability, repeated differences, and exact three edge
   crossings. No real/dummy panel execution is authorized.
3. Confirm the F-3 PRF `item_id` is unambiguously global zero-based and every
   domain component/ordering choice yields one byte stream.
4. Audit the accepted-pair registry against B-1, including exhaustion rather
   than only ordinary collision probability.

## Specific exhaustion challenge

The addendum still permits padding `p_v=0` in rejection-bearing drawn-padding
groups:

- S3-YES rejects `u==v`;
- each non-S4 zone-3 edge group has four items sharing one corner cell and rejects
  a pair already accepted in the stratum registry.

For a fixed displacement and `p_v=0`, `W(v)` is a singleton. If S3 draws the
same singleton for `u` and `v`, or a shared-corner item collides while its fixed
`v` surface is singleton, advancing only the `v`-rank counter cannot produce a
new `v`. This appears to contradict the amendment's claim that B-1 exhaustion is
impossible.

Recompute this explicitly. If confirmed, require the smallest bounded repair:
draw `p_v` only from the ascending **positive admissible padding set** for
S3-YES and every non-S4 repeated-corner group; keep `p_u` under the existing
rule. Show that `p_v>=1` gives enough distinct `v` words for all rejections at
every edge. Verify S4's fixed padding table already supplies the necessary rank
surface. Do not change labels, counts, cells, or any scientific claim.

## Output

Write `reviews/opus_level1_v3_1_4_panel_review.md`. Use exactly one verdict:

- `LEVEL1_V3_1_4_XLINE_APPROVED_FOR_SIGNATURE`
- `REVISE_LEVEL1_V3_1_4_PANEL_TEXT`
- `BLOCKED_LEVEL1_V3_1_4_PANEL_CONTRACT`

Lead with findings and give only exact bounded replacement text if required.
This review authorizes no signature or execution by itself.
