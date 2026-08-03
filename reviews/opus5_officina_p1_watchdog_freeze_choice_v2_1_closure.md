READY_FOR_OFFICINA_P1_WATCHDOG_FREEZE_CHOICE_V2_1_FINAL_XY_CONFIRMATION

# Author closure — P1 watchdog-freeze choice correction v2.1

**Author:** Claude Code Opus 5, **specification author only**. I authored the
whole supervisor/control-channel chain, the identity packet that reported this
blocker, the v1 and v2 choice packets, the v2 closure, and this v2.1 correction.
I am therefore **disqualified** as its independent X-line or Y-line reviewer,
and **this closure is an untrusted author self-assessment**.

**No choice was made and no token was accepted or minted.** Both selection
tokens and all six amendment tokens exist only as text in draft documents
awaiting a bounded independent final confirmation round.

`T = NOT_ACTIVATED`; programme claim `OPEN`. This round produced no selection,
X/Y verdict, amendment acceptance, implementation, code or test edit, verifier
or manifest change, process or behavioural probe, activation, entropy, E1/E2/E3
spend, Q/C work, datum, outcome, Proof or claim movement.

---

## 1. Deliverables and untouched-file confirmation

Exactly two new files. **No existing file was modified.**

| Path | Lines |
|---|---|
| `successor/OFFICINA_P1_WATCHDOG_FREEZE_AUTHOR_CHOICE_PACKET_V2_1_CORRECTION.md` | 1139 |
| `reviews/opus5_officina_p1_watchdog_freeze_choice_v2_1_closure.md` | this file |

`successor/OFFICINA_P1_WATCHDOG_FREEZE_AUTHOR_CHOICE_PACKET_V2_DRAFT.md`,
`successor/OFFICINA_P1_WATCHDOG_FREEZE_AUTHOR_CHOICE_PACKET_V1_DRAFT.md`,
`reviews/opus5_officina_p1_watchdog_freeze_choice_v2_closure.md`,
`reviews/opus_officina_p1_watchdog_freeze_choice_v2_confirmation.md`,
`reviews/sol_officina_p1_watchdog_freeze_choice_v2_confirmation.md`,
`reviews/opus_officina_p1_watchdog_freeze_choice_review.md` and
`reviews/sol_officina_p1_watchdog_freeze_choice_review.md` are
**byte-untouched**, as §2.1 demonstrates by recomputing their digests.

Only read-only commands were run: `git status`, `git log`, `git ls-files`,
`grep`, `sed`, `wc`, `sha256sum`. No test, behavioural probe or process-control
operation was executed. No code was implemented. No `T` state was touched.

---

## 2. Hashes and custody

### 2.1 Reviewed inputs, recomputed on committed bytes

```text
72212a986d9551ef47718e871a81951b55a849a10d34eb12e6276499cb675505  successor/OFFICINA_P1_WATCHDOG_FREEZE_AUTHOR_CHOICE_PACKET_V2_DRAFT.md
7b3708550806fcd5742accb5858a2da05a87c4b22ee7fbdffe73ecdbad07759e  reviews/opus5_officina_p1_watchdog_freeze_choice_v2_closure.md
23e93c7b028d0a7e36c9cd42baf1a03ade0b3cf0e5f18dad3f2d772ce3584b10  reviews/opus_officina_p1_watchdog_freeze_choice_v2_confirmation.md
a4de28727eb25e7879608fd2f9c22a62c0b42086d8d3cbcfd72e478d28147fca  reviews/sol_officina_p1_watchdog_freeze_choice_v2_confirmation.md
15937b84b2e2a61de3d908ea014cbded902ca5ba15f58b988920c99be0702f09  successor/OFFICINA_P1_WATCHDOG_FREEZE_AUTHOR_CHOICE_PACKET_V1_DRAFT.md
d8d3ced2aee226673903223250d810a5e574362132aafa644515c150c05f0cdb  reviews/opus5_officina_p1_watchdog_freeze_author_choice_packet.md
c87cc69f93ddd64c8364bcbcce3fa97e32855b55597a57a44bb05bffeee04ae1  reviews/opus_officina_p1_watchdog_freeze_choice_review.md
37474607e46394178d9dca1f946fd68e58f852cf3157b7948a6e7de6ef13808b  reviews/sol_officina_p1_watchdog_freeze_choice_review.md
```

