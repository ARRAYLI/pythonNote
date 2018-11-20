#!/usr/bin/env python
# coding=utf-8

def test():
    a = 11
    b = 22
    c = 33

    # 方法一：用一个列表来封装
    
    d = [a,b,c]

    # 方法二：直接返回列表

    # return [a,b,c]

    # 方法三：使用元祖来封装
    # return (a,b,c)
    return a,b,c     # 默认使以元组的形式进行封装
    # return b 
    # return c 

num = test()
print(num)

num = test()
print(num)
