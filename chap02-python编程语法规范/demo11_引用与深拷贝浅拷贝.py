# *_* coding:utf-8 *_*
# @author:sdh
# @Time : 2021/3/16 0016 11:43
# 引用：
# 引用就是变量的别名，地址一样，可变类型修改一个全部修改。
# 干扰的情况：使用同一个标识符进行变量的表示，且是不可变类型。

a = "sdh"  # 不可变类型
b = a
print(id(a), id(b))  # 地址相同

c = [11, 22, 33]  # 可变类型
d = e = c
print(id(c), id(d), id(e))

c[0] = 55
print(c, d, e)  # 全部修改

# 干扰的情况：不可变类型
x = 1
y = x
print(id(x), id(y))

x = 2
print(id(x))  # 这里的x与上面的x不是一个东西
print(x, y)

# 深拷贝：
# 深拷贝做递归拷贝，递归拷贝所有的内部嵌套数据。
# 深拷贝递归拷贝遇到可变类型则创建新的内存空间。
# 深拷贝递归拷贝遇到不可变数据类型就是拷贝的引用。
import copy

v1 = [11, 22, 33, [44, 55, 66]]
v2 = copy.deepcopy(v1)
print(id(v1), id(v2))  # 地址不一样
print(id(v1[0]), id(v2[0]))  # 地址一样
print(id(v1[3]), id(v2[3]))  # 地址不一样
print(id(v1[3][0]), id(v2[3][0]))  # 地址一样

# 浅拷贝：

# 浅拷贝只做最顶层的数据类型判断。
# 如果顶层是可变类型则创建新的内存空间。
# 如果顶层是不可变数据类型就是引用拷贝。

import copy

x1 = [1, 2, 3, [4, 5, 6]]
y1 = copy.copy(x1)

print(id(x1), id(y1))  # 地址不一样
print(id(x1[0]), id(y1[0]))  # 地址一样
print(id(x1[3]), id(y1[3]))  # 地址一样(与深拷贝的区别就在这里，顶层拷贝而不是递归拷贝)
print(id(x1[3][0]), id(y1[3][0]))  # 地址一样
x1[3][0] = 555
print(x1, y1)  # x1 与 y1 相同

# 不可变类型
x1 = (1, 2, 3, [4, 5, 6])
y1 = copy.copy(x1)

print(id(x1), id(y1))  # 地址一样
print(id(x1[0]), id(y1[0]))  # 地址一样
print(id(x1[3]), id(y1[3]))  # 地址一样(与深拷贝的区别就在这里，顶层拷贝而不是递归拷贝)
print(id(x1[3][0]), id(y1[3][0]))  # 地址一样

x1[3][0] = 555
print(x1, y1)  # x1 与 y1 相同
