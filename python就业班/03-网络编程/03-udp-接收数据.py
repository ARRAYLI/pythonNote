#!/usr/bin/env python
# coding=utf-8


from socket import *

udpSocket = socket(AF_INET,SOCK_DGRAM)

udpSocket.bind(("",7788))

recvData = udpSocket.recvfrom(1024)

print(recvData)
