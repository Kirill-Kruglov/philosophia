# Officina P1 W-B v2.14 — final bounded independent Y review

**Reviewer:** GPT-5.6 Sol, independent Y line  
**Review date:** 2026-08-06  
**Verdict:** `REVISE_OFFICINA_P1_WB_V2_14`

## 1. Byte basis and scope

I recomputed the six pinned SHA-256 values before analysis. All six match:

```text
3571c1f75283851e4cf1a9b04dfe67c2f35d9c52392e6b97582274195b475cf7  successor/OFFICINA_P1_WATCHDOG_FREEZE_AUTHOR_CHOICE_PACKET_V2_14_CORRECTION.md
5f2c74ff371f618039de705f21464454684da122f91e06c251e147bfc61d26be  successor/OFFICINA_GENERIC_HARNESS_WATCHDOG_FREEZE_AUTHORITY_AMENDMENT_V1_11_DRAFT.md
11c8963ac3cbd4c72a90b0a1f0fdc0fe3bfb35be84a974c3a2a953ec699bbdee  successor/OFFICINA_GENERIC_HARNESS_SUPERVISOR_CONTROL_CHANNEL_P1_OPERATIVE_COMPOSITE_V1_14.md
0b08bd3e5e49666dddb475c1e282589a0c1d940221bdebf7ca132a860d4564f1  successor/OFFICINA_P1_WB_POST_SELECTION_BINDING_V5_DRAFT.md
9b07b718a6f5de7c27d05bec6a205813329255b8b344adfe0447338357814a77  successor/OFFICINA_P1_WB_IMPLEMENTATION_HANDOFF_V5_DRAFT.md
b981a88e724c493f2d84d1a92d448394ce21f931e5584fe8f49690b0158b9f92  reviews/opus5_officina_p1_wb_v2_14_governing_repair_closure.md
```

The repair commit `cb3780814f407166499a0b34ce6b85913a08994e` is the parent of the current
prompt-only `HEAD` commit. The six reviewed artifacts are unchanged from the repair
commit and match the pinned bytes, so this did not block the byte review. I treated
the authored closure as untrusted and did not use dirty code/test/runtime paths as
authority.

## 2. Findings by severity

### Major Y14-M1 — KG-2 still permits a second write and makes P-9/P-10 overlap

The ordinary first-evaluation routes are repaired, but the exact `K1`..`K6`
machine is not total and disjoint once the expressly required retry states are
included.

Counterexample A, reissue after a successful write:

```text
starting state       H-GROUP-RECORDED from an earlier successful P-2 write
operation            a later AWAIT_STOP evaluation, expressly covered by P-3/P-10
outcome              STOPPED
K4 observation       PRESENT_VALID
identity             matches
pgrp                 equals h.pid
```

`P-2 K5` says the write occurs **if and only if** its three observation
conjuncts hold, and explicitly says the complete population predicate has only
the four conjuncts `outcome == STOPPED`, PRESENT_VALID, identity match and
`pgrp == pid`. `P-9` consequently assigns `THE ONE WRITE`. But `P-3` says every
evaluation after the successful write performs no write, and `P-10`'s reissue
row says `NO SECOND WRITE`. The exact `K1`..`K6` sequence has no
`pgid_or_null is NULL`/`not previously written` guard that could select the
second answer without violating K5's `if and only if`. This route is described
by both P-9 (every STOPPED K4 route) and P-10 (reissue after successful write),
with contradictory write results. A conforming implementation cannot choose
between a forbidden second write and an unstated extra K5 conjunct.

Counterexample B, current-generation invalidation after observation:

```text
starting state       H-NULL-GROUP, no prior write
outcome              STOPPED
K4 observation       PRESENT_VALID, identity matches, pgrp == h.pid
event                 generation invalidates after K4 and before K5 lands
```

`P-2 K5` again mandates the write from the exhaustive four-conjunct predicate.
`P-10`'s mid-attempt invalidation row says `no write lands`. No generation-valid
recheck appears in K1..K6 or in the exhaustive population predicate. This is a
second double-valued route.

The interruption rows also disprove the literal assertion that the two tables
never overlap: P-10 places `EINTR during the K4 read` inside the STOPPED route,
and maps deadline exhaustion directly to P-9's ERROR row. That procedural
overlap is not by itself harmful when a retry later resolves, but it confirms
that P-9/P-10 are not the claimed disjoint partition.

This is an executable transition-authority and double-write defect. The smallest
repair is to put an explicit already-written/current-generation decision into
the pinned sequence before K4/K5, state its outcome and observation behavior,
and make P-9 and P-10 predicates genuinely disjoint. Merely repeating P-3/P-5
does not resolve K5's unconditional `if and only if`.

