# *_* coding:utf-8 *_*
# @author:sdh
# @Time : 2021/3/16 0016 11:20
"""
集合类型：集合是无序的
交并补、差、父子
"""
set_1 = {1, 2, 3}
set_2 = {3, 4, 5}
# 1 交集
print(set_1 & set_2)
# 2 并集
print(set_1 | set_2)
# 3 差集
print(set_1 - set_2)
# 4 判断子集
print(set_1.issubset(set_2))
# 5 判断父集
print(set_1.issuperset(set_2))

# 6 使用集合对列表进行去重：
list_test = [1, 1, 2, 3, 2, 3, 1, 2]
list(set(list_test))  # [1,2,3]
