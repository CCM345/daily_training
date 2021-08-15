# -*- coding: utf-8 -*-
from time import sleep
"""
如下为迭代的学习思路梳理：

（1）一个类中加入__iter__f (self) 方法后变成可迭代的
并返回如下的错误，说明是类型不正确，但是已经能够发生迭代了
    for i in A:
TypeError: iter() returned non-iterator of type 'NoneType'

（2）在此基础上增加一个新的类 class Stuends_iter():
并同时含有__iter__()h和__next__()方法

（3）在class Students():的__iter__()方法中返回一个对象
结果为 None ,并且 None是无限的循环下去，说明已经变成了可以进行迭代的，只是返回值不正确而已

（4）在（3）的基础上加上一个正确的返回值,做如下的修改
   def __next__(self):
        return "zhangsan"
    得到的结果为不是None，而是变成了zhangsan ,说明迭代的基础已经能够实现了，但是仍是无限循环的，
 (5)需要停止循环的话，就需要确定长度，如何确定长度呢？
    采用类之间的传参 
     def __iter__(self):
        return Stuends_iter(self)
        
    def __next__(self):
        # len_name = len(self.obj.nam)
        return self.obj.names[0]  
    传参的结果如下，已经能够成功打印列表中的第一个值
 (6) 获取所有传递的列表的长度
    len_name = len(self.obj.names) #获得了长度就可以用循环遍历了
    
 (7)完成循环遍历，并且判断长度，存在问题，遍历结束后，仍没有退出
     def __next__(self):
        all_len = len(self.obj.names)
        if self.nums < all_len:
            ret = self.obj.names[self.nums]
            self.nums += 1
            return ret
(8)需要想办法，让循环结束
    解决方法:加else抛出异常情况
    def __next__(self):
    all_len = len(self.obj.names)
    if self.nums < all_len:
        ret = self.obj.names[self.nums]
        self.nums += 1
        return ret
    else:
        raise StopIteration
（9）通过以上办法就实现了对象的迭代
    
"""

class Students():
    def __init__(self):
        self.names = list()
        self.len = 0

    def add(self, name):
        self.names.append(name)

    def show(self):
        print(self.names)

    def get_lst(self):
        return len(self.names)

    def __iter__(self):  # 具有本方法的对象是可迭代的
        # return Stuends_iter(self)
        return self

    def __next__(self): # 具有本方法的对象是可迭代的，加上__next__()的方法才是迭代器
        if self.len < len(self.names):
            ret = self.names[self.len]
            self.len += 1
            return ret
        else:
            raise StopIteration


# class Stuends_iter():
#
#     def __init__(self, obj):
#         self.obj = obj
#         self.nums = 0
#
#     def __iter__(self):
#         pass
#
#     def __next__(self):
#         all_len = len(self.obj.names)
#         if self.nums < all_len:
#             ret = self.obj.names[self.nums]
#             self.nums += 1
#             return ret
#         else:
#             raise StopIteration




if __name__ == "__main__":
    A = Students()
    A.add("Bob")
    A.add("Tom")
    A.add("Joe")
    A.add("Coe")

    A.add("Bob2")
    A.add("Tom2")
    A.add("Joe2")
    A.add("Coe2")

    for i in A:
        print(i)