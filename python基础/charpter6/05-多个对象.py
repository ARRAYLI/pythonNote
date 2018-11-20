#!/usr/bin/env python
# coding=utf-8

class Cat:
    # 属性

    # 方法
    def eat(self):
        print("猫在吃鱼...")

    def drink(self):
        print("猫正在喝可乐...")
    
    def introduce(self):
        print("%s 的年龄是: %d"%(tom.name,tom.age))

# 创建一个对象
tom  = Cat()

# 调用 tom 指向对象中的 方法
tom.eat()
tom.drink()

# 给 tom 指向的对象添加 2 个属性
tom.name = "汤姆"
tom.age = 40

# 获取属性的第一种方式
# print("%s 的年龄是: %d"%(tom.name,tom.age))

tom.introduce()

lanmao = Cat()
lanmao.name = "蓝猫"
lanmao.age = 10
lanmao.introduce()

