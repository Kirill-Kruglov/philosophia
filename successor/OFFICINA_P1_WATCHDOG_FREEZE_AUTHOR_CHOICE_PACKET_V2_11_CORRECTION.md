# Officina P1 watchdog-freeze mechanism — author choice packet v2.11 (correction)

**Author:** Claude Code Opus 5, **specification author only**. Not an
independent X-line or Y-line reviewer. Every author closure, including this
packet's companion closure, is an untrusted self-assessment.

**THIS PACKET OPENS NO AUTHOR CHOICE AND CLOSES NONE.** The watchdog-freeze
mechanism cell is **already signed**. Kirill selected

```text
I_SELECT_P1_WATCHDOG_FREEZE_B_PCS_FREEZES_ON_PEER_ENDPOINT_LOSS
```

on 2026-08-05, at
`successor/OFFICINA_P1_WATCHDOG_FREEZE_SELECTION_V1_SIGNATURE.md`
(`ffcb4116a9171d873be773138cc2c97547f8ff919a1d71f4cbd46e328eb3a7dc`). **That
selection is not reopened, not
re-run, not re-recommended and not re-argued anywhere in this packet.** There is
no option table here, no recommendation, no comparison and no new cell.

This packet exists for one reason: the v2.11 generation is a **replacement
governing generation**, and every governing generation of this chain carries an
author-facing packet that records what its two governing files say, at what
digests, with what accounting. It is the pre-selection anchor target named by
`TS-1`'s `governing_pre_selection.packet` and the hash-read target of `TS-2B`
`A16(b)`, and nothing else.

`T` is `NOT_ACTIVATED`; the programme claim is `OPEN`.

---

## §0. Scope — a bounded governing repair after two independent REVISE verdicts

### §0.1 What licensed this round

Both independent lines reviewed the W-B post-selection binding against the
v1.7/v1.10 governing bytes and both returned the same verdict:

```text
REVISE_OFFICINA_P1_WB_GOVERNING_PAIR
```

```text
d8483c185c6f438f4a209353716b7d8aef31529c5f6876381ea03431beb15ba1  reviews/fable_officina_p1_wb_binding_x_review.md
e1bf893a00fc625f97698ddbe9a2f0d4413a8578c65722559f3ddefe7bcd8628  reviews/sol_officina_p1_wb_binding_y_review.md
```

Each line independently determined **two Major, executable findings against the
governing pair** and each produced its own counterexample against the v1.10
bytes. The v2.10 exit discipline reserves regeneration to exactly that: an
independent reviewer's counterexample against the current bytes. **Both lines
supplied one. This round is licensed and is bounded to what they named.**

```text
F1  MAJOR, EXECUTABLE, FAIL-OPEN.  amendment §A9 H-3 stated the pre-production
    enforcement point as CK-1..CK-12 while §A10, VP-4, IR-9, CK-15, FC-1 and
    composite §P1-14.8 all said fifteen; and FOUR governing sentences claimed
    §A9 and §P1-14.8 were stated "in full and identically" when their bytes
    differed in four passages. The omitted range drops CK-14 and therefore B14,
    the ONLY clause binding the signed option token across the two
    authorization stages.
F2  MAJOR, EXECUTABLE.  KV-1..KV-6 was an operative per-_killpg precondition of
    the W-B classifier — the sole executor of group stops on the endpoint-loss
    route — referenced exactly twice in composite v1.10 and DEFINED NOWHERE in
    either live specification surface. Row 89 was an unsatisfiable test row of
    the SELECTED branch.
Y-M3, Y-M4, Y-M5, X-1, X-2, X-3   binding-level and handoff-level defects,
    repaired in the regenerated binding v2 and handoff v2, not in governing
    bytes.
F3, F4   MINOR, log: OR-4's "the v1.3 amendment is installed" as a fifth
    generation-scoped operative string that §A9's four-place audit missed, and
    composite line 90's §P1-14.3 locator for a rule defined at §P1-14.4.
```

### §0.2 What this round is, and what it is not

