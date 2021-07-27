#!/usr/bin/python
import datetime
import random
import json
import time

SHOES = [
{"name": "AlphyFly Next%", "used km": 139, "race": "True", "SFD": "False", "LSD": "False", "rainy day": "False", "walk": "False"}, 
{"name": "VaporFly Next%", "used km": 179, "race": "True", "SFD": "False", "LSD": "False", "rainy day": "False", "walk": "False"}, 
{"name": "Tempo Next%", "used km": 125, "race": "True", "SFD": "True", "LSD": "False", "rainy day": "False", "walk": "False"}, 
{"name": "Fly3", "used km": 298, "race": "True", "SFD": "True", "LSD": "False", "rainy day": "False", "walk": "True"}, 
{"name": "160x", "used km": 690, "race": "False", "SFD": "True", "LSD": "True", "rainy day": "True", "walk": "True"}, 
{"name": "Feiying PB", "used km": 92, "race": "True", "SFD": "True", "LSD": "False", "rainy day": "False", "walk": "False"}, 
{"name": "Jueying essential", "used km": 41, "race": "False", "SFD": "False", "LSD": "True", "rainy day": "False", "walk": "False"}, 
{"name": "Jingtan", "used km": 80, "race": "False", "SFD": "True", "LSD": "True", "rainy day": "False", "walk": "False"}, 
{"name": "Takumi", "used km": 27, "race": "False", "SFD": "True", "LSD": "False", "rainy day": "False", "walk": "True"}, 
{"name": "Zhanshen", "used km": 33, "race": "False", "SFD": "False", "LSD": "True", "rainy day": "True", "walk": "True"}, 
{"name": "K26", "used km": 735, "race": "False", "SFD": "False", "LSD": "True", "rainy day": "False", "walk": "True"}, 
{"name": "K21", "used km": 553, "race": "False", "SFD": "False", "LSD": "True", "rainy day": "True", "walk": "True"}, 
{"name": "Ultraboost 18", "used km": 433, "race": "False", "SFD": "False", "LSD": "True", "rainy day": "False", "walk": "True"}, 
{"name": "Feiran", "used km": 163, "race": "Fasle", "SFD": "True", "LSD": "False", "rainy day": "False", "walk": "True"}, 
{"name": "Jifeng", "used km": 34, "race": "Fasle", "SFD": "False", "LSD": "True", "rainy day": "False", "walk": "True"}, 
{"name": "160x 2.0", "used km": 126, "race": "True", "SFD": "True", "LSD": "True", "rainy day": "False", "walk": "False"}, 
{"name": "160x Pro", "used km": 182, "race": "True", "SFD": "True", "LSD": "False", "rainy day": "False", "walk": "False"},
{"name": "Fengxing 10", "used km": 12, "race": "False", "SFD": "False", "LSD": "True", "rainy day": "False", "walk": "True"},
{"name": "Speedstar", "used km": 20, "race": "False", "SFD": "True", "LSD": "True", "rainy day": "False", "walk": "False"},
{"name": "Adizero prime x", "used km": 22, "race": "False", "SFD": "True", "LSD": "False", "rainy day": "False", "walk": "False"},
{"name": "Metaspeed sky", "used km": 0, "race": "True", "SFD": "True", "LSD": "False", "rainy day": "False", "walk": "False"},
{"name": "C202GT", "used km": 0, "race": "False", "SFD": "True", "LSD": "True", "rainy day": "False", "walk": "False"},
{"name": "Biaosu", "used km": 17, "race": "False", "SFD": "True", "LSD": "True", "rainy day": "False", "walk": "False"},
{"name": "Altra 4.0", "used km": 0, "race": "False", "SFD": "False", "LSD": "True", "rainy day": "True", "walk": "True"},
{"name": "New one", "used km": 0, "race": "False", "SFD": "False", "LSD": "False", "rainy day": "False", "walk": "False"}]


new_shoe = { "name" : "xxx", "used km" : 0, "race" : "False", "SFD" : "False",  "LSD" : "False", "rainy day" : "False", "walk" : "False"}

NULL = 0

def init():
    with open("./shoes.json","r") as shoes_f:
        return json.load(shoes_f)

def update_box(s):
    with open("./shoes.json","w") as shoes_f:
        json.dump(s, shoes_f)

y=datetime.datetime.now().year
m=datetime.datetime.now().month
d=datetime.datetime.now().day

def by_used_km():
    return rslt(shoes, "used km")

def by_race():
    return flt(shoes, "race")

