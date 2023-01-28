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


def print_models(k, fn, models_to_write):
    with open(fn, "w") as ofp:
        ofp.write(f"models{k} := ["+os.linesep)
        for model in models_to_write:
            m = [ f'[ {", ".join([str(x) for x in row])} ]' for row in model ]
            m = ", ".join(m)
            ofp.write("[ ")
            ofp.write(m)
            ofp.write(" ]," + os.linesep)
        ofp.write("];")


def conv_a_file(fn, k, out_file_0, max_models, function = "function(*", delim = "])"):
    all_models = list()
    count = 0
    f_count = 0
    out_file = f'{out_file_0}.{f_count}'
    with open(fn) as fp:
        line = fp.readline()
        while line:
            if function in line:
                model = conv_a_model(fp, delim)
                all_models.append(model)
                if len(all_models) >= max_models:
                    print_models(k, out_file, all_models)
                    all_models = []
                    f_count += 1
                    out_file = f'{out_file_0}.{f_count}'
                count += 1
                if count % 1000000 == 0:
                    print(f"Done {count} models")
            line = fp.readline()
    if all_models:
        print_models(k, out_file, all_models)


if __name__ == "__main__":
    #delim = "])])."
    delim = "])"
    k = 12
    ck = 1032000   # 1 million
    in_file = f"../master_non_iso/models_done/models_c.out"
    out_file = f"non_iso/monoids_{k}.g"
    if len(sys.argv) > 4:
        k = int(sys.argv[1])
        ck = int(sys.argv[2])
        in_file = sys.argv[3]
        out_file = sys.argv[4]

    function = "function(*"
    # print(conv_a_row("    [[1,2,3,4,5,6],"))
    conv_a_file(in_file, k, out_file, ck, function, delim)

