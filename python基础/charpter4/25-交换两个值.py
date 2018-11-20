#!/usr/bin/env python
# coding=utf-8


a = 4
b = 5
c = 0

# 第一种方法：
'''
c = a
a = b
b = c

print("a = %d,b = %d"%(a,b))
'''

# 第二种方法：
'''
a=a+b
b = a-b
a = a-b
print("a = %d,b = %d"%(a,b))
'''

# 第三种方法：
a,b = b,a
print("a = %d,b = %d"%(a,b))
