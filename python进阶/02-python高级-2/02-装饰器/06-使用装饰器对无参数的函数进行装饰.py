#!/usr/bin/env python
# coding=utf-8

def func(functionName):
    print("-----func--1---")
    def func_in():
        print("-----func_in--1---")
        functionName()
        print("-----func_in--2---")
    
    return func_in

    print("-----func--2---")
    print("-----func--3---")


@func
def test():
    print("--------test-----")

#test = func(test)

test()
