#!/usr/bin/env python
# coding=utf-8

import gevent

def f(n):
    for i in range(n):
        print("%s%d"%(gevent.getcurrent(),i))
        # 用来模拟一个耗时的操作，注意不是 time 模块中的 sleep
        gevent.sleep(1)


g1 = gevent.spawn(f,5)
g2 = gevent.spawn(f,5)
g3 = gevent.spawn(f,5)

g1.join()
g2.join()
g3.join()
