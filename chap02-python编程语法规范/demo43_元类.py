# *_* coding:utf-8 *_*
# @author:sdh
# @Time : 2021/3/18 0018 18:10
"""
在Python当中万物皆对象，我们用class关键字定义的类本身也是一个对象，负责产生该对象的类称之为元类，元类可以简称为类的类，
元类的主要目的是为了控制类的创建行为.
type是Python的一个内建元类，用来直接控制生成类，在python当中任何class定义的类其实都是type类实例化的结果
只有继承了type类才能称之为一个元类，否则就是一个普通的自定义类，自定义元类可以控制类的产生过程，类的产生过程其实就是元类
的调用过程.

python中type的作用:
1 测试对象的类型
2 动态地创建类：
    用法：type(类名,(父类，父类2,),{属性名：值，方法名：方法})
"""
# 创建类：
# 创建类的第一种方式
# class Stu(object):
#     num = 0
#
#     def __init__(self, name):
#         self.name = name
#
#     def show(self):
#         print(self.name)
#
#
# print(type(Stu))  # <class 'type'> Stu类就是type类的实例对象

# 创建类的第二种方式
num = 0


def __init__(self, name):
    self.name = name


def show(self):
    print(self.name)


Stu = type('Stu', (object,), {'num': num, '__init__': __init__, 'show': show})
print(type(Stu))  # <class 'type'>

# 创建自定义元类：继承于type类
"""
元类就是创建类的类，凡是继承了type的类，都是元类.
python中类的实例化过程中，首先会在这个类中寻找是否继承Metaclass，如果找到了就通过Metaclass创建类，如果找不到才会通过type创建类。
元类的主要目的就是为了当创建类时能够自动地改变类。
"""


class Meta(type):
    pass


class Magic(metaclass=Meta):
    pass


m = Magic()
