#!/usr/bin/env python
# coding=utf-8

class Tool(object):
    def __init__(self,name):
        self.name = name


num = 0
too1 = Tool("铁锹")
num += 1
print(num)

too2 = Tool("工兵铲")
num += 1
print(num)

too3 = Tool("水桶")
num += 1
print(num)
