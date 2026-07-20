# Sol Y-line prompt: Officina WP-1/WP-2 repair confirmation

You are GPT-5.6 Sol, the Y-line reviewer. Work in
`/home/master/llm_projects/philosophia`.

Review only the exact repair diff `fe9a982..bd61cf9`. Its parent commit archives
your `REVISE_OFFICINA_WP12_HARDENING` review and the Opus review. Read both, but
do not reopen cells they explicitly accepted.

Write only a new file:
`reviews/sol_officina_wp12_repair_confirmation.md`. Do not edit or commit any
existing file.

## Exact question

Does `fe9a982..bd61cf9` close the five live counterexample families in your
hardening review without introducing entropy, execution authority, or a
WP-3/WP-4/WP-6/WP-9 choice?

Re-run the original probes, not only the committed tests:

1. **One-shot:** try `record_pre_entropy_disposition` after `DRAW_ARMED` and
   `LAUNCHED`; duck objects/subclasses/contradictory mappings; direct private
   append with an uncharged terminal; malformed commitments; suffix/head/file
   mutation. Confirm replay centrally validates predecessor, event kind, exact
   payload, charge, and canonical `QTerminal`.
2. **Resume:** obtain an overdue gate and try charge, candidate registration,
   ordinary review, repeated gate completion, resume-before-pause,
   pause-before-activation/review, and backdated ledger append. Confirm the
   serialized resumed state itself is pending and rejects work until one
   durable monotone review completion.
3. **Provenance:** repeat token/view copying, `dataclasses.replace`, same-path
   relabel plus re-hash, empty/changed parents, parent deletion, hand-built
   metadata, direct registry mutation, suffix deletion, and Q/C admission.
   Confirm WP-1/WP-2 structurally contain no `promotable=True`, derived writes
   re-read parent paths, and reopen recursively matches the externally headed
   exact registry ancestry.
4. **PRF:** try duck objects, direct construction, copied material/object, raw
   `prf_digest`, `CounterStream`, invalid/bool/out-of-range counters, and typed
   domain collisions. Confirm only an object identity issued by `dummy_key` is
   accepted and that no production/sealed key type exists.
5. **Verifier/genesis:** repeat aliased and reflective entropy, `getattr`,
   dynamic execution/import, system random-device literals, unreviewed imports,
   exact ledger prose/head field/type mutations, and timestamp backdating.

Run:

```bash
.venv/bin/python -m pytest -q \
  tests/test_officina_bootstrap.py \
  tests/test_officina_governance.py \
  tests/test_officina_accounting.py
.venv/bin/python scripts/verify_officina_wp12.py
git diff --check fe9a982..bd61cf9
```

Use exactly one leading verdict:

- `OFFICINA_WP12_YLINE_REPAIR_CONFIRMED`; or
- `REVISE_OFFICINA_WP12_REPAIR`, with one reproducible counterexample and the
  smallest bounded correction.

If confirmed, state that WP-1/WP-2 may close and WP-3 may be **drafted only**.
No real world, entropy, T activation, candidate, Q/C execution, lock, escrow,
datum, outcome, or claim movement is authorized.
