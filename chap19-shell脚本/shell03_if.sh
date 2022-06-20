#!/bin/bash

# If条件判断语句，通常以if开头，fi结尾。也可加入else或者elif进行多条件的判断
#
#
#
## 单分支语句 ---比较大小
#	if (条件表达式);then
#		语句1
#	fi

a=1
b=2

if [ $a -lt $b ]; then
  echo "1<2"
fi


if((a<b));then
  echo "$a"
fi