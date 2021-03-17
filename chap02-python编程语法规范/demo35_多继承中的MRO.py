# *_* coding:utf-8 *_*
# @author:sdh
# @Time : 2021/3/17 0017 15:45
"""
当多个父类具有相同的属性和方法时，子类继承的顺序按照广度优先、MRO顺序。
为防止这类情况发生：尽量不要使用同名的属性和方法！！！
"""


class GF:
    def __init__(self):
        self.home = "home1111"

    def show_g(self):
        print(self.home)


class GM:
    def __init__(self):
        self.home = "home22222"

    def show_g(self):
        print(self.home)


class F(GF, GM):
    def __init__(self):
        super(F, self).__init__()
        self.home = "home3333"


f = F()
print(f.home)
print(F.__mro__)