### Major Y14-M2 — the pinned v5 handoff still delegates authority to v4/v1.13

The generation-name/dependent-literal sweep fails in the pinned implementation
handoff:

- line 76 says to read the handoff with
  `OFFICINA_P1_WB_POST_SELECTION_BINDING_V4_DRAFT.md`, and says the binding
  governs on disagreement. The current transformation is binding v5; v4 carries
  the superseded v1.13 transform figures.
- lines 90 and 194 name
  `OFFICINA_GENERIC_HARNESS_SUPERVISOR_CONTROL_CHANNEL_P1_OPERATIVE_COMPOSITE_V1_13.md`
  as the behavior source/frozen governing file. At line 91, that v1.13 path is
  paired with the v1.14 digest `11c8963a...9bbdee`; the actual v1.13 digest is
  `15e11f0e...8fb3`.

These are not historical citations. `§H1 R-1` says these are the **only**
documents opened for behavior, and `§H2.2` repeats the frozen governing path.
An implementer following the handoff either fails its own path/digest identity
check or opens the superseded governing composite; the v4 precedence sentence
also directs it to superseded transform authority. This is an executable
authority/provenance defect in a pinned current document.

### Major Y14-M3 — handoff D-6 requires the valid 89-member enumeration to fail

Handoff `D-6` first fixes `total 89` and `TS-3 member_count 89`, then requires a
dummy negative test under which `63, 69, 73, 77, 81 or 89 FAILS`. Binding v5
`PR-4` instead correctly requires `63, 69, 73, 77, 81, 85 or 93` to fail, and
handoff `T-14` repeats that correct list. Thus the current 89-member enumeration
is simultaneously the mandatory value and a mandatory failure. This is a live
accounting/test contradiction, not a historical mention.

### Minor Y14-L1 — the non-normative provenance narrative names the wrong review generation

Composite §P1-18 says the four new rows include the two final reviews of the
`v2.12` pair. The literal rows are the two v2.13 reviews, and normative `MS-2`
correctly calls them v2.13. Because §P1-18 is explicitly non-normative and is
not read for behavior or membership, this is editorial rather than a Major.

No Critical finding was found.

## 3. Y-Q1 — independent KG-2 enumeration

I enumerated the cross-product of:

```text
outcome             STOPPED, EXITED, TIMEOUT, and no outcome determined
KG-1 result          PRESENT_VALID, ABSENT, UNREADABLE, UNPARSABLE, ERROR,
                    PRIMITIVE_FAULT
identity             match, mismatch
group relation       pgrp == pid, pgrp != pid
K4 read              clean, EINTR then resolution, EINTR through deadline
prior write          absent, present
generation event     none, before outcome, after outcome/before K4,
                    after K4/before K5
```

Combinations whose later dimensions are unreachable were short-circuited at the
first applicable K step rather than treated as observations.

For an unwritten, current-generation handle, the basic terminal table is
single-valued: non-STOPPED/no-outcome routes take no KG-1 observation and no
write; the five non-PRESENT_VALID KG-1 classes write nothing; PRESENT_VALID plus
identity mismatch contradicts ownership; identity match plus non-leader writes
nothing; and identity match plus leader performs the first write. EINTR retry
writes nothing during retry, and exhaustion reaches ERROR with no write.

`K1`..`K3` do successfully forbid every observation and write before
`outcome == STOPPED`. The ordinary live-leader TIMEOUT therefore has exactly one
result: no observation, no write, `H-NULL-GROUP`, `pgid_is_leader = 0`, not
group-signalable.

The full enumeration nevertheless fails for the two concrete states in
Y14-M1. It found P-9/P-10 overlaps and contradictory write authority, including
a route that makes a second write unless an unstated K5 guard is invented. I
found no separate unknown-provenance route and no pre-outcome observation route.

**Y-Q1 result: FAIL (Major Y14-M1).**

## 4. Y-Q2 — primitive closure and generation accounting

### Primitive closure

The v2.13 primitive dead end itself is repaired. Tracing `c1..c18` and `m0..m9`
finds a bound supplier for every mandatory primitive operation. In particular:

- §P1-3.4 binds `_getsid` and `_getpgid` from `os` in the exact binding block;
- `c10` uses `_getsid(middle_child_pid)` and
  `_getpgid(middle_child_pid)`, `c14` uses
  `_getpgid(supervisor_pid)`, and `m3` uses `_getsid(0)` and `_getpgid(0)`;
