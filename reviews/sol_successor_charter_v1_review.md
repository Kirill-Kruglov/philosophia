`REVISE_SUCCESSOR_CHARTER_V1`

# Successor charter v1 — Y-line statistical and identifiability review

Review anchor: commit `6e3de4d91a8040b5d56481927dd51533d08cf043`.
This is a bounded review of the charter's inferential contract. It does not
reopen Route B, the five signed author tokens, or the stopped Level 1 line.

## Ordered findings

### Critical

1. **Q has no family-level false-pass control.** Fresh worlds per attempt do
   not by themselves control the probability that adaptive candidate search
   eventually produces a qualifier. The draft leaves the total and
   per-candidate caps open but does not require a charter-level tolerance for
   the event “at least one population-incompetent candidate passes,” an
   attempt-wise spending rule, a sample-size/confidence guarantee, or a
   candidate-equivalence rule. Calling Q non-citable does not remove this
   obligation: Q is the load-bearing assurance that spending C is reasonable.

2. **The public dev-root defeats the stated freshness property for Q.** If the
   root and domain map are public before candidate freeze, every nominally
   future Q world is computable during T. Disjoint indices then prevent literal
   reuse but not registry overfitting. Each Q sample must instead depend on
   randomness unavailable until after the candidate manifest and attempt claim
   are durably frozen, under a fixed sampling contract and a no-redraw rule.

3. **The scout bridge is not safe as written.** Arm-specific censoring,
   variance, or resource aggregates can identify arms and reveal direction or
   effect magnitude; with a right-censored RMST endpoint, arm-specific
   censoring is itself outcome information. Allowing the scout to inform
   budget or margins would tune the estimand or scientific meaning around the
   promoted candidate. A separate scout surface may support only a
   preregistered, arm-label-invariant nuisance calculation for sample size and
   label-free engineering resources. The endpoint horizon and all scientific
   margins must be frozen before the scout. Optionality is valid only with a
   predeclared non-scout fallback for every affected numeric cell.

4. **“One candidate, one confirmation” does not eliminate confirmatory
   multiplicity.** It removes a candidate-level second chance, but C1 still
   uses ACTIVE, YOKED, and static contrasts, and C2–C5 contain multiple
   superiority, equivalence, non-superiority, presentation, ledger, and path
   predicates. The charter must assign those comparisons to multiplicity
   families and require simultaneous inference, closed testing, or locked
   gatekeeping before any relevant data. Otherwise a selected design could
   accumulate `PROOF_CORE` or `PROOF_STRONG` through undeclared tests.

### Major

5. **The selection-conditional estimand is named but not defined.** The draft
   does not say exactly what history is conditioned on, what randomness is
   averaged over, or what population receives the claim. Conditionality is not
   a footnote. It belongs in the estimand and in the scope object attached to
   every C verdict. Confirmation can support the selected, frozen design on
   the locked C population; it cannot validate the learner class, candidate
   generator, promotion procedure, or an unselected design.

6. **“Same construct” is not a population contract.** Parameter-space
   disjointness does not imply exchangeability. The later contracts must define
   the world/block unit, frame or generator, target measure, strata, weights,
   inclusion probabilities, seed/device conditioning, and whether C is a
   finite-frame sample, a census, or a superpopulation sample. Q and C must be
   disjoint draws from a common target superpopulation or be connected by a
   predeclared transport guarantee; otherwise Q competence is not informative
   about C spendability.

7. **The Q predicate's present shape is too weak to prevent candidate-shaped
   qualification.** “Endpoint-shaped, binary, validity-first” leaves the
   competence null, aggregation unit, threshold, budget, and generalization
   guarantee free after arbitrary T outcomes are known. The later Q contract
   may own numeric values, but it must instantiate a charter-fixed operational
   meaning and use one invariant rule for every candidate, attempt, and stack.
   Its scientific thresholds may not be justified from candidate-specific T
   arm outcomes. Stack-specific engineering caps must be separate from the
   competence predicate.

8. **The terminal taxonomy is not yet exclusive and total.** In particular,
   “no automatic rerun” conflicts with Q attempts being “individually
   recoverable”; Q failure is not separated from Q invalidity; no-qualifier cap
   exhaustion is not separated from T-envelope exhaustion; and missing data,
   non-finite learner states, resource stops, malformed escrow, and recovery's
   effect on caps are not fully assigned. Every launched Q attempt must consume
   its attempt identity and cap slot, and no C process/resource state may become
   scientific censoring or a boundary.

