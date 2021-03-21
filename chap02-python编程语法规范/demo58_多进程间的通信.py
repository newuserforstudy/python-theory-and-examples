# *_* coding:utf-8 *_*
# @author:sdh
# @Time : 2021/3/21 0021 09:27

# 进程间的通信 ：队列Queue

import multiprocessing
from multiprocessing import Queue

# 进程中数据相关
q = Queue(3)
q.put("11")
q.put(100)
q.put([1, 2, 3])

q.full()

q.get()

q.empty()


#  多进程间通过队列进行通信
# 多进程的实现与调用要在__main__中

def down_from_web(q):
    data = [11, 22, 33, 44]
    for i in data:
        q.put(i)

    print("download over!")


def analysis_data(q):
    wait_list = []
    while True:
        data = q.get()
        wait_list.append(data)
        if q.empty():
            break

    print(wait_list)


def main():
    q = Queue()
    p1 = multiprocessing.Process(target=down_from_web, args=(q,))
    p2 = multiprocessing.Process(target=analysis_data, args=(q,))

    p1.start()
    p2.start()


if __name__ == '__main__':
    main()
