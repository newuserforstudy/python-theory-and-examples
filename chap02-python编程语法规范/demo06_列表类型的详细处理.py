# *_* coding:utf-8 *_*
# @author:sdh
# @Time : 2021/3/16 0016 10:32
"""
列表类型：
追加、合并、插入、删除、查找、统计、切片、遍历、排序

"""
# 1 列表中元素的追加：
list_0 = [1, 2, 3, 4]
list_0.append(5)
print(list_0)  # [1, 2, 3, 4,5]

# 2 列表中追加另一个列表：
list_0.append([5, 6, 7])
print(list_0)  # [1, 2, 3, 4, 5, [5, 6, 7]]

# 3 列表中的元素插入：
list_1 = [1, 2, 3, 4]
list_1.insert(0, 100)  # 在第0个位置插入100
print(list_1)

# 4 列表中元素的删除：
list_2 = [1, 1, 1, 2, 3, 4]
list_2.remove(1)  # 刪除1,多个值删除第一个
print(list_2)

# 5 列表中获取元素的索引：
list_2 = [1, 1, 2, 3, 4]
print(list_2.index(1))  # 索引值为0,返回第一个

# 6 统计列表某个元素出现的次数：
list_2 = [1, 1, 2, 3, 4, 1]
print(list_2.count(1))  # 3

# 7 列表的切片，取指定范围的元素：
list_3 = [1, 2, 3, 4]
# list_3[::] # [1,2,3,4]
# list_3[-3:-1] # [2,3]
# list_3[-3:] # [2,3,4]
# list_4 = [1,2,3,4,5,6,7,8,9]
# list_4[0:10:2] # 1,3,5,7,9
# list_4[::2] # 1,3,5,7,9

# 8 列表的逆序或翻转
list_5 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# list_5.reverse() # [9,8,7,6,5,4,3,2,1]
# list_5[::-1] # [9,8,7,6,5,4,3,2,1]

# 9 列表的遍历
list_6 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
list_temp = []
for i in list_6:
    if i % 2 == 1:
        list_temp.append(i)

# 10 列表的不变序去重：
list_7 = [1, 1, 1, 1, 2, 2, 3, 3, 3]
list_temp1 = []
for i in list_7:
    if i not in list_temp1:
        list_temp1.append(i)

# 11 列表的遍历删除：用3种方法
list_4 = [1, 1, 1, 1, 2, 2, 3, 3, 3]
# 第一种方法：逆序遍历
for i in range(len(list_4) - 1, -1, -1):
    if list_4[i] == 1:
        list_4.remove(list_4[i])
print(list_4)  # [2,2,3,3,3]

# 第二种方法：列表推导式
print([i for i in list_4 if i != 1])  # [2,2,3,3,3]

# 第三种方法：filter过滤器和匿名函数lambda
list(filter(lambda x: x != 1, list_4))  # [2,2,3,3,3]

# 12 列表中元素的排序：
list_8 = [1, 3, 2, 5, 7, 6, 8, 9, 0]
list_8.sort()  # [0,1,2,3,4,5,6,7,8,9]
sorted(list_8, reverse=False)  # [0,1,2,3,4,5,6,7,8,9]
sorted(list_8, reverse=True)  # [[9, 8, 7, 6, 5, 3, 2, 1, 0]]

# 13 合并两个列表
lost_01 = [1, 2, 3]
lost_02 = [4, 5, 6]
print(lost_01 + lost_02)  # [1, 2, 3, 4, 5, 6]

# 14 两个列表对应元素运算(列表元素长度相同)
t = []
for i, j in zip([1, 2, 3], [4, 5, 6]):
    t.append(i + j)
print(t)
