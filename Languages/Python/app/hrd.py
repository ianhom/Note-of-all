#!/usr/bin/python
map = [[1,2,3,4],
       [5,6,7,8],
       [9,10,11,12],
       [13,14,15,0]]

map_ck = [[1,2,3,4],
          [5,6,7,8],
          [9,10,11,12],
          [13,14,15,0]]

def win_ck():
    for i in range(4):
        for j in range(4):
            if map[i][j] != map_ck[i][j]:
                return False
    return True

def find_num(num):
    for i in range(4):
        for j in range(4):
            if map[i][j] == num:
                return i,j
    return -1,-1

def find_empty():
    i = j = up = down = left = right = -1
    i,j = find_num(0)
    if i > 0:
        up = map[i-1][j]
    if i < 3:
        down = map[i+1][j]
    if j > 0:
        left = map[i][j-1]
    if j < 3:
        right = map[i][j+1]
    return i,j,up,down,left,right

def move(dir):
    i,j,up,down,left,right = find_empty()
    if dir == 'up'and i != 0:
        map[i][j] = map[i-1][j]
        map[i-1][j] = 0
    elif dir == 'down'and i != 3:
        map[i][j] = map[i+1][j]
        map[i+1][j] = 0
    elif dir == 'left'and j != 0:
        map[i][j] = map[i][j-1]
        map[i][j-1] = 0
    elif dir == 'right'and j != 3:
        map[i][j] = map[i][j+1]
        map[i][j+1] = 0
    else:
        print('error direction')

def print_map():
    for i in range(4):
        print("%02d,%02d,%02d,%02d"%(map[i][0],map[i][1],map[i][2],map[i][3]))

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
        else:
            dir = "right"
        move(dir)
        print("----------------")
        print_map()
              
if __name__ == '__main__':
    print(find_empty())
    print_map()
    print("=================")
    move('up')
    move('left')
    move('left') # double left move
    move('right')
    move('down')
    print_map()
    print("=================")
    start()
    
