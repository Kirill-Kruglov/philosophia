# Free manipulation and the hidden quotient — a bounded dev note

**Headline claim (the sound one):** in rank 1 the free normal form adds nothing
beyond the signed counts; in rank 2 it strictly refines them. That is a
distinction about *computational structure*, provable from the presentations. It
is not a claim that some measurable portion of a world is manufacturable.

Status: NON-CITABLE dev note, register (б) (a structural principle and the path
to it; artifact secondary). Bearing on Slot 4c; it does NOT fill or discharge any
registered essay slot, is not a confirmatory datum, and changes no label in the
essay. Analytic over two presentations, plus one cheap leakage/control audit (F1).
For one bounded Sol/Opus review round before it is trusted.

Filename is legacy: "manufacturable fraction" was the earlier, unsound framing
and has been removed from the note. Rename the file when nothing else points at
it.

## 0. Why this note is not a tautology

The tempting sentence — *"a mind can manufacture only what is invariant under its
own transformations, so the world-wall must be supplied, not manufactured"* — is
nearly analytic: the manufacturable invariants are, by definition, the invariants
of the transformation group one can apply, and the quotient is not among them.
Published as a result, that is a compression event that would also appear on
random labels — the essay's own named failure mode. This note states the claim
only where it has empirical content, in three places:

1. **Rank changes what free manipulation computes.** In rank 1 the free normal
   form *is* the signed count; in rank 2 it strictly refines it. Both halves are
   theorems about the presentations, not measurements — so this is a
   computational-structure distinction, and the note claims nothing more. The
   word "fraction" has been dropped throughout: it implied a measure over a
   world that was never defined, and any operational definition would make
   "rank 2 > 0" a claim needing a run rather than a proof. What is empirical is
   whether a learner at a given budget induces the refinement at all — and in
   this world REPRPROBE_07 already answers no for even the trivial invariant on
   novel words.
2. **An indistinguishability boundary** splits the "cannot manufacture the
   quotient" half in two. The *data* half is proved (§2), and F1's byte-identical
   n = 66 / n′ = 67 control makes it concrete rather than testing it. The
   empirical half is the *prior*: whether an architecture and objective, given a
   provably n-free stream, nonetheless land on n anyway. That is what F1 tests.
3. **Over-manufacturing has a cost**: a learner that mistakes the manufacturable
   invariant for the wall installs a false wall. E-SSL establishes the direction
   (over-invariance suppresses structure); what is not measured elsewhere is the
   trained-in false wall landing on exactly the items the quotient decides.

## 1. The ladder

A word here is a walk over generators; the element it names is its image in a
quotient of the free group. Three levels, one status each:

| level | F₁ (current world, R = L⁻¹) | F₂ (words over a, A, b, B) | status |
|---|---|---|---|
| a particular word / arrangement | a particular word | a particular word | wall of the **language** |
| the free-reduction invariant | displacement #R − #L (linear count) | free-reduced normal form (algorithmic) | the **complete manufacturable invariant** — true in every quotient, and too *fine* to be the world's element |
| the world's element | displacement mod n | image in F₂ / ⟨⟨relators⟩⟩ | wall of the **world** |

The middle rung is **not** a false wall, and calling it one (as earlier drafts and
B2 v2 did) inverts the logic. Free equivalence asserts only `w ~ w'` where the two
are freely equal — which is true in *every* quotient, so the assertion is never
wrong. Manufacture fails not by lying but by stopping short: it delivers the
finest invariant and is silent about which coarsening of it the world uses.

The boundary, restated: **free manipulation determines the free class, and
nothing coarser. It licenses `w ~ w'` when the two are freely equal, and it
licenses nothing whatever about `w ≁ w'`.** That asymmetry is why B2's path
signal had to be positives-only.

Two ways a false wall does arise, and neither is the middle rung:

1. **The converse, trained in** (`P0-neg`): asserting "freely unequal → different
   element." False exactly on the wrap items, where the quotient identifies what
   free reduction separates. This is the mind's own false wall — §6.
2. **Forced by the world** (essay §V): competent roads co-fail because the task
   funnels every one of them through the same door. Not correlated derivation,
   not a manufactured invariant, and not on this ladder — the essay's harder
   case, recorded here so the ladder is not read as claiming every false wall is
   the mind's.

**Relators as an information budget** (replaces the earlier "no partial
injection", which was wrong — supplying some relators of many is precisely
partial). The manufacturable data carries zero bits about `N` (§2). Every bit
about `N` must therefore be transferred from somewhere else: a supplied relator,
an oracle label, the prior, or observed interaction. A relator handed to the
learner is not a modelling convenience; it is a withdrawal from the contact
budget booked to the design budget, and it should be counted in the same ledger.
Firewall it exactly as the code firewalls modulus/residue/fold.

## 2. The indistinguishability boundary

