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
    
def create_map():
    map_l = [[inc_cnt() for i in range(9)] for j in range(9)]
    reset_cnt()
    return map_l
