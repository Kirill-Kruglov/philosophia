# Officina executable-contract migration charter v1 — independent Y review

**Reviewer:** GPT-5.6 Sol, independent Y line. Read-only review except for this
single review file.

**Reviewed objects:** exactly the two byte sequences named in the review
request. The architecture memo was treated as untrusted.

## Verdict

```text
REVISE_OFFICINA_MIGRATION_CHARTER_V1
```

The route is suitable for one bounded revision, but it does not yet eliminate
generation/provenance drift by construction. The external-signature exception
reintroduces a hand-copied digest; the five-lemma proof assumes rather than
enforces template/source purity and manifest completeness; physical archival
is contradictory and evidence-risking; and the extraction, trusted-surface
budget and stop counters are not closed mechanically.

These are structural provenance/authority/budget findings. This verdict does
not reopen W-B science and does not request another W-B prose generation.

```text
T = NOT_ACTIVATED
OR-3..OR-11 NOT AUTHORIZED
PROGRAMME CLAIM = OPEN
```

## Input gate and repository boundary

Both requested hashes were recomputed before substantive review and match:

```text
e9f9f641adec0d826f3c974f2e2e6ec14d184758ce933457b1949e9e7b9cd3f9  successor/OFFICINA_EXECUTABLE_CONTRACT_MIGRATION_CHARTER_V1_DRAFT.md
879d9c34aba2d8ff57c45e1fc1a29978bac627d672912b7a637a08eda8bf7d36  reviews/fable_officina_executable_contract_migration_charter.md
```

Commit `9e93df5` exists and carries those same two byte sequences. The live
checkout was `07f4fd58c46a4a4e77a58625694c6245adcfaed7`, with `9e93df5` as an
ancestor. The committed difference between them is limited to the X- and
Y-review prompt files; neither reviewed object differs. Pre-existing modified
and untracked work was left untouched. The commit-position observation is
therefore not a blocker.

## Y1 — external release binding

### Major Y1-M1 — the signature exception reconstructs Class B

Charter §2.1(4) permits a hand-written author signature to repeat the digest of
`MANIFEST.json`, while §4.3 checks only generated files. The following state is
therefore green under the stated checks: source and generated files change,
`MANIFEST.json` is correctly regenerated, and the signature retains the old
named manifest digest. The signature is outside the memo's live-surface
definition, but it is the proposed external release binding. Excluding the
only release-binding object from the theorem does not eliminate release
provenance drift.

Adding a signature-file option to `verify.py --check` would make that stale
copy fail, but would retain a second assertion of the same derived fact and
make acceptance depend on always invoking the extra option. It is a workable
consistency check, not elimination by construction.

A generated release-candidate envelope is also the wrong repair if it repeats
paths or digests: it becomes a second manifest. If it repeats neither, it adds
no binding that Git does not already supply.

### Single-valued repair

Use Git object binding, with no digest field in an author-authored file:

1. Delete the permission for an author signature file to carry the manifest
   digest. Author-authored acceptance material may contain the exact acceptance
   token and fixed negative-authority statements only: no count, path, digest,
   generation name or commit identifier.
2. Freeze the M3 release candidate as one Git commit. The X and Y M4 review
   commits must each descend directly from that candidate and may add only
   their one review file. A closure commit may combine those review commits but
   may not change `contract/**`, `generated/**`, the generator, verifier or
   provenance guard.
3. Make the M5 author act one cryptographically signed annotated Git tag with
   the exact acceptance token as its message, targeting that closure commit.
   The tag object's target edge binds the act to the complete tree; nobody
   copies a file digest or commit identifier into prose.
4. Require `verify.py --check --release-ref <tag>` (or one equivalently named,
   mandatory mode) to validate the tag signature against the pinned author
   identity, the exact token-only tag message, the candidate/review/closure DAG,
   the review-only diffs, and ordinary check mode at the tagged tree. Release
   status is false unless this complete mode passes.
