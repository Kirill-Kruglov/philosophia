I'll begin by recomputing the governing hashes and examining the files. Let me start with the independent verification.

Current HEAD is `1c6bc56`, but I must review `1731811`. Let me recompute hashes against the committed blobs at that commit, not the working tree.

All five hashes match exactly. Since HEAD ≠ 1731811, I'll extract the committed blobs into scratchpad to work against the exact reviewed state.

No working-tree drift on the three governing files. Now let me read the closure (untrusted self-assessment) and the prior X review to understand the claims I must independently recompute.

Now let me read the prior X v2.8 confirmation to anchor what MS-11.1 must match, then start independent recomputation.

This is the final confirmation of the exact v2.8 blocking fix. Let me set up a task list and check whether my host matches the pinned build so I can reconstruct MS-11.1 independently.

Host matches the pinned build exactly (`3.12.3 (main, Jun 19 2026, 12:46:00) [GCC 13.3.0]`, x86_64), and `_datetime` is builtin. I can reconstruct MS-11.1 on the exact interpreter. Let me locate the key sections in the composite.

MS-11.3 now reads "SEVEN" (line 3744). Let me read the MS-11.1 canonical value and the three scoped allowlists so I can reconstruct independently.

I have the full MS-11.1 table. Let me get the exact canonical object shape (field names / ordering) and MS-0 rules, then reconstruct the digest independently on this pinned interpreter.

I have the canonical shape and MS-0 rules. Now let me reconstruct the digest independently. I'll parse the MS-11.1 literal table and build the canonical JSON, and separately reconstruct residency+kinds from the pinned interpreter. Let me write the parser/reconstruction script.

The MS-11.1 table recomputes to length 20534 and digest `aa974e0c…dc20ee` exactly — internal consistency confirmed. Now the factual-independence prong: reconstruct residency, kinds, and edges directly from the pinned interpreter (importing no production module).

My generic alias-detection over-collapsed `_collections_abc`/`collections.abc`. Let me investigate the actual module identities before fixing the normalization.

Now clear: `_collections_abc.__name__` is misleadingly `'collections.abc'` but its `__spec__.name` is correct, and it's a distinct object. The three true aliases are the shared-id groups. Let me fix the normalization to use `__spec__.name` and dedupe by object identity.

Interpreter residency independently yields exactly **89 modules** with exactly the claimed kind counts (BUILTIN 29 / FROZEN 13 / EXTENSION 2 / PURE_PYTHON 45). My static edge parser under-counts some transitive edges (18873 vs 20534) — expected, since exact edge reconstruction needs full fromlist/submodule handling. Let me instead (a) confirm the 89 module names match the literal, and (b) confirm MS-11.1 is byte-identical to the v2.8-confirmed value, which is the operative question for this bounded round.

The 89 interpreter-derived module names are **identical** to the literal, with **zero kind mismatches** — residency and kinds factually confirmed. Now let me verify the MS-11.1 table is byte-identical between v1.8 (v2.8-confirmed) and v1.9.

MS-11.1 is **byte-identical** between v1.8 and v1.9 (sha `8c97e086…`, 188 lines) — the frozen value is carried forward untouched and recomputes exactly. **Q2 confirmed.**

Now Q3: the seven-branch inventory. Let me read MS-11.3's branch section and packet §2.5, and verify each branch factually.

MS-11.3 lists seven branches with `datetime → _pydatetime` explicitly added as the seventh v1.6 correction. Let me factually enumerate all non-resident module-scope import targets across the 89 loaded code objects to confirm the branch set is exactly these seven and nothing else was missed.

Six of seven branch groups confirmed (os→nt, os→ntpath resident-via-pathlib, ntpath→{nt,_winapi}, abc→_py_abc, hashlib→logging, datetime→_pydatetime). The `_frozen_importlib_external → nt, winreg` row didn't surface — my frozen-module code parse likely returned None. Let me check that specific module directly.

get_code fails because `__name__` is rebound to the alias. Let me fetch the frozen code object by its true frozen name and parse module-scope imports.

`_frozen_importlib_external` has module-scope IMPORT_NAME of `nt` and `winreg` (unexecuted Windows-only) — my earlier script only missed it because get_code failed on the frozen alias. So the complete unexecuted-branch set is exactly the **seven** groups MS-11.3 lists, and `datetime → _pydatetime` is the seventh. **Q3 confirmed.** Now let me read MS-13, packet §2.5, and verify the four project modules statically.

Let me read MS-13 in full and then the packet §2.5 section.

