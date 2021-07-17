from condition_if_array_dict import split_line,split_line2
"""
input
"""
# num = input("enter current numbers for dinner:")
# num = int(num)
# if num < 8:
#     print("current number is %s" % num)
# else:
#     print("number is more than %s,sorry,no tables" % num)
split_line2()
"""
while 
"""
pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
print(pets)
while 'cat' in pets:
    pets.remove('cat')
print(pets)
split_line()

"""
7-8
"""
sandwish_ordrs = ["banana", "apple", "egg", "chicken", "dog",  "hamberger", "rice","orange"]
finish_sandwish = []
while sandwish_ordrs != []:
    tmp = sandwish_ordrs.pop()
    print("I made your %s sandwish" % tmp.title())
    finish_sandwish.append(tmp)
print(finish_sandwish)

"""
任意数量的实参,处理的是元组数据
"""
def make_pizz(*option):
    print(option)
make_pizz(1,2,3,4,5,6,7,8,9,0)
split_line()

"""
8-14 接受任意数量的键值对，内部使用字典完成
"""
def make_car(shop, type, **other):
    car = {}
    car["shop"] = shop
    car["type"] = type
    for key,value in other.items():
        car[key] = value
    return car

car = make_car("sbuaru", "outbak", color = "blue",
                    tow_packe = True,year = 15 )
print(car)
split_line2()