9. **Promotion and device freeze leave post-Q discretion.** Author selection
   from a qualified set remains statistically interpretable only after
   conditioning on everything the author saw, but it is the higher-risk route.
   The lower-risk rule is automatic promotion of the first valid qualifier
   under a preregistered serial queue. The exact stack tested in Q must already
   be part of the frozen candidate; promotion freezes that tested stack rather
   than permitting a post-Q stack change. A changed stack is a new candidate
   and must qualify under the common caps.

### Minor

10. **C randomness timing needs one unambiguous sentence.** The C frame,
    generator, strata, weights, domain separation, and root-generation
    protocol are fixed before T; the secret root value and C membership are
    generated once only after the complete scientific lock. Thus the contract
    exists before lock but the entropy does not.

11. **Process endings need stable names.** “Development did not produce a
    qualifiable learner” is acceptable prose, but the record must distinguish
    `T_ENVELOPE_EXHAUSTED`, `Q_CAP_EXHAUSTED_NO_QUALIFIER`, and `AUTHOR_STOP`.
    None is scientific `INSUFFICIENT`, a C1 boundary, or evidence that no
    competent learner exists.

These defects require charter revision, not a Route B boundary block: the
three-surface successor architecture, separate C1, non-citability of T/Q, and
independently locked confirmation all remain compatible with the five exact
Route B tokens.

## A. Exact confirmatory estimand after selection

Let `H_TQ` be the complete record that the promotion rule is allowed to consume:
all T choices and observations, candidate-registry history, all Q attempt
identities, validity states and released outputs, the stopping history, and the
promotion rule. Let `H_preC` extend `H_TQ` with the permitted scout, device
freeze, spec, review, and signature history through the scientific lock. Let

- `d* = R(H_TQ)` be the one promoted content-addressed candidate;
- `s*` be its exact Q-qualified device/software stack;
- `L*` be the later locked scientific design, endpoint, analysis, seeds or seed
  law, and treatment implementations; and
- `P_C` be the locked C target measure (or the corresponding weighted finite
  frame).

For arm `a`, write `Y_a(w; d*, s*, L*)` for the locked, right-censored
budget-to-certified-competence outcome on C unit `w`. In the ACTIVE-versus-YOKED
orientation, the selected-design C1 estimand is

```text
Delta_C1^sel(H_preC)
  = E_{w ~ P_C}[Y_YOKED(w; d*,s*,L*) - Y_ACTIVE(w; d*,s*,L*)
                | H_preC, d*=R(H_TQ), s*, L*].
```

The expectation additionally averages only over a seed law explicitly placed
inside `L*`; if seeds are fixed, the estimand is seed-conditioned. For a finite
frame, the expectation is replaced by the locked design-weighted frame mean;
for a census it is descriptive of that frame. Because the C sample is drawn
independently after selection under the locked design, ordinary design-based or
model-based inference may be conditionally valid for this fixed `d*`. The
selection event is not erased: the claim does not average over the adaptive
candidate generator and does not estimate the probability that Route B finds a
good design.

Conditionality must be part of the estimand and a machine-readable `scope_id`
attached to every scientific verdict, not a footnote. The symbolic verdict may
remain short, but its record and public sentence must identify the candidate,
T/Q-history commitment, promotion rule, stack, scientific lock, and C
population contract.

Permitted future claim wording is:

> For the adaptively selected and subsequently locked successor design
> `[candidate_id]` on `[stack_id]`, conditional on the committed
> pre-confirmation history and promotion rule `[selection_scope_id]`, the
> preregistered confirmation on
> fresh C units sampled from `[C_population_id]` estimated the locked
> ACTIVE-versus-YOKED effect as `[locked result language]`. This confirms or
> fails to confirm that effect for this selected design and C population only;
> it does not validate the candidate-search procedure, a learner class, or any
> unselected design.

Forbidden are “the search procedure works,” “the learner class works,” “Route B
was confirmed,” and generalization beyond the locked C population or seed/device
scope.

## B. Qualification multiplicity

Suppose attempt `j` tests a candidate that is incompetent under the common Q
population criterion. The Q contract must guarantee, conditional on all prior
adaptive history and candidate freeze,

```text
Pr(Q_PASS_j | past, candidate j is Q-incompetent) <= alpha_Q,j,
sum over every launchable attempt alpha_Q,j <= delta_Q.
```

Then the union bound (or a predeclared always-valid sequential equivalent)
gives

```text
Pr(any Q-incompetent candidate ever passes) <= delta_Q
```

