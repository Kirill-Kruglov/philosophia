READY_FOR_OFFICINA_P1_WATCHDOG_V2_5_INDEPENDENT_XY_CONFIRMATION

# Officina P1 watchdog-freeze choice — v2.5 author closure

**Author.** Claude Code Opus 5, **specification author only**. This closure is
an **untrusted self-assessment**. It is normative for nothing, it is a member of
no class, and both governing files forbid any normative dependency on it
(`DA-5`, amendment §A9, composite §P1-14.8). Every fact below is recomputable
from the four files named in §1 and from the repository as it stands.

**Verdict.** `READY_FOR_OFFICINA_P1_WATCHDOG_V2_5_INDEPENDENT_XY_CONFIRMATION`.

**What this verdict is not.** It authorizes **no** option token, **no** key
generation or entropy draw, **no** Stage-A or Stage-B artifact, **no** detached
signature, **no** manifest, attestation or install record, **no** implementation,
**no** commit, and **no** activation. `T` is `NOT_ACTIVATED`; the programme claim
is `OPEN`; the watchdog-freeze cell is `NOT SELECTED`; the process-claim identity
cell is `NOT SELECTED`.

---

## §1. Exact custody

```text
NEW FILES, this round
e794813e58a0d59f2eb6ce8c88fda34fc8d4bf0ffbd2c4045d9604ae5bb89cc5
  successor/OFFICINA_P1_WATCHDOG_FREEZE_AUTHOR_CHOICE_PACKET_V2_5_CORRECTION.md
058c119c5de770dc537fd16962723063d2c3d4dad5da17d1431d4402927ebd1b
  successor/OFFICINA_GENERIC_HARNESS_WATCHDOG_FREEZE_AUTHORITY_AMENDMENT_V1_2_DRAFT.md
8751317511a3f738de35402b3c67ab9786e7fe1c95ea12d1e175ddd6540ddb20
  successor/OFFICINA_GENERIC_HARNESS_SUPERVISOR_CONTROL_CHANNEL_P1_OPERATIVE_COMPOSITE_V1_5.md

COMPOSITE v1.5 REGION DIGESTS, by the extraction algorithm at the head of that
file (six sentinels, one occurrence each, in the required order)
H_BODY       f4e17ad40546cd099a042bf7f14fa3ab30ef193298c457f84d524839c20fa015
H_GUARDDATA  faf2d709cb711baca148c98eb36dccd06efdf716a2682d6d7611dc80fe540426
H_NORMATIVE  f12330735dc14c903cfce79fb553d685bac27e41f376b8502d2e2556ae8c4a26
H_FILE       8751317511a3f738de35402b3c67ab9786e7fe1c95ea12d1e175ddd6540ddb20

H_GUARDDATA IS UNCHANGED FROM v1.4. The guard pattern data was not touched.

SOURCES REPLACED, byte-intact, now provenance and now M2 members 36 and 37
ec5ddff8f8d09c1574a56d173579a6b585a8f9de230afb86e43d9415fb7a4390
  successor/OFFICINA_GENERIC_HARNESS_WATCHDOG_FREEZE_AUTHORITY_AMENDMENT_V1_1_DRAFT.md
c904ec4318485acd49a6128ca32f9e52fe523c3703b730351f8ad98adb3e60f1
  successor/…P1_OPERATIVE_COMPOSITE_V1_4.md

GOVERNING REVIEWS, now M2 members 38 and 39
bd8147a5085096c6a08ec0fec40ad22df23d55f23f77e3349218b3da93b6b2ba
  reviews/fable_officina_p1_watchdog_v2_4_independent_x_confirmation.md
3fab1b09e2724534b2b5a080fbfeb98cc861cbe3b9764790084dfec050944a05
  reviews/sol_officina_p1_watchdog_v2_4_final_y_confirmation.md

LINES  amendment 1110 → 1750    composite 3379 → 4070
```

---

## §2. Disposition of every v2.4 finding, one to one

### §2.1 The X-line finding

