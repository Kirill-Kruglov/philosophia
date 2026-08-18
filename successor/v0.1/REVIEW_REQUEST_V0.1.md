# External review request — preregistration v0.1

This bundle is deliberately at the **review-before-lock** stage. Please attack the contract, not the prose.

## Primary claim under review

Does six-world sequential history with **world identity unavailable at learner input** (`ALIASED`) produce a larger reduction in restricted in-weights adaptation cost to a reserved seventh modular world than a paired history where world identity is available via fixed non-trainable context codes (`SEPARABLE`)?

The signed practical threshold is `delta_SESOI = ln(1.20)`.

## Please try to kill v0.1 on these axes

1. **Manipulation identity:** Is there still any place where the document pretends to isolate “contradiction alone” rather than aliased/unlabeled vs separable history?
2. **k=1 identity:** Does the code construction really force the arms to be exact through H1, including the k=1 C fork? If not, the built-in integrity gate is fake.
3. **Capacity leak:** Does SEPARABLE receive any trainable per-world capacity, directly or indirectly?
4. **Fresh-C fairness:** Is use of a novel `z_C` in both arms scientifically coherent given that only SEPARABLE saw context-code variation in history? The draft treats this as part of the regime rather than a removable confound; challenge that if wrong.
5. **Fixed compute:** Can either arm receive more history optimizer updates/examples before C under any path?
6. **Calibration freedom:** Can an experimenter use P0/P2 results to choose an unregistered scale, LR, WD, budget, criterion, or world pool?
7. **Floor/ceiling:** Are the P0 and k=1 headroom gates sufficient to prevent a trivial zero caused by a too-easy fresh C or saturation caused by a too-hard C?
8. **Restricted cost:** Is `R=ln(1+min(T,tau))` a defensible primary functional for this question, and is its saturation disclosed strongly enough?
9. **SESOI/power:** Is `ln(1.20)` unambiguous, and does the variance-only six-seed pilot mechanically price N without using the observed pilot mean?
10. **Decision logic:** Are `PRODUCTIVE_ALIASING_CANDIDATE`, `SEPARABILITY_ADVANTAGE`, `PRACTICALLY_NULL`, and `UNRESOLVED` mutually coherent under the 95%/90% CI rules?
11. **Scope fence:** Could a positive result still be rhetorically over-read as “contradiction causes abstraction” or “experience manufactured”? If yes, point to exact language to narrow.
12. **Repository provenance:** The exact Level 0 numerical model config is intentionally unresolved in this draft because it is absent from the supplied public files. Is `MODEL_CONFIG_REF + SHA` sufficient, and are the allowed deviations from it explicit enough?

## Reviewer output requested

Please return findings in descending severity:

- `BLOCKER` — v0.1 cannot be locked without changing scientific meaning or validity;
- `MAJOR` — design survives but an ambiguity can materially affect the result;
- `MINOR` — implementation/reporting clarification;
- `PASS` — no blocker found on the reviewed axis.

For every BLOCKER/MAJOR, propose the smallest fail-closed repair and state whether it changes the scientific estimand.
