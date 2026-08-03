READY_FOR_OFFICINA_P1_PROCESS_CLAIM_IDENTITY_CHOICE_V2_XY_CONFIRMATION

# Author closure — P1 process-claim identity choice packet v2

**Author:** Claude Code Opus 5, **specification author only**. I authored the
whole supervisor/control-channel chain, v1, v1.1, v1.2, the v1 choice packet and
this v2 repair, and am therefore **disqualified** as its independent X-line or
Y-line reviewer. **This closure is an untrusted author self-assessment.** The
verdict on its first line is a readiness claim about a bounded confirmation
round; it is not an X or Y verdict and it clears nothing.

**No choice was made and no token was minted or accepted.** The packet presents
the options; the selection is Kirill's and is not signable until a bounded X/Y
confirmation round confirms v2 on identical bytes.

`T = NOT_ACTIVATED`; programme claim `OPEN`. This round produced no selection,
X/Y verdict, implementation, code or test edit, verifier or manifest change,
process or behavioural probe, activation, entropy, E1/E2/E3 spend, Q/C work,
datum, outcome, Proof or claim movement.

---

## 1. Deliverables and untouched-file confirmation

Exactly two new files. **No existing file was modified.**

| Path | Lines |
|---|---|
| `successor/OFFICINA_P1_PROCESS_CLAIM_IDENTITY_AUTHOR_CHOICE_PACKET_V2_DRAFT.md` | 1566 |
| `reviews/opus5_officina_p1_process_claim_identity_choice_v2_closure.md` | this file |

`successor/OFFICINA_P1_PROCESS_CLAIM_IDENTITY_AUTHOR_CHOICE_PACKET_V1_DRAFT.md`,
`reviews/opus5_officina_p1_process_claim_identity_author_choice_packet.md`,
`reviews/opus_officina_p1_process_claim_identity_choice_review.md` and
`reviews/sol_officina_p1_process_claim_identity_choice_review.md` are
**byte-untouched**, as §2 demonstrates by recomputing their digests.

Only read-only commands were run against the repository: `git show`, `grep`,
`sed`, `wc` and `sha256sum`. No test, behavioural probe or process-control
operation was executed. No code was implemented. No T state was touched.

---

## 2. Hashes and custody

### 2.1 Reviewed inputs, recomputed on committed bytes

```text
ad8b5791f043f201c00812a11de2ab3b765664e65e6d0ebf9778e150913096d3  successor/OFFICINA_P1_PROCESS_CLAIM_IDENTITY_AUTHOR_CHOICE_PACKET_V1_DRAFT.md
e8bceb8098c9a1d96fcd76f0796fccdcd49b79ce4cd690d1ef3a7d9ced54e128  reviews/opus5_officina_p1_process_claim_identity_author_choice_packet.md
bfa7f6dd6a09313033b2a00c75f0e1e0632c63f65733b80424ee889433364f3b  reviews/opus_officina_p1_process_claim_identity_choice_review.md
705b36b6ce1a9387261f66f2a473295be4384903b0e0240ae8e7496af6899e80  reviews/sol_officina_p1_process_claim_identity_choice_review.md
```

The first two match the digests both reviews independently recomputed and
declared `[MATCH]`, so the bytes the X and Y lines reviewed are the bytes v2
repairs. The last two are the review files themselves, pinned here so that a
confirmation round can prove it is dispositioning the same defect reports.

### 2.2 Governing contracts, recomputed on committed bytes

