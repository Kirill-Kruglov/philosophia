#!/usr/bin/env python3
"""L0 Stage-B schema, canonical bytes, causes and renderer regressions."""

from __future__ import annotations

import ast
import hashlib
import json
import sys
import unittest
from pathlib import Path

LEARNING_DIR = Path(__file__).resolve().parent
if str(LEARNING_DIR) not in sys.path:
    sys.path.insert(0, str(LEARNING_DIR))

from phase2_stageb_canonical import canonical_bytes, canonical_dumps, canonical_hash
from phase2_stageb_causes import (
    CAUSE_PLAN_CONSTRAINT_INVALID,
    CAUSE_PLAN_NON_NORMAL,
    CAUSE_PLAN_SCHEMA_INVALID,
    CAUSE_PLAN_TYPE_INVALID,
    CAUSE_QUERY_MEASUREMENT_OVERFLOW,
    CAUSE_SEQUENT_REDERIVATION_MISMATCH,
    DEV_CORE_FEASIBILITY_STOP_REASONS,
    DRAW_CAUSES,
    L1_CAUSES,
    MUTATION_TO_CAUSE,
    TOP_LEVEL_TERMINALS,
)
from phase2_stageb_render import render_sequent
from phase2_stageb_schema import (
    BAND_EDGES,
    DEV_QUERY_MEASUREMENT_N_POSITIONS,
    FAMILY_ORDER,
    MAX_FORMULA_NODES,
    THEORY_SHA256,
    band_of_node_count,
)


def _atom(name):
    return {'kind': 'ATOM', 'name': name}


def _and(left, right):
    return {'kind': 'AND', 'left': left, 'right': right}


def _or(left, right):
    return {'kind': 'OR', 'left': left, 'right': right}


RENDERER_AND_COMMUTE = (
    "[('a0 : prop) -> ('a1 : prop) -> (and 'a0 'a1) -> (and 'a1 'a0)]"
)
RENDERER_OR_COMMUTE = (
    "[('a0 : prop) -> ('a1 : prop) -> (or 'a0 'a1) -> (or 'a1 'a0)]"
)


