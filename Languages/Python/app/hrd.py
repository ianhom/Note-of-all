#!/usr/bin/python
import random
MAX = 4

act = {'w':"up",'s':"down",'a':"left",'d':"right"}
lst = ["up","down","left","right"]

map = [[1,2,3,4],
       [5,6,7,8],
       [9,10,11,12],
       [13,14,15,0]]

map_ck = [[1,2,3,4],
          [5,6,7,8],
          [9,10,11,12],
          [13,14,15,0]]

dirs =["up","down","left","right"]

def create_map(n):
    global MAX
    MAX = n
    num = 1
    map_l = [[-1 for i in range(n)] for j in range(n)]

    for i in range(n):
        for j in range(n):
            map_l[i][j] = num
            num = num + 1
    map_l[n-1][n-1] = 0;
    return map_l

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
        for j in range(MAX):
            print(map[i][j],"\t")
        print(" ")
    print("****************************************")

def start():
    while True:
        if win_ck() == True:
            print("You win")
            return
        dir = input("Please input")
        if act.haskey(dir):
            move(act(dir))
        elif dir == 'r':
            print("Reset the game")
        elif dir == 'd':
        else:
            print("Please input valid key")
            continue
        move(dir)
        print("----------------")
        print_map()
              
if __name__ == '__main__':
    print(find_empty())
    mess_up(1000)
    print_map()
    start()
    
