#!/usr/bin/env python
# coding=utf-8


from socket import *

servSocket = socket(AF_INET,SOCK_STREAM)

servSocket.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)

localAddr =('',7788)

servSocket.bind(localAddr)
servSocket.listen(5)

while True:
    print("------主进程，，等待新客户到来--------")
    newSocket,destAddr = servSocket.accept()
    print("------主进程，接下来负责数据处理[%s] ------"%str(destAddr))

    try:
        while True:
            recvData = newSocket.recv(1024)
            if len(recvData) >0:
                print("recv[%s]:%s"%(str(destAddr),recvData))
            else:
                print("[%s]客户端已经关闭"%str(destAddr))

    finally:
        newSocket.close()


servSocket.close()

