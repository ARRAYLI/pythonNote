#!/usr/bin/env python
# coding=utf-8

import random
player = int(input("请输入 0剪刀 ，1石头，2布："))

computer = random.randint(0,2)

if player == 0 and computer == 2 or player == 1 and computer == 0 or player == 2 and computer == 1:
    print("赢了，，，，可以去买奶粉了...")
elif player == computer:
    print("平局了，洗洗手决战到天亮...")
else:
    print("输了，回家拿钱再来...")

