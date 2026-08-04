# Officina P1 watchdog-freeze v2.6 — independent X-line confirmation

**Verdict:** `OFFICINA_P1_WATCHDOG_V2_6_INDEPENDENT_X_CONFIRMED_FOR_AUTHOR_SELECTION`

**Reviewer:** Claude Code, model `claude-opus-4-8`, fresh session. Fable 5 was
not available in this environment; the packet's fallback (Opus 4.8, fresh
session, did not author v2.3–v2.6) applies. I did not author the v2.3, v2.4,
v2.5 or v2.6 watchdog documents. The Opus 5 closure
`reviews/opus5_officina_p1_watchdog_freeze_choice_v2_6_closure.md` and the two
v2.5 confirmations were treated as **adversarial context only**; every claim
below was recomputed from the governing bytes.

**Scope reviewed:** the bounded v2.6 schema-completeness and honesty repair, and
preservation of the previously accepted watchdog design. Not reopened: the
signed process-identity Option A, the generic-harness core, scientific claims,
learner design, or T activation.

**Reviewed state:** committed bytes at HEAD `92c7012` (`Repair watchdog trust
claims in v2.6`). Working tree confirmed byte-identical to that commit for all
four governing inputs before reading.

---

## Hashes checked (SHA-256, recomputed from `92c7012`)

```text
1dbb99b7390c943a6f82be2be867652f43504f03a87f9017349a1acd522369a9  successor/OFFICINA_P1_WATCHDOG_FREEZE_AUTHOR_CHOICE_PACKET_V2_6_CORRECTION.md          MATCH
c3da2a7d24d0cea025f014f9231c0b856318b4a4c11ffc40c66972e7f905b3d1  successor/OFFICINA_GENERIC_HARNESS_WATCHDOG_FREEZE_AUTHORITY_AMENDMENT_V1_3_DRAFT.md    MATCH
6283d081df3eb3978bf963820859a5ebbf125689a4a3e249d3e85c1ca8d3d49d  successor/OFFICINA_GENERIC_HARNESS_SUPERVISOR_CONTROL_CHANNEL_P1_OPERATIVE_COMPOSITE_V1_6.md  MATCH
7a8ab2daefe9ad5d8d5bce74d7921a4fa600b44f17aa7a407acab26e472e3d1f  successor/OFFICINA_P1_PROCESS_CLAIM_IDENTITY_SELECTION_V1_SIGNATURE.md                  MATCH
```

Supporting recomputations:

```text
b839a668b28ce0707a2c280bcc542bfd6ff74718dff71dbb1ac102ca93bbba8f  JOINT INSTALL AND AUTHORIZATION BLOCK — identical in amendment §A10 and composite §P1-14.4 (1071 lines each)
058c119c5de770dc537fd16962723063d2c3d4dad5da17d1431d4402927ebd1b  amendment v1.2 on disk — equals its MS-2 recorded digest (M2 member 40 real)
```

---

## Item-by-item findings

### 1. `MS-4`, `MS-7`, `IR-3`, `TS-1`, `TS-3` completeness — PASS (validity predicate fully constructible)

Every top-level key set is stated as EXACTLY-n with no extra/missing key
(`MS-4` 20 keys, `MS-7` 10, `IR-3` 5, `TS-1` 11, `TS-3` 13). Each key carries an
exact type and value grammar; the mandatory `schema` literal is stated as the
value of the key in all five; every digest is "64 characters, each one of
`0123456789abcdef`"; every array states its cardinality and order (`roots` 5 in
§P1-3.1 order; `test_bundle_modules` 2 in MS-6 order; `rows_attested` exactly
`92..115`; `members` 57 in IR-1 order); `MS-0` fixes canonical encoding with
array order as part of the value. **Two independent implementations checking a
given artifact will derive the same artifact-validity predicate for all five.**

Byte-emission of a *required* artifact is fully determined for `M7`, the record
(`IR-3`) and Stage B (`TS-3`); for Stage A (`TS-1`) it is determined modulo the
author/runtime inputs (key, option token, timestamps, pre-selection digests)
whose *grammar* is fully pinned. The single field whose *value* is not
byte-derivable from the governing bytes is `MS-4.reachable_closure`'s content —
see item 7; its SHAPE is single-valued.

