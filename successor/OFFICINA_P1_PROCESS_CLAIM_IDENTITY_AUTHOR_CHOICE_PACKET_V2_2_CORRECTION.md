# Officina P1 process-claim identity — author choice packet v2.2 (bounded correction)

**Author:** Claude Code Opus 5, **specification author only**. Not an
independent X-line or Y-line reviewer. **This correction selects nothing.** It
closes exactly the three residuals that the two independent bounded *final*
confirmation lines returned `REVISE` on against the v2.1 bytes, and changes
nothing else.

**No token in this correction is signable.** Every token remains signable only
after a bounded independent X-line and Y-line confirmation round on identical
bytes. `T` is `NOT_ACTIVATED`; the programme claim is `OPEN`; the
watchdog-freeze cell is `UNRESOLVED AND ORTHOGONAL`. This document creates
nothing executable and authorizes no implementation.

**Status.** v2.2 is a **bounded correction of a bounded correction**, not a
replacement. It carries
`successor/OFFICINA_P1_PROCESS_CLAIM_IDENTITY_AUTHOR_CHOICE_PACKET_V2_1_CORRECTION.md`
forward **verbatim** except for the three loci named in the replacement index at
§0.2, and v2.1 in turn carries
`successor/OFFICINA_P1_PROCESS_CLAIM_IDENTITY_AUTHOR_CHOICE_PACKET_V2_DRAFT.md`
forward verbatim except for its own two loci. v2, v2.1, v1, both v1 reviews,
both v2 confirmations and both v2.1 final confirmations are preserved
byte-untouched as the evidentiary record. **Reading order: v2, then v2.1, then
v2.2. Where v2.2 and v2.1 differ, v2.2 governs; where v2.1 and v2 differ, v2.1
governs; everywhere else v2's text is the operative text and is read as
written.**

**Bounded repair mandate.** Both final confirmation lines returned `REVISE` and
both are treated here as **binding defect reports**, adopted without
reservation:

```text
X-line, reviews/opus_officina_p1_process_claim_identity_choice_v2_1_final_confirmation.md
        REVISE_OFFICINA_P1_IDENTITY_V2_1. Determination 2 — a leaking AST
        satisfies every rule of S-25a..S-25m and reaches a second sink:
            p   = "successor/officina/runtime/T_PROCESS_CLAIMS/" + process_id + ".json"
            raw = open(p, "rb").read()
            m   = json.loads(raw)
            vals = list(m.values())
            leaked = vals[5]                    # controller_pid by key order
        Root cause: M-R4's decidability rests on D-8's premise "each durable
        artifact has exactly one open site", which §P1-13.7 establishes for
        INSTALLS and for P1-LAYER reads but NOT for PEER-LAYER reads of the
        process claim — the one root where the governed code lives. Repair 2
        (C-5 / YV2-C1) was confirmed fully closed on the same bytes.
Y-line, reviews/sol_officina_p1_process_claim_identity_choice_v2_1_final_confirmation.md
        REVISE_OFFICINA_P1_IDENTITY_V2_1. Two independent items:
        (i)  C-5, DC-1 and DC-6 assert exactly one SHA-256 / one carrier-derived
             digest, while the same correction expressly requires a SECOND
             ACC-5 evaluation over occupant_bytes for collision conjunct X-4.
             Calling that result a boolean comparison operand does not make the
             second digest cease to exist.
        (ii) DC-3, DC-4, DC-5 and WL-4(a) OVERSTATE what whole-object hashing
             proves. Given the other eighteen canonical fields the equality
             test over the forced attested_pgid == attested_pid space has at
             most 4,194,304 candidates; the constructing actor already holds
             those fields and an archive reader reads the integers in
             cleartext. The absolute claims "never process identity" and
             "never evidence/comparison" are false outside their narrower,
             normative authorized-use sense.
```

**Nothing else is reopened.** The eight findings both lines confirmed closed
(`X M-1`, `X m-1`, `X m-2`, `X m-3`, `Y-C2`, `Y-M1`, `Y-M2`, `Y-m1`) are
untouched, and so is the whole of Repair 1's mechanism that the X line confirmed
sound (`S-25i`, `M-R1`/`M-R2`, `S-25j`, `S-25k`, `CR-1`..`CR-4`, `MS-4`..`MS-12`)
and the whole of Repair 2's architecture that both lines confirmed correct
(`C-5` as a record-level consumer, `ACC-4`/`ACC-5`, `ACC-R5`, the two direct
destinations, `DC-2`, `DC-7`, `RC-1`..`RC-4`, `§3.5`'s model choice, `§3.6`'s
destination search). §8 lists every one of them with the exact locus that must
remain intact.

---

## §0. What v2.2 changes, and where

### §0.1 The three residuals, in the reviewers' own terms

```text
RESIDUAL A — THE FRESH CLAIM-REOPEN PATH (X-line determination 2).
  v2.1 pinned the MAPPING (M-R1..M-R5, S-25j) and the BYTES (CR-1..CR-4,
  S-25k) — but only as occurrence disciplines over three governed mapping
  Names and three carrier Names. It did not pin the PATH or the READ. So a
  second open() of the claims path in generic_harness.py, where the builtin
  open is deliberately RETAINED (S-25i-N1) and where the peer layer legitimately
  opens many durable records, produces a byte string bound to a NON-CARRIER
  Name; json.loads of it produces a mapping bound to a NON-GOVERNED Name; and
  .values()[5] then reaches controller_pid touching no governed Name, no
  carrier Name, no key literal, no dunder and no reflective name. S-25i/j/k,
  M-R1/M-R2 and CR-* are all blind. M-R4's intended catch — "no other
  expression may yield a claim or lease mapping" — is not DECIDABLE without
  the taint reasoning D-9 forbids.

  The X line's three-part repair, adopted here verbatim in substance:
    1. pin the claims path literal to exactly one construction site, MS-1;
    2. pin every claim/occupant read to _read_claim_bytes at MS-2, so that
       every claim byte string is bound to a carrier Name;
    3. pin json.loads of a claims read to MS-3 (which (2) largely subsumes).

RESIDUAL B — THE TWO ACC-5 EVALUATIONS (Y-line §3, §9.1).
  C-5's "EXACTLY ONE SHA-256", DC-1's "there is never a second" and DC-6's "NO
  SECOND DIGEST ... the only value derived from a carrier" are contradicted by
  v2.1's own §3.2 paragraph and by S-25m's "exactly two ACC-5 call sites". The
  X-4 occupant digest is a real second digest value. It is legitimate integrity
  checking; the count and classification texts, not the operation, are wrong.

RESIDUAL C — THE OVERSTATED CRYPTOGRAPHIC CLAIM (Y-line §5, §9.2).
  DC-3 "never process identity, ... never a name of anything addressable",
  DC-4 "may not enter ... comparison ... evidence", DC-5 "ONE-WAY", and
  WL-4(a) "the eighteen other canonical values are obtainable only by reading
  the claim" are false as ABSOLUTE assertions. WL-3 already disclosed the
  4,194,304-candidate search but the surrounding rules then denied the channel
  it creates. The AUTHORIZATION boundary is sound and must be preserved; the
  CRYPTOGRAPHIC boundary must be withdrawn and restated honestly.
```

All three were re-derived here from the committed contract bytes and from the
v2.1 bytes, not accepted on the reviewers' authority. All three are correct.

### §0.2 The exact replacement index — three rows, and no fourth

| # | v2.1 locus replaced | Replaced by | Closes |
|---|---|---|---|
| **A** | §2.4 rows `MS-1`, `MS-2`, `MS-3` **as they bear on the path and the read**; §2.7 `D-8`; and `M-R4`'s decidability anchor | **§2 of this correction**: the path-anchoring rules `PA-1`..`PA-9`, the path-constructor table `PC-1`/`PC-N`, the closure theorem `PT-1`, the amended `D-8′`, and the new verifier rule `S-25n` | X-line determination 2 — the fresh claim-reopen path |
| **B** | §3.2 `C-5`'s "OPERATION. EXACTLY ONE SHA-256" and its "the one enumerated second invocation" paragraph; §3.4 `DC-1`, `DC-6`; §4.3 `S-25e`; §4.4 `S-25l`, `S-25m`; §6.1's declassification row; §6.3 step 5; §7 `A-T15`(a) | **§3 of this correction**: the two authorized evaluations `EV-1`/`EV-2`, the transitive-lineage enumeration `L-1`..`L-5`, the occupant-digest confinement `OD-1`..`OD-4`, the amended `C-5`, `DC-1′`, `DC-6′`, `S-25e′`, `S-25l′`, `S-25m′`, and the new verifier rule `S-25o` | Y-line §9.1 and §9.4 — the two `ACC-5` evaluations and the transitive lineage |
| **C** | §3.4 `DC-3`, `DC-4`, `DC-5`; §3.5 `WL-3`, `WL-4` | **§4 of this correction**: the two predicates `IP`/`ACU`, the honest claim scope `CS-1`..`CS-7`, and the replaced `DC-3′`, `DC-4′`, `DC-5′`, `WL-3′`, `WL-4′` | Y-line §9.2 and §9.3 — the narrowed cryptographic claim and the preserved authorization boundary |

**Everything else in v2.1 and in v2 carries forward verbatim.** In particular
v2.1 §2.1, §2.2 (`S-25i`, `S-25i-N1`..`N4`), §2.3 (`M-R1`, `M-R2`, `M-R3`,
`M-R5`, `S-25j` and its scope note), §2.4 rows `MS-4`..`MS-12` and
`MS-R1`..`MS-R4`, §2.5 (`CR-1`..`CR-4`, `S-25k`), §2.6, §2.7 `D-5`/`D-6`/`D-7`/
`D-9`, §2.8 `P-1`..`P-4`, §3.1, §3.2's precondition/keys-read/destinations/
forbidden blocks, §3.3 (`ACC-4`, `ACC-5`, `ACC-R5`, class member `(f)`), §3.4
`DC-2`, `DC-7`, §3.5 `WL-1`, `WL-2` and the whole model-choice argument, §3.6,
§3.7 (`RC-1`..`RC-4`), §4.1, §4.2, §4.3's `S-25d`/`S-25g`, §5, §6.2, §7's
`A-T13`, `A-T14`, `A-T15`(b), `A-T16`, §8 and §9 stand as written, together with
the whole of v2 as v2.1 already carries it.

**No selection is made. Neither `A` nor `B` is chosen. The weakening token is
neither minted nor accepted.**

---

## §1. Binding inputs, on committed bytes

All digests below were recomputed with `sha256sum` on the committed bytes of
this repository at the time of writing, and each working-tree file was verified
byte-identical to its `HEAD` blob.

### §1.1 The bytes this correction repairs, and the verdicts it answers

```text
3796de017449a9786db0b9b0ca0e8c2d84762e2239463033773b1fdb92b8ef37  successor/OFFICINA_P1_PROCESS_CLAIM_IDENTITY_AUTHOR_CHOICE_PACKET_V2_1_CORRECTION.md
c2d7a95784ad1bbc2a34898c0d3abf4de94dcd3416b14b959a3b2b61d6fab614  reviews/opus_officina_p1_process_claim_identity_choice_v2_1_final_confirmation.md
cee60b4b85358a50a90729645081419b166cbc1224b53776ffb41a357cb5f578  reviews/sol_officina_p1_process_claim_identity_choice_v2_1_final_confirmation.md
```

The v2.1 digest `3796de01…ef37` is the value **both** final confirmation lines
independently recomputed and pinned as their target (X §0; Y §2.1), so the bytes
v2.2 repairs are the bytes the two `REVISE` verdicts were returned against.

### §1.2 The preserved evidentiary record, confirmed byte-untouched

```text
ad8b5791f043f201c00812a11de2ab3b765664e65e6d0ebf9778e150913096d3  successor/OFFICINA_P1_PROCESS_CLAIM_IDENTITY_AUTHOR_CHOICE_PACKET_V1_DRAFT.md
f5d95a0d4a7c72731b5a20cf668e67dbc66329e0989fb945bd0a5727717f6095  successor/OFFICINA_P1_PROCESS_CLAIM_IDENTITY_AUTHOR_CHOICE_PACKET_V2_DRAFT.md
b7d061f5c60d75705f50ffc100bff24664336107dd450a8372e825c6f1afffa0  reviews/opus5_officina_p1_process_claim_identity_choice_v2_closure.md
0b104f3ec240acc5e067184efb752091f92920da7773c78aa35337de6a30f129  reviews/opus_officina_p1_process_claim_identity_choice_v2_confirmation.md
152b6dd2237a63d3ada6bd6a82a828892443a7752f838abf71cba0401ac01eb8  reviews/sol_officina_p1_process_claim_identity_choice_v2_confirmation.md
56d0f598331a713918ea3f5b642449dd4dca1a08224b6e9eb4afb239ba128246  reviews/opus5_officina_p1_process_claim_identity_choice_v2_1_closure.md
```

