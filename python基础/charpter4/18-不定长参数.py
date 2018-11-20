#!/usr/bin/env python
# coding=utf-8


def sum_2nums(a,b,*args):
    print("-"*30)
    print(a)
    print(b)
    print(args)
    
    #result = a+b
    #print("result = %d"%result)


def sum_add_nums(a,b,*args):
    result = a+b
    for i in args:
        result += i

    return result


sum_2nums(11,22,33,44,55,66,77)
sum_2nums(11,22,33)
sum_2nums(11,22)
#sum_2nums(11)   # 错误

print("-"*30)
print("result = %d"%sum_add_nums(11,2,22,33,44,666,777,777))
