#!/usr/bin/python
map = [[1,2,3,4],
       [5,6,7,8],
       [9,10,11,12],
       [13,14,15,0]]

def find_empty():
    for i in range(4):
        for j in range(4):
            if map[i][j] == 0:
                return i,j
    return -1,-1
