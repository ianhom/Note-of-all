#!/usr/bin/python
import datetime
import requests
import json

r = requests.get('http://www.weather.com.cn/data/sk/101070201.html')
r.encoding='utf-8'
print(r.json())

y=datetime.datetime.now().year
m=datetime.datetime.now().month
d=datetime.datetime.now().day

def get_last_day(year, month):
    return (datetime.datetime(year,month+1,1) - datetime.datetime(year,month,1)).days

vol_total = int(input("The object is :"));
cur_total = int(input("The current is :"));
days = get_last_day(y,m)
vol = int(vol_total) / days
left = vol * ( days - d)
haveto = (vol_total - cur_total) / (days - d)

if __name__ == '__main__':
    print("The object distance of this month is %d km"%(vol_total))
    print("The days of this month is %d"%(days))
    print("The daily distance is %d km"%(vol))
    print("The current distance should be %dkm"%(vol*d))
    print("The left vol should be %d km"%(left))
    print("The left days is %d"%(days - d))
    print("You have to run %d km every day"%(haveto))

