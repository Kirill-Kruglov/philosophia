REVISE_OFFICINA_P1_WATCHDOG_FREEZE_CHOICE_V2

# Independent Y-line bounded confirmation — P1 watchdog-freeze choice v2

**Reviewer:** GPT Sol, independent Y-line scientific-validity and governance reviewer.  
**Scope:** bounded confirmation of the committed v2 packet against both v1 reviews and the governing signed chain. The author closure was treated as untrusted.

## Findings

### Critical

None.

### Major — YV2-M1: `A-ABS-2` is constructible, but its claimed exact signed-sentence closure is incomplete

**Finding.** The nullable `EVIDENCE_ABSENT` value set is constructible under either process-identity outcome. However, §6.3's claim that the amendment reopens only the §N5.2 key-list sentence while §N5.4 remains unchanged is false after `A-ABS-2` globally renames `current_unresolved_member_count` to `current_unresolved_member_count_or_null`.

The governing `OFFICINA_GENERIC_HARNESS_SUPERVISOR_CONTROL_CHANNEL_V2_1_2_CORRECTION.md` contains four additional normative references to the old key:

- §N5.4's field-definition block at line 900;
- §N5.4's legal `FREEZE_INSTANT_UNKNOWN` example at line 906;
- §N10.2's fact-location table at line 1370; and
- §N11's crash-cut example at line 1416.

The two examples remain semantically valid on their non-`ABSENT` branch, but they cannot remain byte-unchanged: after the schema key is renamed, they must name `current_unresolved_member_count_or_null = 0`. The field-definition and fact-location rows likewise require the new key and must state that it is null exactly on `rejection_conjunct == 0`.

**Exact consequence.** Original findings X `F3` and Y `Y-C3` are not fully closed as dispositioned. Applying the current deterministic handoff would leave a signed schema and four signed readers/descriptions naming different keys. The branch's values, §N5.3 routing, unknowable-pool accounting and full charge are sound; the defect is the incomplete normative rename surface. No new author cell is required.

### Major — YV2-M2: two of the twelve role-reassignment replacements conflate the fallback schema with the freeze-observation schema

**Finding.** The twelve operative-composite sites in §7.2 are a complete freezer/witness-role enumeration, but exact replacements `R2` and `R9` are internally inconsistent with `R10` and the signed §N5 writer model:

- `R2` says the §P1-13.2 row-4 freeze-witness record class is written by the supervisor on both the dead-watchdog route and the §N5 `ABSENT` fallback route.
- `R9` similarly adds the §N5 `ABSENT` fallback route to the executing-process clause for row 4.
- `R10` correctly says the `t-freeze-observation.v1` writer is called from the supervisor's dead-watchdog route only.
- Signed §N5.1–§N5.3 defines `ABSENT` as a different object, `t-freeze-fallback-observation.v1`, in `WATCHDOG/FREEZE_FALLBACK/`, written by the supervisor under `T_RUNTIME.lock`.

**Exact consequence.** Original X finding `F1` is not fully closed: a literal v1.3 handoff would assign the separate fallback route to the wrong row-4 schema and contradict the single-writer text. This does not permit fabricated evidence—the schemas and namespaces remain distinct in the governing contracts—but the proposed replacement text is not single-valued enough for author selection.

### Minor

None.

## One-to-one disposition of the original findings

| Original finding | Bounded Y-line determination |
|---|---|
| X `F1`, incomplete freezer/witness amendment surface | **Not fully closed.** The twelve operative-composite sites are complete, and the handoff now replaces rather than duplicates contradictory rows, but `R2` and `R9` incorrectly put the separate §N5 fallback on the row-4 `t-freeze-observation.v1` writer path. |
| X `F2`, EOF/death conflation and empty-record discrimination | **Closed.** `PEER_CONTROL_ENDPOINT_LOST` proves endpoint unavailability only; exit, crash, orderly close and half-close have the same validity-first continuation. A zero-length record with `_MSG_EOR` is malformed and cannot trigger a freeze. |
| X `F3`, unconstructible numeric `ABSENT` fallback | **Not fully closed.** `A-ABS-1..A-ABS-6` make the values constructible, but the global count-key rename omits four normative references. |
| Y `Y-C1`, incomplete/nonconstructible common scope and classifier | **Closed.** The scope is P1-owned, current-generation, role-bounded, unreaped, `OWNED`, non-null and freshly kernel-verified; it is deduplicated before signalling. Every exclusion, identity result, signal result, enumeration result, quiescence result, timeout and exception has a token and a deterministic terminal. |
| Y `Y-C2`, W-A repeatable invalidity/resource capability | **Closed.** The request is constant, target-free and generation-bound; the PCS-side endpoint-loss gate prevents healthy-generation acceptance; the generation-wide terminal rule prevents a replacement handle from obtaining a second accepted action. Rejection/replay performs no process-control syscall, and silence remains an honestly priced liveness denial. |
| Y `Y-C3`, identity-cell entanglement at `ABSENT` | **Not fully closed only on the rename surface identified in YV2-M1.** The actual nullable values establish orthogonality under either identity outcome. |
| Y `Y-M1`, endpoint loss overclaimed as death | **Closed.** No death inference or ordering identity between the protocol socket and update pipe remains. |
| Y `Y-M2`, W-B acts before journalling | **Closed.** `ACCEPTED` is appended and fsynced before any signal; every replay/restart that sees it performs no second freeze. |
| Y `Y-M3`, W-A ordering against the non-returning reaper | **Closed.** The bounded service window precedes the reaper state; socket EOF, watchdog loss, timeout, stale generation and restart have no-freeze deterministic routes. |
| Y `Y-m1`, insufficient publication caveat | **Closed.** `L6..L9` and `ND-1..ND-4` separate endpoint loss, actual freeze occurrence, PCS journal state and peer evidence. |

