#!/usr/bin/env python
# coding=utf-8

# 定义一个全局变量，wendu

wendu = 0

def get_wendu():
    # 如果 wendu 这个变量已经在全局变量的位置定义了，此时在函数中对这个全局变量进行修改的话,
    #那么 仅仅是 wendu= 一个值   这还不够,,,此时wendu这个变量是一个局部变量，仅仅适合全局变量的名字相同罢了

    # 使用 global 用来对一个全局变量的声明，那么这个函数中的 wendu=33 就不是定义一个局部变量，而是一对全局变量进行修改
    # wendu = 33
     global wendu
     wendu = 33

def print_wendu():
    print("温度是 %d"%wendu)

get_wendu()
print_wendu()
