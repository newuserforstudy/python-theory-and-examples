# *_* coding:utf-8 *_*
# @author:sdh
# @Time : 2021/3/16 0016 12:15
"""
1 函数的作用
封装，代码集中，避免混乱。
实现特定功能，一劳永逸，且区分其他功能。
小规模问题的常用手段，大规模使用面向对象的方法。
定义在类中的函数称之为方法。
"""
"""
2 python函数的定义与实现
使用关键字def定义函数。
函数的定义和调用是分开的。
"""


# 定义
def areas():
    pass


# 调用
areas()

"""
3 带返回值的函数
使用return关键字返回值
"""


def two_sum():
    a = 10
    b = 10
    return a + b


"""
4 带参数和返回值的函数
"""


def two_sums(a, b):
    return a + b


"""
5 带缺省参数的函数
缺省参数即含有默认值的参数。
定义函数时该参数一定在参数列表的最后。
调用函数时若不传参则使用默认值，传参则使用传参值。
"""


def nums_sum(a, b, c=1):
    return a + b + c


x = nums_sum(1, 2)
y = nums_sum(1, 2, 3)
print(x, y)  # 4,6
"""
6 带不定长参数的函数
不定长参数用在不确定参数长度的时候。
默认使用 * args和 ** kwargs作为元组类型和字典类型的不定长参数的形参。
传参时要进行元组和字典的拆包。
"""


def test_1(p_a, p_b, *args, **kwargs):
    return p_a + p_b + args[0] + kwargs["birthday"]


tuple_p = (3, 4, 5)
dict_p = {"birthday": 71}
test_1(1, 2, *tuple_p, **dict_p)

"""
7 函数嵌套定义和调用
python中允许在一个函数的内部定义另一个函数和调用它。
python中函数嵌套的最大实现是闭包和装饰器。
"""


def outer():
    def inner(x, y):
        return x + y

    z = inner(1, 2)
    print(z)


outer()
"""
8 python中的匿名函数lambda
python中的匿名函数为lambda。
匿名函数就是隐藏函数名即没有函数名。
匿名函数通常被认为是表达式。
匿名函数通常的用法是配合其他操作。

"""

z = lambda x, y: x + y
print(z(1, 2))  # 3

"""
9 形参和实参
形参：形式参数，在用def关键字定义函数时函数名后面括号里的变量称作为形式参数。
实参：实际参数，在调用函数时提供的值或者变量称作为实际参数。
"""

"""
10 命名空间和作用域
命名空间指的是变量存储的位置，每一个变量都需要存储到指定的命名空间当中。
python中4种命名空间：
内置名称（built - in names）， Python语言内置的名称，比如函数名和异常名称等等。
全局名称（global names），模块中定义的名称，记录了模块的变量，包括函数、类、其它导入的模块、模块级的变量和常量。
局部名称（localnames），函数中定义的名称，记录了函数的变量，包括函数的参数和局部定义的变量。类中定义的也是。
非局部名称(non - localnames)，闭包中外部非内部函数内的变量。
python中变量的作用域： 
L： local函数内部作用域。
E: enclosing闭包函数外的函数作用域。 
G: global全局作用域。 
B： build - in内置作用域。
全局变量和局部变量，通常在函数内部定义的变量称为局部变量，函数外部定义的变量称为全局变量。
函数内部修改全局变量要使用global关键字,闭包内部函数使用内部函数外的变量要使用nonlocal
"""

year = 2020


def next_year():
    global year
    year = 2021
    return year


print(next_year())  # 2021


def outer_fun():
    x = 100

    def inner_fun():
        nonlocal x
        x = 200
        return x

    return inner_fun()


print(outer_fun())

"""
11 递归函数：在函数内部，可以调用其他函数。如果一个函数在内部调用自身本身，这个函数就是递归函数。
递归函数特性：
必须有一个明确的结束条件；
每次进入更深一层递归时，问题规模相比上次递归都应有所减少
相邻两次重复之间有紧密的联系，前一次要为后一次做准备（通常前一次的输出就作为后一次的输入）。

"""


def n_sum(n):
    if n > 0:
        s = n + n_sum(n - 1)
        return s
    else:
        return 0


print(n_sum(10))


def n_multi(n):
    if n == 1:
        return 1
    else:
        return n * n_multi(n - 1)


print(n_multi(5))
