READY_FOR_OFFICINA_P1_PROCESS_CLAIM_IDENTITY_CHOICE_XY_REVIEW

# Author closure — P1 process-claim identity choice packet v1

**Author:** Claude Code Opus 5, **specification author only**. I authored the
whole supervisor/control-channel chain, v1, v1.1, v1.2 and this packet, and am
therefore **disqualified** as its independent X-line or Y-line reviewer. **This
closure is an untrusted author self-assessment**, and so is every prior closure
in this chain, including the v1.2 closure whose diagnosis this round was told to
re-establish rather than trust.

**No choice was made and no token was accepted.** The packet presents the
options; the selection is Kirill's and is not signable until bounded X/Y review
confirms the packet on identical bytes.

`T = NOT_ACTIVATED`; programme claim `OPEN`. This round produced no selection,
X/Y verdict, implementation, code or test edit, verifier or manifest change,
process or behavioural probe, activation, entropy, E1/E2/E3 spend, Q/C work,
datum, outcome, Proof or claim movement.

---

## 1. Deliverables and untouched-file confirmation

Exactly two new files. **No existing file was modified.**

| Path | Lines |
|---|---|
| `successor/OFFICINA_P1_PROCESS_CLAIM_IDENTITY_AUTHOR_CHOICE_PACKET_V1_DRAFT.md` | 664 |
| `reviews/opus5_officina_p1_process_claim_identity_author_choice_packet.md` | this file |

Only read-only commands were run against the repository: `grep`, `sed`, `wc`,
`sort`, `uniq`, `cat` and `sha256sum`. No test, behavioural probe or
process-control operation was executed.

## 2. Hashes and custody

Governing block, hashed this round:

```text
2c857fa8ad7be1c861eb8cf561f396e7d2339403c7714abc7958745bf34e5d5d  successor/…P1_OPERATIVE_COMPOSITE_V1_2.md
cda0ff673c639d5f09ca490a3aeaf866cc2421a00a61c1cf8c90a4a772bd1069  reviews/opus5_…_v1_2_closure.md
6ef98132990f8c686fa9678509bb07ba8259f3d6e4cbc483861edfc03ea8e3ef  successor/OFFICINA_SUPERVISOR_PROCESS_AUTHORITY_SELECTION_V1_SIGNATURE.md
c494ef8884948bd0e737373d2d57a3ab74bbd456db2c3463711c4405f2fdf86a  successor/OFFICINA_SUPERVISOR_AUTHOR_SELECTIONS_V1_SIGNATURE.md
4918a208bb94549ba3e7c38571265e723cc51a0a3394e291a62a85c333d864a6  successor/OFFICINA_SUPERVISOR_OUTPUT_CAPACITY_SELECTION_V1_SIGNATURE.md
cd106d7fef491601f9ff948aba3ba0ceaac0774ac18a6564247c0c5899b4c40c  successor/OFFICINA_T_ACTIVATION_PROTOCOL_V2_CORRECTION.md
724d633a55668013b78058eed1c76e12e9bbaf487f71ea94b7a4568ea1ced8a0  successor/OFFICINA_GENERIC_HARNESS_CONTRACT_V2_3_1_CORRECTION.md
8c47da352ef5954406964647a32e97939c404806bdf9b3d3ff5bc70866e6369a  successor/OFFICINA_GENERIC_HARNESS_SIGNATURE.md
b5a1523290b6b8417a7b3288329cc4a4e5ff80214c8f28e6ea1ae51a450a94c9  successor/OFFICINA_BATCH_SETTLEMENT_CORE_AMENDMENT_V1_1_1_CORRECTION.md
```

The five previously pinned digests match what v1.1 and v1.2 recorded, so the
custody chain is byte-intact across this round.

Produced this round:

```text
ad8b5791f043f201c00812a11de2ab3b765664e65e6d0ebf9778e150913096d3  successor/OFFICINA_P1_PROCESS_CLAIM_IDENTITY_AUTHOR_CHOICE_PACKET_V1_DRAFT.md
```

The packet contains none of its own digests, so custody stays acyclic: packet →
this closure → X/Y review → any future signature.

