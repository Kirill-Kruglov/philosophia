# Officina

`officina` is the signed identifier of the Philosophia successor line. This
tree is the only runtime data namespace admitted by WP-1. Repository ancestry
is provenance, not a runtime data source.

Current gate: **WP-1/WP-2 implementation and dummy tests only.** No real T
world, entropy draw, learner, candidate registration, Q attempt, promotion,
scientific lock, escrow, C run, or outcome is authorized.

Files:

- `LINEAGE.json` pins the predecessor and governing signatures.
- `PATH_POLICY.json` declares the deny-by-default data-access policy.
- `T_ENVELOPE.json` records the signed but inactive resource envelope.
- `T_LEDGER.md` is the append-only public ledger skeleton. T is not activated.

All machine-readable JSON files are canonical ASCII JSON with one trailing
newline. Runtime code lives in `src/philosophia/officina/` and must not import
the predecessor `level0` or `level1` packages.
