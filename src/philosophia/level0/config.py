from __future__ import annotations

from dataclasses import asdict, dataclass, field
import hashlib
import json
from typing import Any, Literal


PINNED_TORCH_VERSION = "2.9.1"
PINNED_PYTHON_VERSION = (3, 12, 3)
RECONSTRUCTION_ID = "level0-companion-v2"
MASTER_SEEDS = (0, 1, 2, 3, 4)


@dataclass(frozen=True)
class ModelConfig:
    modulus: int = 113
    vocabulary_size: int = 114
    equals_token: int = 113
    sequence_length: int = 3
    residual_width: int = 128
    heads: int = 4
    head_width: int = 32
    mlp_width: int = 512
    training_classes: int = 114
    reporting_classes: int = 113

    def __post_init__(self) -> None:
        expected = {
            "modulus": 113,
            "vocabulary_size": 114,
            "equals_token": 113,
            "sequence_length": 3,
            "residual_width": 128,
            "heads": 4,
            "head_width": 32,
            "mlp_width": 512,
            "training_classes": 114,
            "reporting_classes": 113,
        }
        for name, value in expected.items():
            if getattr(self, name) != value:
                raise ValueError(f"{name} is frozen at {value}")
        if self.heads * self.head_width != self.residual_width:
            raise ValueError("attention heads must exactly fill the residual width")


@dataclass(frozen=True)
class ArmConfig:
    identity: Literal["A", "B"]
    role: str
    weight_decay: float
    fixed_epochs: int
    master_seeds: tuple[int, ...]

    def __post_init__(self) -> None:
        if not self.master_seeds or len(set(self.master_seeds)) != len(self.master_seeds):
            raise ValueError("master seeds must be non-empty and unique")
        if any(seed not in MASTER_SEEDS for seed in self.master_seeds):
            raise ValueError("master seeds must come from the frozen 0..4 schedule")

        if self.identity == "A":
            expected = ("paper-mainline-decision", 1.0, 40_000, MASTER_SEEDS)
            actual = (
                self.role,
                self.weight_decay,
                self.fixed_epochs,
                self.master_seeds,
            )
            if actual != expected:
                raise ValueError("Arm A cannot contain artifact-arm or hybrid values")
        elif self.identity == "B":
            if self.role != "artifact-fidelity-control":
                raise ValueError("Arm B role is frozen")
            if self.weight_decay != 0.1 or self.fixed_epochs != 120_000:
                raise ValueError("Arm B cannot contain paper-arm or hybrid values")
            if 1 not in self.master_seeds:
                raise ValueError("Arm B must retain master seed 1 for paired comparison")
            if self.master_seeds != (1,) and len(self.master_seeds) < 3:
                raise ValueError("Arm B uses seed 1 alone or at least three locked seeds")
        else:
            raise ValueError(f"unknown arm identity: {self.identity!r}")


def paper_mainline_arm() -> ArmConfig:
    return ArmConfig(
        identity="A",
        role="paper-mainline-decision",
        weight_decay=1.0,
        fixed_epochs=40_000,
        master_seeds=MASTER_SEEDS,
    )


def artifact_fidelity_arm(master_seeds: tuple[int, ...]) -> ArmConfig:
    return ArmConfig(
        identity="B",
        role="artifact-fidelity-control",
        weight_decay=0.1,
        fixed_epochs=120_000,
        master_seeds=master_seeds,
    )


@dataclass(frozen=True)
class RunConfig:
    arm: ArmConfig
    master_seed: int
    model: ModelConfig = field(default_factory=ModelConfig)
    learning_rate: float = 0.001
    warmup_updates: int = 10
    betas: tuple[float, float] = (0.9, 0.98)
    epsilon: float = 1e-8
    reconstruction_id: str = RECONSTRUCTION_ID

    def __post_init__(self) -> None:
        if self.master_seed not in self.arm.master_seeds:
            raise ValueError("run seed is not admitted by its arm")
        if self.learning_rate != 0.001:
            raise ValueError("learning rate is frozen at 0.001")
        if self.warmup_updates != 10:
            raise ValueError("companion warmup is frozen at ten updates")
        if self.betas != (0.9, 0.98) or self.epsilon != 1e-8:
            raise ValueError("AdamW betas and epsilon are frozen")
        if self.reconstruction_id != RECONSTRUCTION_ID:
            raise ValueError("unknown reconstruction version")

    @property
    def split_seed(self) -> int:
        return self.master_seed

    @property
    def init_seed(self) -> int:
        return 10_000 + self.master_seed


def canonical_dict(config: RunConfig) -> dict[str, Any]:
    return asdict(config)


def canonical_json(config: RunConfig) -> str:
    return json.dumps(
        canonical_dict(config),
        sort_keys=True,
        separators=(",", ":"),
        ensure_ascii=True,
    )


def config_hash(config: RunConfig) -> str:
    return hashlib.sha256(canonical_json(config).encode("ascii")).hexdigest()