**Schema evidence used, by source location:** claim keys and path,
`…ACTIVATION_PROTOCOL_V2_CORRECTION.md:83, :233-238`; lease = claim keys plus
five, same file `:240-245`; `AWAIT_STOP` response operands,
`…V2_1_10_2_CORRECTION.md:366`; §Z4.6 conjunct 7,
`…V2_1_1_CORRECTION.md:1047`; §Z3.4 discovery predicate, same file `:758-778`;
argv-as-evidence deletion, `…V2_1_10_CORRECTION.md:188`; the signed sentence,
`…PROCESS_AUTHORITY_SELECTION_V1_SIGNATURE.md:24-26` and its derivation at
`…V2_1_10_4_P1_BINDING.md:156-158`; watchdog slot map and freeze assertion,
v1.2 §P1-6.2 and §P1-9.2, `…V2_1_10_4_P1_BINDING.md:552-566, :627-633`.

---

## 3. The re-derived conflict

The v1.2 diagnosis was treated as untrusted and re-established from the
contracts. **The conflict is confirmed.** One statement in it was too strong and
is corrected below.

**Requirement A.** `t-process-claim.v1` has exactly twenty keys including the
integers `controller_pid` and `process_group_id`. `process_group_id` is
load-bearing: §Z4.6 conjunct 7 dereferences it when accepting freeze evidence.
`t-active-lease.v1` is "the claim keys plus five", so both integers propagate.

**Requirement B.** The signed selection states the supervisor "receives opaque
handles only" and "cannot express a PID"; the binding derives this from
`t-pcs.v1` having no PID field.

**The gap.** I enumerated the response operands of all nine opcodes: `handle_id`
twice, `outcome`/`start_identity`/`pgid_is_leader`, two `result` tokens, the
six-token classifier, two empties, and `pcs_uptime_ticks`. **None is a pid or a
process-group number.** `pgid_is_leader` is a `{0,1}` predicate that decides
whether the group id equals the process id while naming neither.

**Alternative sources tested and excluded:** the four singleton spawn records
name only the PCS, middle and supervisor; `t-fork-child.v1` records a
supervisor-forked watchdog and is itself P1-orphaned; the worker status pipe is
empty at claim time because the role self-stops at `A-12` before writing
anything and the claim precedes its resume; `os.getpgid` needs a pid and is
circular.

### 3.1 Correction to v1.2 — the one thing it stated too strongly

v1.2's closure said the peer layer "cannot obtain" the values. **That is too
strong.** The accepted chain contains §Z3.4, a `/proc/*/cmdline` discovery
predicate for exec'ing children, by which a supervisor could obtain a
controller or worker pid without the PCS.

It is still not a live source, for two independent reasons:

1. **Its fixed indices do not match the selected P1 argv.** §Z3.4 requires
   `cmdline[3] == "--officina-bootstrap"` and `cmdline[6] ==
   "--officina-spawn-intent"`. v1.2 §P1-7.4 fixes index 3 as `-E`, index 6 as
   `--officina-role`, and puts the marker keyword at 12 and the hex at 13.
   **Against any P1 role the predicate matches zero processes.**
2. **Its evidentiary basis was deleted.** v2.1.10 removed argv as evidence
   outright: "No layer of this contract henceforth treats argv as evidence of a
   clean image, of a fresh `execve`, or of the executor set."

The corrected claim, which the packet uses throughout, is therefore: *no
authorized, non-stale source exists*. That §Z3.4 is stale against the P1 argv is
a **separate peer-chain defect**, recorded and not repaired here.

This correction does not change the verdict — it changes the argument, and the
argument is what a reviewer must be able to check.

---

## 4. Option-completeness table

| Requirement from the round | A | B | C |
|---|---|---|---|
| which response carries the tuple, on which outcomes | §2.1 — `AWAIT_STOP` only, `STOPPED` only, with the minimality argument | n/a | n/a |
| exact field order, grammar, bounds | §2.2 — appended at indices 11 and 12; 1–7 digits, no leading zero, ≥ 1; both present or both `-` | n/a | n/a |
| frame-size impact | §2.2 — worst case +16 bytes against a 4096 ceiling | n/a | n/a |
| relation to `handle_id`, `start_identity`, `pgid_is_leader` | §2.2 — handle stays the only addressable name; cross-field invariant `pgid_is_leader == 1 ⟺ pid == pgid` | n/a | n/a |
| PCS proof that both numbers name the handle's process | §2.3 — `A-P1`…`A-P6`, ordered, no partial tuple | n/a | n/a |
| both numbers only on `STOPPED` | §2.1, enforced by `A-T1`/`A-T6` | n/a | n/a |
| sole allowed data sink | §2.4 — the two claim keys, nothing else | n/a | n/a |
| request grammar stays PID-free | §2.5 — `A-R1`…`A-R6` | n/a | n/a |
| static / dataflow / runtime escape tests | §2.6 — `S-25a`…`S-25d`, `A-T1`…`A-T7`, incl. `A-T5` fault injection | n/a | n/a |
| replay / B1 treatment | §2.7 — recorded response replayed, **re-observation prohibited** with the `WAIT_ONE` precondition reason | §5.3 | n/a |
| PID reuse / start-identity binding | §2.8 — no new predicate needed; conjunct 7 already compares both | §3.2 | n/a |
| crash cuts | §2.9 — seven cuts | §5.3 | n/a |
| exact amendment to the signed sentence, named as a weakening, dedicated token | §2.10 — `P1_IDENTITY_OBSERVATION_BOUNDED_WEAKENING_V1` | not required | n/a |
| single coherent replacement, not a family | n/a | §3.1 — `t-process-claim.v2` plus a PCS-written binding artifact, keys given | n/a |
| every reader traced | n/a | §3.2 — eight surfaces, with explicit **no migration** | n/a |
| single-valued, or marked non-selectable | n/a | §3.3 — **non-selectable**, sub-cells `B-1` and `B-2` named | n/a |
| genuinely distinct, closed, chain-supported | n/a | n/a | §4 — **rejected**, four reasons, recorded for auditability only |

