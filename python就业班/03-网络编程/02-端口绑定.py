#!/usr/bin/env python
# coding=utf-8


from socket import *

udpSocket = socket(AF_INET,SOCK_DGRAM)

#udpSocket.bind(("",7788))

udpSocket.sendto(b"haaahhaha",("192.168.170.219",8080))
