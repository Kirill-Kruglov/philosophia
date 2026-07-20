# Officina WP-1/WP-2 implementation contract

Authorization: `successor/AUTHOR_SELECTIONS_V1_SIGNATURE.md`, commit
`d3be92f116ec10580fe28423adaac0c56119b492`.

## Implemented surface

- `philosophia.officina.quarantine`: realpath-first, deny-by-default data access;
  T-only hash-pinned engineering fixtures; non-promotable provenance propagation.
- `manifest`: conservative content-addressed candidate identity with mandatory
  from-scratch initialization and no unknown fields.
- `canonical`, `prf`, `escrow`: canonical ASCII JSON, durable file primitives,
  caller-supplied domain-separated PRF, and caller-supplied salted commitments.
- `terminal`, `interlock`, `one_shot`: validity-first result types, explicit
  execution refusal, and an immutable pre-entropy journal whose ambiguous
  draw-armed recovery is charged with competence unset.
- `ledger`, `accounting`, `checkpoint`: append-only hash-chain, exact cumulative
  E1/E2/E3 state, durable operational pause, and fail-closed resume verification.
- `verification`: canonical bootstrap, governing hashes, inactive T state,
  forbidden runtime imports, and zero entropy calls.

## Test-only boundary

Tests may use deterministic caller-provided keys, temporary repositories,
temporary ledgers, dummy manifests, and dummy state bytes. No test may create or
read a real T/Q/C world, obtain entropy, register a real candidate, run a model,
or create a scientific artifact.

The committed `T_LEDGER.md` remains a valid empty ledger with status
`NOT_ACTIVATED`. No committed checkpoint, attempt journal, fixture grant, root,
or escrow artifact exists.

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
