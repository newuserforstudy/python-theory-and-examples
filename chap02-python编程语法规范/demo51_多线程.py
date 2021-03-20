# *_* coding:utf-8 *_*
# @author:sdh
# @Time : 2021/3/20 0020 21:23
# %% md

# 多线程的主要知识
"""
什么是多任务？
多任务是如何执行的？
什么是线程？
理解串行和并行？
为什么使用多线程？
python实现多线程的步骤？
多线程共享全局变量？
互斥锁实现全局变量？
死锁的概念？
"""

# 1 什么是多任务？
# 多任务是指用户可以在同一时间内运行多个应用程序, 每个应用程序被称作一个任务.


# 2 多任务是如何执行的？
"""
单核CPU：同一时刻只执行一个程序，时间片轮转和优先级调度，假的多任务。
多核CPU：并行(真的多任务)：CPU与任务数一致和并发(假的多任务)：CPU小于任务数，实际中多为并发。
"""

# 3 什么是线程？
"""
(1)线程也叫轻量级进程，是操作系统能够进行运算调度的最小单位，它被包涵在进程之中，是进程中的实际运作单位。
(2)线程自己不拥有系统资源，只拥有一点儿在运行中必不可少的资源，但它可与同属一个进程的其他线程共享进程所拥有的全部资源。
(3)一个线程可以创建和撤销另一个线程，同一个进程中的多个线程之间可以并发执行。
"""


# 4 串行和并行
"""
串行：单条线程来执行多个任务来说的，拿下载文件举例：当我们下载多个文件，等下载完A之后才能开始下载B，它们在时间上是不可能发生重叠的。
并行：下载多个文件，开启多条线程，多个文件同时进行下载，这里是严格意义上的，在同一时刻发生的，并行在时间上是重叠的。

"""


## 5 为什么要使用多线程？
"""
(1)线程在程序中是独立的、并发的执行流。与分隔的进程相比，进程中线程之间的隔离程度要小，它们共享内存、文件句柄和其他进程应有的状态。
(2)因为线程的划分尺度小于进程，使得多线程程序的并发性高。
(3)进程在执行过程之中拥有独立的内存单元，而多个线程共享内存，从而极大的提升了程序的运行效率。
(4)线程比进程具有更高的性能，这是由于同一个进程中的线程都有共性，多个线程共享一个进程的虚拟空间。
(5)线程的共享环境包括进程代码段、进程的共有数据等，利用这些共享的数据，线程之间很容易实现通信。
(6)操作系统在创建进程时，必须为改进程分配独立的内存空间，并分配大量的相关资源，但创建线程则简单得多。因此，使用多线程来实现并发比使用多进程的性能高得要多。

"""


## 6 python实现多线程的步骤
"""
(1)导入threading多线程模块
(2)创建需要执行任务的函数
(3)利用threading模块中的Thread类创建线程任务对象
(4)任务对象调用start()函数执行线程
"""


import threading
import time


def th1():
    for i in range(10):
        print("--------target1---------")


#         time.sleep(1)
def th2():
    for i in range(10):
        print("--------target2---------")


#         time.sleep(1)


s1 = threading.Thread(target=th1)
s2 = threading.Thread(target=th2)

s1.start()
s2.start()


# 6 怎么理解python中的多线程？
# 6.1 多线程是如何执行的？
"""
(1)python的多线程分为主线程和子线程。函数执行结束则子线程结束，主线程会等待所有子线程结束，主线程结束则整个程序结束。
(2)操作系统调度子线程和主线程，由于每个子线程的程序执行时间消耗不同，所以当子线程和主线程执行起来之后，子线程和主线程的运行没有先后顺序。
控制子线程轮流执行
time.sleep(1): 推迟调用线程的运行
"""


def thread1():
    for i in range(5):
        print("--------target1---------")
        time.sleep(1)


def thread2():
    for i in range(5):
        print("--------target2---------")
        time.sleep(1)


def main1():
    s1 = threading.Thread(target=thread1)
    s2 = threading.Thread(target=thread2)
    s1.start()
    s2.start()


main1()


# 带参数的多线程

def thd1(n):
    for i in range(n):
        print("--------target1---------")
        time.sleep(1)


def thd2(n):
    for i in range(n):
        print("--------target2---------")
        time.sleep(1)


def main1():
    s1 = threading.Thread(target=thd1, args=(5,))
    s2 = threading.Thread(target=thd2, args=(10,))
    s1.start()
    s2.start()


main1()



# 实际中的多进程: 系统自己调度
# 每个子进程任务不同，耗时不同


def threads1():
    for i in range(10):
        print("--------target1---------")


def threads2():
    for i in range(20):
        print("--------target2---------")


def main2():
    s1 = threading.Thread(target=threads1)
    s2 = threading.Thread(target=threads2)
    s1.start()
    s2.start()


main2()



