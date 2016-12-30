#!/usr/bin/python

import sys,os


try:
    fd_src = open(sys.argv[1],'r+')
except:
    print "open fd_src failed"

fd_src.seek(0,2)
size = fd_src.tell()


try:
    fd_dst = open(sys.argv[2],'w+')
except:
    print "open fd_dst failed"

size /= 2

pid = os.fork()

if pid < 0:
    print "fail to fork"
    exit(-1)
elif pid == 0:
    fd_src.close()
    fd_dst.close()
    fd_src = open(sys.argv[1],'r+')
    fd_dst = open(sys.argv[2],'w+')

    fd_src.seek(size,0)
    fd_dst.seek(size,0)

    while True:
        buf = fd_src.readline()
        if buf == '':
            break
        fd_dst.write(buf)

    exit(0)
else:
    num = 1
    fd_src.seek(0,0)
    fd_dst.seek(0,0)
    while True:
        buf = fd_src.readline()
        num += len(buf)
        if num <= size:
            fd_dst.write(buf)
        else:
            break

    os.wait()
    exit(0)
