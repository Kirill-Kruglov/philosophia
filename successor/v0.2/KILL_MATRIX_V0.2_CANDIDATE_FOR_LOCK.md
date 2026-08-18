# Kill matrix v0.2 — candidate for lock

**Status:** CANDIDATE FOR LOCK — fail-closed decision surface

First applicable higher-priority invalidation/engineering terminal prevents lower scientific claims.

| Stage | Condition | Terminal/status | Permitted interpretation | Forbidden response |
|---|---|---|---|---|
| P-1 | exact Level 0 MODEL_CONFIG_REF cannot be recovered | `BLOCKED_CONFIG_PROVENANCE` | inherited learner provenance unavailable | reconstruct/tune silently |
| Pre-P0 | generator/p_flip/split/context/position/fork/D0 test fails | `BLOCKED_IMPLEMENTATION` | implementation not ready | run science anyway |
| P0 M96 | median Tfresh <2000 | `ESCALATE_TO_M128` | M96 too easy by signed selector | tune LR/WD/custom pool |
| P0 attempted scale | median Tfresh >8000 OR >2/16 capped at 20k | `INADMISSIBLE_SUBSTRATE_TOO_HARD` | cell too hard under inherited learner | hyperparameter search |
| P0 M128 | median Tfresh <2000 | `INADMISSIBLE_SUBSTRATE_TOO_EASY` | authorized scales lack headroom | add scale after data |
| P1.5 | duplicate full H1+k1 C replay differs bit-for-bit | `BLOCKED_DETERMINISM` | trajectory not reproducible | relax determinism; continue |
| P2 | k1 arm trajectory/hash differs | `INVALID_K1_ARM_DIVERGENCE` | manipulation/determinism invalid | drop seed/treat as science |
| P2 M96 | k1 median T<1000 OR >1/6 T=0 | `ESCALATE_TO_M128` | transfer floor | tune B_history |
| P2 M128 | same floor | `INADMISSIBLE_TRANSFER_FLOOR` | C too cheap after one history | call delta=0 scientific null |
| P2 | >1/6 k1 probes capped | `INADMISSIBLE_TRANSFER_CEILING` | baseline C too hard/unstable | enlarge tau post hoc |
| P3 | mechanically required N>128 | `BLOCKED_POWER` | SESOI/equivalence not affordably resolvable | run smaller confirmatory N |
| Final pre-run | final deterministic duplicate replay fails | `BLOCKED_DETERMINISM_FINAL` | locked runtime not reproducible | change backend and continue |
| Confirmatory | valid paired seeds < locked N | `INVALID_INCOMPLETE_CONFIRMATION` | confirmation incomplete | analyze smaller N as confirmatory |
| Confirmatory | unresolved trajectory/config/hash/probe mutation violation | `INVALID_CONFIRMATION` | no scientific category | exclude inconvenient runs |
| Confirmatory, no heavy cap | 95% CI lower>0 AND delta_hat>=+Delta | `ALIASED_TRANSFER_ADVANTAGE` | ALIASED regime transferred better; estimated gain reaches signed threshold | claim mechanism/full experience |
| Confirmatory, heavy cap | same positive conditions + SIGN_POS_PASS | `ALIASED_TRANSFER_ADVANTAGE_BOUNDED` | positive restricted-cost regime direction survives conservative sign gate; uncapped magnitude unavailable | claim uncapped effect size |
| Confirmatory, no heavy cap | 95% CI upper<0 AND delta_hat<=-Delta | `SEPARABLE_TRANSFER_ADVANTAGE` | SEPARABLE regime transferred better; causal component not yet decomposed | say informative separation itself caused advantage before SHUFFLED_TAG |
| Confirmatory, heavy cap | same negative conditions + SIGN_NEG_PASS | `SEPARABLE_TRANSFER_ADVANTAGE_BOUNDED` | negative restricted-cost regime direction survives conservative sign gate; component unresolved | claim uncapped magnitude or identity-specific cause |
| Confirmatory, no heavy cap | 90% CI entirely within ±Delta | `PRACTICALLY_EQUIVALENT` | meaningful differential unresolved inside signed equivalence region | call it universal no-effect |
| Confirmatory, heavy cap | neither bounded directional gate passes | `UNRESOLVED_HEAVY_CAP` | ceiling prevents equivalence/magnitude resolution | declare practical null |
| Confirmatory | valid, none above | `UNRESOLVED` | direction/magnitude not resolved | add seeds/select favorable k |
| Conditional diagnostic | required SHUFFLED_TAG not completed at locked N | `DIAGNOSTIC_INCOMPLETE` attached to primary non-positive status | primary regime status remains; component attribution forbidden | skip diagnostic and claim separation/informativeness cause |
| SHUFFLED_TAG | V resolved positive, I not | `VARIABILITY_COMPONENT_SUPPORTED` diagnostic annotation | context variability/novel-code shock contributes | rewrite primary category |
| SHUFFLED_TAG | I resolved positive, V not | `STABLE_INFORMATIVE_CODE_REGIME_SUPPORTED` diagnostic annotation | stable world-informative coding contributes beyond per-example variability; identity vs temporal stability not separately identified | rewrite primary category / claim pure identity effect |
| SHUFFLED_TAG | both resolved positive | `MIXED_COMPONENTS_SUPPORTED` | both nuisance/information components contribute | claim unique cause |
| SHUFFLED_TAG | neither/other pattern | `COMPONENT_DECOMPOSITION_UNRESOLVED` | primary regime wording only | choose preferred contrast post hoc |
| Positive follow-up | ALIASED advantage but no structural null | `REGIME_RESULT_ONLY` | licenses separate Experiment B/null | claim common modular law learned |

---

## Claim ledger

### ALIASED_TRANSFER_ADVANTAGE

Allowed:

> Under the locked modular cell, six-world history with world identity unavailable at learner input produced a larger reduction in restricted fresh-world in-weights adaptation cost than matched history with explicit fixed world separation; the estimated gain ratio reached the preregistered 20% point threshold and the positive direction excluded zero.

Not allowed: contradiction-only cause, learned modular mechanism, balcony, manufactured experience, language generalization.

### ALIASED_TRANSFER_ADVANTAGE_BOUNDED

Same directional statement, but explicitly:

> More than 10% of at least one k6 primary arm hit the locked cap; the positive restricted-cost direction also passed the conservative paired sign gate. Uncapped effect magnitude is not identified.

### SEPARABLE_TRANSFER_ADVANTAGE / _BOUNDED before SHUFFLED_TAG

Allowed only:

> The SEPARABLE **regime** produced lower restricted fresh-world adaptation cost than ALIASED under the locked cell.

Not yet allowed: “world identity caused the advantage”, “explicit separation itself helps”, or “aliasing is harmful because of conflict.” Those require the mandatory decomposition.

### PRACTICALLY_EQUIVALENT

Allowed:

> With no heavy cap, the locked 90% interval lay inside the preregistered reciprocal gain-ratio region `[1/1.20, 1.20]` (equivalently `±ln(1.20)` in delta-space) for the restricted-cost differential.

### UNRESOLVED / UNRESOLVED_HEAVY_CAP

Only registered boundary wording.

---

## Inadmissible is not null

Engineering/floor/ceiling/power terminals do not support the scientific statement that forced sharing has no effect. They state only that v0.2 failed to construct an admissible measurement regime under its predeclared learner/world/budget constraints.
