Written to `reviews/opus_officina_wp3_population_contract_review.md`.

## Verdict: `REVISE_OFFICINA_WP3_CONTRACT`

The world-side design is coherent and charter-faithful, but the contract is **not bit-exact** — its own signed frame section prints an enumeration that contradicts its normative rule and would violate T/Q/C disjointness, and it is byte-exact only for the recommended CH-1a+CH-2a combination.

**The arithmetic counterexample — confirmed, Critical.** From the rule (`b_p={24+2p,25+2p}`, `j∈{2,4}`→Q), the Q-reserve is `{28,29,32,33,38,39,42,43,48,49,52,53,58,59,62,63}` — **exactly the prompt's implied set**. The draft §3 instead prints `{…,40,41,44,45,50,51,54,55,60,61,64,65}`, whose upper 12 worlds are `p∈{8,10,13,15,18,20}` — **C-frame blocks**. So the printed Q-reserve overlaps the C frame in **12 of 16 worlds**: the frame document isn't byte-reproducible (rule vs print diverge, SHA differs) and, taken literally, T/Q/C disjointness fails catastrophically (Q≡C). The rule is correct; the print is a transcription error; the rule-corrected partition is clean. I independently recomputed CH-2b (24 Q / 16 C, disjoint, N_h=2).

**Findings (anchored):**
- **W3-C1 (Critical)** — correct the printed Q-reserve to the rule set; add an enumeration table + machine-checkable `Q∩C=∅`.
- **W3-M1** — the contract is bit-exact only for CH-1a+CH-2a: the band→block formula is `[26,65]`-specific, and §4 hard-codes N_h=3/π_h=n_h/3/FPC/census (wrong for CH-2b, N_h=2). Parameterize both by the open cells.
- **W3-M2** — the `officina.frame.v1` canonical-JSON schema is unspecified (a promise to choose one later ≠ closure).
- **W3-M3** — typed-refusal byte + query wire format unpinned; PAD/SEP conflated with world semantics (they don't enter `disp` — serialization only).
- **W3-M4** — public moduli + "pure function of (n,query)" leave a caller-supplies-`n` route; the oracle must be surface-capability-gated (T→T-dev only) in WP-3 text.
- **W3-M5** — frozen T-dev bands `[10,25]∪[166,205]` are an unjustified, CH-1-non-scaling scale-extrapolation design; justify or make an author cell.
- **W3-M6** — public finite support + admitted divisibility solver narrow (not break) interpretability; extend §8 forbidden-language to bar "learned the construct / small-learner contact" claims absent a WP-6 admissibility rule.
- Minors on donor/B WP-9 deferral and the generic reserve bound.

**Other surfaces:** world/frame boundary clean except PAD/SEP; quarantine routes split correctly between WP-3 text (oracle gating) and already-closed WP-1/WP-2 code; no WP-6/WP-9 numeric accidentally fixed; **no stopped-Level-1 outcome tuning** (band/split/Λ derive from disjointness hygiene, strata arithmetic, the Λ pattern, and the resource envelope). Verifier OK; the WP-3 draft is not under `successor/officina/`, so the bootstrap set is untouched (0 files).

**CH-1/CH-2 are not yet reviewable for selection** — they become reviewable only after W3-C1/M1/M2 make the frame byte-exact for all four combinations. This authorizes **only a bounded Fable revision** — no author selection, WP-4, entropy, T activation, Q/C process, root, lock, escrow, datum, or outcome; the revised delta needs a fresh X/Y confirmation.

**Confirmed:** no existing file edited, one new review file, no cell/token selected, nothing committed; predecessor stays `OPEN`/`BLOCKED_LEVEL1_FEASIBILITY`, programme claim `OPEN`.