```text
2c857fa8ad7be1c861eb8cf561f396e7d2339403c7714abc7958745bf34e5d5d  successor/…SUPERVISOR_CONTROL_CHANNEL_P1_OPERATIVE_COMPOSITE_V1_2.md
cd106d7fef491601f9ff948aba3ba0ceaac0774ac18a6564247c0c5899b4c40c  successor/OFFICINA_T_ACTIVATION_PROTOCOL_V2_CORRECTION.md
6ef98132990f8c686fa9678509bb07ba8259f3d6e4cbc483861edfc03ea8e3ef  successor/OFFICINA_SUPERVISOR_PROCESS_AUTHORITY_SELECTION_V1_SIGNATURE.md
ee3171724c89bd7e8f890141f42bf478838608c6f1908f9284218f1e940be635  successor/…SUPERVISOR_CONTROL_CHANNEL_V2_1_1_CORRECTION.md
2b4f9cad7be7a69527e828c73928a399209fcd8151780b9b4c839934893e0dc8  successor/…SUPERVISOR_CONTROL_CHANNEL_V2_1_10_CORRECTION.md
6197d2a4073d35fc978119db32128c50d12594343ac87731640a1d8e19f09e84  successor/…SUPERVISOR_CONTROL_CHANNEL_V2_1_10_4_P1_BINDING.md
724d633a55668013b78058eed1c76e12e9bbaf487f71ea94b7a4568ea1ced8a0  successor/OFFICINA_GENERIC_HARNESS_CONTRACT_V2_3_1_CORRECTION.md
b5a1523290b6b8417a7b3288329cc4a4e5ff80214c8f28e6ea1ae51a450a94c9  successor/OFFICINA_BATCH_SETTLEMENT_CORE_AMENDMENT_V1_1_1_CORRECTION.md
8c47da352ef5954406964647a32e97939c404806bdf9b3d3ff5bc70866e6369a  successor/OFFICINA_GENERIC_HARNESS_SIGNATURE.md
c494ef8884948bd0e737373d2d57a3ab74bbd456db2c3463711c4405f2fdf86a  successor/OFFICINA_SUPERVISOR_AUTHOR_SELECTIONS_V1_SIGNATURE.md
4918a208bb94549ba3e7c38571265e723cc51a0a3394e291a62a85c333d864a6  successor/OFFICINA_SUPERVISOR_OUTPUT_CAPACITY_SELECTION_V1_SIGNATURE.md
```

Every previously pinned digest matches what v1.1, v1.2 and the v1 closure
recorded. **The custody chain is byte-intact across this round.**

### 2.3 Produced this round

```text
f5d95a0d4a7c72731b5a20cf668e67dbc66329e0989fb945bd0a5727717f6095  successor/OFFICINA_P1_PROCESS_CLAIM_IDENTITY_AUTHOR_CHOICE_PACKET_V2_DRAFT.md
```

**On this closure's own digest.** A file cannot contain the SHA-256 of its own
committed bytes without a fixpoint, so this closure does not embed it. It is
recomputed by:

```text
sha256sum reviews/opus5_officina_p1_process_claim_identity_choice_v2_closure.md
```

Custody therefore stays acyclic: v2 packet → this closure → X/Y confirmation →
any future signature. The v2 packet contains none of its own digests.

### 2.4 Evidence used, by source location

All citations in v2 were read directly from the committed bytes of the
contracts, not from v1's or either review's quotations:

```text
claim / lease / final-record / review-record / invalidity-record key sets
  …ACTIVATION_PROTOCOL_V2_CORRECTION.md:231-238, :241-246, :248-257,
  :262-268, :269-276; activation-claim keys :134-144; claim path :78-86;
  process-id preimage :296-299; immutability of the process group :300-305;
  dispositions and invalid causes :308-322; "Recovery cannot delete/reuse a
  claim or process id" :338-341; archival sets :88-97
opcode table, PID-free closure, handle model, journal and replay
  …P1_OPERATIVE_COMPOSITE_V1_2.md:1218-1228, :1240, :1256-1266, :1276-1304
    (J4 at :1289; COMPLETED replay at :1301; ACKED replay at :1303)
ownership, PID-reuse proof, WAIT_ONE precondition, STAT_OBSERVE, I-3
  same file :1519-1550, :1566, :1600-1626, :1640
role argv layout, setsid=True, watchdog properties and fdmap, slot 6
  same file :961-990, :480-481, :1446, :1464, :680, :978, :1167
PCS loss, supervisor freeze unavailability, invalidity routing and dominance
  same file :1757-1785 (freeze unavailable at :1781), :1849-1866, :2323-2330
R-L4, layer ownership, row 2, row 4, the single-writer table, the code rules
  same file :2022-2027, :1993-1995, :2098-2136, :2232-2276, :2357-2368,
  :2555-2645; same-UID capability :1942, :1952
§Z4.6 conjunct 7 and conjunct 9; §Z3.4 discovery predicate
  …V2_1_1_CORRECTION.md:1047, :1049, :758-778
argv-as-evidence deletion, with its exact scope
  …V2_1_10_CORRECTION.md:188
the signed sentence and its derivation
  …PROCESS_AUTHORITY_SELECTION_V1_SIGNATURE.md:24-26;
  …V2_1_10_4_P1_BINDING.md:156-158
```

