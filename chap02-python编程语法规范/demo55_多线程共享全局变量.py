# *_* coding:utf-8 *_*
# @author:sdh
# @Time : 2021/3/20 0020 21:35
import threading
import time
# 多线程共享全局变量

g_num = 100


def work1():
    global g_num
    for i in range(3):
        g_num += 1

    print("----in work1, g_num is %d---" % g_num)


def work2():
    global g_num
    print("----in work2, g_num is %d---" % g_num)


print("---线程创建之前g_num is %d---" % g_num)

t1 = threading.Thread(target=work1)
t1.start()

# 延时一会，保证t1线程中的事情做完
time.sleep(1)

t2 = threading.Thread(target=work2)
t2.start()

print("---线程创建之前后g_num is %d---" % g_num)
