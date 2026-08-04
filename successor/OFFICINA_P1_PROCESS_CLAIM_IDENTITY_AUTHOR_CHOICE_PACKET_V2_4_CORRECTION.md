# Officina P1 process-claim identity — author choice packet v2.4 (bounded satisfiability correction)

**Author:** Claude Code Opus 5, **specification author only**. Not an
independent X-line or Y-line reviewer. **This correction selects nothing.** It
repairs exactly the four fail-closed satisfiability defects the X line returned
against the v2.3 bytes, by adopting that line's `R-1`..`R-7` in full, and changes
nothing else.

**No token in this correction is signable.** Every token remains signable only
after an independent X-line confirmation and a bounded Y-line no-regression check
on identical bytes. `T` is `NOT_ACTIVATED`; the programme claim is `OPEN`; the
watchdog-freeze cell is `UNRESOLVED AND ORTHOGONAL`. This document creates
nothing executable and authorizes no implementation, activation, entropy draw,
resource use, data, trajectory, comparison, outcome or Proof.

**Status.** v2.4 is a **bounded satisfiability correction**. It carries
`successor/OFFICINA_P1_PROCESS_CLAIM_IDENTITY_AUTHOR_CHOICE_PACKET_V2_3_CORRECTION.md`
forward **verbatim** except for the loci named in the replacement index at §0.2,
and v2.3 carries v2.2, v2.1 and v2 forward as their own indices record. Every
earlier packet, closure and review is preserved byte-untouched as the evidentiary
record. **Reading order: v2, v2.1, v2.2, v2.3, then v2.4. Where two tiers differ
the later governs; everywhere else the earlier text is the operative text and is
read as written.**

**Repair mandate, and its two asymmetric inputs.**

```text
Y-LINE, reviews/sol_officina_p1_identity_v2_3_final_y_confirmation.md
        OFFICINA_P1_IDENTITY_V2_3_YLINE_CONFIRMED_FOR_AUTHOR_SELECTION
        The scientific-validity and governance boundary is CONFIRMED on the
        v2.3 bytes: the pathname theorem and its narrowed corollaries, the
        content-alias class CA-0..CA-5, the gate order and its four planted
        cases, the conditional information boundary, EV-3/C-6 and the
        authorized-use boundary, the bounded st_nlink strengthening, the
        arithmetic, the eight prior closures, the terminal routes, the author
        recommendation and the negative authorization.
        ⇒ NOTHING IN THAT SURFACE IS REOPENED HERE. v2.4 changes no sentence
          the Y line confirmed, except where a cross-reference or a count must
          mechanically follow R-1..R-7, and §9 lists every such follow.

X-LINE, reviews/opus_officina_p1_identity_v2_3_final_x_confirmation.md
        REVISE_OFFICINA_P1_IDENTITY_V2_3. CLOSED but NOT SATISFIABLE: no AST
        reaches either identity field from either record, and four operations
        the signed chain REQUIRES have no conforming spelling.
        B-1  PA-6′ bans os.chdir in every production root. The signed PCS
             preflight's FIRST step is P-cwd, _chdir("/") (composite :819-820).
             The X line further recorded that its own v2.2 review had
             affirmatively certified that ban as sound, and that the
             certification was false on the signed bytes.
        B-2  PA-6′ bans the dir_fd keyword on every read and write call. The
             composite states as a GENERAL rule that "Every later filesystem
             operation is dir_fd-relative to fd 5 or fd 6" (:822) and uses it
             at :905, :911, :916, :917-918 and :1052 — and the ban also
             contradicts the held-descriptor discipline PG-3 itself imports.
        B-3  PA-5′/PA-7′ require every enumerated read form's first operand to
             be a PATH. Nine of the thirty-three enumerated forms take a
             DESCRIPTOR — including os.read and os.fstat, which v2.4's own
             MS-2 shape and PG-3 conjuncts REQUIRE. The signed descriptor reads
             P-h (:901) and L-4 (:784) are static violations, and the central
             repair of v2.3 is self-refuting.
        B-4  PA-6′ asserts "EXACTLY TWO WRITE CALLS EXIST IN THE FIVE ROOTS".
             §P1-13.7 assigns FOUR durable installs to generic_harness.py
             alone, and protocol §B adds the ledger, head, state cache and
             locks. The count is false on the signed chain.
        Nonblocking: S-25m″ asserts the accessor count but omits the
        governed-mapping producer count, and PG-4's one-key read is in tension
        with its own "before any parse" ordering.
```

**Independence.** The X-line review that produced `B-1`..`B-4` disclosed that it
was performed in the same session that authored v2.3, and recommended that an
independent X line re-run the confirmation. **This correction adopts that
recommendation as binding**: v2.4's closure requires the next X review to be
performed by an agent that authored neither v2.3 nor v2.4.

---

## §0. What v2.4 changes, and where

### §0.1 The single defect shape, stated once

```text
ONE SHAPE, FOUR INSTANCES. Every one of B-1..B-4 is the same drafting error:
a clause written to protect TWO PINNED PATHNAME FAMILIES was stated as a rule
over ALL FILESYSTEM OPERATIONS IN ALL FIVE ROOTS. The intent of each clause is
correct and is preserved; only its SCOPE is repaired.

  B-1  "no chdir in any root"          should be  "exactly the signed one"
  B-2  "no dir_fd on any call"         should be  "none on a PINNED operand;
                                                   an anchored one elsewhere"
  B-3  "every read form has a path"    should be  "the PATH-OPERAND forms do;
                                                   the DESCRIPTOR-OPERAND forms
                                                   have their own binding rule"
  B-4  "exactly two write calls exist" should be  "exactly two have a PINNED
                                                   path operand"

NOTHING IN THIS SHAPE TOUCHES CLOSURE. Each repair widens what a CONFORMING
implementation may spell; none widens what a LEAKING one may reach, because
every widened form remains inside PA-1′'s two substring pins, PA-4′'s two
enumerated Name-use sets, PA-7″'s single read function, CR-3′'s five carrier
positions and PG-1..PG-7's gate. §6 demonstrates satisfiability operation by
operation; §7 re-derives every count; the X line's own closure audit found no
escaping AST and this correction adds no route to one.
```

### §0.2 The exact replacement index — four substantive rows and one mechanical row