The exhaustive key search behind v2 §2.6.4 and §3.2 was run across every
schema in the governing block; `controller_pid` and `process_group_id` appear
in exactly two durable peer schemas, and the identically-named key of
`SPAWNING_GROUP.json` denotes the **middle's** group per §P1-5.2 `:604`, which
v2 §2.6.5 handles explicitly rather than by silence.

---

## 3. Finding disposition — one to one

Every finding of both reviews, with its status, the exact repair, and the
residual. **Nothing is marked closed by restatement.**

### 3.1 X line — `reviews/opus_officina_p1_process_claim_identity_choice_review.md`

| Finding | Class | Status | Repair, and where |
|---|---|---|---|
| **M-1** replay durability asserted on an unestablished guarantee; journal-schema edit missing from blast radius and handoff | Major | **CLOSED** | v2 §2.8.1 **withdraws** "exactly as `start_identity` already is" verbatim and states why the cited bytes do not carry it. §2.8.2 amends the `J4` record to the full thirteen-key AWAIT_STOP operand vector with pinned order and encoding `E-1`..`E-4`. §2.8.3 rewrites the `COMPLETED`/`ACKED` replay rows as a byte-identical redelivery with `R-P1`..`R-P4`. §5.1/§5.4/§5.5 move the journal record format **into** A's blast radius; §7.2 step 8 adds it to the v1.3 handoff. §7.1 withdraws "A touches one sentence and one response grammar". `S-25h` and `A-T10` check it mechanically. The counterexample (crash between `J4` and the peer claim write) is row 4 and row 6 of §2.10.2. |
| **M-2** no-second-sink rests on `S-25d` taint completeness that is asserted, not established, and the propagation classes are not closed under Python | Major | **CLOSED** | v2 §2.5 **withdraws** `S-25d` and its decidability justification, and replaces taint with a **positional occurrence whitelist**: Zone 1's closed operation list `V-1`..`V-9` + `Z1-R1`..`Z1-R6`; Zone 2's exact-three-occurrence rule `Z2-R1`..`Z2-R5`. §2.5.4 gives the prohibition catalogue explicitly as **redundant**, and §2.5.5 states why the rule is decidable with no fixpoint, no call graph and no taint soundness. The four laundering constructs the X line named are each rejected by occurrence count and are fixtures in `A-T9`. |
| **m-1** `A-P4` re-reads `getpgid` although the handle table holds `pgid_or_null`; authority unstated | Minor | **CLOSED** | v2 §2.3 `A-P4a`..`A-P4d`: the **fresh read is authoritative** (the claim binds identity at the stop instant, and `pgid_or_null` is nullable and not tied by schema to that instant); the stored value is a **mandatory cross-check when non-null**, disagreement ⇒ `STRUCTURAL_VIOLATION`; the `setsid` equality remains mandatory; **no other source exists**. Single-valued for an implementer. |
| **m-2** the 7-digit bound is correct but its justification is absent | Minor | **CLOSED** | v2 §2.2 pins `PID_MAX_LIMIT = 4194304` as the provenance, adds `G-3` (value in `1..4194304`), `G-5` (8+ digits fail closed, never truncated), `G-6` (7-digit value above the limit fails closed), states the platform premise explicitly, and tests it at `A-T8`. |
| **m-3** §6 wording risk: the supervisor and watchdog freeze cases could be conflated | Minor | **CLOSED** | v2 §6.1 separates them as `CASE 1` and `CASE 2` by **actor, trigger, citation and status** — supervisor / control-socket EOF / `:1781` / already recorded, versus watchdog / update-pipe EOF / `:1464` with `:1446`, `:680`, `:978`, `:1167` / unresolved — and states in terms that Case 1 is not evidence that Case 2 is handled. |

