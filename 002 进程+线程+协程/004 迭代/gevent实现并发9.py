# -*- coding:utf-8 -*-

"""
gevent的携程的实现
利用了等待耗时的时间，等待的时间可以腾出来做别的事情
如果没有等待时间，则还是按照函数的执行的流程进行执行
"""
import time
import gevent
COUNT = 100
WAIT_TIME = 0.5

def test_1(count):
    for i in range(count):
        print(f"*{i}*****test1**********")
        # time.sleep(WAIT_TIME)  # 普通的等待时间，对于携程的等待时间不生效
        gevent.sleep(WAIT_TIME)  # 真正的携程的的等待的时间

def test_2(count):
    for i in range(count):
        print(f"@{i}@@@@@test2@@@@@@@@@")
        # time.sleep(WAIT_TIME) # 普通的等待时间，对于携程的等待时间不生效
        gevent.sleep(WAIT_TIME)

def test_3(count):
    for i in range(count):
        print(f"#{i}######test2########")
        # time.sleep(WAIT_TIME)
        gevent.sleep(WAIT_TIME)



if __name__ == "__main__":
    g1 = gevent.spawn(test_1, COUNT)
    g2 = gevent.spawn(test_2, COUNT)
    g3 = gevent.spawn(test_3, COUNT)

    g1.join()
    g2.join()
    g3.join()


