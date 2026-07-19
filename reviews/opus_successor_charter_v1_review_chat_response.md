Written to `reviews/opus_successor_charter_v1_review.md`.

## Verdict: `REVISE_SUCCESSOR_CHARTER_V1`

The three-surface architecture is the right shape for Route B and is **not** blocked — a charter consistent with the five tokens is coherent. But one Critical and six Major charter-level defects would make two implementers and two reviewers build different phase boundaries and freeze orders.

**Critical**
- **X-A — the qualification surface is not actually unseen.** §4/§9 derive Q worlds "under the **public** dev-root" per attempt. Since the root and PRF generator are public, a candidate can precompute *all* future Q worlds, bake them into a frozen manifest, and "qualify" on worlds it has effectively seen — nullifying Route B's load-bearing innovation. Disjoint labels and frozen manifests don't help. **Fix needs no secrecy — only post-freeze unpredictability:** draw each attempt's Q seed (OS-CSPRNG, once) *only after* the candidate manifest is durably committed; publish it afterward. I proved the ordering both ways and gave the exact temporal/information contract.

**Major**
- **X-B** — lock/escrow order contradicts itself: §4/§9 say escrow root *after* lock; §5/§7 say escrow *before* lock. Lock-before-escrow is correct (no C realization may influence the spec); fix §5/§7.
- **X-C** — device/manifest immutability contradicts: §4/§5 freeze the stack at Q-attempt; §6 freezes it "at promotion," permitting qualify-on-X / confirm-on-Y. Every manifested field binds at the Q attempt; promotion carries it unchanged.
- **X-D** — the scout's "never effect direction" is rhetoric: per-arm censoring/variance/timing *encode* direction. Needs a signed, direction-blind schema (scale-of-difference + pooled rates + pooled resources) or drop the scout.
- **X-E** — the competence predicate numerics are set "before the first attempt" = after T reveals candidates → tunable around a favorite. Must be candidate-blind and signed before any candidate is registered.
- **X-F** — first-to-qualify is search-order exploitable without a pre-committed order; and "no Q fact beyond the binary in promotion" is unstated.
- **X-G** — "no automatic rerun" vs "individually recoverable" is crash-farmable: needs burned worlds, new-attempt-only recovery under signed disposition, and a separate bounded recovery ceiling.

**Minor:** X-H (the "separate repo is scientifically stronger" claim is overstated — the guarantee is the signed semantic quarantine, layout-independent; mechanically enforce a path-allowlist either way); X-I (the selection-conditional claim is honest, but its limitation must ride in the *estimand*, scoped to the promoted design, never the learner class).

I provided direct answers to A–I, a corrected executable phase/freeze-order table (reconciling B and C), exact replacement clauses R-A…R-I, the validly-deferred cells (the *numbers* stay open; the *rules* that keep them honest must be fixed now), and bounded final-confirmation questions.

**Tokens:** none signable as written — `I_ACCEPT_PHILOSOPHIA2_CHARTER_V1` and `..._THREE_SURFACE_PHASE_ARCHITECTURE` need the repairs (X-A most of all); `..._SELECTION_CONDITIONAL_CONFIRMATORY_CLAIM` is the one internally-sound token but should be signed with the repaired packet under R-I. All three become signable after R-A…R-I.

**Four questions for Kirill:** promotion variant; whether to keep the schema-constrained scout or drop it; repository layout (an author cell, not scientifically decisive); and the off-CPU breathing-check option.

**Confirmed:** no existing file changed, `essay/OUTLINE.md` untouched, one new review file created, nothing committed or executed; no learner/world/device/partition/promotion/repository chosen; the old censors were turned into evidence for no specific repair.
