#!usr/bin/python
#coding=utf-8

#这个程序是启动两个进程，创建两个
from time import sleep
import os,sys

try:
    os.mkfifo('fifo1')
    os.mkfifo('fifo2')
except OSError:
    print 'fifo exist~'

r = open('fifo1','r')
w = open('fifo2','w')

while True:
    str1 = r.readline()#这里只能一行一行的读，不能使用read
    print str1
    sys.stdin.flush()
    str2 = sys.stdin.readline()
    w.write(str2)
    w.flush()
