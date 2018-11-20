#!/usr/bin/env python
# coding=utf-8

def w1(func):
    print("----正在装饰---")
    def inner():
        print("----正在验证权限----")
        func()
    return inner

# 只要python 解释器执行到了这个代码，那么就会自动的进行装饰，而不是等到调用的时候才进行装饰
@w1
def f1():
    print("---f1---")

# 在调用 f1 之前，已经进行了装饰
f1()
