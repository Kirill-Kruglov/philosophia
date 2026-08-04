REVISE_OFFICINA_P1_WATCHDOG_V2_4

# Final Y-line confirmation — Officina P1 watchdog v2.4

**Reviewer:** GPT-5.6 Sol, independent governance Y line.

**Scope.** Bounded confirmation of the v2.4 governing pair and joint-install
protocol against the seven requested properties. I read the v2.3 Y review, the
v2.4 packet, both governing files and the author closure. The closure was used
only as an untrusted custody/checklist aid. No historical or closure text was
treated as behavioural or installation authority.

## Custody

The four supplied SHA-256 values recompute exactly:

```text
ce68b810611304b3877b6ecc227ce5c7a02e3d7b939183089a90d188c1d0ab6f
  successor/OFFICINA_P1_WATCHDOG_FREEZE_AUTHOR_CHOICE_PACKET_V2_4_CORRECTION.md
ec5ddff8f8d09c1574a56d173579a6b585a8f9de230afb86e43d9415fb7a4390
  successor/OFFICINA_GENERIC_HARNESS_WATCHDOG_FREEZE_AUTHORITY_AMENDMENT_V1_1_DRAFT.md
c904ec4318485acd49a6128ca32f9e52fe523c3703b730351f8ad98adb3e60f1
  successor/OFFICINA_GENERIC_HARNESS_SUPERVISOR_CONTROL_CHANNEL_P1_OPERATIVE_COMPOSITE_V1_4.md
1e230432a6e81c8b7705257168a9e8fa192a634afce076e568d3be422ed856d9
  reviews/opus5_officina_p1_watchdog_freeze_choice_v2_4_closure.md
```

All 43 path/digest rows in composite §P1-18 recompute exactly, including the
v2.3 pair newly added to provenance and the explicitly non-enforced verifier
baseline. The six sentinels occur once each and in the required order. Direct
extraction gives:

```text
H_BODY       0e769e3139f144df4e2f487d546976ca725976ea033cdcc22900c96f800f083f
H_GUARDDATA  faf2d709cb711baca148c98eb36dccd06efdf716a2682d6d7611dc80fe540426
H_NORMATIVE  df85ebb5a843d65af38c91d6fba7da7f2481a240f5f4cfdcea657f9f81ac7efd
H_FILE       c904ec4318485acd49a6128ca32f9e52fe523c3703b730351f8ad98adb3e60f1
```

Custody is intact. The revision finding is normative and procedural.

## Determination

### 1. Governing surfaces and handoff placement pass

Amendment §A9 and composite §P1-14.8 each state the complete ordered handoff
in normative bytes. `DA-1` through `DA-5` make history document-level
provenance, withdraw v1 `H-4`, and prohibit dependency on an author closure.
The two governing files restate the behavioural rules needed by the restored
acknowledgement, recovery, swap and consumption paths. No closure or historical
document must be followed for behaviour.

The amendment §A9 introduction's reference to composite `§P1-19` is a wrong
section number; the complete list nevertheless follows immediately in §A9
itself, and the other governing references correctly name §P1-14.8. This typo
does not reactivate another document or omit a rule.

### 2. Guard separation and verifier-baseline repair pass

Composite §P1-14.1 confines `G-1` through `G-10` and `AD-1` to one composite
file. `G-11` is the sole set-valued exception. The provenance note explicitly
marks the present `verification.py` digest as a non-enforced pre-install
baseline, excludes it from `M2`, and permits and requires a post-handoff
verifier as `M5`. The v2.3 verifier self-refusal is removed.

`G-10` is now reserved uniquely for unresolved option markers; `AD-1` has the
former authoring-discipline meaning. Their pattern classes are disjoint, and
`G-10` and `G-11` are explicitly independent. After one author option is
resolved and the other branch is removed, `G-10` is satisfiable.

### 3. `G-11` does not have the claimed closed, enumerable input set — blocking

`IR-9` step 1 requires the verifier to enumerate members from the normative
class definitions, not from the install record. Those definitions do not make
that operation possible:

1. `M4` supplies no normative manifest path and no literal schema id or version.
   The only path hint is in the non-normative future-edit table.
2. `M5` supplies no normative verifier path.
3. `M6` supplies no exact test-module path or path set and no canonical rule for
   forming one digest if the rows occupy multiple modules. The future-edit table
   says only `test modules`.
4. `M7` supplies no path, schema, exact key set or canonical attestation bytes.

