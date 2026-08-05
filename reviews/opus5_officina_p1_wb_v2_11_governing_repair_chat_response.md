I'll start by examining the repository state and reading the exact inputs.

All seven input digests match exactly. Now reading the inputs.

This is a large, precise task. Let me systematically map the governing pair.

Now I have the full map. Let me build the transformation programmatically.

Joint block confirmed byte-identical (`2584913e…`), guarddata `faf2d709…` matches the Y line. Now building the v2.11 generation.

Joint block v2.11 built (63 M2 rows, 77 members). Now the composite v1.11.

Composite v1.11 built and verified. Now the amendment v1.8.

Now finalize the placeholders and verify byte-identity of both delimited blocks.

Both delimited blocks are byte-identical across the pair. Now the remaining four deliverables.

Now the regenerated W-B binding v2, with the exact locus classes and permitted-occurrence census.

Now the honestly narrowed handoff v2.

Final verification of the complete deliverable set.

All six deliverables are written and mechanically verified. Nothing was committed.

## Verdict

```text
READY_FOR_OFFICINA_P1_WB_V2_11_FINAL_XY_REVIEW
```

## Output paths and hashes

| Digest | Path |
|---|---|
| `efe0f908…fdfb` | [packet v2.11](successor/OFFICINA_P1_WATCHDOG_FREEZE_AUTHOR_CHOICE_PACKET_V2_11_CORRECTION.md) |
| `71ec025a…8a4c` | [amendment v1.8](successor/OFFICINA_GENERIC_HARNESS_WATCHDOG_FREEZE_AUTHORITY_AMENDMENT_V1_8_DRAFT.md) |
| `c9712f7c…87b6` | [composite v1.11](successor/OFFICINA_GENERIC_HARNESS_SUPERVISOR_CONTROL_CHANNEL_P1_OPERATIVE_COMPOSITE_V1_11.md) |
| `d7ccf170…c91d` | [binding v2](successor/OFFICINA_P1_WB_POST_SELECTION_BINDING_V2_DRAFT.md) |
| `a70f6a77…5c6b` | [handoff v2](successor/OFFICINA_P1_WB_IMPLEMENTATION_HANDOFF_V2_DRAFT.md) |
| `e6ef3a8f…9677` | [closure](reviews/opus5_officina_p1_wb_v2_11_governing_repair_closure.md) |

Composite regions: `H_BODY ce728942…51cf`, **`H_GUARDDATA faf2d709…0426` byte-unchanged**, `H_NORMATIVE 01ea7391…43b8`, `H_FILE c9712f7c…87b6`. Anchor `P1_WATCHDOG_V2_11_…` = composite `H_FILE`, exactly one matching line.

## F1 repair

One canonical `H-1..H-4` block, delimited, **extracted from both files and diffed: zero difference**, digest `ca2ff30b…a785` (4052 bytes, amendment 1209–1271, composite 6614–6676). The shared OR/check block stays byte-identical at `9bf4a831…abe5` (222364 bytes). Every operative range is `CK-1..CK-15`; the three surviving `CK-1..CK-12` mentions per file are all negations or descriptions of the removed defect. The identity claim is narrowed to those two regions only. The option-mismatch fixture sits at `CK-14` **inside** the shared block: `CK-2..CK-13` pass, `B14` refuses `STAGE_B_OPTION_MISMATCH`, and a 12-check implementation fails conformance.

## KV definition

`KG-1`, `KG-2`, `KV-1..KV-6`, `SC-1..SC-8` at composite §P1-10.7 only, with a source-trace table over current clauses. `KG-1` is the one supporting rule: the same single `/proc/<pid>/stat` read §P1-10.3 already performs, same three bound primitives, same errno map, one extra already-present token (3rd after the final `)`). §P1-10.3, §P1-3.2, MS-11's 89 rows, MS-13 and S-12 are all unchanged; `_getpgid` is not bound and not used. `SC-7` partitions 24+32+4+6+6 = 72 tuples; `SC-8` leaves no default-allow path; `KV-6` terminates the whole classifier. Row 89 carries the adversarial fixtures; row 101 names the seven tokens.

## Accounting

`MS-2` 55→63, `MS-8`/`TS-3`/`B7`/`B17` 69→77, provenance region 63→71, one atomic update, seven classes, only M2 grew. Counted from the produced bytes: **MS-2 = 63 rows, provenance = 71 rows**. The two W-B binding reviews were not substituted for the v2.10 pair-confirmation rows.

## W-B transformation

Byte-exact line-by-line table over the **whole Cell-2 span, lines 55–95** — reaching the marker-free blocking notice (57–58), "what remains open" (60–62), the W-A capability exposition (64–68) and "selects neither" (75–76), none of which v1 touched. Census reproduced exactly: 20 marker lines, 13/13, 3/16/1 regions, 6 whole-file and 4 body both-marker lines. Permitted-occurrence table: class R retains TS-1's two option tokens, both amendment tokens, the CK-14 fixture's W-A token, guarddata byte-identical, seven supervisor/PCS socket loci, two closed-sense watchdog slot-6 loci; class F removes W-A grants and all nine `t-wd-freeze.v1` occurrences. **No whole-file zero-W-A-strings rule remains.** `PO-9` D1–D4 is a whole-file-minus-guarddata content verifier; `G-10` stays body-scoped.

## Scaffold scope

Retitled **inert oracle and declarative scaffolding only**; §H-0 states plainly it does not and cannot implement the runtime EOF route, the PCS classifier, the descriptor topology or any process operation. Three v1 test paths with no implementation under test were removed; nothing was added. `test_p1_row_NNN_` and both MS-6 modules remain forbidden; no process-control smoke anywhere; `generic_harness.py` was not read this round and requires a fresh reviewed audit. §H11 is the later-stage authorization table.

## Identity and acceptance

No identity-observation code (`attested_pid`/`attested_pgid` = 0 in both new files); not the XS-1 combined binding; the bounded weakening unaccepted; the combined binding still blocked. Cell 1 recorded as **gate 0** of the binding ledger, not added to the composite. Token bumped to `I_ACCEPT_…_AMENDMENT_V1_8`; v1.7's is retired. Even a future signature authorizes no code edit, `OR-3`, key, `OR-4`, install or activation.

## Negative space

Exactly six files created; nothing else modified, staged, reverted or deleted; nothing committed. No key, entropy, Stage A/B, manifest, attestation, install record or `OR` step; `OR-4` did not run. No test run, no module imported, no process/`/proc`/clock operation. The superseded V2 draft was not opened for behaviour. `T = NOT_ACTIVATED`, claim `OPEN`.

Two items I reported rather than repaired, both raised as bounded questions (Q7, L-2): `H-4` attributes `HISTORICAL_BYTE_MOVED` to `CK-12` where `CK-7` owns it — carried verbatim from both v1.7 and v1.10, already byte-identical there, raised by neither review line and not in R1–R6; and composite line 94's "finished replacement for v1.2" inside the retained part of the Cell-2 span.

## Exact next boundary

A fresh bounded independent X-line and Y-line round on the v2.11 bytes, by reviewers who did not author v2.3–v2.11. Not authorized: acceptance, inactive-scaffold authorization, runtime implementation authorization, any key, `OR-3`..`OR-11`, the one-shot handoff authorization, identity-token acceptance, or `T` activation.
