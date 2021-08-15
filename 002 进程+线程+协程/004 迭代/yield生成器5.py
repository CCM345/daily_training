# -*- coding:utf-8 -*-

"""
生成器是一种特殊的迭代器
(1)函数中含有yield ,则是创建生成器模板
"""

def Sheng(nums):
    i = 0
    while i < nums:
        print("******************")
        yield i
        i += 1

if __name__ == "__main__":
    nums = [i**2 for i in range(10)]
    print(nums)
    """
    [0, 1, 4, 9, 16, 25, 36, 49, 64, 81] 
    """

    nums = (i ** 2 for i in range(10))
    print(nums)
    """
    <generator object <genexpr> at 0x000001C9AA3BB480> 已经变成了生成器
    """

    s = Sheng(10)  # 生成一个生成器对象
    ret = next(s)  # 让生成器往下走一步
    print(ret)     # 打印生成器的返回值，yield i 的返回值

    ret = next(s)  # 让生成器往下走一步
    print(ret)     # 打印生成器的返回值，不会从头开始执行,会从上一次的执行的结果后面
                   # 继续下一步，并yield i 的返回值

    ret = next(s)  # 打印生成器的返回值，不会从头开始执行,会从上一次的执行的结果后面，
    print(ret)     # 继续下一步，并yield i 的返回值


    ret = next(s)
    print(ret)

    ret = next(s)
    print(ret)

