#!/usr/bin/python

import multiprocessing

from time import ctime,sleep

import os

def worker(interval = 2):
    n = 5

    while n > 0:
        print "the time is {}".format(ctime())
        print "child pid >>",os.getpid()
        sleep(interval)
        n -= 1

if __name__ == '__main__':
    p = multiprocessing.Process(target = worker)
    p.start()

    print "p.pid",p.pid
    print "p.name",p.name
    print "p.is_alive",p.is_alive

    print os.getpid()
