Wrote the full review at `reviews/sol_level1_gated_implementation_review.md:1`.

**Verdict**
- `REVISE_LEVEL1_GATED_IMPLEMENTATION`

**Blocking edits**
- Restrict `estimate_contrast` to signed outcome sizes `n_h ∈ {4,5,6,7,8}` or split a dev-only helper from the outcome estimator.
- Add tests rejecting `n_h=2/3`.
- Add a hand-computed non-census FPC/Satterthwaite/Bonferroni interval test.
- Keep committee mean aggregation explicitly gated or implement it before any evaluator/trajectory gate.

**Validation run**
- `.venv/bin/python -m pytest tests/test_level1_*.py` — 26 passed.
- `.venv/bin/python scripts/verify_all.py` — passed.
- `.venv/bin/python -m pytest` — 115 passed.
- System `python3 -m pytest ...` failed because `pytest` is not installed for system Python.

No implementation, entropy, panel generation, data, lock, escrow, or outcome artifact was created.
