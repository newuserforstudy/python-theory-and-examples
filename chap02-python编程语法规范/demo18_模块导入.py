# *_* coding:utf-8 *_*
# @author:sdh
# @Time : 2021/3/16 0016 18:09
"""
1 项目、包和模块
项目：project，一般包含程序文件和数据文件或文件夹等。
包：package，包含一个_init_文件。

模块：module，一个python文件就是一个模块。

"""
"""
2 导入包和模块
通常使用pip install 的工具箱是包。
导入包使用import。
"""

import numpy
# 导入包并且起别名。

# import numpy as np
# 3 导入包或者模块内的函数、变量、类等。
from torchvision import transforms as tf
from torch.optim import adam as ad

# 4 从同级模块中导入函数、类等
from .demo17_操作系统相关 import rename_batch_files

# 5 从子包中导入
# from . import xx
# from .. import yy
# from ..mmmm import zzzz

# 6 在本模块中执行但是希望执行代码被其他模块调用，使用__main__封闭起来

if __name__ == '__main__':
    # 这段代码只在本文件执行，不会被外界使用
    a = 1
    print(a)
