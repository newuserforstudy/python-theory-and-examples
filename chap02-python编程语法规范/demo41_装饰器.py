# *_* coding:utf-8 *_*
# @author:sdh
# @Time : 2021/3/18 0018 17:50
"""
闭包：函数嵌套，外部函数返回内部函数的引用。
在一个内部函数里，对在外部函数作用域，但不是全局作用域，的变量进行引用，那么整个函数就被认为是闭包closure

装饰器的作用：开放封闭原则
不修改固有的代码，在需求的时候编写自己的代码实现要求的功能！

"""

# 1 闭包的实例
# def outer():
#     num = 100
#
#     def inner():
#         y = num + 1
#         return y
#     return inner
#
#
# print(outer()())
import time


# 2 不使用装饰器
# def outer(fn):
#     s = time.time()
#     fn()
#     e = time.time()
#     print(e - s)
#
#
# def f1():
#     print("测试函数1")
#     time.sleep(3)
#     print("函数1测试结束")
#
#
# def f2():
#     print("测试函数2")
#     time.sleep(3)
#     print("函数2测试结束")
#
#
# outer(f1)
# outer(f2)

# 3 使用装饰器
# def outer(fn):
#     def inner():
#         s = time.time()
#         fn()
#         e = time.time()
#         print(e - s)
#
#     return inner
#
#
# @outer  # @outer语法糖做了2件事： 1立刻调用外部函数；2把@outer下面的函数作为参数传给外部函数
# def f1():
#     print("测试函数1")
#     time.sleep(3)
#     print("函数1测试结束")
#
#
# f1()  # 3 此时的f1不再是上面的f1了，而是返回的inner函数。


# 4 装饰器：内部函数带返回值
# def outer(fn):
#     def inner():
#         s = time.time()
#         fn()
#         e = time.time()
#         print(e - s)
#
#         # 内部函数带返回值
#         return "hello world"
#
#     return inner
#
#
# @outer  # @outer语法糖做了2件事： 1立刻调用外部函数；2把@outer下面的函数作为参数传给外部函数
# def f1():
#     print("测试函数1")
#     time.sleep(3)
#     print("函数1测试结束")
#
#
# re = f1()  # 3 此时的f1不再是上面的f1了，而是返回的inner函数，inner函数有返回值！
# print(re)

# 5 装饰器:被装饰的函数带有返回值
# def outer(fn):
#     def inner():
#         s = time.time()
#         # 调用被装饰的函数，re接收fn返回的结果
#         re = fn()
#         e = time.time()
#         print(re)
#
#     return inner
#
#
# @outer  # @outer语法糖做了2件事： 1立刻调用外部函数；2把@outer下面的函数作为参数传给外部函数
# def f1():
#     print("测试函数1")
#     time.sleep(3)
#     print("函数1测试结束")
#
#     # 被装饰的函数带返回值
#     return "hello world"
#
#
# f1()  # 3 此时的f1不再是上面的f1了，而是返回的inner函数.

# 6 装饰器：被装饰的函数带有参数
# def outer(fn):
#     def inner(n):
#         s = time.time()
#         # 调用被装饰的函数，fn需要参数
#         fn(n)
#         e = time.time()
#         print(e-s)
#
#     return inner
#
#
# @outer  # @outer语法糖做了2件事： 1立刻调用外部函数；2把@outer下面的函数作为参数传给外部函数
# def f1(n):
#     print("测试函数1")
#     time.sleep(n)
#     print("函数1测试结束")
#
#
# f1(2)  # 3 此时的f1不再是上面的f1了，而是返回的inner函数.

# 7 装饰器：带可变参数
def outer(fn):
    def inner(n, *args, **kwargs):
        s = time.time()
        # 调用被装饰的函数，fn需要参数
        fn(n)
        e = time.time()
        print(e - s)

    return inner


@outer  # @outer语法糖做了2件事： 1立刻调用外部函数；2把@outer下面的函数作为参数传给外部函数
def f1(n):
    print("测试函数1")
    time.sleep(n)
    print("函数1测试结束")


f1(2, (1, 2, 3), m="xxxx")  # 3 此时的f1不再是上面的f1了，而是返回的inner函数.
