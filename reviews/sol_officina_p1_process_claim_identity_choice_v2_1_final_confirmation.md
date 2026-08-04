REVISE_OFFICINA_P1_IDENTITY_V2_1

# Independent Y-line final confirmation — P1 process-claim identity choice v2.1

**Reviewer:** GPT Sol, independent Y-line validity/governance reviewer.

**Date:** 2026-08-03.

**Scope:** bounded final confirmation of the v2 packet as modified by the v2.1 correction. The author closure was treated as untrusted. This review performed only reads, textual lineage tracing, and SHA-256 recomputation. It created this one deliverable and authorizes no implementation, activation, process control, spend, datum, outcome, Proof, or claim movement.

## 1. Executive determination

The v2.1 correction closes the indirect-read defect and correctly identifies **two direct, live, named persistent destinations** of the lineage value: the `T_PROCESS_STARTED` event and the `process_claim_sha256` key of `t-process-record.v1`. The historical `OK/CLAIM` matrix is not a live third destination under the operative authority hierarchy.

The complete one-way boundary is nevertheless **not confirmable on these bytes**, for two independent reasons:

1. `C-5`, `DC-1`, and `DC-6` say there is exactly one SHA-256/declassification and no other digest derived from a carrier, while the same correction expressly requires a second `ACC-5` invocation over `occupant_bytes` for collision conjunct `X-4`. Calling that result a boolean comparison operand does not make the second digest cease to exist. The collision use is legitimate integrity checking, but the count and classification texts are contradictory.
2. `DC-3`, `DC-4`, `DC-5`, and `WL-4(a)` overstate what whole-object hashing proves. Given the other eighteen canonical fields, the equality test over the forced `attested_pgid == attested_pid` space has at most 4,194,304 candidates. The actor constructing the claim already possesses or determines those other fields; later readers may obtain them from the claim and its archive. The digest is therefore an efficiently searchable commitment to the PID/PGID pair. It transfers no process-control authority, but it can be an **informational proxy and equality evidence for process identity**. The absolute claims “never process identity” and “never evidence/comparison” are false outside their narrower, normative authorized-use sense.

Accordingly, Kirill's selection and the conditional weakening token are **not authorized on v2.1**. A bounded textual revision is required; no new architecture cell is required.

## 2. Custody and recomputed hashes

All hashes below were recomputed from the current bytes, not copied from the closure.

### 2.1 Packet and review chain

```text
ad8b5791f043f201c00812a11de2ab3b765664e65e6d0ebf9778e150913096d3  successor/OFFICINA_P1_PROCESS_CLAIM_IDENTITY_AUTHOR_CHOICE_PACKET_V1_DRAFT.md
e8bceb8098c9a1d96fcd76f0796fccdcd49b79ce4cd690d1ef3a7d9ced54e128  reviews/opus5_officina_p1_process_claim_identity_author_choice_packet.md
bfa7f6dd6a09313033b2a00c75f0e1e0632c63f65733b80424ee889433364f3b  reviews/opus_officina_p1_process_claim_identity_choice_review.md
705b36b6ce1a9387261f66f2a473295be4384903b0e0240ae8e7496af6899e80  reviews/sol_officina_p1_process_claim_identity_choice_review.md
f5d95a0d4a7c72731b5a20cf668e67dbc66329e0989fb945bd0a5727717f6095  successor/OFFICINA_P1_PROCESS_CLAIM_IDENTITY_AUTHOR_CHOICE_PACKET_V2_DRAFT.md
b7d061f5c60d75705f50ffc100bff24664336107dd450a8372e825c6f1afffa0  reviews/opus5_officina_p1_process_claim_identity_choice_v2_closure.md
0b104f3ec240acc5e067184efb752091f92920da7773c78aa35337de6a30f129  reviews/opus_officina_p1_process_claim_identity_choice_v2_confirmation.md
152b6dd2237a63d3ada6bd6a82a828892443a7752f838abf71cba0401ac01eb8  reviews/sol_officina_p1_process_claim_identity_choice_v2_confirmation.md
3796de017449a9786db0b9b0ca0e8c2d84762e2239463033773b1fdb92b8ef37  successor/OFFICINA_P1_PROCESS_CLAIM_IDENTITY_AUTHOR_CHOICE_PACKET_V2_1_CORRECTION.md
56d0f598331a713918ea3f5b642449dd4dca1a08224b6e9eb4afb239ba128246  reviews/opus5_officina_p1_process_claim_identity_choice_v2_1_closure.md
```

