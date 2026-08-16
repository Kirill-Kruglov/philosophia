# TWOPRES_00 — disposition of the protocol review

Status: `TICKET_00_SUPERSEDED_BY_00A`

Input: `TWOPRES_00_PROTOCOL_REVIEW_SOL.md`, verdict `TWOPRES_00_PROTOCOL=REVISE`
(second dispatch; the first returned `REVISE` on dispatch integrity only —
the ticket was absent from the repository, and the reviewer correctly refused
to reconstruct a protocol from paraphrase).

## Disposition table

| finding | disposition |
|---|---|
| C1 — correspondence not identifiable under presentation automorphisms | **ACCEPT.** `D-1` symmetry typing added; recovery scored against the best representative of the equivalence class; the `t = 0` instrument kill fires only after class-quotienting. |
| C2 — Tietze moves change the type of the target object | **ACCEPT THE DEFECT, REJECT THE REPAIR.** See below; the object changes instead of the move set. |
| C3 — D1.0 and its converse are inadmissible cell kills | **ACCEPT.** High spectral similarity yields `PREDICTED_CHEAP` and orders the work; it never kills. Chance-level recovery everywhere yields `REACHABILITY_UNRESOLVED`, not a kill. |
| M1 — no observable stream law | **ACCEPT.** A deterministic materialization function and every size are frozen in 00a §3. |
| M2 — reading rules are not a total function | **ACCEPT.** Closed first-match terminal cascade in 00a §6, covering partial grids, method failure and non-monotone curves. |
| M3 — reverse search not executable as specified | **ACCEPT.** Removed from 00a entirely. Nominal `t` stands as nominal; no re-labelling rule exists, so none can misfire. |
| M4 — D2 incomplete beyond the corpus invariant | **ACCEPT.** D2 deferred to 00b. |
| M5 — D4 is not a ledger | **ACCEPT.** Reclassified `PAPER_OBLIGATION_NOT_SCRIPT`; it must close before cell authorization and consumes no audit budget. |
| M6 — scope cap does not match content | **ACCEPT.** 00a is cut to `D-1`, `D0`, descriptive `D1.0`, and exact rule/frequency baselines. Cap lowered to **120 lines / 90 minutes**, below the reviewer's proposal, because repeating the error at a smaller scale is still the error. |
| Minor — AC and Two-Hump are group-presentation priors | **ACCEPT.** Restated as adjacent motivating prior. The claim that arXiv:2606.21611 reports bimodality "in this family" is withdrawn as an overclaim. |
| Minor — Miller–Schupp work dated 2025 | **ACCEPT.** |
| Minor — Bridson claim | **ACCEPT.** Softened to what the abstract supports; flagged as requiring verification against the paper before it may appear in any citable text. |
| Minor — provenance needs both digests | **ACCEPT.** Raw-byte and LF-normalized SHA-256 both recorded. |

## C2: the defect is real, the proposed repair is not available

The reviewer is right that `M3`/`M4` induce a generator-to-word map rather than
an alphabet bijection, while rule matching, frequency matching and recovery
accuracy all assumed symbol-to-symbol correspondence.

The proposed repair — allow only a hidden bijective renaming plus redundant
relations — does not survive arithmetic. With `|Sigma| <= 6` there are at most
720 bijections. They can be enumerated exhaustively and the best scored.
**Alphabet correspondence is therefore recoverable by brute force at every
`t`, and cannot be a difficulty axis in this world at all.**

That is not a repair to the move set. It is a discovery that ticket 00 scored
the wrong object. Two objects were being conflated:

- **generator correspondence** — the alphabet map. Trivial here by
  enumeration. Retained only as an instrument positive control.
- **element correspondence** — which words over `Sigma_1` and `Sigma_2` denote
  the same element of the monoid. This is the word problem, and knowing the
  alphabet map does not solve it.

00a scores the second. Under that object, C2 dissolves: `M3`/`M4` remain
admissible precisely because breaking the alphabet bijection does not touch
element correspondence. The terminal renaming is demoted from load-bearing to
cosmetic.

Consequence, recorded so it is not lost: `RECOVERY_MAX` from the ticket-00
constants file is void. Recovery is now the fraction of correctly classified
**word pairs**, with a defined chance level, which is an improvement — the
denominators the reviewer asked for in item 2 now exist.

## One scope restriction 00a introduces, and its asymmetry

Certified *negative* pairs require knowing that two words denote different
elements — the word problem again. 00a therefore restricts to a **finite**
monoid `M`, so both polarities are ground truth by construction, exactly as
Wall B generates goals with their witness.

This restriction is not free and its consequence is one-sided. A finite `M`
makes the co-occurrence structure easier for cheap methods, so:

- **survival transfers upward:** if the correspondence is not cheaply
  recoverable even here, it is unlikely to be recoverable in the general case;
- **a kill does not:** `CELL_VOID_CHEAP_RECOVERY` obtained under finite `M`
  closes the finite case only and does not close the general one.

The terminal token carries the restriction in its name for this reason.

## What this disposition does not authorize

No implementation, no triple, no monoid, no run, no commit to a citable path.
00a requires its own acceptance before dispatch.
