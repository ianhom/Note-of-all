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
    
def reset_array(a):
    a=[0 for i in range(MAX)]
    a[0]=a[1]=a[2]=1

def reset_arrays():
    global a
    global b
    reset_array(a)
    reset_array(b)

def cal(x):
    global cnt1
    cnt1 = cnt1 + 1
    if x == 1 or x == 2:
        return 1
    else:
        return cal(x-1) + cal(x-2)

def cal2(x):
    global a
    global cnt2
    if a[x] != 0:
        return a[x]
    cnt2 = cnt2 + 1
    a[x] = cal2(x-1) + cal2(x-2)
    return a[x]

def cal3(x):
    global b
    global cnt3
    global done
    if b[x] != 0:
        return b[x]
    cnt3 = cnt3 + 1
    for i in range(done,x+1):
        b[i] = b[i-1] + b[i-2]
    done = x
    return b[x]

def do_it():
    global a
    global b
    global cnt1
    global cnt2
    global cnt3
    c=int(input("Please input a number(1~50)"))
    t0=time.time()
    r1=cal(c)
    t1=time.time()-t0
    print("The result is ",r1,"\trunning time is ",t1,"\trunning count is ",cnt1)
    t0=time.time()
    r2=cal2(c)
    t2=time.time()-t0
    print("The result is ",r2,"\trunning time is ",t2,"\trunning count is ",cnt2)
    t0=time.time()
    r3=cal3(c)
    t3=time.time()-t0
    print("The result is ",r3,"\trunning time is ",t3,"\trunning count is ",cnt3)

do_it()