The v2 target, both prior v2 confirmations, the v2.1 correction, and the untrusted v2.1 closure are byte-identifiable and internally acyclic.

### 2.2 Live governing and signed inputs

```text
2c857fa8ad7be1c861eb8cf561f396e7d2339403c7714abc7958745bf34e5d5d  successor/OFFICINA_GENERIC_HARNESS_SUPERVISOR_CONTROL_CHANNEL_P1_OPERATIVE_COMPOSITE_V1_2.md
cd106d7fef491601f9ff948aba3ba0ceaac0774ac18a6564247c0c5899b4c40c  successor/OFFICINA_T_ACTIVATION_PROTOCOL_V2_CORRECTION.md
6ef98132990f8c686fa9678509bb07ba8259f3d6e4cbc483861edfc03ea8e3ef  successor/OFFICINA_SUPERVISOR_PROCESS_AUTHORITY_SELECTION_V1_SIGNATURE.md
c494ef8884948bd0e737373d2d57a3ab74bbd456db2c3463711c4405f2fdf86a  successor/OFFICINA_SUPERVISOR_AUTHOR_SELECTIONS_V1_SIGNATURE.md
4918a208bb94549ba3e7c38571265e723cc51a0a3394e291a62a85c333d864a6  successor/OFFICINA_SUPERVISOR_OUTPUT_CAPACITY_SELECTION_V1_SIGNATURE.md
64b8d3f63594b79a6abc767a032383c5704beaf09b32a1e0c58fdc444bb0af71  successor/OFFICINA_GENERIC_HARNESS_CONTRACT_V2_DRAFT.md
6bbaf4d17295a8a4d4fa0f42a9347707e4e2319ea5183163c756b94008764077  successor/OFFICINA_GENERIC_HARNESS_CONTRACT_V2_1_CORRECTION.md
624dfc9b34c8009ee4c1610bfff91f5cfceea128e84d850c3e90ffb1e7be9e2f  successor/OFFICINA_GENERIC_HARNESS_CONTRACT_V2_2_CORRECTION.md
b2288b0a9fb44d23c19d853aeb6d57edd4de888c6058af8001a379f9237d3154  successor/OFFICINA_GENERIC_HARNESS_CONTRACT_V2_3_CORRECTION.md
724d633a55668013b78058eed1c76e12e9bbaf487f71ea94b7a4568ea1ced8a0  successor/OFFICINA_GENERIC_HARNESS_CONTRACT_V2_3_1_CORRECTION.md
8c47da352ef5954406964647a32e97939c404806bdf9b3d3ff5bc70866e6369a  successor/OFFICINA_GENERIC_HARNESS_SIGNATURE.md
4afca93172a39cb8924b48285965a791707cec71330b2a8f81328961f92ec01a  successor/OFFICINA_BATCH_SETTLEMENT_CORE_AMENDMENT_V1_DRAFT.md
3ce629ed5afe567b5aba936906c114008df989acb1a946443a6ede1e31dca7de  successor/OFFICINA_BATCH_SETTLEMENT_CORE_AMENDMENT_V1_1_CORRECTION.md
b5a1523290b6b8417a7b3288329cc4a4e5ff80214c8f28e6ea1ae51a450a94c9  successor/OFFICINA_BATCH_SETTLEMENT_CORE_AMENDMENT_V1_1_1_CORRECTION.md
```

The generic-harness signature accepts the v2 draft as corrected in order through v2.3.1. None of those corrections replaces §2c's `T_PROCESS_STARTED` carriage. The activation protocol fixes the claim and final-record key sets.

