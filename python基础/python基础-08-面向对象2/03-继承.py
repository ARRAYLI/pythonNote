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
    """
    def eat(self):
        print("-------吃-------")

    def drink(self):
        print("-------喝-------")

    def sleep(self):
        print("-------睡觉-------")

    def run(self):
        print("-------炮-------")
    """
    def bark(self):
        print("-------汪汪叫-------")

class Cat(Animal):
    def catch(self):
        print("--------捕捉老鼠------")

#a = Animal()
#a.eat()

wangcai = Dog()
wangcai.eat()

tom = Cat()
tom.eat()

