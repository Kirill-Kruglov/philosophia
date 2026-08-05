# Officina P1 W-B v2.12 final Y review

**Reviewer:** GPT-5.6 Sol, independent Y line  
**Reviewed commit:** `9be51488f190f03e74f0633aa509274bba5adfab`  
**Review mode:** read-only adversarial review of closure §9 Q1-Q7. The closure
was treated as untrusted. W-B was treated as signed and not reopened.

## Verdict

```text
REVISE_OFFICINA_P1_WB_V2_12
```

The original Y counterexample is repaired for every requested signed-value
permutation, and the reported 67/81/75 censuses and pinned Cell-2 bytes
recompute. Acceptance is nevertheless blocked by demonstrated Major
fail-closed, identifiability, quarantine and authority defects: `KG-1` accepts
shifted malformed stat fields; `§P1-10.3` remains behaviorally ambiguous on an
ordinary Linux state character; malformed/stale classifier cases do not have a
single governing result; and the transformation pins only Cell 2 while leaving
the other body-branch output bytes under-specified. `PO-9`'s exact literals also
do not establish its claimed semantic false-negative boundary.

## Input, commit and scope verification

All six task-pinned inputs recomputed to the supplied SHA-256 values. The live
worktree was at descendant `bd52991b2b65ab55fc50ede711d747112bd7f5b4c`, not at
the requested commit, but `git diff 9be5148 -- <the six inputs>` was empty; the
review therefore used the exact `9be5148` input bytes. Pre-existing unrelated
dirty and untracked paths were neither used as authority nor modified.

Commit `9be5148` actually creates seven files, not the closure's claimed six:
the six declared artifacts plus
`reviews/opus5_officina_p1_wb_v2_12_governing_repair_chat_response.md`. That
undeclared seventh file is non-governing, but it repeats the previous round's
scope-accounting error and makes closure §2.2 false.

The two extracted cross-file regions are byte-identical:

```text
H_HANDOFF  a03cb516958052109a860f461e7777916b4185ff1cd1deedeb0d3d955c343a66
           4166 UTF-8 bytes
H_JOINT    6b0e64e0bd4f56c6c2b6a748808944221125ced2d482d8684c7566461584a2f7
           223250 UTF-8 bytes
```

Composite regions also recompute:

```text
H_BODY       d5125d54e312fd87fff7c622cedf8538ef2ea99c9666ec619becfd2e4651a1e6
H_GUARDDATA  faf2d709cb711baca148c98eb36dccd06efdf716a2682d6d7611dc80fe540426
H_NORMATIVE  0d3b411e6f92c37f759025d71af6fa59d7b648a0106869829c30c1917b490d66
H_FILE       e796d9e8838b160cc76a3c14814881ac38a0b2a6568ee3103c1286334e5f729b
```

## Demonstrated Major blockers

### M-1 — `KG-1`'s positional tokenizer accepts the malformed integer forms it says it refuses

On the local Linux 7.0.0 x86_64 host, the executable G0..G5 reading of the real
`/proc/<pid>/stat` buffer returned `PRESENT_VALID`; the observed state was `R`,
and the ordinary field positions were read correctly. The named simple
malformations also refused as claimed: no final `)`, fewer than twenty tokens,
wrong-length or out-of-set state, a directly signed integer, a directly
overflowing integer, and `pgrp == 0`.

The whitespace and separator claims are false, however. G0 splits the entire
suffix into tokens and requires only *at least* twenty. It does not establish
field framing. Starting from an ordinary-shaped synthetic suffix with state
`R`, `ppid=12`, `pgrp=345` and enough later numeric fields:

```text
baseline                       PRESENT_VALID(ppid=12,    pgrp=345, start=20)
ppid rendered as "1 2"         PRESENT_VALID(ppid=1,     pgrp=2,   start=19)
pgrp rendered as "3 45"        PRESENT_VALID(ppid=12,    pgrp=3,   start=19)
separator removed between
  ppid and pgrp                PRESENT_VALID(ppid=12345, pgrp=4,   start=21)
```

The added or removed separator shifts every later token; G3, G4 and G5 then
validate the wrong numeric fields. This directly contradicts G0's claim that no
extra or missing separator is absorbed silently and row 89's required refusal
of whitespace-bearing integers. It is a Major fail-closed group-identification
defect because `PRESENT_VALID` can carry a `pgrp` that was not the stat pgrp
field at all.

### M-2 — `§P1-10.3` has two executable results for one ordinary Linux line

The unchanged rule says to parse start time "together with the state field and
the ppid field" and then says "a non-integer field" is `UNPARSABLE`. On the
same real stat line whose state token was `R`:

```text
reading A: "non-integer field" means the two numeric fields
           => PRESENT_VALID
reading B: it means every named field, including state
           => UNPARSABLE because R is not an integer
```

Both readings follow the bytes. They alter every existing `STAT_OBSERVE`
consumer, including whether a start identity can be captured and whether a
durable identity-bearing record can be built. `KG-1`'s local grammar does not
repair those consumers. This is the same executable identifiability shape as
the prior `KG-1` defect, knowingly retained in the live composite, and it is a
this-round Major blocker rather than deferred work.

