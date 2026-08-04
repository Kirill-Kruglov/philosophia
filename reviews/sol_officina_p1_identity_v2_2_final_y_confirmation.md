REVISE_OFFICINA_P1_IDENTITY_V2_2

# Independent final Y-line confirmation — Officina P1 identity v2.2

**Reviewer:** GPT-5.6 Sol, independent scientific-validity and governance line.

**Date:** 2026-08-04.

**Scope:** bounded confirmation of the v2 identity packet as modified by v2.1
and v2.2. The v2.2 author closure was treated as an untrusted self-assessment.
The review used reads, textual lineage tracing, repository searches, and digest
recomputation only. It did not implement or activate anything.

## 1. Executive determination

The v2.2 correction closes the two substantive v2.1 digest-accounting defects:
it names the persistent and occupant evaluations separately, preserves exactly
two direct raw-lineage-digest destinations, enumerates the signed transitive
integrity lineage, and withdraws the claim that the digest can never carry
identity or equality information.

It is nevertheless not yet honest enough for author selection on these bytes.
Two exact, bounded failures remain:

1. `CS-4` still makes the unconditional statement that there is **no reader**
   for whom the digest conceals the identity fields, and `WL-3′` says the digest
   has **no confidentiality property**. The proved search bound is conditional
   on possession of the other eighteen canonical fields. A digest-only reader
   is neither proved to possess those fields nor analysed. The packet is right
   to disclaim a confidentiality guarantee, but that is not equivalent to
   proving absence of every confidentiality property for every reader.
2. `PT-1` proves a pathname-spelling property, then its corollaries promote that
   result to a byte-provenance property: every canonical claim byte string is
   said to enter only through `MS-2`. A permitted `PC-N` pathname can resolve to
   or contain claim bytes through a planted symlink, a hard link, or copied
   bytes. v2.2 names only the external-symlink residual, incorrectly says a
   conforming root does not follow the redirect, and does not contain the
   consequence that claim bytes can then bind to a non-carrier Name and parse
   into a non-governed mapping. This reopens the precise no-second-sink premise
   that Repair A is meant to establish.

These are consistency and boundary-scope defects, not an architectural block.
The smallest repairs are specified in §8. No other accepted cell is reopened.

## 2. Byte custody and governing chain

The requested v2.2 digest recomputes exactly:

```text
05046cd17fe0839541b9ec7614aaf66a84e69c169f9142a29e6a5cabf7bf0fc7  successor/OFFICINA_P1_PROCESS_CLAIM_IDENTITY_AUTHOR_CHOICE_PACKET_V2_2_CORRECTION.md
```

The relevant predecessors and final-review inputs also recompute to the values
recorded by the chain:

```text
f5d95a0d4a7c72731b5a20cf668e67dbc66329e0989fb945bd0a5727717f6095  successor/OFFICINA_P1_PROCESS_CLAIM_IDENTITY_AUTHOR_CHOICE_PACKET_V2_DRAFT.md
3796de017449a9786db0b9b0ca0e8c2d84762e2239463033773b1fdb92b8ef37  successor/OFFICINA_P1_PROCESS_CLAIM_IDENTITY_AUTHOR_CHOICE_PACKET_V2_1_CORRECTION.md
c2d7a95784ad1bbc2a34898c0d3abf4de94dcd3416b14b959a3b2b61d6fab614  reviews/opus_officina_p1_process_claim_identity_choice_v2_1_final_confirmation.md
cee60b4b85358a50a90729645081419b166cbc1224b53776ffb41a357cb5f578  reviews/sol_officina_p1_process_claim_identity_choice_v2_1_final_confirmation.md
a9d48c9d8d64214e4685065f9c16989aa095ccca14273019805682d00526f8e4  reviews/opus5_officina_p1_process_claim_identity_choice_v2_2_closure.md
```

The prompt names a `...PACKET_V2_CORRECTION.md` predecessor that does not exist
in the repository. The identity chain itself consistently names
`...PACKET_V2_DRAFT.md`; I used that committed file and did not invent a missing
artifact.

The operative signed inputs also match the recorded custody values:

