from __future__ import annotations

from dataclasses import dataclass, replace
from datetime import datetime, timezone
import re
from typing import Mapping


NANOSECONDS_PER_SECOND = 1_000_000_000
NANOSECONDS_PER_HOUR = 3600 * NANOSECONDS_PER_SECOND
_HEX64 = re.compile(r"[0-9a-f]{64}")


def parse_utc(value: str) -> datetime:
    if not isinstance(value, str) or re.fullmatch(
        r"[0-9]{4}-[0-9]{2}-[0-9]{2}T[0-9]{2}:[0-9]{2}:[0-9]{2}Z",
        value,
    ) is None:
        raise ValueError("timestamp must use canonical UTC second Z form")
    parsed = datetime.fromisoformat(value[:-1] + "+00:00")
    if parsed.tzinfo != timezone.utc:
        raise ValueError("timestamp must be UTC")
    return parsed


@dataclass(frozen=True)
class TEnvelope:
    device_hour_cap: int = 168
    candidate_cap: int = 12
    review_wall_hours: int = 48
    review_device_hours: int = 40

    def __post_init__(self) -> None:
        if not all(
            type(value) is int
            for value in (
                self.device_hour_cap,
                self.candidate_cap,
                self.review_wall_hours,
                self.review_device_hours,
            )
        ):
            raise ValueError("T envelope values must be integers")
        if min(
            self.device_hour_cap,
            self.candidate_cap,
            self.review_wall_hours,
            self.review_device_hours,
        ) <= 0:
            raise ValueError("T envelope values must be positive")


