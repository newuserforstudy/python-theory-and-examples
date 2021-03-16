# *_* coding:utf-8 *_*
# @author:sdh
# @Time : 2021/3/16 0016 19:16
import sys

import argparse

if __name__ == '__main__':
    print(sys.argv)
    parser = argparse.ArgumentParser()
    parser.add_argument('--user', type=str, help='user')
    parser.add_argument('--password', type=int, help='password')
    args = parser.parse_args()
    print(args.user)
    print(args.password)
