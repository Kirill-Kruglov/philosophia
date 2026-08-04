REVISE_OFFICINA_P1_WATCHDOG_V2_3

# Final Y-line confirmation — Officina P1 watchdog v2.3

**Reviewer:** GPT-5.6 Sol, independent scientific/governance Y line.

**Scope.** Bounded final confirmation of the new two-file watchdog authority
surface. I read both v2.2 final reviews, the accepted peer chain, the v2.3
packet and closure, the peer amendment, and composite v1.3. No existing file
was modified and nothing was committed.

## Custody

The four reviewed SHA-256 values recompute exactly:

```text
4244e331dc7530dad743c640ae16ada048aed7cd2ec58822bf2d0dde77c8ffcc
  successor/OFFICINA_P1_WATCHDOG_FREEZE_AUTHOR_CHOICE_PACKET_V2_3_CORRECTION.md
380b87f0524ac06ef2fb0173c83b234c3eedc34344c3c61ed9415bd2c1a63858
  successor/OFFICINA_GENERIC_HARNESS_WATCHDOG_FREEZE_AUTHORITY_AMENDMENT_V1_DRAFT.md
b510a7b504ddc370529a7d968d362ccff332538d6bb493b387a2bc0ae4e9db54
  successor/OFFICINA_GENERIC_HARNESS_SUPERVISOR_CONTROL_CHANNEL_P1_OPERATIVE_COMPOSITE_V1_3.md
9a5e400c4762d937072bb008b7ada9e1c3e4d7705a25ff92aa5fcfedcf76a347
  reviews/opus5_officina_p1_watchdog_freeze_choice_v2_3_closure.md
```

All 41 digests listed in composite §P1-18, including the accepted
generic-harness chain, batch-settlement chain, signatures and historical
supervisor/control chain, also recompute exactly. Composite extraction is
total: each of the six sentinels occurs once and in order.

```text
H_BODY       e759f1f2f23b37ba378f2b833aa9a1c7ab86aae745ffcc48b1a8dcd17a898836
H_GUARDDATA  0d3131b4a319d0bf03310e203485320253b671501ec44f87d67e8d47f8616733
H_NORMATIVE  6524bc0cb273be99805a52a9128bbb2732d229ced177093cb7d0f23eed4e264f
H_FILE       b510a7b504ddc370529a7d968d362ccff332538d6bb493b387a2bc0ae4e9db54
```

Custody is intact. The revision finding is semantic and procedural.

## Determination

### 1. Watchdog semantics and `killer` re-entry pass

The occurrence and route audit finds no admissible `killer == WATCHDOG` path.
The accepted peer-chain files contain no `killer` field occurrence. In the two
governing files, `WATCHDOG` occurs in that field only as the retained schema
enum, provenance/legacy description, or an explicit rejection target. Peer
amendment §A5 conjunct 8 accepts only `killer == SUPERVISOR`; `KW-1` applies
before settlement on every path; the fallback has the fixed literal
`SUPERVISOR`; and composite tests 93 and 94 cover occurrence, default,
migration, compatibility, recovery, archival re-import, takeover
re-derivation and fixtures. No grandfathering, coercion or reconstruction
route survives.

Every admissible observation is supervisor-written and has
`killer = SUPERVISOR`. Retaining the two-value enum makes old or forged objects
rejectable rather than unparseable and grants no authority.

### 2. Historical content does not regain behavioural force

The historical supervisor/control documents are classified at document
granularity as provenance only. The quotations of accepted harness §5a and
historical §W6.5 in amendment §A2 identify the displaced text and are followed
by complete governing replacements in the amendment's own bytes. They neither
incorporate the quotations as rules nor require history to be opened for
behaviour. Composite §P1-10.6, row 4 and §P1-13.9 independently state the same
negative surface, writer and routes. No historical cross-reference restores a
watchdog executor, quiescence prover or evidence writer.

### 3. Membership is total for behaviour, but not for installation

For watchdog behaviour, membership is reproducible by the two named paths and
no paragraph-level test. Historical authority is zero.

Installation is not confined to those two files. Amendment `H-4` says that
the **full** handoff list is in §C4 of the companion author closure. That
closure is expressly an untrusted self-assessment and is not one of the two
governing files. The governing amendment therefore depends on a third file for
normative installation completeness. The asserted two-file membership rule is
not total over the handoff it is meant to govern.

