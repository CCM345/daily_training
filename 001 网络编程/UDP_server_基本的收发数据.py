#--coding:utf-8--
import socket
"""
UDP 的服务端
1，socket 创建socket
2.bind 绑定IP地址
3.recvfrom 接收数据
4.close 关闭
"""

def CCM_UDP_server():
    #创建UDP的
    udp_ser = socket.socket(family=socket.AF_INET,type=socket.SOCK_DGRAM)

    #bind
    SER_IP = "192.168.43.90"
    SER_PORT = 8888
    SER_INFO = (SER_IP,SER_PORT)
    udp_ser.bind(SER_INFO)
    while True :
        #recvfrom
        print("服务端正在等待接收数据")
        udp_recv_info = udp_ser.recvfrom(1024)
        print("服务端收到:%s,来自%s" % (str(udp_recv_info[0]), str(udp_recv_info[1])))

    #close
    udp_ser.close()

if __name__ == "__main__":
    CCM_UDP_server()




