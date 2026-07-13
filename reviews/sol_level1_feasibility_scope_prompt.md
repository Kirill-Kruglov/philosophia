# Sol review prompt: Level 1 feasibility scientific-scope audit

Audit the **scientific inertness and reporting contract** of the feasibility
implementation at reviewed-code commit
`308aa6fcfd165b1742a1ec4988a660d9a6c21333`. The current HEAD may add review
prompts only; verify the load-bearing source diff from the reviewed commit is
empty.

Read:

- `experiments/level_1_contact/SCIENTIFIC_SPEC_V3_DRAFT.md` §5–§8;
- `experiments/level_1_contact/SCIENTIFIC_SPEC_V3_1_ADDENDUM.md` A6, A8–A10;
- the signed corrections and signature records;
- `scripts/level1_run_feasibility.py`;
- `src/philosophia/level1/{feasibility,interlock,train,pool,panel}.py`;
- `tests/test_level1_feasibility.py`.

The intended check is one development world (`pair_slot=0`, `n=66`), one
RANDOM-STATIC arm, one replicate, `B=2000`, and a scorer-only ACTIVE-path
microbenchmark capped at 200 steps. It is non-comparative and non-citable. The
only learner-performance output is one binary censoring indicator; it may
justify only a signed binary feasibility-floor amendment and may never tune a
threshold, margin, architecture, B, or target solve rate silently.

Please attack these questions:

1. Does any allowed field, projection, dummy-panel result, or timing aggregate
   permit an arm comparison or post-hoc tuning beyond A8?
2. Is `censored_at_b` computed with the signed persistence rule and reported in
   a way that cannot be narrated as a Level 1 result?
3. Is the use of the actual public-root reservation geometry with a test-only
   dummy panel seed statistically and procedurally compatible with “no escrow”?
4. Does selecting the first allocated development pair/lower world (`slot 0`,
   `n=66`) create a scientific interpretation leak, or is it an acceptable
   predeclared feasibility fixture?
5. Are the runtime/artifact projections dimensionally honest, and is any
   omitted resource component large enough to make them misleading?
6. Does the one-shot claim/authorization mechanism prevent repeated peeking,
   including alternate output directories and untracked authorization files?
7. What exact statements are forbidden after a successful or censored check?

Do **not** run the feasibility driver, create authorization/claim/report files,
draw entropy, build a real panel, select N3, or inspect any scientific outcome.
Unit tests and repository verifiers are allowed.

Write the review to `reviews/sol_level1_feasibility_scope_review.md` without
committing it. Lead with exactly one verdict:

- `LEVEL1_FEASIBILITY_SCOPE_CONFIRMED`, or
- `REVISE_LEVEL1_FEASIBILITY_SCOPE`.

Give ordered findings, mandatory edits, an allowed/forbidden interpretation
table, and explicitly answer: **may Codex prepare an authorization candidate,
but not execute it?**
