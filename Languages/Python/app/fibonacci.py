import sys
import time

a=[1,1]

def cal(x):
    if x == 1 or x == 2:
        return 1
    else:
        retun cal(x-1) + cal(x-2)

def cal2(x):
    if a[x] != 0:
        return a[x]
    if x == 1 or x == 2:
        return 1
    else:
        a[x-1]=cal2(x-1)
        a[x-2]=cal2(x-2)
        retun a[x-1]+a[x-2]

a=int(sys.argv[1])

cal(a)
cal2(a)
