#!/usr/bin/env python
# coding=utf-8

from multiprocessing import Process

def test(num):
    print("pid = %d,ppid=%d,,num = %d"%(os.getpid(),os.getppid()))

p = Process(target = test,args(100))
p.start()

print("------main---pid =%d---"%os.getpid())
