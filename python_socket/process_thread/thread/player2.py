#!/usr/bin/python

from time import sleep
import threading

def super_player(file,time):
    for i in range(2):
        print "start playing: %s"%(file)
        sleep(time)

l = {'baby.mp3':3,'haha.mp4':5,'you.mp3':4}

threads = []
files = range(len(l))

for file,time in l.items():
    t = threading.Thread(target=super_player,args=(file,time))
    threads.append(t)

if __name__ == '__main__':
    for i in files:
        threads[i].start()

    for i in files:
        threads[i].join()

    print "game over"
