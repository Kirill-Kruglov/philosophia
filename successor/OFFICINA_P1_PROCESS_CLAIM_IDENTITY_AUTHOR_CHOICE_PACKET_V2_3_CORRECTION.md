# Officina P1 process-claim identity — author choice packet v2.3 (bounded correction)

**Author:** Claude Code Opus 5, **specification author only**. Not an
independent X-line or Y-line reviewer. **This correction selects nothing.** It
closes exactly the findings the two independent bounded *final* confirmation
lines returned `REVISE_OFFICINA_P1_IDENTITY_V2_2` on against the v2.2 bytes, and
changes nothing else.

**No token in this correction is signable.** Every token remains signable only
after a bounded independent X-line and Y-line confirmation round on identical
bytes. `T` is `NOT_ACTIVATED`; the programme claim is `OPEN`; the
watchdog-freeze cell is `UNRESOLVED AND ORTHOGONAL`. This document creates
nothing executable and authorizes no implementation, no activation, no entropy
draw, no data, no trajectory and no outcome.

**Status.** v2.3 is a **bounded correction of a bounded correction of a bounded
correction**, not a replacement. It carries
`successor/OFFICINA_P1_PROCESS_CLAIM_IDENTITY_AUTHOR_CHOICE_PACKET_V2_2_CORRECTION.md`
forward **verbatim** except for the loci named in the replacement index at §0.2;
v2.2 carries v2.1 forward verbatim except its three loci; v2.1 carries
`…PACKET_V2_DRAFT.md` forward verbatim except its two. v1, v2, v2.1, v2.2, both
v1 reviews, both v2 confirmations, both v2.1 final confirmations and both v2.2
final confirmations are preserved byte-untouched as the evidentiary record.
**Reading order: v2, then v2.1, then v2.2, then v2.3. Where two tiers differ the
later governs; everywhere else the earlier text is the operative text and is read
as written.**

**Bounded repair mandate.** Both final confirmation lines returned `REVISE` and
both are treated here as **binding defect reports, adopted without reservation
and without asking the author-principal to choose a different design cell**:

```text
X-line, reviews/opus_officina_p1_identity_v2_2_final_x_confirmation.md
        REVISE_OFFICINA_P1_IDENTITY_V2_2.
        D1 (blocking) THE LEASE IS THE UNPINNED HALF. successor/officina/
            runtime/T_ACTIVE_LEASES/<process_id>.json is the claim key set PLUS
            FIVE (protocol :241-246), is inside RESTRICTED_PROCESS_IDENTITY by
            name (v2 §2.6.1(d)) and inside RESTRICTED_CLAIM_CANONICAL_BYTES by
            name (v2.1 CR-1), and receives no path pin, no read pin, no carrier
            position and no install row. The v2.1 determination-2 construct
            reproduces verbatim through _lease_path and passes every rule of
            S-25a..S-25o; PC-R1 and fixture R-d affirmatively assert that it
            PASSES. PT-1 corollary 2 asserts a lease property its own four-case
            proof does not establish.
        D2 PA-6 defines a READ CALL by func name only, so MS-12's atomic
            no-replace install IS a read call and PA-7 statically rejects the
            packet's own install site; and PA-4(a)/PA-7 are jointly
            unsatisfiable by any implementation given MS-2's `path` parameter.
        D3 PA-5's "never a Constant" plus PA-7's constructor-binding
            requirement plus PA-3's mandatory stem grammar make the signed
            exact-constant descriptor paths of S-13/S-18 unspellable at the
            three /proc/self/fd enumerations §P1-6.5 requires, and make every
            constant durable path unreadable.
        D4 D-14 mislabels PA-7's analysis: classifying an RHS as a
            path-constructor call is a one-hop callee-definition lookup, not an
            intra-function one.
        D5 DC-6′ and C-5's amended FORBIDDEN clause deny the existence of any
            digest "of a claim, a LEASE, an occupant" other than EV-1/EV-2,
            while contract :116-124 REQUIRES active_lease_sha256. State where
            it is evaluated; do not guess.
Y-line, reviews/sol_officina_p1_identity_v2_2_final_y_confirmation.md
        REVISE_OFFICINA_P1_IDENTITY_V2_2.
        Y1  CS-4's "THERE IS NO READER FOR WHOM THE DIGEST CONCEALS THE
            IDENTITY FIELDS" and WL-3′'s "THE DIGEST HAS NO CONFIDENTIALITY
            PROPERTY" are absolutes that a search conditioned on eighteen known
            fields does not establish. The defensible statement is that this
            cell PROVIDES AND AUTHORIZES NO CONFIDENTIALITY GUARANTEE. The same
            conditional fact propagates through L-1..L-5 only for a reader who
            also knows each containing object's other fields.
        Y2  PT-1 proves a PATHNAME-SPELLING property and its corollaries
            promote it to a BYTE-PROVENANCE property. A permitted PC-N pathname
            can resolve to or contain claim bytes through a planted symlink, a
            hard link, a descriptor alias or copied bytes. Ordinary
            open(path,"rb") FOLLOWS a symlink; omitting follow_symlinks does
            not prevent it; samestat cannot distinguish a hard link, because a
            hard link is the same inode; and no path test distinguishes copied
            bytes. The consequence is uncontained: such bytes bind to a
            non-carrier Name and parse into a non-governed mapping, and the
            exact prior leak shape resumes after runtime aliasing.
```

**Nothing else is reopened.** Everything both lines confirmed closed is
untouched: `EV-1`/`EV-2`'s operands, sites, preconditions, destinations and
confinement; `D-1` and `D-2` as **exactly two** direct persistent destinations of
the raw claim lineage digest; `L-1`..`L-5`; `ACC-1`..`ACC-5`, `ACC-R1`..`ACC-R5`,
`RC-1`..`RC-4`, `NC-1`..`NC-3`; the eight findings closed at v2/v2.1; the whole
of Repair C's `IP`/`ACU` distinction and every sink prohibition; §3.5's model
choice and §3.6's destination search; and the author recommendation. §8 lists
every one of them with the exact locus that must remain intact.

---

## §0. What v2.3 changes, and where

### §0.1 The six residuals, in the reviewers' own terms

```text
RESIDUAL D — THE SECOND IDENTITY-BEARING RECORD (X D1, and Y §6's
  content-equivalence half). v2.2 pinned ONE of the TWO durable records that
  carry controller_pid and process_group_id. The active lease carries the same
  two integers by signature, and v2's own restricted class names it, names its
  reload, and names "an archived copy". Repair A's mechanism is correct; its
  DOMAIN was half the problem. The repair is to pin the second family with the
  same instruments and to re-derive every count.

RESIDUAL E — INTERNAL SATISFIABILITY (X D2, D3, D4). Three of Repair A's rules
  reject conforming code: the install site (PA-6/PA-7), MS-2's own read operand
  (PA-4/PA-7), and every exact-constant path the signed chain fixes (PA-5/PA-3
  against S-13/S-18/§P1-6.5). All three fail CLOSED and none is a leak, but a
  specification that cannot be conformed to is not a closure.

RESIDUAL F — PATHNAME IS NOT PROVENANCE (Y §5, §8.2). PT-1 is a sound theorem
  about which EXPRESSIONS can DENOTE a pinned-root pathname. It is not a
  theorem about which BYTES can reach a Name, because a pathname does not
  determine its content: symlink, hard link, descriptor alias and byte copy all
  break the promotion. The repair is to narrow the theorem to what it proves,
  to name the residual class honestly, and — the part v2.2 omitted entirely —
  to CONTAIN THE CONSEQUENCE with a read-time gate and a dominant invalidity
  route, so that aliased content cannot become an ordinary peer mapping.

RESIDUAL G — THE THIRD EVALUATION (X D5). active_lease_sha256 is required by
  the signed chain at every heartbeat. §1.4 audits WHERE it is evaluated and
  finds the governing bytes DETERMINE it: INSIDE the five production roots. It
  is therefore a real third authorized evaluation and a real sixth persistent
  consumer, and DC-6′'s inventory was false.

RESIDUAL H — THE SURVIVING ABSOLUTES (Y §4, §8.1). CS-4 and WL-3′ converted a
  correct disclaimer ("this cell guarantees no confidentiality") into an
  incorrect universal ("no reader is concealed from"). The conditioning fields
  must appear in every statement of the fact, including the summaries.

RESIDUAL I — LABELLING (X D4). PA-7's recognition step is a local
  single-assignment lookup FOLLOWED BY a one-hop callee-definition lookup. It
  is still not taint, not a fixpoint and not a transitive call graph, and it is
  restated in those words.
```

All six were re-derived here from the committed contract bytes, not accepted on
the reviewers' authority. All six are correct.

### §0.2 The exact replacement index — six rows, and no seventh

| # | v2.2 / v2.1 locus replaced | Replaced by | Closes |
|---|---|---|---|
| **D** | `PA-1`, `PA-4`, `PA-7`, `PA-9(d)`; `PC-1`/`PC-N` table; `PC-R1`; §2.4 rows `MS-2`, `MS-3`, `MS-6`, `MS-7`, `MS-10`, `MS-11`; `CR-2`, `CR-3`; `M-R4`; fixture `R-d` | **§2**: `PA-1′`, `PA-4′`, `PA-7′`, `PA-9′`, the `PC-1`/`PC-1L`/`PC-N` table, `PC-R1′`, the new rows `MS-1L`, `MS-13`, `MS-14` and the amended rows, `CR-2′`/`CR-3′`, `M-R4′`, `R-d′`, `S-25n′` | X `D1` |
| **E** | `PA-3`, `PA-5`, `PA-6`; `PA-4`'s position count; `MS-2`'s row shape; `PC-R2` | **§3**: `PA-3′`, `PA-5′`, `PA-6′` with the `WRITE CALL` definition, `PA-4′`'s use-counting note, `MS-2`'s descriptor-anchored row, `PC-R2′`, fixtures `R-e`, `R-f` | X `D2`, `D3` |
| **F** | `PT-1` and its three corollaries; §8 item 3's disposition of `V-m`; fixture-table rows `V-m` | **§4**: `PT-1′` narrowed to pathname construction with restated corollaries, `CA-1`..`CA-5`, the read gate `PG-1`..`PG-7`, `S-25p`, `V-m′` | Y `Y2` |
| **G** | `C-5` OPERATION clause and FORBIDDEN clause; `DC-1′`; `DC-6′`; `EV-R1`, `EV-R3`; `S-25e′`, `S-25l′`, `S-25m′`; the consumer count | **§5.1–§5.2**: `EV-3`, `C-6`, `LD-1`..`LD-3`, `C-5″`, `DC-1″`, `DC-6″`, `EV-R1′`, `EV-R3′`, `S-25e″`, `S-25l″`, `S-25m″` | X `D5` |
| **H** | `CS-4`; `WL-3′`; `B-A5′`'s summary sentence; every restatement of either | **§5.3**: `CS-4′`, `WL-3″`, `CS-8`, `B-A5″` | Y `Y1` |
| **I** | `D-14`; §8 item 1 | **§3.4**: `D-14′` | X `D4` |

**Everything else in v2.2, v2.1 and v2 carries forward verbatim.** In particular
`S-25i`/`S-25i-N1..N4`, `M-R1`, `M-R2`, `M-R3`, `M-R5`, `S-25j` and its scope
note, `PA-2`, `PA-8`, `CR-1`, `CR-4`, `S-25k`, `MS-1`, `MS-4`, `MS-5`, `MS-8`,
`MS-9`, `MS-12`, `MS-R1`..`MS-R4`, `D-5`..`D-7`, `D-8′`, `D-9`..`D-13`, `D-15`,
`P-1`..`P-4`, `EV-1`, `EV-2`, `EV-R2`, `OD-1`..`OD-4`, `S-25o`, `L-0`..`L-5`,
`L-R1`, `L-R2`, `D-1`, `D-2`, `IP`/`ACU`, `CS-R1`, `CS-R2`, `CS-1`, `CS-2`,
`CS-3`, `CS-5`, `CS-6`, `CS-7`, `DC-2`, `DC-3′`, `DC-4′`, `DC-5′`, `DC-7`,
`WL-1`, `WL-2`, `WL-4′`, `WL-R1`, `CS-P1`..`CS-P7`, `ACC-1`..`ACC-5`,
`ACC-R1`..`ACC-R5`, `RC-1`..`RC-4`, `NC-1`..`NC-3`, `P-R1`..`P-R5`, §3.5's model
choice, §3.6's destination search, and the whole of v2 as v2.1 and v2.2 carry it,
stand as written.

**No selection is made. Neither `A` nor `B` is chosen. The weakening token is
neither minted nor accepted.**

---

## §1. Binding inputs, on committed bytes

All digests below were recomputed with `sha256sum` on the committed bytes of
this repository at the time of writing, and each working-tree file was verified
byte-identical to its `HEAD` blob before being read.

### §1.1 The bytes this correction repairs, and the verdicts it answers

```text
05046cd17fe0839541b9ec7614aaf66a84e69c169f9142a29e6a5cabf7bf0fc7  successor/OFFICINA_P1_PROCESS_CLAIM_IDENTITY_AUTHOR_CHOICE_PACKET_V2_2_CORRECTION.md
```

Both final confirmation lines independently recomputed that value and pinned it
as their target (X §0 custody; Y §2), so the bytes v2.3 repairs are the bytes the
two `REVISE` verdicts were returned against.

### §1.2 The preserved evidentiary record, confirmed byte-untouched