**Completeness verdict:** A is mechanically complete and selectable. B is fully
specified and honestly marked non-selectable behind two named sub-cells. C is
examined and rejected rather than offered for symmetry.

---

## 5. The A3 question, answered directly

The round required an explicit answer, distinguishing three things the packet
keeps separate at §5.6.

**Does merely observing a PID grant process authority under this project's
procedural A3 threat model? No.**

1. **OS information.** Under A3 the supervisor is same-UID with every process
   here and may already read every pid from `/proc` unilaterally. The attested
   tuple conveys **zero** OS-level information it could not otherwise obtain.
   What it adds is provenance — a number the PCS vouches for rather than one the
   supervisor scraped.
2. **Authorized addressing.** What P1 removed is the *authorized* ability to
   name a process as an operation target. Option A adds a response field with no
   request counterpart; `A-R1`–`A-R6` close the request side explicitly.
3. **Same-UID adversarial capability.** A contaminated supervisor can already
   call `kill(any_pid)`; the kernel permits it and v1.2 §P1-12.3 states it
   affirmatively. P1's guarantee was never that the supervisor lacks the kernel
   power, but that no Officina route authorizes it and no Officina decision
   consumes its result — safety `S2` and `S3`, both unchanged under A.

**Therefore Option A weakens the English sentence, not the safety property.**
The genuine cost is **testability**: an invariant that is today lexical becomes
a dataflow invariant. That is the thing to weigh, and the packet says so in
those words rather than implying equivalence with the old phrase.

---

## 6. Recommendation

On the three permitted criteria only — preserving signed schemas, minimizing
reopened validity predicates, keeping the authority boundary testable:

> **Option A**, unless the independent audit disproves §5.6.

A leaves `t-process-claim.v1`, `t-active-lease.v1`, `t-process-record.v1` and
§Z4.6 conjunct 7 **byte-untouched** and reopens **zero** validity predicates,
touching one signature sentence and one response grammar. B supersedes three
record schemas, reopens a signed acceptance predicate, inverts `R-L4`, and is
not selectable today. A's single real cost is closable by `S-25a`–`S-25d` plus
the `A-T5` fault injection.

**No outcome is predicted and nothing is optimized toward qualification. The
author selects nothing.**

---

## 7. Exact v1.3 handoff for each selection

### If `I_SELECT_P1_PROCESS_CLAIM_IDENTITY_A_OBSERVATION_ONLY` is signed

Also requires `P1_IDENTITY_OBSERVATION_BOUNDED_WEAKENING_V1`. Then v1.3:

1. amends the signed sentence exactly as §2.10 renders it, and records the
   weakening token in the authority hierarchy — never presenting it as
   equivalent to the old phrase;
2. rewrites the `AWAIT_STOP` row of §P1-8.3 with operands 11 and 12 and the
   grammar of §2.2;
3. adds `A-P1`…`A-P6` as a numbered subsection of §P1-9.1 and the cross-field
   invariant to §P1-8.4;
4. **completes §P1-13.2 row 2**, removing the `BLOCKED` marking and the two
   options, and setting the status line back to
   `CANDIDATE_FOR_INDEPENDENT_X_AND_Y_REVIEW_NOT_ACCEPTED`;
5. adds `A-R1`…`A-R6` to §P1-12 as a closed rule set;
6. adds `S-25a`…`S-25d` to §P1-14.6 CHANGE 3 and updates the edit surface from
   `S-1…S-24b` to `S-1…S-25d`;
