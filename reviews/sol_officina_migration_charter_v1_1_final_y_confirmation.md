OFFICINA_MIGRATION_CHARTER_V1_1_Y_STRUCTURAL_FAILURE

# Independent Y-line final confirmation

**Reviewed object:** solely
`successor/OFFICINA_EXECUTABLE_CONTRACT_MIGRATION_CHARTER_V1_1_DRAFT.md` as committed in
`28a3189fb25c06a160778c48b93dec015e0d78b3`.

**Input gate.** The working-tree candidate and the candidate bytes read directly from commit
`28a3189` both recompute to the required SHA-256:

```text
3266a18f4584e14297c886529c51f57ef20a47719a636b5101c001967c2cdb5e
```

The commit exists, has parent `00786276994766564228c06eb645c2661f297711`, and contains the
candidate as blob `4a25f1d0ebe82bf4135957d1b404ba30e2d1552d`. It is an ancestor of the
current `main` tip. The candidate is byte-identical between that commit and the working tree.
Pre-existing modified and untracked work was not touched.

## Decisive counterexample: negative reviews produce a release-green tag

The smallest counterexample needs no source, manifest, template or generated-byte corruption:

1. Let `C` be any M3 candidate commit for which every source, generation, provenance, budget and
   test gate is genuinely green.
2. Let `RX` descend from `C` and add exactly one X review file. The file records the correct O2
   comparison and the correct canonical route-vector digest, but its verdict is structural
   failure.
3. Let `RY` do the same for the Y line on the identical `C` bytes. X and Y agree that the
   candidate fails; there is no semantic divergence between them.
4. Let `L` combine those two review commits without changing any reviewed surface, and let Kirill
   create the correctly signed annotated tag with the token-only message required by §1.3.

Every mechanical condition actually stated remains green:

- `RX` and `RY` each add one review file and no other diff from `C`;
- all reviewed surfaces at `L` are byte-identical to `C`;
- both M4 memos exist on identical bytes;
- O2 is recorded and each `G-STALE` value matches the recomputed tagged route vector;
- X and Y do not diverge on a semantic question;
- ordinary check mode, `G-PROV`, the suite, blocker reporting, tag type, tag signature, tag
  message and the described DAG all pass.

The falsely green gate is **M4**, propagated by mandatory
`verify.py --check --release-ref` into **M5 release status**. Section 6 defines M4 closure only by
memo existence, byte identity, O2 recording and a pinned `G-STALE`; its terminal condition covers
X/Y semantic divergence only. Section 1.3 likewise requires review-only diffs and reviewed-byte
identity but no mechanically recognized positive X verdict, positive Y verdict, or positive-review
predicate. A negative memo is therefore sufficient review evidence under the stated executable
conditions. Git binds the tag to one tree, but the tree has not been positively confirmed.

This defeats the central release claim without breaking a hash, forging Kirill's signature, or
changing bytes after review. Supplying the missing acceptance semantics would change the
governing release and M4 predicates; it is not an implementation choice available under these
bytes. Because this is round 2, §8.3 fires. It cannot be repaired inside this charter-design
episode, and there is no v1.2 or silent continuation route.

## Surface findings

### 1. Release identity

The `C -> RX/RY -> L -> T` construction is acyclic and, for the surfaces it names, gives one
Git-bound byte identity. The signed annotated tag is token-only; no copied file or commit digest
is required in author material. Review-only diffs and `C`/`L` equality prevent a post-review
source, generator or contract substitution.

That sound object binding does not cure the decisive failure above: reachability proves which
bytes were presented, not that either external evaluation confirmed them. The release verifier's
described predicate accepts agreed negative evaluations. Thus there is one release object but no
mechanically established positive review of it.

### 2. Raw-byte provenance

For an unchanged, independently reviewed trust root, the original drift attacks are closed:

| Attack | Required failing mechanism |
|---|---|
| stale generated artifact or manual generated edit | in-memory rerender differs under `--check` |
| stale manifest, omitted member or extra member | raw recursive path-set equality and independent SHA-256 fail |
| altered source without manifest update | independently recomputed manifest digest fails |
| altered source with regenerated outputs | candidate bytes change and require a new full M4 review |
| alternate template or renderer | reviewed trust root changes; `G-TPL` and full M4 apply |
| supplied/expected hash substitution | independent recomputation and MF-4 fail |
| symlink or non-regular source | `G-PROV` and MF-6 fail |

