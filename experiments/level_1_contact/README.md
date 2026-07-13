# Level 1: contact

Status: `READY_FOR_LEVEL1_SPEC`; not authorized for comparative scout, escrow,
lock, or outcome.

The signed design replaces answer-entropy matching with three arms under one
common fixed oracle budget and no early stop:

- **ACTIVE:** chooses equality queries from its own learner-state uncertainty;
- **YOKED-GEOMETRY:** receives a full-budget query sequence from a disjoint,
  exactly stratum-matched ACTIVE donor, but obtains answers only from its own
  target oracle;
- **RANDOM-STATIC:** samples the same candidate pool under a locked random
  design.

The inferential block is one target world plus its unique donor world/transcript.
Blocks are disjoint; seeds are repeated measures. Realized answer entropy and
label balance are mediators and diagnostics, not matching targets.

The primary endpoint is right-censored budget-to-certified-solve within the
common budget, evaluated post hoc on an arm-independent, balanced escrow panel.
The learner and acquisition policy cannot observe solve status. C1 is the paired
ACTIVE-versus-YOKED estimand; RANDOM-STATIC locates whether active geometry is
useful without target adaptivity.

A Level 1 null yields `BOUNDARY_CONTACT_CHOICE`; it does not falsify first-hand
contact or the retained-history core. The Level 2 contact mode is selected by
the signed total three-arm rule. `INSUFFICIENT` blocks Level 2.

Before any comparative development scout, the S-gate must freeze the cyclic
world contract, acquisition policy, endpoint and benefit orientation, censoring,
N6 margins and interval rules, analysis plan, and invalidity gates. The scout is
non-citable and may inform variance, censoring, feasibility, and N3 precision
only. It may not change the frozen rule or margin.

Governing signatures and review lineage:
`reviews/LEVELS1_3_CLAIM_GRAPH_SIGNATURES.md`.