**The first two digests are exactly the two target digests BOTH v2
confirmations independently recomputed and declared matching** (X §0, Y "Custody
and authorization boundary"). So the bytes v2.1 repairs are exactly the bytes
both `REVISE` verdicts were issued against. The last four pin the v1 record
unchanged across three rounds.

### 2.2 Governing contracts, recomputed on committed bytes

```text
2c857fa8ad7be1c861eb8cf561f396e7d2339403c7714abc7958745bf34e5d5d  successor/…SUPERVISOR_CONTROL_CHANNEL_P1_OPERATIVE_COMPOSITE_V1_2.md
6197d2a4073d35fc978119db32128c50d12594343ac87731640a1d8e19f09e84  successor/…SUPERVISOR_CONTROL_CHANNEL_V2_1_10_4_P1_BINDING.md
9f1d018e7630d00da954910fa92cacc8005e0ecff90372e513f2fcec8593818b  successor/…SUPERVISOR_CONTROL_CHANNEL_V2_1_CORRECTION.md
ee3171724c89bd7e8f890141f42bf478838608c6f1908f9284218f1e940be635  successor/…SUPERVISOR_CONTROL_CHANNEL_V2_1_1_CORRECTION.md
2cd8b7b53c8efc292535ef79f38aa5e33ce57c5834138cc3deb1700f7edae373  successor/…SUPERVISOR_CONTROL_CHANNEL_V2_1_2_CORRECTION.md
cd106d7fef491601f9ff948aba3ba0ceaac0774ac18a6564247c0c5899b4c40c  successor/OFFICINA_T_ACTIVATION_PROTOCOL_V2_CORRECTION.md
c494ef8884948bd0e737373d2d57a3ab74bbd456db2c3463711c4405f2fdf86a  successor/OFFICINA_SUPERVISOR_AUTHOR_SELECTIONS_V1_SIGNATURE.md
```

**Every digest matches what the v2 closure recorded and what both v2
confirmations independently recomputed.** The custody chain is byte-intact
across all three rounds. The C1 selection whose role this cell reassigns remains
`I_SELECT_SUPERVISOR_WATCHDOG_C1_DEDICATED_FREEZER`
(`…SUPERVISOR_AUTHOR_SELECTIONS_V1_SIGNATURE.md:18`), unrevoked and not re-run.

### 2.3 Produced this round

```text
947ed6a954f87eb3971218f9fa2bfa6461999a9a099eb182bc0a09b2f505eed2  successor/OFFICINA_P1_WATCHDOG_FREEZE_AUTHOR_CHOICE_PACKET_V2_1_CORRECTION.md
```

**On this closure's own digest.** A file cannot contain the SHA-256 of its own
committed bytes without a fixpoint, so this closure does not embed it. Recompute
it with:

```bash
sha256sum reviews/opus5_officina_p1_watchdog_freeze_choice_v2_1_closure.md
```

Custody stays acyclic: v2 packet → v2 closure → two `REVISE` confirmations →
v2.1 correction → this closure → the final X/Y confirmation → any future
signature. The correction contains none of its own digests.

### 2.4 New evidence read this round, by source location

Every citation added in v2.1 was read from the committed bytes of the contracts,
not from either confirmation's quotations:

```text
§P1-3.4 primitive binding block             composite :402-426
§P1-3.5 primitive identity validation,
  the integer-constant row                  composite :428-446
§P1-3.6 no rebinding, local-name rule       composite :448-457
§P1-2.1 platform pin (Linux/x86_64/3.12.3)  composite :233-247
_clock's three existing monotonic samples   composite :636, :1673, :1795
grep: zero CLOCK_ tokens in the composite   verified this round
§P1-9.2 property 11 rationale               composite :1459-1463
§P1-10.5 "killpg only against a
  kernel-verified group"                    composite :1655-1656
§P1-11.4 supervisor continuation step 2     composite :1781-1782
R-L1..R-L5 layer/ownership rules            composite :2011-2032
§P1-13.2 row 4 in full                      composite :2232-2302
  key set / logical writer                  :2240-2248
  executing process                         :2249-2253
  discriminator block                       :2254-2257
  P1 invariant block                        :2270-2275
  rationale ¶                               :2278-2287
  "what P1 replaced" ¶                      :2289-2293
  adjacent peer artifacts ¶                 :2295-2302
§P1-13.3 SIGNAL_GROUP mediation row         composite :2312
§P1-13.6 SW-1..SW-5                         composite :2333-2352
§P1-13.7 implementation surface table       composite :2359-2372
§P1-13.8 reader sentence                    composite :2385-2393
§P1-14.6 S-1..S-24b, highest rule S-24b     composite :2556-2635
§P1-14.7 runtime preflight                  composite :2643-2652
invariants 57..65, 84..91, highest row 91   composite :2726-2760
binding's seven mirror statements           …P1_BINDING.md:564-567, :579,
                                            :629-630, :660-663, :860-863,
                                            :932, :933
§N5.1 fallback namespace and id preimage    …V2_1_2_CORRECTION.md:830-851
§N5.2 fallback schema key set               …V2_1_2_CORRECTION.md:853-869
§N5.3 routing and supervisor authority      …V2_1_2_CORRECTION.md:876-886
§N5.4 field block + legal example           …V2_1_2_CORRECTION.md:888-910
§N5.5 production/duplicate/conflict/order   …V2_1_2_CORRECTION.md:912-937
§N5.6 t-replacement-freeze.v1 (NOT amended) …V2_1_2_CORRECTION.md:957, :976
§N10.2 fact-location table row              …V2_1_2_CORRECTION.md:1370
§N11 crash-cut example row                  …V2_1_2_CORRECTION.md:1416
grep: every pgid / start_identity site in
  …V2_1_2_CORRECTION.md, classified         verified this round
§W3.3 freeze procedure, <process_id>.json   …V2_1_CORRECTION.md:744-770, :763
```

---

## 3. The five-row replacement index

| # | Finding | Class | Locus replaced | v2.1 locus | Status |
|---|---|---|---|---|---|
| 1 | X `R-A` — `CLOCK_MONOTONIC` undisclosed | must fix | v2 §3.6 `C-4` clock expression; §5.2 binding disclosure; §9.1 row; §10 blast-radius row; §12.0 / §12.2 handoff; §12.0 item 9 | **§1** (`B-1`..`B-8`, tests 92–95, §1.4 table replacements) | **CLOSED** |
| 2 | X `R-B` — audit incomplete; invariant 89 rejects the classifier | must fix | v2 §7 in whole — §7.2 twelve sites, §7.3 `R1`..`R12`, §7.4 headline; §9.1 row; §10; §12.0 item 6 | **§2** (§2.2 count, §2.3 twenty-two sites, §2.4 `R1`..`R22`, §2.5, tests 96–100) | **CLOSED** |
| 3 | Y `YV2-M1` — count-key rename surface incomplete | Major | v2 §6.3 table and its "exactly one … sentence" claim; §12.0 item 8 | **§3** (`K1`..`K5`, §3.3 negative surface, §3.4 count, tests 101–102) | **CLOSED** |
| 4 | Y `YV2-M2` first half — `R2` conflates the two schemas | Major | v2 §7.3 `R2` | **§2.4 `R2`**, with the separation rule at **§4** (`SEP-1`..`SEP-3`) | **CLOSED** |
| 5 | Y `YV2-M2` second half — `R9` carries the fallback route; `R10` must stand | Major | v2 §7.3 `R9`; `R10` retained | **§2.4 `R9`/`R10`**, with `D-1`..`D-4` at **§5** | **CLOSED** |

**Nothing else was changed.** Four consequences of rows 1 and 2 are disclosed at
correction §6 as `O-5`..`O-8`; none is a mechanism change and none opens a cell.

---

## 4. One-to-one disposition of the four residual findings

### 4.1 X `R-A` — undisclosed constant `CLOCK_MONOTONIC`

| Element the X line required | Where v2.1 does it | Exact |
|---|---|---|
| disclose `CLOCK_MONOTONIC` as a **second** pinned-integer-constant addition to §P1-3.4, companion to `_MSG_EOR` | §1.2 `B-1` | the list is extended by exactly two names, appended in order `… _MSG_EOR _CLOCK_MONOTONIC`, so `S-3`'s "exactly the list of §P1-3.4, in that order" stays decidable |
| pin its **source** | §1.2 `B-2` | the Attribute `time.CLOCK_MONOTONIC`; `time` is already one of the six modules `S-1` admits and already supplies `_clock`; **no new import, module or primitive** |
| pin its **value** | §1.2 `B-3` | `_CLOCK_MONOTONIC == 1`, added as a literal conjunct to §P1-3.5's integer-constant row, exact under §P1-2.1's Linux / x86_64 / CPython 3.12.3 platform pin |
| pin its **validation** | §1.2 `B-4` | the extended §P1-3.5 check runs in the §P1-14.7 preflight; failure is `PRIMITIVE_NOT_GENUINE`, fail-closed, **no fork, no lock acquisition, no record installed** |
| **refuse structurally** on a runtime-binding mismatch | §1.2 `B-4` | "no degraded mode, no substitute clock id, no continuation on a mismatch" |
| **no silent implicit default clock** | §1.2 `B-5`, `B-7` | a zero-argument `_clock()` is forbidden in both roots, enforced statically by new rule `S-25`, not by prose |
| pin the **exact use** by `_clock(…)` for `freeze_ns` | §1.2 `B-6` | v2 §3.6 `C-4`'s clock expression is withdrawn verbatim and replaced by `freeze_ns := _clock(_CLOCK_MONOTONIC)`, sampled on the proving pass and never the signal-send time |
| count it in **both options'** blast radius | §1.4, §8, `B-8` | §9.1's row, §10's row and §12.0's new common item `1b` all carry both names for both selections |
| count it in the **binding-block handoff** | §7 item `1b` | moved out of the W-B-only list (v2 §12.2 item 12 **deleted**) into §12.0 as common |
| count it in **verifier rules** | §1.2 `B-7` | `S-25`, the next free number after `S-24b` |
| count it in **tests** | §1.3 | rows 92–95 |

**Author-flagged deviation, stated rather than made silently.** The X line named
the constant `CLOCK_MONOTONIC`; v2.1 binds it as **`_CLOCK_MONOTONIC`**, because
§P1-3.4 binds every constant under an underscored local name and §P1-3.6 requires
every later use to go through that local name. Same constant, contract-conformant
spelling. This is put to the X line as the first half of its bounded question.

**Author-found consequence, `O-7`.** `S-25` is uniform over both roots, so it
also pins the composite's **three pre-existing** monotonic samples (`:636`,
`:1673`, `:1795`), which the composite describes as monotonic without ever naming
a clock id. The X line identified that under-specification as **pre-existing**;
v2.1 repairs it once for every site rather than only for `freeze_ns`.

