# GPT-5.6 Sol prompt: Officina WP-1/WP-2 implementation review

Work in `/home/master/llm_projects/philosophia` at commit `2de1df5`
(`Implement Officina WP-1 and WP-2`). Review the exact diff
`d3be92f..2de1df5` against the signed authorization.

Read, at minimum:

1. `successor/AUTHOR_SELECTIONS_V1_SIGNATURE.md`
2. `successor/officina/*`
3. `src/philosophia/officina/*.py`
4. `tests/test_officina_*.py`
5. `scripts/verify_officina_wp12.py`
6. `.github/workflows/ci.yml`, `pyproject.toml`, and the bounded X/Y selection
   reviews that supplied the WP obligations

This is a bounded Y-line statistical/governance implementation review. It may
run non-outcome unit tests and read-only verifiers. It must not create entropy,
real worlds, model runs, candidate registrations, Q attempts, locks, escrow
secrets, or outcomes.

## Required checks

1. **Validity-first types:** invalid Q leaves competence unset; invalid C leaves
   all scientific fields unset; no process/pause state can become censoring,
   equivalence, boundary, or `INSUFFICIENT`.
2. **Q launch accounting:** verify the immutable journal implements the
   exhaustive pre-entropy/no-charge versus first-byte-and-after/charged split,
   including the ambiguous draw-armed recovery. Check hash chains, transition
   totality, retry/reset paths, and whether caller-supplied PRF can be mistaken
   for an authorized entropy source.
3. **T accounting:** audit integer units, additive concurrency semantics,
   E1-crossing and post-exhaustion behavior, E2 uniqueness/cap, conservative
   candidate identity, E3 elapsed-calendar and device clocks, early-review
   gaming, maintenance pause, resume, author stop, and no-off-time E1 accrual.
4. **Information boundary:** fixtures and breathing-check scaffolding remain
   engineering-only and non-promotable; nothing implemented can set competence
   numerics, population values, scientific endpoints, treatment contrasts, or
   sample size.
5. **Canonical/durable artifacts:** reject NaN/noncanonical JSON and tampering;
   assess ledger/checkpoint transactions and whether a crash can silently erase
   resource use or manufacture a valid resume.
6. **Statistical scope:** confirm finite-frame is only a selected type and no
   frame/sample/weight value exists; `T` is `NOT_ACTIVATED`; implementation and
   tests contain no scientific datum.

Create exactly one file:

`reviews/sol_officina_wp12_implementation_review.md`

Do not edit existing files or commit. Use exactly one verdict:

- `OFFICINA_WP12_YLINE_ACCEPTED`,
- `REVISE_OFFICINA_WP12_IMPLEMENTATION`, or
- `BLOCKED_OFFICINA_WP12_IMPLEMENTATION`.

Lead with Critical/Major/Minor findings and exact repairs. Distinguish blockers
before WP-3 drafting from cells correctly deferred to WP-3/WP-4/WP-6. State the
exact tests and verifiers run. If accepted, say whether Codex may close
WP-1/WP-2 and begin only drafting WP-3, with no real world generation.
