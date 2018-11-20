#!/usr/bin/env python
# coding=utf-8


class Dog(object):
    def __init__(self):
        print("-------init方法----") 
        pass

    def __del__(self):
        print("-------del 方法----") 
        pass

    def __str__(self):
        print("-------str方法----") 
        return "对象的描述信息"

    def __new__(cls):  # cls 此时是Dog 指向的那个对象
        #print(id(cls))
        print("-------new 方法----") 
        return object.__new__(cls)


#print(id(Dog))
xtq = Dog()   # 相当于要做 3 件事情   1.调用 __new__ 方法来创建对象,然后找了一个变量的返回值，这个返回值表示创建出来的引用  2.__init__(self) 刚刚创建出来对象的引用  3.返回对象的引用

