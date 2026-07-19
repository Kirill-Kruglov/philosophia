# Opus 4.8 X-line — successor line charter v1 review

**`REVISE_SUCCESSOR_CHARTER_V1`**

Reviewer: Opus 4.8 (X-line, bounded scientific/governance audit). Repository:
`/home/master/llm_projects/philosophia`. **I changed no existing file, created
nothing executable, chose no numeric/learner/world/device/promotion/repository
cell, and ran nothing. `essay/OUTLINE.md` untouched. Nothing committed.** Charter
commit `6e3de4d`.

The three-surface architecture is the right shape for Route B and is **not**
blocked — a charter consistent with the five signed tokens is scientifically
coherent, so `BLOCKED_ROUTE_B_BOUNDARY` does not apply. But one **Critical**
defect (the qualification surface is derivable in advance from a public root, so
"competence on unseen worlds" is not actually unseen) plus six **Major**
charter-level defects would make two implementers and two reviewers build
different phase boundaries and freeze orders. All are repairable with the exact
clauses below without reopening Route B and without turning the old censors into
evidence for any specific repair.

---

## 1. Findings (ordered)

### Critical

**X-A — Q worlds are precomputable at candidate-freeze time, defeating the
qualification surface.** §4 (Q row) and §9 derive Q worlds "under the public
dev-root," per-attempt only by domain label `("P2","Q",attempt,…)`. Because the
dev-root is **public** (§9: "drawn once … public successor dev-root") and the PRF
generator is public, anyone holding the root can compute `HMAC(root, "Q"‖attempt‖…)`
for **every** attempt index before freezing any candidate. Domain separation and
"a fresh, never-reused draw per attempt" prevent *world reuse across attempts* but
**not prediction**: a developer can enumerate all future Q worlds, bake them into
a frozen candidate (weights or config that memorize those exact worlds), and
"qualify" on worlds it has effectively already seen. The frozen-manifest and
disjoint-label defenses do not help — the candidate is not drawing from T's
partition, it is precomputing Q's. This nullifies the single load-bearing
innovation of Route B (competence demonstrated on worlds the candidate never
touched). This is a charter-level soundness error, not a deferred numeric.

**The fix does not require secrecy — it requires post-freeze unpredictability
(proven ordering).** Q worlds must be determined by entropy that does not exist
until *after* the candidate manifest is durably frozen. Publicity of the Q seed
*after* the attempt is harmless. See the §4/§5/§9 replacement clauses in §4 below
and the temporal contract in answer A.

### Major

