# Opus 4.8 X-line — Level 1 feasibility-floor amendment v2, final confirmation

Reviewer: Opus 4.8 (X-line, bounded final confirmation — **not** a fresh design
review). Repository: `/home/master/llm_projects/philosophia`. **Nothing was
edited, committed, implemented, or run beyond read-only inspection and read-only
SHA-256 recomputation of the two immutable v1 artifacts. No code, authorization,
entropy, resource probe, trajectory, comparative datum, N3, lock, panel, escrow,
or outcome was created or touched.** Branch 1 is not reopened; no new learner
repair is introduced.

Scope: I checked the five closure sets against
`FEASIBILITY_FLOOR_AMENDMENT_V2_DRAFT.md` and its closure memo, adjudicated the
one flagged `committed`-before-step ambiguity, and ruled on the source-pin
enumeration question.

---

## Verdict

**`REVISE_LEVEL1_FEASIBILITY_FLOOR_AMENDMENT_V2_FINAL`**

Every substantive closure landed — AM-1..AM-7, the §2 literal signed replacement
text, the executable single-valued full-history rule, the §6 v2 contract, and the
§7 validity-first recovery table are all correct, and I **accept the strict Sol
resolution** of my AM-1 nuance and of the Level 0 wording (see below). The v1
hash pins in §6 are byte-accurate (I recomputed both). **The sole blocker is the
one ambiguity the task flagged:** §6's "written and committed before any learner
step" leaves two materially different implementations open. This is a
single-sentence correction. One last bounded confirmation (that the sentence
landed, nothing else moved) is needed before signature — no new data, no broader
review.

---

## The one mandatory correction

**§6 — "committed before any learner step" is not sufficiently executable.** The
sentence reads: *"The durable v2 claim is written and committed **before any
learner step**; the report is written **atomically after valid completion**."* The
word **committed** admits two incompatible readings:

- (a) **git-committed** before step 1 — which would require an exact, unreviewed
  two-phase protocol: what the commit contains, clean-index preconditions, the
  HEAD transition, the resume command after a fault, and the mid-run failure
  behavior; **or**
- (b) **durably created on the filesystem** (`atomic_create` + fsync) before step
  1, with git archival of the terminal artifacts after the report — which is
  exactly the **reviewed v1 discipline** (`scripts/level1_run_feasibility.py`:
  `atomic_create(... CLAIM ...)` before `run_noncomparative_feasibility`, the
  report `atomic_create`d after, and git archival out-of-band after completion;
  the v1 evidence was git-committed at `052a341`, *after* execution HEAD
  `c89a6b6`).

Because the claim's durability before step 1 is load-bearing for the one-shot
no-retry discipline (a crash between step 1 and a durable record must never
permit a silent re-run), an implementer must not be free to choose between (a)
and (b). Reading (a) would also invent a git-commit-before-step mechanism that v1
never had and that would itself need review. The **smallest** correction is to
pin reading (b), which matches the already-reviewed v1 driver.

**Exact bounded replacement (replace the two quoted sentences in §6 with):**

> The durable v2 claim is **created before any learner step** via `atomic_create`
> (exclusive-create write followed by fsync of the file and its directory),
> matching the reviewed v1 claim-before-run discipline; the run refuses if the
> claim path already exists. The report is written the same way (`atomic_create`
> + fsync) **only after valid completion**. **Git archival of the terminal
> artifacts (claim and report) occurs after the report is written and is never a
> precondition of any learner step**; the pre-run git guards remain exactly the
> reviewed set (clean tracked tree, empty index, `EXPECTED_HEAD == HEAD`, the
> authorization and public-root transcript git-tracked).

This changes no schema, path, cap, route, or scientific claim; it only removes the
implementer latitude the word "committed" created.

---

## The second flagged question — source-pin enumeration (no correction needed)

**"Source-byte pins over every amended and reachable module" may be frozen during
reviewed implementation; the amendment need not enumerate the path set itself.**
The amendment is a scientific/contract document; the exact module-path tuple is an
implementation artifact (v1's `REVIEWED_SOURCE_PATHS` was reviewed when the
*driver* was reviewed, not in any spec). §6 already fixes the load-bearing
*principle* at the right level: pins over **every amended and reachable module**,
plus the committed amendment-document hash, plus the verify-and-refuse-on-mutation
v1 link, with the explicit statement that **the v1 pin set cannot be reused**.
Hard-coding the tuple into the amendment would couple the contract to a code
layout that may legitimately refactor before implementation and risk drift on a
rename. The correct discipline: freeze the enumerated set during the reviewed v2
driver implementation and confirm at that review that it covers every amended and
reachable module. No edit required — but the implementation review must verify
completeness (the m3/FS-4 lesson: a missing reachable module, e.g. the output
plumbing in `public_root.py`, is exactly what that review must catch).

