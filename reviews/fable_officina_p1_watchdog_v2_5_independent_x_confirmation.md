OFFICINA_P1_WATCHDOG_V2_5_INDEPENDENT_X_CONFIRMED_FOR_AUTHOR_SELECTION

# Officina P1 watchdog-freeze v2.5 — independent X-line confirmation

**Reviewer.** Claude Code, model `claude-opus-4-8` (Opus 4.8), fresh session.
Bounded independent engineering audit of the closed-member-set and
external-trust repair. No redesign performed. **No existing file was modified,
no key or artifact was generated, and nothing was committed.**

**Verdict.** `OFFICINA_P1_WATCHDOG_V2_5_INDEPENDENT_X_CONFIRMED_FOR_AUTHOR_SELECTION`.
v2.5's member enumeration and two-stage authorization are **bit-exact,
constructible and non-circular** under the procedural threat model the pair
itself states. The single X-line defect of v2.4 (`FX24-1`) is fixed and the two
Y-line blocks (`Y24-1`/`Y24-2` member set, `Y24-3` trust root) are closed by
construction. Every count reproduces. The one residual — full-chain substitution
by a repository writer at or before Stage A — is **stated, not closed**, exactly
as required, and no stronger claim survives anywhere in the pair.

The only authorization this confirmation carries is for **Kirill's future
watchdog option-selection token** (`OR-2`). No option is selected here; no key,
selection artifact, authorization artifact, signature, manifest, attestation or
install record is generated, requested or predicted. `T` remains
`NOT_ACTIVATED`; the programme claim remains `OPEN`.

---

## 1. Exact-byte custody — all four recomputed and matched

```text
packet     e794813e58a0d59f2eb6ce8c88fda34fc8d4bf0ffbd2c4045d9604ae5bb89cc5  MATCH
amendment  058c119c5de770dc537fd16962723063d2c3d4dad5da17d1431d4402927ebd1b  MATCH
composite  8751317511a3f738de35402b3c67ab9786e7fe1c95ea12d1e175ddd6540ddb20  MATCH
closure    97045681b2e73a64a1ab270fef1c1564a85a4e4c8155a5fa3308b0c945a24806  MATCH
```

Cited v2.4 verdict custody recomputes exactly and both are `REVISE`:

```text
bd8147a5085096c6a08ec0fec40ad22df23d55f23f77e3349218b3da93b6b2ba  reviews/fable_officina_p1_watchdog_v2_4_independent_x_confirmation.md
3fab1b09e2724534b2b5a080fbfeb98cc861cbe3b9764790084dfec050944a05  reviews/sol_officina_p1_watchdog_v2_4_final_y_confirmation.md
```

## 2. Independence attestation

v2.3, v2.4 and v2.5 — both governing files, the packet and the closure — were
authored by the **Opus 5** specification-author instance, and the author closure
records as much (`§10`). **I am Opus 4.8 in a fresh session; I did not author
v2.3, v2.4 or v2.5 and I am not the Opus 5 instance.** I am an admissible
independent X-line reviewer.

The author closure `opus5_officina_p1_watchdog_freeze_choice_v2_5_closure.md`
was treated as an **untrusted self-assessment** and was relied on for no
conclusion below. Its digest is recorded for custody only. Every fact in §3 was
recomputed from the two governing files on disk.

---

## 3. Bounded-audit results (independently recomputed)

### Item 1 — cross-references resolve; no live `§P1-19`: CONFIRMED
- The joint block is delimited once in each file; §A9 → composite **§P1-14.8**
  resolves (heading present at composite line 3718), and the ordering steps at
  §A10 ↔ composite **§P1-14.4** resolve (heading at line 2825; block at
  2883–3573).
- Mechanical reference audit: every `§P1-…` reference in the composite resolves
  to a composite heading (0 dangling); every `§A…` reference in the composite
  resolves to an amendment heading (`§A2`, `§A9`, `§A10`); every `§P1-…`
  reference in the amendment resolves to a composite heading **except the string
  `P1-19`**, which occurs only inside the `FX24-1` audit note and the quotation
  it explains (amendment lines 102, 107, 932, 941, 942) identifying the
  *withdrawn* locator. It occurs as a live locator nowhere, in either file, and
  the composite contains `P1-19` **zero** times.

### Item 2 — member set enumerable, cardinalities, disjointness, digests, provenance: CONFIRMED
- `M1..M7` are re-enumerated from normative literals alone (amendment `MS-1..MS-7`
  = composite byte-identical). Cardinalities recompute exactly:
  `2, 39, 7, 1, 1, 2, 1`, union **53** (`MS-8`).