- **X-B — lock/escrow order is self-contradictory (§4/§9 vs §5/§7).** §4 (C row)
  and §9 say the C escrow-secret root is generated "only after the scientific
  lock"; §5 and §7 order "escrow generation → preregistration lock." Two
  implementers get opposite sequences. The signed-line principle ("no C
  realization may influence the specification") requires **lock before escrow**;
  §4/§9 are correct and §5/§7 must be fixed. (Answer B; freeze table §3.)

- **X-C — device/manifest immutability point is contradictory (§4/§5 vs §6).**
  §4/§5 bind the device stack into the candidate manifest **frozen before the Q
  attempt**; §6 says the stack "freezes at (or before) promotion signature," and
  §5's freeze order inserts a separate "device-stack freeze" step *after*
  promotion. This lets a candidate qualify on stack X and be confirmed on an
  unqualified stack Y. The stack — and every manifested field — is part of
  candidate identity and is bound at the Q attempt; promotion carries the
  qualified manifest **unchanged**. (Answer C.)

- **X-D — the design-scout restriction is rhetoric, not a mechanism.** §5 permits
  a post-promotion scout reporting "variance, censoring, and resource aggregates
  only — never effect direction." But per-arm censoring counts, per-arm variance,
  and arm-resolved timing **encode direction** (ACTIVE censored 2/10 vs YOKED 8/10
  is an ordering). "Never direction" is enforced today only by after-the-fact
  audit of unconstrained numbers. It must be enforced by a **signed
  direction-blind output schema** (pooled/scale statistics only) or the scout must
  be dropped. (Answer D.)

- **X-E — the competence predicate may be tuned around a favored learner.** §5
  fixes the predicate *shape* at charter level (good) but sets its numerics "before
  the first attempt" — i.e., **after** T development has revealed candidate
  behavior. Numerics chosen with knowledge of candidate T-performance can be
  reverse-engineered to pass a favorite. The number stays a deferred cell, but the
  charter must add a **candidate-blindness** rule and move the sign point to
  *before any candidate is registered for qualification*. (Answer E.)

- **X-F — first-to-qualify is search-order exploitable; no-Q-fact-beyond-binary
  is unstated.** §5 offers author-selection or first-to-qualify as an open cell.
  First-to-qualify without a **pre-committed submission/tiebreak order** lets a
  developer control the winner by submission sequence. And neither variant states
  that **no Q fact beyond the binary** may enter promotion. Both constraints are
  charter-level and must be fixed now even though the variant may stay open.
  (Answer F.)

- **X-G — "no automatic rerun" vs "Q attempts individually recoverable" is
  underspecified and crash-farmable.** §8 must define: each attempt burns its fresh
  worlds; a crash *before any competence observation* may be recovered only as a
  **new attempt id on new worlds under an explicit signed disposition** (never
  automatic, never in-place); a crash *after* any competence signal consumes the
  attempt and its cap; and process-invalid recoveries need their **own bounded,
  signed ceiling** so crash-and-retry cannot multiply qualification chances.
  (Answer G.)

### Minor

- **X-H — the "separate repo is scientifically stronger" claim (§1) is
  overstated.** No filesystem layout prevents narrative relabeling; the
  anti-continuation guarantee is the *signed semantic quarantine* (§2/§3/§9),
  which holds under either layout. Layout is an author cell governing
  accidental-reuse risk and audit ergonomics, not scientific strength. (Answer H.)

- **X-I — the selection-conditional claim is honest but its limitation must ride
  in the estimand, not a footnote.** §3 is sound; the only requirement is that a
  future positive claim be scoped to *the promoted design on the confirmatory
  partition*, never to the learner class or unselected designs. (Answer I.)

- **X-J (minor/consistency)** — §11 lists "design-scout allowed-statistics list"
  as a deferred numeric; after X-D it must be a deferred cell **of a fixed
  direction-blind type**, not a free list. Small wording follow-through.

---

## 2. Direct answers to A–I

**A. Qualification really unseen.** As written, **no** — a candidate can
reconstruct all future Q worlds before freezing (X-A). Cryptographic secrecy is
**not** needed; an unpredictable **post-freeze** public draw is sufficient, and
the ordering proof is: if the Q seed is drawn only after the candidate manifest is
durably committed, the candidate's frozen bytes are independent of the worlds it
will face, so its qualification measures generalization, not memorization —
regardless of whether the seed is published afterward. Exact temporal/information
contract (minimum sound replacement):

1. **When each Q attempt root exists** — the per-attempt Q seed is drawn once
   (OS-CSPRNG) by a reviewed one-shot driver **only after** that attempt's
   candidate manifest is durably committed and git-tracked; it does not exist
   before manifest freeze.
2. **Who can derive/inspect Q worlds** — nobody can derive attempt-k's worlds
   before attempt-k's seed is drawn; the candidate's frozen code cannot encode
   them; after the draw, only the harness/reviewers hold the seed.
3. **Candidate-manifest durability before the Q draw** — the driver refuses to
   draw the seed unless the manifest (architecture, learner code commit,
   optimizer, policy, interface, device stack, config hash) is already committed
   and its hash is recorded in an atomic claim-before-draw (the stopped line's
   one-shot discipline).
4. **Post-attempt publicity** — the seed and realized worlds **may** be published
   in the attempt ledger after the attempt terminates; post-freeze publicity is
   harmless and aids audit. No long-lived secret key is required.
5. **No-redraw / process-invalidity** — one seed per attempt id; a fault before
   the durable attempt transcript is typed process invalidity with the competence
   field unset and no silent redraw (see G).
6. **Candidate cannot access Q truth/generator state** — the qualification harness
   exposes to candidate code only the sealed contact interface (oracle answers on
   the drawn worlds), never the seed, PRF key, generator counter, world identities,
   or truth labels — the stopped line's fail-closed noninterference boundary.

The single public dev-root is retained **for T only** (a sandbox; publicity is
fine there).

**B. Confirmation generation and lock order.** The correct, single sequence
(distinguishing the five stages): (1) signed scientific specification → (2)
**durable preregistration lock** of that spec → (3) **post-lock** escrow-secret
root generation + C-world realization → (4) ciphertext + salted-content-hash
commitment (sealed; no plaintext inspection pre-outcome) → (5) execution
authorization (Kirill one-shot) → confirmatory execution → authorized unsealing.
§4/§9 (root after lock) are right; **§5 and §7 are inverted and must be corrected**
to place the lock before escrow. Lock-before-escrow is what guarantees no C
realization can influence the specification.

**C. Candidate and device immutability.** A device may **not** change between a
successful Q attempt and promotion. The device stack — and every manifested field
(learner code commit, optimizer, policy, interface encoding, config hash) — is
bound into the candidate id at Q-attempt freeze; changing any of them yields a
**new candidate id requiring fresh Q worlds and fresh qualification**. Promotion
carries the qualified manifest **unchanged** into spec/lock/confirmation; there is
no separate "choose the stack at promotion" step. §6's "stack change after
promotion returns to qualification" is correct but must be generalized to "any
manifest change after the Q attempt that qualified it," and the standalone
"device-stack freeze" step in the §5/§7 order (implying a promotion-time choice)
must be removed.

**D. Design-scout channel.** The restriction is currently only **after-the-fact
auditable** and is scientifically **insufficient as prose**; it is **salvageable**
as a **mechanically enforced** channel via a sealed/blinded aggregator with a
**signed output schema fixed before the scout runs**. Minimum safe schema
(direction-blind by construction):

- **scale of the paired-difference distribution only** — e.g. variance or MAD of
  the *magnitude* of block differences (a scale, never the signed mean/location);
- **pooled censoring rate across all arms** (one scalar), never per-arm counts;
- **pooled resource aggregates** (total wall, peak RSS, mean step latency across
  all arms), never arm-resolved timing.

It may inform **only**: confirmatory **sample size**, **margin scale**, and
**resource caps**. It may inform nothing requiring the sign of the effect. The
spec-review provenance audit then checks the *schema* (mechanical), not just
narration. If even scale-of-difference is judged to leak (it can weakly, via which
margin is "achievable"), the honest fallback is **(d): no scout** — set spec
numerics from T-only priors and conservative bounds (the stopped line's
`B²`-fallback pattern). Do **not** preserve the bridge by rhetoric: the charter
must either fix the blind schema now or defer the scout to its own bounded
schema-review gate and treat it as unauthorized until then.

**E. Competence-predicate timing.** "Before the first attempt" is too late. Fix
timing by phase: predicate **shape** before T (already charter-fixed); predicate
**numerics** must be **candidate-blind** — a function of the scientific competence
floor (what makes a design worth confirming), **not** of any candidate's observed
T behavior — and signed **before any candidate manifest is registered for
qualification**, with an explicit no-candidate-tuning attestation. The *numbers*
remain a deferred cell; the *blindness rule and sign point* are charter cells that
must be added now. Meaning must be identical across candidates and attempts.

**F. Promotion and multiplicity.** Author-selection-from-closed-set and
first-to-qualify are both defensible **under the selection-conditional claim**,
and the variant may remain an open cell — but only after the charter fixes, now,
for **both** variants: (i) **no Q fact beyond the binary** may enter promotion;
(ii) exactly one promoted, set closed at promotion, before any confirmatory
artifact (already present); and, **for first-to-qualify specifically**, (iii) a
**pre-committed candidate submission/tiebreak order** (e.g., manifest-hash order)
fixed before the first Q attempt, so the winner is not set by developer-controlled
search order. Author-selection's discretion is honest only because §3 prices it;
the author must attest the basis is not a Q-fact-beyond-binary. With (i)–(iii)
added, the variant itself can stay open until before the first Q attempt.

**G. Invalidity and recovery.** Reconcile as: recovery is **never** an automatic
in-place rerun; it is always a **new, explicitly-disposed attempt**. Rules: (1)
each attempt **burns** its fresh Q worlds (never reused); (2) a crash **before any
competence observation**, verifiably process-invalid by mechanical evidence, may
be re-attempted **only** as a new attempt id on new worlds under an explicit
**signed process disposition** — the competence binary stays unset, and this is
not a "failed qualification"; (3) a crash **after** any competence signal consumes
the attempt **and** its cap slot (outcome knowledge was gained); (4) the cap
counts **valid completed attempts**, with a **separate bounded, signed ceiling on
process-invalid recoveries** so crash-and-retry cannot multiply qualification
chances; (5) nothing may be repeated with knowledge of any competence result. The
two ceilings and the signed-disposition requirement are charter cells; their
numbers are deferred.

**H. Lineage boundary.** No filesystem layout prevents narrative relabeling — the
anti-continuation guarantee is the **signed semantic quarantine** (§2 quarantine
table, §3 "no dev/Q result moves C1–C6," the `lineage` field, the non-citability
labels, the "no v1/v2 comparison exists or ever will" statement), which holds
under either layout. So the §1 claim that a separate repository is "the stronger
guarantee that the successor cannot be narrated as a continuation" is overstated
and should be corrected. **Recommendation:** treat layout as an author cell decided
on engineering grounds — separate repo slightly reduces *accidental reuse* (fewer
stopped-line paths in reach); same-repo `successor/` gives the strongest
*immutable ancestor lineage* (the stopped line is a literal hash-pinned ancestor),
one audit surface, and publication cohesion. **Regardless of layout, mechanically
enforce the quarantine** (a path-allowlist in every successor driver that
fail-closes on any read of a stopped-line path or entropy stream) — that mechanism,
not the directory boundary, is what prevents reuse. State it as an author choice.

**I. Claim semantics.** The selection-conditional claim is **honest** and is the
standard select-then-confirm structure (exploratory selection, then independent
confirmation on disjoint worlds under a locked analysis); with a single promoted
candidate, disjoint C, and a locked analysis, the confirmatory inference is valid
**for the promoted design**, and it **can** earn `PROOF_CORE`/`PROOF_STRONG` as
defined — *for that design*. The exact limitation a future positive claim must
carry, **in the estimand itself (not a footnote):** the result establishes the
effect for the **design selected by [promotion rule] from development, confirmed on
the confirmatory partition** — never a claim about the learner class, unselected
designs, or other partitions. Distinguish sharply: *legitimate* = "selected design
D exhibited E under preregistered confirmation on disjoint worlds"; *forbidden* =
"learners of class L exhibit E." The proof semantics are **design-conditional** in
the successor.

---

## 3. Executable phase / freeze-order table (corrected; B and C reconciled)

| # | Phase | Freeze / sign event | Fixed by |
|---|---|---|---|
| 0 | Charter X/Y review | author charter signatures (§12) | Kirill |
| 1 | Lineage bootstrap | repo/manifests/quarantine; **path-allowlist** quarantine mechanism | Codex |
| 2 | Partition sign | T/Q/C parameter-partition boundaries signed **before any generation** | Kirill |
| 3 | Public dev-root draw | one-shot reviewed driver → **T worlds only** | driver |
| 4 | T development | open sandbox, non-citable, envelope-bounded | — |
| 5 | Qualification predicate | **shape + candidate-blind numerics** signed **before any candidate registered** (E) | Kirill |
| 6 | Per-attempt Q | freeze+commit candidate manifest (incl. stack) → **then** draw post-freeze Q seed → fresh worlds → binary terminal; worlds burned; caps + recovery ceiling (A, G) | driver |
| 7 | Promotion | qualified set closes; exactly one promoted; variant pre-fixed; **no Q-fact-beyond-binary**; manifest (incl. stack) carried **unchanged** (C, F) | Kirill |
| 8 | Optional design scout | blind aggregator, **signed direction-blind schema**; informs only {N, margin scale, resource caps} (D) | Kirill |
| 9 | Successor scientific spec | estimand/margins/analysis/stops | Kirill |
| 10 | Spec X/Y review → spec signatures | | Kirill |
| 11 | **Preregistration lock** | durable commit of frozen spec — **before escrow** (B) | Kirill |
| 12 | **Post-lock escrow** | escrow-secret root → C worlds → ciphertext + salted-hash commit (sealed) | driver |
| 13 | Execution authorization | one-shot token → confirmatory execution → authorized unsealing (beyond this charter) | Kirill |

Nothing later modifies anything earlier; every signature and X/Y review is its own
bounded artifact.

---

## 4. Exact replacement clauses (mandatory repairs)

**R-A (Critical, §4 Q-row "Worlds" cell + §9):**
- §4 Q-row Worlds → "Q-partition, disjoint from T; **per attempt, a fresh set of
  worlds derived from a per-attempt entropy seed drawn once (OS-CSPRNG) by a
  reviewed one-shot driver only after the candidate manifest for that attempt is
  durably committed and git-tracked — never from the public dev-root**. The
  per-attempt seed and worlds may be published in the attempt ledger after the
  attempt terminates."
- §9 sentence → "**T worlds** derive from a public successor dev-root drawn once by
  a reviewed one-shot driver. **Q worlds do not derive from that root: each Q
  attempt's worlds derive from a per-attempt OS-CSPRNG seed drawn once, after the
  candidate manifest is durably committed, and published only post-attempt.** C
  worlds derive from a separate escrow-secret root generated only after the
  preregistration lock."

**R-B (Major, §5 and §7 order):** replace "…author signatures → C-world escrow
generation → preregistration lock → …" (§5) and "…escrow generation → lock → …"
(§7) with "**…author spec signatures → preregistration lock → post-lock
escrow-secret generation + C-world realization + ciphertext/salted-hash commitment
→ execution authorization → one-shot confirmatory execution.**"

**R-C (Major, §5 freeze order + §6 immutability point):** remove the standalone
"device-stack freeze (§6; may be co-signed with promotion)" step; add to §5/§6
"**Every manifested field (learner code commit, optimizer, policy, interface,
device stack, config hash) is bound into the candidate id at Q-attempt freeze; any
change after the qualifying attempt yields a new candidate id requiring fresh Q
worlds and re-qualification. Promotion carries the qualified manifest unchanged;
it selects, it does not re-choose.**"

