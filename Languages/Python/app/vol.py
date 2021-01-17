#!/usr/bin/python
import sys
import datetime
y=datetime.datetime.now().year
m=datetime.datetime.now().month
d=datetime.datetime.now().day

def get_last_day(year, month):
    flag = False
    if year%4 == 0 and year%100 != 0:
        flag = True
    if year%400 == 0:
        flag = True
    if month in [1,3,5,7,8,10,12]:
        return 31
    if month in [4,6,9,11]:
        return 30
    if month == 2 and flag == True:
        return 29
    if month == 2 and flag == False:
        return 28

vol_total = int(input("The object is :"));
#vol_total = sys.argv[1]
vol = int(vol_total) / get_last_day(y,m)

if __name__ == '__main__':
    print(vol)
