# *_* coding:utf-8 *_*
# @author:sdh
# @Time : 2021/3/20 0020 11:11


# TCP
# 传输控制协议（TCP，Transmission Control Protocol）是一种面向连接的、可靠的、基于字节流的传输层通信协议。
# TCP严格区分客户端和服务器


import socket

# 1 TCP客户端 步骤
# (1)创建客户端套接字对象
# (2)连接服务器
# (3)向服务器发送数据和接收数据
# (4)关闭套接字


def tcp_client():
    # 1 创建套接字
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # 2 链接接服务器
    servier_ip_port = ("192.168.1.1", 7788)
    s.connect(servier_ip_port)
    # 3 收发数据
    send_data = "hello"
    s.send(send_data.encode("utf-8"))
    # 4 关闭套接字
    s.close()


## 2 TCP服务器 步骤
# (1)创建服务器套接字对象
# (2)服务器绑定ip和port信息bind
# (3)将套接字设置为监听状态，可以被链接listen
# (4)等待客户端链接accept
# (5)收发数据
# (6)关闭套接字


def tcp_servicer():
    # 1 创建套接字
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # 2 服务器绑定ip和port
    servier_ip_port = ("", 7788)
    s.bind(servier_ip_port)

    # 3 设置为监听套接字
    s.listen(128)

    # 3 等待客户端到来
    new_socket, client_addr = s.accept()

    recv_data = new_socket.recv(1024)  # 服务器接收客户端的请求
    new_socket.send("hello".encode("utf-8"))  # 服务器给客户端回复客户端

    # 4 关闭套接字
    new_socket.close()
    s.close()
