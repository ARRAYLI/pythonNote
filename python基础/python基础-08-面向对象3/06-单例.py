#!/usr/bin/env python
# coding=utf-8

class Dog(object):
    
    # 类属性
    __instance = None

    def __new__(cls):
        if cls.__instance == None:
            cls.__instance = object.__new__(cls)
            return cls.__instance
        else:
            #return 上一次创建对象的引用
            return  cls.__instance


a = Dog()
print(id(a))
b = Dog()
print(id(b))
