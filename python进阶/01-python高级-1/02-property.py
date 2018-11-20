#!/usr/bin/env python
# coding=utf-8

class Test(object):
    def __init__(self):
        self.__num = 100

    @property
    def num(self):
        print("------------getter------")
        return self.__num

    @num.setter
    def num(self, newNum):
        print("------------setter------")
        self.__num = newNum


    #num = property(getNum,setNum)

t = Test()

t.num = 200    # 相当于调用了 t.setNum(200)
print(t.num)   # 相当于调用了 t.getNum()

'''

注意点：
t.num  到底是调用 getNum() 还是 setNum() ，要根据实际的场景来判断
1.如果是给 t.num 赋值的话，那么一定调用 setNum()
2.如果是获取 t.num 的值，那么就一定调用 getNum()

property的作用：相当于把方法进行了封装，开发者在对私有属性蛇者数据的时候更方便 

'''