```text
2c857fa8ad7be1c861eb8cf561f396e7d2339403c7714abc7958745bf34e5d5d  successor/OFFICINA_GENERIC_HARNESS_SUPERVISOR_CONTROL_CHANNEL_P1_OPERATIVE_COMPOSITE_V1_2.md
cd106d7fef491601f9ff948aba3ba0ceaac0774ac18a6564247c0c5899b4c40c  successor/OFFICINA_T_ACTIVATION_PROTOCOL_V2_CORRECTION.md
64b8d3f63594b79a6abc767a032383c5704beaf09b32a1e0c58fdc444bb0af71  successor/OFFICINA_GENERIC_HARNESS_CONTRACT_V2_DRAFT.md
8c47da352ef5954406964647a32e97939c404806bdf9b3d3ff5bc70866e6369a  successor/OFFICINA_GENERIC_HARNESS_SIGNATURE.md
```

## 3. `EV-1`, `EV-2`, direct destinations, and the full lineage

### 3.1 The two authorized `ACC-5` evaluation classes

The two classes now match the signed lineage:

| Evaluation | Operand and precondition | Result and use |
|---|---|---|
| `EV-1` | complete canonical bytes of a fully validated process claim | the persistent raw lineage value, carried directly only by `D-1` and `D-2` |
| `EV-2` | complete canonical bytes of the independently validated `EEXIST` occupant, after `X-2` and `X-3` | a transient equality operand consumed only by `X-4`, with no durable destination |

Repository-wide exact-key search over the governing successor contracts found
no missing live raw `process_claim_sha256` destination. The two live direct
destinations are:

- `D-1`: the durable non-state-bearing `T_PROCESS_STARTED` event required by
  generic-harness contract §2c.2;
- `D-2`: `t-process-record.v1.process_claim_sha256`, fixed by the activation
  protocol's exact key set.

The older `OK/CLAIM` reply matrix is not a third live destination: it remains in
the superseded supervisor/control-channel history, is not restated by the v1.2
operative composite, and is absent from the accepted peer contracts. The active
lease repeats the claim keys, but the claim does not contain its own digest, so
the lease is not another raw-digest destination.

`S-25m′` is an AST call-site/count rule. Accordingly, “two evaluations” is
sound as two authorized syntactic evaluation classes, not as a claim that a
multi-process lifetime executes SHA-256 only twice. Recovery or retry may
re-establish the same persistent value only through the same `EV-1` class or an
already-durable lineage fact; it creates neither a third accessor site nor a
second persistent lineage value.

### 3.2 The five transitive continuations

The signed graph is exhaustively covered by `L-1` through `L-5`:

1. the complete start-entry hash and its use as the initial lease-chain seed;
2. later charge/event hashes and lease equality/hash continuity;
3. the final-record hash named by `T_PROCESS_STOPPED`, including the signed
   invalid-close shape;
4. archive copies and containing Git object/tree/commit hashes;
5. recovery and post-crash canonical/hash verification.

These continuations do not create a third field equal to the raw lineage
digest. In authorized use they provide record identity, ordering, canonical
equality, and lineage continuity only. They do not authorize a PID selector,
opcode argument, signal or wait target, treatment assignment, scientific
covariate, learner input, outcome interpretation, qualification fact, capacity
fact, custody disposition, spend fact, Q/C input, or Proof.

Information-theoretically, a containing hash can inherit the same conditional
search channel when a reader knows the enclosing object's other fields and the
claim's other fields. That does not turn it into an authorized scientific or
process-control input, but it is part of the information-flow surface and must
be included in the conditional wording repaired in §8.1.

## 4. Confidentiality and conditional identity information

The numerical bound is correct. The unknown identity tuple collapses to one
integer because the selected leader construction requires
`attested_pgid == attested_pid`. With the pinned inclusive range
`1..PID_MAX_LIMIT` and `PID_MAX_LIMIT = 4,194,304`, there are at most
4,194,304 candidate canonical claims. Given the other eighteen exact fields,
ordinary exhaustive comparison against the digest is practical. A claim or
archive reader needs no search because both integers are in cleartext.

The correct scientific classification is therefore conditional:

- with the other eighteen canonical values, the raw digest is a searchable
  identity commitment and a matching candidate supplies conditional identity
  evidence;
- digest equality supplies probabilistic cryptographic equality evidence for
  the canonical claim bytes, subject to the usual collision qualification;
- a claim/archive reader sees the identity directly;
- for a reader holding only a digest or a transitive containing hash, v2.2 has
  not bounded the remaining unknown space and has not proved recoverability.

Most of Repair C states this correctly: `CS-2`, `CS-3`, `CS-5`, `CS-7`,
`DC-3′` through `DC-5′`, and `WL-4′` distinguish informational possibility
from authorized use and preserve the process/science sink bans. But the
following absolutes survive:

