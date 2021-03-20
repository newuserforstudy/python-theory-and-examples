# *_* coding:utf-8 *_*
# @author:sdh
# @Time : 2021/3/20 0020 21:31
# %% md
import threading
import time
# 查看线程的数量


# %%

def thread1():
    for i in range(5):
        print("--------target1---------")
        time.sleep(1)


def thread2():
    for i in range(10):
        print("--------target2---------")
        time.sleep(1)


def main3():
    s1 = threading.Thread(target=thread1)
    s2 = threading.Thread(target=thread2)
    s1.start()
    s2.start()
    while True:
        print(threading.enumerate())
        if len(threading.enumerate()) == 1:
            break
        time.sleep(1)


main3()