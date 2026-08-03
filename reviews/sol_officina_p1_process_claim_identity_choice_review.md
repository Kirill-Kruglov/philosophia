REVISE_OFFICINA_P1_PROCESS_CLAIM_IDENTITY_CHOICE_PACKET

# Independent Y-line review — P1 process-claim identity choice

## Findings

### Critical

**Y-C1 — Option A's claimed sole-sink/dataflow closure is not closed across the
signed durable schemas.** Packet §2.4 (lines 247–255) says the two claim fields
are the only consumers, forbids echoing either value into another record, and
forbids retention past the claim write. The signed activation protocol says
instead that `t-active-lease.v1` contains **all claim keys plus five**
(`OFFICINA_T_ACTIVATION_PROTOCOL_V2_CORRECTION.md:231-246`). A valid lease must
therefore carry `controller_pid` and `process_group_id`. The already-signed
freeze predicate also later reads `process_group_id` from the durable claim
(`...V2_1_1_CORRECTION.md:1044-1048`). The literal "no second sink" rule cannot
coexist with those required continuations.

The verifier proposal does not repair that contradiction. `S-25a`–`S-25d`
taint only the two names at the wire parse site and declassify them at the claim
constructor. A conforming-looking implementation can serialize the tuple into
the claim, reopen the claim or lease, bind `claim["controller_pid"]` or
`lease["process_group_id"]` to a fresh name, and then feed that fresh name to a
request builder, handle selection, process control, capacity/custody logic,
selection, Q, C, or a purported scientific fact. None of `S-25a`–`S-25d` as
written follows that persistent alias. `A-R6` declares those uses forbidden,
but the recommendation's claim that the boundary is *mechanically closed* is
false.

**Consequence:** Option A is not yet a closed validity boundary and cannot be
confirmed for author selection. The revision must distinguish the immediate
wire tuple's authorized write from the signed downstream claim-to-lease copy
and freeze-predicate read, enumerate those legitimate persistent consumers,
taint every read of the two keys (including lease copies and aliases), and make
every other use a deterministic process-invalidity route. A write-and-reload
must not launder observation into addressing, capacity, custody, selection,
Q/C, or science.

**Y-C2 — The replay promise is not constructible from the literal J4 record,
so the J4→J5 crash counterexample breaks B1.** Packet §2.7 says the tuple is in
the J4 `COMPLETED` record "exactly as start_identity already is" and packet
§5.1 says the journal surface is untouched. The operative composite's literal
J4 append is only `{ ..., state: COMPLETED, outcome, handle_id,
fd_vector_len }`; its replay rows name recorded status, detail, and handle
(`...P1_OPERATIVE_COMPOSITE_V1_2.md:1276-1304`). It does not state that
`start_identity`, `pgid_is_leader`, the new tuple, or the complete response
bytes are durable. The packet's v1.3 handoff likewise orders only a replay
prohibition, not a J4 record amendment.

After a crash after J4 and before J5, the PCS must not re-observe the process,
but the specified journal does not contain enough literal data to reproduce
the tuple. Returning absent fields loses the authorized stopped claim; fresh
observation violates §2.7 and can hit a reaped/reused pid; inventing bytes
violates B1. These are the only continuations under the current text.

**Consequence:** the claim that Option A preserves signed B1 exactly is not
earned. The revision must make the complete replayable response representation
and its J4 durability explicit, update the journal surface/blast-radius table
and v1.3 handoff, and require byte-identical replay without re-observation.

### Major

**Y-M1 — The crash/collision table contradicts durable claim existence and
does not preserve invalidity dominance.** Packet §2.9 first recognizes a crash
after the claim write, then says "PCS death at any point" means no claim is
written. PCS death after a durable claim write is a direct counterexample: the
claim exists and cannot be made nonexistent by prose. The operative rule is
whole-generation process invalidity with invalidity dominant over completion,
capacity, custody, spend, qualification, comparison, and science
(`...P1_OPERATIVE_COMPOSITE_V1_2.md:1849-1866,2323-2329`).

The same table calls a second no-replace install an unconditional `EEXIST`
no-op. No-replace establishes only that some object occupies the path, not that
its canonical bytes equal the recorded reply and expected claim. Treating a
conflicting or malformed occupant as convergence creates post-outcome
discretion and can accept a false claim.

**Consequence:** the revision must route PCS death after claim durability to a
retained claim plus the signed invalid-process settlement, never to claim
absence. `EEXIST` may converge only after deterministic byte/schema/hash
identity verification; every mismatch must be record-first invalidity with no
completion or resource/scientific interpretation. Malformed, partial, and
cross-field-inconsistent identity replies must be bound explicitly to the same
dominant invalidity route.

**Y-M2 — Option B's schema blast radius is materially overstated.** Packet
§3.2 says `t-process-record.v1` "inherits the same key change"; §§5.1, 5.4,
5.5, and 7 then count three record schemas/four schemas and every record reader
against B. The signed activation schema disproves this. The final process
record has its own exact key set and contains neither `controller_pid` nor
`process_group_id`; it contains `process_claim_sha256`
(`OFFICINA_T_ACTIVATION_PROTOCOL_V2_CORRECTION.md:248-257`). It does not
mechanically become `.v2` merely because the claim and active lease change.