despite adaptive candidate generation. This is the guarantee Q needs: not a C1
type-I claim, but a family-level assurance that the promoted candidate exceeds
the predeclared population competence floor with controlled false-pass risk.
It does not establish an arm effect and remains permanently non-citable for
C1–C6.

Charter-level obligations are: a finite total launch cap; a finite
per-candidate/equivalence-class cap; a family false-pass tolerance; fresh
post-freeze Q sampling; no Q-world reuse or redraw; and a canonical candidate
equivalence rule. The later Q contract owns the numeric caps and tolerance, the
attempt-wise alpha-spending or sequential method, Q sample size, confidence
construction, and exact predicate numerics. A simple low-risk implementation is
one valid opportunity per canonical candidate equivalence class plus a fixed
total launch cap and prespecified Bonferroni/alpha spending. Holdout reuse is
forbidden.

The equivalence rule must canonicalize the executable scientific manifest.
Changes only to names, comments, packaging, timestamps, serialization order, or
other behavior-inert metadata do not reset a candidate's cap. Any change that
can alter Q or C potential outcomes creates a new candidate but still consumes
the common total cap. Every launched attempt consumes its attempt id and total
cap slot; invalidity cannot be used to erase a look.

## C. Q information and freshness

Future Q worlds are predictable if they are derived solely from the public
dev-root available during T. The necessary independence is

```text
W_Q,j independent of (candidate_j, H_TQ before attempt j)
given the precommitted Q frame, sampler, strata, weights, and attempt id.
```

The sampler and its domains may be public; the attempt's randomness must not be
available before durable candidate/attempt freeze. A post-freeze public
randomness beacon is valid only if the beacon event and deterministic mapping
are committed before the beacon is realized and the researcher cannot choose
among beacon events. A sealed post-freeze root is also valid if its one-shot
generation, custody, attestation, and later audit are fixed. In either design,
one attempt gets one sample, the sample is never reused, and generation or
attestation failure is Q process invalidity with no redraw of that attempt.

The public dev-root may continue to serve T. It cannot be the sole entropy for
Q.

## D. Promotion rule

| Rule | Conditioning required in C | Permitted Q input | Interpretation |
|---|---|---|---|
| Author selects after seeing a closed qualified set | condition on the full closed-set rule, every author-visible T/Q fact, closure timing, and the realized author choice | eligibility binary necessarily; resource/validity facts only if their role was fixed before Q; no hidden Q statistic | valid only for the selected locked design on fresh C; says nothing about author-selection quality or other qualifiers |
| First valid qualifier, fixed before Q | condition on the serial candidate order, prior failures/invalidities, stopping event, and automatic promotion | pass/fail/validity needed by the fixed rule; resource fields only as predeclared validity/cap checks | valid for the selected locked design; lower discretion and simpler audit, but still no claim about the search procedure |

The recommended lower-risk rule is: a serial, durably ordered attempt queue;
the first valid `Q_PASS` automatically closes Q and is promoted; no simultaneous
attempts; no author choice after a pass. Adaptive T still determines which
candidate is submitted next, so selection conditioning remains necessary.

The exact candidate manifest, including device/software stack, must freeze
before its Q draw. Promotion freezes that already qualified stack. Q resource
aggregates cannot rank candidates or change promotion; they may only apply
predeclared resource-validity gates. A stack change is a new candidate and a
new capped attempt.

## E. Scout identifiability and leakage

Arm-specific censoring rates, RMST variances, event counts, resource traces, or
sample sizes are not direction-free merely because means are omitted. Censoring
and bounded-time distributions encode performance, and treatment machinery can
deblind an otherwise unnamed arm. The bridge is admissible only under this
enforceable contract:

- the scout uses a separately domain-separated sample disjoint from all T, Q
  attempts, and C, and is never reused;
- the candidate, stack, C population contract, endpoint horizon, treatment
  definitions, contrast family, margins, and analysis method freeze before the
  scout;
- a sealed evaluator may compute only a preregistered nuisance function proved
  invariant to arm-label permutations and sign reversal of every locked
  contrast;
- the public output is limited to validity, a direct sample-size value selected
  by the precommitted recalculation rule, and label-free aggregate engineering
  resources. If a nuisance scalar is released instead, its range and invariance
  proof must be locked in advance;
- no arm-specific or candidate-level means, censor counts, quantiles, losses,
  contrasts, intervals, scores, series, or resource fields are released;
- margins and endpoint budget are never scout-informed; sample size may be
  recalculated from blinded nuisance variation only through the locked rule;
  and
