#!/usr/bin/python
#coding=utf-8
import signal,time

signal.alarm(5)
time.sleep(3)#睡眠3s，上面还剩2s，下面的4秒会覆盖上面的2s
num = signal.alarm(4)
print num#返回上面剩余的时间
#signal.pause()#阻塞函数，当收到信号，程序改变

while True:
    time.sleep(1)
    print "wait....."
