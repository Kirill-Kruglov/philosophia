# Philosophia extraction manifest

Source repository: `/home/master/llm_projects/ascesis`
Source commit: `8839d5f119350cf87cfbab8b723af214cb54e7c0`
Target repository: `/home/master/llm_projects/philosophia`

The files named below were copied verbatim. Their target-relative hashes are in
[`SOURCE_SHA256SUMS`](SOURCE_SHA256SUMS) and are checked in CI. Generated
Philosophia scaffolding is not represented as inherited evidence.

| Source | Target | Status |
|---|---|---|
| `ontology/lines/13-philosophia.md` | `ROADMAP.md` | programme route; not a result |
| `ontology/lines/12-the-same-wall.md` | `inheritance/line12_same_wall/LINE12_MAP.md` | inherited research record |
| `experiments/12_same_wall/experiment_A/` | `inheritance/line12_same_wall/experiment_A/` | primary harness-valid; holdout boundary preserved |
| `experiments/12_same_wall/scouts/` | `inheritance/line12_same_wall/non_citable/scouts/` | exploratory, explicitly non-citable |
| `gate_harness/` | `gate_harness/` | instrument and verifier |
| `LICENSE` | `LICENSE` | project license |

## Citability rule

Only a `decision.json` written by `gate_harness.runner.run_gate`, verified against
the exact current harness, and admitted by `canonical/RESULTS_CANONICAL.md` may be
cited as a decision of this repository.

The inherited primary decision satisfies the mechanical verifier. It remains a
Line 12 result, not a Philosophia result. `holdout_result.json` is evidence of the
registered holdout outcome but is not a harness decision. Scouts remain
non-citable regardless of whether their numbers are useful for design.

## New trust root

The copied Line 12 `PREREG.lock` names an Ascesis commit. It is retained as
historical provenance and must never be reused to authorize a Philosophia run.
All new gates must be locked in this repository in a commit that is a strict
ancestor of their execution commit.