### 2.3 Superseded supervisor/control-channel chain audited for apparent carriage

```text
bed7033eab1fa123598f6d4b03a7b69cb81c040af4cec4b21ca0e2e074181b7e  successor/OFFICINA_GENERIC_HARNESS_SUPERVISOR_CONTROL_CHANNEL_V2_DRAFT.md
9f1d018e7630d00da954910fa92cacc8005e0ecff90372e513f2fcec8593818b  successor/OFFICINA_GENERIC_HARNESS_SUPERVISOR_CONTROL_CHANNEL_V2_1_CORRECTION.md
ee3171724c89bd7e8f890141f42bf478838608c6f1908f9284218f1e940be635  successor/OFFICINA_GENERIC_HARNESS_SUPERVISOR_CONTROL_CHANNEL_V2_1_1_CORRECTION.md
2cd8b7b53c8efc292535ef79f38aa5e33ce57c5834138cc3deb1700f7edae373  successor/OFFICINA_GENERIC_HARNESS_SUPERVISOR_CONTROL_CHANNEL_V2_1_2_CORRECTION.md
72bfcc3f088ba538157145aed0bccc95a9ff2e1ad6c41f0579f32c9926274888  successor/OFFICINA_GENERIC_HARNESS_SUPERVISOR_CONTROL_CHANNEL_V2_1_3_CORRECTION.md
cc5af143f7e4dd886e21ca9e6734618236c2cc32daf2d7a610943e731cb7cc62  successor/OFFICINA_GENERIC_HARNESS_SUPERVISOR_CONTROL_CHANNEL_V2_1_4_CORRECTION.md
7ef8e4d3ac8f281dd50191e81d2760ed4467648b45ed2b17f6ce2012e4d017d4  successor/OFFICINA_GENERIC_HARNESS_SUPERVISOR_CONTROL_CHANNEL_V2_1_5_CORRECTION.md
e4aa9ef4f0de2fe705d54cb7ac016212098cfe71b8575ef2b435e8c9b09f5609  successor/OFFICINA_GENERIC_HARNESS_SUPERVISOR_CONTROL_CHANNEL_V2_1_6_CORRECTION.md
789732476938ca8c1436eebb49e54a1f994c2c000b7689e1eb9aad082f6871a8  successor/OFFICINA_GENERIC_HARNESS_SUPERVISOR_CONTROL_CHANNEL_V2_1_7_CORRECTION.md
33b0b91621439bdc42b4c41b3d00741b8c20d014a686097d2bc63c001db0ed50  successor/OFFICINA_GENERIC_HARNESS_SUPERVISOR_CONTROL_CHANNEL_V2_1_8_CORRECTION.md
1468c9ab1806c1eb25523e6a9fd8567592076f0dc74418ca698a52f933c7f3b0  successor/OFFICINA_GENERIC_HARNESS_SUPERVISOR_CONTROL_CHANNEL_V2_1_9_CORRECTION.md
2b4f9cad7be7a69527e828c73928a399209fcd8151780b9b4c839934893e0dc8  successor/OFFICINA_GENERIC_HARNESS_SUPERVISOR_CONTROL_CHANNEL_V2_1_10_CORRECTION.md
2d4d4b189e460605ce95f8f464d7ef1c6d0c8ce317ad26033a91b4d2c556759b  successor/OFFICINA_GENERIC_HARNESS_SUPERVISOR_CONTROL_CHANNEL_V2_1_10_1_CORRECTION.md
c7ff27775fd1b394b850be1be3e1d361d95f5e12af251949f8363980bd2900ec  successor/OFFICINA_GENERIC_HARNESS_SUPERVISOR_CONTROL_CHANNEL_V2_1_10_2_CORRECTION.md
02d862e76f76a57cd154ecfd8a67f88abb02c2ce324e4026e4145069cee63143  successor/OFFICINA_GENERIC_HARNESS_SUPERVISOR_CONTROL_CHANNEL_V2_1_10_3_CORRECTION.md
6197d2a4073d35fc978119db32128c50d12594343ac87731640a1d8e19f09e84  successor/OFFICINA_GENERIC_HARNESS_SUPERVISOR_CONTROL_CHANNEL_V2_1_10_4_P1_BINDING.md
798d0cbd51e93cc1f4c0a443785f90d90a2e121d35738189cbee9c61acf557cc  successor/OFFICINA_GENERIC_HARNESS_SUPERVISOR_CONTROL_CHANNEL_V2_1_10_5_P1_PRE_XY_REPAIR.md
8f806e33d85c00933871072dadda30110f18ea6bf34b5ebc388f23f8b067143e  successor/OFFICINA_GENERIC_HARNESS_SUPERVISOR_CONTROL_CHANNEL_V2_1_10_6_PRE_XY_REPAIR.md
66dc6fdc26d8b27f50e8de9603e8ac217492a13385c04822a1450a938495d51a  successor/OFFICINA_GENERIC_HARNESS_SUPERVISOR_CONTROL_CHANNEL_V2_1_10_7_PRE_XY_CONSISTENCY_REPAIR.md
d2975d19c553d9f9338bacff9d0a2af1855af45881e305a8706c110820896935  successor/OFFICINA_GENERIC_HARNESS_SUPERVISOR_CONTROL_CHANNEL_P1_OPERATIVE_COMPOSITE_V1.md
90ddf3ff76a1d08994c06d9c7f938e45f32fdeb46f58251ebb162bc96cf01680  successor/OFFICINA_GENERIC_HARNESS_SUPERVISOR_CONTROL_CHANNEL_P1_OPERATIVE_COMPOSITE_V1_1.md
```