5. Amend §5/§8.1 only enough to permit those future, gate-scoped Git objects.
   This review authorizes no commit, tag, signature or token.

This preserves an auditable author act, uses the Git tree as the external
envelope, and creates neither a second manifest nor a self-hash.

## Y2 — authority graph and template/source drift

### Major Y2-M1 — each lemma admits a green counterexample

The five-lemma proof is conditional on conventions that the charter does not
mechanically enforce.

| Lemma | Malicious but syntactically valid green change |
|---|---|
| L1 | Add `EXPECTED_MEMBER_COUNT`, `CURRENT_GENERATION`, a digest, a path list or a replacement/authority string to Python/JSON and have the renderer consume it. `contract/**` is general Python plus JSON, not a grammar containing declarations only. |
| L2 | Hard-code a false count, path, generation or authority sentence in `render.py` or its template. Regeneration and checked-in bytes agree exactly. |
| L3 | Let renderer and verifier share a hand-written file allowlist, omit one regular source file, or accept a supplied digest. The manifest is internally consistent and incomplete. |
| L4 | Acyclicity prevents a hash fixpoint; it does not prove completeness, correct path selection or truthful emitted claims. |
| L5 | Put a generation name in source data, a docstring, a template, generated prose or a signature. “No generation numbers” is policy, not a rejection rule. |

There are two additional structural collisions. First,
`contract/EQUIVALENCE_LEDGER.md` is placed under `contract/**` while being
explicitly excluded from `MANIFEST.json`; that contradicts the rule that the
manifest covers `contract/**` and creates the first sanctioned omission.
Second, the duplicated-string-literal test is not a provenance proof: string
concatenation, formatting, encoding, data files and differently worded
authority claims all bypass literal equality.

Byte equality against the same renderer proves reproducibility, not truthful
derivation. A wrong primary authority choice can also remain green; that is a
semantic/author-choice risk and must not be relabelled as Class-B elimination.

### Mandatory mechanical guard

Add one independent provenance gate to the M3 trusted base and make it part of
the definition of a green tree. It must not import or call the renderer and
must, from raw repository bytes:

- reject symlinks and non-regular files under `contract/**`, enumerate every
  regular file recursively, and require that exact set—without a hand-written
  allowlist—to equal the manifest path set;
- independently SHA-256 those bytes and compare the exact canonical manifest
  records, rejecting supplied/expected digests and all omissions or extras;
- enforce a closed, machine-readable contract schema that labels fields as
  primary or derived and makes count, digest, inventory, generation,
  replacement and duplicated authority-edge fields illegal as primary input;
- restrict documentation templates to a declarative placeholder grammar with
  fixed presentation labels only; generated factual and authority claims must
  be structured records that the gate parses back and independently recomputes
  from the contract IR;
- reject generation-shaped strings and digest-shaped literals from every live
  location except the canonical digest field in `MANIFEST.json`; require the
  token-only Git release form from Y1 for author acceptance;
- include mutation fixtures for each counterexample in the table above and
  prove that each makes the provenance gate fail even when normal render/check
  byte comparison passes.

Move the equivalence ledger outside `contract/**`, for example to
`successor/officina/migration/EQUIVALENCE_LEDGER.md`; keep it as evidence, not
as a manifest exception.

The theorem must then be restated narrowly: for every tree passing the
**unchanged independent provenance gate**, every published derived claim is
independently recomputed from the complete current authoritative file set. Any
change to the schema, template grammar, renderer, verifier or provenance gate
invalidates prior green status and requires the full independent M4 review; it
is not an ordinary source fix. No in-repository theorem can protect against a
malicious replacement of its own checker while continuing to call that a
green tree, so the pinned gate is an explicit trust root rather than an omitted
premise.

## Y3 — archive disposition

### Major Y3-M1 — choose logical archival in place

