#!/bin/bash
# shellcheck disable=SC2054
# shellcheck disable=SC2034
array=(1,2,3,4)

for i in ${array[*]} ; do
    echo "$i"
done

for((i=0;i<${#array[*]};i++)); do
    echo "${array[$i]}"
done