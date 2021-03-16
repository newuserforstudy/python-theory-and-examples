# *_* coding:utf-8 *_*
# @author:sdh
# @Time : 2021/3/16 0016 11:24
# 1 一个列表中的元素全部是字典，根据字典的键将列表进行排序
list_0 = [{"x": 20}, {"x": 10}, {"x": 30}]
sorted(list_0, key=lambda t: t["x"], reverse=True)  # [{'x': 30}, {'x': 20}, {'x': 10}]

list_1 = [{"x1": 20, "y1": 15}, {"x1": 30, "y1": 5}, {"x1": 10, "y1": 10}]
sorted(list_1, key=lambda t: t["y1"])

# 2 一个列表中的元素全部是字符串，找到最长和最短的字符串
list_2 = ["python", "java", "JavaScript", "matlab"]
max_len_str = max(list_2, key=len, default="")
min_len_str = min(list_2, key=len, default="")
print(max_len_str, min_len_str)

# 3 对嵌套列表按照指定维度进行排序。
# 假设根据方程y = 3*x + 2，采样坐标。根据y的值对坐标从大到小排序。
p = [[2, 8], [1, 5], [4, 14], [3, 11]]
sorted(p, key=lambda x: x[1], reverse=True)