| # | v2.3 locus replaced | Replaced by | Closes |
|---|---|---|---|
| **I** | `PA-6′` in whole | **§2**: `PA-6″` — the `chdir` clause, the `dir_fd` clause, the operand-kind split, the scoped write-call count, and the imperative write-call safety clause | X `B-1`, `B-2`, `B-4`; `R-1`, `R-2`, `R-4`, `R-5` |
| **II** | `PA-5′`; `PA-7′` | **§3**: `PA-5″` and `PA-7″`, applying to **path-operand** read calls only, plus `PA-7″(iv)`'s descriptor-operand binding rule | X `B-3`; `R-3` |
| **III** | `S-25m″` | **§4**: `S-25m‴`, adding the five governed-mapping producers as a count explicitly distinct from the five accessors, and scoping the write-call count | X Determination 5; `R-6` |
| **IV** | `PG-4` | **§5**: `PG-4′`, adding the discriminator's one-key-read clause | X Determination 6; `R-7` |
| **M** | mechanical only: `S-25n′`'s conjunction list; `A-T9′`'s named rule; `A-T26`; the fixture list `R-a`..`R-f`; the count table rows that name a repaired quantity | `S-25n″`, `A-T9″`, `A-T26′`, `A-T27`, `R-a`..`R-j`, §7's table | cross-references and counts that must follow `R-1`..`R-7` |

**Everything else in v2.3, v2.2, v2.1 and v2 carries forward verbatim.** In
particular — and this is the whole of the surface the Y line confirmed —
`PA-1′`, `PA-2`, `PA-3′`, `PA-4′`, `PA-8`, `PA-9′`, `PT-1′` and its three
corollaries, `D-8′`, `CA-0`..`CA-5`, `CA-R1`, `CA-R2`, `PG-1`, `PG-2`, `PG-3`,
`PG-5`, `PG-6`, `PG-7`, `S-25p`, `MS-1`, `MS-1L`, `MS-2`..`MS-14`,
`MS-R1`..`MS-R6`, `PC-1`/`PC-1L`/`PC-N`, `PC-R1′`, `PC-R2′`, `PC-R3`, `CR-1`,
`CR-2′`, `CR-3′`, `CR-4`, `S-25k`, `M-R1`..`M-R3`, `M-R4′`, `M-R5`, `S-25j`,
`S-25i` and its notes, `EV-1`, `EV-2`, `EV-3`, `EV-R1′`..`EV-R4`, `C-1`..`C-6`,
`C-5″`, `DC-1″`, `DC-6″`, `LD-1`..`LD-3`, `L-0`..`L-5`, `L-R1`, `L-R2`, `D-1`,
`D-2`, `S-25e″`, `S-25l″`, `S-25o`, `CS-1`..`CS-3`, `CS-4′`, `CS-5`..`CS-7`,
`CS-8`, `WL-1`, `WL-2`, `WL-3″`, `WL-4′`, `WL-R1`, `DC-2`, `DC-3′`, `DC-4′`,
`DC-5′`, `DC-7`, `IP`/`ACU`, class member `(f)`, `ACC-1`..`ACC-5`,
`ACC-R1`..`ACC-R5`, `RC-1`..`RC-4`, `NC-1`..`NC-3`, `P-R1`..`P-R5`, §3.5's model
choice, §3.6's destination search, `N-1`..`N-10`, and the author recommendation,
**stand as written**.

**No selection is made. Neither `A` nor `B` is chosen. The weakening token is
neither minted nor accepted.**

---

## §1. Binding inputs, on committed bytes

All digests were recomputed with `sha256sum` on the committed bytes, and each
working-tree file was verified byte-identical to its `HEAD` blob before being
read.

### §1.1 The bytes this correction repairs, and the two verdicts it answers

```text
832d31693d719a43198544807ffa74c96c88fb55d82bfb4ce70ef9fd265643e3  successor/OFFICINA_P1_PROCESS_CLAIM_IDENTITY_AUTHOR_CHOICE_PACKET_V2_3_CORRECTION.md
55e19217502c7f217f3ec1768f4db122abd14d4ef22c315d76fde38dac790633  reviews/opus5_officina_p1_process_claim_identity_choice_v2_3_closure.md
710d828d46a9bbb7f0cf7068c3f3f1667f83a4f22002693f5f8de48f9f321bf2  reviews/opus_officina_p1_identity_v2_3_final_x_confirmation.md   REVISE_OFFICINA_P1_IDENTITY_V2_3
f17adb9c439aa5c261bc159d505f4fda6fe73039830f90a08f6ddf900fe92a0f  reviews/sol_officina_p1_identity_v2_3_final_y_confirmation.md    OFFICINA_P1_IDENTITY_V2_3_YLINE_CONFIRMED_FOR_AUTHOR_SELECTION
```

Both v2.3 review lines independently recomputed `832d3169…43e3` and pinned it as
their target, so the bytes v2.4 repairs are the bytes both verdicts were returned
against.

### §1.2 The preserved evidentiary record, byte-untouched

```text
ad8b5791f043f201c00812a11de2ab3b765664e65e6d0ebf9778e150913096d3  successor/…PACKET_V1_DRAFT.md
f5d95a0d4a7c72731b5a20cf668e67dbc66329e0989fb945bd0a5727717f6095  successor/…PACKET_V2_DRAFT.md
3796de017449a9786db0b9b0ca0e8c2d84762e2239463033773b1fdb92b8ef37  successor/…PACKET_V2_1_CORRECTION.md
05046cd17fe0839541b9ec7614aaf66a84e69c169f9142a29e6a5cabf7bf0fc7  successor/…PACKET_V2_2_CORRECTION.md
e2ad45b7d3dd84d2537d19e52302a729ac390dae2a2fd6b169b4a84d15eca242  reviews/opus_officina_p1_identity_v2_2_final_x_confirmation.md
e82a6974d413b830b5913ddaaa788571aac56705ddaa0f3a9843f50c5b43abc1  reviews/sol_officina_p1_identity_v2_2_final_y_confirmation.md
a9d48c9d8d64214e4685065f9c16989aa095ccca14273019805682d00526f8e4  reviews/opus5_officina_p1_process_claim_identity_choice_v2_2_closure.md
56d0f598331a713918ea3f5b642449dd4dca1a08224b6e9eb4afb239ba128246  reviews/opus5_officina_p1_process_claim_identity_choice_v2_1_closure.md
c2d7a95784ad1bbc2a34898c0d3abf4de94dcd3416b14b959a3b2b61d6fab614  reviews/opus_officina_p1_process_claim_identity_choice_v2_1_final_confirmation.md
cee60b4b85358a50a90729645081419b166cbc1224b53776ffb41a357cb5f578  reviews/sol_officina_p1_process_claim_identity_choice_v2_1_final_confirmation.md
b7d061f5c60d75705f50ffc100bff24664336107dd450a8372e825c6f1afffa0  reviews/opus5_officina_p1_process_claim_identity_choice_v2_closure.md
0b104f3ec240acc5e067184efb752091f92920da7773c78aa35337de6a30f129  reviews/opus_officina_p1_process_claim_identity_choice_v2_confirmation.md
152b6dd2237a63d3ada6bd6a82a828892443a7752f838abf71cba0401ac01eb8  reviews/sol_officina_p1_process_claim_identity_choice_v2_confirmation.md
```