Every one of these matches the value the two final confirmations recorded. No
existing file is modified by this correction.

### §1.3 The governing signed chain, recomputed

```text
2c857fa8ad7be1c861eb8cf561f396e7d2339403c7714abc7958745bf34e5d5d  successor/OFFICINA_GENERIC_HARNESS_SUPERVISOR_CONTROL_CHANNEL_P1_OPERATIVE_COMPOSITE_V1_2.md
cd106d7fef491601f9ff948aba3ba0ceaac0774ac18a6564247c0c5899b4c40c  successor/OFFICINA_T_ACTIVATION_PROTOCOL_V2_CORRECTION.md
64b8d3f63594b79a6abc767a032383c5704beaf09b32a1e0c58fdc444bb0af71  successor/OFFICINA_GENERIC_HARNESS_CONTRACT_V2_DRAFT.md
8c47da352ef5954406964647a32e97939c404806bdf9b3d3ff5bc70866e6369a  successor/OFFICINA_GENERIC_HARNESS_SIGNATURE.md
```

Load-bearing loci read directly for this correction:

```text
composite :349-357     §P1-3.1, the five production roots, exactly five paths
composite :359-375     §P1-3.2, the import allowlists; generic_harness.py 17
composite :2095-2128   §P1-13.2 row 2 — the claim's path rule
                       "successor/officina/runtime/T_PROCESS_CLAIMS/<process_id>.json",
                       its twenty-key set, and its exactly two reader classes:
                       the generic-harness peer layer, and the freeze-evidence
                       acceptance predicate
composite :2354-2371   §P1-13.7 — "exactly one root and one function, so that no
                       two layers can INSTALL the same no-replace record"; the
                       table pins INSTALL sites and three NAMED reads
composite :2566        S-2   — no Lambda, Global, Nonlocal, Yield
composite :2573        S-4   — every bound name assigned exactly once
composite :2577        S-6   — every Call func is a plain Name or a bound name
composite :2581        S-7   — forbidden names, scoped "the PCS and role roots"
composite :2601        S-12  — subprocess, Popen, fork, waitpid, kill, killpg,
                       system appear on NO PATH of generic_harness.py
composite :2603        S-13  — no "/proc/self/fd/" literal is concatenated with
                       a non-constant expression; the descriptor paths are exact
                       constants                      <-- THE FRAMERS' OWN
                                                          PATH-SPELLING RULE
composite :2753        invariant 84 — "the P1 layer opens the process-claim and
                       freeze-observation records on no path"
composite :2757        invariant 88 — duplicate claim WRITE; one INSTALL site
protocol  :83          the claim's path rule, restated
protocol  :231-238     the twenty claim keys, in canonical order
protocol  :241-246     the lease keys — the claim keys plus five
protocol  :248-257     t-process-record.v1's key set, carrying
                       process_claim_sha256 and NEITHER identity key
protocol  :85-97       the exact archival sets
contract  :99-102      §2c.2 T_PROCESS_STARTED carrying process_claim_sha256
contract  :103-106     §2c.3 the lease's prior_charge_event_sha256 seeded to the
                       T_PROCESS_STARTED entry hash
contract  :125-140     §2c.6 the valid-close order; T_PROCESS_STOPPED carrying
                       process_record_sha256 of the final record
contract  :165-173     §2c.12 the invalid-close order and its archival set
```

**The X line's key-order arithmetic, re-derived and confirmed.** The twenty
canonical claim keys at `protocol :231-238` are, in order: `schema`(0),
`scientific_outcome`(1), `activation_record_sha256`(2), `process_id`(3),
`process_sequence`(4), **`controller_pid`(5)**, `controller_start_identity`(6),
**`process_group_id`(7)**, `argv`(8), `behavior_source_sha256`(9),
`config_sha256`(10), `stack_sha256`(11), `numerical_mode_sha256`(12),
`device_identity`(13), `device_units`(14), `created_utc`(15), `clock_kind`(16),
`boot_identity`(17), `start_reading_ns`(18), `immutable_control_sha256`(19).
`vals[5]` **is** `controller_pid` and `vals[7]` **is** `process_group_id`. The
counterexample is exact, not illustrative.

---

## §2. Repair A — closing the fresh claim-reopen path

**Design constraint, restated and not spent.** This repair introduces **no
taint analysis, no call graph, no fixpoint, no interprocedural dataflow, and no
soundness assumption about value flow**. Every rule below is a name match, a
node-shape match, an occurrence count, a position match, a constant fold over
`Constant` nodes only, or an **intra-function single-assignment lookup** — the
last of which is a lookup in one function body's own `Assign` index, made
unambiguous by `S-4`'s assign-once discipline (composite `:2573`). §2.6 states
that cost explicitly rather than hiding it inside "decidable".

The X line named the requirement precisely: *"Make recognition
syntax-mechanical: enumerate exact path constructors, call forms and operands.
Do not require taint, dataflow or semantic 'can denote' reasoning without a
closed syntactic rule."* §2.5's theorem `PT-1` is that closed syntactic rule:
it converts *"can this expression denote `T_PROCESS_CLAIMS`?"* from a semantic
question into a four-case syntactic case analysis.

### §2.1 Why v2.1's rules did not reach the construct — re-derived, not summarized

```text
G-1  D-8's load-bearing sentence reads: "§P1-13.7 (:2357-2368) already gives
     each durable artifact exactly one open site." Re-derived from composite
     :2354-2371, §P1-13.7's actual sentence is "Every interface operation is
     assigned to exactly one root and one function, so that no two layers can
     INSTALL the same no-replace record." Its table pins INSTALL sites and
     three NAMED reads — spawn-intent at SPAWN_ROLE, supervisor identity at c17,
     supervisor identity in the watchdog. It pins no peer-layer claim READ.
G-2  Invariant 84 (:2753) says "the P1 layer opens the process-claim and
     freeze-observation records on no path." That constrains the P1 LAYER —
     the four scripts. generic_harness.py is the PEER layer and is where every
     governed value lives.
G-3  Invariant 88 (:2757) enforces one INSTALL site per artifact ("duplicate
     claim WRITE"). It says nothing about reads.
G-4  S-25i-N1 deliberately RETAINS the builtin open in generic_harness.py, and
     that decision is correct: the peer layer's signed durable I/O must not be
     withdrawn by an identity packet. The X line agrees the fix is an
     open-SITE PIN, not an open BAN.
G-5  v2.1 §2.4 MS-1 describes "one path construction over the fixed constant
     successor/officina/runtime/T_PROCESS_CLAIMS/" — but NO RULE ANYWHERE IN
     v2.1 says that constant occurs only there, and process_id is a
     non-restricted 64-hex claim key freely in scope in the peer layer, which
     builds the claim at MS-4.
G-6  MS-2 is called at >= 2 sites by design (post-install verify, and the
     EEXIST occupant load MS-11), so "exactly one open site" is not even true
     inside v2.1's own design. D-8's premise fails on two independent counts.
G-7  CONSEQUENCE. Every claim byte string is forced through a carrier Name if
     and only if peer-layer opens of the claims path are pinned to MS-2. They
     were not. The mapping and carrier disciplines are airtight for values that
     ENTER through them, and blind to a value that never does.

WHAT WAS NOT AT RISK, so the repair is not sold as wider than it is:
G-8  S-12 (composite :2601) bars subprocess, Popen, fork, waitpid, kill,
     killpg and system from generic_harness.py ON EVERY PATH, so no
     process-mediated read of the claim exists in the peer root.
G-9  mmap, io, codecs, shutil, fileinput and linecache are in NEITHER the
     19-member global allowlist NOR generic_harness.py's 17-member scoped
     allowlist (§P1-3.2), so they are UNIMPORTABLE in all five roots today.
     PA-6 still enumerates them, so that a future allowlist change cannot
     silently reopen the route.
```

### §2.2 The precedent this repair follows

`S-13` (composite `:2603`) reads: *"no `/proc/self/fd/` string literal is
concatenated with a non-constant expression; the descriptor paths are exact
constants."* The framers have already decided, for the one path family where
misdirection would be fatal, that the answer is a **constant-only spelling rule
plus an enumerated site**, not a dataflow analysis. `PA-1`..`PA-3` are `S-13`'s
discipline applied to the claims path family. This is not a new kind of rule in
this contract; it is the existing kind, extended to the one path family the
identity cell owns.

### §2.3 `PA-1`..`PA-9` — the path-anchoring rules

#### §2.3.1 Spelling: the claims root can be written in exactly one place

```text
PA-1  THE CLAIMS-ROOT LITERAL IS PINNED TO MS-1.
      In the five production roots of §P1-3.1, a string or bytes Constant whose
      value contains the substring "T_PROCESS_CLAIMS" occurs EXACTLY ONCE: as
      the single Constant path-root operand inside _claim_path (MS-1). Any
      other occurrence, in any syntactic position, at any depth, in any of the
      five roots, is a static violation.
      RECOGNITION: substring test over the value of every Constant node in the
      parsed AST. No resolution, no imports, no flow.

PA-2  NO ASSEMBLED SPELLING. In the five roots, a PATH-BUILDING EXPRESSION is
      any of: BinOp Add or Mod whose operands include a str/bytes Constant; a
      JoinedStr (f-string); a Call to .format, .join, os.path.join,
      os.fspath, os.path.normpath, os.path.abspath, os.path.realpath,
      os.path.expanduser, os.path.expandvars, pathlib.Path, pathlib.PurePath,
      PosixPath, .joinpath, .with_name, .with_suffix, .with_stem, .relative_to,
      .resolve, .absolute, .expanduser, .parent, .parents, .readlink; or a
      BinOp TrueDiv either of whose operands is a pathlib object.
      EVERY path-building expression in the five roots occurs INSIDE a PATH
      CONSTRUCTOR (§2.4), and each of its operands is either
        (a) a str/bytes Constant, or
        (b) the constructor's own grammar-checked stem parameter Name (PA-3).
      A path-building expression whose operand is a Call, a Subscript, an
      Attribute, a comprehension variable, a parameter of a non-constructor
      function, an os.environ read, or any Name not satisfying (b) is a static
      violation. This is S-13's rule (composite :2603) generalized from one
      path family to every path family in the five roots.
      RECOGNITION: node-shape match at each path-building expression, plus the
      intra-function check of PA-3. No flow.

PA-3  GRAMMAR-CHECKED STEMS. Every path constructor takes at most one dynamic
      stem parameter. Its FIRST statement is a grammar check that refuses any
      value containing "/", "\\", NUL, "..", a leading ".", or any byte outside
      the constructor's own pinned character class, and whose refusal branch
      raises or routes to the invalidity disposition with no fallthrough. For
      MS-1 the pinned class is the 64-lowercase-hex process_id stem already
      required by §2.4. A constructor without this first statement, or with a
      second dynamic operand, is a static violation.
      RECOGNITION: node-shape match on the constructor's first statement and on
      its parameter count. No flow.
      PURPOSE: PA-3 is what makes traversal spellings — a stem of
      "../T_PROCESS_CLAIMS/x.json", or "T_PROCESS_CLAIMS/x.json" appended to a
      shared runtime root — unspellable, so that PA-1's substring pin cannot be
      evaded by splitting the literal across a constructor boundary.
```

#### §2.3.2 Reads: the claim is opened in exactly one function

