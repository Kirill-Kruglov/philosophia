from __future__ import annotations

from dataclasses import replace
import hashlib

import pytest

from philosophia.level1.panel import (
    DummyPanelBuilder,
    panel_schema_surface,
    verify_all_dummy_worlds,
    verify_s4_feature_null,
)
from philosophia.level1.serialization import DeterministicKey, dummy_key


def _keys():
    return (
        dummy_key("panel-public", purpose="public-root"),
        dummy_key("panel-secret", purpose="panel"),
    )


def test_dummy_builder_refuses_non_test_and_wrong_purpose_keys() -> None:
    public, panel = _keys()
    non_test = DeterministicKey(b"x" * 32, purpose="panel", test_only=False)
    with pytest.raises(PermissionError):
        DummyPanelBuilder(public, non_test)
    with pytest.raises(PermissionError):
        DummyPanelBuilder(panel, public)


def test_edge_panels_have_exact_crossings_ids_and_positive_v_padding() -> None:
    builder = DummyPanelBuilder(*_keys())
    panel_124 = builder.build(124, world_slot=58)
    panel_125 = builder.build(125, world_slot=59)
    edge_124 = [item for item in panel_124.items if item.stratum != "S4" and item.zone == 3]
    edge_125 = [item for item in panel_125.items if item.stratum != "S4" and item.zone == 3]
    assert [(item.global_id, item.difference, item.cell.identity) for item in edge_124] == [
        (global_id, 126, (63, -63)) for global_id in range(180, 184)
    ]
    assert [(item.global_id, item.difference, item.cell.identity) for item in edge_125] == [
        *[(global_id, 126, (63, -63)) for global_id in range(136, 140)],
        *[(global_id, 127, (64, -63)) for global_id in range(180, 184)],
    ]
    assert all(item.padding_v >= 1 for item in [*edge_124, *edge_125])


def test_s4_surface_and_labels_are_unchanged() -> None:
    panel = DummyPanelBuilder(*_keys()).build(125, world_slot=59)
    s4 = [item for item in panel.items if item.stratum == "S4"]
    assert [item.global_id for item in s4] == list(range(156, 172))
    assert [item.difference for item in s4] == [250] * 8 + [246] * 4 + [254] * 4
    assert [item.truth for item in s4] == [True] * 8 + [False] * 8
    assert all(item.padding_v in (1, 2, 3) for item in s4)


def test_all_world_dummy_enumeration_is_deterministic() -> None:
    first = verify_all_dummy_worlds(*_keys())
    second = verify_all_dummy_worlds(*_keys())
    assert first == second
    assert len(first) == 60
    assert all(len(value.items) == 188 for value in first)
    assert all(sum(item.truth for item in value.items) == 32 for value in first)


def test_schema_surface_and_s4_exemptions_are_frozen() -> None:
    panels = verify_all_dummy_worlds(*_keys())
    assert len({panel_schema_surface(panel) for panel in panels}) == 1
    exemptions = verify_s4_feature_null(panels)
    assert len(exemptions) == 11
    assert all(
        isinstance(difference, int)
        for reconstruction in exemptions.values()
        for difference in reconstruction.values()
    )


def test_reserved_cell_identities_are_golden_at_center_and_edges() -> None:
    builder = DummyPanelBuilder(*_keys())
    expected = {
        66: {
            0: (259,), 124: (14822,), 136: (15010,),
            140: (1,), 172: (19,), 180: (15201,),
        },
        124: {
            0: (259,), 124: (24242,), 136: (24376,),
            140: (1,), 172: (19,), 180: (63, -63),
        },
        125: {
            0: (259,), 124: (24376,), 136: (63, -63),
            140: (1,), 172: (19,), 180: (64, -63),
        },
    }
    for modulus, identities in expected.items():
        panel = builder.build(modulus, world_slot=modulus - 66)
        assert {
            global_id: panel.items[global_id].cell_identity
            for global_id in identities
        } == identities


def test_full_dummy_panel_word_bytes_have_golden_digest() -> None:
    panel = DummyPanelBuilder(*_keys()).build(66, world_slot=0)
    digest = hashlib.sha256()
    for item in panel.items:
        digest.update(item.global_id.to_bytes(2, "big"))
        digest.update(len(item.left).to_bytes(2, "big"))
        digest.update(item.left)
        digest.update(len(item.right).to_bytes(2, "big"))
        digest.update(item.right)
    assert digest.hexdigest() == (
        "93674833af7d3f98bc19079de449acd8bf3e68d5f0acc53f9eefb8084909d9c2"
    )


def test_feature_null_verifier_rejects_non_d_label_separator() -> None:
    panel = DummyPanelBuilder(*_keys()).build(66, world_slot=0)
    items = tuple(
        replace(
            item,
            padding_u=0 if item.truth else 1,
            padding_v=0 if item.truth else 1,
        )
        if item.stratum == "S4"
        else item
        for item in panel.items
    )
    bad_panel = replace(panel, items=items)
    with pytest.raises(ValueError, match="non-d nuisance combination"):
        verify_s4_feature_null((bad_panel,))


def test_s5_fixed_eligibility_and_s3_distinctness() -> None:
    panels = verify_all_dummy_worlds(*_keys())
    for panel in panels:
        for item in panel.items[140:148]:
            assert item.left != item.right
            assert item.padding_v >= 1
        for item in panel.items[172:176]:
            assert item.padding_u == item.padding_v == 5
            assert len(item.left) >= 100 and len(item.right) >= 100
        for item in panel.items[176:180]:
            assert (item.padding_u, item.padding_v) == (5, 0)
            assert abs(len(item.left) - len(item.right)) >= 60
        assert [item.difference for item in panel.items[184:188]] == [3, 5, 7, 9]
