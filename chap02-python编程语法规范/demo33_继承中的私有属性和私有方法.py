# *_* coding:utf-8 *_*
# @author:sdh
# @Time : 2021/3/17 0017 15:02
"""
私有属性和方法不能被继承！！
"""


class Father:
    def __init__(self, first_name, blood):
        self.__first_name = first_name
        self.__blood = blood

    def __show_name(self):
        print(self.__first_name)


class Son(Father):
    # 这里报错、不能继承私有属性和方法
    def show(self):
        print(self.__first_name)


s = Son("wang", "O")
s.show()
