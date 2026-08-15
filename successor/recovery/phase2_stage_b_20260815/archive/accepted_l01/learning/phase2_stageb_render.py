#!/usr/bin/env python3
"""Pure Peano-surface renderer. No cardinality or canonicalization validation."""

from __future__ import annotations

from typing import Mapping, Sequence


def render_formula(formula: Mapping) -> str:
    kind = formula['kind']
    if kind == 'ATOM':
        return "'" + formula['name']
    if kind == 'FALSE':
        return 'false'
    if kind == 'NOT':
        return '(not ' + render_formula(formula['arg']) + ')'
    if kind == 'AND':
        return (
            '(and '
            + render_formula(formula['left'])
            + ' '
            + render_formula(formula['right'])
            + ')'
        )
    if kind == 'OR':
        return (
            '(or '
            + render_formula(formula['left'])
            + ' '
            + render_formula(formula['right'])
            + ')'
        )
    raise ValueError('unrenderable formula kind')


def render_declaration(atom_name: str) -> str:
    return "('" + atom_name + ' : prop)'


def render_sequent(
        atoms: Sequence[str],
        hypotheses: Sequence[Mapping],
        goal: Mapping,
) -> str:
    parts = [render_declaration(name) for name in atoms]
    parts.extend(render_formula(formula) for formula in hypotheses)
    parts.append(render_formula(goal))
    return '[' + ' -> '.join(parts) + ']'
