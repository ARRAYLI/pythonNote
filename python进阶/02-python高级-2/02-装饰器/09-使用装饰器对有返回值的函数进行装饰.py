#!/usr/bin/env python
# coding=utf-8

def func(functionName):
    print("-----func--1---")
    def func_in():
        print("-----func_in--1---")
        ret = functionName()  # 保存返回来的 hahaha
        print("-----func_in--2---")
        return ret  # 把 haha 返回到17 行的调用处
    return func_in


@func
def test():
    print("--------test-----")
    return "hahaha"

ret = test()
print("rest return value is %s"%ret)
