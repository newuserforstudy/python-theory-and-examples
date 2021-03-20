# *_* coding:utf-8 *_*
# @author:sdh
# @Time : 2021/3/18 0018 18:26
"""
在python中一切皆对象！！！

"""
# 1 变量的类型
x = 1
print(type(x))  # int类型的对象

# 2 元组类型
t = (1, 2, 3)
print(type(t))


# 3 函数类型:函数是function类的对象
def sn():
    pass


print(type(sn))  # <class 'function'>

# 4 type类型：类是type类的对象
class Model(object):
    pass

print(type(Model))  # <class 'type'>


