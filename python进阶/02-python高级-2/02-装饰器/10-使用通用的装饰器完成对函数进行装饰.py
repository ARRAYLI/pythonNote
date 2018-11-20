#!/usr/bin/env python
# coding=utf-8

def func(functionName):
    def func_in(*args,**kwargs):
        print("---记录日志---")
        ret = functionName(*args,**kwargs)  # 保存返回来的 hahaha
        return ret  # 把 haha 返回到17 行的调用处
    return func_in


@func
def test():
    return "hahaha"

@func
def test2():
    print("-----test2----")

@func
def test3(a):
    print("-----test3- a=%d---"%a)




ret = test()
print("rest return value is %s"%ret)

a = test2()
print(a)

test3(11)
