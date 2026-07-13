# Codex correction: Level 1 public-root m3 path closure

Date: 2026-07-14. This corrects only the incomplete m3 claim in
`codex_level1_public_root_review_closure.md`; the historical review and closure
remain preserved.

Opus demonstrated that `config.py` is load-bearing for public allocation:
coherent drift of `DEVELOPMENT_PAIRS_PER_STRATUM` and
`OUTCOME_PAIRS_PER_STRATUM` could change D/roles while satisfying the old
self-referential guard. The bounded repair is:

1. `src/philosophia/level1/config.py` is the sixth
   `REVIEWED_SOURCE_PATHS` entry.
2. It is included in the reachable-module entropy scan.
3. A dedicated temp-repo commit changing only `config.py` must fail preflight
   with `execution source bytes differ`.
4. `derive_public_allocations` independently asserts the literal signed
   cardinalities D=6 (2/stratum) and roles=24 (8/stratum).
5. An in-memory regression reproduces Opus's DEV=1/OUTCOME=9 drift and requires
   the literal-cardinality guard to raise.
6. The staged-path check now compares an exact set plus cardinality, not git's
   output order; its test deliberately supplies reversed name order.
7. `PUBLIC_ROOT_EXECUTION_PROTOCOL.md` names all six paths.

No allocation was generated, no entropy was drawn, and no real one-shot artifact
exists. This correction changes no signed allocation law; it makes that law
independently enforced.

Requested bounded verdict:

- `LEVEL1_PUBLIC_ROOT_DRIVER_CONFIRMED`
- `REVISE_LEVEL1_PUBLIC_ROOT_DRIVER`
