# *_* coding:utf-8 *_*
# @author:sdh
# @Time : 2021/3/15 0015 12:45
import re

# 第一个参数匹配的规则，第二个参数是要匹配的字符串。
# 返回的结果使用group()获取，位置用span()获取


# 1 match :从头开始匹配,只找一次，找到即停止。

re.match(r"hello", "hello world hello China")  # hello
re.match(r"world", "hello world hello China")  # None
re.match(r"China", "hello world hello China")  # None

# 2 search:不是从头开始匹配而是在整个字符串中进行匹配，也只找一次，找到即停止。
re.search(r"hello", "hello world hello China")  # hello
re.search(r"world", "hello world hello China")  # world
re.search(r"China", "hello world hello China")  # China

# 3 finditer:在整个字符串中进行匹配，找到所有的结果,结果是一个可迭代对象。
m = re.finditer(r"hello", "hello world hello China")
# for i in m:
#     print(i)

# 4 findall: 查找到所有的字符串，放到一个列表
re.findall(r"hello\d+", "hello456hello123")  # ['hello456', 'hello123']

# 5 fullmatch： 完整匹配，需要完全满足正则规则才会有结果
re.fullmatch(r"hello word", "hello world")  # None
re.fullmatch(r"hello world", "hello world")  # hello world
re.fullmatch(r"h.*d", "hello world")  # hello world
re.fullmatch(r"h.*d", "hello xxxxx world")  # hello xxxxx world

# 6 正则修饰符
# re.S：让.匹配换行
# re.I：忽略大小写
# re.M：让$能够匹配换行
re.search(r'Y', "python", re.I)  # 不区分大小写
re.search(r'.', "a\n123", re.S)  # 能匹配到换行度
re.search(r"h.*a", "hello world\n hello China", re.S)

# 7 正则表达式规则
pattern = re.compile(r'a\d+')
pattern.findall("a12345")
# 8 标点符号的特殊含义
"""
%s: 任意的空白字符，\s、\n
%S: 任意的非空白字符
():分组
. :换行符以外的任意字符
* :0次以及以上，任意次数
+ :1次以及以上
[]:表示可选项，用来表示区间范围
| : 表示或者 
{n}:用来限制前面一个元素出现的次数,不多不少 
{，n}:用来限制前面一个元素出现的最多n次
{m,n}:用来限制前面一个元素出现m到n次
{m,}:用来限制前面一个元素出现最少m次
? :前面的元素最多出现一次、非将贪婪模式转为贪婪模式,贪婪模式是尽可能多地匹配，非贪婪尽可能少。
^ :以指定的内容开头，在[]表示取反
$ :以指定的内容结尾
数字和字母：表示其本身，没有特殊含义
"""
re.search(r"d", "abc")  # None
re.search(r"1", "234abc56")  # None
re.search(r'1+2', "1111111112")  # 1111111112
re.search(r's(ab)+', "sababab")
re.search(r's?', "sababab")
re.search(r'a{3}h', 'a12h')  # None
re.search(r'a{，3}h', 'a12h')  # a12h

print(re.search(r'a[1-5]+p', 'a12p'))  # a12p
print(re.search(r'a[1-5]+p', 'a789p'))  # None
print(re.search(r'a[1-5]+p', 'a123789p'))  # None
print(re.search(r'a[0-9]+p', 'a123789p'))  # a123789p
print(re.search(r'a[0-9a-zA-Z_]+p', 'a1237_8w_9p'))  # a1237_8w_9p

print(re.search(r'a[0-9a-zA-Z_]+p', 'a1237_8w_9p'))  # a1237_8w_9p
r = re.finditer(r'a(12|34|56)x', 'a12xa34xa56x')
for p in r:
    print(p)

print(re.search(r'^ab', 'ab123789p'))  # ab
print(re.search(r'^ab', '12378ab9p'))  # None
print(re.findall(r'a[^1-5]+x', 'a123xxa67x123xab89x'))  # ['a67x', 'ab89x']

print(re.search(r'ab$', '123ab'))  # ab
print(re.search(r'ab$', '123ab123x'))  # None

print(re.search(r'^a\d+b$', '123ab123x'))  # None
print(re.search(r'^a\d+b$', 'a123b'))  # a123b
print(re.search(r'^[^a]\d+b$', 'x123b'))  # x123b
print(re.search(r'^[^a]\d+b$', 'a123b'))  # None

# 9 字母的特殊含义
"""
\n:换行
\t:制表符
\r：回车
\s:空白字符
\S:非空白字符
\d:数字
\D:非数字
\w:数字、字母、下划线_、中文
\W:非数字、字母、下划线_、中文

"""
print(re.sub(r"\d", "T", "a123aa"))


def test(x):
    data = x.group()
    return str(int(data) * 2)


print(re.sub(r"\d+", test, "a12b12"))

