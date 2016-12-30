#!/usr/bin/python

from signal import *
import os,time

def receive_sig(signum,stack):
    if signum == SIGINT:
        print "keep..."
    elif signum == SIGALRM:
        print "receive a alarm"
    else:
        print "other signal"


alarm(7)

signal(SIGINT,receive_sig)
signal(SIGALRM,receive_sig)

print "my pid is: ",os.getpid()

while True:
    print "wating"
    time.sleep(2)
