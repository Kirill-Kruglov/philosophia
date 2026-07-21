# Opus 4.8 X-line: Officina WP-4 descriptor/use-time confirmation

Work in `/home/master/llm_projects/philosophia`. Review only repair commit
`c359aa4` against archived-review commit `b9e2ed3`. Sol's two exact residual
counterexamples govern this round; do not reopen accepted WP-3 design. The
load-bearing diff is `b9e2ed3..c359aa4` and contains four files.

Create exactly one new file:

`reviews/opus_officina_wp4_anchor_confirmation.md`

Do not edit existing files or commit. Do not prepare or execute a T-activation
candidate. Use temporary fixtures only; committed T must remain pristine and
`NOT_ACTIVATED`.

## Exact bounded confirmation

1. Independently reproduce valid ledger/head substitution after harness
   issuance. Audit the held directory/file descriptor lifetime, close behavior,
   path-to-anchor comparison, protected-alias checks, and full integrity checks.
2. Prove the object opened by `AppendOnlyLedger.append` is the anchored ledger,
   not merely a pathname that matched earlier. Confirm rejection happens before
   mutation when the harness check is deliberately bypassed.
3. Audit the atomic-head handoff: old descriptor retained until its successor is
   opened and verified; two legitimate sequential contacts must work; failure
   must leave no falsely advanced in-memory state.
4. Re-run Q/C/TEST relabel attacks via `object.__setattr__`. Confirm the
   use-time T-only invariant is checked before classification and that no invalid
   surface falls through to C membership.
5. Recheck frame hash, classifier/oracle behavior, fail-closed real entry points,
   artifact non-promotion, committed genesis, and source quarantine for
   regression. Run targeted 69 tests, full pytest, and the inactive verifier.

Lead with exactly one verdict:

- `OFFICINA_WP4_DESCRIPTOR_USE_XLINE_CONFIRMED`; or
- `REVISE_OFFICINA_WP4_DESCRIPTOR_USE_REPAIR`; or
- `BLOCKED_OFFICINA_WP4_DESCRIPTOR_USE_REPAIR`.

Report only residual findings in this bounded delta. A positive verdict may
authorize only preparation of a separately reviewed T-activation candidate. It
authorizes no activation, real world, entropy, E1/E2/E3 spend, registration,
learner run, Q/C activity, or claim movement.
