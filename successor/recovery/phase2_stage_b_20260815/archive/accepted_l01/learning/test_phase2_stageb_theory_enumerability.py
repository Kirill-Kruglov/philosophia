#!/usr/bin/env python3
"""L0 Peano enumerability for the intuitionistic fragment. No search or plans."""

from __future__ import annotations

import sys
import unittest
from pathlib import Path

import peano

LEARNING_DIR = Path(__file__).resolve().parent
if str(LEARNING_DIR) not in sys.path:
    sys.path.insert(0, str(LEARNING_DIR))

from phase2_stageb_schema import (
    DIRECTION_BACKWARD,
    DIRECTION_FORWARD,
    REQUIRED_DIRECTIONS,
    THEORY_FILENAME,
    THEORY_PREMISES,
    THEORY_SHA256,
)


THEORY_PATH = LEARNING_DIR / 'theories' / THEORY_FILENAME

ANNOTATION_ABSENT = 'ABSENT'

WITNESS_GOALS = {
    'and_i': "[('a0 : prop) -> ('a1 : prop) -> (and 'a0 'a1)]",
    'and_el': "[('a0 : prop) -> ('a1 : prop) -> (and 'a0 'a1) -> 'a0]",
    'and_er': "[('a0 : prop) -> ('a1 : prop) -> (and 'a0 'a1) -> 'a1]",
    'or_il': "[('a0 : prop) -> ('a1 : prop) -> 'a0 -> (or 'a0 'a1)]",
    'or_ir': "[('a0 : prop) -> ('a1 : prop) -> 'a1 -> (or 'a0 'a1)]",
    'or_e': "[('a0 : prop) -> ('a1 : prop) -> (or 'a0 'a1) -> (or 'a1 'a0)]",
    'not_i': "[('a0 : prop) -> ['a0 -> false] -> (not 'a0)]",
    'not_e': "[('a0 : prop) -> (not 'a0) -> 'a0 -> false]",
    'exfalso': "[false -> ('a0 : prop) -> 'a0]",
}

FROZEN_PREMISE_TABLE = (
    {
        'premise': 'and_i',
        'annotation_text_or_ABSENT': '#backward and_i.',
        'enumerable': True,
        'enumerable_directions': (DIRECTION_BACKWARD,),
        'required_direction': DIRECTION_BACKWARD,
        'witness_state': WITNESS_GOALS['and_i'],
    },
    {
        'premise': 'and_el',
        'annotation_text_or_ABSENT': "#forward and_el ('_ : (and 'P 'Q)).",
        'enumerable': True,
        'enumerable_directions': (DIRECTION_FORWARD,),
        'required_direction': DIRECTION_FORWARD,
        'witness_state': WITNESS_GOALS['and_el'],
    },
    {
        'premise': 'and_er',
        'annotation_text_or_ABSENT': "#forward and_er ('_ : (and 'P 'Q)).",
        'enumerable': True,
        'enumerable_directions': (DIRECTION_FORWARD,),
        'required_direction': DIRECTION_FORWARD,
        'witness_state': WITNESS_GOALS['and_er'],
    },
    {
        'premise': 'or_il',
        'annotation_text_or_ABSENT': '#backward or_il.',
        'enumerable': True,
        'enumerable_directions': (DIRECTION_BACKWARD,),
        'required_direction': DIRECTION_BACKWARD,
        'witness_state': WITNESS_GOALS['or_il'],
    },
    {
        'premise': 'or_ir',
        'annotation_text_or_ABSENT': '#backward or_ir.',
        'enumerable': True,
        'enumerable_directions': (DIRECTION_BACKWARD,),
        'required_direction': DIRECTION_BACKWARD,
        'witness_state': WITNESS_GOALS['or_ir'],
    },
    {
        'premise': 'or_e',
        'annotation_text_or_ABSENT': (
            '#backward or_e infer infer infer infer subgoal subgoal.'
        ),
        'enumerable': True,
        'enumerable_directions': (DIRECTION_BACKWARD,),
        'required_direction': DIRECTION_BACKWARD,
        'witness_state': WITNESS_GOALS['or_e'],
    },
    {
        'premise': 'not_i',
        'annotation_text_or_ABSENT': '#backward not_i.',
        'enumerable': True,
        'enumerable_directions': (DIRECTION_BACKWARD,),
        'required_direction': DIRECTION_BACKWARD,
        'witness_state': WITNESS_GOALS['not_i'],
    },
    {
        'premise': 'not_e',
        'annotation_text_or_ABSENT': ANNOTATION_ABSENT,
        'enumerable': True,
        'enumerable_directions': (DIRECTION_BACKWARD, DIRECTION_FORWARD),
        'required_direction': DIRECTION_BACKWARD,
        'witness_state': WITNESS_GOALS['not_e'],
    },
    {
        'premise': 'exfalso',
        'annotation_text_or_ABSENT': '#backward exfalso.',
        'enumerable': True,
        'enumerable_directions': (DIRECTION_BACKWARD,),
        'required_direction': DIRECTION_BACKWARD,
        'witness_state': WITNESS_GOALS['exfalso'],
    },
)

