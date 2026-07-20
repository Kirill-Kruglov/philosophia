# Sol Y-line prompt: Officina WP-1/WP-2 hardening confirmation

You are GPT-5.6 Sol, the Y-line reviewer. Work in the local repository
`/home/master/llm_projects/philosophia`.

Review the exact hardening commit `6b6d55d` against its parent review archive
`c6a41b2` and against your governing review
`reviews/sol_officina_wp12_implementation_review.md`. The author has not
authorized WP-3, T activation, real entropy, Q execution, or C execution.

Write your review to
`reviews/sol_officina_wp12_hardening_confirmation.md`. Do not edit any existing
file and do not commit.

## Bounded question

Does `c6a41b2..6b6d55d` close every Critical and Major WP-1/WP-2 blocker you
named, without choosing a deferred WP-3/WP-4/WP-6/WP-9 cell or creating a
production execution surface?

## Required attacks

1. **Durable provenance.** Try the original fixture-copy/reopen laundering
   counterexample and variants: absent metadata, copied/relabelled metadata,
   content mutation, forged `promotable:true`, undeclared paths, symlink escape,
   direct Q/C admission, and taint propagation. Confirm that no public
   constructor can manufacture a store-issued parent or a promotable artifact
   under WP-1/WP-2.
2. **Pause/resume.** Attack exact T-state keys/types/invariants; inactive pause;
   false inactive maintenance; checkpoint-before-ledger; partial append; stale
   checkpoint; suffix deletion; artifact deletion/mutation/substitution; forged
   artifact identity; pause linkage; `resets_e3`; and powered-off E3 expiry.
   Confirm overdue resume cannot yield a work-admitting state before a durable
   review entry.
3. **Validity-first closure.** Exhaust Q and C constructors with strings,
   invalid causes, T/pause labels, invalidity labels, and arbitrary mappings.
   Confirm only the closed C scientific enum can represent a valid scientific
   terminal and every Q journal terminal is typed.
4. **One-shot partition.** Audit every phase transition. Confirm a CLAIMED
   attempt can close before entropy only through a signed-disposition-shaped
   uncharged record; DRAW_ARMED ambiguity can close only as charged invalid;
   every LAUNCHED successor is charged; attempt IDs cannot be reused; and
   deletion/persistence failures are detected by the external registry/head.
   Concrete entropy, alpha spending, and Q numerics must remain absent.
5. **PRF boundary.** Confirm typed domain components are injective for supported
   types/boundaries, booleans are rejected, only the internal dummy factory can
   produce an accepted key, and there is no production/sealed-root type.
6. **Candidate identity.** Confirm only the closed inert-metadata class plus
   provenance commit are removed from behavioral identity; behavior source,
   stack, initialization, optimizer, policy, interface, config, and unknown
   fields remain load-bearing or rejected.
7. **Verifier.** Mutate every governed bootstrap field/type; test import aliases,
   dynamic imports, and unreviewed imports; confirm exact inactive ledger genesis
   including the external head. Note any alias or entropy route still missed.
8. **Scope.** Confirm no finite frame, construct, real T metering, production
   root, Q predicate/cap/alpha, C endpoint, lock, world, candidate, trajectory,
   datum, or outcome was introduced.

Run at least:

```bash
.venv/bin/python -m pytest -q \
  tests/test_officina_bootstrap.py \
  tests/test_officina_governance.py \
  tests/test_officina_accounting.py
.venv/bin/python scripts/verify_officina_wp12.py
git diff --check c6a41b2..6b6d55d
```

Use exactly one leading verdict:

- `OFFICINA_WP12_YLINE_HARDENING_CONFIRMED` if all your closure blockers are
  closed and only explicitly deferred obligations remain; or
- `REVISE_OFFICINA_WP12_HARDENING` with reproducible counterexamples and the
  smallest bounded repairs.

If confirmed, state whether WP-1/WP-2 may be closed and WP-3 may be **drafted
only**. This review never authorizes a real world, entropy, T/Q/C execution,
lock, escrow, or outcome.
