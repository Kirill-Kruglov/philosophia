Now the decisive audit for I-1: where `active_lease_sha256` is evaluated.

The audit resolves decisively. Writing the v2.3 correction.

Both deliverables written. Nothing existing modified, nothing committed.

```text
832d31693d719a43198544807ffa74c96c88fb55d82bfb4ce70ef9fd265643e3  successor/OFFICINA_P1_PROCESS_CLAIM_IDENTITY_AUTHOR_CHOICE_PACKET_V2_3_CORRECTION.md
55e19217502c7f217f3ec1768f4db122abd14d4ef22c315d76fde38dac790633  reviews/opus5_officina_p1_process_claim_identity_choice_v2_3_closure.md
```

**Closure verdict: `READY_FOR_OFFICINA_P1_IDENTITY_V2_3_FINAL_XY_CONFIRMATION`** — no blocker was needed.

**The I-1 audit resolved on the bytes, not by choice.** `active_lease_sha256` is evaluated **inside** the five production roots. Three signed loci compose: `contract :116-124`/`batch :93-97` put it in heartbeat settlement; `contract :576` assigns "§4 reservation/**settlement**/batch/conservation" and the `heartbeat` CLI to `src/philosophia/officina/generic_harness.py`, with `:517-522` foreclosing any other entry point; `contract :505-514` and `composite :349-357` both make that file a production root. So X R-5 resolves in its first branch: `EV-3` is a real third evaluation, `C-6` a real sixth consumer, and v2.2's `DC-6′` ("no other digest of a claim, a **lease**, an occupant exists in the five roots") was false on signed bytes. The lease install is likewise in-root, so `MS-13` was required.

**Six repairs, one per residual.** (D) Both records pinned symmetrically — `PA-1′` two root literals, `MS-1L`/`lease_path`, `MS-13`, `MS-14`, `CR-2′` five carriers, `M-R4′` five producers, `PC-R1′` withdrawing "only claim paths are restricted", `R-d′` withdrawing the fixture that certified the leak. (E) `PA-6′` separates write calls from read calls, `PA-4′` counts uses at call sites, `PA-5′(b)`/`PA-3′(b)` admit constant and no-stem paths, and `MS-2` becomes descriptor-anchored — which turned out to be importing `protocol :58-72`'s already-signed `samestat` discipline that v2.1's `open(path,"rb")` row had silently dropped. (F) `PT-1′` narrowed to pathname denotation, `CA-1`..`CA-5` named as one open external residual, and `PG-1`..`PG-7` + `S-25p` containing the consequence — including the point that `samestat` *cannot* catch a hard link because it is the same inode, so `st_nlink == 1` is a genuinely new conjunct, priced separately at `B-A8`. (G) `EV-3`/`C-6`/`LD-1..3`. (H) `CS-4′`/`WL-3″`/`CS-8` — no confidentiality **guarantee**, ≤ 4,194,304 only given the other eighteen fields, and explicitly no claim in either direction for a reader without them. (I) `D-14′` relabels `PA-7` as local single-assignment **plus a one-hop callee lookup**.

Counts re-derived: 6 consumers, 5 accessors, 16 rules, 26 tests, 5 carriers, 15 call sites, 3 evaluations, **2 direct destinations unchanged**, 5 continuations unchanged, 15 handoff steps.

Two things a reviewer should hit hardest, and I've flagged both: `PG-4` is a runtime predicate that `S-25p` can only position-check, not verify — a real, disclosed weakening of the all-static property; and `EV-3`/`C-6` rest entirely on my reading of `contract :576` as normative.