### M-3 — malformed/stale precedence is contradictory and `KV_FORBIDDEN_TARGET` is not single-valued

The stable original counterexample is repaired, but the literal Q1 asks more.
For one current-generation entry carrying a protected `pgid_or_null` and a
malformed signed-set value such as `state = MALFORMED`:

```text
P0-4/group-test first       => KV_FORBIDDEN_TARGET
SC-8/structural-test first  => STRUCTURAL_VIOLATION
```

`SC-6` says the two are equally terminal and "whichever ... fires first" wins,
while simultaneously claiming total, single-valued dominance by
`KV_FORBIDDEN_TARGET`. No ordering between these applicable tests is supplied.
Both routes send zero signals, but the journal token and classifier accounting
are not identifiable.

There is also an executable stale/malformed contradiction. A stale-generation
entry with malformed `role` or `pgid_or_null`, plus a valid unprotected current
candidate, is excluded from P0 by P0-3/P0-5 and stops at `KV-1` in P1 with
`KV_STALE_HANDLE`; the valid candidate can proceed to signals. Row 89 and
`SC-8` instead require every malformed `role`, `generation_id` or
`pgid_or_null` to take the structural-violation terminal. The composite thus
requires both a skip-and-proceed and a terminate-with-no-signal answer for the
same table. This is a Major fail-closed/accounting identifiability defect.

### M-4 — the post-selection composite bytes remain under-specified outside Cell 2

Binding §2.2.1-§2.2.3 successfully pins one Cell-2 source span and one
replacement block. It does not pin the other sixteen body marker loci. For
those loci §2.3 still says only "retain the W-B text inline, without its marker,
and delete the W-A text"; OR-4 is equally semantic. No byte range, deletion
boundary, whitespace rule, whole resolved-file digest, or full resolved byte
block is supplied.

For a both-marker line such as composite line 2959, deleting the W-A clause and
the two marker tokens can leave one, two, or three of the spaces adjacent to
the deleted spans. Each output retains exactly the W-B sentence, deletes the
W-A sentence and markers, and normalizes identically under every stated PO
check, yet the outputs differ byte-for-byte. The exact Cell-2 splice therefore
does not make the complete OR-4 transformation identifiable.

`PO-9`'s arrays are now literal and their serializations are correct, but their
semantic quarantine claim is also too broad. This marker-free rejected grant
normalizes to zero `D1` and zero `D2` matches:

```text
The watchdog is permitted a socket in descriptor slot 6 and may send one fixed
freeze command; acceptance causes the PCS to invoke its group-freeze routine
during a time-limited service period.
```

It restores the W-A slot-6 socket, request/frame, acceptance-driven trigger and
bounded service window in different words. All 11 literal D1 self-carriers and
all 13 literal D2 self-carriers were detected, but that proves exact-literal
coverage, not zero false negatives for forbidden grants. This is a Major byte
identifiability and quarantine defect in the proposed oracle boundary.

### M-5 — the two purported live authority surfaces identify themselves as their predecessors

The amendment path and operative clauses call the document v1.9, but its title
says "version 1.8", its first paragraph says it wholly replaces v1.7 rather
than v1.8, and it says the eight predecessors become provenance rather than the
nine versions 1 through 1.8. The composite path and live clauses call it v1.12,
but its title says "version 1.11" and line 50 attributes this version's
identity boundary to Version 1.11. The same composite's mixed-generation test
then requires v1.9 plus composite v1.11 to be refused.

These are not historical quotations: they are the titles and opening authority
statements of the new live files. A pair cannot be accepted as the unique
v1.9/v1.12 authority while its own governing bytes identify both members as
the superseded generation. This is a Major authority-identification defect.

## Literal answers to closure §9 Q1-Q7

**Q1 — NO.** P0/P1 prevents the original current-generation ownership skip,
but `KV_FORBIDDEN_TARGET` does not dominate `SC-8`: the contract expressly
makes them equal and gives no precedence for an entry that is both malformed
and protected. Stale+malformed entries also produce the contradictory
P0-5/KV-1 skip versus row-89/SC-8 terminal described in M-3. Current malformed
`SPAWNING_GROUP.json` and non-`PRESENT_VALID` observations otherwise have
closed branches, and collect-before-act closes late discovery during the full
P1 scan.

**Q2 — YES for the original Y counterexample and every requested signed-value
permutation.** I executed the cross-product of 5 positions, 3 roles, 4 states,
3 ownership values and 4 protected values: 720/720 produced
`KV_FORBIDDEN_TARGET` and exactly zero signals. The protected-only table added
144/144 zero-signal results. Both two-entry orders across all four protected
values added 8/8 zero-signal results. This passing subcheck does not cure Q1's
malformed/stale contradictions.

