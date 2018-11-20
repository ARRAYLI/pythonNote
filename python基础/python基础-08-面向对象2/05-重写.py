#!/usr/bin/env python
# coding=utf-8

class Animal:

    def eat(self):
        print("-------吃-------")
    
    def drink(self):
        print("-------喝-------")
    
    def sleep(self):
        print("-------睡觉-------")
    
    def run(self):
        print("-------炮-------")


class Dog(Animal):
    def bark(self):
        print("-------汪汪叫-------")

class Xiaotq(Dog):

    def fly(self):
        print("---------飞-------")
    
    def bark(self):
        print("---------狂叫------")
        Dog.bark(self)
    

xiaotq = Xiaotq()
xiaotq.fly()
xiaotq.bark()
xiaotq.eat()
