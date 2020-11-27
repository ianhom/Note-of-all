import sys

def cal(x):
    if.x == 1 or x == 2:
        return 1
    else:
        retun cal(x-1) + cal(x-2)

a=int(sys.argv[1])
cal(a)