### 4.2 X `R-B` — the freezer / witness and execution-site audit

| Element the X line required | Where v2.1 does it |
|---|---|
| add **§P1-13.2 row-4 rationale ¶, `:2278-2287`** ("dedicated freezer watchdog as the normal witness", "two possible executing processes") | **site 17**, replaced whole by `R17` |
| add **the freeze-evidence reader sentence, `:2389`** | **site 20**, replaced by `R20` |
| add **invariant 89, `:2758`** | **site 21**, replaced by `R21` |
| **re-audit the whole composite** and give the **final exact site count** | §2.2 and §2.3: **twenty-two**, of which ten are new — the X line's three plus **seven found only by this re-audit** (`:1459-1463`, `:1781-1782`, `:2254-2257`, `:2270-2275`, `:2337-2341`, `:2368`, `:2760`) |
| **do not preserve "twelve-site" wording** | §2.1 withdraws every "twelve" sentence verbatim from §7.2/§7.3/§7.4/§9.1/§10/§12.0 and states that the word is not restated in paraphrase |
| **replace, not append to,** every contradictory sentence | §2.4: every one of `R1`..`R22` is a replacement; §7 handoff items 6 and 6b say "REPLACE contradictory rows, sentences and blocks; do not add beside them" |
| in invariant 89, **admit the PCS autonomous §3 classifier `_killpg` path** as a signed freeze-execution site | `R21` site **(b)**: the §P1-10.7 classifier, in the PCS root, under `KV-1..KV-6` before every `_killpg`, against the §3.5 scope |
| **distinguish it from the request-driven `SIGNAL_GROUP` opcode** | `R21`: site (a) is `SIGNAL_GROUP`-mediated and **may not bypass it**; site (b) is "request-driven by no peer opcode" and "not `SIGNAL_GROUP`-mediated"; also `R19`, which splits §P1-13.7's group-stop row into a mediation row and an execution row |
| **retain the sole-PCS-caller rule** | `R21`: "both sites' `_killpg` executes in the PCS root and nowhere else, so the PCS remains the sole caller of `killpg` and `S-12` is retained unchanged"; correction `N-3`; handoff item 5; test 97 |
| **reject every other writer / executor** | `R21`: a freeze observation written by a process that is not the supervisor role is rejected; any other executor of a freeze group stop is rejected |
| keep **PCS journal state scientifically invisible** and **distinct from peer freeze evidence** | `R21`'s closing clause: the terminal, the per-group tokens and `freeze_ns` are never a `t-freeze-observation.v1`, never a fallback field, never an input to any peer validity predicate (`L8`, `ND-1..ND-3`); **test 98** fails any build in which one reaches a peer artifact, predicate, qualification, comparison, Q/C fact or published record |
| close the audit in **both directions** | §2.3's "checked and confirmed NOT to need amendment" list: invariants 57, 60, 62, 65, 84, 85, 86, 88, 90; `R-L2`, `R-L4`, `R-L5`; §P1-10.5 `:1655-1656`; §P1-13.3 `:2312`; row 4's path/schema/key set/logical writer/readers/durability/deletion; the "what P1 replaced" ¶; the adjacent-artifacts ¶; row 3's freeze-evidence readers; the C1 cell token; the P1 cell text; `S-12` |

