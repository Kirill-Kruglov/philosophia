from __future__ import annotations

from dataclasses import dataclass
from collections import Counter
from itertools import combinations
from typing import Callable

from .config import MAX_WORD_LENGTH, PANEL_SIZE, PANEL_STRATUM_COUNTS, validate_modulus
from .pool import PoolPartition, partition_cells, verify_partition
from .serialization import CounterStream, DeterministicKey, encode_component, uint16_be, uint32_be
from .world import Cell, admissible_paddings, global_cell_rank, oracle_eq, rank_word, unrank_word, word_count


Eligibility = Callable[[Cell], bool]


@dataclass(frozen=True)
class PanelItem:
    global_id: int
    stratum: str
    local_id: int
    difference: int
    zone: int
    cell: Cell
    cell_identity: tuple[int, ...]
    padding_u: int
    padding_v: int
    left: bytes
    right: bytes
    truth: bool

    def __post_init__(self) -> None:
        if self.stratum not in PANEL_STRATUM_COUNTS:
            raise ValueError("unknown stratum")
        if self.cell.difference != self.difference:
            raise ValueError("panel difference and cell disagree")
        if len(self.left) > MAX_WORD_LENGTH or len(self.right) > MAX_WORD_LENGTH:
            raise ValueError("panel word exceeds the frozen cap")


@dataclass(frozen=True)
class DummyPanel:
    modulus: int
    world_slot: int
    items: tuple[PanelItem, ...]