No original mechanism is reopened beyond the two concrete textual contradictions above.

## Bounded determinations

### 1. Closure of the original findings

All original mechanism repairs are confirmed except the exact closure of X `F1` and X `F3` / Y `Y-C3` for the reasons stated in YV2-M1 and YV2-M2. Those are bounded replacement/enumeration repairs, not new design cells.

### 2. `EVIDENCE_ABSENT` constructibility under either identity outcome

The proposed branch has a truthful source for every required field:

| Field | Constructible value and authority |
|---|---|
| `schema` | fixed `philosophia.officina.t-freeze-fallback-observation.v1` literal |
| `scientific_outcome` | fixed `false` |
| `supervisor_generation_sha256` | current durable supervisor-generation identity |
| `fallback_witness_id` | deterministic §N5.1 hash of generation, opaque `process_id`, `table_seq`, and the two null rejected-object members |
| `process_id` | durable canonical process identifier from the claim/lease and watchdog table; it is not a PID and survives either identity choice |
| `pgid_or_null` | `null`, biconditional with `rejection_conjunct == 0` |
| `start_identity_or_null` | `null`, same biconditional |
| `deadline_ns` | durable deadline in the expected watchdog-table row |
| `table_seq` | durable expected/current watchdog table sequence |
| `rejected_witness_path_or_null` | `null` for the signed `ABSENT` sentinel |
| `rejected_object_sha256_or_null` | `null` for the same sentinel; no nonexistent object is hashed |
| `rejection_conjunct` | integer `0` |
| `unknown_reason` | `EVIDENCE_ABSENT` |
| `current_unresolved_member_count_or_null` | `null`; no unnamed group count is fabricated |
| `supervisor_quiescence` | `UNKNOWN`; no unnamed group is declared proved quiescent |
| `killer` | fixed `SUPERVISOR` |
| `created_utc` | canonical current UTC supplied by the supervisor writer |

There is no `freeze_ns` or `overrun_ns` field in the fallback schema. Neither is synthesized. All object hashes that the schema actually requires are available or deterministically null as specified. Thus **no value remains unavailable**; the defect is only that four signed references still use the superseded count-key name.

### 3. Nullable branch, routing and accounting

The branch reopens one peer contract, three keys and one discriminated branch in substance. The three null biconditionals, `UNKNOWN` quiescence and `EVIDENCE_ABSENT` prohibit numeric identity, member-count, instant, overrun and success fabrication. §N5.3 remains record-first `PROCESS` invalidity, the all-live batch, the unknowable pool and full §4c charge. It cannot produce a valid terminal, zero-overrun result, scientific datum or comparison input.

The packet's claim that no additional signed sentence changes is refuted only by the four mechanical old-key references in YV2-M1. Routing, identifier preimage, conflict order and §Z4.6 remain unchanged.

### 4. Total classifier and partial/inconclusive routes

The P1-owned classifier is total over the signed handle role/state/ownership sets and has deterministic benign, non-benign and structural exclusions. `FREEZE_TOTAL_PROVED` is the only P1 journal completion terminal; `FREEZE_INCOMPLETE`, `FREEZE_NOT_ATTEMPTED`, an `ACCEPTED` crash cut, denial, malformed input, stale generation and every partial side effect all settle as whole-generation `PROCESS` invalidity with invalidity dominant.

No classifier terminal is a resource success, capacity or custody fact, qualification/comparison input, Q/C fact, scientific evidence or Proof. Full charging is a deterministic accounting consequence, not a success and not outcome-dependent.

### 5. W-B trigger, authority and replay

W-B acts only on `PEER_CONTROL_ENDPOINT_LOST` as discriminated by `E-1a`. It expressly does not infer supervisor death, and the protocol EOF and watchdog-pipe EOF are independent observations. The autonomous action remains in the sole PCS and is bounded to the verified §3 scope.

The constant `(generation_id, "PEEREOF", 1)` key, stale-head check and durable `ACCEPTED` fsync precede every signal. `ACCEPTED`, `COMPLETED` and `TERMINAL_INVALID` all suppress every later syscall. A PCS restart cannot adopt the generation. Crash, re-entry or repeated endpoint observation therefore cannot cause a second autonomous freeze.

### 6. W-A capability, gate and pricing

