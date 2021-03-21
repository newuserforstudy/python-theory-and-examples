# *_* coding:utf-8 *_*
# @author:sdh
# @Time : 2021/3/21 0021 09:55
"""
协程，又称作Coroutine。从字面上来理解，即协同运行的例程，它是比线程（thread）更细量级的用户态线程，
特点是允许用户的主动调用和主动退出，
挂起当前的例程然后返回值或去执行其他任务，接着返回原来停下的点继续执行。
等下，这是否有点奇怪？我们都知道一般函数都是线性执行的，不可能说执行到一半返回，等会儿又跑到原来的地方继续执行。
但一些熟悉python（or其他动态语言）的童鞋都知道这可以做到，答案是用yield语句。
其实这里操作系统具有getcontext和swapcontext这些特性，通过系统调用，可以把上下文和状态保存起来，切换到其他的上下文，
这些特性为coroutine的实现提供了底层的基础。

"""

# 7 python实现协程
# 最简单的协程实现 gevent

"""
gevent是第三方库，通过greenlet实现协程，其基本思想是：
当一个greenlet遇到IO操作时，比如访问网络，就自动切换到其他的greenlet，等到IO操作完成，
再在适当的时候切换回来继续执行。由于IO操作非常耗时，经常使程序处于等待状态，
有了gevent为我们自动切换协程，就保证总有greenlet在运行，而不是等待IO。
由于切换是在IO操作时自动完成，所以gevent需要修改Python自带的一些标准库，
这一过程在启动时通过monkey patch完成.
"""

from gevent import monkey
import gevent
import random
import time

# 有耗时操作时需要
monkey.patch_all()  # 将程序中用到的耗时操作的代码，换为gevent中自己实现的模块


def coroutine_work(coroutine_name):
    for i in range(10):
        print(coroutine_name, i)
        time.sleep(random.random())


gevent.joinall([
        gevent.spawn(coroutine_work, "work1"),
        gevent.spawn(coroutine_work, "work2")
])