class DummyPanelBuilder:
    def __init__(self, public_key: DeterministicKey, panel_key: DeterministicKey) -> None:
        if not public_key.test_only or public_key.purpose != "public-root":
            raise PermissionError("dummy builder requires a test-only public root")
        if not panel_key.test_only or panel_key.purpose != "panel":
            raise PermissionError("dummy builder requires a test-only panel key")
        if public_key.material == panel_key.material:
            raise ValueError("public and panel keys must be domain-separated")
        self.public_key = public_key
        self.panel_key = panel_key
        self.partition = partition_cells(public_key)
        verify_partition(self.partition)
        self._reserved_by_rank = tuple(sorted(self.partition.reserved, key=global_cell_rank))

    def build(self, modulus: int, *, world_slot: int) -> DummyPanel:
        validate_modulus(modulus)
        if world_slot < 0:
            raise ValueError("world_slot must be non-negative")
        used_reserved: set[int] = set()
        registries: dict[str, set[tuple[bytes, bytes]]] = {
            name: set() for name in PANEL_STRATUM_COUNTS
        }
        items: list[PanelItem] = []

        def reserved(difference: int, eligibility: Eligibility | None = None) -> Cell:
            predicate = eligibility or (lambda cell: True)
            for cell in self._reserved_by_rank:
                rank = global_cell_rank(cell)
                if cell.difference == difference and rank not in used_reserved and predicate(cell):
                    used_reserved.add(rank)
                    return cell
            raise RuntimeError("reserved-cell exhaustion is design invalidity")

        def add(
            *, global_id: int, stratum: str, local_id: int, difference: int,
            cell: Cell, fixed_padding: tuple[int, int] | None = None,
            positive_v: bool = False, reject_equal: bool = False,
        ) -> None:
            zone = 2 if difference <= 125 else 3
            identity = (global_cell_rank(cell),) if zone == 2 else (cell.a, cell.b)
            padding_u, padding_v = self._paddings(
                world_slot, stratum, global_id, identity, cell, fixed_padding, positive_v
            )
            left, right = self._words(
                world_slot, stratum, global_id, identity, cell, padding_u, padding_v,
                registries[stratum], reject_equal,
            )
            registries[stratum].add((left, right))
            items.append(PanelItem(
                global_id, stratum, local_id, difference, zone, cell, identity,
                padding_u, padding_v, left, right, oracle_eq(left, right, modulus),
            ))

        for local_id in range(1, 125):
            difference = 1 + ((local_id - 1) % (modulus - 1))
            add(global_id=local_id - 1, stratum="S1", local_id=local_id,
                difference=difference, cell=reserved(difference))

        for local_id in range(1, 17):
            difference = modulus if local_id <= 8 else (modulus - 1 if local_id <= 12 else modulus + 1)
            cell = reserved(difference) if difference <= 125 else _corner(difference)
            add(global_id=123 + local_id, stratum="S2", local_id=local_id,
                difference=difference, cell=cell, positive_v=difference > 125)

        for local_id in range(1, 17):
            difference = 0 if local_id <= 8 else (1 if local_id <= 12 else 2)
            add(global_id=139 + local_id, stratum="S3", local_id=local_id,
                difference=difference, cell=reserved(difference),
                positive_v=local_id <= 8, reject_equal=local_id <= 8)

        self._add_s4(modulus, world_slot, items, registries["S4"])

        for local_id in range(1, 17):
            global_id = 171 + local_id
            if local_id <= 4:
                difference = 0
                cell = reserved(difference, lambda value: abs(value.a) >= 95)
                padding, positive_v = (5, 5), False
            elif local_id <= 8:
                difference = modulus
                cell = reserved(
                    difference,
                    lambda value: abs((abs(value.a) + 10) - abs(value.b)) >= 60,
                )
                padding, positive_v = (5, 0), False
            elif local_id <= 12:
                difference = modulus + 2
                cell = reserved(difference) if difference <= 125 else _corner(difference)
                padding, positive_v = None, difference > 125
            else:
                difference = (3, 5, 7, 9)[local_id - 13]
                cell = reserved(
                    difference,
                    lambda value: abs(value.a) >= 95 and abs(value.b) >= 95,
                )
                padding, positive_v = (5, 5), False
            add(global_id=global_id, stratum="S5", local_id=local_id,
                difference=difference, cell=cell, fixed_padding=padding,
                positive_v=positive_v)

        panel = DummyPanel(modulus, world_slot, tuple(items))
        verify_dummy_panel(panel, self.partition)
        return panel

    @staticmethod
    def _identity_domain(
        world_slot: int, stratum: str, global_id: int, side: str,
        identity: tuple[int, ...], purpose: str,
    ) -> tuple[str | int, ...]:
        return ("L1", "panel", world_slot, stratum, global_id, side, *identity, purpose)

    def _paddings(
        self, world_slot: int, stratum: str, global_id: int,
        identity: tuple[int, ...], cell: Cell,
        fixed: tuple[int, int] | None, positive_v: bool,
    ) -> tuple[int, int]:
        if fixed is not None:
            if fixed[0] not in admissible_paddings(cell.a) or fixed[1] not in admissible_paddings(cell.b):
                raise RuntimeError("fixed padding violates the word cap")
            return fixed
        u_values = admissible_paddings(cell.a)
        v_values = tuple(value for value in admissible_paddings(cell.b) if value > 0 or not positive_v)
        if not u_values or not v_values:
            raise RuntimeError("admissible padding set is empty")
        u_stream = CounterStream(self.panel_key, self._identity_domain(
            world_slot, stratum, global_id, "u", identity, "pad"))
        v_stream = CounterStream(self.panel_key, self._identity_domain(
            world_slot, stratum, global_id, "v", identity, "pad"))
        return u_values[u_stream.uniform(len(u_values))], v_values[v_stream.uniform(len(v_values))]

    def _words(
        self, world_slot: int, stratum: str, global_id: int,
        identity: tuple[int, ...], cell: Cell, padding_u: int, padding_v: int,
        registry: set[tuple[bytes, bytes]], reject_equal: bool,
    ) -> tuple[bytes, bytes]:
        u_stream = CounterStream(self.panel_key, self._identity_domain(
            world_slot, stratum, global_id, "u", identity, "rank"))
        v_stream = CounterStream(self.panel_key, self._identity_domain(
            world_slot, stratum, global_id, "v", identity, "rank"))
        left = unrank_word(cell.a, padding_u, u_stream.uniform(word_count(cell.a, padding_u)))
        available_v = word_count(cell.b, padding_v)
        blocked = set()
        for prior_left, prior_right in registry:
            if prior_left != left:
                continue
            right_net, right_padding, _ = rank_word(prior_right)
            if (right_net, right_padding) == (cell.b, padding_v):
                blocked.add(prior_right)
        if reject_equal:
            left_net, left_padding, _ = rank_word(left)
            if (left_net, left_padding) == (cell.b, padding_v):
                blocked.add(left)
        if len(blocked) >= available_v:
            raise RuntimeError("B-1 exhaustion is design invalidity")
        while True:
            right = unrank_word(cell.b, padding_v, v_stream.uniform(available_v))
            if right not in blocked:
                return left, right

    def _add_s4(
        self, modulus: int, world_slot: int, items: list[PanelItem],
        registry: set[tuple[bytes, bytes]],
    ) -> None:
        base = ((1, 1), (1, 2), (2, 1), (2, 2))
        signs = (-1, 1, -1, 1)
        groups = (
            (modulus, base, True),
            (modulus, tuple((u + 1, v + 1) for u, v in base), True),
            (modulus - 2, tuple((u + 1, v + 1) for u, v in base), False),
            (modulus + 2, base, False),
        )
        for group_index, (center, paddings, expected_truth) in enumerate(groups):
            for index, ((padding_u, padding_v), sign) in enumerate(zip(paddings, signs, strict=True)):
                global_id = 156 + group_index * 4 + index
                a, b = center + sign, -(center - sign)
                cell = Cell(a - b, a, b)
                identity = (a, b)
                left, right = self._words(
                    world_slot, "S4", global_id, identity, cell, padding_u, padding_v,
                    registry, False,
                )
                registry.add((left, right))
                item = PanelItem(
                    global_id, "S4", global_id - 155, cell.difference, 3, cell,
                    identity, padding_u, padding_v, left, right,
                    oracle_eq(left, right, modulus),
                )
                if item.truth != expected_truth:
                    raise RuntimeError("S4 construction label mismatch")
                items.append(item)


