#!/usr/bin/python

write_in = "Hello world"

def file_read():
    with open("./test.txt","r") as f:
        s=f.read()
        print(s)

def file_write():
    with open("./test.txt","w") as f:
        f.write(write_in)
