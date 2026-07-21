Written to `reviews/opus_officina_t_activation_protocol_v1_review.md`.

## Verdict: `REVISE_OFFICINA_T_ACTIVATION_PROTOCOL`

The protocol is well-structured and sound in principle — but three Major spec gaps leave two implementers building different state machines, plus Minor pins. All six §1 governing-pin hashes match the committed files, and it authorizes nothing / chooses no WP-6 numeric.

**Major:**
- **P-1 — durability/commit model is inconsistent and collides with "clean HEAD."** §5.7 makes activation a git commit; §6 requires capability issuance "at the current clean HEAD"; but §7 metering appends the ledger and replaces `T_STATE.json` **without a commit** — so after the first charge the tree is dirty and the next lease's clean-HEAD precondition can't hold. Fix: declare metering working-tree-durable (fsync file+dir), commit only at defined checkpoints, and scope "clean HEAD" to the non-runtime tree while the runtime files are actively metered.
- **P-2 — the "exclusive runtime lock" has no specified mechanism/scope.** Name a dedicated `flock(LOCK_EX)` lock file, `O_NOFOLLOW`, held across the entire read-verify-append-replace of every state-mutating transaction.
- **P-3 — the "state-bearing" ledger event set is never enumerated,** so the cache↔ledger reconciliation (§4) is implementer-defined. Enumerate which events carry a full post-`t_state`.

**Minor:** P-4 (require the just-confirmed WP-4 held-fd `samestat` anchoring for the runtime ledger/state/lease, not just hash-linking + lock); P-5 (pin the metering clock source, e.g. `CLOCK_MONOTONIC`, and state a lease can't span a power-off); P-6 (name the activated-envelope schema; note activation supersedes the inactive `verify_officina_wp12`); P-7 (fix the exact commit staged-set and authorship trailers); P-8 (confirmation: the heartbeat max-uncharged-interval is correctly deferred as a named runtime constant, not a WP-6 numeric).

**Confirmed sound:** governing pins all hash-correct; claim-before-effect and capability-only-after-commit; typed `T_ACTIVATION_INVALID`/`T_RUNTIME_INVALID:PROCESS` routing with no auto-retry/rollback/deletion and signed bounded recovery; overshoot retention; E3/pause/resume via the confirmed `ResumeGate` with powered-off time advancing E3-not-E1; author-stop signature-bound and distinct; the E2/WP-6 boundary (no production registration, WP-6 defers Q/breathing numerics — **no WP-6 numeric prematurely chosen, no WP-4 cell improperly deferred**); capability binding revalidated at use, unusable for Q/C or frame/predecessor moduli.

**Eligible surface (after repair + positive re-review):** inactive implementation and tests only — the activation-driver/metered-runtime state-machine library + the §10 test matrix on disposable mirrors, with **no** activation, real world, entropy, lease, E1/E2/E3 spend, registration, learner run, Q/C activity, authorization record, or runtime artifact in the real tree. Implementation then needs its own X/Y review, a separate authorization candidate, and Kirill's explicit token before the driver runs once.

**Confirmed:** no existing file edited, one new review file, authorized nothing, T not activated, nothing committed; T pristine/`NOT_ACTIVATED`, predecessor `OPEN`/`BLOCKED_LEVEL1_FEASIBILITY`, programme claim `OPEN`.
