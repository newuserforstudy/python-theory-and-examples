# *_* coding:utf-8 *_*
# @author:sdh
# @Time : 2021/3/18 0018 18:15
"""
不同于Java、C++，python中并没有直接提供ABC，Abstract Base Class抽象基类与抽象方法，
但是提供了内置模块abc(abstract base class)来模拟实现抽象类。
可以通过abc将基类声明为抽象类的方式，然后注册具体类作为这个基类的实现。

抽象基类的几大特点：

1：定义但是不实现方法，抽象基类不能实例化！
2：作为父类，供子类继承实现多态,子类必须全部重写虚函数(类似于C++)


"""
import abc
from abc import ABC, ABCMeta

"""
collections 模块中有一些派生自 ABC 的具体类；当然这些类还可以进一步被派生。
此外，collections.abc子模块中有一些 ABC 可被用于测试一个类或实例是否提供特定的接口.
该模块提供了一个元类ABCMeta，可以用来定义抽象类，另外还提供一个工具类 ABC，可以用它以继承的方式定义抽象基类
"""


# 定义一个抽象基类


class MyABC(ABC):
    pass


print(type(MyABC))  # <class 'abc.ABCMeta'>

"""
注意 ABC 的类型仍然是 ABCMeta，因此继承 ABC 仍然需要关注元类使用中的注意事项，比如可能会导致元类冲突的多重继承。
当然也可以直接使用 ABCMeta 作为元类来定义抽象基类
"""


class MyABC2(metaclass=ABCMeta):
    pass


print(type(MyABC2))  # <class 'abc.ABCMeta'>


# 子类继承抽象基类

class IStream(metaclass=ABCMeta):
    @abc.abstractmethod
    def read(self, maxbytes=-1):
        pass

    @abc.abstractmethod
    def write(self, data):
        pass


# 抽象类不能直接被实例化
# a = IStream() # TypeError: Can't instantiate abstract class IStream with abstract methods read, write


class SocketStream(IStream):
    def read(self, maxbytes=-1):
        pass

    def write(self, data):
        pass


# 除了继承这种方式外，还可以通过注册方式来让某个类实现抽象基类：
import io

# Register the built-in I/O classes as supporting our interface
IStream.register(io.IOBase)

# Open a normal file and type check
f = open('../section2数据部分/test.txt')
print(isinstance(f, IStream))  # True


# @abstractmethod 还能注解静态方法、类方法和 properties 。 只需保证这个注解紧靠在函数定义前即可.
class A(metaclass=ABCMeta):
    @property
    @abc.abstractmethod
    def name(self):
        pass

    @name.setter
    @abc.abstractmethod
    def name(self, value):
        pass

    @classmethod
    @abc.abstractmethod
    def method1(cls):
        pass

    @staticmethod
    @abc.abstractmethod
    def method2():
        pass


"""
标准库中有很多用到抽象基类的地方。
collections 模块定义了很多跟容器和迭代器(序列、映射、集合等)有关的抽象基类。 
numbers 库定义了跟数字对象(整数、浮点数、有理数等)有关的基类。
io 库定义了很多跟I/O操作相关的基类。
"""
