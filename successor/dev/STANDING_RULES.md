# Standing rules

Draft adopted alongside PHASE1_18 Part B amendment 5; extend as incidents
accumulate. No verdict token; nothing here is a result. Each rule carries the
incident that produced it, because a rule without its incident reads as
bureaucracy and gets dropped.

---

## 1. Provenance classes

Every field in a results JSON carries a class:

| class | meaning |
|---|---|
| `MEASURED_IN_PROCESS` | produced by the process the field describes |
| `VERIFIED_BY_CODE_READ` | established by inspection; carries file and line |
| `DERIVED` | computed from other recorded fields; carries the inputs |
| `INFERRED` | concluded from something outside the record; carries the basis |

**A field of class `INFERRED` may never be compared against a field of class
`MEASURED_IN_PROCESS` without the class travelling into the comparison and
into every statement made from it.**

*Incidents, four in one ticket:* B2/09 recorded a `script_hash` matching no
document, because the executed file was CRLF and the archived copy LF.
PHASE1_18 hardcoded `torch_use_deterministic_algorithms: False` in the
analysis process as a claim about the eval process. The same analyzer recorded
`instrumentation_enters_search_decision: False` — a real code read, written as
a measurement. `host_otherwise_idle` asserted a property of a 75-minute
interval from two instants.

## 2. Reading rules must have both outcomes reachable

Before any run, state for every threshold and verdict what data would produce
the opposite outcome. A rule whose opposite cannot be named is a defect, not a
result. Put the statement in the executable file as a comment, not only in the
ticket.

Two failure directions, both seen:

- a rule that can only pass — 16D's `ck1 > ck2 at every seed` under a
  deterministic search; a repeat at a configuration assumed deterministic used
  as a noise floor;
- a rule that fires on the expected outcome and reports it as a fault —
  PHASE1_18's gate comparing an `OMP=1` run against `OMP=16` pins while the
  ticket's own subject is that thread configuration flips theorems.

## 3. Matched comparison means matched corpus, not only matched weights

A delta needs both sides drawn from the same immutable, ordered, hashed
evaluation object. Domain-separate the corpus stream by seed only — never by
run tag, arm, method name or attempt. Assert identity immediately before each
measurement; a mismatch voids the number rather than annotating it.

*Incident:* B2/09 drew init and trained probes from `probe-init-P0` and
`probe-P0`. The matched-length stratum held 1036 samples at init and 21 after
training, and the published diagnosis attributed the shrinkage to the learned
representation — impossible, since stratum size is a property of the sampled
words.

## 4. Name the currency, and refuse analyses that lack it

Cost claims require a host-independent per-item counter recorded on every
record. Wall seconds are never a substitute and no count may be reconstructed
from timings. Enforce it as a fail-closed schema check in the analysis code,
not as a convention.

*Incident:* 16B reported "159 s vs 181 s" as search cost. PHASE1_17 later
established that no host-independent counter existed in any artifact; there
had never been another quantity.

## 5. Fixed sets get description, not inference

When the evaluation set is fixed and external rather than sampled from a
population — the 30 Kleene theorems, a finite audit table — every quantity is
a deterministic description of that set. No hypothesis test, no confidence
interval, no bootstrap, however tempting a paired structure makes it. Give
repeated records equal weight within their stratum, strata equal weight in any
pooled figure, and print every numerator and denominator.

## 6. Hash both forms, and never record an inference as a stamp

Record raw-byte and LF-normalized SHA-256 for every script, input and output;
the normalized digest does not replace byte provenance. A configuration
recovered from a run script is `INFERRED`, is labelled in the field itself,
and is never stamped as though recorded.

*Incident:* PHASE1_18 was offered the option of stamping historical `16C`/`17`
artifacts with a thread configuration read off their launcher. Refused —
recording an inferred fact as a registered one is manufacturing provenance.

## 7. Declare what closes a line before it needs closing

Before the second review of any line, declare the pattern of review outcome
that closes it rather than repairing it again. A rule written after it would
have bound is worthless.

*Incident:* TWOPRES declared that a third protocol review returning new
Critical findings — rather than findings on the previous repairs — would close
the line. It returned exactly that, and the line closed with three paper
passes and zero compute spent. The rule bound against the line its author
wanted to continue, which is the only condition under which such a rule is
worth anything.

## 8. Overclaim shapes to check before dispatch

A recurring family, caught repeatedly in this programme's own drafts: a
universal quantifier where only existence was shown, and a transfer claim
where only reachability was shown.

Concrete instances: "settles at every `t`"; "survival transfers upward";
"M1/M2 reduce to normal-form comparison"; "changes every cross-stream label";
"does not approximate". Each was written by the drafter, caught by review, and
none was a difficult error to see once looked for.

Read every draft once for this shape specifically, before dispatch.
