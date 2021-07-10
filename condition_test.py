""""
0710
列表的练习
"""
def split_line():
    print("++++++++++++分割线++++++++++++++++++++++分割线+++++++++++++++++++++分割线++++++++++++++\n")


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