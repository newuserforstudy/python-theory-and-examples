# *_* coding:utf-8 *_*
# @author:sdh
# @Time : 2021/3/20 0020 11:09
# %% md

# 1 什么网络通信？
# 如QQ、微信等通过网络进行信息交流。


# 2 计算机中的ip地址
# 标记网络中的唯一一台电脑


#3 查看电脑的网卡信息
# windows：ipconfig
# linux：ifconfig


# 4 端口
# 标记应用程序


# 5 如何实现网络通信？
# 使用socket
# 套接字实现


#6 创建一个udp套接字
# 用户数据报协议UDP，User Datagram Protocol
# UDP为应用程序提供了一种无需建立连接就可以发送封装的IP数据包的方法。


import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.close()


# 7 UDP发送数据

def udp_send_info():
    # 1 创建套接字
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    send_data = b"hello python"
    send_ip_port = ("192.168.1.100", 8080)

    # 使用套接字发送数据
    s.sendto(send_data, send_ip_port)

    # 关闭套接字
    s.close()


# 8 UDP接收输入

def receive_info():
    # 1 创建套接字
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # 2 绑定本地信息
    local_info = ("", 8081)
    s.bind(local_info)

    # 3 接收数据
    rec_data = s.recvfrom(1024)
    print("receive data:", rec_data[0].decode("gbk"))
    print("sender ip port: ", rec_data[1])

    # 4 关闭套接字
    s.close()
