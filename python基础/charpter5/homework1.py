#!/usr/bin/env python
# coding=utf-8

import os
# 读取一个文件,显示除了以井号(#)开头的行以外的所有行

file_name = input("请您输入要读取的文件名:")

# 1.打开文件
f = open(file_name,"r")

# 2.把文章全部读取，以列表的形式存储

results = f.readlines()

# 3.循环整个列表，去除以空格开头的行的空格，然后去除以 # 开头的行的编号

for tmp in results:
    tmp.strip()     # 去除以空格开头的行的空格
    if tmp[0] == '#':
        continue
    else:
        print(tmp)
# 4.关闭文件
f.close()



