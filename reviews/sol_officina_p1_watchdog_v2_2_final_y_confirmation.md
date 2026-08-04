REVISE_OFFICINA_P1_WATCHDOG_V2_2

# Final Y-line confirmation — Officina P1 watchdog v2.2

**Reviewer:** GPT-5.6 Sol, independent Y-line scientific-validity and governance reviewer.

**Scope.** This is a bounded final confirmation of the v2.2 authority partition, not a new mechanism-design round. I read the v1, v2, v2.1 and v2.2 watchdog packets and closures, all prior Opus/Sol watchdog reviews, the supervisor/P1 selection and composite chain cited by them, and the governing generic-harness and batch-settlement peer chains. Existing files were not modified. No code, verifier, process-control operation, activation, spend, datum, outcome or claim movement was authorized.

## Custody

The required digest recomputes exactly:

```text
651dba04592b16ee2899cfd3e3368ecbf0dd462b371b87644968acf5737c77f4  successor/OFFICINA_P1_WATCHDOG_FREEZE_AUTHOR_CHOICE_PACKET_V2_2_CORRECTION.md
```

The v2 and v2.1 packet digests, both v2 confirmations, both v2.1 final confirmations, both closures, the operative composite, the accepted generic-harness chain, the batch-settlement chain, the supervisor selection/signature files, and every peer/control file listed in v2.2 §1.8 also recompute to the values pinned in the chain. Custody is intact. The defect below is substantive, not a byte-identity problem.

## Determination

The answer to the bounded question is **no**. The proposed local replacement text removes watchdog writing in many places, but v2.2 does not establish one coherent authority partition or one total writer/execution route. Historical watchdog semantics can still affect the handoff because the tier rule treats document-level provenance as locus-level operative text, and the new deadline replacement conflicts with the retained composite writer route.

### 1. `AUTH-1` through `AUTH-5` do not reproduce the composite's document-level authority rule

The composite's hierarchy is categorical at `…P1_OPERATIVE_COMPOSITE_V1_2.md:42-49`: **every earlier supervisor/control-channel document**, including corrections v2.1 through v2.1.10.7 and the binding, is immutable historical/provenance evidence only; no implementer, verifier or reviewer opens any of it for behaviour or verification. Its provenance region repeats the same rule at `:2828-2840`. The separately accepted peer contracts are then named exactly at §P1-13.0/§P1-13.1 (`:1980-2050`): the accepted generic-harness chain ending in `OFFICINA_GENERIC_HARNESS_CONTRACT_V2_3_1_CORRECTION.md`, and the batch-settlement amendment. Section §P1-13.2 additionally says no row delegates a value to another document.

V2.2 `AUTH-3` nevertheless classifies selected sections inside the historical supervisor/control documents — §W, §Z, §N, §U, and `…V2_1_10_4_P1_BINDING.md` — as tier-1 operative text, while `AUTH-4` classifies other loci in the same files as immutable tier-2 evidence. That file-internal split has no source in the composite. The composite's immutability attaches to documents, not to selected paragraphs. References among documents that the composite has already made historical cannot reactivate one another.

The handoff makes the contradiction operational: v2.2 §7 item 6c directs edits to five historical supervisor/control correction files and the historical binding, then item 10 directs the composite's provenance digests to be changed to match them. This destroys the immutable evidentiary bytes that `AUTH-4` claims to preserve. Consequently, the classification rule admits both outcomes it was meant to prevent: a reader following the composite ignores PW/PZ/PN/PU/PB entirely, while a reader following v2.2 reopens and edits them.

This is a governance defect in the authority partition itself. It is not cured by exhaustive enumeration inside the disputed classification.

### 2. The arithmetic reproduces, but the memberships and six-file handoff do not pass

The packet's arithmetic is internally reproducible:

```text
peer reassignment:  1 PH + 14 PW + 7 PZ + 5 PN + 3 PU + 10 PB = 40
peer reopened:      40 reassignment + 5 disjoint K loci             = 45
governing replaced: 22 composite + 40 peer                          = 62
enumerated tier 2:  T2-1 through T2-18                              = 18
```

The cited ranges are distinct, `K1` through `K5` are disjoint from `PN1` through `PN5`, and the six named peer files are reproducible. But a count is acceptable only if its membership rule is valid. Under the composite's document-level rule, PW/PZ/PN/PU/PB are not governing loci at all; under v2.2's rule, editing them contradicts immutability. Therefore 40, 45, 62 and 18 are list cardinalities, not confirmed authority cardinalities.

The handoff is also not globally atomic. Item 6c requires `PW1` through `PW9` in one step, `PZ3`/`PZ4` with `PN2`/`PN3`, and three table rows to agree, but nowhere requires the complete composite-plus-six-file replacement and provenance update to land all-or-none as one reviewed version. The closure itself concedes that a partial application is worse than no application. Subset ordering constraints are not a seven-governing-file atomicity rule.

### 3. V2.2 creates an unaccounted ordinary-deadline writer route

V2.1's retained composite replacements are single-valued: `R2`, `R9` and `R10` permit the row-4 `t-freeze-observation.v1` writer only in the supervisor's **dead-watchdog route**. V2.2 preserves those replacements except `R8` and `R16`, and its own `PA-1`, `PW11`, `PZ5` and `PN5` repeat “on the dead-watchdog route.”

