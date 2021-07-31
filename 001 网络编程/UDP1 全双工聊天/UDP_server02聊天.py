#--coding:utf-8--
import socket
import logging
"""
UDP 的服务端
1，socket 创建socket
2.bind 绑定IP地址
3.recvfrom 接收数据
4.close 关闭
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
    udp_socket.bind(SER_INFO)

def udp_recv_message(udp_socket):
    print("服务端正在等待接收数据")
    udp_recv_info = udp_socket.recvfrom(1024)
    print("服务端收到:%s,来自客户端%s" % (str(udp_recv_info[0]), str(udp_recv_info[1])))
    return udp_recv_info

def udp_send_message(udp_socket, cli_info):
    send_info = str(input("服务端发送的数据为:"))
    udp_socket.sendto(send_info, cli_info[1])

def udp_close(udp_socket):
    udp_socket.close()

def CCM_UDP_server():
    #创建UDP的套接字
    udp_ser = udp_creat_socket()

    #bind
    udp_bind_ip_port(udp_socket=udp_ser)
    while True :
        #recvfrom
        cli_info = udp_recv_message(udp_socket=udp_ser)

        #send
        udp_send_message(udp_socket=udp_ser, cli_info=cli_info)

    #close
    udp_close(udp_socket=udp_ser)

if __name__ == "__main__":
    CCM_UDP_server()




