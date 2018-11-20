#!/usr/bin/env python
# coding=utf-8

class Person(object):
    def __init__(self,name,age):
        self.name = name 
        self.age = age
    
    def eat(self):
        print("--------%s正在吃---------"%self.name)

def run(self):
    print("-------%s正在跑--------"%self.name)


p1 = Person("p1",10)
p1.eat()
p1.run = run
p1.run() # 虽然 p1 对象中 run 属性已经指向了 12 行的函数,,,但是这句代码还不正确
         # 因为 run 属性指向的函数是后来添加的，p1.run() 的时候，并没有把 p1 当做第一个参数，导致了第12行的函数调用的时候，出现缺少参数的问题
