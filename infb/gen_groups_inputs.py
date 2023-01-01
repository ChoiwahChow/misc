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
import groups

powers10 = { 2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 14, 15, 20, 21, 30 }
powers11 = { 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 14, 15, 18, 20, 21, 24, 28, 30 }
powers12 = { 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 14, 15, 18, 20, 21, 24, 28, 30, 35, 42, 60 }

def gen_inputs(grp_dir, n, pos, grp):
    fn = os.path.join(grp_dir, f"groups_{n}_{pos}.in")
    order = len(grp)
    with open(fn, "w") as fp:
        fp.write(f"formulas(group{n})." + os.linesep)
        for r, row in enumerate(grp):
            for c, cell in enumerate(row):
                fp.write(f'{r} * {c} = {cell}. ')
            fp.write(os.linesep)
        fp.write('end_of_list.' + os.linesep)



if __name__ == "__main__":
    in_dir = 'inputs'

    # iterate over each order k
    for k, kgrps in groups.groups.items():
        groups_dir = os.path.join(in_dir, f"groups_{k}")
        os.makedirs(groups_dir, exist_ok=True)
        # for each k, iterate over all n
        for n, groups in kgrps.items():
            for pos, grp in enumerate(groups): 
                gen_inputs(groups_dir, n, pos, grp)

