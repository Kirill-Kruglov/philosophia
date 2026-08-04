READY_FOR_OFFICINA_P1_IDENTITY_V2_3_FINAL_XY_CONFIRMATION

# Author closure — P1 process-claim identity choice v2.3

**Author:** Claude Code Opus 5, **specification author only**. Not an
independent X-line or Y-line reviewer. **This closure is an untrusted author
self-assessment and must be treated as such.** Every load-bearing point below is
re-derivable from the committed contract bytes, and a confirmation line should
re-derive rather than accept it. The verdict token at the top of this file
states only that the correction is, in the author's judgement, **ready to be
reviewed** — not that it is correct.

**Deliverables of this round, and nothing else:**

```text
successor/OFFICINA_P1_PROCESS_CLAIM_IDENTITY_AUTHOR_CHOICE_PACKET_V2_3_CORRECTION.md   NEW
reviews/opus5_officina_p1_process_claim_identity_choice_v2_3_closure.md                NEW  (this file)
```

**No existing file was modified.** No code was written, no process executed, no
resource spent, no entropy drawn, no trajectory produced, `T` was not activated,
and the programme claim was not moved.

---

## §1. Custody — every digest recomputed on the bytes

### §1.1 This round's product

```text
832d31693d719a43198544807ffa74c96c88fb55d82bfb4ce70ef9fd265643e3  successor/OFFICINA_P1_PROCESS_CLAIM_IDENTITY_AUTHOR_CHOICE_PACKET_V2_3_CORRECTION.md
```

This closure's own digest is not embedded — a file cannot carry its own digest —
and is to be recomputed by each confirmation line with `sha256sum` on the
committed bytes.

### §1.2 The bytes v2.3 repairs, and the two binding verdicts

```text
05046cd17fe0839541b9ec7614aaf66a84e69c169f9142a29e6a5cabf7bf0fc7  successor/OFFICINA_P1_PROCESS_CLAIM_IDENTITY_AUTHOR_CHOICE_PACKET_V2_2_CORRECTION.md
e2ad45b7d3dd84d2537d19e52302a729ac390dae2a2fd6b169b4a84d15eca242  reviews/opus_officina_p1_identity_v2_2_final_x_confirmation.md   REVISE_OFFICINA_P1_IDENTITY_V2_2
e82a6974d413b830b5913ddaaa788571aac56705ddaa0f3a9843f50c5b43abc1  reviews/sol_officina_p1_identity_v2_2_final_y_confirmation.md    REVISE_OFFICINA_P1_IDENTITY_V2_2
```

The v2.2 digest `05046cd1…0fc7` is the value **both** final confirmation lines
independently recomputed and pinned as their target (X §0; Y §2), so the bytes
repaired are the committed bytes the two `REVISE` verdicts were returned against.

### §1.3 The preserved evidentiary record, byte-untouched

```text
ad8b5791f043f201c00812a11de2ab3b765664e65e6d0ebf9778e150913096d3  successor/…PACKET_V1_DRAFT.md
f5d95a0d4a7c72731b5a20cf668e67dbc66329e0989fb945bd0a5727717f6095  successor/…PACKET_V2_DRAFT.md
3796de017449a9786db0b9b0ca0e8c2d84762e2239463033773b1fdb92b8ef37  successor/…PACKET_V2_1_CORRECTION.md
b7d061f5c60d75705f50ffc100bff24664336107dd450a8372e825c6f1afffa0  reviews/opus5_officina_p1_process_claim_identity_choice_v2_closure.md
0b104f3ec240acc5e067184efb752091f92920da7773c78aa35337de6a30f129  reviews/opus_officina_p1_process_claim_identity_choice_v2_confirmation.md
152b6dd2237a63d3ada6bd6a82a828892443a7752f838abf71cba0401ac01eb8  reviews/sol_officina_p1_process_claim_identity_choice_v2_confirmation.md
56d0f598331a713918ea3f5b642449dd4dca1a08224b6e9eb4afb239ba128246  reviews/opus5_officina_p1_process_claim_identity_choice_v2_1_closure.md
c2d7a95784ad1bbc2a34898c0d3abf4de94dcd3416b14b959a3b2b61d6fab614  reviews/opus_officina_p1_process_claim_identity_choice_v2_1_final_confirmation.md
cee60b4b85358a50a90729645081419b166cbc1224b53776ffb41a357cb5f578  reviews/sol_officina_p1_process_claim_identity_choice_v2_1_final_confirmation.md
a9d48c9d8d64214e4685065f9c16989aa095ccca14273019805682d00526f8e4  reviews/opus5_officina_p1_process_claim_identity_choice_v2_2_closure.md
```

