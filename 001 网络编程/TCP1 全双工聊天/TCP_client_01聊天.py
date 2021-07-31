#*coding:utf-8*
import socket
import logging
"""
TCP 的客户端编程
1.socket
2.connet （TCP）
3.send
4.close
"""



def tcp_creat_socket():
    tcp_cli = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)
    return tcp_cli

def tcp_connet_socket(tcp_socket):
    # SER_IP = input("要连接服务器的地址:")
    SER_IP = "127.0.0.1"
    SER_PORT = int(input("要连接服务器的端口:"))
    SER_INFO = (SER_IP, SER_PORT)
    tcp_socket.connect(SER_INFO)

def tcp_send_message(tcp_socket):
    send_info = str(input("输入客户端发送的消息:"))
    if (send_info == "exit") or (None == send_info):
        print("输入客户端发送的消息不正确")
    tcp_socket.send(send_info.encode("utf-8"))

def tcp_recv_message(tcp_socket):
    tcp_cli_recv_info = tcp_socket.recv(1024)
    print("客户端的接收信息为: %s" % tcp_cli_recv_info)

def tcp_close(tcp_sockeet):
    tcp_sockeet.close()

def CC_client():
    # 创建
    tcp_socket = tcp_creat_socket()

    # 链接
    tcp_connet_socket(tcp_socket=tcp_socket)

    while True:
        # send
        tcp_send_message(tcp_socket=tcp_socket)

        #recv
        tcp_recv_message(tcp_socket=tcp_socket)


    #clsoe
    tcp_close(tcp_socket=tcp_socket)

if __name__ == "__main__":
    CC_client()
