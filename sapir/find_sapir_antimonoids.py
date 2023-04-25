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
    arr = list()
    model = list()
    while line:
        row = conv_a_row(line)
        arr.append(row)
        model.append(line)
        if delim in line:
            return model, arr
        line = fp.readline()
    return model, arr


def find_ips(mt):
    """  Returns the smallest n such that s^n is an idempotent for all s in mt.
    """
    pow = {x: x for x in range(0, len(mt))}
    done = False
    n = 1
    while not done:
        idem_count = 0
        for x in range(0, len(mt)):
            oldpow = pow[x]
            pow[x] = mt[x][oldpow]
            if mt[oldpow][oldpow] == oldpow:
                idem_count += 1
        if idem_count == len(mt):
            return n 
        n += 1

def pow_n(mt, n, a):
    b = a
    for x in range(1, n):
        b = mt[a][b]
    return b


def find_identity_element(mt):
    id = [x for x in range(0, len(mt))]
    for x in range(0, len(mt)):
        if mt[x] == id:
           return x
    return None
        

def violate_sapir(mt, n, a, b):
    ab = mt[a][b]
    ba = mt[b][a]
    ab_n = pow_n(mt, n, ab)
    ba_n = pow_n(mt, n, ba)
    left = mt[mt[ab_n][ba_n]][ab_n]
    return pow_n(mt, n, left) != ab_n

    
def witness_violate_sapir(mt):
    n = find_ips(mt)
    for a in range(0, len(mt)-1):
        for b in range(a+1, len(mt)):
            if violate_sapir(mt, n, a, b):
                return n, (a, b)

    return n, ()


def find_all_sapir_anti_monoids(fn, function = "function(*", delim = "])"):
    with open(fn) as fp:
        line = fp.readline()
        inter = ""
        while line:
            if line.startswith("interp"):
                interp = line
            elif function in line:
                (model, mt) = conv_a_model(fp, delim)
                if not find_identity_element(mt):
                    (ipS, witnesses) = witness_violate_sapir(mt)
                    if witnesses:
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
  find_all_sapir_anti_monoids(fn)