The chain v1 → v2 → v2.1 → v2.2 → v2.3 is acyclic and each link is
byte-identifiable. Every value matches what the two v2.2 final confirmations
recorded for the same paths. **Both lines independently noted that no
`…PACKET_V2_CORRECTION.md` exists**; the v2 tier is `…PACKET_V2_DRAFT.md`, and
v2.3 §1.2 adopts that custody note.

### §1.4 The governing signed chain

```text
2c857fa8ad7be1c861eb8cf561f396e7d2339403c7714abc7958745bf34e5d5d  successor/…P1_OPERATIVE_COMPOSITE_V1_2.md
cd106d7fef491601f9ff948aba3ba0ceaac0774ac18a6564247c0c5899b4c40c  successor/OFFICINA_T_ACTIVATION_PROTOCOL_V2_CORRECTION.md
64b8d3f63594b79a6abc767a032383c5704beaf09b32a1e0c58fdc444bb0af71  successor/OFFICINA_GENERIC_HARNESS_CONTRACT_V2_DRAFT.md
8c47da352ef5954406964647a32e97939c404806bdf9b3d3ff5bc70866e6369a  successor/OFFICINA_GENERIC_HARNESS_SIGNATURE.md
724d633a55668013b78058eed1c76e12e9bbaf487f71ea94b7a4568ea1ced8a0  successor/OFFICINA_GENERIC_HARNESS_CONTRACT_V2_3_1_CORRECTION.md
b5a1523290b6b8417a7b3288329cc4a4e5ff80214c8f28e6ea1ae51a450a94c9  successor/OFFICINA_BATCH_SETTLEMENT_CORE_AMENDMENT_V1_1_1_CORRECTION.md
```

The first four match the values **both** final lines recomputed. The last two are
the two accepted peer contracts, read this round because the `X D5` audit turns
on the generic-harness contract's implementation surface and on the batch
settlement amendment's settlement entry. Every working-tree file was verified
byte-identical to its `HEAD` blob before being read.

---

## §2. The audit `X D5` demanded, decided on the bytes

The X line required this to be **stated, not guessed**, and required a bounded
blocker if the governing bytes did not determine it. **They determine it, and no
blocker is returned.** The chain composes from three signed loci:

| Step | Question | Signed locus | Answer |
|---|---|---|---|
| 1 | What computes `active_lease_sha256`? | `contract :116-124` (§2c.5 heartbeat settlement); `batch :93-97` | the heartbeat, over "the hash of the exact pre-settlement lease" / "SHA-256 of the durable pre-settlement lease" |
| 2 | Which file carries the heartbeat? | `contract :576` — the implementation-surface row assigning `generic_harness.py` "lifecycle tables (§2) … §4 reservation/**settlement**/batch/conservation … `__main__` CLI (claim/start/**heartbeat**/close/pause/resume)"; `contract :517-522` — "No additional `scripts/*.py` entry point is introduced" | `src/philosophia/officina/generic_harness.py`, with no alternative signed home |
| 3 | Is that file a production root? | `contract :505-514` "Production roots are exactly the immutable-control verifier's pinned tuple"; `composite :349-357` §P1-3.1's five roots | yes, under **both** governing documents |

**Conclusion: `active_lease_sha256` is evaluated INSIDE the five production
roots.** So is the lease installation (`contract :103-106`) and the successor
lease install (`contract :116-124`).

