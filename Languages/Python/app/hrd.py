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

if __name__ == '__main__':
    move('up')
    move('left')
    move('left') # double left move
    move('right')
    move('down')
    print(find_empty())