```text
PA-4  CLAIM-PATH NAMES, EXACTLY ONE.
      MS-1 (_claim_path) is DEFINED once and CALLED at exactly one site, and
      its result binds to exactly one Name, claim_path. The occupant path of
      MS-11 IS claim_path — the EEXIST occupant occupies the very path this
      install targets (v2 §2.10.3, protocol :83) — so no second path Name
      exists for it and none may be introduced.
      claim_path occurs in EXACTLY THREE positions and NOWHERE ELSE:
        (a) the path operand of the single read call inside MS-2;
        (b) the path operand of the single atomic no-replace write at MS-12;
        (c) the argument of the MS-11 occupant load, which is MS-2 then MS-3.
      It is never aliased, re-assigned, returned, stored in a container, passed
      to a non-MS function, compared, formatted, logged, or joined.
      ⇒ this closes the ALIAS variant (q = claim_path) by position, and the
        SECOND-CONSTRUCTION variant (p = _claim_path(pid)) by call count.

PA-5  READ-OPERAND SHAPE. In the five roots, the path operand of every
      enumerated read call form (PA-6) is a PLAIN NAME. Never a Constant,
      never a concatenation or f-string, never a Call result, never a
      Subscript, never an Attribute, never a comprehension variable, never a
      starred or defaulted argument.
      RECOGNITION: node-type match at the call's path argument. No flow.

PA-6  ENUMERATED READ CALL FORMS. For PA-5, PA-7 and S-25n, a READ CALL is any
      Call whose func is, or whose func's attr is, one of:
        builtin open; os.open, os.read, os.pread, os.preadv, os.readv,
        os.sendfile, os.copy_file_range, os.readlink, os.listdir, os.scandir,
        os.walk, os.fwalk, os.stat, os.lstat, os.statvfs;
        pathlib .open, .read_bytes, .read_text, .iterdir, .glob, .rglob,
        .stat, .lstat, .readlink;
        mmap.mmap; io.open; io.FileIO; codecs.open; fileinput.input;
        linecache.getline; shutil.copyfileobj
      — the last seven being unimportable today (G-9) and enumerated so that a
      future allowlist change cannot silently reopen the route.
      NO READ CALL IN THE FIVE ROOTS PASSES A dir_fd OR follow_symlinks
      KEYWORD, and os.chdir, os.fchdir, os.symlink and os.link appear in no
      production root, so no read is resolved relative to a redirected base.

PA-7  THE CLAIM READ IS PINNED TO MS-2. A read call whose path operand is the
      Name claim_path occurs ONLY inside _read_claim_bytes (MS-2), which
      contains EXACTLY ONE read call and exactly one .read(). Every other read
      call in the five roots has a path operand that is a Name assigned exactly
      once, in its own enclosing function body, from a call to a path
      constructor of §2.4 other than MS-1. A read call whose path operand is a
      bare parameter Name of a non-constructor function, or a Name with no such
      binding in the enclosing body, is a static violation — i.e. NO
      GENERAL-PURPOSE READ HELPER EXISTS IN THE FIVE ROOTS.
      RECOGNITION: name match, site match, and one intra-function
      single-assignment lookup. Not interprocedural. No call graph. No fixpoint.
      ⇒ this closes the HELPER-RETURN variant
        (def _get(p): return open(p,"rb").read()) twice: at the helper's own
        read, whose operand is an unbound parameter Name; and at the call
        _get(claim_path), which is a fourth position for claim_path.

PA-8  IMMEDIATE CARRIER BINDING. The byte string produced by MS-2's read binds
      IMMEDIATELY and ONLY to a carrier Name of CR-2. Inside MS-2:
        - the read call's value is the RHS of exactly one Assign whose single
          target is a carrier Name, or is the direct operand of exactly one
          .read() whose value is that RHS;
        - the function's only Return returns that carrier Name, bare;
        - NO alternate variable, tuple or list target, Starred target,
          augmented assignment, walrus, default argument, container literal,
          dict value, set element, generator, comprehension, callback, Lambda
          (already banned by S-2), decorator, class attribute, global or
          nonlocal (both banned by S-2), context-manager __exit__ value, or
          EXCEPTION PAYLOAD receives it;
        - MS-2 contains no try/except/else/finally whose body binds, re-raises
          with, logs, or formats the bytes, and no branch returning a second
          shape (MS-R2).
      RECOGNITION: node-shape match inside one function body. No flow.

PA-9  CANONICAL PARSING IS PINNED TO MS-3. In the five roots:
        (a) json.loads and json.load occur only with a PLAIN NAME operand —
            never a Call, Subscript, Attribute, concatenation or literal — so
            that every parse operand is classifiable by Name alone;
        (b) a json.loads or json.load whose operand is a carrier Name occurs
            ONLY inside _claim_mapping_from_bytes (MS-3), which contains
            exactly one such call (already CR-3(a); restated here so the parse
            pin is stated as its own rule);
        (c) json.JSONDecoder and json.JSONEncoder remain banned root-wide by
            S-25i(iii), and ast.literal_eval by S-25i(iii);
        (d) NO FRESH MAPPING MAY BE PRODUCED FROM A CLAIM-PATH READ OUTSIDE
            MS-3. By PT-1 the only claim-path read is MS-2's, by PA-8 its
            bytes bind only to a carrier, and by (a)+(b) a carrier reaches
            json.loads only at MS-3. The proposition is therefore DERIVED from
            syntax, not asserted.
      ⇒ this closes the inline form json.loads(open(p,"rb").read()) at (a)
        before any of the rest is reached, and v2's A-T9 fixture 5
        (claim2 = json.loads(open(claim_path).read())["controller_pid"])
        at (a), at PA-7, and at S-25d, three times over.
```

### §2.4 The path-constructor table — closed by shape, not by enumeration of the peer's records

This packet owns the claim's path and no other. It must not enumerate the peer
layer's durable record set, which is peer-contract-owned and outside this
mandate. The table is therefore closed by **shape** — one named row, and one
named residual class governed only by `PA-2`/`PA-3`:

| # | Constructor | Root prefix | Stem | Binds to | Governed by |
|---|---|---|---|---|---|
| `PC-1` | `_claim_path(process_id)` = `MS-1` | the single pinned Constant containing `T_PROCESS_CLAIMS` (`PA-1`) | `process_id`, 64 lowercase hex, checked at the constructor's first statement (`PA-3`) | `claim_path`, exactly one Name, three positions (`PA-4`) | `PA-1`..`PA-4`, `PA-7`, `MS-1` |
| `PC-N` | every other path constructor in the five roots — the spawn-intent record, the supervisor identity record, the freeze observation, the lease, the ledger, the head, the state, the journal, checkpoints, manifests, and every other peer-owned durable path | a Constant that, by `PA-1`, does **not** contain `T_PROCESS_CLAIMS` | its own grammar-checked stem (`PA-3`) | its own path Name | `PA-2`, `PA-3`, `PA-5`, `PA-6`, `PA-7`'s second sentence — **and nothing else** |

```text
PC-R1  PC-N IS NOT ENUMERATED BY THIS PACKET AND IS NOT RESTRICTED BY IT. The
       peer layer keeps every durable path it has and may add more. What PC-N
       rows must satisfy is a SPELLING and SHAPE discipline (constants plus
       grammar-checked stems; a plain-Name read operand; no general-purpose
       read helper), not a permission list. ONLY CLAIM PATHS ARE RESTRICTED.
PC-R2  RETAINED PEER-ROOT open() IS RECONCILED, NOT WITHDRAWN. S-25i-N1's
       decision stands verbatim: the builtin open is NOT added to
       generic_harness.py's forbidden set. §P1-13.7's peer-layer install and
       read sites — spawn-intent, supervisor identity, freeze observation — and
       every other peer durable record continue to be opened with open() and
       parsed with json.loads exactly as the peer contract signs them. What
       changes for them is only HOW THE PATH IS SPELLED and THAT THE READ'S
       PATH OPERAND IS A PLAIN NAME. No peer read site is removed, relocated,
       or made to pass through MS-2.
PC-R3  THE COST IS REAL AND IS PRICED. PA-2/PA-3/PA-5/PA-7 constrain path
       construction across the whole peer root, not only the claim. That is
       wider than the two identity fields need. It is the price of deciding
       "can this expression denote the claims path?" syntactically, it follows
       the framers' own S-13 precedent, and it is counted as blast-radius item
       B-A4(iii) at §6.2 rather than hidden inside a claim-only rule.
```

### §2.5 `PT-1` — the closure theorem, as a four-case syntactic analysis

```text
PT-1  CLAIM-PATH DENOTATION IS SYNTACTICALLY DECIDED.
      CLAIM: in the five production roots, the ONLY expression that can denote
      a path under successor/officina/runtime/T_PROCESS_CLAIMS/ is the Name
      claim_path, and the only read of it is MS-2's.

      PROOF, by exhaustion over the syntactic forms a path operand may take
      under PA-5 (it is a plain Name) and PA-2 (its binding, if any, is a path
      constructor call):

      case 1  The Name is claim_path. Then by PA-4 it occurs only at MS-2's
              read, MS-12's write, and the MS-11 load that IS MS-2 then MS-3.
              CLOSED by position.
      case 2  The Name is bound by a PC-N constructor. By PA-1 that
              constructor's root Constant does not contain "T_PROCESS_CLAIMS";
              by PA-2 its only other operands are Constants and its own stem;
              by PA-3 the stem contains no "/", "\\", ".." or leading "."
              — so no PC-N result is a path under the claims root, and none
              traverses into it. CLOSED by spelling.
      case 3  The Name is bound by something that is not a path constructor —
              a parameter, a Subscript, an os.environ read, a literal, a call
              result. By PA-7's second sentence such a read call is a static
              violation outright. CLOSED by absence.
      case 4  The operand is not a plain Name at all — a concatenation, an
              f-string, an inline Call, a Subscript. By PA-5 it is a static
              violation, and by PA-1 it could not have spelled the claims root
              anyway. CLOSED twice.

      COROLLARY 1 (what the X line required). Every byte string that is the
      canonical serialization of a durable claim or occupant is produced by
      MS-2's read, and by PA-8 binds immediately and only to a carrier Name.
      CR-1's class "however obtained" therefore has, in the five roots, exactly
      the three inhabitants CR-2 names — which is what S-25k already assumed
      and what v2.1 did not establish.
      COROLLARY 2. M-R4 becomes DECIDABLY sound. Its premise is no longer
      D-8's false "each durable artifact has exactly one open site" but PT-1's
      "the claim has exactly one read site, and its bytes bind only to
      carriers." The four enumerated producers MS-3, MS-4, MS-5, MS-11 are then
      genuinely the only expressions in the five roots that yield a claim or
      lease mapping.
      COROLLARY 3. list(m.values())[5] on a laundered fresh mapping is
      UNREACHABLE: m cannot exist, because its json.loads either has a
      non-Name operand (PA-9(a)), or a carrier operand outside MS-3
      (PA-9(b)/CR-3), or an operand produced by a read that PT-1 forbids.

D-8′  REPLACES v2.1 §2.7 D-8. M-R4's closure is decidable because the producer
      set is four enumerated call sites AND, by PT-1, the durable-read route to
      a claim mapping is MS-2 -> MS-3 with both sites enumerated and the path
      pinned. THE APPEAL TO §P1-13.7's "exactly one open site" IS WITHDRAWN:
      §P1-13.7 pins INSTALL sites and three NAMED reads, and pins no peer-layer
      claim read (G-1..G-3), and MS-2 itself has two call sites (G-6). NC-2 of
      v2 §2.6.5 relied on §P1-13.7 for the SPAWNING_GROUP.json name collision,
      which is an INSTALL-site property and is UNAFFECTED by this withdrawal;
      NC-1..NC-3 stand as written.
```

### §2.6 Decidability, priced honestly

```text
D-10  PA-1 is a SUBSTRING TEST over Constant node values. Nothing else.
D-11  PA-2, PA-5, PA-6, PA-8 and PA-9(a) are NODE-SHAPE MATCHES at enumerated
      node kinds. Nothing else.
D-12  PA-3 is a node-shape match on a function's first statement and its
      parameter count. Nothing else.
D-13  PA-4 and PA-7's first sentence are OCCURRENCE COUNTS and POSITION
      MATCHES over exactly one Name and one function. Nothing else.
D-14  PA-7's second sentence is the ONE new analysis kind in v2.2: an
      INTRA-FUNCTION SINGLE-ASSIGNMENT LOOKUP. At a read call, take the path
      operand Name, find its unique Assign in the SAME function body (unique by
      S-4, composite :2573), and check that the RHS is a Call to a path
      constructor. This is a local index over one function's own statements.
      IT IS NOT interprocedural, NOT a call graph, NOT a fixpoint, NOT a taint
      analysis, and it terminates in one pass. It is nevertheless MORE than the
      pure name/position matching of S-25a..S-25m, and it is disclosed here
      as such rather than described as "the same discipline".
D-15  THE WHOLE OF S-25a..S-25o REMAINS A SINGLE AST WALK OVER THE FIVE ROOTS,
      with one per-function assignment index built during that walk. This is
      the property X M-2 demanded, and v2.2 spends exactly the increment named
      at D-14 and nothing more.
```

### §2.7 The counterexample fixtures, one-to-one

**The X line's exact construct**, and every variant the mandate names, each with
the rule that fires and the mechanical reason. This catalogue is **illustrative
and normatively redundant**: every entry is rejected by **absence from an
enumerated position**, not by presence in a prohibition list.