```text
ad8b5791f043f201c00812a11de2ab3b765664e65e6d0ebf9778e150913096d3  successor/OFFICINA_P1_PROCESS_CLAIM_IDENTITY_AUTHOR_CHOICE_PACKET_V1_DRAFT.md
f5d95a0d4a7c72731b5a20cf668e67dbc66329e0989fb945bd0a5727717f6095  successor/OFFICINA_P1_PROCESS_CLAIM_IDENTITY_AUTHOR_CHOICE_PACKET_V2_DRAFT.md
3796de017449a9786db0b9b0ca0e8c2d84762e2239463033773b1fdb92b8ef37  successor/OFFICINA_P1_PROCESS_CLAIM_IDENTITY_AUTHOR_CHOICE_PACKET_V2_1_CORRECTION.md
b7d061f5c60d75705f50ffc100bff24664336107dd450a8372e825c6f1afffa0  reviews/opus5_officina_p1_process_claim_identity_choice_v2_closure.md
0b104f3ec240acc5e067184efb752091f92920da7773c78aa35337de6a30f129  reviews/opus_officina_p1_process_claim_identity_choice_v2_confirmation.md
152b6dd2237a63d3ada6bd6a82a828892443a7752f838abf71cba0401ac01eb8  reviews/sol_officina_p1_process_claim_identity_choice_v2_confirmation.md
56d0f598331a713918ea3f5b642449dd4dca1a08224b6e9eb4afb239ba128246  reviews/opus5_officina_p1_process_claim_identity_choice_v2_1_closure.md
c2d7a95784ad1bbc2a34898c0d3abf4de94dcd3416b14b959a3b2b61d6fab614  reviews/opus_officina_p1_process_claim_identity_choice_v2_1_final_confirmation.md
cee60b4b85358a50a90729645081419b166cbc1224b53776ffb41a357cb5f578  reviews/sol_officina_p1_process_claim_identity_choice_v2_1_final_confirmation.md
a9d48c9d8d64214e4685065f9c16989aa095ccca14273019805682d00526f8e4  reviews/opus5_officina_p1_process_claim_identity_choice_v2_2_closure.md
```

The two v2.2 final confirmations, which are the direct inputs to this
correction, are recorded in the closure that accompanies it; a correction cannot
carry a digest of a file written after it without creating a cycle, and this one
does not.

**A custody note both final lines raised independently, adopted here.** No path
`…PACKET_V2_CORRECTION.md` exists. The v2 tier is `…PACKET_V2_DRAFT.md`
(`f5d95a0d…6095`). Every reference in this chain is to that committed file.

### §1.3 The governing signed chain, recomputed

```text
2c857fa8ad7be1c861eb8cf561f396e7d2339403c7714abc7958745bf34e5d5d  successor/OFFICINA_GENERIC_HARNESS_SUPERVISOR_CONTROL_CHANNEL_P1_OPERATIVE_COMPOSITE_V1_2.md
cd106d7fef491601f9ff948aba3ba0ceaac0774ac18a6564247c0c5899b4c40c  successor/OFFICINA_T_ACTIVATION_PROTOCOL_V2_CORRECTION.md
64b8d3f63594b79a6abc767a032383c5704beaf09b32a1e0c58fdc444bb0af71  successor/OFFICINA_GENERIC_HARNESS_CONTRACT_V2_DRAFT.md
8c47da352ef5954406964647a32e97939c404806bdf9b3d3ff5bc70866e6369a  successor/OFFICINA_GENERIC_HARNESS_SIGNATURE.md
724d633a55668013b78058eed1c76e12e9bbaf487f71ea94b7a4568ea1ced8a0  successor/OFFICINA_GENERIC_HARNESS_CONTRACT_V2_3_1_CORRECTION.md
b5a1523290b6b8417a7b3288329cc4a4e5ff80214c8f28e6ea1ae51a450a94c9  successor/OFFICINA_BATCH_SETTLEMENT_CORE_AMENDMENT_V1_1_1_CORRECTION.md
```

Load-bearing loci read directly for this correction, in addition to every locus
v2.2 §1.3 lists, which is carried forward unchanged:

```text
protocol  :80-84       the tracked runtime paths, including
                       successor/officina/runtime/T_ACTIVE_LEASES/<process_id>.json
protocol  :241-246     "The active lease keys are exactly the claim keys plus"
                       last_charged_reading_ns, cumulative_charge_ns,
                       heartbeat_deadline_ns, outstanding_liability_ns,
                       prior_charge_event_sha256          <-- THE SECOND RECORD
                                                              CARRYING BOTH
                                                              IDENTITY KEYS
protocol  :58-72       §B. the runtime lock O_RDWR|O_CLOEXEC|O_NOFOLLOW,
                       "checked as a regular file at its canonical path"; and
                       "The runtime directory, ledger, external head, state
                       cache, PROCESS CLAIM, ACTIVE LEASE, and process record
                       use the held-file-descriptor `samestat` discipline
                       accepted in WP-4 ... Pathname hashes or recyclable inode
                       tuples alone are insufficient."   <-- THE SIGNED
                                                             ANTI-ALIAS
                                                             DISCIPLINE
contract  :190-200     §3. the same discipline inherited exactly: canonical
                       ASCII JSON with trailing newline; temp write -> fsync ->
                       atomic install, "no-replace for creations; replace only
                       where the protocol says replace"; the held-descriptor
                       lock across read -> ANCHOR VALIDATION -> verify ->
                       append -> cache/lease update -> fsync -> post-verify
contract  :116-124     §2c.5 heartbeat settlement; T_DEVICE_TIME_CHARGED whose
                       active_lease_sha256 is "the hash of the exact
                       pre-settlement lease"; "install the successor lease"
contract  :103-106     §2c.3 lease installation
contract  :505-514     §9. "Production roots are exactly the immutable-control
                       verifier's pinned tuple", the third of which is
                       src/philosophia/officina/generic_harness.py
contract  :517-522     generic_harness.py's __main__ IS the CLI
                       (claim/start/HEARTBEAT/close/pause/resume); "No
                       additional scripts/*.py entry point is introduced"
contract  :576         the implementation-surface row:
                       src/philosophia/officina/generic_harness.py carries
                       "supervisor, lifecycle tables (§2), §3 transaction
                       helpers, §4 RESERVATION/SETTLEMENT/BATCH/CONSERVATION,
                       §5 isolation-and-promotion, §6 pause/resume/recovery,
                       CPU meter adapter, __main__ CLI"
batch     :93-97       the settlement entry's active_lease_sha256 = "SHA-256 of
                       the durable pre-settlement lease"
composite :349-357     §P1-3.1 the five production roots, the third of which is
                       src/philosophia/officina/generic_harness.py
composite :905-917     the P1 roots' own O_NOFOLLOW + S_ISREG + (st_dev, st_ino)
                       identity discipline at p-2..p-7
composite :1006-1020   A-5..A-11, the same discipline at the role entry
composite :2612        S-18, the /proc/self/fd enumeration at exactly the three
                       sites of §P1-6.5
```

### §1.4 The audit X `D5` required: where `active_lease_sha256` is evaluated

The X line refused to let this be guessed, and required a bounded blocker if the
governing bytes did not determine it. **They determine it.** Three independent
signed loci compose:

```text
AUDIT STEP 1 — WHAT COMPUTES IT.
  contract :116-124 places active_lease_sha256 inside HEARTBEAT SETTLEMENT, and
  batch :93-97 fixes its value as "SHA-256 of the durable pre-settlement
  lease". The operand is a whole durable lease. Settlement is §2c.5 of the
  lifecycle tables and §4 of the contract.

AUDIT STEP 2 — WHICH FILE CARRIES SETTLEMENT.
  contract :576, the signed implementation-surface table, assigns to
  src/philosophia/officina/generic_harness.py: "supervisor, lifecycle tables
  (§2), §3 transaction helpers, §4 reservation/SETTLEMENT/batch/conservation,
  ... __main__ CLI (claim/start/HEARTBEAT/close/pause/resume)". contract
  :517-522 forecloses the alternative: generic_harness.py's __main__ IS the
  CLI, invoked python -m philosophia.officina.generic_harness, and "No
  additional scripts/*.py entry point is introduced". There is no other signed
  home for the heartbeat.

AUDIT STEP 3 — WHETHER THAT FILE IS A PRODUCTION ROOT.
  contract :505-514 "Production roots are exactly the immutable-control
  verifier's pinned tuple", listing src/philosophia/officina/generic_harness.py
  third. composite :349-357 lists the same path third among the five P1
  production roots. It is a production root under BOTH governing documents.

CONCLUSION, STATED RATHER THAN GUESSED.
  active_lease_sha256 IS EVALUATED INSIDE THE FIVE PRODUCTION ROOTS, in
  src/philosophia/officina/generic_harness.py. So is the lease installation of
  contract :103-106 and the successor-lease install of :116-124. THE GOVERNING
  BYTES DETERMINE IT; NO BLOCKER IS RETURNED ON X R-5.

CONSEQUENCES, TAKEN IN FULL AT §2 AND §5.
  (a) the lease install row belongs in the approved call-site table (X R-1);
  (b) active_lease_sha256 is a REAL THIRD AUTHORIZED EVALUATION over a
      restricted carrier, and DC-6′'s "NO OTHER digest ... of a claim, a LEASE,
      an occupant ... exists in the five roots" WAS FALSE ON THE SIGNED BYTES;
  (c) it is a REAL SIXTH PERSISTENT CONSUMER of RESTRICTED_CLAIM_CANONICAL_BYTES,
      exactly as C-5 was a real fifth one at v2.1;
  (d) NONE OF THIS IS CREATED HERE. Every one of these operations is already
      required by the signed chain. v2.3 names what v2.1 and v2.2 denied.
```

**The key-order arithmetic, extended to the lease and re-derived.** The lease
key set is the claim's twenty keys **plus five appended** (`protocol :241-246`),
so a lease's canonical serialization contains `controller_pid` and
`process_group_id` at whatever positions the canonical order fixes for the claim
— index 5 and index 7 in the protocol's stated order. The X line's construct
needs no adaptation beyond the path: it is the same construct against a strictly
larger record.

---

## §2. Repair D — the second identity-bearing record

### §2.1 Why v2.2 did not reach it — re-derived, not summarized

```text
H-1  PA-1 pins ONE substring, "T_PROCESS_CLAIMS". The lease root spells
     "T_ACTIVE_LEASES". A substring test over one substring is blind to the
     other by construction.
H-2  PA-4 pins ONE Name, claim_path. PA-7 pins ONE read. PA-9(d) is scoped to
     "A CLAIM-PATH READ". PT-1's four cases are over expressions that can
     denote "a path under successor/officina/runtime/T_PROCESS_CLAIMS/".
H-3  PC-R1 says "ONLY CLAIM PATHS ARE RESTRICTED" and fixture R-d asserts that
     "any other PC-N peer durable record ... read through a plain-Name operand
     PASSES". The lease is therefore not merely unguarded; v2.2 AFFIRMATIVELY
     CERTIFIES the leaking read.
H-4  CR-1's restricted-bytes class is "a t-process-claim.v1 OR t-active-lease.v1
     object, however obtained", and S-25k enforces positions on three NAMES.
     Lease bytes bound to a fourth, ungoverned Name are outside every position
     rule — the identical blindness the X line documented at v2.1 for claim
     bytes.
H-5  M-R4's second sentence covers "a claim OR LEASE mapping", and D-8′ rests
     its decidability on PT-1. PT-1 proves nothing about a lease path. So
     M-R4's lease half has NO decidability anchor at all — the exact defect
     shape D-8 had before v2.2, displaced one record to the left.
H-6  CONSEQUENCE, THE LEAKING AST, ADOPTED FROM THE X LINE VERBATIM:
         lp     = _lease_path(process_id)
         raw    = open(lp, "rb").read()
         m      = json.loads(raw)
         vals   = list(m.values())
         leaked = vals[5]
     passes PA-1..PA-9, S-25n, S-25i/j/k, M-R1/M-R2, CR-*, S-25c/d and every
     count rule, and reaches controller_pid at a second sink.

WHAT WAS NOT AT RISK, so the repair is not sold as wider than it is:
H-7  The lease adds NO new schema, NO new production root, NO new destination
     and NO new authority. It is a signed durable record this packet already
     names in its own restricted class. Pinning it enlarges the DOMAIN of an
     accepted mechanism; it invents no mechanism.
H-8  The lease does NOT carry process_claim_sha256, so it is not a third direct
     destination of the claim lineage digest, and D-1/D-2 are untouched. The Y
     line established this independently at its §3.1 and it is confirmed here
     against protocol :241-246.
```

### §2.2 `PA-1′`..`PA-9′` — the rules, over two pinned families

