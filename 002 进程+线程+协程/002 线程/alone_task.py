import time
import threading

def sing():
    for i in range(5):
        print("sing")
        time.sleep(1)


def dance():
    for i in range(5):
        print("dance")
        time.sleep(1)

def play():
    for i in range(5):
        print("play")
        time.sleep(1)

if __name__== "__main__":
    sing()  #单线程的情况
    dance()
    play()

    len = len(threading.enumerate())
    print("线程数:%d" % len)



