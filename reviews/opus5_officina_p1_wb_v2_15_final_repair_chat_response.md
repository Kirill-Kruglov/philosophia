Now installing the four governing/binding deliverables and writing the packet and closure.

Done. All eight pinned inputs recomputed and matched — not `BLOCKED`. Six deliverables created, nothing committed, no existing file modified.

## Deliverables

| File | Bytes | SHA-256 |
|---|---|---|
| [packet v2.15](successor/OFFICINA_P1_WATCHDOG_FREEZE_AUTHOR_CHOICE_PACKET_V2_15_CORRECTION.md) | 28791 | `6a00e058…f26a` |
| [amendment v1.12](successor/OFFICINA_GENERIC_HARNESS_WATCHDOG_FREEZE_AUTHORITY_AMENDMENT_V1_12_DRAFT.md) | 314994 | `e156d662…f4a8` |
| [composite v1.15](successor/OFFICINA_GENERIC_HARNESS_SUPERVISOR_CONTROL_CHANNEL_P1_OPERATIVE_COMPOSITE_V1_15.md) | 668002 | `a41c1424…113a` |
| [binding v6](successor/OFFICINA_P1_WB_POST_SELECTION_BINDING_V6_DRAFT.md) | 102351 | `c9db32bb…2ff2` |
| [handoff v6](successor/OFFICINA_P1_WB_IMPLEMENTATION_HANDOFF_V6_DRAFT.md) | 47240 | `279f59a2…c1f1` |
| [closure](reviews/opus5_officina_p1_wb_v2_15_final_repair_closure.md) | — | recomputed by the reader |

Verdict in the closure: `READY_FOR_OFFICINA_P1_WB_V2_15_FINAL_XY_CONFIRMATION`.

## What the repairs did

**R1** — `KG-2` `P-2`'s four-conjunct `iff`, the `K1..K6` order and the two-table `P-9`/`P-10` split are withdrawn. `P-2` is now an ordered machine `W0..W8` with nine disjoint routes; `W0` pins handle existence, generation, role eligibility and the **prior-write boolean** before any observation; EINTR and deadline exhaustion live *inside* `W4` (which is what removed the overlap Sol demonstrated); `W6` is the named linearization point `L`. Atomicity comes from `P-3` + `§P1-8.4` + `§P1-3.2` + `§P1-8.6` — no new writer invented; the prior-write-at-`L` route is proved unreachable rather than explained away.

The published row predicates were transcribed independently of the machine and driven over all **110592** combinations: **0 with no route, 0 with two, 0 machine/guard disagreements, 4 writes all via `R-H`**. Both Y14-M1 counterexamples now resolve to `R-D`/`R-A0` and `R-F`.

**R2** — handoff v6 carries one current-authority table (every path paired with its own digest) and one precedence rule over current files only. `D-6` derives 93 from this generation and requires it to **pass**; the negative list is the seven retired values `63, 69, 73, 77, 81, 85, 89` at all three loci (`D-6`, `T-14`, `PR-4`), with no look-ahead value.

**R3** — the handoff region was extracted independently from each governing file *after* every other change; byte identity holds; both files now carry the measured `29a6d7e3…7bb4` / 4168 bytes. Neither `7c5cabe2…` nor v2.14's `7d5cd453…` is carried as authority.

**R4** — Phase 3's five terminal-bearing predicates enumerated with a total two-step reduction; the watchdog self-collision closed at the `KG-2` eligibility gate (lifecycle preserved, `§P1-8.3` not narrowed); the tie-break replaced with least `handle_id`.

**R5** — measured recount MS-2 75→79, MS-8 89→93, provenance 83→87, digests 82→86 (all 86 verified against disk); complete new transform, reproduced independently from binding v6's own fenced blocks: `668002 − 27262 + 24419 = 665159`, output `e9577809…34be`, guarddata byte-unchanged at 1816 bytes, MP-1 at 665354 / `6cbd6e2d…c09b` failing `PO-0`.

## Two things worth flagging

I found and repaired **six further stale literals reported by neither line**, all declared in the packet §6.4 and closure §7.2: amendment v1.11's `DA-4` named the *v1.10/v1.13* pair as the two **live** specification surfaces (a normative delegation of exactly the `Y14-M2` class); its §A9 preamble and five-locus audit note named the wrong generation; its §A0.4 said the anchor token occurred *seven* times where the bytes said six; its `N-14`/`N-16` carried MS-2 71 / MS-8 85 / provenance 79; and handoff v5's `§H4` and `T-10` carried **v4-era** resolved `H_BODY`, `H_NORMATIVE` and MP-1 digests against binding v5's own figures.

I also treated Fable's `X-1` as governing and repaired it, notwithstanding that review's own gate. The reasoning is in the closure §4: the consumption analysis is accepted, but the pair's own clause calls any difference a defect, and a false normative sentence is not kept on the strength of not being load-bearing.

`T = NOT_ACTIVATED`; programme claim `OPEN`; `OR-4` not executed; no resolved bytes at any path.
