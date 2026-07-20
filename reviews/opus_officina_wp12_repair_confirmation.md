# Opus 4.8 X-line — Officina WP-1/WP-2 repair confirmation

**`OFFICINA_WP12_XLINE_REPAIR_CONFIRMED`**

Reviewer: Opus 4.8 (X-line, focused repair confirmation). Repository:
`/home/master/llm_projects/philosophia`, reviewed diff `fe9a982..bd61cf9`. **I
created no entropy, real world, model run, candidate registration, Q attempt,
lock, escrow secret, or outcome. Nothing committed; no existing file edited.** I
ran the targeted three-file suite, the verifier, `git diff --check`, and read-only
`/tmp`/pytest-temp reproductions of every counterexample. HEAD (`416ed5d`) differs
from `bd61cf9` only by review prompts.

The repair closes my C-1 **and** Sol's four additional live families, each now
fail-closed with a reproduction and a committed regression test, without
regressing any previously accepted contract or touching a deferred WP-3/WP-4/WP-6/
WP-9 cell.

---

## C-1 (my blocker) and the journal charge/type partition — CLOSED

The transition table now runs a **central `_validate_transition`** that couples
event kind ↔ predecessor phase ↔ exact payload schema, and it is applied **both on
write (`_append`) and on replay (`_events`)**, so hand-forged event files are also
rejected. Reproduced (temp paths, no real surface):

- `record_pre_entropy_disposition` from `DRAW_ARMED` → **ValueError**; from
  `LAUNCHED` → **ValueError** (it now guards `previous is CLAIMED`).
- Direct `_append(TERMINAL, charged:false)` from `LAUNCHED` → **ValueError**
  ("charged Q terminal payload differs").
- `LAUNCHED`/`DRAW_ARMED` can terminate **only** as a charged, canonically
  round-tripped `QTerminal` (`record_q_terminal` requires `type(t) is QTerminal`
  then reconstructs via `from_mapping`; a duck-typed object with a malicious
  `to_mapping()` → **TypeError**; `DRAW_ARMED` restricted to `Q_INVALID`).
- `CLAIMED` retains **exactly one** uncharged route — the signed-disposition-shaped
  `charged:false, competence:null, PRE_ENTROPY_STOP` terminal; `record_q_terminal`
  from `CLAIMED` → **ValueError**.

So "pre-byte ⇒ no charge (CLAIMED disposition)" vs "first byte or ambiguity ⇒
charged typed Q record" is now an exclusive, total, durable partition, enforced on
both write and read. Regression tests present:
`test_pre_entropy_disposition_is_rejected_after_draw_boundary`,
`test_launched_attempts_are_always_charged_and_typed`,
`test_q_journal_rejects_duck_types_subclasses_and_malicious_payloads`,
`test_claimed_attempt_can_close_only_by_signed_pre_entropy_disposition`.

## Sol family 2 — pending resume state & time monotonicity — CLOSED

`TState` gains `resume_review_pending`; `charge_device_nanoseconds`,
`register_candidate`, and `complete_review` all **refuse while it is set**
(reproduced: both charge and register → **ValueError** on a pending state).
`verify_resume` now computes `due = review_due(...)` and returns
`replace(state, resume_review_pending=due)`, so the raw resumed state — not just
`admit_work()` — rejects work; `admit_work` refuses on `review_required` **or**
`resume_review_pending`; and `complete_overdue_review` clears the flag only in the
same durable transaction that appends `T_REVIEW_COMPLETED`. Timestamp monotonicity
is enforced: `parse_utc` requires exact canonical UTC-second-Z; `record_operational_pause`
requires `pause ≥ activation/last-review`; `verify_resume` rejects `resume < pause`;
`complete_overdue_review` rejects `review < resume` and re-checks due-ness.
Regression tests: `test_overdue_resume_blocks_work_until_durable_review`,
`test_pause_resume_and_ledger_timestamps_cannot_move_backwards`,
`test_resume_refuses_artifact_identity_failures`.

## Sol family 3 — recursive externally-registered provenance — CLOSED

Promotability is now **structural**: `ArtifactLabel.promotable` is a `@property`
returning `False` (no field to set), so `require_promotable` **always raises** for
Q/C (reproduced on both a fixture and a certified native label). The token-bearing
`TaggedArtifact` is replaced by a plain `ArtifactView` that "conveys no write or
promotion authority," so there is nothing to copy for authority. A new external
`ProvenanceRegistry` (own hash-anchored `HEAD.json`, directory-exactness,
path-uniqueness) records every write; `read` calls `registry.require_exact(record)`
and then **recursively re-reads and re-verifies each parent** (visited-set cycle
guard) and requires `set(sources)` to equal the parents' union (or
`{"test-only-native"}` if none). Reproduced: a same-path relabel from
`test-only-native`→`engineering-fixture` with a recomputed self-hash is **rejected**
("artifact provenance differs from registry"). `write_derived` re-reads parents by
path rather than trusting caller-carried objects.

