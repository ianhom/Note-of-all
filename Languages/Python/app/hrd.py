#!/usr/bin/python
import random
MAX = 0

act = {'w':"up",'s':"down",'a':"left",'d':"right"}
lst = ["up","down","left","right"]


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
    global MAX
    global map
    num = 1
    for i in range(MAX):
        for j in range(MAX):
            map[i][j] = num
            num = num + 1
    map[MAX-1][MAX-1] = 0;

def mess_up(n):
    for i in range(n):
        r = int(random.random()*10)%4
        move(dirs[r])

def win_ck():
    global MAX
    global map
    num = 1
    for i in range(MAX):
        for j in range(MAX):
            if map[i][j] != num:
                if i == MAX-1 and j == MAX-1 and map[i][j] == 0:
                    return True
                return False
            num = num + 1
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
    global map
    for i in range(MAX):
        for j in range(MAX):
            if map[i][j] == 0:
                print(" ",end="\t")
            else:
                print(map[i][j],end="\t")
        print(" ")
    print("****************************************")

def start():
    while True:
        if win_ck() == True:
            print("You win")
            return
        dir = input("Please input")
        if act.has_key(dir):
            move(act(dir))
        elif dir == 'r':
            reset()
            print("Reset the game")
        else:
            print("Please input valid key")
        print("----------------")
        print_map()
              
if __name__ == '__main__':
    map = create_map(5)
    mess_up(1000)
    print_map()
    start()
    
