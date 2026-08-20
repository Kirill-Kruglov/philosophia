# B2_INSTRUMENT_REPAIR_09 — driver disposition of the static audit

Date: 2026-08-16
Status: `PRE_FIX_RUN_RETAINED_AS_DIAGNOSTIC__CLEAN_RERUN_REQUIRED_FOR_VERDICT`

Inputs:

| file | SHA-256 |
|---|---|
| `B2_09_AUDIT_SOL_STATIC.md` | *(as emitted; token `B2_09_STATIC_AUDIT=DEFECT`)* |
| `B2_09_AUDIT_SOL_RESPONSE.md` | `f79a8f23fd02b57671fa9bfe9af8d0ab2fc88e47219312d2187ca87608f0ed27` |
| `b2_instrument_repair_09.py` | `f5b23a9026111870d6cc93b858b807868f2fd072bbbcfab0802213cc4bb0a2e6` |

All three defects are accepted as stated. Sol's per-defect "rerun required" is
correct against the ticket's written invariants. This disposition asks a
narrower question the audit was not asked: **which of the five decision criteria
does each defect actually void in the run now executing?**

## 1. Criterion impact

| criterion | measured | defect 1 (held-out vs K-set) | defect 3 (length ruler) | defect 7 (conditional branch) |
|---|---|---|---|---|
| 1. held-out loss monotone | path stage | clean — path exclusion is asserted at lines 265-276, 797, 861-864, and destination runs strictly after | — | only if branch fires |
| 2. `mean_std >= 1.0` @600 | path stage, pre-fix, trunk surface | clean | — | only if branch fires |
| 3. `road_gap` P0 vs init vs P_shuf | path stage | clean | **VOID** | — |
| 4. `delta exact_d` vs matched init | arm-local init, P0 has no destination stage | clean (item 4 `OK`) | — | — |
| 5. M3 on P0 readout | P0, `dest_wall_s = 0.0` | clean | — | — |

**Defect 1** breaches the ticket's written "excluded from every training batch,
for every arm" invariant, and Sol is right to flag it. But every criterion is
read on the path stage, and destination training runs strictly afterwards, so no
criterion number in this run is corrupted by it. What it can contaminate is the
D / P+ / P_shuf floor table — already declared non-comparable under amendment 2.
It must be repaired before any run whose verdict is load-bearing.

**Defect 3 voids criterion 3 outright.** `align_same` is averaged over one
length mixture and `align_diff` over another, and their difference is taken
unconditionally. Left-padding makes length roughly affine in `|d|` and ~85%
separable, which is precisely why the matched-`|d|` control was required in the
first place. There is no post-hoc rescue: per-pair cosines are not emitted.

**Defect 7 bites only if the branch fires**, and it likely will. The working
hypothesis behind this whole ticket is that the variance hinge is pinned near
its maximum — `25 * var ≈ 15-18` implies per-dimension `std` well under 1, hence
`mean_std < 0.5`. If it fires, pre-fix `mean_std` is a 128-dim trunk statistic
and post-fix is a 256-dim BN-projector statistic, both tested against the same
literal `0.5`; and the two attempts draw different held-out words because
`run_tag` enters the stream domain at lines 1855-1860.

## 2. Consequence for the run in progress

With criterion 3 void, "criteria 1-4 all pass" cannot be established. By the
ticket's own table both `DONE` and `KILL` require that conjunction, so the
executing run **cannot produce either**. Its only reachable verdict is
`INCONCLUSIVE`.

That is not a reason to discard it. Criteria 1, 2, 4 and 5 remain clean in the
pre-fix attempt, and criteria 1 and 2 are exactly the collapse diagnosis this
ticket was written to obtain:

- does the VICReg objective descend at all on a fixed held-out batch;
- is `mean_std` below 1, and below 0.5.

Those two numbers decide whether the BN-projector repair is warranted, and they
cost nothing further — the GPU time is already spent.

**Decision: retain the pre-fix attempt as a diagnostic. Discard the post-fix
attempt if the branch fires.** Do not let post-fix numbers enter any table: under
defect 7 they are measured on a different surface, over different held-out
words, against a threshold calibrated for the other surface.

Preferred, if the process can still be reached: stop after the pre-fix attempt
completes and before the conditional rerun starts, saving ~45 min of GPU. If it
cannot be reached cleanly, let it finish and mark every `post_fix` row
`DISCARDED_DEFECT_7` in the report.

No verdict prompt is dispatched against this run. Opus 5 stays on hold.

## 3. Repair scope for the clean rerun — dispatch 2 of 2

Four items. Nothing else changes; the frozen constants, arms, world, panel,
floor, scoring and the kill/done table are untouched.

**S1 — held-out disjoint from the K-set (defect 1).** Build each seed's K-set
*before* its held-out set, pass the union of K-set words as forbidden input to
`build_heldout_batch`, and assert disjointness fail-closed before any arm
trains. Extend `destination_train_with_checkpoints` to accept and assert the
exclusion set rather than leaving it untested.

**S3 — length-matched `road_gap` (defect 3).** Record the target length of every
equal-displacement held-out pair; generate its different-displacement comparator
at that exact length; assert pairwise equality of the two length sequences
before evaluation. `road_gap` then contrasts displacement at fixed length, which
is what criterion 3 was written to read.

**S7 — one surface, one held-out set across both attempts (defect 7).**
Domain-separate the held-out stream by seed only; drop `run_tag` from the stream
domain so pre-fix and post-fix see byte-identical held-out words. Define the
collapse statistic on the pre-projector trunk in both attempts, label the
surface explicitly in the report, and use only that statistic for the `0.5`
trigger and the persistence test. The objective's own components stay on the
objective's surface.

**S2b — arm the firewall (from Sol's item 2, marked `OK`).**
`_assert_path_clean("road_gap")` at line 531 inspects no kwargs and is vacuous;
line 408 checks only the harmless `n`. Sol's clean verdict came from tracing the
reachable call graph, not from these guards. Pass the actual arguments so the
assertion tests something. This changes no number today — it is the guarantee
criterion 3 leans on tomorrow.

## 4. Budget and escalation

The ticket allowed two dispatches. The repair rerun is dispatch 2. Per operating
rule 4, if the rerun does not yield a clean reading of criteria 1-5, the matter
escalates to the author rather than a third round.

Sequence: builder implements S1/S3/S7/S2b and reruns → Sol's numeric pass (items
5 and 8, plus re-verification of 1, 3, 7) → Opus 5 verdict.

## 5. What this episode establishes

The static audit was dispatched while the GPU was busy and cost no schedule
time. It caught a defect that would have made criterion 3 unreadable and a
second that would have made the collapse threshold incomparable to itself. Both
would otherwise have surfaced only after the verdict was written on them.

The ordering — audit the instrument before reading its numbers — is what the
whole ticket exists to establish, and it just paid for itself.
