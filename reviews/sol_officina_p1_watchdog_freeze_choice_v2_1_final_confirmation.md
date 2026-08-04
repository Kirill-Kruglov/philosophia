REVISE_OFFICINA_P1_WATCHDOG_V2_1

# Independent Y-line final confirmation — P1 watchdog-freeze choice v2.1

**Reviewer:** GPT Sol, independent Y-line scientific-validity and governance
reviewer.

**Scope.** I reviewed the committed v2 packet and v2.1 correction, treated the
author closure as untrusted, read both prior v2 confirmations, re-audited the
operative composite, and traced the governing peer surfaces outside the
composite. This is a bounded validity/governance confirmation only. It creates
no implementation, activation, process-control act, spend, datum, outcome,
Proof, or claim movement.

## Custody

All paths below were clean relative to `HEAD`; hashes are SHA-256 of the bytes
at commit `e46b8db36346bdc7f31071917a841edfc4fa1b4d`.

```text
72212a986d9551ef47718e871a81951b55a849a10d34eb12e6276499cb675505  successor/OFFICINA_P1_WATCHDOG_FREEZE_AUTHOR_CHOICE_PACKET_V2_DRAFT.md
947ed6a954f87eb3971218f9fa2bfa6461999a9a099eb182bc0a09b2f505eed2  successor/OFFICINA_P1_WATCHDOG_FREEZE_AUTHOR_CHOICE_PACKET_V2_1_CORRECTION.md
45e5ddbbec47ad659b783ec052800f10713bd793a100772eb6fa1fec9263488d  reviews/opus5_officina_p1_watchdog_freeze_choice_v2_1_closure.md
23e93c7b028d0a7e36c9cd42baf1a03ade0b3cf0e5f18dad3f2d772ce3584b10  reviews/opus_officina_p1_watchdog_freeze_choice_v2_confirmation.md
a4de28727eb25e7879608fd2f9c22a62c0b42086d8d3cbcfd72e478d28147fca  reviews/sol_officina_p1_watchdog_freeze_choice_v2_confirmation.md
```

The relevant governing peer and P1 chain recomputes as:

```text
64b8d3f63594b79a6abc767a032383c5704beaf09b32a1e0c58fdc444bb0af71  successor/OFFICINA_GENERIC_HARNESS_CONTRACT_V2_DRAFT.md
6bbaf4d17295a8a4d4fa0f42a9347707e4e2319ea5183163c756b94008764077  successor/OFFICINA_GENERIC_HARNESS_CONTRACT_V2_1_CORRECTION.md
624dfc9b34c8009ee4c1610bfff91f5cfceea128e84d850c3e90ffb1e7be9e2f  successor/OFFICINA_GENERIC_HARNESS_CONTRACT_V2_2_CORRECTION.md
b2288b0a9fb44d23c19d853aeb6d57edd4de888c6058af8001a379f9237d3154  successor/OFFICINA_GENERIC_HARNESS_CONTRACT_V2_3_CORRECTION.md
724d633a55668013b78058eed1c76e12e9bbaf487f71ea94b7a4568ea1ced8a0  successor/OFFICINA_GENERIC_HARNESS_CONTRACT_V2_3_1_CORRECTION.md
4afca93172a39cb8924b48285965a791707cec71330b2a8f81328961f92ec01a  successor/OFFICINA_BATCH_SETTLEMENT_CORE_AMENDMENT_V1_DRAFT.md
3ce629ed5afe567b5aba936906c114008df989acb1a946443a6ede1e31dca7de  successor/OFFICINA_BATCH_SETTLEMENT_CORE_AMENDMENT_V1_1_CORRECTION.md
b5a1523290b6b8417a7b3288329cc4a4e5ff80214c8f28e6ea1ae51a450a94c9  successor/OFFICINA_BATCH_SETTLEMENT_CORE_AMENDMENT_V1_1_1_CORRECTION.md
8c47da352ef5954406964647a32e97939c404806bdf9b3d3ff5bc70866e6369a  successor/OFFICINA_GENERIC_HARNESS_SIGNATURE.md
9f1d018e7630d00da954910fa92cacc8005e0ecff90372e513f2fcec8593818b  successor/OFFICINA_GENERIC_HARNESS_SUPERVISOR_CONTROL_CHANNEL_V2_1_CORRECTION.md
ee3171724c89bd7e8f890141f42bf478838608c6f1908f9284218f1e940be635  successor/OFFICINA_GENERIC_HARNESS_SUPERVISOR_CONTROL_CHANNEL_V2_1_1_CORRECTION.md
2cd8b7b53c8efc292535ef79f38aa5e33ce57c5834138cc3deb1700f7edae373  successor/OFFICINA_GENERIC_HARNESS_SUPERVISOR_CONTROL_CHANNEL_V2_1_2_CORRECTION.md
6197d2a4073d35fc978119db32128c50d12594343ac87731640a1d8e19f09e84  successor/OFFICINA_GENERIC_HARNESS_SUPERVISOR_CONTROL_CHANNEL_V2_1_10_4_P1_BINDING.md
2c857fa8ad7be1c861eb8cf561f396e7d2339403c7714abc7958745bf34e5d5d  successor/OFFICINA_GENERIC_HARNESS_SUPERVISOR_CONTROL_CHANNEL_P1_OPERATIVE_COMPOSITE_V1_2.md
```

