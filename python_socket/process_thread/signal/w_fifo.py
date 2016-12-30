#!/usr/bin/python

from time import sleep
import os,sys

try:
    os.mkfifo('fifo1')
    os.mkfifo('fifo2')
except OSError:
    print 'fifo exist~'

w = open('fifo1','w')
r = open('fifo2','r')

while True:
    str1 = sys.stdin.readline()
    w.write(str1)
    w.flush()
    str2 = r.readline()
    print str2
    sys.stdin.flush()
