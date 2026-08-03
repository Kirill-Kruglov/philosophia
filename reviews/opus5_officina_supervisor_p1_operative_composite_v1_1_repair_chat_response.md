All three defects need mechanical confirmation before I rewrite. Checking R1 first.

R1 confirmed exactly: the body truncated at line 1707, excluding lines 1708–2012 — most of §C13, **all 80 test rows**, and §C15. Gathering the literal values I need.

All three defects mechanically confirmed. Writing the full replacement.

Now the mechanical audit. Sentinel cardinality and order first:

Exactly six, one each, correct order. Now confirm no sentinel string occurs anywhere else, even as a substring:

R1 closed — no collision possible. Now the byte-level placeholder audit over both normative regions:

One hit. Locating it:

False positive — the substring sits inside "whatever it **was before**". I'll reword it so a naive substring search also returns zero, leaving no judgement call for a reviewer:

Now a broader scan for any remaining delegation of content, including within-document ones:

Five genuine delegations remain. Literalizing each:

Re-running the full audit on the corrected file:

The remaining hit is a literal comparison predicate, not a delegation. One structural gap to close first — the region scheme sits in the preamble, outside all three regions, so it is pinned only by the whole-file digest. Making that explicit and putting the operative rule under `H_BODY`:

Now the body-region restatement, so the operative rule is under `H_BODY`:

Now the definitive audit and digest computation on the final bytes:

Guard `G-4` self-fires once. Locating:

The guard rule's own prose in `BODY` contains the phrase it forbids — the R1 failure mode in a new dress. Fixing the wording and adding a standing constraint so it can't be reintroduced:

Re-running the complete audit on the corrected bytes:

Zero. Final placeholder audit and digest computation:

Confirming the R1 truncation class is closed — every section that v1 lost is inside the digested region:

All checks pass. Writing the closure:

Final verification — digests still current, and no existing file touched:

Both deliverables are in place and every claim in the closure is mechanically backed.

## R1 — marker collision: closed

v1's `NORMATIVE_BODY` terminated at the **example** END on line 1707, digesting 1 663 of 2 117 lines and silently excluding lines 1708–2012: most of §C13, all 80 test rows of §C14, and all of §C15.

v1.1 defines its six sentinels by an **exact byte-construction rule** (`FRAG_OPEN + FRAG_SP + FRAG_TAG + …`) so no literal sentinel line is ever written inside a normative region — an example can no longer collide because no example spells one. Verified on final bytes: each of the six occurs **exactly once as a substring anywhere in the file**, in correct order. `G-8` checks cardinality and order before any digest; `G-9` requires the verifier's own fragment constants to match. Every previously-truncated section is now interior to `BODY` (§P1-13 at 1949, §P1-15 at 2298 with 85 rows, §P1-16 at 2399; `BODY` ends 2413).

## R2 — placeholders: closed, zero shown with its domain

Domain: `REGION(BODY) || REGION(GUARDDATA)` — 2 318 lines, 138 527 bytes, matching `H_NORMATIVE`. Method: case-insensitive literal-substring occurrence counts. `unchanged` 0, `carried` 0, `as before` 0, `same as` 0, `preserved` 0, `signed adapter` 0, `signed record` 0, plus 18 further patterns all 0.

One occurrence survives and I report rather than suppress it: `identical to`, at §P1-11.1 P2a — "byte-identical to what this attempt would install", a literal comparison predicate, not a delegation.

The audit also caught five genuine *within-document* delegations a token search would miss (`SIGNAL_GROUP`'s "as above", `ACKED ⇒ identical to COMPLETED`, the `S-5` structural row, I-7/I-8, and the watchdog descriptor row). All five were literalized. All eight commissioned loci are literal.

## R3 — verifier input authority: closed

Guard patterns now occupy their own `GUARDDATA` region, labelled normative verifier data, with their own digest enforced by `G-6`.

**One defect I found in my own draft:** the first self-fire scan showed `G-4`'s pattern `cannot gain process authority` occurring in `BODY` — inside §P1-14.3's own prose describing the rule forbidding it. The R1 failure mode in a new dress. Fixed by rewording `G-4` and adding `G-10`, which forbids reproducing any pattern in the body **including in self-description**, with no exemption (an exemption would be an exclusion list). All thirty patterns now return **TOTAL GUARD FIRES: 0**.

## Digests

```
H_FILE       90ddf3ff76a1d08994c06d9c7f938e45f32fdeb46f58251ebb162bc96cf01680
H_BODY       aff3d4eea1105f3f9572379c53a27673486a6bd263c3c23810f16be9f1b7391c
H_GUARDDATA  0d3131b4a319d0bf03310e203485320253b671501ec44f87d67e8d47f8616733
H_NORMATIVE  03536a6b72d5d9326d2b646329c295d3ee4c3a3447a49106a252932b8597622b
```

No self-hash cycle — v1.1 contains none of its own digests.

## No `BLOCKED_` verdict

No conflict between signed contracts surfaced; every literalization transcribed a value the signed chain had already fixed. I invented no constant and chose nothing on Kirill's behalf. The one place a choice could have hidden — the region-scheme preamble sits outside all three regions, so it is covered by `H_FILE` but not `H_BODY` — I did not resolve silently: it is stated explicitly, restated inside `BODY` as §P1-14.0, and backed by `G-9`.

Verdict line 1 of the closure is `READY_FOR_OFFICINA_SUPERVISOR_P1_OPERATIVE_COMPOSITE_V1_1_XY_REVIEW`, with §8 listing where I judge my own work weakest — the substring audit is not a semantic proof, `G-10` is discipline not mechanism, and §P1-13's peer boundary is my reading and needs a Y-line holder of the peer contracts to confirm it partitions cleanly.

`T` remains `NOT_ACTIVATED`; the programme claim remains `OPEN`.

Two notes on repository state: only read-only commands ran (`grep`, `sed`, `wc`, `sort`, `uniq`, `tr`, `sha256sum`). I created exactly the two commissioned files and edited no pre-existing file — the additional `M`/`??` entries in `git status` for `*_chat_response.md` are written by the session's own transcript tooling, not by me.
