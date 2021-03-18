# *_* coding:utf-8 *_*
# @author:sdh
# @Time : 2021/3/18 0018 10:31
"""

1 生成器的作用：
    数据特别大的时候建立一个显式的储存数据就会很占内存的，
    生成器是一个不怎么占计算机资源的数据存储方法，只有在使用它时才会取出数据。

2 生成器的创建：
    生成器是一种特殊的迭代器，本质就是迭代器，但是不需要想迭代器一样创建__iter__、__next__方法，
    而是在函数中使用yield关键字。

3 生成器的执行：
    只有在for遍历或者使用__next__方法和next函数时采用执行，
    当执行迭代时，程序运行到yield语句时，返回yield后面的结果，返回结果后当前一次迭代结束
    进行下一次迭代时，程序从yield语句的下一行继续执行而不是从头执行，一直执行到yield语句。

4 生成器传参
    在进行迭代时，可以通过send函数对生成器传参。
    send与next作用相同，都是进行下一次迭代的意思。 (都会解阻塞yield关键字)
    send可以传递参数表示yield语句的返回值。 而next不能传递参数。
    send一般不会放到第一次启动(迭代)生成器，如果非要这样做 那么传递None (否则会抛异常)
"""
# 1 简单的生成器

# x = [i for i in range(5)] # 列表

# generator:这是生成器
g = (i for i in range(5))
print(g)


# 迭代器是生成器，可以使用for进行遍历，也可以调用__next__方法。
# print(g.__next__())
# print(g.__next__())
# print(g.__next__())


# for e in g:
#     print(e)


# 2 使用yield创建生成器
def arithmetic_sequence(n, d):
    x = 0
    for i in range(n):
        yield x
        x += d


for j in arithmetic_sequence(5, 2):
    print(j)


# 3 生成器的参数

def make_examples():
    for i in range(10):
        x = yield i
        print(x)


m = make_examples()
# 第一次迭代：程序执行到yield，返回yield后面的值，即 0 ，打印结果为 0
# r1 的结果是 0
r1 = next(m)
print(r1)

# 第二次迭代：程序已经执行完yield后面的语句，接着执行yield前面的语句，即通过send传递参数给x，x的结果"sdh"。
# r2的结果是 1
r2 = m.send("sdh")
print(r2)
# 第三次迭代:
r3 = next(m)
print(r3)
