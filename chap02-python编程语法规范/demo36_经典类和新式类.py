# *_* coding:utf-8 *_*
# @author:sdh
# @Time : 2021/3/17 0017 16:00
"""
经典类又叫旧式类
python2:
新式类：继承object类，MRO采用深度优先。
经典类：不继承object类，MRO采用深度优先。

python3：
移除了经典类，所有类默认继承object类，MRO采用广度优先

广度优先和深度优先：
广度优先：先从子类的父类搜索，搜不到再第二个父类，以此类推，所有父类都找不到再找父类的父类。
深度优先：先从子类的父类搜索，搜不到就找父类的父类知道找到，搜不到再从第二个父类开始找。
"""


class A(object):
    pass


class B(A):
    pass


a = A()
b = B()

# isinstance判断一个对象是否是某个类型
print(isinstance(a, object))  # True
print(isinstance(a, A))  # True
print(isinstance(b, B))  # True
print(isinstance(b, A))  # True  B继承A，则b的对象也是A的类
print(isinstance(a, B))  # False A不继承B，则b的对象不是A的类

print(type(b))