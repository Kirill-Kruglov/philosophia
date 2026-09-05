# Climbing the Wall of Experience

### Can a mind earn a world from contact it manufactures itself?

> **Status, September 2026.** The comparative experiment in this repository never
> ran. Its frozen feasibility gate stopped it, and that local fact has not
> changed. What changed is the question around it. Experiments in the neighbouring
> `experience` programme later showed that contact can shorten the next work and
> that, under an exact yoke, authorship of the actions adds nothing: the same
> transcript given to the same learner produces the same learner. The literature
> supplies the missing boundary. Under stated conditions, one view can leave the
> structure beneath it unidentified, while several sufficiently different views
> can make their shared content identifiable up to a stated equivalence. The
> proposal that a learner could make independent contact by resampling one formal
> view failed here. Contact as transcript selection and future-work reduction
> remain. Evidence behind the climb: [**What the Instruments and the Literature
> Actually Show**](#what-the-instruments-and-the-literature-actually-show).

---

*Before the apparatus, the whole essay in plain words.*

*A machine can read everything people have ever written and still receive the
world through observations already selected by someone else. Measurements are
retold, arguments arrive after they have been settled, and many of the errors
that made discovery possible have been smoothed away. I wanted to know whether a
mind could manufacture the missing contact for itself in a world small enough
to answer exactly. Finite algebra and geometry gave me such a world.*

*They did not give me the answer I expected. A formal generator can produce
inexhaustible data while showing the learner the same kind of view every time.
Resampling a road inside that view does not make another view. The non-trivial
structure in my walk world was supplied only by the wall -- the oracle answers
-- and the transformations the learner could manufacture did not identify it.*

*The neighbouring experiments changed the ending. Contact reduced the work
needed in the next world, and an exactly yoked learner given the same transcript
remained bitwise identical. What mattered was not who made the contact but which
contact entered the transcript. Published results make the distinction precise
in formal settings: several views can identify what one view leaves ambiguous,
under conditions that must be named. They do not say that gradient descent will
find the identified structure. The essay now ends in that gap, not at the
feasibility gate where this particular apparatus stopped.*

---

## Introduction

We are entering what David Silver and Richard Sutton call an
[era of experience](https://storage.googleapis.com/deepmind-media/Era-of-Experience%20/The%20Era%20of%20Experience%20Paper.pdf):
systems that do not merely imitate records left by people, but act, observe, and
learn over long horizons of their own.

I think they are pointing in the right direction. I also think the word doing
the work in that sentence -- *experience* -- is carrying more than we have made
it earn.

The position has stronger and more current forms than a position paper, and I
would rather argue with those. Blaise Agüera y Arcas holds in
[*What Is Intelligence?*](https://mitpress.mit.edu/9780262049955/what-is-intelligence/)
that prediction runs all the way down, through mind and brain and life, and the
[Computational Life](https://arxiv.org/abs/2406.19108) work he co-authored shows
self-replicating programs arising in a soup of random ones with no fitness
function imposed: structure from interaction, with nobody supplying the
structure. A different at-scale neighbouring form has now appeared:
[Hamilton-Zero](https://arxiv.org/abs/2608.11911), a foundation model with
roughly 0.5B variational parameters, is pretrained over hundreds of thousands of
generated Hamiltonian systems that vary in connection topology, system size, and
interaction type and strength, with its
[source](https://github.com/simulacra-research/HamiltonZero) and a
[foundation checkpoint](https://huggingface.co/simulacra-research/HamiltonZero)
released. Its scale makes it a stronger contemporary form of amortized learning
across generated systems than any position paper, but it is not a completed
answer to the question here: it does not isolate self-selected contact from
matched donated contact. The verified-discovery line proposes the other half.
[*Formal Conjectures*](https://arxiv.org/abs/2605.13171) puts more than a
thousand open research conjectures into Lean so that a machine's mathematics can
be checked by a kernel instead of argued about by us.

I think both are right about what they claim, and neither is what I am asking.
Emergence from interaction says that structure can arise unaided; it does not
say which learner earned which structure. A complete verifier says whether an
answer holds; it does not say whether the mind that produced it touched anything.
My question is what a mind is entitled to claim when nothing is checking, and
how anyone outside it could tell.

The internet is full of experience, but the model reading it does not control
which parts of that experience became text. It receives the fossil of somebody
else's contact: measurements and memories, arguments and incentives, honest
errors and performed certainty, pressed together into a corpus. A model can
learn extraordinary structure from that fossil. It can also learn to detect
conflicts inside it. What the corpus cannot expose is a distortion shared by
every route through which the corpus was made. Nothing in that observation
process marks the distortion as distortion.

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
holding the underlying object fixed. I thought this would be enough to make
different views. In most of the designs it made different wrappers around one
observation process. That distinction took longer to see than the algebra did.

No body. No camera. No inherited proof. Just a small learner, a derivable world,
and a ledger of the places where its expectations broke.

I did not choose mathematics because mathematics is the destination. I chose it
because it is the cleanest place to ask whether a mind can earn experience
rather than inherit its description.

At first an inexhaustible formal world looked sufficient: let a model keep
querying it and knowledge should accumulate. This essay began by distrusting
that claim and ended by losing its own weaker version. A rule can generate
endless data without adding an independent view; a learner can agree with itself
by walking the same road twice; a compressed representation can be nothing more
than the generator's hidden parameters discovered and renamed.

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

Write the data as $x$, the language as $L$, and the shortest description of
$x$ available in that language as $K_L(x)$. Then the candidate experience is
not $x$, and it is not $L$. It is the change in description length when the two
meet:

\[
R_L(x) = |x| - K_L(x).
\]

Large $R_L(x)$ means the language found a short account of what otherwise had
to be stored raw. It is tempting to call that knowledge. It is not enough.

Kolmogorov complexity is uncomputable in general, and the invariance theorem
does not make description length independent of language. It bounds the
difference between universal description languages by a language-dependent
constant. In a finite experiment, that constant can be the whole apparent
effect. A pattern can be short because the world has structure, or because the
researcher placed the right primitive in the language before the learner began.

There is a mature theory for the second case. Neural networks can approximate
continuous maps that are invariant or equivariant under a known group, and they
can do so with architectures built around that group. This is an expressiveness
result, not a discovery result. The symmetry has been placed in the language
before the data arrives. In the vocabulary inherited from *proxylimen*, it was
supplied rather than earned.

*Skip the formula and keep this: finding a short description is evidence that
the data and the language fit. It is not yet evidence that the fit belongs to
the world.*

So I use *experience* operationally, with obligations. A compression becomes a
candidate for experience only if it does work the learner did not receive for
free: it predicts held-out contact, survives a declared intervention, and
shortens work in a world or representation not used to name it. Otherwise it is
a regularity, perhaps a beautiful one, but not yet contact.

So experience is not a substance stored inside a learner. It is a relation that
must pay rent outside the description in which it was found.

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

Experience leaves a trace before it has a language, but it earns its name only
when a later language compresses the trace and changes what the learner can do
next.

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

Here the metaphor touches a theorem.

In unrestricted nonlinear independent component analysis, one observed view
can admit infinitely many incompatible decompositions that fit it equally well.
Under those assumptions the structure underneath is not merely difficult to
recover; it is not determined. Several sufficiently different views can change
the problem. Under their own stated conditions, multi-view results recover a
common latent source, or the content shared across partial views, up to the
equivalence each theorem permits.

These are population identifiability results. They say when the observations
determine a solution; they do not say that gradient descent will reach it. My
finite-field experiments are not instances of those theorems either. Their
contact tuples are injective on the world, so the object is already determined
by one observation. The connection is a design lesson, not a theorem about my
runs: most of the worlds gave the learner one kind of presentation, while the
world that later transferred gave it several. The worlds also differed in scale,
architecture, target, and exactness, so even that comparison remains a
hypothesis about the outcome rather than its isolated cause.

Another road therefore has to mean another observation process -- another way
for the world to preserve some distinctions and destroy others. Another sample
from the same generator may be only a longer version of the first road.

Two implementations can have different names, random seeds, prompts, or surface
algorithms and still share the assumption that causes both to fail. Knight and
Leveson's experiments on multiversion programming made the problem concrete
decades ago: independently developed programs did not justify treating their
failures as independent. Common specifications and common habits create common
errors.

A thousand roads drawn by the same road-maker may be one road with decorative
noise. Two corpora made by the same observation process may be one view at twice
the size.

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

Let $e_i^{(a)}$ be the error token left by path $a$ on instance $i$, with
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

Robustness requires varied roads, but variety cannot be inferred from labels or
origins.

> Independence is a property of measured failure, not a biography of the path.

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

The calibration study found the harder version of the same fact. A disciplined
validator -- one that double-checks itself before answering -- was genuinely
derived from its source, yet the detector saw the derivation **0 times in 1,200
trials across all candidate windows**. Discipline had not changed the ancestry.
It had erased the symptom by which a black-box instrument could observe it.

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

Self-consistency is not experience. It becomes evidence only to the extent that
the learner's roads are known to expose different ways of being wrong.

---

## V. The Knife Misses

The first same-wall run did what it was built to do. Inside its locked family the
instrument told a derived pair apart from an independently built one -- flagging
the road that shared an origin, clearing the road that did not, while both still
agreed on every core destination. The rules, the calibration, the null-world
gate, and the pair assignments were all frozen before the run produced a number.
Three hundred and twenty seeds. It held.

That was validation, not confirmation. Before the held-out test, a smaller result
stung first.

The same locked run carried one more pair -- the two roads behind the loud number
from earlier, the ones that had agreed on the same wrong value twenty-four times
out of twenty-four when I first put them in contact by hand. I registered that
pair as a control I expected the certified instrument to catch: a textbook case
of a shared prior producing shared blindness. It was not caught. Under the frozen
thresholds its shared-mistake signal fell just under the bar, and its schedule
signal sat below the floor the design required. The one number loud enough to
build a story on, before the instrument was locked, did not clear the instrument
once the instrument was locked.

I did not want to write that sentence. Twenty-four out of twenty-four is the
better story, and it is a true number -- I did not invent it. But it was a number
from before the discipline, and the discipline discounts exactly the kind of
agreement a world can force for free. When the field-relative instrument refused
to credit that pair as shared ancestry, it may have been right to refuse, or it
may have been under-powered on that one pair. The honest report does not get to
choose which. The run is the run, and it is published as it fell -- one control
of eight reading the opposite of what I expected, and the whole run labelled by
that one disagreement.

Then came the part I could not tune. The confirmation set had been commissioned
from a fresh clean-room agent under a hash-fixed prompt, encrypted the moment it
arrived, and committed before the primary run. I could not read the plaintext
until after the primary outcome was already public. The generator was allowed
exactly one attempt; a malformed one would have ended the holdout, not invited a
better one.

On that holdout, the shared-mistake test held. The forward-derived pair and its
reverse reconstruction were caught. A pair that shared only a prior, with
genuinely different machinery, read clean. An independent replication of the
derived construction was caught. And the strictest case -- the cross-prior clean
room the whole holdout was built around -- read clean on the shared-mistake test,
with its excess numerically at zero.

The other blade failed. On that same cross-prior pair, the schedule test reported
dependence where the registered holdout expected none. The two tests together
therefore called a clean pair coupled, and confirmation of a world-portable
combined instrument was withheld exactly as the preregistration required.

This was not the instrument uncovering a secret ancestry it had been too polite
to name. On fresh failure classes, several competent adaptive roads had simply
found the world's one useful door. Their failure-schedules lined up because the
task funnelled every competent path through the same few places -- shared
adaptation to a world with one exit, wearing the costume of shared origin. The
blade that had learned to tell a common road from a common wall met a new wall:
sometimes the world itself manufactures the correlation.

One limit underneath all of this cannot be repaired by any instrument that sees
only outputs. Two roads can share an implementation and still express it through
*opposite* symptoms -- one falls silent where the other guesses wrong -- and
leave no common trace on the surface at all. I have a measured example of exactly
that: two paths sharing their helpers, reading clean, because their visible
errors diverged. No detector reading only what a mind produces can infer a
kinship that produces nothing in common to read.

So the instrument's domain is not a boast; it is a fence. It detects one
registered class of shared failure, when that failure is visible, admissible, and
not forced by the world's one door. It cannot certify independence. No finite
failure-detector can -- and twice now, once inside the run and once on the
holdout, it showed me the edge of what it can do rather than let me pretend the
edge was further out.

There is also a domain where none of this is the right tool at all, and I should
say so before the fence is mistaken for a perimeter. Where a complete verifier
exists and is cheap -- a formal statement and a proof kernel, as in the open
Lean conjecture benchmarks -- the question this essay circles is already settled
for the answer. The proof checks or it does not. Nobody needs a co-failure
statistic to decide whether a machine memorized or knew, because the check is
not a matter of agreement in the first place. The same-wall instrument is for the
remainder: taste, which conjecture is worth the afternoon, transfer into a domain
with no formal target, and every regime where no complete oracle exists and
agreement is all one has. That remainder is most of thinking, but it is a
remainder, and the concession is not a rhetorical one.

Even inside formal mathematics the criterion does not vanish; it moves down one
level. A verified theorem is a wall of the formal language, and the formal
statement may not be the mathematical one. A formalization can be vacuous or
accidentally trivial, and the kernel will certify it exactly as willingly. The
*Formal Conjectures* authors handle this by having systems attempt proofs and
disproofs of their own statements and treating a suspiciously easy result as
evidence that the formalization, rather than the mathematics, was what gave way.
That is this essay's criterion running inside theirs: change the road and see
whether the wall dissolves. They arrived at it by needing it. I am claiming only
the name.

> The knife can find a shared cut. It cannot prove that two uncut surfaces came
> from different blades -- and the run that taught me that is the one I trust,
> precisely because it cost me the number I liked best.

---

## VI. The Workshop

Now the original question can be stated without romance.

Can a small learner, trained from scratch on a derivable algebraic and geometric
world, acquire structure that satisfies the obligations of experience?

The world must be derivable, but the learner must still touch it. It receives an
oracle that answers narrow equality questions about hidden finite structures.
The oracle is not a teacher and does not expose the generating formula. It is a
wall that answers when pushed.

The programme has four experimental steps. Level 0 answers whether the
platform can breathe. Levels 1 through 3 ask the programme question and cannot
inherit Level 0's answer.

### 1. The platform must breathe

A small transformer first had to reproduce published modular-addition grokking.
This was Level 0: a replication anchor, not evidence for the thesis. Nanda and
colleagues showed that such models can form Fourier-structured circuits and that
mechanistic progress measures can precede the abrupt generalization transition.

The reconstruction was reconciled against the official companion source, then
reviewed, preregistered, and locked before outcome. The primary paper-mainline
arm reproduced delayed generalization in **five of five seeds**, above the
registered quorum of four. Every seed reached persistent FIT at step **200**;
persistent GENERALIZE began between steps **5,200 and 7,700**, leaving locked
delays of **5,000 to 7,500** steps. The random-label control reached FIT and did
not GENERALIZE. There were no platform violations. Recorded as diagnostic-only
with `NO_PRIMARY_INFERENCE` because the primary arm already reproduced, the
alternate-fidelity arm also generalized in three of three seeds.

**Registered kill, resolved:** the kill did not fire. The platform breathes.
This licenses the replication statement and nothing about active contact,
cross-world transfer, path credit, or manufactured experience.

### 2. Contact must beat a corpus honestly

Level 1 compares three ways of touching adjacent hidden cyclic worlds. ACTIVE
chooses equality queries from its own uncertainty. YOKED receives the complete
query geometry produced by an active learner on a different, precisely matched
distance-1 world, but every answer still comes from its own oracle.
RANDOM-STATIC draws from the same candidate pool without an active donor. All
three receive one fixed budget and none stops early.

Realized answer entropy is not matched away. It is part of what contact may
change, so it is recorded as a mediator while success is judged on the same
arm-independent escrowed panel with fixed per-stratum criteria for every arm.

The scientific contract, implementation, and one-shot public allocation root
were committed before any comparative trajectory. Before spending that
comparison, the signed gate required one frozen RANDOM-STATIC development
fixture to produce a complete qualifying window. The signed floor amendment
fixed a full-history, mean-CE update after every answer. That amended one-shot
fixture completed all **2,000** steps with finite losses and parameters and a
computable dummy panel, but produced no complete qualifying window.

The route had been written before those numbers existed. It now reads
`BLOCKED_LEVEL1_FEASIBILITY`. This does not show that the learner lacked the
modulus, that RANDOM-STATIC was inferior, or that chosen contact failed. The
ACTIVE/YOKED comparison, scout, N3, lock, real-panel escrow, and outcome were
never run. There is no third learner-policy intervention under the signed route.

**Unreached registered boundary:** if ACTIVE had failed to beat YOKED in the
unrun comparison, the exact result would have been
`BOUNDARY_CONTACT_CHOICE_AT_DISTANCE_1`: chosen contact has not added the
proposed advantage under this narrow adjacent-world test of online
responsiveness. That boundary was not observed here.

It was observed more cleanly next door. In the later `experience` programme, an
exactly yoked learner receiving the same transcript as the active learner was
bitwise identical after **6,400** updates. Replaying the raw records reproduced
the trajectory. In the contrast that followed, ACTIVE and YOKED both reached
`1.0/1.0`, while a fixed equal-budget exposure reached `0.0309`. Within that
design, first-handedness added nothing. The advantage was in selecting the
transcript, not in being the mind that first touched the oracle.

### 3. Experience must shorten the next work

Level 2 would separate three things usually blended under "memory": weights, an
explicit ledger, and replay. Five arms move through a fixed curriculum of world
families: fresh; inherited weights; inherited weights plus ledger; fresh weights
plus ledger; inherited weights plus a false ledger.

It was not run. The total contact-mode selector has no resolved Level 1
comparison, so it returns `INSUFFICIENT` and blocks Level 2 upstream. This is not
a negative Level 2 result.

The test is not whether an old task remains easy. It is whether history reduces
budget-to-truth, confident lies, or time-to-honest-abstention on a new family --
and whether the reduction survives a semantics-preserving change from algebraic
interfaces to Cayley-graph geometry.

**Registered kill:** if history does not beat scratch, or if the false ledger
carries the effect, the claim that experience shortened future work fails.

This repository never spent that test, but the obligation did receive a
positive elsewhere. In `experience` E08D/E08T, contact in max16 produced
zero-shot competence in max32 and shortened the first **20--25** target
iterations in **five of five seeds** against the same architecture starting from
scratch. It is not a Philosophia result, and it does not establish the ledger or
the algebra-to-geometry transfer. It does establish that the criterion was not
empty: in a bounded world, yesterday's contact changed the cost of tomorrow's
work.

### 4. The road cannot manufacture the wall

The verifiable-reward wave gives credit for arriving at a checked answer. That
the road can carry credit the destination does not is already established, and
not ours: process supervision, which rewards the steps rather than the final
answer, outperforms outcome supervision on reasoning tasks. I mark that
direction known.

The proposed Level 2.5 asked whether experience could live partly in a bundle of
roads the learner supplied for itself. Process supervision grades a path against
an outside judgment of good steps. This design had no such judge. It would have
credited ledger entries that survived the learner's own resampled paths while
the oracle answered equality questions and never scored a step.

The premise fails before the comparison. Take the walk behind these worlds:
words over two moves, with the reached element represented by displacement.
Under the road-equivalence the design meant to use -- resampling a word while
preserving its endpoint -- the retained quantity is displacement, right steps
minus left. That is a linear function of the move counts already present in the
input. The non-trivial structure is the modulus `n`, and no such resampling can
reveal it. Resampling preserves every possible modulus. Because every candidate
survives, no road selects one. Only the oracle answers do that.

The learner can manufacture transformations. It cannot infer from those
transformations alone which distinctions the world meant them to preserve.
Work on self-supervised learning makes the positive side precise: paired views
can identify invariant content under explicit assumptions about the augmentation
process. The views and their relation do the identifying work. Calling every
self-generated variation a new view quietly supplies the conclusion in the
name.

The matched path-credit experiment was never run, and no empirical failure is
claimed. The axis is withdrawn for a narrower reason: in this cell, the quantity
to be manufactured was already a count in the input, while the non-trivial
quantity came only from contact. The road could not manufacture the wall.

The unrun Level 3 design asked whether the balcony could be detected rather than
programmed: does the ledger undergo a cross-world compression event, and do
mechanistic progress measures predict the transition before ordinary loss does?
Random labels and shuffled checkpoints must receive their own null arms before
any progress measure is trusted.

**Registered kills:** a compression event that also appears on random labels is
a tautology; a "new" basis present from the beginning is an artifact; a progress
measure that cannot beat its controls predicts nothing.

That question remains useful, but it no longer decides whether experience was
manufactured. A compression event can reveal how a learner reorganised what it
received. It cannot turn one observation process into two.

---

## VII. What the Roads Were Missing

The comparative route in this repository stopped before ACTIVE met YOKED. I
treated that as leaving every ending open. It left this experiment open. The
larger question continued in experiments built for different purposes, and
their answers now change what this essay can say.

The exact yoke removed one distinction I had given too much weight. If the same
learner receives the same transcript in the same order and ends in the same
state, it does not matter which copy chose the actions first. First-hand contact
has no extra substance in that comparison. The choice matters only when it
changes what enters the transcript.

That puts contact in the observation process rather than in the biography of the
observer. Someone else's measurement can be as good as my own touch if it
preserves the same distinctions. My own repeated touch can be useless if every
repetition comes through the same blind channel.

A second result did the work I had asked experience to do. Contact left
structure that worked in a new world before new training began and shortened the
training that followed. The learner's transformations failed to create the
independent view needed for the non-trivial part, while earlier contact still
changed later work in another bounded setting.

Large models show pieces of the same pattern. Representation spaces in vision
and language models become more aligned as the models scale, the empirical
pattern called the
[Platonic Representation Hypothesis](https://arxiv.org/abs/2405.07987). That is
evidence of convergence across modalities. Convergence shows that the models
agree more; it does not supply an external reason that the agreement is right.

Language models also contain internal directions from which classifiers can
[separate true and false statements](https://proceedings.neurips.cc/paper_files/paper/2024/hash/f9f54762cbb4fe4dbffdd4f792c31221-Abstract-Conference.html)
with substantial accuracy, and recent mechanistic work finds a
[small representational workspace](https://transformer-circuits.pub/2026/workspace/)
whose contents can be used by several downstream functions. Both results are
real and narrower than the claim I need. A truth direction can expose a conflict
represented inside the model; the studies do not test a distortion shared by
all of its evidence. A broadcast representation can serve capital, language,
and continent queries at once; that does not show that independent presentations
converged upon it.

The theory stops at a similar line. Identifiability results say when a
population of observations determines a representation up to an equivalence.
Approximation results say a network can express an invariant map when the group
is supplied. Neither says that an optimiser will discover the identified
structure from finite contact. The experiments sit between those results. They
show examples of transfer and work reduction, and a correlated series of exact
failures. They do not turn that series into a law about neural networks.

Resampling one formal view did not build independent contact. Together, the
theory and the later experiments move the boundary away from authorship:
experience depends on what the observation process lets the world distinguish,
not on whether the learner wrote the resulting transcript itself.

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

The criterion emerged from the view: what survives genuinely different ways of
contact is less likely to be an artifact of any one of them. Even then it is
identified only to the resolution those contacts share.

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
shared-mistake core survived; the schedule test did not. The instrument became
smaller and more real at the same time.

That was where the new literature found the essay. The ambiguity between a wall
and a blind route is not only a metaphor. In formal multi-view settings, one
observation process can leave many latent structures equally possible, while
several sufficiently different processes can identify what they share. The
conditions matter, and the answer remains only up to the equivalence the views
can resolve. But the direction is no longer intuition alone.

The workshop also supplied its own correction. I had treated many paths through
one formal world as candidate experience. In the walk design, every resampled
path preserved every possible modulus. The paths could recover a displacement
already present in their move counts; they could not select the modulus that
made the displacement an element of this world. Only the oracle answers selected
it. There were many paths and still only one view.

The neighbouring experiments separated contact from first-handedness. When two
copies received the same transcript, they remained the same learner. When the
selection of the transcript changed, the result changed. Earlier contact also
reduced the cost of learning the next world. Those findings do not belong to the
stopped run in this repository, but the question asked here cannot pretend they
did not happen.

So the proposal has become smaller. Do not ask a learner to create an
independent world by transforming its own description. Give it observation
processes that can fail differently, keep their provenance visible, and test
whether what survives them changes later work. A body is one way to obtain such
contact. Another instrument, another modality, or another person's measurement
may do the same work. Their value lies in the distinctions they preserve, not in
who touched them first.

There is still an unsolved piece. Population identifiability does not tell us
what gradient descent reaches. Expressiveness does not tell us which symmetry a
learner discovers. The positive experiments show that contact can change the
regime and pay forward into a new task; the exact failures show how often a
learner acquires a transformation law without its canonical content. The record
comes from one connected programme and cannot carry the weight of a general
theorem.

I had hoped that a mind could manufacture the missing contact inside one
derivable world. It could not do so here. The remaining engineering problem is
less romantic: the learner needs ways for the world to disagree with itself as
seen through any one channel.

> A road can be manufactured. The wall has to answer from somewhere the road did
> not supply.

--- ---

# What the Instruments and the Literature Actually Show

*The story now rests on three kinds of evidence, and they should not borrow
authority from one another. The literature establishes conditional results
about identifiability and expressiveness. The neighbouring `experience`
programme supplies bounded empirical answers to two questions this repository
left unrun. Philosophia supplies its instrument, its grokking replication, and a
valid feasibility stop. The ledger keeps those sources separate.*

## What the literature establishes

| Result | What it supports here | What it does not support |
|---|---|---|
| [Hyvärinen & Pajunen (1999)](https://doi.org/10.1016/S0893-6080(98)00140-3) | With unrestricted nonlinear mixing, a single-view ICA problem has infinitely many non-trivially different solutions | A theorem that one modality can never suffice for any learning problem |
| [Gresele et al. (2019)](https://arxiv.org/abs/1905.06642), [von Kügelgen et al. (2021)](https://arxiv.org/abs/2106.04619), and [Yao et al. (2024)](https://arxiv.org/abs/2311.04056) | Under stated multi-view assumptions, common sources or shared content can be identified up to the stated invertible or smooth equivalence | A claim that any two augmentations are independent views, or that the result is exact in arbitrary coordinates |
| [Yarotsky (2022)](https://arxiv.org/abs/1804.10306) | Networks can approximate continuous invariant and equivariant maps when the relevant group action is given | A method for discovering which symmetry the world has |
| [Tahmasebi & Weber (2026)](https://arxiv.org/abs/2512.11855) | Exact and approximate symmetry enforcement have provably different costs in a finite-group averaging framework | A result that exact structure is exponentially harder for gradient descent to learn |
| [Huh et al. (2024)](https://arxiv.org/abs/2405.07987) | Representations become more aligned across models and modalities as scale grows | Evidence that the converged representation is externally correct |

The first two rows are the spine of the revision. They concern population
identifiability: whether the observations determine a solution. The fourth
concerns linear post-processing of a black-box model by action queries. None of
them establishes what SGD reaches from finite data.

## What the neighbouring experiments add

| Question inherited from Philosophia | Later result | Scope |
|---|---|---|
| Does authorship of the queries add anything beyond their transcript? | E12A: an exactly yoked learner was bitwise identical after 6,400 updates | Exact null in that learner, world, order, and budget |
| Can transcript selection matter with the learner held fixed? | E12C: ACTIVE and YOKED reached `1.0/1.0`; fixed equal-budget exposure reached `0.0309` | The advantage localises to selection in that design |
| Can earlier contact shorten later work? | E08D/E08T: max16 contact gave max32 zero-shot competence and shortened the first 20--25 target iterations, 5/5 seeds | Positive in the tested threshold worlds; no algebra-to-geometry or ledger claim |

These results are imported as answers to shared questions, not relabelled as
Philosophia outcomes.

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

The same locked run also carried a common-prior control (`C_C8`) -- the pair
behind the 24/24 wrong-value agreement below -- registered with the expectation
that the certified instrument would flag it as coupled. It did not. Its token
excess (**0.034**) fell below the margin and its journal statistic (**0.565**)
sat below the field floor (**0.672**) on a three-pair quorum edge, so the pair
read `CLEAN` and the whole run was labelled `EXPA-NOT-CLEAN`. The loud
pre-lock number did not clear the instrument once the instrument was locked; the
control is published as it fell, not reinterpreted.

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
- At outcome commit `2daec9b`, **89 tests** and both repository verifiers passed.
- At public-root commit `6008757`, **133 tests** and both repository verifiers
  passed. This is engineering status, not programme evidence.
- The authorized v2 determinism prefix produced matching initialization, split,
  loss-sequence, and final-state hashes across two ten-step replays.
- The scientific specification was accepted and committed before the canonical
  lock; all nine fixed-budget runs then completed. The independent verifier
  reports `VALID` for
  [`outcomes/decision.json`](../experiments/level_0_grokking/outcomes/decision.json).
- Arm A reproduced in 5/5 seeds; R-0 passed both control obligations; no platform
  violation occurred.
- The Level 1 scientific contract and panel amendment were signed before
  comparative data, and their implementation passed bounded external review.
- The one-shot Level 1 public-root transcript at commit `6008757` records one
  CSPRNG call, fixes six development pairs and 24 target/donor role assignments,
  defers `R_h`, and declares `scientific_outcome:false`.
- The authorized Level 1 feasibility-v2 fixture completed `B = 2,000` with
  finite losses and parameters but no complete qualifying window. Its pre-signed
  terminal is `BLOCKED_LEVEL1_FEASIBILITY`; C1 remains unrun and untested, and
  no programme inference is admitted.

The permanent Level 0 statement is:
**REPRODUCED, PLATFORM ONLY -- NO PROGRAMME INFERENCE.**

## Status ledger

| Claim | Status | Artifact or kill |
|---|---|---|
| Correlated wrong-value failures can expose shared derivation | **EARNED, inherited and bounded** | Line 12 primary decision + holdout token channel |
| Co-success identifies shared ancestry | **REJECTED** | correct agreement is the world's credit; Amendment 1 |
| Random seed, provider, or clean room guarantees independence | **REJECTED** | 24/12/0 and 0/1200 visibility boundary |
| The full token+journal blade transfers across worlds | **FALSIFIED** | H4 journal false positive; confirmation withheld |
| The certified instrument flags the informal 24/24 common-prior pair as shared | **NOT REPRODUCED in the locked run** | `C_C8` read CLEAN: token 0.034 below margin, journal 0.565 below field floor 0.672 on the quorum edge |
| Companion-faithful Level 0 code is deterministic on the tested prefix | **EARNED, platform only** | matching v2 prefix report |
| Modular-addition grokking is reproduced here | **EARNED, platform only** | VALID locked decision; Arm A 5/5, quorum 4/5 |
| Random-label leakage control behaves correctly | **EARNED, control only** | R-0 FIT at 200 and does not GENERALIZE |
| Artifact-fidelity arm changes the primary inference | **REJECTED BY DESIGN** | B 3/3; `NO_PRIMARY_INFERENCE` because Arm A reproduced |
| Level 1 design, implementation, and allocation root are fixed | **PROCESS EARNED, NO PROGRAMME INFERENCE** | signed specs + reviewed code + public-root transcript |
| Level 1 feasibility floor | **BLOCKED_LEVEL1_FEASIBILITY, PROCESS ONLY** | valid v2 censor at B; C1 untested; no comparative scout |
| Chosen contact beats independently donated active geometry in Philosophia | **UNRUN / UNTESTED HERE** | registered boundary not evaluated; no arm comparison exists in this repository |
| Authorship of queries adds value beyond receiving the identical transcript | **REJECTED NEXT DOOR, EXACT NULL** | `experience` E12A; bitwise-identical learner after 6,400 updates |
| Transcript selection can add value with the learner fixed | **EARNED NEXT DOOR, BOUNDED** | `experience` E12C; ACTIVE = YOKED = `1.0/1.0`, fixed exposure `0.0309` |
| Experience shortens work on new families | **EARNED NEXT DOOR, BOUNDED** | `experience` E08D/E08T; zero-shot max16→max32 and faster first 20--25 updates, 5/5 seeds |
| Experience survives algebra-to-geometry representation change | **BLOCKED UPSTREAM / UNRUN** | no Level 2 result |
| Path credit adds transferable structure in the walk world | **VOID BY CONSTRUCTION / UNRUN** | the targeted invariant is already a move count; the modulus comes only from oracle answers |
| A cross-world compression event marks earned experience | **BLOCKED UPSTREAM / UNRUN DIAGNOSTIC** | never decisive |
| Hidden progress predicts transition before ordinary loss | **BLOCKED UPSTREAM / UNRUN DIAGNOSTIC** | never decisive |
| Path-derived structure can provide non-trivial manufactured experience in the walk world | **VOID BY CONSTRUCTION** | the path invariant targeted by this design, endpoint displacement, is a linear function of the move counts already in the input; the non-trivial factor, the modulus, is reachable only from oracle answers. Structural reasoning recorded in VI.4, not a measurement; the unrun ACTIVE/YOKED contact contrast is not voided by this argument |
| A standard single learner earns competence in that world without full history | **NO-COMPETENCE / PRE-MEMORIZATION** | [successor development sweep](../successor/dev/GROKKING_PROBE_09.md), non-citable: best held-out equality 58.8% against a 50% chance level, train fit never above 92.6% at any weight decay including 0.0, frozen floor never cleared at any checkpoint. Delayed generalization is defined after the training set is fitted; that window was never entered, so the sweep says nothing about whether a larger budget would enter it |
| That competence block is localized to a named wall | **NOT ESTABLISHED** | three candidates -- reading the walk, binding the two words, the modular quotient -- are separated by no probe that was run; the strict [disjoint-displacement residue probe](../successor/dev/B2_PILOT_08.md) sits at chance, which places the modular factor among the candidates without electing it. Localization was not purchased |
| A world intended to test path-manufactured structure needs a non-trivial compositional invariant | **DERIVED CONSTRAINT, UNRUN** | follows from the triviality limit in VI.4: a count is not enough, the mind's own transformations must compose. Path concatenation and comparison transitivity are candidate cells; none is built |
| Equational Wall-B library carrier | **CLOSED / SPARSE** | preregistered [frame audit 13](../successor/dev/WALLB_FRAME_AUDIT_13.md): 2/40 screen-qualified against threshold 5, Wilson 95% [0.014, 0.165]; [closure](../successor/dev/WALLB_EQUATIONAL_CELL_CLOSURE.md) preserved; non-citable development, not an ACTIVE/YOKED result |
| Equational Wall-B policy carrier | **SCREEN-VIABLE; ACTIVE/YOKED UNRUN** | preregistered [policy-channel audit 14b](../successor/dev/WALLB_POLICY_CHANNEL_AUDIT_14B.md): hard-oracle sweep froze `best_first`; 12/40 screen-qualified, Wilson 95% [0.181, 0.454]; recorded beside the library kill; no design contract and no ACTIVE/YOKED run authorized |
| Continuation route | **SUCCESSOR STOPPED AT DEVELOPMENT GATE** | Route B produced no locked successor scientific test: walk-world path-manufacture was void by construction; the equational cell is closed on both carriers with different verdicts (library sparse; policy screen-viable and left unrun); a later MINIMO-based route had its Phase-2 Stage-A and Stage-B L0–L3 engineering surfaces accepted but stopped before any scientific execution, the Stage-R route ending at its minimum-L4 paper boundary and a purpose-built E2 alternative stopping at IDEA_GATE before build; active substrate search is now stopped; Officina remains frozen rather than active |

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

The Level 1 feasibility terminal does not show that ACTIVE, YOKED, or
RANDOM-STATIC wins or loses, that the learner lacked `n`, or that full-history
training is ineffective. It shows only that the amended frozen development
fixture completed validly without clearing its signed floor. No comparative
panel or outcome exists in this repository. The later E12 result answers a
related estimand in another design; it does not retroactively turn this stopped
run into evidence.

The successor development runs do not show that manufactured contact fails, nor
that the walk world cannot host any test of chosen contact: ACTIVE and YOKED were
never compared. The structural limit is narrower. This cell cannot host the
path-manufacture axis in a non-trivial form: the path invariant targeted by the
design is a linear function of the mind's own move counts, so there is nothing
for that form of manufacturing to earn. A small learner failing to reach
competence in the cell adds no evidence on either side of the question the essay
asks, and the runs do not show why it failed. They are non-citable development,
and the negative they carry is bounded to one learner, one encoding, one
optimizer, and one budget. What they carry forward is a constraint on any next
world intended to test path-manufactured structure, not a verdict on chosen
contact.

A separate non-citable development line reached a related boundary from the side
of representation rather than contact. Under the unpaired-stream interface
considered by that line (TWOPRES), element correspondence between two
presentations of one finite monoid is identifiable at best up to `Aut(M)`; the
line closed as `NOT_CHEAPLY_AUDITABLE` before any implementation. It is a mapped
development boundary under that interface, not an experiment and not a claim
about representations in general.

The later equational development screens do not show that compositional
libraries fail, that ranking policies fail, or that chosen contact earns
nothing. They asked prior questions about whether each experience carrier was
common enough, under a frozen screen, to support a multi-world experiment. The
library carrier was not: two of forty fresh presentations passed, below the
preregistered minimum of five. The policy carrier, under a later
preregistered `best_first` frame, was screen-viable at twelve of forty, with a
Wilson interval that clears the same five-world engineering floor. Both
estimates remain non-citable development. ACTIVE and YOKED were never built or
compared; the author records the policy screen and does not spend the single
experimental slot on this substrate. What survives is a method constraint:
measure the prevalence of the mechanism an experiment needs before selecting a
convenient world and mistaking it for a family, and do not rewrite a correctly
earned sparse kill when a different carrier later screens.

[Minimo](https://arxiv.org/abs/2407.00695), an agent that jointly learns to pose
conjectures and prove them, bootstrapping from the axioms of propositional
logic, arithmetic and group theory, is the nearest external instance of a
self-teaching formal substrate. This programme ran one repository-default
exploratory realization of it, trained on self-generated formal material and
evaluated on a fixed human-written theorem panel — the only point at which such a
substrate was actually run here, and its fixed-panel transfer measured. It is
non-citable development: not ACTIVE/YOKED evidence, not the programme's
cross-world or presentation transfer, and not a Philosophia result. A later route
built on the same substrate stopped before any scientific execution, and active
substrate search is now stopped. Whether a learner reaches exact canonical
identification from the designated contact remains open across this connected
programme.

It does not show that a harness-valid decision is true. The harness certifies
declared procedure. The question, metrics, nulls, implementation, and
interpretation can still share one author's blind spot.

Nothing here turns the correlated case series into a general limit on neural
networks. The repositories share an author, an experimental lineage, evaluation
habits, and much of an architecture family. The exact boundary may belong to
that box. A new architecture or optimisation regime is a new hypothesis, not an
excuse for the old one; it is also the kind of independent test this record does
not contain.

---

*This essay is the fourth panel of a quartet. [**justitia**](https://kirill-kruglov.github.io/justitia/)
asks how a world remains livable when no one can read anyone's soul -- trust in
identities replaced by consequences and structure. [**proxylimen**](https://kirill-kruglov.github.io/proxylimen/)
asks where a mind's world comes from -- trust in inherited text replaced by
calibrated contact. [**fallacy-cutter**](https://kirill-kruglov.github.io/fallacy-cutter/)
asks how an experiment remains legible when the experimenter cannot trust their
own intentions -- promises replaced by a fail-closed instrument. **philosophia**
asks which part of the contact those projects require can be manufactured, and
which part must arrive through an independently answering view. One thesis
underneath all four: do not certify intentions; build contact, consequences, and
constraints that can be checked.*

---

## Acknowledgements and references

This project was developed in dialogue with Claude Fable 5, Claude Opus 4.8,
Codex GPT-5.5, GPT-5.6 Sol, and clean-room systems from several model families.
The philosophical questions, the decision to treat failures as results, and the
final claims are mine; so are the errors that remain. The AI systems are named
because hidden collaboration would violate the provenance standard the work asks
of everything else.

The nearest precedents I found include
algorithmic information theory (Solomonoff, Kolmogorov, Martin-Lof, Chaitin),
Wimsatt's robustness by multiple means, Knight and Leveson on correlated failure
in multiversion software, error-consistency work by Geirhos and colleagues,
grokking and Fourier progress measures (Power et al.; Nanda et al.; Gromov),
DreamCoder's library learning, active learning, EWC and replay, process- versus
outcome-based supervision (Uesato et al.; Lightman et al.), equivariant
self-supervised learning, POET and PAIRED, AlphaGeometry and AlphaProof and the
*Formal Conjectures* benchmark that continues that line, Agüera y Arcas on
prediction and on structure emerging from bare interaction, and Silver and
Sutton's *Era of Experience*.

The identifiability boundary is anchored by Hyvärinen and Pajunen on the
non-uniqueness of unrestricted nonlinear ICA; Gresele and colleagues on
multi-view nonlinear ICA; von Kügelgen and colleagues on identifying invariant
content from paired augmentations; and Yao and colleagues on shared structure
under partial multi-view observation. Yarotsky supplies the complementary
expressiveness result for invariant and equivariant maps when the group is
known. Tahmasebi and Weber separate the cost of exact and approximate symmetry
enforcement in a narrower averaging setting. Huh and colleagues provide the
cross-modal convergence evidence; Bürger and colleagues the activation-space
truth-discrimination result; and Gurnee and colleagues the broadcast-workspace
result. Each is used inside the limit stated in the evidence table, not as a
theorem about this programme.

The novelty claims are deliberately narrow. Grokking, Fourier circuits, active
learning, replay, consolidation, library learning, and verifiable reward are not
ours. Neither is the direction of the path axis: that process supervision beats
outcome supervision is an established result, and so is the observation that
invariance imposed too strongly suppresses the structure it was meant to expose.
The inherited contribution is the same-wall instrument and its measured limits.
The attempted path contribution is withdrawn in this walk world: its invariant
is already a move count, and its non-trivial content comes only from the oracle.
What remains from Philosophia is the instrumented distinction between repeated
and independently failing roads, the measured limits of that instrument, and the
operational criterion later experiments were able to meet. The synthesis --
contact as control over the view-generating process rather than first-handed
authorship -- is an interpretation of the theory and the combined experimental
record, not a novelty claim for any one run.

Primary reading and exact links are collected in the repository's
[`references/LITERATURE_MAP.md`](../references/LITERATURE_MAP.md). The canonical
claim boundary is maintained in
[`canonical/RESULTS_CANONICAL.md`](../canonical/RESULTS_CANONICAL.md),
[`canonical/CLAIM_LEDGER.md`](../canonical/CLAIM_LEDGER.md), and
[`canonical/KILL_MATRIX.md`](../canonical/KILL_MATRIX.md). The authorial
continuation boundary is recorded separately in
[`canonical/AUTHOR_ROUTE_DECISION.md`](../canonical/AUTHOR_ROUTE_DECISION.md).
