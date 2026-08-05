I'll start by reading the input files and verifying hashes.

All six input hashes match. Reading the governing pair and closure.

Now the independent mechanical verification. Starting with F1 (CK range).

Joint block is byte-identical (`2584913e…`), but §A9/§P1-14.8 are not. Now CK-13/14/15 and B14.

F2 confirmed mechanically. Now the independent marker census (Q3).

Now the implementation handoff (Q5, Q8, Q9 depend on it).

Verification complete. Writing the single review file.

Working tree is unchanged apart from my single new file; nothing committed. (Two `sol_…y_review` files appeared during the session — that is the parallel Y-line, not this review.)

## Verdict

```text
REVISE_OFFICINA_P1_WB_GOVERNING_PAIR
```

**Output:** [reviews/fable_officina_p1_wb_binding_x_review.md](reviews/fable_officina_p1_wb_binding_x_review.md)
`d8483c185c6f438f4a209353716b7d8aef31529c5f6876381ea03431beb15ba1`

All six input hashes matched. Both prioritized findings are confirmed Major and executable, so the escalation rule applies.

## F1 — CONFIRMED MAJOR, fail-open

Not reconcilable by any reading. I extracted and diffed both copies of the joint block: amendment 1214–4277 and composite 3019–6082 **are** byte-identical (`2584913e…`), 3064 lines, zero hunks — and every fifteen-check statement (§A10, `IR-9`, `CK-15`, `FC-1`, `VP-4`) lives inside it. The twelve-check statement does not: §A9 `H-3` sits at line 1149, outside. Meanwhile §A9 and §P1-14.8 are **not** byte-identical — four divergent passages, `H-3` entirely — though four governing sentences (composite 86, 147, §A9's preamble, `DA-5`) assert they are. No precedence rule selects between them; line 54 ranges over the historical chain, and `H-2`'s "cannot disagree" is about the ordering, which doesn't.

**Minimal counterexample:** an otherwise perfect final state — all 69 members, genuine manifest/record, valid Ed25519 signature under the pinned key — where Stage A carries the W-B token and Stage B carries the W-A token. `CK-2` (A1–A14, Stage A alone) passes; `CK-3` (B1–B13, self-contained by their own text) passes, including `B12`; `CK-4`–`CK-12` never read the field. Verifier returns PASS, production entry proceeds. The sole owner of that equality is `B14`/`STAGE_B_OPTION_MISMATCH` at `CK-14` (`IR-13` row 35). Also lost: `CK-13`'s member partition, `B15`–`B18`, and all of `CK-15`. Note `B17` is what the binding's own `PR-1` relies on to keep the deferred `MS-2` rows out.

## F2 — CONFIRMED MAJOR, quarantine/fail-closed

`KV` occurs exactly twice in composite v1.10 (1932, 6391), zero in amendment v1.7, zero in packet v2.10. The controlling prohibition is **`DA-4`**, not `DA-1` — "the two live specification surfaces are exactly two" excludes every packet including the governing v2.10 one. I confirmed only the token's presence in the superseded draft and read no clause from it. Exact W-B PCS scope is **not** implementable: actor, trigger, mediation, evidence and publication boundary are all stated; only the per-`_killpg` safety predicate is missing, and W-B makes that classifier the sole group-stop executor. On the closure's (a)/(b): **(a) is the fix, (b) is the fence** — `§H12` is the right interim state, not a repair.

## Q1–Q10

**Q1** yes/yes. **Q2** not implementable; reconstruction prohibited under `DA-4`/`DA-2`/`IR-12`; repair (a). **Q3** census independently reproduced exactly — 20 lines, 13/13, 3/16/1, both-marker 6 whole-file / 4 body; (a) confirmed, `PO-2` genuinely needed; (b) confirmed. **Q4** exclusion correct; this is not the combined binding (`XS-1` does (a) only, refuses (b)(c)(d)); blocking would be the opposite error. **Q5** not mechanical — I found three legitimate *supervisor-side* slot-6 occurrences (392, 1349, 6344) that handoff `U-5` would fail. **Q6** confirmed, plus a reinforcement the binding misses: `TS-1` is inside the joint block, so deleting the W-A token also breaks byte identity. **Q7** `PR-2` and `PR-3` correct; 63 provenance rows recounted; 55→63, `MS-8`→77. **Q8** lists correct and complete; zero `test_p1_row_NNN_` verified. **Q9** `§H11` confirmed on every clause, including the exculpatory half. **Q10** no — `F2` is fenceable, `F1` is not.

## Blockers against the binding draft (not the pair)

- **X-1 Major** — `PO-4` is unsatisfiable and contradicts `PO-6`: the W-A option and amendment tokens survive at composite 4867/4873, which `PO-6` *requires* retained.
- **X-2 Major** — §2.2 mislabels lines 79/80/83 as the Cell-2 blocking notice. The actual notice is at 57–58, carries no marker, and `PO-2` cannot see it. `E-1` diagnoses correctly and its own remedy misses the sentence.
- **X-3 Major** — the §3.1 ledger has no row for Cell 1 as a gate on the composite's operativeness, hence on `OR-3`..`OR-11` and `T`.

## Next boundary

An **authoring** act: draft amendment v1.8 / composite v1.11 carrying R1–R4 (R1 = the `CK-1..CK-15` correction plus a second delimited byte-identical block for `H-1..H-4`; R2 = carry `KV-1..KV-6` in, content to be derived by that round, not by me), then an independent X/Y round on those bytes. v1.7 should **not** be accepted now — R1 changes the bytes the token would accept. No acceptance, implementation, key, `OR-3`/`OR-4` or activation is authorized. `T = NOT_ACTIVATED`; programme claim `OPEN`.
