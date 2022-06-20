#!/bin/bash

# shellcheck disable=SC2160

while [ true ]; do
  echo 111
  break
done

i=1
j=0
while ((i <= 100)); do
  # shellcheck disable=SC2006
  # shellcheck disable=SC2003
  j=`expr $i + $j`
  ((i++))
done
echo "$j"
