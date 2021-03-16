# *_* coding:utf-8 *_*
# @author:sdh
# @Time : 2021/3/16 0016 18:48
"""
python中的输入和输出
输入：键盘输入内容，input函数
输出：控制台输出，print函数
"""

# 1 输入
user = input("请输出账号： ")
print(type(user))  # 输入的信息是：字符串类型,str
password = input("输出密码： ")

# 2 输出
print("hello world")  # 标准

# 格式化输出:第一种方式
print("账号：%s,密码：%s" % (user, password))
print("账号：%d,密码：%d" % (123, 456))
print("账号：%.3f,密码：%.3f" % (1.230, 4.567))

# 格式化输出:第二种方式
print("账号：{},密码：{}".format(user, password))
print("账号：{1},密码：{0}".format(password, user))

table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 8637678}
print('Jack: {Jack:d}; Sjoerd: {Sjoerd:d}; Dcab: {Dcab:d}'.format(**table))