AMBIENT_ARROW_CHAINS = (
    "[('a0 : prop) -> ('a1 : prop) -> ('h0 : ['a0 -> 'a1]) -> ('base : 'a0) -> 'a1]",
    "[('a0 : prop) -> ('a1 : prop) -> ('a2 : prop) -> ('h0 : ['a0 -> 'a1]) -> ('h1 : ['a1 -> 'a2]) -> ('base : 'a0) -> 'a2]",
    "[('a0 : prop) -> ('a1 : prop) -> ('a2 : prop) -> ('a3 : prop) -> ('h0 : ['a0 -> 'a1]) -> ('h1 : ['a1 -> 'a2]) -> ('h2 : ['a2 -> 'a3]) -> ('base : 'a0) -> 'a3]",
    "[('a0 : prop) -> ('a1 : prop) -> ('a2 : prop) -> ('a3 : prop) -> ('a4 : prop) -> ('h0 : ['a0 -> 'a1]) -> ('h1 : ['a1 -> 'a2]) -> ('h2 : ['a2 -> 'a3]) -> ('h3 : ['a3 -> 'a4]) -> ('base : 'a0) -> 'a4]",
    "[('a0 : prop) -> ('a1 : prop) -> ('a2 : prop) -> ('a3 : prop) -> ('a4 : prop) -> ('a5 : prop) -> ('h0 : ['a0 -> 'a1]) -> ('h1 : ['a1 -> 'a2]) -> ('h2 : ['a2 -> 'a3]) -> ('h3 : ['a3 -> 'a4]) -> ('h4 : ['a4 -> 'a5]) -> ('base : 'a0) -> 'a5]",
    "[('a0 : prop) -> ('a1 : prop) -> ('a2 : prop) -> ('a3 : prop) -> ('a4 : prop) -> ('a5 : prop) -> ('a6 : prop) -> ('h0 : ['a0 -> 'a1]) -> ('h1 : ['a1 -> 'a2]) -> ('h2 : ['a2 -> 'a3]) -> ('h3 : ['a3 -> 'a4]) -> ('h4 : ['a4 -> 'a5]) -> ('h5 : ['a5 -> 'a6]) -> ('base : 'a0) -> 'a6]",
    "[('a0 : prop) -> ('a1 : prop) -> ('a2 : prop) -> ('a3 : prop) -> ('a4 : prop) -> ('a5 : prop) -> ('a6 : prop) -> ('a7 : prop) -> ('h0 : ['a0 -> 'a1]) -> ('h1 : ['a1 -> 'a2]) -> ('h2 : ['a2 -> 'a3]) -> ('h3 : ['a3 -> 'a4]) -> ('h4 : ['a4 -> 'a5]) -> ('h5 : ['a5 -> 'a6]) -> ('h6 : ['a6 -> 'a7]) -> ('base : 'a0) -> 'a7]",
    "[('a0 : prop) -> ('a1 : prop) -> ('a2 : prop) -> ('a3 : prop) -> ('a4 : prop) -> ('a5 : prop) -> ('a6 : prop) -> ('a7 : prop) -> ('a8 : prop) -> ('h0 : ['a0 -> 'a1]) -> ('h1 : ['a1 -> 'a2]) -> ('h2 : ['a2 -> 'a3]) -> ('h3 : ['a3 -> 'a4]) -> ('h4 : ['a4 -> 'a5]) -> ('h5 : ['a5 -> 'a6]) -> ('h6 : ['a6 -> 'a7]) -> ('h7 : ['a7 -> 'a8]) -> ('base : 'a0) -> 'a8]",
)

APPLY_PREFIX = 'a '
CONSTRUCT_PREFIX = 'c '


def _annotation_text(theory_text: str, premise: str):
    for raw in theory_text.splitlines():
        line = raw.strip()
        if line.startswith('#backward ') or line.startswith('#forward '):
            rest = line.split(' ', 1)[1]
            name = rest.split(' ', 1)[0].rstrip('.')
            if name == premise:
                return line
    return ANNOTATION_ABSENT


def _directions(actions, premise: str):
    found = []
    apply_serial = APPLY_PREFIX + premise
    construct_serial = CONSTRUCT_PREFIX + premise
    serials = [str(action) for action in actions]
    if apply_serial in serials:
        found.append(DIRECTION_BACKWARD)
    if construct_serial in serials:
        found.append(DIRECTION_FORWARD)
    return tuple(found), serials


def _arrow_argument_name(edge_index: int, base_name: str) -> str:
    if edge_index == 0:
        return base_name
    if edge_index == 1:
        return 'p'
    return 'p' + str(edge_index - 2)


