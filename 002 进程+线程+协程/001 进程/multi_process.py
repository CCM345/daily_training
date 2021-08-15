import multiprocessing
import time
import os
#可以发布文章
'''
多进程的练习
进程之间的资源是单独的，不会进行共享全局的信息
'''
number = 0
TIMES = 100000000
def test1(num):
    for i in range(num):
        global number
        number += 1
    print("number1:%d" % number)

def test2(num):
    for i in range(num):
        global number
        number += 1
    print("number2:%d" % number)

def test3(num):
    for i in range(num):
        global number
        number += 1
    print("number2:%d" % number)

"""
线程与进程对比：
线程是CPU的执行最小单元 ，消耗资源少
进程是资源分配的最小单元，消耗资源多，资源会全部进行复制一份
"""


if __name__ == "__main__":
    print("多进程练习的开始")
    print("PID:%d" % os.getpid())
    p1 = multiprocessing.Process(target=test1, args=(TIMES,))
    p2 = multiprocessing.Process(target=test2, args=(TIMES,))
    p3 = multiprocessing.Process(target=test3, args=(TIMES,))

    p1.start()
    p2.start()
    p3.start()