| Finding | Disposition | Where |
|---|---|---|
| `FX24-1` — amendment §A9 cited the identical handoff at composite **§P1-19**, a section that does not exist | **REPAIRED, and the failure mode removed.** §A9 now names composite v1.5 **§P1-14.8**, and the ordering is stated **once**, as `OR-1`..`OR-11`, carried byte-identically in both files, so two statements of it cannot disagree. A full mechanical cross-reference audit is stated in §A9 itself and reproduced at packet §1. `P1-19` occurs **0** times in composite v1.5. | amendment §A9; packet §1 |
| Scope note — the v2.4 closure's "24 body markers, all inside variant blocks" conflated body markers with the preamble legend | **ADOPTED VERBATIM, prior wording withdrawn.** The census is now stated in the X line's terms: 10/10 inside `REGION(BODY)` in resolvable variant blocks, 2/2 in the preamble legend outside all three regions (covered by `H_FILE` through `G-7`, not scanned by `G-10`), 1/1 in `GUARDDATA`. Whole file 13/13. | packet §6.2; §4.3 below |
| X items 1–4, 6–8 CONFIRMED | **PRESERVED, byte-unchanged in substance.** No constant, disposition, ack rule, publication rule, swap-only unit, order rule, route, guard or negative destination was reopened. | packet §5 table |
| X item 5 — `G-11` substance CONFIRMED except the locator | **PRESERVED AND EXTENDED, not replaced.** Content-addressing, external trust root, no self-attestation, verifier-baseline exclusion, mixed-generation rejection, fail-closed refusal and the one-runnable-state property all survive; what changed is that each is now mechanically checkable. | §3 below |

### §2.2 The Y-line findings

| Finding | Disposition | Where |
|---|---|---|
| `Y24-1` — `M1`..`M7` were semantic descriptions, not an enumerable set; `M4` no path/schema/version, `M5` no path, `M6` no path set and no bundle rule, `M7` no path/schema/keys/encoding; `IR-9` step 1 not performable; the "no adjective" claim false | **REPAIRED.** `MS-0`..`MS-7` give every class a literal path, an exact cardinality, and where applicable an exact schema id, version, key set and canonical encoding, plus an exact digest construction. 53 literal members. `CK-4` enumerates from these constants alone and names, in the governing bytes, everything it may not use: wildcard, glob, directory scan, adjective, record-supplied path, manifest-supplied path, provenance region, future-edit table. | amendment §A10 `MS-0`..`MS-7`, `CK-4`; composite §P1-14.4 (same bytes) |
| `Y24-2` — `M2` and `M3` overlapped on seven physical paths | **REPAIRED STRUCTURALLY.** `MS-2` is a literal 39-path list with recorded digests. The provenance region is not read to build `M2` at all, so the overlap is impossible rather than merely absent. `MS-9` proves all twenty-one class pairs disjoint by path. Composite §P1-18 now states its own arithmetic: 47 rows = 39 `M2` + 7 `M3` + 1 non-enforced baseline, and says in its own bytes that it is not the source of `M2`. | `MS-2`, `MS-3`, `MS-9`; composite §P1-18 |
| `Y24-3` — the external trust root was not mechanically authenticated; no path, schema, key, algorithm or verification rule; no ordered step obtaining and verifying authorization after the digests fix the id and before the record is written; "pre-existing" did not resolve the two-time-point problem | **REPAIRED by the two-stage protocol Y named.** `IR-5` withdraws "the author signature file". `TS-1`..`TS-6` define Stage A (option token + option-specific token + Ed25519 public key + key id + pre-selection digests + author + threat model) and Stage B (Stage-A hash + key id + option token + install-record id + member count + governing digests + algorithm), with the signed message, the pure-Ed25519 rule and the detached 128-hex signature encoding all exact. `OR-3` fixes Stage A **before** `M1` is final; `OR-9`/`OR-10` fix Stage B **after** the id and **before** the record; `OR-11` installs the record last. | `TS-1`..`TS-6`, `OR-1`..`OR-11` |
| `Y24-3` sub-point — the tests could not have their asserted meaning | **REPAIRED.** Rows 103..115 rewritten against the exact sets and the exact paths; row 106 is now eight named authorization fixtures; row 108 additionally requires the **v2.4 overlap itself** to fail. | composite rows 103..115 |
| Y passes §1, §2, §5, §6 — governing surfaces, guard separation, verifier-baseline repair, behavioural authority, scientific boundaries, choice and status | **PRESERVED.** Not one of these was reopened. | packet §5 |
| Y's four-point "smallest bounded repair" | **ALL FOUR ADOPTED**, in the order Y gave them: (1) literal paths and cardinalities, with schema/version/key set for `M4` and `M7` and the path list and bundle digest for `M6`; (2) `M2` made an explicit exact path set excluding the seven `M3` members and the baseline; (3) the authorization artifact defined by exact path and schema, binding the token and the id, with signature verification against a pinned key, an obtain-and-verify step after `M7` and the id and before the record, the artifact kept outside `M1`..`M7`, and the record installed last; (4) rows 104..115 exercising exact-path substitution, class overlap and trust-root path and signature substitution. | throughout §A10 |