The v1.2 composite's authority hierarchy makes all files in §2.3 immutable provenance only and makes v1.2 the sole operative implementation object. Their bytes were still inspected because the apparent `OK/CLAIM` third destination occurs there.

## 3. Determination 1 — `C-5`, accessors, destinations, and `DC-1..DC-7`

| Item | Determination | Reason |
|---|---|---|
| `C-5` | **Requires revision** | The validated whole-object lineage hash is a legitimate fifth consumer, but “EXACTLY ONE SHA-256” is contradicted by the required second `ACC-5` call at `X-4`. |
| `ACC-4` | **Confirmed, bounded** | One canonical whole-record serializer, with no field extraction, is the right mapping-to-carrier boundary. It must remain after complete validation. |
| `ACC-5` | **Requires revision** | One accessor definition is coherent, but it has two live call sites and produces two digest values: the persistent lineage value and the transient occupant comparison value. The specification must classify both honestly. |
| `ACC-R5` | **Confirmed** | The ban on subscript, slicing, decode, iteration, regex, formatting, branching, logging, and individual field return prevents the accessor bodies from extracting either identity field. |
| Exactly two destinations | **Confirmed only as direct raw-digest destinations** | `D-1` and `D-2` are the only live named persistent fields carrying the raw lineage digest. Archive replication and hashes of containing objects are continuations of those destinations, not third raw-digest schema fields. |
| `DC-1` | **Requires revision** | “Exactly one ... and never a second” conflicts with `X-4`; “declassification” must also state that it is not confidentiality declassification. |
| `DC-2` | **Proved nonblocking** | It correctly says that release from the restricted field class is not unconstrained authorization. |
| `DC-3` | **Requires revision** | It is an authorized integrity/lineage identifier, but cryptographically it is also a searchable commitment to the full claim and thus can identify the PID/PGID conditionally on the other fields. “Never process identity” is too absolute. |
| `DC-4` | **Requires revision** | The signed sink prohibition can ban authorized uses, but cannot truthfully say the digest provides no comparison or evidence channel. Its defining operations and `X-4` are comparisons/equality evidence. |
| `DC-5` | **Requires revision** | The five-root static ban prevents conforming implementation code from enumerating candidates, but it does not make inversion/search impossible to another reader with the digest and the eighteen known values. |
| `DC-6` | **Requires revision** | A second carrier-derived SHA-256 exists at `X-4`. It is transient and integrity-only, but it is still a second digest value. |
| `DC-7` | **Confirmed, bounded** | Invalidity-first handling is coherent for noncanonical operands, unauthorized call sites, and unauthorized direct destinations. It does not cure the semantic overclaims above. |

