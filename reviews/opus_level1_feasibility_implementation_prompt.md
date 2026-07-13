# Opus review prompt: Level 1 feasibility implementation

Review the **implementation only** at reviewed-code commit
`308aa6fcfd165b1742a1ec4988a660d9a6c21333`. The current HEAD may contain this
prompt and other review-only files; first verify that the reviewed source bytes
are unchanged from that commit.

Read the governing contract in:

- `experiments/level_1_contact/SCIENTIFIC_SPEC_V3_DRAFT.md` §5;
- `experiments/level_1_contact/SCIENTIFIC_SPEC_V3_1_ADDENDUM.md` A3, A5, A8, A10;
- corrections through `SCIENTIFIC_SPEC_V3_1_4_1_PANEL_CORRECTION.md`;
- `SCIENTIFIC_SPEC_SIGNATURES.md` and `PANEL_CONTRACT_SIGNATURE.md`.

Audit these load-bearing files:

- `scripts/level1_run_feasibility.py`;
- `src/philosophia/level1/{feasibility,interlock,train,pool,panel,model,acquisition,config,serialization,scoring,world}.py`;
- `tests/test_level1_feasibility.py` and the inherited Level 1 tests.

The intended scope is exactly one development world (`pair_slot=0`, `n=66`),
one RANDOM-STATIC arm, one replicate, `B=2000`, plus at most 200 scorer-only
ACTIVE-path timing steps. The only persistent measurement artifact may contain
latency aggregates, peak memory, projected wall time, artifact sizes, finiteness
flags, panel computability, and one single-arm censoring bit. It must contain no
query/loss/solve series, second arm, contrast, N3 selection, real panel, escrow,
lock, or decision.

Please independently check:

1. A3 raw-pool realization, four slots, duplicate and `d=0 / u=v` rejection,
   flat-index mapping, and RANDOM-STATIC without-replacement schedule.
2. The online update order, one shared replay minibatch across all four members,
   and whether the capability counts oracle steps rather than member updates.
3. Five-checkpoint persistence including step 0, non-finite routing, the binary
   censoring result, and the in-memory checkpoint-size payload.
4. The scorer microbenchmark: exact `S=512`, `E=4`, no mutation, discarded
   choices, and whether its timing boundary is an honest A8 measurement.
5. Dummy-panel separation: real public reservation geometry plus a declared
   test-only panel seed must remain development-only and must not weaken the
   future real-panel escrow boundary.
6. The 12-hour shared wall, exact caps, canonical output path, tracked
   authorization/transcript checks, source-byte pin, durable pre-run claim, and
   no-retry behavior.
7. Whether the tests could distinguish a shape-correct but trajectory-wrong or
   contamination-prone implementation.

Do **not** run `scripts/level1_run_feasibility.py`, create an authorization,
create/delete a claim/report, draw entropy, build a real panel, or execute any
scientific trajectory. Running unit tests and verifiers is allowed.

Write the review to `reviews/opus_level1_feasibility_implementation_review.md`
without committing it. Lead with exactly one verdict:

- `LEVEL1_FEASIBILITY_IMPLEMENTATION_CONFIRMED`, or
- `REVISE_LEVEL1_FEASIBILITY_IMPLEMENTATION`.

List Critical/Major/Minor findings, mandatory edits, exact execution guards a
future authorization must bind, and the negative space. Explicitly answer:
**may Codex prepare an authorization candidate, but not execute it?**
