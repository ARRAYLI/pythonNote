#!/usr/bin/env python
# coding=utf-8

from socket import *

#1. 创建套接字
udpSocket = socket(AF_INET, SOCK_DGRAM)

#2. 绑定本地的相关信息
bindAddr = ('', 7788) # ip地址和端⼝号， ip⼀般不⽤写， 表示本机的任何⼀个ip
udpSocket.bind(bindAddr)

num = 1

while True:
    #3. 等待接收对⽅发送的数据
    recvData = udpSocket.recvfrom(1024) # 1024表示本次接收的最⼤字节数
    #4. 将接收到的数据再发送给对⽅
    udpSocket.sendto(recvData[0], recvData[1])
    #5. 统计信息
    print('已经将接收到的第%d个数据返回给对⽅,内容为:%s'%(num,recvData[0].decode("utf-8")))
    num+=1

#5. 关闭套接字
udpSocket.close()
