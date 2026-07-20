Written to `reviews/opus_officina_wp3_v2_1_final_confirmation.md`.

## Verdict: `OFFICINA_WP3_V2_1_XLINE_CONFIRMED_FOR_AUTHOR_SIGNATURE`

Both bounded corrections I flagged and the optional wording are landed exactly; the diff is contained to the five authorized families; every previously confirmed frame/capability/ownership/token cell is unchanged.

**The seven items:**
1. **Total, ordered classifier — confirmed.** §4 specifies `STRUCTURE → BYTE → LENGTH → answer` (first match governs). I implemented it and probed 13 edges — each resolves to exactly one outcome: invalid/non-canonical/missing/extra/duplicate/non-string/non-ASCII → STRUCTURE; illegal byte / PAD/SEP → BYTE; over-length → LENGTH; **joint over-length+illegal-byte → BYTE**; empty word → valid. Stateless, deterministic → byte-identical transcripts.
2. **Raw decoding cleanly separated from the mathematical oracle** (oracle never sees raw bytes or emits refusals); PAD/SEP route to BYTE, never oracle-visible; capability invariant textually unchanged.
3. **v1 path fixed** — v2.1 references the existing `…_V2_DRAFT.md`; the stale path is gone.
4. **`contract_sha256`** pins the exact committed v2.1 bytes named in the signature record, acyclic, tokens as separate fields.
5. **T-dev wording softened** accurately ("crosses the frame's full internal scale range… no claim it avoids scale transfer"); bands and cells unchanged.
6. **Containment holds** — §2/§2a frame formulas and regression vectors byte-identical; capability invariant unchanged; all eight author token strings identical; §9 ownership changed only to add the C-randomization entries (no reassignment); §10/§11 only process wording. The two Sol families (C-randomization, `H_preC`) are contained and touch neither the frame bytes nor the capability invariant — their statistical adjudication is Sol's line.
7. **Verifier green**, bootstrap set unchanged (0 files under `successor/officina/`).

**Both Opus questions — Yes / Yes** (classifier total and byte-reproducible; path + `contract_sha256` correct, unambiguous, acyclic).

**Packet eligibility:** the five-token packet is unchanged and the contract is now bit-exact on every X-line surface. **From the X-line, it is eligible for Kirill's informed selection/signature** (`I_ACCEPT_OFFICINA_WP3_POPULATION_CONTRACT` + one CH-1 + one CH-2 + one OR + the transport token) — **contingent, per the dual-line gate, on Sol's parallel confirmation** of the C-randomization/`H_preC` families its line owns. This authorizes **only** those author tokens — no WP-4, entropy, T activation, world generation, Q/C process, lock, escrow, datum, or outcome; no qualification or direction predicted.

**Confirmed:** no existing file edited, one new confirmation file, no cell/token selected, nothing committed; predecessor stays `OPEN`/`BLOCKED_LEVEL1_FEASIBILITY`, programme claim `OPEN`.
