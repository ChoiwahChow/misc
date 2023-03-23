#! /usr/bin/python3
"""
For order 12: only the following n's are needed
[ 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 14, 15, 18, 20, 21, 24, 28, 30, 35, 42, 60 ]
"""

import os


primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59]

def power_n(base, n):
    product = base
    for x in range(1, n):
        product = f"({product} * {base})"
    return product


def gen_sapir(n):
    #p01 = power_n("(0*1)", n)
    #p10 = power_n("(1*0)", n)
    p01 = "(0*1)"
    p10 = "(1*0)"

    left_base = f"(({p01}*{p10})*{p01})"
    left = power_n(left_base, n)
    return f"% Sapir identity\n{left} = {p01}."

def gen_non_sapir(n):
    p01 = "(0*1)"
    p10 = "(1*0)"

    left_base = f"(({p01}*{p10})*{p01})"
    left = power_n(left_base, n)
    return f"{left} != {p01}"

def gen_input(n):
    clause2 = "1 * 1 != 1.                                % idempotency "
    clause3 = "(x * y) * z = x * (y * z)."
    clause4 = "0 = 0 * (1 * 0).                           % mutual inverse1 "
    clause5 = "1 = 1 * (0 * 1).                           % mutual inverse2 "
    exist1 = "all x exists u (x = 0 * u | x = 1 * u).     % clause a "
    # exist2 = "all x exists u (x = u * 0 | x = u * 1).     % clause b "
    # exist3 = "all u exists x (u * x != x).                % anti-monoid  "
    non_sapirs = [gen_non_sapir(x) for x in primes if x <= n]
    non_sapir_clause = "\n | ".join(non_sapirs) 
    
    main_clauses = f"formulas(assumptions).\n{clause2}\n{clause3}\n{clause4}\n{clause5}\n\n{exist1}\n" 

    inputs = f"{main_clauses}\n\n{non_sapir_clause}.\n\n\nend_of_list.\n"

    return inputs


if __name__ == "__main__":
    os.makedirs("inputs", exist_ok=True)
    for n in range(30, 31):
        inputs = gen_input(n)
        with (open(f"inputs/sapir_{n}.in", "w")) as fp:
            fp.write(inputs)

    #print(gen_exists(10))
    #print(gen_main_n(4))
    #print(gen_goal(2))
    #print(gen_input(3))
