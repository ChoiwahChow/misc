#!/bin/bash

order=$1
cubelength=$2

./bin/mace4c -m-1 -A-1 -W-1 -n${order} -O0 -M5 -C${cubelength} -f inputs/alt-qg5.in > logs/alt-qg5-${order}-${cubelength}.O0M5.log 2>&1

mv cubes.out data/alt-qg5-${order}-${cubelength}.O0M5.data
