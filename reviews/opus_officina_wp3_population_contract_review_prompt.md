# Opus 4.8 X-line review: Officina WP-3 population/construct contract v1

Work in `/home/master/llm_projects/philosophia`. Review the committed WP-3
draft at commit `2bc781d` against the signed charter and author selections.
The later commit containing this prompt must differ from `2bc781d` only by
review prompts. Read the repository, not only this prompt.

Create exactly one new file:

`reviews/opus_officina_wp3_population_contract_review.md`

Do not edit existing files and do not commit. Do not create entropy, a world,
sample, panel, candidate, ledger event, root, lock, escrow artifact, datum, or
outcome. Do not activate T or execute any T/Q/C process. Static calculations,
temporary dummy-only serialization probes, tests, and the inactive bootstrap
verifier are permitted; report them precisely.

## Governing files

- `successor/CHARTER_V2_DRAFT.md`
- `successor/CHARTER_V2_1_CORRECTION.md`
- `successor/CHARTER_SIGNATURE.md`
- `successor/AUTHOR_SELECTIONS_V1_SIGNATURE.md`
- `successor/OFFICINA_WP1_WP2_CLOSURE.md`
- `successor/OFFICINA_WP3_POPULATION_CONSTRUCT_CONTRACT_V1_DRAFT.md`
- `reviews/fable_officina_wp3_population_contract.md`
- `successor/officina/{LINEAGE.json,PATH_POLICY.json,README.md}`

The signed fixed-finite-frame interpretation is not open. CH-1 and CH-2 are
still proposals and must not be treated as selected.

## Review mandate

Take an adversarial implementation/fidelity stance. Determine whether two
independent WP-4 implementers could produce the same construct and frame bytes,
whether open T is mechanically quarantined from Q/C units, and whether every
generation failure is fail-closed. Do not accept a narrative description as a
bit-exact contract.

Audit at least these surfaces:

1. **Recompute the frame from the normative formulas.** There is an apparent
   counterexample that must be resolved explicitly. Under Split-1,
   `b_p={24+2p,25+2p}` and `j in {2,4}` imply Q worlds
   `{28,29,32,33,38,39,42,43,48,49,52,53,58,59,62,63}`. The draft instead
   prints `{28,29,32,33,40,41,44,45,50,51,54,55,60,61,64,65}`. Several printed
   entries are assigned to C by the same document. Decide the consequence for
   T/Q/C disjointness, all derived counts, and signature readiness. Recompute
   CH-2b independently as well.
2. **Bit-exact construct identity.** Check whether the oracle, word/query byte
   grammar, typed-refusal representation, canonical frame JSON schema, block
   orientation domains, IDs, hashes, and rejection rules are fully specified.
   List every free byte or call-order choice that could make implementations
   diverge. A promise that a future implementation will choose a schema is not
   closure.
3. **World/frame boundary.** Verify that pools, panels, acquisition machinery,
   and learner choices are genuinely excluded without leaving WP-4 unable to
   implement the world. Check whether `PAD` and `SEP` are world semantics or
   accidental learner/panel constants.
4. **Quarantine and no reuse.** Attack every route from open T and test-only
   fixtures to a frame/reserve modulus, including direct oracle construction,
   alternate imports, forged provenance, symlinks, and a caller supplying `n`.
   State which routes belong in WP-3 contract text and which can be safely
   discharged by reviewed WP-4 code.
5. **T-dev bands and CH-1 provenance.** The draft freezes
   `[10,25] U [166,205]` as T-dev while presenting only the frame band as an
   author cell. Decide whether those T boundaries are justified world-side
   constants, hidden author choices, or an uncontrolled extrapolation design.
   Check that LOW/HIGH both yield a coherent, disjoint T/Q/C construction.
6. **Donor construction.** Verify that target/donor ordering, orientation,
   donor ACTIVE transcript production, and reuse prohibitions are defined
   tightly enough to preserve the intended instance-non-adapted yoke. Flag any
   trajectory or arm detail improperly pulled forward from WP-9.
7. **Shortcut and parameter leakage.** Decide whether public finite support and
   the admitted symbolic divisibility solver merely narrow a
   selection-conditional claim or make the intended contact estimand
   uninterpretable. If an admissibility rule is necessary, identify its proper
   owning phase without choosing its numeric content.
8. **Ownership discipline.** Identify every WP-6 or WP-9 cell that the draft
   accidentally fixes, and every WP-3 world-side value it improperly defers.
   Confirm that no stopped-Level-1 outcome was used to tune a value.
9. Run `scripts/verify_officina_wp12.py` and confirm that placing the draft at
   `successor/` leaves the exact `successor/officina/` bootstrap set unchanged.

## Required output

Lead with exactly one verdict token:

- `OFFICINA_WP3_XLINE_ACCEPTED_FOR_AUTHOR_SELECTION`; or
- `REVISE_OFFICINA_WP3_CONTRACT`; or
- `BLOCKED_OFFICINA_WP3_CONTRACT`.

Then provide findings ordered Critical/Major/Minor with file and line anchors;
an explicit disposition of the arithmetic counterexample; exact mandatory
repairs; whether CH-1/CH-2 are reviewable after those repairs; and a negative
space statement. If revision is required, authorize only a bounded Fable
revision, not author selection, WP-4, entropy, or execution. If accepted, state
the exact author tokens that become eligible, but do not sign them.

Do not predict qualification or any scientific outcome.