M0 makes a physical move conditional, §7 says the line moves on the M0 token,
and T-1 says the token archives it. Those are three different authorization
boundaries. At the pinned commit, a conservative filename inventory already
finds 103 successor draft/correction/composite/binding/handoff paths and 546
Officina review paths, while `successor/archive/` does not exist. A bulk move
would change paths named by signatures, reviews and provenance records, create
a large rename diff, and add merge/custody risk without changing one scientific
fact.

The single-valued disposition is **logical archive by signed status/index;
all Git paths remain unchanged**. M0 should create one machine-readable status
policy and a derived path index, bound by the same token-only signed-Git method
as Y1. The index carries statuses but no file digests or copied counts. The
provenance gate derives its path set from the tagged tree and rejects missing,
extra or multiply classified paths. Live authority resolution must reject
every entry marked `HISTORICAL_NONOPERATIVE`.

The status/index must record, without altering either evidence file:

```text
v2.15 candidate                    UNACCEPTED; HISTORICAL_NONOPERATIVE
v2.15 X evidence                   X_CONFIRMED_FOR_AUTHOR_CONSIDERATION_ONLY
v2.15 Y evidence                   REVISE; UNRESOLVED
aggregate v2.15 acceptance status  NOT_ACCEPTED
archive operation                  NO_ACCEPTANCE_EFFECT
```

The signed scientific and author-choice files remain separately classified as
live Class-C authority and are not swept into the halted prose line. No archive
status may convert “confirmed for author consideration” into author acceptance.
This preserves the X-confirmed/Y-revised divergence exactly and avoids path
breakage.

## Y4 — live scope, budgets, future invariants and stop rule

### Major Y4-M1 — I-1..I-15 is a thematic boundary, not a closed extraction

I-1..I-15 names the intended topics, but several entries incorporate large
unnamed semantic sets by reference. In particular I-7/I-8 refer to the current
candidate's entire KG-2 machine, I-9/I-10 refer to classifier phases, and M2 is
expected to settle already known Class-A readings that §3 does not enumerate.
The inventory does not pin the exact candidate path/section for those entries,
nor list all dimensions, values, routes, precedence edges, schema fields and
fail-closed continuations that M2 must preserve. A conforming M2 author can
therefore omit a state dimension or select one reading and remain inside the
wording of an I-item. §4.7 expressly admits that an undeclared dimension is
invisible.

Before M1, expand §3 into a finite semantic-atom inventory: exact source path
and section at the charter's Git-bound tree, every machine dimension/value set,
every route and write gate, every classifier phase/precedence edge, every
schema/frame field and every negative capability. Each atom must have exactly
one primary authority locator and later exactly one executable test. This is a
bounded inventory repair, not a new W-B prose generation. An unresolved
reading is a named blocked decision slot; an implementer or reviewer cannot
silently choose it.

The 2,500 LOC/120 KiB limit must be stated explicitly as applying only to the
authoritative specification under `contract/**`. All `src/**` implementation,
including the 2,380-LOC uncommitted harness and the rest of the approximately
7,349-LOC current Officina implementation surface, is outside that budget and
outside M1/M2 authorization. M6 reconciles implementation to the accepted
contract; it does not import implementation behavior into authority merely to
make existing code conform.

Define the LOC test mechanically as physical lines of every regular file under
`contract/**` (including blank and comment lines and a final non-LF line), with
symlinks rejected. Enforce both LOC and byte limits before review. Also place a
separate bounded cap on the provenance trusted base—schema, template grammar,
renderer, verifier and provenance gate—because otherwise the 2,500-LOC source
cap can hide an unbounded authority-producing program outside the budget. A
single total cap of **1,000 physical LOC and 64 KiB** for that non-test trusted
base is sufficient and mechanically checkable; generated output and tests do
not count toward it.

### M6 invariant discovery rule

M6 must classify a newly discovered item exactly once:

1. an implementation detail stays in `src/**`/tests and creates no contract
   authority;
2. a logical consequence of an existing semantic atom receives a derived test
   and no new primary invariant; or
3. a genuinely new or contradictory normative invariant emits
   `M6_BLOCKED_NEW_INVARIANT`, leaves the inactive accepted contract unchanged,
   and requires a separate future signed scope-extension route.