The correction and closure hashes match the author's custody claims. Custody
does not establish their substantive claims.

## Findings

### Y21-C1 — the peer chain outside the composite remains load-bearing and unamended

The correction itself discloses at `O-6` that the peer chain was not audited.
Direct review finds operative contradictions, not merely historical wording.

1. The accepted generic-harness contract is v2 corrected in order by v2.1,
   v2.2, v2.3, and v2.3.1. Its v2 §5a remains carried because no later
   replacement index replaces it. It says the watchdog owns the deadline and
   **executes** `revoke -> freeze/terminate -> backend synchronize -> prove
   quiescence -> durably settle actual E1`. Under both W-A and W-B the watchdog
   no longer executes a freeze, proves quiescence, or settles. The proposed
   twenty-two composite replacements and seven binding mirrors do not amend
   this accepted peer sentence.
2. The peer evidence predicate at v2.1.1 §Z4.6 conjunct 8 still permits
   `killer == WATCHDOG` when the watchdog was live, and its closing C1 paragraph
   says the watchdog remains a witness. Under corrected `R2`, `R9`, `R10`, and
   `R21`, a watchdog-written `t-freeze-observation.v1` must instead be rejected.
3. v2.1.2 §N5.3 still says “The watchdog remains a witness only,” and §N5.4
   twice classifies the row-4 object as the “watchdog-written”
   `t-freeze-observation.v1`. These are directly adjacent to, and load-bearing
   for, the fallback routing that v2/v2.1 rely on. They are not included in the
   handoff.

The composite calls earlier supervisor/control documents historical, while the
packet directly reopens their §N5/§Z4 peer semantics. Either authority reading
produces the same required repair: amend the currently accepted generic-harness
peer contract and its evidence predicate, or identify the exact still-governing
§Z/§N surface and replace it comprehensively. The current packet does neither.
Per the mandate, an unaudited load-bearing peer surface is unresolved.

This repair does not require another mechanism or author cell. It can remain
inside `P1_WATCHDOG_FREEZER_ROLE_REASSIGNMENT_V1`, but its complete peer surface
must be enumerated, disclosed in the blast radius, and independently reviewed.

### Y21-C2 — the twenty-two-site composite audit is not closed

Replacement `R8` says the watchdog becomes “P1 role-entry layer only.” The
composite nevertheless retains four normative requirements for peer-layer
supervisor-identity reading by the watchdog:

```text
§P1-9.2 property 8                           lines 1452-1453
§P1-13.2 row 3, readers item (b)             lines 2210-2212
§P1-13.7 “read ... in the watchdog” row      line 2366
invariant 87                                 line 2756
```

Invariant 87 rejects a build in which the watchdog does not perform that read.
The correction lists none of these four as a replacement or checked-fine
surface. As written, `R8` and the retained cluster cannot both hold. The repair
may either retain and correctly classify the read in `R8`, or replace the four
requirements; until that choice is made mechanically explicit, the exact count
is not proved to be twenty-two.