```text
PA-1′  REPLACES PA-1. THE IDENTITY-BEARING RECORD-ROOT LITERALS ARE PINNED.
       In the five production roots:
         (a) a string or bytes Constant whose value contains the substring
             "T_PROCESS_CLAIMS" occurs EXACTLY ONCE, as the single Constant
             path-root operand inside _claim_path (MS-1);
         (b) a string or bytes Constant whose value contains the substring
             "T_ACTIVE_LEASES" occurs EXACTLY ONCE, as the single Constant
             path-root operand inside _lease_path (MS-1L).
       Any other occurrence of either substring, in any syntactic position, at
       any depth, in any of the five roots, is a static violation.
       THE TWO SUBSTRINGS ARE THE COMPLETE PINNED SET. They are the two record
       classes whose signed key sets contain controller_pid and
       process_group_id (protocol :231-238, :241-246), and no third signed
       record class contains either key — the final process record does not
       (protocol :248-257), and the three other interface artifacts do not
       (composite §P1-13.2 rows 1, 3, 4). A future record class that acquires
       either key requires its own bounded correction adding its own row.
       RECOGNITION: two substring tests over the value of every Constant node.
       No resolution, no imports, no flow.

PA-2   UNCHANGED. Every path-building expression in the five roots occurs
       inside a path constructor over Constants and its own grammar-checked
       stem, in the enumerated node shapes.

PA-3′  REPLACES PA-3. GRAMMAR-CHECKED STEMS, AND NO-STEM CONSTRUCTORS.
       Every path constructor takes AT MOST ONE dynamic stem parameter.
         (a) A constructor WITH a stem parameter: its FIRST statement is a
             grammar check that refuses any value containing "/", "\\", NUL,
             "..", a leading ".", or any byte outside the constructor's own
             pinned character class, whose refusal branch raises or routes to
             the invalidity disposition with no fallthrough. For MS-1 and MS-1L
             the pinned class is the 64-lowercase-hex process_id stem.
         (b) A constructor with NO dynamic stem parameter — one that returns a
             fixed Constant path — has NO grammar check and is well-formed. Its
             body is exactly one Return of a str/bytes Constant admitted by
             PA-5′. This closes X D3's no-stem case, which PA-3 made
             unspellable.
       A constructor with a second dynamic operand, or with a stem parameter
       and no first-statement grammar check, is a static violation.

PA-4′  REPLACES PA-4. THE TWO PINNED PATH NAMES, AND HOW USES ARE COUNTED.
       MS-1 is DEFINED once and CALLED at exactly one site, binding exactly one
       Name, claim_path. MS-1L is DEFINED once and CALLED at exactly one site,
       binding exactly one Name, lease_path. The occupant path of MS-11 IS
       claim_path (v2 §2.10.3, protocol :83) and no second Name exists for it.
       claim_path occurs in EXACTLY THESE USES AND NOWHERE ELSE:
         (a) the single positional path argument of the MS-2 call at the
             post-install verify site;
         (b) the single positional path argument of the MS-2 call inside the
             MS-11 occupant load;
         (c) the single positional path argument of the MS-12 install call.
       lease_path occurs in EXACTLY THESE USES AND NOWHERE ELSE:
         (d) the single positional path argument of the MS-2 call inside the
             MS-14 lease load;
         (e) the single positional path argument of the MS-13 lease install.
       USE COUNTING, STATED SO THE RULE IS SATISFIABLE (X D2). The Assign
       target that binds the Name from its constructor is its BINDING, not a
       use, and is not counted. A use is an occurrence of the Name in a load
       position. Passing the Name to an enumerated MS function and that
       function's own use of its path parameter are THE SAME use, counted once
       at the call site.
       Neither Name is aliased, re-assigned, returned, stored in a container,
       passed to a non-MS function, compared, formatted, logged, or joined.
       ⇒ closes the ALIAS variant by position and the SECOND-CONSTRUCTION
         variant by call count, for both families.

PA-5′  REPLACES PA-5. READ-OPERAND SHAPE, WITH CONSTANTS ADMITTED (X D3).
       In the five roots, the path operand of every enumerated read call form
       (PA-6′) is EITHER
         (a) a PLAIN NAME, or
         (b) a str/bytes Constant whose value contains NEITHER pinned substring
             of PA-1′.
       Never a concatenation or f-string, never a Call result, never a
       Subscript, never an Attribute, never a comprehension variable, never a
       starred or defaulted argument.
       (b) IS SAFE PRECISELY BECAUSE PA-1′ MAKES A PINNED-ROOT CONSTANT A
       STATIC VIOLATION ON SIGHT. A Constant operand therefore cannot denote an
       identity-bearing record path, and the signed chain requires exactly this
       spelling: S-13's "the descriptor paths are exact constants" (composite
       :2603), S-18's three /proc/self/fd enumerations (composite :2612,
       §P1-6.5), and every fixed durable path of protocol :80-84.
       RECOGNITION: node-type match plus one substring test. No flow.

PA-6′  REPLACES PA-6. READ CALLS, AND — NEW — WRITE CALLS (X D2).
       A READ CALL is any Call whose func is, or whose func's attr is, one of:
         builtin open; os.open, os.read, os.pread, os.preadv, os.readv,
         os.sendfile, os.copy_file_range, os.readlink, os.listdir, os.scandir,
         os.walk, os.fwalk, os.stat, os.lstat, os.fstat, os.statvfs;
         pathlib .open, .read_bytes, .read_text, .iterdir, .glob, .rglob,
         .stat, .lstat, .readlink;
         mmap.mmap; io.open; io.FileIO; codecs.open; fileinput.input;
         linecache.getline; shutil.copyfileobj
       — the last seven being unimportable today under both allowlists (G-9)
       and enumerated so that a future allowlist change cannot silently reopen
       the route.
       A WRITE CALL is a Call to builtin open or os.open whose mode or flags
       operand is a Constant, or a BinOp Or over Constants, denoting creation
       or writing WITHOUT read access. EXACTLY TWO WRITE CALLS EXIST IN THE
       FIVE ROOTS: the atomic no-replace claim install at MS-12, and the durable
       lease write at MS-13. A write call is NOT a read call: PA-5′ and PA-7′
       do not apply to it, it contains no read expression, and it binds no byte
       string. Its path operand is claim_path (MS-12) or lease_path (MS-13), as
       PA-4′(c) and (e) enumerate.
       RECOGNITION: func-name match plus a Constant-operand test. No flow.
       NO READ CALL AND NO WRITE CALL IN THE FIVE ROOTS PASSES A dir_fd
       KEYWORD, and os.chdir, os.fchdir, os.symlink and os.link appear in no
       production root, so no operation is resolved relative to a redirected
       base. follow_symlinks is not passed as a keyword; no-follow is imposed
       by the PG-2 flag Constant instead, because — as the Y line established —
       omitting the keyword does not prevent symlink following.

PA-7′  REPLACES PA-7. THE PINNED READS ARE THE ONLY READS OF THEIR FAMILIES.
       (i)  MS-2 (_read_record_bytes) is the ONLY function in the five roots
            containing a read call whose path operand is MS-2's own path
            parameter. That parameter is bound by no Assign, is used exactly
            once, and MS-2 is CALLED AT EXACTLY THREE SITES: the post-install
            claim verify, the MS-11 occupant load, and the MS-14 lease load.
       (ii) No read call outside MS-2 has a path operand that is claim_path or
            lease_path. By PA-4′ those two Names have no other use anyway; (ii)
            states it as its own rule so the check is a name match rather than
            an inference.
       (iii) EVERY OTHER READ CALL in the five roots has a path operand that is
            either a Constant admitted by PA-5′(b), or a Name assigned EXACTLY
            ONCE, in its own enclosing function body, from a call to a path
            constructor of §2.4 other than MS-1 and MS-1L. A read call whose
            path operand is a bare parameter Name of any function other than
            MS-2, or a Name with no such binding in the enclosing body, is a
            static violation — i.e. NO GENERAL-PURPOSE READ HELPER EXISTS IN
            THE FIVE ROOTS BESIDES MS-2, WHOSE THREE CALL SITES ARE COUNTED.
       RECOGNITION: name match, site match, one intra-function
       single-assignment lookup, and one one-hop callee-definition lookup
       (D-14′). Not transitive. No call graph. No fixpoint. No taint.
       ⇒ closes the HELPER-RETURN variant twice, for both families.

PA-8   UNCHANGED IN SUBSTANCE, EXTENDED BY DOMAIN. The byte string produced by
       MS-2's read binds IMMEDIATELY and ONLY to a carrier Name of CR-2′, under
       every clause of PA-8 as written — one Assign to a carrier target, one
       bare Return, no alternate target, container, comprehension, callback,
       decorator, exception payload or second return shape. The three carrier
       Names it may bind at its three call sites are claim_bytes, occupant_bytes
       and lease_bytes respectively.

PA-9′  REPLACES PA-9. CANONICAL PARSING IS PINNED TO MS-3.
       In the five roots:
         (a) json.loads and json.load occur only with a PLAIN NAME operand;
         (b) a json.loads or json.load whose operand is a carrier Name occurs
             ONLY inside _record_mapping_from_bytes (MS-3), which contains
             exactly one such call;
         (c) json.JSONDecoder, json.JSONEncoder and ast.literal_eval remain
             banned root-wide by S-25i(iii);
         (d) NO FRESH MAPPING MAY BE PRODUCED FROM A PINNED-PATH READ OUTSIDE
             MS-3. By PT-1′ the only pinned-path reads are MS-2's three, by
             PA-8 their bytes bind only to carriers, and by (a)+(b) a carrier
             reaches json.loads only at MS-3. The proposition is DERIVED from
             syntax for pinned paths, and for PC-N paths it is supplied
             instead by the gate at §4, which is where a pathname argument
             cannot reach.
```

### §2.3 The path-constructor table — two named rows, one shape-closed class

| # | Constructor | Root prefix | Stem | Binds to | Governed by |
|---|---|---|---|---|---|
| `PC-1` | `_claim_path(process_id)` = `MS-1` | the single pinned Constant containing `T_PROCESS_CLAIMS` (`PA-1′(a)`) | `process_id`, 64 lowercase hex, checked at the constructor's first statement (`PA-3′(a)`) | `claim_path`, one Name, three uses (`PA-4′`) | `PA-1′`..`PA-4′`, `PA-7′`, `MS-1` |
| `PC-1L` | `_lease_path(process_id)` = `MS-1L` | the single pinned Constant containing `T_ACTIVE_LEASES` (`PA-1′(b)`) | `process_id`, 64 lowercase hex, checked at the constructor's first statement (`PA-3′(a)`) | `lease_path`, one Name, two uses (`PA-4′`) | `PA-1′`..`PA-4′`, `PA-7′`, `MS-1L` |
| `PC-N` | every other path constructor in the five roots, with or without a stem — the spawn-intent record, the supervisor identity record, the freeze observation, the ledger, the head, the state, the journal, checkpoints, manifests, the locks, and every other peer-owned durable path | a Constant that, by `PA-1′`, contains **neither** pinned substring | its own grammar-checked stem, or none (`PA-3′(b)`) | its own path Name, or a Constant operand admitted by `PA-5′(b)` | `PA-2`, `PA-3′`, `PA-5′`, `PA-6′`, `PA-7′(iii)` — **and the read gate `PG-1`..`PG-7` of §4** |

```text
PC-R1′ REPLACES PC-R1. PC-N IS NOT ENUMERATED BY THIS PACKET AND ITS PATH SET
       IS NOT RESTRICTED BY IT. The peer layer keeps every durable path it has
       and may add more. What PC-N rows must satisfy is (i) a SPELLING AND
       SHAPE discipline and (ii) THE READ GATE OF §4 — not a permission list.
       THE v2.2 SENTENCE "ONLY CLAIM PATHS ARE RESTRICTED" IS WITHDRAWN TWICE
       OVER: the lease path is restricted too (PA-1′(b)), and every PC-N read
       is gated on content (PG-1..PG-7), because a pathname does not determine
       its bytes.
PC-R2′ REPLACES PC-R2. RETAINED PEER-ROOT open() IS RECONCILED, NOT WITHDRAWN,
       AND THE PINNED READS ARE DESCRIPTOR-ANCHORED. S-25i-N1 stands verbatim:
       the builtin open is NOT added to generic_harness.py's forbidden set, and
       peer records outside protocol §B's named set continue to be opened with
       open() and parsed with json.loads exactly as the peer contract signs
       them. What changes is HOW THE PATH IS SPELLED, THAT THE READ'S OPERAND
       IS A PLAIN NAME OR AN ADMITTED CONSTANT, and THAT EVERY READ PASSES THE
       §4 GATE BEFORE ITS BYTES ARE PARSED, RETURNED OR BOUND. No peer read
       site is removed or relocated.
       FOR THE TWO PINNED FAMILIES THE SHAPE IS NOT NEGOTIABLE AND IS NOT NEW:
       protocol :58-72 ALREADY requires the process claim and the active lease
       to use "the held-file-descriptor `samestat` discipline", and contract
       :190-200 inherits it exactly. v2.1's MS-2 row — "exactly one
       open(path,"rb")" — DID NOT IMPLEMENT THAT SIGNED DISCIPLINE. §3.1
       repairs the row rather than the contract.
PC-R3  THE COST IS REAL AND IS PRICED, AND IT IS NOW LARGER THAN v2.2 PRICED
       IT. PA-2/PA-3′/PA-5′/PA-7′ constrain path construction across the whole
       peer root; PG-1..PG-7 constrain every durable read in it. That is wider
       than two identity fields need. It follows the framers' own S-13
       precedent and protocol §B's own anchor discipline, it removes no
       capability, and it is counted at B-A4(iii) and B-A8 rather than hidden.
```

### §2.4 The amended approved call-site table

Rows `MS-1`, `MS-4`, `MS-5`, `MS-8`, `MS-9`, `MS-12` and `MS-R1`..`MS-R4` are
**unchanged**. The rows below are added or amended; every amendment is listed in
§0.2 row **D** or **E**.

| # | Enumerated function | Exact call it may contain | Operand | Result binds to |
|---|---|---|---|---|
| `MS-1L` | **NEW.** `_lease_path(process_id)` | one path construction over the single pinned Constant containing `T_ACTIVE_LEASES` and the 64-hex `process_id` stem | `process_id` | `lease_path` |
| `MS-2` | **AMENDED (X D2, PC-R2′).** `_read_record_bytes(record_path)` | the descriptor-anchored read of §3.1 `PG-2`: exactly one `os.open` with the pinned no-follow flag Constant, exactly one `fstat` of that descriptor, the `PG-3` conjuncts, exactly one whole-content read in the form contract §3 fixes for descriptor-anchored durable reads, and exactly one close | its own path parameter, at exactly three call sites: `claim_path` twice (verify, `MS-11`), `lease_path` once (`MS-14`) | a carrier Name (§2.5) |
| `MS-3` | **AMENDED (domain).** `_record_mapping_from_bytes(carrier)` | exactly one `json.loads(carrier)` | one carrier Name | `claim_mapping`, `occupant_mapping` **or** `lease_mapping` |
| `MS-6` | **AMENDED (domain).** `_canonical_record_bytes(mapping)` — **`ACC-4`** | exactly one canonical serialization of the whole mapping in the encoding the peer contract already fixes for durable records, and exactly one `.encode("ascii")`; **this packet invents no encoding** | `claim_mapping`, `occupant_mapping` **or** `lease_mapping` | a carrier Name |
| `MS-7` | **AMENDED (domain).** `_canonical_record_sha256(carrier)` — **`ACC-5`** | exactly one `hashlib.sha256(carrier)` and exactly one `.hexdigest()` | one carrier Name | a 64-lowercase-hex `str` |
| `MS-10` | **AMENDED (domain).** `_validate_record_mapping(mapping)` | the schema validation of `X-2` against the exact key set its record class fixes — `protocol :231-238` for a claim or occupant, `protocol :241-246` for a lease — with exact types, strict `int`, recursive scientific-field rejection. It reads keys **only** by literal subscript and binds **no** value of either identity key to a Name; the two identity keys are validated through `MS-8` and its boolean result alone | `claim_mapping`, `occupant_mapping` **or** `lease_mapping` | a boolean |
| `MS-11` | **UNCHANGED IN TEXT.** the `EEXIST` occupant load (§2.10.3) | `MS-2` then `MS-3`, in that order, at exactly one site | `claim_path` | `occupant_mapping` |
| `MS-13` | **NEW.** `_install_lease(lease_path, carrier)` | exactly one durable write of the carrier bytes in the form contract §3 fixes — same-directory temp write, file `fsync`, atomic install (no-replace for the creation of `contract :103-106`; replace for the successor lease of `contract :116-124`, which is where "the protocol says replace"), parent-directory `fsync` — under the held-descriptor `T_RUNTIME.lock`. **This packet fixes no durability rule of its own and defers every one of them to the owning contract.** | `lease_path`, one carrier Name | none |
| `MS-14` | **NEW.** the lease load | `MS-2` then `MS-3`, in that order, at exactly one site | `lease_path` | `lease_mapping` |