Thus `C-5`, `ACC-4/ACC-5`, `ACC-R5`, exactly-two direct destinations, and `DC-1..DC-7` do **not**, in their present combined wording, form a complete one-way integrity-lineage boundary.

## 4. Entire live carriage and consumer audit

| Stage or apparent stage | Live status | Classification |
|---|---|---|
| Validated `t-process-claim.v1` canonical bytes | live | `C-5` input; contains both numeric identity fields. |
| `ACC-4` canonical serialization | live | Restricted carrier production; no individual-key read. |
| First `ACC-5` call | live | Produces the raw lineage digest intended for persistence. |
| `D-1`: `T_PROCESS_STARTED.process_claim_sha256` | live and governing | First direct persistent destination. The event is non-state-bearing but durable. |
| Hash of the complete `T_PROCESS_STARTED` entry | live and governing | A superseding composite. It includes the raw digest transitively and seeds `t-active-lease.v1.prior_charge_event_sha256`. This is integrity lineage, not a third raw-digest field. |
| Lease/event hash chain | live and governing | Subsequent charge-event and lease equality/hash checks carry only containing-entry hashes. Their use is lineage, reservation, and state consistency; no PID addressing follows from them. |
| `D-2`: `t-process-record.v1.process_claim_sha256` | live and governing | Second direct persistent destination. |
| Hash of the final process record | live and governing | A superseding composite carried by `T_PROCESS_STOPPED.process_record_sha256`; it is record integrity/lineage, not raw digest carriage. |
| Close/invalid-close archive set | live and governing | Archives the claim and final record. The archived final record is a copy of `D-2`, and the archived claim exposes the fields directly. Archive/Git object and commit hashes are containing-object lineage, not new raw-digest schema destinations. |
| Recovery and post-crash verification | live and governing | Re-reads retained claim/final-record/archive facts for hash and canonical equality. It may consume `D-2` or a containing hash for integrity; no recovery rule authorizes PID-based control from the digest. |
| `EEXIST` `X-1` byte equality | live | Exact canonical-byte integrity comparison. |
| `EEXIST` `X-4` occupant SHA-256 equality | live | A second `ACC-5` call and second digest value, consumed transiently by a boolean integrity check. It is not a third persistent destination, but it refutes the one-digest count. |
| P1 process-control `J4` / replay | live after Option A selection | Carries the attested PID/PGID tokens themselves in the complete response vector; it does **not** carry `process_claim_sha256`. It is a separate restricted-identity journal consumer already accounted for by the v2 journal repair. |
| Peer client-journal reply | no live raw-digest schema proved | The operative peer contracts retain journal/recovery responsibilities but do not define a `process_claim_sha256` reply field. No current contract text creates a third destination by implication. |
| Historical `OK/CLAIM` reply matrix | non-governing | The raw field occurs in the v2 draft, v2.1 correction, and v2.1.1 cached-reply row. The v1.2 composite authority hierarchy expressly supersedes that entire chain for behaviour and verification, does not restate the matrix, and the two accepted peer contracts omit the key. It is provenance, not a live third destination. |

This audit confirms the narrow direct-destination count of two. It also shows why the boundary must enumerate **indirect lineage composites** and the transient collision digest rather than using “two destinations” as if it were the whole consumer graph.

## 5. Confidentiality, proxy identity, authority, and evidence

The relevant preimage is not a generic 256-bit secret. Once the other eighteen canonical fields are fixed, `A-P4c` collapses the two identity fields to one value and the candidate set is at most `PID_MAX_LIMIT = 4,194,304`. Enumeration is practical.

`WL-4(a)` is not an adequate answer to this fact. The supervisor constructing the claim already has the activation hash, process id/sequence inputs, start identity, argv, source/config/stack/numerical hashes, device fields, timestamps/clock facts, boot identity, and immutable-control hash. It need not first reopen the claim to know those values. At close, the claim and final record are archived together; an archive reader can read the identity directly, making the digest no confidentiality barrier at all for that reader.