**Q3 — NO.** G0..G5 accepts the real Linux stat structure and rejects the
simple named malformed cases, and the observed `R` lies in G1's nine-byte set.
But inserted and removed separators shift positional fields and still return
`PRESENT_VALID`, as M-1 demonstrates. The platform predicate admits Linux
x86_64 without pinning kernel 5.x/6.x, so G1's provenance statement is also
narrower than the actual supported-platform clause; an unknown future state is
fail-closed, but the claimed exact provenance is not established for every
admitted kernel.

**Q4 — NO overall.** The source-trace split is materially more honest. The
genuinely existing content is limited to: existence of `pgid_or_null`, the
requirement that `_killpg` use a kernel-verified group, and bootstrap's
verification/recording of the supervisor group. `P-1` through `P-7`, G1/G2/G4,
and SC-9/SC-10 are correctly labelled new normative supporting content, not
derived content. No `_getpgid` binding or allowlist expansion was found.

The claimed total path table is still incomplete. `P-7` lists the five normal
`PGRP_OBSERVE` outcomes but not a wrong-shaped return or a non-`OSError`
`BaseException` from `_open`, `_read` or `_close` during KG-2 population;
`SC-8` supplies a classifier-phase continuation but P-2 population occurs at
the post-creation write site and P-7 supplies no corresponding population-path
result. Nor is the retry/population attempt attached to a concrete
`SPAWN_ROLE`, `SPAWN_WATCHDOG` or `AWAIT_STOP` step. The malformed-token
acceptance in M-1 independently makes the legitimate-population claim false.

**Q5 — NO.** The exact checks that pass are:

```text
source span       41 lines, 2184 bytes,
                  1623dc45bb5c17c507ca590c3d6ca2a171ed7e40e5c4f287a8a736ee860db2b8
replacement       37 lines, 2120 bytes, final LF,
                  f2782a63db003dfb370d0c0c5afb9c928a8fc61c8af29285c8a1172657a84fee
D1                11 literals, CANON 926 bytes,
                  d5b375c518c935d3a6935a1932bf6bfa237cb9c99c7b81913f4e1433142b6c1e
D2                13 literals, CANON 1044 bytes,
                  4e2120857dd67124095e5f5479d69cbf7ba703605abb3448a2fe414b3ff8a15c
```

Both source sentinels occur once and the splice is deterministic for Cell 2.
The remaining body resolution is not byte-deterministic, and the executable
marker-free W-A paraphrase in M-4 is a D1/D2 false negative. Therefore neither
the unique complete output nor the claimed zero-false-negative boundary holds.

**Q6 — MUST BE REPAIRED IN THIS ROUND.** The real `R` state counterexample in
M-2 yields `PRESENT_VALID` under the natural reading and `UNPARSABLE` under the
strict reading. Because §P1-10.3 is a live governing observer used outside the
self-contained KG-1 classifier, knowingly leaving it ambiguous blocks
acceptance of this pair. It cannot be deferred as unrelated maintenance.

**Q7 — NO overall.** The core censuses do recompute exactly:

```text
MS-2              67 rows, 67 distinct paths
MS-3               7 rows, 7 distinct paths
M1..M7 total       2+67+7+1+1+2+1 = 81
PROVENANCE         75 digest/path rows, 75 distinct paths
```

`N-16` now says 81; H-4 correctly assigns `HISTORICAL_BYTE_MOVED` to CK-7;
row 106 says ten groups; CK-13 and row 107 say 82nd entry; the Cell-2 v1.2
phrase and §A9 line-number locator are repaired. But composite row 108 still
says a members array of any length other than **77** is structural, conflicting
with `MS-8`, `CK-6`, row 105 and its own 81/82 setup. In addition, the live-file
version identifiers in M-5 are stale, and commit `9be5148` contains the
undeclared seventh chat-response file. The closure's claim that every dependent
literal moved and no seventh file exists is false.

## Minor log items

1. Row 108's stale `77` does not make its particular 82-entry fixture pass,
   because the governing CK-6 rule still requires 81; independently of the
   broader blockers, the stale explanation must be corrected to 81.
2. The undeclared seventh commit file is non-governing and does not itself add
   authority, but the exact-file-list accounting must stop claiming six.
3. The state-set provenance should be phrased against the actual platform
   predicate or that predicate should pin the reviewed kernel family.

## Exact next boundary

The next act is a new bounded governing/binding repair. It must make stat-field
framing executable, repair §P1-10.3, give malformed/stale/protected states one
ordered result, totalize KG-2's population paths, pin the complete resolved
composite bytes or a complete byte algorithm, make the claimed quarantine
boundary no broader than its executable detector, correct the live generation
identities and stale row-108 count, and account for the actual commit file set.
Both independent lines must then review the same new bytes.

This review authorizes no consideration of amendment v1.9, no scaffold, no
implementation, no key or entropy, no Stage A or Stage B, no `OR-3` through
`OR-11`, no install, no activation, no identity weakening, and no programme-
claim movement. `OR-2` alone remains complete; `T = NOT_ACTIVATED`; programme
claim `OPEN`.
