#!/usr/bin/env python
# coding=utf-8

sex = input("请输入您的性别：")

if sex == "男":
    print("您是男的，可以留胡子...")
elif sex == "女":
    print("您是女的，可以留长发...")
elif sex == "中性":
    print("您是第三种性别，可以随便搞...")
else:
    print("其他...")

num = int(input("请输入一个数字1~7："))
if num == 1:
    print("星期1:")
elif num == 2:
    print("星期2:")
elif num == 3:
    print("星期3:")
elif num == 4:
    print("星期4:")
elif num == 5:
    print("星期5:")
elif num == 6:
    print("星期6:")
elif num == 7:
    print("星期7:")
else:
    print("您输入的数据有误...")
