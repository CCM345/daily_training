import multiprocessing
from multiprocessing import Queue
import time
import os
'''
多进程的练习
进程之间的资源是单独的，不会进行共享全局的信息
'''
number = 0
TIMES = 15
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
进程是资源分配的最小单元，消耗资源多，资源会全部进行复制一份,相互之间是独立的
"""

'''
进程间通信：
例如：socket，文件，
'''

"""
一个进程写数据
"""
def write_data(num, queue):
    for i in range(num):
        num_lst = list()
        num_lst.append(i)
        if queue.full():
            print("queue is full")
            break
        else:
            queue.put(num_lst)

"""
一个进程读取数据  进程间通信完成数据的通信
"""
def read_data(num, queue):
    wait_ing_lst = list()
    for i in range(num):
        data = queue.get()
        wait_ing_lst.append(data)
        print(wait_ing_lst)

        if queue.empty():
            break



if __name__ == "__main__":
    print("多进程练习的开始")
    print("PID:%d" % os.getpid())
    p1 = multiprocessing.Process(target=test1, args=(TIMES,))
    p2 = multiprocessing.Process(target=test2, args=(TIMES,))
    p3 = multiprocessing.Process(target=test3, args=(TIMES,))

    p1.start()
    p2.start()
    p3.start()

    q = multiprocessing.Queue()  # 产生一个队列，并注明队列里面的值的大小，未写就是默认

    p4 = multiprocessing.Process(target=write_data, args=(TIMES, q))
    p5 = multiprocessing.Process(target=read_data, args=(TIMES, q))

    p4.start()
    p5.start()

