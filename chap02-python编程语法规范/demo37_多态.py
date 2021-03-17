# *_* coding:utf-8 *_*
# @author:sdh
# @Time : 2021/3/17 0017 16:09
"""
多态依赖于继承：
多个子类继承一个父类并重写父类的方法实现不同的功能！
"""


class Job(object):
    def __init__(self, job):
        self.job = job

    def show_job(self):
        print(self.job)


class Stu(Job):
    def show_job(self):
        # do something
        print("11111")


class Teacher(Job):
    def show_job(self):
        # do something
        print("2222")


class Runner(Job):
    def show_job(self):
        # do something
        print("333")
