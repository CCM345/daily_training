# coding=utf-8

import re
RULES = "HELLO WORD!,"
RULES_PYTHON = "python3"
RULES_ABCDEF = "pythonF"
RULES_abcedf = "pythonabcdef"
RULES_W = "python#####"

# 匹配单个字符  []  匹配其中的一位数字



def sangle_word():
    ret = re.match(r"[H]ELLO", RULES)
    print(ret)

    ret = re.match("python[\d]", RULES_PYTHON)  # 匹配单个的数字
    print("python[\d]")

    ret = re.match("python[3]", RULES_PYTHON)
    print("python[3]")

    ret = re.match("python[1-3]", RULES_PYTHON)
    print("python[1-3]")

    ret = re.match("python[1-23-6]", RULES_PYTHON)  # 匹配其中的一位
    print("python[1-23-6]")

    ret = re.match("python[A]", RULES_ABCDEF)
    print("python[A]")

    ret = re.match("python[A-H]", RULES_ABCDEF)  # 匹配大写字符
    print(ret)

    ret = re.match("python[a]", RULES_abcedf)  # 匹配小写字符
    print(ret)

    ret = re.match("python[\w]", RULES_ABCDEF)  # \w 匹配 字母 数字下划线  变量的定义
    # 包含了汉字
    print(ret)

    ret = re.match("python[\W]", RULES_W)  # \w 匹配 字母 数字下划线  变量的定义 的补集  ··
    print(ret)



# 匹配多个字符
RE_123456789 = "RE_1234567890"
RE_ABCDEFGHIJK = "RE_ABCDEFGHIJK"
RE_SS_ABCDEFGHIJK = "RE_AB#CDE@@FGHIJK RE_aa！！aaaaa YYY:YYY%YY KKKKK66^777788()99 python = 123,c = 456, C++ = 789"

def multi_words():
    ret = re.match("RE_\d{10}", RE_123456789)  # 匹配一个字符10次
    print(ret)
    print("RE_\d{10}")

    ret = re.match("RE_\d{3}", RE_123456789)  # 匹配一个字符3次
    print(ret)
    print("RE_\d{3}")

    ret = re.match("RE_\d{3,5}", RE_123456789)  # 匹配一个字符5次
    print(ret)
    print("RE_\d{3,5}")

    ret = re.match("RE_.\d{3,5}", RE_123456789)  # 匹配任意的字符
    print(ret)
    print("RE_.\d{3,5}")

    ret = re.match("RE_?\d{3,5}", RE_123456789)  # 匹配？前面的一个字符出现1次或者不出现
    print(ret)
    print("RE_?\d{3,5}")

    ret = re.match("RE_*\d{3,8}", RE_123456789)  # 匹配*前面的一个字符出现0次或者无限制次数
    print(ret)
    print("RE_*\d{3,8}")

    ret = re.match("RE_+\d{2,9}", RE_123456789)  # 匹配+前面的一个字符出现1次或者无线次数，
    # 至少有一次
    print(ret)
    print("RE_+\d{2,9}")


def name():
    names = ["_", "1", "a", "A", "99cong", "name", "name1", "n你好me1", "name!", "age@", "__123", "!name", "**name", "cheng99"]

    for i in names:
        if re.match("[a-zA-Z_][a-zA-Z_0-9]*$", i):  # 匹配变量名
            print(f"{i}:是变量名")
        else:
            print(f"{i}:不是变量名")

# 判断字符串的开始和结尾
# ^ 表示开始
# $ 表示结束
# 取到正则里面得到分组 （ab）里面的内容就称为分组
# \num  得到分组中的字符串的结果


def email():
    email = ["123@qq.com","1234@163.com", "cheng123@.qqxx.com", "cheng__@tenda.com", "yyy@google.com"]

    for i in email:
        ret = re.match("^([a-zA-Z0-9]{2,20})@(163|qq)\.(com)$", i)  # 去到里面的具体的分组
        if ret:
            print(f"{i}:是正确的邮箱地址,分组:{ret.group(1)},{ret.group(2)},{ret.group(3)}")
        else:
            print(f"{i}:是不正确的邮箱地址")

    # for i in email:
    #     ret = re.match("^([a-zA-Z0-9]{2,20})@(163|qq)\.(com)$", i)  # 去到里面的具体的分组
    #     if ret:
    #         print(f"{i}:是正确的邮箱地址,分组:{ret.group(1)},{ret.group(2)},{ret.group(3)}")
    #     else:
    #         print(f"{i}:是不正确的邮箱地址")

def search():
    ret = re.search("\d+",RE_123456789)
    print(ret)

def findall():
    ret = re.findall("\d+", RE_SS_ABCDEFGHIJK) # 提前字符串中的所有满足条件的字符
    print(ret)

    ret = re.findall("\w+", RE_SS_ABCDEFGHIJK)  # 提前字符串中的所有满足条件的字符
    print(ret)

    ret = re.findall("\W+", RE_SS_ABCDEFGHIJK)  # 提前字符串中的所有满足条件的字符
    print(ret)

def sub():
    ret = re.sub("\d+","PYTHON", RE_SS_ABCDEFGHIJK)
    print(ret)

    ret = re.sub("\W+", "PYTHON", "python==666")  # 替换当中的==为PYTHON
    print(ret)


def split():
    ret = re.split(" ",RE_SS_ABCDEFGHIJK)
    print(ret)

    ret = re.split("#", RE_SS_ABCDEFGHIJK)
    print(ret)

    ret = re.split(":", RE_SS_ABCDEFGHIJK)
    print(ret)

    ret = re.split("()", RE_SS_ABCDEFGHIJK)
    print(ret)

# str = "工作职责：<br>1、参与公司新产品开发设计合理的技术方案，开发、测试、部署与改进内部平台框架
# 改进现有工具或开源项目的效率、扩展性与稳定性；<br>4、新技术研究和应用，并推动适合的技术应用于生产
# 任职资格：
# 熟练掌握Golang语言，具备良好的算法和数据结构基础，熟悉设计模式；
# 熟悉Linux操作系统，掌握至少一门脚本语言，并有一定的troubleshooting经验；
# 熟练掌握Linux系统和网络编程的相关技能，熟悉TCP/IP、HTTP/HTTPS协议的相关知识；
# 掌握常见的数据库、缓存、消息队列的使用方法，了解内部实现原理及使用场景；
# 逻辑清晰、踏实勤奋、有责任心、积极主动、良好沟通、团队协作。<br>加分项：
# 对Hadoop生态熟悉，并有一定经验的开发者优先；<br>2、对K8s、ServiceMesh/Serverless、
# Cloud Native技术栈、微服务系统设计和开发有经验者优先；
# 有高性能，高可用的大规模分布式系统开发经验者优先"






def main():
    print("main")
    # re.match("正则表达式", "字符串")
    ret = re.match("Hello", RULES)
    print(ret)





if __name__ == "__main__":
    sangle_word()
    multi_words()
    search()
    findall()
    sub()
    split()