```text
THE EXACT X-LINE COUNTEREXAMPLE (opus…v2_1_final_confirmation.md, determination 2)

  p      = "successor/officina/runtime/T_PROCESS_CLAIMS/" + process_id + ".json"
  raw    = open(p, "rb").read()
  m      = json.loads(raw)
  vals   = list(m.values())
  leaked = vals[5]
  <peer capacity / custody / selection / Q-C / scientific expr>(leaked)

  FIRES, INDEPENDENTLY, FIVE TIMES:
    line 1  PA-1  second occurrence of a Constant containing T_PROCESS_CLAIMS
    line 1  PA-2  path-building BinOp outside a path constructor, with a
                  non-Constant, non-stem operand (process_id)
    line 2  PA-5  the read call's path operand is a Name with no
                  path-constructor Assign in the enclosing body (PA-7)
    line 2  PA-8  is not reached — the read is already illegal — but would
                  also fail, since raw is not a carrier Name (CR-2)
    line 3  PA-9(a) json.loads operand is the Name raw, which is not a carrier,
                  and by PT-1 no such Name can hold claim bytes; if raw WERE a
                  carrier this is CR-3/PA-9(b), json.loads off MS-3
  AND THE ORIGINAL SINK IS NEVER REACHED. Lines 4-5 need no rule: m cannot
  exist (PT-1 corollary 3).
```

| # | Variant | Rule(s) that fire | Mechanically |
|---|---|---|---|
| V-a | `os.open(p, os.O_RDONLY)` then `os.read(fd, n)` | `PA-1`, `PA-2`, `PA-5`/`PA-7`, `PA-6` | `os.open`/`os.read` are enumerated read forms; the path operand fails the plain-Name-with-constructor-binding test identically to builtin `open` |
| V-b | `pathlib.Path("successor/officina/runtime/T_PROCESS_CLAIMS")/f"{process_id}.json"` then `.read_bytes()` | `PA-1`, `PA-2`, `PA-6` | the `Path(...)` call and the `/` operator are both path-building expressions outside a constructor; the f-string operand is neither a Constant nor a stem |
| V-c | `raw = mmap.mmap(fd, 0)` over a claims descriptor | `PA-6` + `G-9` | `mmap` is enumerated as a read form **and** is unimportable under both allowlists; the descriptor's `os.open` already failed |
| V-d | **alias** — `q = claim_path; raw = open(q, "rb").read()` | `PA-4` | `claim_path` in an `Assign` RHS is a fourth position; only (a) `MS-2`'s read, (b) `MS-12`'s write, (c) the `MS-11` load exist |
| V-e | **second construction** — `p = _claim_path(process_id)` at a new site | `PA-4` | `MS-1` is called at exactly one site and binds exactly one Name |
| V-f | **helper return** — `def _get(p): return open(p,"rb").read()` … `raw = _get(claim_path)` | `PA-7` twice | the helper's read operand is an unbound parameter Name (no general-purpose read helper); and `_get(claim_path)` is a fourth position for `claim_path` |
| V-g | **helper return, laundered further** — `def _load(p): return json.loads(open(p,"rb").read())` | `PA-7`, `PA-9(a)` | same as V-f, plus a `json.loads` whose operand is a `Call` |
| V-h | **split literal** — `ROOT = "successor/officina/runtime/"; SUB = "T_PROCESS_CLAIMS/"` | `PA-1` | `SUB`'s Constant value contains the substring; the pin is a substring test, not an equality test |
| V-i | **split across a boundary** — `ROOT = "successor/officina/runtime/"; p = ROOT + "T_PROCESS_" + "CLAIMS/" + process_id` | `PA-1` after constant folding of adjacent Constants, **and** `PA-2` | folding is over `Constant` operands only — decidable, no flow; and the expression is path-building outside a constructor regardless |
| V-j | **stem traversal** — `_lease_path("../T_PROCESS_CLAIMS/" + process_id + ".json")` | `PA-3`, `PA-1`, `PA-2` | the stem grammar refuses `/`, `..` and a leading `.` at the constructor's first statement; the literal pin fires anyway |
| V-k | **environment or config path** — `p = os.environ["CLAIMS_DIR"] + …`, or a path read from a config record | `PA-2`, `PA-5`, `PA-7` | a `Subscript` is not a permitted path-building operand; the read operand is not a constructor-bound Name |
| V-l | **relative redirect** — `os.chdir(claims_dir)` then `open(process_id + ".json")` | `PA-6`, `PA-2` | `os.chdir` appears in no production root; the operand is a concatenation |
| V-m | **symlink indirection** — plant a link, then `open(other_path)` | `PA-6` | `os.symlink`, `os.link` and `os.readlink` appear in no production root; no read passes `follow_symlinks`; and `PA-1` still binds the only claims-root spelling. **Disclosed residual:** a symlink planted by an actor OUTSIDE the five roots is not a static property and is not claimed to be closed here — see §9 item 3 |
| V-n | **exception payload** — `try: raw = open(claim_path,"rb").read() except OSError as e: leaked = e.characters_written` or a re-raise carrying the bytes | `PA-8` | inside `MS-2` no exception payload, no `try` body binding or formatting the bytes, and no second return shape; outside `MS-2` the read is already illegal by `PA-7` |
| V-o | **container capture** — `bufs = []; bufs.append(open(claim_path,"rb").read())` | `PA-8`, `PA-7` | the read value must be the RHS of one `Assign` to a carrier Name; a container element is not a carrier position |
| V-p | **directory enumeration** — `for f in os.listdir(claims_dir): …` | `PA-6`, `PA-1`, `PA-2` | `os.listdir`/`os.scandir`/`os.walk`/`.iterdir`/`.glob` are enumerated read forms with the same operand discipline; and the directory path cannot be spelled |
| V-q | **archive re-read** — open the archived copy of the claim instead of the live path | `PA-1`, `PA-2`, `PA-5`, `PA-7` | archival is path-based over "that process claim and final record" (`protocol :85-97`); any archived-claim path is still a path-building expression, and any spelling of it that reaches the claims root fires `PA-1` |

**Retained-behaviour fixtures, asserted to PASS** — so that the repair is
demonstrated not to withdraw the peer layer's signed I/O:

```text
R-a  the spawn-intent record: p = _spawn_intent_path(); raw = open(p,"rb").read();
     m = json.loads(raw)                                      PASSES
R-b  the supervisor identity record, read at the watchdog role entry PASSES
R-c  the freeze observation install and read                        PASSES
R-d  any other PC-N peer durable record built from a Constant root and a
     grammar-checked stem, read through a plain-Name operand         PASSES
     — in every case because PA-1 does not fire (no claims-root substring),
       PA-2/PA-3 are satisfied by construction, and PA-7's second sentence is
       satisfied by the in-body constructor Assign. ONLY CLAIM PATHS ARE
       RESTRICTED (PC-R1).
```

### §2.8 What Repair A preserves exactly

```text
PA-P1  S-25i and S-25i-N1..N4 are UNCHANGED IN TEXT. The builtin open stays
       available in generic_harness.py. The fix is a SITE PIN, not a BAN.
PA-P2  M-R1, M-R2, M-R3, M-R5, S-25j and its scope note are UNCHANGED. Ordinary
       peer-layer mappings remain entirely unaffected and .values(), .items()
       and ** remain available on them.
PA-P3  CR-1..CR-4 and S-25k are UNCHANGED. PT-1 corollary 1 SUPPLIES the
       premise S-25k needed rather than altering the rule.
PA-P4  MS-4..MS-12 and MS-R1..MS-R4 are UNCHANGED. MS-1, MS-2 and MS-3 keep
       their v2.1 row text; PA-1..PA-9 constrain the PATH and the READ around
       them and change no operand, result or count in the table.
PA-P5  D-5, D-6, D-7 and D-9 are UNCHANGED. D-8 alone is replaced, by D-8′.
       The count of twelve approved call sites is UNCHANGED.
PA-P6  v2's A-T9 fixture text is UNCHANGED, including fixture 5. Its assertion
       is amended at A-T9′ (§7) to require that S-25d AND S-25n both fire, so
       the fixture is not silently reclassified from an accessor violation into
       a path violation.
PA-P7  NC-1..NC-3 (the SPAWNING_GROUP.json name collision) are UNCHANGED and
       are unaffected by D-8′, because NC-2 rests on §P1-13.7's INSTALL-site
       property, which D-8′ does not disturb.
```

---

## §3. Repair B — `ACC-5` has two authorized evaluations, not one

The Y line is right, and its point is not a wording quibble: v2.1 asserted a
one-digest world in `C-5`/`DC-1`/`DC-6` while its own `§3.2` paragraph and
`S-25m`'s "exactly two `ACC-5` call sites" described a two-digest world. A
specification that contradicts itself about how many digests exist cannot be the
basis of a closure claim about where digests go. **The operation is not
changed. The count and the classification are.**

### §3.1 The two evaluations, named

```text
EV-1  THE LINEAGE EVALUATION.
      OPERAND: the canonical byte string MS-6 (ACC-4) produces for the claim
        BEING INSTALLED, over a mapping that has passed complete canonical
        validation at MS-10 — the exact twenty-key set of :231-238, exact
        types, strict int, recursive scientific-field rejection, the
        process_id recomputation from its signed preimage (:296-299),
        scientific_outcome the literal false, and the §2.2 cross-field
        invariant on its identity keys.
      SITE: MS-7 (ACC-5), lineage call site.
      RESULT: the RAW LINEAGE DIGEST, 64 lowercase hex.
      DIRECT PERSISTENT DESTINATIONS: EXACTLY TWO, D-1 and D-2, and no third.
      LIFETIME: persistent, by signature.

EV-2  THE OCCUPANT EVALUATION.
      OPERAND: the canonical byte string MS-6 (ACC-4) produces for the EEXIST
        OCCUPANT, over occupant_mapping, AFTER that occupant has INDEPENDENTLY
        passed MS-10 validation at X-2 and the cross-field conjunct X-3. The
        occupant is validated on its own bytes; it does not inherit the
        installing claim's validation, and no digest is computed over an
        unvalidated occupant.
      SITE: MS-7 (ACC-5), occupant call site.
      RESULT: the TRANSIENT OCCUPANT DIGEST, 64 lowercase hex.
      CONSUMER: EXACTLY ONE — the boolean collision conjunct X-4 of v2 §2.10.3,
        which compares it against EV-1's value and yields a boolean.
      LIFETIME: transient. It exists inside the X-4 comparison expression and
        does not outlive it.
      DESTINATIONS: NONE. It reaches neither D-1 nor D-2 nor any third place.

EV-R1  THESE ARE THE ONLY TWO EVALUATIONS. A third ACC-5 evaluation, at any
       site, over any operand, is a static violation by count (S-25m′).
EV-R2  ACC-5 IS STILL ONE ACCESSOR, DEFINED ONCE (ACC-R4, MS-R1). Two
       evaluations of one accessor is what the specification now says, and it
       is what v2.1's own S-25m already counted. The contradiction was between
       C-5/DC-1/DC-6 and S-25m, and it is resolved in favour of S-25m.
EV-R3  BOTH EVALUATIONS ARE PRECONDITIONED ON VALIDATION. EV-1 on MS-10 over
       claim_mapping; EV-2 on MS-10 over occupant_mapping plus X-2 and X-3.
       Neither may be invoked before its precondition returns true (DC-7).
```

### §3.2 `C-5`, restated — the replaced clauses only

`C-5`'s **PRECONDITION**, **KEYS READ INDIVIDUALLY** and **DESTINATIONS** blocks
carry forward from v2.1 §3.2 verbatim. The **OPERATION** clause and the
"one enumerated second invocation" paragraph are replaced:

```text
C-5 OPERATION, REPLACED.
    ACC-5 (MS-7) IS THE SOLE SHA-256 ACCESSOR OVER A CARRIER, AND IT HAS
    EXACTLY TWO AUTHORIZED EVALUATIONS, EV-1 AND EV-2.

    EV-1, the LINEAGE evaluation, over the complete canonical claim byte string
      produced at MS-6 for the claim being installed, yields the raw lineage
      digest process_claim_sha256 as 64 lowercase hex. THIS IS THE ONLY DIGEST
      VALUE THAT REACHES A PERSISTENT DESTINATION, and its direct persistent
      destinations are EXACTLY TWO: D-1 and D-2.
    EV-2, the OCCUPANT evaluation, over the complete canonical byte string
      produced at MS-6 for the independently validated EEXIST occupant, yields
      a TRANSIENT digest consumed ONLY by the boolean collision conjunct X-4.

    The v2.1 phrase "EXACTLY ONE SHA-256" IS WITHDRAWN as false on this
    specification's own bytes. What is exactly one is: one accessor definition
    (ACC-R4); one PERSISTENT lineage digest value (EV-1); one declassifying
    OPERATION (DC-1′). What is exactly two is: the authorized evaluations
    (EV-1, EV-2); the ACC-5 call sites (S-25m′); the direct persistent
    destinations of the lineage digest (D-1, D-2).

C-5 FORBIDDEN, AMENDED — the v2.1 list carries forward with one clause
    replaced and one added:
      REPLACED  "a second digest, a secondary digest, ..." BECOMES:
        - any digest evaluation other than EV-1 and EV-2; any truncated digest,
          keyed digest, HMAC, checksum, fingerprint, shortened form or numeric
          projection of a claim, a lease, an occupant, or of either digest
      ADDED
        - any persistence, logging, return, storage, transmission, or
          comparison of EV-2's result outside the X-4 conjunct (OD-1..OD-4)
```