## Sol family 4 — opaque issued dummy PRF identity — CLOSED

`dummy_key` returns a private `_TestOnlyKey` (constructed via `object.__new__`,
recorded in an issuance `WeakSet`); the **public constructor is dead**
(`_TestOnlyKey(...)` → **PermissionError**). A centralized `require_test_only_key`
(exact `type` + issuance-set membership + 32-byte material) is called from
**both** `prf_digest` and `CounterStream.__post_init__`. Reproduced: a duck-typed
object with `_material=b"x"*32` → **PermissionError** in `prf_digest` and
`CounterStream`; the public key constructor → **PermissionError**. There is no
reusable authority token and no public raw-material constructor; the type tag keeps
`1`≠`"1"` and no production/sealed-root type exists.

## Sol family 5 — exact / reflection-aware verifier genesis — CLOSED

`verify_bootstrap` now compares the committed `T_LEDGER.md` to the **exact** canonical
`HEADER` bytes (not a substring) and its head to the canonical genesis payload
(imported `GENESIS`/`HEADER`/`HEAD_SCHEMA`). `verify_source_quarantine` adds
`getattr`, `eval`, `exec`, `compile` to the reflective/dynamic-call set and flags
`/dev/random`/`/dev/urandom` string constants. Reproduced: a source using
`getattr(os,'urandom')` and `open('/dev/urandom')` yields
`['reflective or dynamic call getattr…', 'system random device /dev/urandom…']`.
(The officina source itself uses none of these, so the verifier still passes on the
tree.)

---

## Regression watch (no accepted contract reopened)

This diff touches only the eight governance-primitive modules + tests + the WP
doc. It does **not** touch `manifest.py` (accepted candidate normalization intact),
`terminal.py`'s `CScientificTerminal` enum (accepted, still closed and used only as
a type), or any scope/deferred-scientific cell — no frame, entropy source,
production key, Q/C numerics, endpoint, margin, real-T meter, world, candidate, or
outcome is added. The structural removal of the `promotable` field is the intended
"no promotion authority in WP-1/WP-2" posture, not a regression (nothing relied on
`promotable:true`). The standing WP-6 obligation — that a real registration must
*compute* `behavior_source_sha256` from the normalized source rather than trust a
caller-asserted digest — remains a later cell, not a WP-2 blocker and not part of
this diff.

## Tests and verifiers run (read-only)

- `pytest tests/test_officina_{accounting,bootstrap,governance}.py` → **45 passed**
  (up from 38; the new tests pin the disposition/charge partition, duck-typed Q
  terminal rejection, overdue-resume block, timestamp monotonicity, and artifact
  identity failures).
- `scripts/verify_officina_wp12.py` → **OK: quarantined and inactive**.
- `git diff --check fe9a982..bd61cf9` → **clean**.
- Read-only reproductions confirmed fail-closed: C-1 disposition after the draw
  boundary, direct `_append` uncharged terminal, duck-typed Q terminal, PRF fake
  key / dead constructor, structural non-promotability, same-path provenance
  relabel, resume-pending charge/register, and the verifier's `getattr`/`/dev/urandom`
  detection.

## Disposition

**WP-1/WP-2 are confirmed closed**, and **WP-3 drafting is permitted** — the WP-3
population/construct contract may be **drafted only** as a reviewable document.
This confirmation authorizes **nothing** downstream: no entropy, T activation, real
world, candidate registration, breathing-check qualification, Q or C execution,
lock, escrow secret, data, outcome, or claim movement. WP-3 is itself independently
X/Y-reviewed and author-signed before any real T world exists; WP-4/WP-6 and every
later gate keep their own review and signature. The `interlock.py` raising stubs and
the CI quarantine verifier remain the fail-closed floor.

## Negative space and confirmation

The predecessor line remains immutable, `OPEN`, and `BLOCKED_LEVEL1_FEASIBILITY`;
its C1 unrun and untested; v1/v2 non-comparable, non-citable, and choosing nothing
here. Officina's T and Q can never earn, kill, or boundary-label C1–C6; S is
unavailable; only a valid, independently locked C execution may move a successor
claim, within its selection-conditional scope. Censored/`UNKNOWN`/every invalid
state are never success, equivalence, a boundary, or learner impossibility. This
review moved no scientific claim and created no world, entropy, candidate, run, Q,
lock, escrow, or outcome; `PROOF_CORE`/`PROOF_STRONG` remain earned by nothing and
the programme claim stays `OPEN`.

I edited no existing file, created exactly one new file (this review), selected no
open cell, and committed nothing. `essay/OUTLINE.md` untouched. My actions were
reading the diff and running the read-only tests, verifier, diff-check, and the
reproductions above.

— Opus 4.8, X-line. No outcome is asserted or predicted in this document.