---

## §3. The member table, and the disjointness proof

```text
CLASS CARD  PATHS / RULE                                        DIGEST RULE
M1      2   successor/…AMENDMENT_V1_2_DRAFT.md                  whole-file
            successor/…COMPOSITE_V1_5.md  (post-selection)      whole-file
M2     39   literal list, MS-2, with recorded digests           whole-file,
            excludes the 7 M3 paths and verification.py         compared to
                                                                the recorded
                                                                value at MS-2
M3      7   the 5 harness contracts, the harness signature,     whole-file,
            batch-settlement v1.1.1 — MS-3, digests as §A0.1    compared to
                                                                MS-3
M4      1   successor/officina/runtime_control/                 whole-file;
              PRODUCTION_CALL_GRAPH.json                        bytes must
            schema …t-production-call-graph.v1, version 1,      equal CANON
            17 mandatory keys, CANON bytes                      of the object
M5      1   src/philosophia/officina/verification.py            whole-file,
            POST-handoff bytes; the pre-handoff bytes are the   no
            non-enforced baseline and are in no class           normalization
M6      2   tests/test_officina_p1_freeze_authority.py    92..103   whole-file
            tests/test_officina_p1_install_integrity.py  104..115   whole-file
            row rule: exactly one module-scope function named
            test_p1_row_<NNN>_… per row, 12 per module, none
            outside 92..115, none duplicated
            bundle digest = SHA-256(CANON({schema, modules:[…]}))
            in that fixed order, used only by M7
M7      1   successor/officina/runtime_control/INSTALL/         whole-file;
              T_WATCHDOG_AUTHORITY_TEST_ATTESTATION_V1.json     bytes must
            schema …t-watchdog-authority-test-attestation.v1,   equal CANON
            10 mandatory keys, CANON bytes, bound to the M5     of the object
            and M6 digests found on disk, rows 92..115,
            row_count 24, all_rows_passed true
TOTAL  53
```

**Disjointness, twenty-one pairs.**

```text
GROUP 1 — 12 pairs, {M1,M2,M3} × {M4,M5,M6,M7}.
  The 48 strings of M1 ∪ M2 ∪ M3 each begin with "reviews/" or with
  "successor/OFFICINA_", or are exactly successor/officina/T_ENVELOPE.json.
  M4 and M7 begin with the 35 bytes "successor/officina/runtime_control/",
  whose eleventh byte is 0x6F where "successor/OFFICINA_" has 0x4F, and which
  is neither "reviews/" nor the T_ENVELOPE string.
  M5 begins with "src/" and M6 with "tests/"; neither prefix occurs in the
  first three lists. Twelve pairs disjoint.
GROUP 2 — 6 pairs, among {M4,M5,M6,M7}.
  Three distinct roots settle five pairs. For M4 against M7, after the shared
  35-byte prefix the remainders begin 0x50 ("P") and 0x49 ("I"). Six disjoint.
GROUP 3 — 3 pairs, among {M1,M2,M3}.
  M1 × M2: M1's strings end _V1_2_DRAFT.md and _COMPOSITE_V1_5.md; MS-2 carries
    the amendment only at _V1_DRAFT.md and _V1_1_DRAFT.md and the composite only
    at _V1, _V1_1, _V1_2, _V1_3, _V1_4.
  M1 × M3: MS-3 is the harness chain, the harness signature and batch
    settlement v1.1.1; no amendment-v1.2 or composite-v1.5 path occurs.
  M2 × M3: two literal lists, intersection empty by direct comparison.
UNION 2+39+7+1+1+2+1 = 53 distinct paths = MS-8. No path counted twice, no
member unassigned, no eighth class.

VERIFIED MECHANICALLY THIS ROUND:
  MS-2 rows                                                    39
  MS-3 rows                                                     7
  MS-2 ∩ MS-3                                                   ∅
  composite provenance rows                                    47
  provenance minus MS-2 minus MS-3   { src/philosophia/officina/verification.py }
  every MS-2 and MS-3 digest recomputed against the file on disk   MATCH
  MS-3 digests equal amendment §A0.1's seven digests               MATCH
```

