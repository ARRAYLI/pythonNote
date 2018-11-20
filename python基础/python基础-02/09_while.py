#!/usr/bin/env python
# coding=utf-8

i = 0
while i<5:
    j = 0;
    while j<=i:
       print("*",end="") 
       j = j + 1           #  i = i+1 在C语言中可以表示为 i++,++i,i+=1,i = i + 1;在python 中只能使用 i+=1,i = i + 1
    print("")
    i = i + 1