```text
MS-R5  NEW. MS-1L, MS-13 and MS-14 are each DEFINED EXACTLY ONCE in the five
       roots and called only at the sites enumerated here, under MS-R1's
       discipline. MS-R2 (no default argument, no *args/**kwargs, no fallback
       branch, no cache, no attribute assignment, no second return shape) and
       MS-R3 (no row returns a governed mapping Name's value, a carrier's
       slice, or any individual identity field) apply to them unchanged.
MS-R6  NEW. THE THREE FUNCTION NAMES THAT LOST A CLAIM-SPECIFIC PREFIX —
       MS-2, MS-3, MS-6, MS-7, MS-10 — ARE THE SAME FUNCTIONS WITH THE SAME
       SHAPE, SAME OPERAND COUNT, SAME RESULT KIND AND SAME SINGLE DEFINITION.
       The rename is descriptive, not substantive: the operand class of each
       was already "a mapping" or "one carrier Name" in v2.1's own row text,
       and the lease was always inside CR-1's byte class. No row acquires a
       second operand, a second call form, or a second return shape.
```

### §2.5 `CR-2′`/`CR-3′` — five carriers, closed positions

```text
CR-1   UNCHANGED. RESTRICTED_CLAIM_CANONICAL_BYTES is every byte string that
       is, or is derived from, the canonical serialization of a
       t-process-claim.v1 or t-active-lease.v1 object, however obtained.
CR-2′  REPLACES CR-2. CARRIER NAMES, EXACTLY FIVE:
          canonical_bytes        the bytes MS-6 produces for the claim being
                                 installed
          claim_bytes            the bytes MS-2 reads from the durable claim
                                 path
          occupant_bytes         the bytes MS-2 reads from the EEXIST occupant
                                 path
          lease_canonical_bytes  the bytes MS-6 produces for a lease being
                                 installed
          lease_bytes            the bytes MS-2 reads from the durable lease
                                 path
       Each is assigned exactly once, never rebound, never deleted, never
       parameterized outside the approved signatures of §2.4.
       WHY FIVE AND NOT FOUR. The X line's R-1 named the fourth, lease_bytes,
       as the read carrier. The fifth is forced and is not an elaboration: the
       lease INSTALL (MS-13) must write canonical lease bytes, those bytes are
       produced at MS-6, and CR-3′ must give them a position or the signed
       lease install is unspellable — the same gap that made v2.2's lease
       install impossible. Both are stated rather than one being folded into
       the other.
CR-3′  REPLACES CR-3. CARRIER POSITIONS, CLOSED. A carrier Name may occur ONLY
       as:
         (a) the single operand of MS-3;
         (b) the single operand of MS-7 (ACC-5);
         (c) the byte operand of MS-12, the atomic no-replace claim install;
         (d) one side of the single X-1 byte-equality comparison of §2.10.3,
             whose other side is the other carrier and whose result is a
             boolean;
         (e) the byte operand of MS-13, the durable lease write.
       NOWHERE ELSE.
CR-4   UNCHANGED. On a carrier: no Subscript or slice, index, decode, split or
       any other bytes method, regex, iteration, comprehension, unpacking,
       destructuring, len/ord/int/str/repr/format/f-string, second hash, second
       serialization, alternate encoding, logging, diagnostic or frame
       placement, or any return other than the enumerated ones.
S-25k  UNCHANGED IN TEXT. CR-1..CR-4 hold over the five production roots as an
       occurrence count and position match — now on exactly five Names.
```

### §2.6 `M-R4′` — the producers, re-derived

```text
M-R3   UNCHANGED. GOVERNED MAPPING NAMES, EXACTLY THREE: claim_mapping,
       lease_mapping, occupant_mapping.
M-R4′  REPLACES M-R4. CLOSED PRODUCERS, FIVE SITES. A governed mapping Name is
       bound ONLY by MS-3, MS-4, MS-5, MS-11 or MS-14, and by nothing else.
       No other expression in the five roots may yield a claim or lease
       mapping. ITS DECIDABILITY NOW HAS TWO ANCHORS, NOT ONE:
         (i)  for the two pinned families, PT-1′: the only expressions that can
              denote a pinned-root pathname are claim_path and lease_path, and
              the only reads of them are MS-2's three call sites, whose bytes
              bind only to carriers (PA-8) and reach json.loads only at MS-3
              (PA-9′);
         (ii) for every other pathname, the §4 gate: a PC-N read whose content
              is a claim- or lease-shaped object routes to dominant invalidity
              BEFORE any mapping is bound, so no such expression yields a claim
              or lease mapping either — it yields an invalidity disposition.
       THE v2.2 CLAIM THAT (i) ALONE SUFFICES IS WITHDRAWN. It was false for
       lease paths (H-1..H-5) and, as the Y line proved, false for content
       aliases at any path.
M-R5   UNCHANGED. A governed mapping Name occurs only as the single positional
       operand of an approved call of §2.4's table.
```

### §2.7 The lease counterexample fixtures, one-to-one

```text
THE X-LINE'S LEASE CONSTRUCT (opus…v2_2_final_x_confirmation.md, §1.3)

  lp     = _lease_path(process_id)
  raw    = open(lp, "rb").read()
  m      = json.loads(raw)
  vals   = list(m.values())
  leaked = vals[5]

  FIRES, INDEPENDENTLY, FOUR TIMES UNDER v2.3:
    line 1  PA-1′(b)  a second Constant containing T_ACTIVE_LEASES, since
                      _lease_path IS MS-1L and is called at exactly one site;
                      a second construction site fires PA-4′ by call count
    line 2  PA-7′(ii) a read call whose path operand is lease_path outside
                      MS-2
    line 2  PA-6′     the read is not the descriptor-anchored MS-2 form, so it
                      cannot satisfy PG-2/PG-3 either
    line 3  PA-9′(b)  json.loads whose operand is a carrier outside MS-3, or —
                      if raw is a non-carrier Name — a mapping produced from a
                      pinned-path read outside MS-3, PA-9′(d)
  AND THE SINK IS NEVER REACHED: m cannot exist (PT-1′ corollary 3).
```

| # | Lease variant | Rule(s) that fire | Mechanically |
|---|---|---|---|
| `LV-a` | `p = "successor/officina/runtime/T_ACTIVE_LEASES/" + process_id + ".json"` | `PA-1′(b)`, `PA-2` | second pinned Constant; path-building outside a constructor with a non-Constant, non-stem operand |
| `LV-b` | second call `p = _lease_path(other_id)` | `PA-4′` | `MS-1L` is called at exactly one site and binds exactly one Name |
| `LV-c` | alias `q = lease_path` | `PA-4′` | an `Assign` RHS is not one of `lease_path`'s two enumerated uses |
| `LV-d` | helper `def _get(p): return open(p,"rb").read()` … `_get(lease_path)` | `PA-7′(ii)`, `PA-7′(iii)` | the helper's operand is a bare parameter Name of a function other than `MS-2`; and `_get(lease_path)` is a third use |
| `LV-e` | split literal `"T_ACTIVE_" + "LEASES/"` | `PA-1′(b)` after constant folding, and `PA-2` | folding is over `Constant` operands only |
| `LV-f` | stem traversal `_state_path("../T_ACTIVE_LEASES/" + process_id + ".json")` | `PA-3′(a)`, `PA-1′(b)`, `PA-2` | the stem grammar refuses `/`, `..`, leading `.`; the literal pin fires anyway |
| `LV-g` | read the lease through `os.open`/`os.read`, `pathlib`, `mmap`, `listdir`, `scandir` | `PA-6′`, `PA-7′(ii)`, `G-9` | every form is enumerated and the operand discipline is identical |
| `LV-h` | reach the lease's identity through `MS-5`'s in-memory `lease_mapping` | `S-25j`, `M-R5` | `lease_mapping` is a governed Name; every extraction shape was already closed at v2.1 |
| `LV-i` | hash the lease outside `MS-7`, or hash a lease slice | `S-25k` (`CR-4`), `S-25m″` | second hash on a carrier; evaluation count |
| `LV-j` | write lease bytes to a non-lease path | `CR-3′` | a carrier's only write positions are `MS-12` and `MS-13` |

**Retained-behaviour fixtures, asserted to PASS** — extended from `R-a`..`R-d`,
with the two the X line required:

```text
R-a  the spawn-intent record: p = _spawn_intent_path(); raw = MS-2-shaped read;
     gate passes; m = json.loads(raw)                              PASSES
R-b  the supervisor identity record at the watchdog role entry     PASSES
R-c  the freeze observation install and read                       PASSES
R-d′ REPLACES R-d. any other PC-N peer durable record, built from a Constant
     root and a grammar-checked stem or from a no-stem constructor, read
     through a plain-Name or admitted-Constant operand AND THROUGH THE §4
     GATE, whose content is not claim- or lease-shaped                PASSES
     — the added clause is the whole of Y2: PC-N reads pass on CONTENT as well
       as on SPELLING, and R-d's unconditional PASS is withdrawn
R-e  NEW (X R-3). the three /proc/self/fd enumerations of §P1-6.5, over the
     exact constant path S-13 requires                             PASSES
R-f  NEW (X R-3). a constant durable path read — T_STATE.json, the ledger, the
     head, a lock — through a no-stem constructor or an admitted Constant
                                                                   PASSES
     — in every case because PA-1′ does not fire (neither pinned substring),
       PA-2/PA-3′ are satisfied by construction, PA-5′(b) admits the Constant,
       PA-7′(iii) is satisfied, and the gate returns "not a pinned-class
       object". A build in which R-a..R-f fail is a TEST FAILURE, NOT A
       STRICTER BUILD.
```

### §2.8 What Repair D preserves exactly

```text
PA-P1′ S-25i and S-25i-N1..N4 are UNCHANGED IN TEXT. The builtin open stays
       available in generic_harness.py for records outside protocol §B's named
       set. The fix is a SITE PIN and a CONTENT GATE, not a BAN.
PA-P2  M-R1, M-R2, M-R3, M-R5, S-25j and its scope note are UNCHANGED.
       Ordinary peer-layer mappings remain entirely unaffected and .values(),
       .items() and ** remain available on them — subject only to the gate,
       which decides whether a mapping is ordinary at all.
PA-P3′ CR-1 and CR-4 and S-25k are UNCHANGED IN TEXT; CR-2/CR-3 are extended by
       domain only. PT-1′ corollary 1 supplies the premise S-25k needs FOR
       PINNED PATHS, and the gate supplies it for every other path.
PA-P4′ MS-1, MS-4, MS-5, MS-8, MS-9, MS-12 and MS-R1..MS-R4 are UNCHANGED.
       MS-2, MS-3, MS-6, MS-7, MS-10 and MS-11 keep their operand kinds,
       result kinds and single definitions; only their record-class domain and,
       for MS-2, their read shape change, and both changes are listed at §0.2.
PA-P5  D-5, D-6, D-7, D-9 and D-8′ are UNCHANGED. D-14 is replaced by D-14′ for
       labelling only.
PA-P6′ v2's A-T9 fixture text is UNCHANGED, and A-T9′'s amended assertion
       stands: fixture 5 must fire S-25d AND S-25n′.
PA-P7  NC-1..NC-3 are UNCHANGED and remain grounded in §P1-13.7's INSTALL-site
       property, which nothing here disturbs.
```

---

## §3. Repair E — making the rules internally satisfiable

### §3.1 The install is a write, and `MS-2` is descriptor-anchored

`PA-6′` already separates write calls from read calls. What remains is `MS-2`'s
own shape, which v2.1 wrote as `open(path,"rb")` and which the signed chain does
not permit for these two records:

```text
protocol :58-72  "The runtime directory, ledger, external head, state cache,
                 PROCESS CLAIM, ACTIVE LEASE, and process record use the
                 held-file-descriptor `samestat` discipline accepted in WP-4 ...
                 Pathname hashes or recyclable inode tuples alone are
                 insufficient."
contract :190-200 the same discipline inherited exactly, with anchor validation
                 inside the held lock.
```

`MS-2`'s amended row at §2.4 states the shape; the conjuncts it must check are
`PG-2`/`PG-3` below, so that the pinned reads and the `PC-N` reads pass through
**one** discipline rather than two. This is not a new requirement invented by
this cell — it is the signed requirement v2.1's row silently omitted.

### §3.2 The remaining satisfiability repairs, stated as deltas

```text
E-1  MS-12 IS A WRITE CALL (PA-6′). PA-4′(c) enumerates its path use and PA-5′
     and PA-7′ do not apply to it. The v2.2 state in which S-25n rejected the
     packet's own install site is closed.
E-2  MS-13 IS THE SECOND AND LAST WRITE CALL. Exactly two exist.
E-3  MS-2's PARAMETER IS ITS OWN, AND USES ARE COUNTED AT CALL SITES (PA-4′).
     The v2.2 state in which no implementation could satisfy PA-4(a) and PA-7
     together is closed by making MS-2 the single enumerated read function
     whose parameter is not a pinned Name, and by counting a pinned Name's use
     once at the call site rather than twice.
E-4  CONSTANT PATH OPERANDS ARE ADMITTED WHEN THEY CANNOT DENOTE A PINNED ROOT
     (PA-5′(b)), and NO-STEM CONSTRUCTORS ARE WELL-FORMED (PA-3′(b)). The
     signed exact-constant descriptor paths of S-13 and the three /proc/self/fd
     enumerations of S-18/§P1-6.5 are spellable again, and so is every fixed
     durable path of protocol :80-84. Fixtures R-e and R-f assert it.
E-5  NOTHING IN E-1..E-4 WEAKENS A PIN. A Constant containing either pinned
     substring remains a static violation in every syntactic position at any
     depth (PA-1′), which is exactly why (b) is safe.
```

### §3.3 Decidability, priced honestly

