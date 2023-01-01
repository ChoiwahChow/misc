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

powers = [[]] * 15
powers[10] = { 2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 14, 15, 20, 21, 30 }
powers[11] = { 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 14, 15, 18, 20, 21, 24, 28, 30 }
powers[12] = { 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 14, 15, 18, 20, 21, 24, 28, 30, 35, 42, 60 }

def gen_cmd(k, n, pos, grp, bin_dir, in_dir, grp_dir):
    """ generate command line for executing mace4
    """
    mace_exe = os.path.join(bin_dir, 'mace4')
    monoid_in = os.path.join(in_dir, f'monoids_{n}.in')
    grp_in = os.path.join(grp_dir, f'groups_{n}_{pos}.in')

    cmd = ''
    if len(grp) <= k:
        cmd = f'{mace_exe} -n{k} -N{k} -m-1 -O3 -A1 -f {monoid_in} {grp_in}'
    return cmd


if __name__ == "__main__":
    k = 10
    bin_dir = os.path.join("..", "..", "bin")
    in_dir = 'inputs'
    groups_dir = os.path.join(in_dir, "groups")

    cmds = []
    for n in powers[k]:
        grps = groups.groups[n]
        for pos, grp in enumerate(grps):
            cmd = gen_cmd(k, n, pos, grp, bin_dir, in_dir, groups_dir)
            if cmd:
                cmds.append(cmd)

    fn = os.path.join("data", f"mace4_cmd_{k}.bat")
    with open(fn, "w") as fp:
        for cmd in cmds:
            fp.write(cmd + os.linesep)

    print(len(cmds))