### 3.2 Y line — `reviews/sol_officina_p1_process_claim_identity_choice_review.md`

| Finding | Class | Status | Repair, and where |
|---|---|---|---|
| **Y-C1** the sole-sink/dataflow closure is not closed across the signed durable schemas; a reload can launder the value | Critical | **CLOSED** | v2 §2.4 **withdraws** the v1 §2.4 rule verbatim and states why it is false against `:241-246` and `:1047`. §2.6 replaces it with the `RESTRICTED_PROCESS_IDENTITY` class whose member (e) is "every alias, copy, reload, deserialization, cached form", so **a reload never declassifies**. §2.6.2 enumerates the complete legitimate persistent flow as `C-1` claim write, `C-2` claim-to-lease whole-mapping copy (because the lease is "the claim keys plus" five), `C-3` the lease/claim immutability comparison, `C-4` the signed conjunct-7 comparison — with `P-R1`..`P-R5` and record-first dominant invalidity for everything else. §2.6.3 adds the centralized accessor surface `ACC-1`..`ACC-3` with `ACC-R1`..`ACC-R4`, which rejects the Y line's exact evasion at both the reopen and the fresh binding. §2.6.4 **recomputes** the schema readers key-by-key rather than claiming taint completeness. `S-25d`, `S-25e`, `S-25g` check it. |
| **Y-C2** the replay promise is not constructible from the literal `J4` record; the `J4`→`J5` cut breaks B1 | Critical | **CLOSED** | Same repair as `X M-1`: v2 §2.8.2 makes the complete replayable representation and its `J4` durability explicit; §2.8.3 requires byte-identical redelivery with no re-observation; §5.1/§5.5 update the journal surface and blast radius; §7.2 step 8 updates the handoff. The three continuations the Y line called the only ones available under v1's text (absent fields, fresh observation, invented bytes) are each now excluded by `R-P1`..`R-P4`. |
| **Y-M1** the crash/collision table contradicts durable claim existence and does not preserve invalidity dominance; `EEXIST` is not convergence | Major | **CLOSED** | v2 §2.10.1 **withdraws** "PCS death at any point ⇒ no claim is written" verbatim. §2.10.2 rebuilds the matrix keyed to the **exact durable boundary crossed**, so no row can contradict the one before it; post-claim PCS death **retains the claim** and settles through the signed invalid-process route as `T_PROCESS_INVALID` / `invalid_cause` `PROCESS`, cited to `:338-341`, `:1849-1866`, `:2323-2330`. §2.10.3 makes `EEXIST` converge only after `X-1` canonical bytes, `X-2` schema, `X-3` cross-field, `X-4` expected hash — every failure being record-first invalidity with the occupant never replaced. §2.10.4 binds malformed, partial, out-of-range, cross-field-inconsistent and tuple-mismatched replies (`I-1`..`I-10`) to that same dominant surface. `A-T11`, `A-T12` test it. |
| **Y-M2** Option B's schema blast radius is materially overstated; `t-process-record.v1` does not inherit the keys | Major | **CLOSED** | v2 §3.2 **withdraws** the inheritance claim verbatim, quoting the final record's exact key set from `:248-257` and noting it carries `process_claim_sha256`. The reader audit is **recomputed row by row with an explicit dependency for each**; `t-process-record.v1`, the review record, the invalidity record, the activation claim, the freeze observation, the archive and batch settlement are all shown **not** to change, and the `process_claim_sha256` **value** dependency is counted as content, not schema. Corrected count: **two** record schemas superseded, one new schema, one signed predicate, one architectural rule, one write-surface property. §5.1/§5.4/§5.5 and §7.1 carry the corrected figures. |
| **Y-m1** the stale `/proc` route is unauthorized, but one stated reason is broader than its source | Minor | **CLOSED** | v2 §1.5 restates the exclusion as `R-1` stale indices, `R-2` unattested self-scan, `R-3` authority bypass (pid→`killpg` outside the nine opcodes), `R-4` narrowed evidentiary basis — with `R-4` stating **in terms** that `:188` deletes argv as evidence *of a clean image, of a fresh `execve`, or of the executor set* and **does not literally delete every argv-derived identity use**, and that `R-1`..`R-3` close the route independently of `R-4`. §4 carries the same corrected rationale. §Z3.4's staleness is retained as a separate peer-chain defect, not a hidden Option C. |

