#!/usr/bin/python

import os,time

pid = os.fork()

if pid < 0:
    print "create process failed"
elif pid == 0:
    print "This is child process",os.getpid()
    print os.getppid()
    exit('hahahha')

else:
    time.sleep(0.1)
    print os.waitpid(-1,os.WNOHANG)
    print "This is parent process",os.getpid()
    print pid
    while True:
        pass

print "+++++++++++++++++++"