- the scout raw surface remains sealed until after C's terminal decision and is
  permanently non-citable.

A blinded pooled nuisance estimate can be sufficient if the future inference
method proves it sufficient and the recalculation function is locked before the
scout. If paired/block contrast variance is needed, the evaluator may calculate
a centered variance internally, but may release only the invariant scalar or
the deterministic sample-size output, never its sign-bearing mean. If no
adequate invariant estimator exists, the scout cannot be used for that cell.

The scout can remain optional only if the spec gate predeclares an external or
conservative fallback for sample size and resource caps. Without that fallback,
“optional” leaves the confirmatory numerics without admissible provenance and
must be replaced by a mandatory scout gate. It may never source a margin.

## F. T/Q/C population contract

Before any T world generation, later documents must pin these mathematical
objects without yet needing to realize any world:

1. the elementary world or inferential block, including target/donor roles and
   the treatment potential outcomes attached to it;
2. a versioned construct generator or finite sampling frame `Omega`, with the
   admissible parameter support and exclusion rules;
3. the target C measure `P_C`, or finite-frame strata `Omega_C,h`, inclusion
   probabilities, analysis weights, and finite-population correction;
4. T/Q/C partition rules and domain separation, distinguishing set
   disjointness from distributional exchangeability;
5. Q's target measure `P_Q` and either `P_Q = P_C` at the superpopulation and
   stratum-weight level or a predeclared transport/conservatism relation that
   makes Q competence informative about C;
6. the candidate/world interaction estimand and any predeclared heterogeneity
   or stratum summaries, with their multiplicity ownership;
7. whether learner seeds are fixed and conditioned on or sampled from a locked
   seed distribution; and
8. exactly one C interpretation: a fixed-frame census, a probability sample
   from a fixed finite frame, or an i.i.d./stratified sample from a named
   superpopulation.

T, Q, and C must be disjoint in realized units. Q and C should share the same
target superpopulation and stratum weights while remaining disjoint unless an
explicit transport contract is reviewed. T may deliberately differ, but then
it supports no population claim. A generator or support change after these
objects freeze defines a new estimand and requires a loud pre-data amendment;
it cannot be treated as another draw from the old population.

The C sampling contract and secret-root generation protocol are fixed before T.
The root value is generated once after the complete scientific lock, and its
deterministic C membership is never redrawn.

## G. Competence predicate

The endpoint-shaped binary skeleton may be charter-fixed while numeric values
are deferred, but the present skeleton is incomplete. The charter must fix Q's
meaning as a population assurance predicate: under the exact frozen candidate
and stack, the probability/mean of achieving the operational certificate within
the fixed Q budget on a fresh unit from `P_Q` exceeds a common minimum needed to
make C spendable. The later Q contract must define the null, unit, aggregation,
certificate, horizon, threshold, sample size, confidence rule, family
false-pass tolerance, and all missing/non-finite handling before the first Q
attempt.

One rule applies to every candidate, equivalence class, attempt, and device
stack. Numeric competence cells may not be moved in response to a candidate's
T arm contrast or candidate-specific endpoint performance. Device-dependent
wall, memory, and reproducibility limits are separately signed engineering
validity gates; they cannot weaken the scientific competence floor. Changing
the competence meaning or numerics after any Q attempt voids the Q contract and
does not preserve previous qualifiers.

## H. Validity, censoring, and process endings

The future state machine must be exclusive and total:

| Surface | Valid terminal or ending | Invalid terminal | Meaning and recovery |
|---|---|---|---|
| T | `T_ENVELOPE_EXHAUSTED`, `T_AUTHOR_STOP`, or candidate submitted | typed environment/resource/process/hash failure in T infrastructure | engineering only; T may recover inside its signed envelope; no C1–C6 field exists |
| Q attempt | `Q_VALID_PASS` or `Q_VALID_FAIL` after complete valid evaluation | `Q_INVALID:<ENVIRONMENT\|RESOURCE\|PROCESS\|HASH\|SEAL>` with qualification binary unset | pass/fail uses the common competence rule; every launch consumes its id, alpha allocation, and total-cap slot; invalidity is not fail and permits no redraw or automatic rerun |
| Q phase | first valid pass promotes, or `Q_CAP_EXHAUSTED_NO_QUALIFIER` | contract/hash failure may end the phase | no qualifier is a process/gate ending, not `INSUFFICIENT`, a learner impossibility claim, or a scientific boundary |
| C escrow | one valid attested ciphertext/root commitment | `C_ESCROW_INVALID:<cause>` | malformed/missing escrow ends that artifact; no scientific field and no automatic regeneration |
| C execution | only a valid completed run may produce a scientific pass, null, boundary, `INSUFFICIENT`, or the spec's right-censored terminal | `C_INVALID:<ENVIRONMENT\|RESOURCE\|PROCESS\|HASH\|SEAL>` with all scientific outcome fields unset | no invalid state is censoring or a boundary; no automatic rerun |