---

## Confirmation of the five closure sets

**1. AM-1..AM-7 landed exactly.**
- **AM-1** — §7's five mutually-exclusive routes make `censored_at_b` exist *only
  after validity*; wall-hit/OOM/environment/crash → `LEVEL1_FEASIBILITY_V2_INVALID:
  <ENVIRONMENT|RESOURCE_CAP|PROCESS>` with the binary **unset**, never `BLOCKED`;
  hash/seal → `…:<HASH|SEAL>` whole-check invalidity; "no third attempt" scoped
  precisely to *no third learner/training-policy intervention*. ✓
- **AM-2** — §4 states 2,000 AdamW updates/member **unchanged** in both regimes
  (8,000 member-updates), the change described as 32-example stochastic mean
  gradient → exact full-history mean gradient, and 31.51 kept **only** as a
  compute-work ratio; §8 withdraws "≈400×", "mechanically unsurprising", "≈10×
  below" by name. ✓
- **AM-3** — §6 freezes all paths/schemas/token/caps (`scorer_steps: 0`, wall
  `129600`); §2 gives literal replacement text (see closure 2). ✓
- **AM-4** — §5 relabels the 30 h figure "linear-scaling planning projection, not
  a guaranteed or demonstrated bound", names the 62.5× per-step tail, and states
  the full-batch profile is unknown until measured; §8 records the relabel. ✓
- **AM-5** — §1 carries the narrow v1 statement; §8 item 1 withdraws the
  "predictably all-censored … designed to route to `INSUFFICIENT`" sentence by
  name; branch-2 rejection now rests on the narrow statement + the A10/C7 gate
  order alone. ✓
- **AM-6** — §2d proves non-perturbation from the injective length-prefixed domain
  encoding + per-domain counters (C2), with the mean-CE permutation-invariance note
  and the order still pinned for deterministic float bytes. ✓
- **AM-7** — §3 names the temporal reweighting (`1/t`; contact 1 in all 2,000
  updates, contact 2,000 in one) as signed scope text, with arm-symmetry ≠
  neutrality stated. ✓

**2. §2 is literal signed replacement text for every changed cell.** v3 §5 "Online
step" (§2a) and v3.1 A5 step-ordering (§2b) are replaced preserving each original
skeleton (receive-bit → pre-update p̂ → assemble → forward/backward/step/zero_grad,
`U=1`, CE mean, checkpoint contents, no early stop, common B) with only the batch
assembly changed and replay retired; v3.1 A2's domain list (§2c) drops **only**
`("L1","replay", …)` and defers the C2 allocation-domain refinements by reference;
the C3 public-root surface row (§2e) deletes the word "replay"; **C2 and C4 are
correctly declared unchanged**; §2d's non-perturbation proof is sound. No other
governing cell is moved. ✓

**3. The full-history rule is executable and single-valued.** §2a/§2b pin: own
contact history only; canonical contact-schedule order (steps `1..t`); one shared
unchunked tensor; four members each taking one independent forward/backward/AdamW
step + `zero_grad`; CE `reduction='mean'`; `U=1`; no replay draw; no chunking, no
gradient accumulation. The batch-order pin (§2b) resolves float32 non-associativity
for deterministic state-hash bytes. All eight required properties are present and
admit one implementation (matching the `feasibility_committee_step` shape). ✓

**4. §6 freezes a complete v2 contract.** Distinct authorization
(`FEASIBILITY_EXECUTION_AUTHORIZATION_V2.json`), output dir (`feasibility_v2/`),
claim/report files and their `.v2` schemas, token
`I_AUTHORIZE_LEVEL1_NONCOMPARATIVE_FEASIBILITY_V2`, caps `{1, 2000, 0, 129600}`,
arm/world `{RANDOM-STATIC, pair_slot 0, modulus 66}`; canonical JSON; exact
environment/HEAD/clean-tree/empty-index guards; amended-source pins (v1 set not
reused) + amendment-doc hash; verify-and-refuse-on-mutation v1 link; refuse on
existing v2 path; refuse on any later-gate artifact. **I recomputed both v1
hashes** — `357baef2…c106ab` (claim) and `1c3843ec…820b7f` (report) — and they
match §6 exactly, independently confirming the loud transcription correction
(the historical `…820f7f` abbreviation was wrong; the true tail is `…820b7f`).
✓ — with the one `committed`-word correction above.