**Stage A, Stage B, the detached signature and the public key are in no class.**
All three artifact paths begin with the 35 bytes
`successor/officina/authorization/P1`, which is a prefix of no member path and
equals no literal member path; the key exists only inside Stage A and has no
path of its own. Neither stage is a specification surface: both carry values and
no rules.

---

## §4. The two-stage state machine, and the trust proof

### §4.1 State machine

```text
S0  NOTHING EXISTS. This is the state these bytes leave the world in.
      → requires OR-2: Kirill emits exactly one EXISTING option token.
S1  OPTION EMITTED, NO ARTIFACT.
      → OR-3: Stage A created (key pair generated) at TS-1's exact path;
        verified TS-2(a)–(d). (e) and (f) are not yet evaluable: no manifest.
S2  STAGE A PRESENT AND WELL-FORMED. Option and key pinned. No member final.
      → OR-4: variant blocks resolved to the signed branch, other branch
        deleted; v1.2 amendment installed; G-10 finds zero markers. M1 final.
      → OR-5: M5 verifier and the two M6 modules installed.
      → OR-6: M4 manifest written, binding Stage A's path, digest and key id.
S3  M1..M6 FINAL EXCEPT M7.
      → OR-7: full matrix runs; every row passes; TS-2 evaluated in full.
      → OR-8: M7 attestation written, bound to the M5/M6 digests on disk.
S4  ALL 53 MEMBERS FINAL.
      → OR-9: canonical member list built FROM THE CLASS CONSTANTS;
        install_record_id computed per IR-1.
S5  ID KNOWN, NOTHING AUTHORIZED.
      → OR-10: Stage B written at TS-3's path; detached signature written at
        the .sig path; TS-5 clauses (a)–(j) verified.
S6  AUTHORIZED, RECORD ABSENT.
      → OR-11: record installed no-replace at its content-addressed path,
        LAST; all M2 and M3 bytes verified byte-identical.
S7  INSTALLED. The only state from which a production entry point can proceed,
    and only after CK-1..CK-12 pass in full on every entry.
ANY DEVIATION FROM S0→S7 IN THAT ORDER REFUSES. There is no partial mode, no
warning mode, no override, no fallback key, no unsigned shortcut and no
degradation to a prior behaviour.
```

### §4.2 Trust and circularity

```text
DETERMINATION ORDER, and it is one-way:
  53 members            →  install_record_id            (IR-1)
  install_record_id     →  the record's filename        (IR-2)
  Stage B names that id and is signed over its own canonical bytes
                                                        (TS-3, TS-4)
  the key that verifies Stage B is pinned in Stage A    (TS-1, TS-5(e))
  Stage A exists before any M1 byte is final            (OR-3 before OR-4)
    and is written by no later step

NO SELF-ATTESTATION ANYWHERE:
  the record is not a member of itself and its id is not in its own preimage
  Stage B carries no signature of itself
  Stage A carries no digest of itself
  the manifest carries no digest of itself
  the attestation does not attest itself
  the composite carries none of its own digests (§P1-14.5, six-link DAG)

WHAT IS CLOSED — every partial and post-hoc substitution, each by a named
check and a named code: Stage A alone (STAGE_A_BINDING_MISMATCH, via the
manifest binding at TS-2(f)); the signature alone or absent
(STAGE_B_SIGNATURE_INVALID / _ABSENT); the manifest alone (MEMBER_SUBSTITUTED,
and STAGE_A_BINDING_MISMATCH if the binding fields are dropped); the
attestation alone (ATTESTATION_MISMATCH); the record alone
(INSTALL_RECORD_NAME_MISMATCH); a replayed id (STAGE_B_INSTALL_ID_MISMATCH and
INSTALL_RECORD_REPLAYED); an option mismatch (STAGE_B_OPTION_MISMATCH); an
unsigned install (inadmissible — no path admits it).

WHAT IS NOT CLOSED, and the governing bytes say so at TR-2 — an actor able to
write this repository AT OR BEFORE Stage-A creation can substitute Stage A,
Stage B, the signature, the manifest and the record together. No
filesystem-resident trust root can close that. The residual is procedural, is
of the same kind as the A3 same-UID residual already named at composite
§P1-12.4, is an infrastructure fact, and is citable in no Q or C fact. The
exact threat-model string Stage A must carry states this to the author's face.
```

