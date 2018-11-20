#!/usr/bin/env python
# coding=utf-8

# -*- coding:utf-8 -*-


# 统计字符串中的各个字符的个数

str = input("请输入一个字符串:")
result = {}

for i in str:
    result[i] = str.count(i)
print(result)
