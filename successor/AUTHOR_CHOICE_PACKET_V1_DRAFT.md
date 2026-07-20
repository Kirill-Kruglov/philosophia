# Successor author-choice packet — v1 draft

Status: `AUTHOR_CHOICE_PACKET_FOR_SELECTION`. Governing base: the
signed charter (v2 as corrected by v2.1, `CHARTER_SIGNATURE.md`, commit
`9dcfd7e`). This is a decision aid and authorization map: it places the
charter's author cells before Kirill with mutually exclusive choices,
consequences, and exact tokens. It is not implementation, a population
contract, a Q contract, or a scientific specification; it selects
nothing itself, derives nothing from stopped-line outcome or efficacy
records, and creates no code, entropy, world, candidate, manifest, run,
lock, escrow, or outcome. Recommendations are marked; the choice is
Kirill's in every cell.

---

## A1. Identity and layout (required before WP-1)

**Name.** Two objects, deliberately distinct: the **repository/line
identifier** (infrastructure, chosen now) and the **essay/publication
title** (voice, chosen at essay time — never bound by this packet).

| Choice | Token | Consequence |
|---|---|---|
| **A1-N1 (recommended):** line identifier **`officina`** (Latin: workshop) | `I_NAME_SUCCESSOR_LINE_OFFICINA` | continues the essay's central Workshop metaphor without reusing "philosophia" as the line name; the stopped line keeps its title cleanly; publication title stays free (e.g., decided with the essay) |
| A1-N2: plain `philosophia-2` | `I_NAME_SUCCESSOR_LINE_PHILOSOPHIA_2` | maximally literal lineage; risks reading as "Level 1 v3 by another name" in public prose and needs constant disclaimers |
| A1-N3: defer the public name; keep internal `successor` | `I_DEFER_SUCCESSOR_PUBLIC_NAME` | zero commitment now; WP-1 manifests use the neutral namespace; a later naming decision is purely editorial |

**Layout.** Compared only on the charter's engineering axes; filesystem
layout creates no scientific independence — the quarantine is the
signed semantic contract plus the mechanical path-allowlist under
either layout.

| Choice | Token | Accidental-reuse risk | Audit continuity | Publication cohesion |
|---|---|---|---|---|
| **A1-L1 (recommended):** same-repository `successor/` tree | `I_SELECT_SUCCESSOR_LAYOUT_SAME_REPO` | mitigated mechanically (allowlist); more old paths in reach, so the allowlist is load-bearing | **strongest**: the signed `successor/` tree already exists here, and the predecessor is a literal, immutable, hash-pinned git ancestor — no external pin needed | one canonical record, one atlas, one essay home |
| A1-L2: separate repository | `I_SELECT_SUCCESSOR_LAYOUT_SEPARATE_REPO` | slightly lower (fewer stopped-line paths reachable) | weaker: ancestry becomes an external `INHERITANCE.md` hash pin; the already-signed charter/signature artifacts must be migrated or governance splits across two repos | split across repositories |

The recommendation follows from the facts that a signed `successor/`
tree already exists at the signature base and that the charter's
allowlist — not the directory boundary — carries the reuse guarantee.

## A2. C interpretation type (required at WP-3, before any T world generation)

| Type | Token | What a valid C claim generalizes to | What it cannot claim | Cost |
|---|---|---|---|---|
| A2-1: fixed-frame **census** | `I_SELECT_C_INTERPRETATION_CENSUS` | exactly the enumerated frame, descriptively; zero sampling assumptions | anything outside the frame | C size = frame size; hardest resource pressure |
| **A2-2 (recommended): probability sample from a fixed finite frame** (locked inclusion probabilities, weights, finite-population correction) | `I_SELECT_C_INTERPRETATION_FINITE_FRAME_SAMPLE` | the **whole registered finite frame**, by design-based inference, with no distributional model | any world outside the registered frame; any "worlds like these" reading | moderate C size; census remains the exact degenerate case if the frame is small |
| A2-3: named **superpopulation** sample | `I_SELECT_C_INTERPRETATION_SUPERPOPULATION` | the named generator law (infinite family) | anything beyond the named law or under a changed generator | buys the widest scope; the modeling assumption is unusually cheap here (the generator *is* code), but inference then leans on the sampling law rather than on an auditable enumerated registry |

