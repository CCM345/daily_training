import time
import threading
import queue

"""
如下为三个单独的进程，分别执行使用
"""
def sing(times):
    for i in range(times):
        print("sing 001")
        time.sleep(1)


def dance(times):
    for i in range(times):
        print("dance 002 ")
        time.sleep(1)

def play(times):
    for i in range(times):
        print("play 003")
        time.sleep(1)


"""
进程之间共享全局变量的练习,
对一个全局变量进行不断的加操作
"""
number=0
TIMES = 100000
def add_num_10000(num):
    for i in range(num):
        thread_lock.acquire()  # 加锁操作
        global number
        number +=1
        thread_lock.release()  # 解锁操作
    print("NUM:%d" % number)

def add_num2_10000(num):
    for i in range(num):
        thread_lock.acquire()
        global number
        number +=1
        thread_lock.release()
    print("NUM:%d" % number)

def add_num3_10000(num):
    for i in range(num):
        thread_lock.acquire()
        global number
        number += 1
        thread_lock.release()
    print("NUM:%d" % number)


if __name__== "__main__":
    times = 10
    '''
    多线程的基本实现
    '''
    t1 = threading.Thread(target=sing, args=(times,))   #线程的执行顺序不确定
    t2 = threading.Thread(target=dance, args=(times,))
    t3 = threading.Thread(target=play, args=(times,))
    t1.start()  #线程的创建和线程的开始运行
    t2.start()
    t3.start()

    ''''
    多线程的同步，采用互斥锁的方式
    '''
    t4 = threading.Thread(target=add_num_10000, args=(TIMES,))
    t5 = threading.Thread(target=add_num2_10000, args=(TIMES,))
    t6 = threading.Thread(target=add_num3_10000, args=(TIMES,))

    thread_lock = threading.Lock()


    t4.start()
    t5.start()
    t6.start()

    # add_num_10000(TIMES)
    # add_num2_10000(TIMES)

    # while True:
    #     lenth = len(threading.enumerate())
    #     if lenth > 1:
    #         break
    #     print("线程数:%d" % lenth)
    #     print(threading.enumerate()) #显示当前的线程的数量
    #     print(threading.enumerate()) #显示当前的线程的数量



