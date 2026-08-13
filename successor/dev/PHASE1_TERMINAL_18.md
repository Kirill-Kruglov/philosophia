# PHASE1_TERMINAL_18

NON-CITABLE Phase-1 close-out. Not an experiment. No scientific claim.

## VERDICT: `EXPLORATORY_FEASIBILITY_OBSERVED__NO_PHILOSOPHIA_CLAIM`

This package closes exploratory MINIMO Phase 1 with an exact counter
repair, deterministic aggregation, and honest provenance. It does not
authorize Phase 2 and does not make a scientific Philosophia claim.

Authoritative evaluation inputs are the five Phase-17 JSON files under
`successor/dev/phase1_extrinsic_17/`. The training run is
`minimo/learning/outputs/2026-08-10/00-14-33`, a repository-default
CPU-debug MINIMO realization. Lenovo Legion runs `2026-08-09/23-57-05`
and `2026-08-10/07-27-05` are excluded as
`STOPPED_PERFORMANCE_FEASIBILITY` and are not Phase-16/17 evidence.

Every Phase-17 record made one MCTS invocation under `max_searches=1`.
The legacy field stored zero-based loop index `i`; exact entered MCTS work is
therefore reconstructed as `raw+1` for every item, including `7999 -> 8000`.
This counts entered search-loop iterations, not necessarily newly expanded leaves.
This changes absolute means and two mean savings slightly, but not the
direction, solved counts or paired sign counts. No bootstrap interval,
p-value, or theorem-population inference is emitted.

This report supersedes the broad Phase-17 sentence "the phenomenon is
real" and its bootstrap-CI interpretation. Historical file
`PHASE1_EXTRINSIC_17.md` is not rewritten or deleted.

## Computed table

| ck | solved | restricted mean | saving vs ck0 | positive/negative/tie |
|---:|---:|---:|---:|---:|
| 0 | 11/30 | 5257.833333 | 0.000000 | 0/0/30 |
| 1 | 20/30 | 4374.966667 | 882.866667 | 19/1/10 |
| 2 | 11/30 | 5168.000000 | 89.833333 | 8/3/19 |
| 3 | 11/30 | 5254.233333 | 3.600000 | 8/3/19 |
| 4 | 13/30 | 4916.133333 | 341.700000 | 9/5/16 |

## Terminal reading

> In one unseeded repository-default CPU-debug MINIMO realization, the post-hoc
> checkpoint after one self-training iteration reduced capped proof-search work
> on the fixed 30-item Kleene panel relative to checkpoint zero. This is a
> property of saved artifacts, not an estimate of a theorem population,
> training-seed stability, monotone self-improvement, ACTIVE versus YOKED, or a
> general Philosophia effect.

## Input hashes

- `/home/master/llm_projects/philosophia/successor/dev/phase1_extrinsic_17/checkpoint_0.json`: sha256 `8c264cc2b1e219b02fca5d2c79d6bef3bdcdc9667e7a47cb16c98d0035bdffe3` (6275 bytes)
- `/home/master/llm_projects/philosophia/successor/dev/phase1_extrinsic_17/checkpoint_1.json`: sha256 `92ec290830544939f3aba49910e1ecace96bf43745328aa041093440f82189a1` (6431 bytes)
- `/home/master/llm_projects/philosophia/successor/dev/phase1_extrinsic_17/checkpoint_2.json`: sha256 `c0dc9c23b8dbb9854d0484d049a163d0743ce599261d585ac311e31153bc56a2` (6285 bytes)
- `/home/master/llm_projects/philosophia/successor/dev/phase1_extrinsic_17/checkpoint_3.json`: sha256 `c6eb9ee658aecdfd421b4fdde677c6e476bb0099aa054b3369cb617df834839c` (6286 bytes)
- `/home/master/llm_projects/philosophia/successor/dev/phase1_extrinsic_17/checkpoint_4.json`: sha256 `1d60aca077999bf67135fd8adfe32af660d364fe2c00b2a2ad3dde200278262c` (6309 bytes)

## Bounded action-order probe

Status: `ORDER_VARIATION_OBSERVED`; distinct ordered-sequence hashes: `8` across `8` fresh workers.

Phase-17 evaluation is not demonstrated fresh-process invariant.
Peano enumeration order is a demonstrated candidate mechanism, not
an established sole cause. Phase 2 must canonicalize unique action
identities before constructing children.