**The substantive point, not the enumeration.** Before this correction the
composite enforced a single model in which every freeze group stop is
`SIGNAL_GROUP`-mediated (invariant 89, `:2287`, `:2368`, `:2389`). v2 introduced
a PCS-side classifier that calls `_killpg` directly and never reconciled the
invariant that forbade it — v2's own new verifier rule already assumed two
`_killpg` call sites. `R19` and `R21` make the **two signed freeze-execution
sites** explicit. §2.5 states plainly that this is a real cost **both** options
carry, because §3 is common, and that it separates nothing.

### 4.3 Y `YV2-M1` — the count-key rename surface

| Element the Y line required | Where v2.1 does it |
|---|---|
| in §6.3 **and** the v1.3 handoff, enumerate and replace all four remaining references | §3.2 `K2`..`K5`, plus `K1` for the §N5.2 key list v2 had already named; §7 handoff item 8 |
| §N5.4 field-definition block, `:900` | `K2` — `current_unresolved_member_count_or_null`, with the biconditional stated |
| §N5.4 legal `FREEZE_INSTANT_UNKNOWN` example, `:906` | `K3` — renamed key, **integer `0` retained** |
| §N10.2 fact-location table, `:1370` | `K4` — renamed key, with the `(null, UNKNOWN)` pair named for the `rejection_conjunct == 0` branch |
| §N11 crash-cut example, `:1416` | `K5` — renamed key, **integer `0` retained** |
| each must use `current_unresolved_member_count_or_null` | all five, verbatim |
| generic definitions say **null iff `rejection_conjunct == 0`** | `K1`, `K2`, `K4` |
| non-`ABSENT` examples **retain integer `0`** | `K3`, `K5`, each stating why: they are `rejection_conjunct != 0` branches where the field is a mandatory non-null integer |
| update **schema / readers / examples / tests** | schema `K1`; the fact-location row `K4`; examples `K3`/`K5`; tests 101–102. §3.3 records the verified fact that **no signed acceptance predicate, validity conjunct or settlement rule reads the fallback count**, so this is a rename surface and not a predicate change — exactly Y's determination |
| update the **claimed reopened-sentence count exactly** | §3.4: v2 said **one** sentence; the correct number is **five**. The file count (one), key count (three) and branch count (one) are unchanged |

**Closed in both directions.** §3.3 records that `unresolved_member_count` — the
key of the watchdog-written `t-freeze-observation.v1` (composite `:2243`), bound
by §Z4.6 conjunct 9 as narrowed at §N5.4 `:890-894` — is a **different key on a
different schema** and is **not** renamed; and that `pgid` / `start_identity`
occur in the fallback schema at exactly one locus (`:860`), every other
occurrence belonging to §N3's spawning records or §N5.6's
`t-replacement-freeze.v1`, neither amended. For those two keys v2's
one-sentence claim was correct and stands.

### 4.4 Y `YV2-M2` — the two observation schemas

| Element the Y line required | Where v2.1 does it |
|---|---|
| replace §7.3 `R2` so row-4 `t-freeze-observation.v1` is written **only** by the supervisor on the signed dead-watchdog route | §2.4 `R2` — v2's text withdrawn verbatim; the replacement names the class, its path `WATCHDOG/FREEZE/`, and "by no other process on any path" |
| state **separately** that §N5 `ABSENT` writes `t-freeze-fallback-observation.v1` under `WATCHDOG/FREEZE_FALLBACK/` | §2.4 `R2`'s second half, and §4 `A-1`/`A-2` citing `…V2_1_2_CORRECTION.md:856-857` and `:842` |
| **never** assign the fallback to the row-4 writer / class / namespace | §4 `SEP-1`, applied to every replacement text, handoff item and test row; test 100 fails any build that installs the fallback under `WATCHDOG/FREEZE/`, validates it with row 4's predicate, or writes it with row 4's writer |
| remove §N5 `ABSENT` from `R9`'s row-4 executing-process clause | §5 `D-1`; §2.4 `R9` — v2's text withdrawn verbatim; the replacement names exactly one executing process and states the fallback "is NOT an executing-process branch of this row" |
| keep `R10` **semantically unchanged** | §5 `D-2`; §2.4 `R10` retained verbatim: "called from the supervisor's dead-watchdog route only" |
| update the closure dispositions for X `F1`/`F3` and Y `Y-C3` | §5 `D-4` and §5 of this closure |

