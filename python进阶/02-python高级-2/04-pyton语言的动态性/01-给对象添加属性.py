#!/usr/bin/env python
# coding=utf-8


class Person(object):
    def __init__(self,name,age):
        self.name = name
        self.age = age


laowang = Person("老王",2000)
print(laowang.name)
print(laowang.age)
laowang.addr = "北京..."
print(laowang.addr)


laozhao = Person("老赵",18)
#print(laozhao.addr)


Person.num = 100
print(laowang.num)
print(laozhao.num)
