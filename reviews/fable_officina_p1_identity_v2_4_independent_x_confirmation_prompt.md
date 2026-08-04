# Officina P1 identity v2.4: independent X confirmation

You are Claude Code Fable 5 (Claude Opus 4.8 is an acceptable substitute only if it did not author v2.3 or v2.4). This independence condition is load-bearing. Perform a bounded adversarial engineering confirmation, not a design round.

## Exact bytes

- `successor/OFFICINA_P1_PROCESS_CLAIM_IDENTITY_AUTHOR_CHOICE_PACKET_V2_4_CORRECTION.md`
  SHA-256 `bef7012a5fce59857372755c23f6da87d1d1045f7d62d8945914cb60d9c48fda`
- `reviews/opus5_officina_p1_process_claim_identity_choice_v2_4_closure.md`
  SHA-256 `5ac5fbc31faa565d44729bf814726e97e491fcfa5acf70ffa55fd4373eddf4f3`

Read the complete identity chain, the v2.3 X/Y reviews, and signed filesystem operations they cite. Treat the author closure as untrusted. Recompute custody and state explicitly that you did not author v2.3/v2.4.

## Bounded question

Did v2.4 make the closed identity rules satisfiable without reopening an escape?

Independently test:

1. `PA-6″(5)`: exactly the signed `os.chdir("/")` is admitted before every name open; no second/dynamic `chdir`, `fchdir`, link or symlink becomes legal.
2. `PA-6″(6)`: signed `dir_fd=6` constants and the approved descriptor Name are admitted on `PC-N` operations, while pinned claim/lease operands cannot use `dir_fd`; unanchored constants, expressions and Names are rejected. Decide whether protocol `:58-72` requires anchored claim/lease opens and would conflict with the pinned prohibition.
3. The 24 path-operand and 9 descriptor-operand forms are exhaustive, disjoint and correctly classified. Attempt descriptor laundering, aliasing, helper/default/closure returns and one-hop binding bypasses without introducing taint reasoning.
4. Every signed operation in the 18-row table has a conforming spelling: PCS preflight; four `dir_fd=6` opens; anchored lock open; `P-h`/`L-4`; `P-f`/`A-5`; MS-2/PG-3; both pinned installs; four peer installs; protocol-B writes; `/proc/self/fd`; constant durable paths; all PC-N reads.
5. Verify the two-write statement is scoped only to pinned operands and does not forbid ordinary signed installs; write safety is imperative.
6. Verify `PG-4′` permits only its literal `schema` discrimination read before gate completion, with no other value binding.
7. Recompute 27 tests, 10 fixtures, 33 read forms, five accessors, five disjoint mapping producers, all unchanged evaluation/destination counts, and no regression of the Y-confirmed alias/information boundary.

Produce a concrete AST or signed unsatisfiable operation for any failure. Do not accept author assertions as evidence and do not invent a new option.

## Output

Write only `reviews/fable_officina_p1_identity_v2_4_independent_x_confirmation.md`.

Emit exactly one verdict:

- `OFFICINA_P1_IDENTITY_V2_4_INDEPENDENT_X_CONFIRMED_FOR_AUTHOR_SELECTION`
- `REVISE_OFFICINA_P1_IDENTITY_V2_4`
- `BLOCKED_OFFICINA_P1_IDENTITY_V2_4`

If confirmed, authorize only Kirill's identity author-choice token. Do not modify existing files or commit.