```text
IT IS the first ACTUAL REPLACEMENT GENERATION after the two bounded rounds v2.9
  and v2.10. Both of those declared themselves surgical corrections and
  deliberately added no provenance row. This one is a replacement, so it
  performs the whole deferred accounting at once (§4).
IT IS NOT a design round. No author cell is opened or closed, no option is
  added, removed, renamed or re-recommended, no scientific cell is created, no
  treatment is defined, no constant is introduced, no member class is added and
  no programme claim moves.
IT IS NOT an acceptance. The v1.8 acceptance token is unsigned and is not made
  signable here.
IT IS NOT an implementation, install or activation authorization, and it grants
  no OR step.
IT DOES NOT REOPEN THE SIGNED W-B SELECTION or its sensor-only semantics.
```

---

## §1. The v2.11 governing pair

### §1.1 Paths and digests

```text
71ec025a6d5da2b975e8f958d4c5e218e37e0de76fc1c64e2824e20cb3e08a4c  successor/OFFICINA_GENERIC_HARNESS_WATCHDOG_FREEZE_AUTHORITY_AMENDMENT_V1_8_DRAFT.md
c9712f7c9ae86d4ded8243c6501c29737acae2262ad5a291c7a4b188087687b6  successor/OFFICINA_GENERIC_HARNESS_SUPERVISOR_CONTROL_CHANNEL_P1_OPERATIVE_COMPOSITE_V1_11.md
```

Composite region digests, recomputed by the §P1-14.0 extraction algorithm:

```text
H_BODY       ce728942d3d1a746960a9fbf0feb4a969b79b9793d2b89f67a5d73c9b31b51cf
H_GUARDDATA  faf2d709cb711baca148c98eb36dccd06efdf716a2682d6d7611dc80fe540426
H_NORMATIVE  01ea73918211509a19126e5847234a4b64d6ffbabf8a064d7051b460949743b8
H_FILE       c9712f7c9ae86d4ded8243c6501c29737acae2262ad5a291c7a4b188087687b6
```

**`H_GUARDDATA` IS BYTE-UNCHANGED FROM v1.10.** The guard-pattern region was not
touched by this round, so `G-10`'s pattern source and the `VARIANT_MARKER` class
are exactly what the previous generation carried.

### §1.2 The two delimited byte-identical regions

This generation carries **two** regions that must be byte-identical across the
pair, each extractable by its own pair of delimiter lines, each of which occurs
exactly once per file.

```text
REGION                              AMENDMENT v1.8   COMPOSITE v1.11   DIGEST
canonical atomic-handoff preamble   lines 1209..1271 lines 6614..6676
  H-1..H-4                          4052 bytes       4052 bytes
                                    ca2ff30b93818f7945b442de68438ddaa8f71879443595903fddfa950cf4a785
joint install and authorization     lines 1324..4442 lines 3273..6391
  MS-0..XS-1                        222364 bytes     222364 bytes
                                    9bf4a831b138889b4ae71d2985820793f10a649311199ec3136d75a6514babe5
```

Both extractions were performed and diffed: **zero difference in either
region.** The digests above are of the region CONTENT, excluding the two
delimiter lines themselves.

**The "stated in full and identically" claim is now narrowed to exactly these
two regions and to nothing else.** `DA-5` of the amendment says so; §P1-14.8 and
the composite preamble say so. Prose outside these two regions is not claimed to
be identical and may not be read as if it were.

### §1.3 The pre-selection anchor

```text
P1_WATCHDOG_V2_11_PRE_SELECTION_COMPOSITE_SHA256 = c9712f7c9ae86d4ded8243c6501c29737acae2262ad5a291c7a4b188087687b6
```

One anchor line exists in the amendment, matching `A16(d)`'s grammar exactly
once; the complete token occurs six times in that file and five of the six are
not anchor lines. The retired complete names carrying the generation segments
`8`, `9` and `10` occur **zero** times in either governing file.

**This anchor is not a freshness property, not a monotonic counter, not an
external witness and not a rollback defence.** `TR-2(b)` is unchanged by it.

---

## §2. `R1` — one canonical fifteen-check handoff

### §2.1 What was broken

`§A9` `H-3` of v1.7 and `§P1-14.8` `H-3` of v1.10 were **not** byte-identical,
and stated **different enforcement ranges**. Four sentences of the pair — two in
the composite preamble, one in §A9's own preamble, one in `DA-5` — asserted the
two sections were identical. Against the bytes, those four sentences were false.

The X line traced the exact loss and the Y line traced the same one
independently. Under `§A9`'s range a verifier runs `CK-1`..`CK-12` and returns
success, so `CK-13`'s total member partition, all of `CK-14` (`B14` option
binding, `B15` install-id, `B16` record path, `B17` external count, `B18`
governing digests) and all of `CK-15` (`M7` semantics) never execute.

