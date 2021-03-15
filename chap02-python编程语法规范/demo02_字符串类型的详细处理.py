# *_* coding:utf-8 *_*
# @author:sdh
# @Time : 2021/3/15 0015 11:17
"""
字符串类型的详细处理

"""
# 0 查看python内置处理字符串的方法都有哪些
print(dir(str))
# 1 字符串的遍历
s0 = "python"
for c in s0:
    print(c)

# 2 统计字符串中某个字符出现的次数
s1 = "china make change nnnnn"
w_n_count = 0
for c in s1:
    if c == 'n':
        w_n_count += 1
print(w_n_count)

# 3 统计字符串中每个字符出现的次数
s3 = "要爱中国，爱社会，爱奉献"
from collections import Counter

element_times = dict(Counter(s3))
print(element_times)

# 4 字符串的首字母大写,其余小写
s4 = "facts speak louder than words"
print(s4.capitalize())

# 5 将字符串全部转为小写
s5 = "A Journey of A Thousand Miles Begins With One Step"
s5.lower()  # only English
s5.casefold()  # English and others

# 6 字符串以某个字符结尾(批量读取文件特别是图像文件时常用)
str_6 = "lena.jpg"
str_6.endswith(".jpg")  # True
# 7 字符串的拼接
s7 = "www."
s8 = "baidu."
s9 = "com"
# print("".join((s7, s8, s9)) ) # "www.baidu.com"

# 8 字符串的分割：
s10 = "会当凌绝顶,一览众山小"
s10.split(",")  # ['会当凌绝顶', '一览众山小']

# 9 字符串头尾空格和换行符的删除(用于文件读取)
s11 = "    会当凌绝顶,一览众山小      "
s11.strip()  # "会当凌绝顶,一览众山小"

# 10 字符串的替换
s12 = "chinese  Kungfu"
s12.replace("f", "F")  # "chinese  KungFu"
# 11 字符串的切片
s13 = "chinese  Kungfu"

print(s13[0], s13[0:1], s13[-1])  # 取收尾
print(s13[0:6])  # 切片
print(s13[::2])  # 间隔取
print(s13[::-1])  # 逆序取

# 12 字符串的首个子字符串的查找：find和index
s14 = "www.baidu.com"
s14.find("ww")  # 0
s14.index("ww")  # 0

s14.find("z")  # 找不到，返回-1
s14.index("z")  # 找不到，报错wrong
