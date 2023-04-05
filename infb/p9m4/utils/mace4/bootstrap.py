#!/usr/bin/python3

"""
This is the entry point for running with parallel cubes and isomorphic cube removal

Complete cube-and-conquer with bootstrapping

Iterative:
1. lengthen cubes by parallel Mace4
2. remove isomorphic cubes
3. repeat until the desired length of cubes is reached

Then
4. run the cubes


Mace4 options:
-O3   strictly follows the cube ordering
-A1   print the models in the format expected by isofilter


grep "Exiting with " semi_working_[0-9]/mace.log | grep model | utils/mace4/counter.py

"""


import os
import sys
import shutil
from datetime import datetime
import time
import subprocess
import threading
import ast
from itertools import permutations
import random

import extend_cubes
import multi_cube_analyzer as analyzer
import run_cubes

top_data_dir = "utils/mace4/working"


request_work_file = "request_work.txt"
work_file = "release_work.out"
print_models = "A3"  # P0 - don't output models, A1 - output models, P1 print models


def get_data_dir(algebra, order):
    return f"{top_data_dir}/{algebra}{order}"


def get_working_dir(algebra, order, cube_length):
    """ compose working dir
    """
    return f"{algebra}_working_{order}_{cube_length}"
    

def collect_cubes(algebra, cube_dir, cube_length, data_dir, num_threads):
    """ collect the cubes generated, and remove isomorphic cubes
    """
    # get rid of leading "cube "
    cmd = f"cat {cube_dir}_*/{cube_length}.out | grep '^cube' | sort --parallel={num_threads} -u | sed 's/[^ ]* //' > {data_dir}/cubes{cube_length}.out"
    subprocess.run(cmd, capture_output=False, text=True, check=False, shell=True)
    cube_file = f"{data_dir}/cubes{cube_length}.out"
    out_cube_file = f"{data_dir}/cubes_{order}_{cube_length}.out"
    
    t1 = time.time()
    analyzer.gen_sequence_multi(order, cube_length, 0, [2], [False], [], 1000000000000,
                          "utils/mace4/iso_cubes_multi.py", cube_file, out_cube_file, max_threads=num_threads)
    analyze_time = time.time() - t1
    return analyze_time
    

def gen_all_cubes(algebra, order, power, target_cube_length, threshold, mace4_exe, cubes_options, num_threads):
    """
    Args:
        algebra (str): name of the algebra
        order (int): order of the algebra
        power (int)  n
        target_cube_length (int): target cube length
        threshold (int):  use invariant when the number of models is at least this manany
        mace4_exe (str): path name of the mace4 executable
        cubes_options (int): bit vector lsb 1 - work stealing, 2 - cube has num cells filled at beginning
        num_threads (int): max number of threads to use
    """
    data_dir = get_data_dir(algebra, order)
    os.makedirs(data_dir, exist_ok=True)

    seq = [target_cube_length]
    input_file = f"../inputs/sapir_{power}.in"
    propagated_models_count = 0
    working_dir_prefix = get_working_dir(algebra, order, 2)    

    extend_cubes.extend_cubes(input_file, order, 2, None, print_models, mace4_exe,
                                  working_dir_prefix, num_threads, cubes_options, request_work_file, work_file)
    collect_cubes(algebra, working_dir_prefix, 2, data_dir, num_threads)        

    cube_1_file = f"{top_data_dir}/{algebra}{order}/cubes_{order}_2.out"
    working_dir_prefix = get_working_dir(algebra, order, target_cube_length)    
    extend_cubes.extend_cubes(input_file, order, target_cube_length, cube_1_file, print_models, mace4_exe,
                                  working_dir_prefix, num_threads, cubes_options, request_work_file, work_file)
        
    cmd = f'grep "Exiting with " {working_dir_prefix}_*/{target_cube_length}.out | grep model | utils/mace4/counter.py'
    # print(f'^^^^^^^^^^^^^^^^^^^^^^{cmd}^^^^^^^^^^^^^^^^^^^^^')
    sp = subprocess.run(cmd, capture_output=True, text=True, check=False, shell=True)
    propagated_models_count += int(sp.stdout)
        
    analyze_time = collect_cubes(algebra, working_dir_prefix, target_cube_length, data_dir, num_threads)        
    print(f"{algebra}, {order}, cube length={target_cube_length}, threshold={threshold}, analyze time {analyze_time}, #propagated models {propagated_models_count}", flush=True)
    return propagated_models_count
    
    