### §1.3 The governing signed chain, recomputed

```text
2c857fa8ad7be1c861eb8cf561f396e7d2339403c7714abc7958745bf34e5d5d  successor/…P1_OPERATIVE_COMPOSITE_V1_2.md
cd106d7fef491601f9ff948aba3ba0ceaac0774ac18a6564247c0c5899b4c40c  successor/OFFICINA_T_ACTIVATION_PROTOCOL_V2_CORRECTION.md
64b8d3f63594b79a6abc767a032383c5704beaf09b32a1e0c58fdc444bb0af71  successor/OFFICINA_GENERIC_HARNESS_CONTRACT_V2_DRAFT.md
8c47da352ef5954406964647a32e97939c404806bdf9b3d3ff5bc70866e6369a  successor/OFFICINA_GENERIC_HARNESS_SIGNATURE.md
724d633a55668013b78058eed1c76e12e9bbaf487f71ea94b7a4568ea1ced8a0  successor/OFFICINA_GENERIC_HARNESS_CONTRACT_V2_3_1_CORRECTION.md
b5a1523290b6b8417a7b3288329cc4a4e5ff80214c8f28e6ea1ae51a450a94c9  successor/OFFICINA_BATCH_SETTLEMENT_CORE_AMENDMENT_V1_1_1_CORRECTION.md
```

Loci newly load-bearing for this correction, in addition to every locus v2.3 §1.3
lists:

```text
composite :815-824    §P1-7.2 the PCS preflight; P-cwd. _chdir("/") with its
                      own CHDIR_FAILED token, "Executed after the six imports,
                      the binding block and §P1-3.5's identity check, and
                      BEFORE ANY NAME IS OPENED"; and the general rule "Every
                      later filesystem operation is dir_fd-relative to fd 5 or
                      fd 6, or acts on an already-open descriptor, or is an
                      absolute /proc name"
composite :901        P-h. "read descriptor 3 to EOF"
composite :784        L-4. "read the reply pipe to EOF"
composite :905-918    p-1, p-4, p-6, p-7, each _open(..., dir_fd = 6)
composite :920        "Only after every step above may c1 acquire SPAWN.lock"
composite :1050-1052  c1. _open("SPAWN.lock", _O_RDWR|_O_CREAT|_O_CLOEXEC,
                      0o600, dir_fd = T_PCB_FD_RUNTIME_ROOT)
composite :405-425    §P1-3.4 the primitive binding block: _open _read _write
                      _close _fstat _stat _listdir _unlink _fsync _rename ...
                      and the integer constants including _O_NOFOLLOW
composite :846-857    P-f. _fstat descriptors 3 through 8; S_ISREG; the
                      (st_dev, st_ino) identity records
composite :1006-1020  A-5..A-11, the role root's fstat and identity sequence
composite :2354-2371  §P1-13.7 — FOUR durable installs assigned to
                      generic_harness.py: spawn-intent, process claim,
                      supervisor identity, freeze observation
```

---

## §2. Repair I — `PA-6″` replaces `PA-6′` in whole

