# *_* coding:utf-8 *_*
# @author:sdh
# @Time : 2021/3/17 0017 10:13
"""
实例和对象：实例即对象。
实例属性：写在__init__方法中的通过self调用的变量，self代表当前实例对象。
实例方法：写在类内的，必须包含参数self的函数称为实例方法。

类创建的本质：
当创建对象时：
(1)首先是调用从 object 类继承的__new__方法，__new__方法返回一个实例;
(2)然后初始化实例时自动调用__init__方法;
(3)返回的实例会作为第一个参数self传给__init__方法。


"""


# 创建类
class Student(object):
    def __init__(self, name, score, rank):
        # 实例属性
        self.name = name
        self.score = score
        self.rank = rank

    # 实例方法
    def show_stu_message(self):
        print(self.name, self.score, self.rank)

    # 带参数的实例方法
    def show_math_score(self, math):
        # 方法内部调用其方法
        self.show_stu_message()
        print(self.name, math)


# 在类的外部 创建对象、对象属性、对象方法、修改属性
sdh = Student("sdh", 98, 1)
print(sdh.name)
sdh.show_stu_message()
sdh.show_math_score(100)

sdh.score = 100

# 不能通过类名调用实例属性和方法
# print(Student.name)
# print(Student.show_stu_message())