**Consequence:** the comparative table and the governance/blast-radius basis
for recommending A are quantitatively biased. The recommendation remains
outcome-independent, but it is not valid on the packet's stated facts. The
reader-by-reader audit must be recomputed from the exact schemas; any final
record or archive change must be justified through the claim-hash dependency,
not asserted as a key inheritance that does not exist.

### Minor

**Y-m1 — The stale `/proc` route is unauthorized, but one of the packet's two
stated reasons is broader than its source.** §Z3.4 really does select nothing
against P1: it expects the marker at indices 3/6/7, while P1 fixes `-E` and
`--officina-role` at 3/6 and the spawn marker at 12/13. Re-indexing it would
still not create a legitimate alternative: it would give the supervisor a pid
through an unattested self-scan and revive direct `killpg` selection outside
P1's handle-only, PCS-mediated authority.

But v2.1.10 line 188 deletes argv as evidence specifically of a clean image, a
fresh `execve`, or the executor set. It does not literally delete every use of
argv as identity evidence. Packet §§1.5 and 4 should not quote that narrower
rule as an across-the-board argv-evidence prohibition.

**Consequence:** correct the rationale, while retaining the route's status as
a separate stale peer-contract defect rather than a hidden Option C.

## Required Y-line determinations

1. **A3 authority:** observing a PCS-attested PID/PGID does not confer any
   *authorized* process-control power. A3 already admits same-UID kernel power;
   P1 authority is conferred only by handles, the closed request grammar, and
   PCS execution of control primitives. The tuple adds trustworthy provenance
   and therefore a more useful association, but it is neither a handle nor a
   request capability. Option A is a real lexical-to-dataflow weakening, not a
   transfer of authorized process control.

2. **Legitimate sinks:** the immediate wire tuple may be admitted only into
   `controller_pid` and `process_group_id` of the process claim. That statement
   is insufficient as the packet writes it, because the signed lease repeats
   those keys and conjunct 7 reads the claim. Those existing downstream uses
   must be explicitly authorized and guarded; all other direct or reloaded
   uses must fail into process invalidity, never become capacity, custody,
   spend, selection, Q/C, or scientific facts.

3. **Option A preservation:** the response grammar, ordered PCS attestation,
   stopped/unreaped ownership proof, PID-reuse binding, absent tuple on
   inconclusive branches, and prohibition on replay re-observation are sound in
   principle. As written, however, the durable-sink, J4 replay, `EEXIST`, and
   post-claim PCS-death defects mean A does not yet preserve activation/lease
   semantics, B1 replay, or invalidity dominance without discretion. The claim
   schema and freeze conjunct can remain byte-unchanged only after those gaps
   are closed.

4. **Disclosure:** §2.10 is loud enough in form for informed signature: it
   quotes the old and proposed meanings, calls the change a strict weakening,
   supplies a dedicated token, and states the regression risk. That adequate
   disclosure does not cure the substantive defects above.

5. **Option B:** B is honestly non-selectable under the current chain. A
   PCS-written peer-visible binding adds a durable P1 artifact class, while a
   peer predicate opening that P1 artifact falls outside `R-L4`'s nine-opcode-
   only interface. The accepted chain supplies no silent affirmative answer to
   either question. A later author packet may bind both decisions together,
   but the present chain cannot close them without new author authority.

6. **Stale discovery:** `/proc/*/cmdline` is another defect, not an authorized
   alternative. Its current indices are dead under P1; repairing the indices
   would not authorize the resulting pid-to-`killpg` route.

7. **Recommendation basis:** no expected result, qualification outcome, arm,
   comparison, Q/C fact, capacity observation, or scientific datum appears in
   the recommendation. Its stated basis is governance and blast radius only.
   Y-M2 makes that blast-radius comparison factually unreliable, and Y-C1/Y-C2
   disprove the claim that A's residual is mechanically closed.

## Separate blocker, not merged into this choice

The watchdog-freeze defect is confirmed and remains orthogonal. P1 §P1-9.2
requires the watchdog to freeze known groups on update-pipe EOF while its only
channels are sealed pipes at slots 3 and 4; it has no PCS socket, P1 grants it
no numeric process authority, and the supervisor is dead on the route where the
watchdog must act. Neither A nor B supplies that missing authority or channel.
This review neither solves it nor treats it as part of the process-claim
identity selection.

## Byte custody and authorization boundary

Recomputed SHA-256 values:

```text
ad8b5791f043f201c00812a11de2ab3b765664e65e6d0ebf9778e150913096d3  successor/OFFICINA_P1_PROCESS_CLAIM_IDENTITY_AUTHOR_CHOICE_PACKET_V1_DRAFT.md
e8bceb8098c9a1d96fcd76f0796fccdcd49b79ce4cd690d1ef3a7d9ced54e128  reviews/opus5_officina_p1_process_claim_identity_author_choice_packet.md
```

Both match the expected bytes. This `REVISE` verdict confirms no selection and
authorizes no implementation, activation, spend, datum, outcome, process,
claim movement, or watchdog repair. `T` remains `NOT_ACTIVATED`; the programme
claim remains `OPEN`.
