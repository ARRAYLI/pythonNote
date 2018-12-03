#!/usr/bin/env python
# coding=utf-8

from socket import *

servSocket = socket(AF_INET,SOCK_STREAM)

servSocket.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)

servSocket.bind(('',7788))
servSocket.listen(5)

newSocket,newAddr = servSocket.accept()

print("newSocket:[%s],newAddr:[%s]"%(str(newSocket),newAddr))

while True:
    recvData = newSocket.recv(1024).decode("utf-8")
    if recvData:
        print("收到来自[%s]的数据:[%s]"%(newAddr,recvData))
    else:
        newSocket.close()
        break
    
    inputData = input()
    newSocket.send(inputData.encode())

servSocket.close()
