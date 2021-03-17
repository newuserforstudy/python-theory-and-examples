# *_* coding:utf-8 *_*
# @author:sdh
# @Time : 2021/3/17 0017 12:13
"""

使用super(Son, self).__init__(first_name, blood)去初始化父类.
函数super(Son, self)将返回当前类继承的父类，然后调用父类的__init__()方法，
注意self参数已在super()中传入，在__init__()中将隐式传递，不能再写出self。
"""


class Father:
    def __init__(self, first_name, blood):
        self.first_name = first_name
        self.blood = blood

    def show_name(self):
        print(self.first_name)


class Son(Father):
    def __init__(self, first_name, blood, years):
        super(Son, self).__init__(first_name, blood)
        self.years = years


s = Son("wang", "O", "25")
s.show_name()