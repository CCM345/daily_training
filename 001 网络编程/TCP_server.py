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
def CC_server():
    #创建
    tcp_ser = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)

    #bind
    SER_IP = "192.168.43.90"
    SER_PORT = 8888
    ser_info = (SER_IP, SER_PORT)
    tcp_ser.bind(ser_info)

    #listen
    LISTEN_NUM = 10
    tcp_ser.listen(LISTEN_NUM)

    while True:
        #accept  1默认会阻塞，2并返回一个新的套接字用于和接进来的客户端进行数据传输，3并记录客户端的信息,为用户进行服务
        print("服务器的IP：%s,端口:%d,正在等待新的客户端的到来" % (SER_IP,SER_PORT ))
        tcp_ser_for_client,client_addr = tcp_ser.accept()
        print("客户端已经到来,信息如下:%s" % str(client_addr))

        while True:
            #recv
            tcp_ser_recv_info = tcp_ser_for_client.recv(1024)
            if tcp_ser_recv_info == "exit":
                break
            print("服务端接收:%s" % tcp_ser_recv_info.decode("utf-8"))

            #send
            tcp_ser_send_info = str(input("服务端发送:"))
            tcp_ser_for_client.send(tcp_ser_send_info.encode("utf-8"))

    #close
        #close 关闭客户端的连接
        tcp_ser_for_client.close()
        print("为客户端%s的服务已经结束" % str(client_addr))
    tcp_ser.close()

if __name__ == "__main__":
    CC_server()



