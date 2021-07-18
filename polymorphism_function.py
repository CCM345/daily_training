from condition_if_array_dict import split_line,split_line2
"""
多态的学习
（1）发生在继承关系上
（2）鸭子类型实现多态（特殊的多态）
"""
class Man():

    def teach(self):
        print("man teach")

    def driver(self):
        print("man driver")

    def son(self):
        print("man son")

class Driver():
    def driver(self):
        print("driver diver")

    def father(self):
        print("diver father")

class Teacher():
    def teach(self):
        print("teacher teach")

    def son(self):
        print("teacher son")

class Demo(Man,Driver,Teacher):
    def driver(self,driver):
        driver.driver()

    def teach(self,teacher):
        teacher.teach()

    def son(self,teacher):
        teacher.son()

t = Teacher()
m = Man()
p = Demo()
p.driver(m)
p.teach(m)
p.son(t)
split_line()

class Pig():
    def jiao(self):
        print("en en en en")

class Dog():
    def jiao(self):
        print("wang wang wang wang")

class Chicken():
    def jiao(self):
        print("ge ge ge ge ")

class Cat():
    def jiao(self):
        print("miao miao miao miao")

class Demo():
    def jiao(self,a):
        a.jiao()

def duotai(a):
    a.jiao()

p = Pig()
d = Dog()
ch = Chicken()
c = Cat()

f = Demo()

f.jiao(c)
f.jiao(p)
f.jiao(ch)
f.jiao(d)
split_line()
duotai(p)
duotai(d)
duotai(ch)
duotai(c)
