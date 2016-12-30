#!/usr/bin/python 

import os,time


pid = os.fork()

if pid < 0:
    print "create process error"
elif pid == 0:
    pid = os.fork()
    
    if pid < 0:
        print "create process error"
    elif pid == 0:
        while True:
            time.sleep(1)
            print "greatson do something"
    else:
        exit()
else:
    os.wait()
    while True:
        time.sleep(1)
        print "parent do something"


