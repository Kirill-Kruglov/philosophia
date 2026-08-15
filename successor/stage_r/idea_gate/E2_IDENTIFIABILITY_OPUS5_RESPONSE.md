# E2 IDENTIFIABILITY — TASK A

## Findings

**F1. A complete minimal construction exists.** A semiautomaton *entry-coverage* cell with a non-abelian primitive set identifies the reciprocal recipient×source interaction without an oracle channel. It is given in §§1–7.

**F2. Non-tautology is conditional, not free.** Under the *natural* parameterization — seed-random gaps, equal aggregate competence, self-uncertainty selector, uniform held-out demand — `D > 0` is forced by symmetry and the "experiment" measures my own arithmetic. The cell is admissible **only** with a prospectively registered generator family whose uncertainty–demand alignment is not fixed at 1. That family is the empirical residue. Registering it before any run is mandatory; choosing the uniform generator makes the result analytic and it must not be run.

**F3. The killing attack is degeneracy, not leakage.** Every forbidden channel can be closed cleanly (§7). The live threat is that same-architecture different-seed twins fail on nearly the same items — the line's own inherited 24/12/0 result and the error-consistency literature both predict this. If discordance is below floor, `D ≡ 0` as an instrument verdict, not a scientific null.

**F4. The difficulty×competence confound is not removed by reciprocity.** It is an interaction and does not cancel. It can be *nulled at first order* by an aggregate-competence matching gate, and only then. Without that gate a positive `D` is unreadable. With it, `D` still means "state-dependent task value", never "epistemic content". This is a scope limit, not an identifiability failure.

**F5. Composition must be combinatorial, not depth.** Held-out items must require ordered primitive *pairs* absent from training, not merely longer words. Length extrapolation is Rajaraman et al. II and is occupied.

**F6. Proof-irrelevance is real and should be conceded, not dressed.** Traces here are deterministic; there is exactly one witness per item. The verifier makes work objective; it does not make this a proof-search cell. No "proof diversity" claim is available or needed.

**F7. The cheapest kill precedes any harness** and is a forward-pass measurement (§9), not a reciprocal block.

---

## The construction

### 1. Objects, verifier, erasure

Fix state set `Q`, `|Q| = q`; primitives `g_1..g_m`, each a permutation of `Q`, generating a **non-abelian** group. Registered admissibility check, analytic: the map (multiset of primitives) → terminal state must be many-to-one on the item length used. A task is `x = (s_0, u)`, `u ∈ [m]^L`. Answer is `s_0·g_{u_1}⋯g_{u_L}`. The *trace* is `s_0,…,s_L`. The verifier evaluates the trace against the primitive tables — deterministic, independent of the learner, no search.

**Public erasure.** Public bytes of an item are exactly `(s_0, u)`. Traces, intermediate states, the entry set `E(x)` (below), primitive tables and held-out membership are sealed.

### 2. What composes, and why it is not a count, key, ID or label

Define the **entry** `(i, s)` = "the value of `g_i(s)`". Item `x` touches `E(x) = {(u_t, s_{t-1})}`, `|E(x)| ≤ L`.

- **Not token counts.** Non-abelian generation ⇒ the multiset of `u` does not determine `s_L`. This is the exact defect that voided the walk world (essay VI.4: displacement is `#R − #L`, already in the input); it is closed here by construction and checked analytically before anything is built.
- **Not a lookup key.** Entries are *shared across items*. Knowledge transfers only through the entry inventory, never through item identity.
- **Not a public task ID.** `E(x)` is not a function of `u` alone: which entries an item touches depends on the intermediate states, which depend on the primitives. Two items with identical `u` and different `s_0` touch different entries.
- **Not a hidden-label oracle.** No skill labels exist; "skill" is exactly entry knowledge, which is never exposed.
- **Compositional, not deep.** The identity of the entries an item needs is itself produced by composing earlier entries. Depth alone does not create new entries; new *ordered pairs* do.

### 3. Learner, reservoir, selector, update, endpoint

- **State `w`**: parameters of a small predictor `f_w: (s_0,u) → Q`, trained from scratch. Not a set of known entries — that would be a direct encoding of the missing rule and is disqualified by §7.
- **Reservoir `R`**: a sealed public pool of items, all public bytes only.
- **Selector `S(w,x)`**: a self-uncertainty score computed from `f_w`'s own output distribution on `x`'s public bytes — no oracle call, no verifier call, no trace. Batch = top-`b` by score within registered strata, item-addressed tie-break.
- **Update `U`**: one aggregate supervised update on the selected batch with verifier-supplied answers; equal budget and equal update ceiling across branches; one update, not a curriculum.
- **Endpoint `X`**: capped verifier/oracle work to certainty on a sealed held-out panel `H`, `X(w) = Σ_{y∈H} min(cost(w,y), C)`, where `cost` counts oracle queries the learner must issue to answer `y` with certainty. Lower is better.

### 4. Twins, divergence, four branches