### 3.3 The Y line's seven required determinations

| # | Determination | v2 status |
|---|---|---|
| 1 | A3 authority: observing an attested PID/PGID confers no authorized process control | **Adopted unchanged.** §5.6, plus `A-R1`..`A-R8`. v2 states in §2.12 that the change is a real weakening of the sentence, not a transfer of authorized control. |
| 2 | Legitimate sinks must include the lease repeat and the conjunct-7 read, and all other uses must fail into process invalidity | **Implemented.** §2.6.2 `C-1`..`C-4`, `P-R4`, `P-R5`. |
| 3 | A's mechanisms are sound in principle, but the durable-sink, `J4` replay, `EEXIST` and post-claim-death defects must be closed before the claim schema and freeze conjunct may stay byte-unchanged | **All four closed** at §2.6, §2.8, §2.10.3, §2.10.2. The claim schema and conjunct 7 remain byte-unchanged under A, now on repaired grounds. |
| 4 | §2.10's disclosure is adequate in form | **Preserved and extended.** §2.12 keeps the old and new text side by side, keeps the dedicated token, and now also corrects v1's own characterization: the post-A property is **syntactic**, not dataflow. |
| 5 | B is honestly non-selectable | **Preserved.** §3.3, and §7.1 states in terms that the corrected blast radius does **not** change this, because the blocker is an authority gap, not a size argument. |
| 6 | The stale `/proc` route is a defect, not an alternative | **Preserved**, with the rationale corrected. §1.5, §4. |
| 7 | The recommendation's basis is governance and blast radius only, and `Y-M2`/`Y-C1`/`Y-C2` made it unreliable | **Re-evaluated, not tuned.** §7.1 withdraws v1's stated reason as false in both halves, presents the corrected figures — A larger, B smaller — and rests the surviving recommendation on the three rows that did **not** move: zero reopened validity predicates, no architectural rule inverted, and non-selectability. It says in terms that blast radius is no longer the load-bearing argument, and it states A's newly disclosed cost (a durable format change v1 explicitly denied). |

### 3.4 Findings opened by v2 itself

```text
NONE that create a new author cell.

v2 §2.8.2 records that the "J4 records the complete response operand vector"
rule repairs a PRE-EXISTING UNDER-ENUMERATION in v1.2's journal text that
affects all nine opcodes, not only AWAIT_STOP. This is a broader edit than
Option A strictly needs, it is disclosed as such rather than hidden inside an
AWAIT_STOP-only change, and it is counted in A's blast radius at §5.

v2 §2.6.7 records that the activation protocol's admission-time
group-membership sentence (:300-303) is NOT a fifth persistent consumer under
P1, because group determination is P1's and is keyed by handle (SIGNAL_GROUP's
kernel-verified-group precondition, :1223). This consumes only already signed
text and opens no cell.

v2 §2.6.5 records the SPAWNING_GROUP.json key-name collision and scopes the
accessor rule by SCHEMA rather than by key name (NC-1..NC-3), so that the
middle's process-group id is neither constrained nor relaxed by this packet.
```

---

## 4. Corrected blast-radius table