```text
D-10   UNCHANGED. PA-1′ is two substring tests over Constant node values.
D-11′  PA-2, PA-5′, PA-6′, PA-8 and PA-9′(a) are NODE-SHAPE MATCHES at
       enumerated node kinds, plus — for PA-5′(b) and PA-6′'s write-call test —
       one substring test and one Constant-operand test. Nothing else.
D-12′  PA-3′ is a node-shape match on a constructor's first statement, its
       parameter count, and (for the no-stem case) its single Return. Nothing
       else.
D-13′  PA-4′ and PA-7′(i)-(ii) are OCCURRENCE COUNTS and POSITION MATCHES over
       exactly two Names and one function. Nothing else.
D-14′  REPLACES D-14. THE ONE NEW ANALYSIS KIND, LABELLED HONESTLY (X D4).
       PA-7′(iii) performs, at each read call: (1) a SINGLE-ASSIGNMENT LOOKUP
       in the enclosing function body — take the operand Name, require exactly
       one Assign to it in that body; and (2) a ONE-HOP CALLEE-DEFINITION
       LOOKUP — resolve the RHS Call's func Name to its module-level
       FunctionDef and test that definition against PA-3′. Both indices are
       built during the same AST walk.
       IT IS NOT a taint analysis, NOT a fixpoint, NOT a transitive call graph
       — there is no edge beyond depth one and no propagation — and it
       terminates in one pass. It is nevertheless MORE than the pure
       name/position matching of S-25a..S-25m AND MORE THAN AN INTRA-FUNCTION
       LOOKUP, and v2.2's description of it as "a local index over one
       function's own statements ... NOT interprocedural" IS WITHDRAWN AS
       INACCURATE.
       PA-7′ DOES NOT RELY ON S-4. It states its own exactly-once requirement,
       so it is sound in the peer root whatever S-4's scope. v2.2's citation of
       S-4 as the uniqueness ground is replaced by this sentence.
D-15′  THE WHOLE OF S-25a..S-25p REMAINS A SINGLE AST WALK OVER THE FIVE ROOTS,
       with one per-function assignment index and one module-level definition
       index built during that walk, plus — for S-25p — a node-order check
       inside each read's enclosing function. No taint engine, no fixpoint, no
       unrestricted interprocedural analysis, and no ban on unrelated
       filesystem access is introduced.
```

---

## §4. Repair F — pathname is not provenance, and the consequence is contained

### §4.1 `PT-1′` — the theorem, narrowed to what it proves

```text
PT-1′  REPLACES PT-1. PINNED PATHNAME DENOTATION IS SYNTACTICALLY DECIDED.
       CLAIM, AND NOTHING BEYOND IT: in the five production roots, the ONLY
       expressions that can DENOTE a pathname under
       successor/officina/runtime/T_PROCESS_CLAIMS/ or under
       successor/officina/runtime/T_ACTIVE_LEASES/ are the Names claim_path and
       lease_path, and the only reads of those Names are MS-2's three
       enumerated call sites.
       THIS IS A THEOREM ABOUT PATHNAME CONSTRUCTION. IT IS NOT A THEOREM ABOUT
       BYTES, INODES, DESCRIPTORS OR CONTENT.

       PROOF, unchanged in structure, by exhaustion over the syntactic forms a
       path operand may take under PA-5′ and PA-2:
       case 1  The Name is claim_path or lease_path. By PA-4′ it occurs only at
               its enumerated uses. CLOSED by position.
       case 2  The Name is bound by a PC-N constructor. By PA-1′ that
               constructor's root Constant contains neither pinned substring;
               by PA-2 its only other operands are Constants and its own stem;
               by PA-3′ the stem contains no "/", "\\", ".." or leading "."
               — so no PC-N result NAMES a path under either pinned root, and
               none traverses into one. CLOSED by spelling.
       case 3  The Name is bound by something that is not a path constructor.
               By PA-7′(iii) such a read call is a static violation outright.
               CLOSED by absence.
       case 4  The operand is a Constant. By PA-5′(b) it contains neither
               pinned substring, so it does not name either root; by PA-1′ any
               Constant that did would already be a static violation.
               CLOSED by spelling.
       case 5  The operand is not a plain Name or an admitted Constant at all.
               By PA-5′ it is a static violation. CLOSED by shape.

COROLLARY 1′ REPLACES COROLLARY 1. Every byte string obtained IN THE FIVE ROOTS
       BY READING A PATHNAME UNDER EITHER PINNED ROOT is produced by MS-2's
       read and, by PA-8, binds immediately and only to a carrier Name.
       WITHDRAWN: v2.2's "every byte string that is the canonical serialization
       of a durable claim or occupant is produced by MS-2's read". A pathname
       theorem cannot establish that, because CA-1..CA-5 supply routes by which
       canonical claim or lease bytes arrive at a NON-pinned pathname. CR-1's
       class "however obtained" is closed for those routes by the GATE of §4.3,
       not by PT-1′.
COROLLARY 2′ REPLACES COROLLARY 2. M-R4′ is decidable because its producer set
       is five enumerated sites AND, by PT-1′, the pinned-path route to a
       governed mapping is MS-2 -> MS-3 with every site enumerated and both
       paths pinned, AND, by PG-1..PG-7, every other path's route to a
       claim- or lease-shaped object terminates in dominant invalidity before a
       mapping is bound. WITHDRAWN: any reading in which the four (now five)
       producers are "the only expressions that yield a claim or lease
       mapping" BY PATH SPELLING ALONE.
COROLLARY 3′ REPLACES COROLLARY 3. list(m.values())[5] on a laundered fresh
       mapping is unreachable in the five roots: for a pinned pathname because
       m cannot exist (PA-9′(d)); for any other pathname because the gate
       routes claim- and lease-shaped content to invalidity BEFORE m is bound
       (PG-5), so m is not reached rather than not existing.
D-8′   UNCHANGED, with its anchor now reading PT-1′ and PG-1..PG-7 jointly.
```

### §4.2 `CA-1`..`CA-5` — the external content-alias residual class, named once

```text
CA-0   THE FACT, STATED PLAINLY. A PATHNAME DOES NOT DETERMINE ITS CONTENT. No
       static analysis of source code can decide what bytes a name will resolve
       to at run time. Every rule in §2 and §3 is a statement about SOURCE; the
       members below are statements about the FILESYSTEM. v2.2 named one of
       them and mis-disposed it; v2.3 names all of them and contains their
       consequence instead of denying their existence.
CA-1   PLANTED SYMLINK. An actor outside the five roots makes a permitted PC-N
       pathname a symbolic link to a process claim or an active lease. ORDINARY
       open(path, "rb") FOLLOWS IT. v2.2's disposition — that omitting a
       follow_symlinks keyword prevents this — IS WITHDRAWN AS FALSE.
CA-2   HARD LINK. An actor gives the claim's or lease's inode a second,
       permitted name. PA-1′..PA-9′ inspect path syntax and are blind. SO IS
       samestat: A HARD LINK IS THE SAME INODE, so (st_dev, st_ino) equality
       cannot distinguish it. Only a link-count conjunct can.
CA-3   DESCRIPTOR ALIAS. A live descriptor for a pinned-root object is named
       through /proc/self/fd/<N>. S-13 keeps such paths exact constants and
       PA-5′(b) admits them, so the path rules cannot reject the read; only the
       content gate can.
CA-4   COPIED BYTES. Byte-identical canonical claim or lease content is placed
       at a permitted PC-N pathname on an ordinary single-link inode. NO PATH,
       SYMLINK, LINK-COUNT OR samestat TEST DISTINGUISHES IT. Only a schema
       discriminator can.
CA-5   RENAME, BIND-MOUNT AND EQUIVALENT NAMESPACE SUBSTITUTION. The same
       inode or the same bytes appear under a permitted name by an operation no
       source rule can observe.

CA-R1  THIS IS ONE RESIDUAL CLASS WITH ONE CONTAINMENT, NOT FIVE PROBLEMS.
       Every member has the same shape — restricted content arrives at an
       unpinned pathname — and the same containment: PG-1..PG-7 at read time,
       and dominant invalidity before any value binding.
CA-R2  THE RESIDUAL IS NOT CLOSED AND IS NOT CLAIMED TO BE. An actor with
       same-UID filesystem power can perform every one of CA-1..CA-5, and no
       sentence in this packet prevents it. What IS closed is the GOVERNANCE
       CONSEQUENCE: such content cannot become an ordinary peer mapping, a
       bound value, a record, a comparison, a resource fact or a scientific
       fact. WL-4′(b)'s observation that the actor already holds kernel power
       remains true AND IS NOT A DISPOSITION OF THIS RESIDUAL — the Y line is
       right that admitted kernel power does not make interference a valid
       Officina fact.
```

### §4.3 `PG-1`..`PG-7` — the read gate, grounded in the signed discipline

```text
PG-1   SCOPE. PG-2..PG-7 apply to EVERY read call in the five production roots
       that reads a durable file's content — that is, MS-2's three pinned-path
       reads and every PC-N content read. They do not apply to write calls
       (PA-6′), to the three /proc/self/fd ENUMERATIONS of S-18, or to a stat
       that binds no content.
PG-2   NO-FOLLOW, BY FLAG AND NOT BY OMISSION. The read is descriptor-anchored:
       it opens with the no-follow flag Constant the signed chain already uses
       — O_NOFOLLOW together with O_RDONLY and O_CLOEXEC, as at composite
       :905-917 and :1006-1020 for the P1 roots and protocol :58-72 for the
       runtime artifacts — and reads THROUGH THE HELD DESCRIPTOR. A read that
       opens by pathname without the flag Constant is a static violation.
PG-3   THE FOUR CONJUNCTS, CHECKED ON THE HELD DESCRIPTOR BEFORE ANY CONTENT IS
       READ. Immediately after the open, on that descriptor:
         (a) REGULAR FILE. fstat's type is S_ISREG — not a symlink, directory,
             FIFO, socket, device or door. This is the discipline of composite
             :848-849 and :1006-1014, applied to durable record reads.
         (b) LINK COUNT. st_nlink == 1. THIS CONJUNCT IS THE ONE MEMBER OF THE
             GATE THAT THE LIVE SIGNED TIER DOES NOT ALREADY STATE: protocol
             §B's samestat discipline cannot supply it, because CA-2's hard
             link is the same inode. The same rule exists in the superseded
             control-channel chain as provenance
             (…CONTROL_CHANNEL_V2_DRAFT.md:529, :539, "Accept only regular
             files, nlink==1"; "Hardlinks (nlink≠1) refused before read"),
             which is authority level 3 and is cited as evidence that the
             framers reached the same conclusion, NOT as authority. It is
             counted as a new requirement at B-A8.
         (c) PATH IDENTITY. The (st_dev, st_ino) of the held descriptor equals
             the (st_dev, st_ino) of the pathname it was opened by, checked
             without releasing the descriptor — protocol §B's held-file-
             descriptor samestat discipline, and composite p-2/A-6/A-11's
             "require (st_dev, st_ino) of self_fd == ...".
         (d) ANCHOR. For the runtime artifacts protocol §B names, the read
             occurs inside the held T_RUNTIME.lock sequence, with anchor
             validation, exactly as contract :190-200 fixes. This packet adds
             nothing to that clause and repeats it so the gate is read as one
             discipline.
       ANY CONJUNCT FAILING ROUTES TO DOMINANT FILESYSTEM INVALIDITY BY PG-5.
PG-4   THE PATH-BOUND EXACT-SCHEMA DISCRIMINATOR. After PG-3 and BEFORE the
       bytes are parsed into a mapping that any ordinary consumer may touch,
       before they are returned from the reading function, and before any value
       of the parsed object is bound to a Name, the read establishes that the
       object's `schema` value is EXACTLY the schema value that the PATH FAMILY
       fixes:
         - a pathname under the pinned claims root  ⇒ exactly
           philosophia.officina.t-process-claim.v1
         - a pathname under the pinned leases root  ⇒ exactly
           philosophia.officina.t-active-lease.v1
         - any PC-N pathname                        ⇒ exactly the schema value
           its own owning contract fixes for that path, AND NEITHER OF THE TWO
           ABOVE.
       The discriminator reads the single key "schema" by literal subscript and
       binds no other value. It is not a validation (MS-10 is) and it is not a
       parse of the record for use; it is a one-key admissibility test.
PG-5   DOMINANT INVALIDITY, BEFORE VALUE BINDING. If a PC-N read yields an
       object whose schema is t-process-claim.v1 or t-active-lease.v1, or
       yields bytes that are the canonical serialization of either — the case
       CA-4 supplies, caught here because the discriminator is PATH-BOUND and
       not merely schema-bound — then the read routes RECORD-FIRST to the
       filesystem/process invalidity disposition of §P1-11.6 and §P1-13.5
       (composite :1849-1866, :2323-2330), with invalidity DOMINANT, BEFORE any
       mapping is bound, any value is read, any comparison is made and any
       consumer sees it. It is NEVER treated as an ordinary peer mapping, and
       it is NEVER a completion, a capacity fact, a custody disposition, a
       spend fact, a comparison, a datum, an outcome or a Proof. This is P-R5's
       existing dominance applied at the read boundary; it creates no new
       disposition and no new cause class.
PG-6   NO EXEMPTION AND NO FALLBACK. The gate has no bypass flag, no cached
       result, no "trusted path" list, no retry that proceeds on failure, and
       no branch in which content is bound before PG-3 and PG-4 complete. A
       reading function containing a statement that binds, returns, parses,
       logs, formats or compares the content lexically before the gate's
       statements is a static violation.
PG-7   WHAT THE GATE DOES NOT DO. It does not prove that the bytes are the
       bytes some other actor wrote; it does not detect a substitution that
       preserves the path family's own schema; it does not make CA-1..CA-5
       impossible; and it does not claim inode identity across time. It
       establishes exactly this: NO CLAIM- OR LEASE-SHAPED CONTENT ENTERS AN
       ORDINARY CONSUMER IN THE FIVE ROOTS THROUGH ANY PATHNAME, and every
       alias route terminates in dominant invalidity instead.
```

### §4.4 The rule

