#!/usr/bin/python

write_in = "Hello world"

with open("./test.txt","r") as f:
    s=f.read()
    print(s)

with open("./test.txt","w") as f:
    f.write(write_in)
