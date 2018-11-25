#!/usr/bin/env python
# coding=utf-8

import time 
from threading import Thread


# 1.如果多个线程执行的都是同一个函数的话，各自之间不会有影响，各是各的

def test():
    print("------昨晚喝多了，下次少喝点------")
    time.sleep(1)


for i in range(5):
    t = Thread(target = test)
    t.start()



