# Sol confirmation — Level 1 gated implementation

Verdict: `LEVEL1_GATED_IMPLEMENTATION_CONFIRMED`

This is a bounded confirmation of the prior Sol implementation findings in
`reviews/sol_level1_gated_implementation_review.md` and their closure in
`reviews/codex_level1_implementation_review_closure.md`. It does not reopen
accepted design choices and does not authorize any scientific execution gate.

## Findings

### Critical

None. The prior blocking implementation findings are closed.

### Major

None. The current implementation is acceptable as gated implementation code.

### Minor

- The committee aggregation helper is intentionally a pure tensor helper; it does
  not create a sealed evaluator, checkpoint scorer, or trajectory path.
- Later gates still need reviewed drivers for public-root entropy, real panel
  generation, feasibility/scout execution, N3 selection, lock, escrow, trajectory,
  and outcome.

## Closure checks

1. **Outcome sample sizes.** `estimate_contrast` now rejects unregistered
   stratum counts outside `4..8` at `src/philosophia/level1/inference.py:70`.
   Tests reject `n_h=2` and `n_h=3` at
   `tests/test_level1_acquisition_inference.py:75`.

2. **Non-census FPC anchor.** The hand anchor at
   `tests/test_level1_acquisition_inference.py:81` independently pins estimate
   `20`, variance `13.88888888888889`, Satterthwaite df `6`,
   Bonferroni half-width `12.2516220070524`, and the finite-population label.
   This covers the FPC and df path in `src/philosophia/level1/inference.py:75`
   through `src/philosophia/level1/inference.py:94`.

3. **Committee aggregation.** `committee_equal_probability` requires exactly
   four models, evaluates under `torch.no_grad`, checks shape compatibility, and
   returns the exact arithmetic mean at `src/philosophia/level1/model.py:176`.
   Tests pin exact mean, no gradient, and rejection of three members at
   `tests/test_level1_model_scoring.py:41`. No evaluator or trajectory surface is
   introduced.

4. **Optimizer order.** The AdamW decayed and non-decayed group construction is
   unchanged at `src/philosophia/level1/model.py:200`. Tests now pin the exact
   parameter identities and group order at `tests/test_level1_model_scoring.py:65`.

5. **Gate surface.** Static inspection found no new OS entropy, real panel,
   feasibility/scout, N3 lock, escrow, or outcome path. The only trajectory API
   remains the deliberate fail-closed `run_level1_trajectory`.

## Tests run

- `.venv/bin/python -m pytest tests/test_level1_acquisition_inference.py tests/test_level1_model_scoring.py`
  — 16 passed.
- `.venv/bin/python -m pytest` — 122 passed.

## Signature and gate boundary

This confirmation authorizes only accepting/committing the reviewed gated
implementation. It does not authorize the public-root draw, real panel
generation, feasibility/scout execution, N3 selection, lock, escrow, learner
trajectory, scientific data, or outcome.
