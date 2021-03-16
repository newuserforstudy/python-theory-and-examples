# *_* coding:utf-8 *_*
# @author:sdh
# @Time : 2021/3/16 0016 12:58
"""
1 错误、警告与异常
错误：语法错误和逻辑错误，语法错误导致程序不能正常执行，逻辑错误使得程序不能达到预期效果。
警告：当代码不能满足某种标准时的提示，警告不会影响程序的正常执行。
异常：在程序执行过程中发生，导致程序正常执行，原因可能是写程序时考虑不周也可能是无法考虑全面。
"""

"""
2 python异常的捕获
常见的异常：IOError、IndexError、MemoryError、RuntimeError、SyntaxError、TypeError、ValueError等。
异常处理的格式。
try捕获代码中异常，有异常则使用except进行捕获不再到else内执行，没有异常则执行try内的语句，程序跳到else语句继续进行，最后到finally中执行结束。

"""

def add_one(x):
    try:
        x += 1
    except IndexError as e1:
        print(e1)
    except KeyError as e2:
        print(e2)
    except ValueError as e3:
        print(e3)
    else:
        x += 1
        print('try内没有异常')
    finally:
        x += 1
        print('无论异常与否都会执行!')

    return x


print(add_one(1))  # 4
"""
3 抛出捕获的异常
抛出异常使用raise关键字。
捕获自己抛出的异常。

"""

def raise_exception(index, x=None):
    if x is None:
        x = [0, 1, 2, 3, 4]
    try:

        if index == 5:
            # 抛出异常之后，调到except进行捕获
            raise IndexError("超出索引范围xxx")
        print("没有捕获异常")

    except Exception as e:
        index -= 1
        # e 超出索引范围xxx
        print(e)

    # try内有异常则不执行
    else:
        print(index)
    # except执行完或者else执行完，最终都会跳至finally
    finally:
        return x[index]


print(raise_exception(5))