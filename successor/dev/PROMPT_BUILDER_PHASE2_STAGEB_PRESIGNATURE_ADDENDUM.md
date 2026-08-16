# PHASE2_STAGE_B — pre-signature addendum

Status: `DEV_PROBE_ONLY__NO_SIGNATURE_AUTHORIZED`
Compute: CPU, under an hour. Increment to
`phase2_stageb_presignature_probes_20.py`, not a new instrument.

Both original probes returned clean: `not_e` is enumerable despite its absent
annotation, and the §9 positive-control family is realizable under grammar A.
Two gaps remain between here and the signature, and both are small.

## Item 1 — depth 1..8 expressibility

Probe B witnessed depths 1 and 3. §9 scores Spearman over depth 1..8. A family
that expresses at depth 3 and fails at depth 6 kills §9 just as surely, and
`CARRIER_CLOSED_NO_USABLE_FRAME` is a carrier kill.

For each depth 1..8, on disposable dev roots, report: expresses under grammar A
(ambient arrows only in the outer sequent and in the declared premise types of
`or_e`/`not_i`), type-checks, compiles to primitive Peano actions, fresh-process
replays to an empty goal, and the resulting statement size.

**Existence facts only.** No search, no cost, no Spearman, no threshold. No
number produced here may later appear in the audit contract as a calibration
— that is the standing rule for pre-signature probes and it is the reason this
item is cheap.

Report the depth at which any of the four properties first fails, or that none
does. If a depth fails, name whether the failure is expressibility or size, and
stop — do not redesign the family.

## Item 2 — durable exclusions registry

The 11 disposable roots from the probes are currently recorded only in a
results JSON. Create the durable registry the Stage B statistical review asked
for, and append them to it alongside L01/L2:

- one file, append-only, listing every disposable identity produced anywhere in
  Phase 2 — root, PRF domain label, the pass that produced it, and the date;
- for each entry, both the alpha-canonical theorem identity and the canonical
  rule-skeleton identity where those exist;
- a fail-closed check, callable by any later generator, that refuses a
  candidate colliding with any registered identity.

The review's finding was that permanent split exclusion was too weak: all
scopes — development, cost, audit, selector, pilot and scientific frame — must
be mutually disjoint in both theorem and skeleton identity. Eleven roots is
the cheapest moment this registry will ever be built. At the audit's scale it
is not optional and not cheap.

Add this item's roots to the registry too.

## Two facts to carry into the signature

Recorded here so they are not lost between the probe report and choice A–E:

1. **`not_e` has a wider action footprint than every annotated premise.** An
   absent annotation is not a restriction but the lack of one, so `not_e`
   enumerates both forward and backward while all eight annotated premises
   enumerate one way. Plans using `NOT_ELIM` therefore have a different cost
   profile from plans that do not. If this is not written into the signature,
   it will surface during `B*` calibration as an unexplained asymmetry between
   bands.
2. **The positive control is realizable, so choice A is no longer blocked by
   §9** — which was the sole reason the signature was held.

## Cap and provenance

`<= 80` added lines. One wall hour. Deterministic; two fresh executions must
agree byte for byte. Raw-byte and LF-normalized SHA-256 for the script and
every input, quoted identically in report and JSON. Lenovo Legion remains
excluded from experimental runs, with the reason recorded in the log.

## Negative authorization

No audit root, no carrier candidate, no cost block, no calibration, no
learner, no training, no selector, no SELF/YOKED, no signature, no commit to a
citable path. Accepted Stage-A behaviour is not reopened.
