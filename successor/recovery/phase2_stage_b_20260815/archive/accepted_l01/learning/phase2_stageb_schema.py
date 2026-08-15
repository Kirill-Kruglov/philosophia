#!/usr/bin/env python3
"""L0 Stage-B schema constants. No generator, identity or checker logic."""

from __future__ import annotations

import re


MAX_FORMULA_NODES = 24
DEV_QUERY_MEASUREMENT_N_POSITIONS = 4096

PLAN_SCHEMA_NAME = 'philosophia.stageb.nd-plan.v1'
EXPECTATION_SCHEMA_NAME = 'philosophia.stageb.plan-expectation.v1'

FORMULA_KINDS = ('ATOM', 'FALSE', 'NOT', 'AND', 'OR')
RULE_KINDS = (
    'ASSUME',
    'AND_INTRO',
    'AND_ELIM_LEFT',
    'AND_ELIM_RIGHT',
    'OR_INTRO_LEFT',
    'OR_INTRO_RIGHT',
    'OR_ELIM',
    'NOT_INTRO',
    'NOT_ELIM',
    'EXFALSO',
)
FAMILY_ORDER = (
    'AND_INTRO',
    'AND_ELIM',
    'OR_INTRO',
    'OR_ELIM',
    'NOT_INTRO',
    'NOT_ELIM',
    'EXFALSO',
)
KIND_TO_FAMILY = {
    'AND_INTRO': 'AND_INTRO',
    'AND_ELIM_LEFT': 'AND_ELIM',
    'AND_ELIM_RIGHT': 'AND_ELIM',
    'OR_INTRO_LEFT': 'OR_INTRO',
    'OR_INTRO_RIGHT': 'OR_INTRO',
    'OR_ELIM': 'OR_ELIM',
    'NOT_INTRO': 'NOT_INTRO',
    'NOT_ELIM': 'NOT_ELIM',
    'EXFALSO': 'EXFALSO',
}
BAND_EDGES = (
    ('S1', 8, 11),
    ('S2', 12, 17),
    ('S3', 18, 25),
    ('S4', 26, 37),
)
BAND_NAMES = ('S1', 'S2', 'S3', 'S4')

PLAN_KEYS = ('schema', 'atoms', 'hypotheses', 'goal', 'proof')
EXPECTATION_KEYS = (
    'schema', 'node_count', 'band', 'families', 'max_dependency_depth',
)
HYPOTHESIS_KEYS = ('id', 'formula')
FORMULA_KEYS = {
    'ATOM': ('kind', 'name'),
    'FALSE': ('kind',),
    'NOT': ('kind', 'arg'),
    'AND': ('kind', 'left', 'right'),
    'OR': ('kind', 'left', 'right'),
}
PROOF_NODE_KEYS = {
    'ASSUME': ('kind', 'conclusion', 'hypothesis_id'),
    'AND_INTRO': ('kind', 'conclusion', 'left', 'right'),
    'AND_ELIM_LEFT': ('kind', 'conclusion', 'source'),
    'AND_ELIM_RIGHT': ('kind', 'conclusion', 'source'),
    'OR_INTRO_LEFT': ('kind', 'conclusion', 'source'),
    'OR_INTRO_RIGHT': ('kind', 'conclusion', 'source'),
    'OR_ELIM': (
        'kind', 'conclusion', 'major', 'left_assumption', 'left_branch',
        'right_assumption', 'right_branch',
    ),
    'NOT_INTRO': ('kind', 'conclusion', 'assumption', 'body'),
    'NOT_ELIM': ('kind', 'conclusion', 'negative', 'positive'),
    'EXFALSO': ('kind', 'conclusion', 'source'),
}
PROOF_CHILD_FIELDS = {
    'ASSUME': (),
    'AND_INTRO': ('left', 'right'),
    'AND_ELIM_LEFT': ('source',),
    'AND_ELIM_RIGHT': ('source',),
    'OR_INTRO_LEFT': ('source',),
    'OR_INTRO_RIGHT': ('source',),
    'OR_ELIM': ('major', 'left_branch', 'right_branch'),
    'NOT_INTRO': ('body',),
    'NOT_ELIM': ('negative', 'positive'),
    'EXFALSO': ('source',),
}

ATOM_NAME_RE = re.compile(r'^a(0|[1-9][0-9]*)$')
GLOBAL_ID_RE = re.compile(r'^h(0|[1-9][0-9]*)$')
LOCAL_ID_RE = re.compile(r'^l(0|[1-9][0-9]*)$')

MIN_DECLARED_ATOMS = 3
MAX_DECLARED_ATOMS = 6
MIN_DEPENDENCY_DEPTH = 2
MIN_FAMILY_COUNT = 3
BRANCHING_FAMILIES = ('AND_INTRO', 'OR_ELIM')

THEORY_FILENAME = 'propositional-logic-intuitionistic-fragment.p'
THEORY_SHA256 = (
    '2056deaf9c12a81dcb047e60154e8a473ffe235b5e48bb9433eb1d9f70afb507'
)
THEORY_PREMISES = (
    'and_i', 'and_el', 'and_er', 'or_il', 'or_ir', 'or_e',
    'not_i', 'not_e', 'exfalso',
)
DIRECTION_BACKWARD = 'BACKWARD_ON_GOAL'
DIRECTION_FORWARD = 'FORWARD_FROM_HYPOTHESIS'
REQUIRED_DIRECTIONS = {
    'and_i': DIRECTION_BACKWARD,
    'and_el': DIRECTION_FORWARD,
    'and_er': DIRECTION_FORWARD,
    'or_il': DIRECTION_BACKWARD,
    'or_ir': DIRECTION_BACKWARD,
    'or_e': DIRECTION_BACKWARD,
    'not_i': DIRECTION_BACKWARD,
    'not_e': DIRECTION_BACKWARD,
    'exfalso': DIRECTION_BACKWARD,
}


def is_printable_ascii(value: object) -> bool:
    if type(value) is not str or value == '':
        return False
    return all(0x20 <= ord(ch) <= 0x7e for ch in value)


def is_exact_int(value: object) -> bool:
    return type(value) is int


def is_atom_name(value: object) -> bool:
    return type(value) is str and ATOM_NAME_RE.fullmatch(value) is not None


def is_global_id(value: object) -> bool:
    return type(value) is str and GLOBAL_ID_RE.fullmatch(value) is not None


def is_local_id(value: object) -> bool:
    return type(value) is str and LOCAL_ID_RE.fullmatch(value) is not None


def band_of_node_count(node_count: int):
    for name, lo, hi in BAND_EDGES:
        if lo <= node_count <= hi:
            return name
    return None


def family_of_kind(kind: str):
    return KIND_TO_FAMILY.get(kind)
