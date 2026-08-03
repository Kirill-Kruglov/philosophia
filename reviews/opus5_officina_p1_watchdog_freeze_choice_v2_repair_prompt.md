# Task: bounded v2 repair of the P1 watchdog-freeze author-choice packet

You are Claude Code Opus 5 acting as the specification author, not an independent reviewer. Work in the local `philosophia` repository. Do not implement code, execute process-control behavior, activate T, or alter scientific/programme state.

## Governing inputs

Read the committed bytes of:

- `successor/OFFICINA_P1_WATCHDOG_FREEZE_AUTHOR_CHOICE_PACKET_V1_DRAFT.md`
- `reviews/opus5_officina_p1_watchdog_freeze_author_choice_packet.md`
- `reviews/opus_officina_p1_watchdog_freeze_choice_review.md`
- `reviews/sol_officina_p1_watchdog_freeze_choice_review.md`
- all governing P1/C1/authority/activation/generic-harness contracts cited by those reviews

Treat both reviews as binding defect reports. Where X and Y differ, adopt the stricter constructible rule. Preserve v1 and both reviews untouched.

## Deliverables

Create exactly:

1. `successor/OFFICINA_P1_WATCHDOG_FREEZE_AUTHOR_CHOICE_PACKET_V2_DRAFT.md`
2. `reviews/opus5_officina_p1_watchdog_freeze_choice_v2_closure.md`

The packet must be a self-contained replacement. The closure must disposition every X/Y finding one-to-one. Do not select W-A or W-B and do not accept any amendment token.

## Mandatory repairs

### 1. Constructible, total PCS freeze scope

Close Y-C1:

- Remove every unsupported claim that the PCS knows a peer lease table or a published `table_seq`.
- Define the common scope solely from P1-owned state: unique ascending kernel-verified pgids belonging to current-generation `CONTROLLER`/`WORKER` handles that are unreaped and `OWNED`. Specify exact inclusion/exclusion for every signed handle state, nullable `pgid_or_null`, duplicate groups, stale generation, lost ownership, and reaped children.
- Pin the kernel verification used before each group action and deduplicate before signalling.
- Give every identity, signal, `/proc`, enumeration, quiescence, timeout, denial, structural error, and partial-freeze result exactly one closed result token and one durable continuation.
- Any unestablished or partial result must be record-first whole-generation `PROCESS` invalidity and full charge, never completion, resource success, witness evidence, qualification, Q/C, or science.

### 2. W-A must be truly one-shot and fully priced

Close Y-C2/Y-M3 and retain the mechanical findings:

- Remove `request_seq` and `table_seq`. Use one constant no-target request identity per `(generation_id, watchdog_handle)` and exactly one accepted action. Every duplicate/replay/refusal performs no syscall.
- Specify whether invocation is permitted before peer-control-endpoint loss. If not, give a mechanically verifiable PCS-side gate. If it is permitted, price explicitly that the single action can force dominant process invalidity and full resource charge while the supervisor is live.
- Order the W-A dispatch path against control-endpoint loss and the existing non-returning PCS reaper transition. Give deterministic routes for watchdog death, socket EOF, timeout, stale generation, PCS restart, and simultaneous endpoint loss.
- Pin slot 6 as the exact socket type and reconcile the persistent non-handle PCS descriptor with descriptor accounting.
- Preserve one opcode, no pid/pgid/handle/role/target field, no arbitrary widening, and no update-pipe write end retained by PCS.

### 3. W-B trigger means endpoint loss, not death

Close X F2 / Y-M1:

- Replace `SUPERVISOR_LOST` death claims with `PEER_CONTROL_ENDPOINT_LOST` or an equally exact endpoint-unavailability term.
- Distinguish true stream EOF/half-close from an empty `SOCK_SEQPACKET` data record using `MSG_EOR`; the empty record is malformed, not EOF.
- State explicitly that orderly close, half-close, peer crash, and supervisor exit are indistinguishable at this interface and prove only endpoint unavailability.
- Endpoint loss remains a sufficient fail-closed trigger because no further authorized peer request can arrive; it must not become evidence that the supervisor died.
- Rewrite the race/death/publication language accordingly.

### 4. Record before autonomous action

Close Y-M2:

- Under W-B, validate the endpoint-loss event, append/fsync a constant once-per-generation `ACCEPTED` journal entry, then execute the total closed group classifier, then append/fsync `COMPLETED` only on its exact valid terminal.
- A restart or live failure that sees `ACCEPTED` performs no second freeze and routes to inconclusive dominant process invalidity.
- Specify all crash cuts, stale-head/state checks, replay behavior, and partial side-effect handling.

### 5. Repair the `ABSENT` fallback constructively

Close X F3 / Y-C3 using the stricter Y repair:

- Do not merely call the issue pre-existing. Add a bounded peer-schema/predicate amendment for the `EVIDENCE_ABSENT` branch: `pgid` and `start_identity` are null exactly when `rejection_conjunct == 0`; current quiescence is `UNKNOWN`; no instant, overrun, numeric identity, or freeze success is synthesized.
- Retain record-first dominant `PROCESS` invalidity, the unknowable pool, and full charge.
- Enumerate the exact signed schema/predicate sentences reopened and provide a dedicated common amendment token required under either W-A or W-B.
- State accurately that the freeze executor choice is separate from the identity choice, while this repaired fallback is what makes settlement constructible under either identity outcome.
- `ABSENT` and any PCS journal state are never peer freeze evidence and never enter qualification, comparison, Q/C, or Proof.

### 6. Enumerate every freezer/witness sentence

Close X F1:

- Audit the complete composite and list every sentence/invariant/table row assigning the watchdog freezer or witness-of-record role, including at least the sites identified by X: intro lines 202-203, §P1-9.2, §P1-9.4, §P1-11.4, §P1-11.7, §P1-13.1, and invariants 61/63.
- Provide exact replacements for both W-A and W-B. Do not say W-B changes “zero P1 sentences”; distinguish topology/opcode changes from normative P1 prose changes.
- Replace contradictory rows rather than merely adding new ones.

### 7. Publication and scientific boundary

Close Y-m1 and related overclaims:

- Mandatory wording must say endpoint loss is not proof of supervisor death; actual freeze occurrence may remain unknown; a PCS journal fact is not a peer witness; `ABSENT` means evidence unavailable even if some groups stopped.
- No qualification, comparison, Q/C, or Proof may distinguish a `COMPLETED` PCS freeze journal from another `ABSENT` case.
- Recommendation must rest only on signed-authority fidelity, constructibility, mechanical testability, liveness, and blast radius, never predicted outcomes.

## Preserve

- The blocker remains proved.
- PCS never retains the watchdog update-pipe write end.
- PCS remains the sole caller of signal/process-control primitives.
- W-B may remain recommended if the corrected comparison still supports it, but no option is selected.
- The identity choice is not selected or repaired here.
- `T = NOT_ACTIVATED`; programme claim `OPEN`.

## Closure requirements

Include:

- verdict `READY_FOR_OFFICINA_P1_WATCHDOG_FREEZE_CHOICE_V2_XY_CONFIRMATION` only if every finding is closed;
- hashes of new artifacts and reviewed inputs;
- one-to-one dispositions for X F1-F3 and Y-C1..Y-C3/Y-M1..Y-M3/Y-m1;
- corrected A/B comparison and exact tokens, including the common `ABSENT` schema amendment token;
- deterministic failure/crash matrix;
- one bounded yes/no confirmation question per reviewer;
- explicit negative authorization.

Do not modify existing files. Report created paths, verdict, recommendation after repair, and residual author choices.
