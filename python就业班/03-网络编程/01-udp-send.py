#!/usr/bin/env python
# coding=utf-8


from socket import *

udpSocket = socket(AF_INET,SOCK_DGRAM)

udpSocket.sendto(b"hahha",("192.168.170.219",7788))

recvData = udpSocket.recvfrom(1024)

print("%s"%recvData[0])
