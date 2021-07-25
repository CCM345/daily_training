#*coding:utf-8*
import socket
"""
TCP 的客户端编程
1.socket
2.connet （TCP）
3.send
4.close
"""

def CC_client():
    # 创建
    tcp_cli = socket.socket(family=socket.AF_INET,type=socket.SOCK_STREAM)

    # 链接
    SER_IP = "192.168.43.90"
    SER_PORT = 8888
    ser_info = (SER_IP,SER_PORT)
    tcp_cli.connect(ser_info)

    #send
    while True:
        send_info = str(input("客户端发送:"))
        # if send_info == "exit":
        #     break
        tcp_cli.send(send_info.encode("utf-8"))

        #recv

        tcp_cli_recv_info = tcp_cli.recv(1024)
        # print("客户端接收:%s" % tcp_cli_recv_info.decode("utf-8"))
        print(tcp_cli_recv_info)
    #clsoe
    tcp_cli.close()

if __name__ == "__main__":
    CC_client()
