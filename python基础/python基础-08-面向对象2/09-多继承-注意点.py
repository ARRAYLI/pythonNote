#!/usr/bin/env python
# coding=utf-8

class Base(object):
    def test(self):
        print("-----Base-----")
    
class A(Base):
    def test(self):
        print("--------A")

class B(Base):
    def test(self):
        print("-------B")

class C(A,B):
    pass
    #def test(self):
    #    print("-------C")
c = C()
c.test()

# C.__mro__ 决定这个调用一个方法的时候，搜索的顺序，如果在某个类中找到了方法，那么就停止搜索
print(C.__mro__)
