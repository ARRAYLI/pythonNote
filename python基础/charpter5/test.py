#!/usr/bin/env python
# coding=utf-8
__author__ = 'ZHHT'
#!/usr/bin/env python
# -*- coding:utf-8 -*-
import os
#1、打开文件
f = open("install-sh","r")
#2、把文章全部读取，以列表形式存储。
res = f.readlines()
#3、循环整个列表，去除以空格开头的行的空格，然后去除以#号开头的行的#号
for i in res:
    i.strip(" ")
    if i[0] == "#":
        continue
    else:
        print(i)
