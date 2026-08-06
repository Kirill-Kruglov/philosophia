A few remaining stale prose references and the §2.3 locus map. Fixing them.

Now handoff v5, then the packet and closure.

Now the packet v2.14.

Now a full verification pass over all five deliverables before writing the closure.

One check flagged — let me diff the Cell 1 block to confirm exactly what changed there.

Exactly one line — the generation self-identification required by the no-predecessor rule; the blocking notice and every operative Cell-1 clause are byte-unchanged. Now the primitive-surface diff for the closure.

All figures verified. Writing the closure.

Done. All six deliverables created; nothing committed.

## Verdict

`READY_FOR_OFFICINA_P1_WB_V2_14_FINAL_XY_REVIEW`

All eight pinned inputs matched before work and were re-verified byte-unmodified after.

## The divergence, settled by reproduction

I reproduced each Sol Major from the governing bytes before repairing it, rather than accepting either line's authority:

- **Y-M1** — built the v1.13 rules as an executable model: the Y counterexample returns `T1` for order `[a,b]` and `T3` for `[b,a]`. Over the same-phase pair matrix, **2 of 9 ordered pairs are order-dependent before, 0 after**.
- **Y-M2** — the live-leader `TIMEOUT` gives `P-2` = *(WRITE, H-GROUP-RECORDED, 1)* and `P-10` = *(NO WRITE, H-NULL-GROUP, 0)*. Single-valued after.
- **Y-M3** — swept `81` across v1.13: exactly **two** live accounting literals (rows 105, 106); the other eight are digest substrings or row indices.
- **Y-M4** — confirmed all five steps of the reachability proof; `§P1-3.4` bound 26 `os` names, neither `_getsid` nor `_getpgid`.

On the one clause the lines graded differently, the stricter grade governs — and Fable's own §10.3 says the defect must be repaired before any scaffold authorization. They differ on *when*, not *whether*.

## Repairs

R1 makes Phase 4 a closed scan (`4A`) plus a total reduction (`4B`) under *structural violation > forbidden target* with a least-index tie-break; Phase 6 carries the equivalent; Phases 1/2/3/5 are proved collision-free exhaustively. R2 conditions population on `outcome == STOPPED` under a pinned `K1..K6` step order. R3 recounts **MS-2 71→75, members 85→89, provenance 79→83, digests 78→82** — all 82 verified against files on disk. R4 binds `_getsid`/`_getpgid`; `S-3`/`S-5`/`S-6`/`S-7` block is byte-identical, and `MS-11`'s closure is untouched because a binding is not an import.

All twelve logged items dispositioned one-to-one. Transform recomputed: 11 spans, `627683 − 21237 + 18394 = 624840`; guarddata byte-unchanged; MP-1 now reproduces from its own recipe (X-L4).

## Two things worth flagging

**An author-found defect neither line reported.** Amendment v1.10 §A0 asserted all five generation-scoped strings named that generation, listing OR-4's *"the v1.10 amendment is installed"*. Both files actually read **v1.9** — a false audit sentence in exactly the class both lines have been catching. Binding v4 §5.3 F3 repeated it. Repaired, and the claim is now verified mechanically rather than asserted.

**X-L7 resolves the other way this generation.** Fable was right that row 106 didn't move in v2.13. It *does* move now, because Y-M3's second half lands there — so the dependent-literal list includes it on merits.

Resolved bytes and MP-1 were built in memory and discarded; no resolved file exists at any path, and `_getsid`/`_getpgid` were never called. `T = NOT_ACTIVATED`, claim `OPEN`, v1.11 token not signable from this round.
