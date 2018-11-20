#!/usr/bin/env python
# coding=utf-8


def test(a,b,c=33,*args,**kwargs):
    print(a)
    print(b)
    print(c)
    print(args)
    print(kwargs)


A = (44,55,66)
B = {"name":"laowang","age":18}

test(11,22,33,*A,**B)
