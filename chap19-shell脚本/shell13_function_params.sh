#!/bin/bash

function foo() {
    x1=$1
    x2=$2

    # shellcheck disable=SC2006
    # shellcheck disable=SC2003
    x3=`expr "$x1" + "$x2"`  # 注意空格 ,3
    # x3=`expr "$x1"+"$x2"`  # 1+2
    echo "$x3"
}
foo 1 2