### §2.2 What v2.11 does

```text
1. EVERY PRE-PRODUCTION RANGE IN THE PAIR IS EXACTLY CK-1..CK-15, IN VP-4 ORDER.
   The string CK-1..CK-12 survives ONLY in sentences that NEGATE it or that
   describe the removed defect. There is no operative twelve-check range in
   either file, and no other proper prefix of the fifteen is a success range.
2. CK-13, CK-14 INCLUDING B14, AND CK-15 ARE MANDATORY BEFORE ANY SUCCESS
   RESULT. H-3 says so in the canonical block; IR-9 already said so and is
   unchanged.
3. H-1..H-4 EXIST ONCE, in one explicitly delimited canonical block, embedded
   byte-identically in both files. THE DIVERGENT COPIES ARE REPLACED, not
   overlaid with a further precedence note.
4. THE EXTRACTION AND HASH CHECK IS STATED, in both files, in prose adjacent to
   the block: two delimiter lines, exactly-once cardinality per file, region
   content concatenated, SHA-256 compared with ca2ff30b…a785.
5. THE IDENTITY CLAIM IS NARROWED at every locus that made it, to the two
   delimited regions of §1.2, and it was verified mechanically (§1.2).
6. THE SHARED OR/CHECK BLOCK REMAINS BYTE-IDENTICAL between the pair, at digest
   9bf4a831…abe5.
```

### §2.3 The executable mismatch fixture, in the governing bytes

The fixture is stated **inside the joint block at `CK-14`**, so both files carry
it byte-identically and no closure is its source.

```text
STATE      every one of the 77 members present and byte-correct; M4 and M7
           genuine; exactly one correctly content-addressed install record; one
           Ed25519 key pair; Stage A and Stage B both CANON at TS-1's and TS-3's
           literal paths; the .sig a valid 128-character Ed25519 signature over
           the exact Stage-B bytes under Stage A's pinned key.
ONE FIELD  Stage A selected_option_token  = the signed W-B token, correctly
             paired with P1_WATCHDOG_SENSOR_ONLY_PCS_FREEZE_V1
           Stage B selected_option_token  = the W-A token
TRACE      CK-2 passes (A8/A9 read Stage A alone; Stage A is a valid W-B
             selection)
           CK-3 passes (B1..B13 are self-contained and none reads
             selected_option_token; B12's Ed25519 verification SUCCEEDS)
           CK-4..CK-13 pass (none of them reads it either)
           CK-14 REFUSES, at B14, with STAGE_B_OPTION_MISMATCH. IR-13 row 35 is
             the sole owner of that equality.
VERDICT    A twelve-check implementation ADMITS this state and therefore FAILS
           CONFORMANCE on this fixture. A conformance suite that does not
           contain it is INCOMPLETE.
```

Composite test row 106 carries an eleventh fixture group `(k)` for the same
state. **Group `(i)`'s expected PASS is preserved unchanged**, as are groups
`(a)` through `(h)` and `(j)`.

---

## §3. `R2` — `KV-1`..`KV-6`, authoritative and self-contained

### §3.1 What was broken

`KV-1`..`KV-6` occurred exactly twice in composite v1.10 — at `§P1-10.7`'s
`SCOPE` line and at test row 89 — and zero times in amendment v1.7. **Neither
occurrence was a cross-reference, because there was no definition anywhere in
either live surface.** Under the signed W-B branch the `§P1-10.7` classifier is
the sole executor of group stops on the endpoint-loss route, and `KV-6`'s
obligation is the only named rule standing between a corrupted handle table and
a self-directed group stop that takes down the PCS and the watchdog together.

### §3.2 Where the definition now lives, and how it was derived

**Composite v1.11 §P1-10.7 carries the complete definition, and nowhere else
does.** `§P1-10.7`'s `SCOPE` line and test row 89 both resolve to it by name.

**It was re-derived from the current v1.7/v1.10 signed invariants, the current
handle and state types, and the currently bound kernel observation primitives.**
The superseded `…AUTHOR_CHOICE_PACKET_V2_DRAFT.md` was **not opened for
behaviour**; `DA-2`, `DA-4` and `IR-12` forbid it, both independent lines
confirmed the prohibition, and no clause below depends on its content. The
composite carries a **source-trace table** naming, for every rule, the live
clauses it comes from.

