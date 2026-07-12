# Climbing the Wall of Experience

### Can a mind earn a world from contact it manufactures itself?

> **Pre-result draft, July 2026.** The instrument and its measured limits are
> real. The small mind's result is not. Philosophia has not yet run its Level 0
> outcome experiment, compared active contact with a static corpus, measured
> cross-world transfer, or tested path credit. Where this essay reaches those
> questions, it changes tense and gives the registered way the claim can die.
> Readers who prefer evidence before the climb can go directly to
> [**What the Instrument Has Shown -- and What the Small Mind Has Not**](#what-the-instrument-has-shown----and-what-the-small-mind-has-not).

---

## Introduction

We are entering what David Silver and Richard Sutton call an
[era of experience](https://storage.googleapis.com/deepmind-media/Era-of-Experience%20/The%20Era%20of%20Experience%20Paper.pdf):
systems that do not merely imitate records left by people, but act, observe, and
learn over long horizons of their own.

I think they are pointing in the right direction. I also think the word doing
the work in that sentence -- *experience* -- is carrying more than we have made
it earn.

The internet is full of experience, but almost none of it belongs to the model
reading it. It is the fossil of somebody else's contact: measurements and
memories, arguments and incentives, honest errors and performed certainty,
pressed together into text. A model can learn extraordinary structure from that
fossil. What it cannot recover from the fossil alone is the difference between
what the world forced its authors to write and what their shared way of seeing
made easy to repeat.

My previous project, *proxylimen*, reached this boundary from below. A learner
could derive real structure from surprisingly little, but never from nothing.
Contact remained obligatory. The strong dream -- a world derived without an
oracle -- was a category error. The useful remainder was **calibrated
derivation**: minimal contact, declared and counted, with the place where the
instrument goes blind drawn in advance.

This essay asks the next question.

If contact is what a mind is missing, can contact itself be manufactured?

Not in an open world first. That would be too large, too contaminated, and too
easy to narrate after the fact. I chose the smallest workshop I know: finite
algebra and geometry. There the world can be generated without human examples,
truth can answer a query exactly, and one can change a representation while
holding the underlying object fixed. No body. No camera. No inherited proof.
Just a small learner, a derivable world, and a ledger of the places where its
expectations broke.

I did not choose mathematics because mathematics is the destination. I chose it
because it is the cleanest place to ask whether a mind can earn experience
rather than inherit its description.

The strong claim is tempting: give a model an inexhaustible formal world and it
will grow knowledge. I do not believe that claim is even well-formed. A rule can
generate endless data without giving the learner contact; a learner can agree
with itself by walking the same road twice; a compressed representation can be
nothing more than the generator's hidden parameters discovered and renamed.

So before growing the mind, I needed an instrument that could distinguish a
wall of the world from two roads sharing one blindness. I built it in the line
of work immediately before this one. It worked. Then the holdout found the place
where part of it did not.

That miss is the foundation of Philosophia, not an embarrassment at its edge.

---

## I. The First Difference

Begin with a point in a zero-dimensional space.

There is nowhere for it to go. No direction, no near or far, no before or after.
Call this zero experience -- not because the point is unreal, but because within
the space there is no distinction for it to encounter.

Now let there be one value.

The value is already more than nothing. It can be present rather than absent.
Let there be two values, and a relation appears: equal or unequal, before or
after if an order is supplied, one transformed into the other if an operation is
allowed. Experience begins as difference.

But a third kind of thing is easy to smuggle in and call another value:
linearity, curvature, order, chaos. These are not values sitting beside the
others. They are claims about how values hang together under a way of
describing them. The same finite sequence can look irregular in a language of
raw symbols and short in a language that already contains its generating rule.

This is the first discipline of the climb:

> A regularity does not live in the data alone. It lives in the relation between
> data and a language that makes the data short.

Write the data as (x), the language as (L), and the shortest description of
(x) available in that language as (K_L(x)). Then the candidate experience is
not (x), and it is not (L). It is the change in description length when the
two meet:

\[
R_L(x) = |x| - K_L(x).
\]

Large (R_L(x)) means the language found a short account of what otherwise had
to be stored raw. It is tempting to call that knowledge. It is not enough.

Kolmogorov complexity is uncomputable in general, and the invariance theorem
does not make description length independent of language. It bounds the
difference between universal description languages by a language-dependent
constant. In a finite experiment, that constant can be the whole apparent
effect. A pattern can be short because the world has structure, or because the
researcher placed the right primitive in the language before the learner began.

*Skip the formula and keep this: finding a short description is evidence that
the data and the language fit. It is not yet evidence that the fit belongs to
the world.*

So I use *experience* as a definition with obligations. A compression becomes
a candidate for experience only if it does work the learner did not receive for
free: it predicts held-out contact, survives a declared intervention, and
shortens work in a world or representation not used to name it. Otherwise it is
a regularity, perhaps a beautiful one, but not yet contact.

**Conclusion:** experience is not a substance stored inside a learner. It is a
relation that must pay rent outside the description in which it was found.

---

## II. The Fall and the Trace

A learner inside a language can do only local work. It can extend a proof,
adjust a hypothesis, make another query, descend another gradient. From there,
progress looks one-dimensional: the next grip is visible; the shape of the
whole climb is not.

Most of that work should be forgotten.

If the next observation is exactly what the current description predicted,
storing it separately adds nothing. The description already generates it. What
deserves a mark is the place where the world and the description part company:
an answer arrived that should not have arrived; a proof path closed where the
learner expected an opening; a confident prediction failed.

The trace is therefore sparse. Its landmarks are prediction errors.

This gives three states that are easy to confuse if they are named only after
success.

**Climbing** is work inside the current language. **Falling** is discovering
that the language did not close over the world; the route is lost, but its
surprises leave landmarks. **Ascending** is a representational change in which
the old route becomes visible as one route among alternatives. Only there does
cost become defined, because only there can the learner see that another path
would have been shorter.

I call that higher view a balcony. The word is phenomenological, not mystical.
In a model it must cash out as an observable re-description: old records become
shorter, previously separate cases share a reusable structure, and the new
structure changes future work.

This last condition matters. A post-hoc story can always trace itself backward.
A real abstraction has to do both:

1. explain why the earlier landmarks belonged together; and
2. reduce the cost of reaching truth after the abstraction exists.

DreamCoder's learned libraries are a bounded precedent for this shape. So are
the Fourier circuits found in grokking transformers: a modular-addition network
can move from memorized cases toward a representation in which addition is
implemented through periodic structure. In Nanda and colleagues' analysis,
mechanism-derived progress measures reveal circuit formation before the abrupt
change in test accuracy.

But those precedents also keep the claim honest. A bounded system can detect a
known family of abstractions. Nothing follows about a universal trigger for
insight. A detector expressive enough to recognize every future shortening
would have to solve the general problem of shortest description that made
(K_L) uncomputable in the first place.

*Skip the computation and keep this: a balcony can be recognized after we know
what kind of balcony to test for. No general instrument can promise to announce
every new dimension before the old language contains it.*

The engineering goal is therefore smaller than programming insight. It is to
make insight possible and auditable: preserve the sparse trace, provide genuinely
different routes, and test whether a new description explains old failures and
shortens new work.

**Conclusion:** experience leaves a trace before it has a language, but it earns
its name only when a later language compresses the trace and changes what the
learner can do next.

---

## III. The Same Wall

Suppose a learner approaches a problem by one route and stops. The stop could
mean two incompatible things.

The world may contain no passage. Or the learner's language may be blind to the
passage that exists.

From inside the route, these states can be observationally identical. More
effort in the same language does not resolve the ambiguity. A longer climb can
end at the same wall for the same reason.

The natural repair is triangulation. Approach by another road. If the obstacle
dissolves, the first wall belonged to the route. If it remains, confidence grows
that the wall belongs to the world.

This is close to William Wimsatt's notion of robustness by multiple means of
access: what can be detected, produced, or derived in varied ways is less likely
to be an artifact of any one way. It is also close to the ordinary practice of
science. We trust an object more when instruments built on different principles
find it.

But the word *different* is carrying the result.

Two implementations can have different names, random seeds, prompts, or surface
algorithms and still share the assumption that causes both to fail. Knight and
Leveson's experiments on multiversion programming made the problem concrete
decades ago: independently developed programs did not justify treating their
failures as independent. Common specifications and common habits create common
errors.

A thousand roads drawn by the same road-maker may be one road with decorative
noise.

That creates the false wall: two paths fail in the same place, not because the
world forced the failure, but because both paths inherited one blindness. From
below, a false wall is more convincing than an honest uncertainty. It is stable,
repeatable, and supported by agreement.

The obvious statistic -- how often two paths agree -- is almost useless here.
Correct answers are attractors. The world pushes competent paths toward the same
destination. Agreement on success is primarily the world's credit.

Failures carry the more diagnostic trace. If two paths independently reach the
same correct answer, they may have learned the same world. If they produce the
same *wrong* answer on the same instance, something in their shared derivation
has left a fingerprint.

Not proof. A fingerprint.

Let (e_i^{(a)}) be the error token left by path (a) on instance (i), with
zero meaning no relevant failure. A same-wall instrument looks for excess
coincidence of nonzero tokens,

\[
C(a,b) = \sum_i \mathbf{1}
  [e_i^{(a)} = e_i^{(b)} \ne 0],
\]

against an instance-matched and seed-crossed null. It asks whether the paths
fall together more often, and more specifically, than competence and the world
alone would predict.

*Skip the formula and keep this: do not ask whether two minds reached the same
place. Ask whether they made the same mistake where other competent minds did
not.*

Even this works only inside a stress window. If both paths are too competent,
they leave no errors to compare. If the task is mostly noise, their traces
decohere. Absence of co-failure can mean independence, perfect validation, or no
signal. The instrument must be allowed to say `INADMISSIBLE` and `NO_TEST`.

**Conclusion:** robustness requires varied roads, but variety cannot be inferred
from labels or origins. Independence is a property of measured failure, not a
biography of the path.

---

## IV. Independence Is Practiced

Before trying to grow experience inside one model, I tested the same-wall
instrument on several minds outside it.

Clean-room agents received the same hidden task without seeing one another's
work or the detector that would later compare them. Their visible mechanisms
were different. Their declared model families were different. That should have
made their errors independent.

It did not.

Against the author's reference path, one clean-room path agreed on the wrong
value in **24 of 24** diagnostic cases. Another agreed in **12 of 24**. A third
agreed in **0 of 24**.

The gradient did not follow the labels we had placed on the solvers. It followed
the probe channel they converged upon and the discipline with which they checked
their own answers. The path at zero was not independent because it came from a
magically independent family. It had removed the visible trace by validating
where the others guessed.

The calibration study found the harder version of the same fact. A
robust-validator base class was truly derived from its source, yet the detector
saw the derivation **0 times in 1,200 trials across all candidate windows**.
Discipline had not changed the ancestry. It had erased the symptom by which a
black-box instrument could observe it.

This result changes the sentence "use independent models" into an operational
obligation. Different seeds are not independence. Different vendors are not
independence. A clean room is not independence. These can help, but none of them
is the thing itself.

> Independence is not inherited. It is practiced.

And practiced independence has a cost. It may require a different probing
mechanism, a different validation habit, a different representation of the task,
or a counterfactual profile showing that the path fails differently when the
world changes. The useful unit is not the number of minds. It is the effective
number of failure channels.

This cuts directly into the idea of one learner triangulating its own thoughts.
A model can sample five chains of reasoning and still produce one epistemic
sample. If all five inherit the same weights, prompt, curriculum, and verifier,
their agreement may be a choir of one voice.

The ledger I want to grow in Philosophia cannot count paths. It has to earn a
reason to treat them as different.

**Conclusion:** self-consistency is not experience. It becomes evidence only to
the extent that the learner's roads are known to expose different ways of being
wrong.

---

## V. The Knife Misses

The primary same-wall experiment produced a harness-valid result inside its
locked development family. The token channel separated a registered derived
pair from a registered clean-room pair while preserving destination agreement.
The full run used 320 seeds. The rules, calibration bundle, null-world gate, and
pair assignments were frozen before the primary outcome.

That was validation, not confirmation.

The confirmation set had been commissioned from a fresh clean-room agent under
a hash-fixed prompt, encrypted on receipt, and committed before the primary run.
The author could not inspect the plaintext until after the primary outcome was
published. The generator was allowed one attempt; an invalid generation would
have ended the holdout rather than invited a better one.

On that holdout, the token channel held.

The forward-derived pair and its reverse reconstruction were `DEPENDENT`. A
same-prior pair with different visible mechanisms was `CLEAN`. The independent
replication was `DEPENDENT`. Most importantly, the registered cross-prior
clean-room pair was `CLEAN` on the token channel, with measured token excess
numerically zero.

The journal channel failed.

On that same cross-prior pair, it reported `DEPENDENT`, with a Jaccard statistic
of **0.857**. The combined blade therefore reported dependence where the
registered holdout expected cleanliness. Confirmation of a world-portable
combined blade was withheld exactly as the preregistration required.

This was not the instrument discovering secret ancestry. On fresh failure
classes, several adaptive scanners had converged on the world's one useful door.
Their failure journals aligned because the task funneled competent paths through
the same places. The journal could not distinguish shared derivation from shared
adaptation to a world with one door.

The miss matters because it is the same ambiguity the instrument was built to
resolve. The blade that distinguished a common road from a common wall in its
development family encountered a new wall: sometimes the world itself creates
correlated failures.

One more limit is impossible to repair with any black-box channel. Two paths can
share an implementation and express its effects through anti-correlated
symptoms. A measured example, `gptA-main` and `gptA-ref1`, shared helpers but
read clean because their visible errors diverged. No detector that sees only
outputs can infer dependence that leaves no common output trace.

This does not make the token channel useless. It makes its domain explicit. It
detects a registered class of shared failure when the failure is visible,
admissible, and not forced by the world's one door. It cannot certify
independence. No finite failure detector can.

> The knife can find a shared cut. It cannot prove that two uncut surfaces came
> from different blades.

**Conclusion:** the instrument is real because the holdout changed its claim.
The transferable result is the token core and its named domain; the combined
world-portable blade is falsified.

---

## VI. The Workshop

Now the original question can be stated without romance.

Can a small learner, trained from scratch on a derivable algebraic and geometric
world, acquire structure that satisfies the obligations of experience?

The world must be derivable, but the learner must still touch it. It receives an
oracle that answers narrow equality questions about hidden finite structures.
The oracle is not a teacher and does not expose the generating formula. It is a
wall that answers when pushed.

The programme has four experimental steps. None has produced a Philosophia
outcome yet.

### 1. The platform must breathe

A small transformer must first reproduce published modular-addition grokking.
This is Level 0: a replication anchor, not evidence for the thesis. Nanda and
colleagues showed that such models can form Fourier-structured circuits and that
mechanistic progress measures can precede the abrupt generalization transition.
Our implementation has been reconciled against the official companion source,
unit-tested, independently reviewed, and certified deterministic on two matching
ten-step prefixes. The scientific run remains unstarted until its thresholds,
controls, cadence, and seed quorum are locked.

**Registered kill:** if the faithful setup does not grok after the bounded
platform-repair policy, fix the platform. Do not reinterpret the theory.

### 2. Contact must beat a corpus honestly

Level 1 compares a learner that chooses equality queries with a learner receiving
a static corpus. Equal query counts are not enough: an active learner can win
trivially by selecting answers with greater entropy. The comparison must match
both oracle budget and realized answer information.

**Registered kill:** if active contact is no better than the
information-matched static corpus, then choosing where to touch the world has not
added the proposed experience advantage.

### 3. Experience must shorten the next work

Level 2 separates three things usually blended under "memory": weights, an
explicit ledger, and replay. Five arms move through a fixed curriculum of world
families: fresh; inherited weights; inherited weights plus ledger; fresh weights
plus ledger; inherited weights plus a false ledger.

The test is not whether an old task remains easy. It is whether history reduces
budget-to-truth, confident lies, or time-to-honest-abstention on a new family --
and whether the reduction survives a semantics-preserving change from algebraic
interfaces to Cayley-graph geometry.

**Registered kill:** if history does not beat scratch, or if the false ledger
carries the effect, the claim that experience shortened future work fails.

### 4. The road must add something beyond the destination

The verifiable-reward wave gives credit for arriving at a checked answer. The
core hypothesis here is narrower and stranger: experience lives partly in the
bundle of roads. Level 2.5 compares destination credit with credit assigned only
to ledger entries that survive resampled paths.

**Registered kill:** if matched path credit and answer credit produce
indistinguishable transfer, the path axis is redundant. That would be a useful
negative result, not a failed publication.

Finally, Level 3 asks whether the balcony can be detected rather than
programmed: does the ledger undergo a cross-world compression event, and do
mechanistic progress measures predict the transition before ordinary loss does?
Random labels and shuffled checkpoints must receive their own null arms before
any progress measure is trusted.

**Registered kills:** a compression event that also appears on random labels is
a tautology; a "new" basis present from the beginning is an artifact; a progress
measure that cannot beat its controls predicts nothing.

*Skip the design and keep this: the learner is not being asked to solve more
problems. It is being asked to prove that yesterday's contact changed the cost
of understanding tomorrow's world.*

**Conclusion:** manufactured contact is a testable proposal only when contact,
memory, transfer, and the path itself are separated into arms that can kill it.

---

## VII. Three Endings, None Chosen

It would be easy to write the rest of this essay now.

The metaphor is ready. A mind climbs, falls, records landmarks, finds a balcony,
and carries a shorter road into a new world. The story has the shape of a result.

That is why the result must not be placed inside it yet.

Philosophia can end in three ways.

### Proof

Active contact beats an honestly matched corpus. Retained experience shortens
work on new world families and survives a change of representation. A real
ledger helps while a false ledger does not. Path credit adds transferable
structure beyond destination credit. Compression and progress measures survive
their nulls.

Only then may the essay say that primary experience was manufactured in this
bounded world.

### Falsification

The claim may die earlier. Active selection may add nothing once information is
matched. History may fail to beat scratch. Transfer may vanish when algebra is
redrawn as geometry. A fake ledger may work as well as a true one. Path credit
may be redundant.

Then the result will be the coordinate where a beautiful account of experience
stopped predicting.

### Boundary

The most familiar ending is mixed. Contact helps inside one family but not
across interfaces. Weights transfer while ledgers do not. Path credit changes
calibration but not speed. A compression event exists but cannot be predicted
early. The workshop manufactures something real and smaller than experience as
we defined it.

Then the essay will be a map of that boundary.

I will not choose among these endings in prose. The repository currently says,
in capital letters, **NO PHILOSOPHIA RESULT YET**. This draft says the same.

**Conclusion:** the architecture of the answer can be written before the
outcome; the answer cannot.

---

## Conclusion

We began with almost nothing: a point with no direction and no difference to
encounter.

A value made the first distinction. Two values made a relation. A language made
some relations short, and the shortening tempted us to call the pattern real.
The first wall appeared there: from inside one language, a real absence of
structure and blindness to structure can look the same.

So the learner climbed. Where prediction held, the path disappeared into its
description. Where prediction failed, a landmark remained. The learner fell and
climbed again, not along the same line but by another road.

Two roads reached one dead end. From below, that looked like a wall. From a
balcony, it might have been the first route seen from another side. A change of
description made cost visible: what had felt inevitable became one path among
alternatives.

The criterion emerged from the view: what survives a change of road is more
likely to belong to the world; what dissolves belonged to the language.

Then the second wall appeared. Roads do not become independent because we name
them differently. Two paths can share a specification, a probe channel, a
validator, a curriculum, or one silent assumption. They can meet at a false
wall with more confidence than an honest path meets reality.

The only blade we found was co-failure. Success is an attractor; the world
deserves much of the agreement. A shared wrong answer is a more useful trace of
shared blindness. The blade measured a gradient -- 24, 12, 0 -- and taught us
that independence follows practice more than pedigree.

Then the holdout cut the blade. On a fresh world, competent adaptive roads found
one door and failed together because of the world, not a common origin. The
token core survived. The journal did not. The instrument became smaller and
more real at the same time.

That is the height from which Philosophia begins.

The proposal is not to give a machine a body made of algebra, nor to call an
infinite rule generator a world. It is to build the smallest honest contact we
can: a derivable world that still answers back; roads whose differences are
measured rather than declared; a sparse ledger of surprise; and tests that ask
whether the resulting structure predicts, survives intervention, shortens the
next work, and crosses into another representation.

If those tests hold, experience will not have appeared from nothing. It will
have been manufactured from the minimum honest something: contact plus a way to
distinguish the world's resistance from the learner's repeated blindness.

If they fail, the failure will not make the climb empty. It will tell us which
piece we had mistaken for experience -- active choice, retained weights, the
ledger, the bundle of paths, or the balcony itself.

The distant hope is a mind that earns a world before inheriting our words for
it, and can keep those layers explicitly apart. This project does not establish
that such a mind can be built. It asks the preceding question in a world small
enough to answer and names what would make the hope die.

> Knowledge is not a property of the learner. It is an invariance the learner
> earns across its own genuinely different roads -- and whether that can be
> built is now an experiment, not a metaphor.

--- ---

# What the Instrument Has Shown -- and What the Small Mind Has Not

*This section is the evidence ledger behind the story. Every inherited number
links to a committed artifact. Every Philosophia claim remains a slot until a
new signed decision changes the canonical results file.*

## The inherited instrument

Line 12's primary result is mechanically harness-valid. Under its locked stress
family, the v4 instrument assigned different residual-dependence labels to one
registered derived pair and one registered clean-room pair while preserving
destination agreement. The primary run used **320 seeds** and records the
preregistration, leakage scan, evaluation oracle, tautology check, and harness
version in its signed
[`decision.json`](../inheritance/line12_same_wall/experiment_A/decision.json).

The scope is narrower than "the detector identifies ancestry." It supports a
token channel based on correlated wrong-value failures in the admitted stress
window. It rejects co-success as ancestry evidence and permits `INADMISSIBLE`,
`UNKNOWN_FIELD`, and `NO_TEST` rather than manufacturing a verdict.

## The 24/12/0 gradient

The clean-room battery measured wrong-value overlap with the author's path:

| Pairing class | Shared wrong values |
|---|---:|
| common-prior / converged channel | 24/24 |
| intermediate converged channel | 12/24 |
| cross-prior, independently validated channel | 0/24 |

The exact battery and eligibility decisions are recorded in
[`PREREG_v4_DRAFT.md`, Amendment 1](../inheritance/line12_same_wall/experiment_A/PREREG_v4_DRAFT.md#appendix-r--frozen-reference-matrix-part-of-the-prereg-hash)
and the first-contact table. This is direct evidence that declared family and
clean-room commissioning do not by themselves buy error independence. It is not
a universal ranking of model providers.

The tune stage then found a base-class visibility boundary: derived-A fired
200/200, derived-gem 198/200, while derived-gptA fired **0/200 at the best
window and 0/1200 across all windows**. That class was removed from the detector's
power domain and published as not tested against, rather than silently averaged
away.

## The three amendments

Each amendment changed the specification because an observation exposed a
missing distinction.

1. **Correct agreement became the world's credit.** The reference criterion was
   changed from raw agreement to wrong-value agreement at most 6/24. A 16/24
   overlap consisting entirely of correct answers remained eligible; a 12/24
   all-wrong overlap did not.
2. **Visibility became a base-class property.** The 0/1200 robust-validator
   result forced per-class power accounting and narrowed the claim domain to the
   classes whose derivation left a measurable trace.
3. **Construction dependence survived a world with no world.** A null-world
   clone flagged, correctly: same-construction paths can couple through any
   consistent answer function. The null gate was repaired to test only
   cross-construction specificity. The same run also exposed Python's
   process-randomized `hash()` as a determinism defect and replaced it with
   stable hashing.

These were not cosmetic revisions. Each paid for a distinction the previous
specification lacked.

## The escrowed holdout

The holdout plaintext hash is
`a0cb7bac0cdeb6d9e76a2336f8725fdee3b2cc879e233f8937cf1188c147bce0`.
Its generation and encryption preceded the primary outcome; its key and
plaintext were released only after publication. The committed
[`holdout_result.json`](../inheritance/line12_same_wall/experiment_A/holdout_result.json)
records:

| Holdout arm | Token channel | Journal channel | Combined |
|---|---|---|---|
| H1 forward derived | DEPENDENT, 0.064 | DEPENDENT, J=0.857 | DEPENDENT |
| H2 reverse derived | DEPENDENT, 0.064 | DEPENDENT, J=0.857 | DEPENDENT |
| H3 same-prior / different mechanism | CLEAN, 0.004 | INADMISSIBLE | CLEAN |
| H4 cross-prior clean room | **CLEAN, ~0.0** | **DEPENDENT, J=0.857** | **DEPENDENT** |
| H5 independent derived replication | DEPENDENT, 0.141 | CLEAN, J=0.571 | DEPENDENT |

H4 falsified portability of the combined blade. H1, H2, and H5 support the
token core within the registered holdout family. No stronger reading is admitted.

## What Philosophia has established

It has established infrastructure and provenance, not the programme claim.

- The Level -1 literature map marks grokking, Fourier mechanisms, replay, EWC,
  active learning, library learning, and open-ended curricula as known,
  partial, or open rather than relabeling precedents as novelty.
- The Level 0 implementation matches the companion training source at every
  traced trajectory-sensitive cell: initialization, split, warmup, and the
  114-class training / 113-class reporting boundary.
- **75 unit tests** and two repository verifiers pass.
- The one authorized v2 determinism prefix produced matching initialization,
  split, loss-sequence, and final-state hashes across two ten-step replays.
- No `PREREG.lock`, Level 0 outcome report, or Philosophia `decision.json`
  exists.

The canonical statement remains:
**NO PHILOSOPHIA RESULT YET.**

## Status ledger

| Claim | Status | Artifact or kill |
|---|---|---|
| Correlated wrong-value failures can expose shared derivation | **EARNED, inherited and bounded** | Line 12 primary decision + holdout token channel |
| Co-success identifies shared ancestry | **REJECTED** | correct agreement is the world's credit; Amendment 1 |
| Random seed, provider, or clean room guarantees independence | **REJECTED** | 24/12/0 and 0/1200 visibility boundary |
| The full token+journal blade transfers across worlds | **FALSIFIED** | H4 journal false positive; confirmation withheld |
| Companion-faithful Level 0 code is deterministic on the tested prefix | **EARNED, platform only** | matching v2 prefix report |
| Modular-addition grokking is reproduced here | **SLOT** | kill: no grok after faithful run and bounded platform repair |
| Active contact beats a matched static corpus | **SLOT** | kill: active no better under matched oracle count and answer entropy |
| Experience shortens work on new families | **SLOT** | kill: history no better than scratch, or false ledger carries effect |
| Experience survives algebra-to-geometry representation change | **SLOT** | kill: transfer disappears under semantics-preserving change |
| Path credit adds transferable structure | **SLOT** | kill: indistinguishable from matched answer credit |
| A cross-world compression event marks earned experience | **SLOT** | kill: event appears on random-label null or existed throughout |
| Hidden progress predicts transition before ordinary loss | **SLOT** | kill: no predictive advantage over random-label and shuffled-order controls |

## What this does not show

It does not show that algebra can substitute for embodiment. It does not show
that a learner can generate its own truth. The oracle is contact, and removing
it would repeat the category error measured in *proxylimen*.

It does not show that multiple chains of thought are independent, that
self-consistency is epistemic robustness, or that correlated errors identify a
unique common cause.

It does not show that Fourier structure is a universal signature of
understanding. Within modular arithmetic it is a known mechanism and a
replication anchor. Across worlds, compression remains a registered question.

It does not show that a harness-valid decision is true. The harness certifies
declared procedure. The question, metrics, nulls, implementation, and
interpretation can still share one author's blind spot.

And it does not show that the final sentence of the story is right. That sentence
is now attached to experiments capable of killing it. Until they run, it is a
hypothesis written in the author's voice, not a result written by the world.

---

*This essay is the fourth panel of a quartet. [**justitia**](https://kirill-kruglov.github.io/justitia/)
asks how a world remains livable when no one can read anyone's soul -- trust in
identities replaced by consequences and structure. [**proxylimen**](https://kirill-kruglov.github.io/proxylimen/)
asks where a mind's world comes from -- trust in inherited text replaced by
calibrated contact. [**fallacy-cutter**](https://kirill-kruglov.github.io/fallacy-cutter/)
asks how an experiment remains legible when the experimenter cannot trust their
own intentions -- promises replaced by a fail-closed instrument. **philosophia**
asks whether the contact those projects require can itself be manufactured --
not from nothing, but from a world small enough to answer and an instrument
honest enough to publish where it goes blind. One thesis underneath all four:
do not certify intentions; build contact, consequences, and constraints that can
be checked.*

---

## Acknowledgements and references

This project was developed in dialogue with Claude Fable 5, Claude Opus 4.8,
Codex GPT-5.5, GPT-5.6 Sol, and clean-room systems from several model families.
The philosophical questions, the decision to treat failures as results, and the
final claims are mine; so are the errors that remain. The AI systems are named
because hidden collaboration would violate the provenance standard the work asks
of everything else.

I would rather be corrected than admired. The nearest precedents include
algorithmic information theory (Solomonoff, Kolmogorov, Martin-Lof, Chaitin),
Wimsatt's robustness by multiple means, Knight and Leveson on correlated failure
in multiversion software, error-consistency work by Geirhos and colleagues,
grokking and Fourier progress measures (Power et al.; Nanda et al.; Gromov),
DreamCoder's library learning, active learning, EWC and replay, POET and PAIRED,
AlphaGeometry and AlphaProof, and Silver and Sutton's *Era of Experience*.

The novelty claims are deliberately narrow. Grokking, Fourier circuits, active
learning, replay, consolidation, library learning, and verifiable reward are not
ours. The inherited contribution is the same-wall instrument and its measured
limits. The open contribution is the attempt to turn path-invariant failure into
a training signal and test manufactured contact by forward work reduction and
cross-representation transfer.

Primary reading and exact links are collected in the repository's
[`references/LITERATURE_MAP.md`](../references/LITERATURE_MAP.md). The canonical
claim boundary is maintained in
[`canonical/RESULTS_CANONICAL.md`](../canonical/RESULTS_CANONICAL.md),
[`canonical/CLAIM_LEDGER.md`](../canonical/CLAIM_LEDGER.md), and
[`canonical/KILL_MATRIX.md`](../canonical/KILL_MATRIX.md).
