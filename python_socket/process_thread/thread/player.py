#!/usr/bin/python
from time import sleep
import threading,os


def music(name):
    print "i was listen music %s"%(name)
    # print os.getpid()
    sleep(2)

def movie(name):
    print "i was watching move %s"%(name)
    # print os.getpid()
    sleep(3)

def player(name):
    r = name.split('.')[1]
    if r == 'mp3':
        music(name)
    if r == 'mp4':
        movie(name)
    else:
        print 'error'

l = ['baby.mp3','haha.mp4']
keys = l.keys
value = l.values
threads = []
files = range(len(l))

for i in files:
    t = threading.Thread(target=player,args=(l[i],))
    threads.append(t)

if  __name__ == '__main__':
    for t in files:
        threads[t].start()
    for t in files:
        threads[i].join()

    # print os.getpid()

    print "game over"
