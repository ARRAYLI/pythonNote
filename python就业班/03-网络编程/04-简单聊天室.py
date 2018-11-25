#!/usr/bin/env python
# coding=utf-8

from socket import *

def main():
    udpSocket = socket(AF_INET,SOCK_DGRAM)
    udpSocket.bind(("",6789))

    # 收，打印

    while True:
        recvInfor = udpSocket.recvfrom(1024)
        print("[%s]:%s"%(recvInfor[1],recvInfor[0].decode("utf-8")))


if __name__ == "__main__":
    main()