```text
S-25p  NEW. PC-N AND PINNED-PATH READ GATE, ALL FIVE PRODUCTION ROOTS.
       PG-1..PG-7 hold: every durable content read opens with the no-follow
       flag Constant and reads through the held descriptor; the four PG-3
       conjuncts appear, in that order, lexically before any content-binding
       statement in the same function body; the PG-4 discriminator appears
       lexically before any parse, return or value binding; the PG-5 invalidity
       route is the only successor of a failing conjunct or a mismatched
       schema; and no bypass, cache, fallback branch or early binding exists
       ⇒ "S-25p: durable read without the no-follow, regular-file, link-count,
          path-identity and path-bound schema gate, or content bound before it"
       RECOGNITION: node-shape match on the open call's flag Constant, presence
       and ORDER of the enumerated statements inside one function body, and a
       successor check on the failing branch. This is the same intra-function
       node-order discipline PA-3′ already uses for the stem grammar check. No
       taint, no fixpoint, no transitive analysis.
S-25n′ REPLACES S-25n. IDENTITY-BEARING PATH AND READ ANCHORING, ALL FIVE
       PRODUCTION ROOTS. PA-1′..PA-9′ hold: each pinned root literal occurs
       exactly once, at MS-1 and MS-1L; every path-building expression occurs
       inside a path constructor over Constants and a grammar-checked stem, or
       is a no-stem constructor's Constant; every read call's path operand is a
       plain Name or an admitted Constant; claim_path and lease_path occur only
       at their enumerated uses; the pinned reads occur only inside MS-2 at its
       three enumerated call sites; MS-2's bytes bind immediately and only to a
       carrier Name; and json.loads/json.load take a plain-Name operand, with a
       carrier operand only at MS-3
       ⇒ "S-25n: identity-bearing record path or read outside its anchored
          site"
```

### §4.5 What Repair F does not claim

```text
F-N1  IT DOES NOT ENUMERATE THE PEER RECORD SET. PG-4's third bullet defers to
      "the schema value its own owning contract fixes for that path". This
      packet names two schema values — the two it owns — and no others.
F-N2  IT CREATES NO DURABLE SCHEMA, NO PRODUCTION ROOT, NO DESTINATION, NO
      AUTHORITY CELL AND NO INVALIDITY CAUSE. PG-5 routes to the EXISTING
      disposition at the EXISTING loci.
F-N3  IT DOES NOT BAN UNRELATED FILESYSTEM ACCESS. R-a..R-f are asserted to
      pass; the gate adds statements to a read, it does not remove a read.
F-N4  IT CLAIMS NO IMPOSSIBILITY. CA-R2 states the residual survives. The
      packet's assertion is about what a CONFORMING IMPLEMENTATION does with
      aliased content, which is: refuse it, record-first, before use.
```

---

## §5. Repair G and H — the third evaluation, and the honest information statement

### §5.1 `EV-3` — the lease-integrity evaluation

```text
EV-3   NEW. THE LEASE-INTEGRITY EVALUATION.
       OPERAND: the canonical byte string MS-6 (ACC-4) produces for a lease, or
         the byte string MS-2 reads from the durable lease path, over a
         lease_mapping that has passed complete canonical validation at MS-10
         against the exact key set of protocol :241-246.
       SITE: MS-7 (ACC-5), lease call site.
       RESULT: active_lease_sha256, 64 lowercase hex.
       AUTHORITY: contract :116-124 and batch :93-97, which REQUIRE it. This
         packet does not create it, does not choose it, and cannot remove it.
       LOCATION: inside the five production roots, in generic_harness.py, as
         §1.4 determines from the signed bytes.
       DESTINATIONS: the settlement, charge-event, batch and capacity fields
         that the generic-harness contract §2c.5 and the batch settlement
         amendment already fix. THIS PACKET NEITHER CREATES, ENUMERATES NOR
         CONSTRAINS THEM (LD-R1).
       LIFETIME: persistent, by signature.

EV-R1′ REPLACES EV-R1. THESE ARE THE ONLY THREE EVALUATIONS. A fourth ACC-5
       evaluation, at any site, over any operand, is a static violation by
       count (S-25m″).
EV-R2  UNCHANGED. ACC-5 IS STILL ONE ACCESSOR, DEFINED ONCE (ACC-R4, MS-R1).
       Three evaluations of one accessor is what the specification now says.
EV-R3′ REPLACES EV-R3. ALL THREE EVALUATIONS ARE PRECONDITIONED ON VALIDATION.
       EV-1 on MS-10 over claim_mapping; EV-2 on MS-10 over occupant_mapping
       plus X-2 and X-3; EV-3 on MS-10 over lease_mapping. None may be invoked
       before its precondition returns true (DC-7), and no digest is computed
       over an unvalidated record.
EV-R4  NEW. THE THREE EVALUATIONS ARE PAIRWISE DISJOINT IN OPERAND AND SITE.
       EV-1's operand is the installing claim's carrier; EV-2's is the
       occupant's carrier; EV-3's is a lease carrier. No operand is shared and
       no call site is shared. EV-1's and EV-2's operands, sites,
       preconditions, destinations and confinement are UNCHANGED IN EVERY
       PARTICULAR, and nothing in Repair G reopens them.

C-6    NEW. THE SIXTH PERSISTENT CONSUMER — the active-lease canonical
       integrity digest.
       KEYS READ INDIVIDUALLY: NONE. The operand is a whole validated carrier;
         ACC-R5 forbids any Subscript, slice, decode, split, regex, loop,
         comprehension, format or branch over it, so no identity field is bound.
       OPERATION: ACC-4 then ACC-5 (EV-3), over the whole record.
       DESTINATION: the signed settlement fields named above.
       SIGNED AUTHORITY: contract :116-124; batch :93-97.
       WHY IT IS A CONSUMER AND NOT A NEW POWER: it is the exact shape v2.1
         recognized when it added C-5 — a record-level whole-object consumer
         that binds neither identity key and therefore escaped C-1..C-4. v2.1
         found one such consumer and stopped; v2.3 finds the second and names
         it. P-R1's "C-1..C-n is the complete list" now reads C-1..C-6.

C-5″   REPLACES C-5's OPERATION and FORBIDDEN clauses. Its PRECONDITION, KEYS
       READ INDIVIDUALLY and DESTINATIONS blocks carry forward verbatim.
       OPERATION. ACC-5 (MS-7) IS THE SOLE SHA-256 ACCESSOR OVER A CARRIER, AND
       IT HAS EXACTLY THREE AUTHORIZED EVALUATIONS: EV-1, EV-2 AND EV-3.
         EV-1 yields the raw claim lineage digest, whose direct persistent
           destinations are EXACTLY TWO, D-1 and D-2, AND NO THIRD. THIS COUNT
           IS UNCHANGED BY EV-3, because a lease digest is a digest of a
           different object and is not the claim lineage value.
         EV-2 yields a transient digest consumed only by the X-4 boolean.
         EV-3 yields active_lease_sha256, whose destinations are peer-owned and
           signed.
       WHAT IS EXACTLY ONE: one accessor definition (ACC-R4); one declassifying
         operation (DC-1″); one raw CLAIM lineage digest value.
       WHAT IS EXACTLY TWO: the direct persistent destinations of the claim
         lineage digest (D-1, D-2); the persistent digest VALUES (the claim
         lineage digest and the lease integrity digest).
       WHAT IS EXACTLY THREE: the authorized evaluations; the ACC-5 call sites.
       FORBIDDEN, AMENDED — v2.2's clause is replaced:
         WAS  "any digest evaluation other than EV-1 and EV-2; any truncated
               digest, keyed digest, HMAC, checksum, fingerprint, shortened
               form or numeric projection of a claim, a lease, an occupant, or
               of either digest"
         IS   any digest evaluation other than EV-1, EV-2 and EV-3; any
              truncated digest, keyed digest, HMAC, checksum, fingerprint,
              shortened form or numeric projection of a claim, a lease, an
              occupant, or of any of the three digests
       and the v2.2 ADDED clause confining EV-2 stands verbatim.

DC-1″  REPLACES DC-1′. MODEL, SINGLE-OPERATION AND HONESTLY COUNTED.
       ACC-5 is THE SOLE NAMED DECLASSIFYING OPERATION from
       RESTRICTED_PROCESS_IDENTITY and RESTRICTED_CLAIM_CANONICAL_BYTES. There
       is exactly ONE such operation, at exactly one site (MS-7), accepting
       exactly one operand shape (a validated complete canonical carrier), with
       exactly THREE AUTHORIZED EVALUATIONS, of which TWO produce persistent
       values — EV-1's, with exactly two direct destinations, and EV-3's, whose
       destinations the peer contracts own.
       DECLASSIFICATION HERE MEANS RELEASE FROM THE RESTRICTED FIELD CLASS AND
       NOTHING ELSE. IT IS NOT CONFIDENTIALITY DECLASSIFICATION, BECAUSE THIS
       CELL SUPPLIES NO CONFIDENTIALITY GUARANTEE TO RELEASE (CS-4′, WL-3″).
       The alternative model remains REJECTED for v2.1 §3.5's and §3.6's
       reasons, which both final lines accepted at every round.

DC-6″  REPLACES DC-6′. DIGEST INVENTORY, COMPLETE AND AUDITED.
       Exactly three digest VALUES are derived from a carrier in the five
       roots:
         (i)   EV-1's raw claim lineage digest — persistent, two direct
               destinations;
         (ii)  EV-2's transient occupant digest — no destination, one boolean
               consumer, confined by OD-1..OD-4 and S-25o;
         (iii) EV-3's active_lease_sha256 — persistent, destinations owned and
               required by the signed peer contracts.
       NO OTHER digest, checksum, fingerprint, truncated form, keyed form, HMAC
       or numeric projection of a claim, a lease, an occupant or of any of the
       three exists in the five roots.
       THE v2.2 SENTENCE — "NO OTHER digest ... of a claim, a LEASE, an
       occupant ... exists in the five roots" — IS WITHDRAWN AS FALSE ON THE
       SIGNED BYTES. It was contradicted by contract :116-124 at every
       heartbeat, and the audit at §1.4 establishes the contradiction rather
       than assuming it.

S-25e″ REPLACES S-25e′. persistent-consumer closure: the returns of ACC-2/ACC-3
       are unpacked only at the C-3, C-4 and X-3 comparison sites, each
       unpacked Name occurring exactly once inside its comparison and each
       yielding a boolean; ACC-5's return AT ITS LINEAGE SITE (EV-1) is
       consumed only at D-1 and D-2; AT ITS OCCUPANT SITE (EV-2) occurs exactly
       once as one operand of the single X-4 equality; and AT ITS LEASE SITE
       (EV-3) is consumed only at the signed settlement fields its owning
       contracts fix, and in no addressing, selection, signalling, waiting,
       process-control, request-builder, handle, journal-key, retry-key,
       qualification, blinding, Q, C, scientific datum, evidence, outcome or
       Proof expression
       ⇒ "S-25e: restricted identity value or record digest used outside a
          whitelisted position"
S-25l″ REPLACES S-25l′. DIGEST DESTINATION CLOSURE. EV-1's value reaches exactly
       D-1 and D-2 and no third direct destination; EV-3's value reaches only
       the settlement fields its owning contracts fix; neither appears in any
       addressing, selection, signalling, waiting, process-control,
       request-builder, handle, journal-key, retry-key, capacity-as-observation,
       custody, qualification, blinding, Q, C, scientific datum, evidence,
       outcome or Proof expression, and no numeric value is derived from
       either. EACH MAY APPEAR IN EXACTLY THE INTEGRITY COMPARISONS THE SIGNED
       CHAIN REQUIRES — for EV-1 the X-4 conjunct and the containing-object
       hashing and verification of L-1..L-5; for EV-3 the settlement equality
       and continuity checks its owning contracts require — and in no other
       comparison
       ⇒ "S-25l: a record digest reaches an unauthorized destination or an
          unauthorized comparison"
S-25m″ REPLACES S-25m′. COUNT CLOSURE. The five roots contain exactly five
       accessor definitions (ACC-1..ACC-5), exactly SIX persistent consumers
       (C-1..C-6), exactly three governed mapping Names (M-R3), exactly FIVE
       carrier Names (CR-2′), exactly FIFTEEN approved call-site rows (§2.4),
       exactly TWO pinned root literals and TWO pinned path Names (PA-1′,
       PA-4′), exactly ONE read function with THREE call sites (PA-7′), exactly
       TWO write calls (PA-6′), exactly THREE ACC-5 evaluations (EV-1, EV-2,
       EV-3), exactly TWO persistent digest values, exactly TWO direct
       persistent destinations of the claim lineage digest (D-1, D-2), and
       exactly ONE declassifying operation. Each count is asserted as a number,
       so an addition fails by arithmetic rather than by review
       ⇒ "S-25m: accessor, consumer, governed-name, carrier, call-site,
          evaluation, pin or destination count changed"
```

### §5.2 `LD-1`..`LD-3` — the lease digest's status, classified rather than enumerated

```text
LD-1   IT IS NOT A THIRD DIRECT DESTINATION OF THE CLAIM LINEAGE DIGEST. The
       lease does not contain process_claim_sha256 (protocol :241-246 is the
       claim key set plus five, and the claim does not carry its own digest), so
       active_lease_sha256 is a digest OF A DIFFERENT OBJECT and D-1/D-2's
       count is untouched. The Y line established this independently at its
       §3.1 and it is re-derived here.
LD-2   IT IS NOT A TRANSITIVE CONTINUATION OF L-1..L-5 EITHER. L-0's
       continuations are objects CONTAINING the claim lineage digest. The lease
       does not contain it. EV-3 is a PARALLEL lineage, named separately, and
       L-1..L-5 are left exactly as written.
LD-3   ITS DESTINATIONS ARE PEER-OWNED. This packet neither creates,
       enumerates, constrains nor renames them. What it requires is only that
       the value be produced at MS-7 over a whole validated carrier, that it
       bind no identity field (ACC-R5), and that S-25l″'s sink ban apply to it
       exactly as to EV-1's value. L-R1's one-question test extends unchanged:
       DOES THIS FIELD'S VALUE EQUAL A RAW RECORD DIGEST? If it is the claim
       lineage digest in a new field, it is a forbidden third destination
       (L-R2). If it is active_lease_sha256 in the fields its owning contract
       fixes, it is the signed operation. If it is anything else, it needs its
       own bounded correction.
```

### §5.3 The conditional information statement — `CS-4′`, `WL-3″`, `CS-8`

