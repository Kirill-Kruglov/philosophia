# Officina executable-contract migration charter v1 — X review

You are Claude Code Fable 5, independent X-line reviewer. Work read-only in
`/home/master/llm_projects/philosophia` at commit `9e93df5`.

Review exactly these bytes:

```text
e9f9f641adec0d826f3c974f2e2e6ec14d184758ce933457b1949e9e7b9cd3f9  successor/OFFICINA_EXECUTABLE_CONTRACT_MIGRATION_CHARTER_V1_DRAFT.md
879d9c34aba2d8ff57c45e1fc1a29978bac627d672912b7a637a08eda8bf7d36  reviews/fable_officina_executable_contract_migration_charter.md
```

Recompute both hashes. Treat the memo as untrusted author self-assessment. Do
not modify charter/history/code/tests/signatures/runtime artifacts or unrelated
work. Do not commit. Create exactly one review file.

This is an architecture review, not another W-B clause review. Do not reopen
signed science, run processes, design v2.16, or demand copied historical prose.

## Questions

### X1 — independent semantic oracle

The charter proposes generating both the ordered state machine and guard-row
predicates from one declaration. Decide whether this destroys the independence
that caught earlier ambiguity. Specify the smallest architecture that retains a
real independent oracle without creating another live prose authority.

Evaluate at least:

- canonical machine implementation plus independently hand-written test oracle;
- declarative transition table plus independently coded evaluator;
- one generated projection plus one M4-only disposable transcription from
  generated documentation.

Recommend one. Pin what is live authority, what is test-only, and how drift is
detected without duplicating governing facts.

### X2 — unresolved KG-2 enumeration semantics

The v2.15 confirmation exposed two readings producing 4 vs 6 writes while both
retained safety. The migration must not silently inherit ambiguity. Determine
whether M2 must adopt one reading now, expose a bounded author choice, or encode
the route relation so counts are derived without a prose forcing rule.

Require the dimension set itself to be a reviewed executable object. State the
exact gate that detects a missing dimension.

### X3 — template theorem and crash-cut boundary

Attack the theorem that Class-B drift is impossible in a green tree:

- Can `render.py` or templates contain hand-typed counts, digests, paths,
  generation identifiers or authority claims?
- Is an AST/token guard sufficient? Define the forbidden literal classes and
  how legitimate protocol constants are distinguished.
- Can generated Markdown introduce authority that source does not encode?
- What happens if M3 crash-cut tests reveal defects in existing `canonical.py`,
  which M3 cannot edit?

Recommend a fail-closed route: recording an M6 blocker versus expanding M3.

### X4 — complexity budget and semantic completeness

Assess whether 2,500 authoritative LOC/120 KiB is a credible budget for
I-1..I-15 while existing implementation remains outside contract scope. Decide
whether the budget should count tests, oracle code, data and generator templates
separately. Identify any missing invariant that M6 would necessarily need.

## Verdict discipline

Return `REVISE` only for a structural hole that can recreate the prose loop,
make semantic equivalence untestable, or make a gate impossible. Give bounded
replacement text/decisions rather than a new charter. Minor wording is logged.

Write exactly `reviews/fable_officina_migration_charter_v1_x_review.md` and emit:

- `OFFICINA_MIGRATION_CHARTER_V1_X_ACCEPTED_FOR_BOUNDED_REVISION`
- `REVISE_OFFICINA_MIGRATION_CHARTER_V1`
- `BLOCKED_OFFICINA_MIGRATION_CHARTER_V1`

Report verdict, path/SHA-256, X1-X4, mandatory edits, negative space and exact
next boundary. No token is authorized by this review. `T = NOT_ACTIVATED`;
`OR-3..OR-11 NOT AUTHORIZED`; claim = `OPEN`.