def by_rainy():
    return flt(shoes, "rainy day")

def by_walk():
    return flt(shoes, "walk")

def by_lsd():
    return flt(shoes, "LSD")

def for_lsd():
    return rslt(by_lsd(),"used km")

def by_sfd():
    return flt(shoes, "SFD")

def by_rainy_lsd():
    return flt(by_rainy(), "LSD")

def rslt(lis,a):
    return sorted(lis, key = lambda i: (i[a]))

def flt(lis,k):
    return filter(lambda x:x[k] == "True", lis)

def rnd(lst):
    return lst[int(random.random()*100%len(lst))]

def find_by_name(lis,name):
    for i in lis:
        if i["name"] == name:
            return i
    print("Wrong name")
    return NULL

def update_km(lis,name,km):
    i = find_by_name(lis,name)
    if i != NULL:
        i["used km"] = int(km)
        return True
    return False

def increase_km(lis,name,plus):
    i = find_by_name(lis,name)
    if i != NULL:
        i["used km"] = i["used km"] + int(plus)
        return True
    return False

def add_shoe(dict):
    shoes.append(dict)
   
def prt(lis):
    for i in lis:
         print(i)
    pirnt("------------------")

def output(lst):
    for i in lst:
         print(i["name"],"\t\t\t",i["used km"])

def pickone(lst):
     l=rnd(lst)
     return l

def check_right(d1,d2,k):
    return d1[k] == d2[k]

def find_same(d1,d2):
    return (check_right(d1,d2,"race") and
            check_right(d1,d2,"SFD") and
            check_right(d1,d2,"LSD") and
            check_right(d1,d2,"rainy day") and
            check_right(d1,d2,"walk"))

def check_same(b):
    flag = [1] * len(b)
    for i in range(0,len(b)):
         c = []
         if flag[i] == 0:
             continue
         c.append(b[i])
         for j in range(i+1,len(b)):
             if find_same(b[i],b[j]):
                  c.append(b[j])
                  flag[j] = 0
         output(c)
         print("----------")

def back_up():
    tm = time.strftime("%Y%m%d%H%M%S", time.localtime())
    print(tm)

def print_help():
    print("Please input the valid command:")
    print("----list     : Print all shoes")
    print("----help     : Print this help info")
    print("----lsd      : Filter LSD shoes")
    print("----sfd      : Filter SFD shoes")
    print("----km       : Filter by used km")
    print("----rainy    : Filter by rainy day")
    print("----race     : Filter race shoes")
    print("----format   : Format shoes list") 
    print("----update   : Update used km")
    print("----increase : Increase used km")
    print("----same     : Find the same usage shoes")
    print("----backup   : Backup shoes.json")
    print()

def yn_value(dic,key):
    k = input(key,"? y/n")
    if k == "y":
        dic[key] = "True"
    else:
        dic[key] = "False"   

if __name__=="__main__":
    try:
        shoes = init()
    except:
        print("Inside data")
        shoes = SHOES #Use shoes list in this file
    while True:
        cmd = input("Please input a command: ")
        if cmd == "lsd":
            output(for_lsd())
            print(pickone(for_lsd()))
        elif cmd == "km":
            output(by_used_km())
        elif cmd == "list":
            output(shoes)
        elif cmd == "rainy":
            output(by_rainy())
        elif cmd == "race":
            output(by_race())
        elif cmd == "sfd":
            output(by_sfd())
        elif cmd == "format":
            update_box(SHOES)
        elif cmd == "update" or cmd == "increase":
            output(shoes)
            name = input("which one?")
            if find_by_name(shoes, name) == NULL:
                continue
            km = input("how long?")
            if cmd == "update":
                ret = update_km(shoes,name,km)
            else:
                ret = increase_km(shoes,name,km)
            if True == ret:
                update_box(shoes)
                output(shoes)
        elif cmd == "same":
            check_same(shoes)
        elif cmd == "add":
            name = input("Shoe name")
            if find_by_name(shoes, name) != NULL:
                print("Already exist")
                continue
            new_shoe["name"] = name
            km = input("How long used")
            new_shoe["used km"] = int(km)
            yn_value(new_shoe,"race")
            yn_value(new_shoe,"LSD")
            yn_value(new_shoe,"SFD")
            yn_value(new_shoe,"walk")
            yn_value(new_shoe,"rainy")
            add_shoe(new_shoe)
        elif cmd == "backup":
            back_up()
        else:
            print_help()


 