```text
PA-6″  REPLACES PA-6′. READ CALLS, WRITE CALLS, AND THE TWO FILESYSTEM-BASE
       DISCIPLINES.

(1) PATH-OPERAND READ CALLS — TWENTY-FOUR FORMS. A PATH-OPERAND READ CALL is
    any Call whose func is, or whose func's attr is, one of:
      builtin open;
      os.open, os.stat, os.lstat, os.statvfs, os.readlink, os.listdir,
      os.scandir, os.walk, os.fwalk;
      pathlib .open, .read_bytes, .read_text, .iterdir, .glob, .rglob, .stat,
      .lstat, .readlink;
      io.open; io.FileIO; codecs.open; fileinput.input; linecache.getline
    Its first positional operand is a PATH. PA-5″ and PA-7″ govern it.

(2) DESCRIPTOR-OPERAND READ CALLS — NINE FORMS. A DESCRIPTOR-OPERAND READ CALL
    is any Call whose func is, or whose func's attr is, one of:
      os.read, os.pread, os.preadv, os.readv, os.fstat, os.sendfile,
      os.copy_file_range;
      mmap.mmap; shutil.copyfileobj
    Its first positional operand is a FILE DESCRIPTOR, not a path. PA-5″ and
    PA-7″(i)-(iii) DO NOT GOVERN IT; PA-7″(iv) does.
    THE TWO LISTS PARTITION THE THIRTY-THREE FORMS v2.3 ENUMERATED. No form is
    added and none is removed; 24 + 9 = 33. The last six of (1) and the last
    two of (2) remain unimportable today under both allowlists (G-9) and are
    enumerated so that a future allowlist change cannot silently reopen a route.

(3) WRITE CALLS. A WRITE CALL is a Call to builtin open or os.open whose mode
    or flags operand is a Constant, or a BinOp Or over Constants, denoting
    creation or writing WITHOUT read access. A Call with no mode operand, or
    with a readable mode or flags Constant (including "r", "rb", "r+b", "w+b",
    "a+b", _O_RDONLY, _O_RDWR), is NOT a write call and remains a path-operand
    read call under (1). A Call whose mode or flags operand is not a Constant
    is NOT a write call and remains a path-operand read call, which fails
    closed under PA-7″.
    EXACTLY TWO WRITE CALLS IN THE FIVE ROOTS HAVE A PINNED PATH NAME AS THEIR
    PATH OPERAND: the atomic no-replace claim install at MS-12 (claim_path) and
    the durable lease write at MS-13 (lease_path). PA-4′(c) and PA-4′(e)
    enumerate those two uses.
    EVERY OTHER DURABLE INSTALL THE SIGNED CHAIN REQUIRES IS AN ORDINARY PC-N
    WRITE CALL AND IS NOT RESTRICTED BY THIS RULE — the spawn-intent record,
    the supervisor identity record and the freeze observation (composite
    §P1-13.7's other three peer installs), the ledger append, the external
    head, the state cache, the process record and the locks (protocol :58-72,
    contract :190-200; composite :1050-1052 shows the lock open in its signed
    form). Such calls are governed only by PA-2, PA-3′ and PA-5″'s spelling
    discipline, exactly as PC-R1′ already says of PC-N paths.
    THE v2.3 SENTENCE "EXACTLY TWO WRITE CALLS EXIST IN THE FIVE ROOTS" IS
    WITHDRAWN AS FALSE ON THE SIGNED CHAIN.

(4) WRITE-CALL SAFETY, IMPERATIVE. A write call SHALL contain no read
    expression and SHALL bind no byte string. A write call that contains a
    descriptor-operand read call, a .read(), or an Assign whose target receives
    its value, IS A STATIC VIOLATION. (v2.3 stated these as properties of a
    definition; they are stated here as a checked clause.)

(5) WORKING-DIRECTORY DISCIPLINE. os.chdir occurs EXACTLY ONCE in the five
    production roots: at the PCS preflight step P-cwd (composite :819-824), in
    scripts/officina_process_control_bootstrap.py, with the single str Constant
    "/" as its operand, lexically BEFORE every path-operand read call and every
    write call in that root. Any other chdir, a chdir with a non-Constant or
    non-"/" operand, or a chdir at any other position or in any other root, is
    a static violation. os.fchdir, os.symlink and os.link appear in NO
    production root.
    THE v2.3 SENTENCE BANNING os.chdir OUTRIGHT IS WITHDRAWN AS FALSE ON THE
    SIGNED CHAIN: P-cwd is mandatory, is the preflight's first filesystem step,
    and carries its own CHDIR_FAILED token. Its purpose is the same as this
    rule's — "the inherited working directory affects nothing" (:821-824) — and
    the anti-redirect property comes from (6), not from banning chdir.
    RECOGNITION: occurrence count, root match, position match, one Constant
    test. No flow.

(6) FILESYSTEM-BASE DISCIPLINE. NO READ CALL AND NO WRITE CALL WHOSE PATH
    OPERAND IS claim_path OR lease_path PASSES A dir_fd KEYWORD.
    Every other read or write call MAY pass dir_fd, and where it does the
    keyword's value is EITHER
      (a) an int Constant that is one of the signed anchor descriptor slots of
          §P1-6.2/§P1-6.5 — the composite's fd 5 or fd 6 (:822, and the four
          uses at :905, :911, :916, :917-918) — OR
      (b) a plain Name assigned exactly once, in its own enclosing function
          body or in the signed binding block, from a signed anchor: the
          composite's fd 5 or fd 6, or a held descriptor of protocol §B's
          held-file-descriptor set (:58-72), as at composite :1050-1052's
          dir_fd = T_PCB_FD_RUNTIME_ROOT.
    A dir_fd whose value is any other expression — a Call, a Subscript, an
    Attribute, an arithmetic expression, a parameter with no such binding — is
    a static violation.
    THE v2.3 BLANKET dir_fd BAN IS WITHDRAWN AS FALSE ON THE SIGNED CHAIN: the
    composite states dir_fd-relative access as its GENERAL rule at :822 and
    uses it at five enumerated sites, and PG-3(c)'s held-descriptor identity
    check depends on the same mechanism. THIS IS THE SIGNED DISCIPLINE, NOT AN
    EXCEPTION TO IT.
    RECOGNITION: name or Constant match at the keyword, plus the SAME
    single-assignment lookup PA-7″ already performs. NO NEW ANALYSIS KIND.

(7) NO follow_symlinks KEYWORD is passed by any read or write call in the five
    roots; no-follow is imposed by PG-2's flag Constant instead, because — as
    the Y line established at v2.2 — omitting the keyword does not prevent
    symlink following. UNCHANGED FROM v2.3.
```

---

## §3. Repair II — `PA-5″` and `PA-7″`, scoped to path operands

