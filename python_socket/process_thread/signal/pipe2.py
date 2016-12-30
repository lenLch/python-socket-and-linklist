#!/usr/bin/python

from multiprocessing import Process,Pipe
import os,time

process_list = []
parent_conn,child_conn = Pipe()

def f(conn,name):
    time.sleep(1)
    conn.send(['hello' + str(name)])
    print os.getppid(),'-------',os.getpid()

if __name__ == '__main__':
    for i in range(10):
        p = Process(target= f, args=(child_conn,i))
        p.start()
        process_list.append(p)
    for j in process_list:
        j.join()
    for p in range(10):
        print parent_conn.recv()
