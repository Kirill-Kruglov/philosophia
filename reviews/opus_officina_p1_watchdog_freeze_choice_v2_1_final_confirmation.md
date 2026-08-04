REVISE_OFFICINA_P1_WATCHDOG_V2_1

# Final X-line confirmation — P1 watchdog-freeze choice v2.1

**Reviewer:** Claude Code Opus, independent X-line engineering reviewer. I did
not author any part of the supervisor/control-channel chain, the identity
packet, the watchdog choice packets, the v2 closure, or the v2.1 correction.
This is a bounded read-only final confirmation with exactly one deliverable —
this file. **It authorizes no selection, amendment, implementation, activation,
process control, spend, or programme movement.**

`T = NOT_ACTIVATED`; programme claim `OPEN`; both author cells UNSELECTED. This
round ran only read-only commands (`git cat-file`, `sha256sum`, `sed`, `grep`,
`wc`, and `python3 -c` to read one library constant). No code, test, verifier,
schema or manifest was written or executed. No process-control operation was
performed. No `/proc` was read against any live process.

---

## 0. Custody — hashes recomputed on committed bytes

Recomputed independently against `git HEAD` and the working tree; the two agree
and the three targets are byte-identical to what the closure recorded.

```text
72212a986d9551ef47718e871a81951b55a849a10d34eb12e6276499cb675505  successor/OFFICINA_P1_WATCHDOG_FREEZE_AUTHOR_CHOICE_PACKET_V2_DRAFT.md
947ed6a954f87eb3971218f9fa2bfa6461999a9a099eb182bc0a09b2f505eed2  successor/OFFICINA_P1_WATCHDOG_FREEZE_AUTHOR_CHOICE_PACKET_V2_1_CORRECTION.md
45e5ddbbec47ad659b783ec052800f10713bd793a100772eb6fa1fec9263488d  reviews/opus5_officina_p1_watchdog_freeze_choice_v2_1_closure.md
```

- The first digest matches the target both v2 confirmations issued `REVISE`
  against; so v2.1 repairs exactly the reviewed bytes.
- The governing composite is
  `2c857fa8…SUPERVISOR_CONTROL_CHANNEL_P1_OPERATIVE_COMPOSITE_V1_2.md`, 2892
  lines, byte-intact. The governing harness/settlement chain
  (`…V2_1_CORRECTION`, `…V2_1_1_CORRECTION`, `…V2_1_2_CORRECTION` `2cd8b7b5…`,
  `…GENERIC_HARNESS_CONTRACT_V2_3_1_CORRECTION`) is byte-intact.
- **The closure is treated as untrusted author self-assessment.** Every citation
  below was read from the contracts' committed bytes, not from the closure's
  quotations.

Both prior confirmations returned `REVISE_OFFICINA_P1_WATCHDOG_FREEZE_CHOICE_V2`
(X on `R-A`/`R-B`; Y on `YV2-M1`/`YV2-M2`). Both are binding defect reports.

---

## 1. Determination 1 — the five bounded repairs

| Repair | Finding | On the committed bytes | Verdict |
|---|---|---|---|
| 1 | X `R-A` `_CLOCK_MONOTONIC` | §1 `B-1`..`B-8`; second pinned constant; `_CLOCK_MONOTONIC == 1` conjunct; `S-25`; tests 92–95 | **CONFIRMED** (§2) |
| 2 | X `R-B` role/execution audit | §2.2 count 22; §2.3 twenty-two sites; §2.4 `R1`..`R22`; two-site model `R19`/`R21` | **CONFIRMED at the composite** (§3); **but see §4** |
| 3 | Y `YV2-M1` count-key rename | §3.2 `K1`..`K5` over `…V2_1_2_CORRECTION.md`; §3.3 negative surface; §3.4 count 5 | **CONFIRMED** |
| 4 | Y `YV2-M2` `R2` schema separation | §2.4 `R2`; §4 `SEP-1`..`SEP-3` | **CONFIRMED** |
| 5 | Y `YV2-M2` `R9`; `R10` unchanged | §2.4 `R9`/`R10`; §5 `D-1`..`D-4` | **CONFIRMED** |