```text
PA-5″  REPLACES PA-5′. PATH-OPERAND SHAPE.
       In the five roots, the path operand of every PATH-OPERAND READ CALL
       (PA-6″(1)) and of every WRITE CALL (PA-6″(3)) is EITHER
         (a) a PLAIN NAME, or
         (b) a str/bytes Constant whose value contains NEITHER pinned substring
             of PA-1′.
       Never a concatenation or f-string, never a Call result, never a
       Subscript, never an Attribute, never a comprehension variable, never a
       starred or defaulted argument.
       (b) IS SAFE PRECISELY BECAUSE PA-1′ MAKES A PINNED-ROOT CONSTANT A
       STATIC VIOLATION ON SIGHT, in any syntactic position at any depth. The
       signed chain requires exactly this spelling at S-13's exact-constant
       descriptor paths (composite :2603), S-18's three /proc/self/fd
       enumerations (:2612, §P1-6.5), the four p-* package-root opens
       (:905-918), the SPAWN.lock open (:1052) and every fixed durable path of
       protocol :80-84.
       THIS RULE DOES NOT GOVERN DESCRIPTOR-OPERAND READ CALLS. PA-7″(iv) does.

PA-7″  REPLACES PA-7′. THE PINNED READS ARE THE ONLY READS OF THEIR FAMILIES,
       AND DESCRIPTORS HAVE THEIR OWN BINDING RULE.
       (i)   MS-2 (_read_record_bytes) is the ONLY function in the five roots
             containing a PATH-OPERAND READ CALL whose path operand is MS-2's
             own path parameter. That parameter is bound by no Assign, is used
             exactly once, and MS-2 is CALLED AT EXACTLY THREE SITES: the
             post-install claim verify, the MS-11 occupant load, and the MS-14
             lease load.
       (ii)  No path-operand read call outside MS-2 has a path operand that is
             claim_path or lease_path.
       (iii) EVERY OTHER PATH-OPERAND READ CALL in the five roots has a path
             operand that is either a Constant admitted by PA-5″(b), or a Name
             assigned EXACTLY ONCE, in its own enclosing function body, from a
             call to a path constructor of §2.4 other than MS-1 and MS-1L. A
             path-operand read call whose path operand is a bare parameter Name
             of any function other than MS-2, or a Name with no such binding in
             the enclosing body, is a static violation — i.e. NO
             GENERAL-PURPOSE READ HELPER EXISTS IN THE FIVE ROOTS BESIDES MS-2,
             WHOSE THREE CALL SITES ARE COUNTED.
       (iv)  NEW. DESCRIPTOR-OPERAND BINDING. The first operand of every
             DESCRIPTOR-OPERAND READ CALL (PA-6″(2)) is EITHER
               (a) a plain Name assigned EXACTLY ONCE, in its own enclosing
                   function body, from a PATH-OPERAND READ CALL that itself
                   satisfies PA-5″ and PA-7″(i)-(iii) — this is the case for
                   MS-2's own whole-content read and for PG-3's fstat
                   conjuncts, whose descriptor comes from MS-2's single
                   no-follow open; or
               (b) an int Constant that is one of the signed descriptor slot
                   numbers of §P1-6.2/§P1-6.5, or a plain Name bound once from
                   the signed binding block or the signed slot table — this is
                   the case for the request and reply descriptors of the signed
                   protocol path (composite :901's P-h "read descriptor 3 to
                   EOF" and :784's L-4) and for the enumerated slot descriptors
                   the P-f and A-5 sequences fstat (:846-857, :1006-1020).
             A descriptor operand with no such binding — a parameter, a
             Subscript, an Attribute, a Call result, an arithmetic expression —
             is a static violation.
             THE CLOSURE IS PRESERVED BY (a): A DESCRIPTOR CAN ONLY ARISE FROM
             AN OPEN THAT WAS ITSELF PATH-CHECKED. A descriptor for a pinned
             record therefore exists only inside MS-2, where PA-8 already
             confines the bytes it yields.
       RECOGNITION: name match, site match, occurrence count, one
       intra-function single-assignment lookup, and one one-hop
       callee-definition lookup (D-14′). (iv) uses THE SAME single-assignment
       lookup applied to a descriptor Name instead of a path Name. NO NEW
       ANALYSIS KIND, NO TAINT, NO TRANSITIVITY, NO FIXPOINT, NO CALL GRAPH.

D-11″  MECHANICAL. PA-2, PA-5″, PA-6″(1)-(4), PA-8 and PA-9′(a) are node-shape
       matches at enumerated node kinds, plus — for PA-5″(b), PA-6″(3)'s mode
       test and PA-6″(5)'s operand test — one substring test and two Constant
       tests. PA-6″(6) and PA-7″(iv) are a Constant-or-Name match plus the
       single-assignment lookup D-14′ already prices. Nothing else.
D-15″  MECHANICAL. THE WHOLE OF S-25a..S-25p REMAINS A SINGLE AST WALK over the
       five roots, with one per-function assignment index and one module-level
       definition index built during that walk, plus S-25p's node-order check.
       v2.4 spends no increment beyond what D-14′ already disclosed.
```

---

## §4. Repair III — `S-25m‴` and the mechanical rule cross-references

```text
S-25m‴ REPLACES S-25m″. COUNT CLOSURE. The five roots contain exactly:
         five accessor definitions            ACC-1..ACC-5
         FIVE GOVERNED-MAPPING PRODUCER SITES M-R4′: MS-3, MS-4, MS-5, MS-11,
                                              MS-14
           — A DIFFERENT SET OF FIVE FROM THE FIVE ACCESSOR DEFINITIONS,
             SHARING NO MEMBER WITH IT. ACC-2 and ACC-3 are MS-8 and MS-9;
             ACC-4 and ACC-5 are MS-6 and MS-7; ACC-1 is the wire accessor.
             None of the five produces a governed mapping, and none of the five
             producers is an accessor. The two numbers are equal by
             coincidence and are asserted separately so that a sixth of either
             fails by arithmetic rather than by review.
         six persistent consumers             C-1..C-6
         three governed mapping Names         M-R3
         five carrier Names                   CR-2′
         fifteen approved call-site rows      §2.4
         two pinned root literals             PA-1′
         two pinned path Names                PA-4′
         one read function at three call sites PA-7″(i)
         TWO WRITE CALLS WHOSE PATH OPERAND IS A PINNED PATH NAME
                                              PA-6″(3) — MS-12, MS-13. The
                                              number of PC-N write calls is
                                              NOT counted by this packet and is
                                              not restricted by it.
         one chdir, at P-cwd                  PA-6″(5)
         three ACC-5 evaluations              EV-1, EV-2, EV-3
         two persistent digest values, one transient digest value
         two direct persistent destinations of the claim lineage digest
                                              D-1, D-2
         one declassifying operation          DC-1″
       ⇒ "S-25m: accessor, producer, consumer, governed-name, carrier,
          call-site, pin, evaluation, write-call or destination count changed"

S-25n″ MECHANICAL REPLACEMENT OF S-25n′. Identical in substance; its
       conjunction now reads PA-1′, PA-2, PA-3′, PA-4′, PA-5″, PA-6″, PA-7″,
       PA-8, PA-9′
       ⇒ "S-25n: identity-bearing record path or read outside its anchored
          site"

S-25p  UNCHANGED IN TEXT. Its gate-order check now reads PG-4′ in place of
       PG-4, which changes no clause of S-25p itself.
A-T9″  MECHANICAL REPLACEMENT OF A-T9′. Fixture text unchanged; the assertion
       names S-25d AND S-25n″.
```

---

## §5. Repair IV — `PG-4′`

```text
PG-4′  REPLACES PG-4. THE PATH-BOUND EXACT-SCHEMA DISCRIMINATOR.
       Every clause of PG-4 carries forward verbatim — the discriminator runs
       after PG-3 and before the bytes are parsed for ordinary use, before they
       are returned from the reading function, and before any value of the
       parsed object is bound to a Name; a pinned claims path requires exactly
       philosophia.officina.t-process-claim.v1; a pinned leases path requires
       exactly philosophia.officina.t-active-lease.v1; a PC-N path requires
       exactly the schema value its own owning contract fixes for that path AND
       NEITHER OF THE TWO ABOVE — with one clause ADDED:

       THE DISCRIMINATOR'S OWN ONE-KEY READ IS NOT THE PARSE THIS RULE ORDERS
       AGAINST. The discriminator reads exactly the key "schema" by literal
       subscript, binds no other value, yields a boolean, and is THE ONLY READ
       OF THE CONTENT PERMITTED BEFORE THE GATE COMPLETES. The ordinary parse
       that PG-4′ and PG-5 order against is the one whose result may reach a
       consumer: the mapping binding, the return of content from the reading
       function, and any binding of a parsed value to a Name. No other key, no
       slice, no iteration and no second subscript is permitted before the gate
       completes.
```