def _corner(difference: int) -> Cell:
    a, b = (difference + 1) // 2, -(difference // 2)
    return Cell(difference, a, b)


def verify_dummy_panel(panel: DummyPanel, partition: PoolPartition) -> None:
    if len(panel.items) != PANEL_SIZE:
        raise ValueError("panel must contain exactly 188 items")
    if [item.global_id for item in panel.items] != list(range(PANEL_SIZE)):
        raise ValueError("global panel ids are not canonical")
    for stratum, count in PANEL_STRATUM_COUNTS.items():
        values = [item for item in panel.items if item.stratum == stratum]
        if len(values) != count or [item.local_id for item in values] != list(range(1, count + 1)):
            raise ValueError("panel stratum surface changed")
    expected_yes = {"S1": 0, "S2": 8, "S3": 8, "S4": 8, "S5": 8}
    observed_yes = {
        stratum: sum(item.truth for item in panel.items if item.stratum == stratum)
        for stratum in PANEL_STRATUM_COUNTS
    }
    if observed_yes != expected_yes:
        raise ValueError("panel stratum label counts changed")
    reserved_identities = [
        item.cell_identity for item in panel.items if item.zone == 2
    ]
    if len(reserved_identities) != len(set(reserved_identities)):
        raise ValueError("a reserved panel cell was consumed more than once")
    for stratum in PANEL_STRATUM_COUNTS:
        pairs = [
            (item.left, item.right) for item in panel.items if item.stratum == stratum
        ]
        if len(pairs) != len(set(pairs)):
            raise ValueError("a panel word pair repeats within a stratum")
    acquisition = set(partition.acquisition)
    for item in panel.items:
        if item.cell in acquisition:
            raise ValueError("a public acquisition cell was used by the panel")
        if item.truth != (item.difference % panel.modulus == 0):
            raise ValueError("panel label disagrees with Z/n truth")
        if item.zone == 2 and len(item.cell_identity) != 1:
            raise ValueError("reserved identity must be one integer rank")
        if item.zone == 3 and item.cell_identity != (item.cell.a, item.cell.b):
            raise ValueError("zone-3 identity must be endpoint components")


