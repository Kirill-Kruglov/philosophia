I'll start by orienting myself in the repository and reading the input documents.

All six input hashes match. Note HEAD is `bd52991` (the review-request commit on top of `9be5148`); the input files themselves match the stated hashes.

Now let me examine the governing bytes. Starting with composite v1.12's §P1-10.7.

`_getpid` is bound (§P1-3.4), so P0-2(a) is executable. Now §P1-10.3 for Q6.

The commit added a 7th file (a chat response) despite closure §2.2's claim. Noting that. Now the binding's splice section.

Now the mechanical verification. Writing a verification script.

Splice verified byte-exact. But the ENCODING claim needs checking — the block contains `§` too.

Confirmed: 5 `§` (U+00A7) in the pinned block, contradicting §2.2.2's non-ASCII claim. Now the D1/D2 arrays.

Now the full PN / D1 / D2 verification.

D1/D2 hashes and coverage reproduce exactly. Now the resolved-file test and the locus table.

Now the accounting recount (Q7) — MS-2 / MS-8 / provenance rows.

Accounting fully reproduces. Now the stale-literal sweep.

`"70th entry"` still occurs once in the amendment. Let me check that and the other numeric hits.

Found a stale literal. Let me confirm it precisely and sweep for others.

Now Q3 — implementing KG-1 G0..G5 and exercising it on ordinary and adversarial stat lines.

A concrete hole in Phase P1. Let me confirm the exact bytes before concluding.

Verification complete. Writing the review.

Review written. The pre-existing dirty/untracked files are untouched; the only file I created is the review. (The `sol_*_v2_12_final_y_review*` files appeared during my session from the parallel Y line — not mine, and I did not read them.)

## Verdict

```text
REVISE_OFFICINA_P1_WB_V2_12
```

**Path:** [reviews/fable_officina_p1_wb_v2_12_final_x_review.md](reviews/fable_officina_p1_wb_v2_12_final_x_review.md)
**SHA-256:** `ca02d4858022fef026fdbbe65dfb07dc7fb1e885563530be27238d7dbcc8a61a`

All six pinned inputs recomputed and matched. Note HEAD is `bd52991`, not `9be5148`; the input bytes are identical.

## Two executable Majors

**X-M1 — `KV-5`/`KV-4` mask `KV-6`'s fresh-observation conjunct.** Phase P0 tests only the *recorded* group. `KV-6`'s second conjunct (new in v1.12) tests the *freshly observed* `pgrp` — but `SC-6` says evaluation "stops at the FIRST failing predicate," and `KV-5` fails *exactly when* the fresh `pgrp` differs from the recorded one. Table: `a` valid/unprotected; `b` recorded 601, live `pgrp` = supervisor group 2000. P0 clean; `b` → `KV_GROUP_MISMATCH`, skipped, `KV-6` never runs; `P1-6`'s four conjuncts all hold; `_killpg(600,15)` and `_killpg(600,9)` issue. `KG-2` `P-6` states the opposite answer in terms, so the contract contradicts itself and two conforming builds differ. Row 89 doesn't catch it — its clause (4) fires only when a later entry *yields* `KV_FORBIDDEN_TARGET`. `KV-4` masks identically on a reused pid.

**X-M2 — a stale accounting literal survived the forced sweep.** Composite line 7227, row 108, still reads "a members array of any length other than **77** is a STRUCTURAL failure." Enforced cardinality is 81 at `MS-8`/`TS-3`/`CK-6`/`TS-5` B7,B17/`IR-13` row 38. The other three figures in that same row moved (78→82, 70→74, 63→67). Closure §5.2 lists this literal as moved; it did not.

## Q1–Q7

- **Q1** — P0 total and fail-closed against the recorded group (all named paths verified). **Not** total against the fresh observation → X-M1.
- **Q2** — Y-CE-1 now yields exactly zero signals. Ran the full cross-product: **2160 fixtures** (4 protected values × 3 roles × 4 states × 3 ownerships × n=1..5 × every position) — **0** non-terminal outcomes. Control table still signals correctly.
- **Q3** — `KG-1` executable. A real `/proc/self/stat` returns `PRESENT_VALID`; all nine state characters pass; every named malformed form refuses (missing `)`, <20 tokens, `W`/`x`/`K`, 2-byte state, `pgrp` 0 and `00`, sign bytes, 19/20-digit overflow with the bound inclusive at INT64_MAX, `comm` containing `)`). Nine-char set is right and fail-closed.
- **Q4** — Part 1/Part 2 split honest; `c10` genuinely says nothing about child handles. `P-1`..`P-7` total over the decision tree, no residue. All three `_getpgid` occurrences are negations; `MS-11`/`MS-13`/`S-12` unchanged.
- **Q5** — Splice byte-unique: sentinels cardinality 1 at lines 55/95, span 41 lines/2184 bytes and replacement 37 lines/2120 bytes, **both hashes match**. `D1`/`D2` canonical serializations reproduce exactly (926/1044 bytes, both SHAs). Coverage 11/11 and 13/13; zero false positives against the replacement and against Cell 1. All four region digests match.
- **Q6** — Boundary is right; `§P1-10.3` is byte-identical to v1.11, never meets `KG-1` operatively, and its strict reading is fail-closed (degrades identity capture, opens no kill path). Next round's work, not this round's defect.
- **Q7** — 67/81/75 recount exactly; **all 67 `MS-2` and all 75 provenance digests verified against disk**, 0 mismatches; M2∩M3 empty. Retired tokens and anchors swept to zero. One literal left behind → X-M2.

Seven log items, including: §2.2.2's "no other non-ASCII character" is false (the pinned block carries `U+00A7` five times); and commit `9be5148` added a **seventh** file — a chat response — against closure §2.2's explicit "no seventh" claim, a repeat of Sol's Q10.

## Next boundary

A bounded repair round against X-M1 and X-M2 only, plus the Y line's independent verdict. No acceptance, scaffold, code, key, `OR` step, install or activation is authorized. `T = NOT_ACTIVATED`, programme claim `OPEN`, W-B not reopened. Nothing committed.
