from condition_if_array_dict import split_line,split_line2

split_line()

"""
创建一个类
"""
class Dog():
    """
    一次模拟小狗的简单尝试
    """
    def __init__(self, name, age):
        """
        初始化属性
        :param name:
        :param age:
        """
        self.name = name
        self.age = age

    def sit(self):
        """
        模拟蹲下的动作
        :return:
        """
        print(self.name.title() + " is sit down now")

    def roll_over(self):
        """
        模拟打滚的动作
        :return:
        """
        print(self.name.title() + " is roll_over now")

my_dog = Dog("小白", 3)
my_dog2 =  Dog("小黑", 4)
print("My dog name is :%s" % my_dog.name)
print("My dog age is :%d" % my_dog.age)
my_dog.sit()
my_dog.roll_over()
split_line2()

print("My dog name is :%s" % my_dog2.name)
print("My dog age is :%d" % my_dog2.age)
my_dog2.sit()
my_dog2.roll_over()
split_line2()

"""
9-1 餐馆类
"""
class Restuarant():
    def __init__(self,re_name,cu_name):
        self.rename = re_name
        self.cuname = cu_name
        self.current_number_served = 0
        self.max_number_served = 0

    def describe_retuarant(self):
        print("re_name:%s" % self.rename)
        print("cu_name:%s" % self.cuname)

    def open_retuarant(self):
        print("opening")

    def print_number_served(self):
        print("current_number_srved:%d" % (self.current_number_served))

    def set_max_number_served(self, number):
        self.max_number_served = self.max_number_served + number
        print("now max_number_served: %d " % self.max_number_served)

    def incremen_number_served(self, number):
        if (self.current_number_served + number >  self.max_number_served):
            print("too many,can't increment")
        else:
            self.current_number_served = self.max_number_served + number
            print("increment %d success" % number)



re1 = Restuarant("hao","zailai")
print(re1.rename)
print(re1.cuname)

re1.describe_retuarant()
re1.open_retuarant()

re1.set_max_number_served(20)
re1.incremen_number_served(10)
re1.incremen_number_served(1)




"""
9-3 用户类
"""

class User():
    def __init__(self,first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def describe_user(self):
        print("describe_user,name:%s %s" % (self.first_name, self.last_name))

    def greet_user(self):
        print("Hi %s%s,nice to meet you" % (self.first_name, self.last_name))

person1 = User("张", "三")
person2 = User("李", "四")
person3 = User("王", "二")

# person1.describe_user()
# person1.greet_user()
# split_line2()
# person2.describe_user()
# person2.greet_user()
# split_line2()
# person3.describe_user()
# person3.greet_user()
split_line2()
class Car():
    def __init__(self, source, model, year):
        self.source = source
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def describe_car(self):
        print("source:%s" % self.source)
        print("model:%s" % self.model)
        print("year:%s" % self.year)

    def update_odometer_reading(self,number):
        self.odometer_reading = self.odometer_reading + number
        print("after update odometer_rading is %d" % (self.odometer_reading))

car1 = Car("China", "aodi", 2020)
car1.describe_car()
car1.update_odometer_reading(12)
split_line2()

"""
面向对象的学习
"""
class Cat():
    """
    成员变量格式一
    """
    country = "China"  # 类变量，并非创建所有的对象时，才有的
    def __init__(self):
        self.type = "bosi"
        self.name = "xiaobai"
        self.clour = None

    """
    成员方法调用成员方法，加self
    """
    def catch(self):
        print("catch1")
        self.jump()
        self.grasp()
        self.introduce()

    def introduce(self):
        print("introduce %s %s" % (self.type,self.name))

    def jump(self):
        print("jump")

    def grasp(self):
        print("grasp")

    def __str__(self):
        return "str打印了对象"

cat1 = Cat()
cat1.catch()
cat1.country = "Japan"
print(cat1.country)
print(Cat.country)  ##使用类的方法调用
split_line2()

""""
手机充电的例子
"""
class Phone():
    def __init__(self):
        self.power = 100

    def game(self):
        if (self.power < 10):
            print("power is less than 10,不能操作")
        else:
            self.power = self.power - 10
            print("doing game,power 减少 10")

    def music(self):
        if (self.power < 5):
            print("power is less than 5,不能操作")
        else:
            self.power = self.power - 5
            print("doing music,power 减少 5")

    def call(self):
        if (self.power < 3):
            print("power is less than 3,不能操作")
        else:
            self.power = self.power - 3
            print("doing call,power 减少 3")

    def answer(self):
        if (self.power < 4):
            print("power is less than 5,不能操作")
        else:
            self.power = self.power - 4
            print("doing answer,power 减少 4")

    def charge(self,number):
        if (self.power + number > 100):
            print("full,charge power failure")
        else:
            self.power = self.power + number
            print("doing charge,power 增加 %d" % (number))

    def play(self):
        self.charge(20)
        self.game()
        self.music()
        self.call()
        self.answer()

    def __str__(self):
        return "current power:%d" % (self.power)

p = Phone()
p.play()
print(p)
split_line2()
"""
封装的练习
"""

class Card():
    def __init__(self):
        self.__id = None
        self.__pwd = None

    def set_id(self, id):
        self.__id = id

    def get_id(self):
        return self.__id

    def set_pwd(self,pwd):
        self.__pwd = pwd

    def get_pwd(self):
        return self.__pwd

    @classmethod  #类方法
    def ac(cls):
        print("this is classmethod")

    def a2(self):
        print("ac meth")

    @staticmethod #类方法（静态的方法，常用做函数使用
    def show():
        print("this is static")

card1 = Card()
card1.set_id(123456)
card1.set_pwd("123")
print(card1.get_id())
print(card1.get_pwd())
card1.ac()
Card.ac()
card1.show()
Card.show()
split_line()

"""
继承的练习
+ 
"""
class GrandFather():
    def __init__(self):
        pass

    def sing(self):
        print("grand father sing")

    def play(self):
        print("grand father play")

class Father():
    def __init__(self):
        self.first_name = "F"
        self.age =  None
        self.__id = "id"
        # print("father __init__")

    def sing(self):
        print("father bad sing")

    def play(self):
        print("father good play")




class Mother():
    def __init__(self):
        self.last_name = "M"
        self.clour = None

    def sing(self):
        print("father good sing")

    def play(self):
        print("father bad play")




class Child(Mother, Father,GrandFather):
    def __init__(self):
        # print("Child __init__")
        # super().__init__()
        pass
    def sing(self):
        Mother.sing(self)
        GrandFather.sing(self)

    def play(self):
        Father.play(self)
        GrandFather.play(self)
        GrandFather.play(self)


c = Child()
c.sing()
c.play()
print(Child.__mro__)
split_line()
