#!/usr/bin/python
import sys

f = open('test.txt','r+')


str = f.write("hello")
print str

print f.tell()

f.seek(5,1)

str = f.read(5)
print str

print f.tell()
