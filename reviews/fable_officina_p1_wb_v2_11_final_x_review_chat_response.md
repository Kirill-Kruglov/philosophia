I'll start by orienting in the repo and verifying the exact inputs.

All six input hashes match exactly. Let me examine the documents.

Commit adds only 7 files, all new — no code/test movement. Now the closure's Q1–Q10.

Now the substantive verification. Let me start with R1 — the delimited blocks.

Both hashes reproduce exactly. Let me check the byte-count literals, which differ from my measurement.

The mislabeled counts propagate into two governing files. Let me check whether they're operative.

Both are descriptive tables; no operative check consumes a length literal. Now the narrowing-completeness half of Q1.

Now the CK range audit (Q2) — every operative range.

Now the B14 thought experiment — I need to verify B1..B13 genuinely don't read the option token.

B14 is confirmed the first refusal — no B1–B13 clause reads the token's value. Now the CK definitions and the H-4 owner question (Q7).

Let me test whether H-4's preamble could dominate the operative check definitions — that decides Major vs Minor.

Let me check whether a conformance test row pins the CK-7 ownership — that settles the classification.

Decisive: attested row 109 pins CK-7 and fails any fixture placing it elsewhere. Now the largest piece — KG/KV/SC totality (Q3/Q4).

`_getpid` is bound at §P1-3.4 line 594; `_getpgid` is not. Let me brute-force the SC-7 partition.

SC-7's partition verifies exactly. Now the source-trace honesty — does `pgid_or_null` actually exist in §P1-8.5's signed schema?

`pgid_or_null` pre-exists in the §P1-8.5 schema (line 1445) — KG-2 populates, doesn't add. Let me verify the no-perturbation claims against v1.10.

Let me diff v1.10 → v1.11 in full — this answers both the no-perturbation claims and Q10 scope discipline.

Now R3 — recomputing the eight provenance digests from disk (Q5).

All eight recompute. Now the dependent counts — 63 / 77 / 71, counted from the produced bytes.

Line 4497 of the amendment may be a stale `69`. Let me read it.

Found a stale literal. Let me confirm its scope and check the closure's own sweep claim.

Let me verify the 71-row provenance region and check for other stale version strings in N-16.

Provenance region = 71 distinct rows. ✓ Now R4 — the Cell-2 transformation and PO-9 (Q6).

Let me independently recompute the entire marker census (Q6).

The census reproduces exactly. Now the full Cell-2 transformation table — I noticed a possible range overlap at line 58.

The 20 locus lines match exactly. Let me check for any Cell-2 assertion outside the 55–95 span, then audit PO-9.

Let me verify the Cell-1 preamble notices, which bear on both Q6 and Q9.

C-1 verified (zero occurrences); Cell-1 changed only by the version self-reference repair. Now Q8 — the scaffold.

Let me verify the handoff's factual claims about the working tree (Q8, and that no code was created).

Now Q10 — scope discipline. Let me diff the amendment v1.7 → v1.8 and review the remaining composite hunks.

Let me verify the test matrix row count is unperturbed and row 103's dependent digest count was updated.

Let me do a final systematic sweep for any other missed dependent count.

Let me verify the five generation-scoped loci and the anchor token (R6 / scope).

Let me verify the region digests, especially H_GUARDDATA's byte-unchanged claim.

All four region digests reproduce exactly, and H_GUARDDATA is byte-identical to v1.10. Let me confirm the changed test rows moved only counts (Q10).

I need to verify this carefully — row 106 may declare a fixture group it never defines.

One more check — the closure's own declared log items, so I classify correctly against them.

I have everything I need. Let me write the review.

Review complete. Only `reviews/fable_officina_p1_wb_v2_11_final_x_review.md` was created; nothing else in the tree moved. (The Y-line files that appeared during the run were not opened — this review is independent.)

## Verdict

```text
OFFICINA_P1_WB_V2_11_X_CONFIRMED_FOR_ACCEPTANCE_REVIEW
```

**Output:** [reviews/fable_officina_p1_wb_v2_11_final_x_review.md](reviews/fable_officina_p1_wb_v2_11_final_x_review.md)
`sha256 3964469740fc73a6a4836b64247003c39d5261a6af9c6ddf37a0da76c13f0759` (688 lines)

All six input hashes matched. Commit `d273765` = 7 new files, 0 deletions, no code/test/signature movement.

## Q1–Q10

