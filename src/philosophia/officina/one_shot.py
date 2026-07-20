from __future__ import annotations

from enum import Enum
import json
from pathlib import Path
import re
from typing import Mapping

from .canonical import (
    atomic_create,
    atomic_replace,
    canonical_json,
    load_canonical_json,
    sha256_bytes,
)
from .terminal import QTerminal, QValidity


GENESIS = "0" * 64
_HEX64 = re.compile(r"[0-9a-f]{64}")


def _is_sha256(value: object) -> bool:
    return isinstance(value, str) and _HEX64.fullmatch(value) is not None


class AttemptPhase(str, Enum):
    CLAIMED = "CLAIMED"
    DRAW_ARMED = "DRAW_ARMED"
    LAUNCHED = "LAUNCHED"
    TERMINAL = "TERMINAL"


def _head(schema: str, events: list[dict[str, object]]) -> bytes:
    return canonical_json(
        {
            "entry_count": len(events),
            "head_sha256": str(events[-1]["event_sha256"]) if events else GENESIS,
            "schema": schema,
            "scientific_outcome": False,
        }
    )


def _read_chain(directory: Path, *, stem: str) -> list[dict[str, object]]:
    events: list[dict[str, object]] = []
    event_paths = sorted(directory.glob(f"[0-9][0-9][0-9]-{stem}-*.json"))
    expected_names = {"HEAD.json", *(path.name for path in event_paths)}
    actual_names = {path.name for path in directory.iterdir() if path.is_file()}
    if actual_names != expected_names:
        raise ValueError(f"{stem} journal files differ")
    for index, path in enumerate(event_paths):
        value = load_canonical_json(path)
        expected_keys = {
            "event_sha256", "payload", "phase", "previous_sha256", "sequence"
        }
        if not isinstance(value, dict) or set(value) != expected_keys:
            raise ValueError(f"{stem} event fields differ")
        if type(value["sequence"]) is not int or value["sequence"] != index:
            raise ValueError(f"{stem} sequence mismatch")
        previous = GENESIS if not events else str(events[-1]["event_sha256"])
        if value["previous_sha256"] != previous:
            raise ValueError(f"{stem} hash chain mismatch")
        payload = {key: item for key, item in value.items() if key != "event_sha256"}
        if value["event_sha256"] != sha256_bytes(canonical_json(payload)):
            raise ValueError(f"{stem} event hash mismatch")
        events.append(value)
    return events


class AttemptRegistry:
    """External append-only commitment to attempt ids and journal heads."""

    SCHEMA = "philosophia.officina.attempt-registry-head.v1"

    def __init__(self, directory: Path) -> None:
        self.directory = directory
        self.head_path = directory / "HEAD.json"

    def initialize(self) -> None:
        self.directory.mkdir(parents=True, exist_ok=True)
        atomic_create(self.head_path, _head(self.SCHEMA, []))

    def _events(self) -> list[dict[str, object]]:
        if not self.head_path.exists():
            raise ValueError("attempt registry is not initialized")
        events = _read_chain(self.directory, stem="registry")
        if canonical_json(load_canonical_json(self.head_path)) != canonical_json(
            json.loads(_head(self.SCHEMA, events))
        ):
            raise ValueError("attempt registry head mismatch")
        for event in events:
            payload = event["payload"]
            if not isinstance(payload, dict) or set(payload) != {
                "attempt_id", "journal_head", "phase"
            }:
                raise ValueError("attempt registry payload fields differ")
            if (
                type(payload["attempt_id"]) is not int
                or not _is_sha256(payload["journal_head"])
                or payload["phase"] not in {phase.value for phase in AttemptPhase}
            ):
                raise ValueError("attempt registry payload values are malformed")
        return events

    def assert_unused(self, attempt_id: int) -> None:
        if type(attempt_id) is not int or attempt_id < 0:
            raise ValueError("attempt id must be a non-negative integer")
        if any(event["payload"]["attempt_id"] == attempt_id for event in self._events()):
            raise ValueError("attempt id has already been used")

    def latest_for(self, attempt_id: int) -> dict[str, object] | None:
        matches = [
            event for event in self._events()
            if event["payload"]["attempt_id"] == attempt_id
        ]
        return matches[-1] if matches else None

    def append(
        self, *, attempt_id: int, phase: AttemptPhase, journal_head: str
    ) -> dict[str, object]:
        events = self._events()
        payload = {
            "attempt_id": attempt_id,
            "journal_head": journal_head,
            "phase": phase.value,
        }
        sequence = len(events)
        core = {
            "payload": payload,
            "phase": "REGISTRY",
            "previous_sha256": GENESIS if not events else events[-1]["event_sha256"],
            "sequence": sequence,
        }
        event = {**core, "event_sha256": sha256_bytes(canonical_json(core))}
        atomic_create(
            self.directory / f"{sequence:03d}-registry-{attempt_id}.json",
            canonical_json(event),
        )
        atomic_replace(self.head_path, _head(self.SCHEMA, [*events, event]))
        return event