### 2. `TS-2 A1..A17` and `TS-5 B1..B18` exhaustive — PASS

Mapping each of TS-1's 11 keys and TS-3's 13 keys to its clause: every key is
checked for literal/type/length/derived-relation (TS-1: schema A4, version A5,
author A6, algorithm A7, option A8, paired-amendment A9, key A10/A11,
pre-selection A12/A13/A15/A16, threat_model+created_utc A14; TS-3: schema B4,
version B5, stage_a_path/hash/key_id B13(+B8), option B14, id B15(+B8), path
B9/B16, member_count B7/B17, governing digests B18(+B8), algorithm B10,
created_utc B6, signature B11/B12). No key is satisfied by mere presence.
Composite row **106(j)** test-pins the "field present but wrong" attack for
every field (wrong literal / wrong type / wrong length / wrong derived relation,
plus a companion correct-type-wrong-value fixture). **I could not construct an
artifact with a present-but-wrong field that passes.**

### 3. `MS-10` — PASS (one grammar, one validator, provenance-only)

`MS-10` gives exactly one grammar (20 ASCII chars `YYYY-MM-DDThh:mm:ssZ`, no
fraction, no offset but literal `Z`, no lowercase) and one semantic validator
(2000–2999, month 1–12, proleptic-Gregorian day bound with the ordinary leap
rule, 0–23/0–59/0–59, **no leap second**). It is used at MS-4, MS-7, IR-3, TS-1,
TS-3. `created_utc` is stated PROVENANCE ONLY; A14 and B6 add "not compared with
any other timestamp and orders nothing." A byte sweep of both governing files
for `created_utc` in any ordering/comparison/freshness/recency context returned
**only the two prohibition sentences** ("A verifier that ordered artifacts by
created_utc would be trusting an unauthenticated author-supplied string"). No
comparison, ordering, freshness, recency or liveness use exists.

### 4. Member classes recomputed from constants — CONFIRMED

```text
MS-1 = 2   (2 literal paths)              counted
MS-2 = 43  (43 literal digest+path rows)  counted
MS-3 = 7   (7 literal digest+path rows)   counted
MS-4 = MS-5 = MS-7 = 1 ; MS-6 = 2
union      = 2+43+7+1+1+2+1 = 57          57 distinct paths verified (no dup)
21 pairs   = C(7,2) = 21, all disjoint    path-prefix argument holds; no M1 path
                                          in M2/M3; verification.py absent from M2/M3
files/dig  = all 50 M2+M3 digests recomputed from disk = recorded value (0 bad, 0 missing)
provenance = 51 = 43 M2 + 7 M3 + 1 non-enforced verifier baseline   §P1-18 counted = 51,
                                          of which 50 equal M2+M3 records, 1 baseline
```

### 5. Region digests, joint-block identity, Ed25519 format — CONFIRMED (one LOW note)

The JOINT INSTALL AND AUTHORIZATION BLOCK is **byte-identical** in amendment
§A10 and composite §P1-14.4 (SHA `b839a668…`, 1071 lines each). Stage-B format
(`TS-4`): signed message = the exact Stage-B `.json` CANON bytes with trailing
`0x0A`, pure Ed25519 RFC 8032, no prefix/suffix/domain-separator/pre-hash;
detached `.sig` of exactly 128 lowercase hex chars, no trailing byte; algorithm
fixed by TS-3, key by TS-1. Diffed against amendment v1.2 (v2.5-era): the only
change is a **cosmetic reflow** of the `.sig` sentence ("128 lowercase
hexadecimal characters" → "128 characters, each one of `0123456789abcdef`") —
identical character set, identical format. Non-circular per `TR-1`: the
verifying key lives in Stage A, not Stage B; Stage A/B are outside `M1..M7`
(`TS-6`); members → id → filename, chain terminates outside the installed set.
The four `p1_composite_*` region digests are `M4` fields produced at OR-6 from
the defined region scheme; they are not independently recomputable now without a
live manifest, which is an install-time obligation, not a v2.6 defect.

*LOW note:* the packet §7 phrases this as "TS-4 carried forward verbatim /
format byte-unchanged." That is slightly loose — TS-4's prose was reflowed and
its hex charset made explicit. Format substance and the validity predicate are
unchanged; non-blocking.

### 6. Composite rows 105, 106(a)-(j), 111, 113, 115 — PASS

All present and enumerated against the generated-object schemas. Row 105
exhausts the `IR-3` record schema; 111 exhausts every `MS-4` field including
every `reachable_closure` malformation and `created_utc`; 113 exhausts every
`MS-7` field; 115 asserts the redundant-edge graph positively and rejects any
unique-attester / unique-external-attester fixture; 106(a)-(j) cover
path/key/signature/hash/replay/option/substituted-subset/procedural-driver/
coherent-rollback/exhaustive-field cases, each naming its exact clause and FC-1
code. No malformed/type/order/value/path case was found un-pinned.
*Observation (INFO):* amendment `CK-7`/`CK-8` prose do not individually name
their codes, but the codes are in FC-1's closed 25-set and are test-pinned by
composite rows 105, 106(e) and 112 (`INSTALL_RECORD_NAME_MISMATCH`,
`MEMBER_OMITTED/EXTRA/STALE/SUBSTITUTED`). Acceptable; could be tightened later.

### 7. `reachable_closure` — ANSWER: legitimate downstream obligation, NOT a selection blocker

**Determination: primarily (a) — a legitimate implementation-and-test
obligation under a now single-valued SHAPE contract — with an explicit caveat
that the content-mapping is genuinely under-specified and must be closed before
any manifest is authored.** I do **not** accept "shape is fixed" as proof the
content is derivable; the content is *not* fully derivable, and here is the
precise boundary:

- The SHAPE is now canonical and single-valued: an array of objects with exactly
  the six keys, `kind ∈ {BUILTIN, FROZEN, EXTENSION, PURE_PYTHON}`,
  `transitive_imports` sorted/distinct, array sorted by `module`, `module`
  values distinct, closed under itself. Given one audited closure, both
  implementations emit identical bytes.
- The CONTENT is under-specified relative to composite §P1-3.3: that table has 6
  rows whose "Kind" vocabulary ("built-in", "Python wrapper over built-in
  `posix`") has **no stated mapping** to MS-4's four literals, and whose stated
  transitive closures name modules (`abc`, `stat`, `posixpath`, `genericpath`,
  `_collections_abc`) that are **not rows**, so MS-4's own closure rule cannot be
  satisfied from §P1-3.3 as written. The value therefore is not mechanically
  derivable from the governing bytes.
- **Why this does not block author selection** — the only thing this verdict
  gates:
  1. `reachable_closure` is a field of `M4`, written at **OR-6**, entirely
     downstream of Kirill's option token (OR-2) and Stage A (OR-3);
  2. it is **option-independent** — identical under W-A and W-B — and is never an
     input to the watchdog choice;
  3. `G-11`/`CK-5` verify only that `M4.reachable_closure` satisfies the MS-4
     **shape**; **no check recomputes the actual Python import/fork graph and
     compares it**, so correspondence-to-reality is an audit/test obligation, not
     a gate predicate;
  4. the documents make **no over-claim**: MS-4 conditions on "the same audited
     closure," and §P1-3.3 is labelled "audited" / "human-readable audit table" /
     "NOT a canonical value." The honesty repair is genuine.

So the mapping from the actual graph to the canonical value **is an unmet
implementation-and-test obligation** that must be closed before a manifest is
authored/installed — but it lives downstream of, and is independent of, the
author's watchdog choice, and is correctly declared rather than falsely proven.
It does not block author selection.

### 8. Counts recomputed — ALL CONFIRMED

```text
225 governing loci = 171 (file 1) + 54 (file 2)          ✓
171 = 141 tags + 10 (§A5) + 6 (§A3.3) + 2 (§A3.1) + 12 (§A7.3)   ✓
 54 = 23 (R1..R22+inv60) + 4 (new §§) + 3 (guards) + 24 (rows)   ✓
141 = family sum, and IR12 MS11 TS6 OR11 CK12 FC1 TR2 FS5 XS1 N13 verified in file  ✓
 57 members ; 25 failure codes (counted in FC-1) ; 51 provenance rows ; 24 test rows (92..115)  ✓
```

### 9. Preservation of every v2.5-X-confirmed item — CONFIRMED

Cross-references resolve; composite contains `P1-19` **0** times and the
amendment's 2 mentions are the §A9 audit note recording the corrected v1.1
defect (no live dangling ref). Enumeration from `MS-1..MS-7` alone (`CK-4`);
bundle rules (`MS-6`) intact; option symmetry preserved — `W-B` recommended,
neither selected (`N-1`, `N-2`, §8), variant markers balanced **13/13**
whole-file; Stage A/B format preserved; residual **widened** to two clauses in
`TR-2`, never narrowed; scientific boundary held (`N-10`, `FS-4`, `XS-1` — the
gate is process-integrity only and enters no acceptance predicate);
`T = NOT_ACTIVATED`; watchdog cell `NOT SELECTED`. All v2.6 changes are additive
or claim-narrowing; nothing X-confirmed was weakened.

### 10. Hidden-authorization sweep — CLEAN

Every occurrence of `ACTIVATED` is `NOT_ACTIVATED`. No key/entropy/artifact is
generated, requested or made creatable (the only entropy/key mentions are in
negative-space prohibition lists). `P1_IDENTITY_OBSERVATION_BOUNDED_WEAKENING_V1`
is **not accepted** — `XS-1` and the composite blocking notice state it is not
signed, not signable and not predicted, and requires separate review before
Option A can become operative. No option token is pre-filled in the Stage-A
schema (only "one of the two", "either", "neither selected"). No implementation,
commit, install record, activation or claim movement is authorized. The signed
identity Option A is **recorded** at `XS-1` as current author state and **bound
into nothing** (not a member of `M1..M7`; digest in no install record).

---

## Findings by severity

- **BLOCKING:** none.
- **MAJOR:** none.
- **MINOR / LOW:**
  1. §7 wording "TS-4 carried forward verbatim / format byte-unchanged" is
     slightly loose; TS-4 prose was reflowed (charset made explicit). Format and
     validity predicate unchanged.
  2. `reachable_closure` content-derivation (kind-literal mapping, closure
     membership, boolean derivation) is genuinely under-specified relative to
     §P1-3.3 and **must be closed before any `M4` is authored/installed** —
     correctly declared, option-independent, downstream of selection;
     non-blocking for the author choice.
- **INFO:**
  3. Amendment `CK-7`/`CK-8` prose do not individually name failure codes; the
     codes are in FC-1's closed set and are test-pinned by composite rows
     105/106(e)/112.

None of the above prevents Kirill from making the watchdog author choice.

---

## Precise next authorization boundary

Confirmation means **only** that Kirill may make the watchdog-freeze author
choice — emit exactly one of the two existing option tokens
(`…_FREEZE_A_WATCHDOG_REQUESTS_PCS_EXECUTES` or
`…_FREEZE_B_PCS_FREEZES_ON_PEER_ENDPOINT_LOSS`). It authorizes **no** key
generation or entropy draw, **no** Stage A or Stage B artifact, **no** detached
signature, **no** manifest / attestation / install record, **no** implementation
or verifier/manifest edit, **no** test run or install, **no** T activation, and
**no** scientific execution.

```text
T = NOT_ACTIVATED
PROGRAMME CLAIM = OPEN
P1 PROCESS-CLAIM IDENTITY CELL = SELECTED: OPTION A (recorded at XS-1, bound into nothing)
P1 IDENTITY BOUNDED-WEAKENING TOKEN = NOT ACCEPTED
P1 WATCHDOG-FREEZE CELL = NOT SELECTED → now selectable by author choice
```

Before this pair can become operative, a later independently reviewed combined
binding must (per `XS-1`) record the identity signature's path/digest, record
separate acceptance of `P1_IDENTITY_OBSERVATION_BOUNDED_WEAKENING_V1` or refuse,
state that signature's membership status, and re-derive the process-claim
identity fields; and the `reachable_closure` content obligation of item 7 must be
discharged in the manifest-authoring round.

---

**VERDICT:** `OFFICINA_P1_WATCHDOG_V2_6_INDEPENDENT_X_CONFIRMED_FOR_AUTHOR_SELECTION`