**The authority for the separation is signed and was already in the composite.**
`:2295-2302` names the freeze fallback and the replacement-freeze record as "two
adjacent peer artifacts … named so their absence from this table is not read as
an omission … so that no implementer collapses them." §2.3 records that sentence
as **checked, unchanged and load-bearing**.

**A consequence the Y repair forces, disclosed.** Once row 4 has exactly one
executing process, four composite sentences that assert row 4 is the multi-process
`R-L5` case become false: the row-4 discriminator block (`:2254-2257`), the
rationale ¶ (`:2278-2287`), `SW-2` (`:2337-2341`) and invariant 91 (`:2760`).
They are sites 15, 17, 18 and 22, replaced by `R15`, `R17`, `R18` and `R22`.
**The peer schema is not amended**: `killer` remains a mandatory key of
`t-freeze-observation.v1`, retained, with value `SUPERVISOR` on every reachable
path.

---

## 5. Corrected dispositions for X `F1`, X `F3` and Y `Y-C3`

The v2 closure marked all three **CLOSED**. Both confirmations found that
premature. This closure restates them honestly:

| Finding | v2 closure said | Both confirmations said | **v2.1 says** |
|---|---|---|---|
| X `F1` freezer/witness surface not fully enumerated; handoff self-contradicting | **CLOSED** | X: "SUBSTANTIALLY CLOSED — residual `R-B`". Y: "**Not fully closed**" on `R2`/`R9` | **NOT closed by v2. Closed by v2.1 §2 and §5.** The v2 closure's `F1` row is superseded: twelve was the wrong count (twenty-two), and `R2`/`R9` were internally inconsistent with `R10`. The v2 closure's claim that "the audit is closed in both directions" was true only of the two sites it checked; §2.3 now checks twenty-one further sites and rules them fine |
| X `F3` `ABSENT` route unconstructible | **CLOSED, constructively** | X: **CLOSED**. Y: "**Not fully closed** … the global count-key rename omits four normative references" | **Closed on VALUES by v2 (`A-ABS-1..6`), closed on the RENAME SURFACE only by v2.1 §3.** Both halves are now closed |
| Y `Y-C3` identity-cell entanglement at `ABSENT` | **CLOSED** | X: **CLOSED**. Y: "**Not fully closed only on the rename surface** identified in `YV2-M1`" | **Same as `F3`.** The orthogonality itself was and is established: the `EVIDENCE_ABSENT` branch is constructible under either identity outcome, with `process_id` a constructible opaque claim identifier and not a PID |

---

## 6. No-regression table — every already-closed finding, re-checked against v2.1

| Finding | Closed by | Confirmed by | Does v2.1 touch it? | Regression check |
|---|---|---|---|---|
| **X `F2`** EOF/death conflation; `MSG_EOR` discrimination | v2 §5.2 `E-1`..`E-4` | X **CLOSED**, Y **Closed** | **Only in accounting.** `O-7` moves `_MSG_EOR` from W-B's blast radius to both options' | **NO REGRESSION.** `E-1a`/`E-1b`/`E-1c`, the four indistinguishable causes, the withdrawn `SUPERVISOR_LOST` name and the withdrawn same-event claim are byte-unchanged. The constant is the same constant; only which option is charged for it changed, and the change removes a W-A advantage |
| **Y `Y-C1`** total constructible classifier | v2 §3 | X **CLOSED** (determination 2 verified in full), Y **Closed** | **One expression only:** §3.6 `C-4`'s clock call | **NO REGRESSION.** `STAT_OBSERVE_G`'s indices, `KV-1..KV-6`, `P-1..P-3`, `SC-1..SC-4`, the total handle-state table, the sixteen closed tokens, §3.7's continuations, §3.8's three terminals, §3.9's `S-1..S-4` and §3.10's residual are untouched. The sampled quantity, the pass it is sampled on and its use are unchanged; only the clock id is now named and pinned |
| **Y `Y-C2`** W-A one-shot capability and pricing | v2 §4.2, §4.3, §4.6 | X **CLOSED** (determination 5), Y **Closed** | **No** | **NO REGRESSION.** The four-field constant grammar, the constant key `(generation_id,"WDFREEZE",watchdog_handle_id)`, exactly-one-accepted-action, `G-1..G-4`, and `P-1..P-4`'s full-charge pricing are untouched. `R13`'s W-A variant *cites* `G-1` and does not modify it |
| **Y `Y-M1`** endpoint loss is not death | v2 §5.2, §5.4, §8 `L7` | X **CLOSED**, Y **Closed** | **No** | **NO REGRESSION.** `PEER_CONTROL_ENDPOINT_LOST` remains the only name; `E-4`'s two-independent-descriptors statement stands; no ordering, simultaneity or causal identity is asserted anywhere in v2.1. `R13` and `R14` are careful not to reintroduce death language |
| **Y `Y-M2`** record before act | v2 §5.5 `R1`..`R6`, §5.6 | X **CLOSED**, Y **Closed** | **No** | **NO REGRESSION.** `ACCEPTED`+fsync before any signal, the stale-head check, `COMPLETED` only on `FREEZE_TOTAL_PROVED`, and the thirteen-row crash matrix are untouched. **Note on naming:** v2 §5.5's ordering steps are also called `R1`..`R6`; v2.1's `R1`..`R22` are the §7.3 **site replacements**. Two different `R` families, both from v2, neither renamed here — flagged so no reader conflates them |
| **Y `Y-M3`** W-A ordering vs the non-returning reaper | v2 §4.5 `T-1`..`T-7` | X **CLOSED**, Y **Closed** | **No** | **NO REGRESSION.** The bounded 60 s window, its four deterministic ends, `T-4`'s by-definition ordering, `T-5`/`T-6`/`T-7` are untouched. `R11`'s W-A variant and `R21`'s W-A bracket cite the window and do not modify it |
| **Y `Y-m1`** publication caveat | v2 §8 `L6`..`L9`, `ND-1`..`ND-4` | X **CLOSED**, Y **Closed** | **Strengthened, not changed** | **NO REGRESSION.** `L6`..`L9` and `ND-1`..`ND-4` are byte-unchanged. `R21` adds an *enforcement* clause and test 98 for what `L8` and `ND-1..ND-3` already forbid; it adds no permission |
| **Y determinations 1–8** | v2 §3.3 | Y re-affirmed all eight in its v2 confirmation | **No** | **NO REGRESSION.** Determination 4 ("neither successful signalling nor a PCS journal timestamp is scientific evidence") is *reinforced* by `R21` and test 98. Determination 7 ("W-B does not change who may call `killpg`") is *reinforced* by `N-3` and test 97: `R21` admits a second execution **site**, not a second **caller** |
| **X determinations 2, 4, 5, 7, 8** | v2 §3–§9 | X confirmed each | **No** | **NO REGRESSION.** Determination 7's finding that `process_id` is a **constructible opaque claim identifier, not a raw kernel PID** is preserved verbatim in `N-5`; `A-ABS` leaves it mandatory and non-null on every branch |
| **The blocker** | v2 §1, four mechanisms | both lines independently **PROVED**, twice | **No** | **NO REGRESSION.** §1 is untouched; `N-1` restates it |
| **`S-12` retained** | v2 §13 `N-3` | both lines | **Restated and tested** | **NO REGRESSION.** `R21`, `N-3`, handoff item 5 and test 97 each assert `S-12` unchanged |