### §4.3 Negative fixtures

```text
ROW  WHAT IT REFUSES                                       FIXTURES
103  any M2/M3 digest moved; either M1 member absent/stale     46 + 2
104  no hex-named record under INSTALL/                             1
105  record filename ≠ IR-1 digest of its member list; and
     a correct record renamed                                       2
106  TWO-STAGE AUTHORIZATION NEGATIVES                              8
       a wrong path            Stage A or Stage B off its exact path
       b wrong key             signature by another key; key id not the
                               digest of its own key; a second "permitted"
                               key offered
       c wrong signature       bit-flip; signature over re-serialized
                               non-canonical bytes; signature over the parsed
                               value; pre-hashed Ed25519; absent .sig;
                               .sig with trailing newline or uppercase hex
       d wrong Stage-A hash    Stage B naming the wrong hash; Stage A
                               substituted after the manifest; pre-selection
                               digests not matching the manifest
       e replayed id           earlier-generation record + its valid Stage B;
                               and two hex-named records present at once
       f option mismatch       Stage B token ≠ Stage A token; crossed
                               option/amendment token pair; invented token
       g substituted auth      a self-consistent attacker-key quadruple with
                               the genuine manifest — refused; and the fixture
                               asserts explicitly that substituting ALL of
                               them is the TR-2 residual and is NOT claimed
                               to be refused
       h ordering              record before Stage B; attestation before the
                               matrix; manifest after the id; Stage A after
                               variant resolution — and the assertion that no
                               order other than OR-1..OR-11 is runnable
107  member omission, every class, 53 → 52                          7
108  extra member, every class; AND a verifier that builds M2
     from the provenance region — 46 instead of 39 — the exact
     v2.4 overlap, which MUST fail                              7 + 1
109  stale member, every class; for M2/M3 also against the
     literally recorded digest, without consulting the record        7
110  substituted verifier: baseline; G-10 without G-11; G-11
     without G-10; correct verifier at another path                 4
111  substituted manifest: wrong version; wrong bytes;
     non-canonical bytes; missing key; extra key; missing
     stage_a_* binding                                              6
112  test bundle: missing row; row in the wrong module; duplicated
     row; row-form name outside 92..115; modules swapped; bytes
     differing from the attested digest; rows present but never run 7
113  attestation: wrong verifier digest; wrong module digest;
     wrong bundle digest; row_count ≠ 24; rows ≠ 92..115;
     all_rows_passed false                                          6
114  mixed generation: v1.1 with v1.5; v1.2 with v1.4; any other
     v2.4/v2.5 mixture                                              3
115  self-attestation: composite carrying its own H_FILE; verifier
     its own digest; manifest its own digest; attestation attesting
     itself; Stage A its own digest; Stage B its own signature;
     record listing itself                                          7
```

---

## §5. Preserved surfaces — the confirmed behaviour did not move

```text
QC-1..QC-5, FD-1..FD-4, AK-1..AK-7, PUB-1..PUB-4, RF-1..RF-3, TO-1..TO-5,
F-1..F-8, FB-1..FB-5, KW-1..KW-3, NS-1..NS-4, WA-1..WA-6, TIMING-1..TIMING-4,
DA-1..DA-5, the ten §A5 conjuncts, the six §A3.3 steps, ROUTE-D and ROUTE-W,
and the twelve swap-only units — CARRIED FORWARD UNCHANGED IN SUBSTANCE.

ROUTE-D / ROUTE-W: exhaustive, one procedure, one actor, one mediation, one
evidence class, one namespace, one writer, one killer value.
ONE SUPERVISOR EVIDENCE WRITER: WA-2, composite §P1-13.7, invariant 89.
EVERY GROUP STOP THROUGH SIGNAL_GROUP: WA-1, §A3.3 steps 2–3, invariant 89(a).
killer == WATCHDOG REJECTED at §A5 conjunct 8, no re-entry by any mechanism
(KW-1), enum retained not narrowed (WA-5, KW-2), tests 93 and 94.
PCS FREEZE CLASSIFIER JOURNAL NON-SCIENTIFIC: composite §P1-10.7, invariant 89,
test 101 — terminal, per-group tokens and freeze_ns reach no peer artifact, no
acceptance predicate, no qualification, no comparison, no Q or C fact.
G-10 UNIQUE AND SELF-MATCH-SAFE: reserved to the variant guard alone, patterns
only in GUARDDATA, definition and test 102 marker-free, independent of G-11.
AD-1 DISTINCT: the authoring discipline, ranging over G-1..G-5 only.
BODY AND WORDING GUARDS: G-1..G-9 unchanged; H_GUARDDATA unchanged from v1.4.
W-A AND W-B: definitions, recommendation, endpoint counts and NON-SELECTION
unchanged; markers balanced 10/10 in the body region.
HISTORY: zero bytes edited; zero historical loci with governing force.
PROGRAMME CLAIM OPEN; T NOT_ACTIVATED.
NO NEW SCIENTIFIC CELL, WATCHDOG MECHANISM, TREATMENT, EVIDENCE CLASS OR
AUTHOR OPTION. The two-stage authentication is process integrity only.
```

