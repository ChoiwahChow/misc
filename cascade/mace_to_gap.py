#!/usr/bin/python3

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


def conv_a_file(fn, function, delim):
    all_models = list()
    with (open(fn)) as fp:
        line = fp.readline()
        while line:
            if function in line:
                model = conv_a_model(fp, delim)
                all_models.append(model)
            line = fp.readline()
    return all_models


if __name__ == "__main__":
    #delim = "])])."
    delim = "])"
    function = "function(*"
    k = 6
    # print(conv_a_row("    [[1,2,3,4,5,6],"))
    all_models = conv_a_file("models_200.out", function, delim)
    print(f"models{k} := [")
    for m in all_models:
        print(m, end="")
        print(",")
    print("];")

    # print(all_models)
