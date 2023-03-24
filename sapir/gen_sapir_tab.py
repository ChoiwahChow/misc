#!/usr/bin/python3

import os
import sys
import re


def conv_a_row(line):
    m = re.search(r"\d", line)
    m2 = re.match('.+([0-9])[^0-9]*$', line)
    a = line[m.start(): m2.start(1)+1]
    b = a.split(',')
    
    return [int(x)+1 for x in b]


def conv_a_model(fp, delim):
    line = fp.readline()
    arr = list()
    while line:
        row = conv_a_row(line)
        arr.append(row)
        if delim in line:
            return arr
        line = fp.readline()
    return arr


def print_models(fn, models_to_write):
    with open(fn, "w") as ofp:
        for model in models_to_write:
            ord = len(model)
            header_format = "c" * (ord)
            # ofp.write(f"\begin{table}[ht]\n")
            ofp.write("\\begin{tabular}[t]{c|")
            ofp.write(header_format)
            ofp.write("}\n")
            ofp.write(f"*&{'&'.join([str(x) for x in range(1, ord+1)])} \\\\ \\hline\n")
            for pos, row in enumerate(model):
                ofp.write(f'    {str(pos+1)}&{"&".join([str(x) for x in row])} ')
                if pos < ord-1:
                    ofp.write("\\\\")
                ofp.write("\n")
            ofp.write("\\end{tabular}\n\n\n")


def conv_a_file(fn, out_file, function = "function(*", delim = "])"):
    all_models = list()
    with open(fn) as fp:
        line = fp.readline()
        while line:
            if function in line:
                model = conv_a_model(fp, delim)
                all_models.append(model)
            line = fp.readline()
    if all_models:
        print_models(out_file, all_models)


if __name__ == "__main__":
    #delim = "])])."
    delim = "])"
    k = 6
    if len(sys.argv) > 1:
        k = int(sys.argv[1])
    in_file = f"sapir_monoids/monoids_{k}.out"
    out_file = f"sapir_monoids/latex/monoids_{k}.tex"

    function = "function(*"
    # print(conv_a_row("    [[1,2,3,4,5,6],"))
    conv_a_file(in_file, out_file, function, delim)

