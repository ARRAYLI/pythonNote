#!/usr/bin/env python
# coding=utf-8

def get_wendu():
   wendu = 22
   print("当前的温度是 %d"%wendu)
   return wendu

def get_wendu_huashi(wendu):
    print("---------4---------------")
    wendu = wendu + 3
    print("当前的温度(华氏) 是： %d"%wendu)
    print("---------5---------------")

print("---------1---------------")
result = get_wendu()
print("---------2---------------")
get_wendu_huashi(result)
print("---------3---------------")
