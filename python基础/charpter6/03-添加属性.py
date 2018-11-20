#!/usr/bin/env python
# coding=utf-8

class Cat:
    # 属性

    # 方法
    def eat(self):
        print("猫在吃鱼...")

    def drink(self):
        print("猫正在喝可乐...")

# 创建一个对象
tom  = Cat()

# 调用 tom 指向对象中的 方法
tom.eat()
tom.drink()

tom.name = "汤姆"
tom.age = 40