### §3.3 The shape of the definition

```text
KG-1  the group observation. One /proc/<pid>/stat read through the
      already-bound _open/_read/_close, §P1-10.3's exact errno classification,
      and ONE additional already-present field — the 3rd whitespace-separated
      token after the final ")", the process group id — taken from the same
      buffer as the 20th token §P1-10.3 already parses. Results ABSENT,
      PRESENT_VALID, UNREADABLE, UNPARSABLE, ERROR; only PRESENT_VALID
      contributes.
KG-2  the recorded group field: NULL at creation, written at exactly one place
      after a kernel verification of §P1-7.5 c10's shape, never written again.
      The legitimate population is exactly the group-leader pids of this PCS's
      own current-generation children.
KV-1  current-generation handle
KV-2  role in {CONTROLLER, WORKER}; ownership exactly OWNED; state not REAPED;
      recorded group non-null
KV-3  a FRESH KG-1 observation taken at this instant; PRESENT_VALID required
KV-4  exact start-identity equality; on mismatch, irreversible CONTRADICTED
KV-5  exact equality of the freshly observed process group with the recorded one
KV-6  forbidden-target exclusion: the PCS's own process group, every watchdog
      leader group AND watchdog pid, and the recorded supervisor group of
      SPAWNING_GROUP.json. NOT A SKIP — it terminates the whole classifier.
SC-1  closed candidate set: the PCS's own handle table and nothing else
SC-2  deterministic ascending, deduplicated scope sequence
SC-3  re-verification in full before EVERY _killpg, SEPARATELY FOR EVERY SIGNAL,
      with NO cached success
SC-4  no signal on any failed predicate; no partial, best-effort or override mode
SC-5  the closed result-token set, exactly seven, P1-owned journal tokens only
SC-6  dominance and termination; first-failure evaluation; KV_FORBIDDEN_TARGET
      dominates and terminates the classifier with a single terminal
SC-7  totality over all 72 role x state x ownership x pgid tuples, plus the
      orthogonal stale-generation case; 24 + 32 + 4 + 6 + 6 = 72
SC-8  any value outside the signed sets is STRUCTURAL_VIOLATION under §P1-10.2;
      there is NO default-allow path and no "unknown, proceed" branch
```

### §3.4 What the supporting rule costs, and what it does not

`KG-1` is the **smallest supporting rule** that makes the predicate decidable,
and it is the only thing the live pair did not already carry.

```text
§P1-10.3 STAT_OBSERVE                     UNCHANGED, every consumer unchanged
§P1-3.4 primitive binding                 UNCHANGED — no new primitive
§P1-3.2 scoped import allowlists          UNCHANGED — no name added
MS-11 canonical reachable_closure         UNCHANGED — 89 rows, length 20534,
                                          digest aa974e0c…c20ee
MS-13 project-import dependency surface   UNCHANGED — 4 modules, 6 element keys,
                                          8 effect booleans, 32 assertions false
S-12 / sole-caller discipline             RETAINED — KG-1 calls no fork, wait,
                                          kill or killpg primitive
FC-1's 25 closed failure codes            UNCHANGED — SC-5's seven tokens are
                                          journal tokens, not install-gate codes
```

**Safety was not weakened to avoid a supporting definition**, and there is no
reference anywhere in the pair to an undefined `KV`, `SC`, token or table.

---

## §4. `R3` — the complete generational accounting

### §4.1 The eight new `M2` rows, in `MS-2` order