```text
CS-4′  REPLACES CS-4. THIS CELL SUPPLIES NO CONFIDENTIALITY GUARANTEE.
       [ACU] Officina neither provides nor authorizes reliance on any
       confidentiality property of process_claim_sha256, of active_lease_sha256,
       or of any containing lineage hash of L-1..L-5. No rule, record, decision,
       datum or Proof in this chain may rest on the digest concealing anything.
       [IP] What is PROVED about recovery is conditional and is stated with its
       condition every time it is stated:
         (a) FOR A READER WHO KNOWS THE OTHER EIGHTEEN CANONICAL CLAIM FIELDS,
             recovery of the identity pair is practical by enumeration over AT
             MOST 4,194,304 candidates (CS-2), because A-P4c forces
             attested_pgid == attested_pid for the leader case this contract
             installs and PID_MAX_LIMIT = 4194304.
         (b) FOR A READER OF THE CLAIM, THE LEASE OR THEIR ARCHIVE, no search
             is needed at all: both integers are present in cleartext
             (protocol :231-238, :241-246; the archival sets stage the claim
             itself, protocol :85-97, L-4).
         (c) FOR A READER WHO HOLDS ONLY A DIGEST, OR ONLY A CONTAINING LINEAGE
             HASH, AND NOT THE CONDITIONING FIELDS, THIS PACKET MAKES NO CLAIM
             WHATEVER — not that recovery is feasible, not that it is
             infeasible, and not what entropy remains. THE ABSENCE OF A
             GUARANTEE IS NOT A PROOF OF EXPOSURE, AND v2.2's SENTENCE "THERE
             IS NO READER FOR WHOM THE DIGEST CONCEALS THE IDENTITY FIELDS" IS
             WITHDRAWN AS AN UNPROVED UNIVERSAL.
WL-3″  REPLACES WL-3′. THE RESIDUAL, STATED WITH ITS CONDITION.
       [IP] SHA-256 is not a confidentiality barrier for a low-entropy unknown
       WHEN THE REMAINING UNKNOWN IS LOW-ENTROPY — which is the case exactly
       when the other eighteen canonical values are known (CS-2), and the actor
       who constructs the claim already holds them (CS-3), and the actor who
       reads the claim, the lease or the archive holds the integers outright
       (CS-4′(b)). THIS PACKET RESTS NO CLAIM ON PREIMAGE RESISTANCE AND
       ASSERTS NO CONFIDENTIALITY PROPERTY IN EITHER DIRECTION. v2.2's "THE
       DIGEST HAS NO CONFIDENTIALITY PROPERTY" IS WITHDRAWN: the defensible
       statement is CS-4′'s, that no confidentiality guarantee is supplied or
       relied upon, and no sentence in v2, v2.1, v2.2 or v2.3 may be read as
       asserting either a guarantee or its universal absence.
CS-8   NEW. PROPAGATION THROUGH THE LINEAGE, STATED CONDITIONALLY (Y §3.2).
       [IP] A containing lineage hash of L-1..L-5, and active_lease_sha256
       (EV-3), inherit THE SAME CONDITIONAL CHANNEL AND NO OTHER: a reader who
       knows the other canonical fields of the claim AND the other fields of
       the containing object can run the same enumeration against the
       containing hash. A reader who does not know those fields is outside
       every claim this packet makes (CS-4′(c)).
       [ACU] NOTHING IN CS-8 AUTHORIZES ANYTHING. The conditional channel is
       not a permitted use, not evidence, not a datum and not a selector. Every
       prohibition of DC-4′, S-25l″, WL-R1 and P-R4 applies to a value
       recovered or inferred from ANY of these hashes exactly as it applies to
       one recovered from the claim digest, through class member (f).
CS-7   UNCHANGED AND STILL GOVERNING, with one clause read through CS-4′: "It
       is not confidentiality-preserving" is to be read as "this cell supplies
       and authorizes no confidentiality guarantee", which is what it was
       adopted to mean.
```

**What Repair H does not weaken.** `DC-3′`, `DC-4′`, `DC-5′`, `WL-1`, `WL-2`,
`WL-4′`, `WL-R1`, `DC-2`, `DC-7`, `P-R4`, `P-R5`, class member `(f)`,
`CS-P1`..`CS-P7`, `N-3` and every sink prohibition are **unchanged in text**. The
bans on process-control, addressing, selection, signalling, waiting, resource,
capacity, custody, spend, settlement-as-authorization, qualification, blinding,
`Q`/`C`, scientific datum, observation, evidence, outcome and Proof use stand
verbatim, and now cover `EV-3`'s value and every containing hash by `S-25l″` and
`CS-8`.

---

## §6. Amended counts, blast radius, and handoff

### §6.1 The count table, re-derived after the lease closure

| Quantity | v2.1 | v2.2 | **v2.3** |
|---|---|---|---|
| persistent consumers | 5 | 5 | **6 — `C-1`..`C-6`** |
| centralized accessors | 5 | 5 | **5** (unchanged) |
| verifier rules added by Option A | 13 | 15 | **16 — `S-25a`..`S-25p`** |
| behavioural tests added by Option A | 17 | 21 | **26 — `A-T1`..`A-T26`** |
| governed mapping Names | 3 | 3 | **3** (unchanged) |
| carrier Names | 3 | 3 | **5** (`CR-2′`) |
| approved call-site rows | 12 | 12 | **15** (`MS-1`, `MS-1L`, `MS-2`..`MS-14`) |
| governed mapping producers | 4 | 4 | **5** (`M-R4′`) |
| pinned root literals | — | 1 | **2** (`PA-1′`) |
| pinned path Names | — | 1 | **2** (`claim_path`, `lease_path`) |
| path constructors for pinned roots | — | 1 | **2** (`MS-1`, `MS-1L`) |
| read functions / call sites | — | 1 / 2 | **1 / 3** (`MS-2`; verify, `MS-11`, `MS-14`) |
| write calls | — | not distinguished | **2** (`MS-12`, `MS-13`) |
| `ACC-5` authorized evaluations | "one" *(contradicted)* | 2 | **3 — `EV-1`, `EV-2`, `EV-3`** |
| persistent digest values | 1 implied | 1 | **2** (claim lineage; lease integrity) |
| transient digest values | unnamed | 1 | **1** (unchanged) |
| direct persistent destinations of the claim lineage digest | 2 | 2 | **2 — `D-1`, `D-2`** (unchanged) |
| transitive continuations | — | 5 | **5 — `L-1`..`L-5`** (unchanged) |
| declassifying operations | "1" | 1 | **1** (unchanged) |
| content-alias residual class | — | 1 named, mis-disposed | **5 — `CA-1`..`CA-5`, contained by `PG-1`..`PG-7`** |
| retained-behaviour fixtures | — | 4 | **6 — `R-a`..`R-f`** |
| handoff steps | 11 | 13 | **15** |
| sentences withdrawn/replaced this round | 2 | 6 | **7 — `R-W9`..`R-W15`** |

**Rule-letter arithmetic:** `S-25a`..`S-25p` is sixteen letters; `S-25p` is the
one added and `S-25n′` the one replaced. **Test arithmetic:** `21 + 5 = 26`,
mapping to handoff test rows 92–117.

### §6.2 Amendments to the blast radius

```text
B-A1″  §5.4 "verifier: S-25a-S-25o (fifteen rules)"
         BECOMES  S-25a-S-25p (SIXTEEN rules, up from four)
B-A2″  §5.4/§5.5 "tests: A-T1-A-T21 (twenty-one)"
         BECOMES  A-T1-A-T26 (TWENTY-SIX)
B-A3″  §5.4 supervisor code line ADDS: a second pinned path constructor, a
       second durable write site, a lease load site, two further carrier Names,
       and a descriptor-anchored read shape for both pinned families
B-A4   §5.5 items (i), (ii) UNCHANGED; (iii) UNCHANGED IN KIND AND WIDENED IN
       DOMAIN: the path-spelling and read-operand discipline now covers two
       pinned families and admits constant paths, so it constrains the same
       surface with one more pin and one fewer false rejection
B-A8   NEW. THE READ GATE IS A REAL COST TO EVERY DURABLE READ IN THE FIVE
       ROOTS (PG-1..PG-7). Three of its four PG-3 conjuncts and its no-follow
       flag are ALREADY REQUIRED by protocol :58-72 and contract :190-200 for
       the runtime directory, ledger, head, state cache, claim, lease and
       process record — so for those artifacts the gate IMPORTS a signed
       requirement that v2.1's MS-2 row had silently dropped, and costs
       nothing new. What IS new is (a) the st_nlink == 1 conjunct, which the
       live tier does not state and which CA-2 shows samestat cannot supply,
       and (b) the extension of the whole discipline to PC-N records the signed
       chain does not name. Both are counted here as one item and neither is
       hidden inside (iii).
B-A5″  §5.8 "new residual", Option A — REPLACES B-A5′:
         the record digests are SEARCHABLE FULL-RECORD COMMITMENTS. THIS CELL
         SUPPLIES NO CONFIDENTIALITY GUARANTEE for them or for any containing
         lineage hash. FOR A READER WHO KNOWS THE OTHER EIGHTEEN CANONICAL
         FIELDS the identity pair is recoverable by enumeration over at most
         4,194,304 candidates; the constructing supervisor holds those fields;
         and a claim, lease or archive reader holds the integers in cleartext.
         FOR A READER WITHOUT THOSE FIELDS NO CLAIM IS MADE IN EITHER
         DIRECTION. They transfer NO capability and NO authorization (WL-4′,
         CS-6), and NO Officina act may rest on them outside record integrity
         and lineage (WL-R1).
B-A9   NEW. AND SEPARATELY DISCLOSED: the EXTERNAL CONTENT-ALIAS RESIDUAL
       (CA-1..CA-5) is not closed and is not claimed to be. Its governance
       consequence is contained by PG-1..PG-7 and P-R5's dominance.
B-A6   UNCHANGED AND NOT RE-PRICED: signed sentences amended (1); peer-owned
       durable record schemas superseded (0 for A, 2 for B); new durable
       schemas (0); signed validity predicates reopened (0 for A);
       architectural rules inverted (0 for A); wire grammar changed (1 response
       grammar, no request grammar); durable formats changed (1 — P1's own J4);
       collision/idempotency rules changed (1 — EEXIST X-1..X-4); migration
       (none); SELECTABLE TODAY: A yes, B NO.
B-A7   OPTION B'S CORRECTED COUNT IS UNTOUCHED. B remains NON-SELECTABLE behind
       sub-cells B-1 and B-2, for authority reasons and not size reasons.
```

### §6.3 Amendments to the handoff

```text
STEP 5 AMENDED AGAIN. "...and — new in v2.3 — the second pinned family with
  MS-1L/MS-13/MS-14, CR-2′'s five carriers, M-R4′'s five producers, the read
  gate PG-1..PG-7 with the content-alias class CA-1..CA-5, the third evaluation
  EV-3 with the sixth consumer C-6 and LD-1..LD-3, and CS-4′/WL-3″/CS-8, as a
  new subsection of §P1-13."
STEP 6 AMENDED AGAIN. "...adds S-25a...S-25p to §P1-14.6 CHANGE 3 and updates
  the edit surface from S-1...S-24b to S-1...S-25p."
STEP 7 AMENDED AGAIN. "...adds A-T1...A-T26 as test rows 92-117."
STEPS 11, 12, 13 UNCHANGED.
STEP 14 NEW. "...records the §1.4 AUDIT as a finding of fact on the signed
  bytes: active_lease_sha256 is evaluated inside the five production roots, in
  src/philosophia/officina/generic_harness.py, on the joint authority of
  contract :576, :517-522, :505-514 and composite :349-357; therefore EV-3 and
  C-6 exist, and any future document asserting a two-evaluation or
  five-consumer world is contradicted by this record."
STEP 15 NEW. "...records that PT-1′ is a PATHNAME theorem only; that
  CA-1..CA-5 are an OPEN external residual; that PG-1..PG-7 contain their
  governance consequence and do not close them; and that no future contract may
  cite this cell as authority for the proposition that claim or lease bytes can
  reach a reader only through MS-2."
STEPS 1, 2, 3, 4, 8, 9, 10 ARE UNCHANGED.
```

---

## §7. Tests added and amended by v2.3

`A-T1`..`A-T17` are unchanged in text; `A-T9′`'s amended assertion stands with
`S-25n′` substituted for `S-25n`. `A-T18`..`A-T21` are unchanged except that
`A-T19`'s retained-behaviour list becomes `R-a`..`R-f` and `A-T20`'s positive
case admits the third evaluation.

