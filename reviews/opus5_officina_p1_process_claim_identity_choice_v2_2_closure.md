READY_FOR_OFFICINA_P1_IDENTITY_V2_2_FINAL_XY_CONFIRMATION

# Author closure — P1 process-claim identity choice v2.2

**Author:** Claude Code Opus 5, **specification author only**. Not an
independent X-line or Y-line reviewer. **This closure is an untrusted author
self-assessment and must be treated as such.** Every load-bearing point below
is re-derivable from the committed contract bytes, and a confirmation line
should re-derive rather than accept it. Nothing here is a verdict on the
author's own work: the verdict token at the top of this file states only that
the correction is, in the author's judgement, **ready to be reviewed**, not that
it is correct.

**Deliverables of this round, and nothing else:**

```text
successor/OFFICINA_P1_PROCESS_CLAIM_IDENTITY_AUTHOR_CHOICE_PACKET_V2_2_CORRECTION.md   NEW
reviews/opus5_officina_p1_process_claim_identity_choice_v2_2_closure.md                NEW  (this file)
```

**No existing file was modified.** No code was written, no process executed, no
resource spent, `T` was not activated, and the programme claim was not moved.

---

## §1. Custody — every digest recomputed on the bytes

### §1.1 This round's product

```text
05046cd17fe0839541b9ec7614aaf66a84e69c169f9142a29e6a5cabf7bf0fc7  successor/OFFICINA_P1_PROCESS_CLAIM_IDENTITY_AUTHOR_CHOICE_PACKET_V2_2_CORRECTION.md
```

This closure's own digest is not embedded — a file cannot carry its own digest —
and is to be recomputed by each confirmation line with `sha256sum` on the
committed bytes.

### §1.2 The bytes v2.2 repairs, and the two binding verdicts

```text
3796de017449a9786db0b9b0ca0e8c2d84762e2239463033773b1fdb92b8ef37  successor/OFFICINA_P1_PROCESS_CLAIM_IDENTITY_AUTHOR_CHOICE_PACKET_V2_1_CORRECTION.md
c2d7a95784ad1bbc2a34898c0d3abf4de94dcd3416b14b959a3b2b61d6fab614  reviews/opus_officina_p1_process_claim_identity_choice_v2_1_final_confirmation.md   REVISE_OFFICINA_P1_IDENTITY_V2_1
cee60b4b85358a50a90729645081419b166cbc1224b53776ffb41a357cb5f578  reviews/sol_officina_p1_process_claim_identity_choice_v2_1_final_confirmation.md   REVISE_OFFICINA_P1_IDENTITY_V2_1
```

The v2.1 digest `3796de01…ef37` is the value **both** final confirmation lines
independently recomputed and pinned as their target (X §0 custody block; Y
§2.1). Each working-tree file was verified byte-identical to its `HEAD` blob
before being read, so the bytes repaired are the **committed** bytes the two
`REVISE` verdicts were returned against.

### §1.3 The preserved evidentiary record, byte-untouched

```text
ad8b5791f043f201c00812a11de2ab3b765664e65e6d0ebf9778e150913096d3  successor/OFFICINA_P1_PROCESS_CLAIM_IDENTITY_AUTHOR_CHOICE_PACKET_V1_DRAFT.md
f5d95a0d4a7c72731b5a20cf668e67dbc66329e0989fb945bd0a5727717f6095  successor/OFFICINA_P1_PROCESS_CLAIM_IDENTITY_AUTHOR_CHOICE_PACKET_V2_DRAFT.md
b7d061f5c60d75705f50ffc100bff24664336107dd450a8372e825c6f1afffa0  reviews/opus5_officina_p1_process_claim_identity_choice_v2_closure.md
0b104f3ec240acc5e067184efb752091f92920da7773c78aa35337de6a30f129  reviews/opus_officina_p1_process_claim_identity_choice_v2_confirmation.md
152b6dd2237a63d3ada6bd6a82a828892443a7752f838abf71cba0401ac01eb8  reviews/sol_officina_p1_process_claim_identity_choice_v2_confirmation.md
56d0f598331a713918ea3f5b642449dd4dca1a08224b6e9eb4afb239ba128246  reviews/opus5_officina_p1_process_claim_identity_choice_v2_1_closure.md
```

Every value matches what the two final confirmations recorded for the same
paths. The chain v1 → v2 → v2.1 → v2.2 is acyclic and each link is
byte-identifiable.