7. adds `A-T1`…`A-T7` as test rows 92–98;
8. adds the §2.7 replay prohibition to §P1-8.6 and the §2.9 cuts to §P1-11.7;
9. recomputes `H_FILE`, `H_BODY`, `H_GUARDDATA`, `H_NORMATIVE`, sentinel counts,
   the placeholder audit and guard fires; required placeholder and guard-fire
   counts remain **zero**.

### If `I_SELECT_P1_PROCESS_CLAIM_IDENTITY_B_OPAQUE_BINDING` is directed

**No v1.3 may be authored yet.** Sub-cells `B-1` (does the PCS gain a
peer-visible durable-write role?) and `B-2` (may a peer validity predicate read a
P1-owned artifact, inverting `R-L4`?) must be signed first, in their own packet.
Only then can v1.3 bind `t-process-claim.v2`, the binding artifact, the rewritten
conjunct 7, and the lease and record successors.

### If neither is signed

v1.2 stands as-is: blocked, not operative, with row 2 unfilled. No
implementation may begin, because no conforming implementation can write a valid
process claim.

---

## 8. Bounded questions

### Three for the X line

1. **Is the enumeration at §1.3 exhaustive and correct?** Recompute it from the
   signed opcode table. Does any response operand of any of the nine opcodes
   carry a pid or pgid that I missed?
2. **Do `A-P1`…`A-P6` actually prove what §2.3 claims** — that both integers name
   the same stopped, unreaped, direct-child process the handle denoted at that
   operation? In particular, is `A-P4`'s `getpgid` read at an instant where the
   value cannot have changed, given `setsid=True` at spawn?
3. **Are `S-25a`…`S-25d` decidable on the actual supervisor root?** `S-25d` is a
   taint analysis; is its sink set closed, and can a conforming implementation
   defeat it through a container, a format string, or an integer arithmetic
   round-trip?

### Three for the Y line

1. **Is §5.6's A3 analysis sound**, or does receiving a PCS-attested pid confer
   something the supervisor did not have — in particular, does *provenance*
   (a vouched-for number rather than a scraped one) constitute authority under
   the procedural threat model, even though the raw number does not?
2. **Is the §2.10 weakening correctly scoped?** Does the proposed sentence retain
   the safety property at its earned strength, and is naming it a bounded
   weakening with its own token sufficient governance, or does it require a fresh
   process-authority selection rather than an amendment?
3. **Is B correctly marked non-selectable?** Are `B-1` and `B-2` genuinely
   separate author cells, or could either be resolved inside the already signed
   chain — which would make B selectable and change the recommendation?

---

## 9. Weakest points in this packet

1. **§1.5 is a correction to my own prior round.** If a reviewer finds a third
   route to the two integers, the packet's premise weakens the same way v1.2's
   did.
2. **§2.3's proof is mine, not any signed document's.** `A-P4`'s reliance on
   `setsid=True` making `pgid == pid` is the load-bearing step.
3. **`S-25d` is the only genuinely new verification technique** in this chain and
   has had the least scrutiny.
4. **§6 flags a defect I did not fully investigate:** the watchdog cannot execute
   a freeze under P1. I established the slot map and the absence of a PCS socket;
   I did not exhaust whether some other accepted route supplies a mechanism. It
   is orthogonal to this choice but it is not small.
5. **B's blast radius is estimated from the schema definitions**, not from a
   reader-by-reader audit of the settlement and archive code.

---

## 10. Confirmation and verdict

**No choice was made. No token was accepted. No token is signable.** The two
selection tokens and the weakening token exist only as text in a draft packet
awaiting bounded independent review. No existing file was modified. `T` remains
`NOT_ACTIVATED`; the programme claim remains `OPEN`. This round authorized no
selection, X/Y verdict, implementation, activation, entropy, resource spend,
T/Q/C datum, outcome, Proof or claim movement.

```text
READY_FOR_OFFICINA_P1_PROCESS_CLAIM_IDENTITY_CHOICE_XY_REVIEW
```

Meaning precisely: the conflict is independently re-derived and one overstatement
in the prior round is corrected; Option A is mechanically complete to the level
the round required; Option B is fully specified and honestly non-selectable with
its blocking sub-cells named; a third route was examined and rejected on stated
grounds; the comparative audit, the A3 answer and the recommendation are present.
It does **not** mean the packet is correct, and it clears nothing. The X and Y
lines should recompute the hashes of §2, treat every sentence here as untrusted,
and begin with §9.
