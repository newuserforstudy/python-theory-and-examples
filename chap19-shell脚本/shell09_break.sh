#!/bin/bash

i=0
while ((i<10)); do
  echo "$i"
  if((i==3));then
    break
  fi
  ((i++))
done