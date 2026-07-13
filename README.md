# philosophia

[![CI](https://github.com/Kirill-Kruglov/philosophia/actions/workflows/ci.yml/badge.svg)](https://github.com/Kirill-Kruglov/philosophia/actions/workflows/ci.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

*Can experience be made rather than inherited?*

`philosophia` is an open research programme testing whether a derivable world of
algebra and geometry can provide primary experience to a small model trained from
scratch, and whether that experience is real in an operational sense: traceable to
contact, work-reducing, intervention-robust, and transferable across worlds and
representations.

> **Status: bootstrap complete; no Philosophia result yet.** The route and its
> failure conditions are fixed in [`ROADMAP.md`](ROADMAP.md). Line 12's validated
> instrument is inherited with its holdout failure intact. Level 0 has not yet
> been preregistered or run.

## The question

Can a learner acquire structure from active contact with a world that is itself a
derivation, rather than from an internet corpus of other minds' reports? If it
can, does the acquired structure shorten future work, survive interventions, and
transfer from algebraic worlds to geometric duals?

The programme accepts three publishable endings: proof, falsification, or a mapped
boundary. A negative result at a preregistered kill condition is a result, not a
reason to silently redesign the question.

## Research route

1. **Level -1: literature map.** Mark every premise as known, partial, or open.
2. **Level 0: platform replication.** Reproduce grokking on modular addition.
3. **Level 1: contact.** Compare active equality queries with an
   information-matched static corpus.
4. **Level 2: experience.** Separate weights, a truthful ledger, a false ledger,
   and fresh starts across a fixed curriculum of worlds.
5. **Level 2.5: path credit.** Compare answer-only credit with credit for
   invariants that survive the model's own resampled paths.
6. **Level 3: balcony.** Test cross-world compression and hidden-progress
   measures, then write the essay from the signed decisions.

See [`canonical/KILL_MATRIX.md`](canonical/KILL_MATRIX.md) for the current
decision surface and [`canonical/RESULTS_CANONICAL.md`](canonical/RESULTS_CANONICAL.md)
for the only claims this repository presently permits.

## Repository map

- [`ROADMAP.md`](ROADMAP.md) - the locally maintained execution roadmap derived
  from Fable's route to the fourth essay.
- [`inheritance/line13_philosophia_map.md`](inheritance/line13_philosophia_map.md)
  - Fable's original route, copied verbatim from Ascesis and hash-checked in CI.
- [`MANIFEST.md`](MANIFEST.md) - extraction provenance and citability classes.
- [`inheritance/line12_same_wall/`](inheritance/line12_same_wall/) - the certified
  detector lineage, including the primary decision and the adverse holdout.
- [`gate_harness/`](gate_harness/) - fail-closed preregistration and decision
  verifier inherited verbatim.
- [`canonical/`](canonical/) - claim ledger, kills, and citable results.
- [`experiments/`](experiments/) - one independently locked directory per level.
- [`references/`](references/) - literature map and clean-room protocol.

## Verification

Python 3.11+ is required.

```bash
pip install -e ".[dev]"
pytest -q
python scripts/verify_inheritance.py
python scripts/verify_all.py
```

The inherited primary decision must verify `VALID` against the exact vendored
harness. This does **not** make its scientific conclusion universally valid, and
it does not promote scouts or the holdout result into new citable decisions.

## Publication

The essay, browser demo, and GitHub Pages site will be built from canonical
artifacts after the corresponding levels exist. Until then the absence of a
finished public story is deliberate.

## License

MIT - see [`LICENSE`](LICENSE).
