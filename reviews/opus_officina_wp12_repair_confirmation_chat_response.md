Written to `reviews/opus_officina_wp12_repair_confirmation.md`.

## Verdict: `OFFICINA_WP12_XLINE_REPAIR_CONFIRMED`

The repair closes my C-1 **and** Sol's four additional live families — each now fail-closed with a reproduction and a committed regression test, with no accepted contract regressed and no deferred cell touched.

**C-1 + journal charge/type partition — closed.** A central `_validate_transition` couples event kind ↔ predecessor phase ↔ exact payload schema, enforced on **both write and replay**. Reproduced: disposition from `DRAW_ARMED`/`LAUNCHED` → ValueError; direct `_append` uncharged terminal → ValueError; `LAUNCHED` closes only as a charged, canonically round-tripped `QTerminal`; duck-typed Q terminal → TypeError; `CLAIMED` retains exactly one signed-disposition uncharged route. The pre-byte/post-byte charge partition is now exclusive, total, and durable.

**Sol's four families — closed:**
- **Family 2 (resume/time):** `TState.resume_review_pending` blocks charge/register/complete_review; `verify_resume` marks the returned state pending when review is due and rejects `resume < pause`; monotonicity enforced across pause ≥ activation, resume ≥ pause, review ≥ resume with exact canonical UTC. Reproduced: charge/register on a pending state → ValueError.
- **Family 3 (provenance):** promotability is now **structural** (`promotable` is a property returning `False` → `require_promotable` always raises for Q/C); the token-bearing artifact is replaced by an authority-free `ArtifactView`; an external `ProvenanceRegistry` with `require_exact` + recursive parent verification + source-union check. Reproduced: same-path relabel/re-hash → rejected.
- **Family 4 (PRF):** dead public `_TestOnlyKey` constructor; centralized `require_test_only_key` (type + issuance WeakSet) in both `prf_digest` and `CounterStream`. Reproduced: fake duck key and public constructor → PermissionError.
- **Family 5 (verifier):** exact ledger-genesis bytes; `getattr`/`eval`/`exec`/`compile` + `/dev/*random` detection. Reproduced: `getattr(os,'urandom')` + `/dev/urandom` flagged.

**No regression:** the diff doesn't touch `manifest.py` (candidate normalization intact) or `terminal.py`'s C enum; no WP-3/4/6/9 content added; the `promotable`-field removal is the intended "no promotion authority" posture. The standing WP-6 obligation (compute, don't trust, `behavior_source_sha256`) remains a later cell.

**Ran (read-only):** targeted suite **45 passed** (up from 38), verifier **OK**, `git diff --check` **clean**, plus reproductions of every counterexample now failing closed.

**Disposition:** WP-1/WP-2 are **confirmed closed**; **WP-3 drafting is permitted** (a reviewable document only). This authorizes nothing downstream — no entropy, T activation, real world, candidate, breathing check, Q/C execution, lock, escrow, data, outcome, or claim movement; WP-3 is itself independently reviewed and author-signed before any real T world exists.

**Confirmed:** no existing file edited, one new review file, no open cell chosen, nothing committed or run beyond read-only tests/verifier/reproductions; predecessor stays `OPEN`/`BLOCKED_LEVEL1_FEASIBILITY`, programme claim `OPEN`.
