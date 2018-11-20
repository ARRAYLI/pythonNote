#!/usr/bin/env python
# coding=utf-8


age = input("请输入您的年龄：")   # input 获取的所有数据，都当做字符串类型  20....age...."20"

age_num = int(age)    #-------------->整型，去除了双引号后的值  20
# 如果年龄大于18，可以去网吧
if age_num>18:
    print("已成年，可以去网吧嗨皮......")
else:
    print("未成年，回家写作业吧")


