#!/usr/bin/env python
# coding=utf-8

class Dog:

    def __del__(self):
        print("-----英雄 over======")
    pass

dog1 = Dog()
dog2 = dog1

del dog1   # 不会调用 __del__方法，因为这个对象，还有其他的变量指向它，即引用计数不是 0 
del dog2   # 此时会调用 __del__ 方法，因为没有变量指向它了
print("= = = = = = = = = = = = = = = = = = =")

# 如果在程序结束时，有些对象还存在，那么 python 解释器会自动调用它们的 __del__ 方法来完成清理工作



