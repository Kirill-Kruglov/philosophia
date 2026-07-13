# Level 0 outcome result

Status: **VALID — REPRODUCED.** Derived once from the complete locked battery.

- Decision artifact: `outcomes/decision.json`
- Decision SHA-256: `12acaff549994c9eec1a66fe52b3702879d7760f611ce7c53d18607866b1ade1`
- Accepted source commit: `4dbd3b1`
- Lock commit: `e4a0fee`
- Primary quorum: 4 of 5 Arm A runs
- Observed primary result: 5 of 5
- Platform violations: none

| Run | FIT start | GENERALIZE start | Delay | Locked result |
|---|---:|---:|---:|---|
| A-0 | 200 | 6,700 | 6,500 | replicates |
| A-1 | 200 | 5,200 | 5,000 | replicates |
| A-2 | 200 | 6,600 | 6,400 | replicates |
| A-3 | 200 | 7,700 | 7,500 | replicates |
| A-4 | 200 | 6,700 | 6,500 | replicates |
| B-1 | 200 | 40,400 | 40,200 | diagnostic success |
| B-2 | 200 | 61,200 | 61,000 | diagnostic success |
| B-3 | 200 | 51,300 | 51,100 | diagnostic success |
| R-0 | 200 | none | none | FIT, does not GENERALIZE |

Arm B is recorded as `NO_PRIMARY_INFERENCE` because Arm A already reproduced;
it is not an independent success claim. R-0 passes the locked memorization and
leakage-negative-control rules.

This result licenses only the preregistered statement that all five canonical
CPU paper-mainline seeds reproduced delayed generalization under the locked
operational predicates. It is not evidence for the Philosophia programme,
mechanism, Fourier prediction, weight-decay causality, cross-world transfer, or
generality beyond this task.
