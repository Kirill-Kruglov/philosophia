I'll start by verifying the pinned hashes and getting oriented.

All six hashes match. HEAD is `9ed98a7`, not `23a7816` — let me check whether the pinned files differ between them.

All six pinned files are byte-identical at `23a7816` and HEAD (the only delta is the two review prompts). Hashes verified — proceeding.

Closure read. Now the packet and the structure of the two big governing files.

Now the classifier and vectors — §P1-10.7 (lines 2153–3198).

Critical for Q8 — let me examine the roots and import allowlists.

Now the executable work. Building an independent `STAT_PARSE` from the L0–L5 prose alone.

V0 reproduces exactly (144 bytes, digest matches). Now the independent parser.

All 50 published vectors match. The 144 "failures" are my own harness bug (passing `None` as expected for truncation). Fixing and re-running.

Now verifying the *published refusal rule attribution* (L0/L1/L2/L3/L4), not just the refusal itself.

Q1 is settled. One attribution anomaly at V18 to pin down — let me check the classifier surfaces first (§P1-8.3/8.5) before modelling.

Now the classifier: modelling all six phases as a total function and attacking it.

Now the exhaustive safety search and the Phase-4 exclusion audit.

This is significant. Let me verify whether the watchdog is its own group leader.

Watchdog is `setsid=False` — that resolves the Phase-3 question but undermines an author proof. Now Q5: the eleven-span OR-4 transform.

Now implementing the OR-4 transform independently.

Sentinel-prefix parsing bug on my side. Fixing — and I'll recover the four substring literals purely by pinned length+digest, sliding a window over the binding bytes.

All 11 spans locate exactly and every source digest matches. S7's replacement is the one that doesn't reproduce — let me isolate why.

Found it. The S7 delete literal is uniquely recoverable from the source line by its pinned digest; only the binding's *transcription* is wrong. Completing the splice.

Full OR-4 output reproduces byte-exactly. Now the delimited regions, the detectors (Q6), and MP-1.

MP-1's length reproduces exactly but its digest doesn't. Let me pin down the insertion point.

Now Q7 — the counts, recounted from the bytes.

Q8 turns on whether a mechanical gate blocks c10. Let me check the verifier's code rules.

All checks are complete. Writing the review.

Working tree confirms read-only discipline: the pre-existing dirty and untracked files are untouched, nothing committed, exactly one file created. (The `sol_officina_p1_wb_v2_13_final_y_review*` files appeared during my session — that's the parallel Y line, not my work; I did not read them.)

---

# Officina P1 W-B v2.13 — final independent X review

```text
OFFICINA_P1_WB_V2_13_X_CONFIRMED_FOR_ACCEPTANCE_REVIEW
```

**Path:** [reviews/fable_officina_p1_wb_v2_13_final_x_review.md](reviews/fable_officina_p1_wb_v2_13_final_x_review.md)
**SHA-256:** `89e210430b617d88a67229df2beeff82c5c844f6de1da1d03b376b758d7cb0c2`

All six pinned hashes recomputed and **MATCH**. One disclosed deviation: the prompt pins `23a7816`, HEAD is `9ed98a7` — I verified all six pinned files are byte-identical at both, so the review ran against exactly the pinned bytes. Not a `BLOCKED` condition.

## Q1–Q8, answered executably

- **Q1 — one exact grammar: YES.** Built a reference `STAT_PARSE` from the L0–L5 prose alone. V0 reconstructed at 144 bytes / `0ea1e5bc…`. **50 published vector assertions, 0 mismatches** — every length and digest. Plus ~600 constructed cases (inserted/removed separators at every boundary, all 49 rotations, truncation at every byte, all 256 state bytes, field counts 0–60, parenthesised comms) and **200,000 mutation trials with 0 wrong-field values**, **200,000 consumer trials with 0 disagreements about parsing**.
- **Q2 — terminal single-valued: YES.** CE-1, CE-2 (both forms), CE-3 (all three) pass. Every SC-10 multi-fault pair in both orders, triples in 6 orders, all four in 24 orders. **32,400 exhaustive tables: 0 signals to a protected group, 0 signals while any protected group existed in either form, 0 order-dependence.** SC-7's 24/32/4/6/6=72, the 12 prospective and 36 non-NULL tuples all recount.
- **Q3 — exclusions honest: YES**, and the NULL-group limit is stated correctly — I built the adverse case and confirmed the undetected handle grants no scope.
- **Q4 — KG-2 total: YES.** P-2's instant is real and single-valued (AWAIT_STOP precondition `SPAWNED`, one outstanding request removes interleaving); all six KG-1 outcomes covered; no route escapes the six handle states.
- **Q5 — OR-4 reproduces byte-exactly.** All 11 source and 11 replacement digests, non-overlap verified, **586426 bytes / `3a88798f…c339`**, all region digests, guarddata byte-unchanged, both shared regions byte-identical across both files and across OR-4.
- **Q6 — claim no broader than detector: YES.** D1 0/11, D2 0/13; coverage 11/11 and 13/13; both CANON digests. **The §2.5 W-A option-token count of 3 is correct.**
- **Q7 — 71/85/79 all recount** from the bytes, with the four new M2 digests verified against the real files on disk. No stale figure survives anywhere; anchor line count exactly 1 and equals composite H_FILE.

## Q8 — `L-X6`: outside the accepted authority, not a current Major

The classifier **never calls `getpgid`** — P3(a) uses `PGRP_OBSERVE(_getpid())` with the bound `_getpid` and the canonical parser; P3(c) *reads* `SPAWNING_GROUP.json` rather than recomputing it, and fails closed if it's absent or malformed. So the W-B mechanism is implementable in full.

**The mechanical gate** is §P1-14.6 CHANGE 3: **S-3** (binding block must equal §P1-3.4's list *exactly, in that order*), **S-5** (module names as Attribute values only inside that block), **S-6** (call targets are plain names only), **S-7** (no `getattr`/`eval`/`importlib` indirection). Any build attempting c10 fails the verifier statically — fail-closed, no certified artifact.

I did *not* waive it for being previously logged, and I record that **the author's `L-X6` is narrower than the bytes**: it also bites `c14` and `m3`, and `getsid` — which unlike `pgrp` has no substitute route, since `STAT_PARSE` returns no session id.

## Findings — no Critical, no Major; 7 logged

Most substantive first: **X-L1** L1's 0x29 refusal is unreachable (L0's last-`)` framing already excludes it), so V18's named rule is wrong and L0's justification is circular — the safety property itself holds. **X-L2** the watchdog exclusion's "REQUIRED" proof assumes a group-leader watchdog, but `setsid=False` means it never is. **X-L3** §2.2.4's S7 delete literal is transcribed one backtick short — I recovered the true 277-byte literal from the source line by pinned digest (unique), and everything then reproduced. **X-L4** MP-1's pinned digest does not reproduce: length is exact and all behaviour holds, but **none of 8,067 line-boundary insertions under either payload ordering** yields `afbdb075…`.

I considered grading X-L4 Major and rejected it: the fixture's required behaviour (detectors silent, PO-0 fails closed) reproduces independently, no rule consumes the digest as a gate, and the quarantine boundary it exists to prove is established directly by the byte-exact OR-4 reproduction.

**Next boundary:** the X-line half of an acceptance-review record for Kirill's later *consideration* of v1.10 — nothing else. `L-X6` is carried as an explicit precondition: it must be repaired, in a separately reviewed import-surface round, before any scaffold or runtime authorization. `T = NOT_ACTIVATED`; programme claim `OPEN`.