class OneShotJournal:
    """Fail-closed Q attempt journal. It performs no entropy draw or launch."""

    SCHEMA = "philosophia.officina.attempt-head.v1"

    def __init__(
        self, directory: Path, *, attempt_id: int, registry: AttemptRegistry
    ) -> None:
        if type(attempt_id) is not int or attempt_id < 0:
            raise ValueError("attempt id must be a non-negative integer")
        self.directory = directory
        self.attempt_id = attempt_id
        self.registry = registry
        self.head_path = directory / "HEAD.json"

    def _events(self) -> list[dict[str, object]]:
        if not self.head_path.exists():
            return []
        events = _read_chain(self.directory, stem="attempt")
        if canonical_json(load_canonical_json(self.head_path)) != canonical_json(
            json.loads(_head(self.SCHEMA, events))
        ):
            raise ValueError("one-shot journal head mismatch")
        previous: AttemptPhase | None = None
        for event in events:
            phase = AttemptPhase(str(event["phase"]))
            payload = event["payload"]
            if not isinstance(payload, dict):
                raise ValueError("attempt event payload must be an object")
            self._validate_transition(previous, phase, payload)
            previous = phase
        latest = self.registry.latest_for(self.attempt_id)
        if not events or latest is None:
            raise ValueError("journal is not committed by the attempt registry")
        if latest["payload"] != {
            "attempt_id": self.attempt_id,
            "journal_head": events[-1]["event_sha256"],
            "phase": events[-1]["phase"],
        }:
            raise ValueError("attempt registry and journal head differ")
        return events

    def _append(self, phase: AttemptPhase, payload: Mapping[str, object]) -> dict[str, object]:
        events = self._events()
        previous_phase = AttemptPhase(str(events[-1]["phase"])) if events else None
        allowed = (
            (previous_phase is None and phase is AttemptPhase.CLAIMED)
            or (previous_phase is AttemptPhase.CLAIMED and phase in {
                AttemptPhase.DRAW_ARMED, AttemptPhase.TERMINAL
            })
            or (previous_phase is AttemptPhase.DRAW_ARMED and phase in {
                AttemptPhase.LAUNCHED, AttemptPhase.TERMINAL
            })
            or (previous_phase is AttemptPhase.LAUNCHED and phase is AttemptPhase.TERMINAL)
        )
        if not allowed:
            raise ValueError(f"invalid one-shot transition: {previous_phase} -> {phase}")
        self._validate_transition(previous_phase, phase, payload)
        sequence = len(events)
        core = {
            "payload": dict(payload),
            "phase": phase.value,
            "previous_sha256": GENESIS if not events else events[-1]["event_sha256"],
            "sequence": sequence,
        }
        event = {**core, "event_sha256": sha256_bytes(canonical_json(core))}
        if not events:
            self.registry.assert_unused(self.attempt_id)
            self.directory.mkdir(parents=True, exist_ok=False)
            atomic_create(self.head_path, _head(self.SCHEMA, []))
        atomic_create(
            self.directory / f"{sequence:03d}-attempt-{phase.value.lower()}.json",
            canonical_json(event),
        )
        atomic_replace(self.head_path, _head(self.SCHEMA, [*events, event]))
        self.registry.append(
            attempt_id=self.attempt_id,
            phase=phase,
            journal_head=str(event["event_sha256"]),
        )
        return event

    @staticmethod
    def _validate_transition(
        previous: AttemptPhase | None,
        phase: AttemptPhase,
        payload: Mapping[str, object],
    ) -> None:
        keys = set(payload)
        if previous is None:
            if phase is not AttemptPhase.CLAIMED or keys != {
                "attempt_id", "manifest_sha256"
            }:
                raise ValueError("initial attempt claim payload differs")
            if type(payload["attempt_id"]) is not int or not isinstance(
                payload["manifest_sha256"], str
            ):
                raise ValueError("initial attempt claim values are malformed")
            if not _is_sha256(payload["manifest_sha256"]):
                raise ValueError("candidate manifest commitment is not SHA-256")
            return
        if previous is AttemptPhase.CLAIMED and phase is AttemptPhase.DRAW_ARMED:
            if (
                keys != {"source"}
                or not isinstance(payload["source"], str)
                or not payload["source"]
            ):
                raise ValueError("draw-armed payload differs")
            return
        if previous is AttemptPhase.CLAIMED and phase is AttemptPhase.TERMINAL:
            expected = {
                "charged", "competence", "disposition", "reason", "signature_id"
            }
            if (
                keys != expected
                or payload["charged"] is not False
                or payload["competence"] is not None
                or payload["disposition"] != "PRE_ENTROPY_STOP"
                or not isinstance(payload["reason"], str)
                or not payload["reason"]
                or not isinstance(payload["signature_id"], str)
                or not payload["signature_id"]
            ):
                raise ValueError("pre-entropy disposition payload differs")
            return
        if previous is AttemptPhase.DRAW_ARMED and phase is AttemptPhase.LAUNCHED:
            if (
                keys != {"charged", "root_commitment"}
                or payload["charged"] is not True
                or not _is_sha256(payload["root_commitment"])
            ):
                raise ValueError("launch commitment payload differs")
            return
        if (
            previous in {AttemptPhase.DRAW_ARMED, AttemptPhase.LAUNCHED}
            and phase is AttemptPhase.TERMINAL
        ):
            if keys != {"charged", "q_terminal"} or payload["charged"] is not True:
                raise ValueError("charged Q terminal payload differs")
            terminal = QTerminal.from_mapping(payload["q_terminal"])
            if (
                previous is AttemptPhase.DRAW_ARMED
                and terminal.validity is not QValidity.INVALID
            ):
                raise ValueError("draw-armed ambiguity requires Q invalid")
            return
        raise ValueError("one-shot transition validator has no matching branch")

    def create_claim(self, manifest_sha256: str) -> dict[str, object]:
        if not _is_sha256(manifest_sha256):
            raise ValueError("candidate manifest commitment must be SHA-256")
        return self._append(
            AttemptPhase.CLAIMED,
            {"attempt_id": self.attempt_id, "manifest_sha256": manifest_sha256},
        )

    def record_pre_entropy_disposition(
        self, *, signature_id: str, reason: str
    ) -> dict[str, object]:
        if not signature_id or not reason:
            raise ValueError("pre-entropy disposition must be signed and reasoned")
        events = self._events()
        if (
            not events
            or AttemptPhase(str(events[-1]["phase"])) is not AttemptPhase.CLAIMED
        ):
            raise ValueError("pre-entropy disposition is valid only from CLAIMED")
        return self._append(
            AttemptPhase.TERMINAL,
            {
                "charged": False,
                "competence": None,
                "disposition": "PRE_ENTROPY_STOP",
                "reason": reason,
                "signature_id": signature_id,
            },
        )

    def arm_draw(self, source: str) -> dict[str, object]:
        if not source:
            raise ValueError("entropy source must be named")
        return self._append(AttemptPhase.DRAW_ARMED, {"source": source})

    def record_launch_commitment(self, root_commitment: str) -> dict[str, object]:
        if not _is_sha256(root_commitment):
            raise ValueError("root commitment must be SHA-256")
        return self._append(
            AttemptPhase.LAUNCHED,
            {"charged": True, "root_commitment": root_commitment},
        )

    def record_q_terminal(self, terminal: QTerminal) -> dict[str, object]:
        if type(terminal) is not QTerminal:
            raise TypeError("Q journal terminal must be an exact QTerminal")
        canonical_terminal = QTerminal.from_mapping(terminal.to_mapping())
        events = self._events()
        if not events:
            raise ValueError("attempt has no claim")
        phase = AttemptPhase(str(events[-1]["phase"]))
        if (
            phase is AttemptPhase.DRAW_ARMED
            and canonical_terminal.validity is not QValidity.INVALID
        ):
            raise ValueError("draw-armed ambiguity can close only as charged Q invalid")
        if phase not in {AttemptPhase.DRAW_ARMED, AttemptPhase.LAUNCHED}:
            raise ValueError("Q terminal requires a charged attempt")
        return self._append(
            AttemptPhase.TERMINAL,
            {"charged": True, "q_terminal": canonical_terminal.to_mapping()},
        )

    def recovery_requires_charge(self) -> bool:
        events = self._events()
        return bool(events) and AttemptPhase(str(events[-1]["phase"])) in {
            AttemptPhase.DRAW_ARMED,
            AttemptPhase.LAUNCHED,
        }
