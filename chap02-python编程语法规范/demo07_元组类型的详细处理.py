# *_* coding:utf-8 *_*
# @author:sdh
# @Time : 2021/3/16 0016 11:01
"""
元组是不可变类型，一般计算其统计特性，与列表类型相似。
切片、转为列表、拆包

"""
# 1 元组的切片
tuple_0 = (1, 2, 3, 4)
# tuple_0[0:2] # (1,2)


# 2 元组转为列表：
list(tuple_0)  # [1,2,3,4]
# 列表转为元组
tuple([1, 2, 3, 4])  # (1,2,3,4)

# 3 元组的拆包，简单拆包：
tuple_1 = (1, 2)
a, b = tuple_1
print(a, b)  # a=1 b=2

# 元组的拆包，复杂拆包:
tuple_1 = (1, 2, 3, 4, 5)
a, b, *c = tuple_1
print(a, b, c)  # a=1,b=2,c=[3,4,5]

# 更多元组的操作方法 查看
print(dir(tuple))