@dataclass(frozen=True)
class TState:
    activated_utc: str | None = None
    device_nanoseconds: int = 0
    candidate_ids: tuple[str, ...] = ()
    last_review_utc: str | None = None
    device_nanoseconds_at_review: int = 0
    author_stopped: bool = False
    resume_review_pending: bool = False

    def __post_init__(self) -> None:
        if type(self.device_nanoseconds) is not int or type(
            self.device_nanoseconds_at_review
        ) is not int or type(self.author_stopped) is not bool or type(
            self.resume_review_pending
        ) is not bool:
            raise ValueError("T accounting fields have incorrect types")
        if type(self.candidate_ids) is not tuple or not all(
            type(item) is str for item in self.candidate_ids
        ):
            raise ValueError("T candidate_ids must be a tuple of strings")
        if self.candidate_ids:
            raise ValueError(
                "candidate registrations require the absent signed WP-6 authority"
            )
        for name, value in (
            ("activated_utc", self.activated_utc),
            ("last_review_utc", self.last_review_utc),
        ):
            if value is not None and type(value) is not str:
                raise ValueError(f"T {name} must be string or null")
        if self.device_nanoseconds < 0 or self.device_nanoseconds_at_review < 0:
            raise ValueError("T accounting cannot be negative")
        if self.device_nanoseconds_at_review > self.device_nanoseconds:
            raise ValueError("review counter exceeds total device time")
        if len(set(self.candidate_ids)) != len(self.candidate_ids):
            raise ValueError("candidate registrations must be unique")
        if any(_HEX64.fullmatch(item) is None for item in self.candidate_ids):
            raise ValueError("candidate ids must be lowercase SHA-256")
        if self.activated_utc is None:
            if (
                self.device_nanoseconds != 0
                or self.candidate_ids
                or self.last_review_utc is not None
                or self.device_nanoseconds_at_review != 0
                or self.author_stopped
                or self.resume_review_pending
            ):
                raise ValueError("inactive T state must be the exact pristine state")
        else:
            activated = parse_utc(self.activated_utc)
            if self.last_review_utc is not None:
                reviewed = parse_utc(self.last_review_utc)
                if reviewed < activated:
                    raise ValueError("T review predates activation")
            if self.author_stopped and self.last_review_utc is None:
                raise ValueError("author stop requires a completed review")

    def activate(self, timestamp_utc: str) -> "TState":
        if self.activated_utc is not None:
            raise ValueError("T is already activated")
        parse_utc(timestamp_utc)
        return replace(self, activated_utc=timestamp_utc)

    def charge_device_nanoseconds(self, value: int, envelope: TEnvelope) -> "TState":
        if (
            self.activated_utc is None
            or self.author_stopped
            or self.resume_review_pending
        ):
            raise ValueError("T is not available for charging")
        if self.exhausted(envelope):
            raise ValueError("T envelope is already exhausted")
        if value <= 0:
            raise ValueError("device charge must be positive")
        return replace(self, device_nanoseconds=self.device_nanoseconds + value)

    def register_candidate(self, candidate_id: str, envelope: TEnvelope) -> "TState":
        del candidate_id, envelope
        raise PermissionError(
            "candidate registration requires the absent signed WP-6 registry authority"
        )

    def exhausted(self, envelope: TEnvelope) -> bool:
        return self.device_nanoseconds >= (
            envelope.device_hour_cap * NANOSECONDS_PER_HOUR
        )

    def review_due(self, envelope: TEnvelope, timestamp_utc: str) -> bool:
        if self.activated_utc is None:
            return False
        now = parse_utc(timestamp_utc)
        origin = parse_utc(self.last_review_utc or self.activated_utc)
        if now < origin:
            raise ValueError("T review time cannot move backwards")
        wall_due = (now - origin).total_seconds() >= envelope.review_wall_hours * 3600
        device_due = (
            self.device_nanoseconds - self.device_nanoseconds_at_review
            >= envelope.review_device_hours * NANOSECONDS_PER_HOUR
        )
        return wall_due or device_due

    def complete_review(self, envelope: TEnvelope, timestamp_utc: str) -> "TState":
        if self.resume_review_pending:
            raise ValueError("pending resume review requires the durable ResumeGate")
        if not self.review_due(envelope, timestamp_utc):
            raise ValueError("early review cannot reset E3 clocks")
        return replace(
            self,
            last_review_utc=timestamp_utc,
            device_nanoseconds_at_review=self.device_nanoseconds,
        )

    def record_author_stop(self, timestamp_utc: str) -> "TState":
        if self.last_review_utc != timestamp_utc:
            raise ValueError("author stop must be signed at a completed review")
        return replace(self, author_stopped=True)

    def to_mapping(self) -> dict[str, object]:
        return {
            "activated_utc": self.activated_utc,
            "author_stopped": self.author_stopped,
            "candidate_ids": list(self.candidate_ids),
            "device_nanoseconds": self.device_nanoseconds,
            "device_nanoseconds_at_review": self.device_nanoseconds_at_review,
            "last_review_utc": self.last_review_utc,
            "resume_review_pending": self.resume_review_pending,
            "schema": "philosophia.officina.t-state.v2",
        }

    @classmethod
    def from_mapping(cls, value: Mapping[str, object]) -> "TState":
        expected = {
            "activated_utc", "author_stopped", "candidate_ids",
            "device_nanoseconds", "device_nanoseconds_at_review",
            "last_review_utc", "schema",
            "resume_review_pending",
        }
        if set(value) != expected:
            raise ValueError("T state fields differ")
        if value["schema"] != "philosophia.officina.t-state.v2":
            raise ValueError("T state schema mismatch")
        candidates = value["candidate_ids"]
        if not isinstance(candidates, list) or not all(
            type(item) is str for item in candidates
        ):
            raise ValueError("T candidate ids must be strings")
        for field in ("device_nanoseconds", "device_nanoseconds_at_review"):
            if type(value[field]) is not int:
                raise ValueError(f"T {field} must be an integer")
        if type(value["author_stopped"]) is not bool:
            raise ValueError("T author_stopped must be bool")
        if type(value["resume_review_pending"]) is not bool:
            raise ValueError("T resume_review_pending must be bool")
        for field in ("activated_utc", "last_review_utc"):
            if value[field] is not None and type(value[field]) is not str:
                raise ValueError(f"T {field} must be string or null")
        return cls(
            activated_utc=value["activated_utc"],  # type: ignore[arg-type]
            device_nanoseconds=value["device_nanoseconds"],  # type: ignore[arg-type]
            candidate_ids=tuple(candidates),
            last_review_utc=value["last_review_utc"],  # type: ignore[arg-type]
            device_nanoseconds_at_review=value[
                "device_nanoseconds_at_review"
            ],  # type: ignore[arg-type]
            author_stopped=value["author_stopped"],  # type: ignore[arg-type]
            resume_review_pending=value["resume_review_pending"],  # type: ignore[arg-type]
        )
