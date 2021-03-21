# *_* coding:utf-8 *_*
# @author:sdh
# @Time : 2021/3/21 0021 09:18


## 1 什么是进程？
"""
进程是系统中正在运行的一个程序，程序一旦运行就是进程。
进程可以看成程序执行的一个实例。
进程是系统资源分配的独立实体，每个进程都拥有独立的地址空间。
一个进程无法访问另一个进程的变量和数据结构，如果想让一个进程访问另一个进程的资源，需要使用进程间通信，比如管道，文件，套接字等。

"""



## 2 进程的状态
"""
就绪态：等待cpu执行
执行态：cpu正在执行其功能
等待态：等待某些条件满足
杀死进程

"""



## 3 使用进程实现多任务

import multiprocessing
import time


def mut1():
    for i in range(10):
        print("--------target1---------")
        time.sleep(1)


def mut2():
    for i in range(10):
        print("--------target2---------")
        time.sleep(1)


def main():
    p1 = multiprocessing.Process(target=mut1)
    p2 = multiprocessing.Process(target=mut2)
    p1.start()
    p2.start()


if __name__ == '__main__':
    main()