# Codex closure: Level 1 gated implementation reviews

Date: 2026-07-13. This memo closes only the implementation findings in:

- `opus_level1_panel_implementation_review.md`
- `sol_level1_gated_implementation_review.md`

It changes no signed scientific constant, panel item, label, threshold, estimand,
predicate, route, or gate order.

## Opus X-line dispositions

- **PI-1 closed:** `test_reserved_cell_identities_are_golden_at_center_and_edges`
  pins representative S1/S2/S3/S5 canonical identities at `n=66,124,125`,
  including all three zone-3 edge forms.
- **PI-2 closed:** `test_full_dummy_panel_word_bytes_have_golden_digest`
  pins SHA-256
  `93674833af7d3f98bc19079de449acd8bf3e68d5f0acc53f9eefb8084909d9c2`
  over the length-delimited `(global_id,left,right)` stream for the fixed dummy
  keys and `n=66/world_slot=0`.
- **PI-3 closed:** `test_feature_null_verifier_rejects_non_d_label_separator`
  injects a label-separating padding feature whose NO key spans both S4 NO
  differences, so it cannot reconstruct `d`; the verifier must raise.
- **PI-4:** no code change required. Pad/rank streams remain independently
  domain-separated by side and purpose, so source call grouping does not alter
  F-3 bytes.

No panel production code changed.

## Sol Y-line dispositions

- **M1 closed:** `estimate_contrast` now rejects all outcome stratum sizes outside
  `n_h in {4,5,6,7,8}`; parameterized tests reject 2 and 3.
- **M2 closed:** a non-census `n_h=4` hand anchor pins estimate `20`, variance
  `13.88888888888889`, Satterthwaite df `6`, Bonferroni half-width
  `12.2516220070524`, and the finite-population label.
- **M3 closed:** `committee_equal_probability` requires exactly four members,
  evaluates their `p_equal` values without gradients, checks compatible shapes,
  and returns their exact arithmetic mean. Tests pin the mean and reject three
  members. The sealed evaluator/trajectory driver remains absent and gated.
- **Minor optimizer-order gap closed:** the test now pins the exact identities and
  order of both AdamW parameter groups, not only their counts and decay values.
- RNG-state hashing is not added: the signed current scorer uses no RNG. Any
  future randomized scorer remains obligated to add that state to the mutation
  contract before review.
- Real panel order/emission remains absent as required.

## Verification

```text
122 passed
VALID  inheritance/line12_same_wall/experiment_A/decision.json
VALID  experiments/level_0_grokking/outcomes/decision.json
OK: inherited primary and Philosophia Level 0 decisions are valid.
```

Static search still finds only the deliberately fail-closed
`run_level1_trajectory`; no OS entropy, real-key constructor, panel writer,
feasibility/scout driver, N3 lock, escrow, or outcome path exists.

## Requested bounded confirmations

- Opus: `LEVEL1_DUMMY_PANEL_IMPLEMENTATION_CONFIRMED`
- Sol: `LEVEL1_GATED_IMPLEMENTATION_CONFIRMED`

These confirmations authorize only accepting and committing the reviewed gated
implementation. They do not authorize the public-root draw, real panel,
feasibility/scout, N3 selection, lock, escrow, trajectory, or outcome.
