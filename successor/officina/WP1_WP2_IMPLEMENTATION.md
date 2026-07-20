# Officina WP-1/WP-2 implementation contract

Authorization: `successor/AUTHOR_SELECTIONS_V1_SIGNATURE.md`, commit
`d3be92f116ec10580fe28423adaac0c56119b492`.

## Implemented surface

- `philosophia.officina.quarantine`, `provenance`: realpath-first,
  deny-by-default data access; content/path/parent-bound durable provenance;
  T-only hash-pinned engineering fixtures and non-promotable taint propagation.
- `manifest`: conservative behavioral identity with mandatory from-scratch
  initialization, a load-bearing source digest, and a closed inert-metadata list.
- `canonical`, `prf`, `escrow`: canonical ASCII JSON, durable file primitives,
  typed domain-separated test-only PRF, and caller-supplied salted commitments.
- `terminal`, `interlock`, `one_shot`: validity-first result types, explicit
  execution refusal, typed Q/C terminals, and an immutable attempt journal bound
  to an external attempt-id/head registry. Pre-entropy closure requires a signed
  disposition; every draw-armed or launched closure is charged.
- `ledger`, `accounting`, `checkpoint`: append-only hash-chain bound to an
  external head, exact non-coercive E1/E2/E3 state, artifact-recomputing durable
  pause, and an overdue-review gate that blocks resumed work.
- `verification`: canonical bootstrap, governing hashes, inactive T state,
  forbidden runtime imports, and zero entropy calls.

## Test-only boundary

Tests may use deterministic caller-provided keys, temporary repositories,
temporary ledgers, dummy manifests, and dummy state bytes. No test may create or
read a real T/Q/C world, obtain entropy, register a real candidate, run a model,
or create a scientific artifact.

The committed `T_LEDGER.md` and `T_LEDGER.md.head.json` remain a valid empty
ledger at the genesis head with status `NOT_ACTIVATED`. No committed checkpoint,
attempt journal/registry, provenance record, fixture grant, root, or escrow
artifact exists.

## Deferred obligations

WP-3 owns the eight-object finite-frame population/construct contract. WP-4
owns real-T harness timing and process accounting. WP-6 owns the concrete Q
entropy driver, custody, caps, alpha spending, competence rule, stack-family
identity, and breathing-check numerics. None is implemented or defaulted here.

## Verification

```bash
pytest -q tests/test_officina_bootstrap.py \
  tests/test_officina_governance.py tests/test_officina_accounting.py
python scripts/verify_officina_wp12.py
```
