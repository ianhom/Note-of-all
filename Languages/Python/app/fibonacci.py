import sys
import time

MAX = 1000000
done = 3
cnt1 = 0
cnt2 = 0
cnt3 = 0

a=[0 for i in range(MAX)]
a[0]=a[1]=a[2]=1
b=[0 for i in range(MAX)]
b[0]=b[1]=b[2]=1

def cal(x):
    global cnt1
    cnt1 = cnt1 + 1
    if x == 1 or x == 2:
        return 1
    else:
        retun cal(x-1) + cal(x-2)

def cal2(x):
    global a
    global cnt2
    if a[x] != 0:
        return a[x]
    cnt2 = cnt2 + 1
    a[x]=cal2(x-1)+cal2(x-2)
    retun a[x]

def cal3(x):
    global b
    global cnt3
    if b[x] != 0:
        return b[x]
    cnt3 = cnt3 + 1
    done = x
    for i in range(done,x-1):
        b[x] = b[x-1] + b[x-2]
    return b[x]

c=int(sys.argv[1])
t0=time.time()
cal(c)
t1=time.time()-t0
cal2(c)
t2=time.time()-t1
cal3(c)
t3=time.time()-t2
print(t1,cnt1)
print(t2,cnt2)
print(t3,cnt3)
