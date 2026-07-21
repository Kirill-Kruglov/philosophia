# GPT-5.6 Sol Y-line: Officina WP-4 descriptor/use-time confirmation

Work in `/home/master/llm_projects/philosophia`. Review only repair commit
`c359aa4` against the archived counterexamples at commit `b9e2ed3`. The exact
load-bearing diff is `b9e2ed3..c359aa4` and contains four files.

Create exactly one new file:

`reviews/sol_officina_wp4_anchor_confirmation.md`

Do not edit existing files or commit. Do not prepare or execute a T-activation
candidate. Use temporary fixtures only; committed T must remain pristine,
`NOT_ACTIVATED`, and byte-identical.

## Exact bounded confirmation

1. Re-run the valid post-issuance ledger/head replacement from Major 1. Confirm
   the harness now retains open root/ledger/head descriptors, so unlink/recreate
   cannot reuse the anchored inode while the descriptor is held and pathname
   substitution fails use-time identity validation.
2. Confirm `AppendOnlyLedger.append` compares the descriptor actually opened
   for writing against the retained ledger descriptor before lock, parse, write,
   or head replacement. Directly bypass the harness precheck with a substituted
   valid ledger and confirm refusal without byte mutation.
3. Confirm legitimate atomic head replacement remains usable: the old head
   descriptor stays open until the new head is opened, path-bound, and checked
   against the ledger; only then is the harness anchor advanced. Exercise at
   least two sequential valid contacts and a later substitution.
4. Attack root/ledger/head deletion, rename/recreate, symlink, hard-link,
   descriptor closure, malformed-but-same-path content, duck/subclass harness,
   and post-close use. Report any route that reaches evaluation, charge, or
   append after identity loss.
5. Re-run Major 2 exactly: mutate an issued T capability with
   `object.__setattr__` to Q, C, and TEST. Confirm `_require_world_capability`
   refuses each at every consumer before query classification or modulus lookup,
   and `_surface_moduli` has no fallthrough-to-C case.
6. Confirm the four-file repair moves no WP-3 scientific cell or future root
   design. Run the 69-test targeted suite, full pytest, and inactive verifier;
   compare the committed envelope/ledger/head before and after.

Lead with exactly one verdict:

- `OFFICINA_WP4_DESCRIPTOR_USE_YLINE_CONFIRMED`; or
- `REVISE_OFFICINA_WP4_DESCRIPTOR_USE_REPAIR`; or
- `BLOCKED_OFFICINA_WP4_DESCRIPTOR_USE_REPAIR`.

Report only residual findings within these two counterexamples. A positive
verdict may authorize only preparation of a separately reviewed T-activation
candidate. It authorizes no activation, real world, entropy, E1/E2/E3 spend,
registration, learner run, Q/C activity, or claim movement.