**R-D (Major, §5 scout + §11):** replace "variance, censoring, and resource
aggregates only — never effect direction" with "**a signed, direction-blind output
schema — scale (variance/MAD) of the paired-difference *magnitude* only, pooled
censoring rate across all arms, and pooled resource aggregates — emitted by a
sealed aggregator; no per-arm mean, per-arm censoring, arm-resolved timing, or
signed contrast may appear. It may inform only sample size, margin scale, and
resource caps.**" §11 "design-scout allowed-statistics list" → "design-scout
allowed-statistics **numbers within the fixed direction-blind schema type**."

**R-E (Major, §5 qualification entry rule):** add "**The predicate numerics are
candidate-blind — a function of the scientific competence floor, never of any
candidate's observed T behavior — and are signed before any candidate manifest is
registered for qualification, with an explicit no-candidate-tuning attestation.**"

**R-F (Major, §5 promotion):** add "**No Q fact beyond the competence binary may
enter promotion. If the first-to-qualify variant is chosen, a candidate
submission/tiebreak order (e.g., manifest-hash order) is pre-committed before the
first Q attempt.**"

**R-G (Major, §8):** replace the recovery sentence with "**Each Q attempt burns
its fresh worlds. A fault before any competence observation, verifiably
process-invalid by mechanical evidence, may be re-attempted only as a new attempt
id on new worlds under an explicit signed process disposition — the competence
binary stays unset; this is not a failed qualification and never an automatic
in-place rerun. A fault after any competence signal consumes the attempt and its
cap slot. The qualification cap counts valid completed attempts; a separate
bounded, signed ceiling limits process-invalid recoveries.**"