```text
d5e1d4dbd7731bd6a154c423b36f41e60de771d5ff635423b608bba02d88640f  successor/OFFICINA_GENERIC_HARNESS_WATCHDOG_FREEZE_AUTHORITY_AMENDMENT_V1_6_DRAFT.md
3ce26ba63ca1546ddd7c8422ccf5a4e71e05678e58d1f3deca18e24668e4c1ad  successor/OFFICINA_GENERIC_HARNESS_SUPERVISOR_CONTROL_CHANNEL_P1_OPERATIVE_COMPOSITE_V1_9.md
588fe8a23fd56a4366f920d4b1463d00ee3e7bd8bbc4cc1cbaca61b89a12f489  reviews/fable_officina_p1_watchdog_v2_9_independent_x_confirmation.md
6d83e9b2f082354917b134955d35b8b8f1fdf76761b368c8d34ffae3cd99cf66  reviews/sol_officina_p1_watchdog_v2_9_final_y_confirmation.md
4b7442bd1dafa1ff141212ac8cd59e94983f32633561b6396837ff0767aa48ff  successor/OFFICINA_GENERIC_HARNESS_WATCHDOG_FREEZE_AUTHORITY_AMENDMENT_V1_7_DRAFT.md
86755531f5a7a5f11085802c3e6b5770f4ef5aa90d98ae1a62599348e11f0e8f  successor/OFFICINA_GENERIC_HARNESS_SUPERVISOR_CONTROL_CHANNEL_P1_OPERATIVE_COMPOSITE_V1_10.md
0998fce3b881e0d0d1947c450b442821047f040a4bdd4a987a1a091ece3a56f7  reviews/fable_officina_p1_watchdog_v2_10_targeted_x_confirmation.md
90fb9f9155926df89e9993de1146c05e279639469d7bf2a60c63c6419bc37e52  reviews/sol_officina_p1_watchdog_v2_10_targeted_y_confirmation.md
```

Every digest was recomputed from the bytes on disk in this round. **The two
later W-B binding reviews are NOT substituted for the v2.10 pair-confirmation
rows**: they review the post-selection binding, not the v2.10 governing pair,
and they are members of nothing.

### §4.2 The atomic update

```text
                                       v2.10   v2.11
MS-2   M2 immutable provenance set        55  ->  63
MS-3   M3 accepted peer chain              7      7   unchanged
MS-8   total member cardinality           69  ->  77
TS-3   member_count literal               69  ->  77
composite provenance region rows          63  ->  71
member classes                             7      7   unchanged; only M2 grows
MS-8 arithmetic  M1 2 + M2 63 + M3 7 + M4 1 + M5 1 + M6 2 + M7 1 = 77
MS-9 union       2+63+7+1+1+2+1 = 77 distinct paths
MS-9 inspected literal strings            64  ->  72
```

### §4.3 Every dependent literal that moved with them

```text
JOINT BLOCK (both files, byte-identical)
  MS-1     both literal member paths -> _V1_8_DRAFT.md and _COMPOSITE_V1_11.md
  MS-2     cardinality 63; eight rows appended; the accounting note added
  MS-8     63 / 77
  MS-9     P(M2) 63; 72 inspected strings; the M1-against-M2 argument rewritten
           for this generation's endings; 63-against-7 intersection; 77 union;
           "CK-4 still enumerates 77"
  MS-13.3  the 77-member enumeration; the 77 members --IR-1--> id; MS-8 is 77
  IR-1     "exactly the 77 entries of MS-8"
  IR-3     members ARRAY of exactly 77 OBJECTS
  IR-4     each of the 77 members (M1 2, M2 63, M3 7, M4 1, M5 1, M6 2, M7 1)
  IR-11    mixed-generation examples re-scoped to v1.7/v1.11 and v1.8/v1.10
  IR-13    row 24 -> the V2_11 token; row 38 -> enumerated count 77; the K6/K7
           coverage note -> member_count 77; the B7 coverage row -> 77
  TS-1     the three governing_pre_selection literal paths -> the v2.11 packet,
           the v1.8 amendment, composite v1.11
  TS-2B    A16(d) -> P1_WATCHDOG_V2_11_PRE_SELECTION_COMPOSITE_SHA256
  TS-3     member_count INTEGER exactly 77
  TS-5     B7 -> INTEGER 77; B17 -> enumerated member count 77
  OR-4     "the v1.8 amendment is installed"   [F3 repair]
  OR-9     THE CANONICAL 77-MEMBER LIST
  CK-4     ENUMERATE THE 77 MEMBERS
  CK-6     "not one of the 77 members"
  CK-7     "Visit the 77 enumerated members"
  CK-13    77 entries; also 77; structurally valid 77-entry array; any length
           other than 77; cardinality fixed at 77
  CK-14    the option-mismatch fixture added, referencing the 77 members
  FS-1     "all 77 members exist at their literal paths"
  TR-1     "the 77 members determine install_record_id"

COMPOSITE ONLY
  §P1-18   the literal 63-path list; 71 rows; the 63/7/1 composition; the
           accounting paragraph replacing v1.7's deferral note; the "not counted
           in the 71" exclusions for the packet, the four MS-13 modules and the
           identity signature; eight rows appended to the region list
  row 89   KV/SC resolution and the adversarial scope fixtures
  row 101  SC-5's seven tokens named, "and no eighth"
  row 103  70 recorded digests
  row 104  all 77 members
  row 105  a members array of other than 77 entries
  row 106  eleven fixture groups; "all 77 of its members"; group (k)
  row 107  77 -> 76; one of the 63 literal provenance paths
  row 108  78 entries against CK-4's 77; any length other than 77; a region
           enumeration yields 70 instead of 63
  row 114  mixed generation re-scoped to v1.7/v1.11 and v1.8/v1.10
  row 115  all 77 member digests

AMENDMENT ONLY
  §A0.4    the V2_11 token everywhere; the anchor value; the composite path in
           the extraction fixture; the token occurrence count
  §A9      the five-place generation-scoped audit; the heading-defines-the-rule
           audit clause
  §A11 N-14 rewritten: the accounting is performed, not deferred
```

