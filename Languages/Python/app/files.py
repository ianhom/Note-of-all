#!/usr/bin/python

write_in = "Hello world"

with open("./test.txt","w") as f:
    s=f.read()
    print(s)
    f.write(write_in)
