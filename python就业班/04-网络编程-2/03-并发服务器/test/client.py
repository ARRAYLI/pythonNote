#!/usr/bin/env python
# coding=utf-8

from socket import *

clientSocket = socket(AF_INET,SOCK_STREAM)
clientSocket.connect(('127.0.0.1',7788))


while True:
    data = input()
    clientSocket.send(data.encode())
    recvData = clientSocket.recv(1024).decode("utf-8")
    if recvData:
        print("[%s]"%recvData)
    else:
        clientSocket.close()
        break
