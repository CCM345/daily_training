# -*- coding:utf-8 -*-

"""
生成器是一种特殊的迭代器
(1)函数中含有yield ,则是创建生成器模板
"""

def Sheng(nums):
    i = 0
    while i < nums:
        print("******************")
        ret = yield i
        print("ret %s" % ret)
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
    ret = next(s)
    print(ret)

    ret = next(s)  # 执行到yeild时，会发生返回，ret 得到的值时yeild 返回的值，函数会发生暂停了，
                   # ret = yield i 这条语句之执行了一半
    print(ret)

    ret = s.send("HAHAHA")  # 使用send 再次进行启动，进行执行，此时执行的是赋值语句，并把send的参数给传递进去，给ret
    print(ret)

    """
    总结:
    迭代器：能够让对象变得可以迭代的，保存的是数据的生成方式，能够减少内存空间的消耗
    生成器：yield能够让函数到指定的位置进行暂停，不执行后面的代码，并且下次能够继续从这个位置进行执行
    还能够通过send方法进行传参
    """