**R-H (Minor, §1):** replace "the separate repository is the stronger guarantee
that the successor cannot be narrated as a continuation" with "**the
anti-continuation guarantee is the signed semantic quarantine (§2/§3/§9), not the
filesystem layout; the layout is an author choice affecting accidental-reuse risk
and audit ergonomics, and the quarantine is mechanically enforced by a
path-allowlist under either layout.**"

**R-I (Minor, §3 honesty clause):** add "**A future positive claim states its
selection-conditionality in the estimand itself: it establishes the effect for the
promoted design on the confirmatory partition, never for the learner class or
unselected designs; `PROOF_CORE`/`PROOF_STRONG`, if earned, are design-conditional
in the successor.**"

---

## 5. Validly deferred cells (not defects)

These are correctly open (§11) once the charter-level *rules* above are fixed:
T/Q/C partition boundary **values**; T budget envelope and checkpoint schedule;
qualification predicate **numbers** (given R-E's blindness/timing rule);
per-candidate/total attempt caps and the process-recovery ceiling **numbers**
(given R-G's two-ceiling structure); device numerical tolerance and
bounded-reproducibility criterion; the design-scout allowed-statistics **numbers**
(given R-D's fixed blind schema type); all confirmatory estimand numerics (budget,
margins, sample size, arm construction); escrow environment details; final line
name; repository location (author cell per R-H). Deferring the numbers is right;
deferring the rules that keep them honest is not.

## 6. Are the three proposed tokens signable as written?

**No — none, as the charter currently reads.**
- `I_ACCEPT_PHILOSOPHIA2_CHARTER_V1` — not signable until X-A (Critical) and X-B…X-G
  (Major) are repaired.
- `I_ACCEPT_THREE_SURFACE_PHASE_ARCHITECTURE` — the architecture *concept* is sound,
  but surface Q is currently defined unsoundly (X-A); signable only after R-A.
- `I_ACCEPT_SELECTION_CONDITIONAL_CONFIRMATORY_CLAIM` — the claim itself is
  scientifically **honest and sound** (answer I) and is the one token with no
  internal defect; recommend signing it only as part of the repaired packet
  (with R-I's estimand-wording constraint), not ahead of it.
After R-A…R-I land, all three become signable.

## 7. Questions for Kirill (≤4)

1. **Promotion variant** — author-signed selection from the closed qualified set,
   or pre-committed first-to-qualify (which then requires a pre-committed
   submission/tiebreak order, R-F)? May stay open until before the first Q
   attempt, but which do you intend?
2. **Design scout** — keep the post-promotion scout under the mandatory
   direction-blind schema (R-D), or drop it and set spec numerics from
   conservative T-only priors? (Keeping it adds a sealed-aggregator mechanism to
   build and review.)
3. **Repository layout** — separate `philosophia2` repo or same-repo `successor/`?
   Confirm the choice is on accidental-reuse/audit-ergonomics grounds; it is not
   scientifically decisive (R-H), and the quarantine is mechanically enforced
   either way.
4. **Level-0-style breathing check off-CPU** — if development converges on a
   non-CPU stack, do you want an optional non-citable platform check inside T, or
   is the qualification gate alone the platform assurance (F-2/R-11)?

## 8. Bounded questions for the final confirmation (after revision)

1. Do R-A/§9 make Q worlds provably independent of the frozen candidate (seed
   drawn only post-manifest-commit, candidate code with no access to seed/
   generator/truth), so qualification measures generalization not memorization?
2. Does the corrected §5/§7 order place lock strictly before escrow, with the
   five stages (spec → lock → post-lock root+realization → ciphertext/hash commit
   → execution authorization) distinct and non-reorderable?
3. Do R-C's manifest-immutability wording and the removed standalone stack-freeze
   step close the qualify-on-X/confirm-on-Y loophole for every manifested field?
4. Is the R-D scout schema direction-blind by construction (scale-only,
   pooled-only), and does R-E fix predicate numerics candidate-blind before
   candidate registration?
5. Do R-F (no-Q-fact-beyond-binary + pre-committed order) and R-G (burned worlds,
   new-attempt recovery, two signed ceilings) leave no search-order or
   crash-farming path?

## 9. Negative space (preserved, unweakened)

The stopped line remains immutable and `OPEN`; Level 1 remains
`BLOCKED_LEVEL1_FEASIBILITY`; C1 is unrun and untested; v1 and v2 are non-comparable
non-citable gate records and chose nothing in this charter or its repair; there is
no third Level 1 intervention. No tuning or qualification result may ever earn,
kill, or boundary-label C1–C6 — only the confirmation surface, under its own future
lock and signatures, can move a claim. Censored/`UNKNOWN`/"no qualifier" are never
success; a competence failure never proves the learner lacked the structure. This
review chose no learner, world, device, threshold, budget, partition, promotion
winner, or repository, and turned the old censors into evidence for no specific
repair — they motivate the *architecture* (a process lesson) and supply no
preference among designs. `PROOF_STRONG` remains reachable in principle in the
successor and is earned by nothing yet; the programme claim stays `OPEN`.

## 10. Confirmation

I changed no existing file (charter, canonical records, essay, reviews, code,
README, ROADMAP, atlas), left `essay/OUTLINE.md` untouched, and committed nothing.
I created exactly one new file (this review). No code, entropy, world, model,
learner, run, scout, escrow, lock, promotion, device selection, partition, or
outcome was created or run; no series was inspected (none exists); no arms were
compared; no v1/v2 contrast was formed. My only actions were reading the governing
inputs and reasoning about them.

— Opus 4.8, X-line. No outcome is asserted or predicted in this document.