| | Answer |
|---|---|
| **Q1** | **Yes**, + L-X3. Both blocks byte-identical; `H_HANDOFF` = `ca2ff30b…a785`, joint = `9bf4a831…babe5`; delimiter cardinality exactly 1/file. Narrowing complete — no sentence claims broader identity. |
| **Q2** | **Yes** ×4. Every operative range is `CK-1..CK-15`. B14 traced independently: no `B1..B13` clause reads the token's *value* (B3 tests the key set only) → B14 first and only refusal. Joint-block placement correct — matrix still 123 rows/max 115, `rows_attested` 92..115/24/true unmoved. |
| **Q3** | **Yes.** Brute-forced all 72 tuples: 24+32+4+6+6, total, no residue, no double answer; remainder ≡ KV-2's conjuncts exactly. SC-8 no default-allow. KV-6 dominance sound — I proved the masking case is harmless (SC-2 filters scope; KV-6(b) scans all watchdog handles). Source trace honest. |
| **Q4** | **Yes.** KG-1 reuses the same `/proc/<pid>/stat` buffer + `_open/_read/_close`; `_getpid` bound at line 594, **`_getpgid` bound nowhere**. `pgid_or_null` pre-exists in §P1-8.5 (line 1445). §P1-3.2, MS-11's 89 rows, MS-13, S-12 unperturbed. |
| **Q5** | **Digests yes — one literal missed.** 8/8 provenance hashes recompute. MS-2=63, MS-3=7, MS-8=77, provenance=71, all recounted from bytes. **Missed: amendment N-16 line 4497 says `MS-8` = 69.** Both structural judgements (one update; no substitution) correct. |
| **Q6** | **Yes** ×3. Census reproduces exactly (20/13/13, both-marker lines, sentinels, 3/16/1); the 20 body loci match element-for-element. All four marker-free assertions reached. PO-9 sufficient; D3 is what blocks deletion-evasion. |
| **Q7** | **Minor.** Executable divergence fails against 5 operative statements *and* attested row 109, which fails any fixture placing the code off `CK-7`. No precedence rule favours the preamble (H-2 says the opposite). → next round that opens the pair anyway. |
| **Q8** | **Yes** ×4. §H-0 narrowing honest; the 3 removed test paths were genuinely unimplementable; D-4 is pure data (SC-7 has no I/O component); §H11 complete. Verified on disk: **no scaffold code exists**, MS-5/MS-6 paths absent, 0 `test_p1_row_` functions. |
| **Q9** | **Yes.** `attested_pid`/`attested_pgid` = 0 occurrences in both files. Cell 1 byte-unchanged but for a stale self-reference repair. Gate-0 ledger placement is the correct boundary. Anchor line: cardinality 1, value = composite `H_FILE`. |
| **Q10** | **One locus moved inside R1 (L-X1); nothing else.** All 10 changed test rows word-diffed — R1/R2/counts/generation strings only. |

## Findings — none executable

- **L-X1 (Major-descriptive, new this round, governing bytes)** — composite row 106 now says "**eleven** fixture groups" and enumerates `(k)`, but defines only (a)–(j); **group (k) is defined nowhere**. v1.10 said "ten" and defined ten. It sits in an *attested* row, inside the R1 repair. Not executable: CK-15 checks only `rows_attested`/`row_count`/`all_rows_passed`, and the fixture obligation is independently carried by CK-14 in the joint block.
- **L-X2 (Minor, new)** — amendment N-16:4497 `MS-8` = 69; correct in v1.7, missed in the cascade, contradicted by N-14 29 lines below.
- **L-X3 (Minor)** — "content bytes 4052 / 222364" are UTF-8 *character* counts; true byte lengths 4061 / 222736. In packet §1.2 and binding v2 only — fixable without a governing generation.
- **L-X4** H-4 → CK-12 (concur with closure L-1). **L-X5** closure miscounts CK-1..CK-12 as 3/file; the amendment has 5 (all still negations). **L-X6** §2.2's Cell-2 spans overlap at 58/60/85/88. **L-X7** KV-6 masking argument unstated.

I recommend L-X1, L-X2 and L-X4 be repaired together in the next round that opens the pair for another reason — each alone costs a full generation cascade, and none blocks.

## Next boundary

Authorizes **only** the paired Y review on identical bytes, and after it passes, an author's separate consideration of amendment v1.8 acceptance. No code, no tests, no key, no `OR` step, no install, no activation. `T = NOT_ACTIVATED`; programme claim `OPEN`; XS-1 combined identity binding remains blocked.