There is a second option-specific contradiction. Common `R16` says P1 provides
the watchdog “its two sealed descriptors.” That is true for W-B, but W-A adds
the slot-6 freeze-request socket and expressly changes the watchdog to three
sealed endpoints. `R16` therefore requires a W-A variant. This is not a new
cell, but it refutes the claim that all twenty-two replacements are presently
coherent under both selections.

### Y21-M1 — the filename discrepancy is already resolved, but v2/v2.1 classify it backwards

The governing sequence is:

```text
v2.1 §W3.3:       WATCHDOG/FREEZE/<process_id>.json
v2.1.1 §Z4.5:     expressly replaces that path with
                  WATCHDOG/FREEZE/<witness_id>.json
operative v1.2:   WATCHDOG/FREEZE/<witness_id>.json
```

`witness_id` is the SHA-256 of canonical
`{supervisor_generation_sha256, process_id, table_seq}`. Thus the apparent
discrepancy is a superseded predecessor spelling, not an unresolved conflict
between governing documents. The governing object identity, no-replace replay
key, and evidence filename all use `witness_id`; `process_id` remains a member
of the identifier preimage and a record field, not the filename.

Accordingly, correction `O-8` is false when it calls this a live discrepancy,
and v2 §0.3 `W-7` / §1.1 are stale when they “correct” the path back to
`<process_id>.json`. The stale statement does not change writer authority or
make PCS journal state evidence, because the common classifier writes no peer
record. It must nevertheless be corrected before author selection so the
handoff cannot regress object identity or replay naming.

## Bounded determinations

### 1. Five-locus nullable count-key rename

**Confirmed as an exact proposed rename surface.** In v2.1.2 the bare fallback
key occurs at exactly five normative loci:

```text
§N5.2 schema key list                         line 866
§N5.4 generic field definition                line 900
§N5.4 non-ABSENT legal example                line 906
§N10.2 fact-location row                      line 1370
§N11 crash-cut example                        line 1416
```

`K1` through `K5` replace all five with
`current_unresolved_member_count_or_null`; generic definitions enforce null iff
`rejection_conjunct == 0`, and the two non-`ABSENT` examples retain integer
`0`. No sixth occurrence of the old fallback key exists in the searched signed
chain.

The distinct `unresolved_member_count` key belongs to
`t-freeze-observation.v1`, occurs in its schema/predicate surfaces, and must
remain unchanged. The rename is therefore closed in both directions. This
determination does not cure Y21-C1's separate stale claims that the object is
watchdog-written.

### 2. Separation of the two observation objects

**Confirmed in the replacement text, with one terminology qualification.**
Corrected `R2`, `R9`, and unchanged `R10`, together with `R15`, `R17`, `R18`,
`R20`, `R21`, and `R22`, do not collapse the objects:

| Property | Row-4 observation | §N5 fallback |
|---|---|---|
| schema | `t-freeze-observation.v1` | `t-freeze-fallback-observation.v1` |
| namespace | `WATCHDOG/FREEZE/` | `WATCHDOG/FREEZE_FALLBACK/` |
| install function / logical writer | freeze-witness function | fallback writer under `T_RUNTIME.lock` |
| physical process after reassignment | supervisor role | supervisor role |

The install authorities/functions, schemas, identifiers, predicates, and
namespaces are disjoint. The physical process is intentionally shared, so
“disjoint writers” is valid only as logical writer/install authority, not as a
claim of different process residence. Routing from an absent row-4 object to a
fallback is not authorship. The peer predicate contradictions in Y21-C1 still
prevent final closure.

### 3. Peer-chain assumptions

**Unresolved.** The accepted peer contract and the §Z4/§N5 evidence surfaces
retain load-bearing watchdog-executor/writer assumptions, as Y21-C1 shows.

The audit found no governing sentence that makes PCS process-control journal
state scientific evidence. v2 §3.9, `L8`, `ND-1` through `ND-3`, corrected
`R17`/`R21`, and the pre-existing statement that the PCS journal is a separate
control-plane journal with no scientific field all point the other way.

