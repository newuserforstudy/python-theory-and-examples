#!/bin/bash

# 字体颜色: echo -e
for i in {31..32};
do
echo -e "\033[$i;40mHello world!\033[0m"
done
## 背景颜色
#for i in {41..47}; do
#echo -e "\033[47;${i}mHello world!\033[0m"
#done
## 显示方式
#for i in {1..8}; do
#echo -e "\033[$i;31;40mHello world!\033[0m"
#done

