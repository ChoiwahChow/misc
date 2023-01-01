#! /usr/bin/python3
"""
For order 12: only the following n's are needed
[ 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 14, 15, 18, 20, 21, 24, 28, 30, 35, 42, 60 ]



If k=6, then there are semigroups satisfying x^n = x^2n only when n in [ 1, 2, 3, 4, 5, 6 ].

If k=7, then there are semigroups satisfying x^n = x^2n only when n in [ 1, 2, 3, 4, 5, 6, 7, 10, 12 ].

If k=8, then there are semigroups satisfying x^n=x^2n only when n in [ 1, 2, 3, 4, 5, 6, 7, 8, 10, 12, 15 ].

The possible values for n=10 are:
[ 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 14, 15, 20, 21, 30 ]


The possible values for n=11 are:
[ 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 14, 15, 18, 20, 21, 24, 28, 30 ]
"""

import os
import subprocess

k = 10
powers10 = { 2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 14, 15, 20, 21, 30 }
powers11 = { 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 14, 15, 18, 20, 21, 24, 28, 30 }
powers12 = { 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 14, 15, 18, 20, 21, 24, 28, 30, 35, 42, 60 }


def gen_gap(power):
    gap_code = f'all:=AllSmallGroups([1..12]);; fil:= Filtered(all,G->ForAll(G,g->g^{power*2}=g^{power}));; for G in fil do Print(MultiplicationTable(G),"\n"); od;'
    command = f"gap -c 'n:={power};;' < infb.g"
    print(command)
    subprocess.call(command, shell=True)


    return []



if __name__ == "__main__":
    all_powers = powers10.union(powers11.union(powers12))
    in_dir = 'inputs'
    data_dir = "data"

    os.makedirs(in_dir, exist_ok=True)
    os.makedirs(data_dir, exist_ok=True)

    with open('groups.py', 'w') as fp:
        fp.write(f'groups = [[]] * {max(all_powers)+1}\n\n')
    for n in all_powers:
        gen_gap(n)
