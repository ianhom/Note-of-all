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

def cal3(x):
    global a
    if x == 1 or x == 2:
        return 1
    for i in range(3,x-1):
        a[x] = a[x-1] + a[x-2]
    return a[x]

c=int(sys.argv[1])
t0=time.time()
cal(c)
t1=time.time()-t0
cal2(c)
t2=time.time()-t1
cal3(c)
t3=time.time()-t2