- All **21** unordered class pairs are path-disjoint. I re-ran the `MS-9`
  argument mechanically: `M2 ∩ M3 = ∅` on the two literal lists (39 vs 7); every
  `M1/M2/M3` path begins with `reviews/`, `successor/OFFICINA_`, or is exactly
  `successor/officina/T_ENVELOPE.json`; `M4/M7` begin with
  `successor/officina/runtime_control/` (11th byte `0x6F`, not `0x4F`), `M5` with
  `src/`, `M6` with `tests/`; `M4` vs `M7` diverge at the first byte after their
  shared 35-byte prefix (`0x50` vs `0x49`). Union cardinality equals the sum
  (53), so no path is double-counted and none is unassigned.
- **Every M2 (39) and M3 (7) digest recomputes byte-exact against disk** — 46/46
  PASS, 0 mismatches, 0 missing.
- Provenance accounting: composite §P1-18 carries **exactly 47 rows**, all
  recompute against disk (47/47), and `provenance − M2 − M3 = {
  src/philosophia/officina/verification.py }` — the single non-enforced baseline
  (`327b1bb2…`, matched on disk). `47 = 39 + 7 + 1` holds, and every M2∪M3 path
  is present in the region. `Y24-2` is repaired **structurally**: `M2` is the
  literal `MS-2` list, never derived from the region, so no provenance row can
  re-enter a class.

### Item 3 — M4/M5/M6/M7 exact schema, paths, encoding, bundle rule: CONFIRMED
- `M4`: literal path `successor/officina/runtime_control/PRODUCTION_CALL_GRAPH.json`,
  schema `philosophia.officina.t-production-call-graph.v1`, `version` int 1,
  **17-key** mandatory set, bytes exactly `CANON` (`MS-0`). Carries no digest of
  itself.
- `M5`: literal path `src/philosophia/officina/verification.py`, digest = SHA-256
  of whole file bytes, no normalization; pre-handoff bytes are the baseline and
  are in no class.
- `M6`: two ordered, non-sorted module paths (`…_freeze_authority.py` rows 92–103,
  `…_install_integrity.py` rows 104–115); exact `test_p1_row_<NNN>_` membership
  rule giving 24 functions, 12 per module; each module its own member (2 entries);
  canonical two-entry `test_bundle_digest` defined for M7's use only, order-fixed
  (swap ⇒ refusal).
- `M7`: literal INSTALL path, schema
  `philosophia.officina.t-watchdog-authority-test-attestation.v1`, **10-key**
  set, bytes exactly `CANON`, bound to the M5/M6 digests found on disk, attests
  no install record and carries no digest of itself.
- `CK-4` draws only on `MS-1..MS-7`: **no wildcard, glob, directory scan,
  adjective, record-supplied path, manifest-supplied path, provenance-supplied
  path, or future-edit-table path.** The composite's future-edit table is
  expressly marked `NON-NORMATIVE AND SUPPLIES NO PATH TO ANY CHECK`.

### Item 4 — Stage A token pairing, key/key-id, pre-selection binding, threat bytes, temporal gate: CONFIRMED
- `TS-1`: literal path, schema `…t-p1-watchdog-freeze-selection.v1`, **11-key**
  set, bytes `CANON`. `selected_option_token` is exactly one of the two
  **existing** tokens and `selected_option_amendment_token` is the token it is
  paired with (crossed pair does not validate; a third/invented token does not
  validate). `public_key_hex` is 64 lowercase hex → 32 bytes; `key_id` = SHA-256
  of the 32 **raw** bytes. `governing_pre_selection` binds the three
  pre-selection digests (packet/amendment/composite) and `TS-2(e)` cross-checks
  them against the manifest. `threat_model` must equal the exact `TR-2` string
  byte-for-byte.
- **Cannot be conformingly created before Kirill's token.** `TS-1` mandates
  creation only after Kirill emits one explicit option token, and `OR-2`
  (Kirill's emission) strictly precedes `OR-3` (Stage A creation, key
  generation). The token value is Kirill's choice, so no conforming Stage A
  exists before that choice.

### Item 5 — Stage B canonical bytes, pure Ed25519, detached encoding, bindings: CONFIRMED
- `TS-3`: two literal paths (`.json` + `.sig`), schema
  `…t-p1-watchdog-authority-install-authorization.v1`, **13-key** set, `.json`
  bytes exactly `CANON`.
