#!/usr/bin/env python
# coding=utf-8

from threading import Thread,Lock
import time

g_num = 0

def test1():
    global g_num
    # 这个线程和 test2 线程都在抢着 对这个锁 进行上锁 ，如果有一方成功的上锁，那么导致另外一方会堵塞（一直等待）到这锁被解开位置
    mutex.acquire()
    for i in range(1000000):
        g_num += 1
    # 用来对 mutex 指向的这个锁，进行解锁，，只要解开了锁，那么接下来会让所有因为这个锁被上了锁 而堵塞的线程 进行抢着上锁
    mutex.release()

    print("-------test1-----g_num=%d"%g_num)


def test2():
    global g_num 
    mutex.acquire()
    for i in range(1000000):
        g_num += 1
    mutex.release()
    print("-------test2---g_num=%d"%g_num)

# 创建一把互斥锁，这个锁默认是没有上锁的
mutex = Lock()


p1 = Thread(target=test1)
p1.start()

time.sleep(3) # 取消屏蔽之后 再次运行程序，结果会不一样

p2 = Thread(target = test2)
p2.start()

print("-----g_num=%d-----"%g_num)