But v2.2 `PH1` replaces the accepted harness §5a so that the supervisor executes the deadline sequence “at or before the deadline” and writes the freeze observation itself. `PW2` likewise starts amended §W3.3 whenever the **supervisor's clock** reaches a lease deadline. That is the ordinary live-watchdog deadline route, not merely ack-absence/dead-watchdog recovery.

The result is a hidden second supervisor writer route:

- the accepted peer replacement requires a supervisor write at an ordinary lease deadline;
- the retained composite and v2.2's writer tables authorize that class only after watchdog death;
- `PA-5` still claims exactly two freeze-execution sites without classifying this ordinary-deadline entry; and
- the handoff does not replace composite `R2`, `R9`, `R10`, `R17` or `R21` to admit and bound it.

This is both procedural and scientific: it leaves unclear whether the ordinary-deadline object is admissible evidence, which route may invoke `SIGNAL_GROUP`, and which execution-site invariant governs it. It also defeats the claim that no hidden writer survives.

### 4. `killer == WATCHDOG` is locally rejected, but global closure is not established

Within the proposed replacement text, `PZ3` is correct and strong: conjunct 8 requires `killer == SUPERVISOR`; `killer == WATCHDOG` has no admissible writer, is permanently non-evidence, and routes to §N5 with `rejection_conjunct = 8`. The retained enum is schema/provenance only. I found no recovery, migration, compatibility, archival or defaulting clause that converts `WATCHDOG` into admissible new-contract evidence. The fallback remains separately supervisor-written with fixed `killer = SUPERVISOR`.

That local result cannot establish the global claim while §1's authority split is invalid. A composite-governed reader never opens amended `PZ3`; a v2.2-governed reader does. The exact predicate must be placed once in an indisputably governing peer contract/new composite version, not in a file whose operative status is itself disputed.

### 5. The four identity reads and the PCS journal pass the scientific-boundary check

`RD-1` through `RD-4` are accurately enumerated and can remain read-only. They install no artifact, own no decision, perform no signal or freeze, and enter no evidence predicate. Amended `R8` states their negative authority surface explicitly. Their only function is generation/identity verification; they do not classify scientific outcomes or create a peer witness.

The PCS journal boundary also remains sound. `L8`, `ND-1` through `ND-3`, v2.1 `R21`, and tests 98/110 keep the classifier terminal, per-group tokens and `freeze_ns` operational/audit facts only. They are neither an endpoint nor a covariate and cannot repair missing peer evidence. Nothing in v2.2 regresses that boundary.

### 6. `R16`, namespace and witness filename pass

The `R16` variants are accurate: W-A has three sealed endpoints at slots 3, 4 and 6; W-B has two sealed pipes at slots 3 and 4 with slot 6 closed. The W-A PCS end is the disclosed additional `FD_CLOEXEC` socketpair endpoint, not the watchdog update-pipe write end, and later role descendants do not inherit it. No hidden update-pipe writer is introduced by either option.

The filename history is also correctly closed by §Z4.5 in favor of `WATCHDOG/FREEZE/<witness_id>.json`, with `process_id` retained only as a preimage member and record field. Keeping the archival-excluded `WATCHDOG/**` namespace does not assign authority or create a second channel. Neither naming decision changes the signed scientific claim.

### 7. Recommendation independence and negative space remain intact

The three-endpoint/two-pipe comparison, topology/opcode cost and liveness comparison are outcome-independent. No learner, arm, qualification, Q/C fact, result or scientific outcome enters the recommendation. The defects above are common authority/writer-route defects and do not justify reopening W-A versus W-B for style.

No candidate, entropy, world, trajectory, data, scientific lock, escrow, outcome, Proof or claim movement is authorized. `T` remains `NOT_ACTIVATED`; the programme claim remains `OPEN`; both the process-identity cell and watchdog-freeze cell remain unselected.

## Minimal bounded repair

1. Replace `AUTH-1` through `AUTH-5` with a document-level rule that agrees with the composite. Keep every historical supervisor/control file byte-immutable. Put any required peer semantics in the accepted generic-harness chain, and put P1 interface/execution invariants in one new reviewed composite version. Do not reactivate historical §W/§Z/§N/§U/PB paragraphs by cross-reference.
2. Recompute all authority counts from that rule. Preserve the useful occurrence inventory as provenance, but do not count historical loci as governing replacements. State one all-or-none handoff covering the new composite, the governing peer amendment, every manifest/provenance digest, and all tests; no partial landing is conforming.
3. Reconcile the ordinary-deadline route. If `PH1`/`PW2`'s supervisor deadline execution is retained, amend the governing row-4 writer/executing-process/function/invariant texts so they explicitly authorize both the ordinary-deadline and dead-watchdog supervisor entries, both through the existing `SIGNAL_GROUP` mediation, while retaining exactly one supervisor writer and `killer = SUPERVISOR`. Update the execution-route count and tests. If it is not retained, remove it everywhere. Do not leave `PH1`/`PW2` opposed to `R2`/`R9`/`R10`/`PA-1`.
4. Place the `killer == WATCHDOG` rejection in the resulting indisputably governing predicate and re-run the bounded occurrence/default/recovery audit on those bytes.

No new option, token or author cell is required. These are bounded authority, enumeration, atomicity and route-consistency repairs. Kirill's watchdog author-choice token is **not authorized** on the present bytes. No implementation or activation authority follows.

```text
T = NOT_ACTIVATED
PROGRAMME CLAIM = OPEN
PROCESS-IDENTITY CELL = NOT SELECTED
WATCHDOG-FREEZE CELL = NOT SELECTED
```
