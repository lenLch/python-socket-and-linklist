#!/usr/bin/python

with open('file','w') as f:
    f.write("begin")
    f.seek(1024,1)
    f.write('end')