MS-13 is fully specified. Now let me verify Q4 statically: recompute the four digests from the committed blobs at 1731811, and parse each file's AST for module-scope imports, execution order, and module-scope calls — importing/executing/compiling nothing.

All four digests match MS-13 exactly. Now let me parse each file's AST for module-scope imports (project vs stdlib), and module-scope calls, without importing/executing.

The AST audit matches MS-13 exactly on all four modules — digests, project-import edges and order, stdlib seeds, and module-scope calls (only `interlock` has one, `object()`). The seven-name union `{__future__, dataclasses, hashlib, json, os, pathlib, typing}` is a subset of the sixteen generic_harness seeds. Let me confirm canonical's body composition and that no module-scope call performs any of the eight effects.

Let me look at canonical.py's actual import statements — MS-13.1's prose says "one __future__ statement, four import statements" but my AST parse found 6 import statements total.

canonical.py has **five** non-`__future__` import statements (hashlib, json, os, pathlib, typing), but MS-13.1's prose says "four import statements." The bound VALUE — `stdlib_seeds` = the six names, sorted/distinct — is correct, and the operative conclusion ("no module-scope call") is correct. This is a Minor descriptive-prose miscount, not an accounting defect touching any bound value/owner/code/check. I'll log it implementation-only. Q4's enumerated facts all hold.

Now Q1's joint block and §A0.4 anchor. Let me extract the joint block from both governing files and compare bytes.

Joint block is **byte-identical** in both files, 2626 lines, sha256 `d89995ea…b2b47fec` — matches the closure. Now the §A0.4 anchor: cardinality one, equal to composite H_FILE, zero retired V2_8-token lines, and no file contains its own digest.

Let me examine the V2_8 token occurrences to distinguish a live retired anchor line (defect) from descriptive prose.

The two V2_8 mentions are inside the **A16(d) extraction rule** prose in both files — and there is no V2_8 *anchor-grammar* line, so the closure's literal claim holds. But this raises a critical question: A16(d) (the rule that extracts the anchor) specifies the token `P1_WATCHDOG_V2_8_...`, while the only actual anchor line (§A0.4) uses `P1_WATCHDOG_V2_9_...`. I need to read §A0.4 and the full A16(d) to determine whether this is a token mismatch that breaks extraction. Let me read both carefully.

There's an apparent internal contradiction: §A0.4 (line 255) states A16(d)'s extraction token is **V2_9**, but the actual A16(d) clause text (amendment 2838, composite 4689) says the token is **V2_8**. This could break anchor extraction. Let me read the full A16(d) clause in both files to confirm exactly what token it binds.

A16(d) is an **operative** extraction clause ("extracted by this exact rule and no other"), and it literally binds the retired token `P1_WATCHDOG_V2_8_...`. Yet §A0.4 line 255 states A16(d) uses `V2_9`, and the sole anchor line (268) is `V2_9`. This is an internal contradiction. Let me check the v1.5 amendment to confirm whether v2.9 re-scoped §A0.4 but left A16(d) stale (an incomplete re-scope).

Confirmed and decisive. In v1.5 (v2.8) all three occurrences were consistently `V2_8`. In v1.6 (v2.9) the re-scope to `V2_9` was applied to §A0.4's prose (line 255) and the anchor line (268), **but the operative A16(d) extraction clause was left at `V2_8` in BOTH governing files** (amendment 2838, composite 4689). Let me make sure there's no reconciling "substitute current generation" clause before finalizing.

No reconciliation clause exists. This is a demonstrated defect: the closure (§7 line 402, §1.2 line 58) claims the §A0.4 anchor was "re-scoped to V2_9," but the operative A16(d) extraction rule — the consumer of that token — was left at the retired `V2_8` in **both** governing files. Let me complete the remaining questions (Q5–Q8) efficiently, then verify the commit's scope.

The commit touches exactly 5 doc files, all pure insertions (no code, keys, tests, manifest, or install record) — **Q8 = NO**. Let me read IR-13's scope statement (Q6) and verify the §7 counts (Q7) and the ordering guarantee (Q5).

IR-13's stated derivation range enumerates **fifteen** distinct section labels (MS-4, MS-6, MS-7, MS-11, MS-12, MS-13, IR-1, IR-2, IR-3, TS-1, TS-2A, TS-2B, TS-3, TS-4, TS-5) though the prose (and closure) call it "sixteen" — a counting descriptor to note. Let me count the IR-13 table rows and verify the other key §7 constants.

