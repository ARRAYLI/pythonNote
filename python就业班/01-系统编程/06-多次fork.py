#!/usr/bin/env python
# coding=utf-8

import os 
import time

ret = os.fork()
if ret == 0:
    # 子进程
    print("----1----")
else:
    # 父进程
    print("----2----")


# 父子进程
ret = os.fork()
if ret == 0:
    # 孙子进程
    # 2 儿子
    print("----11----")
else:
    # 儿子
    # 父进程
    print("----22----")
