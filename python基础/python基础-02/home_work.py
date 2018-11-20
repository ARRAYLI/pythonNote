#!/usr/bin/env python
# coding=utf-8

name = "arrayli"
passwd = "123"

_name = input("请输入用户名:")
_passwd = input("请输入密码：")

if name == _name and passwd == _passwd:
    print("欢迎进入arrayli的界面")
else:
    print("用户名或者密码错误")


i = 0
k = 0
while i<9:
    j = 0
    if i > 4:
        k = 9-i-1
    else:
        k = i
    while j<=k:
        print("*",end="")
        j+=1
    
    print("")
    i+=1