This is the table the confirmation round should check, replacing v1 §5.5.

| Dimension | **Option A**, corrected | **Option B**, corrected |
|---|---|---|
| signed sentences amended | 1 — the P1 process-authority sentence, under `P1_IDENTITY_OBSERVATION_BOUNDED_WEAKENING_V1` | 0 |
| **peer-owned durable record schemas superseded** | **0** — `t-process-claim.v1`, `t-active-lease.v1`, `t-process-record.v1` byte-untouched | **2** — claim and lease. **Not 3, not 4**; the final process record does **not** change (`:248-257`) |
| new durable schemas created | 0 | 1 — `t-process-identity-binding.v1` |
| **signed validity predicates reopened** | **0** | **≥ 1** — §Z4.6 conjunct 7 |
| architectural rules inverted | 0 — `R-L4` holds (`A-R8`) | 1 — `R-L4` inverted; the PCS write surface expanded to a fifth peer-visible class |
| wire grammar changed | 1 response grammar (`AWAIT_STOP`, operands 11–12); **no request grammar** | none |
| **durable formats changed** | **1 — P1's own journal record (`J4`) and its two replay rows.** New in v2; v1 denied this | 0 journal changes; the 2 record schemas above |
| collision/idempotency rules changed | 1 — the claim-install `EEXIST` verification `X-1`..`X-4` | binding artifact is no-replace; a GC rule for orphan bindings does **not** yet exist |
| verifier rules added | 8 — `S-25a`..`S-25h`, all syntactic, none requiring taint soundness | new validators for 2 superseded schemas + 1 new class; a new conjunct-7 predicate |
| tests added | 12 — `A-T1`..`A-T12` | full re-validation of claim and lease readers; binding lifecycle |
| readers requiring recomputation | claim constructor, lease constructor, immutability check, conjunct 7 — **all already existing, none amended** | every claim and lease reader; conjunct 7 rewritten |
| migration | none — `T` is `NOT_ACTIVATED`; no claim, lease, record or journal exists | none **today**, for the same reason; large after activation |
| rollback | delete 2 response fields, revert the `J4` key list, delete 8 rules. **No peer record changes shape**; a journal already written in the new shape would be stranded | revert 2 schemas, delete the binding class; any `.v2` object already written is stranded |
| **selectable today** | **yes** | **no** — blocked behind `B-1` and `B-2` |

**Honest summary of the correction: A grew, B shrank, and the recommendation
survives on the rows that did not move.**

---

## 5. Invariants confirmed unchanged

| Invariant | Where v2 keeps it |
|---|---|
| the identity conflict is real and loud | §1, restated without softening; `N-1` |
| Option A is an **explicit** weakening of the lexical "cannot express a PID" sentence, not a hidden reinterpretation | §2.12, old and new text side by side, dedicated token, plain statement of the cost; `N-2` |
| observing PID/PGID grants no authorized process-control authority; only handles, the closed request grammar and PCS execution do | §5.6, `A-R1`..`A-R8`; `N-3` |
| both-or-neither tuple semantics | `G-4`, `A-T3` |
| stopped/unreaped direct-child proof | `A-P1`..`A-P6`, `A-T2` |
| PID-reuse binding | §2.9, unchanged from v1 |
| fail-closed absence | `G-5`, `G-6`, `Z1-R6`, `A-T8` |
| no replay re-observation | `R-P1`..`R-P4`, `S-25h`, `A-T10` |
| the watchdog-freeze cell is orthogonal and unresolved | §6, `N-5` |
| `T = NOT_ACTIVATED`; programme claim `OPEN` | §10, `N-6`, and this closure |

---

## 6. The exact residual author choices

**Unchanged in substance by this repair.** v2 narrows nothing and adds nothing
to what Kirill must decide.

