# *_* coding:utf-8 *_*
# @author:sdh
# @Time : 2021/3/16 0016 13:11
"""
1 文件读操作
默认是文本文件的读操作。
读取文件的内容，utf-8编码。
读取文件的操作：打开open、读取内容read、readline、readlines、关闭close。
read: 读取整个文件。
readline: 读取下一行。
readlines:读取整个文件到一个迭代器以供遍历。
"""
file_name = " "
file_list = []
with open(file_name, "r", encoding="utf-8") as f:
    lines = f.readlines()
    for line in lines:
        content = line.strip()
        file_list.append(content)

"""
2 文件的写操作
默认是文本文件的读操作。
将设定的内容写入到文件中，utf-8编码。
写入文件的操作：打开open、写入内容write、writelines、关闭close。
write：写入一行字符串。
writelines：写入多行。
"""

with open(file_name, "w") as f:
    f.write("go for it")

"""
3 如何读取一个超过内存空间的超大文件
"""


# 假设计算机的内存是8G，要读取的文件时20G。
# 思路：将大文件分割成若干小文件处理，分块读取，处理完每个小文件后释放该部分内存。

def read_in_chunks(file_name, chunk_size=1024 * 1024 * 1024):
    """ chunk size: 1G"""
    while True:
        data = file_name.read(chunk_size)
        if not data:
            break
        yield data


with open('xxx.txt') as f:
    for piece in read_in_chunks(f):
        pass

from mmap import mmap


def get_lines(fp):
    with open(fp, "r+") as f:
        m = mmap(f.fileno(), 0)
        tmp = 0
        for i, char in enumerate(m):
            if char == b"\n":
                yield m[tmp:i + 1].decode()
                tmp = i + 1


for i in get_lines("fp_some_huge_file"):
    print(i)

"""
如何读取一个txt文件，read、readline、readlines有何区别，统计文件中每个字出现的频次
# 读取文件的操作：打开open、读取内容read、readline、readlines、关闭close。

# read、readline、readlines区别:
# read: 读取整个文件。
# readline: 读取下一行。
# readlines:读取整个文件到一个迭代器以供遍历。

# 统计文件中每个字出现的频次
"""

file_path = r"./test.txt"
word_counter = {}
with open(file_path, "r", encoding="utf-8") as f:
    lines = f.readlines()
    for line in lines:
        for word in line:
            word_counter[word] = word_counter.get(word, 0) + 1