---

## 7. Final corrected counts and the exact blast-radius delta

```text
NORMATIVE COMPOSITE SITES BOTH OPTIONS AMEND:     22   (v2 said 12)
  carried from v2                                 12
  named by X R-B                                   3   (2278-2287, 2389, 2758)
  found by this correction's re-audit              7   (1459-1463, 1781-1782,
                                                        2254-2257, 2270-2275,
                                                        2337-2341, 2368, 2760)

PEER-CONTRACT SENTENCES REOPENED:                  5   (v2 said 1)
  one file, three keys, one branch — unchanged
  §N5.2 :859-866, §N5.4 :899-902, §N5.4 :905-909,
  §N10.2 :1370, §N11 :1416

PINNED INTEGER CONSTANTS ADDED:                    2   (v2 disclosed 1)
  _MSG_EOR and _CLOCK_MONOTONIC, BOTH on BOTH options

NEW VERIFIER RULES:            v2's classifier rules + S-25
NEW §P1-15 TEST ROWS:          v2's classifier rows + 92..102
SIGNED FREEZE-EXECUTION SITES: 2, explicit (was 1, implicit)
BINDING MIRROR STATEMENTS to carry in step (O-5, NOT in the 22):  7
```

**Exact blast-radius delta, by option.**

| Row | W-A, v2 → v2.1 | W-B, v2 → v2.1 | Moves the comparison? |
|---|---|---|---|
| normative composite prose sites | 12 → **22** | 12 → **22** | **no** |
| peer sentences reopened | 1 → **5** | 1 → **5** | **no** |
| pinned constants added | 0 → **2** | 1 → **2** | **no** — and it **removes** a row that wrongly favoured W-A |
| verifier rules | + `S-25` | + `S-25` | **no** |
| test rows | + 92..102 | + 92..102 | **no** |
| explicit freeze-execution sites | 1 → **2** | 1 → **2** | **no** |
| **topology / opcode changes** | several — **unchanged** | **zero** — **unchanged** | **W-B**, as before |
| **new liveness dependency** | yes — **unchanged** | none new — **unchanged** | **W-B**, as before |

**Every row v2.1 touched falls identically on both options. The two rows that
decide were not touched at all.**

---

## 8. Verdict and recommendation after repair

```text
READY_FOR_OFFICINA_P1_WATCHDOG_FREEZE_CHOICE_V2_1_FINAL_XY_CONFIRMATION
```

**Meaning precisely.** All four residual findings of the two binding `REVISE`
confirmations — X `R-A`, X `R-B`, Y `YV2-M1`, Y `YV2-M2` — are dispositioned
one-to-one at §4, each by a named repair at a named locus, with the five
mandated repairs delivered exactly as specified and no sixth mechanism opened.
Five v2 claims are withdrawn verbatim rather than paraphrased away: the "twelve
site" wording, "the same twelve normative prose changes", §6.3's
"exactly one … sentence" reopening claim, `R2`'s fallback clause and `R9`'s
fallback clause. §6 of this closure re-checks every previously closed finding
against the corrected bytes and finds no regression.

**Recommendation after repair: W-B**, on signed-authority fidelity,
constructibility, mechanical testability, liveness and blast radius only. Both
independent lines reached the same recommendation after their own repairs, and
both re-affirmed it in their `REVISE` confirmations. **The author selects
nothing, accepts no token, mints no token, and predicts no outcome.**

**It does not mean the correction is correct.** This is an author
self-assessment by the party that wrote the defects being repaired, for the
third round running. The prior two author closures each claimed readiness and
each was found defective by independent review.

---

## 9. One bounded confirmation question per reviewer

### For the X line — one question, yes or no

