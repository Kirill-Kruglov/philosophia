from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DECISION = ROOT / "canonical" / "AUTHOR_ROUTE_DECISION.md"


TOKENS = (
    "I_SELECT_PHILOSOPHIA_ROUTE_B",
    "I_ACCEPT_DEVELOPMENT_BEFORE_CONFIRMATORY_LOCK",
    "I_KEEP_C1_FIRST_CLASS_IN_THE_SUCCESSOR_LINE",
    "I_ALLOW_SIGNED_DEVICE_SELECTION_BEFORE_CONFIRMATORY_LOCK",
    "I_RESERVE_WALL_FOR_WORLD_ROUTE_AMBIGUITY",
)


def test_route_b_tokens_are_recorded_verbatim_once() -> None:
    text = DECISION.read_text(encoding="utf-8")
    for token in TOKENS:
        assert text.count(token) == 1


def test_route_b_is_governance_only_and_preserves_open_status() -> None:
    text = DECISION.read_text(encoding="utf-8")
    required = (
        "programme-governance decision, not a scientific result",
        "does not authorize a learner choice, device choice",
        "does not authorize",
        "scientific lock",
        "confirmatory run",
        "current programme claim remains `OPEN`",
        "cannot be cited as evidence for C1-C6",
        "no third feasibility intervention",
    )
    for phrase in required:
        assert phrase in text


def test_canonical_surfaces_link_the_author_decision() -> None:
    for path in (
        ROOT / "README.md",
        ROOT / "ROADMAP.md",
        ROOT / "canonical" / "RESULTS_CANONICAL.md",
        ROOT / "canonical" / "CLAIM_LEDGER.md",
        ROOT / "essay" / "climbing-the-wall-of-experience.md",
    ):
        text = path.read_text(encoding="utf-8")
        assert "AUTHOR_ROUTE_DECISION.md" in text, path


def test_public_prose_calls_the_feasibility_stop_a_gate() -> None:
    atlas = (ROOT / "docs" / "index.html").read_text(encoding="utf-8")
    essay = (ROOT / "essay" / "climbing-the-wall-of-experience.md").read_text(
        encoding="utf-8"
    )
    assert "The Workshop stopped at its own gate before the experiment." in atlas
    assert "It reached a different gate:" in essay
    assert "reached a wall before the experiment" not in atlas
    assert "It located a different wall:" not in essay
