#!/usr/bin/python
import random
MAX = 4
map = [[1,2,3,4],
       [5,6,7,8],
       [9,10,11,12],
       [13,14,15,0]]

map_ck = [[1,2,3,4],
          [5,6,7,8],
          [9,10,11,12],
          [13,14,15,0]]

dirs =["up","down","left","right"]

def reset():
    for i in range(MAX):
        for j in range(MAX):
            if map[i][j] = map_ck[i][j]

def mess_up(n):
    for i in range(n):
        r = int(random.random()*10)%4
        move(dirs[r])

def win_ck():
    for i in range(MAX):
        for j in range(MAX):
            if map[i][j] != map_ck[i][j]:
                return False
    return True

def find_num(num):
    for i in range(MAX):
        for j in range(MAX):
            if map[i][j] == num:
                return i,j
    return -1,-1

def find_empty():
    i = j = up = down = left = right = -1
    i,j = find_num(0)
    if i > 0:
        up = map[i-1][j]
    if i < MAX-1:
        down = map[i+1][j]
    if j > 0:
        left = map[i][j-1]
    if j < MAX-1:
        right = map[i][j+1]
    return i,j,up,down,left,right

def move(dir):
    i,j,up,down,left,right = find_empty()
    if dir == 'up'and i != 0:
        map[i][j] = map[i-1][j]
        map[i-1][j] = 0
    elif dir == 'down'and i != MAX-1:
        map[i][j] = map[i+1][j]
        map[i+1][j] = 0
    elif dir == 'left'and j != 0:
        map[i][j] = map[i][j-1]
        map[i][j-1] = 0
    elif dir == 'right'and j != MAX-1:
        map[i][j] = map[i][j+1]
        map[i][j+1] = 0
    else:
        return

def print_map():
    for i in range(MAX):
        print("%2d,%2d,%2d,%2d"%(map[i][0],map[i][1],map[i][2],map[i][3]))

def start():
    while True:
        if win_ck() == True:
            print("You win")
            return
        dir = input("Please input")
        if dir == 's':
            dir = "up"
        elif dir == 'w':
            dir = "down"
        elif dir == 'd':
            dir = "left"
        elif dir = "a":
            dir = "right"
        elif dir = "t":
            reset()
            print("Reset the game \r\n\r\n")
            continue
        move(dir)
        print("----------------")
        print_map()
              
if __name__ == '__main__':
    print(find_empty())
    mess_up(1000)
    print_map()
    start()
    
