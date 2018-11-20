#!/usr/bin/env python
# coding=utf-8

i = 1
while i<=10:
    i += 1
    print("-----")

    if i == 3:
        continue

    print(i)


print("=========")


i = 1
while i<=5:
    j = 1
    while j<=i:
        print("*",end="")
        j+1
        break
    print("")  #换行

    i+=1
    break