Fallback identity/count nullability is mechanically repaired by `A-ABS` and
`K1` through `K5`; `process_id` remains mandatory because it is an opaque claim
identifier, not a PID. The remaining peer-chain defect concerns executor and
evidence-writer identity, not nullable fallback values.

### 4. Reassignment, execution authority, and tokens

The two PCS execution sites are scientifically coherent in principle:

- the supervisor dead-watchdog route requests `SIGNAL_GROUP`, whose `_killpg`
  executes in the PCS; and
- the common classifier executes `_killpg` autonomously in the PCS under `KV`.

Both preserve the sole-PCS-caller rule and `S-12`; neither journal terminal is
peer evidence. The common token can authorize this shared widening without a
new author cell. But the current twenty-two-site surface, the W-A `R16` text,
and the governing peer chain are incomplete. The disclosed common token is
therefore not yet sufficient for informed selection.

### 5. Filename and object identity

Resolved in favor of `<witness_id>.json` by §Z4.5 and the operative composite.
With that correction, there is no change to logical writer authority, replay,
no-replace identity, or evidence acceptance. The packet's contrary historical
classification must be repaired.

### 6. Routing and publication boundaries

The following mechanisms themselves remain closed on v2.1 bytes:

- §N5.3 record-first `PROCESS` invalidity, all-live batch, unknowable pool, and
  full §4c charge;
- endpoint-loss semantics: endpoint unavailability, not supervisor death, with
  orderly close, half-close, crash, and exit indistinguishable;
- W-A's constant target-free request, PCS-side `G-1` gate, one accepted action,
  full-charge pricing, and bounded pre-reaper service window;
- W-B's autonomous, record-first PCS action with constant journal key and no
  second syscall on replay;
- `L6` through `L9` and `ND-1` through `ND-4`: no guarantee of freeze or
  evidence, no death inference, PCS journal invisibility, and no inference from
  `ABSENT` to physical non-occurrence.

They do not compensate for the unamended peer acceptance/writer surface.

### 7. Outcome independence of the W-B recommendation

**Confirmed.** The v2.1 corrections to site count, rename count, pinned
constants, verifier rules, tests, and the common classifier fall equally on
W-A and W-B. The additional peer-contract reassignment found here also falls on
both. W-B's recommendation remains based on governance and engineering facts:
zero watchdog topology/opcode additions and no new dependency on a live,
responsive watchdog. It does not depend on learner behavior, qualification,
comparison, Q/C, a scientific datum, or an outcome.

W-B may remain recommended after repair. Neither option is selectable on the
present bytes.

## Smallest bounded repair

1. Re-audit and amend the accepted generic-harness peer contract and the
   load-bearing §Z4/§N5 evidence surfaces so no reachable rule permits or
   requires a watchdog executor or evidence writer; make the peer acceptance
   predicate reject `killer == WATCHDOG` on every new-contract path.
2. Resolve the identity-read cluster by either preserving it explicitly in
   `R8` or replacing property 8, row-3 reader (b), the §P1-13.7 read row, and
   invariant 87. Recompute the exact composite site count.
3. Give `R16` a W-A three-endpoint variant and retain its W-B two-pipe form.
4. Correct v2 §0.3/§1.1 and v2.1 `O-8`: §Z4.5 already selected
   `<witness_id>.json`; do not reopen filename identity.
5. Update the handoff, blast-radius table, common-token surface, closure, and
   bounded questions, then obtain independent final X/Y confirmation on the
   new identical committed bytes.

These repairs are bounded and need no additional option or author cell, so the
appropriate verdict is revision rather than blockage.

## Authorization boundary

This verdict authorizes no W-A/W-B selection and accepts no amendment token. It
authorizes no implementation, activation, process control, resource spend,
datum, outcome, Proof, or claim movement. Kirill's selection authority is not
opened on these bytes.

```text
T = NOT_ACTIVATED
PROGRAMME CLAIM = OPEN
PROCESS-IDENTITY CELL = NOT SELECTED
WATCHDOG-FREEZE CELL = NOT SELECTED
```
