#!/usr/bin/python3

import os
import sys
import re


def conv_a_row(line):
    m = re.search(r"\d", line)
    m2 = re.match('.+([0-9])[^0-9]*$', line)
    a = line[m.start(): m2.start(1)+1]
    b = a.split(',')

    return [int(x) for x in b]


def conv_a_model(fp, delim):
    line = fp.readline()
    model = list()
    row_num = 0
    while line:
        if delim in line:
            t = line.rstrip().replace(delim, "").rstrip(" ")
            model.append(f"{t},{str(row_num)},\n")
            row_num += 1
            model.append(f'    {",".join([str(x) for x in range(0,row_num+1)])} {delim}\n')
            return model
        else:
            line = f"{line.rstrip()}{str(row_num)},\n"
            model.append(line)
        
        line = fp.readline()
        row_num += 1
    return model


def gen_all_sapir_monoids(fn, function = "function(*", delim = "])])."):
    with open(fn) as fp:
        line = fp.readline()
        inter = ""
        while line:
            if line.startswith("interp"):
                interp = line
                order = interp.split(",")[0].split(" ")[1]   # e.g. interpretation( 10, ....
                new_order = str(int(order)+1)
                interp = interp.replace(order, new_order, 1)
            elif function in line:
                model = conv_a_model(fp, delim)
                print(interp, end="")
                print(line, end="")
                for x in model:
                    print(x, end="")
            line = fp.readline()


if __name__ == "__main__":

  mt = [
    [0,0,2,2,4,4,6,6],
    [1,1,3,3,5,5,7,7],
    [0,4,2,6,4,0,6,2],
    [1,5,3,7,5,1,7,3],
    [4,4,6,6,0,0,2,2],
    [5,5,7,7,1,1,3,3],
    [4,0,6,2,0,4,2,6],
    [5,1,7,3,1,5,3,7]
  ]

  mt2 = [
    [0,0,0,0,4,4,4,4],
    [0,0,0,1,4,4,4,5],
    [2,2,2,2,6,6,6,6],
    [2,2,2,3,6,6,6,7],
    [0,0,0,0,4,4,4,4],
    [0,1,0,1,4,5,4,5],
    [2,2,2,2,6,6,6,6],
    [2,3,2,3,6,7,6,7]
  ]

  #res = witness_violate_sapir(mt)
  #print(res)
  #res = find_identity_element(mt)
  #print(res)

  fn = sys.argv[1]
  gen_all_sapir_monoids(fn)


