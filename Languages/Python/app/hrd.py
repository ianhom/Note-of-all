#!/usr/bin/python
map = [[1,2,3,4],
       [5,6,7,8],
       [9,10,11,12],
       [13,14,15,0]]

def find_num(num):
    for i in range(4):
        for j in range(4):
            if map[i][j] == num:
                return i,j
    return -1,-1

def find_empty():
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
    i,j = find_empty()
    if dir == 'up':
        map[i][j] = map[i-1][j]
        map[i-1][j] = 0
    else if dir == 'down':
        map[i][j] = map[i+1][j]
        map[i+1][j] = 0
    else if dir == 'left':
        map[i][j] = map[i][j-1]
        map[i][j-1] = 0
    else if dir == 'right':
        map[i][j] = map[i][j+1]
        map[i][j+1] = 0
    else:
        print('error direction')

def print_map():
    for i in range(4):
        print(map[i])

if __name__ == '__main__':
    print(find_empty())
    print_map()
    move('up')
    move('left')
    move('left') # double left move
    move('right')
    move('down')
    print_map()
