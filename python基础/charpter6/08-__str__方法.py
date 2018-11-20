#!/usr/bin/env python
# coding=utf-8

class Cat:
    """定义了一个 Cat类"""

    # 初始化对象
    def __init__(self,name,age):
        self.name = name 
        self.age = age
    
    def __str__(self):
        return "%s的年龄是:%d"%(self.name,self.age)

    # 方法
    def eat(self):
        print("猫在吃鱼...")

    def drink(self):
        print("猫正在喝可乐...")
    
    def introduce(self):
        print("%s 的年龄是: %d"%(self.name,self.age))

# 创建一个对象
tom  = Cat("汤姆",40)

lanmao = Cat("lanmao",10)

print(tom)
print(lanmao)
