#!/usr/bin/python3

import os
import sys
import re
import zlib
import argparse
import pickle
from pathlib import Path


def model_key(fp, delim):
    line = fp.readline()
    arr = list()
    while line:
        arr.append(line)
        if delim in line:
            break 
        line = fp.readline()
    k = "".join(arr)
    k = k.replace("10", "a").replace("11", "b").replace(" ", "").replace(",", "").replace("])", "").replace(".", "").replace("\n", "")
    # print(f"debug k: {k}")
    return arr, zlib.compress(k.encode())


def print_models(k, fn, models_to_write):
    with open(fn, "a") as ofp:
        ofp.write(f"models{k} := ["+os.linesep)
        for model in models_to_write:
            m = [ f'[ {", ".join([str(x) for x in row])} ]' for row in model ]
            m = ", ".join(m)
            ofp.write("[ ")
            ofp.write(m)
            ofp.write(" ]," + os.linesep)
        ofp.write("];")


def filter_a_file(fp, all_keys, k, out_file_0, max_hash_models, add_to_hash=True, max_models_per_file = 10000000000, function = "function(*", delim = "])"):
    """ unique models are appended to the out_file_0 files
    fp: input file pointer, could be sys.stdin
    k:  order of algebra
    out_file_0: out file path
    max_models_per_file:  if number of output models > max_models_per_file, then a new file out_file_0.<file count> will be used
    """
    count = 0
    out_file = out_file_0
    f_count = 0

    model_count = 0
    ofp = open(out_file, "a")
    #with open(fn) as fp:
    line = fp.readline()
    while line:
        if line.startswith("interp"):
            model = list()
            model.append(line)
        elif function in line:
            model.append(line)
            arr, key = model_key(fp, delim)
            # print(f"debug key: {len(key)} {key}")
            model.extend(arr)
            if not all_keys.get(key, None):
                if add_to_hash and (max_hash_models < 0 or len(all_keys) < max_hash_models):
                    all_keys[key] = 1
                ofp.writelines(model)
                model_count += 1
                if max_models_per_file > -1 and model_count >= max_models_per_file:
                    model_count = 0
                    f_count += 1
                    out_file = f'{out_file_0}.{f_count}'
                    ofp.close()
                    ofp = open(out_file, "a")
                count += 1
                # if count % 1000000 == 0:
                #   print(f"Done {count} models")
        line = fp.readline()
    ofp.close()
    return model_count


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("-k", "--order", type=int, default=12)
    parser.add_argument("-c", "--chunk_size", type=int, default=-1)
    parser.add_argument("-i", "--in_file", default="")
    parser.add_argument("-o", "--out_file", default="non_iso_models.out")
    parser.add_argument("-p", "--output_hash", action='store_true')
    parser.add_argument("-s", "--skip_hash", action='store_true')
    parser.add_argument("-t", "--hash_file", default="")
    parser.add_argument("-m", "--max_hash_size", type=int, default=-1)
    parser.add_argument("-v", "--verbose", action='store_true')

    return parser.parse_args()


if __name__ == "__main__":
    args = parse_args()
    delim = "])"
    k = args.order
    ck = args.chunk_size
    out_file = args.out_file
    hash_file = args.hash_file
    output_hash = args.output_hash
    add_to_hash = not args.skip_hash
    max_hash_size = args.max_hash_size

    if args.verbose:
        print(f"order: {k}")
        print(f"max #models per file: {ck}")
        print(f"input file name: {args.in_file}")
        print(f"output file name: {out_file}")
        print(f"hash pickle file name: {hash_file}")
        print(f"output hash table flag: {output_hash}")
        print(f"output hash table #model limit: {max_hash_size}")
        print(f"skip add to hash flag: {not add_to_hash}")

    function = "function(*"
    all_keys = dict()
    if hash_file and Path(hash_file).is_file():
        all_keys = pickle.load(open(hash_file, "rb"))
    if args.in_file:
        fp = open(args.in_file)
    else:
        fp = sys.stdin
    model_count = filter_a_file(fp, all_keys, k, out_file, max_hash_size, add_to_hash, ck, function, delim)
    if args.in_file:
        fp.close()

    if output_hash:
        pickle.dump(all_keys, open(hash_file, "wb"))

    if args.verbose:
        print(f"Debut: Found {model_count} non-iso models.")