- `TS-4`: the signed message **is the exact `.json` byte sequence** (which `MS-0`
  forces to equal `CANON`, trailing `0x0A` included) — no prefix, suffix, domain
  separator, re-serialization or pre-hash; pure RFC 8032 Ed25519; the pre-hashed
  variant does not validate. Detached signature = exactly **128 lowercase hex**,
  no trailing newline, no other byte; the `.sig` file carries no key/id/algorithm.
- `TS-5(e)`: verification succeeds against **Stage A's 32-byte key and no other
  key** — no key list, discovery, fallback, downgrade or unsigned acceptance.
  Stage B binds the Stage-A path/hash, `key_id`, `selected_option_token`,
  `install_record_id`, `install_record_path`, `member_count == 53`, and the two
  post-resolution governing digests.

### Item 6 — `OR-1..OR-11` has exactly one conforming order: CONFIRMED
`OR-1` declares the order mandatory and total with no optional/reorderable/
alternate step. The determination order is forced:
- Stage A (`OR-3`) precedes M1 finalization (`OR-4`);
- `M1..M7` (`OR-4..OR-8`) precede id computation (`OR-9`);
- Stage-B authorization and its signature (`OR-10`) precede the no-replace record
  (`OR-11`); the record is **last**.

Attack replays, all refused at a named check:
- **Replay** — two INSTALL records ⇒ `INSTALL_RECORD_REPLAYED` (`CK-10`); a
  replayed record presented alone with its own old signed Stage B ⇒ id recomputed
  at `CK-6` ≠ filename ⇒ `CK-7` and `TS-5(h)` refuse.
- **Mixed generation** — `MS-1`'s two literal paths make any v2.4/v2.5 cross-mix
  leave one path absent or stale ⇒ `CK-5`/`CK-8` (`MEMBER_OMITTED`/`_STALE`), and
  a rebuild ⇒ `TS-5(h)` `STAGE_B_INSTALL_ID_MISMATCH` (`IR-11`, test 114).
- **Wrong key/path/signature** — `TS-5(e)`/`STAGE_B_SIGNATURE_INVALID`,
  `TS-1`/`TS-3` path rules, `TS-4` encoding (test 106 a–h).
- **Reordered steps** — a record written before `OR-10` completes is refused at
  `CK-3`/`CK-9` because no Stage-B artifact authorizes it (`OR-11`).
- **Whole-member substitution** — the sole surviving path is the `TR-2` residual
  (see Item 8), which is stated, not closed.

### Item 7 — no self-attestation; Stage artifacts outside `M1..M7`; partial substitution rejected: CONFIRMED
- `IR-4`/`TR-1`: the record is not its own member and `install_record_id` is not
  in its own preimage; no member carries its own digest; Stage A carries no digest
  of itself; Stage B carries no signature of itself; the manifest and attestation
  do not attest themselves. Each link is verified by the link above it; the chain
  terminates outside the installed set at an artifact created before that set
  existed. No cycle.
- `TS-6`: Stage A, Stage B, the `.sig` and the public key are outside every
  class — their paths share the `successor/officina/authorization/P1` prefix,
  which is a prefix of, and equal to, no member path (`M4`/`M7` live under
  `runtime_control/`, disjoint). The private key is named by no governing path.
- **M4's Stage-A binding rejects every partial substitution.** `TS-2(f)` pins
  Stage A's whole-file digest, path and key-id into the manifest; M4 is itself a
  member whose digest enters `install_record_id`, which Stage B signs.
  Substituting Stage A alone ⇒ `STAGE_A_BINDING_MISMATCH`; Stage A + M4 ⇒ id
  changes ⇒ `TS-5(h)`; any proper subset of {Stage A, Stage B, sig, manifest,
  record} fails at a named check (test 106 (a)–(g)).

### Item 8 — `TR-2` states, does not close, full-chain substitution; no stronger claim survives: CONFIRMED
`TR-2` states plainly that an actor able to write the repository **at or before**
Stage-A creation can substitute Stage A, Stage B, the signature, the manifest and
the record **together** to produce an internally consistent install, that no
filesystem-resident trust root can close this, and that nothing here claims to.
Its scope of closure is exactly "every partial and every post-hoc substitution."
Test 106(g) explicitly asserts the all-together case is the residual and **does
not** claim to refuse it. The packet §3.3, composite §P1-16 and amendment
`N-10`/`§A12` all describe the two-stage protocol as **process integrity only**
and disclaim executable/scientific authority. No section overstates the boundary.

