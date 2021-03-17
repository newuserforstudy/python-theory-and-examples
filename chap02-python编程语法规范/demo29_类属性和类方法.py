# *_* coding:utf-8 *_*
# @author:sdh
# @Time : 2021/3/17 0017 11:04
"""
类属性和类方法：
用来描述类的相关信息

"""


class Student(object):
    stu_num = 0  # 学生的数量

    def __init__(self, stu_name, stu_id):
        # 通过类名调用类属性
        Student.stu_num += 1
        self.stu_name = stu_name
        self.stu_id = stu_id

    @classmethod
    def show_stu_nums(cls):
        print(cls.stu_num)


# 创建一个对象__init__就会被调用一次
s1 = Student("sdh", 1)
s2 = Student("xyz", 2)
s3 = Student("abc", 3)

# 通过类名调用类属性和类方法
Student.show_stu_nums()
print(Student.stu_num)

# 通过对象名调用类属性
print(s1.stu_num)
print(s2.stu_num)
print(s3.stu_num)

# 不能通过对象名调用类方法
print(s1.show_stu_nums())  # None