**Invariant is not the same as identifiable, and this governs the wording
everywhere else in the note.** The quotient map is not something free reduction
destroys: `π_N ∘ freered` is invariant under every rewrite the mind can perform,
for *every* `N`. So the missing thing was never invariance — the world's element
is perfectly invariant, and so is every other coarsening. What manufacture cannot
do is **identify** which coarsening is the world's. Earlier phrasings that said
the modulus "is not preserved" or "is not a symmetry" were wrong; it is preserved,
and that is precisely the problem.

Let `G_N = F(S) / N` for an unknown normal subgroup `N`. Data manufactured solely
from the alphabet `S ∪ S⁻¹`, concatenation, insertion/deletion of `s s⁻¹` and
`s⁻¹ s`, and free reduction has the **same distribution for every `N`**. It
therefore contains **zero information about which quotient is the world**: two
worlds with different `N` are observationally indistinguishable to any oracle-free
process. Free manipulation can install a stack-like algorithm, remove syntactic
nuisance, and give a useful initialization — it cannot supply evidence about the
quotient.

Honest scope (this is the crack that keeps the claim falsifiable): the boundary
holds **relative to a named transformation group AND a prior that does not already
contain the quotient**. Naming both, for everything claimed here:

- **Transformation group** — for F₁: rearrangement of a word's moves at fixed
  displacement, plus balanced padding; i.e. the full stabilizer of the free
  reduction, and nothing else. In F1's run this is the support of
  `sample_unlabeled_word`: displacement uniform on a fixed [-125, 125] chosen
  independently of n, admissible padding uniform, arrangement rank uniform.
- **Prior** — a four-member `ContactTransformer` committee, 128-dimensional
  committee-mean pre-head, bidirectional masked-token reconstruction at 15%,
  1,000 updates, AdamW at 1e-3.

Change either and the boundary must be re-argued. Nothing below is claimed for
priors with a periodic or spectral bias, which is where F1 could plausibly fire.

## 3. Rank: what free manipulation computes

Both statements below are theorems about the presentations. Neither is measured,
and neither is offered as a contribution beyond stating the distinction exactly.

- **Rank 1 (F₁ ≅ Z, the current world): the free normal form adds nothing.**
  Free reduction of a word over `{R, L}` yields `R^d` with `d = #R − #L`, so the
  normal form *is* the signed count, already a linear function of the input. This
  is what F₁ is, not a defect of the world's design.
- **Rank 2 (F₂): the free normal form strictly refines the signed counts.** The
  signed-count vector `(#a − #A, #b − #B)` is the abelianization; the map from
  normal form to abelianization is onto and not injective — `a b A B` and the
  empty word share signed counts `(0,0)` and differ in F₂. Computing the normal
  form needs an algorithm (a deterministic stack, linear time) rather than a
  count. "Strictly refines" is the whole claim; nothing follows about how much
  a learner gains.
- **Whether the refinement buys anything is a run, not a proof.** A learner takes
  the cheap invariant first, and the cheap invariant in rank 2 is still the
  abelianization. Any F₂ experiment must therefore discriminate on pairs with
  **equal abelianization and different normal form**; measuring anything else
  silently collapses rank 2 back to rank 1 and reports the trivial invariant as
  a success.
- Consistent with the above, though not evidence for it: DIAG_04 memorized under
  maximal contact, and REPRPROBE_07 found residue not linearly represented for
  novel words. Both are facts about a learner failing to induce the *quotient* —
  neither measures what free manipulation computes.

## 4. Falsifiers (the fence, named)

| # | Falsifier | Status |
|---|---|---|
| F1 | a prior recovers the modulus from a provably n-free stream | **audited, one prior, did not fire** (§5) — not a falsifier of the boundary, see §5 |
| F2 | a natural world where free manipulation does most of the discriminative work and the quotient little | open; rank 2 is the near-miss case, a sparse-relator group the test |
| F3 | manufactured invariance robustly makes a scarce oracle budget go further (P+ > D and P+ > P_shuf) | open (the registered B2 estimand); does not falsify the limit but replaces "empty" with "leveraged" |
| F4 | bootstrapping: a relator acquired once by contact, then everything downstream manufactured | dissolves the limit's force over time → the limit is a statement about **acquisition**, not steady state |

## 5. F1 — a leakage and control audit (not a falsifier)

What F1 is, stated correctly. The byte-identity of the n = 66 and n′ = 67 streams
settles the *data* half **by construction**: identical bytes cannot distinguish
identical bytes, for any process whatsoever. Nothing was tested there; a control
passed. What remains is the *prior* half — whether one architecture and objective,
handed a provably n-free stream, lands on n anyway. F1 audits that for exactly one
prior. It is a leakage and control audit, and the note no longer calls it a
falsifier test of the boundary.

**Pre-registration: none on record.** The three-part recovery condition lives in
`f1_zero_oracle_08.py:496`, but the script, results, and this note are all
untracked, with no commit predating the run. There is therefore no artifact
showing the condition was fixed before the outcome was seen. Per the register's
own standard this makes §5 **a reading, not a falsifier** — treat it that way
until a successor run registers the condition first.