The Q contract must classify non-finiteness before data: a finite, correctly
executed learner divergence may count as `Q_VALID_FAIL` only if it is explicitly
part of the competence predicate; hardware/numerical-environment failure is
invalidity. The C spec must make the same scientific-versus-process distinction
before lock. Missing required observations or a malformed report are process
invalidity unless a missingness rule was explicitly built into the scientific
endpoint. Scientific censoring is available only after all C validity, seal,
completeness, and persistence predicates pass.

“Recoverable Q process” means only that the still-open line may submit a new,
separately claimed attempt under the pre-signed caps and spending rule. It never
means deleting, replacing, or redrawing the failed attempt. No process state
may be narrated as a scientific wall or boundary.

## I. Proof semantics and multiplicity at C

Before any scout or data relevant to a family, the successor claim graph and
level specifications must assign:

1. **C1/contact-mode family:** every ACTIVE/YOKED/static superiority,
   equivalence, and non-superiority predicate used either for C1 or operational
   mode selection, controlled by simultaneous intervals, closed testing, or a
   locked hierarchical rule. Static cannot become an undeclared alternative
   route to a positive C1 claim.
2. **C2–C4 family:** every same- and destination-presentation contrast, anchor,
   weights, inherited-ledger, placebo, superiority, equivalence, and
   non-superiority predicate entering the priority cascade, with joint coverage
   or a closed gatekeeping procedure.
3. **C5 family:** every registered path-credit contrast and any subgroup or
   robustness predicate capable of earning or denying C5.
4. **C6 reporting family:** C6 remains annotation-only. Any inferential C6
   subclaims must have their own multiplicity control and can never grant,
   veto, or rescue proof.
5. **Proof composition:** `PROOF_CORE = C2 AND C3 AND C4` and
   `PROOF_STRONG = PROOF_CORE AND C1 AND C5` remain conjunctions. An
   intersection-union/gatekeeping argument may exploit that conjunction, but
   only after each component's internal family is validly controlled. If the
   programme also publishes the component claims as a family, its familywise
   error must be allocated or closed explicitly.

Numeric alpha and margins may wait for their owning pre-data spec gates. Family
membership, primary-versus-secondary status, and who freezes the control method
may not wait until results. Reusing C data for unregistered candidate,
subgroup, endpoint, margin, or proof routes is forbidden.

## Phase-by-phase sampling and multiplicity contract

| Phase | Sampling/independence object | Statistical obligation | Citable scope |
|---|---|---|---|
| T | public T frame/domains; arbitrary adaptive reuse inside signed envelope | no scientific type-I claim; engineering checks may be descriptive; all outcomes permanently non-citable | engineering only |
| Candidate freeze | content-addressed executable manifest including stack, committed before Q randomness | canonical equivalence class and attempt order fixed | none |
| Q | unpredictable post-freeze fresh sample from `P_Q`; no reuse/redraw; disjoint from T/C | family false-pass guarantee `sum alpha_Q,j <= delta_Q`, finite caps, common competence null and confidence rule | gate assurance only; never C1–C6 |
| Promotion | fixed serial first-valid-qualifier rule; complete selection event committed | no effect selection from Q; record all conditioning variables | identifies `d*`, not an effect |
| Q scout | separate fresh Q-scout domain, disjoint from Q attempts and C | blinded permutation/sign-invariant nuisance rule; no hypothesis verdict; B/margins frozen; sample-size rule fixed | non-citable design input only |
| C1 confirmation | post-lock one-shot sample/census under `P_C`, independent of selection history conditional on lock | locked C1/contact-mode multiplicity family; design weights/strata; validity-first endpoints | selected design, stack, seeds, and C population only |
| C2–C4 confirmation | fresh locked surface and population contract owned by its level | jointly controlled C2–C4 cascade family | selected locked design and registered population only |
| C5 confirmation | fresh locked surface and registered path family | C5 family control | selected locked design and registered population only |
| C6 | registered annotation surface | descriptive, or separately controlled if inferential | annotation only |
| Proof decision | consumes only locked family decisions | predeclared conjunction/gatekeeping; no undeclared tests | `PROOF_CORE`/`PROOF_STRONG` only if every owned family is valid |