class TestStageBL0(unittest.TestCase):
    def test_schema_constants(self):
        self.assertEqual(MAX_FORMULA_NODES, 24)
        self.assertEqual(DEV_QUERY_MEASUREMENT_N_POSITIONS, 4096)
        self.assertEqual(
            BAND_EDGES,
            (('S1', 8, 11), ('S2', 12, 17), ('S3', 18, 25), ('S4', 26, 37)),
        )
        self.assertEqual(
            FAMILY_ORDER,
            (
                'AND_INTRO', 'AND_ELIM', 'OR_INTRO', 'OR_ELIM',
                'NOT_INTRO', 'NOT_ELIM', 'EXFALSO',
            ),
        )
        self.assertEqual(band_of_node_count(8), 'S1')
        self.assertEqual(band_of_node_count(11), 'S1')
        self.assertEqual(band_of_node_count(12), 'S2')
        self.assertEqual(band_of_node_count(17), 'S2')
        self.assertEqual(band_of_node_count(18), 'S3')
        self.assertEqual(band_of_node_count(25), 'S3')
        self.assertEqual(band_of_node_count(26), 'S4')
        self.assertEqual(band_of_node_count(37), 'S4')
        self.assertIsNone(band_of_node_count(7))
        self.assertIsNone(band_of_node_count(38))
        self.assertEqual(
            THEORY_SHA256,
            '2056deaf9c12a81dcb047e60154e8a473ffe235b5e48bb9433eb1d9f70afb507',
        )

    def test_constants_live_only_in_schema_module(self):
        names = (
            'MAX_FORMULA_NODES',
            'DEV_QUERY_MEASUREMENT_N_POSITIONS',
            'BAND_EDGES',
            'FAMILY_ORDER',
        )
        for filename in (
                'phase2_stageb_canonical.py',
                'phase2_stageb_causes.py',
                'phase2_stageb_render.py',
                'phase2_stageb_checker.py',
        ):
            tree = ast.parse((LEARNING_DIR / filename).read_text(encoding='utf-8'))
            assigned = set()
            for node in ast.walk(tree):
                if isinstance(node, ast.Assign):
                    for target in node.targets:
                        if isinstance(target, ast.Name):
                            assigned.add(target.id)
            for name in names:
                with self.subTest(filename=filename, name=name):
                    self.assertNotIn(name, assigned)

    def test_canonical_ascii_json_and_hash(self):
        obj = {'b': 1, 'a': {'z': True, 'm': 'x'}}
        dumped = canonical_dumps(obj)
        self.assertEqual(dumped, '{"a":{"m":"x","z":true},"b":1}')
        self.assertEqual(canonical_bytes(obj), dumped.encode('ascii'))
        self.assertEqual(
            canonical_hash(obj),
            hashlib.sha256(dumped.encode('ascii')).hexdigest(),
        )
        self.assertEqual(canonical_hash(obj), canonical_hash(obj).lower())
        self.assertNotIn('\\u', dumped)

    def test_closed_causes_and_mutation_mapping(self):
        self.assertEqual(
            L1_CAUSES,
            (
                CAUSE_PLAN_SCHEMA_INVALID,
                CAUSE_PLAN_TYPE_INVALID,
                CAUSE_PLAN_CONSTRAINT_INVALID,
                CAUSE_PLAN_NON_NORMAL,
            ),
        )
        self.assertEqual(CAUSE_SEQUENT_REDERIVATION_MISMATCH, 'SEQUENT_REDERIVATION_MISMATCH')
        self.assertNotIn(CAUSE_SEQUENT_REDERIVATION_MISMATCH, L1_CAUSES)
        self.assertEqual(
            TOP_LEVEL_TERMINALS,
            (
                'DEV_CORE_FEASIBILITY_STOP',
                'DEV_CORE_FEASIBLE_FOR_AUDIT_CONTRACT',
            ),
        )
        self.assertEqual(
            DEV_CORE_FEASIBILITY_STOP_REASONS,
            (
                'PREMISE_ENUMERABILITY_FAILED',
                'DAG_ENUMERABILITY_FAILED',
                'DAG_REPLAY_FAILED',
                'CHECKER_UNSOUND',
                'COMPILER_UNSOUND',
                'MUTATION_ESCAPE',
                'PUBLIC_PROJECTION_LEAK',
                'COLLISION_ACCOUNTING_ERROR',
                'NONDETERMINISM',
                'COMPILER_FAMILY_UNREACHABLE',
                'QUERY_MEASUREMENT_OVERFLOW',
                'ROOT_QUOTA_UNFILLED',
                'RESOURCE_CEILING_EXHAUSTED',
            ),
        )
        self.assertEqual(
            DRAW_CAUSES,
            (
                'PLAN_CONSTRUCTION_FAILED',
                'PLAN_SCHEMA_INVALID',
                'PLAN_TYPE_INVALID',
                'PLAN_CONSTRAINT_INVALID',
                'PLAN_NON_NORMAL',
                'SEQUENT_REDERIVATION_MISMATCH',
                'CLASSICAL_COUNTEREXAMPLE',
                'THEOREM_ID_COLLISION',
                'SKELETON_ID_COLLISION',
                'COMPILER_NO_MATCH',
                'COMPILER_AMBIGUOUS_MATCH',
                'PEANO_REPLAY_REFUSAL',
                'PEANO_REPLAY_NONTERMINAL',
                'QUERY_MEASUREMENT_OVERFLOW',
                'TARGET_BAND_ALREADY_FULL',
            ),
        )
        self.assertEqual(len(TOP_LEVEL_TERMINALS), 2)
        self.assertEqual(len(DEV_CORE_FEASIBILITY_STOP_REASONS), 13)
        self.assertEqual(len(DRAW_CAUSES), 15)
        self.assertIn(CAUSE_SEQUENT_REDERIVATION_MISMATCH, DRAW_CAUSES)
        self.assertEqual(CAUSE_QUERY_MEASUREMENT_OVERFLOW, 'QUERY_MEASUREMENT_OVERFLOW')
        self.assertIn(CAUSE_QUERY_MEASUREMENT_OVERFLOW, DRAW_CAUSES)
        self.assertIn(CAUSE_QUERY_MEASUREMENT_OVERFLOW, DEV_CORE_FEASIBILITY_STOP_REASONS)
        self.assertEqual(
            MUTATION_TO_CAUSE,
            (
                ('wrong kind/key/type/string/atom-name/ID/atom-list', 'PLAN_SCHEMA_INVALID'),
                ('duplicate or shadowed hypothesis ID', 'PLAN_SCHEMA_INVALID'),
                ('missing or out-of-scope hypothesis reference', 'PLAN_TYPE_INVALID'),
                ('wrong child/conclusion/root goal', 'PLAN_TYPE_INVALID'),
                ('wrong discharge formula', 'PLAN_TYPE_INVALID'),
                ('undeclared or unused declared atom', 'PLAN_CONSTRAINT_INVALID'),
                ('unused global/local hypothesis', 'PLAN_CONSTRAINT_INVALID'),
                ('duplicate global hypothesis formula', 'PLAN_CONSTRAINT_INVALID'),
                ('formula bound', 'PLAN_CONSTRAINT_INVALID'),
                ('node-count/band/expectation mismatch', 'PLAN_CONSTRAINT_INVALID'),
                ('shallow dependency/too few families/no branching', 'PLAN_CONSTRAINT_INVALID'),
                ('each section-2.3 beta-redex', 'PLAN_NON_NORMAL'),
            ),
        )

    def test_renderer_and_commute_anchor(self):
        sequent = render_sequent(
            ['a0', 'a1'],
            [_and(_atom('a0'), _atom('a1'))],
            _and(_atom('a1'), _atom('a0')),
        )
        self.assertEqual(sequent, RENDERER_AND_COMMUTE)
        self.assertEqual(sequent, sequent.encode('ascii').decode('ascii'))

    def test_renderer_or_commute_anchor(self):
        sequent = render_sequent(
            ['a0', 'a1'],
            [_or(_atom('a0'), _atom('a1'))],
            _or(_atom('a1'), _atom('a0')),
        )
        self.assertEqual(sequent, RENDERER_OR_COMMUTE)

    def test_renderer_zero_hypotheses_and_no_cardinality_check(self):
        sequent = render_sequent(['a0', 'a1'], [], _atom('a0'))
        self.assertEqual(sequent, "[('a0 : prop) -> ('a1 : prop) -> 'a0]")
        two = render_sequent(['a0', 'a1'], [_atom('a0')], _atom('a0'))
        self.assertEqual(two, "[('a0 : prop) -> ('a1 : prop) -> 'a0 -> 'a0]")


if __name__ == '__main__':
    unittest.main()
