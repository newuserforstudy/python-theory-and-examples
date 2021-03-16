# *_* coding:utf-8 *_*
# @author:sdh
# @Time : 2021/3/16 0016 12:11

# 0顺序结构

# 1 分支语句
# python中的分支语句只有if语句。
# if语句有单分支、二分支、多分支。
# 配合if语句的关键字有else、elif。
# 1.1 单分支if语句

x = float(input("输入一个数:"))
if x > 5:
    print("这是个大于5的数")
# 1.2 二分支if语句

x = float(input("输入一个数："))
if x > 5:
    print("这是个大于5的数")
else:
    print("这是个不大于5的数")
# 1.3 多分支语句

x = float(input("输入一个数："))
if x > 5:
    print("这是个大于5的数")
elif x > 3:
    print("这是个大于3小于等于5的数")
else:
    print("这是个不于等于3的数")

# 2 while循环语句
# while循环配合if语句、break关键字、continue关键字、True关键字、False关键字使用。
# while循环每次判断循条件。
# break：终止循环。
# continue：跳过本次循环进入下一个循环。
while True:
    x = input("输入一个字符：")
    if x == "q":
        break
    elif x == "p":
        continue
    else:
        print("啥也不是")
# 3 for循环语句
# for 循环必须配合关键字in使用。
# for循环可以进行嵌套使用。
# for循环中也可使用break、continue。
# for循环中也可配合if语句。
for i in range(10):
    if i % 2 == 0:
        print("%d 是偶数" % i)
    else:
        print("%d 是奇数" % i)

for i in range(10):
    for j in range(10):
        if i * j == 16:
            print(i, j)
