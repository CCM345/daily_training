#--coding:utf-8--
import socket
"""
TCP 的服务端
1，socket 创建socket
2.bind 绑定IP和端口
3.listen 处于监听状态
4.accept 接进来客户端的连接
5.recv/send 接受或者发送信息
6.close 关闭
"""

def tcp_creat_socket():
    tcp_ser = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)
    return tcp_ser

def tcp_bind_listern_info(tcp_socket):
    # SER_IP = input("服务器绑定的IP:")
    SER_IP = "127.0.0.1"
    SER_PORT = int(input("服务器绑定的端口:"))
    SER_INFO = (SER_IP, SER_PORT)
    tcp_socket.bind(SER_INFO)

    LISTEN_NUM = 10
    tcp_socket.listen(LISTEN_NUM)
    return SER_INFO

def tcp_accept(tcp_socket,ser_info):
    # accept  1默认会阻塞，2并返回一个新的套接字用于和接进来的客户端进行数据传输，3并记录客户端的信息,为用户进行服务
    print("服务器的IP：%s,端口:%d,正在等待新的客户端的到来" % (ser_info[0], ser_info[1]))
    tcp_ser_new_socket, client_addr = tcp_socket.accept()
    print("客户端已经到来,信息如下:%s" % str(client_addr))
    return tcp_ser_new_socket

def tcp_recv_message(tcp_socket):
    # recv  返回值为空时，则客户端调用了close
    tcp_ser_recv_info = tcp_socket.recv(1024)
    if ((tcp_ser_recv_info == "exit") or (tcp_ser_recv_info == None)):
        print("recv_info error")
    print("服务端接收:%s" % tcp_ser_recv_info)

def tcp_send_message(tcp_socket):
    send_info = str(input("输入服务端发送的信息:"))
    tcp_socket.send(send_info.encode("utf-8"))

def tcp_close(tcp_socket):
    tcp_socket.close()


def CC_server():
    # 创建
    tcp_ser =tcp_creat_socket()

    #bind and listen
    ser_info = tcp_bind_listern_info(tcp_socket=tcp_ser)

    while True:  #循环为多个客户端服务，一直处于监听状态
        new_socket = tcp_accept(tcp_socket=tcp_ser,ser_info=ser_info)

        while True: #循环为同一个用户服务多次
            #recv  返回值为空时，则客户端调用了close
            tcp_recv_message(tcp_socket=new_socket)

            #send
            tcp_send_message(tcp_socket=new_socket)

        #close 关闭发送数据的客户端的连接
        tcp_close(tcp_socket=new_socket)

    #close
    tcp_close(tcp_socket=tcp_ser)

if __name__ == "__main__":
    CC_server()



