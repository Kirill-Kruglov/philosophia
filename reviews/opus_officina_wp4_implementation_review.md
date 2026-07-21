# Opus 4.8 X-line — Officina WP-4 inactive implementation review

**`OFFICINA_WP4_XLINE_ACCEPTED_FOR_BOUNDED_NEXT_GATE`**

Reviewer: Opus 4.8 (X-line, adversarial implementation/fidelity). Repository:
`/home/master/llm_projects/philosophia`, WP-4 range `de8aa1e^..a8cbd91` (HEAD
`3555efe` differs only by review prompts). **I created no real world, entropy,
candidate, root, lock, escrow, datum, outcome, or T/Q/C execution; I did not
activate the committed T state; my probes used temporary test-only fixtures and
ledgers under `/tmp` only. Nothing committed; no existing file edited.** I ran
static recomputation, frame-mutation and capability attack batteries, a total
byte-string classifier probe, the four-file suite, the verifier, and
`git diff --check` (reported below).

The WP-4 world substrate is a faithful, fail-closed, **inactive** realization of
the signed WP-3 contract (LOW / C_RICH / OR-2 / transport): deterministic frame
generation bound to the signed contract+signature hashes with formula-recomputed
verification, a total ordered oracle wire classifier, capability-gated test-only
oracle contacts bounded to their surface modulus sets, and no real-execution
entry point of any kind. No Critical or Major finding; three Minor observations,
none blocking.

---

## Findings

### Critical / Major
None.

### Minor