Question audited: can this prior recover n = 66 from **words alone**, with no
equality-oracle contact? Artifact: `successor/dev/F1_ZERO_ORACLE_08.md` (9.2 min).

- **Indistinguishability control (passed, not tested):** the unlabeled word stream
  was **byte-identical for nominal n = 66 vs n′ = 67**. This is §2 made concrete
  in the code path, and it is why the data half needs no experiment.
- Residue-mod-66 linear probe: **18.26% at init → 14.62% after unsupervised MLM**
  (chance 1.52%). The above-chance signal is the *displacement* leak, not n;
  unsupervised training **reduced** it.
- Blind period search (the falsifier's best shot, not told n): best period p = 2
  (parity); the **true p = 66 ranked 60th and 57th** of 124 candidates — mid-pack,
  no attraction to the modulus. Pre-empting the obvious objection: 2 divides 66,
  so the winner is a divisor of the true period. It is not a shadow of n. Parity
  of the displacement is fixed by word length under this alphabet — it is the
  trivial manufacturable invariant, exactly what the boundary predicts survives.
  Permutation-calibrated null (K = 1000 label shuffles, seed 0): the observed
  rank falls at **p = 0.95** under the shuffle null — no specificity for the true
  modulus, confirming the descriptive read.

**Verdict, at its real strength: the limit was not broken by the one prior tested
against it** — two seeds, one architecture, one objective, one horizon, condition
not registered in advance. Not "the limit holds", not
"tested". A prior with a periodic or spectral bias remains the case where this
could plausibly go the other way, and it has not been run.

## 6. Over-manufacturing has a cost

The mechanism is predicted, and the measurement is not yet in hand. In B2's
pilot the naive contrastive arm (`P0-neg`, "same free class → pull, other →
push") should train in a **false wall** on exactly the wrap items the quotient
decides — a learner that mistakes the manufacturable invariant for the world's
element. What the pilot actually returned is **anti-correct on 10 of 20 wrap
items on both seeds**, which the pilot itself records as "false wall incomplete,
not saturated," inside a run whose `M3_PASS = False` design-bug flag makes every
arm reading provisional. 10/20 is not separated from chance here, and this note
does not treat it as an effect. Stated at its real strength: this is the
system-level analogue of E-SSL's over-invariance result, it is the effect
adjacent work does not measure on the items a quotient decides, and it is
**registered as predicted, not reported as observed**.

## 7. Relation to prior art (this is not a new paradigm)

- Formal-language pre-pretraining transfers computational structure downstream
  ([Hu et al. 2025](https://arxiv.org/abs/2502.19249)) — close conceptual prior.
- Equivalence-preserving rewrite self-supervision ([S4Eq, Kommrusch et al.
  2021](https://arxiv.org/abs/2109.10476)).
- [MatrixNet (Laird et al., NeurIPS 2024)](https://arxiv.org/abs/2501.09571)
  learns representations of the *generators* and then enforces invariance to the
  *relations* by a separate regularization term — the boundary of this note built
  into an architecture: generators are generic scaffolding, relations are extra
  information that has to be supplied.
- Grokking acceleration: [Grokfast](https://arxiv.org/abs/2405.20233) changes
  optimization (no relation injected); invariance-regularizer acceleration
  **supplies** the group structure.
- Group structure *is* learnable from interaction with the environment —
  [Bartók, Szepesvári & Zilles, "Active Learning of Group-Structured
  Environments", ALT 2008, LNCS 5254,
  pp. 329–343](https://doi.org/10.1007/978-3-540-87987-9_28). Verified;
  directly on point. So the correct statement is *the wall must be externally
  evidenced — by prior, labels, or interaction* — never *human-supplied*.
  Interaction is what the oracle is in this world.
- Process vs outcome supervision (Uesato; Lightman) and E-SSL (Dangovski) as in
  the essay.

What is left after the downgrade, stated without rescue: a **rank distinction**
that is a theorem, not a finding; an **indistinguishability boundary** whose data
half is proved and whose prior half has been audited against exactly one prior;
and a **predicted** cost of over-manufacturing that has not been measured. None
of the three is a contribution. Together they are a correctly drawn fence and a
list of what would have to be run to put anything inside it.

## 8. What this note does not claim

Dev-status; not a confirmatory datum; fills no registered slot; one world-family,
one modulus, one architecture where empirical. It does not claim a measurable
manufacturable fraction of any world; it does not claim F1 tested the boundary;
it does not claim the over-manufacturing cost was observed. A publishable version
would need
(per the review line): a precise definition of oracle-free self-manufacture; a
stated no-information theorem over a quotient family with proof; the B2 controls
run so any apparent self-generated gain is shown to vanish or survive; and a
positive boundary result that observed interaction, but not free manipulation,
recovers quotient structure.
