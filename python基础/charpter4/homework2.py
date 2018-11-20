#!/usr/bin/env python
# coding=utf-8

# 使用函数实现 100-200 里的所有素数
result = []

def test(num):
    """用于判断一个数字是不是素数"""
    i = num-1
    list = []
    while i>1:
        if num % i == 0:
            list.append(i)
        i -= 1

    print("len = %d"%len(list))
    if len(list) == 0:
        return True
    else:
        return False
    
# 计算 100-200 内的素数个数

def sushu(start=100,end=200):
    j = start
    print(j)
    while j<end:
        print(j)
        res = test(j)
        print(res)
        if res == True:
            result.append(j)
        j += 1
start = int(input("请输入起始边界："))
end = int(input("请输入结束边界："))

sushu(start,end)
print(result)