```text
A-T22  NEW. THE LEASE-REOPEN COUNTEREXAMPLE, EXACT. The X line's lease
       construct is included VERBATIM as a build fixture:
           lp     = _lease_path(process_id)
           raw    = open(lp, "rb").read()
           m      = json.loads(raw)
           vals   = list(m.values())
           leaked = vals[5]
       and is asserted REJECTED STATICALLY with S-25n′ named, AT THE FIRST LINE
       and not merely somewhere. The test additionally asserts rejection with
       lines 3-5 deleted, so the closure is shown to be at the PATH and the
       READ; and it asserts that the identical construct against the CLAIM path
       is still rejected, so Repair A is shown not to have regressed.

A-T23  NEW. THE LEASE VARIANT MATRIX AND THE RETAINED FIXTURES. Each of
       LV-a..LV-j is a build fixture asserted REJECTED STATICALLY with the
       named rule fired, INDIVIDUALLY. AND R-a..R-f are asserted to PASS,
       including R-e (the three /proc/self/fd exact-constant enumerations) and
       R-f (a constant durable path). A build in which any of R-a..R-f fails is
       a TEST FAILURE, NOT A STRICTER BUILD.

A-T24  NEW. THREE-EVALUATION CONFORMANCE.
       (a) positive: exactly three ACC-5 evaluations exist; EV-1 runs only
           after MS-10 on claim_mapping and reaches exactly D-1 and D-2; EV-2
           runs only after the occupant independently passes MS-10, X-2, X-3
           and occurs exactly once inside X-4; EV-3 runs only after MS-10 on
           lease_mapping and reaches only the settlement fields its owning
           contracts fix;
       (b) negative, each rejected statically with the named rule asserted:
             a fourth ACC-5 evaluation at any site            S-25m″
             a digest over an unvalidated lease               DC-7 / EV-R3′
             EV-3's value in any addressing, selection,
               signalling, process-control, Q/C, scientific
               or Proof expression                            S-25l″
             EV-1's value reaching any third destination      S-25l″ / L-R2
             a numeric value derived from any digest          S-25l″
       (c) the count assertions of S-25m″ are asserted AS NUMBERS: five
           accessors, SIX consumers, three governed Names, FIVE carriers,
           FIFTEEN call-site rows, TWO pins, ONE read function with THREE call
           sites, TWO write calls, THREE evaluations, TWO persistent digest
           values, TWO direct destinations, ONE declassifying operation. Adding
           any one fails S-25m″ BY ARITHMETIC and the test asserts that
           specific failure.

A-T25  NEW. THE CONTENT-ALIAS NEGATIVES — asserted as RUNTIME dispositions, not
       as static impossibilities, which is the whole point of Repair F:
         (a) PLANTED SYMLINK. A permitted PC-N pathname is made a symlink to a
             process claim. ASSERTED: the read refuses at PG-2/PG-3(a),
             routes to dominant filesystem invalidity, binds no value, parses
             no mapping, and produces no record, comparison or datum.
         (b) HARD LINK. The claim inode is given a second permitted name.
             ASSERTED: refusal at PG-3(b) — and the test additionally asserts
             that a samestat-only check would have PASSED it, so the necessity
             of the link-count conjunct is demonstrated rather than assumed.
         (c) COPIED CLAIM BYTES. Byte-identical canonical claim content is
             placed at a permitted PC-N pathname on a single-link regular file.
             ASSERTED: PG-3 passes, PG-4's path-bound discriminator REFUSES,
             and PG-5 routes to dominant invalidity BEFORE any mapping is
             bound. The test asserts the ordering explicitly.
         (d) LIVE /proc/self/fd ALIAS. A descriptor for a pinned-root object is
             named through an exact-constant descriptor path. ASSERTED: the
             read is admitted by PA-5′(b) and then REFUSED by PG-4/PG-5, so the
             path rules and the gate are shown to divide the work as designed.
         (e) NEGATIVE CONTROL: an ordinary peer record at a PC-N path, of its
             own signed schema, on a single-link regular file, PASSES the gate
             and is consumed normally with .values() and .items() available.

A-T26  NEW. SATISFIABILITY, ASSERTED POSITIVELY — the defect class X D2/D3
       named must not recur silently:
         (a) the conforming MS-12 claim install PASSES; it is a write call and
             fires neither PA-5′ nor PA-7′;
         (b) the conforming MS-13 lease install PASSES;
         (c) MS-2's three call sites PASS and a fourth fails S-25n′;
         (d) the three /proc/self/fd enumerations PASS (R-e);
         (e) a no-stem constructor PASSES (PA-3′(b));
         (f) a Constant path operand containing NEITHER pinned substring PASSES
             (PA-5′(b)), and one containing EITHER fails PA-1′ — asserted as a
             matched pair, so the admission cannot drift into an exemption.
```

---

## §8. What v2.3 does not change

### §8.1 The eight findings both confirmation lines accepted as closed

| Finding | Locus that must remain intact | **v2.3 effect** |
|---|---|---|
| `X M-1` | v2 §2.8.1–§2.8.3, thirteen-key `J4`, `R-P1`..`R-P4` | **none** |
| `X m-1` | v2 §2.3 `A-P4a`..`A-P4d` | **none** — `CS-4′(a)` cites `A-P4c` without altering it |
| `X m-2` | v2 §2.2 `PID_MAX_LIMIT = 4194304`, `G-1`..`G-6`, `A-T8` | **none in substance** — cited as the size of a conditional search space |
| `X m-3` | v2 §6.1 Case 1 / Case 2 | **none** |
| `Y-C2` | v2 §2.8.2/§2.8.3 byte-identical redelivery | **none** |
| `Y-M1` | v2 §2.10.1–§2.10.4, `X-1`..`X-4`, `I-1`..`I-10` | **none in substance** — `X-1` gains a fifth carrier position only in the sense that `CR-3′(d)` is unchanged text; no matrix row, conjunct or routing changes |
| `Y-M2` | v2 §3.2, two superseded schemas | **none** — `LD-1` re-derives that the lease carries no claim digest |
| `Y-m1` | v2 §1.5 `R-1`..`R-4`; §4 | **none** |

### §8.2 The mechanism the confirmation lines confirmed sound

| Locus | Status at v2.2 | **v2.3 effect** |
|---|---|---|
| `S-25i`, `S-25i-N1`..`N4` | X: retained `open` is "the correct decision" | **none in text**; `PC-R2′` narrows only the two pinned families' read shape, on protocol §B's signed authority |
| `M-R1`, `M-R2`, `M-R3`, `M-R5`, `S-25j` + scope note | X: closes eight routes | **none** |
| `CR-1`, `CR-4`, `S-25k` | X: closes slicing, decode, regex, second hash, inline parse | **none in text**; domain extended by `CR-2′` |
| `MS-1`, `MS-4`, `MS-5`, `MS-8`, `MS-9`, `MS-12`, `MS-R1`..`MS-R4` | X: confirmed | **none** |
| `ACC-1`..`ACC-5`, `ACC-R1`..`ACC-R5` | X and Y: confirmed; a sixth accessor is a static violation | **none** — still five |
| `EV-1`, `EV-2`, `OD-1`..`OD-4`, `S-25o` | X and Y: confirmed exhaustive and non-overlapping | **none** — `EV-R4` states the disjointness explicitly |
| `D-1`, `D-2` | X and Y: confirmed, exactly two | **none** |
| `L-0`..`L-5`, `L-R1`, `L-R2` | X and Y: verified at every cited locus | **none** — `LD-2` keeps `EV-3` outside them |
| `DC-2`, `DC-3′`, `DC-4′`, `DC-5′`, `DC-7`, `WL-1`, `WL-2`, `WL-4′`, `WL-R1` | Y: the authorization boundary is preserved in full | **none** |
| `RC-1`..`RC-4`, `NC-1`..`NC-3`, `P-R1`..`P-R5` | X: "the exemption is correctly the only one" | **none**, except `P-R1`'s list reading `C-1..C-6` |
| §3.5 model choice, §3.6 destination search | X and Y: confirmed | **none** |
| the author recommendation | both lines: A recommended, unselected | **none** |

### §8.3 The preserved invariants

```text
N-1..N-9  UNCHANGED, with N-2's post-A property still SYNTACTIC and still
          granting no process-control authority; N-3's "observing a PID confers
          no authorized process control" now covering EV-3's value and every
          containing hash through CS-8 and S-25l″; N-5's Option B still
          non-selectable; N-7's watchdog-freeze cell still orthogonal and
          unresolved; N-8's T = NOT_ACTIVATED and OPEN programme claim; and
          N-9's no-selection.
N-10 NEW. NO SCIENTIFIC CELL IS TOUCHED. No entropy, capacity, custody, spend,
          settlement authorization, qualification, blinding, Q, C, datum,
          trajectory, comparison, outcome or Proof is created, moved, predicted
          or authorized by any sentence of v2.3, including EV-3, whose only
          effect is to NAME an operation the signed chain already requires.
```

### §8.4 Withdrawals and replacements introduced by v2.3

```text
R-W9   v2.2 PC-R1's "ONLY CLAIM PATHS ARE RESTRICTED"      WITHDRAWN at PC-R1′
       — the lease path is restricted, and every PC-N read is content-gated.
R-W10  v2.2 fixture R-d's unconditional PASS               REPLACED at R-d′.
R-W11  v2.2 PT-1 corollary 1's "every byte string that is the canonical
       serialization of a durable claim or occupant is produced by MS-2's
       read"                                               WITHDRAWN at
       COROLLARY 1′ — a pathname theorem cannot establish byte provenance.
R-W12  v2.2 PT-1 corollary 2's "the only expressions in the five roots that
       yield a claim or lease mapping"                     REPLACED at
       COROLLARY 2′ — its lease half had no anchor.
R-W13  v2.2 §8 item 3's disposition of the symlink residual — "no conforming
       root plants or follows a redirect" and "not a new exposure"
                                                           WITHDRAWN at CA-1,
       CA-R2 — ordinary open follows a symlink, and admitted kernel power is
       not a disposition of a governance consequence.
R-W14  v2.2 DC-6′'s "NO OTHER digest ... of a claim, a LEASE, an occupant ...
       exists in the five roots", and C-5's FORBIDDEN clause barring any
       evaluation other than EV-1 and EV-2 of a lease
                                                           WITHDRAWN at DC-6″,
       C-5″ — contract :116-124 requires active_lease_sha256, and §1.4 locates
       it inside the five roots on the signed bytes.
R-W15  v2.2 CS-4's "THERE IS NO READER FOR WHOM THE DIGEST CONCEALS THE
       IDENTITY FIELDS" and WL-3′'s "THE DIGEST HAS NO CONFIDENTIALITY
       PROPERTY"                                           WITHDRAWN at CS-4′,
       WL-3″ — both are unproved universals; the proved facts are conditional
       and the governance statement is that no guarantee is supplied.
       AND v2.2's D-14 "NOT interprocedural"               WITHDRAWN at D-14′.
```

None of these replacements is restated anywhere in v2.3 in its old form.

---

## §9. Weakest points in v2.3, stated by the author

1. **The gate is the largest single cost this cell has ever imposed, and part
   of it is genuinely new.** Three of `PG-3`'s four conjuncts and the no-follow
   flag are already signed at `protocol :58-72` and `contract :190-200` for the
   named runtime artifacts, so for those the gate imports rather than adds. But
   `st_nlink == 1` is **not** in the live signed tier — only in the superseded
   control-channel chain — and extending the whole discipline to `PC-N` records
   the signed chain does not name is this packet's own requirement. I priced it
   at `B-A8` rather than folding it into `B-A4(iii)`. A reviewer may hold that a
   read gate over records this cell does not own is the `YV2-C1` error in a new
   costume; my defence is that the gate constrains **how a read is performed**,
   never **which records exist or what they mean**, and that without it the Y
   line's alias consequence is uncontained.

2. **`PG-4`'s discriminator is a runtime check, and `S-25p` can only enforce its
   presence and position.** The verifier can see that the statements exist, in
   order, before any binding, with the failure branch routing to invalidity. It
   cannot see that the predicate is correct. That is a genuine weakening of the
   "everything is static" property this chain has held since v2.1, and I state
   it rather than describing `S-25p` as if it decided content. `A-T25` is what
   actually tests the predicate.

3. **`EV-3` and `C-6` enlarge the disclosed surface, and I did not look for a
   way to avoid them.** Once §1.4 located `active_lease_sha256` inside the five
   roots, naming it was forced. But a reviewer should check my audit rather than
   my conclusion: if `contract :576`'s implementation-surface row is read as
   non-normative, or if a future amendment moves settlement out of
   `generic_harness.py`, `EV-3` becomes an evaluation outside the five roots and
   `DC-6″`'s inventory must be re-scoped, not deleted.

4. **Five carriers is one more than the X line's repair named, and the fifth is
   mine.** `lease_canonical_bytes` is forced by the lease install's write, which
   `CR-3′(e)` had to give a position or `MS-13` would be unspellable — the exact
   failure mode `MS-12` had at v2.2. I say so at `CR-2′` rather than presenting
   four carriers and letting the fifth appear at implementation time.

5. **The rename of five `MS` functions is cosmetic but it touches rows two
   independent lines confirmed.** `MS-R6` states that shape, operand count,
   result kind and single definition are unchanged. If a reviewer prefers the
   claim-specific names retained with a widened operand column, that is a
   presentational choice and I would accept it without argument.

6. **`CS-4′(c)` makes this packet's information claim strictly smaller, and
   something now depends on nothing.** By declining to say anything about a
   digest-only reader, I leave a question genuinely open. I believe that is
   right — the Y line proved the universal was unearned — but a reviewer who
   wanted a bound on the digest-only case will not find one here, and no
   sentence of this chain may be cited as supplying one.

7. **`PT-1′` is now a theorem about a smaller thing, and `M-R4′` leans on the
   gate for the half the theorem lost.** If `PG-1`..`PG-7` are judged
   insufficient, `M-R4′`(ii) fails and with it the no-second-sink property for
   every non-pinned pathname. That dependency is stated at `M-R4′` in the open
   rather than buried in a corollary, which is precisely what v2.2 failed to do.

8. **Everything here still rests on `PRODUCTION_ROOTS` being exactly five
   paths.** A sixth root re-derives every number in `S-25m″`, re-opens `PT-1′`,
   and re-opens §1.4's audit, since the audit's third step is membership in that
   list.

9. **I found no new defect in the parts both lines confirmed closed, and that is
   itself a claim a reviewer should test.** §8 asserts that thirty-odd loci are
   untouched. I checked each against the v2, v2.1 and v2.2 bytes; the assertion
   is mine and the check is the reviewer's to repeat.

---

## §10. Negative space

This correction creates nothing executable and authorizes no selection, no X/Y
verdict, no implementation, no commit, no verifier or manifest edit, no code or
test artifact, no process, socket, pipe, fork, exec, signal, wait or `prctl`
operation, no supervisor, PCS, controller, worker or watchdog, no capability,
world, learner, entropy draw, capacity artifact, custody disposition, result
manifest, spend, settlement authorization, datum, trajectory, comparison,
outcome, Proof or claim movement. It predicts no qualification and no comparison
outcome. `PA-1′`..`PA-9′`, `PC-1L`, `PT-1′`, `CA-1`..`CA-5`, `PG-1`..`PG-7`,
`MS-1L`, `MS-13`, `MS-14`, `CR-2′`/`CR-3′`, `M-R4′`, `EV-3`, `C-6`,
`LD-1`..`LD-3`, `CS-4′`, `WL-3″`, `CS-8`, the primed and double-primed rule
texts, `S-25n′`, `S-25p` and `A-T22`..`A-T26` are **specification text, not
artifacts**. `EV-3` and `C-6` **name** operations the signed chain already
requires; they authorize nothing that was not already signed, and they widen no
authority. It selects neither option and mints no token. **No existing file was
modified.** `T` remains `NOT_ACTIVATED`; the programme claim remains `OPEN`; the
watchdog-freeze cell remains unresolved and orthogonal; Kirill's identity author
selection remains **unauthorized** pending both bounded final confirmations on
these bytes.