### §4.4 What did not move

```text
the 89-row reachable_closure VALUE, its 14-row bootstrap subset, its seven
  unexecuted branches, its CANON length 20534 and its digest
  aa974e0c91e5c9afd0aceefa6b0e47ef42b5ad7b71dc4de690a4873232dc20ee
MS-11, MS-11.1..MS-11.6, MS-13 and MS-13.1..MS-13.3 in substance
the seven member classes and MS-9's twenty-one-pair proof structure
FC-1's 25 closed failure codes and the retirement of MEMBER_EXTRA
the CK-13 D1/D2 partition
IR-13's 50 rows and its K1..K5 / K6..K8 relation-class boundary
MS-7's rows_attested 92..115, row_count 24 and all_rows_passed true
MS-6's two modules, their fixed order and the 92..103 / 104..115 split
the M4 21-key set and CK-10's exactly nine semantic relations
FS-1..FS-5, TR-1, TR-2(a) and TR-2(b), XS-1
H_GUARDDATA and the VARIANT_MARKER class
the 16-name generic_harness.py scoped allowlist and S-12
```

---

## §5. `R4` — the two logged Minors, repaired

```text
F3  OR-4 said "the v1.3 amendment is installed" while MS-1 named a far later
    generation, and §A9's audit claimed FOUR generation-scoped operative
    strings when this was a fifth. THE STRING IS INSIDE THE JOINT BLOCK, so the
    repair lands in BOTH files and the block remains byte-identical — the X line
    corrected the v1 binding's framing of it as an amendment-only locus, and the
    correction is carried. §A9's audit now enumerates FIVE loci and says which
    file each lives in.
F4  composite line 90's "(`G-10`, §P1-14.3)" now reads §P1-14.4, where G-10 is
    defined. Line 90 is outside REGION(BODY), so this moves H_FILE only, not
    H_BODY or H_NORMATIVE. §A9's audit is strengthened from "the named heading
    exists" to "the named heading is the one that defines the named rule".
STALE-STRING SWEEP, folded in because the files regenerate anyway:
    the composite's own "full replacement for version 1.8" self-description,
      stale by two generations, now names version 1.10;
    the composite's Version-1.9 identity-weakening sentence now names 1.11;
    authority level 3's predecessor lists in both files now name every
      superseded composite (through 1.10) and every superseded amendment
      (through 1.7);
    the amendment's replacement chain names version 1.7 and reads "all eight";
    DA-1's two version lists; DA-4's two surface names; the acceptance-token
      version and its reviewer-independence range.
```

---

## §6. Recommendation, tokens and invariants

### §6.1 There is no recommendation, because the cell is signed

**This packet makes no recommendation and states no option comparison.** The
watchdog-freeze mechanism cell was signed on 2026-08-05 and the selection is
`W-B`, sensor-only. Nothing here re-opens it, re-weighs it or predicts anything
about it.

### §6.2 The closed validation vocabulary is retained in full

`TS-1` remains the **closed two-option validation set** and it is not narrowed
by the selection. Both option tokens and both paired option-specific amendment
tokens **must remain** in `TS-1` after `OR-4`:

```text
selected_option_token            EXACTLY ONE OF
  I_SELECT_P1_WATCHDOG_FREEZE_A_WATCHDOG_REQUESTS_PCS_EXECUTES
  I_SELECT_P1_WATCHDOG_FREEZE_B_PCS_FREEZES_ON_PEER_ENDPOINT_LOSS
selected_option_amendment_token  THE PAIRED ONE OF
  P1_WATCHDOG_SINGLE_OPCODE_CAPABILITY_V1  <-> _FREEZE_A_
  P1_WATCHDOG_SENSOR_ONLY_PCS_FREEZE_V1    <-> _FREEZE_B_
```

Deleting the non-selected literals would break `TS-2A` `A8` and `A9`, `TS-5`
`B14`, `IR-13` row 47, **and** the joint block's byte identity, since `TS-1`
lives inside it. **"Remove every W-A string" is not a valid resolution rule**, and
the regenerated binding replaces it with an exact permitted-occurrence table.

### §6.3 Tokens

```text
SIGNED, NOT REOPENED
  I_SELECT_P1_WATCHDOG_FREEZE_B_PCS_FREEZES_ON_PEER_ENDPOINT_LOSS
  I_SELECT_P1_PROCESS_CLAIM_IDENTITY_A_OBSERVATION_ONLY

UNSIGNED, VERSION-BUMPED TO THIS PAIR, AND NOT MADE SIGNABLE HERE
  I_ACCEPT_OFFICINA_GENERIC_HARNESS_WATCHDOG_FREEZE_AUTHORITY_AMENDMENT_V1_8

NOT ACCEPTED, AND NOT PREDICTED
  P1_IDENTITY_OBSERVATION_BOUNDED_WEAKENING_V1

OPTION-SPECIFIC AND COMMON AMENDMENT TOKENS THE SIGNED CHOICE ADOPTS, NONE OF
WHICH THIS PACKET ACCEPTS OR INSTALLS
  P1_WATCHDOG_SENSOR_ONLY_PCS_FREEZE_V1
  P1_FREEZE_ABSENT_FALLBACK_NULLABLE_IDENTITY_V1
  P1_PCS_FREEZE_CLASSIFIER_V1
  P1_WATCHDOG_FREEZER_ROLE_REASSIGNMENT_V1
  P1_FREEZE_PUBLICATION_L6_L9_V1
```

**Even a future signature of the acceptance token authorizes no code edit, no
`OR-3`, no key or entropy, no `OR-4`, no install and no `T` activation.**

---

## §7. Independence

This packet, the governing pair it describes, the regenerated binding and
handoff drafts and the companion closure were **all written by the same author
line**. That line **cannot** be an independent X or Y reviewer of any of them.

The v2.11 pair requires a **fresh bounded independent X-line and Y-line round on
identical bytes**, performed by reviewers that did not author v2.3 through
v2.11, before the acceptance token may become signable and before the binding
and handoff can be reviewed again.

---

## §8. Negative space

This packet creates nothing executable and authorizes no selection, X/Y verdict,
acceptance, implementation, commit, verifier or manifest edit, process, socket,
pipe, fork, exec, signal, wait or `prctl` operation, supervisor, PCS,
controller, worker or watchdog, capability, world, learner, entropy, candidate,
trajectory, capacity artifact, custody disposition, result manifest, spend,
datum, outcome, Proof or claim movement.

No key pair, entropy, Stage-A selection artifact, Stage-B authorization
artifact, detached signature, manifest, attestation, member list or install
record was generated, requested or predicted. No `OR` step ran; **`OR-4` did not
run, and no resolved amendment or composite bytes exist at any path.** No
identity token was accepted and no identity bounded weakening was authorized. No
`/proc` was read against any live process. No clock was sampled for any contract
purpose. No project or production module was imported, executed, compiled or
edited.

```text
T = NOT_ACTIVATED
PROGRAMME CLAIM = OPEN
P1 PROCESS-CLAIM IDENTITY CELL = SELECTED: OPTION A, OBSERVATION-ONLY
P1 IDENTITY BOUNDED-WEAKENING TOKEN = NOT ACCEPTED
P1 WATCHDOG-FREEZE CELL = SELECTED: OPTION W-B, SENSOR-ONLY
WATCHDOG AUTHORITY AMENDMENT V1.8 = NOT ACCEPTED
IMPLEMENTATION AUTHORIZATION = NOT GRANTED
ATOMIC HANDOFF = OR-2 COMPLETE; OR-3..OR-11 NOT AUTHORIZED
```

The exact selected token and the formal selection signature govern. Saved chat
responses and author closures are provenance aids only.