---

## §6. Satisfiability, demonstrated operation by operation

Every operation the X line named, with its signed locus and its conforming
spelling under v2.4. **This section is the deliverable `B-1`..`B-4` demanded and
is normatively redundant with §2–§5: each row is satisfiable because a rule was
scoped, not because an exception was granted.**

| # | Signed operation | Locus | Conforming under v2.4 by |
|---|---|---|---|
| 1 | the PCS preflight `P-cwd. _chdir("/")` | composite `:819-824` | `PA-6″(5)` — exactly one chdir, PCS root, Constant `"/"`, before any open |
| 2 | `p-1`, `p-4`, `p-6` package-root opens, `dir_fd = 6` | `:905`, `:911`, `:916` | `PA-6″(6)(a)` — int Constant anchor slot; `PA-5″(b)` admits the path Constants (none contains a pinned substring) |
| 3 | `p-7` `_open("src", _O_DIRECTORY, dir_fd = 6)` | `:917-918` | same as 2 |
| 4 | `c1` `_open("SPAWN.lock", _O_RDWR\|_O_CREAT, 0o600, dir_fd = T_PCB_FD_RUNTIME_ROOT)` | `:1050-1052` | `_O_RDWR` is readable ⇒ a **read** call by `PA-6″(3)`; `PA-5″(b)` admits `"SPAWN.lock"`; `PA-6″(6)(b)` admits the anchor Name |
| 5 | `P-h` "read descriptor 3 to EOF" | `:901` | `PA-7″(iv)(b)` — signed slot descriptor |
| 6 | `L-4` "read the reply pipe to EOF" | `:784` | `PA-7″(iv)(b)` |
| 7 | `P-f` `_fstat` descriptors 3–8; `A-5`..`A-11` fstat sequence | `:846-857`, `:1006-1020` | `PA-7″(iv)(b)` — `os.fstat` is a descriptor-operand form and its operand is a signed slot |
| 8 | `MS-2`'s own no-follow open | v2.3 §2.4; `PG-2` | `PA-5″(a)` — plain Name (`MS-2`'s path parameter), `PA-7″(i)` |
| 9 | `MS-2`'s whole-content read; `PG-3`'s fstat conjuncts | v2.3 §2.4, `PG-3` | `PA-7″(iv)(a)` — descriptor bound once from `MS-2`'s own path-checked open. **This is the self-refutation `B-3` named, and it is closed** |
| 10 | the claim install `MS-12` | v2.3 §2.4 | `PA-6″(3)` — write call, pinned operand, one of the two |
| 11 | the lease install `MS-13` | v2.3 §2.4 | `PA-6″(3)` — the other of the two |
| 12 | the spawn-intent install | composite §P1-13.7 | `PA-6″(3)` — ordinary `PC-N` write call, uncounted, unrestricted |
| 13 | the supervisor identity install | composite §P1-13.7 | as 12 |
| 14 | the freeze-observation install | composite §P1-13.7 | as 12 |
| 15 | the ledger append, head, state cache, process record, locks | protocol `:58-72`; contract `:190-200` | as 12 |
| 16 | the three `/proc/self/fd` enumerations | `S-18`, `:2612`, §P1-6.5 | `PA-5″(b)` admits the exact constant; `PG-1` excludes enumerations from the gate |
| 17 | ordinary constant durable paths (`T_STATE.json`, ledger, head, locks) | protocol `:80-84` | `PA-5″(b)`, `PA-3′(b)` |
| 18 | every other `PC-N` peer read | `PC-R1′`, `PC-R2′` | `PA-5″`, `PA-7″(iii)`, plus the `PG` gate on content |

**Retained-behaviour fixtures, extended from six to ten, all asserted to PASS:**

```text
R-a  the spawn-intent record read                                    PASSES
R-b  the supervisor identity record at the watchdog role entry       PASSES
R-c  the freeze observation install and read                         PASSES
R-d′ any other PC-N peer durable record, spelled and gated           PASSES
R-e  the three /proc/self/fd exact-constant enumerations             PASSES
R-f  a constant durable path — T_STATE.json, ledger, head, a lock    PASSES
R-g  NEW. the PCS preflight P-cwd, _chdir("/")                       PASSES
R-h  NEW. the four p-* dir_fd = 6 opens and c1's anchored lock open  PASSES
R-i  NEW. the descriptor reads P-h and L-4, the P-f/A-5 fstat
     sequences, MS-2's whole-content read and PG-3's fstat conjuncts PASSES
R-j  NEW. the four §P1-13.7 peer installs and the protocol §B ledger,
     head, state cache and lock writes                               PASSES
A BUILD IN WHICH ANY OF R-a..R-j FAILS IS A TEST FAILURE, NOT A STRICTER BUILD.
```

**And the negatives that the scoping must NOT admit** — each still rejected:

```text
N-a  a second chdir, or a chdir with any operand but "/"      PA-6″(5)
N-b  a chdir in generic_harness.py or a role root             PA-6″(5)
N-c  dir_fd on a read or write whose operand is claim_path
     or lease_path                                            PA-6″(6)
N-d  dir_fd whose value is a Call, Subscript, Attribute or an
     unbound parameter                                        PA-6″(6)
N-e  a descriptor-operand read whose fd comes from a parameter,
     a Subscript or a Call result                              PA-7″(iv)
N-f  a descriptor-operand read whose fd comes from an open that
     itself failed PA-5″/PA-7″                                 PA-7″(iv)(a)
N-g  a write call containing a .read() or binding its value    PA-6″(4)
N-h  a third write call with a pinned path operand             PA-6″(3), PA-4′
N-i  the v2.2 lease construct, the v2.1 claim construct, and
     every variant V-a..V-q and LV-a..LV-j                     unchanged
N-j  every planted alias case                                  PG-2..PG-6
```

---

## §7. Counts after `R-1`..`R-7`

