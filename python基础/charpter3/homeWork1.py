#!/usr/bin/env python
# coding=utf-8

# -*- coding:utf-8 -*-

import operator

# 方法一：
a = [1,2,3,4,5,6,7,8,9,0]

i = 1
b = a[0]

while i<= len(a):
    for k in a:
        if(b >= k):
            pass
        else:
            b = k
        i += 1
print(b)

res = max(a)
print(res)

res = min(a)
print(res)
