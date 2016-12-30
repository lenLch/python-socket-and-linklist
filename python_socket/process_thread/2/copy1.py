#!/usr/bin/python

import os

pid = os.fork()

f = open('1.txt','r')
f_cp = open('2.txt','w')
index = f.seek(0,2)
size = f.tell() / 2

if pid < 0:
    print "create failed"
elif pid == 0:
    f.seek(0,0)
    f_cp.seek(0,0)
    num = 0
    while True:
        s = f.readline()
        if num < size:
            f_cp.write(s)
        else:
            break
        num += len(s)
else:
    os.wait()

    f.seek(size,0)
    f_cp.seek(size,0)
    while True:
        s = f.readline()
        if s == '':
            break
        f_cp.write(s)
