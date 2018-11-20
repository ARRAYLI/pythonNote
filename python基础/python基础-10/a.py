#!/usr/bin/env python
# coding=utf-8

class Test(object):

    def __init__(self,num):
        super(Test,self).__init__()
        self.num = num

    def __str__(self):
        return "测试值是:%d"%self.num

def main():

    test = Test(10)
    print(test)

if __name__ == '__main__':
    main()
