# B2_INSTRUMENT_REPAIR_09 — ticket amendment 2

Date: 2026-08-16
Amends: `B2_INSTRUMENT_REPAIR_09_TICKET_AMENDMENT_1.md`
(SHA-256 `3063b4934cbe04fa7ffbbe62d3aefa2c3dd7e8462ec8ff7806a15fa4029c8ee7`)

**Amendment 1 section A1 is superseded. The runner divergence is downgraded from
a dispatch blocker to a declared divergence. The run may proceed.**

A2 (host = Legion RTX 4060), A3 (CUDA precondition), A4 (budget) and A5 (Sol
static pass) are unchanged.

## B1 — what the three saved runner copies actually contain

Normalising line endings:

| file | line terminators | SHA-256 of LF-normalised content |
|---|---|---|
| `gpu_committee_runner.py` (current) | CRLF | `2214d0e12663f62b3c2a6ba4c3f49cad015e40e33eb39ad3dbabf092a050623b` |
| git HEAD `gpu_committee_runner.py` | LF | `2214d0e12663f62b3c2a6ba4c3f49cad015e40e33eb39ad3dbabf092a050623b` |
| `gpu_committee_runner(new).py` | LF | `4b0951e517b99a708480621d8c9907e7de53127354000051da2c6f601345ea2b` |
| `gpu_committee_runner(new)(1).py` | CRLF | `4b0951e517b99a708480621d8c9907e7de53127354000051da2c6f601345ea2b` |

The transfer returned **no new code**. `gpu_committee_runner.py` is byte-identical
to git HEAD once CRLF is normalised; `(new)(1).py` is a duplicate of `(new).py`.
All three define the same sixteen functions, and
`memory_safe_class_balanced_feasibility_committee_step` is in none of them.

There is no drift to worry about — but the missing function was not captured.

## B2 — the function exists on the Legion; two runs prove it

`b2_path_pilot_08.py` (lines 553, 747) and `capacity_diag_04.py` (line 533) both
`import gpu_committee_runner as runner` and both call
`runner.memory_safe_class_balanced_feasibility_committee_step`. Neither defines
nor monkey-patches it. Both completed successfully on 2026-08-07 —
`capacity_diag_04` left a 6.9 MB checkpoint and a 42 KB run log.

So the Legion holds a `gpu_committee_runner.py` that no repository has, and that
this transfer did not retrieve.

## B3 — why this does not block the run

Every one of the five decision criteria is measured on the **path** stage. None
touches the destination runner.

| criterion | measured on | destination runner involved |
|---|---|---|
| 1. held-out loss monotone | path stage | no |
| 2. `mean_std >= 1.0` at step 600 | path stage | no |
| 3. `road_gap` P0 vs init vs P_shuf | path stage — `b2_instrument_repair_09.py` lines 1444/1450 (P0) and 1534/1539 (P_shuf), all **before** the destination stage | no |
| 4. `delta exact_d` vs matched init | path-stage trunk probes | no |
| 5. M3 on the P0 readout | P0 arm, which has **no destination stage** (`dest_wall_s = 0.0` in pilot 08) | no |

Only the D / P+ / P_shuf floor table depends on the destination learner, and
that table is reported context, not a criterion. It was already declared
non-comparable to pilot 08, whose numbers carry no evidential weight.

**The verdict DONE / KILL / INCONCLUSIVE cannot be changed by which destination
runner is used.**

## B4 — dispatch instruction

Run with `memory_safe_feasibility_committee_step` as the builder implemented it.
Record in `B2_INSTRUMENT_REPAIR_09.md` section 2, verbatim:

> `DESTINATION_LEARNER_DIVERGENCE: class balancing absent; the Legion copy of`
> `gpu_committee_runner.py defining memory_safe_class_balanced_feasibility_`
> `committee_step was not recoverable at dispatch time. D, P+ and P_shuf are not`
> `comparable to pilot 08. Criteria 1-5 are unaffected — all are measured on the`
> `path stage; see amendment 2 section B3.`

Also record the SHA-256 of the runner actually imported, LF-normalised.

## B5 — hygiene, not a blocker

Two items, neither gating this run:

1. **Recover the real Legion runner.** On the Legion:

   ```bash
   grep -rn "def memory_safe_class_balanced" ~ 2>/dev/null
   ```

   Copy the file that matches to `successor/dev/gpu_committee_runner_legion.py`,
   hash it, commit it. **Required before the Stage-2 six-block call**, where the
   destination arm becomes load-bearing. Not required now.

2. **Line endings and duplicates.** `gpu_committee_runner.py` is now CRLF and
   diffs against git as 628 changed lines while being semantically identical.
   Restore it and drop the duplicate:

   ```bash
   git checkout -- successor/dev/gpu_committee_runner.py
   rm "successor/dev/gpu_committee_runner(new)(1).py"
   ```

   Do not commit CRLF copies of tracked files; every future diff becomes
   unreadable.

This is the third instance in two days of executed state existing on exactly one
machine and in no repository — after the `/tmp` wipe and the runner divergence
itself. It is worth one deliberate sweep of the Legion's `successor/dev/` into a
quarantine directory with a `SHA256SUMS` manifest, diffed against the repo, at a
time of the author's choosing.
