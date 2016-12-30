#!/usr/bin/python
# coding=utf-8

import sys

try:
    f = open(sys.argv[1],'r')
    buf = f.read()
except IOError as e:
    print e
else:
    print buf
