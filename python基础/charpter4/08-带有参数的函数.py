#!/usr/bin/env python
# coding=utf-8

# 定义了一个函数

def sum(a,b):
    result = a+b
    print("%d + %d = %d"%(a,b,result))

num1 = int(input("请输入第一个数字："))
num2 = int(input("请输入第二个数字："))

# 调用函数
sum(num1,num2)