---

## §6. Recomputed counts

```text
GOVERNING LOCI                    216   =  162 (amendment) + 54 (composite)
  amendment tagged rules          132   DA 5 WA 6 TIMING 4 QC 5 FD 4 F 8 KW 3
                                        FB 5 TO 5 RF 3 NS 4 AK 7 PUB 4 H 4
                                        N 11 IR 12 MS 10 TS 6 OR 11 CK 12
                                        FC 1 TR 2
  §A5 conjuncts                    10
  §A3.3 steps                       6
  named routes                      2
  swap-only units                  12
  composite behavioural repairs    23
  composite new sections            4
  composite guard rules             3
  composite test rows              24
DELTA FROM v2.4's 180             +36   all in file 1, all in the install and
                                        authorization block
GOVERNING SPECIFICATION FILES       2
HISTORICAL LOCI WITH FORCE          0
HISTORICAL BYTES EDITED             0
INSTALL-RECORD MEMBERS             53   2 + 39 + 7 + 1 + 1 + 2 + 1
MEMBER CLASSES                      7   pairwise disjoint, union = 53
CLOSED FAILURE CODES               24   6 STAGE_A_ · 9 STAGE_B_ ·
                                        3 INSTALL_RECORD_ · 4 MEMBER_ ·
                                        ATTESTATION_MISMATCH ·
                                        HISTORICAL_BYTE_MOVED
COMPOSITE PROVENANCE ROWS          47   39 M2 + 7 M3 + 1 non-enforced baseline
VARIANT MARKERS, body region    10 / 10
VARIANT MARKERS, whole file     13 / 13  = 10/10 body + 2/2 preamble legend
                                          + 1/1 GUARDDATA
G-1..G-5 PATTERNS IN THE BODY       0
OCCURRENCES OF "P1-19" IN THE COMPOSITE   0
```

**The identical-restatement clause is the one addition to the counting rule.**
When a normative unit is carried byte-identically in both governing files it is
one locus, counted once, in file 1. This is not new practice — v2.4 already
counted `H-1`..`H-4` once — and it is what the byte-identical joint block
requires. The joint block's 54 tags are counted in file 1; file 2 counts `G-11`
as one guard locus, exactly as before.

---

## §7. What I could not verify, stated plainly

```text
1. I AM NOT AN INDEPENDENT REVIEWER OF THESE BYTES. I authored v2.3, v2.4 and
   v2.5. This closure is a self-assessment. The v2.3 X line was produced by
   this same instance; that defect is now partly resolved, because the v2.4 X
   line was Opus 4.8 in a fresh session and was genuinely independent — and it
   found a defect (FX24-1) that my own self-review had not. That is direct
   evidence that self-review under-detects, and it applies to this closure too.
2. THE TWO-STAGE PROTOCOL HAS NOT BEEN EXERCISED. No key exists, no artifact
   exists, no signature has been produced or verified, and no Ed25519
   implementation has been named, chosen or audited. Everything in §4 is a
   specification of what must hold, not a report of what did.
3. NO TEST HAS RUN. Rows 92..115 are future obligations. The M6 modules do not
   exist. The counts in §6 are counts of specification text, never of passing
   tests.
4. THE MANIFEST, ATTESTATION AND INSTALL RECORD DO NOT EXIST. The paths at
   MS-4, MS-7 and IR-2 name files that no step of this round created.
5. THE TR-2 RESIDUAL IS REAL AND IS NOT CLOSED. §4.2 states exactly what it is.
   A reviewer should confirm that the governing bytes claim no more than that.
6. WHETHER THE JOINT BLOCK IS THE RIGHT SHAPE IS A JUDGEMENT, NOT A FACT. I
   chose one byte-identical block over two separately worded statements
   precisely because FX24-1 was a divergence between two statements. An
   independent line may prefer a different structure and should say so.
```