Case 3 must not amend charter v1, reopen M1/M2, reset their counters or authorize
integration. This prevents “charter amendment” from becoming the renamed
generation loop that the charter stops.

### Major Y4-M2 — the stop rule can be renamed or overridden away

“Review round,” “work package” and the 21-day clock lack mechanical identity.
A third evaluation can be called a confirmation, closure or pre-review; a
package can be renamed or split; M0 can be re-signed; and §6.3 says every limit
may be overridden by a new route decision. The nominal mandatory stop is
therefore waivable.

Add these exact counter rules:

- one migration episode is keyed by the first M0 signed Git object; its UTC
  start and 21-day deadline are immutable and inherited by every rename,
  split, merge, repair or successor package with substantially the same inputs,
  outputs or authority boundary;
- one round is one byte-distinct candidate submission followed by any external
  evaluation, whether labelled review, confirmation, audit, closure,
  pre-review or otherwise; simultaneous X/Y evaluations of identical candidate
  bytes are one round, and a changed candidate submitted again is the next;
- package counters attach to artifact scope, not package name; split/merged or
  renamed scopes inherit the maximum applicable counter;
- the round limit and deadline are excluded from §6.3 overrides. On either
  trigger, no author act can extend or reset this episode: only one of §6.2(a),
  (b) or (c) may be selected. A later route is a new route, not continuation of
  this migration, and cannot retroactively make this episode green.

## Mandatory edits for bounded revision

1. Replace signature-carried manifest digests with the token-only signed Git
   tag and mechanically checked candidate/review/closure DAG in Y1.
2. Add the independent provenance gate, adversarial mutation fixtures, narrow
   theorem and protected trust-root rule in Y2; move the equivalence ledger out
   of `contract/**`.
3. Resolve archival to the logical in-place status/index in Y3 and encode
   v2.15's X-confirmed/Y-revised aggregate status as not accepted.
4. Turn I-1..I-15 into a closed semantic-atom inventory with exact Git-bound
   source locators; do not delegate unresolved readings to M2 implementers or
   reviewers.
5. State that implementation is outside the 2,500-LOC authoritative budget,
   define mechanical counting, add the 1,000-LOC/64-KiB provenance-trusted-base
   cap, and adopt the three-way M6 invariant rule.
6. Define episode/round/scope identities and make the two-round and 21-day stop
   non-resettable and non-overridable within charter v1.

No other programme redesign is requested.

## Minor prose

- §5 M4 says X/Y “cannot” diverge on provenance before the guard needed to
  establish that claim exists. Replace the prediction with the gate condition.
- §3.1 calls the ledger both a `contract/**` output and non-member evidence;
  the path move required above resolves the wording as well as the structural
  exception.
- Use `PROGRAMME CLAIM = OPEN` consistently rather than alternating prose and
  code-block forms of the same state.

## Negative space

This review accepts no charter, executable contract, amendment, composite,
binding, handoff, implementation, archive move, signature or token. It
authorizes no M0-M6 work, no commit, no tag, no code or test edit, no runtime
artifact, no scientific action, no activation, and no `OR-3`..`OR-11` step.
It does not choose between W-B semantic readings and does not alter or withdraw
either v2.15 review.

Exactly one file was created: this review. No governing, historical, code,
test, signature, runtime or unrelated working-tree file was modified, moved,
staged, committed or deleted. No live process, `/proc`, socket, pipe, signal,
entropy, key, world, learner, candidate, spend, datum, outcome or Proof was
created or exercised.

```text
T = NOT_ACTIVATED
OR-3..OR-11 NOT AUTHORIZED
PROGRAMME CLAIM = OPEN
```

## Exact next boundary

One bounded charter-v1 revision applying only the six mandatory edits above,
followed by byte-identical independent X/Y review of that revised charter. No
M0-M6 work, implementation, archive operation, author token or Git release
object is in scope before that review closes.