| Quantity | v2.3 | **v2.4** | Why |
|---|---|---|---|
| persistent consumers | 6 | **6** | unchanged |
| centralized accessors | 5 | **5** | unchanged |
| governed-mapping producers | 5 (table only) | **5 (now asserted in `S-25m‴`)** | `R-6` |
| verifier rules | 16 | **16** — `S-25a`..`S-25p` | no rule added; `S-25m‴`, `S-25n″` replace |
| behavioural tests | 26 | **27** — `A-T1`..`A-T27` | `A-T27` added; `A-T26′` replaces `A-T26` |
| governed mapping Names | 3 | **3** | unchanged |
| carrier Names | 5 | **5** | unchanged |
| approved call-site rows | 15 | **15** | unchanged |
| pinned root literals / path Names | 2 / 2 | **2 / 2** | unchanged |
| read function / call sites | 1 / 3 | **1 / 3** | unchanged |
| **enumerated read forms** | 33, one list | **33, partitioned 24 path-operand + 9 descriptor-operand** | `R-3`; no form added or removed |
| **write calls** | "2 in the five roots" *(false)* | **2 with a pinned path operand**; `PC-N` write calls uncounted | `R-4` |
| **chdir occurrences** | banned *(false)* | **1, at `P-cwd`** | `R-1` |
| **`dir_fd` uses** | banned *(false)* | **0 on pinned operands; anchored elsewhere** | `R-2` |
| `ACC-5` evaluations | 3 | **3** | unchanged |
| persistent / transient digest values | 2 / 1 | **2 / 1** | unchanged |
| direct destinations of the claim lineage digest | 2 | **2 — `D-1`, `D-2`** | unchanged |
| transitive continuations | 5 | **5 — `L-1`..`L-5`** | unchanged |
| declassifying operations | 1 | **1** | unchanged |
| content-alias residual members | 5 | **5 — `CA-1`..`CA-5`** | unchanged |
| retained-behaviour fixtures | 6 | **10 — `R-a`..`R-j`** | `R-1`..`R-4` demonstrations |
| handoff steps | 15 | **15** | unchanged |
| sentences withdrawn this round | 7 | **3 — `R-W16`..`R-W18`** | §9.3 |

**Arithmetic checks.** `24 + 9 = 33` read forms, the same thirty-three v2.3
enumerated. `26 + 1 = 27` tests, mapping to handoff test rows 92–118. `6 + 4 = 10`
fixtures. `S-25a`..`S-25p` is sixteen letters. The two fives of `S-25m‴` are
disjoint sets, as that rule now states in its own text.

**Handoff, mechanically amended:** `STEP 6` reads `S-1`…`S-25p` unchanged;
`STEP 7` becomes "adds `A-T1`…`A-T27` as test rows 92-118"; `STEPS 1`–`5`, `8`–`15`
are unchanged.

---

## §8. Tests added and amended by v2.4

`A-T1`..`A-T25` are unchanged in text, with `A-T9″`'s mechanical rule name.

```text
A-T26′ REPLACES A-T26. SATISFIABILITY, ASSERTED POSITIVELY AND EXHAUSTIVELY
       OVER §6's TABLE. Each row of §6 is a build fixture asserted to PASS,
       INDIVIDUALLY and with the admitting clause named:
         (a) P-cwd's _chdir("/")                            PA-6″(5)
         (b) p-1, p-4, p-6, p-7 with dir_fd = 6             PA-6″(6)(a)
         (c) c1's anchored SPAWN.lock open                  PA-6″(6)(b)
         (d) P-h and L-4 descriptor reads                   PA-7″(iv)(b)
         (e) P-f and A-5..A-11 fstat sequences              PA-7″(iv)(b)
         (f) MS-2's open, its whole-content read, and PG-3's
             fstat conjuncts                                PA-7″(iv)(a)
         (g) MS-12 and MS-13                                PA-6″(3)
         (h) the four §P1-13.7 peer installs and protocol §B's
             ledger, head, state cache and lock writes      PA-6″(3)
         (i) the three /proc/self/fd enumerations           PA-5″(b), PG-1
         (j) constant durable paths and no-stem constructors PA-5″(b), PA-3′(b)
         (k) a Constant path operand containing NEITHER pinned substring
             PASSES and one containing EITHER fails PA-1′ — asserted as a
             MATCHED PAIR, so the admission cannot drift into an exemption
       A build in which any of (a)-(k) fails is a TEST FAILURE, NOT A STRICTER
       BUILD.

A-T27  NEW. THE SCOPING NEGATIVES. Each of N-a..N-h of §6 is a build fixture
       asserted REJECTED STATICALLY with the named rule fired, INDIVIDUALLY:
         N-a second chdir / non-"/" operand        PA-6″(5)
         N-b chdir outside the PCS root            PA-6″(5)
         N-c dir_fd on a pinned path operand       PA-6″(6)
         N-d dir_fd from an unanchored expression  PA-6″(6)
         N-e descriptor from a parameter/Subscript/Call  PA-7″(iv)
         N-f descriptor from a non-conforming open  PA-7″(iv)(a)
         N-g write call containing a read or binding bytes  PA-6″(4)
         N-h a third pinned-operand write call     PA-6″(3), PA-4′
       AND the closure negatives are re-asserted unchanged: the v2.1 claim
       construct, the v2.2 lease construct, V-a..V-q, LV-a..LV-j and the four
       planted alias cases of A-T25 all remain REJECTED, so the scoping is
       shown to have widened only what a CONFORMING implementation may spell.
```

---

## §9. What v2.4 does not change

### §9.1 The whole of the Y-confirmed surface

The Y line confirmed v2.3 for author selection on the pathname theorem and its
corollaries, the content-alias class, the gate order and its four planted cases,
the conditional information boundary, `EV-3`/`C-6` and the authorized-use
boundary, the `st_nlink` strengthening, the arithmetic, the eight prior closures,
the terminal routes, the recommendation and the negative authorization.
**Not one sentence of that surface is amended here.** `PT-1′`, `CA-0`..`CA-5`,
`PG-1`, `PG-2`, `PG-3`, `PG-5`, `PG-6`, `PG-7`, `S-25p`, `CS-1`..`CS-8`,
`WL-1`..`WL-4′`, `WL-R1`, `DC-1″`..`DC-7`, `EV-1`..`EV-R4`, `C-1`..`C-6`,
`LD-1`..`LD-3`, `L-0`..`L-5`, `D-1`, `D-2`, `CR-1`..`CR-4`, `M-R1`..`M-R5`,
`MS-1`..`MS-14`, `ACC-*`, `RC-*`, `NC-*`, `P-R1`..`P-R5`, `N-1`..`N-10` are
untouched.

