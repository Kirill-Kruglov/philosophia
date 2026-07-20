# Opus 4.8 X-line — Officina WP-1/WP-2 hardening confirmation

**`REVISE_OFFICINA_WP12_HARDENING`**

Reviewer: Opus 4.8 (X-line, bounded hardening regression check). Repository:
`/home/master/llm_projects/philosophia`, reviewed diff `c6a41b2..6b6d55d`. **I
created no entropy, real world, model run, candidate registration, Q attempt,
lock, escrow secret, or outcome. Nothing committed; no existing file edited.** I
ran the targeted three-file suite, the verifier, `git diff --check`, and one
read-only reproduction using in-memory temp paths. HEAD (`955ecca`) differs from
`6b6d55d` only by review prompts.

The hardening closes **six of Sol's seven** counterexamples cleanly and preserves
every contract I previously accepted — **except** it introduces one reproducible
regression in exactly the surface I was told to scrutinize (the exhaustive
one-shot charge partition, via a public constructor that bypasses the charge
invariant). One bounded fix + a regression test, then a re-confirmation.

---

## The one blocking defect

### C-1 (Critical) — `record_pre_entropy_disposition` escapes the mandatory charge from `DRAW_ARMED`/`LAUNCHED`.

The refactor moved the old inline `_append` guard ("`DRAW_ARMED → TERMINAL` must
be `charged:true`, competence unset") into the new `record_q_terminal`, but the
new public `record_pre_entropy_disposition` appends a `TERMINAL` with
`charged:false, competence:null` **without any phase guard**, and `_append` now
permits `CLAIMED/DRAW_ARMED/LAUNCHED → TERMINAL`. So a caller who has **armed the
draw** (entropy imminent/drawn) or **launched** (already `charged:true`) can close
the attempt as **`charged:false`**, escaping the charge. This defeats Sol-4's
required "exclusive, total, durable partition" (pre-byte ⇒ no charge; first byte
or ambiguity ⇒ charged) and regresses the "non-gameable" one-shot path my prior
review accepted.

**Reproduced (read-only, temp paths):**
```
phase after arm_draw: DRAW_ARMED
BUG: pre-entropy disposition ACCEPTED from DRAW_ARMED -> charged=False
phase after launch: LAUNCHED
BUG: pre-entropy disposition ACCEPTED from LAUNCHED  -> charged=False  (contradicts launch charge)
```
The existing test `test_claimed_attempt_can_close_only_by_signed_pre_entropy_disposition`
asserts the "**only**" in its name but exercises **only** the `CLAIMED` happy
path; it never checks rejection from `DRAW_ARMED`/`LAUNCHED`, so the counterexample
is untested and live.

**Bounded fix (minimal):** guard the disposition to the pre-entropy phase.
```python
def record_pre_entropy_disposition(self, *, signature_id: str, reason: str) -> dict[str, object]:
    if not signature_id or not reason:
        raise ValueError("pre-entropy disposition must be signed and reasoned")
    events = self._events()
    if not events or AttemptPhase(str(events[-1]["phase"])) is not AttemptPhase.CLAIMED:
        raise ValueError("pre-entropy disposition is valid only from CLAIMED")
    return self._append(AttemptPhase.TERMINAL, { ... })   # unchanged payload
```
Then `CLAIMED → TERMINAL` is reachable only as the `charged:false` disposition and
`DRAW_ARMED`/`LAUNCHED → TERMINAL` only via `record_q_terminal` (`charged:true`),
restoring the exclusive/total partition. **Mandatory regression test:** assert
`record_pre_entropy_disposition` raises when the last phase is `DRAW_ARMED` or
`LAUNCHED` (extend the mis-named "only" test to verify the "only"). *(Optional
defense-in-depth: also have `_append` require `charged:true` on any
`DRAW_ARMED`/`LAUNCHED → TERMINAL` and `charged:false` on `CLAIMED → TERMINAL`.)*

This is a WP-1/WP-2 **closure blocker**; it is a two-line fix and does not reopen
any design cell.

---

## Eight-surface inspection (the other seven counterexamples are closed)

1. **Durable provenance & laundering (Sol-1): CLOSED.** `ArtifactLabel` gains a
   `certified` flag; raw native reads now **raise** in `PathPolicy.read_bytes`
   ("native reads require canonical ArtifactStore provenance"). The new
   `ArtifactStore` mediates **writes**, binding a content-hash-pinned, exact-key
   `.provenance.json` (with `parent_provenance_sha256`, `promotable`, `sources`)
   to each artifact; `read` fail-closes on missing/mismatched/malformed provenance
   and rejects any `promotable:true` record ("WP-1/WP-2 expose no promotable
   provenance authority"); `admit` (Q/C) requires `certified ∧ promotable`. Since
   **no** write path yields `promotable:true`, nothing can be laundered into Q/C.
   Copy-and-reopen now fails (no provenance record → raise).

2. **Pause/resume + overdue E3 (Sol-2): CLOSED.** `write_pause_checkpoint`
   requires active-available T and records `{path, sha256}` **recomputed from the
   files** (`_artifact_records`, `strict=True`); `verify_resume` recomputes every
   artifact hash (`_verify_artifacts`), verifies exact checkpoint/ledger keys,
   `resets_e3:false`, checkpoint hash, resolved path, and prior-ledger-head
   binding, and returns a **`ResumeGate`** whose `admit_work()` **raises while an
   overdue E3 review is due** and whose `complete_overdue_review()` must run first
   (and logs `T_REVIEW_COMPLETED`). `record_not_activated_maintenance` now requires
   a **pristine inactive** `TState()`. `from_mapping` is exact-key, exact-type, and
   **no longer coerces** (`int()`/`bool()` removed); the inactive invariant is now
   "exact pristine state" (no counters, candidates, review, or author-stop).

3. **Typed Q/C terminals (Sol-3): CLOSED.** `CScientificTerminal`
   (PASS/NULL/BOUNDARY/INSUFFICIENT/CENSORED) replaces the free C label, so a
   process/pause/invalidity spelling can no longer become a scientific terminal;
   `CTerminal.valid` requires a `CScientificTerminal` instance, invalid exposes
   none. `QTerminal` gains type checks + `to_mapping`/`from_mapping`; the journal's
   `record_q_terminal(QTerminal)` validates a typed terminal, requires a charged
   phase, and restricts `DRAW_ARMED` to charged `Q_INVALID`. (No C terminal is
   constructed — WP-9 type only.)

4. **Exhaustive one-shot partition & reset resistance (Sol-4): PARTIALLY CLOSED
   → C-1.** The external `AttemptRegistry` (own hash-anchored `HEAD.json`) mirrors
   every journal event and pins `(attempt_id, journal_head, phase)`; `assert_unused`
   blocks id reuse and journal `_events()` fails on suffix deletion (head
   mismatch) — both **confirmed by test and reproduction**. The `CLAIMED → TERMINAL`
   disposition exists. **But the charge partition is not total (C-1).**

5. **Typed dummy-only PRF (Sol-5): CLOSED.** `encode_component` prepends a type
   tag (`b"i"`/`b"s"`), so `1` and `"1"` no longer collide. `ProvidedKey` →
   `TestOnlyKey` with an unforgeable-by-accident `_token` (compare/repr-excluded)
   checked in `__post_init__` **and** in `CounterStream`; `dummy_key` is the only
   factory, and no production/Q root type exists. (The sentinel is a procedural
   guard, consistent with the stated threat model; there is no production key type
   to reach regardless.)

6. **Behavioral candidate normalization (Sol-6): CLOSED (schema); WP-6 owns the
   digest.** Schema v2 splits `provenance_commit` (40-hex) from
   `behavior_source_sha256` (64-hex) and adds `inert_metadata` restricted to the
   signed whitelist `{comments, display_name, packaging, serialization_order,
   timestamps}`. `canonical_behavior_manifest` **drops `provenance_commit` and
   `inert_metadata`**, and `candidate_id`/`behaviorally_equivalent` key on it, so an
   inert edit no longer consumes an E2 slot while any unknown top-level or inert
   field still raises (behavior-relevant by rejection). *WP-6 obligation:* the
   registration contract must **compute** `behavior_source_sha256` from the actual
   normalized behavior-bearing source, never trust a caller-asserted value
   (otherwise two different-behavior candidates could share a digest and
   under-charge).

7. **Exact/alias-aware verifier (Sol-8): CLOSED.** The AST scan now builds an
   import-alias map and resolves aliases before the entropy/dynamic-import check;
   adds `os.getrandom`, `secrets.randbelow`, and `__import__`/`importlib.import_module`
   detection; and enforces **fail-closed import allowlists** (`ALLOWED_ABSOLUTE_IMPORTS`,
   `ALLOWED_RELATIVE_IMPORTS`) so an unreviewed import fails. `verify_bootstrap`
   adds `T_LEDGER.md.head.json` to the exact file set. (The ledger gained an
   external hash-anchored head `T_LEDGER.md.head.json`, committed empty at genesis;
   a ledger without its head is invalid.)

8. **Absence of WP-3/WP-4/WP-6/WP-9 content: CONFIRMED.** No population
   frame/strata/weights/FPC (WP-3), no Q caps/`δ_Q`/spending/competence numerics or
   OS-CSPRNG mechanism (WP-6 — the journal still records only a caller root
   *commitment* and draws no entropy), no endpoint/margin/N/arms or real escrow
   (WP-9 — `CScientificTerminal` and escrow are types/building-blocks only), no
   real-T harness/metering (WP-4). The verifier's expanded entropy denylist matches
   are string literals, not call sites; committed T is `NOT_ACTIVATED`.

**Regression watch (as instructed):** the external heads (registry/ledger/journal
`HEAD.json`) are sound and tested; the one regression is the public constructor
`record_pre_entropy_disposition` bypassing the charge invariant (C-1). No other
new public constructor bypasses a claimed type: `TaggedArtifact`/`TestOnlyKey`
are token-gated, `CTerminal`/`QTerminal` are enum-typed, `TState` is
exact-type-checked.

---

## Tests and verifiers run

- `pytest tests/test_officina_{accounting,bootstrap,governance}.py` → **38 passed**
  (up from 22; the new tests assert the positive paths and several counterexamples
  — laundering, suffix-reset, overdue-resume, typed terminals — but **not** the
  C-1 disposition-from-`DRAW_ARMED`/`LAUNCHED` rejection).
- `scripts/verify_officina_wp12.py` → **OK: quarantined and inactive**.
- `git diff --check c6a41b2..6b6d55d` → **clean**.
- Read-only reproduction of C-1 via `AttemptRegistry`/`OneShotJournal` on temp
  paths (no entropy, no real surface) → **charge-escape confirmed** from both
  `DRAW_ARMED` and `LAUNCHED`.

## Disposition

**WP-1/WP-2 may not close** on `6b6d55d`. Apply the C-1 bounded fix + regression
test, then a focused X/Y re-confirmation of the exact delta. All other hardening
repairs (Sol-1/2/3/5/6/8 and the external-head/reset-resistance half of Sol-4) are
accepted and need not be reopened; the WP-6 `behavior_source_sha256`-computation
obligation stands as a later cell, not a WP-2 blocker. This review authorizes
nothing beyond the existing signature — no implementation beyond the C-1 fix, no
entropy, T activation, real world, Q/C execution, lock, escrow, or outcome, and it
does not open WP-3.

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
reading the diff and running the read-only tests, verifier, diff-check, and C-1
reproduction above.

— Opus 4.8, X-line. No outcome is asserted or predicted in this document.
