# *_* coding:utf-8 *_*
# @author:sdh
# @Time : 2021/3/17 0017 17:03
"""

迭代的机制(for循环)：
for语句会在容器对象上调用 iter()。 该函数返回一个定义了 __next__() 方法的迭代器对象，此方法将逐一访问容器中的元素。
当元素用尽时，__next__() 将引发 StopIteration 异常来通知终止 for 循环。
你可以使用 next() 内置函数来调用 __next__() 方法；
"""
from collections.abc import Iterator, Iterable

# 1 判断一个对象是否可迭代
# 实现了__iter__方法就是可迭代的
print(isinstance([1, 2, 3], Iterable))  # True

# 2 判断一个对象是否是迭代器
print(isinstance([1, 2, 3], Iterator))  # False
# 一个类实现__iter__方法且返回一个具有__next__方法的对象(这个对象可以是自己，也可以是其他类的对象)，且该类实现__next__方法
print(isinstance(iter([1, 2, 3]), Iterator))  # True


# 创建自己的迭代器
class Reverse(object):
    def __init__(self, data):
        self.data = data
        self.index = len(data)

    def __iter__(self):
        return self

    def __next__(self):
        if self.index == 0:
            raise StopIteration
        self.index = self.index - 1
        return self.data[self.index]
