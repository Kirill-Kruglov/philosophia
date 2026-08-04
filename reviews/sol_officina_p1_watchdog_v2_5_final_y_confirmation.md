REVISE_OFFICINA_P1_WATCHDOG_V2_5

# Final Y-line confirmation — Officina P1 watchdog v2.5

**Reviewer:** GPT-5.6 Sol, independent governance Y line.

**Bounded determination.** v2.5 repairs the literal `M1`..`M7` member-set
defect and specifies a non-circular Stage-B signature chain, but it does not
mechanically enforce the historical order or the full replay property it
claims. It also leaves several generated-artifact fields under-specified.
Consequently `G-11` is enumerable, but the two-stage authorization is not yet
closed on the exact fail-closed terms stated by the governing pair.

## Custody

The four supplied SHA-256 values recompute exactly:

```text
e794813e58a0d59f2eb6ce8c88fda34fc8d4bf0ffbd2c4045d9604ae5bb89cc5
  successor/OFFICINA_P1_WATCHDOG_FREEZE_AUTHOR_CHOICE_PACKET_V2_5_CORRECTION.md
058c119c5de770dc537fd16962723063d2c3d4dad5da17d1431d4402927ebd1b
  successor/OFFICINA_GENERIC_HARNESS_WATCHDOG_FREEZE_AUTHORITY_AMENDMENT_V1_2_DRAFT.md
8751317511a3f738de35402b3c67ab9786e7fe1c95ea12d1e175ddd6540ddb20
  successor/OFFICINA_GENERIC_HARNESS_SUPERVISOR_CONTROL_CHANNEL_P1_OPERATIVE_COMPOSITE_V1_5.md
97045681b2e73a64a1ab270fef1c1564a85a4e4c8155a5fa3308b0c945a24806
  reviews/opus5_officina_p1_watchdog_freeze_choice_v2_5_closure.md
```

The accepted-chain custody also reproduces: all 39 `MS-2` and all seven
`MS-3` path/digest rows match the files on disk; the two sets have empty path
intersection; and the seven `MS-3` values match amendment §A0.1. The joint
install-and-authorization spans extracted from amendment §A10 and composite
§P1-14.4 are byte-identical, with SHA-256
`1ecbc71b3c849ccdc7ec576bc1995dfee6f666b1a2f9eefac392b202dcacd146`.

The composite has exactly one of each of its six sentinels, in the required
order. Direct extraction reproduces:

```text
H_BODY       f4e17ad40546cd099a042bf7f14fa3ab30ef193298c457f84d524839c20fa015
H_GUARDDATA  faf2d709cb711baca148c98eb36dccd06efdf716a2682d6d7611dc80fe540426
H_NORMATIVE  f12330735dc14c903cfce79fb553d685bac27e41f376b8502d2e2556ae8c4a26
H_FILE       8751317511a3f738de35402b3c67ab9786e7fe1c95ea12d1e175ddd6540ddb20
```

The author closure was used only as an untrusted checklist. No closure or
historical prose was treated as installation or behavioural authority.

## Findings

### 1. Literal enumeration and disjointness pass

Mechanical extraction from `MS-1`..`MS-7`, without reading an install record,
manifest, provenance table or directory, gives:

```text
M1  2   M2  39   M3  7   M4  1   M5  1   M6  2   M7  1
TOTAL 53
DUPLICATE PATHS 0
```

All paths are literal repository-relative byte strings. `M2` is its own
39-row constant and contains neither an `M3` path nor
`src/philosophia/officina/verification.py`. The pre-install verifier digest is
therefore only a non-enforced provenance row, while the post-handoff verifier
at the same literal path is `M5`. `CK-4` can derive the whole member set from
governing constants alone. The v2.4 class-overlap and adjective defects are
closed.

`M6` also fixes two literal module paths, their order, the exact row-name
membership rule, per-module whole-file digests, and the canonical two-entry
bundle preimage. No directory scan or prose table is needed to identify either
member.

### 2. Some generated-artifact schemas are still incomplete

The exact paths, top-level key sets and `MS-0` canonical byte rule are now
present, but the claim that the schemas are fully constructible without a
further choice is too strong:

- `MS-4` does not define the JSON type, entry shape or ordering of
  `reachable_closure`; composite §P1-3.3 is a prose table, not a canonical JSON
  value. `MS-4` also gives no value grammar for `created_utc`.
- `MS-7` gives no value grammar for `created_utc`. `IR-3` has the same omission
  for the install record. In each case `SCHEMA ID` should also be stated
  explicitly as the mandatory value of the `schema` key, as the older exact
  record definitions do.
- `TS-1` describes the three `governing_pre_selection` path values as “the
  v2.5 author choice packet, the v1.2 amendment and the v1.5 composite”, but
  the literal v2.5 packet path does not occur in either governing file.
- `TS-2(b)` checks canonical bytes, the exact key set and types, while
  `TS-2(c)`..`(f)` check only selected option/key/digest bindings. The stated
  six-clause verification never expressly checks the required `schema`,
  `version`, `author`, `signature_algorithm`, embedded pre-selection paths,
  `threat_model` or `created_utc` values. `TS-5` likewise never expressly
  checks the Stage-B `schema`, `version` or `created_utc` values. A schema
  definition and a verification algorithm must not leave it ambiguous whether
  these normative values are actually validated.

These do not change the 53 paths, but they prevent two independent verifier
implementations from deriving exactly the same artifact-validity predicate
from the stated clauses.

### 3. The Stage-B cryptographic binding is non-circular and otherwise passes

Subject to the schema omissions above, the main signature chain is sound on
its stated procedural threat model:

- `OR-2` permits only one of the two existing watchdog option tokens, and
  `TS-1` pairs it with exactly its existing option-specific token.