**Recommendation rationale (A2-2):** for a bounded one-week-scale
programme, design-based inference to a declared finite registry is the
honest middle — wider than a census at feasible cost, with no
distributional assumption to defend, machinery of exactly this type
already proven in the workshop, and a claim boundary ("the registered
frame, nothing further") that cannot be over-read. A2-3 is defensible
and may suit a later line; A2-2 keeps generalization earned and
auditable. Frame size, support values, strata, and N are **not** chosen
here — they belong to WP-3/WP-9.

## A3. Q unpredictability mechanism policy (owned by WP-6)

| Mechanism | Token | Character |
|---|---|---|
| **A3-1 (recommended): one-shot sealed post-freeze root** — OS-CSPRNG drawn once by the reviewed driver only after the durable manifest + attempt claim; sealed until post-attempt publication; procedural custody, no cryptographic-independence claim | `I_SELECT_Q_ENTROPY_SEALED_POSTFREEZE_ROOT` | the pattern this workshop has already built, reviewed, and executed cleanly; no external dependency; the threat model is procedural either way (the operator runs the harness in both designs) |
| A3-2: post-freeze **public beacon** — a pre-committed external randomness event realized only after freeze, with a deterministic committed mapping | `I_SELECT_Q_ENTROPY_PUBLIC_BEACON` | third-party auditability of the entropy itself; adds an external availability dependency and a beacon-commitment protocol, without removing procedural trust in the sampler |

**Minimum failure semantics (policy level, either mechanism; numerics
and concrete implementation stay WP-6 cells):**

- **Launch definition:** an attempt is *launched* at the instant its
  randomness comes into existence (charter §2 step 3). From that
  instant the attempt is charged (id, cap slot, α allocation)
  regardless of what follows.
- **Before any entropy exists** (driver refusal, beacon event
  unavailable, precondition failure): **no launch occurred and nothing
  is charged.** Recovery requires a **signed pre-attempt process
  disposition** — never a silent retry — and, for A3-2, the next beacon
  event is selected by a rule committed *before* the first commitment
  (no beacon shopping: the "if event k unavailable, use event k+Δ"
  ladder is itself pre-committed).
- **No redraw, ever:** one entropy realization per launched attempt;
  generation or attestation failure after entropy exists is
  `Q_INVALID:<cause>` with the binary unset — charged, per unified
  charging.
- **No custody substitution:** the entropy source identity (mechanism,
  driver, custody procedure) is part of the signed Q contract; changing
  it is a signed pre-attempt amendment with bounded review — permitted
  only when no launch has occurred under the pending commitment, and it
  consumes no Q attempt because no launch existed.
- A **standing fallback mechanism is forbidden**; there is exactly one
  signed mechanism at a time.

## A4. T envelope: bit-exact form and profiles (required pre-T)

**The form Kirill fills and signs** (every number is an author resource
commitment — a statement of what the author is willing to spend, never
derived from any stopped-line outcome or efficacy record):

```text
T-ENVELOPE COMMITMENT
  E1  total device-hours for real T development:        ____ h
  E2  max canonical candidates registered in T:         ____
  E3  review checkpoint cadence: every ____ calendar days
      or every ____ device-hours, whichever comes first
  E4  development ledger: append-only public file at
      <namespace>/T_LEDGER.md; every real T run, candidate
      registration, and checkpoint entry is recorded
  E5  T_ENVELOPE_EXHAUSTED: fires mechanically when E1 or E2
      is reached; recorded in the ledger; extension only by a
      loud signed decision with bounded review
  E6  T_AUTHOR_STOP: Kirill's signed stop at any checkpoint;
      distinct ledger record; not an envelope event
```

**Profiles** (pick one and fill the form; labels are offers, not
derivations):

| Profile | Token | E1 | E2 | E3 |
|---|---|---|---|---|
| Minimal | `I_COMMIT_T_ENVELOPE_MINIMAL` | ~120 h | ≤ 8 | weekly |
| **Standard (recommended)** | `I_COMMIT_T_ENVELOPE_STANDARD` | ~400 h | ≤ 20 | twice weekly |
| Extended | `I_COMMIT_T_ENVELOPE_EXTENDED` | ~1,000 h | ≤ 40 | twice weekly + monthly loud review |

**Boundary rules (fixed policy, not numbers):**
implementation-only dry runs — unit tests, dummy fixtures under
declared test-only seeds, harness smoke runs touching no real T world —
**do not consume the envelope**; any run that trains a registrable
learner on real T worlds **does**. A behavior-relevant change to a
registered candidate creates a **new canonical candidate** (charter §4
equivalence) and consumes one E2 slot on registration; behavior-inert
edits do not.

## A5. Device and optional breathing-check policy

Context: the available host is an AMD Ryzen AI Max+ 395 with 128 GB
unified memory. The final Q/C stack is part of the candidate manifest
and **cannot be selected now**; this cell chooses only the development
policy. **Level 0's CPU result does not transfer to any off-CPU
stack** — an off-CPU stack starts with no platform replication anchor.

| Policy | Token | Consequence |
|---|---|---|
| A5-1: CPU-only development | `I_SELECT_DEVICE_POLICY_CPU_ONLY` | keeps the Level 0 anchor relevant for every candidate; forfeits exploring the host's accelerator paths entirely |
| **A5-2 (recommended): off-CPU permitted, with a required bounded, non-citable, deterministic breathing check** passed on a stack family before its first candidate may register for Q | `I_SELECT_DEVICE_POLICY_OFFCPU_WITH_BREATHING_CHECK` | platform assurance is re-earned where Level 0 does not reach, as cheap T-phase engineering rather than as charged Q launches; the check is engineering-only, never citable, never a Level 0 transfer |
| A5-3: off-CPU permitted, no separate breathing check | `I_SELECT_DEVICE_POLICY_OFFCPU_NO_BREATHING_CHECK` | leanest; a stack with zero platform precedent can reach Q, and under unified charging its platform discovery would burn capped, α-charged Q attempts |

The recommendation buys A5-3's flexibility while pushing platform risk
into the uncharged T surface instead of the charged Q surface. No
driver, library build, or numerical tolerance is selected here —
WP-2/WP-6 own the tested equivalence and reproducibility contract.

## A6. Strict S and planning (record, not a choice)

Recorded per the signed v2.1: **S is unavailable; no-S is the signed
base.** No S token or route is offered here. A future S requires a new
author-signed charter amendment with bounded X/Y review and a durable
pre-S scientific-skeleton lock before any S entropy or datum, and would
amend the three-surface architecture token. Confirmatory planning under
the base: conservative sample-size rule + arm-free Q telemetry for
engineering caps, exactly as chartered.

---

## Gate table: now / later / fixed

| Category | Cells |
|---|---|
| **1. Kirill chooses now** | A1 name + layout; A2 C-interpretation type; A3 Q-mechanism policy; A4 envelope profile + filled E1–E3; A5 device/breathing policy |
| **2. Technical contract later** | WP-3: frame/support/partition values, strata, weights, inclusion probabilities; WP-6: Q caps, `δ_Q`, spending rule, competence and resource numerics, concrete entropy implementation and custody; WP-9: endpoint, treatment arms, margins, alphas, N, seed law, C escrow environment |
| **3. Already charter-fixed** | three surfaces T/Q/C; no S; automatic first-valid promotion; every-launch Q charging; canonical candidate equivalence; selection-conditional claim + `selection_scope_id`; multiplicity ownership; exclusive terminal taxonomy; lock-before-C-root order |

## Authorization boundary of this packet

No token above authorizes T generation or any execution. After Kirill's
selections and one bounded X/Y review of them, the consolidated
signature (template below) authorizes **only**:

- **WP-1** — lineage/bootstrap implementation (namespace, manifests,
  quarantine path-allowlist, T ledger skeleton);
- **WP-2** — governance-library implementation and tests
  (validity-first taxonomy, one-shot drivers, PRF/serialization/escrow
  machinery, dummy-seed fail-closed fixtures).

WP-3 must still be drafted, reviewed, and signed before any real T
world exists. Everything from WP-4 onward keeps its own charter gate.

## Expected implementation outcomes (WP-1–WP-10)

| After | Deliverable state | What it is not |
|---|---|---|
| WP-1/WP-2 | **engineering readiness**: namespace, allowlisted drivers, tested governance library, empty ledgers | no world, no learner, no claim |
| WP-3 | **frozen world-side estimand**: signed eight-object population/construct contract, C interpretation instantiated | no world realized; learner side untouched |
| WP-4/WP-5 | open, non-citable T development with valid endings `T_ENVELOPE_EXHAUSTED` / `T_AUTHOR_STOP` / candidates submitted | never evidence; a T ending is a publishable process ending |
| WP-6/WP-8 | either an **automatically promoted candidate + stack** (first valid `Q_PASS`) or `Q_CAP_EXHAUSTED_NO_QUALIFIER` | a pass is a gate fact; no-qualifier is a process ending, never `INSUFFICIENT` or learner impossibility |
| WP-9/WP-10 | a **signed, locked, escrowed, still-unexecuted C experiment**: spec + X/Y review + signatures + preregistration lock + post-lock C root + sealed commitment | not a result; nothing scientific has moved |
| post-charter C execution | the only step that can produce a scientific pass, null, boundary, `INSUFFICIENT`, or censoring — under its own separate author authorization | never promised by implementation |

**Stated plainly:** implementation promises no qualifier, no C run, and
no Proof. The strongest successful implementation endpoint inside the
charter is a reviewed one-shot C package ready for separate author
authorization.

## Consolidated signature template (placeholders; nothing pre-selected)

```text
SUCCESSOR AUTHOR SELECTIONS — signed by Kirill Kruglov on ____
Base: CHARTER_SIGNATURE.md (v2 + v2.1), commit ____

A1 name:    [ I_NAME_SUCCESSOR_LINE_OFFICINA |
              I_NAME_SUCCESSOR_LINE_PHILOSOPHIA_2 |
              I_DEFER_SUCCESSOR_PUBLIC_NAME ]
A1 layout:  [ I_SELECT_SUCCESSOR_LAYOUT_SAME_REPO |
              I_SELECT_SUCCESSOR_LAYOUT_SEPARATE_REPO ]
A2:         [ I_SELECT_C_INTERPRETATION_CENSUS |
              I_SELECT_C_INTERPRETATION_FINITE_FRAME_SAMPLE |
              I_SELECT_C_INTERPRETATION_SUPERPOPULATION ]
A3:         [ I_SELECT_Q_ENTROPY_SEALED_POSTFREEZE_ROOT |
              I_SELECT_Q_ENTROPY_PUBLIC_BEACON ]
A4:         [ I_COMMIT_T_ENVELOPE_MINIMAL | _STANDARD | _EXTENDED ]
            E1 = ____ h   E2 = ____   E3 = ____ / ____
A5:         [ I_SELECT_DEVICE_POLICY_CPU_ONLY |
              I_SELECT_DEVICE_POLICY_OFFCPU_WITH_BREATHING_CHECK |
              I_SELECT_DEVICE_POLICY_OFFCPU_NO_BREATHING_CHECK ]
WP gate:    I_AUTHORIZE_SUCCESSOR_WP1_WP2_IMPLEMENTATION
            (signable only after bounded X/Y review of these selections)
```

These selections are governance and resource commitments. They move no
scientific claim; the predecessor line remains immutable, `OPEN`, and
`BLOCKED_LEVEL1_FEASIBILITY`; T/Q remain permanently non-citable for
C1–C6; only a valid, independently locked C execution may ever move a
successor claim, within its selection-conditional scope.
