#!/usr/bin/python

with open('test.txt','r+') as f:
    str = f.read()

print str

print f.read()
