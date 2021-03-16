# *_* coding:utf-8 *_*
# @author:sdh
# @Time : 2021/3/16 0016 20:29
"""
虚拟环境的作用：
1 方面项目管理，避免所有的安装包拥挤在一起。
2 根据需求配置package版本，防止不兼容，例如出现不同项目对某个package不同版本的需求。
虚拟环境的安装：
1 第一种方法
安装：pip install virtualenv
创建：virtualenv 虚拟环境名
进入：cd到路径 activate.bat
退出：deactivate.bat

2 第二种方法使用anaconda
创建虚拟环境: conda create -n pytorch python==3.7
使用虚拟环境: source activate pytorch
退出虚拟环境: conda deactivate
删除虚拟环境: conda remove -n pytorch --all
"""