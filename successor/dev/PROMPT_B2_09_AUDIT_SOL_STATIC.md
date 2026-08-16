# PROMPT — B2_INSTRUMENT_REPAIR_09 — static code audit (Codex GPT 5.6 Sol, high)

ROLE: adversarial static audit of instrumentation **source code**, before its
numbers exist. Self-contained; no other prompt or amendment is needed.

## Why you are being asked again

You already returned `B2_09_NUMBERS_TRUSTWORTHY=YES` on
`B2_09_AUDIT_SOL_RESPONSE.md` (SHA-256 `f79a8f23…`). That verdict was correct and
honest: the run had stopped at `STOP_NO_CUDA`, so no number existed to be wrong.
It was also empty for our purpose, and that is the dispatcher's fault, not
yours — the static half of the audit was written in a ticket amendment that was
not sent with your prompt.

Two of your findings were static and stand: **item 6** (constants at lines 93-109
match pilot 08; optimised `vicreg_pair_loss` unchanged) and the source half of
**item 5** (lines 566-580 and 583-606 algebraically identical). Do not redo
those.

This pass covers the six items that were answered "no number emitted" and one
new item.

## Absolute rule for this pass

> Every item below is answerable from source code alone. **"No number was
> emitted", "not produced", or "cannot be checked until the run completes" is
> not a valid answer to any item here.** If you cannot decide an item from the
> code, say which specific line or fact you would need, and mark it
> `UNDECIDABLE_FROM_SOURCE` — not `NO_FINDING`.

A run is in progress on the GPU host as you read this. Its numbers will land
against whatever this code does. Three of the five decision criteria depend on
the items below.

## Read

| file | SHA-256 |
|---|---|
| `successor/dev/b2_instrument_repair_09.py` | `f5b23a9026111870d6cc93b858b807868f2fd072bbbcfab0802213cc4bb0a2e6` |
| `successor/dev/b2_path_pilot_08.py` | `d5099d56ec78911a8dfb451a94d34350a3b8060fe90a0d05687edcc458f1c03f` |
| `successor/dev/B2_INSTRUMENT_REPAIR_09_TICKET.md` | `b8759ebdd7743239bf97238394cb267c091382469ac10dfc4308b5b53670cc85` |
| `successor/dev/B2_PATH_VS_DESTINATION_DESIGN_V2.md` | `160726a6c06fed20b5aa554449c3f14c03f45b9ee52cdcf1ca49ff49ce238dd2` |

Diff the two scripts and read the diff.

## Items

**1. Held-out contamination (R2).** The frozen evaluation words must be excluded
from every training batch, for every arm and both seeds. Trace it in code: where
is the held-out set built (`HOLDOUT_PAIRS`, ~line 408), where is
`exclude_words` threaded, and is exclusion **asserted** or merely intended? Does
the `P_shuf` arm, which reshuffles pairing across groups, re-admit held-out
words? Does exclusion survive the section-3 conditional rerun?
This decides criterion 1, the only curve the ticket allows to be read for
convergence.

**2. Firewall breach in the new metrics (R3).** `road_gap` and the held-out
builder must read token counts and exact-displacement sameness only. Follow every
call reachable from `road_gap_metric` (~line 525) and the held-out builder: does
any of them read `modulus`, `n_mod`, residue, fold, oracle, panel or truth —
directly or through a helper? Is `_assert_path_clean` armed on each of these
sites, or was it called with arguments that make it vacuous?

**3. Length ruler in `road_gap` (R3).** Are the `different displacement` pairs
length-matched against the `equal displacement` pairs? If not, `road_gap`
measures word length. The design already records that left-padding makes length
an affine function of `|d|`, ~85% separable, which is why Opus C3a required the
matched-`|d|` control. Show the code path that matches lengths, or state that
none exists.

**4. Init baseline mismatch (R4).** For each arm, is the `init` probe taken on
the same weights that arm actually starts from — same seed, same construction —
or is one arm's init reused for another's delta? Check `rg_init` at ~1444 (P0)
and ~1534 (P_shuf), and the mechanism-probe init path. A mismatched baseline
voids every `delta_*` and criterion 4.

**7. Conditional-fix discipline (section 3 of the ticket).** In code, is the
BN-terminated projector the *only* thing the conditional branch changes? Are
`(INV, VAR, COV) = (25, 25, 1)` untouched on that path? Is `mean_std` measured on
the same surface pre-fix and post-fix — both pre-projector or both
post-projector? A surface change across the fix makes the 0.5 collapse threshold
non-comparable to itself.

**9. Destination learner.** Pilot 08 calls
`runner.memory_safe_class_balanced_feasibility_committee_step`; repair 09 calls
`runner.memory_safe_feasibility_committee_step`. Confirm that this is the only
behavioural difference at the two destination call sites, that nothing else rode
along with the edit, and that no path-stage code path was touched by it.
Context, which you may rely on: the class-balanced symbol exists in no copy of
`gpu_committee_runner.py` available here, and the divergence is accepted and
declared. You are checking that it is *contained*, not whether it is allowed.

## Out of scope

The design of the path objective, VICReg as a choice, the arm set, the panel,
the strata, the floor, M3's thresholds, whether the result will be interesting.
No new metric, arm, sweep or experiment. Do not suggest raising `M_PATH` or
adding an auxiliary head.

## Output

Write to `successor/dev/B2_09_AUDIT_SOL_STATIC.md`. Never `/tmp` — it is volatile
on this machine and was wiped on 2026-08-15.

Per item: `OK`, a defect with (a) exact file and line, (b) which of criteria
1-5 it corrupts, (c) the smallest repair, or `UNDECIDABLE_FROM_SOURCE` with the
fact you would need. Then one token:

```text
B2_09_STATIC_AUDIT=CLEAR
B2_09_STATIC_AUDIT=DEFECT
```

If `DEFECT`, state for each defect whether it requires a rerun or only a
recomputation from the emitted JSON — the GPU host is scarce and a rerun costs a
scheduling round.

## Negative authorization

No code edit, no run, no commit, no push, no design change. Do not touch the run
in progress.
