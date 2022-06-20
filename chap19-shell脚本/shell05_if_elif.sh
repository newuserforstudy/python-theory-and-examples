#!/bin/bash

a=1
b=2
c=3

if [ $a -lt $b ]; then
    echo $b
elif [ $a -lt $c ]; then
    echo $a
fi