# *_* coding:utf-8 *_*
# @author:sdh
# @Time : 2021/3/17 0017 10:43
"""
静态方法的定义：
    静态方法实际上就是定义在类内部的普通函数，定义形式是在def行前加修饰符@staticmethod，
    静态方法的参数不加self参数。
为什么要静态方法：
    静态方法的作用记录与实际目的性操作无关的日志、记录等信息。
可以通过类名或者实例对象调用静态方法
"""
import time


class Model(object):
    def __init__(self, name, file):
        self.name = name
        self.file = file

    # 静态方法
    @staticmethod
    def log_note(now_time):
        print(now_time)


model = Model("python", "class")

# 通过对象调用静态方法
model.log_note(time.asctime())

# 通过类名调用静态方法
Model.log_note(time.asctime())
