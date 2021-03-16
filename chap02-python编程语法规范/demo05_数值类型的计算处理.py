# *_* coding:utf-8 *_*
# @author:sdh
# @Time : 2021/3/16 0016 10:01
"""
数值类型的基本数学运算
+、-、/、*、% 、//
"""
n1 = 2  # int
n2 = 3  # int
n3 = 3.0  # float
n4 = 4  # int
print(type(n1 + n2))  # int+int = int
print(type(n1 + n3))  # int+float = float

print(type(n1 - n2))  # int-int = int
print(type(n1 - n3))  # int-float = float

print(type(n1 * n2))  # int-int = int
print(type(n1 * n3))  # int-float = float

print(type(n2 / n1))  # int/int = float (不能整除)
print(type(n4 / n1))  # int/int = float (能整除)
print(type(n3 / n1))  # float/int = float (能整除)

print(type(n3 % n1))  # float%int = float
print(type(n4 % n1))  # int%int = int

print(type(n3 // n1))  # float//int = float
print(type(n4 // n1))  # int//int = int

"""
math模块中的数值运算

"""
import math

# 常数
print(math.pi, math.e, math.tau)

# 向上或向下取值
print(math.ceil(1.5))  # 2
print(math.floor(1.5))  # 1
