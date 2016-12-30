#!/usr/bin/python
import sys

filename = sys.argv[0]

f = open(filename,'r')

buf = f.read()

print buf