---

## §8. Required next round

```text
X LINE — bounded independent engineering confirmation, on identical bytes, by
  FABLE 5 or OPUS 4.8, in a fresh session, by an agent that did not author
  v2.3, v2.4 or v2.5. Bounded to:
    1 the cross-reference audit: is every §P1-… and §A… reference in the pair
      resolvable, and is FX24-1 actually gone?
    2 is MS-1..MS-7 enumerable from governing constants alone — no wildcard,
      no scan, no adjective, no record-supplied or manifest-supplied path?
    3 is MS-9's disjointness proof sound, and is the union exactly 53?
    4 are MS-4, MS-6 and MS-7's schemas, key sets and canonical encodings
      sufficient to construct those artifacts without any further choice?
    5 is the two-stage protocol constructible and non-circular as TR-1 claims,
      and does TR-2 overclaim anything?
    6 is the joint block byte-identical in the two files?
    7 do rows 103..115 exercise the exact sets, and does row 108's overlap
      fixture actually fail?
    8 are the recomputed counts — 216, 162, 54, 132, 53, 24, 47 — reproducible?
    9 is every confirmed v2.4 surface preserved, and is anything new that
      should not be?

Y LINE — bounded governance confirmation by SOL, on identical bytes, bounded to:
    1 are Y24-1, Y24-2 and Y24-3 each actually closed, or only reworded?
    2 is the trust chain genuinely external and genuinely authenticated, and
      is the residual honestly stated rather than minimized?
    3 does the ordering OR-1..OR-11 admit exactly one conforming sequence?
    4 is any scientific boundary moved: no new cell, mechanism, treatment,
      evidence class, covariate or predicate input?
    5 do the option tokens, the recommendation, the identity cell, T and the
      programme claim all stand exactly where they stood?

BOTH LINES: this closure is untrusted. Recompute every figure from the files.
```

---

## §9. Authorization boundary

```text
THIS CLOSURE AUTHORIZES NOTHING.

NOT AUTHORIZED, explicitly: any option token; any signature by Kirill; any key
pair; any entropy draw; the Stage-A artifact; the Stage-B artifact; the
detached signature; the manifest; the test modules; the attestation; the
install record; any verifier edit; any implementation; any commit; any test
run; any process, socket, pipe, fork, exec, signal, wait or prctl operation;
any supervisor, PCS, controller, worker or watchdog; any capability, world,
learner, entropy, candidate, trajectory or capacity artifact; any custody
disposition, result manifest, spend, datum, outcome, Proof or claim movement.

NO FREEZE WAS EXECUTED, REQUESTED, JOURNALLED OR WITNESSED. NO /proc WAS READ
AGAINST ANY LIVE PROCESS. NO CLOCK WAS SAMPLED FOR ANY CONTRACT PURPOSE. NO
EXISTING FILE WAS MODIFIED AND NOTHING WAS COMMITTED.

Only three new files and this closure were written:
  successor/OFFICINA_P1_WATCHDOG_FREEZE_AUTHOR_CHOICE_PACKET_V2_5_CORRECTION.md
  successor/OFFICINA_GENERIC_HARNESS_WATCHDOG_FREEZE_AUTHORITY_AMENDMENT_V1_2_DRAFT.md
  successor/OFFICINA_GENERIC_HARNESS_SUPERVISOR_CONTROL_CHANNEL_P1_OPERATIVE_COMPOSITE_V1_5.md
```

```text
T = NOT_ACTIVATED
PROGRAMME CLAIM = OPEN
WATCHDOG-FREEZE CELL = NOT SELECTED
PROCESS-CLAIM IDENTITY CELL = NOT SELECTED
```

READY_FOR_OFFICINA_P1_WATCHDOG_V2_5_INDEPENDENT_XY_CONFIRMATION
