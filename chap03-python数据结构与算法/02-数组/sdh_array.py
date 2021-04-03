# *_* coding:utf-8 *_*
# @author:sdh
# @Time : 2021/3/27 0027 11:42
"""
1 数组
1.1  什么是数组array？
  定义是：是由相同类型的元素的集合所组成的数据结构，分配一块连续的内存来存储。
         利用元素的索引可以计算出该元素对应的存储地址。
  数组，常用的是元素是数值类型或者字符串类型。
  数值类型 1,2,3,4
  数组类型 1.0,2.0,3.0
  字符串类型 'a','b','c'

  数组的目的：用于数值的计算或者字符串的匹配。

1.2 一维数组
    数组元素在1个维度上排列，对应于数学中的向量。
1.3 二维数组
    数组元素在2个维度上排列，对应于数学中的二维矩阵。
1.4 多维数组
    数组元素在多个维度上排列，对应于数学中的多维矩阵。

2 python的机制
2.1 python中不能直接操作地址。由于这一点python创建数组时，不能够得到地址。
2.2 python中一切皆对象。
2.3 python中的数组可以通过array

*** 这里仅对一维数据进行操作与设计  ***

"""

"""
数组和python中的列表的区别：
    数组要求的数据类型必须是相同的。
    列表对数据类型不做要求。

当列表中的数据类型相同时，形式上可视为数组，原因是可能地址不连续，做不到像C++/java那样。
"""
# 1 python中的id函数
"""
    id(object)函数是返回对象object在其生命周期内位于内存中的地址。
"""
x = 3
y = 3
z = x
print(id(x), id(y), id(z), id(3))  # 结果是相同的，这一点是python区别于其他语言的一点。
"""
    int x=3;
    int y=3;
    std::cout<<&x<<std::endl;
    std::cout<<&y<<std::endl;  C++中地址是不相同的
"""

# 2 python中列表的机制
"""
在python中，变量并不直接存储值，而是存储值的引用，也就是说先把值放入内存地址之中，再让变量引用这个地址。
所以，在列表中，元素是连续排列存储的，但是他们的引用的地址往往是不连续的。

"""
# 元素是float类型，变量i是元素地址的引用，他们不是连续的。
# list1 = [1.0, 2.0, 3.0, 4.0]
# for i in list1:
#     print(id(i))
#
# # 元素是int类型，变量j是元素地址的引用，他们是连续的。
# list2 = [1, 2, 3, 4]
# for j in list2:
#     print(id(j))
#
# # 元素不完全相同，引用地址不连续
# list3 = [1, 2.0, 3, 3.14, "xyz"]
# for k in list3:
#     print(id(k))

# # 本质是一样的
# list4 = [1.0, 2.0, 3, 4, 5.0, 6, "name"]
# for m in range(len(list4)):
#     print(id(list4[m]))
# print("======================")
# for m in list4:
#     print(id(m))


# 3 数组和列表
# 3.1 列表中的数据都是相同的类型，可视作数组。
arr1 = [1, 2, 3]  # 元素都是int
arr2 = [1.0, 2.0, 3.0]  # 元素都是float
arr3 = ["x", "y", "z"]  # 元素都是str

# 3.2 列表中的元素不完全是相同的类型，不是数组。
arr4 = [1, 2, 3.14, 4.56, "name", "year"]  # 元素不完全相同

# 4 使用array模块,python实现像C++和java类似的数组创建，动态的。
# 4.1 创建像c那样的数组
"""
Type code      C Type             Minimum size in bytes
    'b'         signed integer     1
    'B'         unsigned integer   1
    'u'         Unicode character  2 (see note)
    'h'         signed integer     2
    'H'         unsigned integer   2
    'i'         signed integer     2
    'I'         unsigned integer   2
    'l'         signed integer     4
    'L'         unsigned integer   4
    'q'         signed integer     8 (see note)
    'Q'         unsigned integer   8 (see note)
    'f'         floating point     4
    'd'         floating point     8
"""
import array

a1 = array.array("i", (1, 2, 3, 4))
# print(a1)
a1.append(5)
# a1.append(3.5)  # 报错,类型不同
# print(a1)  # (1,2,3,4,5)
# print(type(a1))  # (1,2,3,4,5)

# 4.2 array模块中数组的属性和操作：类似于列表list
"""
操作：
    添加：
    删除
    修改
    查找
属性：
    长度
"""

# 5 创建自己的数组
"""
1 数组中的数据类型必须相同。
2 数组时动态的，可以增删改查。
"""

"""
基于列表实现python中的数组。其实是伪数组。
"""


class MyselfArray(object):
    allow_array = True

    def __init__(self, *args):
        # 判断元素类型是否完全一致
        ele_type_list_len = len(set([type(args[i]) for i in range(len(args))]))
        if ele_type_list_len == 1:
            self.arr = list(args)
            self.data_type = type(args[0])
        else:
            raise TypeError("数据类型错误")

    def append(self, x):
        if type(x) == self.data_type:
            self.arr.append(x)
        else:
            raise TypeError("数据类型错误！")

    def insert(self, index, x):
        if index in [i for i in range(len(self.arr))] and type(x) == self.data_type:
            self.arr.insert(index, x)
        else:
            raise Exception("无法插入！")

    def pop(self, index):
        self.arr.pop(index)


ma1 = MyselfArray(*(1, 2, 3))
print(ma1.arr)

ma1.append(4)
ma1.append(5)
print(ma1.arr)

ma1.insert(2, 100)
print(ma1.arr)

ma1.pop(1)
print(ma1.arr)