The four Y-line planted cases are unaffected by every repair here: `PG-2`'s
no-follow open, `PG-3`'s three conjuncts and `PG-5`'s dominant invalidity are
unchanged, and `PG-4′` adds only the clause that makes its own one-key read
explicit. The Y line's observation that the `/proc/self/fd` case may terminate
earlier, at the no-follow open, than `A-T25(d)`'s shorthand suggests remains
true and remains a stricter refusal, not a surviving route.

### §9.2 The eight prior closures and the prior mechanism

`X M-1`, `X m-1`, `X m-2`, `X m-3`, `Y-C2`, `Y-M1`, `Y-M2`, `Y-m1` are not in
this correction's replacement index and carry forward verbatim. So do `S-25i`
and its notes, `M-R1`..`M-R5`, `CR-*`, `S-25k`, the `MS` table, `ACC-R1`..`ACC-R5`,
`RC-1`..`RC-4`, `NC-1`..`NC-3`, §3.5's model choice and §3.6's destination
search. **Option A remains recommended and unselected; Option B remains
non-selectable behind `B-1` and `B-2`, on authority grounds.**

### §9.3 Withdrawals introduced by v2.4

```text
R-W16  v2.3 PA-6′'s "os.chdir ... appear in no production root"
       WITHDRAWN at PA-6″(5) — P-cwd is a mandatory signed step with its own
       failure token, and the anti-redirect property comes from the dir_fd
       discipline, not from banning chdir.
R-W17  v2.3 PA-6′'s "NO READ CALL AND NO WRITE CALL IN THE FIVE ROOTS PASSES A
       dir_fd KEYWORD"
       WITHDRAWN at PA-6″(6) — the composite states dir_fd-relative access as
       its general rule at :822 and uses it at five sites, and PG-3(c) depends
       on the same mechanism.
R-W18  v2.3 PA-6′'s "EXACTLY TWO WRITE CALLS EXIST IN THE FIVE ROOTS", and
       PA-5′/PA-7′'s application of a path-operand rule to descriptor-operand
       read calls
       WITHDRAWN at PA-6″(3) and PA-7″(iv) — §P1-13.7 assigns four durable
       installs to generic_harness.py alone, and nine of the thirty-three
       enumerated read forms take a descriptor, two of which MS-2 and PG-3
       themselves require.
```

None of these is restated anywhere in v2.4 in its old form. **All three were
false on the signed bytes, and all three failed closed** — no leak was ever
admitted by them, and none is admitted by their repair.

---

## §10. Weakest points in v2.4, stated by the author

1. **`PA-6″(6)` prohibits `dir_fd` on pinned path operands, and I cannot prove
   from the signed bytes that the peer's claim and lease opens will never be
   required to be `openat`-relative.** Protocol `:58-72` puts "the runtime
   **directory**" in the held-descriptor set, which is the shape one holds in
   order to resolve against. The X line's `R-2` and the repair mandate both
   specify the prohibition, and I have followed them exactly. If a later
   implementation review finds the claim or lease open must be anchored, the
   repair is one line and I state it here in advance so no future round has to
   rediscover it: *give the pinned families the same treatment as every other
   path — permit `dir_fd` whose value is a signed anchor under `PA-6″(6)(a)` or
   `(b)`, and forbid every other value.* That would preserve closure, because
   `PA-1′`, `PA-4′` and `PA-7″(i)` pin the path and the read site regardless of
   the base.

2. **`PA-7″(iv)(b)` defers to "the signed descriptor slot numbers of
   §P1-6.2/§P1-6.5" rather than enumerating them.** That is deliberate — this
   packet does not own the slot table and enumerating it would be the `YV2-C1`
   error — but it means the clause is decidable only against a table in another
   document. A reviewer may reasonably ask for the slot set to be named. I judge
   the deferral correct and the risk low, because a descriptor that is *not* in
   that table is a static violation, so the failure is closed.

3. **The partition at `PA-6″(1)`/`(2)` is by call form, not by argument type,
   and `mmap.mmap` and `shutil.copyfileobj` are judgement calls.** Both take
   descriptors or file objects rather than paths, so I placed them in `(2)`;
   both are unimportable under every current allowlist, so nothing turns on it
   today. If a future allowlist admits either, the placement should be
   re-checked rather than assumed.

4. **`PA-6″(3)`'s readable-mode test is a fixed table over mode strings and
   flag constants, and I have enumerated the common members rather than proving
   the table total.** The direction that matters is closed — a readable mode
   keeps the call inside `PA-5″`/`PA-7″` — so an omission fails closed. But the
   table is mine, and a reviewer should check it against the modes an
   implementation actually uses.

5. **This correction is narrow by construction, and I did not re-audit the
   surface the Y line confirmed.** I re-read it to check that nothing here
   touches it, which is a weaker act than re-deriving it. The Y line's
   confirmation stands on the v2.3 bytes; the bounded no-regression check the
   closure requests is what should establish that it still stands on these.

6. **The X-line findings this correction repairs were produced by a self-review,
   and so was v2.3 itself.** Every finding was verified here against the signed
   bytes and each is real. But the chain's two-line discipline has now been
   satisfied only on one side for two consecutive rounds, and no amount of care
   inside one session substitutes for it. The closure makes independence a
   requirement of the next round rather than a recommendation.

---

## §11. Negative space

This correction creates nothing executable and authorizes no selection, no X/Y
verdict, no implementation, no commit, no verifier or manifest edit, no code or
test artifact, no process, socket, pipe, fork, exec, signal, wait or `prctl`
operation, no supervisor, PCS, controller, worker or watchdog, no capability,
world, learner, entropy draw, capacity artifact, custody disposition, result
manifest, spend, settlement authorization, datum, trajectory, comparison,
outcome, Proof or claim movement. It predicts no qualification and no comparison
outcome. It adds **no production root, no durable schema, no destination, no
invalidity cause, no authority, no option and no author token**. `PA-5″`,
`PA-6″`, `PA-7″`, `S-25m‴`, `S-25n″`, `PG-4′`, `A-T26′`, `A-T27` and the fixtures
`R-g`..`R-j` are **specification text, not artifacts**; each of them *widens what
a conforming implementation may spell and narrows nothing that was closed*. It
selects neither option and mints no token. **No existing file was modified.** `T`
remains `NOT_ACTIVATED`; the programme claim remains `OPEN`; the watchdog-freeze
cell remains unresolved and orthogonal; Kirill's identity author selection remains
**unauthorized** pending an independent X-line confirmation and a bounded Y-line
no-regression check on these bytes.