def verify_all_dummy_worlds(
    public_key: DeterministicKey, panel_key: DeterministicKey,
) -> tuple[DummyPanel, ...]:
    builder = DummyPanelBuilder(public_key, panel_key)
    panels = tuple(builder.build(modulus, world_slot=modulus - 66) for modulus in range(66, 126))
    crossings = [
        (panel.modulus, item.stratum, item.difference)
        for panel in panels for item in panel.items
        if item.stratum != "S4" and item.zone == 3
    ]
    expected = (
        [(124, "S5", 126)] * 4
        + [(125, "S2", 126)] * 4
        + [(125, "S5", 127)] * 4
    )
    surfaces = {panel_schema_surface(panel) for panel in panels}
    if len(surfaces) != 1:
        raise ValueError("panel schema surface depends on the world")
    verify_s4_feature_null(panels)
    if sorted(crossings) != sorted(expected):
        raise ValueError("non-S4 edge crossings differ from the amendment")
    return panels


def panel_schema_surface(panel: DummyPanel) -> bytes:
    payload = bytearray(b"philosophia-level1-panel-schema")
    payload.extend(uint16_be(1))
    payload.extend(uint32_be(len(panel.items)))
    for item in panel.items:
        payload.extend(uint16_be(item.global_id))
        payload.extend(encode_component(item.stratum))
        payload.extend(uint16_be(item.local_id))
    return bytes(payload)


def verify_s4_feature_null(panels: tuple[DummyPanel, ...]) -> dict[tuple[str, ...], dict[object, int]]:
    field_names = (
        "symmetry",
        "side_parity",
        "absolute_imbalance",
        "offset_sign",
        "padding",
        "ordered_lengths",
        "total_length",
    )
    records = []
    for panel in panels:
        for item in panel.items[156:172]:
            values = {
                "symmetry": abs(item.cell.a) == abs(item.cell.b),
                "side_parity": (abs(item.cell.a) % 2, abs(item.cell.b) % 2),
                "absolute_imbalance": abs(abs(item.cell.a) - abs(item.cell.b)),
                "offset_sign": 1 if abs(item.cell.a) > abs(item.cell.b) else -1,
                "padding": (item.padding_u, item.padding_v),
                "ordered_lengths": (len(item.left), len(item.right)),
                "total_length": len(item.left) + len(item.right),
            }
            records.append((item.truth, item.difference, values))

    exemptions: dict[tuple[str, ...], dict[object, int]] = {}
    for size in (1, 2, 3):
        for names in combinations(field_names, size):
            yes = Counter(tuple(values[name] for name in names) for truth, _, values in records if truth)
            no = Counter(tuple(values[name] for name in names) for truth, _, values in records if not truth)
            if yes == no:
                continue
            reconstruction: dict[object, set[int]] = {}
            for _, difference, values in records:
                key = tuple(values[name] for name in names)
                reconstruction.setdefault(key, set()).add(difference)
            if any(len(differences) != 1 for differences in reconstruction.values()):
                raise ValueError(f"non-d nuisance combination separates labels: {names}")
            exemptions[names] = {
                key: next(iter(differences))
                for key, differences in reconstruction.items()
            }
    if len(exemptions) != 11:
        raise ValueError("S4 exemption surface differs from the reviewed 11 combinations")
    return exemptions
