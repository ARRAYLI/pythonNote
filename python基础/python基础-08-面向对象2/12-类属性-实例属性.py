#!/usr/bin/env python
# coding=utf-8

class Tool(object):
    # 类属性
    num = 0  # 类属性
       

    # 方法
    def __init__(self,name):
        # 实例属性
        self.name = name
        # 对类属性 +=1
        Tool.num += 1


too1 = Tool("铁锹")
too2 = Tool("工兵铲")
too3 = Tool("水桶")

print(Tool.num)

'''
总结：
        实例属性：和具体的某个实例对象有关系,并且一个实例对象和另外一个实例对象是不共享属性的
        类属性：类属性所属于类对象，并且多个实例之间共享同一个类属性

'''
