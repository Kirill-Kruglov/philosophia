# Opus 4.8 X-line review: Officina WP-4 inactive implementation

Work in `/home/master/llm_projects/philosophia`. Review the signed WP-3 record
and the WP-4 implementation commits `de8aa1e` and `a8cbd91` at current HEAD.
Read the code and tests, not only the implementation note.

Create exactly one new file:

`reviews/opus_officina_wp4_implementation_review.md`

Do not edit existing files or commit. Create no real world, entropy, candidate,
root, lock, escrow, datum, outcome, or T/Q/C execution. Temporary test-only
fixtures and ledgers are allowed. Do not activate the committed T state.

## Governing files

- `successor/OFFICINA_WP3_SIGNATURE.md`
- `successor/OFFICINA_WP3_POPULATION_CONSTRUCT_CONTRACT_V2_1_DRAFT.md`
- `successor/OFFICINA_WP4_IMPLEMENTATION.md`
- `src/philosophia/officina/world.py`
- `src/philosophia/officina/{interlock,canonical,accounting,ledger,quarantine,verification}.py`
- `tests/test_officina_world.py`

## Review mandate

Take an adversarial implementation/fidelity stance. At minimum:

1. Recompute the signed LOW/C_RICH frame from the contract. Verify all 20 rows,
   exact C/Q memberships, strata, cardinalities, exclusions, canonical schema,
   selected tokens, contract/signature hashes, and golden frame hash.
2. Mutate every frame field and, where useful, monkeypatch internal builders.
   Confirm the generator recomputes from the formula and the verifier rejects
   noncanonical, duplicate-key, reordered/extra/missing, and internally
   inconsistent bytes rather than blessing its own drift.
3. Audit the total raw-wire classifier over arbitrary byte strings: JSON parser
   edge cases, duplicate keys, NaN/infinity, encodings/BOM, escapes, Unicode,
   wrong structures/types, BYTE+LENGTH priority, empty words, exact refusal and
   answer bytes, statelessness, and modular arithmetic.
4. Attack capability issuance and use: direct constructor, duck types,
   subclasses, copied token, altered surface/purpose, raw/private helper import,
   caller-supplied `n`, T contact with frame/reserve moduli, and Q/C test
   capabilities before roots. State clearly whether the accepted accidental-use
   threat model permits any remaining deliberate Python bypass and whether the
   public API honestly has no real capability factory.
5. Audit `_surface_moduli` and every selected support boundary. Confirm T test
   contacts are limited to `[10,25] U [166,205]`, Q to the 16 selected worlds,
   and C to the 24 worlds in 12 selected blocks.
6. Audit `record_test_t_contact`: exact positive-int charge (including bool),
   timestamp/state rules, order of validation/charge/append, failure behavior,
   response/query hashes, event schema, and whether a temporary test ledger can
   be confused with the committed production ledger. It must not be represented
   as a crash-atomic production transaction.
7. Confirm `generate_real_world`, `run_real_t`, `launch_q`, and `execute_c` remain
   fail-closed; there is no timer, learner loop, activation driver, real
   capability, durable real-world registry, or production execution entry point.
8. Run the four-file 63-test Officina suite, `scripts/verify_officina_wp12.py`,
   and `git diff --check`. Confirm the exact bootstrap set and ledger genesis are
   unchanged. Inspect the source-quarantine import allowlist for any bypass.

## Required output

Lead with exactly one verdict:

- `OFFICINA_WP4_XLINE_ACCEPTED_FOR_BOUNDED_NEXT_GATE`; or
- `REVISE_OFFICINA_WP4_IMPLEMENTATION`; or
- `BLOCKED_OFFICINA_WP4_IMPLEMENTATION`.

Then report Critical/Major/Minor findings with file/line anchors, exact mandatory
repairs, checks run, and what next gate (if any) becomes eligible. A positive
verdict may authorize only preparation of a separately reviewed T-activation
candidate; it must not authorize activation, a real world, entropy, or a run.

Preserve the full negative space and make no outcome prediction.

