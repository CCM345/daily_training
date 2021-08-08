#*coding:utf-8*
import socket
import logging


"""
UDP 的客户端编程
1.socket 创建
2.sendto 发送 （可以增加循环）
3.close

"""
def udp_creat_socket():
    """"
    create socket
    """
    udp_ser = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
    return udp_ser

def udp_bind_ip_port(udp_socket):
    SER_IP = "127.0.0.1"
    SER_PORT = int(input("服务端的IP:127.0.0.1,服务器的端口:"))
    SER_INFO = (SER_IP, SER_PORT)
    return SER_INFO

def CCM_UDP_client():
    #创建UDP的

    udp_cli = udp_creat_socket()

    #bind
    CLI_PORT = 9999
    CLI_INFO = ("", CLI_PORT)

    SER_INFO = udp_bind_ip_port(udp_socket=udp_cli)

    while True:
        #send
        send_info = str(input("客户端发送信息:"))
        if ("exit" == send_info) or (None == send_info):
            break
        udp_cli.sendto(send_info.encode("utf-8"), SER_INFO)

        #recv_info
        recv_info = udp_cli.recvfrom(1024)
        print("客户端接收的信息%s,来自服务器:%s" % (str(recv_info[0]), str(recv_info[1])))

    #close
    udp_cli.close()


if __name__ == "__main__":
    CCM_UDP_client()