```text
CS-4:  "THERE IS NO READER FOR WHOM THE DIGEST CONCEALS THE IDENTITY FIELDS"
WL-3′: "THE DIGEST HAS NO CONFIDENTIALITY PROPERTY"
```

Those propositions do not follow from a search conditioned on eighteen known
fields. The defensible governance statement is that this cell **provides and
authorizes no confidentiality guarantee**. It may not convert that disclaimer
into the stronger scientific assertion that every possible reader can recover
the fields. Thus not all false confidentiality language has been withdrawn.

## 5. Path/access closure and the material residual

### 5.1 What `PA-1` through `PA-9` do close

Within the AST and pathname-spelling model, the repair is bounded and useful:

- the sole `T_PROCESS_CLAIMS` literal and `_claim_path` call are pinned;
- dynamic stems cannot contain separators, traversal, NUL, a leading dot, or
  bytes outside their grammar;
- read operands are plain Names with local constructor bindings;
- direct `dir_fd`, `follow_symlinks`, `chdir`, `fchdir`, `os.symlink`, and
  `os.link` uses are excluded from the five roots;
- the claim pathname read is pinned to `MS-2`, carrier binding to `PA-8`, and
  carrier parsing to `MS-3`;
- assembled literals, inline paths, environment/config paths, helper-return
  routes, directory enumeration, and direct archive-path reconstructions are
  rejected mechanically.

The intra-function assignment index at `PA-7` is finite, local, and compatible
with the no-taint/no-call-graph boundary. `PC-N` is genuinely shape-closed for
path strings, and the fixed five-root list makes its static counts decidable.

### 5.2 What pathname spelling does not prove

The promoted byte-provenance conclusion is false without an additional
filesystem/content gate:

- **Symlink:** ordinary `open(path, "rb")` follows a symlink. Omitting a
  `follow_symlinks` keyword does not prevent that behavior. An outside actor can
  make a permitted `PC-N` name resolve to a process claim. v2.2 names this
  residual but incorrectly concludes that no conforming root follows the
  redirect.
- **Hard link:** banning `os.link` in the five roots does not stop an outside
  actor from giving the claim inode a second permitted name. `PA-1` through
  `PA-9` inspect path syntax, not inode identity or link count. This residual is
  not named.
- **Copied bytes:** an outside actor can place byte-identical canonical claim
  content at a permitted `PC-N` path with an ordinary single-link inode. No
  path, symlink, or `samestat` test alone distinguishes those bytes. This
  residual is not named.
- **`dir_fd`:** direct use is adequately excluded by `PA-6`; this is not the
  open route.
- **`/proc/self/fd`:** `S-13` prevents dynamic descriptor-path construction but
  permits exact constants. The current `MS-2` shape supplies no demonstrated
  live claim descriptor outside its read expression, so there is no standalone
  concrete bypass on the reviewed execution shape. Nevertheless the path rules
  do not prove descriptor provenance; a descriptor alias, if one exists, falls
  into the same residual and must be rejected by the content/descriptor gate.

The material consequence is not merely that a same-UID actor can learn bytes it
could already read. A `PC-N` reader may bind those claim bytes to an ordinary
non-carrier Name and `json.loads` may bind the result to an ordinary
non-governed mapping. The preserved scope note leaves `.values()`, `.items()`,
and ordinary-mapping consumers available. Consequently the exact prior leak
shape can resume after runtime aliasing:

```text
permitted PC-N read -> non-carrier raw bytes -> ordinary mapping
                    -> values()[5] / values()[7] -> non-whitelisted sink
```

The signed A3 rescope admits same-UID filesystem power, but it does not permit
interference to become a valid Officina record, resource fact, comparison, or
scientific fact. v2.2 does not connect these alias/content cases to a
path-bound schema check and dominant invalidity before mapping/value use. Its
statement that the symlink residual is “not a new exposure” therefore does not
contain the governance consequence. Existing descriptor-anchor and strict
schema rules may reject particular records, but `PT-1` does not import and pin
such a gate for every `PC-N` read before bytes or mappings are exposed.

Thus `PT-1` is valid only as a pathname theorem. Corollary 1's “every byte
string” conclusion, `M-R4`'s renewed premise, and the universal “only these
readers can observe claim bytes” interpretation are not established.

## 6. `PC-N`, five-root dependency, and inferential expansion

The choice not to enumerate peer-owned paths is procedurally reasonable.
`PC-N` can add a new constructor only under the same constant-plus-checked-stem,
plain-Name-read shape; a sixth production root explicitly reopens `PT-1` and
every `S-25m′` count. Those boundaries are named and do not silently expand by
analogy.

