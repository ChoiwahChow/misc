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

import groups

powers = [None] * 15
powers[10] = { 2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 14, 15, 20, 21, 30 }
powers[11] = { 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 14, 15, 18, 20, 21, 24, 28, 30 }
powers[12] = { 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 14, 15, 18, 20, 21, 24, 28, 30, 35, 42, 60 }




if __name__ == "__main__":
    k = 10
    total = 0
    for n in powers[k]:
        for grp in groups.groups[n]:
            if len(grp) <= k:
                total += 1
                print(f'n = {n},  group order:  {len(grp)}')
    print(f"\n\nTotal runs: {total}\n\n")
