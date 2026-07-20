# Claude Code Opus 4.8 prompt: Officina WP-1/WP-2 implementation review

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

This is a bounded X-line implementation review. It may run non-outcome unit
tests and read-only verifiers. It must not create entropy, real worlds, model
runs, candidate registrations, Q attempts, locks, escrow secrets, or outcomes.

## Required attacks

1. **Quarantine positive and negative paths:** realpath/symlink behavior,
   default deny, T-only immutable fixtures, derived non-promotable provenance,
   old checkpoint warm-start prevention, source-import quarantine, and whether
   same-repo audit ancestry works without runtime predecessor reads.
2. **Bootstrap integrity:** canonical manifests, full predecessor and
   authorization pins, exact allowed file set, inactive envelope, and a
   committed `T_LEDGER.md` that is both empty and parseable by the future
   append-only implementation.
3. **One-shot positive path:** claim -> draw-armed -> launched -> terminal, plus
   draw-armed ambiguity -> charged invalid with competence unset. Look for a
   path to entropy without durable charge, silent retry, redraw, fallback, or
   an uncloseable state. The package must itself draw zero entropy.
4. **Durability:** canonical no-replace/replace primitives, hash-chain ledger,
   concurrent append assumptions, pause checkpoint ordering, prior-ledger-head
   binding, tamper detection, orphan/partial-file behavior, and parent fsync.
5. **Candidate identity/interlocks:** conservative manifest schema, mandatory
   from-scratch initialization, unknown-field behavior, test-only capability,
   and absence of any callable real T/Q/C route.
6. **Scope:** determine whether this is a faithful WP-1/WP-2 implementation or
   whether any module silently implements or selects a WP-3/WP-6/WP-9 cell.

Create exactly one file:

`reviews/opus_officina_wp12_implementation_review.md`

Do not edit existing files or commit. Use exactly one verdict:

- `OFFICINA_WP12_XLINE_ACCEPTED`,
- `REVISE_OFFICINA_WP12_IMPLEMENTATION`, or
- `BLOCKED_OFFICINA_WP12_IMPLEMENTATION`.

Lead with Critical/Major/Minor findings and exact repairs. Distinguish blockers
before WP-3 drafting from later WP-4/WP-6 obligations. State the exact tests and
verifiers run. If accepted, say whether Codex may close WP-1/WP-2 and begin only
drafting the WP-3 population/construct contract, with no real world generation.
