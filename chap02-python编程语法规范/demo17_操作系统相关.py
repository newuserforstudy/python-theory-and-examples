# *_* coding:utf-8 *_*
# @author:sdh
# @Time : 2021/3/16 0016 13:49
import os

# 1 当前系统的名称：Windows 返回 ‘nt'; Linux 返回’posix'
print(os.name)

# 2 得到当前工作的目录
print(os.getcwd())

# 3 当前目录下所有的文件和目录名
print(os.listdir())

# 4 在当前目录下创建目录
# os.mkdir()

# 5 判断指定对象是否为文件。是返回True,否则False
os.path.isfile("")

# 6 判断指定对象是否为目录。是True,否则False。
os.path.isdir()

# 7 检验指定的对象是否存在。是True, 否则False
os.path.exists()
# 8 切分路径，返回路径的目录和文件名
os.path.split()

# 9 获得文件的大小，如果为目录，返回0
os.path.getsize()

# 10 获得绝对路径
os.path.abspath()

# 11 连接目录和文件名
os.path.join()

# 12 获取一个文件夹下所有子文件夹的名字
# 假设file_0文件夹下有3个子文件夹file_1、file_2、file_3和一些其他文件
root_dir = r"C:\Users\Administrator\Desktop\file_0"
s_dir = os.listdir(root_dir)
# ["file_1","file-2","file_3"]
print([sub_dir for sub_dir in s_dir if os.path.isdir(os.path.join(root_dir, sub_dir))])

# 13 获取一个文件夹下所有文件的名字包括子文件夹中文件的名字，名字指的是绝对路径名
file_name_list = []

def get_all_files(root_dir):
    for sub_dir_or_file in os.listdir(root_dir):
        sub_path = os.path.join(root_dir, sub_dir_or_file)
        if os.path.isdir(sub_path):
            get_all_files(sub_path)
        else:
            file_name_list.append(sub_path)


root_path = r"C:\Users\Administrator\Desktop"
get_all_files(root_path)

# 14 如何批量修改文件的后缀名
# 假设将一个文件夹下的所有xls文件转为xlsx文件。
import os


def rename_batch_files(root_dir, former_name, latter_name):
    for file_name in os.listdir(root_dir):
        file_path = os.path.join(root_dir, file_name)
        # 过滤文件夹
        if not os.path.isdir(file_path):
            prefix_suffix = os.path.splitext(file_name)
            print(prefix_suffix)
            file_ext = prefix_suffix[1]

            if former_name == file_ext:
                new_file = prefix_suffix[0] + latter_name
                os.rename(
                    os.path.join(root_dir, file_name),
                    os.path.join(root_dir, new_file)
                )


root = r"C:\Users\Administrator\Desktop\test"
rename_batch_files(root, ".xls", ".xlsx")