| Channel | Determination |
|---|---|
| Confidentiality / information | **Yes, conditional inferential channel.** The digest is an efficiently searchable commitment to the PID/PGID when the other fields are known. It provides no confidentiality guarantee. For actors who can already read the claim, it adds no new secret because the integers are present in cleartext. |
| Process identity proxy | **Yes informationally; no authoritatively.** A matching candidate digest can stand in for evidence that a candidate PID/PGID belongs to the committed claim. It is not a valid opcode address, handle, or signed selector. |
| Authority / capability | **No.** No request grammar accepts the digest or a PID recovered from it; P1 process-control authority remains PCS/handle mediated. Same-UID kernel power pre-exists and is explicitly non-authorized. |
| Addressing / signalling / waiting | **No authorized channel.** The digest cannot be placed in an opcode request or handle table by a conforming implementation. An actor may learn a PID, but that does not make direct PID control an Officina-authorized act. |
| Selection, capacity, custody, spend, settlement, qualification, Q/C | **No authorized channel.** The closed sink rules can and should continue to reject all such uses. |
| Evidence / comparison | **Yes as an information-theoretic and cryptographic equality channel.** `X-4` itself uses a digest equality as integrity evidence. Candidate enumeration can provide identity evidence. It remains forbidden as scientific evidence or Q/C evidence. |

The honest claim scope is therefore:

> Within the conforming five-root implementation and signed downstream contracts, the digest is authorized only for record integrity and lineage, including canonical equality, event/record hash chaining, archive verification, and recovery verification. It confers no process-control authority and is not an authorized PID selector. It is not confidentiality-preserving and may serve as an inferential identity commitment to a reader who knows the other canonical fields.

That narrower statement preserves the governance boundary without making a false cryptographic claim.

## 6. Downstream equality and hash checks

Every **authorized downstream** equality/hash check found in the governing chain is limited to integrity lineage:

- `X-1` compares canonical claim bytes for idempotent convergence;
- `X-4` compares the occupant carrier digest with the install digest;
- `T_PROCESS_STARTED` is hashed as a complete ledger/event entry and seeds the lease chain;
- the final process record is hashed and named by the stop event;
- archive and recovery checks compare canonical bytes, record hashes, ledger/head hashes, and exact staged sets.

None of these checks authorizes addressing, signalling, waiting, capacity, custody, selection, spend, Q/C, or scientific interpretation. This confirms their **authorized purpose**, but it does not establish the stronger proposition that the digest “cannot be used” as an informational proxy by an actor outside those allowed sites.

## 7. Indirect-read repair and the eight prior closures

### 7.1 Indirect-read repair

**Confirmed at the specification boundary.** `S-25i` reaches all five production roots; `M-R1..M-R5` pin the claim/lease representation and every governed mapping occurrence; `CR-1..CR-4` pin canonical carriers; and `MS-1..MS-12` provide a closed call-site table. The three demonstrated bypasses—mapping iteration, `locals()` reflection, and attribute access—and their byte-slicing variants are rejected without taint analysis, a call graph, or a fixpoint. The C-5 path is an enumerated whole-object exception and does not reopen an individual-field route.

### 7.2 Eight previously closed findings

