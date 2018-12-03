#!/usr/bin/env python
# coding=utf-8

from socket import *

clientSocket = socket(AF_INET,SOCK_STREAM)
clientSocket.connect(("192.168.170.219",8899))

# 注意：
# 1. tcp 客户端以及连接好了服务器，所以在以后的数据发送汇总，不需要填写对方的ip和端口      ----->打电话
# 2.udp 在发送数据的时候，因为没有之前的连接，所以需要 在每次发送中都要填写接收方的ip和端口  ---->写信

#clientSocket.send(b"hahaha")
recvData = clientSocket.send("hahaha".encode("gb2312"))

print("recvData:%s"%recvData)

clientSocket.close()