### §3.3 `OD-1`..`OD-4` — confining the transient occupant digest

```text
OD-1  NO PERSISTENCE. EV-2's result is never written to any durable artifact,
      never enters D-1, D-2, or any other record, event, ledger, head, state,
      lease, journal, archive, checkpoint or manifest field, and never becomes
      a third destination.
OD-2  NO SURFACE. It is never logged, printed, formatted, f-stringed,
      diagnosed, framed, transmitted on the control channel, placed in a reply,
      or returned from any function other than ACC-5 itself.
OD-3  NO SECOND COMPARISON. It occurs in EXACTLY ONE comparison — the X-4
      conjunct — whose other operand is EV-1's value and whose result is a
      boolean. It is compared against nothing else, and no third value is
      compared against it.
OD-4  NO REBINDING. It binds to exactly one Name, assigned once inside the X-4
      evaluation scope, never rebound, never aliased, never stored in a
      container, never a dict value, never a function argument other than the
      comparison, and never outlives the conjunct.

S-25o  OCCUPANT-DIGEST CONFINEMENT, ALL FIVE PRODUCTION ROOTS.
       OD-1..OD-4 hold, as an occurrence count and position match on exactly
       one Name at exactly one site: the value returned by ACC-5 at its
       OCCUPANT call site occurs EXACTLY ONCE, as one operand of the single
       X-4 equality comparison, and in no other syntactic position whatsoever
       ⇒ "S-25o: transient occupant digest bound, persisted, surfaced, or
          compared outside the X-4 conjunct"
```

### §3.4 `L-1`..`L-5` — the permitted transitive integrity lineage, enumerated

The Y line's §4 audit is correct and its §9.4 requirement is adopted: the
"exactly two destinations" sentence is true of **direct raw-digest carriage**
and must not be read as the whole consumer graph. The permitted **transitive**
continuations are enumerated here so that no reviewer has to decide, case by
case, whether a downstream hash is a third destination:

```text
L-0   THE DISTINCTION. A DIRECT DESTINATION is a durable schema field whose
      value IS the raw lineage digest. A TRANSITIVE CONTINUATION is a durable
      object that CONTAINS a direct destination and is itself hashed, copied or
      verified as a whole. Continuations carry the digest inside a containing
      object's bytes; they never create a new field whose value is the raw
      digest. EXACTLY TWO DIRECT DESTINATIONS EXIST — D-1 and D-2 — AND THAT
      COUNT IS UNCHANGED BY L-1..L-5.

L-1   THE T_PROCESS_STARTED ENTRY HASH AND THE LEASE SEED. The complete
      T_PROCESS_STARTED entry — which carries D-1 — is hashed as a whole ledger
      /event entry, and that entry hash seeds t-active-lease.v1's
      prior_charge_event_sha256 (contract :103-106, "there being no prior charge
      event; X-R7/Y-5"). PERMITTED as integrity lineage. It is a hash OF a
      containing entry, not a second field carrying the raw digest.
L-2   THE EVENT/CHARGE HASH CHAIN. Subsequent charge events, heartbeat
      settlements and lease equality/hash checks carry only containing-entry
      hashes. PERMITTED. No PID addressing follows from them, and none of them
      is a raw-digest field.
L-3   THE FINAL-RECORD HASH AND THE STOP EVENT. The final t-process-record.v1 —
      which carries D-2 — is hashed as a whole, and T_PROCESS_STOPPED carries
      process_record_sha256 OF THAT RECORD together with the full post-state
      (contract :125-140). The invalid-close route carries the same shape
      (contract :165-173). PERMITTED as record integrity lineage.
L-4   ARCHIVE COPIES AND ARCHIVE COMPOSITES. The normal and invalid close
      archival sets stage "that process claim and final record, state, ledger,
      head" (protocol :85-97). The archived final record is a COPY of D-2; Git
      object, tree and commit hashes over the staged set are containing-object
      lineage. PERMITTED. Archive copies are not new raw-digest schema fields.
      ⇒ AND, STATED PLAINLY BECAUSE IT BEARS ON §4: the archival set stages the
        PROCESS CLAIM ITSELF, whose canonical bytes contain controller_pid and
        process_group_id in cleartext. For any reader of that archive the
        digest is not a confidentiality boundary and never was. See CS-4.
L-5   RECOVERY AND POST-CRASH VERIFICATION. Recovery re-reads retained claim,
      final-record and archive facts and compares canonical bytes, record
      hashes, ledger/head hashes and exact staged sets. It MAY consume D-2 or a
      containing hash for integrity. PERMITTED.
      NO RECOVERY RULE AUTHORIZES PID-BASED CONTROL FROM THE DIGEST, and none
      is created here.

L-R1  L-1..L-5 ARE A CLASSIFICATION, NOT A GRANT. Every one of them is already
      required by the signed chain at the cited loci. This packet neither
      creates nor constrains them; it names them so that the two-destination
      count is not mistaken for a claim about the whole graph, and so that a
      future reviewer can tell a permitted continuation from a proposed third
      destination by looking at one question: DOES THIS FIELD'S VALUE EQUAL THE
      RAW LINEAGE DIGEST? If yes it is a third destination and is forbidden. If
      no it is a continuation and is governed by whichever contract owns it.
L-R2  A THIRD DIRECT DESTINATION REMAINS FORBIDDEN. Any new schema field whose
      value is the raw lineage digest, in any record class, is a static
      violation by S-25l′ and a count violation by S-25m′, and would require
      its own bounded correction with its own X/Y round.
```

### §3.5 The amended rule texts for Repair B

```text
DC-1′  REPLACES DC-1. MODEL, SINGLE-VALUED AND HONESTLY COUNTED.
       ACC-5 is THE SOLE NAMED DECLASSIFYING OPERATION from
       RESTRICTED_PROCESS_IDENTITY and from RESTRICTED_CLAIM_CANONICAL_BYTES.
       There is exactly ONE such operation, defined at exactly one site (MS-7),
       accepting exactly one operand shape (a validated complete canonical
       carrier), with exactly TWO AUTHORIZED EVALUATIONS (EV-1, EV-2), of which
       exactly ONE — EV-1 — produces a value that reaches a persistent
       destination, and that value has exactly TWO direct destinations.
       THE v2.1 CLAUSE "and there is never a second" IS WITHDRAWN: it was false
       of evaluations and of digest values, and true only of persistent lineage
       values, which is now said in the words that mean it.
       DECLASSIFICATION HERE MEANS RELEASE FROM THE RESTRICTED FIELD CLASS AND
       NOTHING ELSE. IT IS NOT CONFIDENTIALITY DECLASSIFICATION, BECAUSE THERE
       WAS NO CONFIDENTIALITY PROPERTY TO RELEASE (CS-4, DC-3′).
       The alternative model — a restricted derived class carrying two
       destinations — remains REJECTED, for the reasons at v2.1 §3.5 and §3.6,
       which are unchanged and which both final confirmation lines accepted.

DC-6′  REPLACES DC-6. DIGEST INVENTORY, COMPLETE.
       Exactly two digest VALUES are derived from a carrier in the five roots:
         (i)  EV-1's raw lineage digest — persistent, two direct destinations;
         (ii) EV-2's transient occupant digest — no destination, one boolean
              consumer, confined by OD-1..OD-4 and S-25o.
       NO OTHER digest, checksum, fingerprint, truncated form, keyed form,
       HMAC, or numeric projection of a claim, a lease, an occupant, or of
       either digest exists in the five roots.
       THE v2.1 SENTENCE "NO SECOND DIGEST ... the only value derived from a
       carrier" IS WITHDRAWN as false. The one-way boundary does not need it
       and never rested on it: what the boundary needs is that no SECOND
       PERSISTENT LINEAGE VALUE and no THIRD DESTINATION exist, and that is
       what DC-1′, OD-1..OD-4, L-R2, S-25l′ and S-25o assert.

S-25e′  REPLACES S-25e. persistent-consumer closure: the returns of ACC-2 /
        ACC-3 are unpacked only at the C-3, C-4 and X-3 comparison sites, each
        unpacked Name occurring exactly once inside its comparison expression
        and each site yielding a boolean; the return of ACC-5 AT ITS LINEAGE
        CALL SITE (EV-1) is consumed only at the two direct destinations D-1
        and D-2; and the return of ACC-5 AT ITS OCCUPANT CALL SITE (EV-2)
        occurs exactly once, as one operand of the single X-4 equality
        conjunct, and nowhere else
        ⇒ "S-25e: restricted identity value or claim digest used outside a
           whitelisted position"

S-25l′  REPLACES S-25l. LINEAGE-DIGEST DESTINATION CLOSURE. The value returned
        by ACC-5 at its LINEAGE call site (EV-1) reaches exactly the two direct
        destinations D-1 and D-2, and no third. It appears in no addressing,
        selection, signalling, waiting, process-control, request-builder,
        handle, journal-key, retry-key, capacity, custody, spend, settlement,
        qualification, blinding, Q, C, scientific datum, evidence, outcome or
        Proof expression, and no numeric value is derived from it.
        IT MAY APPEAR IN EXACTLY THE INTEGRITY COMPARISONS THE SIGNED CHAIN
        REQUIRES — the X-4 conjunct, and the containing-object hashing and
        verification of L-1..L-5 — and in no other comparison. The v2.1
        blanket word "comparison" is REPLACED by this clause, because the
        digest's DEFINING authorized uses are comparisons and a rule that bans
        all comparison bans the operation it exists to permit (DC-4′)
        ⇒ "S-25l: claim lineage digest reaches an unauthorized destination or
           an unauthorized comparison"

S-25m′  REPLACES S-25m. COUNT CLOSURE. The five roots contain exactly five
        accessor definitions (ACC-1..ACC-5), exactly five persistent consumers
        (C-1..C-5), exactly three governed mapping Names (M-R3), exactly three
        carrier Names (CR-2), exactly twelve approved call-site rows (§2.4 of
        v2.1), exactly ONE claim-path Name and ONE claim read site (PA-4,
        PA-7), exactly TWO ACC-5 evaluations (EV-1, EV-2), exactly ONE
        persistent lineage digest value, exactly TWO direct persistent
        destinations (D-1, D-2), and exactly ONE declassifying operation.
        Each count is asserted as a number, so an addition fails by arithmetic
        rather than by review
        ⇒ "S-25m: accessor, consumer, governed-name, call-site, evaluation or
           destination count changed"

S-25n   NEW. CLAIM-PATH AND CLAIM-READ ANCHORING, ALL FIVE PRODUCTION ROOTS.
        PA-1..PA-9 hold: the claims-root literal occurs exactly once, at MS-1;
        every path-building expression occurs inside a path constructor over
        Constants and a grammar-checked stem; every enumerated read call's path
        operand is a plain Name bound in its own function body by a path
        constructor; claim_path occurs in exactly its three positions; the
        claim read occurs only inside MS-2; MS-2's bytes bind immediately and
        only to a carrier Name; and json.loads/json.load take a plain-Name
        operand, with a carrier operand only at MS-3
        ⇒ "S-25n: claim path or claim read outside its anchored site"
```

---

## §4. Repair C — narrowing the cryptographic claim honestly

The Y line's §5 is correct and this section adopts it without reservation.
`WL-3` already disclosed the 4,194,304-candidate search; the surrounding rules
then denied the channel that disclosure creates. **A packet may not disclose a
residual in one paragraph and assert its absence in the next.** What is
withdrawn here is a set of *cryptographic* assertions. What is preserved
verbatim is the *authorization* boundary, which never depended on them.

### §4.1 Two predicates, so every later claim is tagged