Four consequences are taken in full, and none of them is created by this packet:

```text
(a) the lease install belongs in the approved call-site table   → MS-13
(b) active_lease_sha256 is a third authorized evaluation        → EV-3
(c) it is a sixth persistent consumer of the restricted bytes   → C-6
(d) DC-6′'s "NO OTHER digest ... of a claim, a LEASE, an occupant ... exists in
    the five roots" was FALSE on the signed bytes               → DC-6″
```

The X line's `R-5` is therefore resolved in its first branch ("if inside"), and
`C-5″`, `DC-1″`, `DC-6″`, `EV-R1′`, `S-25e″`, `S-25l″` and `S-25m″` are
re-derived to admit `EV-3` as an enumerated integrity evaluation with no
identity destination.

---

## §3. One-to-one disposition of every X and Y finding

### §3.1 X-line findings

| # | X finding | Disposition | Where |
|---|---|---|---|
| `D1` | **blocking.** The lease is the unpinned half; the determination-2 construct reproduces through `_lease_path`; `PC-R1`/`R-d` certify it passes; `PT-1` corollary 2 overclaims | **ADOPTED IN FULL, route (i).** Both roots pinned symmetrically: `PA-1′` two substrings, `MS-1L`, `lease_path`, `PA-4′`/`PA-7′` over both Names, `PA-9′`, `MS-13`, `MS-14`, `CR-2′` five carriers, `CR-3′(e)`, `M-R4′` five producers, `PC-R1′` withdrawing "only claim paths are restricted", `R-d′` withdrawing the unconditional PASS, `S-25n′` | v2.3 §2 |
| `D2` | `PA-6` makes `MS-12` a read call so `PA-7` rejects the install; `PA-4(a)`/`PA-7` jointly unsatisfiable | **ADOPTED.** `PA-6′` defines a `WRITE CALL` by Constant mode/flags operand, exactly two exist (`MS-12`, `MS-13`), and `PA-5′`/`PA-7′` do not apply to them; `PA-4′` counts uses at call sites and makes `MS-2`'s parameter its own | v2.3 §2.2, §3.2 `E-1`..`E-3` |
| `D3` | `PA-5`/`PA-7`/`PA-3` make `S-13`/`S-18` exact constants and every constant durable path unspellable | **ADOPTED.** `PA-5′(b)` admits a Constant containing neither pinned substring; `PA-3′(b)` admits no-stem constructors; fixtures `R-e`, `R-f`; `A-T26(d)(e)(f)` asserts the admission and its matched rejection | v2.3 §2.2, §3.2 `E-4`, §7 |
| `D4` | `D-14` mislabels the analysis kind | **ADOPTED.** `D-14′`: local single-assignment lookup **plus a one-hop callee-definition lookup**; not taint, not a fixpoint, not a transitive call graph; and `PA-7′` does not rely on `S-4`, which is stated rather than inherited | v2.3 §3.3 |
| `D5` | State where `active_lease_sha256` is evaluated; do not guess | **AUDITED AND STATED: inside.** `EV-3`, `C-6`, `LD-1`..`LD-3`, `DC-6″`, `C-5″` | v2.3 §1.4, §5.1, §5.2 |
| `R-1`..`R-5` repair texts | the smallest exact replacements | **ALL FIVE ADOPTED**, with two deviations declared: five carriers rather than four (`CR-2′`, forced by `MS-13`'s write position), and the `PG` gate, which `R-1`..`R-5` did not require but the Y line did | v2.3 §2.5, §4 |
| X §8 item 4 | `B-A4(iii)`'s cost is priced but incomplete | **ADOPTED.** `B-A8` prices the gate separately and names the one genuinely new conjunct | v2.3 §6.2 |

### §3.2 Y-line findings

| # | Y finding | Disposition | Where |
|---|---|---|---|
| `Y1` | `CS-4`'s "no reader is concealed from" and `WL-3′`'s "no confidentiality property" are unproved universals; the defensible statement is that the cell supplies no confidentiality **guarantee** | **ADOPTED VERBATIM IN SUBSTANCE.** `CS-4′` states the `[ACU]` disclaimer, then the `[IP]` facts each with its condition: (a) ≤ 4,194,304 **for a reader who knows the other eighteen**; (b) claim/lease/archive readers see the integers; (c) **no claim in either direction** for a reader without the conditioning fields. `WL-3″` withdraws the universal. `B-A5″` repairs the summary, which Y required explicitly | v2.3 §5.3, §6.2 |
| `Y1`, §3.2 | the conditional fact propagates through `L-1`..`L-5` only when the reader knows each containing object's other fields | **ADOPTED.** `CS-8`, tagged `[IP]`, extended to `EV-3`, with `[ACU]` stating it authorizes nothing and that class member `(f)` and every sink rule apply | v2.3 §5.3 |
| `Y2` (a) | narrow `PT-1` and its corollaries to pathname construction | **ADOPTED.** `PT-1′` claims **denotation of a pathname** and nothing more; corollaries `1′`, `2′`, `3′` restated; `R-W11`, `R-W12` withdraw the promoted versions | v2.3 §4.1 |
| `Y2` (b) | name symlink, hard link, descriptor alias and copied bytes as one external content-alias residual class | **ADOPTED.** `CA-0`..`CA-5` (with rename/bind-mount added as a fifth member), `CA-R1` one containment, `CA-R2` the residual is open and is not claimed closed | v2.3 §4.2 |
| `Y2` (c) | v2.2 wrongly says a conforming root does not follow the redirect | **ADOPTED AND WITHDRAWN.** `CA-1`: ordinary `open(path,"rb")` **follows** a symlink and omitting `follow_symlinks` does not prevent it; `R-W13` withdraws v2.2 §8 item 3's disposition and its "not a new exposure" conclusion | v2.3 §4.2, §8.4 |
| `Y2` (d) | require the signed no-follow, regular-file, link-count and held-descriptor/path-identity discipline before any `PC-N` bytes are parsed, returned or bound | **ADOPTED.** `PG-2` (no-follow **by flag Constant, not by omission**), `PG-3(a)` regular file, `PG-3(b)` `st_nlink == 1` **with the explicit statement that `samestat` cannot supply it because a hard link is the same inode**, `PG-3(c)` held-descriptor path identity, `PG-3(d)` the lock anchor | v2.3 §4.3 |
| `Y2` (e) | a path-bound exact-schema discriminator, with claim-shaped content at a `PC-N` path routing to dominant invalidity before value binding | **ADOPTED.** `PG-4` path-bound discriminator, `PG-5` record-first dominant invalidity **before** any mapping is bound, `PG-6` no exemption/fallback/early binding, `S-25p` enforcing presence and **order** | v2.3 §4.3, §4.4 |
| `Y2` (f) | negative fixtures for planted symlink, hard link, copied claim bytes and live `/proc/self/fd` alias, asserting invalidity before parse rather than static impossibility | **ADOPTED.** `A-T25(a)`..`(d)` plus `(e)` a negative control; `(b)` additionally asserts that a `samestat`-only check would have passed, so the necessity of the link-count conjunct is demonstrated | v2.3 §7 |
| Y §5.2, §6 | the leak shape resumes after runtime aliasing; the inferential surface can expand while every count stays true | **ADOPTED AS THE REASON FOR THE GATE.** `M-R4′` now has two anchors and says so: `PT-1′` for pinned pathnames, `PG-1`..`PG-7` for every other pathname. `PT-1′` corollary `3′` states that `m` is *not reached* rather than *cannot exist* | v2.3 §2.6, §4.1 |
| Y §8 constraints | do not enumerate the peer record set, add a root, change a schema, alter a destination or reopen an authority cell | **HONOURED.** `F-N1`..`F-N4`, `LD-3`, `PC-R1′`. `PG-4`'s third bullet defers to "the schema value its own owning contract fixes"; this packet names two schema values, its own | v2.3 §4.5, §5.2 |

### §3.3 What both lines confirmed, and which v2.3 does not touch

`EV-1`/`EV-2` (operands, sites, preconditions, destinations, `OD-1`..`OD-4`,
`S-25o`); `D-1`/`D-2` as **exactly two** direct persistent destinations of the
claim lineage digest; `L-0`..`L-5`, `L-R1`, `L-R2`; `ACC-1`..`ACC-5`,
`ACC-R1`..`ACC-R5`; `RC-1`..`RC-4`; `NC-1`..`NC-3`; `DC-2`, `DC-3′`, `DC-4′`,
`DC-5′`, `DC-7`, `WL-1`, `WL-2`, `WL-4′`, `WL-R1`, `CS-1`..`CS-3`, `CS-5`..`CS-7`,
`IP`/`ACU`, class member `(f)`; §3.5's model choice and §3.6's destination
search; the eight findings closed at v2/v2.1; the author recommendation (**A
recommended, unselected**); and Option B's non-selectability. `EV-R4` states
`EV-1`/`EV-2`/`EV-3`'s pairwise disjointness explicitly so that adding the third
cannot be read as disturbing the first two.

---

## §4. Replacement index

| # | v2.2 / v2.1 locus replaced | Replaced by | Binding source |
|---|---|---|---|
| **D** | `PA-1`, `PA-4`, `PA-7`, `PA-9(d)`, `PC-1`/`PC-N`, `PC-R1`, `MS-2`/`MS-3`/`MS-6`/`MS-7`/`MS-10`/`MS-11` rows, `CR-2`, `CR-3`, `M-R4`, `R-d` | `PA-1′`, `PA-4′`, `PA-7′`, `PA-9′`, `PC-1`/`PC-1L`/`PC-N`, `PC-R1′`, `MS-1L`/`MS-13`/`MS-14` + amended rows, `CR-2′`/`CR-3′`, `M-R4′`, `R-d′`, `S-25n′` | X `D1`; Y §6 |
| **E** | `PA-3`, `PA-5`, `PA-6`, `PA-4`'s position count, `MS-2`'s read shape, `PC-R2` | `PA-3′`, `PA-5′`, `PA-6′` (+ `WRITE CALL`), `PA-4′`'s use-counting note, `MS-2`'s descriptor-anchored row, `PC-R2′`, `R-e`, `R-f` | X `D2`, `D3` |
| **F** | `PT-1` + corollaries 1–3, v2.2 §8 item 3's disposition, fixture `V-m` | `PT-1′` + corollaries `1′`–`3′`, `CA-0`..`CA-5`, `CA-R1`/`CA-R2`, `PG-1`..`PG-7`, `S-25p` | Y `Y2` |
| **G** | `C-5` OPERATION + FORBIDDEN, `DC-1′`, `DC-6′`, `EV-R1`, `EV-R3`, `S-25e′`, `S-25l′`, `S-25m′`, the consumer count | `EV-3`, `C-6`, `LD-1`..`LD-3`, `C-5″`, `DC-1″`, `DC-6″`, `EV-R1′`, `EV-R3′`, `EV-R4`, `S-25e″`, `S-25l″`, `S-25m″` | X `D5` + the §2 audit |
| **H** | `CS-4`, `WL-3′`, `B-A5′` and every restatement | `CS-4′`, `WL-3″`, `CS-8`, `B-A5″` | Y `Y1` |
| **I** | `D-14`, v2.2 §8 item 1 | `D-14′` | X `D4` |

**No seventh row exists.** Every other line of v2.2, v2.1 and v2 carries forward
verbatim, and §6 of this closure tabulates the loci that must be found unchanged.

---

## §5. Exact revised counts

| Quantity | v2.1 | v2.2 | **v2.3** | Why it changed |
|---|---|---|---|---|
| persistent consumers | 5 | 5 | **6** — `C-1`..`C-6` | `C-6`, the lease-integrity digest, is the same shape `C-5` was at v2.1 |
| centralized accessors | 5 | 5 | **5** | one hashing accessor with three evaluations; no sixth accessor |
| verifier rules | 13 | 15 | **16** — `S-25a`..`S-25p` | `S-25p` added; `S-25n′` replaces `S-25n` |
| behavioural tests | 17 | 21 | **26** — `A-T1`..`A-T26` | `A-T22`..`A-T26`; rows 92–117 |
| governed mapping Names | 3 | 3 | **3** | unchanged |
| governed mapping producers | 4 | 4 | **5** | `MS-14` |
| carrier Names | 3 | 3 | **5** | `lease_bytes` (X `R-1`) and `lease_canonical_bytes` (forced by `MS-13`'s write position) |
| approved call-site rows | 12 | 12 | **15** | `MS-1L`, `MS-13`, `MS-14` |
| pinned root literals / path Names | — | 1 / 1 | **2 / 2** | `T_ACTIVE_LEASES`, `lease_path` |
| read functions / call sites | — | 1 / 2 | **1 / 3** | `MS-14` |
| write calls | — | undistinguished | **2** | `MS-12`, `MS-13` (X `D2`) |
| `ACC-5` evaluations | "1" *(contradicted)* | 2 | **3** | `EV-3`, on the §2 audit |
| persistent digest values | 1 | 1 | **2** | claim lineage; lease integrity |
| transient digest values | — | 1 | **1** | unchanged |
| direct destinations of the claim lineage digest | 2 | 2 | **2** — `D-1`, `D-2` | **unchanged; `LD-1` re-derives why `EV-3` is not a third** |
| transitive continuations | — | 5 | **5** — `L-1`..`L-5` | unchanged; `LD-2` keeps `EV-3` outside them |
| declassifying operations | "1" | 1 | **1** | unchanged |
| content-alias residual members | — | 1, mis-disposed | **5** — `CA-1`..`CA-5` | Y `Y2` |
| retained-behaviour fixtures | — | 4 | **6** — `R-a`..`R-f` | X `R-3` |
| handoff steps | 11 | 13 | **15** | `STEP 14` (the audit), `STEP 15` (the residual) |
| sentences withdrawn this round | 2 | 6 | **7** — `R-W9`..`R-W15` | |

**Arithmetic checks.** `S-25a`..`S-25p` is sixteen letters. `21 + 5 = 26` tests.
`12 + 3 = 15` call-site rows. `3 + 2 = 5` carriers. `2 + 1 = 3` evaluations.
`5 + 1 = 6` consumers. `13 + 2 = 15` handoff steps.

---

## §6. No-regression table

Every item was checked against the v2, v2.1 and v2.2 bytes. **The assertion is
the author's; the check is the reviewer's to repeat.**

| Locus | Confirmed by | v2.3 effect |
|---|---|---|
| `X M-1`, `X m-1`, `X m-3`, `Y-C2`, `Y-m1` | both lines, twice | **none** — not in the replacement index |
| `X m-2` (`PID_MAX_LIMIT = 4194304`) | both lines | **none in substance** — `CS-4′(a)` cites it as the size of a *conditional* search space |
| `Y-M1` (`X-1`..`X-4`, `I-1`..`I-10`) | both lines | **none in substance** — `X-1`'s carrier position (`CR-3′(d)`) is unchanged text; no matrix row, conjunct or routing changes |
| `Y-M2` (two superseded schemas) | both lines | **none** — `LD-1` re-derives that the lease carries no claim digest |
| `S-25i`, `S-25i-N1`..`N4` | X: retained `open` is "the correct decision" | **none in text**; `PC-R2′` changes only the two pinned families' read shape, on `protocol :58-72`'s signed authority |
| `M-R1`, `M-R2`, `M-R3`, `M-R5`, `S-25j` + scope note | X: eight routes closed | **none** |
| `CR-1`, `CR-4`, `S-25k` | X: slicing/decode/regex/second-hash/inline-parse closed | **none in text**; domain extended by `CR-2′` |
| `MS-1`, `MS-4`, `MS-5`, `MS-8`, `MS-9`, `MS-12`, `MS-R1`..`MS-R4` | X: twelve rows | **none** |
| `ACC-4`, `ACC-5`, `ACC-R1`..`ACC-R5` | X and Y | **none** — five accessors, `ACC-R5`'s no-field-extraction now load-bearing for `C-6` |
| `EV-1`, `EV-2`, `OD-1`..`OD-4`, `S-25o` | X and Y: exhaustive, non-overlapping | **none**; `EV-R4` states disjointness |
| `D-1`, `D-2` | X and Y, three rounds | **none** — still exactly two |
| `L-0`..`L-5`, `L-R1`, `L-R2` | X verified each at its locus; Y §3.2 | **none** |
| `DC-2`, `DC-3′`, `DC-4′`, `DC-5′`, `DC-7` | X and Y: authorization boundary preserved in full | **none** |
| `WL-1`, `WL-2`, `WL-4′`, `WL-R1`, `CS-1`..`CS-3`, `CS-5`..`CS-7`, `CS-P1`..`CS-P7` | X `Determination 6`: "closed"; Y §4 | **none** — only `CS-4` and `WL-3′` are replaced |
| `RC-1`..`RC-4`, `NC-1`..`NC-3` | X | **none** |
| `P-R1`..`P-R5` | X | **none in text**; `P-R1`'s list reads `C-1..C-6` |
| §3.5 model choice, §3.6 destination search | X and Y | **none** |
| `N-1`..`N-9`, the author recommendation, Option B's non-selectability | both lines | **none**; `N-10` adds an explicit no-scientific-cell statement |

---

## §7. One bounded question per reviewer

### §7.1 To the X line (Claude Code Opus, independent engineering review)

> **With both identity-bearing families now pinned (`PA-1′`, `MS-1L`,
> `lease_path`, `MS-13`, `MS-14`, `CR-2′`'s five carriers, `M-R4′`'s five
> producers), with write calls separated from read calls (`PA-6′`), with
> constant and no-stem paths admitted (`PA-5′(b)`, `PA-3′(b)`), and with
> `MS-2` descriptor-anchored: is the rule set now (a) CLOSED — is there any AST
> in the five roots that reaches `controller_pid` or `process_group_id`, from
> either record, while satisfying `S-25a`..`S-25p`; and (b) SATISFIABLE — does
> every operation the signed chain requires (the two installs, the three reads,
> the three evaluations, the three `/proc/self/fd` enumerations, every constant
> durable path, and every `PC-N` peer read) have a spelling that passes?**
>
> If (a) fails, the deliverable is the AST. If (b) fails, the deliverable is the
> signed operation that has no conforming spelling, with its locus.

### §7.2 To the Y line (GPT Sol, independent validity/governance review)

> **With `PT-1′` narrowed to pathname denotation, `CA-1`..`CA-5` named as one
> open external residual, the gate `PG-1`..`PG-7` requiring no-follow by flag,
> regular file, `st_nlink == 1`, held-descriptor path identity and a path-bound
> exact-schema discriminator before any parse, return or value binding, with
> `PG-5` routing claim- or lease-shaped content at any `PC-N` path to dominant
> invalidity, and with `CS-4′`/`WL-3″`/`CS-8` restating the information fact
> conditionally: (i) is the governance consequence of the alias class now
> CONTAINED — can aliased or copied restricted content still become an ordinary
> mapping, a bound value, a record, a comparison, a resource fact or a
> scientific fact; and (ii) does any sentence in v2, v2.1, v2.2 or v2.3 still
> assert a confidentiality guarantee, its universal absence, or a
> recoverability/entropy claim without its conditioning fields?**
>
> If (i) fails, the deliverable is the surviving route from aliased content to a
> valid Officina fact. If (ii) fails, the deliverable is the surviving sentence
> and its locus.

---

## §8. Remaining weak points

The author's nine disclosed weak points are at v2.3 §9 and are summarized here
so a reviewer can triage them:

```text
1  THE GATE'S COST, AND THE ONE NEW CONJUNCT. Three PG-3 conjuncts and the
   no-follow flag are already signed at protocol :58-72 / contract :190-200 for
   the named runtime artifacts; st_nlink == 1 is NOT in the live tier (only in
   the superseded control-channel chain, cited as provenance), and extending the
   discipline to unnamed PC-N records is this packet's own requirement. Priced
   at B-A8. DESIGN CHOICE A REVIEWER MAY REVERSE.
2  PG-4 IS A RUNTIME PREDICATE. S-25p enforces its presence, its position and
   its failure successor, not its correctness. This is a real, disclosed
   weakening of the all-static property. DISCLOSED RESIDUAL.
3  EV-3/C-6 REST ON THE §2 AUDIT. If contract :576's implementation-surface row
   is read as non-normative, or settlement later moves out of generic_harness.py,
   DC-6″'s inventory must be re-scoped, not deleted. CHECK THE AUDIT, NOT THE
   CONCLUSION.
4  FIVE CARRIERS, NOT THE FOUR X R-1 NAMED. The fifth is forced by MS-13's write
   position. DECLARED DEVIATION.
5  FIVE MS FUNCTIONS RENAMED DESCRIPTIVELY. MS-R6 states shape, operand count,
   result kind and single definition are unchanged. PRESENTATIONAL; REVERSIBLE.
6  CS-4′(c) LEAVES THE DIGEST-ONLY READER GENUINELY OPEN. No bound is supplied
   in either direction, and none may be cited from this chain. DISCLOSED.
7  M-R4′ NOW LEANS ON THE GATE for every non-pinned pathname. If PG-1..PG-7 are
   judged insufficient, M-R4′(ii) fails with them. STATED IN THE OPEN.
8  EVERYTHING STILL RESTS ON EXACTLY FIVE PRODUCTION ROOTS — including the §2
   audit, whose third step is membership in that list. DISCLOSED RESIDUAL.
9  THE NO-REGRESSION ASSERTION IS THE AUTHOR'S. INSTRUCTION TO THE REVIEWER.
```

Items 1, 4 and 5 are **design choices a reviewer may reverse**. Items 2, 3, 6, 7
and 8 are **disclosed residuals**, not proposals. Item 9 is an **instruction to
the reviewer**.

---

## §9. Verdict and negative authorization

```text
READY_FOR_OFFICINA_P1_IDENTITY_V2_3_FINAL_XY_CONFIRMATION
```

The verdict asserts exactly this and nothing more: in the author's judgement the
findings the two binding `REVISE` verdicts named are repaired exactly — the
second identity-bearing record pinned with the same instruments and every count
re-derived; the rule set made internally satisfiable so that the signed installs,
the exact-constant descriptor paths and the constant durable paths have conforming
spellings; `PT-1` narrowed to the pathname theorem it actually proves, with the
content-alias class named honestly and its governance consequence contained by a
read gate and dominant invalidity rather than denied; the third evaluation
located on the signed bytes rather than guessed, and named with its consumer; and
the information statement made conditional everywhere, including the summaries —
and that the bytes are therefore **fit to be reviewed**. It asserts no
correctness that a confirmation line has not independently established.

**This closure authorizes nothing.** Not Kirill's identity author selection, not
the `P1_IDENTITY_OBSERVATION_BOUNDED_WEAKENING_V1` token, not implementation, not
a verifier or manifest edit, not a commit, not a code or test artifact, not
activation, not process control, not resource use, not entropy, not data, not a
trajectory, not spend, not custody disposition, not a datum, outcome, Proof or
claim movement. **Kirill's author selection remains unauthorized pending both
bounded final confirmations on these exact bytes**, and neither this closure nor
the correction it accompanies may be read as advancing it by one step. No
existing file was modified in producing this round; its sole products are the
v2.3 correction and this file.

```text
T = NOT_ACTIVATED
PROGRAMME CLAIM = OPEN
WATCHDOG-FREEZE CHOICE = UNRESOLVED AND ORTHOGONAL
IDENTITY SELECTION = NOT MADE, NOT AUTHORIZED
OPTION A = RECOMMENDED, UNSELECTED
OPTION B = NON-SELECTABLE
```