- **W4-m1 — deliberate private-sentinel bypass grants only a test-only capability
  (`world.py:50,61-68`; item 4).** A caller importing `world._WORLD_TOKEN` can
  forge a `TestWorldCapability` (`TestWorldCapability(Surface.T,"test-only:x",
  world._WORLD_TOKEN)` succeeds in my probe). This is the **accepted
  accidental-execution threat model** (`interlock.py` docstring: "accidental-
  execution guard, not a security sandbox"), and the forged object grants **only**
  test-only, surface-modulus-bounded oracle evaluation — it cannot produce a real
  world, entropy, sample, or run, because **no real capability factory exists**
  (all four real routes raise). Honest and consistent; no repair required, noted
  for completeness.

- **W4-m2 — `record_test_t_contact` does not restrict the caller-supplied ledger
  path (`world.py:289-327`; item 6).** The hook appends to whatever
  `AppendOnlyLedger` is passed. In practice the committed production ledger is
  protected because it is `NOT_ACTIVATED`: `charge_device_nanoseconds` requires
  `activated_utc is not None` and refuses the inactive production state (verified —
  a contact against `TState()` raises `ValueError`). A deliberate misuse
  (activated dummy state + production ledger path) could append a **clearly
  test-only-labeled** entry (`event=T_TEST_ONLY_WORLD_CONTACT`, `test_only:true`,
  `schema=…test-t-contact.v1`) to the *working-tree* production ledger — a
  deliberate procedural act surfaced by the committed genesis + verifier + git,
  and the hook is explicitly "not a production transaction or a T activation
  path." **Recommendation (not a blocker):** the future T-activation driver — not
  this test hook — must own the real, durable production transaction; consider the
  hook asserting its ledger is not the production path.

- **W4-m3 — test-only Q/C surfaces are oracle-evaluation utilities, correctly
  documented (`world.py:70-78,206-220`; items 4-5).** `test_world_capability`
  accepts `Surface.Q`/`Surface.C` and produces test capabilities that evaluate the
  **pure public oracle** on the 16 Q / 24 C moduli. This does **not** violate
  WP-3 §4's "Q and C capabilities do not exist until their gates," which defers
  *realized-unit* access (post-freeze/post-lock roots): these test capabilities
  realize no sample, draw no root, and cannot enter a real run; they compute
  `disp≡disp (mod n)` for public moduli (the §6 construct-shortcut surface, already
  scoped). The WP-4 note states "T, Q, and C test surfaces enforce their signed
  modulus sets. No real surface-capability factory exists." Confirmed consistent.

---

## Item-by-item confirmation

1. **Signed frame recomputed — CONFIRMED.** `SIGNED_CONTRACT_SHA256` (`6085d9b6…`)
   equals the SHA-256 of the committed contract, and `SIGNED_WP3_SIGNATURE_SHA256`
   (`24fd12b6…`) equals the committed signature (both hashes independently
   recomputed True). `_validate_frame` recomputes every block from
   `p=5(h−1)+j`, `b={n0+2(p−1), n0+2(p−1)+1}` and requires `block == expected`
   (rejecting drift), then checks `Q∩C=∅`, `Q∪C=[26,65]`, frame/T/predecessor
   disjointness, per-stratum balance `{C:3, Q:2}`, and cardinalities `24/16`. I
   independently recomputed the 20 rows: C blocks `p∈{1,3,5,6,8,10,11,13,15,16,18,
   20}`, Q worlds `{28,29,32,33,38,39,42,43,48,49,52,53,58,59,62,63}` — match. The
   frame JSON is canonical, `contract_sha256`/tokens embedded, and
   `verify_frame_bytes(frame_bytes())` round-trips.

2. **Mutation / drift rejection — CONFIRMED.** A mutated `lambda` (141) and a
   non-canonical (spaced) payload are both rejected by `verify_frame_bytes`
   (`ValueError`); the verifier compares against the **formula-recomputed**
   `frame_bytes()` (not its own re-serialization of the input), so it cannot bless
   drift, and `_decode`/`_validate_frame` reject reordered/extra/missing/duplicate
   keys and internally inconsistent bytes.

3. **Total ordered wire classifier — CONFIRMED.** `_decode_query`
   (`world.py:240-264`) uses `json.loads(..., object_pairs_hook=_unique_object)`
   (duplicate keys → `_DuplicateKey`) then requires an exact `{u,v}` string object
   whose `canonical_json` equals the raw bytes, else `STRUCTURE`; then `BYTE` (any
   char ∉`{R,L}`); then `LENGTH` (>Λ=140); else the oracle answer. Probed with
   correct canonical bytes: valid→`0`/`1`, empty words→`1`, joint over-length+illegal
   byte→`BYTE` (clause 2 before 3), illegal-only→`BYTE`, over-length-only→`LENGTH`;
   `NaN`/`Infinity` (allow_nan=False + non-string), BOM, escaped `R`,
   non-ASCII Unicode, non-canonical spacing, missing trailing newline, wrong
   structure/type, duplicate keys → all `STRUCTURE`. Stateless (two identical calls
   agree); modular arithmetic `(disp_u−disp_v)%n==0` is correct for negative
   displacements. Refusal/answer bytes are exact canonical-JSON. (The canonical
   query form includes the WP-2 trailing newline; both conforming implementations
   agree.)

4. **Capability issuance/use — CONFIRMED.** `TestWorldCapability` is token-gated
   (`_WORLD_TOKEN`), exact-typed, and test-only-purposed; `_require_world_capability`
   rejects the direct constructor (no token → `PermissionError`), duck types and
   subclasses (`type() is not TestWorldCapability`), and altered purpose.
   `evaluate_test_query` rejects a caller-supplied out-of-surface modulus (a T
   capability + C modulus 40 → `PermissionError`). The only bypass is the
   accepted deliberate private-sentinel import (W4-m1), which yields only a
   test-only capability. **The public API honestly has no real capability
   factory** (`generate_real_world`, `run_real_t`, `launch_q`, `execute_c` all
   raise `ExecutionNotAuthorized`; `world.py` exports no real route; `__init__`
   exposes none).

5. **`_surface_moduli` bounds — CONFIRMED.** `T` = `[10,25]∪[166,205]` exactly;
   `|Q|=16`, `|C|=24`, `Q∩C=∅`; a contact is refused for any modulus outside the
   capability's surface set (`world.py:277`).

6. **`record_test_t_contact` — CONFIRMED (with W4-m2).** Requires a T capability
   (else `PermissionError`); `device_nanoseconds` must be a **positive int**,
   `bool` excluded (`type(x) is int` rejects `True` — verified) and `≤0` rejected;
   `parse_utc` validates the timestamp; order is validate → `evaluate_test_query`
   → `charge_device_nanoseconds` (which enforces active/not-stopped/not-exhausted/
   not-resume-pending) → atomic `ledger.append`; the event carries query/response
   SHA-256, `t_state`, and `test_only:true`; it is explicitly **not** represented
   as a crash-atomic production transaction, and the inactive production state
   blocks any charge.

7. **Fail-closed stubs — CONFIRMED.** `generate_real_world`, `run_real_t`,
   `launch_q`, `execute_c` all raise `ExecutionNotAuthorized`; there is **no**
   timer, learner loop, activation driver, real capability, durable real-world
   registry, or production execution entry point (verified in `world.py`,
   `interlock.py`, and the WP-4 note).

8. **Suite / verifier / diff / bootstrap — CONFIRMED.** The four-file suite →
   **63 passed**; `scripts/verify_officina_wp12.py` → **OK: quarantined and
   inactive**; `git diff --check de8aa1e^ a8cbd91` → clean; the committed
   `T_LEDGER.md` remains the `NOT_ACTIVATED` genesis skeleton and the exact
   `successor/officina/` bootstrap set is unchanged (0 changes). The
   source-quarantine import allowlist is unchanged and already covers `world.py`'s
   imports (`accounting, canonical, interlock, ledger, quarantine` + stdlib); the
   AST scanner (no `getattr`/`eval`/`exec`/entropy/dynamic imports) still passes on
   the new module.

## Checks run (read-only)

Independent SHA-256 recomputation of the signed contract and signature; frame
recomputation and hash round-trip; frame-mutation and non-canonical rejection;
capability battery (direct ctor, duck type, subclass, copied sentinel, out-of-
surface modulus); `_surface_moduli` bounds; a 13-case + arithmetic classifier
probe with correct canonical bytes; `bool`/positive-int and inactive-state
accounting probes; `pytest` (63 passed); `verify_officina_wp12.py` (OK);
`git diff --check` (clean); committed ledger-genesis and bootstrap-set inspection.

## Next gate

A positive verdict authorizes **only the preparation (drafting) of a separately
reviewed T-activation candidate** — the future driver that would supply the real
T-run capability, the activation ledger event, the device breathing-check gate,
and the durable production transaction — **subject to its own bounded X/Y review**
before any activation decision. It authorizes **no** T activation, real world,
entropy draw, E1/E2/E3 spend, candidate registration, learner run, Q contract or
attempt, root, lock, escrow, datum, or outcome. WP-6 (Q contract) remains a
separate downstream gate. The committed T state remains `NOT_ACTIVATED`.

## Negative space

The predecessor line remains immutable, `OPEN`, and `BLOCKED_LEVEL1_FEASIBILITY`;
its records are non-citable and chose no value here. Officina's T and Q can never
earn, kill, or boundary-label C1–C6; a future Q pass is a spendability gate fact
only; S is unavailable; only a valid, independently locked C execution may move an
Officina claim — within its selection-conditional, selected-frame (12-block C
frame of `officina.frame.v1`), orientation, device, and learner-seed scope, and
nothing wider. Test-only oracle contacts are non-citable engineering and never
scientific evidence. Censored/`UNKNOWN`/every invalid state are never success,
equivalence, a boundary, or learner impossibility. `PROOF_CORE`/`PROOF_STRONG`
remain earned by nothing; the programme claim stays `OPEN`.

I edited no existing file, created exactly one new file (this review), selected no
cell or token, activated no T state, and committed nothing. `essay/OUTLINE.md`
untouched. My actions were reading the code, tests, and note, and running the
read-only recomputation, probes, suite, and verifier above.

— Opus 4.8, X-line. No outcome is asserted or predicted in this document.
