#!/usr/bin/env python
# coding=utf-8

import socket
import select 

# 创建套接字
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

#v 设置可以重复使用绑定的信息
s.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)

# 绑定本机信息
s.bind(("",7788))

# 变为被动
s.listen(10)

# 创建一个 epoll 对象
epoll = select.epoll()

epoll.register(s.fileno(),select.EPOLLIN|select.EPOLLET)

connections = {}
address = {}

while True:
    # epoll 进行 fd 扫描的地方 --- 未指定超时时间则为阻塞等待
    epoll_list = epoll.poll()

    # 对时间进行判断
    for fd,events in epoll_list:
        if fd == s.fileno():
            conn,addr = s.accept()
            print("有新的客户端到来:%s"%str(addr))
            
            # 将 conn 和 addr 信息分别保存起来
            connections[conn.fileno()] = conn
            address[conn.fileno()] = addr

            # 向 epoll 中注册链接 socket 的可读事件
            epoll.register(conn.fileno(),select.EPOLLIN | select.EPOLLET)
        elif events == select.EPOLLIN:
            # 从激活 fd 上接收
            recvData = connections[fd].recv(1024)
            
            if len(recvData)>0:
                print("recv:%s"%recvData)
            else:
                # 从 epoll 中移除该链接 fd
                epoll.unregister(fd)

                # server 则主动关闭该链接 fd
                connections[fd].close()

                print("%s-----------offfline------%s"%str(address[fd]))