Twins `A,B` from independent initializations, identical architecture, configuration and pre-divergence protocol. Divergence source is seed only. Both are frozen, then each scores the *same* `R` and yields `b_A`, `b_B`. Four branches from the same frozen recipient states: `A←A, A←B, B←A, B←B`, equal budgets, one update each, evaluated on the *same* `H`.

**Mandatory pre-gates** (both outcome-blind): (i) aggregate-competence match `|acc_A − acc_B| ≤ ε`; (ii) batch divergence `Jaccard(b_A,b_B) ≤ τ`. Failing (i) makes `D` unreadable (F4); failing (ii) is `CELL_CANNOT_HOST`.

### 5. Disjointness that preserves transfer

`R` and `H` share the **primitive inventory** (`g_1..g_m`) and are disjoint in **ordered primitive bigrams** and in item identity. Shared structure that makes transfer possible: the entries. Deleted structure that would make it memorization: the bigram combinations and the items. Disjointness is on public bytes and on bigram sets, both sealed before selection.

### 6. Causal graph and cancellation

`X_{r←q} = μ + ρ_r + β_q + γ_{rq} + ε`, with `ρ` recipient competence, `β` intrinsic batch quality, `γ` the interaction.

`D = ½[(X_{A←B} − X_{A←A}) + (X_{B←A} − X_{B←B})] = ½[(γ_{AB} − γ_{AA}) + (γ_{BA} − γ_{BB})]`.

Cancels: `ρ_A`, `ρ_B` **within** each recipient's difference; `β_A`, `β_B` **between** the two differences. The batch-quality cancellation is between-recipient and therefore requires additivity on the registered analysis scale; capping `X` at `C` is nonlinear and can break it, so cap-hit rates must be reported per branch and differential censoring must block a directional reading.

Does **not** cancel: `γ` from difficulty×competence (F4), which is why gate (i) exists; and any recipient-specific noise correlated with selection.

### 7. Every channel available to `S`

Permitted: public item bytes `(s_0,u)`; the recipient's own forward outputs on those bytes; registered stratum labels computable from public bytes alone (e.g. `L`); frozen normalization statistics.

Forbidden, and each sealed: traces/witnesses; `E(x)`; primitive tables; held-out membership, bigrams or dependencies; the other twin's state; verifier answers on `R`; any latent skill label; any direct encoding of `w`'s missing entries (this disqualifies the "known-entry set" learner outright); post-update outcomes.

---

## 8. Two admissible parameterizations

Let `α ∈ [0,1]` be the registered **uncertainty–demand alignment** of the generator: the probability that a reservoir item scoring high under a twin's own uncertainty carries bigrams whose entries are demanded by `H`, versus lying in a registered **decoy stratum** whose entries `H` never demands.

- **`α = 1` (aligned): `D > 0`.** High-self-uncertainty items are exactly the ones covering that twin's `H`-relevant gaps. `b_A` covers `A`'s gaps, `b_B` covers `B`'s; gaps differ; so `X_{A←B} > X_{A←A}` and symmetrically. Positive.
- **`α = 0` (decoy-dominated): `D < 0`.** Each twin's highest self-uncertainty concentrates in the decoy stratum, so `b_A` teaches `A` nothing `H` demands, while `b_B`, selected from a *different* gap profile, incidentally covers `H`-relevant entries for `A`. Then `X_{A←B} < X_{A←A}`; symmetrically. Negative.
- **`α` intermediate with `H`-demand common to both twins: `D = 0`.** Both batches cover the same demanded entries; the interaction vanishes while both main effects persist.

These are admissible parameterizations of one fixed generator family, not different worlds. **The registered estimand must therefore be over a prospectively fixed mixture on `α` that is not the point mass at 1.** Under the point mass at 1 the contrast is analytic and the cell is tautological — this is the single condition on which non-tautology rests.

### Attacks

- *Proof-irrelevance*: conceded (F6); no witness-diversity claim is made and none is needed.
- *Surface shortcut*: `L` and other public-byte statistics are the registered stratum; the selector must show incremental predictive value beyond a statement-only regressor or the selector route closes.
- *Hand-coded difficulty matching*: nulled by gate (i); without it, unreadable.
- *Global contradiction*: structurally absent — no `false`, no vacuity channel.
- *Leakage*: closed by §7's sealed list plus public-bytes-only selection.
- *Merely syntactic depth*: excluded by bigram-disjointness (§5).

## 9. Smallest pre-harness kill

Train two seeds to matched aggregate accuracy on `R`. With **forward passes only** — no reciprocal block, no update, no `H` evaluation, no verifier work — measure (a) item-level error discordance between twins on `R`, and (b) `Jaccard(b_A,b_B)` from the self-uncertainty selector. If discordance or batch divergence sits below a registered floor, the twins cannot select differently and `D ≡ 0` by degeneracy: the carrier dies before any harness exists. Given the line's own 24/12/0 result and error consistency across seeds, this has a substantial prior of firing — which is precisely why it must run first.

A second, purely analytic pre-check kills the carrier for free: if the primitive set fails the non-abelian many-to-one test of §1, the answer is a count and the cell is void by construction, as the walk world was.

---

`E2_IDENTIFIABLE_FOR_DISPOSABLE_PROBE_A`
