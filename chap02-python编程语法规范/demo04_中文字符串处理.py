# *_* coding:utf-8 *_*
# @author:sdh
# @Time : 2021/3/15 0015 16:54
"""
python 中文 字符串的处理
设置coding:utf-8或者coding=utf-8
"""
# 1 中文繁体转为简体
# 中文繁体转小写
# 第一种方法：安装opencc-python
from opencc import OpenCC

s = "壹夫作難而七廟隳，身死人手，為天下笑者，何也？仁義不施而攻守之勢異也。"
r = OpenCC("t2s").convert(s)
print(r)


# 2 判断字符串中是否有中文
def there_is_chinese(sentence):
    for char in sentence:
        if "\u4e00" <= char <= "\u9fa5":
            return True

    return False


# 3 判断中文字符串中是否包含英文
def there_is_english(sentence):
    import re
    res = re.search(r"[a-zA-Z]", sentence)
    if res:
        return True
    else:
        return False