All five bounded repairs are, as text applied to the **composite** and to §N5,
correctly and exactly done. The refutation below (§4) is not a defect in any of
the five repairs; it is a load-bearing surface the correction's own mandate
reaches and that v2.1 discloses (`O-6`) rather than closes.

---

## 2. Determination 2 — `_CLOCK_MONOTONIC`, its pin, validation and call signatures

- **Value under the exact platform pin.** §P1-2.1 fixes Linux / x86_64 /
  CPython 3.12.3. I read `time.CLOCK_MONOTONIC` on Linux CPython 3.12.3: it is
  the integer `1` (`type == int`). `B-3`'s `_CLOCK_MONOTONIC == 1` conjunct is
  correct.
- **It was genuinely undisclosed.** `grep -c "CLOCK_"` over the composite
  returns **0** — no clock id appears anywhere in the reviewed composite, so v2's
  single-constant (`_MSG_EOR`) disclosure was incomplete exactly as `R-A` found.
- **Source adds nothing.** `time` already supplies `_clock` and is one of the six
  admitted modules; the constant adds no import, module or primitive (`B-2`).
- **Validation is fail-closed.** The extended §P1-3.5 check runs in the
  §P1-14.7 preflight before any fork/lock/record; a mismatch is
  `PRIMITIVE_NOT_GENUINE` with no degraded mode and no substitute clock id
  (`B-4`, `B-5`).
- **Every `_clock` call signature is pinned.** `S-25` (`B-7`) requires exactly
  one positional argument, the plain Name `_CLOCK_MONOTONIC`, and fails a
  zero-argument call, any other Name/literal/Attribute/expression, or a second
  clock-id binding. It is uniform over both roots and therefore also pins the
  three pre-existing bare monotonic samples (`:636`, `:1673`, `:1795`).
- **Spelling.** The underscored `_CLOCK_MONOTONIC` is the contract-conformant
  local-name form required by §P1-3.4/§P1-3.6; it is the same constant `R-A`
  named, flagged not silent.

**Determination 2: CONFIRMED.** The classifier is executable using only
§P1-3.4 primitives plus the two disclosed constants `_MSG_EOR` and
`_CLOCK_MONOTONIC`, with no further primitive, import, constant or module
required in the composite.

---

## 3. Determination 3 — the 23rd-site hunt, the twenty-two replacements, the two-site model

**Independent exhaustive audit of the composite.** I greped the whole composite
for `freez|witness|observ` and cross-checked every hit against §2.3's two lists
(the twenty-two replaced sites and the "checked-fine" list). Every one of the
twenty-two sites reproduces **verbatim** at the cited line (spot-checked: `:202`,
`:1447`, `:1459`, `:1464`, `:1490`, `:1783`, `:1888`, `:2006`, `:2249`, `:2367`,
`:2368`, `:2389`, `:2758`, `:2760`). Residual hits not in the twenty-two resolve
cleanly:

- `:1510` "watchdog death is observed and reaped" — observation *of* the
  watchdog, not a freezer/witness assignment.
- `:1996` peer-layer ownership row ("freeze-evidence acceptance") — the peer
  layer still owns acceptance after the reassignment; not falsified.
- `:2382` §P1-13.8 out-of-scope list — covered by invariant 85 (checked-fine).
- `:2116`/`:2176`/`:2213`, `:2232`–`:2302` — row-3 readers and the row-4
  schema/`what P1 replaced`/adjacent-artifacts blocks, all in the checked-fine
  list; the observ-cluster at `:1764`/`:1796`/`:1807`/`:1829` is supervisor and
  identity observation, not watchdog freeze; `:2703`/`:2704`/`:2707` are the
  ppid-identity invariants; `:2778` is negative-space enumeration.

**I found no twenty-third freezer/witness/executor/reader site in the
composite.** (Like the author, I cannot prove twenty-two is final; I can state I
found no twenty-third by exhaustive grep plus a full read of §P1-13 and
invariants 57–91.)

