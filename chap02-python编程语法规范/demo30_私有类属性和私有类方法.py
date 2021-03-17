# *_* coding:utf-8 *_*
# @author:sdh
# @Time : 2021/3/17 0017 11:55
"""
私有类属性和私有类方法
(1) 只能由类名访问，对象不能访问。
(2) 只能在内部访问或者经公有方法调用后在外部访问

"""

class Student(object):
    __stu_num = 0  # 私有属性，学生的数量

    def __init__(self, stu_name, stu_id):
        # 内部通过类名调用私有类属性
        Student.__stu_num += 1
        self.stu_name = stu_name
        self.stu_id = stu_id

    @classmethod
    def __show_stu_nums(cls):
        print(cls.__stu_num)

    @classmethod
    def show(cls):
        cls.__show_stu_nums()


# 创建一个对象__init__就会被调用一次
s1 = Student("sdh", 1)
s2 = Student("xyz", 2)
s3 = Student("abc", 3)

# 通过公有类方法，调用私有类属性和私有类方法
Student.show()

# 私有类属性必须在类内部调用
# print(Student.__stu_num)
# print(s1.__stu_num)
# print(s2.__stu_num)
# print(s3.__stu_num)
