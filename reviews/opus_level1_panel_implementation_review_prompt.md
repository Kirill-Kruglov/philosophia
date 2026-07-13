# Opus 4.8 review prompt: Level 1 dummy panel implementation

You are the X-line implementation auditor for Philosophia Level 1. Work in the
local repository at `/home/master/llm_projects/philosophia`. Do not commit.
Write the full review to:

`reviews/opus_level1_panel_implementation_review.md`

Then return a concise chat summary with the verdict and exact blocking edits.

## Authority and scope

Kirill has signed the governing Level 1 contract and the bounded panel
amendment. Read, in order:

1. `experiments/level_1_contact/SCIENTIFIC_SPEC_V3_DRAFT.md`
2. `experiments/level_1_contact/SCIENTIFIC_SPEC_V3_1_ADDENDUM.md`
3. `experiments/level_1_contact/SCIENTIFIC_SPEC_V3_1_1_CORRECTION.md`
4. `experiments/level_1_contact/SCIENTIFIC_SPEC_V3_1_2_CORRECTION.md`
5. `experiments/level_1_contact/SCIENTIFIC_SPEC_V3_1_3_CORRECTION.md`
6. `experiments/level_1_contact/SCIENTIFIC_SPEC_V3_1_4_PANEL_ADDENDUM.md`
7. `experiments/level_1_contact/SCIENTIFIC_SPEC_V3_1_4_1_PANEL_CORRECTION.md`
8. `experiments/level_1_contact/SCIENTIFIC_SPEC_SIGNATURES.md`
9. `experiments/level_1_contact/PANEL_CONTRACT_SIGNATURE.md`
10. `reviews/opus_level1_panel_generator_readiness.md`
11. `reviews/fable_level1_v3_1_4_panel_closure.md`
12. `reviews/opus_level1_v3_1_4_1_final_confirmation.md`

Audit the implementation at current HEAD plus the uncommitted files:

- `src/philosophia/level1/world.py`
- `src/philosophia/level1/serialization.py`
- `src/philosophia/level1/pool.py`
- `src/philosophia/level1/panel.py`
- `tests/test_level1_substrate.py`
- `tests/test_level1_panel.py`

Run:

```bash
.venv/bin/python -m pytest tests/test_level1_panel.py tests/test_level1_substrate.py -q
.venv/bin/python -m pytest -q
.venv/bin/python scripts/verify_all.py
```

## Required audit questions

1. Do all S1/S2/S3/S4/S5 item ids, counts, differences, zones, labels,
   cell-selection rules, padding rules, collision scopes and realization order
   match v3.1.4 + v3.1.4.1 exactly for all `n=66..125`?
2. Are global A3 cell ranks and zone-3 two-integer identities canonical and
   invertible, with no reuse of reserved cells?
3. Does B-1 collision handling hold `u` and both padding draws fixed, advance
   only the v-rank stream, and reject only the specified collision surface?
   Is exhaustion checked against the true admissible v universe?
4. Are the public-root and panel-key domains byte-exact under A2/F-3/B-2,
   including global zero-based item ids, side, cell-identity components,
   purpose and counter ownership?
5. Does S4 preserve the signed operational-certificate construction? Audit the
   feature-null verifier independently. It must reject any separating nuisance
   combination unless that exact combination reconstructs `d`, and it must
   expose exactly the reviewed 11 reconstruction maps rather than silently
   exempting them.
6. Is the schema surface genuinely world-independent without claiming that
   encrypted panel contents or hashes are byte-identical?
7. Is the implementation mechanically dummy/test-seed only? Confirm that no
   real key constructor, OS entropy draw, real panel writer, escrow artifact,
   learner trajectory, scout, lock or outcome path exists.
8. Could a shape-correct or count-correct but scientifically wrong refactor pass
   the tests? Name missing regression tests if so.
9. Does any implementation choice exceed the signed authorization or silently
   reopen an accepted negative destination?

Independently recompute at least the three edge crossings, per-stratum YES
counts, S4 labels, reserved-cell uniqueness, and the exemption count. Do not
infer a missing rule from intent: if two independent implementers can still
produce different bytes, call it blocking.

## Verdicts

Return exactly one:

- `LEVEL1_DUMMY_PANEL_IMPLEMENTATION_ACCEPTED`
- `REVISE_LEVEL1_DUMMY_PANEL_IMPLEMENTATION`
- `BLOCKED_LEVEL1_PANEL_CONTRACT`

Classify findings Critical/Major/Minor with file:line references. State exact
mandatory edits and whether implementation may be committed. Acceptance does
not authorize entropy, real panel generation, feasibility/scout execution,
N3 selection, lock, escrow, learner trajectory or outcome.