**Two-site PCS execution model — CONFIRMED.** `R19` splits §P1-13.7's group-stop
row into a `SIGNAL_GROUP`-mediation row and a PCS-execution row. `R21` rewrites
invariant 89 to admit exactly two signed freeze-execution sites: (a) the
supervisor's dead-watchdog route through `SIGNAL_GROUP`, and (b) the PCS's own
§P1-10.7 classifier executing `_killpg` in the PCS root under `KV-1..KV-6`,
request-driven by no peer opcode and not `SIGNAL_GROUP`-mediated. Both sites'
`_killpg` executes in the PCS root only, so `S-12`'s sole-`killpg`-caller rule is
retained (`N-3`, test 97), and site (b) installs no record of any peer class
(test 98). This correctly reconciles the composite's original invariant 89
(`:2758`, verified: "a supervisor-executed freeze that did not go through
`SIGNAL_GROUP` is rejected"), which as written *would* reject the §3 classifier
both options depend on. `_killpg` vs `SIGNAL_GROUP` is correctly modelled: the
autonomous classifier is an execution site, not a second caller and not an
opcode. **Determination 3: CONFIRMED at the composite level.**

---

## 4. Determination 4 — the peer-chain audit v2.1 leaves open **(this is the REVISE ground)**

The mandate requires me to *perform* the audit `O-6` leaves open — §W3.3, §Z4,
settlement, generic harness, readers/writers, namespaces, archival — and states:
**a still-open unaudited load-bearing surface is a `REVISE`, not merely a
disclosure.** I performed it. It is load-bearing, it is open, and in one respect
the correction mischaracterizes it against the committed bytes.

The common amendment `P1_WATCHDOG_FREEZER_ROLE_REASSIGNMENT_V1` — required under
**either** W-A or W-B (closure §11 residual choice 3) — makes the watchdog write
and freeze **nothing** on any path; the sole `t-freeze-observation.v1` is written
only by the supervisor on the signed dead-watchdog route (`R2`, `R9`, `R21`). The
**governing peer chain** still says the opposite, in load-bearing text that v2.1
neither audits nor repairs (its handoff touches only §N5's `K1`..`K5`):

1. **§W3.3 is the watchdog's freeze procedure, not the supervisor's.**
   `…V2_1_CORRECTION.md:744` titles it *"Freeze evidence: proved quiescence,
   **watchdog-written**"*; `:745` "When the watchdog's clock shows…"; step 2 the
   watchdog `killpg`s; step 4 the watchdog samples `freeze_ns`; step 6 (`:763`)
   *"write `WATCHDOG/FREEZE/…json` **itself**"*; closing prose *"the watchdog
   still holds no lock…"*. Under the reassignment the watchdog executes none of
   this. **`O-6`'s claim that "§W3.3 … remains the supervisor's dead-watchdog
   procedure; no option amends it" is false against the bytes.** §W3.3 is the
   shared freeze mechanism whose *primary actor is the watchdog*; the
   supervisor's dead-watchdog freeze is §W3.5's ack-absent row, which *invokes*
   §W3.3 with `killer = SUPERVISOR`.

2. **§W3.5 supervisor-death row** (`…V2_1_CORRECTION.md:835`): *"watchdog freezes
   all known groups per §W3.3, writes their observations, exits."* This is the
   peer-chain twin of composite sites 3 and 7 — falsified by the reassignment,
   and in **neither** the twenty-two composite sites **nor** the seven binding
   mirrors of `O-5`.

3. **The governing freeze-observation writer** is still the watchdog. Current
   governing file-tables give the logical writer as *"watchdog (or supervisor
   when the watchdog is dead)"*:
   `…V2_1_2_CORRECTION.md:1353` (hash `2cd8b7b5…`, cited by the closure §2.2 as
   governing) and `…GENERIC_HARNESS_CONTRACT_V2_3_1_CORRECTION.md:1353`. After
   the reassignment this must read *supervisor only*. Also
   `…V2_1_3_CORRECTION.md:298` ("the watchdog writes `WATCHDOG/FREEZE/…json`")
   and `…V2_1_3_CORRECTION.md:514`.

4. **§Z4.6 conjunct 9** binds *"the **watchdog-written** witness"*
   (`…V2_1_2_CORRECTION.md:130`, `:890-892`, `:1318`). The acceptance predicate
   the settlement chain and invariant 89 rest on is stated in terms of a
   watchdog-written object that, after reassignment, no longer exists.

None of items 1–4 is a distant tangential surface. They are the **direct object
of the reassignment** — who writes the one freeze-evidence artifact — in the
currently accepted, byte-intact governing peer contract. If Kirill selected W-A
or W-B on these bytes, the governing set would contain a P1 composite saying "the
watchdog writes no freeze observation" and a governing harness/settlement
contract saying "the watchdog writes the freeze observation" — the exact
"two governing documents disagree" hazard the correction itself names at `O-5`
and closed for the binding but not for the harness/settlement chain. The author
concedes this (`O-6`; weak point 6: "the largest known gap in the packet"), but
concession is what determination 4 forbids passing through.

**Determination 4: NOT satisfied. This is the `REVISE`.** The load-bearing peer
surface is open, and `O-6`'s single substantive characterization of it (§W3.3)
is wrong on the bytes.

*Smallest repair that would close it:* extend the reassignment handoff with a
peer-chain replacement set that (a) rewrites the freeze-observation logical
writer to *supervisor only* in every governing file-table
(`…V2_1_2_CORRECTION.md:1353`, `…V2_3_1_CORRECTION.md:1353`,
`…V2_1_3_CORRECTION.md:298`/`:514`); (b) demotes §W3.3 and §W3.5's supervisor-
death row so the watchdog no longer freezes/writes, retaining only the
supervisor's dead-watchdog invocation; (c) reconciles §Z4.6 conjunct 9's
"watchdog-written" binding to the single supervisor writer; and (d) re-scopes or
corrects `O-6` to state §W3.3 accurately. This is enumeration and replacement of
the same kind the composite already received — not a new mechanism or cell.

---

## 5. Determination 5 — the `<witness_id>.json` vs `<process_id>.json` discrepancy (`O-8`)

**Classified: non-governing; no repair required *for this issue* before
selection — but `O-8` is itself stated imprecisely.**

The composite row-4 path is `WATCHDOG/FREEZE/<witness_id>.json` (`:2236`,
verified). §W3.3 step 6 writes `WATCHDOG/FREEZE/<process_id>.json`
(`…V2_1_CORRECTION.md:763`, verified). `O-8` presents this as an unresolved
discrepancy "between two signed documents." It is not unresolved: a later
governing correction already superseded §W3.3's path —
`…V2_1_1_CORRECTION.md:174`: *"§W3.3 `t-freeze-observation.v1` path
`WATCHDOG/FREEZE/<process_id>.json` — **replaced** by §Z4.5
(`WATCHDOG/FREEZE/<witness_id>.json`)."* The governing value is therefore
`<witness_id>.json`, which the composite matches. The residual `<process_id>.json`
tokens (`…V2_1_CORRECTION.md:763`, `:1393`) are stale-but-superseded, not a live
conflict. So the discrepancy does **not** independently block selection.

It is, however, another instance of the §4 pattern: `O-8` reads the peer chain
without noticing the §Z4.5 supersession, corroborating that the peer surface was
searched by key name only and not audited.

---

## 6. Determination 6 — primitives, constants, totality, replay, prior findings

Re-checked against the corrected bytes; no regression found:

- **Classifier primitives / constants.** `KV-1..KV-6`, `STAT_OBSERVE_G`,
  `P-1..P-3`, the sixteen closed tokens, §3.7 continuations, §3.8's three
  terminals, §3.9 dominance, §3.10 residual — untouched by v2.1; only §3.6
  `C-4`'s clock expression changed (§2 here). The integer-constant conjuncts
  `_SIGCHLD == 17`, `_SIG_DFL == 0`, `_F_GETFL == 3`, `_O_ACCMODE == 3`,
  `_O_RDONLY == 0` are joined by `_CLOCK_MONOTONIC == 1` only.
- **Result totality.** The §3.5 total inclusion/exclusion table, `pgid_or_null`,
  and the three terminals are unchanged; the two-site model does not open a
  non-total branch.
- **W-A / W-B replay.** `E-1..E-4` endpoint-loss semantics, §5.5 record-first
  `R1..R6`, the crash matrix (W-B), and the §4.5 `T-1..T-7` window (W-A) are
  untouched. `R7`/`R11`/`R13`/`R21` W-A variants *cite* `G-1`/§4.5 without
  modifying them. Note the two distinct `R1..R` families (v2 §5.5 ordering vs
  v2.1 §2.4 site replacements) — correctly flagged, neither renamed.
- **`O-7` accounting.** Moving `_MSG_EOR` from W-B-only to both options is
  correct: W-A's `G-1` gate inherits §5.2, so W-A needs the `E-1a/E-1b`
  discrimination and hence `_MSG_EOR`. The change deletes a row that wrongly
  favoured W-A; it cannot flatter W-B.
- **Previously closed findings.** `F2`, `Y-C1`, `Y-C2`, `Y-M1`, `Y-M2`, `Y-M3`,
  `Y-m1`, and X determinations 2/4/5/7/8 remain closed on the corrected bytes.
  `process_id` remains a constructible opaque claim identifier, not a PID,
  mandatory and non-null on every fallback branch (`N-5`). PCS journal state
  stays scientifically invisible (`L8`, `ND-1..ND-3`, test 98).

**Determination 6: CONFIRMED.**

---

## 7. Verdict

```text
REVISE_OFFICINA_P1_WATCHDOG_V2_1
```

The five bounded repairs are each correctly executed on the composite and §N5
bytes (determinations 1–3, 6 CONFIRMED). `_CLOCK_MONOTONIC == 1` is verified on
the exact platform pin; the twenty-two-site audit reproduces verbatim and I found
no twenty-third composite site; the two-site `_killpg`/`SIGNAL_GROUP` model and
invariant-89 rewrite are sound; the schema separation and count-key rename are
complete within their files.

The verdict is `REVISE` on **determination 4 alone**: the required common
amendment `P1_WATCHDOG_FREEZER_ROLE_REASSIGNMENT_V1` falsifies load-bearing
statements in the **governing peer chain** — §W3.3 (a watchdog-written freeze
procedure), §W3.5's supervisor-death row, the freeze-observation logical-writer
rows in the current governing file-tables, and §Z4.6 conjunct 9's
"watchdog-written" binding — which v2.1's handoff neither audits nor repairs, and
which `O-6` discloses rather than closes while mischaracterizing §W3.3 against
the committed bytes. Per the mandate, a still-open unaudited load-bearing surface
is a `REVISE`, not a disclosure. `O-8` is non-governing (superseded by §Z4.5) and
does not independently block, but corroborates the same unaudited-peer-surface
pattern.

The correction is close: the defect is bounded enumeration/replacement of the
peer-chain freeze-writer surface (§4's smallest-repair list), of the same kind
already applied to the composite, plus an accurate re-statement of `O-6`/§W3.3.
No new mechanism or author cell is required.

---

## 8. Negative authorization — explicit

```text
NO SELECTION.        Neither W-A nor W-B is selected, recommended into effect, or
                     made signable. No selection token is minted or accepted.
NO AMENDMENT.        None of the six amendment tokens is accepted or made
                     signable. §N5, the composite, invariant 89 and §P1-3.4 stand
                     unamended on disk.
NO IMPLEMENTATION.   No code, test, verifier, schema or manifest written or run.
NO ACTIVATION.       T remains NOT_ACTIVATED. No record created or read for effect.
NO PROCESS CONTROL.  No fork/exec/kill/killpg/signal/wait/prctl/socket/pipe/lock.
                     No process frozen, stopped, signalled, enumerated, observed.
                     No /proc read against any live process. No clock sampled for
                     any contract purpose.
NO SPEND.            No E1/E2/E3 reserved, charged or released.
NO DATUM/OUTCOME.    No datum, qualification, comparison, Q/C fact, world, learner
                     or result manifest produced or predicted.
NO CLAIM MOVEMENT.   Programme claim remains OPEN.
NO IDENTITY MOVEMENT. AUTHOR_CELL_P1_PROCESS_CLAIM_IDENTITY_FIELDS untouched,
                     unselected, unrepaired.
ONE FILE CREATED.    Only this confirmation file. No existing file modified.
```

```text
T = NOT_ACTIVATED
PROGRAMME CLAIM = OPEN
PROCESS-IDENTITY CELL = NOT SELECTED
WATCHDOG-FREEZE CELL = NOT SELECTED
REVISE_OFFICINA_P1_WATCHDOG_V2_1
```
