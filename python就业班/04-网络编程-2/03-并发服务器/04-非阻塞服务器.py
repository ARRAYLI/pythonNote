#!/usr/bin/env python
# coding=utf-8

from socket import *

#1.创建 socket
serSocket = socket(AF_INET,SOCK_STREAM)

#2.绑定本地ip及port
localAddr = ('',7788)
serSocket.bind(localAddr)

#3.让这个socket变为非阻塞
serSocket.setblocking(False)

#4.将socket变为监听（被动)套接字
serSocket.listen(100)

#用来保存所有已经连接到客户端的信息
clientAddrList = []

while True:
    # 等待一个新的客户的到来（即完成3次握手的客户端）
    try:
        clientSocket,clientAddr = serSocket.accept()
    except:
        pass
    else:
        print("一个新的客户端到来：%s"%str(clientAddr))
        clientAddrList.append(newSocket,clientAddr)

    for clientSocket,clientAddr in clientAddrList:
        try:
            recvData = clientSocket.recv(1024)
        except:
            pass
        else:
            if len(recvData)>0:
                print("%s:%s"%(str(clientAddr,recvData)))
            else:
                clientSocket.close()
                clientAddrList.remove(clientSocket,clientAddr)
                print("%s 已经下线"%(str(clientAddr)))