### Item 9 — stated counts recomputed: CONFIRMED
- **Governing loci 216 = 162 + 54.** File 1 (amendment) tagged-rule families
  recomputed mechanically to **132** (`DA5 WA6 TIMING4 QC5 FD4 F8 KW3 FB5 TO5 RF3
  NS4 AK7 PUB4 H4 N11 IR12 MS10 TS6 OR11 CK12 FC1 TR2`), plus §A5 conjuncts 10,
  §A3.3 steps 6, routes 2, swap-only units 12 (`I1..I7`,`S1`,`S2`, 3 states) =
  **162**. File 2 = 23 (`R1..R22` + invariant 60) + 4 new sections + 3 guards
  (`G-10`,`G-11`,`AD-1`) + 24 test rows = **54**. The joint block is counted once
  (file 1) under the identical-restatement clause and is byte-identical in file 2.
- **53 members**, **24 test rows** (92–115 present, complete, no duplicate in
  range; rows 1–91 byte-identical to v1.4 by MD5), **47 provenance rows**, **24
  closed failure codes** (the `INSTALL_RECORD_UNAUTHORIZED`/`WITHDRAWN` text is
  not a code).
- Fixtures 104–115 exercise exact-path absence/name/omission/extra/staleness/
  substitution, the v2.4 class-overlap (test 108 requires the region-derived
  46-path `M2` to **fail** with `MEMBER_EXTRA`), the eight two-stage
  authentication cases (test 106), attestation mismatch, mixed generation and
  no-self-attestation — without contradicting the fixed `MS-6` row set (M2 fixture
  perturbs one of 39 literal paths; M6 fixture one of the two literal modules).

### Item 10 — accepted behavior, option symmetry/non-selection, negative space unchanged: CONFIRMED
- The amendment's behavioural surface §A1–§A8 is **byte-identical** between v1.1
  and v1.2 except one required companion reference (`composite v1.4 §P1-2` →
  `v1.5 §P1-2` in `QC-4`). The composite's pre-§P1-14 body and test rows 1–91 are
  byte-identical except version/closure-reference edits, all of which *remove*
  closure dependencies (aligning with `DA-5`) rather than change behaviour.
- Option symmetry: whole-file marker census is balanced **13 `[W-A]` / 13
  `[W-B]`**; every member, digest, order step, check and failure code is
  option-independent; `W-B` remains recommended on the same five criteria. Neither
  `W-A` nor `W-B` is selected and the identity cell is untouched (`N-1`, `N-5`,
  packet §7).
- Negative space preserved: `killer == WATCHDOG` unreachable (conjunct 8,
  `KW-1..3`), one freeze writer, PCS classifier journal scientifically invisible,
  signed selections not revoked, zero historical bytes moved,
  `T = NOT_ACTIVATED`, claim `OPEN`.

---

## 4. Blocking-condition sweep — none found

No non-enumerable member; no overlapping class (21/21 pairs disjoint, all digests
matched); no ambiguous canonical bytes (`MS-0` fixes `CANON`; `TS-4` fixes the
signed message and detached encoding); no temporal or signature cycle (`TR-1`
determination order is linear and terminates outside the set before it exists);
no self-attestation (`IR-4`, `TS-6`, test 115); and no overstated threat boundary
(`TR-2` names the residual and disclaims closure, echoed by test 106(g)). The
sole X-line defect `FX24-1` and both Y-line blocks `Y24-1`/`Y24-2`/`Y24-3` are
resolved by construction.

## 5. Disposition

- `OFFICINA_P1_WATCHDOG_V2_5_INDEPENDENT_X_CONFIRMED_FOR_AUTHOR_SELECTION`.
- This confirmation authorizes **only Kirill's future watchdog option-selection
  token** (`OR-2`). It selects no option; it recommends nothing beyond the pair's
  own unchanged `W-B` recommendation.
- No key pair, entropy, Stage-A selection artifact, Stage-B authorization
  artifact, detached signature, manifest, attestation or install record was
  generated, requested or predicted. No option token was minted, accepted,
  revoked or forecast.
- No existing file was modified and nothing was committed. `T` remains
  `NOT_ACTIVATED`; the programme claim remains `OPEN`. A parallel bounded Y-line
  confirmation on these identical bytes remains required before the acceptance
  token is signable.

OFFICINA_P1_WATCHDOG_V2_5_INDEPENDENT_X_CONFIRMED_FOR_AUTHOR_SELECTION
