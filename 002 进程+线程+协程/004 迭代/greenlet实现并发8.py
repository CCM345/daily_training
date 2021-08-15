# -*- coding:utf-8 -*-

"""
greenlet 实现并发
"""
import time
from greenlet import greenlet
COUNT = 10

def test_1():
    while True:
        print("******test1**********")
        time.sleep(1)
        gr2.switch()

def test_2():
    while True:
        print("@@@@@@test2@@@@@@@@@")
        time.sleep(1)
        gr1.switch()


if __name__ == "__main__":
    gr1 = greenlet(test_1)
    gr2 = greenlet(test_2)

    gr2.switch()


