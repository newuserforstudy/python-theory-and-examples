# *_* coding:utf-8 *_*
# @author:sdh
# @Time : 2021/4/3 0003 18:00
"""
1 线性表
1.1 线性表的定义：零个或者多个数据元素的有限序列，元素类型不要求一致。
1.2 线性表的顺序存储形式为：顺序线性表
    顺序线性表：指的是一段地址连续的存储单元依次存储线性表的数据元素。
    线性顺序表：可以用一维数组来表示。
1.3 线性表的链式存储形式为：链式线性表。
1.4 单链表：单向链表，区别于双向链表。
1.5 静态链表：用数组描述的链表叫做静态链表。
1.6 循环链表：单循环链表的简称，尾部结束之后又回到首部形成一个闭环的链表。
    单向循环链表
    双向循环链表
1.7 双向链表：链表是双向的，区别于单向链表。
"""

"""
这里介绍最基本的顺序线性表。
顺序线性表：
 -----------------------
| a1 | a2 | a3 |...| an |
 -----------------------


python中的顺序线性表可以用##列表或者一维数组##来代替实现。

访问线性表的元素，可以直接通过下表。
"""
sequential_linear_table1 = [1, 2, 3, 4]
sequential_linear_table2 = [3.14, 5, 8.79]

print(sequential_linear_table2[2])