What is not yet bounded is content equivalence across permitted `PC-N` names.
Because new `PC-N` paths are allowed, a copied or aliased claim can enter a new
ordinary reader without changing the claims-root literal count, claim-path Name
count, accessor count, or call-site count. The inferential surface can therefore
expand while every current arithmetic assertion remains true. This is the same
Repair-A failure, not a demand to enumerate all peer schemas.

## 7. Counts, prior cells, routes, and negative space

The v2.2 arithmetic is internally correct:

```text
5 persistent consumers; 5 centralized accessors; 15 S-25 rules;
21 behavioural tests; 3 governed mapping Names; 3 carrier Names;
12 approved MS rows; 1 claim-path Name; 1 claims-root literal;
1 syntactic claim-read site in MS-2, called from 2 approved contexts;
2 ACC-5 evaluation classes; 1 persistent lineage value;
2 direct persistent raw-digest destinations; 5 transitive continuations;
1 declassifying operation.
```

The v2.2 replacement index does not change the already-accepted journal vector
and byte-identical replay, fresh-PGID authority and cross-check, PID bound,
crash/collision matrix, retained-claim invalidity route, corrected Option-B
schema count, corrected stale-`/proc` rationale, or separation of supervisor
and watchdog freeze failures. The valid-close, invalid-close, batch terminal,
archive, and record-first invalidity routes in the signed peer chain are not
rewritten by v2.2. The present refusal rests only on §§4–6 above.

The negative authorization also remains intact. The repository ledger states
`Status: NOT_ACTIVATED`; the operative composite continues to block on the
unsigned identity cell; the programme claim is `OPEN`; and the watchdog-freeze
cell remains unresolved and orthogonal. No implementation, entropy draw,
capacity use, spend, custody action, learner trajectory, datum, comparison
result, outcome, Proof, or claim movement is authorized by this review.

## 8. Smallest bounded repair

### 8.1 Conditional information statement

Replace only the absolute clauses in `CS-4` and `WL-3′` and their repeated
summaries:

- this cell supplies **no confidentiality guarantee** for the raw digest or its
  containing lineage hashes;
- recovery of PID/PGID is practical when the other eighteen canonical claim
  fields are known, with at most 4,194,304 candidates;
- claim/archive readers see the integers directly;
- no assertion is made about recoverability or remaining entropy for a reader
  who lacks those conditioning fields;
- the same conditional identity-commitment fact propagates through `L-1` to
  `L-5` when the reader also knows the other fields of each containing object.

No authorization rule needs to weaken. The existing ban on process, resource,
selection, Q/C, and scientific use remains verbatim.

### 8.2 Path theorem and alias/content consequence

Keep `PA-1` through `PA-9` as the pathname-spelling closure, but make two
bounded changes:

1. Narrow `PT-1` and its corollaries to pathname construction. Do not infer
   “every canonical claim byte string, however obtained” from path spelling.
   Name symlink, hard-link, descriptor-alias, and copied-byte equivalence as one
   external content-alias residual class.
2. Before any `PC-N` read bytes may be parsed, returned, or bound into an
   ordinary mapping, require the already-signed path/descriptor discipline to
   establish no-follow, regular-file, link-count and held-descriptor/path
   identity, followed by a path-bound exact schema discriminator. A
   `t-process-claim.v1` object or canonical claim bytes at any `PC-N` path must
   route to dominant filesystem/process invalidity before any value binding;
   it may never be treated as an ordinary peer mapping. Copied bytes are caught
   by the schema/path binding even when inode checks pass. Add negative fixtures
   for externally planted symlink, hard link, copied claim bytes, and any live
   `/proc/self/fd` alias, asserting invalidity before parse/use rather than
   asserting that the filesystem fact is statically impossible.

This repair does not enumerate the peer's record set, add a production root,
change a durable schema, alter an identity destination, or reopen an authority
cell. It supplies the missing consequence containment on which `M-R4` and the
no-second-sink claim depend.

## 9. Authorization boundary

Kirill's identity author-choice token and the conditional bounded-weakening
token are not authorized on the present bytes. This review authorizes no
implementation, verifier or manifest edit, commit, activation, process-control
act, resource use, entropy, data collection, trajectory, outcome, Proof, or
claim movement.

```text
T = NOT_ACTIVATED
PROGRAMME CLAIM = OPEN
WATCHDOG-FREEZE CHOICE = UNRESOLVED AND ORTHOGONAL
IDENTITY SELECTION = NOT AUTHORIZED
```