class TestStageBTheoryEnumerability(unittest.TestCase):
    def test_theory_bytes_match_pin(self):
        import hashlib
        raw = THEORY_PATH.read_bytes()
        self.assertEqual(hashlib.sha256(raw).hexdigest(), THEORY_SHA256)

    def _execute_unique_intro(self, state, context):
        matches = [action for action in state.actions() if str(action) == 'intro.']
        if len(matches) != 1:
            self.fail(
                'PREMISE_ENUMERABILITY_FAILED: expected exactly one intro. at '
                + context
                + ' found '
                + str(len(matches))
            )
        children = state.execute_action(matches[0])
        self.assertEqual(len(children), 1, context)
        return children[0]

    def _intro_until_stable(self, state, context):
        prefix = 0
        while True:
            serials = [str(action) for action in state.actions()]
            if 'intro.' not in serials:
                return state
            state = self._execute_unique_intro(state, context + ' prefix=' + str(prefix))
            prefix += 1

    def test_nine_premises_annotation_direction_and_witness(self):
        theory_text = THEORY_PATH.read_text(encoding='utf-8')
        table = []
        for premise in THEORY_PREMISES:
            annotation = _annotation_text(theory_text, premise)
            goal = WITNESS_GOALS[premise]
            state = self._intro_until_stable(
                peano.PyProofState(theory_text, list(THEORY_PREMISES), goal),
                premise,
            )
            directions, serials = _directions(state.actions(), premise)
            required = REQUIRED_DIRECTIONS[premise]
            enumerable = required in directions
            if not enumerable:
                self.fail(
                    'PREMISE_ENUMERABILITY_FAILED: '
                    + premise
                    + ' missing '
                    + required
                    + ' in '
                    + repr(serials)
                )
            table.append({
                'premise': premise,
                'annotation_text_or_ABSENT': annotation,
                'enumerable': True,
                'enumerable_directions': directions,
                'required_direction': required,
                'witness_state': goal,
            })
        self.assertEqual(tuple(table), FROZEN_PREMISE_TABLE)
        self.assertEqual(len(table), 9)
        self.assertEqual([row['premise'] for row in table], list(THEORY_PREMISES))

    def test_ambient_arrow_chains_depth_1_to_8(self):
        theory_text = THEORY_PATH.read_text(encoding='utf-8')
        self.assertEqual(len(AMBIENT_ARROW_CHAINS), 8)
        for depth, statement in enumerate(AMBIENT_ARROW_CHAINS, start=1):
            with self.subTest(depth=depth):
                self._check_ambient_arrow_chain(theory_text, depth, statement)

    def _check_ambient_arrow_chain(self, theory_text, depth, statement):
        state = peano.PyProofState(theory_text, list(THEORY_PREMISES), statement)
        intro_steps = 2 * depth + 2
        for step in range(intro_steps):
            context = 'DAG_ENUMERABILITY_FAILED: intro. at depth %s step %s' % (
                depth, step)
            matches = [
                action for action in state.actions() if str(action) == 'intro.'
            ]
            if len(matches) != 1:
                self.fail(context + ' found ' + str(len(matches)))
            children = state.execute_action(matches[0])
            if len(children) != 1:
                self.fail(context + ' children ' + str(len(children)))
            state = children[0]
        remaining_intros = [
            action for action in state.actions() if str(action) == 'intro.'
        ]
        self.assertEqual(remaining_intros, [], 'extra intro. after declarations')
        names = state.names_in_context()[1:]
        edge_names = names[depth + 1:depth + 1 + depth]
        base_name = names[depth + 1 + depth]
        self.assertEqual(len(names), 2 * depth + 2)
        self.assertEqual(len(edge_names), depth)
        self.assertEqual(base_name, names[2 * depth + 1])
        for edge_index, edge_name in enumerate(edge_names):
            construct_serial = CONSTRUCT_PREFIX + edge_name
            constructs = [
                action for action in state.actions()
                if str(action) == construct_serial
            ]
            if len(constructs) != 1:
                self.fail(
                    'DAG_ENUMERABILITY_FAILED: expected exactly one '
                    + construct_serial
                    + ' at depth '
                    + str(depth)
                    + ' edge '
                    + str(edge_index)
                    + ' found '
                    + str(len(constructs))
                )
            children = state.execute_action(constructs[0])
            if len(children) != 1:
                self.fail(
                    'DAG_ENUMERABILITY_FAILED: construct children at depth '
                    + str(depth)
                    + ' edge '
                    + str(edge_index)
                )
            state = children[0]
            argument = _arrow_argument_name(edge_index, base_name)
            selection_serial = '=> (' + edge_name + ' ' + argument + ').'
            selections = [
                action for action in state.actions()
                if str(action) == selection_serial
            ]
            if len(selections) != 1:
                self.fail(
                    'DAG_ENUMERABILITY_FAILED: expected exactly one '
                    + selection_serial
                    + ' at depth '
                    + str(depth)
                    + ' edge '
                    + str(edge_index)
                    + ' found '
                    + str(len(selections))
                    + ' in '
                    + repr([str(action) for action in state.actions()])
                )
            is_final = edge_index == depth - 1
            if is_final:
                continue
            children = state.execute_action(selections[0])
            if len(children) != 1:
                self.fail(
                    'DAG_ENUMERABILITY_FAILED: selection children at depth '
                    + str(depth)
                    + ' edge '
                    + str(edge_index)
                )
            state = children[0]


if __name__ == '__main__':
    unittest.main()
