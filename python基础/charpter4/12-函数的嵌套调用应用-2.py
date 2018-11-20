#!/usr/bin/env python
# coding=utf-8

def sum(num1,num2,num3):
    result =  num1+num2+num3
    #print("%d + %d + %d = %d"%(num1,num2,num3,resul
    return result

# 计算三个数的平均值
def average(num1,num2,num3):
    result = sum(num1,num2,num3)
    result = result/3
    print("平均值是: %d"%result)
# 获取三个数值

num1 = int(input("第1个值："))
num2 = int(input("第2个值："))
num3 = int(input("第3个值："))

sum(num1,num2,num3)
average(num1,num2,num3)