> **Do `§1`'s `B-1`..`B-8` and `§2`'s twenty-two-site audit close `R-A` and
> `R-B` exactly — that is: (a) is `_CLOCK_MONOTONIC` now pinned by source,
> value and validation such that the §3 classifier is executable using only
> §P1-3.4 primitives plus the two disclosed constants `_MSG_EOR` and
> `_CLOCK_MONOTONIC`, with no further primitive, import, constant or module
> required anywhere, and does the underscored spelling and the uniform rule
> `S-25` correctly express what `R-A` asked for; and (b) does the amended
> invariant 89 (`R21`), together with `R19`'s split of the §P1-13.7 group-stop
> row, admit the PCS's autonomous `_killpg` classifier as a signed
> freeze-execution site while retaining the sole-PCS-caller rule and `S-12`
> unchanged, leaving **no** remaining composite sentence, invariant or table row
> that the amendment makes false and that §2.3 lists neither as a replaced site
> nor as checked-fine?**

Answer `YES` or `NO`. A `NO` should name the primitive, constant or import still
undisclosed, or the exact composite line that remains false and appears in
neither of §2.3's two lists.

### For the Y line — one question, yes or no

> **Do `§3`'s `K1`..`K5` and `§2.4`'s replaced `R2`/`R9` with unchanged `R10`
> close `YV2-M1` and `YV2-M2` exactly — that is: (a) does the five-locus rename
> surface leave **no** signed reference to `current_unresolved_member_count` in
> `…V2_1_2_CORRECTION.md`, with the generic definitions stating null iff
> `rejection_conjunct == 0`, the two non-`ABSENT` examples retaining integer
> `0`, and the distinct watchdog-record key `unresolved_member_count`
> correctly left unrenamed; and (b) is the §N5
> `t-freeze-fallback-observation.v1` object now nowhere assigned to the row-4
> `t-freeze-observation.v1` writer, class or namespace — including in the four
> consequential replacements `R15`, `R17`, `R18` and `R22` that follow from row
> 4 having exactly one executing process — while `process_id` remains a
> constructible opaque claim identifier, PCS journal state remains
> scientifically invisible, and §N5.3's routing, unknowable pool and full
> charging remain unchanged?**

Answer `YES` or `NO`. A `NO` should name the remaining old-key reference, or the
exact sentence that still conflates the two schemas or the two namespaces.

**Both lines should also confirm, as part of the same bounded round,** that the
seven previously closed findings (`F2`, `Y-C1`, `Y-C2`, `Y-M1`, `Y-M2`, `Y-M3`,
`Y-m1`) remain closed on the corrected bytes as §6's no-regression table claims;
that the corrected counts of §7 are exact; that the `O-5`..`O-8` disclosures are
correctly classified as consequences and disclosures rather than new cells; and
that the recommendation basis is unchanged.

---

## 10. Weakest points in v2.1, stated by the author

1. **The site count grew from twelve to twenty-two, and seven of the ten new
   sites were found by me, not by either reviewer.** That is not reassuring
   about the count. I re-audited the whole composite by exhaustive grep on
   `freez|witness|observation`, then read every §P1-13 block, every `R-L` rule
   and every invariant from 57 to 91 in full. **I cannot prove twenty-two is
   final**, only that I found no twenty-third. The X line found sites I missed
   twice running.
2. **`R21` is the most consequential replacement in v2.1 and it is mine.** It
   changes the composite from a single-freeze-execution-site model to a
   two-site model. I believe that is forced — §3's classifier cannot exist
   otherwise, and it is common to both options — but it is a real widening of
   what the composite permits, and a reviewer who thinks the classifier should
   instead be routed *through* `SIGNAL_GROUP` would reject `R21` rather than
   amend it. I did not pursue that alternative because `SIGNAL_GROUP` is a
   request-driven peer opcode and the classifier is by construction not
   request-driven (W-B) or gated on a PCS-side fact (W-A).
3. **Sites 15, 16, 18 and 22 follow from the Y repair, not from either
   finding.** Removing the fallback route from `R9` leaves row 4 with one
   executing process, which falsifies the `R-L5` / `SW-2` / invariant-91
   cluster. I judged that in scope because the mandate requires replacing every
   contradictory sentence and re-auditing the whole composite. A reviewer could
   hold that this is wider than the bounded correction authorized.
4. **`O-7` corrects an error neither reviewer caught**, and it changes a
   comparison row in W-B's favour. I have stated the direction explicitly so
   the correction is not read as quiet advocacy: it deletes a W-A advantage
   that v2 recorded in error, and I would rather flag that than leave it.
5. **`_CLOCK_MONOTONIC == 1` is asserted from the Linux ABI**, not from any
   document in this chain. §P1-2.1 pins the platform exactly, so the value is
   determinate, but the chain never states it. A reviewer should check it, as
   the X line checked `STAT_OBSERVE_G`'s field indices.
6. **The peer chain outside the composite is still not audited** (`O-6`). The X
   line called this "a real, disclosed, still-open item that the `R-B` repair
   should be paired with before any implementation." **It remains open after
   v2.1.** §W3.3, §Z4, the settlement chain and the harness contract were read
   only where cited. This is the largest known gap in the packet.
7. **`O-8` is a genuine discrepancy between two signed documents** — the
   composite's `<witness_id>.json` versus §W3.3's `<process_id>.json` for the
   same artifact — and I disclosed it rather than repairing it, because
   repairing it is not one of the five bounded repairs. Someone must resolve it
   deliberately before v1.3.
8. **§3 remains large and mine**, unchanged from v2's weak point 1: `KV`, the
   sixteen-token set, the exclusion classification and the three terminals are
   author constructions. If any is wrong, both options inherit the error
   equally.

---

## 11. The exact residual author choices

