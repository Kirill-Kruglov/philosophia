from __future__ import annotations

from dataclasses import dataclass
from enum import Enum
from pathlib import Path
from typing import Mapping

from .canonical import atomic_create, canonical_json, load_canonical_json, sha256_bytes


class AttemptPhase(str, Enum):
    CLAIMED = "CLAIMED"
    DRAW_ARMED = "DRAW_ARMED"
    LAUNCHED = "LAUNCHED"
    TERMINAL = "TERMINAL"


@dataclass(frozen=True)
class AttemptEvent:
    phase: AttemptPhase
    charged: bool
    payload: Mapping[str, object]


class OneShotJournal:
    """Immutable event journal around a caller-owned future entropy invocation."""

    def __init__(self, directory: Path) -> None:
        self.directory = directory

    def _path(self, sequence: int, phase: AttemptPhase) -> Path:
        return self.directory / f"{sequence:03d}-{phase.value.lower()}.json"

    def _events(self) -> list[dict[str, object]]:
        if not self.directory.exists():
            return []
        events: list[dict[str, object]] = []
        for index, path in enumerate(sorted(self.directory.glob("*.json"))):
            value = load_canonical_json(path)
            if not isinstance(value, dict) or value.get("sequence") != index:
                raise ValueError("one-shot journal sequence mismatch")
            previous = "0" * 64 if not events else str(events[-1]["event_sha256"])
            if value.get("previous_sha256") != previous:
                raise ValueError("one-shot journal hash chain mismatch")
            payload = {key: item for key, item in value.items() if key != "event_sha256"}
            if value.get("event_sha256") != sha256_bytes(canonical_json(payload)):
                raise ValueError("one-shot journal event hash mismatch")
            events.append(value)
        return events

    def _append(self, phase: AttemptPhase, payload: Mapping[str, object]) -> dict[str, object]:
        events = self._events()
        previous_phase = AttemptPhase(str(events[-1]["phase"])) if events else None
        allowed = (
            (previous_phase is None and phase is AttemptPhase.CLAIMED)
            or (previous_phase is AttemptPhase.CLAIMED and phase is AttemptPhase.DRAW_ARMED)
            or (
                previous_phase is AttemptPhase.DRAW_ARMED
                and phase in {AttemptPhase.LAUNCHED, AttemptPhase.TERMINAL}
            )
            or (previous_phase is AttemptPhase.LAUNCHED and phase is AttemptPhase.TERMINAL)
        )
        if not allowed:
            raise ValueError(f"invalid one-shot transition: {previous_phase} -> {phase}")
        if previous_phase is AttemptPhase.DRAW_ARMED and phase is AttemptPhase.TERMINAL:
            if payload.get("charged") is not True or payload.get("competence") is not None:
                raise ValueError("ambiguous draw recovery must be charged with competence unset")
        sequence = len(events)
        previous_hash = "0" * 64 if not events else str(events[-1]["event_sha256"])
        core = {
            "payload": dict(payload),
            "phase": phase.value,
            "previous_sha256": previous_hash,
            "sequence": sequence,
        }
        event = {**core, "event_sha256": sha256_bytes(canonical_json(core))}
        atomic_create(self._path(sequence, phase), canonical_json(event))
        return event

    def create_claim(self, payload: Mapping[str, object]) -> dict[str, object]:
        return self._append(AttemptPhase.CLAIMED, payload)

    def arm_draw(self, payload: Mapping[str, object]) -> dict[str, object]:
        return self._append(AttemptPhase.DRAW_ARMED, payload)

    def record_launch_commitment(self, root_commitment: str) -> dict[str, object]:
        if len(root_commitment) != 64:
            raise ValueError("root commitment must be SHA-256")
        return self._append(
            AttemptPhase.LAUNCHED,
            {"charged": True, "root_commitment": root_commitment},
        )

    def record_terminal(self, payload: Mapping[str, object]) -> dict[str, object]:
        return self._append(AttemptPhase.TERMINAL, payload)

    def recovery_requires_charge(self) -> bool:
        events = self._events()
        if not events:
            return False
        return AttemptPhase(str(events[-1]["phase"])) in {
            AttemptPhase.DRAW_ARMED,
            AttemptPhase.LAUNCHED,
        }
