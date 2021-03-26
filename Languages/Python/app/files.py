#!/usr/bin/python
import json

write_in = "Hello world"

def file_read():
    with open("./test.txt","r") as f:
        s=f.read()
        print(s)
        return s

def file_write():
    with open("./test.txt","w") as f:
        f.write(write_in)

if __name__ == "__main__":
    s = file_read()
