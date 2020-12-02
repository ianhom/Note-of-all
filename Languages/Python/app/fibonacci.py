import sys
import time

a=[1,1,1]

def cal(x):
    if x == 1 or x == 2:
        return 1
    else:
        retun cal(x-1) + cal(x-2)

def cal2(x):
    global a
    if a[x] != 0:
        return a[x]
    a[x-1]=cal2(x-1)
    a[x-2]=cal2(x-2)
    retun a[x-1]+a[x-2]

c=int(sys.argv[1])

cal(c)
cal2(c)