```text
RESIDUAL CHOICE 1 — the cell AUTHOR_CELL_P1_PROCESS_CLAIM_IDENTITY_FIELDS.
  Exactly one of:
    I_SELECT_P1_PROCESS_CLAIM_IDENTITY_A_OBSERVATION_ONLY
    I_SELECT_P1_PROCESS_CLAIM_IDENTITY_B_OPAQUE_BINDING
  A is selectable today. B is NOT selectable and directing it opens sub-cells
  B-1 and B-2 and requires a further packet before any composite can bind it.

RESIDUAL CHOICE 2 — conditional on A only.
    P1_IDENTITY_OBSERVATION_BOUNDED_WEAKENING_V1
  the bounded weakening of the signed process-authority sentence, in the exact
  text of v2 §2.12. Selecting A without this token is not a coherent state.

NEITHER IS SIGNABLE UNTIL THE BOUNDED X/Y CONFIRMATION ROUND CONFIRMS v2 ON
IDENTICAL BYTES.

NOT A CHOICE IN THIS PACKET, AND NOT OPENED BY IT:
  AUTHOR_CELL_P1_WATCHDOG_FREEZE_MECHANISM  — orthogonal, unresolved, and not
  fixed or worsened by either option (v2 §6). P1 remains non-operative until it
  is resolved, even if A is selected.
  Sub-cells B-1 and B-2                     — reachable only by directing B.
```

---

## 7. Readiness verdict

```text
READY_FOR_OFFICINA_P1_PROCESS_CLAIM_IDENTITY_CHOICE_V2_XY_CONFIRMATION
```

**Meaning precisely.** All ten findings of the two binding defect reports are
dispositioned one-to-one at §3, each by a named repair at a named locus, with
four v1 sentences withdrawn verbatim rather than paraphrased away. The packet
is a self-contained replacement. Both reviews' `REVISE` verdicts asked for a
bounded revision and stated that the packet "should be confirmable on the next
pass"; v2 is that pass.

**Therefore, yes: the packet is ready for one bounded X/Y confirmation round**,
scoped to (a) whether each finding is in fact closed on the v2 bytes, and (b)
whether the repairs introduced a new defect. It is **not** ready for selection,
because a selection requires that round to confirm first.

**It does not mean the packet is correct.** This is an author self-assessment
by the party that wrote the defects being repaired.

---

## 8. One bounded confirmation question per reviewer

### For the X line — one question, yes or no

> **Is the §2.5 positional occurrence whitelist — Zone 1's closed operation
> list `V-1`..`V-9` with `Z1-R1`..`Z1-R6`, and Zone 2's exact-three-occurrence
> rule `Z2-R1`..`Z2-R5`, checked by `S-25a`/`S-25c` — decidable by a single AST
> walk over the five production roots and closed against every laundering
> construct, without any taint-soundness assumption, so that `M-2` is fully
> closed?**

Answer `YES` or `NO`. A `NO` should name one construct that reaches a second
sink while satisfying the occurrence count, since the count, not the §2.5.4
catalogue, is what the closure rests on.

### For the Y line — one question, yes or no

> **Do the four persistent consumers `C-1`..`C-4` of §2.6.2, together with the
> `RESTRICTED_PROCESS_IDENTITY` class of §2.6.1 and the accessor closure
> `ACC-1`..`ACC-3` of §2.6.3, constitute the complete and correct set of
> authorized durable uses of `controller_pid` and `process_group_id` under the
> signed chain — with every other direct or reloaded use routed to dominant
> process invalidity by `P-R5` — so that `Y-C1` is fully closed?**

Answer `YES` or `NO`. A `NO` should name the fifth consumer the signed chain
requires, or the route by which a reload escapes `ACC-R1`/`ACC-R2`.

Both lines should also confirm, as part of the same bounded round, that the
remaining eight findings are closed as dispositioned at §3, and that the
corrected blast-radius table at §4 is exact on the governing schemas.

---

## 9. Weakest points in v2, stated by the author

