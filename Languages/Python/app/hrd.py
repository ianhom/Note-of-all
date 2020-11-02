#!/usr/bin/python
import random
NA   = 99999
MAX  = 0
step = 0
best = 0
act  = {'w':"up",'s':"down",'a':"left",'d':"right"}
dirs = ["up","down","left","right"]

def init():
    global best
    try:
        name = "record_"+ str(MAX)+".txt"
        print(name)
        f = open(name,"r+")
    except IOError:
        print("open failed")
        best = NA
    else:
        s = f.read()
        if s == '' or s == '0':
            best = NA
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
    reset_cnt()
    #num = 1
    for i in range(MAX):
        for j in range(MAX):
            map[i][j] = inc_cnt()
    map[MAX-1][MAX-1] = 0;
    reset_cnt()

def mess_up(n):
    for i in range(n):
        r = int(random.random()*10)%4
        move(dirs[r])

def update_record(n):
    try:
        name = "record_"+ str(MAX)+".txt"
        f = open(name,"w+")
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
                    break
                return False
    reset_cnt()
    if step < best:
        best = step
        update_record(str(step))
        print("New record for size",MAX)
    print("Total step is ",step)
    print("You win!")
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
    print("Total step is ", step,"The Best record is ", best,"(size ",MAX,")")
    for i in range(MAX):
        for j in range(MAX):
            if map[i][j] == 0:
                print(" ",end="\t")
            else:
                print(map[i][j],end="\t")
        print(" ")
    print("****************************************")
    print()

def print_help():
    print("'w/s/a/d' to move up/down/left/right")
    print("'r' to restart")
    print("'R' to reset the record and restart")
    print("'h' to print this help info")
    print("'Q' to quit")

def banner():
    print("_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/")    
    print("_/    Welcone to play HRD   _/")
    print("_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/")  

def start():
    while True:
        if win_ck() == True:
            r = input("Do you want to restart(y/n):")
            if r == 'y':
                 return True
            else:
                 return False
        dir = input("Please input:")
        if dir in act:
            move(act[dir])
        elif dir == 'r' or dir == 'R':
            if dir == 'R':
                best = NA
                update_record(str(NA))
                print("Reset the record!!")          
            reset()
            print("Restart the game")
            return True
        elif dir == 'Q':
            return False
        elif dir == 'h':
            print_help()
            return true
        else:
            print("'w/s/a/d' to move, 'r' to restart, 'R' to reset the record and restart")
            print("Please input valid key")
        print("----------------")
        print_map()
              
if __name__ == '__main__':
    banner()
    d = int(input("Please input matrix size(n*n):"))
    map = create_map(d)
    init()
    while True:
        mess_up(1000)
        step = 0
        print_map()
        if False == start():
            print("Thank you for playing") 
            break