W-A's four-field request contains no PID, PGID, handle, role, count, table sequence or target. Acceptance requires the PCS's already-recorded endpoint-loss fact. The constant handle key plus the generation-terminal rule permits at most one accepted action across original and replacement watchdogs. Early, malformed, duplicate, replayed and post-terminal records perform no process-control syscall and cannot invalidate a healthy generation.

The remaining costs are honestly material: a new descriptor/topology and grammar surface, a bounded 60-second service window, a real but target-free capability, and freeze denial if the watchdog is absent, wedged, silent or loses the ordering race between the independent endpoints. The accepted action forces the already-terminal generation through full-charge invalidity. None creates scientific selection power.

### 7. Freezer/witness reassignment and publication

The twelve-site operative-composite audit is complete, and both options honestly demote the watchdog from executor and witness of record. Publication `L6..L9` is adequate: freeze occurrence is not guaranteed; endpoint loss is not death proof; PCS journal completion is scientifically invisible; and `ABSENT` means evidence unavailable even if all groups were actually stopped.

The role reassignment cannot be confirmed on these bytes because `R2` and `R9` misidentify the §N5 fallback as row-4 freeze evidence. Correcting those two replacements preserves, rather than changes, the intended scientific boundary.

### 8. Comparative recommendation

The recommendation is based only on signed-authority fidelity, constructibility, mechanical testability, liveness and blast radius. It predicts no learner, arm, qualification, comparison, Q/C or scientific outcome.

W-B's advantage survives the honest common cost: both options carry the classifier, nullable fallback amendment, twelve normative role changes and publication amendment. W-B still adds no watchdog endpoint, opcode, target-free capability, dispatch grammar or new watchdog liveness dependency. Its one autonomous PCS initiative is disclosed and mechanically narrower than W-A's added topology. **W-B remains the Y-line validity/governance recommendation after the exact repairs below.**

### 9. `setsid()` escape and quiescence substitution

A controller/worker `setsid()` or `setpgid()` while its lease is open violates the activation protocol's signed process-group immutability premise. It is not an allowed alternative process identity. `KV-5` detects the mismatch before signalling, records `GROUP_CHANGED`, and forces `FREEZE_INCOMPLETE` / whole-generation `PROCESS` invalidity. The mechanism therefore preserves the signed validity premise by failing closed; the target's violation is never evidence or resource success.

The 50 ms × 16-pass PCS schedule differs mechanically from §W3.3's watchdog 100 ms × 8-pass schedule but preserves its stopped/dead/absent proof predicate and total 800 ms budget. Because the PCS terminal is P1-only and scientifically invisible, this substitution does not amend the peer evidence predicate or manufacture quiescence evidence. It is adequately disclosed inside the common `P1_PCS_FREEZE_CLASSIFIER_V1` amendment rather than silently treated as byte-identical §W3.3 behaviour.

## Smallest exact repair

1. In §6.3 and the v1.3 handoff, enumerate and replace all four old-key references in `OFFICINA_GENERIC_HARNESS_SUPERVISOR_CONTROL_CHANNEL_V2_1_2_CORRECTION.md`: §N5.4 lines 900 and 906, §N10.2 line 1370, and §N11 line 1416. Each must use `current_unresolved_member_count_or_null`; the non-`ABSENT` examples retain integer `0`, and the generic field descriptions state null iff `rejection_conjunct == 0`.
2. Replace §7.3 `R2` with: the row-4 `t-freeze-observation.v1` class is written only by the supervisor on the signed dead-watchdog route; the §N5 `ABSENT` route writes the separate `t-freeze-fallback-observation.v1` class.
3. Remove the §N5 `ABSENT` fallback route from `R9`'s row-4 executing-process clause. Keep `R10` unchanged: the row-4 freeze-witness function is called from the supervisor's dead-watchdog route only. Update the closure's X `F1`, X `F3` and Y `Y-C3` dispositions accordingly.

No mechanism, selection set or new author cell is needed. After these repairs, both W-A and W-B remain selectable in principle, and W-B remains recommended.

## Custody and authorization boundary

Recomputed target hashes:

```text
72212a986d9551ef47718e871a81951b55a849a10d34eb12e6276499cb675505  successor/OFFICINA_P1_WATCHDOG_FREEZE_AUTHOR_CHOICE_PACKET_V2_DRAFT.md
7b3708550806fcd5742accb5858a2da05a87c4b22ee7fbdffe73ecdbad07759e  reviews/opus5_officina_p1_watchdog_freeze_choice_v2_closure.md
```

The reviewed v1 reports recompute as:

```text
c87cc69f93ddd64c8364bcbcce3fa97e32855b55597a57a44bb05bffeee04ae1  reviews/opus_officina_p1_watchdog_freeze_choice_review.md
37474607e46394178d9dca1f946fd68e58f852cf3157b7948a6e7de6ef13808b  reviews/sol_officina_p1_watchdog_freeze_choice_review.md
```

This `REVISE` verdict authorizes no W-A/W-B selection, amendment token, implementation, activation, process control, resource spend, datum, outcome, Proof or claim movement. The process-identity cell remains unselected.

```text
T = NOT_ACTIVATED
PROGRAMME CLAIM = OPEN
PROCESS-IDENTITY CELL = NOT SELECTED
```