def run_all_cubes(algebra, order, power, target_cube_length, mace4_exe, mlex_exe, cubes_options, num_threads, batch_size=1000000000):
    # print(f'{datetime.now().strftime("%d/%m/%Y %H:%M:%S")}, run all cubes...', flush=True)
    input_file = f"../inputs/sapir_{power}.in"
    master_cube_file = f"{top_data_dir}/{algebra}{order}/cubes_{order}_{target_cube_length}.out"
    cube_file = f"{top_data_dir}/{algebra}{order}/cubes_{order}_{target_cube_length}_batch.out"
    with open(master_cube_file) as fp:
        all_cubes = fp.readlines()

    while len(all_cubes) > 0 :
        with open(cube_file, "w") as ofp:
            ofp.writelines(all_cubes[0:batch_size])
        all_cubes = all_cubes[batch_size:]
        working_dir_prefix = get_working_dir(algebra, order, target_cube_length)
        run_cubes.run_mace(mace4_exe, input_file, order, cube_file, print_models, cubes_options, working_dir_prefix, num_threads)
    
    
def collect_stat(algebra, order, target_cube_length, cube_options, threshold, models_count, gen_cube_time, runtime):
    data_dir = get_data_dir(algebra, order)
    out_cube_file = f"{data_dir}/cubes_{order}_{target_cube_length}.out"
    count = len(open(out_cube_file).readlines( ))
    print(f'"{algebra}", order={order}, invariant threshold={threshold}, options={cube_options}, cubes count={count}, {gen_cube_time}, #model={models_count}, model gen time={runtime}\n',
          flush=True)


__all__ = ["run_all_cubes", "gen_all_cubes", "collect_stat"]

if __name__ == "__main__":
    mlex_exe = "../../bin/mlex"
    mace4_exe = "../../bin/mace4"
    cubes_options = 1      # bit-0  set to 1 if use work-stealing
    threshold = 1000       # invariants will be used if number of cubes is above threshhold. Large number to disable invariants
    num_threads = 20

    algebra = sys.argv[1]
    order = int(sys.argv[2])
    target_cube_length = int(sys.argv[3])
    power = int(sys.argv[4])
    num_threads = int(sys.argv[5])
    cubes_run_stage = 0
    if len(sys.argv) >= 7:
        cubes_run_stage = int(sys.argv[6])

    propagated_models_count = 0
    t0 = time.time()
    if cubes_run_stage == 0 or cubes_run_stage == 1:
        print(f'{datetime.now().strftime("%d/%m/%Y %H:%M:%S")} Generating all cubes...', flush=True)
        propagated_models_count += gen_all_cubes(algebra, order, power, target_cube_length, threshold, mace4_exe, cubes_options, num_threads)

    cube_file = f"cubes_{order}_{target_cube_length}.out" 
    if cubes_run_stage == 1:
        os.makedirs("cubes", exist_ok=True)
        cfn = f"cubes/{cube_file}"
        shutil.copy(f"utils/mace4/working/{algebra}{order}/{cube_file}", cfn)
        with open(cfn) as fp:
            seq = fp.readlines()
        random.shuffle(seq)
        with open(cfn, "w") as ofp:
            ofp.writelines(seq)
        cmd = f"cat *_working_*/models.out > cubes/models.out"
        subprocess.run(cmd, capture_output=False, text=True, check=False, shell=True)

    t1 = time.time()
    gen_cube_time = t1 - t0
    t2 = time.time()
    print(f'{datetime.now().strftime("%d/%m/%Y %H:%M:%S")} Done generating cubes for {algebra}, order {order}. Generating models...', flush=True)
    if cubes_run_stage == 2:
        os.makedirs(f"utils/mace4/working/{algebra}{order}", exist_ok=True)
        shutil.copy(f"cubes/{cube_file}", f"utils/mace4/working/{algebra}{order}/{cube_file}")
    if cubes_run_stage == 0 or cubes_run_stage == 2:
        run_all_cubes(algebra, order, power, target_cube_length, mace4_exe, mlex_exe, cubes_options, num_threads)
    t3 = time.time()
    runtime = t3 - t2
    collect_stat(algebra, order, target_cube_length, cubes_options, threshold, propagated_models_count, gen_cube_time, runtime)
    print(f'Done {datetime.now().strftime("%d/%m/%Y %H:%M:%S")}')
    
