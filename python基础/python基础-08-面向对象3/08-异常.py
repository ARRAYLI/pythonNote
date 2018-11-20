#!/usr/bin/env python
# coding=utf-8

try:
    num = input(("XXX:"))
    int(num)
    #11/0
    #open("xxx.txt")
    #print(num)
    print("---------------")

except (NameError,FileNotFoundError):
    print("如果捕获到异常后做的 处理...")

except Exception as ret:
    print("如果用了 Exception，那么意味着只要上面的 except 没有捕获到异常，这个 except 一定会捕捉到")
    print(ret)

else:
    print("没有异常才会执行的功能")

finally:
    print("---------finally------")

print("-----------------2----------")