- only literal `0` and a verified positive-pid Name are admissible arguments;
- only plain `int` results in `1..2147483647` are accepted; `bool`, non-int,
  zero, negative and overflow results take PRIMITIVE_FAULT;
- ESRCH, EPERM and every other OSError take the site's fail-closed route with no
  retry/default/match; a non-OSError BaseException takes the structural-violation
  continuation;
- the only behavioral call sites are `c10`, `c14` and `m3`. Neither binding is
  consumed by KG-1/KG-2, KV/SC, the classifier or a signalling path.

`S-3` remains exact-list equality (`exactly the list ... in that order`), not a
minimum or superset rule. `S-5`, `S-6` and `S-7` still prevent module-attribute,
indirect and dynamic escape routes. The added names are attributes of an already
allowed module, so they add no import-closure row and do not widen the import
allowlists.

### Accounting, provenance and dependent literals

Independent recount from the literal lists gives:

```text
MS-2                         75 rows, 75 distinct paths, 75 distinct digests
MS-3                          7 rows,  7 distinct paths
MS-2 intersection MS-3       empty
MS-8                          2 + 75 + 7 + 1 + 1 + 2 + 1 = 89
provenance region            83 distinct paths
provenance relation          MS-2 union MS-3 union verifier baseline
recorded M2+M3 digests       82
```

I recomputed all 82 recorded M2/M3 digests from the named disk files: all 82
match. The joint install/authorization spans are byte-identical. The amendment
has exactly one anchor line; its value is the v1.14 composite's actual whole-file
digest `11c8963a...9bbdee`. Every complete anchor-token occurrence in both
governing files carries generation 14. The operative OR-4 sentence says exactly
once in each byte-identical joint block that the v1.11 amendment is installed.

The retired-cardinal sweep over `57, 67, 71, 74, 75, 77, 78, 79, 81, 85`
finds no stale live cardinal in the composite. Rows 103..115 use current counts;
row 105 requires 89, and row 106 builds/restores all 89 current-generation
members. Their two `81` literals are explicit descriptions of the v1.13 defect,
not live rules. The remaining retired values are row indices, test-row numbers,
the constant `67_108_864`, current values, or explicit history.

The dependent-literal sweep does fail outside the governing pair at the pinned
handoff, as Y14-M2 and Y14-M3 demonstrate. Therefore the primitive repair and
normative 89-member recount pass, but Y-Q2 as asked over all pinned dependent
literals does not.

**Y-Q2 result: FAIL (Majors Y14-M2 and Y14-M3; Minor Y14-L1).**

## 5. Regression boundary

The four v2.13 Y counterexamples themselves now each have one intended result:

- **Y-M1:** SC-10 reduces the Phase-4/Phase-6 structural-plus-protected collision
  to T1 in either table order, with no signal.
- **Y-M2:** the ordinary live-leader TIMEOUT takes no observation and no write,
  remains `H-NULL-GROUP`, and returns `pgid_is_leader = 0`.
- **Y-M3:** rows 105 and 106 both use the current 89-member value; surviving 81s
  there are explicit history.
- **Y-M4:** `_getsid` and `_getpgid` are bound, genuine-primitive checked,
  reachable through local names, and fail closed.

The repairs do not alter the selected identity Option A, XS-1, the signed W-B
choice, the scientific boundary or activation. XS-1 is byte-identical between
v1.13 and v1.14; Cell 1 changes only required generation self-references outside
its operative identity clauses; `attested_pid` and `attested_pgid` occur zero
times in both governing files. W-B remains selected and signed, the bounded
weakening remains unaccepted, no scientific claim moves, `T = NOT_ACTIVATED`,
and the programme claim remains `OPEN`.

The known duplicated closure §12 paragraph is non-normative and is not a
finding.

## 6. Exact next boundary

This review does **not** permit Kirill to consider
`I_ACCEPT_OFFICINA_GENERIC_HARNESS_WATCHDOG_FREEZE_AUTHORITY_AMENDMENT_V1_11`.
A new bounded repair generation may address only the demonstrated executable
transition, handoff-authority and handoff-accounting defects above (and may clean
the Minor without extending the loop), followed by fresh independent review of
the newly pinned bytes.

Nothing here authorizes code, scaffold, key, entropy, seed, Stage A, Stage B,
signature, manifest, attestation, member list, install record, OR step, install
or activation. Identity Option A and signed W-B are not reopened.

```text
T = NOT_ACTIVATED
PROGRAMME CLAIM = OPEN
REVISE_OFFICINA_P1_WB_V2_14
```