- `OR-3` places Stage A before `OR-4` finalizes `M1`. Stage A carries one raw
  32-byte Ed25519 public key, its SHA-256 key id, the option pairing, the
  pre-selection bindings and the exact `TR-2` threat-model string.
- `OR-9` computes the id only after `M1`..`M7`; `OR-10` requires Stage B to
  bind the Stage-A path/hash/key id, option, id and record path, member count
  53, and both post-selection `M1` digests.
- `TS-4` signs the exact canonical Stage-B file bytes, including the final
  newline, with pure RFC-8032 Ed25519. The detached signature encoding and
  single permitted verification key are exact. No unsigned or fallback-key
  route exists.
- The record, Stage A, Stage B, detached signature and public key are outside
  all seven member classes. The record id excludes the record; Stage A carries
  no digest of itself; Stage B carries no signature of itself; and `M7` does
  not attest itself.

The `M4` binding is enough to make substitution of Stage A alone fail. Coupled
with an independently tracked selection-round confirmation of the exact
Stage-A digest, it is a reasonable procedural external root. It is not, and
the governing bytes correctly do not make it, cryptographic proof against an
actor that can replace the entire chain before that external confirmation.

One subsidiary claim should be corrected: `IR-4` says every member is attested
by exactly one other object, and test row 115 says by the record “and by
nothing else”. That is literally false. `M4` carries `M1` digests, and `M7`
carries `M5`/`M6` digests, while the record also carries all member digests.
This does not create self-attestation; the uniqueness wording should simply be
removed.

### 4. Forbidden historical order is not mechanically distinguishable — blocking

`OR-1`..`OR-11` state one mandatory construction procedure, but the artifacts
and `CK-1`..`CK-12` authenticate only the final byte state. They contain no
trusted monotonic event, append-only predecessor, externally checked sequence
number, or other evidence from which the verifier can recover creation order.

For example, take the exact final bytes of an otherwise valid installation:

1. install the final record before Stage B exists;
2. later create the already-authorizing Stage B and its valid signature; and
3. invoke a production entry point only after every final file exists.

At that point `CK-3` and `CK-9` pass. No check observes that the record was
written early. The same indistinguishability applies to writing the final `M7`
bytes before actually running the matrix, computing an id from planned `M4`
bytes before writing that file, or creating Stage A after variant resolution.
The unchecked `created_utc` fields do not repair this, and timestamps alone
would not be trusted order evidence in any event.

Therefore composite test 106(h), `OR-11`'s statement that an early record is
refused, packet §3.2, and closure §4.1's “any deviation” statement are not
mechanical consequences of `G-11`. A conforming installer can follow the
procedure, but the pre-production gate cannot reject an identical final state
produced in the forbidden order.

### 5. Complete-generation rollback passes; `TR-2` minimizes the residual — blocking

The stated replay checks reject an old record against current members and
reject two hex-named records present together. They do not reject rollback of
the complete coherent generation.

After a later generation exists, a repository writer can restore a previously
valid bundle consisting of its Stage A, all 53 members, Stage B, detached
signature and sole content-addressed record. No new signature or private key is
needed. On those restored bytes:

- Stage A matches the restored `M4`;
- the old Stage-B signature verifies under the restored Stage-A key;
- the old id matches the restored members and sole record name;
- `CK-10` sees exactly one hex-named record; and
- every remaining digest and attestation comparison matches.

Thus a whole-generation post-hoc replay reaches a runnable state. `TR-2`
discloses only whole-chain substitution by an actor able to write at or before
Stage-A creation, then claims that every post-hoc substitution is closed. The
same stronger claim appears in the packet and closure summaries. Those claims
conflict with the complete rollback above. There is no conflicting claim of
cryptographic independence or immutable external custody, but the temporal
scope of the disclosed residual is too narrow.

### 6. Scientific and authorization boundaries pass

`G-11`, the authorization artifacts, manifest, attestation and install record
remain process-integrity/control-plane material only. They enter no treatment,
peer evidence object, qualification, comparison, Q/C fact, endpoint, outcome
or Proof. No watchdog mechanism or scientific writer changes.

Neither option is selected. The repository contains no Stage A, Stage B,
detached signature, `M4`, `M6`, `M7`, content-addressed install record, key or
entropy produced by this round. The process-identity cell remains open,
`T = NOT_ACTIVATED`, and the programme claim remains `OPEN`.

## Smallest bounded repair

Revise only the byte-identical joint block, its exact tests, and summaries:

1. Complete every generated-artifact schema and its verification clauses:
   literal nested shapes/types/order, literal pre-selection paths, exact
   `schema` values, timestamp grammar, and an explicit check for every required
   value. In particular, give `reachable_closure` one canonical JSON form.
2. Either add a genuinely external monotonic freshness/order anchor that lets
   `G-11` reject a complete old generation and distinguish the asserted order,
   or narrow the protocol honestly: make `OR-1`..`OR-11` a procedural
   construction obligation, withdraw test 106(h)'s retrospective refusal
   claim, and extend `TR-2` to complete coherent rollback at any later time.
   Because the requested property is fail-closed replay/order rejection, the
   former is required for confirmation on that property.
3. Replace “every post-hoc substitution” with the exact proper-subset cases
   actually closed, and remove the false unique-attester wording from `IR-4`
   and row 115.

No watchdog option, mechanism, scientific rule, treatment or evidence schema
needs to change. Kirill's watchdog option-selection token is not authorized on
these bytes. No acceptance, implementation, key generation, artifact creation,
commit or activation authority follows.

```text
T = NOT_ACTIVATED
PROGRAMME CLAIM = OPEN
WATCHDOG-FREEZE CELL = NOT SELECTED
PROCESS-CLAIM IDENTITY CELL = NOT SELECTED
```
