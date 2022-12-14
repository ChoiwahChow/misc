#! /usr/bin/python3

import os

def power_n(base, n):
    product = base
    for x in range(1, n):
        product = f"({product} * {base})"
    return product


def gen_main_n(n):
    left = power_n('x', n)
    right = f"{left} * {left}"
    return f"{left} = {right}"
    

def gen_exists(n):
    base = f"a{n}"
    left = power_n(base, n)
    right = f"{left} * {left}"

    return f"{left} != {right}"


def gen_goals(n):
    p1 = power_n("(x*y)", n)
    p2 = power_n("(y*x)", n)

    left_base = f"(({p1} * {p2}) * {p1})"
    left = power_n(left_base, n)
    return f"{left} = {p1}"


def gen_input(n, min_ineq, max_ineq):
    goals = gen_goals(n)
    monoid_section = "formulas(assumptions).\n(x * y) * z = x * (y * z).\nx * 0 = x.\n0 * x = x.\nend_of_list.\n" 

    main_clause = gen_main_n(n) + "."
    negate = list()
    max_exist = min(n, max_ineq+1)
    for x in range(min_ineq, max_exist):
        negate.append(gen_exists(x) + ".")
    exists_clause = "\n".join(negate)

    add_section = f"formulas(sos).\n{main_clause}\n\n{exists_clause}\nend_of_list.\n"

    goal_section = f"formulas(goals).\n{goals}.\nend_of_list.\n"

    inputs = f"{monoid_section}\n{add_section}\n{goal_section}\n"

    return inputs


if __name__ == "__main__":
    max_ineq = 2
    os.makedirs("inputs", exist_ok=True)
    for n in range(1, 31):
        inputs = gen_input(n, 2, max_ineq)
        with (open(f"inputs/monoid_{n}.in", "w")) as fp:
            fp.write(inputs)

    #print(gen_exists(10))
    #print(gen_main_n(4))
    #print(gen_goal(2))
    #print(gen_input(3))