```text
IP    INFORMATIONALLY POSSIBLE. A thing an actor holding certain values can
      COMPUTE OR INFER, irrespective of any rule. IP is a fact about
      mathematics and about who holds what. No specification sentence can make
      an IP fact false, and this packet does not try.
ACU   AUTHORIZED CONFORMING USE. A thing a CONFORMING IMPLEMENTATION IN THE
      FIVE PRODUCTION ROOTS may do, and a thing Officina authorizes as a basis
      for an action, a record, a decision, a datum or a Proof. ACU is exactly
      what this contract governs, and it is enforced statically.

CS-R1 EVERY CLAIM IN DC-3′, DC-4′, DC-5′ AND WL-4′ IS TAGGED [IP] OR [ACU].
      An untagged absolute assertion about what the digest "is" or "can" do is
      precisely the defect this repair closes, and none appears below.
CS-R2 IP AND ACU ARE INDEPENDENT. Something informationally possible may be
      unauthorized (and is, here, for identity recovery). Something authorized
      is necessarily possible. The governance property this packet claims is an
      ACU property. IT WAS NEVER AN IP PROPERTY, AND v2.1 SHOULD NOT HAVE
      WRITTEN IT AS ONE.
```

### §4.2 `CS-1`..`CS-7` — the honest claim scope

```text
CS-1  WHAT THE DIGEST IS, CRYPTOGRAPHICALLY. [IP] process_claim_sha256 is a
      SEARCHABLE FULL-CLAIM COMMITMENT: a SHA-256 over the complete canonical
      serialization of the twenty-key claim. It is a commitment to every field
      jointly, and its preimage is not a generic 256-bit secret.
CS-2  THE SEARCH SPACE, STATED AS A NUMBER. [IP] Given the other EIGHTEEN
      canonical field values, the unknown is the pair
      (controller_pid, process_group_id). A-P4c forces
      attested_pgid == attested_pid for the leader case this contract
      installs, and the pinned bound is PID_MAX_LIMIT = 4194304 (v2 §2.2,
      X m-2). THE CANDIDATE SPACE IS THEREFORE AT MOST 4,194,304 SINGLE
      VALUES, and exhaustive enumeration against the digest is practical on
      ordinary hardware. This packet RESTS NO CLAIM ON PREIMAGE RESISTANCE.
CS-3  WHO HOLDS THE OTHER EIGHTEEN FIELDS. [IP] The supervisor CONSTRUCTING the
      claim already possesses or determines all eighteen — the activation
      record hash, process id and sequence, start identity, argv, source,
      config, stack and numerical-mode hashes, device identity and units,
      timestamps and clock kind, boot identity, start reading, and the
      immutable-control hash. IT NEED NOT REOPEN THE CLAIM TO KNOW THEM.
      v2.1 WL-4(a)'s premise — "the eighteen other canonical values are
      obtainable only by reading the claim" — IS WITHDRAWN AS FALSE.
CS-4  THE DIGEST IS NOT A CONFIDENTIALITY BOUNDARY. [IP] For an actor who can
      read the claim or its archive, the two integers are present IN CLEARTEXT
      (protocol :231-238; the archival sets stage the claim itself,
      protocol :85-97, L-4). For an actor who holds the other eighteen fields
      but not the claim, CS-2's search recovers them. THERE IS NO READER FOR
      WHOM THE DIGEST CONCEALS THE IDENTITY FIELDS, and the packet does not
      claim one.
CS-5  CONDITIONAL INFORMATIONAL IDENTITY AND EQUALITY EVIDENCE. [IP] A matching
      candidate digest can stand as evidence that a candidate PID/PGID belongs
      to the committed claim, and digest equality is evidence that two byte
      strings are the same claim. The digest therefore MAY PROVIDE CONDITIONAL
      INFORMATIONAL IDENTITY AND EQUALITY EVIDENCE. v2.1's "never process
      identity" and "never evidence/comparison" ARE WITHDRAWN as absolute
      claims.
CS-6  THE AUTHORIZATION BOUNDARY, PRESERVED IN FULL. [ACU] Within the
      conforming five-root implementation and the signed downstream contracts,
      the digest is authorized ONLY for record integrity and lineage —
      canonical equality, event and record hash chaining, archive verification,
      and recovery verification (L-1..L-5, X-1, X-4). IT CONFERS NO
      PROCESS-CONTROL AUTHORITY AND IS NOT AN AUTHORIZED PID SELECTOR.
CS-7  THE HONEST SCOPE SENTENCE, ADOPTED FROM THE Y LINE'S §5 AND BINDING HERE:
        Within the conforming five-root implementation and signed downstream
        contracts, the digest is authorized only for record integrity and
        lineage, including canonical equality, event/record hash chaining,
        archive verification, and recovery verification. It confers no
        process-control authority and is not an authorized PID selector. It is
        not confidentiality-preserving and may serve as an inferential identity
        commitment to a reader who knows the other canonical fields.
      THIS SENTENCE GOVERNS WHEREVER v2 OR v2.1 SAYS SOMETHING STRONGER.
```

### §4.3 The replaced classification rules

```text
DC-3′  REPLACES DC-3. WHAT IT IS.
       [ACU] An AUTHORIZED INTEGRITY AND LINEAGE IDENTIFIER of a validated
       durable record. In a conforming implementation it is not used as process
       identity, not as process authority, not as a handle, not as a selector,
       and not as a name of anything addressable; no route in the five roots
       may so use it, and S-25l′ rejects each such use statically.
       [IP] It is ALSO a searchable full-claim commitment (CS-1) whose
       identity-field search space is at most 4,194,304 (CS-2), which may
       supply conditional informational identity and equality evidence (CS-5),
       and which IS NOT A CONFIDENTIALITY BOUNDARY (CS-4).
       WITHDRAWN, EXPLICITLY: "It is never process identity, never process
       authority, never a handle, never a selector, and never a name of
       anything addressable" as an UNQUALIFIED assertion. It is true of
       AUTHORIZED CONFORMING USE and false of INFORMATIONAL POSSIBILITY, and
       v2.1 stated it without the distinction.

DC-4′  REPLACES DC-4. WHAT IT MAY NEVER FEED.
       [ACU] THE NORMATIVE PROHIBITION IS PRESERVED IN FULL AND IS NOT
       NARROWED. Neither the digest, NOR ANY VALUE RECOVERED OR INFERRED FROM
       IT (class member (f) of v2.1 §3.3), may enter, at any distance and
       through any number of intermediate bindings: addressing or selection of
       any kind; signalling; waiting; any process-control primitive; any
       request builder for the nine opcodes; a handle-table key or a handle
       comparison; a journal key or a retry key; capacity observation; custody
       disposition; spend or settlement input; qualification or blinding; a Q
       or C input; a scientific datum, observation, evidence, outcome, or
       Proof. Its only DIRECT DESTINATIONS are D-1 and D-2.
       [ACU] AMENDED, COMPARISON. The digest MAY be compared — that is what it
       is for. Its authorized comparisons are exactly: the X-4 conjunct; and
       the containing-object hashing, equality and verification of L-1..L-5.
       Any other comparison is forbidden. The v2.1 blanket ban on "comparison"
       and on "evidence" IS WITHDRAWN as self-contradictory: X-4 IS a digest
       comparison used as integrity evidence, and the packet requires it.
       WHAT REMAINS BANNED IS SCIENTIFIC EVIDENCE, Q/C EVIDENCE, AND EVIDENCE
       OFFERED AS A BASIS FOR PROCESS CONTROL OR SELECTION.
       [IP] Nothing in DC-4′ asserts that an actor CANNOT compute an equality
       or an inference. It asserts that no conforming implementation may
       perform one outside the enumerated sites, and that Officina authorizes
       no decision, record, datum or Proof that rests on one.

DC-5′  REPLACES DC-5. ONE-WAY, NARROWED TO WHAT IS TRUE.
       [ACU] No route in the five production roots may invert, search,
       enumerate against, or otherwise attempt to recover a claim field from a
       digest. Constructing a candidate claim in order to compare digests
       requires binding a candidate identity integer, which is an S-25c
       occurrence violation or an M-R4/S-25j producer violation BEFORE any hash
       expression is parsed (WL-2, unchanged), so the attempt fails STATICALLY
       at its first line rather than at the hash.
       [IP] THIS DOES NOT MAKE INVERSION INFEASIBLE. An actor OUTSIDE the five
       roots, holding the digest and the other eighteen canonical fields, can
       recover the identity pair by CS-2's enumeration, and no rule in this
       packet or any other prevents that. THE WORD "ONE-WAY" IS WITHDRAWN AS A
       CRYPTOGRAPHIC CLAIM and retained only as the name of the ACU property:
       no conforming route runs the inversion.
       [ACU] AND, UNCHANGED: the moment such a recovered value is bound inside
       the five roots it is class member (f), and every rule of §2.5 and §2.6
       applies to it — so the recovery buys no conforming use even where it is
       informationally possible.
```

### §4.4 The replaced laundering analysis

```text
WL-1   UNCHANGED. No field-level route exists through ACC-4/ACC-5; ACC-R5 is a
       node-type match checked by S-25k. [ACU]
WL-2   UNCHANGED. The inverse route fails earlier than the hash, statically.
       [ACU]

WL-3′  REPLACES WL-3. THE RESIDUAL, STATED AS A PROPERTY RATHER THAN A CAVEAT.
       [IP] SHA-256 is not a confidentiality barrier for a low-entropy unknown.
       Given the other eighteen canonical values, the identity pair is
       recoverable by enumeration over at most 4,194,304 candidates (CS-2), and
       the actor who constructs the claim already holds those eighteen values
       (CS-3), and the actor who reads the archive holds the integers outright
       (CS-4). THE DIGEST HAS NO CONFIDENTIALITY PROPERTY. This packet rests no
       claim on preimage resistance, and no sentence in v2, v2.1 or v2.2 may be
       read as asserting one.

WL-4′  REPLACES WL-4. WHY THE RESIDUAL IS NOT A CAPABILITY OR AUTHORIZATION
       TRANSFER — restated as an ACU argument, which is the only kind that
       survives.
       (a) WITHDRAWN AND REPLACED. v2.1's "the eighteen other canonical values
           are obtainable only by reading the claim" is FALSE (CS-3): the
           constructing supervisor holds them without reading anything, and the
           archive reader holds the integers themselves. THE CORRECT
           STATEMENT IS: the digest adds NO CONFIDENTIALITY, and the packet's
           boundary was never a confidentiality boundary. What the five-root
           rules close is the CONFORMING ROUTE, not the arithmetic.
       (b) UNCHANGED AND STILL TRUE. [IP]+[ACU] Under A3 the supervisor is
           same-UID with every process in this contract and may already read
           every pid on the system from /proc unilaterally (v2 §5.6; composite
           :1942 "stop, kill, or delay any same-UID process"; :1952 "Kernel
           power is admitted; Officina authorization is not conferred").
           Recovering a pid from a digest therefore conveys ZERO operating-
           system capability the actor did not already have.
       (c) UNCHANGED AND STILL TRUE. [ACU] A recovered value confers no
           AUTHORIZED addressing: no request field of any of the nine opcodes
           accepts a pid (composite :1240; A-R1..A-R8), and the moment such a
           value is bound in the five roots it is class member (f), so every
           sink rule applies to it unchanged.
       (d) REPLACED CONCLUSION. The digest transfers NO CAPABILITY and NO
           AUTHORIZATION. It DOES carry conditional information about the
           identity fields to a reader who holds the other eighteen (CS-5), and
           that information was already available to every such reader by (b)
           and by CS-4. WHAT C-5 ADDS TO THE WORLD IS A LINEAGE IDENTIFIER, NOT
           A SECRET AND NOT A POWER. That is a narrower claim than v2.1 made,
           and it is the claim this packet actually needs.

WL-R1  THE GOVERNANCE PROPERTY, RESTATED IN ONE SENTENCE SO IT CANNOT BE
       OVERREAD. [ACU] No Officina act, record, decision, datum, outcome,
       Proof, spend, settlement, custody disposition, capacity fact,
       qualification or comparison may rest on the digest except as record
       integrity and lineage at the enumerated sites — and that is enforced
       statically by S-25l′, S-25o and P-R5's dominant invalidity, not by an
       assumption about what an actor can compute.
```

### §4.5 What Repair C explicitly does **not** weaken

```text
CS-P1  DC-2 (declassified is not unconstrained) is UNCHANGED.
CS-P2  DC-7 (deviation is dominant invalidity) is UNCHANGED.
CS-P3  P-R4's sink list and P-R5's invalidity dominance are UNCHANGED.
CS-P4  S-25f and S-25g are UNCHANGED. S-25l is amended only in the two clauses
       named at S-25l′.
CS-P5  Class member (f) of v2.1 §3.3 is UNCHANGED and is now load-bearing: it
       is what makes CS-5's informational possibility yield no conforming use.
CS-P6  N-3 of v2.1 §8.2 stands: observing a PID confers no authorized process
       control, and C-5 confers none either. Repair C narrows a CRYPTOGRAPHIC
       claim; it narrows NO AUTHORIZATION claim, and the authorization boundary
       is strictly the same set of prohibitions it was in v2.1.
CS-P7  §3.5's model choice and §3.6's destination search are UNCHANGED, and
       both final confirmation lines independently confirmed them.
```

