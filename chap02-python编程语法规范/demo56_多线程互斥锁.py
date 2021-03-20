# *_* coding:utf-8 *_*
# @author:sdh
# @Time : 2021/3/20 0020 21:38
"""
# 多线程中的资源精整问题
同步：协同步调，按预定的先后次序进行运行。
互斥锁：保证每次只有一个线程进行写入操作。
死锁：是指由于两个或者多个线程互相持有对方所需要的资源，导致这些线程处于等待状态，无法前往执行。


"""


import threading
import time

g_num = 0


def test01(num):
    global g_num
    mutex.acquire()
    for i in range(num):
        g_num += 1
    mutex.release()
    print("-----------------test01------ g_num=%d" % g_num)


def test02(num):
    global g_num
    mutex.acquire()
    for i in range(num):
        g_num += 1
    mutex.release()
    print("-----------------test02------ g_num=%d" % g_num)


mutex = threading.Lock()


def main():
    t1 = threading.Thread(target=test01, args=(100000,))
    t2 = threading.Thread(target=test02, args=(100000,))

    t1.start()
    t2.start()

    time.sleep(2)


main()


# 死锁的用的位置与结果的区别
#
# def test01(num):
#     global g_num
#     for i in range(num):
#         mutex.acquire()
#         g_num += 1
#         mutex.release()
#     print("-----------------test01------ g_num=%d" % g_num)
#
#
# def test02(num):
#     global g_num
#
#     for i in range(num):
#         mutex.acquire()
#         g_num += 1
#         mutex.release()
#     print("-----------------test02------ g_num=%d" % g_num)
#
#
# mutex = threading.Lock()
#
#
# def main():
#     t1 = threading.Thread(target=test01, args=(100000,))
#     t2 = threading.Thread(target=test02, args=(100000,))
#
#     t1.start()
#     t2.start()
#
#     time.sleep(2)
#
#
# main()
