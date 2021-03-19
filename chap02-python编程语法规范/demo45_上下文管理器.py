# *_* coding:utf-8 *_*
# @author:sdh
# @Time : 2021/3/18 0018 18:16
"""
通常情况下，如果要写一个上下文管理器，
你需要定义一个类，里面包含一个 __enter__() 和一个 __exit__() 方法，

"""
import time
from contextlib import contextmanager


class TimeThis:
    def __init__(self, label):
        self.label = label

    def __enter__(self):
        self.start = time.time()

    def __exit__(self, exc_ty, exc_val, exc_tb):
        end = time.time()
        print('{}: {}'.format(self.label, end - self.start))


"""
f的结果不是创建TimeThis对象，而是TimeThis('counting').__enter__的结果
执行with时先自动进入__enter__，当执行结束时自动触发__exit__
"""

with TimeThis(100) as f:
    pass

"""
实现一个新的上下文管理器的最简单的方法就是使用 contexlib 模块中的 @contextmanager 装饰器。
@contextmanager 应该仅仅用来写自包含的上下文管理函数。 
如果你有一些对象(比如一个文件、网络连接或锁)，需要支持 with 语句，那么你就需要单独实现 __enter__() 方法和 __exit__() 方法。
"""

"""
在函数 timethis() 中，
yield 之前的代码会在上下文管理器中作为 __enter__() 方法执行， 
所有在 yield 之后的代码会作为 __exit__() 方法执行。 如果出现了异常，异常会在yield语句那里抛出。
"""


@contextmanager
def timethis(label):
    start = time.time()
    try:
        yield
    finally:
        end = time.time()
        print('{}: {}'.format(label, end - start))


# Example use

with timethis('counting') as f1:
    n = 10000000
    while n > 0:
        n -= 1