```text
RESIDUAL CHOICE 1 — the cell AUTHOR_CELL_P1_WATCHDOG_FREEZE_MECHANISM.
  Exactly one of:
    I_SELECT_P1_WATCHDOG_FREEZE_A_WATCHDOG_REQUESTS_PCS_EXECUTES
    I_SELECT_P1_WATCHDOG_FREEZE_B_PCS_FREEZES_ON_PEER_ENDPOINT_LOSS
  Both remain selectable after this correction. Both independent lines
  recommend W-B. NEITHER IS SELECTED HERE.

RESIDUAL CHOICE 2 — the per-option amendment, conditional on choice 1:
    P1_WATCHDOG_SINGLE_OPCODE_CAPABILITY_V1        with W-A only
    P1_WATCHDOG_SENSOR_ONLY_PCS_FREEZE_V1          with W-B only

RESIDUAL CHOICE 3 — four COMMON amendments, required under EITHER selection.
  These are not separate choices from choice 1; they are the price of any
  selection, and a selection without them leaves an unimplementable path:
    P1_FREEZE_ABSENT_FALLBACK_NULLABLE_IDENTITY_V1   v2 §6 + v2.1 §3
    P1_PCS_FREEZE_CLASSIFIER_V1                      v2 §3 + v2.1 §1
    P1_WATCHDOG_FREEZER_ROLE_REASSIGNMENT_V1         v2.1 §2, TWENTY-TWO sites
    P1_FREEZE_PUBLICATION_L6_L9_V1                   v2 §8, unchanged

  NO TOKEN IS ADDED, REMOVED OR RENAMED BY THIS CORRECTION. Three common
  tokens now cover a larger surface than v2 stated; their names and meanings
  are unchanged, and the surface is now stated correctly rather than
  under-stated. A reviewer weighing choice 1 should weigh the corrected
  surface, not v2's.

NONE IS SIGNABLE UNTIL THE BOUNDED X/Y FINAL CONFIRMATION ROUND CONFIRMS v2.1
ON IDENTICAL BYTES.

NOT A CHOICE IN THIS PACKET, AND NOT OPENED BY IT:
  AUTHOR_CELL_P1_PROCESS_CLAIM_IDENTITY_FIELDS — neither selected nor repaired
  here. §6 of v2 makes this cell's settlement constructible under EITHER of its
  outcomes; neither v2 nor v2.1 touches the cell itself. `process_id` remains a
  constructible opaque claim identifier and not a PID.

NO NEW AUTHOR CELL IS OPENED BY THIS CORRECTION. The four disclosures
  O-5..O-8 are, in order: a mechanical handoff carry into the binding; a
  restated still-open audit gap; an arithmetic correction to a blast-radius
  row; and a pre-existing chain discrepancy named but not repaired. None is a
  decision, and none requires one to proceed with the bounded confirmation
  round.
```

---

## 12. Negative authorization — explicit

This closure and the v2.1 correction authorize **nothing**. In particular:

```text
NO SELECTION. Neither W-A nor W-B is selected, recommended into effect, or
   treated as selected. No selection token is minted, accepted, signed, or made
   signable by this round. The identity cell remains UNSELECTED.
NO AMENDMENT ACCEPTED. All six amendment tokens exist only as proposed text in
   draft documents. A-ABS is a PROPOSAL; §N5 is unamended on disk; the
   composite is unamended on disk; invariant 89 stands on disk in its original
   form; §P1-3.4 contains neither _MSG_EOR nor _CLOCK_MONOTONIC on disk.
NO X/Y VERDICT. The first line of this file is an AUTHOR READINESS CLAIM, not
   an X-line or Y-line verdict, and not a signature. The two REVISE verdicts of
   the prior round stand until an independent round replaces them.
NO IMPLEMENTATION. No code, test, verifier rule, manifest entry or schema was
   written, edited, or executed. The §3 classifier, KV, STAT_OBSERVE_G, S-25,
   the R1..R22 replacements, the K1..K5 replacements and every test row are
   SPECIFICATION TEXT, not artifacts.
NO ACTIVATION. T remains NOT_ACTIVATED. No activation record, claim, lease,
   process record, review record, freeze observation, fallback observation or
   invalidity record was created or read for effect.
NO PROCESS EXECUTION. No fork, exec, posix_spawn, kill, killpg, signal, wait,
   prctl, socket, socketpair, pipe or lock operation was performed. No PCS,
   supervisor, controller, worker, middle or watchdog was created or contacted.
   No process was frozen, stopped, signalled, enumerated or observed. No /proc
   read was performed against any live process. No clock was sampled for any
   contract purpose. No behavioural probe was run.
NO SPEND. No E1, E2 or E3 resource was reserved, charged or released. No
   capacity artifact, custody disposition, liability or ledger entry was
   created or moved. The full-charge consequences specified in v2 §3.9 and §6
   are SPECIFICATIONS OF A FUTURE ROUTE, not charges taken.
NO DATUM, NO OUTCOME, NO PROOF. No scientific datum, observation, qualification,
   comparison, blinding claim, Q or C fact, entropy draw, world, learner or
   result manifest was produced, predicted, or optimized toward.
NO CLAIM MOVEMENT. The programme claim remains OPEN.
NO FILE MODIFIED. Exactly two files were created. v2, v1, both v1 reviews, both
   v2 confirmations and the v2 closure are byte-untouched, as §2.1 demonstrates.
NO IDENTITY-CELL MOVEMENT. AUTHOR_CELL_P1_PROCESS_CLAIM_IDENTITY_FIELDS is
   untouched, unselected and unrepaired by this round.
NO NEW CELL. No author cell is opened by this correction.
```

```text
T = NOT_ACTIVATED
PROGRAMME CLAIM = OPEN
PROCESS-IDENTITY CELL = NOT SELECTED
WATCHDOG-FREEZE CELL = NOT SELECTED
READY_FOR_OFFICINA_P1_WATCHDOG_FREEZE_CHOICE_V2_1_FINAL_XY_CONFIRMATION
```