All key constants recompute: MS-8 = 2+55+7+1+1+2+1 = **69 members**; IR-13 = 47 relations; MEMBER_EXTRA retired; 89-row closure, 7 branches, 4 deps/32 assertions, seven-name union all confirmed. I have complete evidence. Let me confirm the A16(d) locus is inside the joint block (making the fix a regeneration, not a log note) and then write the review.

Everything is confirmed. The re-scope updated §A0.4 (amendment-only) but missed A16(d), which lives **inside the shared joint block** — so it's stale in both files and the fix requires regenerating the joint block (H_FILE/H_BODY/H_NORMATIVE) and re-anchoring §A0.4. This is a specification correction, not a log note. Writing the review.

Let me record the deliverable's hash and confirm no unintended modifications.

Independent X-line confirmation complete.

## Verdict

```text
REVISE_OFFICINA_P1_WATCHDOG_V2_9
```

**Deliverable:** [reviews/fable_officina_p1_watchdog_v2_9_independent_x_confirmation.md](reviews/fable_officina_p1_watchdog_v2_9_independent_x_confirmation.md)
**SHA-256:** `588fe8a23fd56a4366f920d4b1463d00ee3e7bd8bbc4cc1cbaca61b89a12f489` (only this file added; nothing else modified or committed)

## Answers 1–8

1. **YES on all three literal sub-claims** — outputs recompute; joint block byte-identical in both files (2626 lines, `d89995ea…b2b47fec`); §A0.4 anchor exactly once = composite `H_FILE` (`3ce26ba6…`), zero V2_8 anchor lines, no file carries its own digest. **But the anchor's extraction rule is broken — see B-1.**
2. **YES** — MS-11.1 byte-identical to v1.8 (`8c97e086…`); recomputes to length **20534**, digest **`aa974e0c…dc20ee`**, 89 rows, kinds 29/13/2/45, 267 false booleans. Residency+kinds independently reconstructed on the pinned interpreter (89 modules, zero kind mismatch).
3. **YES** — exactly seven unexecuted branches; `datetime → _pydatetime` verified as the sole v2.8 omission (`_datetime` is builtin).
4. **YES** — four digests match; edges/order correct; seven-name stdlib union `{__future__, dataclasses, hashlib, json, os, pathlib, typing}` ⊂ the 16 seeds; 32 effect assertions all false (only `interlock`'s `object()` at module scope). Derived by AST parse only.
5. **NO** — VP-4 total order + IR-13 single owner/code ⇒ first code is deterministic; no divergent counterexample.
6. **EXHAUSTIVE: YES; OMISSION FOUND: NO** — no refusable relation omitted.
7. **YES** — 89-closure, 7 branches, 47 IR-13 relations, 69 members (2+55+7+1+1+2+1), MEMBER_EXTRA retired, all recompute.
8. **NO** — commit adds only 5 documents (0 deletions, no code/keys/tests/manifest); `T=NOT_ACTIVATED`, claim `OPEN`, cell `NOT SELECTED`, Option A preserved.

## Why REVISE (finding B-1)

The V2_8→V2_9 anchor re-scope reached `§A0.4` (amendment-only) but **missed `TS-2B A16(d)`**, the anchor-extraction rule, which lives **inside the shared joint block** and still binds the retired `P1_WATCHDOG_V2_8_PRE_SELECTION_COMPOSITE_SHA256` in **both** files (amendment 2838, composite 4689). §A0.4 line 255 even states `A16(d)` uses V2_9 — a direct self-contradiction. As written, `A16(d)` finds zero V2_8 anchor lines and fails `STAGE_A_PRESELECTION_MISMATCH`, making the pre-selection composite anchor unextractable by its own rule. Major identifiability/consistency defect (fail-closed, so not Critical); operative clause, not wording. Because it's in the joint block, the fix regenerates `H_FILE`/`H_BODY`/`H_NORMATIVE` and re-anchors §A0.4 — a specification correction, not a log note. Two Minor prose miscounts (MS-13.1 "four import statements" → five; IR-13 "sixteen sections" → fifteen labels) should be folded into the same repair.

## What this authorizes

Nothing. A future CONFIRMED on corrected bytes would authorize **only Kirill's watchdog author selection** — no key, Stage A/B, manifest, install, implementation, test, activation or claim movement.

## Next boundary

Repair B-1 (fold in B-2/B-3) in the joint block of both governing files, re-anchor §A0.4, recompute region/file digests, then re-issue for a bounded independent X and Y re-confirmation by non-authors of v2.3–v2.9.
