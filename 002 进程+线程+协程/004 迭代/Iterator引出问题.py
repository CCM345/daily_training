# -*- coding: utf-8 -*-

"""
演示一个类是不可以迭代的
结果存在报错信息 说明 A对象不是一个可以迭代的对象
    for i in A:
TypeError: 'Students' object is not iterable
"""

class Students():
    def __init__(self):
        self.names = list()

    def add(self, name):
        self.names.append(name)

    def show(self):
        print(self.names)




if __name__ == "__main__":
    A = Students()
    A.add("Bob")
    A.add("Tom")
    A.add("Joe")
    A.add("Coe")

    for i in A:
        print(i)

    A.show()