# -*- coding:utf-8 -*-

"""
yield 实现并发
"""
import time
COUNT = 10

def test_1(count):
    for i in range(count):
        print("******test1**********")
        time.sleep(1)
        yield

def test_2(count):
    for i in range(count):
        print("@@@@@@test2@@@@@@@@@")
        time.sleep(1)
        yield

def test_3(count):
    for i in range(count):
        print("!!!!!!test3!!!!!!!!!")
        time.sleep(1)
        yield

def main():
    t1 = test_1(COUNT)
    t2 = test_2(COUNT)
    t3 = test_3(COUNT)
    while True:
        next(t1)
        next(t2)
        next(t3)


if __name__ == "__main__":
    main()


