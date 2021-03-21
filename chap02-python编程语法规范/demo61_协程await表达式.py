# *_* coding:utf-8 *_*
# @author:sdh
# @Time : 2021/3/21 0021 10:00
"""
python内部的协程实现机制：await和yield

"""


# 1. 普通函数
def function():
    return 1


# 2. 生成器函数
def generator():
    yield 1


# 在3.5过后，我们可以使用async修饰将普通函数和生成器函数包装成异步函数和异步生成器。
# 3 异步函数-协程
async def coroutine():
    return 1


# 4 异步生成器
async def async_gen():
    yield 1


import types

print(type(function) is types.FunctionType)
print(type(generator()) is types.GeneratorType)
print(type(coroutine()) is types.CoroutineType)
print(type(async_gen()) is types.AsyncGeneratorType)


# 在协程函数中，可以通过await语法来挂起自身的协程，并等待另一个协程完成直到返回结果
def run(coroutine_):
    try:
        coroutine_.send(None)
    except StopIteration as e:
        return e.value


# 协程函数
async def async_function():
    return 1


# 协程函数
async def await_coroutine():
    result = await async_function()
    print(result)


run(await_coroutine())