1. **§2.8.2's generalization is larger than the finding.** Making `J4` record
   the complete operand vector for **all nine** opcodes repairs a pre-existing
   v1.2 under-enumeration. A reviewer may reasonably hold that a choice packet
   should not carry a general journal repair, and that it belongs in its own
   correction. I disclosed it rather than scoping it to `AWAIT_STOP` only,
   because an `AWAIT_STOP`-only fix would leave the same hole for the other
   eight and would be a narrower claim than the durability argument needs.
2. **The occurrence-count discipline is strict enough to be awkward to
   implement.** `Z2-R4`'s exactly-three rule and `ACC-R2`'s exactly-once rule
   may prove hard to satisfy in real code without contortions. If so, the right
   response is to revise the count to a larger enumerated set of positions, not
   to reintroduce taint.
3. **§2.6.5's schema-scoped accessor rule (`NC-1`..`NC-3`) is new** and is the
   least-scrutinized construction in v2. It depends on the reading site's
   schema being decidable, which I justified from §P1-13.7's single-site
   discipline but did not exhaustively verify against every open call in the
   peer root.
4. **§2.6.7's disposal of the admission-time membership question** relies on
   reading `SIGNAL_GROUP`'s "kernel-verified group" precondition as the
   authorized membership determination. If a reviewer rejects that reading, a
   fifth persistent consumer may exist and `Y-C1` would not be fully closed.
5. **`A-P4a`'s choice of the fresh read** is mine, not any signed document's.
   The reasoning — that the claim binds identity at the stop instant and
   `pgid_or_null` is nullable and not schema-tied to that instant — is sound to
   me but is an author's judgement, resolved for single-valuedness rather than
   discovered in the chain.
6. **§7.1's recommendation now rests on fewer criteria than v1's did**, because
   the criterion v1 leaned on was disproved. If a reviewer holds that
   "reopens zero validity predicates" and "inverts no architectural rule" are
   not sufficient without the blast-radius argument, the recommendation weakens
   even though the non-selectability of B does not.

---

## 10. Negative authorization — explicit

This closure and the v2 packet authorize **nothing**. In particular:

```text
NO SELECTION. Neither A nor B is selected, recommended into effect, or treated
   as selected. No selection token is minted, accepted, signed, or made
   signable by this round.
NO TOKEN MOVEMENT. P1_IDENTITY_OBSERVATION_BOUNDED_WEAKENING_V1 exists only as
   proposed text in a draft packet.
NO X/Y VERDICT. The first line of this file is an author readiness claim, not
   an X-line or Y-line verdict, and not a signature.
NO IMPLEMENTATION. No code, test, verifier rule, manifest entry or schema was
   written, edited, or executed. S-25a..S-25h and A-T1..A-T12 are specification
   text, not artifacts.
NO ACTIVATION. T remains NOT_ACTIVATED. No activation record, claim, lease,
   process record, review record or invalidity record was created or read for
   effect.
NO PROCESS EXECUTION. No fork, exec, posix_spawn, signal, wait, prctl, socket,
   pipe or lock operation was performed. No supervisor, PCS, controller,
   worker, middle or watchdog was created or contacted. No behavioural probe
   was run.
NO SPEND. No E1, E2 or E3 resource was reserved, charged or released. No
   capacity artifact, custody disposition, liability or ledger entry was
   created or moved.
NO DATUM, NO OUTCOME, NO PROOF. No scientific datum, observation, qualification,
   comparison, blinding claim, Q or C fact, entropy draw, world, learner or
   result manifest was produced, predicted, or optimized toward.
NO CLAIM MOVEMENT. The programme claim remains OPEN. No process claim was
   installed, read for effect, amended, or removed.
NO FILE MODIFIED. Exactly two files were created. v1, the v1 closure, and both
   review files are byte-untouched, as §2.1 demonstrates.
NO WATCHDOG REPAIR. AUTHOR_CELL_P1_WATCHDOG_FREEZE_MECHANISM is untouched and
   unresolved.
```

```text
T = NOT_ACTIVATED
PROGRAMME CLAIM = OPEN
READY_FOR_OFFICINA_P1_PROCESS_CLAIM_IDENTITY_CHOICE_V2_XY_CONFIRMATION
```
