#!/usr/bin/env python
# coding=utf-8

tickets = 1  # 1 代表有车票，0 代表没有车票
knifeLength = 48 # cm

# 先判断有没有车片
if tickets==1:
    print("通过了车票的检测，进入到了车站，接下来要安检了...")

    # 判断刀的长度是否合法
    if knifeLength<=10:
        print("通过安检了，进入到了候车厅...")
        print("马上就可以见到TA了，很开心...")
    else:
        print("安检没有通过，等待公安处理...")
else:
    print("兄弟，你还没有买票了，先去买票再说，才能进站...")
