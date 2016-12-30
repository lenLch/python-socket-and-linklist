#!/usr/bin/python

from multiprocessing import Pool
import os,time,random

def test(name):
    print "start...."
    time.sleep(random.randint(1,10))
    print "task %s is run...."%name
    print "end...."

if __name__ == '__main__':
    print "parent pid: ",os.getpid()

    p = Pool(4)

    for i in range(5):
        p.apply_async(test,args = (i,))

    p.close()
    p.join()

    print "all process end"