## Exact mandatory replacement clauses

The following clauses are exact bounded repairs. They choose no numeric cell,
candidate, learner, world, device, margin, threshold, or alpha.

### R1 — replace the §3 named honesty clause

> **Selected-design conditionality (load-bearing):** Let `H_TQ` be the complete
> committed T/Q registry, attempt, validity, released-output, stopping, and
> promotion history, and let `H_preC` extend it through every permitted scout,
> device-freeze, spec, review, and signature decision in the scientific lock;
> let `d* = R(H_TQ)` be the promoted content-addressed candidate; let `s*` be
> its Q-qualified stack; and let `L*` and `P_C` be the scientific lock and C
> population contract. Every confirmatory estimand and verdict is conditional
> on the realized `H_preC`, `d*`, `s*`, and `L*`, and
> averages only over the worlds and any seed law named by `P_C` and `L*`. Every
> verdict record carries a `selection_scope_id` hashing those objects. A
> confirmation can support an effect for that selected locked design on that C
> population; it cannot validate the candidate generator, promotion procedure,
> learner class, or any unselected design. T and Q remain permanently
> non-citable for C1–C6.

### R2 — replace the Q repeat-policy and Q-root sentences in §§4, 5, and 9

> **Qualification family guarantee:** Before the first Q attempt, the signed Q
> contract fixes a finite total launch cap, a finite per-canonical-candidate cap,
> a family competence false-pass tolerance, and an attempt-wise alpha-spending
> or always-valid sequential rule whose total is bounded by that tolerance.
> Conditional on all adaptive prior history, each attempt's test is valid for a
> candidate frozen before its Q randomness. Candidate equivalence is determined
> from a canonical executable scientific manifest: behavior-inert metadata
> changes never reset a cap; behavior-relevant changes create a new candidate
> but remain inside the total cap. Every launch consumes its attempt id, error
> allocation, and total-cap slot, including an invalid launch. Q worlds are
> never reused or redrawn.
>
> **Qualification freshness:** T may use the public successor dev-root. Each Q
> attempt instead receives one sample from the precommitted Q frame using
> randomness unavailable until after durable candidate-manifest and attempt
> freeze. The source may be a precommitted post-freeze public beacon or a
> one-shot sealed root under reviewed custody; its event, mapping, strata, and
> no-redraw rule are fixed before use. The resulting Q sample is independent of
> the frozen candidate and prior T/Q history conditional on the sampling
> contract. Generation or attestation failure is typed Q invalidity and never
> authorizes a redraw.

### R3 — replace the §5 promotion paragraph and reconcile §6 stack timing

> **Promotion and stack freeze:** Q attempts are serial in their durable ledger.
> The first valid `Q_PASS` automatically closes Q and promotes that candidate;
> no author-visible statistic or post-pass choice ranks qualifiers, and no
> simultaneous attempts are permitted. The candidate's exact device/software
> stack is part of its manifest and freezes before the attempt's Q randomness;
> promotion adopts that already qualified stack. A stack change is a
> behavior-relevant candidate change, requires a new capped Q attempt, and
> invalidates any prior qualification for promotion. Q validity and
> predeclared resource caps may determine eligibility, but Q resource
> aggregates cannot rank candidates or alter promotion.

### R4 — replace the optional design-scout paragraph

> **Optional blinded nuisance scout:** After promotion and before scientific
> lock, a separately domain-separated scout may use fresh worlds disjoint from
> T, every Q attempt, and C. Before it begins, the candidate and stack, C
> population contract, endpoint horizon, treatment definitions, contrast
> family, margins, analysis method, nuisance estimator, and sample-size
> recalculation rule are frozen. A sealed evaluator may compute only a function
> proved invariant to every arm-label permutation and locked-contrast sign
> reversal. The released surface is limited to validity, the deterministic
> sample-size output (or a prebounded invariant nuisance scalar), and label-free
> aggregate engineering resources. No arm-specific censoring, events, RMST,
> moments, quantiles, losses, scores, series, contrasts, intervals, or resource
> fields are released. The scout may inform sample size and engineering caps
> only; it may never inform the endpoint budget, margin, treatment, population,
> or analysis rule. Raw scout data remain sealed until after C's terminal
> decision and permanently non-citable. Every scout-dependent numeric has a
> predeclared external or conservative fallback; absent such a fallback, the
> scout is mandatory rather than optional.

