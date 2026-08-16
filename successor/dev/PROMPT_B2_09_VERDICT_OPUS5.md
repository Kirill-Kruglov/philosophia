# PROMPT — B2_INSTRUMENT_REPAIR_09 — verdict (Opus 5)

ROLE: apply a decision table that was fixed before the run. Nothing else.

This is the terminal step of Slot 4c's instrument repair. Your output determines
whether the project proceeds to the Stage-2 six-block call, publishes a
registered negative, or stops and returns to the author.

## Read before deciding

| file | SHA-256 |
|---|---|
| `successor/dev/B2_INSTRUMENT_REPAIR_09_TICKET.md` | `b8759ebdd7743239bf97238394cb267c091382469ac10dfc4308b5b53670cc85` |
| `successor/dev/B2_PATH_VS_DESTINATION_DESIGN_V2.md` | `160726a6c06fed20b5aa554449c3f14c03f45b9ee52cdcf1ca49ff49ce238dd2` |
| `successor/dev/B2_PILOT_08.md` | `107d8a6ed5dcf3e6dac9d4f43196f6c3bdf3d372ff5068e0df050bcceeb76d7f` |
| `successor/dev/B2_INSTRUMENT_REPAIR_09.md` | *(builder emits)* |
| `successor/dev/b2_repair_09_results.json` | *(builder emits)* |
| `successor/dev/B2_09_AUDIT_SOL_RESPONSE.md` | *(Sol emits)* |

**Precondition.** If Sol returned `B2_09_NUMBERS_TRUSTWORTHY=NO`, stop
immediately and return `BLOCKED_PENDING_NUMBER_REPAIR`, naming the corrupted
number. Do not reason around a number Sol flagged as wrong or leaked.

## The decision table — fixed on 2026-08-15, before the run

Read the numbers from `B2_INSTRUMENT_REPAIR_09.md`. Apply these criteria as
written. You may not add, remove, soften or reinterpret one.

**Instrument criteria (1-4):**

1. held-out loss decreases monotonically over `M_PATH`;
2. `mean_std >= 1.0` at step 600 on the held-out batch (variance hinge satisfied,
   no collapse);
3. `road_gap(P0) > road_gap(init)` **and** `road_gap(P0) > road_gap(P_shuf)`;
4. `delta exact_d > 0` against the matched-init baseline.

**Design criterion (5):**

5. the M3 panel prediction holds on at least one seed: S1 and S3 qualify, S2, S4
   and S5 fail.

**Verdicts:**

| condition | verdict |
|---|---|
| 1-4 all pass **and** 5 passes | `DONE` |
| 1-4 all pass **and** 5 fails on both seeds | `KILL` |
| `mean_std < 0.5` persists after the section-3 conditional fix | `INCONCLUSIVE` |
| any other combination | `INCONCLUSIVE` |

**What each verdict means, so you do not soften one into another:**

- `DONE` — the instrument works and the design's prediction held. Slot 4c
  proceeds to the Stage-2 six-block call.
- `KILL` — the instrument works, the invariance genuinely was installed, and it
  did **not** produce the predicted panel pattern. Manufactured road-invariance
  is redundant to destination-credit in this world. This is the design's own
  registered kill — *"indistinguishable → the path is redundant to the
  destination; also an answer, published"* — and it is a **result**, not a
  failure. Report it as a result, in those terms.
- `INCONCLUSIVE` — the instrument still cannot separate "invariance installed"
  from "representation collapsed". Return to the author. No third round is
  authorised.

## What you may not do

- Do not propose a repair, a new metric, a new arm, a weight sweep, a longer
  `M_PATH`, or any design change. If the verdict is `INCONCLUSIVE`, that is the
  output; the next step is the author's.
- Do not reinterpret a criterion because the result is near a boundary. If
  `mean_std` is 0.97 against a threshold of 1.0, criterion 2 fails.
- Do not weigh criterion 5 against criteria 1-4, or excuse a failed criterion by
  a strong showing elsewhere. The conjunction is the rule.
- Do not treat `KILL` as bad news, and do not hedge it into `INCONCLUSIVE` to
  keep the line alive. A registered kill answered by data is what this programme
  has been unable to reach on four other routes.
- Do not re-open pilot 08's `M3_PASS = False`. It was produced by an instrument
  that could not distinguish installation from collapse; it carries no evidential
  weight here.

## Output

Write to `successor/dev/B2_09_VERDICT_OPUS5.md`. Never `/tmp` — it is volatile on
this machine and was wiped on 2026-08-15.

Contents:

1. the verified hashes of every input you read;
2. Sol's trustworthiness token, quoted;
3. a five-row table: criterion, the exact number(s) read, pass/fail;
4. the verdict, with the specific numbers that decided it;
5. if `KILL` — two or three sentences stating what was learned, in the design's
   own terms, for the essay's Slot 4c;
6. if `INCONCLUSIVE` — the single sentence naming what remained unseparated.

End with exactly one token:

```text
B2_09_VERDICT=DONE
B2_09_VERDICT=KILL
B2_09_VERDICT=INCONCLUSIVE
B2_09_VERDICT=BLOCKED_PENDING_NUMBER_REPAIR
```

## Negative authorization

No code, no rerun, no design change, no Stage-2 call, no commit, no push, no
second round. Your verdict does not authorise the six-block call by itself —
that is the author's decision on your output.
