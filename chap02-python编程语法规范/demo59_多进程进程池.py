# *_* coding:utf-8 *_*
# @author:sdh
# @Time : 2021/3/21 0021 09:32

# 5 进程池

from multiprocessing import Pool


def worker(num):
    print(num)


def main():
    pool = Pool(3)

    for i in range(10):
        pool.apply_async(worker, args=(i,))

    print("----------开始--------------")
    pool.close()
    pool.join()
    print("----------结束--------------")


if __name__ == '__main__':
    main()
