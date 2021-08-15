# -*- coding:utf-8 -*-

"""
gevent的携程的实现
利用了等待耗时的时间，等待的时间可以腾出来做别的事情
如果没有等待时间，则还是按照函数的执行的流程进行执行
"""
import time
import gevent
from gevent import monkey
from time import sleep
COUNT = 10000
WAIT_TIME = 1

monkey.patch_all()
#打上sleep的补丁，能够完成time.sleep的补丁，不用实现time的替换，较少替换
#说明：该替换只针对time.sleep（）生效，不会对别的生效

def test_1(count):
    for i in range(count):
        print(f"*{i}*****test1**********")
        time.sleep(WAIT_TIME)  # 普通的等待时间，对于携程的等待时间不生效
        # gevent.sleep(WAIT_TIME)  # 真正的携程的的等待的时间

def test_2(count):
    for i in range(count):
        print(f"@{i}@@@@@test2@@@@@@@@@")
        time.sleep(WAIT_TIME) # 普通的等待时间，对于携程的等待时间不生效
        # gevent.sleep(WAIT_TIME)

def test_3(count):
    for i in range(count):
        print(f"#{i}######test3########")
        time.sleep(WAIT_TIME)
        # gevent.sleep(WAIT_TIME)

def test_4(count):
    for i in range(count):
        print(f"%{i}%%%%%test4%%%%%%%")
        time.sleep(WAIT_TIME)
        # gevent.sleep(WAIT_TIME)



if __name__ == "__main__":
    # g1 = gevent.spawn(test_1, COUNT)
    # g2 = gevent.spawn(test_2, COUNT)
    # g3 = gevent.spawn(test_3, COUNT)
    #
    # g1.join()
    # g2.join()
    # g3.join()

    #如下为最改进的版本
    gevent.joinall(
        [
            gevent.spawn(test_1, COUNT),
            gevent.spawn(test_2, COUNT),
            gevent.spawn(test_3, COUNT),
            gevent.spawn(test_4, COUNT),


         ]
    )


