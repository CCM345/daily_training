#*coding:utf-8*
import socket
"""
UDP 的客户端编程
1.socket 创建
2.sendto 发送 （可以增加循环）
3.close

"""

def CCM_UDP_client():
    #创建UDP的
    udp_cli = socket.socket(family=socket.AF_INET,type=socket.SOCK_DGRAM)

    #bind
    # CLI_IP = "192.168.5.130"
    # CLI_PORT = 9999
    # CLI_INFO = (CLI_IP,CLI_PORT)

    SER_IP = "192.168.43.90"
    SER_PORT = 8888
    SER_INFO = (SER_IP,SER_PORT)
    # udp_cli.bind(CLI_INFO)

    while True:
        #send
        send_info = str(input("客户端发送:"))
        if ("exit" == send_info) or (None == send_info):
            break
        udp_cli.sendto(send_info.encode("utf-8"), SER_INFO)

    #close
    udp_cli.close()


if __name__ == "__main__":
    CCM_UDP_client()

