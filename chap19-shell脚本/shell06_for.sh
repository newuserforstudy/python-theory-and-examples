#!/bin/bash

for (( i = 0; i < 5; i++ )); do
    echo $i
    echo "$i"
done

for j in {1..5} ; do
    echo "$j"
done


for i in {0..2} ; do
    echo $RANDOM
done


for i in $(seq 10) ; do
    echo $RANDOM
done


for i in $(seq 10 -1 1) ; do
    echo "$i"
done
