#!/usr/bin/python
import random
map = [[],[],[],[],[],[],[],[],[]]

cnt = 0
def inc_cnt():
    global cnt
    cnt = cnt + 1
    return cnt

def reset_cnt():
    global cnt
    cnt = 0
