# *_* coding:utf-8 *_*
# @author:sdh
# @Time : 2021/3/17 0017 15:14
"""
python中允许多继承
子类继承多个父类的属性和方法
"""


class GF:
    def __init__(self, first_name):
        self.first_name = first_name

    def show_gf(self):
        print(self.first_name)


class GM:
    def __init__(self, character):
        self.character = character

    def show_gm(self):
        print(self.character)


class F(GF, GM):
    def __init__(self, first_name, character):
        GF.__init__(self, first_name)
        GM.__init__(self, character)


f = F("123", "oooo")
print(f.first_name, f.character)
f.show_gf()
f.show_gm()

