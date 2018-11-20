#!/usr/bin/env python
# coding=utf-8

# 请用函数实现一个判断用户输入的年份是否是闰年

def isLeapYead(year):
    if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
        return True
    else:
        return False

year = int(input("请输入一个年份:"))
res = isLeapYead(year)
if res == True:
    print("%d 是闰年"%year)
else:
    print("%d 是平年"%year)