There is nevertheless an internal digest-topology contradiction. Section 1.2(4) says “No digest
outside the manifest,” and §2.1(7) requires `G-PROV` to reject digest-shaped literals from every
live location except the manifest's canonical digest field. Section 4.5 simultaneously requires
`generated/CONTRACT.md` to contain the canonical route-vector digest, and §4.2 requires a copy of
that digest in M4 reviewer evidence. A conforming generated document therefore contains a
digest-shaped live value outside the manifest. If §2.1(7) is enforced literally, the mandated
output can never be green; if it is exempted, the stated one-exception topology is false. The
closure's claim that `G-STALE` is the only digest string outside `MANIFEST.json` is factually
inconsistent with governing §4.5, although the closure itself has no authority.

### 3. Manifest topology and archive status

The manifest itself is single, acyclic, excludes itself and all `generated/**`, and covers the
raw regular-file set under `contract/**` without an allowlist. Authoritative source, generated
documentation, the equivalence ledger and historical evidence are distinguished. The logical
archive leaves paths in place, records the old aggregate status as not accepted, rejects
`HISTORICAL_NONOPERATIVE` entries during live authority resolution, and states that archive
classification has no acceptance effect. On these terms, old acceptance prose cannot acquire
current authority and archive status cannot imply scientific acceptance.

### 4. Review provenance and `G-STALE`

In isolation, `G-STALE` is not a second release identity. It identifies the route vector, not the
accepted Git tree; it is reviewer evidence, lies outside author acceptance material, and is
recomputed at the tagged tree. A stale or substituted value makes release checking red.

It is not, however, the sole digest outside the manifest because §4.5 mandates the same class of
derived digest in generated `CONTRACT.md`. More importantly, the charter makes matching
`G-STALE` sufficient for the mechanical review-record portion of M4 while omitting review-verdict
polarity. In the counterexample it authenticates a calculation inside two rejecting reviews and
those reviews still satisfy the release gate. The digest does not itself become authority; the
gate mistakes matching reviewer evidence for positive reviewer acceptance.

### 5. Cardinality and budgets

`contract/**` physical lines, `contract/data/**` bytes, symlink refusal, the live-file count and
the generated/test separation are mechanically expressible and cannot be reset by renaming a
file inside the recursively counted authoritative tree. Counts are evaluated rather than copied.

The trusted-base and 400-line generator/template ledgers are not equivalently closed. They name
semantic components—schema, grammar, renderer, verifier and provenance gate—but specify neither
an exact recursive path set nor an import-closure rule for the counter. For example, emission or
verification logic can be split into a new helper imported by `render.py` while a counter over
the named files remains below both caps. The same logic can be placed in a new allowed
`tests/test_officina_contract_*.py` helper, which §7 declares uncapped, because no rule forbids
`tools/**` from importing test code or brings such an import into the trusted-base ledger.
Generated bytes can remain perfectly derived, so provenance and rerender checks stay green while
the authority-producing trusted program exceeds the intended budget. The prose characterization
that the helper is “really part of the renderer” is not a mechanical counter. Renaming and
splitting therefore remain a budget-reset attack.

### 6. Episode termination

The round rule correctly treats v1 X/Y as round 1 and this byte-identical X/Y confirmation as
round 2. Identical-byte parallel reviews remain one round; changed bytes, delayed resubmission,
renamed review labels, split/merged packages and substantially identical successors do not erase
the round count. A structural failure in this review therefore terminates the charter-design
episode with no v1.2.

The 21-day rule is not fully bound for this scope. Section 8.1 keys an episode and its UTC start
to the first M0 signed Git object, while §8.2 says M0 starts the separately named implementation
episode only after the charter-design rounds. The charter-design episode has no first M0 object
and no mechanically identified UTC start, so a pre-M0 delayed-submission attack cannot be tested
against its deadline. The round-2 trigger is sufficient to terminate this episode now, but the
claimed general non-resettable deadline is not mechanically defined for the episode undergoing
this review.

### 7. Authorization boundary

This review—positive or negative—does not sign or select T-1, T-2, T-3 or T-4. Only Kirill's
explicit token acts can make those choices. Confirmation alone would not authorize M0–M6,
dependency selection, code, data, entropy, installation, `T` activation, any `OR-3..OR-11` step,
spend, scientific action, claim movement or outcome. This structural-failure verdict authorizes
none of them.

## Final boundary

The negative-review counterexample leaves M4 and M5 falsely green and defeats the migration
architecture at its release boundary. Under the candidate's own round accounting this is the
second and final charter-design round. The structural-failure destination applies; no correction
text, v1.2, resubmission, implementation round or renamed continuation is authorized here.

I changed no file other than this review, created no code, data, entropy or artifact, and
authorized no M0–M6 work, token, installation, activation or outcome.
