#!/usr/bin/python
import random
MAX  = 0
step = 0
best = 0
act  = {'w':"up",'s':"down",'a':"left",'d':"right"}
dirs = ["up","down","left","right"]

def init():
    global best
    try:
        f = open("record.txt","r")
    except IOError:
        print("open failed")
    else:
        s = f.read()
        if s == '':
            best = 999999
        else:
            best = int(s)
        f.close()
       
cnt = 0
def inc_cnt():
    global cnt
    cnt = cnt + 1
    return cnt

def reset_cnt():
    global cnt
    cnt = 0

def create_map(n):
    global MAX
    MAX = n
    map_l = [[inc_cnt() for i in range(n)] for j in range(n)]
    reset_cnt()

    map_l[n-1][n-1] = 0
    return map_l

def reset():
    global MAX
    global step
    reset_cnt()
    num = 1
    for i in range(MAX):
        for j in range(MAX):
            map[i][j] = inc_cnt()
    map[MAX-1][MAX-1] = 0;
    reset_cnt()
    mess_up(1000)
    step = 0

def mess_up(n):
    for i in range(n):
        r = int(random.random()*10)%4
        move(dirs[r])

def update_record(n):
    try:
        f = open("record.txt","w+")
    except IOError:
        print("open failed")
    else:
        f.write(n)
        f.close()

def win_ck():
    global MAX
    global step
    global best
    reset_cnt()
    for i in range(MAX):
        for j in range(MAX):
            if map[i][j] != inc_cnt():
                if i == MAX-1 and j == MAX-1 and map[i][j] == 0:
                    return True
                return False
    reset_cnt()
    if step < best:
        update_record(str(step))
        print("New record!")
    print("Total step is ",step)
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
    global step
    step = step + 1
    i,j,up,down,left,right = find_empty()
    if dir == 'down'and i != 0:
        map[i][j] = map[i-1][j]
        map[i-1][j] = 0
    elif dir == 'up'and i != MAX-1:
        map[i][j] = map[i+1][j]
        map[i+1][j] = 0
    elif dir == 'right'and j != 0:
        map[i][j] = map[i][j-1]
        map[i][j-1] = 0
    elif dir == 'left'and j != MAX-1:
        map[i][j] = map[i][j+1]
        map[i][j+1] = 0
    else:
        step = step - 1
        return

def print_map():
    print("Total step is ", step)
    for i in range(MAX):
        for j in range(MAX):
            if map[i][j] == 0:
                print(" ",end="\t")
            else:
                print(map[i][j],end="\t")
        print(" ")
    print("****************************************")

def start():
    print("Welcome to digital HRD")
    while True:
        if win_ck() == True:
            print("You win")
            return True
        dir = input("Please input:")
        if dir in act:
            move(act[dir])
        elif dir == 'r' or dir == 'R':
            if dir == 'R':
                update_record('999999')
                print("Reset the record!!")          
            reset()
            print("Restart the game")
            return True
        else:
            print("'w/s/a/d' to move, 'r' to restart, 'R' to reset the record and restart")
            print("Please input valid key")
        print("----------------")
        print_map()
              
if __name__ == '__main__':
    init()
    map = create_map(3)
    while True:
        print_map()
        mess_up(1000)
        step = 0
        if False == start():
            break