These are semantic descriptions of desired files, not an enumerable set of
`{class, path, sha256}` members. A verifier must therefore obtain paths from the
record (which `IR-9` forbids), consult non-normative text, scan a directory, or
interpret adjectives such as "implementing", "carrying" and "recording". The
claim in composite §P1-14.1 that the input contains no adjective is false.
Consequently `G-11` is not constructible solely from the governing bytes, and
tests 107 through 113 do not yet specify reproducible fixtures for the actual
member set.

There is a second closed-set defect. `M2` is defined as every path listed in
§P1-18 except the named verifier baseline. But §P1-18 also lists all seven
members assigned to `M3`: the five generic-harness contracts, the
generic-harness signature and the batch-settlement v1.1.1 amendment. `M2` and
`M3` therefore overlap on seven physical paths despite both governing files
asserting that all classes are pairwise disjoint. Per-class omission, extra and
stale tests cannot have the asserted independent meaning on that definition.

### 4. The external trust root is not mechanically authenticated — blocking

The record itself is installed no-replace after `M7`, excludes itself from its
member preimage, and production is required to compare the recomputed id before
any entry point. Those aspects are non-self-attesting and fail closed in
principle.

The external authorization step is not closed, however. `IR-5` and `G-11` name
only "the author signature file". They give no exact path, schema, key set,
signature algorithm, signer-key identifier or verification rule. `IR-9` step 5
checks equality with an id found in that file but never requires authenticating
the signature or pins the external verification root. Substitution of the
purported trust-root file can therefore authorize a different internally
consistent record unless an unstated signing convention is imported. Importing
such a convention would violate the complete-handoff and no-adjective rules.

There is also no ordered handoff step for obtaining and verifying the external
authorization after the actual `M1` through `M7` digests determine the id and
before the install record is written. Calling the file pre-existing does not
resolve that ordering: the same file is said to carry the selected watchdog
branch, needed before post-resolution `M1` and the tests exist, while also
carrying the id that depends on the later `M7` digest. A two-stage author
authorization can resolve this, but it is not presently specified.

Thus omission, stale, substitution and mixed-generation checks are declared,
but the verifier cannot determine the intended manifest/verifier/test/
attestation paths or authenticate the object that chooses the authorized set.
The install binding is not yet a genuinely external, closed trust chain.

### 5. Behavioural authority and scientific boundary pass

The restored rules do not reopen `killer == WATCHDOG`. Amendment §A5 conjunct
8 remains mandatory on every path; `KW-1` forbids default, migration,
compatibility, recovery, archival import, takeover re-derivation and fixture
re-entry. Ack publication and draining, the total three-class consumption
order, and the swap-only state machine all retain the supervisor as writer.
Every admissible freeze observation has `killer = SUPERVISOR`; fallback and
replacement objects are supervisor-written.

The PCS classifier remains a separate execution site without a peer evidence
write. Its terminal, per-group tokens, stop samples and `freeze_ns` are
operational/audit facts only and are excluded from peer predicates,
qualification, comparison, Q/C facts and publication. The install record is
also control-plane custody material, not scientific evidence or a predicate
input. No treatment or scientific evidence class was added.

### 6. Choice and status pass

Neither W-A nor W-B is selected. The common repair is symmetric, the
recommendation remains nonbinding, no token or author cell is added, and the
process-identity cell remains open. `T` remains `NOT_ACTIVATED`; the programme
claim remains `OPEN`.

## Smallest bounded repair

Revise only the two governing files and regenerate their custody material:

1. Give every `M1` through `M7` member a literal normative path and cardinality.
   For `M4` and `M7`, also give exact schema ids, versions/key sets and canonical
   encoding; for `M6`, define the exact path list and canonical bundle digest.
2. Make the classes truly disjoint by defining `M2` as an explicit exact path
   set that excludes the seven `M3` peer/batch members as well as the verifier
   baseline, or move those seven digest rows outside the `M2` source list.
3. Define the external authorization artifact by exact path and schema, bind
   both Kirill's selected watchdog token and the computed install-record id,
   and specify signature verification against a pinned external signer key.
   Add the obtain-and-verify authorization step after `M7` and id computation
   and before installing the record; keep the authorization artifact outside
   `M1` through `M7` and install the content-addressed record last.
4. Update rows 104 through 115 to exercise exact-path substitution, class
   overlap and trust-root path/signature substitution as well as the existing
   digest cases.

No watchdog mechanism, evidence schema, treatment, option or scientific rule
needs to change. Kirill's watchdog author-choice token is **not authorized** on
these bytes. No implementation, acceptance or activation authority follows.

```text
T = NOT_ACTIVATED
PROGRAMME CLAIM = OPEN
WATCHDOG-FREEZE CELL = NOT SELECTED
```