---

## §5. Amended counts, blast radius, and handoff

### §5.1 Consumer, accessor, rule and count table

| Quantity | v2 | v2.1 | **v2.2** |
|---|---|---|---|
| persistent consumers | 4 — `C-1`..`C-4` | 5 — `C-1`..`C-5` | **5 — `C-1`..`C-5`** (unchanged) |
| centralized accessors | 3 — `ACC-1`..`ACC-3` | 5 — `ACC-1`..`ACC-5` | **5 — `ACC-1`..`ACC-5`** (unchanged) |
| verifier rules added by Option A | 8 — `S-25a`..`S-25h` | 13 — `S-25a`..`S-25m` | **15 — `S-25a`..`S-25o`** |
| behavioural tests added by Option A | 12 — `A-T1`..`A-T12` | 17 — `A-T1`..`A-T17` | **21 — `A-T1`..`A-T21`** |
| governed mapping Names | not pinned | 3 (`M-R3`) | **3** (unchanged) |
| carrier Names | not pinned | 3 (`CR-2`) | **3** (unchanged) |
| approved call sites | not tabulated | 12 (`MS-1`..`MS-12`) | **12** (unchanged) |
| claim-path Names | not pinned | not pinned | **1** (`claim_path`, `PA-4`) |
| claim-path construction sites | not pinned | not pinned | **1** (`MS-1`, `PA-1`/`PA-4`) |
| claim read sites | not pinned | not pinned | **1 function** (`MS-2`, `PA-7`); called at 2 sites (`MS-2` verify, `MS-11` occupant) |
| path-constructor rows | — | — | **1 named (`PC-1`) + 1 residual class (`PC-N`), shape-closed** |
| `ACC-5` accessor definitions | — | 1 | **1** (unchanged) |
| `ACC-5` authorized evaluations | — | "exactly one SHA-256" **(contradicted)** | **2 — `EV-1`, `EV-2`** |
| persistent lineage digest values | — | 1 (implied) | **1 — `EV-1` only** |
| transient digest values | — | unnamed | **1 — `EV-2`, no destination** |
| direct persistent destinations | — | 2 — `D-1`, `D-2` | **2 — `D-1`, `D-2`** (unchanged) |
| enumerated transitive continuations | — | not enumerated | **5 — `L-1`..`L-5`** |
| declassifying operations | 0, asserted | "exactly 1" | **1 operation, 2 evaluations, 1 persistent value** |

### §5.2 Amendments to the blast radius

```text
B-A1′  §5.4 "verifier: S-25a-S-25m (thirteen rules)"
         BECOMES  S-25a-S-25o (FIFTEEN rules, up from four)
B-A2′  §5.4 / §5.5 "tests: A-T1-A-T17 (seventeen)"
         BECOMES  A-T1-A-T21 (TWENTY-ONE)
B-A3′  §5.4 supervisor code line ADDS: one claims-path construction site, one
       claim read function, one claim-path Name, and a path-spelling discipline
       over every path constructor in the five roots
B-A4   §5.5 blast radius, Option A — v2.1's items (i) and (ii) are UNCHANGED
       and item (iii) is ADDED:
       (iii) A PATH-SPELLING AND READ-OPERAND DISCIPLINE OVER EVERY PATH
             CONSTRUCTOR AND EVERY READ CALL IN THE FIVE ROOTS (PA-2, PA-3,
             PA-5, PA-7). This is wider than the claim: every peer durable path
             must be built from Constants plus a grammar-checked stem, every
             read's path operand must be a plain Name bound in its own function
             body by a path constructor, and no general-purpose read helper may
             exist. NO PEER READ SITE IS REMOVED OR RELOCATED and the builtin
             open is retained (PC-R2), but existing peer code that builds paths
             ad hoc or funnels reads through a shared helper MUST BE RESHAPED.
             It follows the framers' own S-13 precedent (composite :2603). It
             is disclosed here and counted as one item, not folded into (i).
B-A5′  §5.8 "new residual", Option A — v2.1's item is REPLACED:
         WAS  "the claim's canonical digest is a one-way lineage identifier
               whose preimage space ... is small enough to enumerate ... It
               transfers no capability and no authorization (WL-4)"
         IS   the claim's canonical digest is a SEARCHABLE FULL-CLAIM
              COMMITMENT. It is NOT A CONFIDENTIALITY BOUNDARY: given the other
              eighteen canonical fields the identity pair is recoverable by
              enumeration over at most 4,194,304 candidates, the constructing
              supervisor already holds those fields, and the archive reader
              holds the integers in cleartext. It may supply conditional
              informational identity and equality evidence. It transfers NO
              capability and NO authorization (WL-4′, CS-6), and NO Officina
              act may rest on it outside record integrity and lineage (WL-R1).
B-A6   UNCHANGED, AND NOT RE-PRICED: signed sentences amended (1); peer-owned
       durable record schemas superseded (0 for A, 2 for B); new durable schemas
       (0 for A); signed validity predicates reopened (0 for A); architectural
       rules inverted (0 for A); wire grammar changed (1 response grammar, no
       request grammar); durable formats changed (1 — P1's own J4);
       collision/idempotency rules changed (1 — EEXIST X-1..X-4); migration
       (none); SELECTABLE TODAY: A yes, B NO.
B-A7   OPTION B'S CORRECTED COUNT IS UNTOUCHED BY THIS CORRECTION: two record
       schemas superseded, one new schema created, one signed acceptance
       predicate reopened, one architectural rule inverted, one PCS write-
       surface property expanded. B remains NON-SELECTABLE behind sub-cells
       B-1 and B-2, for authority reasons and not size reasons.
```

### §5.3 Amendments to the v1.3 handoff

```text
STEP 5 AMENDED AGAIN. "...adds A-R1...A-R8 to §P1-12 as a closed rule set, and
  RESTRICTED_PROCESS_IDENTITY with C-1..C-5, P-R1..P-R5, ACC-1..ACC-5,
  ACC-R1..ACC-R5, NC-1..NC-3, RESTRICTED_CLAIM_CANONICAL_BYTES with CR-1..CR-4,
  M-R1..M-R5, the MS-1..MS-12 approved call-site table, DC-1′..DC-7, and — new
  in v2.2 — the path-anchoring rules PA-1..PA-9 with the PC-1/PC-N constructor
  table and the PT-1 closure, the two ACC-5 evaluations EV-1/EV-2 with
  OD-1..OD-4 and the transitive-lineage enumeration L-1..L-5, and the claim
  scope CS-1..CS-7 with the IP/ACU distinction, as a new subsection of §P1-13."
STEP 6 AMENDED AGAIN. "...adds S-25a...S-25o to §P1-14.6 CHANGE 3 and updates
  the edit surface from S-1...S-24b to S-1...S-25o."
STEP 7 AMENDED AGAIN. "...adds A-T1...A-T21 as test rows 92-112."
STEP 11 UNCHANGED from v2.1.
STEP 12 NEW. "...records that D-8's appeal to §P1-13.7's 'exactly one open
  site' is WITHDRAWN and replaced by PT-1/D-8′, and that §P1-13.7's committed
  bytes are NOT edited: §P1-13.7 continues to pin INSTALL sites and its three
  named reads exactly as written, and PA-1..PA-9 supply the peer-layer claim
  READ pin as their own rule. NC-1..NC-3 continue to rest on §P1-13.7's
  install-site property and are unaffected."
STEP 13 NEW. "...records that the packet asserts NO CONFIDENTIALITY PROPERTY
  for process_claim_sha256 (CS-4, WL-3′), so that no future contract may cite
  this cell as authority for treating the digest as concealing the identity
  fields, and that CS-7's scope sentence governs wherever v2 or v2.1 says
  something stronger."
STEPS 1, 2, 3, 4, 8, 9, 10 ARE UNCHANGED.
```

---

## §6. Tests added and amended by v2.2

`A-T1`..`A-T8` and `A-T10`..`A-T17` are unchanged in text. `A-T9`'s fixture text
is unchanged and its assertion is amended:

```text
A-T9′  AMENDED ASSERTION ONLY, FIXTURE TEXT UNCHANGED. Fixture 5,
         claim2 = json.loads(open(claim_path).read())["controller_pid"]
       is asserted to be rejected statically with BOTH S-25d AND S-25n named,
       so that the fixture is not silently reclassified from an accessor
       violation into a path violation. Fixtures 1-4 are unchanged and still
       fire S-25c alone.

A-T18  NEW. THE CLAIM-REOPEN COUNTEREXAMPLE, EXACT. The X line's construct is
       included VERBATIM as a build fixture:
           p      = "successor/officina/runtime/T_PROCESS_CLAIMS/" + process_id + ".json"
           raw    = open(p, "rb").read()
           m      = json.loads(raw)
           vals   = list(m.values())
           leaked = vals[5]
       and is asserted REJECTED STATICALLY with S-25n named, at the FIRST line
       and not merely somewhere. The test additionally asserts that the build
       is rejected even if lines 3-5 are deleted, so that the closure is shown
       to be at the PATH and the READ, not at the mapping.

A-T19  NEW. THE VARIANT MATRIX. Each of V-a..V-q of §2.7 is a build fixture,
       asserted REJECTED STATICALLY with the named rule fired, INDIVIDUALLY and
       not as a group:
         V-a  os.open + os.read              V-j  stem traversal
         V-b  pathlib Path / read_bytes      V-k  environment or config path
         V-c  mmap over a claims descriptor  V-l  os.chdir relative redirect
         V-d  alias q = claim_path           V-m  symlink indirection
         V-e  second _claim_path call        V-n  exception payload
         V-f  helper return                  V-o  container capture
         V-g  helper return + json.loads     V-p  directory enumeration
         V-h  split literal                  V-q  archive re-read
         V-i  split across a boundary
       AND the retained-behaviour fixtures R-a..R-d are asserted to PASS, so
       that the test proves the peer layer's signed durable I/O survives. A
       build in which R-a..R-d fail is a TEST FAILURE, not a stricter build.

A-T20  NEW. TWO-EVALUATION CONFORMANCE.
       (a) positive: exactly two ACC-5 evaluations exist; EV-1 runs only after
           MS-10 returns true on claim_mapping and reaches exactly D-1 and D-2;
           EV-2 runs only after the occupant independently passes MS-10, X-2
           and X-3, and its value occurs exactly once, inside the X-4 equality;
       (b) negative, each rejected statically with the named rule asserted:
             a third ACC-5 evaluation at any site            S-25m′
             EV-2's value written to any durable field       S-25o / OD-1
             EV-2's value logged, formatted or returned      S-25o / OD-2
             EV-2's value compared anywhere but X-4          S-25o / OD-3
             EV-2's value aliased or stored in a container   S-25o / OD-4
             EV-1's value reaching any third destination     S-25l′
             a digest computed over an unvalidated occupant  DC-7 / EV-R3

A-T21  NEW. TRANSITIVE LINEAGE AND COUNT CLOSURE.
       (a) L-1..L-5 are asserted PERMITTED: the T_PROCESS_STARTED entry hash
           seeding the lease, the charge/event hash chain, the final-record
           hash named by T_PROCESS_STOPPED, the archive copies and archive
           composites, and recovery verification each pass;
       (b) a new schema field whose VALUE equals the raw lineage digest is
           asserted REJECTED as a third direct destination, by S-25l′ and
           S-25m′, in every record class;
       (c) the verifier asserts, as numbers: five accessor definitions, five
           persistent consumers, three governed mapping Names, three carrier
           Names, twelve approved call-site rows, ONE claim-path Name, ONE
           claims-root literal occurrence, ONE claim read function, TWO ACC-5
           evaluations, ONE persistent lineage digest value, TWO direct
           destinations, and ONE declassifying operation. Adding a sixth
           accessor, a fourth governed Name, a thirteenth call site, a second
           claims-root literal, a third evaluation or a third destination fails
           S-25m′ BY ARITHMETIC, and the test asserts that specific failure.
```

---

## §7. What v2.2 does not change

### §7.1 The eight findings both confirmation lines accepted as closed, twice

