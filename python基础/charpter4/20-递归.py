#!/usr/bin/env python
# coding=utf-8

# 4! = 4*3*2*1
# 5! =5*4*3*2*1


# 循环版本 求阶乘
'''

i = 1
result = 1

while i<=4:
    result = result * i
    i += 1

print(result)

'''

# 递归版本 求阶乘

def getNums(num):
    if num > 1:
        return num * getNums(num-1) 
    else:
        return num


result = getNums(4)
print(result)




