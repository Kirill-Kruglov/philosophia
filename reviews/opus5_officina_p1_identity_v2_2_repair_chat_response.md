I'll start by reading the governing inputs.

Both `REVISE` verdicts are clear. Now the v2.1 correction, which is the document I must amend.

I have the full evidentiary base. Writing the v2.2 correction now.

Both deliverables are written. No existing file was modified.

## Deliverables

**[successor/OFFICINA_P1_PROCESS_CLAIM_IDENTITY_AUTHOR_CHOICE_PACKET_V2_2_CORRECTION.md](successor/OFFICINA_P1_PROCESS_CLAIM_IDENTITY_AUTHOR_CHOICE_PACKET_V2_2_CORRECTION.md)** — `sha256 05046cd1…0fc7`
**[reviews/opus5_officina_p1_process_claim_identity_choice_v2_2_closure.md](reviews/opus5_officina_p1_process_claim_identity_choice_v2_2_closure.md)** — verdict `READY_FOR_OFFICINA_P1_IDENTITY_V2_2_FINAL_XY_CONFIRMATION`

## What each repair does

**A — the claim-reopen path.** `PA-1`..`PA-9` pin the claims-root literal to `MS-1` (substring test over `Constant` nodes), every path-building expression to a constructor over Constants plus a grammar-checked stem, every read call's path operand to a plain Name, `claim_path` to three positions, the claim read to `MS-2`, `MS-2`'s bytes to immediate carrier binding, and `json.loads` to a plain-Name operand with a carrier only at `MS-3`. `PT-1` turns "can this denote `T_PROCESS_CLAIMS`?" into a four-case syntactic analysis, which is what makes `M-R4` decidably sound; `D-8`'s appeal to §P1-13.7's "exactly one open site" is withdrawn as `D-8′` — that section pins *installs* and three named reads, and `MS-2` itself has two call sites. The X counterexample plus 17 variants (`os`/`pathlib`/`mmap`, alias, second construction, helper-return, split literal, stem traversal, `chdir`, symlink, exception payload, container capture, directory enumeration, archive re-read) are carried as fixtures; four retained peer-read fixtures are asserted to **pass** — only claim paths are restricted.

**B — two `ACC-5` evaluations.** `EV-1` lineage (persistent, `D-1`/`D-2` only) and `EV-2` occupant (transient, one boolean consumer at `X-4`, no destination), confined by `OD-1`..`OD-4`/`S-25o`. `L-0`..`L-5` enumerate the five permitted transitive continuations behind a direct/continuation distinction and a one-question test, preserving exactly two direct destinations.

**C — the narrowed claim.** `IP`/`ACU` predicates tag every assertion. Withdrawn by name: `DC-3`'s "never process identity", `DC-4`'s blanket comparison/evidence ban, `DC-5`'s unqualified "one-way", `WL-4(a)`'s possession premise. Stated instead: searchable full-claim commitment, ≤4,194,304 candidates, conditional identity/equality evidence, not a confidentiality boundary. The full sink prohibition and the no-authority/no-PID-selector boundary are preserved intact.

Counts: 15 rules (`S-25a`..`S-25o`), 21 tests, 5 consumers, 5 accessors, 12 call sites, 2 evaluations, 2 direct destinations, 13 handoff steps. Six sentences replaced (`R-W3`..`R-W8`), all traceable to a binding review finding.

## Two things worth your attention before the X/Y round

- `PA-7`'s second sentence introduces one new analysis kind — an intra-function single-assignment lookup. It is local and one-pass, but it is *more* than the pure name/position matching of `S-25a`..`S-25m`. I disclosed it at `D-14` rather than describing it as the same discipline, and made it the X line's bounded question.
- `B-A4(iii)` is a genuine cost: the path-spelling discipline reaches every path constructor and every read call in `generic_harness.py`, not just the claim. It removes no capability and relocates no read site, and it follows the framers' own `S-13` precedent — but a reviewer could reasonably judge it disproportionate and prefer a different architecture.

T remains `NOT_ACTIVATED`, the programme claim `OPEN`, the watchdog cell unresolved, Option A recommended but unselected.
