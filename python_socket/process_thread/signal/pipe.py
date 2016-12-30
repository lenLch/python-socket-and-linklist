#!/usr/bin/python
#coding=utf-8

#无名管道

import sys,os
from time import sleep

(r,w) = os.pipe()#r,w是c语言中的整形

pid = os.fork()

if pid < 0:
    print "create failed"
elif pid == 0:
    print "child:"
    os.close(w)
    #这个是将整形的rw转换成python中的文件对象
    r = os.fdopen(r,'r')#相当于对这个r进行了重定向,其实和open没什么区别

    while True:
        buf = r.readline()
        print "buf: ",buf
        sys.stdout.flush()
else:
    print "parent:"
    os.close(r)

    w = os.fdopen(w,'w')
    while True:
        buf = sys.stdin.readline()

        w.write(buf)
        w.flush()
