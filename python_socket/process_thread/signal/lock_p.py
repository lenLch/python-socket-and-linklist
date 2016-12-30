#!/usr/bin/python
#coding=utf-8
import multiprocessing,sys
from time import sleep

def worker_with(lock,stream):
    with lock:
        for i in range(5):
            sleep(1)
            stream.write('lock acquired via with\n')

def worker_no_with(lock,stream):
    lock.acquire()#上锁
    try:
        for i in range(5):
            sleep(1)
            stream.write('lock acquired directly\n')
    finally:
            lock.release()#解锁


lock = multiprocessing.Lock()
w = multiprocessing.Process(target=worker_with,args=(lock,sys.stdout))
nw = multiprocessing.Process(target=worker_no_with,args=(lock,sys.stdout))
w.start()
nw.start()

w.join()
nw.join()
