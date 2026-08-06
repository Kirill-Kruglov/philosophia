I'll start by verifying the bytes and reading the two files under review.

Both hashes match. Note: repo HEAD is `07f4fd5`, not `9e93df5` — let me check whether the reviewed bytes differ between them.

Both reviewed files are byte-identical at `9e93df5` and at working-tree; `07f4fd5` only adds the two review prompts. Now reading the charter.

Now let me verify the load-bearing factual claims independently.

Verified: 7,349 LOC in `src/philosophia/officina/`, `generic_harness.py` at 2,380 LOC, and all three durability primitives live in [canonical.py:43-101](src/philosophia/officina/canonical.py:43). Now checking the budget arithmetic and the enumeration dimensions.

Repo-wide average is 41.5 B/line. Let me check the dimension declaration the enumeration ranges over.

The composite names the twelve dimensions and — importantly — clause `(6B)(v)` explicitly routes deadline-exhaustion to `R-E`'s ERROR sub-row. Let me confirm the Y findings and the `(x4)`/`(x2)` clause texts.

I have everything I need. Writing the review.

Done. Exactly one file created; the rest of the working tree is unchanged from the session-start snapshot. One note: `reviews/sol_officina_migration_charter_v1_y_review.md` appeared during my session — the Y line is running concurrently. I did not read it, to preserve independence.

## Verdict

```text
OFFICINA_MIGRATION_CHARTER_V1_X_ACCEPTED_FOR_BOUNDED_REVISION
```

**Path / SHA-256:** [reviews/fable_officina_migration_charter_v1_x_review.md](reviews/fable_officina_migration_charter_v1_x_review.md) — `e892068af2f3d799535237761adbbdff4a373439c4a1cdf7725a5a44bf024000` (37,473 B). Both reviewed inputs recomputed and reproduced exactly; verified byte-identical at `9e93df5` and at working-tree HEAD `07f4fd5` (which adds only the review prompts), so the pin discrepancy is not `BLOCKED`.

## X1 — independence

§4.1's claim is inverted: two transcriptions agreeing *is* the evidence; two projections of one declaration agreeing is the tautology. After migration the prose is gone, so independence must be re-anchored outside the declaration or it does not exist. Recommended **(c) amended**, with (b) as implementation style: one live relation (guarded-row table + fact-free evaluator), the projection pair demoted to a *generator/ordering test*, plus **O1** a standing hand-written property oracle that is strictly weaker than the relation (so it can refuse but never define), and **O2** a one-time M4 transcription coded from `generated/CONTRACT.md` alone, never committed. Drift surfaces as a derived enumeration digest block in generated output — a one-line review tripwire duplicating no fact.

## X2 — KG-2 enumeration

The memo's proposed clause-1 default is **not available**: composite `§P1-15 (6B)(v)` explicitly routes deadline exhaustion to `R-E`'s ERROR sub-row, so the textual evidence is split 2–1 across clauses of unequal operative weight. But the dispute is illusory — restricting the X line's own published table to non-self-contradictory tuples, both readings give identical routes (552/8/4/4, **4 writes**). The 4-vs-6 divergence was only about whether to count impossible tuples. Root cause: `KG-1 result` and `EINTR` are declared as independent dimensions but are not — the declared cross-product is not a product, and `(x4)` clause 2 exists to patch that. Recommendation: **encode, don't choose** — collapse the pair into one `ObservationOutcome` sum type, delete clause 2, emit both full-product and feasible-subset counts. Missing-dimension gate is G-DIM-1..4, with **G-DIM-4 (product faithfulness)** the one that would have caught `(x4)`.

## X3 — template theorem

The hole is larger than the memo's §2.5(1) admits: **L1 itself fails**. `ROUTE_COUNT = 9` and `STAT_SUFFIX_FIELDS = 50` are the same construct, and templates read `constants.py` by design — so a derived fact does have a writable home in source. §1.3's "Class B eliminated by construction" is **false as written**. An AST guard alone is insufficient; sufficiency needs three rules of different kinds: **G-TPL** (allowlist over the generator layer, not a blocklist), **G-SRC** (mandatory resolving `# PROTOCOL:` citation — this is what distinguishes `E1=168` from `ROUTE_COUNT=9`), **G-CARD** (evaluated-value `len(C)` comparison, catching computed cardinalities AST cannot see). Generated Markdown *can* introduce authority source doesn't encode, because a test can only detect disagreement about encoded facts — fix is templates emit layout, never sentences. On crash-cut: confirmed deadlock (`canonical.py:43-101` holds all three primitives, M3 can't edit `src/`, §7 doesn't classify it, §3 has no durability invariant). **Recommended: record an M6 blocker, do not expand M3**, made fail-closed by `xfail(strict=True)` plus a derived open-blocker count in the M5 signature.

## X4 — budget

The caps are **arithmetically unsatisfiable**. At the repo's own measured 41.5 B/line (7,349 LOC / 305,045 B), 2,500 LOC ≈ 101.3 KiB, leaving 18.7 KiB against a declared 64 KiB data cap; conversely a full data budget permits only ~1,382 LOC. Recommended: delete the 120 KiB aggregate cap. Four separate ledgers, with tests/oracles explicitly uncapped and a new 400 LOC cap on the highest-risk generator layer. Missing invariants M6 necessarily needs: **I-16** (canonical stat/`PGRP_OBSERVE` grammar + `V0..V39` — §4.2 property-tests a ~40-vector surface no I-n governs), **I-17** (durability), **I-18** (deadline/interruption semantics).

The sharpest interaction found: §6.1's zero-duplicated-literals "Class-B kill switch," if read to include tests, **forbids the Class-A oracle X1 requires** — its entire function is independent restatement.

## Mandatory edits and next boundary

Nine bounded edits (E1–E9) to §1.3, §3, §4.1, §4.4, §4.7, §5, §6.1, §7. Verdict is not `REVISE` because the skeleton — acyclic graph, one manifest, no self-hash, generated-is-not-authority, self-binding stopping condition — survives intact and every hole has bounded replacement text. Next boundary: the Y line's independent review, then author consideration of E1–E9. T-1/T-2/T-3 considerable after the revision; **T-4 not considerable until E1–E9 land**. No token is authorized. `T = NOT_ACTIVATED`; `OR-3..OR-11 NOT AUTHORIZED`; claim `OPEN`. No commit made.
