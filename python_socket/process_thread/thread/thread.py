#!/usr/bin/python
from time import sleep
import threading,os


def music(name):
    print "i was listen music %s"%(name)
    print os.getpid()
    sleep(2)

def movie(name):
    print "i was watching move %s"%(name)
    print os.getpid()
    sleep(3)

threads = []

t1 = threading.Thread(target=music,args=('body',))
t2 = threading.Thread(target=movie,args=('hahaha',))

threads.append(t1)
threads.append(t2)

if  __name__ == '__main__':
    for t in threads:
        t.setDaemon(True)
        t.start()
    for t in threads:
        t.join()
    print os.getpid()

    print "game over"