### R5 — add to §§4 and 9 before any T-world generation

> **Population and sampling contract:** Before T generation, a signed contract
> fixes the elementary world/block unit; versioned frame or generator;
> admissible support; T/Q/C partition; target C measure or finite-frame strata,
> weights, and inclusion probabilities; Q target measure and its common-
> population or transport relation to C; candidate/world interaction estimand;
> seed conditioning or seed law; and exactly one C interpretation (finite-frame
> census, finite-frame probability sample, or named superpopulation sample).
> Realized T, Q, scout, and C units are disjoint. Disjointness alone is not
> called exchangeability. Any generator, support, strata, or weight change after
> this freeze defines a new estimand and requires a loud pre-data amendment.
> The C sampler and root-generation protocol are fixed before T; the secret root
> value and resulting C membership are generated once only after the complete
> scientific lock and are never redrawn.

### R6 — replace the Q competence-entry paragraph

> **Invariant competence predicate:** Q is a population assurance gate that the
> exact candidate and stack exceed one common minimum operational competence
> requirement on fresh units from the signed Q target measure, within the fixed
> Q horizon, strongly enough to make C spendable. Before the first Q attempt,
> the Q contract fixes the null, unit, aggregation, operational certificate,
> horizon, threshold, sample size or confidence guarantee, family false-pass
> tolerance, validity rules, and missing/non-finite handling. The rule is
> identical across candidates, equivalence classes, attempts, and stacks.
> Competence numerics may not be chosen or justified from any observed T
> performance, informal arm contrast, or candidate-specific outcome, and may
> not be moved after any Q attempt. Stack-specific wall, memory, and reproducibility
> limits are separate engineering-validity gates and cannot weaken competence.

### R7 — replace §8's Q/C recovery language

> **Exclusive terminals and recovery:** A complete valid Q attempt yields only
> `Q_VALID_PASS` or `Q_VALID_FAIL`; environment, resource, process, hash, or seal
> failure yields `Q_INVALID:<cause>` with the qualification binary unset. Every
> launched attempt consumes its immutable id, error allocation, and total-cap
> slot. Recovery means only a new separately claimed attempt permitted by the
> pre-signed caps; it is never deletion, replacement, reuse, redraw, or an
> automatic rerun. `Q_CAP_EXHAUSTED_NO_QUALIFIER`, `T_ENVELOPE_EXHAUSTED`, and
> `T_AUTHOR_STOP` are distinct non-scientific endings. Malformed escrow is typed
> process invalidity and is not regenerated automatically. Only a valid complete
> C execution may set a scientific pass, null, boundary, `INSUFFICIENT`, or
> censoring field. C environment/resource/process/hash/seal invalidity leaves
> every scientific field unset and authorizes no automatic rerun. Missing and
> non-finite states follow a classification signed before data; no process state
> may become censoring or a scientific boundary.

### R8 — add to §3 claim semantics

> **Multiplicity ownership:** One promoted candidate and one C execution remove
> candidate-level reconfirmation; they do not remove within-confirmation
> multiplicity. Before any data relevant to a family, the successor claim graph
> assigns (i) every ACTIVE/YOKED/static C1 and contact-selection predicate to a
> jointly controlled C1 family; (ii) every C2–C4 superiority, equivalence,
> non-superiority, presentation, anchor, ledger, and placebo predicate to a
> jointly controlled cascade family; (iii) every claim-bearing path predicate
> to a C5 family; and (iv) any inferential C6 annotation to a separate family
> that cannot alter proof. Each level's spec freezes simultaneous intervals,
> closed testing, or hierarchical gatekeeping and its numeric error allocation
> before relevant data. `PROOF_CORE` and `PROOF_STRONG` use only those validly
> controlled component decisions under a preregistered conjunction rule; no
> unregistered contrast, endpoint, subgroup, or repeated analysis may earn a
> claim.

## Cells validly deferred to later review

The following values remain genuinely open and must not be chosen by this
review:

- T envelope units and magnitude, checkpoints, and author-stop procedure;
- T/Q/C support boundaries, frame members, stratum sizes and weights, after the
  population objects and freeze timing in R5 are accepted;
- total and per-candidate Q caps, `delta_Q`, attempt allocations, Q sample size,
  confidence method, certificate numerics, and resource caps, all owned by the
  signed Q contract and constrained by R2/R6;
- the post-freeze Q randomness implementation (public beacon or sealed root),
  custody details, and attestation, subject to R2;