**5. §7 implements the strict Sol recovery rule without losing the AM-1
distinction.** An invalid run sets **no** `censored_at_b` bit and authorizes **no**
automatic rerun; any future mechanically-justified resource recovery requires a
**new explicit Kirill-signed process/resource decision + bounded review, learner
rule unchanged**, and is explicitly not pre-authorized here. My AM-1 distinction
(resource/process/seal invalidity is never learner-floor evidence) is preserved
route-for-route. ✓

**I accept the two strict-Sol reconciliations (closure memo §3, questions Opus-1
and Opus-2):**
- **Resource re-execution.** My AM-1 would have let a clean, mechanically-evidenced
  resource stop re-execute under the signed A6 process-re-execution category. The
  v2 draft adopts the stricter rule: no invalidity subtype auto-authorizes a rerun;
  recovery needs a new signed decision + review. This is **more** conservative and
  **fully preserves my two requirements** — (i) a timeout is never recorded as
  learner-floor censoring, and (ii) a timeout never *silently or permanently*
  blocks Level 1 (the block is loud, named `…:RESOURCE_CAP`, and reversible only by
  an explicit human-signed decision). I accept it.
- **Level 0 scope.** Restricting Level 0 to "an engineering precedent that
  full-batch AdamW ran on this platform for a different locked task" (no choice
  among repairs) is stricter than my "full-batch viability" wording and subsumes
  it; the update-count fact I surfaced (Level 1's 2,000 sits below Level 0's
  5,200–7,700) is retained. I accept it.

Opus Q3 (a bounded, capped, non-outcome implementation/resource pre-check after
signature, before execution) is correctly left **outside** this amendment as its
own separately-authorized check — the amendment pre-authorizes nothing. Consistent
with my original recommendation.

---

## Authorization boundary

Because the verdict is **REVISE**, the author token
`I_ACCEPT_LEVEL1_FEASIBILITY_FLOOR_AMENDMENT` is **not yet signable**. After the
single §6 `committed`-sentence replacement lands (and Sol's parallel final check
accepts), **one last bounded confirmation** — verifying only that the replacement
sentence is present and no other cell moved — clears the way; then Kirill may sign
`I_ACCEPT_LEVEL1_FEASIBILITY_FLOOR_AMENDMENT` (or issue a named refusal, which
routes Level 1 to `BLOCKED_LEVEL1_FEASIBILITY` by decision). This confirmation
authorizes **nothing else**: no v2 authorization candidate, no driver invocation,
no implementation, no resource probe, no trajectory, no comparative datum, no N3,
no lock, no panel, no escrow, no outcome. The v2 authorization candidate may be
drafted only after signature, and only Kirill's explicit
`I_AUTHORIZE_LEVEL1_NONCOMPARATIVE_FEASIBILITY_V2` can execute the one-shot check.

## Negative space (preserved, unweakened)

Only a valid comparative C1 result can reach
`BOUNDARY_CONTACT_CHOICE_AT_DISTANCE_1`; unresolved executed comparisons →
`INSUFFICIENT`; process/design failures retain `PLATFORM_OR_DESIGN_INVALID`;
certificate failure or censoring never proves the learner lacked `n`;
censored/`UNKNOWN` never success, equivalence, or a narrated boundary; no v1/v2
contrast may ever be formed; development artifacts non-citable forever; neither
feasibility gate can support `PROOF_CORE`; Level 1 is a detector, never programme
evidence, in every branch. The v1 evidence is immutable, non-outcome, and was
neither deleted, renamed, nor narrated as a failed attempt.

## Confirmation

I created **no** code, authorization, entropy, resource probe, trajectory,
comparative datum, N3, lock, panel, escrow, or outcome. I edited and committed
nothing. I inspected no loss/query/score/solve series (none exists) and compared
no arms. My only actions were reading the four documents and read-only recomputing
the two immutable v1 SHA-256 hashes (both match §6; the report tail is `…820b7f`).

— Opus 4.8, X-line. No outcome is asserted or predicted in this document.