### 4. `ROUTE-D` and `ROUTE-W` pass

Both routes enter one supervisor procedure under the same runtime lock, use
the same `SIGNAL_GROUP` mediation, write the same
`t-freeze-observation.v1` class in the same namespace through the same single
install function, use the same acceptance predicate, and set the same killer
value. They differ only in trigger and post-freeze recovery. The PCS classifier
is a separate signed execution site, not a peer evidence writer, and installs
no record of any peer class. No route-dependent evidence class or scientific
treatment appears.

### 5. `G-11` does not make the installation atomic — blocking

The all-or-none claim fails across partial and stale states:

1. Composite §P1-14.1 says the guard rules read exactly one file and no other
   file ever. `G-11` requires reads of the amendment, every provenance file,
   the accepted peer chain and the batch-settlement amendment. Both rules
   cannot be implemented together.
2. Composite §P1-18 pins the present
   `src/philosophia/officina/verification.py` digest as provenance, and `G-11`
   requires every §P1-18 digest to remain exact. The future-edit table then
   permits that verifier to implement only `G-1` through `G-10`, “and nothing
   else.” Installing `G-11` is therefore forbidden; changing the verifier to
   add it also makes `G-11` reject its own installation. Leaving the verifier
   unchanged leaves no operative `G-11` gate.
3. `G-11` compares data *using* the verifier and manifest but binds neither the
   post-handoff verifier nor the manifest/test bundle as an authenticated unit.
   A state with new documents and hashes but a stale verifier, or with omitted
   or stale tests 92–103, is not rejected by the stated comparisons. Test 103
   covers historical/document absence or staleness, not every
   manifest/verifier/test subset.
4. `G-10` is not uniquely specified. §P1-14.3 already names its guard-pattern
   authoring discipline `G-10`, while §P1-14.4 gives the same identifier to the
   W-A/W-B marker guard; tests 76 and 102 exercise the two different meanings.
   The current file has 28 unresolved markers (14 of each), but the duplicate
   identifier makes the required independent post-selection gate ambiguous.

Thus at least one partial state can run without the new gate, while the state
that actually installs the gate is nonconforming or self-refusing. This is the
bounded question's blocking partial-runnable-installation condition.

### 6. Retained reads and PCS journal pass

The four retained supervisor-identity reads remain read-only identity/liveness
checks. They install nothing, own no decision, enter no acceptance predicate,
and supply no endpoint, covariate, evidence repair or scientific fact. The PCS
classifier's terminal, per-group tokens and `freeze_ns` remain operational and
audit material only; §P1-10.7, invariant 89 and test 101 prohibit every route
to a peer artifact, predicate, publication, qualification, comparison, Q or C
fact.

### 7. Recommendation and status pass

The option comparison uses only signed-authority fidelity, constructibility,
mechanical testability, liveness and blast radius. The common authority repair
does not depend on an outcome and does not imply an author selection. W-B
remains a recommendation only. `T` remains `NOT_ACTIVATED`; the programme claim
remains `OPEN`; neither watchdog option is selected.

## Smallest bounded repair

Revise only the two governing files and regenerate their custody material:

1. Move the complete handoff list into both governing files and delete `H-4`'s
   normative dependency on the author closure.
2. Narrow §P1-14.1's one-file rule to the body/wording guards and state the
   exact closed input set for the joint-install guard.
3. Remove the pre-install verifier digest from the immutable historical set, or
   label it explicitly as a non-enforced baseline. Permit and pin the
   post-handoff verifier implementing the joint-install guard.
4. Bind the composite, amendment, exact provenance set, accepted peer-chain
   set, manifest version and bytes, verifier bytes, tests 92–103 and their
   passing attestation in one externally anchored install record checked before
   any production entry point. Add omission, stale, mixed-generation and extra
   member fixtures for every component class. No component may attest its own
   presence or digest.
5. Reserve `G-10` uniquely for unresolved W-A/W-B markers, rename the earlier
   authoring-discipline label, and keep the marker check independent of the
   joint-install guard.

No mechanism, option, token or author cell needs to be added. Kirill's
watchdog author-choice token is **not authorized** on these bytes. No
implementation, acceptance, activation, process-control or scientific
authority follows.

```text
T = NOT_ACTIVATED
PROGRAMME CLAIM = OPEN
WATCHDOG-FREEZE CELL = NOT SELECTED
```
