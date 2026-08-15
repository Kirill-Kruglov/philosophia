prop : type.

false : prop.

not : [prop -> prop].
and : [prop -> prop -> prop].
or : [prop -> prop -> prop].

#backward and_i.
and_i : [('P : prop) -> ('Q : prop) -> 'P -> 'Q -> (and 'P 'Q)].

#forward and_el ('_ : (and 'P 'Q)).
and_el : [('P : prop) -> ('Q : prop) -> (and 'P 'Q) -> 'P].

#forward and_er ('_ : (and 'P 'Q)).
and_er : [('P : prop) -> ('Q : prop) -> (and 'P 'Q) -> 'Q].

#backward or_il.
or_il : [('P : prop) -> ('Q : prop) -> 'P -> (or 'P 'Q)].

#backward or_ir.
or_ir : [('P : prop) -> ('Q : prop) -> 'Q -> (or 'P 'Q)].

#backward or_e infer infer infer infer subgoal subgoal.
or_e : [('P : prop) -> ('Q : prop) -> ('R : prop) ->
        (or 'P 'Q) -> ['P -> 'R] -> ['Q -> 'R] -> 'R].

#backward not_i.
not_i : [('P : prop) -> ['P -> false] -> (not 'P)].

not_e : [('P : prop) -> (not 'P) -> 'P -> false].

#backward exfalso.
exfalso : [false -> ('P : prop) -> 'P].
