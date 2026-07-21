Written to `reviews/opus_officina_wp4_implementation_review.md`.

## Verdict: `OFFICINA_WP4_XLINE_ACCEPTED_FOR_BOUNDED_NEXT_GATE`

A faithful, fail-closed, **inactive** WP-4 world substrate for the signed LOW/C_RICH/OR-2/transport contract. No Critical or Major finding; three Minor observations, none blocking.

**All eight items confirmed:**
1. **Frame** — `SIGNED_CONTRACT_SHA256`/`SIGNED_WP3_SIGNATURE_SHA256` independently match the committed contract/signature; `_validate_frame` recomputes every block from the formula and rejects drift; I recomputed all 20 rows (C `p∈{1,3,5,…,20}`, Q worlds `{28,…,63}`), `|C|=24`, `|Q|=16`, disjoint/covering/excluding; frame JSON canonical and round-trips.
2. **Mutation** — `verify_frame_bytes` rejects mutated (`lambda=141`) and non-canonical payloads by comparing against the *formula-recomputed* bytes (can't bless its own drift).
3. **Classifier** — total, ordered (STRUCTURE→BYTE→LENGTH→answer), stateless, exact. Probed with correct canonical bytes: valid→0/1, joint over-length+illegal→BYTE, illegal-only→BYTE, over-length→LENGTH; NaN/Infinity/BOM/escapes/Unicode/dup-key/non-canonical/missing-newline→STRUCTURE; modular arithmetic correct for negative displacements. *(My first probe's "all STRUCTURE" was a missing trailing newline — the canonical query form; re-probed correctly.)*
4. **Capabilities** — token-gated, exact-typed; direct ctor/duck-type/subclass/out-of-surface-modulus all rejected; the only bypass is the accepted deliberate private-sentinel import (W4-m1), which grants only test-only capability. **No real capability factory exists** (all four real routes raise).
5. **Bounds** — T=`[10,25]∪[166,205]`, |Q|=16, |C|=24, Q∩C=∅; out-of-surface modulus refused.
6. **`record_test_t_contact`** — positive-int (bool excluded), validate→charge→append order, atomic ledger, `test_only:true`; the inactive production state blocks any charge (W4-m2: ledger path not restricted, but protected by NOT_ACTIVATED + labeling + git/verifier).
7. **Stubs** — `generate_real_world`/`run_real_t`/`launch_q`/`execute_c` all raise; no timer, learner loop, activation driver, real capability, or production entry point.
8. **Suite/verifier** — **63 passed**, verifier OK, `git diff --check` clean, committed ledger genesis and bootstrap set unchanged, import allowlist covers `world.py`.

**Minors:** W4-m1 (accepted procedural sentinel bypass grants only test-only eval), W4-m2 (test hook's ledger path unrestricted — real transaction belongs to the future activation driver), W4-m3 (test-only Q/C surfaces are oracle-evaluation utilities, correctly documented, not the deferred realized-unit gates).

**Next gate:** this authorizes **only preparation (drafting) of a separately reviewed T-activation candidate** — the future driver supplying real T-run capability, the activation ledger event, the breathing-check gate, and the durable production transaction — subject to its own bounded X/Y review. It authorizes **no** T activation, real world, entropy, E1/E2/E3 spend, candidate registration, learner run, Q/C process, root, lock, escrow, datum, or outcome; the committed T state stays `NOT_ACTIVATED`.

**Confirmed:** no existing file edited, one new review file, no cell/token selected, T not activated, nothing committed; predecessor stays `OPEN`/`BLOCKED_LEVEL1_FEASIBILITY`, programme claim `OPEN`.
