I'll start by reading the governing inputs.

I have the full audit. Writing the two deliverables now.

Done. Two files created; **no existing file modified** (the pre-existing ` M` entries under `reviews/` were already dirty at session start, and the two identity-cell `V2_2` files are from a separate cell, not this one).

## Deliverables

- [OFFICINA_P1_WATCHDOG_FREEZE_AUTHOR_CHOICE_PACKET_V2_2_CORRECTION.md](successor/OFFICINA_P1_WATCHDOG_FREEZE_AUTHOR_CHOICE_PACKET_V2_2_CORRECTION.md) — `651dba04…`, 1563 lines
- [opus5_officina_p1_watchdog_freeze_choice_v2_2_closure.md](reviews/opus5_officina_p1_watchdog_freeze_choice_v2_2_closure.md) — verdict `READY_FOR_OFFICINA_P1_WATCHDOG_V2_2_FINAL_XY_CONFIRMATION`

## What the audit found

**A — peer chain.** `O-6` withdrawn in whole: §W3.3 is titled *"Freeze evidence: proved quiescence, watchdog-written"* and its step 6 has the watchdog write the object *"itself"* — X's determination 4 is right on the bytes. The replacement set is **40 tier-1 loci in 6 files**: harness §5a (`PH1`, verified carried unamended by all four harness corrections), §W3 (14), §Z4/§Z10/§Z11/§Z12 (7), §N0/§N5/§N10 (5), §U0/§U3 (3), binding (10). `O-5`'s "seven" binding mirrors is **wrong — there are ten**: it omitted §P1B.7.5 `:612-613` and the `S-3`/`S-4` shutdown steps `:712-713`, and conflated two statements at `:660-663`. §Z4.6 conjunct 8 now rejects `killer == WATCHDOG` with the enum retained (schema not reopened). The authority ambiguity Y named is resolved by a stated, checkable rule (`AUTH-1`..`AUTH-5`); 18 tier-2 provenance loci are enumerated and dispositioned but **not edited**, because the composite's own level-3 rule makes them immutable.

**B — read cluster.** Read retained, authority removed. `R8` amended; `RD-1`..`RD-4` (property 8, row-3 reader (b), §P1-13.7 read row, invariant 87) preserved verbatim with a handoff diff-check. Count kept as **22 replaced + 4 retained**, never summed.

**C — `R16`.** Two explicit variants: W-A three sealed endpoints (slots 3/4/6, `SOCK_SEQPACKET`), W-B two sealed pipes. This moved one blast-radius row **against W-A**. `E-D` re-proves the PCS retains the update-pipe write end under neither.

**D — filename.** `W-7`, v2 §1.1 and `O-8` withdrawn; §Z4.5 already superseded §W3.3's path at `…V2_1_1_CORRECTION.md:174`. Not reopened.

## Two things I corrected in the reviews themselves

X's determination 4 cites three loci that don't reproduce: `…CONTRACT_V2_3_1_CORRECTION.md:1353` (that file is 97 lines), `…V2_1_3_CORRECTION.md:298` (the sentence is in `V2_1_10_3`), and `…V2_1_3_CORRECTION.md:514` (already supervisor-only, retained). Recorded at §0.3; **no finding weakened** — each substantive determination is accepted and executed.

Counts: 62 governing loci replaced, 45 peer loci reopened (40 + 5 rename, verified disjoint), 7 files carrying replacement text, tests 92–110, tokens 6, new cells 0. W-B still recommended, unselected; `T NOT_ACTIVATED`; claim `OPEN`.
