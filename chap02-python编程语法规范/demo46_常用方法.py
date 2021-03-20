# *_* coding:utf-8 *_*
# @author:sdh
# @Time : 2021/3/18 0020 18:25

# 1 sort方法和sorted函数
x = [2, 1, 4, 7]
x.sort()
print(x)

sorted(sorted(x))

# 2 filter类
# 第一个参数是函数，第二个参数是可迭代对象
nums = [12, 18, 30, 49, 21]
print(list(filter(lambda e: e > 18, nums)))

# 3 map类
# 需要2个参数，第一个参数 是函数，第二个参数是可迭代对象
print(list(map(lambda e: e + 2, nums)))

# 4 reduce
from functools import reduce

x = [1, 2, 3, 4]
print(reduce(lambda e1, e2: e1 + e2, x))

"""
更多方法和类参考functools模块
"""

"""
几个常用属性

"""


# 1 __call__
# 调用对象

# 2 __name__:直接运行问件时是main，被导入时是文件名

# 3 __slots__：定义在类内不再__init__内，元组类型，规定可以存在的属性
class Stu(object):
    __slots__ = ("name", "age")

    def __init__(self, name, age):
        self.name = name
        self.age = age

s = Stu(11,22)
# s.score = 10