| Finding | v2 locus that must remain intact | v2.1 effect | **v2.2 effect** |
|---|---|---|---|
| `X M-1` | §2.8.1 withdrawal; §2.8.2 thirteen-key `J4` vector with `E-1`..`E-4`; §2.8.3 `R-P1`..`R-P4`; §5.1/§5.5/§7.1/§7.2 step 8 | none | **none** |
| `X m-1` | §2.3 `A-P4a`..`A-P4d`, fresh `getpgid` authoritative, stored value a mandatory non-null cross-check, `setsid` equality mandatory | none | **none** |
| `X m-2` | §2.2 `PID_MAX_LIMIT = 4194304`, `G-1`..`G-6`, the platform premise, `A-T8` | none | **none in substance.** `CS-2` cites the bound as the size of the search space; it neither changes nor reopens it |
| `X m-3` | §6.1 Case 1 / Case 2 separated by actor, trigger, citation and status | none | **none** |
| `Y-C2` | §2.8.2 durable complete representation; §2.8.3 byte-identical redelivery | none | **none** |
| `Y-M1` | §2.10.1 withdrawal; §2.10.2 boundary-keyed matrix; §2.10.3 `X-1`..`X-4`; §2.10.4 `I-1`..`I-10` | none in substance | **none in substance.** `X-4` is not removed, narrowed or renumbered; `EV-2`, `OD-1`..`OD-4` and `S-25o` describe the digest it already used. No row of the matrix, no conjunct and no routing changes |
| `Y-M2` | §3.2 withdrawal of the `t-process-record.v1` inheritance claim; the corrected count of two superseded schemas | none | **none.** `L-3`/`L-4` cite the record's hash and archive copy; the record still carries the digest and neither identity key |
| `Y-m1` | §1.5 `R-1`..`R-4` with `R-4`'s exact scope; §4 | none | **none** |

### §7.2 The v2.1 mechanism both lines confirmed sound

| v2.1 locus | Final-confirmation status | v2.2 effect |
|---|---|---|
| `S-25i`, `S-25i-N1`..`N4` | X: confirmed compatible with all five roots' allowlists; the retained builtin `open` is "the correct decision" | **none** |
| `M-R1`, `M-R2` | X: closes `claim_mapping.controller_pid` twice | **none** |
| `M-R3`, `M-R5`, `S-25j` + scope note | X: closes eight enumerated routes | **none** |
| `CR-1`..`CR-4`, `S-25k` | X: closes slicing, decode, regex, second hash, inline parse of a carrier | **none in text.** `PT-1` corollary 1 supplies the premise `CR-1`'s "however obtained" needed |
| `MS-4`..`MS-12`, `MS-R1`..`MS-R4` | X: confirmed | **none** |
| `ACC-4`, `ACC-5`, `ACC-R5` | X and Y: confirmed; `ACC-R5` "prevents the accessor bodies from extracting either identity field" | **none** |
| `ACC-R1`..`ACC-R4` | X: `ACC-1..ACC-5` complete; a sixth is a static violation | **none** |
| `C-5` as a record-level consumer | X: "fully closed"; Y: "a legitimate fifth consumer" | **none** — only the OPERATION clause's count |
| `D-1`, `D-2` as the two direct destinations | X and Y: confirmed | **none** |
| `DC-2`, `DC-7` | Y: confirmed | **none** |
| `RC-1`..`RC-4` | X: "the exemption is correctly the only one and is well-bounded" | **none** |
| §3.5 model choice, §3.6 destination search | X: verified against the composite and both peer contracts; Y: "Closed" | **none** |
| `NC-1`..`NC-3` | carried from v2 | **none** — unaffected by `D-8′` (`PA-P7`) |

### §7.3 The preserved invariants, restated

```text
N-1   The identity conflict is real and loud (v2 §1).
N-2   Option A remains an EXPLICIT BOUNDED LEXICAL WEAKENING of the signed
      "cannot express a PID" sentence, with its own token, old and new text
      side by side, and a plain statement of the cost (v2 §2.12). v2.2 does not
      soften it, does not restate it as equivalent, and GRANTS NO PROCESS-
      CONTROL AUTHORITY. The post-A property remains SYNTACTIC, not dataflow.
N-3   Observing a PID/PGID confers no authorized process control (v2 §5.6,
      A-R1..A-R8). C-5 confers none either (DC-3′, DC-4′, WL-4′, CS-6).
N-4   Both-or-neither tuple semantics (G-4), the stopped/unreaped direct-child
      proof (A-P1..A-P6), the PID-reuse binding (§2.9), fail-closed absence
      (G-5, G-6, Z1-R6), the J4/replay durability (§2.8), the crash matrix
      (§2.10.2), EEXIST convergence (§2.10.3), the pinned PID bound (§2.2), the
      fresh-PGID rule (A-P4a..d), the corrected Option B count (§3.2, §5.5) and
      the corrected /proc rationale (§1.5) ALL HOLD UNCHANGED.
N-5   Option B remains NON-SELECTABLE behind sub-cells B-1 and B-2, on
      authority grounds, unchanged by any count in this correction. Option A
      remains RECOMMENDED AND UNSELECTED.
N-6   The historical OK/CLAIM reply matrix remains NON-GOVERNING, on the
      evidence of v2.1 §3.6 as independently re-verified by both final
      confirmation lines: composite authority level 3 fixes the whole
      supervisor/control-channel chain as immutable historical and provenance
      evidence only; the v1.2 composite does not restate the matrix; and
      neither accepted peer contract (…GENERIC_HARNESS_CONTRACT_V2_3_1_
      CORRECTION.md, …BATCH_SETTLEMENT_CORE_AMENDMENT_V1_1_1_CORRECTION.md)
      contains process_claim_sha256 at all. DC-1′ continues to accommodate a
      future ruling that it is live, without amendment.
N-7   The watchdog-freeze cell AUTHOR_CELL_P1_WATCHDOG_FREEZE_MECHANISM remains
      ORTHOGONAL AND UNRESOLVED. v2.2 neither fixes nor worsens it, and P1
      remains non-operative until it is resolved even if A is selected.
N-8   T = NOT_ACTIVATED; the programme claim is OPEN.
N-9   NO SELECTION IS MADE. Neither I_SELECT_P1_PROCESS_CLAIM_IDENTITY_A_
      OBSERVATION_ONLY nor I_SELECT_P1_PROCESS_CLAIM_IDENTITY_B_OPAQUE_BINDING
      is chosen, and P1_IDENTITY_OBSERVATION_BOUNDED_WEAKENING_V1 is neither
      minted nor accepted.
```

### §7.4 Withdrawals and replacements introduced by v2.2

v2's four withdrawn v1 sentences (`W-1`..`W-4`) and v2.1's two replacements
(`R-W1`, `R-W2`) stand. v2.2 replaces six further sentences, each because a
binding review line proved it false on the bytes:

```text
R-W3  v2.1 §2.7 D-8's "§P1-13.7 ... already gives each durable artifact exactly
      one open site"                                    REPLACED at D-8′ — the
      cited section pins INSTALL sites and three named reads, not peer-layer
      claim reads, and MS-2 itself has two call sites.
R-W4  v2.1 §3.2 C-5's "OPERATION. EXACTLY ONE SHA-256"  REPLACED at §3.2 —
      there are two authorized evaluations of one accessor.
R-W5  v2.1 §3.4 DC-1's "and there is never a second"    REPLACED at DC-1′.
R-W6  v2.1 §3.4 DC-6's "NO SECOND DIGEST ... the only value derived from a
      carrier"                                          REPLACED at DC-6′.
R-W7  v2.1 §3.4 DC-3's "never process identity ... never a name of anything
      addressable", DC-4's blanket "comparison"/"evidence" ban, and DC-5's
      unqualified "ONE-WAY"                             REPLACED at DC-3′,
      DC-4′, DC-5′ — true of authorized conforming use, false as absolute
      cryptographic assertions.
R-W8  v2.1 §3.5 WL-4(a)'s "the eighteen other canonical values are obtainable
      only by reading the claim"                        REPLACED at WL-4′(a) —
      the constructing supervisor holds them without reading anything, and the
      archive reader holds the integers in cleartext.
```

None of these replacements is restated anywhere in v2.2 in its old form.

---

## §8. Weakest points in v2.2, stated by the author

1. **`PA-7`'s second sentence is a new analysis kind.** Everything in
   `S-25a`..`S-25m` was a name match, a node-type match, an occurrence count or
   a position match. `PA-7` adds an **intra-function single-assignment lookup**
   (`D-14`). I believe it is well inside what `X M-2` permits — it is local,
   one-pass, terminating, and made unambiguous by `S-4` — but it is *more* than
   the previous rules, and a reviewer who reads `X M-2` as forbidding any
   name-resolution step at all would be entitled to say so. I have disclosed it
   as an increment rather than describing it as "the same discipline".

2. **`PC-N` is closed by shape, not by enumeration, and that is a judgement
   call.** I could have enumerated every peer durable path and made the table
   fully closed. I did not, because this packet does not own the peer's durable
   record set and enumerating it would be exactly the error shape of `YV2-C1` —
   imposing this packet's rules on contracts it does not own. The cost is that
   `PT-1` case 2 rests on `PA-1`+`PA-2`+`PA-3` holding over *unenumerated*
   constructors. I believe the case analysis is complete; a reviewer who wants
   a fully enumerated table would be asking for a different, wider packet.

3. **`V-m` (symlink indirection) is not fully closed and I say so.** `PA-6` bans
   `os.symlink`, `os.link`, `os.readlink` and the `follow_symlinks` keyword in
   the five roots, and `PA-1` still binds the only claims-root spelling — so no
   *conforming root* plants or follows a redirect. A symlink planted by an actor
   **outside** the five roots is a filesystem fact, not a static property, and
   this packet does not claim to close it. Under A3 that actor already has
   same-UID kernel power (`WL-4′(b)`), so I judge it not a new exposure — but
   it is a residual and it is disclosed rather than buried in the fixture table.

4. **`B-A4(iii)` is a real cost to the peer root and may be judged
   disproportionate.** A path-spelling and read-operand discipline over *every*
   path constructor and *every* read call in `generic_harness.py` is a large
   ask for a two-field identity cell. My defence is that it is the framers' own
   `S-13` discipline (composite `:2603`), that it removes no capability and
   relocates no read site (`PC-R2`), and that the alternative — deciding "can
   this expression denote the claims path?" semantically — is exactly the taint
   analysis `X M-2` forbids. A reviewer may reasonably hold that the right
   answer is instead to move the claim read into a P1-owned surface, which would
   be a different architecture and a different packet.

5. **Repair C makes the packet's claim strictly weaker, and I have not tried to
   compensate elsewhere.** v2.1 claimed a confidentiality property it did not
   have. v2.2 claims none. Everything the governance boundary needs is an
   authorization property (`CS-6`, `CS-7`, `WL-R1`), and I believe those hold —
   but a reviewer who was relying on the digest concealing the identity fields
   in any downstream reasoning must now redo that reasoning. `STEP 13` records
   this so no future contract can cite this cell as authority for the stronger
   claim.

6. **`L-1`..`L-5` enumerate lineage that other contracts own.** I classified
   them rather than constraining them (`L-R1`), and I gave a one-question test
   for telling a continuation from a third destination. If a reviewer holds that
   any of the five is in fact a third *direct* destination — for instance if a
   future archive index were to store the raw digest as its own key — then
   `L-R2` requires a new bounded correction, not a reinterpretation of `L-1`..
   `L-5`.

7. **The five roots remain a fixed list, and now the path discipline depends on
   it too.** Everything here is decidable because `PRODUCTION_ROOTS` is exactly
   five paths (`CHANGE 1`, composite `:2558`). `PT-1`'s case analysis is over
   expressions *in those five files*. A sixth production root re-derives every
   count in `S-25m′` **and** re-opens `PT-1`, and neither may be extended by
   analogy.

8. **I found no new defect in the parts both lines confirmed closed, and that is
   itself a claim a reviewer should test.** §7.1 and §7.2 assert that eighteen
   separate loci are untouched. I checked each against the v2.1 and v2 bytes,
   but the assertion is mine and the check is the reviewer's to repeat.

---

## §9. Negative space

This correction creates nothing executable and authorizes no selection, no X/Y
verdict, no implementation, no commit, no verifier or manifest edit, no code or
test artifact, no process, socket, pipe, fork, exec, signal, wait or `prctl`
operation, no supervisor, PCS, controller, worker or watchdog, no capability,
world, learner, entropy, capacity artifact, custody disposition, result
manifest, spend, datum, outcome, Proof or claim movement. It predicts no
qualification and no comparison outcome. `PA-1`..`PA-9`, `PC-1`/`PC-N`, `PT-1`,
`D-8′`, `EV-1`/`EV-2`, `OD-1`..`OD-4`, `L-1`..`L-5`, `CS-1`..`CS-7`, the primed
rule texts, `S-25n`, `S-25o` and `A-T18`..`A-T21` are **specification text, not
artifacts**. It selects neither option and mints no token. **No existing file
was modified.** `T` remains `NOT_ACTIVATED`; the programme claim remains `OPEN`;
the watchdog-freeze cell remains unresolved and orthogonal.
