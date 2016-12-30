#!/usr/bin/python

import os,time,sys

pid = os.fork()

if pid < 0:
    print "create process failed"
elif pid ==0:
    pid = os.fork()
    if pid < 0:
        print "create failed"
    elif pid == 0:
        while True:
            time.sleep(1)
            print "grandson do something.."
    else:
        sys.exit()
else:
    os.wait()#这个必须加，不然没用
    while True:
        time.sleep(1)
        print "parent do something.."
