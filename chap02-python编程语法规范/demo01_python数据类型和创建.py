# *_* coding:utf-8 *_*
# @author:sdh
# @Time : 2021/3/15 0015 10:00
"""
python中常见的数据类型？
字符串str、整型int、浮点型float、布尔类型bool、元组tuple、列表list、字典dict、集合set。

"""
# 字符串的创建的4三种方式。

# 1 双单引号
s1 = 'python'

# 2 双双引号
s2 = "python need me"

# 3 三双引号
s3 = """python need me,
I need python,
we all meed computer.
"""
# 4 三双引号
s4 = '''python need me,
I need python,
we all meed computer.
'''

# 双单引号和双双引号的特殊使用,自动转义
# 原始字符串中包含单引号，可以使用双引号定义
# 原始字符串中包含双引号，可以使用单引号定义
s5 = "I'm a student"
s6 = 'The teacher said: "Practice makes perfect" is a very famous proverb.'

# 三单引号和三双引号的作用：实现多行字符串、多行注释功能。
# #######################以上是字符串的创建#################################### #
# 整型的创建
n1 = 10
n2 = int()  # 默认值是0
n3 = int(3.14159)
n4 = int('123')  # 字符串中的值必须是整型才能转换
# print(n1, n2, n3, n4)
# #######################以上是整型的创建###################################### #
# 浮点型的创建
f1 = 132.567
f2 = float()  # 默认值是0.0
f3 = float(3)
f4 = float('1000')  # 字符串中的值可以是整型也可以是浮点型
f5 = float('3.01')
# print(f1, f2, f3, f4, f5)
# #######################以上是浮点型的创建###################################### #
# 布尔类型的创建
b1 = True
b2 = False
b3 = bool()  # 默认为False
# 字符串中空为False，非空为True
# 整型中的0为False，非0为True
# 浮点型型中的0.0为False，非0.0为True
# 元组、列表、字典、集合空为False，非空为True
b4 = bool(3)
# print(b1, b2, b3, b4)
# #######################以上是布尔类型的创建###################################### #
# 元组类型的创建
t0 = ()  # 空元组
t1 = (1, 2.0, 3, "hello")  # 组内数据类型可以不一样
t2 = tuple()  # 默认为空
t3 = tuple((1, 2, 3))  # 注意格式
# print(t1, t2, t3)
# #######################以上是元组类型的创建###################################### #
# 列表类型的创建
l0 = []  # 空列表
l1 = [1, 2, 3, 4.0, 'xyz']
l2 = list()  # 默认为空
l3 = list([1, 2, 3])  # 注意格式
# print(l1, l2, l3)
# #######################以上是列表类型的创建###################################### #
# 字典类型的创建
d0 = {}  # 空字典
d1 = {"name": "python", "years": 2021, "time": 11.04}
d2 = dict()  # 默认为空
d3 = dict({"name": "sdh", "years": 2021})  # 注意格式
# print(d1, d2, d3)
# #######################以上是字典类型的创建###################################### #
# 集合的创建：集合是无序的！
set0 = {1, 2, 3}  # 创建集合，注意和创建字典的区别
set1 = set(s1)  # 字符串转为集合
set2 = set(t1)  # 元组转为集合
set3 = set(l1)  # 列表转为集合
set4 = set(d1)  # 字典转为集合,只取字典的key值。
# print(set1,set2,set3,set4)
# #######################以上是集合类型的创建###################################### #

# #######################查看数据的类型########################################### #

print(type(s1), type(n1), type(f1), type(b1), type(t1), type(l1), type(d1), type(set0))
