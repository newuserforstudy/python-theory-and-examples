# *_* coding:utf-8 *_*
# @author:sdh
# @Time : 2021/3/16 0016 11:08
"""
字典是可变类型，也是在数据处理中用到的最重要的数据类型。
"""
# 1 获取字典的键key、值value
dict_0 = {"name": "Chinese", "people": 14, "birthday": "10-1"}
print(dict_0.keys())
print(dict_0.values())
print(dict_0["name"])

# 2 字典的更新：
dict_0.update({"location": "Asia"})
print(dict_0)

# 3 字典的遍历
for (key, value) in dict_0.items():
    print(key, value)

# 4 字典根据键进行排序：
dict_1 = {"key1": 30, "key2": 25, "key3": 45}
print(dict(sorted(dict_1.items(), key=lambda x: x[0], reverse=False)))

# 5 字典根据值进行排序：
dict_1 = {"key1": 30, "key2": 25, "key3": 45}
print(dict(sorted(dict_1.items(), key=lambda x: x[1], reverse=False)))

# 6 字典推导式：
dict1 = {"name": 555, "age": 10}
print({v: k for k, v in dict1.items()})

# 7 将两个列表或者元组的对应位置组合成一个字典
# x = ["year","month"]
# y = [2020,7]

x = ("year", "month")
y = (2020, 7)
print(dict(zip(x, y)))

# 8 字典的get方法
print(dict1.get("name", 18))  # 获取到555,获取不到设为18

# 更多字典的操作 查看
print(dir(dict))
