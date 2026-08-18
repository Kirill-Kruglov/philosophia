# Kill matrix v0.1

**Status:** DRAFT FOR EXTERNAL REVIEW — fail-closed decision surface

The first applicable higher-priority invalidation/engineering terminal prevents lower scientific claims.

| Stage | Condition | Terminal / status | Permitted interpretation | Forbidden response |
|---|---|---|---|---|
| Pre-lock | Exact Level 0 `MODEL_CONFIG_REF` cannot be recovered | `BLOCKED_CONFIG_PROVENANCE` | v0.1 cannot claim inherited learner config | invent/reconstruct hyperparameters silently |
| Pre-lock | Generator/p_flip/split/context/fork/determinism acceptance test fails | `BLOCKED_IMPLEMENTATION` | implementation not ready | run science anyway |
| P0 M=96 | median Tfresh < 2000 | `ESCALATE_TO_M128` | M96 too easy by signed selector | tune LR/WD or choose custom n |
| P0 attempted scale | median Tfresh > 8000 or >2/16 capped at 20k | `INADMISSIBLE_SUBSTRATE_TOO_HARD` | cell cannot cheaply resolve learner/world at this config | hyperparameter sweep/downscale under v0.1 |
| P0 M=128 | median Tfresh < 2000 | `INADMISSIBLE_SUBSTRATE_TOO_EASY` | authorized scales lack fresh-world headroom | add scale after seeing data |
| P2 | H1 or k=1 arm trajectory/hash differs | `INVALID_K1_ARM_DIVERGENCE` | arm construction/determinism invalid | treat difference as science or drop seed |
| P2 | k1 median T <1000 or >1/6 T=0 at M96 | `ESCALATE_TO_M128` | post-one-world transfer floor at M96 | tune history budget |
| P2 M=128 | same k1 floor | `INADMISSIBLE_TRANSFER_FLOOR` | new C too cheap after one history world | proceed and call delta=0 a scientific null |
| P2 | >1/6 k1 probes capped at tau | `INADMISSIBLE_TRANSFER_CEILING` | new C too expensive/unstable at baseline | enlarge tau post hoc |
| P3 | mechanically required N >128 | `BLOCKED_POWER` | preregistered SESOI not affordably resolvable under this variance | run N=14/20 anyway |
| Confirmatory | valid paired seeds < locked N | `INVALID_INCOMPLETE_CONFIRMATION` | confirmation incomplete | analyze smaller N as confirmatory |
| Confirmatory | any unresolved trajectory/config/hash violation | `INVALID_CONFIRMATION` | no scientific category | exclude inconvenient runs |
| Confirmatory | 95% CI lower >0 AND delta_hat >= +ln1.20 | `PRODUCTIVE_ALIASING_CANDIDATE` | forced non-separability yielded larger practically meaningful estimated transfer gain | claim balcony/mechanism/full experience |
| Confirmatory | 95% CI upper <0 AND delta_hat <= -ln1.20 | `SEPARABILITY_ADVANTAGE` | explicit world separation transferred better by practically meaningful estimated amount | call it failed experiment |
| Confirmatory | 90% CI entirely inside ±ln1.20 | `PRACTICALLY_NULL` | effects of signed meaningful size are unsupported/resolved small at this scale | move SESOI after outcome |
| Confirmatory | valid but none above | `UNRESOLVED` | cell did not resolve direction+magnitude | add seeds or choose favorable k post hoc |
| Positive follow-up | primary positive but no structural null/follow-up | `REGIME_RESULT_ONLY` | license Experiment B / diagnostics | say common modular law was learned |

---

## Claim ledger for the four valid scientific outcomes

### PRODUCTIVE_ALIASING_CANDIDATE

Allowed:

> Under the locked modular cell, a six-world history with world identity unavailable at input produced a larger reduction in restricted fresh-world in-weights adaptation cost than a matched history with world identity available; the estimated gain ratio met the preregistered 20% threshold and the positive direction excluded zero.

Not allowed: mechanism, general experience, language transfer, or contradiction-only causality.

### SEPARABILITY_ADVANTAGE

Allowed:

> Under the locked cell, explicit world separation produced larger later transfer; forced aliasing was a cost rather than productive pressure at the preregistered meaningful scale.

### PRACTICALLY_NULL

Allowed:

> The locked cell ruled the differential transfer effect inside the preregistered ±20% gain-ratio region as practically small under the equivalence criterion.

### UNRESOLVED

Allowed:

> The locked cell produced a valid but inconclusive estimate relative to the signed practical threshold; no direction/magnitude conclusion is licensed.

---

## Why inadmissible is not null

`INADMISSIBLE_SUBSTRATE_TOO_EASY`, `INADMISSIBLE_TRANSFER_FLOOR`, and corresponding ceiling/power terminals are engineering/method boundaries. They do not support “productive forced sharing does not exist”. They state only that v0.1 could not create a measurement regime with enough headroom/resolution to ask the question honestly.
