#!/usr/bin/env python
# coding=utf-8

i = 1

while i <= 5:
    print("----")
    print(i)
    
    if i == 3:
        break
    i += 1

# 打印 1 - 100 之间的 20 个偶数

i = 1
sum = 0
while i<= 100:
    if i % 2 == 0:
        print(i)
        sum += 1

    if sum == 20:
        break
    i += 1