- learner, optimizer, acquisition rule, interface, and candidate stack choices
  inside T; none may use stopped-line v1/v2 outcomes;
- numerical device equivalence/reproducibility tolerances, fixed before the
  corresponding Q attempt;
- scout sample size, invariant nuisance estimator, recalculation bounds, and
  conservative fallback, fixed before the scout; and
- C endpoint numerics, scientific margins, arm implementation, sample size,
  alpha allocations, interval rules, escrow environment, and realized C root,
  each fixed at its owning pre-data gate. Margins and endpoint horizon are not
  scout-owned.

The selection rule, selection-scope semantics, Q family guarantee, Q freshness
property, competence invariance, population-object list, terminal taxonomy,
scout output class, and multiplicity-family ownership are not validly deferred.

## Author-token disposition

The three proposed successor tokens are **not signable against v1 as written**:

- `I_ACCEPT_PHILOSOPHIA2_CHARTER_V1` cannot accept a charter with the Critical
  gaps above;
- `I_ACCEPT_THREE_SURFACE_PHASE_ARCHITECTURE` is premature until Q is genuinely
  fresh and family-controlled and the scout is a separate nuisance-only
  surface; and
- `I_ACCEPT_SELECTION_CONDITIONAL_CONFIRMATORY_CLAIM` is too underspecified
  until R1 and R5 define the conditioning set and target population.

After the exact bounded repairs, the same three token strings may remain: the
third must be normatively defined to accept R1's selected-design estimand and
limited generalization, not merely the generic fact that selection occurred.
No token may authorize an open-cell choice or execution.

## Questions for Kirill

1. Do you accept automatic first-valid-qualifier promotion from a serial Q
   queue, or do you require a different deterministic rule fixed before Q?
2. For Q freshness, should the later contract instantiate a post-freeze public
   beacon or a one-shot sealed root under procedural custody?
3. Should C target a registered finite frame (sample or census) or a named
   superpopulation? This selects the kind of generalization, not its numeric
   boundaries.
4. Do you accept that the scout may inform only blinded sample size and
   engineering caps, never the endpoint budget or scientific margins, with a
   conservative fallback if it is skipped?

## Exact bounded questions for final confirmation

1. Did R1 land so every C estimand and verdict is scoped to the full committed
   selection history, promoted candidate, qualified stack, lock, and C
   population?
2. Did R2/R6 land with a finite Q family false-pass guarantee, canonical
   candidate equivalence, invariant competence meaning, post-freeze
   unpredictable worlds, and no reuse/redraw?
3. Did the promotion clause remove post-Q discretion and make the exact
   Q-qualified stack the promoted stack?
4. Did the scout clause freeze endpoint horizon and margins beforehand, use a
   separate disjoint surface, expose only a permutation/sign-invariant nuisance
   output, and provide a no-scout fallback?
5. Did the population clause pin all required mathematical objects and separate
   the pre-T C sampling contract from the post-lock root realization?
6. Did the terminal table make T/Q/C states exclusive and total, charge every Q
   launch to caps/error spending, and forbid any process state from becoming
   censoring or a boundary?
7. Did the multiplicity clause assign the C1/contact, C2–C4, C5, C6, and proof
   families before their data without choosing numeric alpha or margins?
8. Were all stopped-line quarantine, non-comparability, C1 first-class status,
   permanent T/Q non-citability, and confirmation-only claim movement preserved
   unchanged?

## Negative space and confirmation

The stopped line remains `OPEN` with
`BLOCKED_LEVEL1_FEASIBILITY`; C1 remains unrun and untested there. Route B is a
separate successor, not Level 1 v3, a repair, retry, replication, or comparison.
No v1/v2 outcome may select a learner, world, budget, margin, threshold,
attempt cap, alpha, promotion winner, or device. T and Q can never earn, kill,
or boundary-label C1–C6. Only a valid, independently locked C confirmation may
move successor claims, and only within its selected-design/population scope.
`PROOF_CORE` and `PROOF_STRONG` remain earned by nothing.

This review created only `reviews/sol_successor_charter_v1_review.md`. It did
not modify the charter or any existing file, did not commit, and did not create
or select code, implementation, entropy, root, world, learner, candidate,
device, budget, alpha, margin, threshold, attempt cap, development,
qualification, scout, authorization, lock, escrow, trajectory, comparative
datum, or outcome. The pre-existing user-owned `essay/OUTLINE.md` and the
pre-existing modified review-prompt file were left untouched.
