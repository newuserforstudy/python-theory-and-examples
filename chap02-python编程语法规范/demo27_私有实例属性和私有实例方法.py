# *_* coding:utf-8 *_*
# @author:sdh
# @Time : 2021/3/17 0017 10:31
"""
私有和公有：
公有指的是在类的内部和外部都能访问；
私有指的是只能在类的内部访问不能再外部直接访问。

python中的私有属性和私有方法是在属性前加2个下划线__，不加__的默认为公有。
python中的私有是伪私有，可有通过其他途径访问，但是不建议这样做。

私有属性和私有方法的访问方法：
    在类的内部，通过其他的公有方法访问！！！
"""


# 创建类
class Student(object):
    def __init__(self, name, score, rank):
        # 实例属性
        self.name = name
        self.__score = score # 这个属性是私有的
        self.rank = rank

    # 实例方法
    def show_stu_message(self):
        print(self.name, self.__score, self.rank)

    # 带参数的实例方法,私有方法
    def __show_math_score(self, math):
        print(self.name, math)


# 在类的外部 创建对象、对象属性、对象方法
sdh = Student("sdh", 98.00, 1)
# print(sdh._score)  # 报错，类的外部不能访问私有属性
print(sdh._Student__score) # 通过类名强制访问