| Finding | Final Y-line status |
|---|---|
| `X M-1` — incomplete `J4` durability/replay | **Survives.** Complete operand-vector durability and byte-identical replay remain intact and priced. |
| `X m-1` — fresh PGID authority | **Survives.** Fresh `getpgid` is authoritative, stored non-null PGID is a mandatory cross-check, and disagreement fails closed. |
| `X m-2` — PID bound | **Survives.** `1..4194304`, strict grammar, and over-range rejection remain fixed. |
| `X m-3` — freeze-actor conflation | **Survives.** Supervisor/PCS-loss and watchdog/supervisor-loss cases remain distinct. |
| `Y-C2` — unconstructible replay | **Survives.** The tuple is journal-derived on replay; no re-observation or synthesis is authorized. |
| `Y-M1` — crash/collision/invalidity | **Survives in substance.** Claims remain retained, `EEXIST` requires `X-1..X-4`, and invalidity dominates. The new contradiction is in digest counting/classification, not in convergence semantics. |
| `Y-M2` — overstated Option B record change | **Survives.** The final record carries the digest, not the two identity keys; Option B still supersedes two peer schemas, not three. |
| `Y-m1` — overbroad argv rationale | **Survives.** Staleness, lack of PCS attestation, and authority bypass independently exclude the `/proc` route; the argv-evidence deletion remains narrowly stated. |

## 8. Every author-disclosed weak point classified

| Author weak point | Classification | Y-line disposition |
|---|---|---|
| 1. Root-wide `S-25i` lockdown is broader than the identity fields | **Proved nonblocking** | It is explicit, decidable, priced in Option A's blast radius, and does not change authority. |
| 2. `M-R1` pins a peer-layer representation | **Proved nonblocking** | It is an informed implementation-shape cost, not a hidden durable-schema or authority change. |
| 3. `DC-1` declassification-model choice | **Requires revision** | The model may remain, but must cover both `ACC-5` evaluations and must not imply confidentiality declassification or impossibility of identity inference. |
| 4. Low-entropy preimage residual | **Requires revision** | Disclosure alone is insufficient while `DC-3..DC-5` deny the resulting proxy/evidence channel and `WL-4(a)` misstates actual possession of the other fields. |
| 5. Historical `OK/CLAIM` matrix might be live | **Closed** | Authority level 3, non-restatement in v1.2, and omission from both accepted peer contracts prove it non-governing. |
| 6. Newly named `X-3` and second `ACC-5` site | **Mixed: `X-3` closed; `ACC-5` requires revision** | `X-3` is a pre-existing boolean integrity conjunct. `X-4` is also legitimate, but its second digest conflicts with `C-5`, `DC-1`, and `DC-6`. |
| 7. Closure depends on exactly five roots | **Proved nonblocking** | The operative composite pins exactly five roots and requires re-derivation if that set changes. |

## 9. Smallest sufficient revision

1. Reconcile the hash cardinality. State explicitly that `ACC-5` has two evaluations: one validated lineage evaluation whose raw result reaches only `D-1` and `D-2`, and one validated occupant evaluation consumed only by the `X-4` boolean. Amend `C-5`, `DC-1`, `DC-6`, `S-25e`, `S-25l`, and the counts consistently. Alternatively remove `X-4` only through an explicit revision of the already-closed collision rule; it cannot simply be narrated away.
2. Narrow `DC-3..DC-5` and `WL-4` from an absolute cryptographic assertion to an authorization assertion. Explicitly acknowledge that the digest is a searchable full-claim commitment, may supply conditional identity equality evidence, and is not a confidentiality boundary.
3. Preserve the ban on using the digest or recovered identity for handles, opcode requests, signalling, waiting, capacity, custody, spend, settlement, selection, qualification, Q/C, scientific datum/evidence/outcome, or Proof.
4. Preserve exactly two **direct raw lineage-digest destinations**, while enumerating the permitted transitive integrity lineage: the `T_PROCESS_STARTED` entry hash/lease seed, final-record hash/stop event, archive copies and archive composites, and recovery verification.

These are bounded consistency and claim-scope repairs. They do not reopen Option A's architecture, the indirect-read repair, or the eight prior closures.

## 10. Authorization boundary

This revision verdict authorizes nothing: not Kirill's A/B selection, not `P1_IDENTITY_OBSERVATION_BOUNDED_WEAKENING_V1`, not implementation, not activation, not a verifier or manifest edit, and no process-control, spend, datum, outcome, Proof, or claim movement.

```text
T = NOT_ACTIVATED
PROGRAMME CLAIM = OPEN
WATCHDOG-FREEZE CHOICE = UNRESOLVED AND ORTHOGONAL
```
