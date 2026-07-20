Written to `reviews/opus_officina_wp12_implementation_review.md`.

## Verdict: `OFFICINA_WP12_XLINE_ACCEPTED`

A faithful, conservatively-scoped, **self-verifying** WP-1/WP-2 implementation. No Critical or Major finding; the few Minors are genuine WP-4/WP-6 obligations, not defects, and none blocks WP-3 drafting.

**The six attacks:**
1. **Quarantine — sound.** `PathPolicy` realpath-resolves before deciding, denies by default, hash-pins read-only/T-only fixtures, propagates non-promotability into a Q/C block; warm-start is doubly prevented (path deny + mandatory `from-scratch` init); **source-import quarantine is AST-enforced in CI**; same-repo audit ancestry works via hash pins with `runtime_inheritance: forbidden`.
2. **Bootstrap — sound.** Canonical manifests, authorization+charter+predecessor pins, exact six-file set, `activated:false`, empty-but-parseable ledger.
3. **One-shot — sound, draws zero entropy.** `arm_draw` is durable before the caller's draw, so any `DRAW_ARMED→TERMINAL` is *forced* charged/competence-unset; no path to entropy without a durable charge; no redraw/fallback/silent-retry; `LAUNCHED` records only a root *commitment*.
4. **Durability — sound.** `atomic_create` (O_EXCL→fsync→`os.link` no-replace→fsync dir), hash-chained flock-serialized append-only ledger with full tamper detection, and a correctly-ordered pause protocol (checkpoint-then-entry, prior-ledger-head binding, resume-refuses-mutation, no fictitious checkpoint when inactive).
5. **Identity/interlocks — sound.** Exact manifest field set (unknown fields raise), mandatory from-scratch init, idempotent same-id registration; **every real T/Q/C route is a raising stub**; invalidity can't carry a scientific field.
6. **Scope — faithful.** No WP-3/WP-6/WP-9 cell smuggled in — primitives + inactive bootstrap only.

**Tests/verifiers run (read-only):** officina tests **22 passed**, full suite **189 passed** (no regression), `verify_officina_wp12.py` → **OK: quarantined and inactive**; entropy grep clean (matches were the CI denylist); no stopped-line imports; CI runs the verifier on every push.

**Minors (later obligations, non-blocking):** W-1 WP-6 `code_commit` normalization semantics; W-2 WP-6 signed-disposition annotation of a dangling pre-entropy `CLAIMED`; W-3 WP-4 exhaustion check before each real-T quantum; W-4 the accepted procedural-threat-model TOCTOU boundary.

**May Codex close WP-1/WP-2 and begin WP-3?** **Yes** — with this and Sol's review, Codex may close WP-1/WP-2 and begin **only the drafting** of the WP-3 population/construct contract (a reviewable document), with **no** real world, entropy, T activation, candidate, breathing check, Q, lock, or escrow; WP-3 is itself independently reviewed and author-signed before any real T world exists.

**Confirmed:** no existing file edited, one new review file created, no open cell selected, nothing committed or run beyond read-only tests/verifier; the predecessor stays immutable/`OPEN`/`BLOCKED_LEVEL1_FEASIBILITY` and the programme claim `OPEN`.
