# *_* coding:utf-8 *_*
# @author:sdh
# @Time : 2021/3/20 0020 21:30
import threading
import time
# 控制线程的运行顺序


def thread1():
    for i in range(5):
        print("--------target1---------")


def thread2():
    for i in range(5):
        print("--------target2---------")


def main1():
    s1 = threading.Thread(target=thread1)
    s2 = threading.Thread(target=thread2)

    s1.start()
    time.sleep(1)

    s2.start()
    time.sleep(1)


main1()