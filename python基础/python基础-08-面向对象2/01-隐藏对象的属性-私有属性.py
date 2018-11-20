#!/usr/bin/env python
# coding=utf-8

class Dog:
    # 私有方法
    def __send_msg(self):
        print("-------正在发送短信----")

    def send_msg(self,money):
        if money > 10000:
            self.__send_msg()
        else:
            print("您的余额不足，请先充值，在发送短信")
  
dog = Dog()
dog.send_msg(100)
