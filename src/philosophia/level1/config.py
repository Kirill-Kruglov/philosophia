from __future__ import annotations

from dataclasses import dataclass


MIN_MODULUS = 66
MAX_MODULUS = 125
PAIR_COUNT = 30
DEVELOPMENT_PAIRS_PER_STRATUM = 2
OUTCOME_PAIRS_PER_STRATUM = 8
STRATUM_COUNT = 3

A_WORD = 128
D_ACQ = 125
MAX_PADDING = 5
MAX_WORD_LENGTH = 138
MODEL_INPUT_LENGTH = 277
POOL_MULTIPLICITY = 4

BUDGET = 2_000
SHORTLIST_SIZE = 512
COMMITTEE_SIZE = 4
REPLICATES = (1, 2)
CHECKPOINT_CADENCE = 50
PERSISTENCE_CHECKPOINTS = 5
PERSISTENCE_SPAN = 200

PANEL_STRATUM_COUNTS = {
    "S1": 124,
    "S2": 16,
    "S3": 16,
    "S4": 16,
    "S5": 16,
}
PANEL_SIZE = 188


@dataclass(frozen=True)
class Level1Config:
    min_modulus: int = MIN_MODULUS
    max_modulus: int = MAX_MODULUS
    a_word: int = A_WORD
    d_acq: int = D_ACQ
    max_padding: int = MAX_PADDING
    max_word_length: int = MAX_WORD_LENGTH
    model_input_length: int = MODEL_INPUT_LENGTH
    pool_multiplicity: int = POOL_MULTIPLICITY
    budget: int = BUDGET

    def __post_init__(self) -> None:
        frozen = {
            "min_modulus": MIN_MODULUS,
            "max_modulus": MAX_MODULUS,
            "a_word": A_WORD,
            "d_acq": D_ACQ,
            "max_padding": MAX_PADDING,
            "max_word_length": MAX_WORD_LENGTH,
            "model_input_length": MODEL_INPUT_LENGTH,
            "pool_multiplicity": POOL_MULTIPLICITY,
            "budget": BUDGET,
        }
        for name, expected in frozen.items():
            if getattr(self, name) != expected:
                raise ValueError(f"{name} is frozen at {expected}")
        self.verify_geometry()

    def verify_geometry(self) -> None:
        if 2 * self.a_word < 2 * self.max_modulus + 4:
            raise ValueError("S4 high tooth is not realizable")
        if 2 * self.min_modulus - 4 <= self.d_acq:
            raise ValueError("S4 low tooth contacts acquisition support")
        if self.max_modulus > self.d_acq:
            raise ValueError("single-wrap contact must remain available")
        if self.max_word_length != self.a_word + 10:
            raise ValueError("word-length padding slack changed")
        if self.model_input_length != 2 * self.max_word_length + 1:
            raise ValueError("model input no longer holds two words plus SEP")


def validate_modulus(modulus: int) -> int:
    if not MIN_MODULUS <= modulus <= MAX_MODULUS:
        raise ValueError(f"modulus must be in [{MIN_MODULUS}, {MAX_MODULUS}]")
    return modulus
