#!/usr/bin/env python
# coding=utf-8

from gevent import monkey
import gevent
import urlib2

# 有 IO 做时才需要这一句
monkey.patch_all()

def myDownLoad(url):
    print("GET: %s"%url)
    resp = urlib2.urlopen(url)
    data = resp.read()
    print("%d bytes received from %s:"%(len(data),url))


gevent.joinall([
    gevent.spawn(myDownLoad,'http://www.baidu.com/'),
    gevent.spawn(myDownLoad,'http://www.itcast.cn/'),
    gevent.spawn(myDownLoad,'http://www.itheima.com/'),
])

