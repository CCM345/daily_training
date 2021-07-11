""""
0710
列表的练习
"""
def split_line():
    print("++++++++++++分割线++++++++++++++++++++++分割线+++++++++++++++++++++分割线++++++++++++++\n")
def split_line2():
    print("$$$$$$$$$$$$分割线$$$$$$$$$$$$$$$$$$$$$$分割线$$$$$$$$$$$$$$$$$$$$$分割线$$$$$$$$$$$$$$\n")

split_line()
menu = ["Chinese", "English", "math","secience", "music", "other"]
request_menu = ["math", "music", "123"]

for request_menu in request_menu:
    if request_menu in menu:
        print("Yes,we have:%s" % request_menu)
    else:
        print("Sorry,we don't have:%s" % request_menu)
print("finish,thank you")
split_line()


""""
5-8
"""
names = ["admin", "admin1", "admin2", "admin3", "admin4", "admin5"]
for _ in names:
    # print("当前登录的用户为：%s" % _)
    if _ == "admin" or _ == "admin4":
        print("Hello %s,would you like to see a status report?" % _)
    else:
        print("Hello %s,thank you for logging in again" % _)
split_line()

""""
5-9
"""
names = ["admin", "admin1", "admin2", "admin3", "admin4", "admin5"]
names2 = []
if names2 == []:
    print("we need some users!")
else:
    for _ in names:
        # print("当前登录的用户为：%s" % _)
        if _ == "admin" or _ == "admin4":
            print("Hello %s,would you like to see a status report?" % _)
        else:
            print("Hello %s,thank you for logging in again" % _)
split_line()

"""
5-10
留下的问题:名字需要区分大小写，小写的登录后，大写的不能再进行登录
"""
current_users = ["zhang1", "zhang2", "zhang3", "zhang4", "zhang5"]
new_users = ["zhao1", "zhang1", "zhao3", "zhang5", "zhao4"]
for _ in new_users:
    if _ in current_users:
        print("name:%s 使用过" % _)
    else:
        print("name:%s 未进行使用" % _)
split_line()

"""
以下为字典的学习基础
6_1
"""
persion = {"name":"ccm", "first_name":"cheng", "last_name":"ming", "age":"20", "city":"xian","age":"25", "city":"ankang"}
print(persion["name"].title())
print(persion["first_name"])
print(persion["last_name"])
print(persion["age"])
print(persion["city"].title())
split_line()

"""
循环遍历
打印key value
"""
for key, value in persion.items():
    print("\nkey:" + key.title())
    print("value:" + value.title())
split_line()

"""
打印KEY
"""
for key in persion.keys():  #等价于 for key in persion:
    print("key:" + key.title()) #大写
split_line()

"""
打印值
"""
for value in persion.values():
    print("values:" + value.title())
split_line()

"""
排序打印建
"""
for key in sorted(persion.keys()):
    print("after Sorted key:" + key.title())
split_line()

"""
去除字典中的重复的字段
"""
for key in set(persion.keys()):
    print("去重复key:" + key.title())
split_line()
"""
6-5 练习题
"""
rivers = {"shanxi":"xian", "hubei":"wuhan", "guangdong":"guanzhou", "zhejiang":"hangzhou"}
for key,  value in rivers.items():
    print("The " + key.title() + "provience's city is " + value.title())
split_line()
for key in rivers.keys():
    print("key:" + key.title())
split_line()
for value in rivers.values():
    print("value:" + value.title())
split_line()