### §1.4 The governing signed chain

```text
2c857fa8ad7be1c861eb8cf561f396e7d2339403c7714abc7958745bf34e5d5d  successor/OFFICINA_GENERIC_HARNESS_SUPERVISOR_CONTROL_CHANNEL_P1_OPERATIVE_COMPOSITE_V1_2.md
cd106d7fef491601f9ff948aba3ba0ceaac0774ac18a6564247c0c5899b4c40c  successor/OFFICINA_T_ACTIVATION_PROTOCOL_V2_CORRECTION.md
64b8d3f63594b79a6abc767a032383c5704beaf09b32a1e0c58fdc444bb0af71  successor/OFFICINA_GENERIC_HARNESS_CONTRACT_V2_DRAFT.md
8c47da352ef5954406964647a32e97939c404806bdf9b3d3ff5bc70866e6369a  successor/OFFICINA_GENERIC_HARNESS_SIGNATURE.md
```

All four match the values **both** final confirmation lines recomputed. The
composite v1.2 is the sole operative implementation object; the whole
supervisor/control-channel chain below it remains authority level 3, immutable
historical and provenance evidence only.

---

## §2. The exact replacement index — three rows, and no fourth

| # | v2.1 locus replaced | Replaced by | Binding source |
|---|---|---|---|
| **A** | §2.4 rows `MS-1`/`MS-2`/`MS-3` **as they bear on the path and the read**; §2.7 `D-8`; `M-R4`'s decidability anchor | v2.2 §2 — `PA-1`..`PA-9`, `PC-1`/`PC-N`, `PT-1`, `D-8′`, `S-25n` | X-line determination 2 |
| **B** | §3.2 `C-5` OPERATION clause + the "one enumerated second invocation" paragraph; §3.4 `DC-1`, `DC-6`; §4.3 `S-25e`; §4.4 `S-25l`, `S-25m`; §6.1 declassification row; §6.3 step 5; §7 `A-T15`(a) | v2.2 §3 — `EV-1`/`EV-2`, `OD-1`..`OD-4`, `L-1`..`L-5`, `DC-1′`, `DC-6′`, `S-25e′`, `S-25l′`, `S-25m′`, `S-25o` | Y-line §9.1, §9.4 |
| **C** | §3.4 `DC-3`, `DC-4`, `DC-5`; §3.5 `WL-3`, `WL-4` | v2.2 §4 — `IP`/`ACU`, `CS-1`..`CS-7`, `DC-3′`, `DC-4′`, `DC-5′`, `WL-3′`, `WL-4′` | Y-line §9.2, §9.3 |

**No fourth row exists.** Every other line of v2.1 and of v2 carries forward
verbatim, and §4 of this closure tabulates the eighteen loci that must be found
unchanged.

---

## §3. Repair-by-repair account, with the exact mechanism

### §3.1 Repair A — the fresh claim-reopen path

**The finding, re-derived independently of the X line's summary.** `D-8`'s
load-bearing sentence claims *"§P1-13.7 (:2357-2368) already gives each durable
artifact exactly one open site."* Read directly at composite `:2354-2371`,
§P1-13.7's actual sentence is *"Every interface operation is assigned to exactly
one root and one function, so that no two layers can **install** the same
no-replace record"*, and its table pins **install** sites plus three **named**
reads. Invariant 84 (`:2753`) constrains the **P1 layer**; invariant 88
(`:2757`) enforces one **install** site. None pins a peer-layer claim read. And
`MS-2` itself has two call sites by design (`MS-2` post-install verify,
`MS-11` occupant load). **The premise fails on two independent counts, and the
X line is right.**

The key-order arithmetic is exact, not illustrative: at `protocol :231-238` the
twenty canonical keys place `controller_pid` at index **5** and
`process_group_id` at index **7**, so `vals[5]` and `vals[7]` reach both
restricted integers by position, using neither key literal.

**The repair, and why it is syntax-mechanical.** `PT-1` converts *"can this
expression denote the claims path?"* from a semantic question into a four-case
analysis over the syntactic forms a path operand may take:

| Case | Form | Closed by |
|---|---|---|
| 1 | the Name `claim_path` | `PA-4` — three positions, none of them a second read |
| 2 | a Name bound by a `PC-N` constructor | `PA-1` (root Constant cannot contain `T_PROCESS_CLAIMS`) + `PA-2` (only Constants and its own stem) + `PA-3` (stem grammar excludes `/`, `\`, `..`, leading `.`) |
| 3 | a Name bound by anything that is not a path constructor | `PA-7` second sentence — static violation outright; **no general-purpose read helper exists** |
| 4 | not a plain Name at all | `PA-5` node-type match, and `PA-1` independently |

Corollaries: every claim byte string binds immediately to a carrier Name
(`PA-8`), which is the premise `CR-1`'s "however obtained" needed and never had;
`M-R4` becomes decidably sound with `PT-1` as its anchor instead of the
withdrawn `D-8`; and `list(m.values())[5]` on a laundered fresh mapping is
unreachable because `m` cannot exist.

**The counterexample and its variants** are carried as build fixtures at v2.2
§2.7 and asserted individually at `A-T18`/`A-T19`: the X line's exact construct
(`open` → fresh `raw` → `json.loads` → `list(m.values())[5]`), plus `os.open`/
`os.read`, `pathlib`, `mmap`, alias, second construction, helper return, helper
return with parse, split literal, split-across-a-boundary, stem traversal,
environment/config path, `os.chdir` redirect, symlink indirection, exception
payload, container capture, directory enumeration and archive re-read.

**Reconciliation with retained peer-root `open()`.** `S-25i-N1` is unchanged:
the builtin `open` stays available in `generic_harness.py`. `PC-R2` states
explicitly that no peer read site is removed, relocated, or routed through
`MS-2`, and `A-T19` asserts four retained-behaviour fixtures (spawn-intent,
supervisor identity, freeze observation, generic `PC-N`) **PASS**, with a build
in which they fail counted as a test failure rather than a stricter build.
**Only claim paths are restricted** (`PC-R1`).

**The decidability cost, disclosed rather than absorbed.** `PA-7`'s second
sentence adds one new analysis kind: an **intra-function single-assignment
lookup** (`D-14`) — local, one-pass, terminating, unambiguous by `S-4`. It is
not interprocedural, not a call graph, not a fixpoint, not taint. It is
nevertheless *more* than the pure name/position matching of `S-25a`..`S-25m`,
and v2.2 says so in those words instead of calling it "the same discipline".

### §3.2 Repair B — two `ACC-5` evaluations

**The contradiction was internal, and the Y line located it exactly.** v2.1
asserted a one-digest world at `C-5` ("EXACTLY ONE SHA-256"), `DC-1` ("there is
never a second") and `DC-6` ("NO SECOND DIGEST … the only value derived from a
carrier"), while its own §3.2 paragraph and `S-25m` ("exactly two `ACC-5` call
sites") described a two-digest world. **The operation is not changed; the count
and the classification are.** The contradiction is resolved in favour of
`S-25m`, because the `X-4` conjunct is a closed `Y-M1` repair that cannot be
narrated away.

| | `EV-1` lineage evaluation | `EV-2` occupant evaluation |
|---|---|---|
| operand | canonical bytes of the claim **being installed**, after `MS-10` | canonical bytes of the `EEXIST` occupant, after that occupant **independently** passes `MS-10`, `X-2`, `X-3` |
| result | the raw lineage digest, 64 lowercase hex | a transient digest |
| destinations | **exactly two**, `D-1` and `D-2` | **none** |
| consumer | the two signed durable fields | **exactly one** — the boolean collision conjunct `X-4` |
| lifetime | persistent by signature | transient; does not outlive the conjunct |
| confinement | `S-25l′`, `L-R2` | `OD-1`..`OD-4`, `S-25o` |

`OD-1`..`OD-4` forbid persisting, logging, returning, storing, transmitting,
aliasing or comparing `EV-2`'s value anywhere but inside `X-4`, and `S-25o`
enforces it as an occurrence count on exactly one Name at exactly one site. **No
transient occupant digest may become a third destination.**

**The transitive lineage, enumerated rather than left to case-by-case
judgement.** `L-0` draws the distinction the Y line asked for — a **direct
destination** is a durable schema field whose value *is* the raw digest; a
**transitive continuation** is a durable object that *contains* one and is
itself hashed, copied or verified. `L-1`..`L-5` enumerate the five permitted
continuations, each already required by the signed chain at a cited locus:

| | Continuation | Signed locus |
|---|---|---|
| `L-1` | complete `T_PROCESS_STARTED` entry hash, seeding the lease's `prior_charge_event_sha256` | contract `:103-106` |
| `L-2` | charge-event and lease equality/hash chain | contract `:99-124` |
| `L-3` | final-record hash, named by `T_PROCESS_STOPPED.process_record_sha256`; same shape on the invalid-close route | contract `:125-140`, `:165-173` |
| `L-4` | archive copies and archive composites (Git object/tree/commit hashes over the staged set) | protocol `:85-97` |
| `L-5` | recovery and post-crash verification | contract `:125-140`; protocol `:85-97` |

`L-R1` gives a **one-question test** for a future reviewer — *does this field's
value equal the raw lineage digest?* — and `L-R2` keeps a third direct
destination forbidden by both `S-25l′` and `S-25m′`. **Exactly two direct
persistent raw-lineage-digest destinations are preserved.**

`L-4` also states plainly, because it bears on Repair C, that the archival set
stages **the process claim itself**, whose canonical bytes contain both
integers in cleartext.

### §3.3 Repair C — the narrowed cryptographic claim

The Y line is right that a packet may not disclose a residual in one paragraph
(`WL-3`) and assert its absence in the next (`DC-3`/`DC-4`/`DC-5`/`WL-4(a)`).
v2.2 introduces two predicates — `IP` **informationally possible** and `ACU`
**authorized conforming use** — tags every claim with one of them (`CS-R1`), and
states that they are independent (`CS-R2`).

**Withdrawn, explicitly and by name:**

| Withdrawn sentence | Why it is false |
|---|---|
| `DC-3` "never process identity … never a name of anything addressable" (unqualified) | true of `ACU`, false of `IP` — `CS-5` |
| `DC-4` blanket ban on "comparison" and "evidence" | self-contradictory: `X-4` **is** a digest comparison used as integrity evidence, and the packet requires it |
| `DC-5` unqualified "ONE-WAY" as a cryptographic claim | `CS-2`: with the other eighteen fields the search space is at most **4,194,304**, because `A-P4c` forces `pid == pgid` and `PID_MAX_LIMIT = 4194304` |
| `WL-4(a)` "the eighteen other canonical values are obtainable only by reading the claim" | `CS-3`: the constructing supervisor already holds all eighteen without reading anything; `CS-4`/`L-4`: the archive reader holds the integers in cleartext |
| `DC-6` "no second digest … the only value derived from a carrier" | Repair B — `EV-2` exists |
| `C-5` "EXACTLY ONE SHA-256", `DC-1` "there is never a second" | Repair B |

**Stated honestly in their place:** the digest is a **searchable full-claim
commitment** (`CS-1`); its identity-field search space is at most **4,194,304**
(`CS-2`); it **may provide conditional informational identity and equality
evidence** (`CS-5`); and it **is not a confidentiality boundary** (`CS-4`) —
there is no reader for whom it conceals the identity fields.

**Preserved in full, and not narrowed by one item:** the normative authorization
boundary. `DC-4′` keeps the entire sink prohibition — addressing, selection,
signalling, waiting, process-control primitives, request builders for the nine
opcodes, handle keys and comparisons, journal and retry keys, capacity, custody,
spend, settlement, qualification, blinding, Q/C, scientific datum, observation,
evidence, outcome and Proof — and extends it to **any value recovered or
inferred from the digest** via class member `(f)`. `CS-6` states that the digest
confers no process-control authority and is not an authorized PID selector.
`CS-7` adopts the Y line's scope sentence as binding wherever v2 or v2.1 says
something stronger. `WL-R1` restates the governance property in one sentence so
it cannot be overread, and grounds it in `S-25l′`, `S-25o` and `P-R5`'s dominant
invalidity **rather than in an assumption about what an actor can compute**.

`DC-4′`'s one amendment is the comparison clause: the digest's **authorized**
comparisons are exactly the `X-4` conjunct and the `L-1`..`L-5` containing-object
hashing and verification. Scientific evidence, Q/C evidence, and evidence
offered as a basis for process control or selection remain banned.

---

## §4. No-regression table

Every item below was checked against the v2.1 and v2 bytes. **The assertion is
the author's; the check is the reviewer's to repeat.**

### §4.1 The eight findings both lines confirmed closed, twice

| Finding | Locus that must remain intact | v2.2 effect | Evidence |
|---|---|---|---|
| `X M-1` | v2 §2.8.1–§2.8.3, thirteen-key `J4`, `R-P1`..`R-P4` | **none** | not in v2.2's replacement index |
| `X m-1` | v2 §2.3 `A-P4a`..`A-P4d` | **none** | not in the index; `CS-2` cites `A-P4c` without altering it |
| `X m-2` | v2 §2.2 `PID_MAX_LIMIT = 4194304`, `G-1`..`G-6`, `A-T8` | **none in substance** | `CS-2` cites the bound as the size of the search space; the bound, the grammar and the over-range rejection are unchanged |
| `X m-3` | v2 §6.1 Case 1 / Case 2 | **none** | not in the index |
| `Y-C2` | v2 §2.8.2/§2.8.3 byte-identical redelivery | **none** | not in the index |
| `Y-M1` | v2 §2.10.1–§2.10.4, `X-1`..`X-4`, `I-1`..`I-10` | **none in substance** | `X-4` is not removed, narrowed or renumbered; `EV-2`/`OD-*`/`S-25o` describe the digest `X-4` already used. No matrix row, no conjunct, no routing changes |
| `Y-M2` | v2 §3.2, two superseded schemas | **none** | `L-3`/`L-4` cite the final record's hash and archive copy; it still carries the digest and neither identity key (`protocol :248-257`) |
| `Y-m1` | v2 §1.5 `R-1`..`R-4`; §4 | **none** | not in the index |

### §4.2 The v2.1 mechanism both final lines confirmed sound

| v2.1 locus | Confirmed by | v2.2 effect |
|---|---|---|
| `S-25i`, `S-25i-N1`..`N4` | X determination 3 — compatible with all five allowlists; retained `open` is "the correct decision" | **none in text** |
| `M-R1`, `M-R2` | X determination 1 | **none** |
| `M-R3`, `M-R5`, `S-25j` + scope note | X determination 1 — eight routes closed | **none** |
| `CR-1`..`CR-4`, `S-25k` | X determination 1 | **none in text**; `PT-1` corollary 1 supplies `CR-1`'s missing premise |
| `MS-4`..`MS-12`, `MS-R1`..`MS-R4` | X determination 5 — twelve rows | **none**; count stays 12 |
| `ACC-4`, `ACC-5`, `ACC-R5` | X determination 4; Y §3 | **none** |
| `ACC-R1`..`ACC-R4` | X determination 4 — a sixth accessor is a static violation | **none** |
| `C-5` as a record-level consumer | X "fully closed"; Y "a legitimate fifth consumer" | **none** except the OPERATION clause's count |
| `D-1`, `D-2` | X and Y | **none** — still exactly two |
| `DC-2`, `DC-7` | Y §3 "Proved nonblocking" / "Confirmed, bounded" | **none** |
| `RC-1`..`RC-4` | X determination 4 — "the exemption is correctly the only one" | **none** |
| v2.1 §3.5 model choice | X determination 5; Y §8 item 3 | **none** |
| v2.1 §3.6 destination search | X — key absent from the composite and both accepted peer contracts; Y §8 item 5 "Closed" | **none** |
| `NC-1`..`NC-3` | carried from v2 | **none** — unaffected by `D-8′`, which withdraws only the *read*-site reading of §P1-13.7, while `NC-2` rests on its *install*-site property |
| `S-25a`, `S-25b`, `S-25c`, `S-25d`, `S-25f`, `S-25g`, `S-25h` | X determination 5 | **none in text**; only `S-25e`, `S-25l`, `S-25m` are primed |
| `P-R1`..`P-R5`, `ACC-R1`..`ACC-R5` amended texts (v2.1 §4.1, §4.2) | X determination 5 | **none** |
| v2 §2.5 `V-1`..`V-9`, `Z1-R1`..`Z1-R6`, `Z2-R1`..`Z2-R5` | X — "this part of the mechanism works" | **none** |
| v2 `A-T1`..`A-T17` | X determination 5 | **fixture text unchanged**; only `A-T9`'s *assertion* is amended at `A-T9′` to require `S-25d` **and** `S-25n` both fire, so the fixture is not silently reclassified |

### §4.3 The X line's one nonblocking flag, now answered

X determination 3 flagged that `S-25i(iii)` forbids `json.JSONEncoder`/
`json.JSONDecoder` root-wide while `ACC-4` (`MS-6`) must produce the canonical
serialization the peer contract fixes and "invents no encoding". **The
dependency is satisfiable and is now stated:** standard canonical JSON
(`json.dumps(..., sort_keys=True, separators=(",",":"))` then
`.encode("ascii")`) requires no encoder subclass, and `MS-6`'s row already
specifies exactly one canonical serialization plus exactly one `.encode("ascii")`.
`PA-9(c)` restates the `JSONEncoder`/`JSONDecoder` ban alongside the parse pin so
the two rules are read together. The flag was nonblocking and remains so; it is
recorded here rather than left for a third round to rediscover.

---

## §5. Updated counts

| Quantity | v2 | v2.1 | **v2.2** |
|---|---|---|---|
| persistent consumers | 4 | 5 | **5** — `C-1`..`C-5` |
| centralized accessors | 3 | 5 | **5** — `ACC-1`..`ACC-5` |
| verifier rules added by Option A | 8 | 13 | **15** — `S-25a`..`S-25o` |
| behavioural tests added by Option A | 12 | 17 | **21** — `A-T1`..`A-T21` |
| governed mapping Names | — | 3 | **3** |
| carrier Names | — | 3 | **3** |
| approved call sites | — | 12 | **12** |
| claims-root literal occurrences | — | unpinned | **1** (`PA-1`, at `MS-1`) |
| claim-path Names | — | unpinned | **1** (`claim_path`, `PA-4`) |
| `MS-1` call sites | — | unpinned | **1** (`PA-4`) |
| claim read functions | — | unpinned | **1** (`MS-2`, `PA-7`); called at 2 sites |
| path-constructor rows | — | — | **1 named (`PC-1`) + `PC-N` shape-closed** |
| `ACC-5` accessor definitions | — | 1 | **1** |
| `ACC-5` authorized evaluations | — | "exactly one" *(contradicted)* | **2** — `EV-1`, `EV-2` |
| persistent lineage digest values | — | 1 implied | **1** — `EV-1` only |
| transient digest values | — | unnamed | **1** — `EV-2`, no destination |
| direct persistent destinations | — | 2 | **2** — `D-1`, `D-2` |
| enumerated transitive continuations | — | 0 | **5** — `L-1`..`L-5` |
| declassifying operations | 0 asserted | "exactly 1" | **1 operation, 2 evaluations, 1 persistent value** |
| handoff steps | 10 | 11 | **13** |
| sentences withdrawn/replaced by this round | — | 2 (`R-W1`, `R-W2`) | **6** (`R-W3`..`R-W8`) |

Rule-letter arithmetic: `S-25a`..`S-25o` is fifteen letters, and `S-25n`/`S-25o`
are the two added. Test arithmetic: `A-T18`..`A-T21` is four added, `17 + 4 = 21`,
mapping to handoff test rows 92–112.

---

## §6. One bounded question per reviewer

Each line is asked **one** question, and it is the question whose answer decides
whether that line's `REVISE` is closed.

### §6.1 To the X line (Claude Code Opus, independent engineering review)

> **Does `PT-1`'s four-case analysis, resting on `PA-1` (substring pin),
> `PA-2`/`PA-3` (constant-plus-grammar-checked-stem spelling), `PA-5` (plain-Name
> read operand) and `PA-7` (`claim_path` pinned to `MS-2`; no general-purpose
> read helper), close *every* route by which a claim byte string can be produced
> in the five roots outside `MS-2` — and in particular, is the one new analysis
> kind at `PA-7`'s second sentence, the intra-function single-assignment lookup
> disclosed at `D-14`, within what `X M-2` permits, or does it spend the
> no-taint/no-call-graph property the previous rounds preserved?**
>
> If your answer is no on the first half, the deliverable is the AST that
> reaches a claim byte string outside `MS-2` while satisfying `PA-1`..`PA-9`.
> If your answer is no on the second half, the deliverable is the statement of
> which weaker recognition rule you would accept in `PA-7`'s place.

### §6.2 To the Y line (GPT Sol, independent validity/governance review)

> **With the two `ACC-5` evaluations now named (`EV-1`/`EV-2`), the transient
> occupant digest confined by `OD-1`..`OD-4`/`S-25o`, the five transitive
> continuations enumerated at `L-1`..`L-5` behind the direct/continuation
> distinction of `L-0` and the one-question test of `L-R1`, and the
> cryptographic claim narrowed to `CS-1`..`CS-7` under the `IP`/`ACU`
> distinction — is the resulting boundary now *complete and non-contradictory*:
> does any sentence in v2, v2.1 or v2.2 still assert a confidentiality or
> impossibility property the digest does not have, and does any authorized use
> that the signed chain requires still fall outside `DC-4′`'s permitted
> comparisons or `L-1`..`L-5`?**
>
> If your answer is no on the first half, the deliverable is the surviving
> sentence and its locus. If your answer is no on the second half, the
> deliverable is the required use that `DC-4′`/`L-1`..`L-5` do not admit.

---

## §7. Residual choices — what remains open, and whose they are

### §7.1 The author's disclosed weak points

The eight items at v2.2 §8 are the author's own, stated before review rather
than after: (1) `PA-7`'s new analysis kind; (2) `PC-N` closed by shape rather
than enumeration; (3) `V-m` symlink indirection not fully closed and not claimed
to be; (4) `B-A4(iii)`'s cost to the peer root, possibly disproportionate; (5)
Repair C makes the packet's claim strictly weaker with no compensation
elsewhere; (6) `L-1`..`L-5` classify lineage other contracts own; (7) the five
roots are a fixed list on which `PT-1` now also depends; (8) the no-regression
assertion at §4 is the author's and must be re-checked.

Items 1, 2 and 4 are **design choices a reviewer may reverse**. Items 3, 5, 6
and 7 are **disclosed residuals**, not proposals. Item 8 is an **instruction to
the reviewer**.

### §7.2 Choices this round did not make, and does not authorize

```text
The A/B selection is NOT made. Option A remains RECOMMENDED AND UNSELECTED;
  neither I_SELECT_P1_PROCESS_CLAIM_IDENTITY_A_OBSERVATION_ONLY nor
  I_SELECT_P1_PROCESS_CLAIM_IDENTITY_B_OPAQUE_BINDING is chosen.
Option B remains NON-SELECTABLE behind sub-cells B-1 and B-2, on authority
  grounds and not size grounds. Its corrected count is untouched.
P1_IDENTITY_OBSERVATION_BOUNDED_WEAKENING_V1 is neither minted nor accepted.
The historical OK/CLAIM matrix remains NON-GOVERNING, on the evidence both
  final lines independently verified: composite authority level 3; not restated
  in v1.2; absent from both accepted peer contracts. DC-1′ accommodates a future
  contrary ruling without amendment, which remains the second independent reason
  for the declassification model.
The watchdog-freeze cell AUTHOR_CELL_P1_WATCHDOG_FREEZE_MECHANISM remains
  ORTHOGONAL AND UNRESOLVED. P1 remains non-operative until it is resolved even
  if A is selected.
Whether a sixth production root is ever added — which would re-derive every
  count in S-25m′ and re-open PT-1 — is not this cell's to decide.
```

---

## §8. Verdict and negative authorization

```text
READY_FOR_OFFICINA_P1_IDENTITY_V2_2_FINAL_XY_CONFIRMATION
```

The verdict asserts exactly this and nothing more: in the author's judgement the
three residuals the two binding `REVISE` verdicts named are repaired exactly —
Repair A by pinning the claims-root literal to `MS-1`, the claim read to `MS-2`,
and the canonical parse to `MS-3`, with recognition made syntax-mechanical by
`PT-1` and the peer layer's retained `open()` reconciled rather than withdrawn;
Repair B by naming two `ACC-5` evaluations, confining the transient occupant
digest, preserving exactly two direct persistent destinations and enumerating
the permitted transitive lineage; Repair C by withdrawing the absolute
cryptographic assertions, stating the searchable-commitment and
4,194,304-candidate facts, and preserving the authorization boundary intact —
and that the bytes are therefore **fit to be reviewed**. It asserts no
correctness that a confirmation line has not independently established.

**This closure authorizes nothing.** Not Kirill's A/B selection, not the
`P1_IDENTITY_OBSERVATION_BOUNDED_WEAKENING_V1` token, not implementation, not a
verifier or manifest edit, not a commit, not a code or test artifact, not
activation, not process control, not spend, not custody disposition, not a
datum, outcome, Proof or claim movement. No existing file was modified in
producing this round; its sole products are the v2.2 correction and this file.

```text
T = NOT_ACTIVATED
PROGRAMME CLAIM = OPEN
WATCHDOG-FREEZE CHOICE = UNRESOLVED AND ORTHOGONAL
IDENTITY SELECTION = NOT MADE, NOT AUTHORIZED
OPTION A = RECOMMENDED, UNSELECTED
OPTION B = NON-SELECTABLE
```
