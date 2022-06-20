#!/bin/bash

function foo() {
    x1=$1
    x2=$2
    x3=$3

    # shellcheck disable=SC2046
    # shellcheck disable=SC2006
    # shellcheck disable=SC2003
    return `expr "$x1" + "$x2" + "$x3"`
}

# shellcheck disable=SC1068
foo 1 2 3 # 传参
echo $?   # 获得返回值
