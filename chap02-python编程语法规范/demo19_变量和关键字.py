# *_* coding:utf-8 *_*
# @author:sdh
# @Time : 2021/3/16 0016 18:20
"""
变量的名字规则：
规则：数字字母和下划线，不能以数字开头，不使用中文，不能是python中的关键字。
方式：驼峰命名法和匈牙利命名法。
小驼峰命名法：第一个单词以小写字母开始；第二个单词的首字母大写或每一个单词的首字母都采用大写字母
如myFirstName、myLastName。
大驼峰命名法：单词的首字母大写或每一个单词的首字母都采用大写字母
如MyFirstName、MyLastName。
匈牙利命名法关键是：标识符的名字以一个或者多个小写字母开头作为前缀；前缀之后的是首字母大写的一个单词或多个单词组合，该单词要指明变量的用途
下划线命名法：单词小写，单词之间使用下划线_进行连接。

python中的命名规范：
变量、函数、方法：下划线命名法，my_name
类：大驼峰命名法，如StudentClass、MyHome

"""

# 1 python中的关键字：35个
import keyword

# ['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await',
# 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except',
# 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda',
# 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']
print(len(keyword.kwlist))
print(keyword.kwlist)

# 目前还未用过的关键字
# ['assert', 'async', 'await', 'class','del','yield']
