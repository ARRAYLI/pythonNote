#!/usr/bin/env python
# coding=utf-8

class A:
    def __init__(self):
        self.num1 = 100
        self.__num2 = 200
    
    def test1(self):
        print("====test1=====")

    def __test2(self):
        print("========test2===")

    def test3(self):
        self.__test2()
        print(self.__num2)


class B(A):
    def test4(self):
        self.__test2()
        print(self.__num2)


b = B()
b.test1()
# b.__test2()   # 私有方法不会被继承
#print(b.num1)
#print(b.__num2)

b.test3()
b.test4()

'''
如果调用的是 继承父类中的公有方法，可以在这个公有方法中访问父类的私有属性和私有方法

但是如果在子类实现了一个公有方法，那么这个方法是不能够调用继承的父类中的私有方法和私有属性

'''
