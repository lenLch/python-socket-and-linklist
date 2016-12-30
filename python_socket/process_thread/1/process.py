#!/usr/bin/python

import multiprocessing

from time import ctime,sleep

import os

def worker(interval):
    n = 5

    while n > 0:
        print "The time is {}".format(ctime())
        print "worker pid >> ",os.getppid()
        sleep(interval)
        me/linux/sys' 
        n -= 1


def teacher(interval):
    n = 5

    while n > 0:
        print "The time is {}".format(ctime())
        print "teacher pid >> ",os.getppid()
        sleep(interval)
        n -= 1


if __name__ == '__main__':
    p = multiprocessing.Process(name = 'worker',target = worker,args = (2,))
    p.start()
    q = multiprocessing.Process(name = 'teacher',target = teacher,args = (3,))
    q.start()
    
    p.join()
    q.join()

    print "p.pid:",p.pid
    print "p.name:",p.name
    print "p.is_alive:",p.is_alive
    print "q.pid:",q.pid
    print "q.name:",q.name
    print "q.is_alive:",q.is_alive


